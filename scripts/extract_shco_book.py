#!/usr/bin/env python3
"""Extract book-only SHCO knowledge from the official 3rd Edition PDF.

Outputs scripts/shco_book_knowledge.json with:
- chapter intents and summary of standards (Tier 1 KB)
- mandatory documentation flags (*) per OE
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pdfplumber

PDF_PATH = Path(
    "/home/ubuntu/.cursor/projects/workspace/uploads/SHCO-Standards-3rd-Edition_d4f4.pdf"
)
OES_PATH = Path(__file__).resolve().parent / "shco_oes_data.json"
OUT_PATH = Path(__file__).resolve().parent / "shco_book_knowledge.json"

CHAPTERS = {
    "AAC": "Access, Assessment and Continuity of Care",
    "COP": "Care of Patients",
    "MOM": "Management of Medication",
    "PRE": "Patient Rights and Education",
    "HIC": "Hospital Infection Control",
    "PSQ": "Patient Safety and Quality Improvement",
    "ROM": "Responsibilities of Management",
    "FMS": "Facility Management and Safety",
    "HRM": "Human Resource Management",
    "IMS": "Information Management System",
}

CHAPTER_CODES = set(CHAPTERS)


def normalize(text: str) -> str:
    return (
        text.replace("\ufb01", "fi")
        .replace("\ufb02", "fl")
        .replace("\uf001", "fi")  # alternate PDF ligature encoding
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )


def clean_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_mandatory_flags(pages_text: str, oe_codes: set[str]) -> dict[str, bool]:
    lines = pages_text.split("\n")
    current_std: str | None = None
    mandatory: dict[str, bool] = {}
    level_re = re.compile(r"^(CORE|Commitment|Achievement|Excellence)\s+([a-z])\.\s*(.*)$", re.I)
    std_re = re.compile(r"^([A-Z]{3})\.?\s*(\d+)\.\s*(.*)$")

    for i, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line or line.startswith("C RE Commitment"):
            continue
        if line in ("Objective Elements", "Standard"):
            continue

        std_match = std_re.match(line)
        if std_match and std_match.group(1) in CHAPTER_CODES:
            current_std = f"{std_match.group(1)}.{std_match.group(2)}"
            continue

        level_match = level_re.match(line)
        if not (level_match and current_std):
            continue

        letter = level_match.group(2).lower()
        body = level_match.group(3)
        j = i + 1
        while j < len(lines):
            nxt = lines[j].strip()
            if not nxt or nxt.startswith("C RE Commitment"):
                j += 1
                continue
            if level_re.match(nxt):
                break
            std_next = std_re.match(nxt)
            if std_next and std_next.group(1) in CHAPTER_CODES:
                break
            if nxt in ("Objective Elements", "Standard", "References:"):
                break
            body += " " + nxt
            j += 1

        body = clean_ws(body)
        code = f"{current_std}.{letter}"
        if code in oe_codes:
            mandatory[code] = bool(re.search(r"\*\.?\s*$", body))

    return mandatory


def extract_chapters(pdf) -> dict:
    chapters_info: dict = {}
    for i in range(55, 138):
        t = normalize(pdf.pages[i].extract_text() or "")
        for ch, name in CHAPTERS.items():
            if f"({ch})" not in t[:300] or "Intent of the Chapter" not in t:
                continue
            intent_match = re.search(
                r"Intent of the Chapter:(.*?)\nSUMMARY OF STANDARDS", t, re.S
            )
            summary_match = re.search(r"SUMMARY OF STANDARDS\n(.*)", t, re.S)
            intent = clean_ws(intent_match.group(1)) if intent_match else ""
            std_lines: list[str] = []
            if summary_match:
                for line in summary_match.group(1).split("\n"):
                    line = line.strip()
                    if re.match(r"^\d+$", line):
                        break
                    if re.match(r"^[A-Z]{3}\.\d+\.", line):
                        std_lines.append(line)
            chapters_info[ch] = {
                "page": i + 1,
                "chapter_name": name,
                "intent": intent,
                "summary_standards": std_lines,
            }
    return chapters_info


def build_kb_entries(chapters_info: dict) -> list[dict]:
    entries: list[dict] = []
    for ch, info in chapters_info.items():
        entries.append(
            {
                "kb_type": "chapter_intent",
                "chapter": ch,
                "title": f"{ch} — Intent of the Chapter",
                "content": info["intent"],
                "source_label": (
                    f"SHCO Full — {ch} Chapter Intent (NABH 3rd Edition, p.{info['page']})"
                ),
                "book_page": info["page"],
            }
        )
        entries.append(
            {
                "kb_type": "chapter_summary",
                "chapter": ch,
                "title": f"{ch} — Summary of Standards",
                "content": "\n".join(info["summary_standards"]),
                "source_label": (
                    f"SHCO Full — {ch} Summary of Standards (NABH 3rd Edition, p.{info['page']})"
                ),
                "book_page": info["page"],
            }
        )
    return entries


def main() -> None:
    oes = json.loads(OES_PATH.read_text())
    oe_codes = {o["oe_code"] for o in oes}

    with pdfplumber.open(PDF_PATH) as pdf:
        pages_text = "\n".join(
            normalize(pdf.pages[i].extract_text() or "") for i in range(55, 137)
        )
        chapters_info = extract_chapters(pdf)
        page12 = normalize(pdf.pages[11].extract_text() or "")

    mandatory = extract_mandatory_flags(pages_text, oe_codes)
    kb_entries = build_kb_entries(chapters_info)

    interp = re.search(
        r"WHAT IS AN INTERPRETATION\?(.*?)(?:CORE STANDARD|LEVELS|$)", page12, re.S
    )
    if interp:
        kb_entries.append(
            {
                "kb_type": "general",
                "chapter": None,
                "title": "What is an Interpretation?",
                "content": clean_ws(interp.group(1)),
                "source_label": "SHCO Full — How to Read the Standard (NABH 3rd Edition, p.12)",
                "book_page": 12,
            }
        )

    out = {
        "mandatory_flags": mandatory,
        "kb_entries": kb_entries,
        "chapters_info": chapters_info,
        "stats": {
            "oes_with_mandatory_flag": len(mandatory),
            "oes_starred": sum(mandatory.values()),
            "oes_missing_flag": len(oe_codes - set(mandatory.keys())),
            "kb_entries": len(kb_entries),
        },
    }
    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(json.dumps(out["stats"], indent=2))


if __name__ == "__main__":
    main()
