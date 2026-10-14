#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the PSQ chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the PSQ git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_psq.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "PSQ" / "document" / "PSQ_Package_v2"

MANIFEST = [
    ("sop/PSQ.1/SOP_PSQ1_patient_safety_programme.docx", "PSQ1/SOP_PSQ1_patient_safety_programme.docx"),
    ("sop/PSQ.2/SOP_PSQ2_quality_improvement_programme.docx", "PSQ2/SOP_PSQ2_quality_improvement_programme.docx"),
    ("sop/PSQ.3/SOP_PSQ3_quality_indicators_data_analysis_and_improvement.docx", "PSQ3/SOP_PSQ3_quality_indicators_data_analysis_and_improvement.docx"),
    ("sop/PSQ.4/SOP_PSQ4_quality_improvement_projects.docx", "PSQ4/SOP_PSQ4_quality_improvement_projects.docx"),
    ("sop/PSQ.5/SOP_PSQ5_clinical_audit.docx", "PSQ5/SOP_PSQ5_clinical_audit.docx"),
    ("sop/PSQ.6/SOP_PSQ6_safety_culture_leadership_and_resources.docx", "PSQ6/SOP_PSQ6_safety_culture_leadership_and_resources.docx"),
    ("sop/PSQ.7/SOP_PSQ7_incident_management_and_safety_events.docx", "PSQ7/SOP_PSQ7_incident_management_and_safety_events.docx"),
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
