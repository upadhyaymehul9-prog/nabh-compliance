# -*- coding: utf-8 -*-
"""Insert PSQ.1–PSQ.5 master-policy drafts into live Supabase. Never approves.

These drafts are UNAPPROVED. Do not run --insert until the owner confirms the
write. When that write is confirmed, insert all five rows, leave status = 'draft'
on every one, do not approve, do not generate test docs.

This chapter is PSQ (Patient Safety and Quality Improvement) in the SHCO 3rd
Edition. It is not 2nd Edition CQI. Codes are PSQ.1–PSQ.5.

Uses the same field-by-field hash verification as apply_aac1_supabase.py.
There is no --approve flag on this script. Adding one would be a defect.

Environment:
  SUPABASE_SERVICE_ROLE_KEY  required for --insert / --verify-only.
                             Never printed.
  SUPABASE_URL               optional; defaults to the project URL in
                             apply_aac1_supabase.py.

Usage:
  python3 policies/build/apply_psq_drafts_supabase.py --insert
  python3 policies/build/apply_psq_drafts_supabase.py --verify-only
  python3 policies/build/apply_psq_drafts_supabase.py --dry-run
"""
import argparse
import os
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
from apply_aac1_supabase import (  # noqa: E402
    DEFAULT_URL,
    INSERT_COLUMNS,
    insert_row,
    load_draft,
    verify,
)

CODES = [f"PSQ.{n}" for n in range(1, 6)]
_POLICIES = _HERE.parent


def draft_path_for(code):
    n = code.split(".", 1)[1]
    return _POLICIES / "drafts" / f"psq{n}_draft.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--insert", action="store_true",
                    help="POST each missing PSQ.1–PSQ.5 row (status stays draft)")
    ap.add_argument("--verify-only", action="store_true",
                    help="only verify live rows against local drafts")
    ap.add_argument("--dry-run", action="store_true",
                    help="no network: validate all 5 drafts and print the plan")
    args = ap.parse_args()

    drafts = []
    for code in CODES:
        path = draft_path_for(code)
        draft = load_draft(path, expected_code=code)
        assert draft["status"] == "draft"
        assert draft["chapter"] == "PSQ"
        drafts.append((code, path, draft))
        print(f"draft OK: {path.name}, {len(draft['procedure_steps'])} steps, "
              f"{len(draft['oe_mapping'])} OEs, version {draft['version']}, "
              f"status={draft['status']!r}, chapter={draft['chapter']!r}")

    if args.dry_run:
        print("\nDRY RUN -- no network calls. Plan for each of PSQ.1–PSQ.5:")
        print(f"  1. POST  /rest/v1/shco_policy_masters   ({len(INSERT_COLUMNS)}-column row, status='draft')")
        print("  2. GET   /rest/v1/shco_policy_masters?standard_code=eq.<code>  + field-by-field verify")
        print("  3. Assert live status == 'draft'  (this script never PATCHes status)")
        print("No --approve step exists. Nothing will be flipped to approved.")
        print("Codes are PSQ.1–PSQ.5 (3rd Edition). Not CQI.")
        return 0

    if not args.insert and not args.verify_only:
        raise SystemExit("pass --insert, --verify-only, or --dry-run")

    base_url = os.environ.get("SUPABASE_URL", DEFAULT_URL).rstrip("/")
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not service_key:
        raise SystemExit(
            "SUPABASE_SERVICE_ROLE_KEY is not set. It is a Cloud Agents secret "
            "injected into NEW Cloud Agent VMs only, or available in the "
            "owner's own environment. Nothing was executed. No row was approved."
        )

    summary = []
    all_ok = True
    for code, path, draft in drafts:
        print(f"\n======== {code} ========")
        insert_status = "skipped (verify-only)"
        if args.insert:
            http_status, already = insert_row(base_url, service_key, draft)
            if already:
                insert_status = "REFUSED (row already exists)"
                print(f"INSERT refused: {code} already exists -- not overwriting. "
                      "Verifying the live row against this local draft.")
            else:
                insert_status = f"INSERT ok (HTTP {http_status})"
                print(insert_status)

        ok, live = verify(base_url, service_key, draft)
        live_status = live.get("status") if live else None
        if not ok:
            verify_result = "FAILED"
            all_ok = False
            print(f"verification FAILED for {code}")
        elif live_status != "draft":
            verify_result = f"FAILED (live status={live_status!r}, expected 'draft')"
            all_ok = False
            print(f"verification content matched but live status is {live_status!r} "
                  "-- expected 'draft'. This script did not approve it.")
        else:
            verify_result = "PASSED"
            print(f"verification PASSED: every field of the live {code} row "
                  "matches the local draft; live status='draft'")
        summary.append((code, insert_status, verify_result, live_status or "MISSING"))

    print("\n======== SUMMARY ========")
    print(f"{'code':<8} {'insert':<32} {'verification':<48} {'status'}")
    for code, insert_status, verify_result, live_status in summary:
        print(f"{code:<8} {insert_status:<32} {verify_result:<48} {live_status}")

    if not all_ok:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
