# -*- coding: utf-8 -*-
"""HCO AAC.1 v2 — define and display healthcare services (HCO Full, 6th Edition).

Shape follows PRE/SHCO v2 adoptable-policy shape via pre_v2_common.
Wording from NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition
— AAC chapter (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices 65–66.
OCR source: policies/source/hco6_aac_ocr.txt.

Four OEs (a–d). Asterisk on AAC.1.c. No stop-work. Disclaimer accreditation-only.
Does NOT overwrite SHCO AAC builders or drafts.
"""
from __future__ import annotations

import sys

from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW
from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, document_control, emit_pre_v2

STANDARD_CODE = "AAC.1"
CHAPTER = "HCO"
OE_CODES = ["AAC.1.a", "AAC.1.b", "AAC.1.c", "AAC.1.d"]
POLICY_TITLE = "Defined and Displayed Healthcare Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO Full 6th Edition AAC.1 v2 draft: plain English, four steps, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Patients, families and referrers must know what this hospital provides — "
    "services defined with the community in mind, staffed and equipped, scoped by "
    "department, and displayed where people can read them."
)

PURPOSE = f"""This policy says how {HOSPITAL} defines the healthcare services it provides in consonance with community needs; ensures each defined clinical service has diagnostic and treatment capability with suitably qualified personnel for out-patient, in-patient, day-care and emergency cover; defines the scope of clinical services of each department; and prominently displays those defined clinical services.

The chapter intent is that patients are informed of the services provided, that the scope of each healthcare service including diagnostic and therapeutic services is well defined and available to patients and families, and that only patients the organisation can care for are admitted.

This policy owns the service definition and display. AAC.2 owns registration and admission. AAC.3 owns transfer and referral. AAC.6–AAC.9 own laboratory and imaging detail once those services are named here. PRE.1 owns the patient-rights display; this policy owns the clinical-services display.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every clinical and diagnostic department at {HOSPITAL}. It binds the Medical Superintendent, Heads of departments (broad speciality, super speciality and diagnostic), the Quality Coordinator, registration and front-office staff, and clinical staff who deliver or describe services.

It covers AAC.1.a–d: defining services with community needs; diagnostic and treatment capability with qualified personnel including day-care and emergency cover; department scope (including outsourced clinical and diagnostic services); and permanent bi-lingual display.

Boundaries:

- AAC.2 owns registration, admission and acceptance against the services defined here.
- AAC.6 and AAC.8 own laboratory and imaging service detail. This policy owns that those services appear in the department scope and display.
- PRE.1 owns the patient-rights display. This policy owns the clinical-services display.
- Outsourced services are named and known under this policy; the contract and quality oversight of those vendors sit with the owning clinical or diagnostic policy."""

POLICY_STATEMENT = f"""{HOSPITAL} defines the healthcare services it provides, in consonance with the needs of the community it serves. Each defined clinical service has diagnostic and treatment services with suitably qualified medical, nursing and paramedical personnel who provide out-patient, in-patient, day-care and emergency cover. The scope of clinical services of each department is defined. The defined clinical services are permanently and prominently displayed in at least two languages.

{HOSPITAL} does not claim a clinical service it cannot staff, diagnose for or treat, and does not leave the display out of date or unreadable."""

NON_NEGOTIABLES = f"""1. Do not claim a clinical service the hospital cannot provide with qualified personnel and diagnostic and treatment capability for the care settings that service covers.
2. Do not operate a department whose clinical scope has not been defined and approved by the Medical Superintendent.
3. Do not omit documentation of clinical or diagnostic services that are outsourced; staff must know what is outsourced.
4. Do not remove the clinical-services display from a location visible to patients and visitors, allow it to become temporary when a permanent display is required, or leave it in only one language.
5. Staff who find the displayed services differ from what is actually provided report it the same shift to the {D('Quality Coordinator')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Define healthcare services in consonance with community needs

The Medical Superintendent, with Heads of departments, defines the healthcare services {HOSPITAL} provides. Senior management owns the definition. Community needs are considered when planning new services — captured through {D('patient and family feedback, referral patterns, district disease-burden data, and changing disease patterns')}. Starting a new service on the hospital's own judgment is allowed; community need still informs the decision.

The defined services are recorded in the service directory of {HOSPITAL}. A service not in the directory is not claimed. The directory is reviewed {D('annually')} and whenever a service is added, suspended or withdrawn.""",

f"""5.2 Diagnostic and treatment capability with qualified personnel

Each defined clinical service (broad speciality and super speciality) has:

- diagnostic and treatment services appropriate to that clinical service;
- suitably qualified medical, nursing and paramedical staff for the patient's clinical needs;
- out-patient services, in-patient services, day-care where the service uses day-care, and emergency cover by the consultant(s).

Infrastructure for diagnostics and treatment follows regulatory requirements and professional-body guidance where available. The {D('Medical Superintendent')} ensures personnel qualifications are verified at appointment and kept current. Where a service limitation exists (for example no day-care for that speciality), the limitation is written in the department scope (section 5.3) and reflected in the display (section 5.4).""",

f"""5.3 Define scope of clinical services of each department

Each department — super speciality, broad speciality and diagnostic — has a written scope. Scope may be by inclusion or by exclusion relative to services practised in the department. Example content for a nephrology department could include biopsy, shunts, fistulas, haemodialysis and CAPD where those are practised.

All clinical and diagnostic outsourced services are documented. Staff know what is outsourced. That information is also available to patients through {D('the website, display boards and department brochures')} as the hospital chooses.

The Medical Superintendent approves each scope. The {D('Quality Coordinator')} holds the current set. Scopes are reviewed {D('annually')} and on any material change in capability.""",

f"""5.4 Prominent permanent bi-lingual display of defined clinical services

The display states the names of clinical and diagnostic departments of {HOSPITAL}. It is permanent (board, citizen's charter or equivalent; electronic display is allowed as a supplement or alternative where it remains permanently visible). It is placed where patients and visitors can see it — at least at {D('the main entrance and the registration area')}.

The display is at least bi-lingual: {D('the State language or the language spoken by the majority of people in the catchment')} and English. Brochures, standees and the website may supplement the permanent display; they do not replace it.

When a service is added or withdrawn, the display is updated within {D('seven working days')}. The {D('Quality Coordinator')} checks the display {D('quarterly')} against the service directory and records any mismatch for correction.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that healthcare services are defined, resourced and displayed.
- Approves the service directory and each department clinical scope.

Heads of departments
- Define and maintain the clinical scope of their department, including outsourced elements.
- Ensure diagnostic and treatment capability and qualified personnel for out-patient, in-patient, day-care and emergency cover as applicable.

Quality Coordinator
- Holds the service directory and department scope statements.
- Audits the permanent display {D('quarterly')}.

Registration / front-office staff
- Direct patients only to services listed in the current directory and display.

All clinical staff
- Report any mismatch between displayed and actual services the same shift."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Service directory is current and matches what is actually provided.
- Each listed clinical service has diagnostic and treatment capability and qualified personnel recorded, including day-care and emergency cover where applicable.
- Department scope statements exist, are approved, and document outsourced clinical and diagnostic services.
- Permanent bi-lingual display is legible, current and matches the service directory at every display point.

Root-cause analysis is required when the same service-display mismatch recurs within six months.

This policy is reviewed {D('annually')}, and sooner when services are added, suspended or withdrawn."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff are informed of this policy at induction and {D('once a year')} after that. Training covers the service directory, department scopes, outsourced services, how to check the display, and how to report a mismatch.

Staff acknowledgement

I have read this Defined and Displayed Healthcare Services policy of {HOSPITAL}. I know where the service directory and permanent display are, and I will report any mismatch the same shift.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/01"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care (AAC), standard AAC.1.
- Internal documents of {HOSPITAL}: service directory; department clinical scope statements; outsourced-services list; personnel qualification records; display maintenance log."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: registration; every clinical and diagnostic department; out-patient; emergency; day-care; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH Hospitals chapter)
CAPA — corrective and preventive action
CAPD — continuous ambulatory peritoneal dialysis
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OPD — out-patient department"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.1.a",
        "requirement": "The healthcare services being provided are defined and are in consonance with the needs of the community.",
        "steps": "Section 3; 5.1 Define healthcare services in consonance with community needs; Section 4 item 1",
        "responsible": "Medical Superintendent (approve); Heads of departments (define); Quality Coordinator (hold directory)",
        "records": [
            "Service directory listing every healthcare service provided.",
            "Evidence that community needs informed service planning (feedback, referral, disease-burden or similar).",
            "Minutes or record of annual review of the service directory.",
        ],
    },
    {
        "oe_code": "AAC.1.b",
        "requirement": "Each defined clinical service shall have diagnostic and treatment services with suitably qualified personnel who provide out-patient, in-patient, daycare and emergency cover.",
        "steps": "Section 3; 5.2 Diagnostic and treatment capability with qualified personnel; Section 4 item 1",
        "responsible": "Heads of departments (ensure capability); Medical Superintendent (verify qualifications)",
        "records": [
            "Service directory entry for each clinical service showing diagnostic capability, treatment capability and personnel.",
            "Personnel qualification and verification records for medical, nursing and paramedical staff per service.",
            "Record of out-patient, in-patient, day-care and emergency cover arrangements for each defined clinical service.",
            "Record of any service limitation and the defined referral pathway.",
        ],
    },
    {
        "oe_code": "AAC.1.c",
        "requirement": "Scope of the clinical services of each department is defined.",
        "steps": "Section 3; 5.3 Define scope of clinical services of each department; Section 4 items 2–3",
        "responsible": "Heads of departments (write scope); Medical Superintendent (approve); Quality Coordinator (hold)",
        "records": [
            "Written clinical scope statement for each department (super speciality, broad speciality and diagnostic), approved and dated.",
            "Documented list of clinical and diagnostic outsourced services known to staff.",
            "Record of annual or change-triggered scope review.",
            "Brochure or equivalent detailing department scope where the hospital uses one.",
        ],
    },
    {
        "oe_code": "AAC.1.d",
        "requirement": "The organisation's defined clinical services are prominently displayed.",
        "steps": "Section 3; 5.4 Prominent permanent bi-lingual display of defined clinical services; Section 4 item 4",
        "responsible": "Quality Coordinator (maintain display); registration staff (direct patients per directory)",
        "records": [
            "Photographs or records of the permanent display at each mandated location.",
            "Evidence the display is at least bi-lingual (State/majority language and English).",
            "Quarterly audit log comparing display against the service directory.",
            "Record of display update when services changed, with date of update.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.1 v2 (2026-08-20). HCO Full Accreditation, NABH Hospitals 6th Edition.
PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. OCR: policies/source/hco6_aac_ocr.txt (PDF indices 65–66).

OE COUNT: 4 (a–d). Asterisked: AAC.1.c only (Tier 1 depth). AAC.1.a, AAC.1.b, AAC.1.d are Commitment without asterisk (Tier 2 depth).

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only (HCO 6th Edition). chapter=HCO, standard_code=AAC.1, doc_no HCO/AAC/POL/01.

HCO-SPECIFIC (not SHCO): day-care explicitly in AAC.1.b; permanent bi-lingual display in AAC.1.d; outsourced clinical/diagnostic services documented in AAC.1.c interpretation.

FLAG: none — OE wording clear after OCR clean-up (In-patlent→in-patient; GH cone chrome noise ignored)."""


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
        "prepared_by": D("Quality Coordinator"),
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "HCO Full Accreditation, 6th Edition — defined and displayed healthcare services.",
        "doc_no": D("HCO/AAC/POL/01"),
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": "",
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.1",
    }
    emit_pre_v2(
        draft,
        "hco_aac1_v2_draft.json",
        "HCO.AAC.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
        drafts_dir=HCO_DRAFTS,
        preview_dir=HCO_PREVIEW,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
