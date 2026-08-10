#!/usr/bin/env python3
"""Extract structured video content from AAC LinkedIn posters via Tesseract OCR."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

POSTERS = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "oes_content.json"

# AAC.1–13 letter spans (HCO 6th Edition)
LETTERS = {
    1: "abcd",
    2: "abcde",
    3: "abcd",
    4: "abcdefg",
    5: "abcde",
    6: "abcdefghij",
    7: "abcdefg",
    8: "abcdefghi",
    9: "abcdefghijk",
    10: "abcdefgh",
    11: "abcde",
    12: "abcdefg",
    13: "abcde",
}


def oe_code(std: int, letter: str) -> str:
    return f"AAC.{std}.{letter}"


def poster_path(std: int, letter: str) -> Path:
    return POSTERS / f"AAC-{std}{letter}.png"


def ocr(path: Path) -> str:
    r = subprocess.run(
        ["tesseract", str(path), "stdout", "--psm", "6"],
        capture_output=True,
        text=True,
        check=False,
    )
    return r.stdout or ""


def clean_line(s: str) -> str:
    s = s.strip()
    s = s.replace("|", " ").replace("»", " ").replace("©", " ")
    s = re.sub(r"\s+", " ", s)
    return s.strip(" -•●○@")


def extract(std: int, letter: str, text: str) -> dict:
    code = oe_code(std, letter)
    short = f"AAC {std}{letter}"
    lines = [clean_line(l) for l in text.splitlines()]
    lines = [l for l in lines if l and len(l) > 1]

    # Headline: collect question-ish lines after code header
    headline_parts = []
    started = False
    for l in lines:
        if re.search(rf"AAC\s*{std}\s*{letter}", l, re.I) or re.search(
            rf"AAC\s*{std}{letter}", l, re.I
        ):
            started = True
            continue
        if not started:
            if "NABH" in l.upper():
                continue
            continue
        if re.match(r"^(\d+[\.\)]|SIMPLE|COMMON|What |AccredReady|#)", l, re.I):
            break
        if l.startswith("@") or l.upper().startswith("WE DON'T"):
            break
        # skip tiny OCR junk
        if len(l) < 8:
            continue
        if l.upper() in {"NABH STANDARD", "SERVICE COVER", "DEPARTMENT SCOPE"}:
            continue
        headline_parts.append(l)
        if "?" in l or len(" ".join(headline_parts)) > 90:
            break
        if len(headline_parts) >= 4:
            break
    headline = " ".join(headline_parts)
    headline = re.sub(r"\s+", " ", headline).strip()
    if len(headline) < 12:
        headline = f"Understanding {code}"

    # Requirement-like bullets
    reqs = []
    for l in lines:
        if l.startswith("@") or l.startswith("●") or l.startswith("•"):
            t = clean_line(l)
            if len(t) > 20:
                reqs.append(t)
        # also lines that look like OE statements
    # fallback: long lines containing key verbs
    if len(reqs) < 2:
        for l in lines:
            low = l.lower()
            if any(
                k in low
                for k in (
                    "shall",
                    "should",
                    "defined",
                    "documented",
                    "written guidance",
                    "organisation",
                    "organization",
                    "provide",
                    "implement",
                )
            ) and 40 < len(l) < 220:
                if l not in reqs and "AccredReady" not in l:
                    reqs.append(l)
            if len(reqs) >= 3:
                break
    reqs = reqs[:3]
    while len(reqs) < 3:
        reqs.append(f"Meet the documented requirements for {code}.")

    # Gaps — look for numbered titles / ALL CAPS short headers
    gaps = []
    for l in lines:
        m = re.match(r"^(?:\(?(\d+)\)?[\.\):]?\s+)?([A-Z][A-Z0-9 /,'-]{6,60})$", l)
        if m:
            title = m.group(2).strip(" -")
            if title in {"NABH STANDARD", "SIMPLE FIRST STEP", "COMMON GAPS HOSPITALS MISS"}:
                continue
            if "ACCREDREADY" in title:
                continue
            gaps.append(title.title() if title.isupper() else title)
        # patterns like "1. SPECIALTY ON PAPER ONLY"
        m2 = re.match(r"^(\d+)\.\s+([A-Z].{5,60})$", l)
        if m2:
            gaps.append(m2.group(2).strip())
    # dedupe preserve order
    seen = set()
    gaps2 = []
    for g in gaps:
        k = g.lower()
        if k not in seen and len(g) > 5:
            seen.add(k)
            gaps2.append(g[:48])
    gaps = gaps2[:4]
    defaults_gaps = [
        "Policy exists but practice differs",
        "Staff cannot explain the process",
        "Records are incomplete or late",
        "No monitoring or corrective action",
    ]
    while len(gaps) < 4:
        gaps.append(defaults_gaps[len(gaps)])

    # First steps
    steps = []
    join = "\n".join(lines)
    idx = join.upper().find("SIMPLE")
    chunk = join[idx : idx + 600] if idx >= 0 else ""
    for m in re.finditer(
        r"(?:^|\n|\s)(?:\(?([123])\)?[\.\)]\s*|@\s*)([A-Z][^@\n]{20,140})",
        chunk,
        re.M,
    ):
        steps.append(clean_line(m.group(2)))
    if len(steps) < 3:
        # generic actionable steps from headline theme
        steps = [
            f"Review current practice against {code} with the process owner.",
            "Document the gap list and assign named owners with due dates.",
            "Brief frontline teams this week and verify with a spot check.",
        ]
    steps = steps[:3]

    oe_text = reqs[0]
    # Prefer a sentence that looks like formal OE wording
    for r in reqs:
        if len(r) > 50 and any(
            w in r.lower() for w in ("shall", "should", "is defined", "are defined", "written")
        ):
            oe_text = r
            break

    return {
        "code": code,
        "short": short,
        "file_stem": f"AAC-{std}{letter}",
        "headline": headline[:160],
        "oe_text": oe_text[:280],
        "requirements": [
            {"title": f"Requirement {i+1}", "body": r[:140]} for i, r in enumerate(reqs[:3])
        ],
        "gaps": [{"title": g[:40], "body": "A frequent field gap against this OE."} for g in gaps[:4]],
        "steps": steps[:3],
    }


def main():
    items = []
    for std, letters in LETTERS.items():
        for letter in letters:
            path = poster_path(std, letter)
            if not path.exists():
                print("MISSING", path)
                continue
            print("OCR", path.name)
            text = ocr(path)
            items.append(extract(std, letter, text))
    OUT.write_text(json.dumps(items, indent=2, ensure_ascii=False))
    print("wrote", OUT, "count", len(items))


if __name__ == "__main__":
    main()
