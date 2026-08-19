# -*- coding: utf-8 -*-
"""AAC.1 v2 — defined healthcare services.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.1 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 56.
No stop-work. Disclaimer P2 names CEA 2010 only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.1"
CHAPTER = "AAC"
OE_CODES = ["AAC.1.a", "AAC.1.b", "AAC.1.c", "AAC.1.d"]
POLICY_TITLE = "Defined Healthcare Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, four steps, no stop-work, CEA P2.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation defines and displays the healthcare services that it provides — "
    "so that patients, families and referrers know what is available and what is not."
)

PURPOSE = f"""This policy says how {HOSPITAL} defines the healthcare services it provides, ensures each service has diagnostic and treatment capability with suitably qualified personnel, defines the scope of each department, and prominently displays those services.

The chapter intent is that the organisation's defined healthcare services are clear, resourced and displayed so that patients receive only what the hospital can actually deliver.

This policy owns the service definition. AAC.2 owns registration, admission and transfer. AAC.3 owns assessment and reassessment. PRE.1 owns the patient-rights display. The service directory referred to here is the hospital's own list, not a NABH template.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default and must be filled before this document is signed."""

SCOPE = f"""This policy applies to every department and service at {HOSPITAL}. It binds the Medical Superintendent, Head of each department, the Quality Coordinator and all clinical staff.

It covers the four elements AAC.1.a–d: defining services in consonance with community needs, ensuring diagnostic and treatment services with qualified personnel across out-patient, in-patient and emergency cover, defining departmental scope, and prominent display.

Boundaries:

- AAC.2 owns registration, admission, transfer in/out and bed-management. This policy owns what services exist for AAC.2 to admit patients into.
- AAC.4/AAC.5 own laboratory and imaging services detail. This policy owns that those services are named in the service directory.
- PRE.1 owns the patient-rights display board. This policy owns the service-directory display.
- PSQ.2 owns quality indicators. This policy owns the definition from which indicators are selected."""

POLICY_STATEMENT = f"""{HOSPITAL} defines the healthcare services it provides, in consonance with the needs of the community it serves. Each defined service has diagnostic and treatment capability with suitably qualified personnel providing out-patient, in-patient and emergency cover as applicable. The scope of each department is defined. The defined services are prominently displayed.

{HOSPITAL} does not claim a service it cannot staff, equip or sustain, and does not rely on a display board no patient can read."""

NON_NEGOTIABLES = f"""1. Do not claim a healthcare service the hospital cannot provide with qualified personnel, diagnostic capability and treatment capability.
2. Do not operate a department whose scope has not been defined and approved by the Medical Superintendent.
3. Do not remove the service display from a location where patients and visitors can see it, or allow it to become out of date.
4. Staff who find the displayed services differ from what is actually provided report it the same shift to the {D('Quality Coordinator')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Define healthcare services in consonance with community needs

The Medical Superintendent, in consultation with the Heads of departments, defines the healthcare services {HOSPITAL} provides. The definition considers the needs of the community the hospital serves — {D('the catchment population, referral patterns, burden-of-disease data from the district health office, and feedback from patients and local practitioners')}.

The defined services are recorded in the service directory of {HOSPITAL}. That directory is the single source of truth; a service not in it is not claimed. The directory is reviewed {D('annually')} and whenever a service is added, suspended or withdrawn.""",

f"""5.2 Diagnostic, treatment capability and qualified personnel

Each service listed in the service directory has:

- diagnostic capability appropriate to the service (laboratory, imaging, clinical examination or a defined referral pathway where in-house capability is not provided);
- treatment capability (equipment, consumables, drugs, facilities);
- suitably qualified personnel who provide out-patient, in-patient and emergency cover as applicable to that service.

Where a service provides only out-patient cover and refers in-patient or emergency cases, that limitation is recorded in the department scope (section 5.3) and in the display (section 5.4). The {D('Medical Superintendent')} ensures personnel qualifications are verified at appointment and kept current.""",

f"""5.3 Define scope of each department

Each department has a written scope statement approved by the Medical Superintendent. The scope includes:

- services and procedures the department provides;
- services and procedures the department does not provide and where those patients are referred;
- operating hours, including emergency cover arrangements;
- minimum staffing and qualification requirements.

The scope is reviewed {D('annually')} and whenever there is a material change in capability. Scope statements are held by the {D('Quality Coordinator')} and are available to all staff in the department.""",

f"""5.4 Prominent display of defined services

The defined healthcare services are prominently displayed at {D('the main entrance, the registration area, and each out-patient waiting area')} in {D('Hindi and English')} (and any other language the community commonly uses).

The display is legible, current and matches the service directory. When a service is added or withdrawn, the display is updated within {D('seven working days')}. The {D('Quality Coordinator')} checks the display {D('quarterly')} against the current service directory and records any discrepancy for correction.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that healthcare services are defined, resourced and displayed.
- Approves the service directory and each department scope.

Heads of departments
- Define and maintain the scope of their department.
- Ensure diagnostic and treatment capability and qualified personnel for each service.

Quality Coordinator
- Holds the service directory and department scope statements.
- Audits the display {D('quarterly')} (see monitoring section).

Registration / front-office staff
- Direct patients only to services listed in the current directory.

All clinical staff
- Report any mismatch between displayed and actual services the same shift."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Service directory is current, complete and matches what is actually provided.
- Each listed service has diagnostic, treatment capability and qualified personnel recorded.
- Department scope statements exist, are approved and are current.
- Display is legible, current and matches the service directory at every display point.
- Any mismatch between displayed and actual services since the last audit.

Root-cause analysis is required when the same service-display mismatch recurs within six months.

This policy is reviewed {D('annually')}, and sooner when services are added, suspended or withdrawn."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff are informed of this policy at induction and {D('once a year')} after that. Training covers the service directory, how to check the display, and how to report a mismatch.

Staff acknowledgement

I have read this Defined Healthcare Services policy of {HOSPITAL}. I know where the service directory and display are, and I will report any mismatch the same shift.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/01')}
Issue number: {D('01')}
Version: {VERSION} (AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.1.
- Clinical Establishments (Registration and Regulation) Act, 2010 — registration requirements and display of services.
- Internal documents of {HOSPITAL}: service directory; department scope statements; personnel qualification records; display maintenance log."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: registration; every department; out-patient; emergency; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Clinical Establishments (Registration and Regulation) Act, 2010, "
    "insofar as the organisation registers and displays the healthcare services "
    "it provides under that Act or corresponding State legislation"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "AAC.1.a",
        "requirement": "The healthcare services being provided are defined and are in consonance with the needs of the community.",
        "steps": "Section 3; 5.1 Define healthcare services in consonance with community needs; Section 4 item 1",
        "responsible": "Medical Superintendent (approve); Heads of departments (define); Quality Coordinator (hold directory)",
        "records": [
            "Service directory listing every healthcare service provided.",
            "Evidence of community-need assessment (catchment, referral, burden-of-disease or feedback data).",
            "Minutes or record of annual review of the service directory.",
        ],
    },
    {
        "oe_code": "AAC.1.b",
        "requirement": "Each defined healthcare service should have diagnostic and treatment services with suitably qualified personnel who provide out-patient, in-patient and emergency cover.",
        "steps": "Section 3; 5.2 Diagnostic, treatment capability and qualified personnel; Section 4 item 1",
        "responsible": "Heads of departments (ensure capability); Medical Superintendent (verify qualifications)",
        "records": [
            "Service directory entry for each service showing diagnostic capability, treatment capability and personnel.",
            "Personnel qualification and verification records for each service.",
            "Record of any service limitation (e.g. OPD only) and the defined referral pathway.",
        ],
    },
    {
        "oe_code": "AAC.1.c",
        "requirement": "Scope of healthcare services of each department is defined.",
        "steps": "Section 3; 5.3 Define scope of each department; Section 4 item 2",
        "responsible": "Heads of departments (write scope); Medical Superintendent (approve); Quality Coordinator (hold)",
        "records": [
            "Written scope statement for each department, approved and dated.",
            "Record of annual or change-triggered scope review.",
            "List of services and procedures the department does and does not provide.",
        ],
    },
    {
        "oe_code": "AAC.1.d",
        "requirement": "The organisation's defined healthcare services are prominently displayed.",
        "steps": "Section 3; 5.4 Prominent display of defined services; Section 4 item 3",
        "responsible": "Quality Coordinator (maintain display); registration staff (direct patients per directory)",
        "records": [
            "Photographs or records of display at each mandated location.",
            "Quarterly audit log comparing display against service directory.",
            "Record of display update when services changed, with date of update.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.1 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. AAC.1.c asterisked. No stop-work. P2: CEA 2010 only. Four OEs, four What-we-do subsections."""


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
        "template_test": "aac_v2_adoptable_shape",
        "subtitle": "Defined healthcare services of the organisation.",
        "doc_no": D("AAC/POL/01"),
    }
    emit_pre_v2(
        draft,
        "aac1_v2_draft.json",
        "AAC.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
