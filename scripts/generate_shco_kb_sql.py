#!/usr/bin/env python3
"""Generate Supabase SQL from scripts/shco_book_knowledge.json."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KNOWLEDGE = json.loads((ROOT / "shco_book_knowledge.json").read_text())


def esc(value: str) -> str:
    return value.replace("'", "''")


def main() -> None:
    lines: list[str] = [
        "-- SHCO book-only knowledge seed",
        "-- Source: NABH SHCO 3rd Edition (August 2022) — extracted via scripts/extract_shco_book.py",
        "-- Run in Supabase SQL Editor AFTER 20260706_shco_kb_schema.sql migration",
        "",
        "-- 1. Clear prior book KB rows (safe re-run)",
        "delete from public.shco_kb where source_label like 'SHCO Full —%';",
        "",
        "-- 2. Chapter intents, summaries, and general reference",
    ]

    for entry in KNOWLEDGE["kb_entries"]:
        chapter = f"'{esc(entry['chapter'])}'" if entry.get("chapter") else "null"
        page = str(entry["book_page"]) if entry.get("book_page") else "null"
        lines.append(
            "insert into public.shco_kb (kb_type, chapter, title, content, source_label, book_page) values "
            f"('{esc(entry['kb_type'])}', {chapter}, '{esc(entry['title'])}', "
            f"'{esc(entry['content'])}', '{esc(entry['source_label'])}', {page});"
        )

    lines.extend(
        [
            "",
            "-- 3. Mandatory documentation flags (*) from the standards book",
            "alter table public.shco_full_oes add column if not exists doc_required boolean;",
            "alter table public.shco_full_oes add column if not exists book_page_ref int;",
            "",
        ]
    )

    for code, starred in sorted(KNOWLEDGE["mandatory_flags"].items()):
        val = "true" if starred else "false"
        lines.append(
            f"update public.shco_full_oes set doc_required = {val} where oe_code = '{esc(code)}';"
        )

    missing = KNOWLEDGE["stats"].get("oes_missing_flag", 0)
    lines.extend(
        [
            "",
            f"-- Note: {missing} OEs could not be matched to PDF asterisk marks automatically.",
            "-- Re-run scripts/extract_shco_book.py after PDF parser improvements.",
            "",
            "-- 4. Verify",
            "select kb_type, count(*) from public.shco_kb group by kb_type order by kb_type;",
            "select count(*) filter (where doc_required) as starred, count(*) as total from public.shco_full_oes;",
        ]
    )

    out = ROOT / "shco_kb_seed.sql"
    out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {out} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
