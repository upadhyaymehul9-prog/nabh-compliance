# -*- coding: utf-8 -*-
"""HRM.8 v2 — credentialing and privileging of nursing professionals.

Shape follows PRE v2 adoptable-policy shape. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 132.
Chapter intent: PDF index 130.

HAS stop-work section. Four OEs mapped to four What-we-do subsections.
Disclaimer P2 names Indian Nursing Council Act, 1947 and State Nursing Council.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.8"
CHAPTER = "HRM"
OE_CODES = ["HRM.8.a", "HRM.8.b", "HRM.8.c", "HRM.8.d"]
POLICY_TITLE = (
    "Credentialing and Privileging of Nursing Professionals Permitted to Provide "
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
    "Nursing professionals permitted to provide patient care without supervision are "
    "identified, credentialed, privileged and known to the departments they serve — "
    "so that unsupervised nursing care is given only by those qualified and authorised."
)

PURPOSE = f"""This policy describes how {HOSPITAL} credentials and privileges nursing professionals who are permitted by law, regulation and the organisation to provide patient care without supervision.

It covers four elements: identifying those nursing professionals; verifying and documenting their education, registration, training and experience with periodic updates; granting privileges consonant with qualification, training, experience and registration; and ensuring requisite services are known to the nurses and to departments/units.

Boundaries: HRM.6 owns the staff personal file. This policy owns the nursing credentialing and privileging process and register. HRM.7 owns medical credentialing; HRM.9 owns para-clinical credentialing. COP.4.b uses credentialing outcomes when assigning a nurse to a patient; it does not restate this method.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every nursing professional at {HOSPITAL} who provides patient care without supervision — staff nurses, nursing supervisors, ward in-charges and any nurse whose clinical actions do not require direct physician supervision for the privilege granted.

It covers the four elements HRM.8.a–d. It does not cover medical credentialing (HRM.7), para-clinical credentialing (HRM.9), personal files (HRM.6), or nurse-to-patient assignment (COP.4.b).

Boundaries with other policies of {HOSPITAL}:

- HRM.6 owns the personal file. This policy owns the nursing credentialing file, privileging register and privilege letter.
- HRM.7 owns medical credentialing. This policy is specific to nursing professionals.
- COP.4.b assigns a nurse to a patient using verification from this credentialing process.
- COP.8 owns age-specific nursing competency requirements; this policy verifies the underlying qualification and registration."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies nursing staff permitted by law, regulation and the organisation to provide patient care without supervision. Their education, registration, training and experience are verified, documented and updated periodically. Privileges are granted in consonance with their qualification, training, experience and registration. The requisite services they provide are known to them and to the departments/units of the organisation.

A nursing professional without completed credentialing and privileging does not provide unsupervised patient care at {HOSPITAL}."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Permitting a nursing professional to provide unsupervised patient care who is not listed in the nursing privileging register.
2. Granting nursing privileges beyond the professional's verified qualification, training, experience or current registration with the Indian Nursing Council and the applicable State Nursing Council.
3. Continuing unsupervised nursing practice when registration has lapsed without suspension from the privileging register.
4. Assigning a nurse to a ward or unit whose scope is not reflected in the privilege letter and the unit service list.
5. Allowing a nurse to perform procedures (for example IV cannulation, medication administration, wound care at an advanced level) not listed in the privilege letter.

Staff who cannot confirm completed credentialing and privileging do not permit unsupervised nursing care. They report to the {D('Nursing Superintendent')} or {D('HR Manager')} immediately."""

PROCEDURE_STEPS = [
f"""5.1 Identify nursing staff permitted for unsupervised patient care

Nursing staff permitted by law, regulation and the organisation to provide patient care without supervision are identified.

{HOSPITAL} maintains a Credentialing and Privileging SOP for nursing professionals. The SOP defines which categories of nurse may practise independently at this hospital — {D('registered nurses with completed general nursing and midwifery or B.Sc. Nursing, nursing supervisors, and ward in-charges with defined scope')}.

The {D('HR Manager')}, in consultation with the {D('Nursing Superintendent')}, maintains the nursing privileging register listing every independently practising nurse with:

- name and employee ID;
- Indian Nursing Council registration number and applicable State Nursing Council registration number;
- qualification (GNM, B.Sc. Nursing, Post Basic B.Sc. Nursing or equivalent);
- date of initial credentialing and date of last re-credentialing;
- specific nursing privileges granted and any restrictions.

The register is available to ward in-charges and department heads. A current extract is displayed at {D('each nursing station')} so staff know who is authorised for unsupervised nursing care.""",

f"""5.2 Verify education, registration, training and experience — document and update

The education, registration, training, experience and other information of nursing staff are identified, verified, documented and updated periodically.

At credentialing (initial appointment or privilege renewal), the {D('HR Manager')} collects and verifies:

- nursing diploma or degree certificates (primary source or certified copy verified with the institution or Indian Nursing Council);
- Indian Nursing Council registration certificate and applicable State Nursing Council registration;
- post-basic speciality training certificates where applicable;
- experience letters from previous employers;
- continuing nursing education records.

Verification is documented in the credentialing file with date, source contacted and verifying officer. Registration renewal dates are tracked; re-verification begins {D('sixty days')} before expiry.

Re-credentialing is conducted {D('every two years')} or sooner when scope of practice changes, registration is renewed, or a significant clinical event requires review.""",

f"""5.3 Grant privileges consonant with qualification, training, experience and registration

Nursing staff are granted privileges in consonance with their qualification, training, experience and registration.

The {D('Credentialing Committee')} — chaired by the {D('Nursing Superintendent')} with the {D('HR Manager')} and {D('Medical Superintendent')} — reviews each credentialing application and grants privileges by written privilege letter. The letter specifies:

- nursing procedures and care activities the nurse may perform independently;
- patient categories (adult, paediatric, maternity, emergency) where applicable;
- ward or unit assignment authority if granted;
- any restrictions or supervision requirements;
- validity period (maximum {D('two years')}).

Privileges not supported by verified credentials are not granted. A nurse whose State Nursing Council or Indian Nursing Council registration lapses is suspended from the register pending renewal verification.

Privilege letters are filed in the credentialing file and a copy is held by the nurse and the ward in-charge.""",

f"""5.4 Requisite services known to nursing staff and departments/units

The requisite services to be provided by the nursing staff are known to them as well as the various departments/units of the organisation.

Each privilege letter is cross-referenced to the service directory (AAC.1) and the ward or unit scope. The ward in-charge confirms that the nurse's privileges match the services the unit provides.

At each unit induction or when a new nurse joins a ward, the ward in-charge briefs the nurse on:

- nursing care standards and procedures for the unit;
- medication administration and documentation requirements;
- escalation pathways to the treating doctor;
- handover and shift-reporting requirements;
- infection-control and safety practices for the unit.

The briefing is recorded and filed in the credentialing file. Ward in-charges maintain a current list of credentialed nurses for their unit, matched to the central privileging register {D('quarterly')}.""",
]

STOP_WORK = f"""Any staff member who cannot confirm that a nursing professional has completed credentialing and privileging:

1. Does not permit that nurse to provide unsupervised patient care — including independent medication administration, procedures or ward supervision beyond their verified privileges.
2. Ensures patient care continues under another credentialed nurse or under supervised care as clinically appropriate.
3. Reports to the {D('Nursing Superintendent')} or {D('HR Manager')} immediately — the same shift.

For a nurse whose State Nursing Council or Indian Nursing Council registration has lapsed:

1. Suspends the nurse from the privileging register pending verification.
2. Does not assign unsupervised nursing duties until registration is confirmed current.
3. Notifies the {D('Nursing Superintendent')} the same working day.

No approval is needed to invoke stop-work. Patient safety and statutory registration requirements override convenience."""

RESPONSIBILITY = f"""Nursing Superintendent
- Chairs the Credentialing Committee for nursing; accountable for the nursing privileging register.
- Suspends or restores privileges based on committee recommendation.

HR Manager
- Collects and verifies nursing credentials; maintains credentialing files and the privileging register.
- Tracks registration renewal dates and initiates re-credentialing.

Credentialing Committee
- Reviews applications and grants, restricts or denies nursing privileges by written decision.

Ward in-charges / unit nursing leads
- Confirm privileges match unit scope; brief new nurses; maintain unit nurse lists.

Medical Superintendent
- Participates in Credentialing Committee for governance oversight.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when credentialing gaps or lapsed registrations recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Nursing privileging register is current — every unsupervised nurse is listed.
- Sample credentialing files checked for primary-source verification.
- Registration renewal dates — no nurse practising with lapsed registration.
- Privilege letters within validity period.
- Unit nurse lists match the central register.
- Stop-work invocations and their outcomes.

Root-cause analysis is required when an uncredentialed or unprivileged nurse is found providing unsupervised care, or when registration lapses are detected after the fact.

This policy is reviewed {D('annually')}, and sooner when Indian Nursing Council or State Nursing Council requirements change."""

TRAINING_ACKNOWLEDGEMENT = f"""The Nursing Superintendent, HR Manager, ward in-charges and nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers the nursing privileging register, stop-work authority and how to verify a nurse's credentials.

Staff acknowledgement

I have read this Nursing Professionals Credentialing and Privileging policy of {HOSPITAL}. I understand the privileging register, stop-work authority and that unsupervised nursing care requires completed credentialing.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The HR Manager holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/08"),
    version=VERSION,
    prepared_by=D("HR Manager"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.8.
- Indian Nursing Council Act, 1947 — registration and practice of nursing professionals.
- Applicable State Nursing Council registration requirements for nursing professionals.
- Internal documents of {HOSPITAL}: nursing privileging register; nursing credentialing files; privilege letters; Credentialing Committee minutes."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Nursing Superintendent, HR Manager and Quality Coordinator.

Copies issued to: all nursing stations; nursing administration; HR office; clinical departments.

The current version is available to all staff at the {D('nursing administration policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
GNM — General Nursing and Midwifery
HRM — Human Resource Management (NABH SHCO chapter)
INC — Indian Nursing Council
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations
SNC — State Nursing Council"""

STATUTE_CLAUSE = (
    "the Indian Nursing Council Act, 1947 and the applicable State Nursing Council "
    "registration requirements for nursing professionals"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "HRM.8.a",
        "requirement": "Nursing staff permitted by law, regulation and the organisation to provide patient care without supervision are identified.",
        "steps": "Statement of intent; Section 3; 5.1 Identify nursing staff; Section 4 item 1",
        "responsible": "HR Manager (maintain register); Nursing Superintendent (approve categories)",
        "records": [
            "Credentialing and Privileging SOP for nursing professionals.",
            "Nursing privileging register with INC and SNC registration numbers.",
            "Nursing station display or extract of credentialed nurses.",
            "Quarterly audit sample showing register matches practising nurses.",
        ],
    },
    {
        "oe_code": "HRM.8.b",
        "requirement": "The education, registration, training, experience and other information of nursing staff are identified, verified, documented and updated periodically.",
        "steps": "Section 3; 5.2 Verify education, registration, training and experience; Section 4 items 3, 4",
        "responsible": "HR Manager (collect and verify); Credentialing Committee (review at re-credentialing)",
        "records": [
            "Nursing credentialing file with primary-source verification records.",
            "INC and State Nursing Council registration certificates on file.",
            "Registration renewal tracking log with re-verification dates.",
            "Re-credentialing records at the defined interval.",
        ],
    },
    {
        "oe_code": "HRM.8.c",
        "requirement": "Nursing staff are granted privileges in consonance with their qualification, training, experience and registration.",
        "steps": "Section 3; 5.3 Grant privileges; Section 4 items 2, 4, 5; Section 6 (stop-work)",
        "responsible": "Credentialing Committee (grant privileges); Nursing Superintendent (suspend on lapse)",
        "records": [
            "Written nursing privilege letters specifying procedures, restrictions and validity period.",
            "Credentialing Committee minutes recording grant, restriction or denial.",
            "Suspension records for lapsed registration pending renewal.",
            "Stop-work invocation and outcome records.",
        ],
    },
    {
        "oe_code": "HRM.8.d",
        "requirement": "The requisite services to be provided by the nursing staff are known to them as well as the various departments/units of the organisation.",
        "steps": "Section 3; 5.4 Requisite services known to nursing staff and departments",
        "responsible": "Ward in-charges (brief nurses and maintain unit lists); HR Manager (cross-reference to service directory)",
        "records": [
            "Privilege letters cross-referenced to service directory and unit scope.",
            "Unit induction or joining briefing records for each nurse.",
            "Unit nurse list matched to central register quarterly.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.8 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "There is a process for credentialing and privileging of nursing professionals, permitted to provide patient care without supervision." HRM.8.a–d PDF index 132. No asterisked OEs. HRM.8.a and HRM.8.c are Core; HRM.8.b and HRM.8.d are Commitment.

SHAPE: Four What-we-do subsections (5.1–5.4). Stop-work YES (no unsupervised care without credentialing/privileging). Disclaimer names Indian Nursing Council Act 1947 and State Nursing Council. Workforce roles. Distinct from HRM.7 (medical/NMC)."""


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
        "subtitle": "Credentialing and privileging nursing professionals for unsupervised care.",
        "doc_no": D("HRM/POL/08"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "hrm8_v2_draft.json",
        "HRM.8_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
