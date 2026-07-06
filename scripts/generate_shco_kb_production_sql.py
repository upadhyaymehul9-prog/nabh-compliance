#!/usr/bin/env python3
"""Generate SQL compatible with the LIVE shco_kb schema (category/section/fts)."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KNOWLEDGE = json.loads((ROOT / "shco_book_knowledge.json").read_text())
OUT = ROOT / "shco_kb_production.sql"


def esc(value: str) -> str:
    return value.replace("'", "''")


def main() -> None:
    lines = [
        "-- SHCO book-only knowledge — production-safe (existing shco_kb schema)",
        "-- Source: NABH SHCO 3rd Edition via scripts/extract_shco_book.py",
        "",
        "alter table public.shco_full_oes",
        "  add column if not exists doc_required boolean,",
        "  add column if not exists interpretation text,",
        "  add column if not exists book_page_ref int,",
        "  add column if not exists assessment_stages text;",
        "",
        "-- Remove prior book KB rows (preserves unrelated categories)",
        "delete from public.shco_kb",
        "where source_label like 'SHCO Full —%'",
        "  and category in ('chapter_intent', 'chapter_summary', 'general', 'committees');",
        "",
    ]

    for entry in KNOWLEDGE["kb_entries"]:
        category = esc(entry["kb_type"])
        if entry.get("section"):
            section = esc(entry["section"])
        elif entry.get("chapter"):
            section = esc(entry["chapter"])
        else:
            section = esc(entry["title"])
        lines.append(
            "insert into public.shco_kb (category, section, title, content, source_label) values "
            f"('{category}', '{section}', '{esc(entry['title'])}', "
            f"'{esc(entry['content'])}', '{esc(entry['source_label'])}');"
        )

    lines.extend(["", "-- Mandatory documentation flags (*)"])
    for code, starred in sorted(KNOWLEDGE["mandatory_flags"].items()):
        val = "true" if starred else "false"
        lines.append(
            f"update public.shco_full_oes set doc_required = {val} where oe_code = '{esc(code)}';"
        )

    lines.extend(["", "-- Assessment stages by OE level (book pp.12–16)"])
    for code, stages in sorted(KNOWLEDGE.get("assessment_stages", {}).items()):
        lines.append(
            f"update public.shco_full_oes set assessment_stages = '{esc(stages)}' "
            f"where oe_code = '{esc(code)}';"
        )

    lines.extend(
        [
            "",
            "select category, count(*) from public.shco_kb group by category order by category;",
            "select count(*) filter (where doc_required) as starred, count(*) as total from public.shco_full_oes;",
        ]
    )

    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
