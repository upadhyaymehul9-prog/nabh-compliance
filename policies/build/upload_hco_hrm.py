#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the HRM chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the HRM git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_hrm.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "HRM" / "documents" / "HRM_Package_v2"

MANIFEST = [
    ("sop/HRM.1/SOP_HRM1_human_resource_planning_and_governance.docx", "HRM1/SOP_HRM1_human_resource_planning_and_governance.docx"),
    ("sop/HRM.2/SOP_HRM2_staff_recruitment.docx", "HRM2/SOP_HRM2_staff_recruitment.docx"),
    ("sop/HRM.3/SOP_HRM3_staff_induction_training.docx", "HRM3/SOP_HRM3_staff_induction_training.docx"),
    ("sop/HRM.4/SOP_HRM4_professional_training_and_development.docx", "HRM4/SOP_HRM4_professional_training_and_development.docx"),
    ("sop/HRM.5/SOP_HRM5_job_specific_staff_training.docx", "HRM5/SOP_HRM5_job_specific_staff_training.docx"),
    ("sop/HRM.6/SOP_HRM6_safety_and_quality_related_staff_training.docx", "HRM6/SOP_HRM6_safety_and_quality_related_staff_training.docx"),
    ("sop/HRM.7/SOP_HRM7_staff_performance_appraisal.docx", "HRM7/SOP_HRM7_staff_performance_appraisal.docx"),
    ("sop/HRM.8/SOP_HRM8_disciplinary_and_grievance_handling.docx", "HRM8/SOP_HRM8_disciplinary_and_grievance_handling.docx"),
    ("sop/HRM.9/SOP_HRM9_staff_health_and_safety.docx", "HRM9/SOP_HRM9_staff_health_and_safety.docx"),
    ("sop/HRM.10/SOP_HRM10_staff_personal_information_and_records.docx", "HRM10/SOP_HRM10_staff_personal_information_and_records.docx"),
    ("sop/HRM.11/SOP_HRM11_credentialing_and_privileging_of_medical_professionals.docx", "HRM11/SOP_HRM11_credentialing_and_privileging_of_medical_professionals.docx"),
    ("sop/HRM.12/SOP_HRM12_credentialing_and_privileging_of_nursing_professionals.docx", "HRM12/SOP_HRM12_credentialing_and_privileging_of_nursing_professionals.docx"),
    ("sop/HRM.13/SOP_HRM13_credentialing_and_privileging_of_para_clinical_professionals.docx", "HRM13/SOP_HRM13_credentialing_and_privileging_of_para_clinical_professionals.docx"),
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
