# -*- coding: utf-8 -*-
"""Extract 1:1 Guidebook Interpretation paragraphs for HCO PRE OEs.

Pairs Interpretation: blocks in document order with the 52 portal-PDF OEs.
Applies the MOM-hardened OCR pipe fix (token-start |n → In only; never a
global |n→In replace). Leftover column-rule pipes are stripped after
targeted repairs (detai| → detail; SPIKES '| for invitation' → 'I for').
Next-OE body text is used as the cut (not a bare 'Standard' or letter
heading), so page-break continuations stay with the previous OE.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OCR = ROOT / "policies/source/hco6_pre_guidebook_ocr.txt"
INV = ROOT / "policies/source/hco6_pre_inventory.json"
OUT = ROOT / "policies/source/hco6_pre_interpretations.json"

STANDARD_CUT = re.compile(r"(?is)\n\s*Standard\s*(?:\n|\s+PRE)")
HEADER_LINE = re.compile(
    r"(?i)^(Guidebook to|NABH|NABR|NAB’|sjdebook|uidebook|joke Aon|dean NAG).*$"
)
CHROME = re.compile(
    r"(?i)(?:"
    r"[Gu]?idebook to NABH Accreditation Standards for Hospitals|"
    r"Gdebook to NABH Accreditation Standards for Hospitals|"
    r"\b(?:CORE|CQRE|C@RE|C@QRE|SO@RE|CQ@RE)\b(?:\s+\b(?:HER|HBB|cone)\b)?"
    r"(?:\s+\b(?:Commitment|Achievement|Excellence|Achlevement)\b){1,3}|"
    r"(?:=+\s*)+\b(?:CORE|CQRE|C@RE|Commitment|Achievement|Excellence)\b"
    r")"
)


def clean_pipe_ocr(text: str) -> str:
    """MOM-hardened pipe fix. Do not globally replace |n with In."""
    text = re.sub(r"(^|[\n. ])\|n\b", r"\1In", text)
    text = re.sub(r"detai\|", "detail", text, flags=re.I)
    text = re.sub(r",\s*\|\s*for invitation", ", I for invitation", text)
    text = text.replace("|", "")
    return text


def tidy(note: str, next_oe_text: str | None = None) -> str:
    lines = []
    for ln in note.splitlines():
        s = ln.strip()
        if not s:
            continue
        if HEADER_LINE.match(s):
            continue
        if re.fullmatch(r"[=_\-\sQ)dj;'`]+", s):
            continue
        lines.append(s)
    note = " ".join(lines)
    note = STANDARD_CUT.split(note)[0]
    if next_oe_text:
        def _norm(s: str) -> str:
            s = s.lower()
            s = re.sub(r"\s*/\s*", "/", s)
            s = re.sub(r"\s+", " ", s)
            return s
        needle = _norm(next_oe_text).rstrip(".*")[:64]
        nnote = _norm(note)
        idx = nnote.find(needle)
        if idx > 40:
            raw_needle = re.sub(r"\s+", " ", next_oe_text).strip()[:40]
            ridx = note.lower().find(raw_needle.lower())
            if ridx < 0:
                raw_needle2 = re.sub(r"\s*/\s*", "/", re.sub(r"\s+", " ", next_oe_text)).strip()[:40]
                ridx = note.lower().find(raw_needle2.lower())
            if ridx > 40 and ridx >= 80:
                note = note[:ridx]
    note = CHROME.sub(" ", note)
    note = re.sub(
        r"(?i)\b(?:CORE|CQRE|C@RE|Commitment|Achievement|Excellence|Achlevement)\s+[a-l]\.\s+",
        "",
        note,
    )
    note = re.sub(
        r"(?i)\s*(?:=+\s*)?(?:\b(?:HER|HE|HR|HBB|Hi|ml|yl|el|Ss|Tl)\s+)*"
        r"\b(?:commitment|achievement|excellence|achlevement|exceitence|excettence)\b"
        r"(?:\s+\b(?:commitment|achievement|excellence|achlevement|her|he|hr|hbb|hi|exceitence|excettence)\b){0,6}",
        " ",
        note,
    )
    repairs = {
        "dong effectively": "done effectively",
        "compiaints": "complaints",
        "ofinformation": "of information",
        "recommendedas": "recommended as",
        "Atleast": "At least",
        "theorganisation": "the organisation",
        "Patientand": "Patient and",
        "Therelevanttarifflistis": "The relevant tariff list is",
        "Thepatientand/or": "The patient and/or",
        "and_possible": "and possible",
        "written consentis": "written consent is",
        "signature ona": "signature on a",
        "Ifit is": "If it is",
        "information ona": "information on a",
        "detai the": "detail the",
        "Informed consentis": "Informed consent is",
        "Adoctor": "A doctor",
        "!t shall": "It shall",
        "deposit,are": "deposit, are",
        "i of independent": "of independent",
        "Commitment cc.": "",
        "Commitment hh.": "",
        "Achievement .": "",
        "CQRE Ci": "",
        "CQRE ": "",
        "C@RE e.": "",
        "C@RE ": "",
        "Hi  ": " ",
    }
    for a, b in repairs.items():
        note = note.replace(a, b)
    note = re.sub(r"\s+", " ", note).strip(" .*=-_")
    note = re.sub(
        r"(?i)\s*(?:Achievement|Commitment|Excellence|CORE|CQRE|C@RE|Hy core|z _)\s*[a-l]?\s*\.?\s*$",
        "",
        note,
    )
    note = re.sub(r"\s+", " ", note).strip(" .*=-_")
    if note and note[-1] not in ".;:":
        note += "."
    return note


def extract(ocr_text: str, oes: list[dict]) -> dict[str, str]:
    body = clean_pipe_ocr(ocr_text)
    body = re.sub(r"\n===== PDF_IDX \d+ \(pdf page \d+\) =====\n", "\n", body)
    start = body.find("Interpretation: Organisation shall document")
    if start < 0:
        start = body.find("Interpretation:")
    region = body[start:]
    ref = re.search(r"\nReferences\b", region)
    if ref:
        region = region[: ref.start()]
    raw_blocks = re.split(r"(?i)\n?Interpretation\s*:\s*", region)
    blocks = [b for b in raw_blocks[1:] if b.strip()]
    if len(blocks) != len(oes):
        raise SystemExit(f"Interpretation count {len(blocks)} != OE count {len(oes)}")
    out: dict[str, str] = {}
    for i, (oe, raw) in enumerate(zip(oes, blocks)):
        next_text = oes[i + 1]["text"] if i + 1 < len(oes) else None
        chunk = STANDARD_CUT.split(raw)[0]
        chunk = tidy(chunk, next_text)
        if not chunk or len(chunk) < 20:
            raise SystemExit(f"empty/short interpretation for {oe['oe_code']}: {chunk!r}")
        out[oe["oe_code"]] = chunk
    return out


def main() -> int:
    inv = json.loads(INV.read_text(encoding="utf-8"))
    oes = [o for n in sorted(inv, key=int) for o in inv[n]["oes"]]
    ocr = OCR.read_text(encoding="utf-8")
    interps = extract(ocr, oes)
    joined = "\n".join(interps.values())
    for bad in ("oIn", "wheIn", "takeIn", "informatioIn", "|n"):
        if bad in joined:
            raise SystemExit(f"pipe-OCR corruption leaked: {bad!r}")
    OUT.write_text(json.dumps(interps, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(interps)} interpretations → {OUT}")
    for oe in oes:
        k = oe["oe_code"]
        print(f"{k} ({len(interps[k])}c): {interps[k][:120]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
