# -*- coding: utf-8 -*-
"""Parse official portal ROM chapter OCR into inventory JSON.

Authoritative source: policies/source/hco6_rom_ocr.txt (pdftotext of portal
Standards PDF pages 143–150). Does not use the Guidebook for counts/levels/stars.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OCR = ROOT / "policies/source/hco6_rom_ocr.txt"
OUT = ROOT / "policies/source/hco6_rom_inventory.json"

LIGATURE_MAP = str.maketrans({"\uf001": "fi", "\uf002": "fl", "\ufb01": "fi", "\ufb02": "fl"})
LETTER_RE = re.compile(
    r"^\s+(CORE|Commitment|Achievement|Excellence)\s+([a-lA-L])\.\s+(.*)$"
)
STD_RE = re.compile(r"^\s+ROM\.(\d+)\.\s*(.*)$")
FOOTER_RE = re.compile(
    r"^(?:CORE|Commitment|Achievement|Excellence|\d+|®)$"
    r"|^(?:CORE\s+Commitment\s+Achievement\s+Excellence)$",
    re.I,
)


def clean(s: str) -> str:
    s = s.translate(LIGATURE_MAP)
    s = s.replace("\u00a0", " ")
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
        if re.match(r"^\s*Standard\s*$", line):
            flush_oe()
            pending_title_lines = []
            in_title = True
            continue
        mstd = STD_RE.match(line)
        if mstd and (in_title or stripped.startswith("ROM.")):
            flush_oe()
            n = mstd.group(1)
            rest = (mstd.group(2) or "").strip()
            current = {
                "standard_code": f"ROM.{n}",
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
            if stripped and not is_footer(stripped) and not stripped.startswith("ROM."):
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
            if stripped in {"Standard"}:
                flush_oe()
                pending_title_lines = []
                in_title = True
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
        print(f"ROM.{n}: {d['count']} [{letters}] {d['title']}")
        for o in d["oes"]:
            star = "*" if o["star"] else " "
            print(f"  {o['letter']}{star} {o['level']:12} {o['text']}")
    print(f"TOTAL {total} CORE {cores} Comm {comm} Ach {ach} Exc {exc}")
    print("asterisks", stars)
    assert len(inv) == 6, inv.keys()
    assert total == 37, total
    assert cores == 4 and comm == 23 and ach == 8 and exc == 2, (cores, comm, ach, exc)
    OUT.write_text(json.dumps(inv, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
