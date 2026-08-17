# -*- coding: utf-8 -*-
"""Finishes AAC.1 against live Supabase: insert, verify, approve, re-verify, test-doc.

Written 2026-08-17 because the SUPABASE_SERVICE_ROLE_KEY Cloud Agents secret is
injected only into NEW Cloud Agent VMs, and the run that drafted AAC.1 booted
before the secret existed. This script lets the next run -- or the owner's own
workstation, where the key already lives in the environment -- finish the job
with one command instead of re-deriving the steps.

THE OWNER'S WRITE DISCIPLINE (2026-08-17) applies to this script: every
INSERT/UPDATE against shco_policy_masters or shco_full_oes is shown to the owner
and confirmed BEFORE it is executed. The two writes this script performs were
both explicitly confirmed in the AAC.1 approval instruction of 2026-08-17
("run the insert ... then flip status = 'approved'"). Do not point this script
at any other standard without going through that discipline again.

What it does, in order (each step skippable by flag):
  1. --insert    POST the row to PostgREST from policies/drafts/aac1_draft.json.
                 The draft dict's keys match the insert columns of
                 policies/sql/aac1_insert.sql exactly (asserted below), so this
                 is the same row that SQL would create. Refuses if AAC.1 already
                 exists (no accidental duplicates; PostgREST would 409 anyway on
                 a unique standard_code, but the refusal message is clearer).
  2. (always)    VERIFY: fetch the live row and compare EVERY inserted field
                 against the local draft -- byte equality plus md5 per field,
                 line-ending aware (HIC.1 stores CRLF, HIC.2 LF; see
                 scripts/master-policy-todos.md 2026-08-13 -- comparisons here
                 normalise CR before hashing and report which convention the
                 live row actually stores).
  3. --approve   PATCH status = 'draft' -> 'approved'. SQL equivalent:
                   update public.shco_policy_masters
                     set status = 'approved' where standard_code = 'AAC.1';
                 Refuses to run unless verification has just passed. Note the
                 updated_at trigger (migration 20260812) will stamp now() --
                 expected behaviour, reported after the flip.
  4. --test-doc  POST to the REAL generate-hospital-policy edge function (the
                 shipping path, not the local renderer) with the public anon
                 key, and save the returned docx. Only meaningful after
                 approval -- the function refuses drafts by design.

Environment:
  SUPABASE_SERVICE_ROLE_KEY  required for --insert / --approve / verification
                             (RLS hides the row from anon). Never printed.
  SUPABASE_URL               optional; defaults to the project URL below.

Usage:
  python policies/build/apply_aac1_supabase.py --insert --approve --test-doc
  python policies/build/apply_aac1_supabase.py --verify-only
  python policies/build/apply_aac1_supabase.py --dry-run     # no network, no key
"""
import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request

from pathlib import Path

_HERE = Path(__file__).resolve().parent          # policies/build
_POLICIES = _HERE.parent                         # policies
DRAFT_PATH = _POLICIES / "drafts" / "aac1_draft.json"

DEFAULT_URL = "https://tbptllgcjtiiqspxqcde.supabase.co"
# The public anon key, as shipped in src/supabaseClient.js. Public by design;
# used only for the edge-function call, which needs no privileged role.
ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRicHRsbGdjanRpaXFzcHhxY2RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY2NjkzNjAsImV4cCI6MjA5MjI0NTM2MH0."
    "4CPgNp6ytVNRmTU0FJbu2io94QJmsAow5im-vGtoRAU"
)

STANDARD_CODE = "AAC.1"
HOSPITAL_NAME = "HMP Foundation"

# The columns policies/sql/aac1_insert.sql inserts, i.e. the exact contract this
# script must honour. Asserted against the draft file at runtime.
INSERT_COLUMNS = [
    "standard_code", "chapter", "oe_codes", "policy_title", "purpose", "scope",
    "policy_statement", "procedure_steps", "responsibility", "references_text",
    "distribution", "abbreviations", "disclaimer", "oe_mapping",
    "universal_facts_checklist", "version", "revision_history", "status",
]


def load_draft():
    draft = json.loads(DRAFT_PATH.read_text(encoding="utf-8"))
    assert sorted(draft.keys()) == sorted(INSERT_COLUMNS), (
        "draft keys diverged from the SQL insert's column list:\n"
        f"  draft-only: {sorted(set(draft) - set(INSERT_COLUMNS))}\n"
        f"  sql-only:   {sorted(set(INSERT_COLUMNS) - set(draft))}"
    )
    assert draft["standard_code"] == STANDARD_CODE
    assert draft["status"] == "draft", "draft file must carry status=draft; approval happens live"
    return draft


def request(method, url, key, body=None, extra_headers=None):
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
    }
    headers.update(extra_headers or {})
    data = json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.status, resp.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()


def md5_lf(text):
    return hashlib.md5(text.replace("\r", "").encode("utf-8")).hexdigest()


def verify(base_url, service_key, draft):
    """Fetch the live AAC.1 row and compare every inserted field. Returns ok bool."""
    status, raw = request(
        "GET",
        f"{base_url}/rest/v1/shco_policy_masters"
        f"?standard_code=eq.{STANDARD_CODE}&select=*",
        service_key,
    )
    if status != 200:
        print(f"  VERIFY FAILED: fetch returned HTTP {status}: {raw[:200]!r}")
        return False, None
    rows = json.loads(raw)
    if len(rows) != 1:
        print(f"  VERIFY FAILED: expected exactly 1 row for {STANDARD_CODE}, got {len(rows)}")
        return False, None
    live = rows[0]

    ok = True
    crlf_fields = []
    for col in INSERT_COLUMNS:
        if col == "status":
            continue  # compared by the caller against the stage's expectation
        local, remote = draft[col], live.get(col)
        if isinstance(local, str):
            if "\r" in (remote or ""):
                crlf_fields.append(col)
            same = local.replace("\r", "") == (remote or "").replace("\r", "")
            note = f"md5(LF)={md5_lf(local)}" if same else "MISMATCH"
        else:
            # oe_codes (list), procedure_steps (list), oe_mapping / revision_history (jsonb)
            same = local == remote
            note = "deep-equal" if same else "MISMATCH"
        print(f"  {col:28} {'OK ' if same else 'FAIL'} {note}")
        if not same:
            ok = False
    print(f"  line endings stored by the live row: "
          f"{'CRLF in ' + ', '.join(crlf_fields) if crlf_fields else 'LF throughout (matches the draft)'}")
    print(f"  live status={live.get('status')!r} version={live.get('version')!r} "
          f"created_at={live.get('created_at')} updated_at={live.get('updated_at')}")
    return ok, live


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--insert", action="store_true", help="insert the AAC.1 row")
    ap.add_argument("--approve", action="store_true", help="flip status to approved (after verification)")
    ap.add_argument("--test-doc", action="store_true", help="generate the real edge-function document")
    ap.add_argument("--verify-only", action="store_true", help="only verify the live row against the draft")
    ap.add_argument("--dry-run", action="store_true", help="no network: validate the draft and print the plan")
    args = ap.parse_args()

    draft = load_draft()
    print(f"draft OK: {DRAFT_PATH.name}, {len(draft['procedure_steps'])} steps, "
          f"{len(draft['oe_mapping'])} OEs, version {draft['version']}")

    if args.dry_run:
        print("\nDRY RUN -- no network calls. Plan:")
        print(f"  1. POST  /rest/v1/shco_policy_masters   (the {len(INSERT_COLUMNS)}-column row above)")
        print("  2. GET   /rest/v1/shco_policy_masters?standard_code=eq.AAC.1  + field-by-field verify")
        print("  3. PATCH /rest/v1/shco_policy_masters?standard_code=eq.AAC.1  {\"status\": \"approved\"}")
        print("     SQL equivalent: update public.shco_policy_masters set status = 'approved' where standard_code = 'AAC.1';")
        print("  4. POST  /functions/v1/generate-hospital-policy  {standard_code, hospital_name} -> docx")
        return

    base_url = os.environ.get("SUPABASE_URL", DEFAULT_URL).rstrip("/")
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY")
    if not service_key:
        raise SystemExit(
            "SUPABASE_SERVICE_ROLE_KEY is not set. It is a Cloud Agents secret injected "
            "into NEW Cloud Agent VMs only, or available in the owner's own environment. "
            "Nothing was executed."
        )

    if args.insert:
        status, raw = request(
            "GET",
            f"{base_url}/rest/v1/shco_policy_masters?standard_code=eq.{STANDARD_CODE}&select=standard_code",
            service_key,
        )
        if status == 200 and json.loads(raw):
            raise SystemExit(f"{STANDARD_CODE} already exists -- refusing to insert a duplicate. "
                             "Run with --verify-only to check it.")
        status, raw = request(
            "POST",
            f"{base_url}/rest/v1/shco_policy_masters",
            service_key,
            body=draft,
            extra_headers={"Prefer": "return=minimal"},
        )
        if status not in (200, 201):
            raise SystemExit(f"INSERT failed: HTTP {status}: {raw[:400]!r}")
        print(f"INSERT ok (HTTP {status})")

    ok, live = verify(base_url, service_key, draft)
    if not ok:
        raise SystemExit("verification FAILED -- do not approve; investigate the mismatched fields")
    print("verification PASSED: every field of the live row matches the local draft")

    if args.verify_only:
        return

    if args.approve:
        if live.get("status") == "approved":
            print("status already 'approved' -- nothing to flip")
        else:
            status, raw = request(
                "PATCH",
                f"{base_url}/rest/v1/shco_policy_masters?standard_code=eq.{STANDARD_CODE}",
                service_key,
                body={"status": "approved"},
                extra_headers={"Prefer": "return=representation"},
            )
            if status not in (200, 204):
                raise SystemExit(f"APPROVE failed: HTTP {status}: {raw[:400]!r}")
            updated = json.loads(raw)[0] if status == 200 and raw else {}
            print(f"APPROVE ok (HTTP {status}); status={updated.get('status')!r}, "
                  f"updated_at={updated.get('updated_at')} (trigger-stamped, expected)")
        ok, live = verify(base_url, service_key, draft)
        if not ok or live.get("status") != "approved":
            raise SystemExit("post-approval re-verification FAILED")
        print("post-approval re-verification PASSED (content unchanged, status='approved')")

    if args.test_doc:
        status, raw = request(
            "POST",
            f"{base_url}/functions/v1/generate-hospital-policy",
            ANON_KEY,
            body={"standard_code": STANDARD_CODE, "hospital_name": HOSPITAL_NAME},
        )
        if status != 200:
            raise SystemExit(f"edge function returned HTTP {status}: {raw[:400]!r}")
        out = Path("/tmp/AAC1_edge_function_test.docx")
        out.write_bytes(raw)
        print(f"edge-function document: {len(raw)} bytes -> {out}")


if __name__ == "__main__":
    main()
