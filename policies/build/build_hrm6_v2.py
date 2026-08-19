# -*- coding: utf-8 -*-
"""HRM.6 v2 — documented personal information for each staff member.

Shape follows PRE v2 adoptable-policy shape. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 131.
Chapter intent: PDF index 130.

No stop-work section. Four OEs mapped to four What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.6"
CHAPTER = "HRM"
OE_CODES = ["HRM.6.a", "HRM.6.b", "HRM.6.c", "HRM.6.d"]
POLICY_TITLE = "Documented Personal Information for Each Staff Member"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: adoptable shape, plain English, workforce roles, four steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "There is documented personal information for each staff member — a personal file "
    "maintained for every person, kept confidential, and updated as qualifications, "
    "training and evaluations change."
)

PURPOSE = f"""This policy describes how {HOSPITAL} maintains a personal file for every staff member, keeps those files confidential, and ensures each file contains the personal information the standard requires.

It covers four elements: maintaining personal files for all staff with confidentiality ensured; file contents covering qualification, job description, proof of formal engagement, credential verification and health status; in-service training and education records; and results of all evaluations and remarks.

Boundaries: HRM.6 owns the staff personal file. General records management — how clinical and administrative records are created, stored, retained and destroyed — is IMS (not yet built). HRM.7–9 own credentialing and privileging for professionals who provide unsupervised patient care; this policy holds the underlying personal file those processes draw from.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every staff member at {HOSPITAL} — clinical, nursing, para-clinical, administrative and support — and to the {D('HR Manager')}, department heads who contribute evaluation records, the {D('Medical Superintendent')} and the Quality Coordinator.

It covers the four elements HRM.6.a–d name. It does not cover credentialing and privileging of medical, nursing or para-clinical professionals (HRM.7–9), general staff recruitment (HRM.1–2 when drafted), or the hospital-wide records-management system (IMS, not yet built).

Boundaries with other policies of {HOSPITAL}:

- IMS (not yet built) owns general records management. This policy owns the staff personal file.
- HRM.7–9 own credentialing and privileging registers and privilege letters. This policy owns the personal file that holds the underlying qualification and verification documents.
- ROM.2 owns the qualifications file for the person heading the organisation. HRM.6 owns personal files for all other staff.
- HIC.4 owns the confidential occupational health file for infection-control exposures. HRM.6 owns the general health-status record in the personal file."""

POLICY_STATEMENT = f"""{HOSPITAL} maintains a personal file for every staff member. The confidentiality of personal files is ensured.

Each personal file contains qualification, job description, proof of formal engagement, credential verification and health status. In-service training and education records are contained in the personal files. Personal files contain results of all evaluations and remarks.

{HOSPITAL} does not treat an appointment letter alone as a complete personal file, or a training attendance sheet kept only in a department drawer as an in-service record."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Employing or retaining a staff member without a personal file maintained by HR.
2. Storing personal files in an unsecured location or allowing access without authorisation and an access log.
3. Opening a personal file that lacks qualification proof, a signed job description, proof of formal engagement, credential verification and health status.
4. Completing an appraisal or evaluation without filing the signed result in the staff member's personal file within {D('ten working days')}.
5. Conducting in-service training without filing the attendance record or certificate in the staff member's personal file within {D('ten working days')}.

Staff who become aware of a missing or incomplete personal file report it to the {D('HR Manager')} the same working day."""

PROCEDURE_STEPS = [
f"""5.1 Personal files maintained for all staff — confidentiality ensured

{HOSPITAL} maintains a personal file for every staff member — permanent, contract, locum and part-time. Each file is assigned a unique personnel file number at joining.

Personal files are stored in a {D('locked cabinet in the HR office or a secured HR module in the hospital information system')}. Access is limited to authorised HR staff and the {D('Medical Superintendent')} for governance purposes. An access log records who opened each file, when and why.

Confidentiality is ensured by a signed confidentiality undertaking from every person who handles personal files. Personal information is not disclosed except as required by law, for credentialing (HRM.7–9), or with the staff member's written consent.

The {D('HR Manager')} maintains a master register of all personnel file numbers and verifies that every person on the payroll has a corresponding file {D('quarterly')}.""",

f"""5.2 Personal file contents — qualification, job description, engagement, credentials, health

Each personal file contains personal information regarding the staff member's:

- **Qualification** — certified copies of degrees, diplomas, registration certificates and any licence required for the role.
- **Job description** — the signed job description for the current role, including scope of work and reporting line.
- **Proof of formal engagement** — appointment letter or contract, date of joining, and any renewal or extension.
- **Verification of credentials** — evidence that qualifications and registrations were verified with the issuing body or council at joining (and on renewal where applicable).
- **Health status** — pre-employment health check report and periodic health check results as required by {HOSPITAL} policy (for example {D('annual health check for clinical staff')}).

A personnel file index at the front of each file lists every mandatory document and its date of filing. The {D('HR Manager')} uses this index during file audits.""",

f"""5.3 In-service training and education records in personal files

Records of in-service training and education are contained in the personal files.

For every training event the staff member attends — induction, mandatory refresher, skill update, external course — the personal file holds:

- training topic and date;
- duration and trainer or institution;
- attendance register entry or certificate of completion;
- competency assessment result where the training required return demonstration.

A dedicated training section within each personal file holds these records in chronological order. The {D('HR Manager')} maintains a central training register that mirrors individual file entries and allows a report on any staff member's training history within {D('one working day')}.

Mandatory training gaps identified during the register review are closed within {D('thirty days')} and recorded in the file.""",

f"""5.4 Evaluation results and remarks in personal files

Personal files contain results of all evaluations and remarks.

Every completed performance appraisal, probation review, commendation, disciplinary action, counselling note and improvement plan is filed in a chronological evaluation section within the personal file. Each document is signed by the appraiser, countersigned by the department head where applicable, and dated before filing.

The {D('HR Manager')} verifies annually that evaluation records are complete and that appraisals have been conducted at the frequency {HOSPITAL} defines — {D('annually for permanent staff and at probation completion for new appointees')}.

A summary sheet at the front of the evaluation section lists the date and outcome of every appraisal to date.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that every staff member has a complete personal file.
- May access personal files for governance and credentialing decisions.

HR Manager
- Creates and maintains personal files; ensures confidentiality and access control.
- Conducts quarterly file-completeness audits and annual evaluation-record reviews.
- Maintains the central training register.

Department heads
- Submit signed evaluation records and training attendance to HR within {D('ten working days')}.
- Notify HR when a staff member's role, qualification or registration changes.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA when file gaps recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Master register matches payroll headcount — every person has a file.
- Sample of personal files checked against the mandatory document index.
- Access log reviewed for unauthorised access.
- Training records in files match the central training register.
- Evaluation records are current and signed.

Root-cause analysis is required when more than {D('ten percent')} of sampled files lack a mandatory document, or when evaluation records are overdue for {D('two consecutive quarters')}.

This policy is reviewed {D('annually')}, and sooner when a staff member's file is found incomplete at credentialing (HRM.7–9) or when records-management requirements change."""

TRAINING_ACKNOWLEDGEMENT = f"""The HR Manager, department heads and the Quality Coordinator are briefed on this policy at appointment and {D('once a year')} after that. All staff are informed at induction that a personal file is maintained and that confidentiality is protected.

Staff acknowledgement

I have read this Documented Personal Information policy of {HOSPITAL}. I understand that a personal file is maintained for me and that its confidentiality is protected.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The HR Manager holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/06"),
    version=VERSION,
    prepared_by=D("HR Manager"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.6.
- Internal documents of {HOSPITAL}: personnel file index template; access log; central training register; evaluation summary sheet."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the HR Manager and the Quality Coordinator.

Copies issued to: HR office; department heads (procedure summary only — not personal files); quality office.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
HRM — Human Resource Management (NABH SHCO chapter)
IMS — Information Management System (NABH SHCO chapter; not yet built)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HRM.6.a",
        "requirement": "Personal files are maintained with respect to all staff, and their confidentiality is ensured.",
        "steps": "Statement of intent; Section 3; 5.1 Personal files maintained for all staff; Section 4 items 1–2",
        "responsible": "HR Manager (create and maintain files); Medical Superintendent (accountable)",
        "records": [
            "Master register of personnel file numbers matched to payroll headcount.",
            "Access log for personal file retrieval.",
            "Signed confidentiality undertaking from every person who handles personal files.",
            "Quarterly file-existence audit sample showing every staff member has a file.",
        ],
    },
    {
        "oe_code": "HRM.6.b",
        "requirement": "The personal files contain personal information regarding the staff's qualification, job description, proof of formal engagement, verification of credentials and health status.",
        "steps": "Section 3; 5.2 Personal file contents; Section 4 item 3",
        "responsible": "HR Manager (maintain file contents); department heads (submit documents at joining)",
        "records": [
            "Personnel file index listing mandatory documents and filing dates.",
            "Qualification certificates and registration proof on file.",
            "Signed job description and appointment letter or contract.",
            "Credential verification record from issuing body or council.",
            "Pre-employment and periodic health check reports.",
        ],
    },
    {
        "oe_code": "HRM.6.c",
        "requirement": "Records of in-service training and education are contained in the personal files.",
        "steps": "Section 3; 5.3 In-service training and education records; Section 4 item 5",
        "responsible": "HR Manager (maintain central register and file records); department heads (submit attendance within ten working days)",
        "records": [
            "Training section within each personal file with chronological records.",
            "Central training register mirroring individual file entries.",
            "Attendance registers or completion certificates for each training event.",
            "Competency assessment results where return demonstration was required.",
        ],
    },
    {
        "oe_code": "HRM.6.d",
        "requirement": "Personal files contain results of all evaluations and remarks.",
        "steps": "Section 3; 5.4 Evaluation results and remarks; Section 4 item 4",
        "responsible": "HR Manager (file and verify completeness); department heads (submit signed evaluations)",
        "records": [
            "Chronological evaluation section in each personal file.",
            "Signed appraisal forms with appraiser and department-head signatures.",
            "Evaluation summary sheet listing date and outcome of every appraisal.",
            "Annual completeness review record showing all evaluations are current.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.6 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "There is documented personal information for each staff member." HRM.6.a–d PDF index 131. No asterisked OEs. All Commitment level.

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only. Workforce roles (HR Manager, Medical Superintendent, Quality Coordinator). IMS boundary stated."""


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
        "template_test": "hrm_v2_adoptable_shape",
        "subtitle": "Personal files for every staff member, kept confidential and complete.",
        "doc_no": D("HRM/POL/06"),
    }
    emit_pre_v2(
        draft,
        "hrm6_v2_draft.json",
        "HRM.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
