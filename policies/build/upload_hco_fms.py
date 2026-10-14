#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the FMS chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the FMS git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_fms.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "FMS" / "document" / "FMS_Package_v2"

MANIFEST = [
    ("sop/FMS.1/SOP_FMS1_safe_and_secure_environment.docx", "FMS1/SOP_FMS1_safe_and_secure_environment.docx"),
    ("sop/FMS.2/SOP_FMS2_planned_facilities_and_environment_friendly_measures.docx", "FMS2/SOP_FMS2_planned_facilities_and_environment_friendly_measures.docx"),
    ("sop/FMS.3/SOP_FMS3_safety_of_patients_families_staff_and_visitors.docx", "FMS3/SOP_FMS3_safety_of_patients_families_staff_and_visitors.docx"),
    ("sop/FMS.4/SOP_FMS4_facility_engineering_support_and_utility_systems.docx", "FMS4/SOP_FMS4_facility_engineering_support_and_utility_systems.docx"),
    ("sop/FMS.5/SOP_FMS5_medical_equipment_management.docx", "FMS5/SOP_FMS5_medical_equipment_management.docx"),
    ("sop/FMS.6/SOP_FMS6_medical_gases_vacuum_and_compressed_air.docx", "FMS6/SOP_FMS6_medical_gases_vacuum_and_compressed_air.docx"),
    ("sop/FMS.7/SOP_FMS7_fire_and_non_fire_emergencies.docx", "FMS7/SOP_FMS7_fire_and_non_fire_emergencies.docx"),
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
