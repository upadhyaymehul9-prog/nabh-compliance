#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the IMS chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the IMS git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_ims.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "IMS" / "Documents" / "IMS_Package_v2"

MANIFEST = [
    ("sop/IMS.1/SOP_IMS1_meeting_information_needs.docx", "IMS1/SOP_IMS1_meeting_information_needs.docx"),
    ("sop/IMS.2/SOP_IMS2_management_and_control_of_data_and_information.docx", "IMS2/SOP_IMS2_management_and_control_of_data_and_information.docx"),
    ("sop/IMS.3/SOP_IMS3_the_complete_and_accurate_medical_record.docx", "IMS3/SOP_IMS3_the_complete_and_accurate_medical_record.docx"),
    ("sop/IMS.4/SOP_IMS4_the_medical_record_reflecting_continuity_of_care.docx", "IMS4/SOP_IMS4_the_medical_record_reflecting_continuity_of_care.docx"),
    ("sop/IMS.5/SOP_IMS5_confidentiality_integrity_and_security_of_records_data_and_i.docx", "IMS5/SOP_IMS5_confidentiality_integrity_and_security_of_records_data_and_i.docx"),
    ("sop/IMS.6/SOP_IMS6_availability_and_retention_of_current_documents_records_data.docx", "IMS6/SOP_IMS6_availability_and_retention_of_current_documents_records_data.docx"),
    ("sop/IMS.7/SOP_IMS7_review_of_medical_records.docx", "IMS7/SOP_IMS7_review_of_medical_records.docx"),
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
