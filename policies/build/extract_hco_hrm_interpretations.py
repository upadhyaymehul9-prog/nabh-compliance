# -*- coding: utf-8 -*-
"""Extract 1:1 Guidebook Interpretation paragraphs for HCO HRM OEs.

Source text (policies/source/hco6_hrm_guidebook_ocr.txt) is a verified manual
transcription (no tesseract/pdftoppm binary available on this machine; PyMuPDF
was used only to rasterize pages for visual reading), not a mechanical OCR
pass — so unlike the FMS/ROM extractors this file does not need pipe-OCR or
ligature-drop cleanup. It still trims "Refer to X.Y" trailers are KEPT (they
are genuine Guidebook cross-references, useful as method notes) and strips
only the page-furniture noise (blank lines, standard-header echoes).

Pairs "Interpretation:" blocks in document order with the 76 portal-PDF OEs.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OCR = ROOT / "policies/source/hco6_hrm_guidebook_ocr.txt"
INV = ROOT / "policies/source/hco6_hrm_inventory.json"
OUT = ROOT / "policies/source/hco6_hrm_interpretations.json"

STANDARD_CUT = re.compile(r"(?is)\n\s*Standard\s*\n")
# Same-standard OE-to-OE transitions: the raw block between one "Interpretation:"
# and the next literal token also contains the following OE's own
# "LEVEL letter. requirement text" header line (there is no "Standard" line
# between two OEs of the same standard, so STANDARD_CUT alone does not catch
# this). Cut there too.
NEXT_OE_CUT = re.compile(r"(?is)\n\s*(?:CORE|Commitment|Achievement|Excellence)\s+[a-l]\.\s")


def tidy(note: str) -> str:
    lines = [ln.strip() for ln in note.splitlines() if ln.strip()]
    note = " ".join(lines)
    note = re.sub(r"\s+", " ", note).strip()
    if note and note[-1] not in ".;:":
        note += "."
    return note


def extract(ocr_text: str, oes: list[dict]) -> dict[str, str]:
    body = re.sub(r"\n===== PDF_IDX \d+ \(pdf page \d+\) =====\n", "\n", ocr_text)
    start = body.find("Interpretation:")
    if start < 0:
        raise SystemExit("no Interpretation: marker found")
    region = body[start:]
    # The PDF_IDX marker before "References" was already stripped above; cut
    # defensively at the literal "References" heading that remains at the end.
    ref = re.search(r"\nReferences\s*\n?\s*$", region)
    if ref:
        region = region[: ref.start()]
    raw_blocks = re.split(r"(?i)\n?Interpretation\s*:\s*", region)
    blocks = [b for b in raw_blocks[1:] if b.strip()]
    if len(blocks) != len(oes):
        raise SystemExit(f"Interpretation count {len(blocks)} != OE count {len(oes)}")
    out: dict[str, str] = {}
    for oe, raw in zip(oes, blocks):
        chunk = STANDARD_CUT.split(raw)[0]
        chunk = NEXT_OE_CUT.split(chunk)[0]
        chunk = tidy(chunk)
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
    for bad in ("oIn", "wheIn", "takeIn", "informatioIn", "|n", "il CORE ty", "ensure ~ continuity"):
        if bad in joined:
            raise SystemExit(f"pipe-OCR / chrome leak: {bad!r}")
    OUT.write_text(json.dumps(interps, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(interps)} interpretations -> {OUT}")
    for oe in oes:
        k = oe["oe_code"]
        print(f"{k} ({len(interps[k])}c): {interps[k][:140]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
