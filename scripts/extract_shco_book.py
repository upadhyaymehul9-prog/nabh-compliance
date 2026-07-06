#!/usr/bin/env python3
"""Extract book-only SHCO knowledge from the official 3rd Edition PDF."""

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
OE_PAGE_START = 55
OE_PAGE_END = 152  # includes full IMS chapter OE listings

ASSESSMENT_STAGES = {
    "Core": "Final, Surveillance, Re-accreditation",
    "Commitment": "Final, Surveillance, Re-accreditation",
    "Achievement": "Surveillance, Re-accreditation",
    "Excellence": "Re-accreditation",
}

COMMITTEE_MANDATES = [
    {
        "title": "Committees — Pharmacy & Therapeutics",
        "section": "Committees — Pharmacy & Therapeutics",
        "oe_codes": ["MOM.1.b", "MOM.1"],
        "book_page": 83,
    },
    {
        "title": "Committees — Infection Control",
        "section": "Committees — Infection Control",
        "oe_codes": ["HIC.1.c", "HIC.1"],
        "book_page": 100,
    },
    {
        "title": "Committees — Patient Safety",
        "section": "Committees — Patient Safety",
        "oe_codes": ["PSQ.1.a", "PSQ.1"],
        "book_page": 109,
    },
    {
        "title": "Committees — Quality Assurance / Quality Improvement",
        "section": "Committees — Quality Assurance",
        "oe_codes": ["PSQ.1.e", "PSQ.1"],
        "book_page": 109,
    },
    {
        "title": "Committees — Cardiopulmonary Resuscitation Review",
        "section": "Committees — CPR Review",
        "oe_codes": ["COP.3.d", "COP.3"],
        "book_page": 70,
    },
    {
        "title": "Committees — Committee Effectiveness Review",
        "section": "Committees — Governance",
        "oe_codes": ["ROM.3.c", "ROM.3"],
        "book_page": 117,
    },
]


def normalize(text: str) -> str:
    return (
        text.replace("\ufb01", "fi")
        .replace("\ufb02", "fl")
        .replace("\uf001", "fi")
        .replace("\u2013", "-")
        .replace("\u2014", "-")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )


def clean_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_mandatory_flags(pages_text: str, oe_by_code: dict[str, dict]) -> dict[str, bool]:
    lines = pages_text.split("\n")
    current_std: str | None = None
    pending_level: str | None = None
    mandatory: dict[str, bool] = {}
    level_re = re.compile(r"^(CORE|Commitment|Achievement|Excellence)\s+([a-z])\.\s*(.*)$", re.I)
    level_only_re = re.compile(r"^(CORE|Commitment|Achievement|Excellence)\s*$", re.I)
    letter_only_re = re.compile(r"^([a-z])\.\s*(.*)$", re.I)
    std_re = re.compile(r"^([A-Z]{3})\.?\s*(\d+)\.\s*(.*)$")

    def store(code: str, body: str) -> None:
        if code in oe_by_code:
            mandatory[code] = bool(re.search(r"\*\.?\s*$", clean_ws(body)))

    for i, raw_line in enumerate(lines):
        line = raw_line.strip()
        if not line or line.startswith("C RE Commitment"):
            continue
        if line in ("Objective Elements", "Standard"):
            continue

        std_match = std_re.match(line)
        if std_match and std_match.group(1) in CHAPTER_CODES:
            current_std = f"{std_match.group(1)}.{std_match.group(2)}"
            pending_level = None
            continue

        if level_only_re.match(line):
            pending_level = level_only_re.match(line).group(1).capitalize()
            if pending_level.lower() == "core":
                pending_level = "Core"
            continue

        if pending_level and current_std:
            letter_match = letter_only_re.match(line)
            if letter_match:
                letter = letter_match.group(1).lower()
                body = letter_match.group(2)
                j = i + 1
                while j < len(lines):
                    nxt = lines[j].strip()
                    if not nxt or nxt.startswith("C RE Commitment"):
                        j += 1
                        continue
                    if level_re.match(nxt) or level_only_re.match(nxt):
                        break
                    std_next = std_re.match(nxt)
                    if std_next and std_next.group(1) in CHAPTER_CODES:
                        break
                    if nxt in ("Objective Elements", "Standard", "References:"):
                        break
                    if letter_only_re.match(nxt) and pending_level:
                        break
                    body += " " + nxt
                    j += 1
                store(f"{current_std}.{letter}", body)
                pending_level = None
                continue

        level_match = level_re.match(line)
        if level_match and current_std:
            letter = level_match.group(2).lower()
            body = level_match.group(3)
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if not nxt or nxt.startswith("C RE Commitment"):
                    j += 1
                    continue
                if level_re.match(nxt) or level_only_re.match(nxt):
                    break
                std_next = std_re.match(nxt)
                if std_next and std_next.group(1) in CHAPTER_CODES:
                    break
                if nxt in ("Objective Elements", "Standard", "References:"):
                    break
                body += " " + nxt
                j += 1
            store(f"{current_std}.{letter}", body)

    # Second pass: match OE text snippets for any still missing
    for code, oe in oe_by_code.items():
        if code in mandatory:
            continue
        snippet = clean_ws(oe["text"])[:28]
        for line in lines:
            ls = clean_ws(line)
            if snippet[:20] in ls:
                mandatory[code] = bool(re.search(r"\*\.?\s*$", ls) or "*" in ls[-4:])
                break

    return mandatory


def extract_chapters(pdf) -> dict:
    chapters_info: dict = {}
    for i in range(OE_PAGE_START, OE_PAGE_END):
        t = normalize(pdf.pages[i].extract_text() or "")
        for ch in CHAPTERS:
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
                "chapter_name": CHAPTERS[ch],
                "intent": intent,
                "summary_standards": std_lines,
            }
    return chapters_info


def build_kb_entries(chapters_info: dict, oe_by_code: dict[str, dict]) -> list[dict]:
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

    for mandate in COMMITTEE_MANDATES:
        parts = []
        for code in mandate["oe_codes"]:
            oe = oe_by_code.get(code)
            if not oe:
                continue
            if code.count(".") == 1:
                parts.append(f"Standard {code}: {oe['standard_text']}")
            else:
                parts.append(
                    f"{code} ({oe['level']}): {oe['text']}"
                )
        content = "MANDATED by the SHCO 3rd Edition standards book. " + " ".join(parts)
        entries.append(
            {
                "kb_type": "committees",
                "chapter": None,
                "title": mandate["title"],
                "section": mandate["section"],
                "content": content,
                "source_label": (
                    f"SHCO Full — {mandate['title']} (NABH 3rd Edition, p.{mandate['book_page']})"
                ),
                "book_page": mandate["book_page"],
            }
        )

    entries.append(
        {
            "kb_type": "general",
            "chapter": None,
            "title": "OE assessment stages by level",
            "section": "Assessment stages",
            "content": (
                "Per the SHCO 3rd Edition book (pp.12–16): CORE OEs are mandatorily assessed at "
                "every assessment stage and must never score below 4. Commitment OEs form the basis "
                "for accreditation at Final Assessment (Core + Commitment scored). Achievement OEs "
                "are first assessed at Surveillance Assessment (14–18 months post-accreditation). "
                "Excellence OEs are assessed only at Re-accreditation Assessment. "
                "Final Assessment scores Core + Commitment. Surveillance adds Achievement. "
                "Re-accreditation scores all levels including Excellence."
            ),
            "source_label": "SHCO Full — Assessment Modes & OE Levels (NABH 3rd Edition, pp.12–16)",
            "book_page": 12,
        }
    )
    return entries


def main() -> None:
    oes = json.loads(OES_PATH.read_text())
    oe_by_code = {o["oe_code"]: o for o in oes}
    oe_codes = set(oe_by_code)

    with pdfplumber.open(PDF_PATH) as pdf:
        pages_text = "\n".join(
            normalize(pdf.pages[i].extract_text() or "")
            for i in range(OE_PAGE_START, OE_PAGE_END)
        )
        chapters_info = extract_chapters(pdf)
        page12 = normalize(pdf.pages[11].extract_text() or "")

    mandatory = extract_mandatory_flags(pages_text, oe_by_code)
    kb_entries = build_kb_entries(chapters_info, oe_by_code)

    interp = re.search(
        r"WHAT IS AN INTERPRETATION\?(.*?)(?:CORE STANDARD|LEVELS|$)", page12, re.S
    )
    if interp:
        kb_entries.append(
            {
                "kb_type": "general",
                "chapter": None,
                "title": "What is an Interpretation?",
                "section": "What is an Interpretation?",
                "content": clean_ws(interp.group(1)),
                "source_label": "SHCO Full — How to Read the Standard (NABH 3rd Edition, p.12)",
                "book_page": 12,
            }
        )

    assessment_stages = {
        code: ASSESSMENT_STAGES[oe["level"]]
        for code, oe in oe_by_code.items()
        if oe["level"] in ASSESSMENT_STAGES
    }

    out = {
        "mandatory_flags": mandatory,
        "kb_entries": kb_entries,
        "assessment_stages": assessment_stages,
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
