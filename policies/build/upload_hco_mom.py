#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch upload: pushes the MOM chapter's fixed SOP .docx files from
this local checkout to Supabase Storage (policy-masters-hco-v2), right after
the MOM git commit/push, per the Records/SOPs/Policy Delivery Rule.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_mom.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2" / "MOM" / "Document"

MANIFEST = [
    ("sop/MOM.1/SOP_Emergency_Medication_Sourcing.docx", "MOM1/SOP_Emergency_Medication_Sourcing.docx"),
    ("sop/MOM.10/SOP_Implant_Device_Management.docx", "MOM10/SOP_Implant_Device_Management.docx"),
    ("sop/MOM.2/SOP_NonFormulary_Medication_Request.docx", "MOM2/SOP_NonFormulary_Medication_Request.docx"),
    ("sop/MOM.3/SOP_High_Risk_LASA_Medication_Storage.docx", "MOM3/SOP_High_Risk_LASA_Medication_Storage.docx"),
    ("sop/MOM.4/SOP_Medication_Reconciliation.docx", "MOM4/SOP_Medication_Reconciliation.docx"),
    ("sop/MOM.4/SOP_Safe_Prescribing.docx", "MOM4/SOP_Safe_Prescribing.docx"),
    ("sop/MOM.4/SOP_Verbal_Order_Process.docx", "MOM4/SOP_Verbal_Order_Process.docx"),
    ("sop/MOM.5/SOP_Order_Writing_Standards.docx", "MOM5/SOP_Order_Writing_Standards.docx"),
    ("sop/MOM.6/SOP_HighRisk_Dispensing_Recall.docx", "MOM6/SOP_HighRisk_Dispensing_Recall.docx"),
    ("sop/MOM.6/SOP_Universal_Medication_Labelling.docx", "MOM6/SOP_Universal_Medication_Labelling.docx"),
    ("sop/MOM.7/SOP_IV_Line_Tubing_Safety.docx", "MOM7/SOP_IV_Line_Tubing_Safety.docx"),
    ("sop/MOM.7/SOP_Medication_Administration_Rights.docx", "MOM7/SOP_Medication_Administration_Rights.docx"),
    ("sop/MOM.8/SOP_ADR_Medication_Error_Reporting.docx", "MOM8/SOP_ADR_Medication_Error_Reporting.docx"),
    ("sop/MOM.9/SOP_Chemotherapy_Radiopharmaceutical_Handling.docx", "MOM9/SOP_Chemotherapy_Radiopharmaceutical_Handling.docx"),
    ("sop/MOM.9/SOP_Narcotic_Psychotropic_Handling.docx", "MOM9/SOP_Narcotic_Psychotropic_Handling.docx"),
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
