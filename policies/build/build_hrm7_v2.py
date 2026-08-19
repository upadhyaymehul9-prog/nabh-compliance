# -*- coding: utf-8 -*-
"""HRM.7 v2 — credentialing and privileging of medical professionals.

Shape follows PRE v2 adoptable-policy shape. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 132.
Chapter intent: PDF index 130.

HAS stop-work section. Four OEs mapped to four What-we-do subsections.
Disclaimer P2 names National Medical Commission Act, 2019 and State Medical Council.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.7"
CHAPTER = "HRM"
OE_CODES = ["HRM.7.a", "HRM.7.b", "HRM.7.c", "HRM.7.d"]
POLICY_TITLE = (
    "Credentialing and Privileging of Medical Professionals Permitted to Provide "
    "Patient Care Without Supervision"
)
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: adoptable shape, plain English, workforce roles, four steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Medical professionals permitted to provide patient care without supervision are "
    "identified, credentialed, privileged and known to the departments they serve — "
    "so that unsupervised care is given only by those qualified and authorised."
)

PURPOSE = f"""This policy describes how {HOSPITAL} credentials and privileges medical professionals who are permitted by law, regulation and the organisation to provide patient care without supervision.

It covers four elements: identifying those medical professionals; verifying and documenting their education, registration, training and experience with periodic updates; granting privileges consonant with qualification, training, experience and registration; and ensuring requisite services are known to the professionals and to departments/units.

Boundaries: HRM.6 owns the staff personal file that holds underlying qualification documents. This policy owns the credentialing and privileging process and register for medical professionals. HRM.8 and HRM.9 own parallel processes for nursing and para-clinical professionals respectively. AAC.1.b uses credentialing outcomes when assigning qualified personnel to services; it does not restate this method.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every medical professional at {HOSPITAL} who provides patient care without supervision — treating doctors, consultants, resident medical officers and any doctor whose orders or procedures do not require a supervising physician.

It covers the four elements HRM.7.a–d. It does not cover nursing credentialing (HRM.8), para-clinical credentialing (HRM.9), personal files (HRM.6), or the service directory (AAC.1).

Boundaries with other policies of {HOSPITAL}:

- HRM.6 owns the personal file. This policy owns the credentialing file, privileging register and privilege letter.
- HRM.8 owns nursing credentialing and privileging. This policy is specific to medical professionals.
- MOM.4 owns authorised medication prescribers. This policy credentials the doctor; MOM.4 lists who may write orders.
- COP.4.b assigns a nurse to a patient using verification from HRM credentialing; it does not restate the method."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies medical professionals permitted by law, regulation and the organisation to provide patient care without supervision. Their education, registration, training and experience are verified, documented and updated periodically. Privileges to admit and care for patients are granted in consonance with their qualification, training, experience and registration. The requisite services they provide are known to them and to the departments/units of the organisation.

A medical professional without completed credentialing and privileging does not provide unsupervised patient care at {HOSPITAL}."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Permitting a medical professional to provide unsupervised patient care who is not listed in the privileging register.
2. Granting clinical privileges beyond the professional's verified qualification, training, experience or current registration with the National Medical Commission or the applicable State Medical Council.
3. Continuing unsupervised practice when registration has lapsed without suspension from the privileging register.
4. Admitting or treating patients under privileges that have not been reviewed within {D('two years')}.
5. Assigning a doctor to a department or service whose scope is not reflected in the privilege letter and the department service list.

Staff who cannot confirm completed credentialing and privileging do not permit unsupervised patient care. They report to the {D('Medical Superintendent')} or {D('HR Manager')} immediately."""

PROCEDURE_STEPS = [
f"""5.1 Identify medical professionals permitted for unsupervised patient care

Medical professionals permitted by law, regulation and the organisation to provide patient care without supervision are identified.

{HOSPITAL} maintains a Credentialing and Privileging SOP for medical professionals. The SOP defines which categories of medical professional may practise independently at this hospital — {D('consultants, resident medical officers with completed basic registration, and visiting specialists on a defined privilege letter')}.

The {D('HR Manager')}, in consultation with the {D('Medical Superintendent')}, maintains the medical privileging register listing every independently practising medical professional with:

- name and employee or consultant ID;
- National Medical Commission registration number and State Medical Council registration number;
- qualification (degree and speciality);
- date of initial credentialing and date of last re-credentialing;
- specific privileges granted and any restrictions.

The register is available to department heads and nursing supervisors. A current extract is displayed in {D('each clinical department and at the nursing station')} so staff know who is authorised to provide unsupervised care.""",

f"""5.2 Verify education, registration, training and experience — document and update

The education, registration, training, experience and other information of medical professionals are identified, verified, documented and updated periodically.

At credentialing (initial appointment or privilege renewal), the {D('HR Manager')} collects and verifies:

- medical degree and speciality qualification certificates (primary source or certified copy verified with the university or board);
- National Medical Commission registration certificate and applicable State Medical Council registration;
- post-graduate training certificates and continuing medical education records;
- experience letters from previous employers for the relevant period;
- any malpractice or disciplinary history disclosed and checked.

Verification is documented in the credentialing file with date, source contacted and verifying officer. Registration renewal dates are tracked; re-verification begins {D('sixty days')} before expiry.

Re-credentialing is conducted {D('every two years')} or sooner when scope of practice changes, registration is renewed, or a significant clinical event requires review.""",

f"""5.3 Grant privileges consonant with qualification, training, experience and registration

Medical professionals are granted privileges to admit and care for patients in consonance with their qualification, training, experience and registration.

The {D('Credentialing Committee')} — chaired by the {D('Medical Superintendent')} with the {D('HR Manager')} and relevant department head — reviews each credentialing application and grants privileges by written privilege letter. The letter specifies:

- procedures and services the doctor may perform independently;
- patient categories (adult, paediatric, emergency) where applicable;
- admission authority if granted;
- any restrictions or supervision requirements;
- validity period (maximum {D('two years')}).

Privileges not supported by verified credentials are not granted. A doctor whose registration lapses is suspended from the register pending renewal verification.

Privilege letters are filed in the credentialing file and a copy is held by the doctor and the department head.""",

f"""5.4 Requisite services known to professionals and departments/units

The requisite services to be provided by the medical professionals are known to them as well as the various departments/units of the organisation.

Each privilege letter is cross-referenced to the service directory (AAC.1) and the department scope statement. The department head confirms that the doctor's privileges match the services the department claims to provide.

At each department induction or when a new doctor joins a unit, the department head briefs the doctor on:

- services and procedures the department provides and those referred elsewhere;
- on-call and emergency cover expectations;
- handover and consultation pathways;
- documentation requirements.

The briefing is recorded and filed in the credentialing file. Department heads maintain a current list of credentialed doctors for their unit, matched to the central privileging register {D('quarterly')}.""",
]

STOP_WORK = f"""Any staff member who cannot confirm that a medical professional has completed credentialing and privileging:

1. Does not permit that professional to provide unsupervised patient care — including writing independent orders, performing procedures or admitting patients.
2. Ensures patient care continues under another credentialed medical professional or under supervised care as clinically appropriate.
3. Reports to the {D('Medical Superintendent')} or {D('HR Manager')} immediately — the same shift.

For a doctor whose State Medical Council or National Medical Commission registration has lapsed:

1. Suspends the doctor from the privileging register pending verification.
2. Does not assign unsupervised clinical duties until registration is confirmed current.
3. Notifies the {D('Medical Superintendent')} the same working day.

No approval is needed to invoke stop-work. Patient safety and statutory registration requirements override convenience."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Chairs the Credentialing Committee; accountable for the privileging register.
- Suspends or restores privileges based on committee recommendation.

HR Manager
- Collects and verifies credentials; maintains credentialing files and the privileging register.
- Tracks registration renewal dates and initiates re-credentialing.

Credentialing Committee
- Reviews applications and grants, restricts or denies privileges by written decision.

Department heads
- Confirm privileges match department scope; brief new doctors; maintain unit doctor lists.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when credentialing gaps or lapsed registrations recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Privileging register is current — every unsupervised doctor is listed.
- Sample credentialing files checked for primary-source verification.
- Registration renewal dates — no doctor practising with lapsed registration.
- Privilege letters within validity period.
- Department doctor lists match the central register.
- Stop-work invocations and their outcomes.

Root-cause analysis is required when an uncredentialed or unprivileged doctor is found providing unsupervised care, or when registration lapses are detected after the fact.

This policy is reviewed {D('annually')}, and sooner when National Medical Commission or State Medical Council requirements change."""

TRAINING_ACKNOWLEDGEMENT = f"""The Medical Superintendent, HR Manager, department heads and nursing supervisors are trained on this policy at appointment and {D('once a year')} after that. Training covers the privileging register, stop-work authority and how to verify a doctor's credentials before assigning unsupervised care.

Staff acknowledgement

I have read this Medical Professionals Credentialing and Privileging policy of {HOSPITAL}. I understand the privileging register, stop-work authority and that unsupervised care requires completed credentialing.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The HR Manager holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/07"),
    version=VERSION,
    prepared_by=D("HR Manager"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.7.
- National Medical Commission Act, 2019 — registration and practice of medical practitioners.
- Applicable State Medical Council registration requirements for medical practitioners.
- Internal documents of {HOSPITAL}: medical privileging register; credentialing files; privilege letters; Credentialing Committee minutes."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the HR Manager and the Quality Coordinator.

Copies issued to: all clinical departments; nursing administration; emergency department; operation theatre; HR office.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
HRM — Human Resource Management (NABH SHCO chapter)
NMC — National Medical Commission
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations
SMC — State Medical Council"""

STATUTE_CLAUSE = (
    "the National Medical Commission Act, 2019 and the applicable State Medical Council "
    "registration requirements for medical practitioners"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "HRM.7.a",
        "requirement": "Medical professionals permitted by law, regulation and the organisation to provide patient care without supervision are identified.",
        "steps": "Statement of intent; Section 3; 5.1 Identify medical professionals; Section 4 item 1",
        "responsible": "HR Manager (maintain register); Medical Superintendent (approve categories)",
        "records": [
            "Credentialing and Privileging SOP for medical professionals.",
            "Medical privileging register with NMC and SMC registration numbers.",
            "Department display or extract of credentialed doctors.",
            "Quarterly audit sample showing register matches practising doctors.",
        ],
    },
    {
        "oe_code": "HRM.7.b",
        "requirement": "The education, registration, training, experience and other information of medical professionals are identified, verified, documented and updated periodically.",
        "steps": "Section 3; 5.2 Verify education, registration, training and experience; Section 4 items 3, 4",
        "responsible": "HR Manager (collect and verify); Credentialing Committee (review at re-credentialing)",
        "records": [
            "Credentialing file with primary-source verification records.",
            "NMC and State Medical Council registration certificates on file.",
            "Registration renewal tracking log with re-verification dates.",
            "Re-credentialing records at the defined interval.",
        ],
    },
    {
        "oe_code": "HRM.7.c",
        "requirement": "Medical professionals are granted privileges to admit and care for the patients in consonance with their qualification, training, experience and registration.",
        "steps": "Section 3; 5.3 Grant privileges; Section 4 items 2, 4, 5; Section 6 (stop-work)",
        "responsible": "Credentialing Committee (grant privileges); Medical Superintendent (suspend on lapse)",
        "records": [
            "Written privilege letters specifying procedures, restrictions and validity period.",
            "Credentialing Committee minutes recording grant, restriction or denial.",
            "Suspension records for lapsed registration pending renewal.",
            "Stop-work invocation and outcome records.",
        ],
    },
    {
        "oe_code": "HRM.7.d",
        "requirement": "The requisite services to be provided by the medical professionals are known to them as well as the various departments/units of the organisation.",
        "steps": "Section 3; 5.4 Requisite services known to professionals and departments",
        "responsible": "Department heads (brief doctors and maintain unit lists); HR Manager (cross-reference to service directory)",
        "records": [
            "Privilege letters cross-referenced to service directory and department scope.",
            "Department induction or joining briefing records for each doctor.",
            "Unit doctor list matched to central register quarterly.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.7 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "There is a process for credentialing and privileging of medical professionals, permitted to provide patient care without supervision." HRM.7.a–d PDF index 132. No asterisked OEs. HRM.7.a and HRM.7.c are Core; HRM.7.b and HRM.7.d are Commitment.

SHAPE: Four What-we-do subsections (5.1–5.4). Stop-work YES (no unsupervised care without credentialing/privileging). Disclaimer names NMC Act 2019 and State Medical Council. Workforce roles."""


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
        "subtitle": "Credentialing and privileging medical professionals for unsupervised care.",
        "doc_no": D("HRM/POL/07"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "hrm7_v2_draft.json",
        "HRM.7_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
