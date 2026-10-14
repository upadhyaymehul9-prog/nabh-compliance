#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the IPC chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the IPC git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_ipc.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "IPC" / "Documents" / "IPC_Package_v2"

MANIFEST = [
    ("sop/IPC.1/SOP_IPC1_infection_prevention_and_control_programme.docx", "IPC1/SOP_IPC1_infection_prevention_and_control_programme.docx"),
    ("sop/IPC.2/SOP_IPC2_resources_for_infection_prevention_and_control.docx", "IPC2/SOP_IPC2_resources_for_infection_prevention_and_control.docx"),
    ("sop/IPC.3/SOP_IPC3_infection_prevention_and_control_in_clinical_areas.docx", "IPC3/SOP_IPC3_infection_prevention_and_control_in_clinical_areas.docx"),
    ("sop/IPC.4/SOP_IPC4_infection_prevention_and_control_in_support_services.docx", "IPC4/SOP_IPC4_infection_prevention_and_control_in_support_services.docx"),
    ("sop/IPC.5/SOP_IPC5_prevention_of_healthcare_associated_infections_in_patients.docx", "IPC5/SOP_IPC5_prevention_of_healthcare_associated_infections_in_patients.docx"),
    ("sop/IPC.6/SOP_IPC6_infection_prevention_and_control_surveillance.docx", "IPC6/SOP_IPC6_infection_prevention_and_control_surveillance.docx"),
    ("sop/IPC.7/SOP_IPC7_sterilisation_and_disinfection_of_instruments_equipment_and_.docx", "IPC7/SOP_IPC7_sterilisation_and_disinfection_of_instruments_equipment_and_.docx"),
    ("sop/IPC.8/SOP_IPC8_prevention_of_healthcare_associated_infections_in_staff.docx", "IPC8/SOP_IPC8_prevention_of_healthcare_associated_infections_in_staff.docx"),
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
