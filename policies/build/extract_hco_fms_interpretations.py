# -*- coding: utf-8 -*-
"""Extract 1:1 Guidebook Interpretation paragraphs for HCO FMS OEs.

Pairs Interpretation: blocks in document order with the 43 portal-PDF OEs.
Applies the MOM-hardened OCR pipe fix (token-start |n → In only; never a
global |n→In replace). Next-OE body text and next-standard titles are used
as the cut so page-break continuations stay with the previous OE.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OCR = ROOT / "policies/source/hco6_fms_guidebook_ocr.txt"
INV = ROOT / "policies/source/hco6_fms_inventory.json"
OUT = ROOT / "policies/source/hco6_fms_interpretations.json"

STANDARD_CUT = re.compile(r"(?is)\n\s*Standard\s*(?:\n|\s+FMS)")
HEADER_LINE = re.compile(
    r"(?i)^(Guidebook to|NABH|NABR|NAB’|sjdebook|uidebook|joke Aon|dean NAG|Guebook).*$"
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


def _cut_next_oe(note: str, next_oe_text: str) -> str:
    """Cut next-OE restatement using alphanumeric match (survives OCR punct)."""
    nxt = re.sub(r"[^a-z0-9]+", "", next_oe_text.lower())[:48]
    if len(nxt) < 20:
        return note
    alnum: list[str] = []
    idx_map: list[int] = []
    for i, ch in enumerate(note):
        if ch.isalnum():
            alnum.append(ch.lower())
            idx_map.append(i)
    s = "".join(alnum)
    pos = s.find(nxt)
    if pos >= 0 and idx_map[pos] >= 80:
        return note[: idx_map[pos]].rstrip()
    return note


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
        note = _cut_next_oe(note, next_oe_text)
    m = re.search(r"(?i)\bFMS\.\s*\d+", note)
    if m and m.start() >= 80:
        rest = note[m.start() :]
        if len(rest) > 40:
            note = note[: m.start()]
    m = re.search(r"(?i)(?:^|[. ]\s*)Objective Elements\s*$", note)
    if m and m.start() >= 80:
        note = note[: m.start()]
    note = CHROME.sub(" ", note)
    note = re.sub(
        r"(?i)\b(?:CORE|CQRE|C@RE|Commitment|Achievement|Excellence|Achlevement)\s+[a-l]\.\s+",
        "",
        note,
    )
    note = re.sub(
        r"(?i)\s*(?:=+\s*)?(?:\b(?:HER|HE|HR|HBB|Hi|ml|yl|el|Ss|Tl)\s+)*"
        r"\b(?:commitment|achievement|achlevement|exceitence|excettence)\b"
        r"(?:\s+\b(?:commitment|achievement|achlevement|her|he|hr|hbb|hi|exceitence|excettence)\b){1,6}",
        " ",
        note,
    )
    repairs = {
        "Atleast": "At least",
        "theorganisation": "the organisation",
        "Theorganisation": "The organisation",
        "Referto the": "Refer to the",
        "Even it a": "Even if a",
        "Patientfalls": "Patient falls",
        "ang management": "and management",
        "ang efficiency": "and efficiency",
        "notin use": "not in use",
        "budget/expenditure": "budget / expenditure",
        "form ofa": "form of a",
        "informed i consent": "informed consent",
        "\\t implies": "It implies",
        "\t implies": "It implies",
        "t implies that": "It implies that",
        "has 4 service": "has a service",
        "intégrity": "integrity",
        "day-to- day": "day-to-day",
        "il CORE ty ® Leaders": "Leaders",
        "il CORE ty Leaders": "Leaders",
        "il CORE ty.": "",
        "il CORE ty": "",
        "ensure ~ continuity": "ensure continuity",
        "Documented i z i Excellence -~_ e. f. operational": "Documented operational",
        "committee.For": "committee. For",
        "values- The": "values. The",
        "and operational plan”.": "and “operational plan”.",
        "plan”. Be =i.": "plan”.",
        "z z “a _ b. d, TM core * ": "",
        "z z \"a _ b. d, TM core * ": "",
        "ed Excellence \" g ].": "",
        "zi) Excellence.": "",
        "— C@RE al a Excellence a.": "",
        "® dl y na Yr ) f.": "",
        "=].": "",
        "a).": ".",
    }
    for a, b in repairs.items():
        note = note.replace(a, b)
    note = re.sub(r"\s+", " ", note).strip(" .*=-_")
    note = re.sub(
        r"(?i)\s*(?:Achievement|Commitment|Excellence|CORE|CQRE|C@RE|Hy core|z _)\s*[a-l]?\s*\.?\s*$",
        "",
        note,
    )
    note = re.sub(
        r"(?i)\s*(?:HB|HM|TB|GM|He|Zi\s*=i|_b|_f|—h|al EE i|z\s*_f|z\s*zs\s*lie)"
        r"(?:\s+(?:cone|core|HM|TB|Excetience|Excellence|G|B)){0,6}\s*[.\s®°—_=-]*$",
        "",
        note,
    )
    note = re.sub(r"(?i)\s+(?:HB|HM)\s+cone\b.*$", "", note)
    note = re.sub(r"(?i)\s+(?:[—_-]?\s*[a-l]\.)+\s*$", "", note)
    note = re.sub(
        r"(?i)\s+(?:z\s*_f\.?|i\]\.?|C G d\.?|Zi\s*=i.*|i—.*|Ta zi.*|_ f\..*|— g G.*)\s*$",
        "",
        note,
    )
    note = re.sub(r"\s+[._\-–—='`®°]+\s*$", "", note)
    note = re.sub(r"(?i)Documented\s+.{0,80}?operational plans", "Documented operational plans", note)
    note = re.sub(r"(?i)\s*z\s*z\s*.{0,50}TM core\s*\*?\s*", " ", note)
    note = re.sub(r"^\s*t implies", "It implies", note)
    note = re.sub(r"(?i)\s*il\s+CORE\s+ty\.?\s*$", "", note)
    note = note.replace("ensure ~ continuity", "ensure continuity")
    note = re.sub(r"\s+", " ", note).strip(" .*=-_")
    if note and note[-1] not in ".;:":
        note += "."
    return note


def extract(ocr_text: str, oes: list[dict], titles: list[str] | None = None) -> dict[str, str]:
    body = clean_pipe_ocr(ocr_text)
    body = re.sub(r"\n===== PDF_IDX \d+ \(pdf page \d+\) =====\n", "\n", body)
    start = body.find("Interpretation:")
    if start < 0:
        raise SystemExit("no Interpretation: marker found")
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
        if titles and i + 1 < len(titles):
            nxt_title = titles[i + 1]
            if nxt_title and nxt_title != (titles[i] if i < len(titles) else ""):
                chunk = _cut_next_oe(chunk, nxt_title)
        chunk = re.sub(r"(?i)\s+(?:[—_-]?\s*[a-l]\.)+\s*$", "", chunk).strip(" .")
        chunk = re.sub(r"^IIt implies", "It implies", chunk)
        chunk = re.sub(r"(?i)\s*(?:Achievement\s+)?ed Excellence.*$", "", chunk)
        chunk = re.sub(r"(?i)\s*zi\)?\s*Excellence\.?$", "", chunk)
        chunk = re.sub(r"(?i)\s*—?\s*C@RE.*$", "", chunk)
        chunk = re.sub(r"(?i)\s*Be\s+Commitment.*$", "", chunk)
        chunk = re.sub(r"(?i)\s*Commitment\s*®.*$", "", chunk)
        chunk = re.sub(r"(?i)\s*a\)\s*Achievement\.?$", "", chunk)
        chunk = re.sub(r"\s*=\]\.?\s*$", "", chunk)
        chunk = re.sub(r"(?i)\s*il\s+CORE\s+ty\.?\s*$", "", chunk)
        chunk = chunk.replace("ensure ~ continuity", "ensure continuity")
        chunk = chunk.strip(" .")
        if chunk and chunk[-1] not in ".;:":
            chunk += "."
        if not chunk or len(chunk) < 20:
            raise SystemExit(f"empty/short interpretation for {oe['oe_code']}: {chunk!r}")
        out[oe["oe_code"]] = chunk
    return out


def apply_source_strips(interps: dict[str, str]) -> dict[str, str]:
    """Write proposed OCR strips/reconstructions into the source-of-truth dict.

    Chrome leftovers and page-break cuts are applied here so drafts never
    carry flagged-but-unwritten fragments. Official OE wording is not changed.
    """
    word_fixes = [
        ("Ata minimum", "At a minimum"),
        ("Ata mi", "At a mi"),
        ("anq documented", "and documented"),
        ("ang microbiological", "and microbiological"),
        ("The_organisation", "The organisation"),
        ("case itis", "case it is"),
        ("prescribeq", "prescribed"),
        ("lodged,and", "lodged, and"),
        ("identified,and", "identified, and"),
        ("implemented,and", "implemented, and"),
        ("Medical equipmentis", "Medical equipment is"),
        ("equipmentin", "equipment in"),
        ("Equipmentis", "Equipment is"),
        ("tillthe", "till the"),
        ("or.become", "or become"),
        (" oF ", " or "),
        ("once in ayear", "once in a year"),
        ("once in\nayear", "once in a year"),
        ("case offire", "case of fire"),
        ("fallor slips", "fall or slips"),
        ("Inthe case", "In the case"),
        ("otherwaste", "other waste"),
        ("air- conditioners", "air-conditioners"),
        ("short- circuiting", "short-circuiting"),
        ("Theorganisation", "The organisation"),
        ("Indian Seismic Code S: 1893", "Indian Seismic Code IS: 1893"),
        ("¢ display", "* display"),
    ]
    chrome_tail = [
        r"(?i)\s+z\s*Commitment\s*[—-].*$",
        r"(?i)\s+Commitment\s+a\s+Excellence\.?$",
        r"(?i)\s+HE\s+cone.*$",
        r"(?i)\s+i\s+Achievement\s+Tt\s+Excellence\.?$",
        r"(?i)\s+ti\s+Commitment.*Excellence.*$",
        r"(?i)\s+Achievement\s+h,\.?$",
        r"(?i)\s+HEE\s+Commitment.*Excetience.*$",
        r"(?i)\s+=i\s+rr.*Accreditation Stan.*$",
        r"(?i)\s+Excellence\.?$",
        r"(?i)\s+il\s+CORE\s+ty\.?$",
    ]
    reconstructions = {
        "FMS.2.c": (
            "Manner implies language and/or pictorial signs. Signage could be bilingual "
            "and shall meet statutory requirements."
        ),
        "FMS.2.f": None,  # filled after word-fixes: Refer to FMS.2.d
        "FMS.4.a": (
            "This shall also take into consideration future requirements like DG sets, "
            "Chiller plant. The plans shall be fully implemented, and there shall be a "
            "process for periodic review of plans. Equipment is selected, rented, updated "
            "or upgraded by a collaborative process. Collaborative process implies that "
            "during equipment selection, there is involvement of end-user, management, "
            "finance and engineering departments."
        ),
        "FMS.5.f": (
            "The organisation shall plan for this keeping in mind the strategic plans, "
            "upgrade/update path and the equipment log. The organisation shall condemn "
            "(dispose of) equipment in a systematic manner."
        ),
    }
    out: dict[str, str] = {}
    for k, v in interps.items():
        if k in reconstructions and reconstructions[k]:
            out[k] = reconstructions[k]
            continue
        for a, b in word_fixes:
            v = v.replace(a, b)
        for pat in chrome_tail:
            v = re.sub(pat, "", v)
        v = v.replace("ensure ~ continuity", "ensure continuity")
        v = re.sub(r"\s+", " ", v).strip(" .")
        if v and v[-1] not in ".;:":
            v += "."
        if k == "FMS.2.f":
            v = re.sub(r"Refer to\.?$", "Refer to FMS.2.d.", v)
            if "Refer to FMS.2.d" not in v:
                v = v.rstrip(".") + " Refer to FMS.2.d."
        out[k] = v
    return out


def main() -> int:
    inv = json.loads(INV.read_text(encoding="utf-8"))
    oes = [o for n in sorted(inv, key=int) for o in inv[n]["oes"]]
    titles = [inv[n]["title"] for n in sorted(inv, key=int) for _ in inv[n]["oes"]]
    ocr = OCR.read_text(encoding="utf-8")
    interps = apply_source_strips(extract(ocr, oes, titles))
    joined = "\n".join(interps.values())
    for bad in ("oIn", "wheIn", "takeIn", "informatioIn", "|n", "il CORE ty", "ensure ~ continuity"):
        if bad in joined:
            raise SystemExit(f"pipe-OCR / chrome leak: {bad!r}")
    OUT.write_text(json.dumps(interps, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(interps)} interpretations → {OUT}")
    for oe in oes:
        k = oe["oe_code"]
        print(f"{k} ({len(interps[k])}c): {interps[k][:140]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
