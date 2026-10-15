#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""One-off batch re-upload: pushes the already-fixed AAC/COP/FMS/HRM SOP .docx
files from this local checkout to Supabase Storage (policy-masters-hco-v2),
since these 4 chapters were committed/pushed to git earlier but the Storage
upload step (the one that actually makes a file live on accredready.in) was
never run for them -- only IPC got that step, when the HCO upload path was
first located.

Environment:
  SUPABASE_SERVICE_ROLE_KEY or SUPABASE_SECRET_KEY  required

Usage (from the repo root):
  python policies\\build\\upload_hco_aac_cop_fms_hrm_reupload.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from upload_storage_file import upload  # noqa: E402

BUCKET = "policy-masters-hco-v2"
REPO_ROOT = Path(__file__).resolve().parents[2]  # policies/build/.. -> repo root
BASE_DIR = REPO_ROOT / "policies" / "build" / "chapters_v2"

MANIFEST = [
    ("sop/AAC.1/SOP_Clinical_Scope_Definition.docx", "AAC/document/AAC1/SOP_Clinical_Scope_Definition.docx"),
    ("sop/AAC.1/SOP_Patient_Referral_Transfer.docx", "AAC/document/AAC1/SOP_Patient_Referral_Transfer.docx"),
    ("sop/AAC.1/SOP_Personnel_Qualification_Verification.docx", "AAC/document/AAC1/SOP_Personnel_Qualification_Verification.docx"),
    ("sop/AAC.10/SOP_HandOver_Communication.docx", "AAC/document/AAC10/SOP_HandOver_Communication.docx"),
    ("sop/AAC.10/SOP_Internal_Referral.docx", "AAC/document/AAC10/SOP_Internal_Referral.docx"),
    ("sop/AAC.10/SOP_Internal_Transfer.docx", "AAC/document/AAC10/SOP_Internal_Transfer.docx"),
    ("sop/AAC.11/SOP_Preventive_Screening_Referral.docx", "AAC/document/AAC11/SOP_Preventive_Screening_Referral.docx"),
    ("sop/AAC.12/SOP_Discharge_Planning_Coordination.docx", "AAC/document/AAC12/SOP_Discharge_Planning_Coordination.docx"),
    ("sop/AAC.12/SOP_LAMA.docx", "AAC/document/AAC12/SOP_LAMA.docx"),
    ("sop/AAC.13/SOP_Discharge_Summary_Content.docx", "AAC/document/AAC13/SOP_Discharge_Summary_Content.docx"),
    ("sop/AAC.2/SOP_Bed_NonAvailability.docx", "AAC/document/AAC2/SOP_Bed_NonAvailability.docx"),
    ("sop/AAC.2/SOP_Clinical_Priority_Queue.docx", "AAC/document/AAC2/SOP_Clinical_Priority_Queue.docx"),
    ("sop/AAC.2/SOP_Registration_Admission.docx", "AAC/document/AAC2/SOP_Registration_Admission.docx"),
    ("sop/AAC.3/SOP_Patient_Transfer_Referral.docx", "AAC/document/AAC3/SOP_Patient_Transfer_Referral.docx"),
    ("sop/AAC.4/SOP_Initial_Assessment.docx", "AAC/document/AAC4/SOP_Initial_Assessment.docx"),
    ("sop/AAC.5/SOP_Early_Warning_Escalation.docx", "AAC/document/AAC5/SOP_Early_Warning_Escalation.docx"),
    ("sop/AAC.5/SOP_Reassessment_CarePlan.docx", "AAC/document/AAC5/SOP_Reassessment_CarePlan.docx"),
    ("sop/AAC.6/SOP_Critical_Lab_Result_Communication.docx", "AAC/document/AAC6/SOP_Critical_Lab_Result_Communication.docx"),
    ("sop/AAC.6/SOP_Lab_Recall_Amendment.docx", "AAC/document/AAC6/SOP_Lab_Recall_Amendment.docx"),
    ("sop/AAC.6/SOP_Specimen_Handling_Reporting.docx", "AAC/document/AAC6/SOP_Specimen_Handling_Reporting.docx"),
    ("sop/AAC.7/SOP_IQC_ResultRelease.docx", "AAC/document/AAC7/SOP_IQC_ResultRelease.docx"),
    ("sop/AAC.7/SOP_Lab_Safety_PPE.docx", "AAC/document/AAC7/SOP_Lab_Safety_PPE.docx"),
    ("sop/AAC.8/SOP_Critical_Imaging_Result.docx", "AAC/document/AAC8/SOP_Critical_Imaging_Result.docx"),
    ("sop/AAC.8/SOP_Imaging_Legal_Compliance.docx", "AAC/document/AAC8/SOP_Imaging_Legal_Compliance.docx"),
    ("sop/AAC.8/SOP_Imaging_Recall_Amendment.docx", "AAC/document/AAC8/SOP_Imaging_Recall_Amendment.docx"),
    ("sop/AAC.9/SOP_Imaging_Appropriateness_PeerReview.docx", "AAC/document/AAC9/SOP_Imaging_Appropriateness_PeerReview.docx"),
    ("sop/AAC.9/SOP_PreImaging_Screening_StopWork.docx", "AAC/document/AAC9/SOP_PreImaging_Screening_StopWork.docx"),
    ("sop/COP.10/SOP_High_Risk_Obstetric_Management.docx", "COP/document/COP10/SOP_High_Risk_Obstetric_Management.docx"),
    ("sop/COP.10/SOP_Labour_Delivery_Monitoring.docx", "COP/document/COP10/SOP_Labour_Delivery_Monitoring.docx"),
    ("sop/COP.11/SOP_Child_Abduction_Prevention.docx", "COP/document/COP11/SOP_Child_Abduction_Prevention.docx"),
    ("sop/COP.13/SOP_Anaesthesia_Care.docx", "COP/document/COP13/SOP_Anaesthesia_Care.docx"),
    ("sop/COP.14/SOP_Surgical_Safety_Checklist.docx", "COP/document/COP14/SOP_Surgical_Safety_Checklist.docx"),
    ("sop/COP.15/SOP_Transplant_Regulatory_Compliance.docx", "COP/document/COP15/SOP_Transplant_Regulatory_Compliance.docx"),
    ("sop/COP.16/SOP_DVT_Prophylaxis.docx", "COP/document/COP16/SOP_DVT_Prophylaxis.docx"),
    ("sop/COP.16/SOP_Fall_Prevention.docx", "COP/document/COP16/SOP_Fall_Prevention.docx"),
    ("sop/COP.16/SOP_Pressure_Ulcer_Prevention.docx", "COP/document/COP16/SOP_Pressure_Ulcer_Prevention.docx"),
    ("sop/COP.16/SOP_Restraint_Use.docx", "COP/document/COP16/SOP_Restraint_Use.docx"),
    ("sop/COP.17/SOP_Pain_Assessment_Management.docx", "COP/document/COP17/SOP_Pain_Assessment_Management.docx"),
    ("sop/COP.19/SOP_Nutritional_Screening_Diet_Management.docx", "COP/document/COP19/SOP_Nutritional_Screening_Diet_Management.docx"),
    ("sop/COP.2/SOP_Emergency_Triage.docx", "COP/document/COP2/SOP_Emergency_Triage.docx"),
    ("sop/COP.2/SOP_MLC_Death_Management.docx", "COP/document/COP2/SOP_MLC_Death_Management.docx"),
    ("sop/COP.20/SOP_DNR_DNI_AND_Decision_Making.docx", "COP/document/COP20/SOP_DNR_DNI_AND_Decision_Making.docx"),
    ("sop/COP.3/SOP_Ambulance_Dispatch_InTransit_Care.docx", "COP/document/COP3/SOP_Ambulance_Dispatch_InTransit_Care.docx"),
    ("sop/COP.5/SOP_Code_Blue_CPR_Response.docx", "COP/document/COP5/SOP_Code_Blue_CPR_Response.docx"),
    ("sop/COP.7/SOP_Safe_Procedure_Verification.docx", "COP/document/COP7/SOP_Safe_Procedure_Verification.docx"),
    ("sop/COP.8/SOP_Blood_Transfusion_Administration.docx", "COP/document/COP8/SOP_Blood_Transfusion_Administration.docx"),
    ("sop/COP.9/SOP_ICU_Admission_Discharge_BedShortage.docx", "COP/document/COP9/SOP_ICU_Admission_Discharge_BedShortage.docx"),
    ("sop/FMS.1/SOP_FMS1_safe_and_secure_environment.docx", "FMS/document/FMS_Package_v2/FMS1/SOP_FMS1_safe_and_secure_environment.docx"),
    ("sop/FMS.2/SOP_FMS2_planned_facilities_and_environment_friendly_measures.docx", "FMS/document/FMS_Package_v2/FMS2/SOP_FMS2_planned_facilities_and_environment_friendly_measures.docx"),
    ("sop/FMS.3/SOP_FMS3_safety_of_patients_families_staff_and_visitors.docx", "FMS/document/FMS_Package_v2/FMS3/SOP_FMS3_safety_of_patients_families_staff_and_visitors.docx"),
    ("sop/FMS.4/SOP_FMS4_facility_engineering_support_and_utility_systems.docx", "FMS/document/FMS_Package_v2/FMS4/SOP_FMS4_facility_engineering_support_and_utility_systems.docx"),
    ("sop/FMS.5/SOP_FMS5_medical_equipment_management.docx", "FMS/document/FMS_Package_v2/FMS5/SOP_FMS5_medical_equipment_management.docx"),
    ("sop/FMS.6/SOP_FMS6_medical_gases_vacuum_and_compressed_air.docx", "FMS/document/FMS_Package_v2/FMS6/SOP_FMS6_medical_gases_vacuum_and_compressed_air.docx"),
    ("sop/FMS.7/SOP_FMS7_fire_and_non_fire_emergencies.docx", "FMS/document/FMS_Package_v2/FMS7/SOP_FMS7_fire_and_non_fire_emergencies.docx"),
    ("sop/HRM.1/SOP_HRM1_human_resource_planning_and_governance.docx", "HRM/documents/HRM_Package_v2/HRM1/SOP_HRM1_human_resource_planning_and_governance.docx"),
    ("sop/HRM.10/SOP_HRM10_staff_personal_information_and_records.docx", "HRM/documents/HRM_Package_v2/HRM10/SOP_HRM10_staff_personal_information_and_records.docx"),
    ("sop/HRM.11/SOP_HRM11_credentialing_and_privileging_of_medical_professionals.docx", "HRM/documents/HRM_Package_v2/HRM11/SOP_HRM11_credentialing_and_privileging_of_medical_professionals.docx"),
    ("sop/HRM.12/SOP_HRM12_credentialing_and_privileging_of_nursing_professionals.docx", "HRM/documents/HRM_Package_v2/HRM12/SOP_HRM12_credentialing_and_privileging_of_nursing_professionals.docx"),
    ("sop/HRM.13/SOP_HRM13_credentialing_and_privileging_of_para_clinical_professionals.docx", "HRM/documents/HRM_Package_v2/HRM13/SOP_HRM13_credentialing_and_privileging_of_para_clinical_professionals.docx"),
    ("sop/HRM.2/SOP_HRM2_staff_recruitment.docx", "HRM/documents/HRM_Package_v2/HRM2/SOP_HRM2_staff_recruitment.docx"),
    ("sop/HRM.3/SOP_HRM3_staff_induction_training.docx", "HRM/documents/HRM_Package_v2/HRM3/SOP_HRM3_staff_induction_training.docx"),
    ("sop/HRM.4/SOP_HRM4_professional_training_and_development.docx", "HRM/documents/HRM_Package_v2/HRM4/SOP_HRM4_professional_training_and_development.docx"),
    ("sop/HRM.5/SOP_HRM5_job_specific_staff_training.docx", "HRM/documents/HRM_Package_v2/HRM5/SOP_HRM5_job_specific_staff_training.docx"),
    ("sop/HRM.6/SOP_HRM6_safety_and_quality_related_staff_training.docx", "HRM/documents/HRM_Package_v2/HRM6/SOP_HRM6_safety_and_quality_related_staff_training.docx"),
    ("sop/HRM.7/SOP_HRM7_staff_performance_appraisal.docx", "HRM/documents/HRM_Package_v2/HRM7/SOP_HRM7_staff_performance_appraisal.docx"),
    ("sop/HRM.8/SOP_HRM8_disciplinary_and_grievance_handling.docx", "HRM/documents/HRM_Package_v2/HRM8/SOP_HRM8_disciplinary_and_grievance_handling.docx"),
    ("sop/HRM.9/SOP_HRM9_staff_health_and_safety.docx", "HRM/documents/HRM_Package_v2/HRM9/SOP_HRM9_staff_health_and_safety.docx"),
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
