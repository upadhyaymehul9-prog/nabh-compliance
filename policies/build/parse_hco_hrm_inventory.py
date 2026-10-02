# -*- coding: utf-8 -*-
"""Parse official portal HRM chapter OCR into inventory JSON.

Authoritative source: policies/source/hco6_hrm_ocr.txt (pdftotext -enc UTF-8
of portal Standards PDF pages 161-176 / printed 150-165). Does not use the
Guidebook for counts/levels/stars.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OCR = ROOT / "policies/source/hco6_hrm_ocr.txt"
OUT = ROOT / "policies/source/hco6_hrm_inventory.json"

LIGATURE_MAP = str.maketrans({chr(0xF001): "fi", chr(0xF002): "fl", chr(0xFB01): "fi", chr(0xFB02): "fl"})
LETTER_RE = re.compile(
    r"^\s*(CORE|Commitment|Achievement|Excellence)\s+([a-lA-L])\.\s+(.*)$"
)
STD_RE = re.compile(r"^\s*HRM\.(\d+)\.\s*(.*)$")
FOOTER_RE = re.compile(
    r"^(?:CORE|Commitment|Achievement|Excellence|\d+|®)$"
    r"|^(?:CORE\s+Commitment\s+Achievement\s+Excellence)$",
    re.I,
)


def clean(s: str) -> str:
    s = s.translate(LIGATURE_MAP)
    s = s.replace(chr(0x00A0), " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse() -> dict:
    text = OCR.read_text(encoding="utf-8")
    idx = text.find("Standards and Objective Elements")
    if idx < 0:
        raise SystemExit("body heading not found")
    body = text[idx:]
    ref = re.search(r"^References\s*$", body, re.M)
    if ref:
        body = body[: ref.start()]

    inv: dict[str, dict] = {}
    current: dict | None = None
    pending_title_lines: list[str] = []
    in_title = False
    pending_oe: dict | None = None
    # HRM's "Standard" header is not always alone on its own line — title text
    # can trail it inline ("Standard      Staff are provided induction ...")
    # or trail the HRM.N. code instead ("HRM.2.        The organisation ...").
    # A trigger keyed on the word "Standard" (not requiring it to be the only
    # thing on the line) survives both layouts; verified no false positives
    # (13 chapter-body "Standard" line-starts for 13 standards).
    STANDARD_TRIGGER = re.compile(r"^\s*Standard\b\s*(.*)$")

    def flush_oe() -> None:
        nonlocal pending_oe
        if not pending_oe or current is None:
            pending_oe = None
            return
        raw = clean(pending_oe["raw"])
        star = raw.endswith("*")
        if star:
            raw = raw[:-1].strip()
        pending_oe["text"] = raw
        pending_oe["star"] = star
        del pending_oe["raw"]
        current["oes"].append(pending_oe)
        pending_oe = None

    def flush_title() -> None:
        nonlocal in_title, pending_title_lines
        if current is not None and pending_title_lines:
            current["title"] = clean(" ".join(pending_title_lines))
        pending_title_lines = []
        in_title = False

    def is_footer(stripped: str) -> bool:
        return bool(FOOTER_RE.match(stripped)) or "NABH Accreditation" in stripped or stripped.startswith("®")

    for line in body.splitlines():
        stripped = line.strip()
        mtrig = STANDARD_TRIGGER.match(line)
        if mtrig:
            flush_oe()
            pending_title_lines = []
            in_title = True
            carry = (mtrig.group(1) or "").strip()
            if carry and not is_footer(carry):
                pending_title_lines.append(carry)
            continue
        mstd = STD_RE.match(line)
        if mstd and (in_title or stripped.startswith("HRM.")):
            flush_oe()
            n = mstd.group(1)
            rest = (mstd.group(2) or "").strip()
            current = {
                "standard_code": f"HRM.{n}",
                "title": "",
                "oes": [],
                "count": 0,
            }
            inv[n] = current
            in_title = True
            if rest and not is_footer(rest):
                pending_title_lines.append(rest)
            continue
        if in_title:
            if re.match(r"^\s*Objective Elements\s*$", line):
                flush_title()
                continue
            if LETTER_RE.match(line):
                continue
            if stripped and not is_footer(stripped) and not stripped.startswith("HRM."):
                pending_title_lines.append(stripped)
            continue
        if re.match(r"^\s*Objective Elements\s*$", line):
            flush_title()
            continue
        m = LETTER_RE.match(line)
        if m and current is not None:
            flush_oe()
            letter = m.group(2).lower()
            pending_oe = {
                "oe_code": f"{current['standard_code']}.{letter}",
                "letter": letter,
                "level": m.group(1),
                "star": False,
                "raw": m.group(3),
            }
            continue
        if pending_oe is not None:
            if not stripped:
                continue
            if is_footer(stripped):
                continue
            pending_oe["raw"] += " " + stripped

    flush_oe()
    flush_title()
    for n, data in inv.items():
        data["count"] = len(data["oes"])
    return inv


def main() -> int:
    inv = parse()
    total = sum(d["count"] for d in inv.values())
    cores = sum(1 for d in inv.values() for o in d["oes"] if o["level"] == "CORE")
    comm = sum(1 for d in inv.values() for o in d["oes"] if o["level"] == "Commitment")
    ach = sum(1 for d in inv.values() for o in d["oes"] if o["level"] == "Achievement")
    exc = sum(1 for d in inv.values() for o in d["oes"] if o["level"] == "Excellence")
    stars = [o["oe_code"] for d in inv.values() for o in d["oes"] if o["star"]]
    print("standards", sorted(inv, key=int))
    for n in sorted(inv, key=int):
        d = inv[n]
        letters = "".join(o["letter"] for o in d["oes"])
        print(f"HRM.{n}: {d['count']} [{letters}] {d['title']}")
        for o in d["oes"]:
            star = "*" if o["star"] else " "
            print(f"  {o['letter']}{star} {o['level']:12} {o['text']}")
    print(f"TOTAL {total} CORE {cores} Comm {comm} Ach {ach} Exc {exc}")
    print("asterisks", stars)
    assert len(inv) == 13, inv.keys()
    assert total == 76, total
    assert cores == 16 and comm == 56 and ach == 4 and exc == 0, (cores, comm, ach, exc)
    OUT.write_text(json.dumps(inv, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
