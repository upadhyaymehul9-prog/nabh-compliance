#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the PRE chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the PRE git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_pre.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "PRE" / "Documents"

MANIFEST = [
    ("sop/PRE.1/SOP_Patient_Rights_Display_Promotion_Reporting.docx", "PRE1/SOP_Patient_Rights_Display_Promotion_Reporting.docx"),
    ("sop/PRE.2/SOP_Cost_Records_Access_and_InfoSharing_Preferences.docx", "PRE2/SOP_Cost_Records_Access_and_InfoSharing_Preferences.docx"),
    ("sop/PRE.2/SOP_Privacy_Dignity_Confidentiality_Neglect_Protection.docx", "PRE2/SOP_Privacy_Dignity_Confidentiality_Neglect_Protection.docx"),
    ("sop/PRE.2/SOP_Treatment_Refusal_Second_Opinion_HighRisk_Consent.docx", "PRE2/SOP_Treatment_Refusal_Second_Opinion_HighRisk_Consent.docx"),
    ("sop/PRE.3/SOP_Informed_Decision_Making_Care_Planning.docx", "PRE3/SOP_Informed_Decision_Making_Care_Planning.docx"),
    ("sop/PRE.4/SOP_Informed_Consent_Process.docx", "PRE4/SOP_Informed_Consent_Process.docx"),
    ("sop/PRE.5/SOP_Patient_Family_Education.docx", "PRE5/SOP_Patient_Family_Education.docx"),
    ("sop/PRE.6/SOP_Cost_Information_and_Estimates.docx", "PRE6/SOP_Cost_Information_and_Estimates.docx"),
    ("sop/PRE.7/SOP_Feedback_Experience_Complaint_Redressal.docx", "PRE7/SOP_Feedback_Experience_Complaint_Redressal.docx"),
    ("sop/PRE.8/SOP_Effective_and_Enhanced_Communication.docx", "PRE8/SOP_Effective_and_Enhanced_Communication.docx"),
]


def main() -> int:
    ok, failed = 0, []
    for storage_path, rel_local in MANIFEST:
        local_file = BASE_DIR / rel_local
        if not local_file.exists():
            failed.append((storage_path, "local file not found: " + str(local_file)))
            continue
        try:
            upload(BUCKET, storage_path, local_file)
            ok += 1
        except SystemExit as e:
            failed.append((storage_path, str(e)))

    print(f"\n{ok}/{len(MANIFEST)} uploaded successfully.")
    if failed:
        print(f"{len(failed)} FAILED:")
        for p, err in failed:
            print(f"  - {p}: {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
