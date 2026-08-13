# -*- coding: utf-8 -*-
"""Patches evidence + responsible into a policy draft's oe_mapping, and emits the SQL.

Local-first: this writes the updated draft JSON and a SQL file. It does not touch Supabase.
Run the emitted SQL only after the diff has been reviewed and approved.

Usage:
    python policies/build/apply_oe_evidence.py hic1
    python policies/build/apply_oe_evidence.py hic2
"""
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_POLICIES = _HERE.parent
DRAFTS = _POLICIES / "drafts"
SQL_OUT = _POLICIES / "sql"

SOURCES = {
    "hic1": ("HIC.1", "hic1_oe_evidence", "HIC1_EVIDENCE"),
    "hic2": ("HIC.2", "hic2_oe_evidence", "HIC2_EVIDENCE"),
}


def sql_quote(value: str) -> str:
    """Single-quoted SQL literal with embedded quotes doubled."""
    return "'" + value.replace("'", "''") + "'"


def main(key: str) -> None:
    standard_code, module_name, attr = SOURCES[key]
    sys.path.insert(0, str(_HERE))
    evidence_map = getattr(__import__(module_name), attr)

    draft_path = DRAFTS / f"{key}_draft.json"
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    mapping = draft["oe_mapping"]

    # Every OE in the mapping must be covered, and nothing extra may be supplied.
    mapped = {m["oe_code"] for m in mapping}
    supplied = set(evidence_map)
    if mapped != supplied:
        raise SystemExit(
            f"OE code mismatch for {standard_code}:\n"
            f"  in oe_mapping but not authored: {sorted(mapped - supplied)}\n"
            f"  authored but not in oe_mapping: {sorted(supplied - mapped)}"
        )

    for m in mapping:
        evidence, responsible = evidence_map[m["oe_code"]]
        # Guard the record split the renderer performs: no empty records, no trailing ';'.
        records = [r.strip() for r in evidence.split(";")]
        if any(not r for r in records):
            raise SystemExit(f"{m['oe_code']}: evidence contains an empty record")
        m["evidence"] = evidence
        m["responsible"] = responsible

    draft_path.write_text(
        json.dumps(draft, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    # The update replaces oe_mapping only. Nothing else in the approved row is touched.
    payload = json.dumps(mapping, ensure_ascii=False)
    sql = (
        f"-- {standard_code}: add evidence + responsible to oe_mapping.\n"
        f"-- Replaces oe_mapping only; every other column of the approved row is untouched.\n"
        f"update public.shco_policy_masters\n"
        f"   set oe_mapping = {sql_quote(payload)}::jsonb\n"
        f" where standard_code = {sql_quote(standard_code)};\n"
    )
    sql_path = SQL_OUT / f"{key}_oe_evidence_update.sql"
    sql_path.write_text(sql, encoding="utf-8")

    total = sum(len(m["evidence"].split(";")) for m in mapping)
    print(f"{standard_code}: {len(mapping)} OEs, {total} records")
    for m in mapping:
        print(
            f"  {m['oe_code']}: {len(m['evidence'].split(';')):3d} records, "
            f"{len(m['evidence']):5d} evidence chars, "
            f"{len(m['responsible']):4d} responsible chars"
        )
    print(f"\nwrote {draft_path}")
    print(f"wrote {sql_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in SOURCES:
        raise SystemExit("usage: apply_oe_evidence.py {hic1|hic2}")
    main(sys.argv[1])
