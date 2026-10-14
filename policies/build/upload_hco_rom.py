#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the ROM chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the ROM git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_rom.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "ROM" / "Document" / "ROM_Package_v2"

MANIFEST = [
    ("sop/ROM.1/SOP_ROM1_those_responsible_for_governance.docx", "ROM1/SOP_ROM1_those_responsible_for_governance.docx"),
    ("sop/ROM.2/SOP_ROM2_ethical_management_of_the_organisation.docx", "ROM2/SOP_ROM2_ethical_management_of_the_organisation.docx"),
    ("sop/ROM.3/SOP_ROM3_sustainability_social_responsibility_and_staff_well_being.docx", "ROM3/SOP_ROM3_sustainability_social_responsibility_and_staff_well_being.docx"),
    ("sop/ROM.4/SOP_ROM4_day_to_day_leadership_of_the_organisation.docx", "ROM4/SOP_ROM4_day_to_day_leadership_of_the_organisation.docx"),
    ("sop/ROM.5/SOP_ROM5_professional_functioning_of_the_organisation.docx", "ROM5/SOP_ROM5_professional_functioning_of_the_organisation.docx"),
    ("sop/ROM.6/SOP_ROM6_patient_safety_risk_management_and_outsourced_services.docx", "ROM6/SOP_ROM6_patient_safety_risk_management_and_outsourced_services.docx"),
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
