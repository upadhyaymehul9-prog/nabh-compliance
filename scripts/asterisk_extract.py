#!/usr/bin/env python3
"""Extract the asterisk (documented-evidence) flag for every OE in the official
NABH SHCO 3rd Edition PDF, and compare it against `shco_full_oes.doc_required`.

The asterisk marks the OE that anchors a standard's documented evidence, so a
wrong flag under-builds the one place an assessor is most likely to ask for a
document. It is NOT safe to infer the flag from an OE's position or level.

Each OE is read as a full block -- opening line plus every wrapped continuation
line -- because the asterisk frequently lands on a wrapped second or third line
(HIC.6.e, AAC.2.d, COP.8.f, COP.10.f, COP.13.c, IMS.2.b, IMS.4.e).

Run:
    python scripts/asterisk_extract.py [--pdf PATH] [--sql]

Writes scripts/shco_oe_asterisks.json. With --sql, also writes
scripts/shco_oe_asterisks_compare.sql -- run that against Supabase to list
every OE whose doc_required disagrees with the PDF, in both directions.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pdfplumber

HERE = Path(__file__).resolve().parent

# The official 3rd Edition standards PDF. This file is not in the repo -- it is
# the book itself. Override with --pdf if it lives elsewhere on your machine.
# (The path in extract_shco_book.py is a stale /home/ubuntu one from an earlier
# environment and does not resolve here; do not copy it.)
DEFAULT_PDF = Path(r"C:/Users/SERVER/Desktop/NABH/SHCO-Standards-3rd-Edition.pdf")

OUT_JSON = HERE / "shco_oe_asterisks.json"
OUT_SQL = HERE / "shco_oe_asterisks_compare.sql"
# Independent OE list used to validate the parse (code set + level agreement).
REF_OES = HERE / "shco_oes_data.json"

EXPECTED_OE_COUNT = 408

CHAPTERS = ["AAC", "COP", "MOM", "PRE", "HIC", "PSQ", "ROM", "FMS", "HRM", "IMS"]
CH_RE = "|".join(CHAPTERS)

# A standard header line. The book is inconsistent about these and all three
# forms occur: "HIC.6." alone on its own line, "MOM.3. <standard text>", and
# "COP 1. <standard text>" -- a space instead of a dot after the chapter code.
# Matching only the first form silently drops the whole COP chapter.
STD_RE = re.compile(rf"^({CH_RE})[\s.](\d+)\.(\s|$)")

# An OE opening line: "<level> <letter>. <text>".
OE_RE = re.compile(r"^(CORE|C RE|Commitment|Achievement|Excellence)\s+([a-z])\.\s*(.*)$")

# Page footer, e.g. "C RE Commitment 96 Achievement Excellence". Skipped rather
# than treated as a break, so an OE can continue across a page turn.
FOOTER_RE = re.compile(r"^C\s*RE\s+Commitment\s+\d+\s+Achievement\s+Excellence\s*$")

# Each chapter ends with a References list and the book ends with a glossary.
# Without this cutoff the chapter's final OE swallows all of it, and any
# asterisk in that text becomes a false positive (this wrongly flagged AAC.8.g
# and IMS.6.e on the first pass of the 2026-08-10 audit).
REFERENCES_RE = re.compile(r"^(References|REFERENCES|Glossary|GLOSSARY)\b")

SKIP_LINES = {
    "NABH Accreditation Standards for Small Healthcare Organizations",
    "3rd Edition, August 2022",
    "R",
}

# "Standard" opens a new standard block; ending the current OE there keeps the
# standard's own prose out of the preceding OE.
BREAK_LINES = {"Standard", "Objective Elements", "STANDARDS AND OBJECTIVE ELEMENTS"}

# The detailed standards section starts here. Everything before it is the TOC,
# chapter intents and the 2nd/3rd edition comparison tables, which repeat OE
# codes in a different layout and must not be parsed.
FIRST_DETAIL_PAGE = 55

# In a few places the level label is laid out on its own line, either just
# before the line carrying the OE letter (COP.6.e) or just after it (IMS.2.b,
# IMS.6.b). Stitch those back together before parsing.
LEVEL_ONLY_RE = re.compile(r"^(CORE|C RE|Commitment|Achievement|Excellence)$")
BARE_OE_RE = re.compile(r"^[a-z]\.\s+\S")

# Ligature glyphs used by this PDF's embedded font.
LIGATURES = {"\uf001": "fi", "\uf002": "fl", "\ufb01": "fi", "\ufb02": "fl"}


def normalize(text: str) -> str:
    for glyph, repl in LIGATURES.items():
        text = text.replace(glyph, repl)
    return text


def merge_split_levels(lines: list[str]) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(lines):
        m = LEVEL_ONLY_RE.match(lines[i])
        if m:
            if i + 1 < len(lines) and BARE_OE_RE.match(lines[i + 1]):
                out.append(f"{m.group(1)} {lines[i + 1]}")
                i += 2
                continue
            if out and BARE_OE_RE.match(out[-1]):
                out[-1] = f"{m.group(1)} {out[-1]}"
                i += 1
                continue
        out.append(lines[i])
        i += 1
    return out


def parse(pdf_path: Path) -> list[dict]:
    records: list[dict] = []
    with pdfplumber.open(pdf_path) as pdf:
        cur_std: str | None = None
        cur_oe: dict | None = None

        def flush() -> None:
            nonlocal cur_oe
            if cur_oe is None:
                return
            body = " ".join(cur_oe.pop("lines")).strip()
            cur_oe["raw"] = body
            cur_oe["text"] = re.sub(r"\s+", " ", body.replace("*", "").strip())
            # The flag is the presence of an asterisk anywhere in the OE's own
            # block, not just on its first line.
            cur_oe["asterisk"] = "*" in body
            records.append(cur_oe)
            cur_oe = None

        for pageno, page in enumerate(pdf.pages):
            if pageno < FIRST_DETAIL_PAGE:
                continue
            lines = merge_split_levels(
                [normalize(l).strip() for l in (page.extract_text() or "").split("\n")]
            )
            for line in lines:
                if line in BREAK_LINES or REFERENCES_RE.match(line):
                    flush()
                    continue
                if not line or line in SKIP_LINES or FOOTER_RE.match(line):
                    continue
                m_std = STD_RE.match(line)
                if m_std:
                    flush()
                    cur_std = f"{m_std.group(1)}.{m_std.group(2)}"
                    continue
                m_oe = OE_RE.match(line)
                if m_oe and cur_std:
                    flush()
                    cur_oe = {
                        "oe_code": f"{cur_std}.{m_oe.group(2)}",
                        "level": "Core"
                        if m_oe.group(1) in ("CORE", "C RE")
                        else m_oe.group(1),
                        "page_pdf_index": pageno,
                        "lines": [m_oe.group(3)],
                    }
                    continue
                if cur_oe is not None:
                    cur_oe["lines"].append(line)
        flush()
    return records


def validate(records: list[dict]) -> list[str]:
    """Checks that catch a mis-parse before its output is trusted."""
    problems: list[str] = []

    codes = [r["oe_code"] for r in records]
    if len(codes) != len(set(codes)):
        dupes = sorted({c for c in codes if codes.count(c) > 1})
        problems.append(f"duplicate OE codes parsed: {dupes}")
    if len(records) != EXPECTED_OE_COUNT:
        problems.append(f"parsed {len(records)} OEs, expected {EXPECTED_OE_COUNT}")

    if REF_OES.exists():
        ref = json.loads(REF_OES.read_text(encoding="utf-8"))
        ref_levels = {r["oe_code"]: r["level"] for r in ref}
        got = set(codes)
        missing = sorted(set(ref_levels) - got)
        extra = sorted(got - set(ref_levels))
        if missing:
            problems.append(f"OEs in {REF_OES.name} but not parsed: {missing}")
        if extra:
            problems.append(f"OEs parsed but not in {REF_OES.name}: {extra}")
        # Levels sit on the same lines as the asterisks, so agreement here is
        # direct evidence that the OE block boundaries are right.
        bad = [
            f"{r['oe_code']} parsed={r['level']} ref={ref_levels[r['oe_code']]}"
            for r in records
            if r["oe_code"] in ref_levels and ref_levels[r["oe_code"]] != r["level"]
        ]
        if bad:
            problems.append(f"level disagreements ({len(bad)}): {bad[:10]}")
    else:
        problems.append(f"{REF_OES.name} not found - skipped cross-validation")

    # A block that ran away has swallowed a References list or a later standard.
    runaway = [r["oe_code"] for r in records if len(r["raw"]) > 600]
    if runaway:
        problems.append(f"suspiciously long OE blocks: {runaway}")

    return problems


def compare_sql(records: list[dict]) -> str:
    vals = ",".join(
        f"('{r['oe_code']}',{str(r['asterisk']).lower()})" for r in records
    )
    return (
        "-- Every OE whose shco_full_oes.doc_required disagrees with the\n"
        "-- asterisk in the official SHCO 3rd Edition PDF, in both directions.\n"
        "-- Generated by scripts/asterisk_extract.py --sql\n"
        f"with pdf(oe_code, pdf_asterisk) as (values {vals})\n"
        "select p.oe_code, d.level, d.doc_required as db_doc_required, p.pdf_asterisk,\n"
        "  case when p.pdf_asterisk then 'DB MISSING asterisk'\n"
        "       else 'DB has EXTRA asterisk' end as direction\n"
        "from pdf p full join public.shco_full_oes d using (oe_code)\n"
        "where d.doc_required is distinct from p.pdf_asterisk\n"
        "order by split_part(p.oe_code,'.',1),\n"
        "         (split_part(p.oe_code,'.',2))::int,\n"
        "         split_part(p.oe_code,'.',3);\n"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf", type=Path, default=DEFAULT_PDF, help="path to the SHCO 3rd Edition PDF")
    ap.add_argument("--sql", action="store_true", help="also write the comparison SQL")
    args = ap.parse_args()

    if not args.pdf.exists():
        print(f"PDF not found: {args.pdf}\nPass --pdf with the correct path.", file=sys.stderr)
        return 2

    records = parse(args.pdf)
    problems = validate(records)

    OUT_JSON.write_text(
        json.dumps({"pdf": str(args.pdf), "oes": records}, indent=1, ensure_ascii=False),
        encoding="utf-8",
    )

    asterisked = [r for r in records if r["asterisk"]]
    print(f"parsed {len(records)} OEs, {len(asterisked)} asterisked -> {OUT_JSON.name}")
    print(f"{'Ch':<5}{'OEs':>5}{'asterisks':>11}")
    for ch in CHAPTERS:
        total = sum(1 for r in records if r["oe_code"].startswith(ch + "."))
        ast = sum(1 for r in asterisked if r["oe_code"].startswith(ch + "."))
        print(f"{ch:<5}{total:>5}{ast:>11}")

    if args.sql:
        OUT_SQL.write_text(compare_sql(records), encoding="utf-8")
        print(f"comparison SQL -> {OUT_SQL.name}")

    if problems:
        print("\nVALIDATION FAILED - do not trust this output:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1

    print("\nvalidation OK (count, code set, levels, block lengths)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
