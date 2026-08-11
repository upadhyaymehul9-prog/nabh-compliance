"""Assemble policies/drafts/hic2_draft.json and verify every field against the live row.

WHY THIS EXISTS
HIC.2 is the only approved master with no local draft file. shco_policy_masters has
RLS enabled with zero policies, so only the service role can read it, and the service
role key deliberately never enters this terminal. The row was therefore exported from
the Supabase dashboard by the owner.

The dashboard export truncated exactly one field, universal_facts_checklist, so that
field is supplied separately from a SELECT of the live row.

NOTHING here is trusted on faith: every field is md5-compared against the live row
before the draft file is considered usable. The expected hashes in LIVE_MD5 were read
with the query documented in that dict's comment.

Usage:
    python policies/build/build_hic2_draft.py \
        --export  <path to dashboard export .json> \
        --checklist <path to universal_facts_checklist .txt>
"""

import argparse
import hashlib
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
OUT = REPO / "policies/drafts/hic2_draft.json"

RS = chr(30)  # record separator, used to join array elements before hashing
US = chr(31)  # unit separator, used between oe_mapping fields

# Read from the live row with:
#   select md5(policy_title), md5(purpose), ... ,
#          md5(array_to_string(procedure_steps, chr(30))),
#          md5((select string_agg(
#                (e->>'oe_code')||chr(31)||(e->>'requirement')||chr(31)||(e->>'steps')||chr(31)||
#                coalesce(e->>'evidence','')||chr(31)||coalesce(e->>'responsible',''), chr(30) order by ord)
#              from jsonb_array_elements(oe_mapping) with ordinality as t(e, ord)))
#   from public.shco_policy_masters where standard_code = 'HIC.2';
LIVE_MD5 = {
    "policy_title": "9d0ba51dab04317408a8bac572bb1105",
    "purpose": "02374954a2f0aac4da8ec3a188fca1d4",
    "scope": "733d5477a77c4d77661fd820f27b7009",
    "policy_statement": "f534a3d0ff35daa464dce3e045dd6f64",
    "responsibility": "8a3d0d660c5458c08c2149feafe4d231",
    "references_text": "239d9038bfb87ac9fdb4741216d60d10",
    "distribution": "2a6f5cff39ce6254c164421e9108e644",
    "abbreviations": "83c02a3d5b7eed99f53fd1ee7edd6f92",
    "disclaimer": "8a5d570582bfccd56eb9c217b4f4b43c",
    "universal_facts_checklist": "8ac1d64db619bbdd76820407cba07932",
    "chapter": "a25baf723f95fbcbceae8399b638f108",
    "standard_code": "20325d0a5fe42fcb65d1754c56173d25",
    "status": "787d5f05953ec39b108869dfdd7733e6",
    "oe_codes": "4feb4462c7fb63fb0a12dd81de131334",
    "procedure_steps": "8608aeb04ebc2d7c9d19ff925d1c887d",
    "oe_mapping": "4ef3fc6ab2e46522a855e73aafca3468",
}

# Columns confirmed NULL on the live row; the draft must not invent values for them.
LIVE_NULL = [
    "definitions",
    "exceptions",
    "monitoring_audit",
    "resources_required",
    "training_competency",
]

md5 = lambda s: hashlib.md5(s.encode("utf-8")).hexdigest()


def canonical(field, value):
    """Reduce a field to the exact string the live-row query hashed."""
    if field == "procedure_steps" or field == "oe_codes":
        return RS.join(value)
    if field == "oe_mapping":
        return RS.join(
            US.join(
                [
                    e["oe_code"],
                    e["requirement"],
                    e["steps"],
                    e.get("evidence") or "",
                    e.get("responsible") or "",
                ]
            )
            for e in value
        )
    return value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", required=True)
    ap.add_argument("--checklist", required=True)
    args = ap.parse_args()

    export = json.loads(Path(args.export).read_text(encoding="utf-8"))
    if isinstance(export, list):
        export = export[0]
    row = export.get("to_jsonb", export)

    # The one field the dashboard export truncated, taken from the live row instead.
    row["universal_facts_checklist"] = Path(args.checklist).read_text(encoding="utf-8")

    # Shape it like the other five drafts: content fields only, in the same key order.
    draft = {
        "standard_code": row["standard_code"],
        "chapter": row["chapter"],
        "oe_codes": row["oe_codes"],
        "policy_title": row["policy_title"],
        "purpose": row["purpose"],
        "scope": row["scope"],
        "policy_statement": row["policy_statement"],
        "procedure_steps": row["procedure_steps"],
        "responsibility": row["responsibility"],
        "references_text": row["references_text"],
        "distribution": row["distribution"],
        "abbreviations": row["abbreviations"],
        "disclaimer": row["disclaimer"],
        "oe_mapping": row["oe_mapping"],
        "universal_facts_checklist": row["universal_facts_checklist"],
        "status": row["status"],
    }

    results = []
    for field, want in LIVE_MD5.items():
        got = md5(canonical(field, draft[field]))
        results.append((field, got == want, got, want))

    for field in LIVE_NULL:
        present = row.get(field) is not None
        results.append((f"{field} (must be NULL)", not present, "null" if not present else "SET", "null"))

    width = max(len(r[0]) for r in results)
    print(f"{'FIELD'.ljust(width)}  RESULT   md5")
    print("-" * (width + 44))
    for field, ok, got, want in results:
        mark = "MATCH " if ok else "DIFFER"
        print(f"{field.ljust(width)}  {mark}   {got}")
        if not ok:
            print(f"{''.ljust(width)}           expected {want}")

    failed = [r[0] for r in results if not r[1]]
    print("-" * (width + 44))
    print(f"{len(results) - len(failed)} of {len(results)} checks passed.")

    if failed:
        print("FAILED: " + ", ".join(failed))
        print("Draft NOT written.")
        raise SystemExit(1)

    OUT.write_text(json.dumps(draft, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nAll fields match the live row. Wrote {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
