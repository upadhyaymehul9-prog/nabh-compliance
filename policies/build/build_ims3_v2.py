# -*- coding: utf-8 -*-
"""IMS.3 v2 — medical record reflects continuity of care.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 139.
No stop-work. Six OEs in six What-we-do subsections.
Disclaimer P2 is accreditation-only plus a light data-protection forward-note.
"""
from __future__ import annotations

import sys

from ims_v2_disclaimer import make_ims_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "IMS.3"
CHAPTER = "IMS"
OE_CODES = [
    "IMS.3.a", "IMS.3.b", "IMS.3.c", "IMS.3.d", "IMS.3.e", "IMS.3.f",
]
POLICY_TITLE = "Medical Record Reflects Continuity of Care"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "IMS v2 template: PRE v2 shape, plain English, IMS roles, six steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The medical record reflects continuity of care — admission reason, diagnosis and "
    "plan; assessments and care given; transfer details; a discharge-summary copy; a "
    "cause-of-death certificate copy where death occurs; and access for care providers "
    "to current and past records."
)

PURPOSE = f"""This policy describes how the medical record at {HOSPITAL} contains the continuity-of-care items IMS.3 names: reasons for admission, diagnosis and plan of care; details of assessments, reassessments, consultations, investigation results, operative and other procedures, and care provided; transfer details when the patient is transferred to another hospital; a copy of the discharge summary; a copy of the cause-of-death certificate in case of death; and access for care providers to the current and past medical record.

IMS.3 owns these as record-completeness requirements. Care chapters own the clinical content: AAC.3 owns assessment and care planning; AAC.7 owns handover and internal transfer mechanics; AAC.2 owns transfer-out mechanics; AAC.8 owns the discharge summary itself; COP owns operative and procedure notes. This policy requires that copies and details are in the record — it does not rewrite those clinical methods.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors, nurses, the {D('Medical Records Officer')}, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the six elements IMS.3.a–f. It does not cover entry authentication (IMS.2), confidentiality of access (IMS.4), retention (IMS.5), or the review programme (IMS.6).

Boundaries with other policies of {HOSPITAL}:

- AAC.8 owns the discharge summary given to the patient. This policy owns that a copy is in the medical record (IMS.3.d).
- AAC.2 and AAC.7 own transfer-out and internal-handover mechanics. This policy owns that transfer details are in the record when the patient is transferred to another hospital (IMS.3.c).
- AAC.3 owns initial assessment, reassessment and the plan of care. This policy owns that those details are in the record (IMS.3.a–b).
- COP owns operative notes, procedure notes and clinical documentation of care given. This policy owns that those details are in the record (IMS.3.b).
- IMS.4 owns who may access the record. IMS.3.f owns that care providers have access to current and past records for care."""

POLICY_STATEMENT = f"""The medical record at {HOSPITAL} reflects continuity of care.

It contains reasons for admission, diagnosis and plan of care; details of assessments, reassessments, consultations, investigation results, operative and other procedures, and the care provided; transfer details when the patient is transferred to another hospital; a copy of the discharge summary; and, in case of death, a copy of the cause-of-death certificate. Care providers have access to the current and past medical record.

{HOSPITAL} does not close a record that is missing a discharge-summary copy, a required transfer note, or a cause-of-death certificate copy after a death."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Filing a record that has no reason for admission, diagnosis or plan of care.
2. Omitting assessments, reassessments, consultations, investigation results, operative or other procedure notes, or details of care provided.
3. Transferring a patient to another hospital without recording the transfer details in the medical record.
4. Closing a discharged patient's record without a copy of the discharge summary.
5. Closing a deceased patient's record without a copy of the cause-of-death certificate.
6. Denying a treating care provider access to the current or past medical record needed for care.

Staff who find a missing continuity item report it the same shift to the {D('treating doctor')} and the {D('Medical Records Officer')}."""

PROCEDURE_STEPS = [
f"""5.1 Reasons for admission, diagnosis and plan of care

The medical record contains information regarding reasons for admission, diagnosis and plan of care.

The treating doctor records the reason for admission (or the presenting problem for an ambulatory visit), the working or confirmed diagnosis, and the plan of care. AAC.3 owns how assessment and planning are done. This step owns that those three items are present in the record and can be found without reconstructing the episode from memory.

The {D('Medical Records Officer')} checks presence of these items at filing after discharge or death.""",

f"""5.2 Assessments, investigations, procedures and care provided

The medical record contains the details of assessments, reassessments, consultations, results of investigations, operative and other procedures, and the details of the care provided.

Treating doctors and nurses record:

- initial assessment and each reassessment (AAC.3);
- consultations requested and the consultant's opinion;
- investigation results (filed or electronically linked — AAC.4/AAC.5 own the reports);
- operative notes and other procedure notes (COP owns the clinical method);
- the care actually provided, including nursing care.

A gap in this chain (for example a procedure with no note, or an investigation with no result in the record) is treated as an incomplete record and is completed before the record is closed.""",

f"""5.3 Transfer to another hospital — details in the record

When a patient is transferred to another hospital, the medical record contains the details of the transfer.

Details include: reason for transfer, receiving organisation, date and time of transfer, clinical condition at transfer, documents sent with the patient, and the name of the transferring doctor. AAC.2 owns the transfer-out decision and safety criteria. This step owns that those details are in this hospital's record.

A copy of the transfer note remains in the record after the patient has left.""",

f"""5.4 Copy of the discharge summary in the record

The medical record contains a copy of the discharge summary.

AAC.8 owns the discharge summary given to the patient (including patients leaving against medical advice). This step owns that a copy — paper or electronic — is filed in the medical record before the record is closed.

The {D('Medical Records Officer')} does not file a discharged patient's record as complete until the discharge-summary copy is present.""",

f"""5.5 Cause-of-death certificate copy in case of death

In case of death, the medical record contains a copy of the cause-of-death certificate.

The treating doctor (or the doctor who certifies death) ensures a copy of the cause-of-death certificate is filed in the record. AAC.8 owns the death-summary content given to the family. This step owns the certificate copy in the record.

The {D('Medical Records Officer')} does not file a deceased patient's record as complete until the cause-of-death certificate copy is present.""",

f"""5.6 Care providers' access to current and past medical records

Care providers have access to current and past medical records.

A treating doctor or nurse responsible for the patient can obtain the current record and previous-episode records needed for care, during working hours and after hours. The {D('Medical Records Officer')} (day) and the {D('nursing supervisor on duty')} (after hours) know how to retrieve a record.

IMS.4 owns confidentiality, security and the disclosure gate. Access under this step is for care providers who need the record to care for the patient — not open browsing. After-hours retrieval is logged.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for continuity items being present in every closed record.

Treating doctors
- Record admission reason, diagnosis, plan, assessments, procedures and care given.
- File transfer notes, discharge-summary copies and cause-of-death certificate copies.

Nurses
- Record nursing assessments and care provided.
- Support after-hours retrieval for treating care providers.

Medical Records Officer (or the person carrying that role)
- Checks presence of continuity items before a record is closed.
- Enables care-provider access to current and past records.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Feeds missing-item rates to IMS.6 review."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Sample of closed records: admission reason, diagnosis and plan present.
- Sample: assessments, investigations, procedure notes and care details present.
- All transfers-out in the period: transfer details in the record.
- All discharges in the sample: discharge-summary copy present.
- All deaths in the period: cause-of-death certificate copy present.
- After-hours retrieval log in use.

Root-cause analysis is required when a closed record is missing a discharge-summary copy or a cause-of-death certificate copy.

This policy is reviewed {D('annually')}, and sooner when the discharge or death-certification process changes."""

TRAINING_ACKNOWLEDGEMENT = f"""Treating doctors, nurses and the Medical Records Officer are trained on this policy at induction and {D('once a year')} after that. Training covers the six continuity items, the discharge-summary copy, the cause-of-death certificate copy, and after-hours access.

Staff acknowledgement

I have read this Medical Record Reflects Continuity of Care policy of {HOSPITAL}. I understand the six continuity items, including the discharge-summary copy and the cause-of-death certificate copy, and how care providers obtain current and past records.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The Medical Records Officer holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("IMS/POL/03"),
    version=VERSION,
    prepared_by=D("Medical Records Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Information Management System chapter, standard IMS.3.
- Internal documents of {HOSPITAL}: medical-record completeness checklist (continuity items); transfer-note copy; discharge-summary copy; cause-of-death certificate copy; after-hours retrieval log.
- Cross-referenced policies: AAC.2 (transfer-out); AAC.3 (assessment and plan); AAC.7 (handover); AAC.8 (discharge summary and death summary); COP (operative and procedure notes)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Medical Records Officer and the Quality Coordinator.

Copies issued to: all clinical departments; nursing administration; records office.

The current version is available to all staff at the {D('records-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
IMS — Information Management System (NABH SHCO chapter 10)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_ims_disclaimer()

OE_MAPPING = [
    {
        "oe_code": "IMS.3.a",
        "requirement": "The medical record contains information regarding reasons for admission, diagnosis and plan of care.",
        "steps": "Statement of intent; Section 3; 5.1 Reasons for admission, diagnosis and plan of care; Section 4 item 1",
        "responsible": "Treating doctors (record); Medical Records Officer (check at filing)",
        "records": [
            "Medical record with reason for admission, diagnosis and plan of care present.",
            "Filing checklist confirming these three items.",
            "Quarterly audit sample of presence.",
        ],
    },
    {
        "oe_code": "IMS.3.b",
        "requirement": "The medical record contains the details of assessments, reassessments, consultations, results of investigations, operative and other procedures, and the details of the care provided.",
        "steps": "Section 3; 5.2 Assessments, investigations, procedures and care provided; Section 4 item 2",
        "responsible": "Treating doctors and nurses (record); Medical Records Officer (completeness check)",
        "records": [
            "Record containing assessments, consultations, investigation results, procedure notes and care details.",
            "Gap list for any missing item before record closure.",
            "Quarterly audit sample of continuity-chain completeness.",
        ],
    },
    {
        "oe_code": "IMS.3.c",
        "requirement": "When a patient is transferred to another hospital, the medical record contains the details of the transfer.",
        "steps": "Section 3; 5.3 Transfer to another hospital; Section 4 item 3",
        "responsible": "Treating doctors (write transfer details); Medical Records Officer (file copy)",
        "records": [
            "Transfer note in the record for every transfer-out (reason, receiving organisation, time, condition, documents sent).",
            "Copy retained after the patient has left.",
            "Period list of transfers-out matched to records.",
        ],
    },
    {
        "oe_code": "IMS.3.d",
        "requirement": "The medical record contains a copy of the discharge summary.",
        "steps": "Section 3; 5.4 Copy of the discharge summary in the record; Section 4 item 4",
        "responsible": "Treating doctors (prepare summary — AAC.8); Medical Records Officer (file copy)",
        "records": [
            "Discharge-summary copy in every discharged patient's record.",
            "Filing hold until the copy is present.",
            "Quarterly rate of records closed with a discharge-summary copy.",
        ],
    },
    {
        "oe_code": "IMS.3.e",
        "requirement": "In case of death, the medical record contains a copy of the cause-of-death certificate.",
        "steps": "Section 3; 5.5 Cause-of-death certificate copy; Section 4 item 5",
        "responsible": "Treating / certifying doctor (file copy); Medical Records Officer (check before closure)",
        "records": [
            "Cause-of-death certificate copy in every deceased patient's record.",
            "Filing hold until the copy is present.",
            "Period list of deaths matched to records with the copy.",
        ],
    },
    {
        "oe_code": "IMS.3.f",
        "requirement": "Care providers have access to current and past medical record.",
        "steps": "Section 3; 5.6 Care providers' access to current and past medical records; Section 4 item 6",
        "responsible": "Medical Records Officer (day retrieval); nursing supervisor on duty (after-hours retrieval)",
        "records": [
            "Written method for current and past-record retrieval, including after hours.",
            "After-hours retrieval log.",
            "Quarterly check that a treating care provider can obtain a past record when needed for care.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """IMS.3 v2 template test (2026-08-20). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: IMS.3.a–f PDF index 139. No asterisked OEs — whole standard is Tier 2. All six OEs covered including IMS.3.e cause-of-death certificate copy.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer accreditation-only plus data-protection forward-note.

BOUNDARIES: AAC.8 owns discharge-summary content; IMS.3.d owns the copy in the record. AAC.2/AAC.7 own transfer mechanics; IMS.3.c owns transfer details in the record. COP owns operative notes; IMS.3.b owns that they are in the record."""


def main() -> int:
    draft = {
        "standard_code": STANDARD_CODE,
        "chapter": CHAPTER,
        "oe_codes": OE_CODES,
        "policy_title": POLICY_TITLE,
        "purpose": PURPOSE,
        "scope": SCOPE,
        "policy_statement": POLICY_STATEMENT,
        "procedure_steps": PROCEDURE_STEPS,
        "responsibility": RESPONSIBILITY,
        "references_text": REFERENCES,
        "distribution": DISTRIBUTION,
        "abbreviations": ABBREVIATIONS,
        "disclaimer": DISCLAIMER,
        "oe_mapping": OE_MAPPING,
        "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
        "version": VERSION,
        "revision_history": REVISION_HISTORY,
        "status": "draft",
        "definitions": STATEMENT_OF_INTENT,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "ims_v2_adoptable_shape",
        "subtitle": "Continuity items in the record, including discharge-summary and cause-of-death copies.",
        "doc_no": D("IMS/POL/03"),
        "acknowledgement_note": "The Medical Records Officer holds signed acknowledgements.",
    }
    emit_pre_v2(
        draft,
        "ims3_v2_draft.json",
        "IMS.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
