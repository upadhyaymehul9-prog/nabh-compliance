# -*- coding: utf-8 -*-
"""AAC.5 v2 — imaging services.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.5 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 58–59.
No stop-work. Disclaimer P2 names AERP Rules 2004 and PC-PNDT Act 1994.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.5"
CHAPTER = "AAC"
OE_CODES = [
    "AAC.5.a", "AAC.5.b", "AAC.5.c", "AAC.5.d", "AAC.5.e",
    "AAC.5.f", "AAC.5.g", "AAC.5.h", "AAC.5.i",
]
POLICY_TITLE = "Imaging Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, nine steps, no stop-work, AERP/PC-PNDT P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Imaging services are provided as per the scope of services of the organisation "
    "and adhere to best practices — so that results are reliable, timely, safe and quality-assured."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides imaging services that comply with legal requirements, are commensurate with scope, have adequate infrastructure and human resources, deliver results in standardised manner within a defined turnaround time (TAT), communicate critical results immediately, outsource on quality criteria, implement a quality assurance programme with peer review, and maintain calibration and maintenance of equipment.

The chapter intent is that imaging services are reliable, timely, safe and quality-assured.

This policy owns imaging services. AAC.6 owns imaging safety (screening, radiation safety, signage). AAC.4 owns laboratory services. PSQ.2 owns quality indicators; imaging TAT and quality-assurance data feed PSQ.2.

TAT — turnaround time. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the imaging/radiology in-charge, radiographers, treating doctors who request imaging, nurses who accompany patients, and the Quality Coordinator at {HOSPITAL}.

It covers the nine elements AAC.5.a–i: legal compliance, scope, infrastructure and human resources, TAT, critical results, outsourcing, quality assurance programme, peer review, and calibration and maintenance.

Boundaries:

- AAC.6 owns imaging safety (patient screening, radiation safety devices, signage). This policy owns the imaging service process.
- AAC.4 owns laboratory services. Where point-of-care imaging and laboratory overlap, each service policy owns its quality assurance.
- HIC owns infection control in imaging. This policy owns the imaging process.
- PSQ.2 owns quality indicators. Imaging TAT and quality-assurance data feed PSQ.2.
- Spell out: turnaround time (TAT), personal protective equipment (PPE)."""

POLICY_STATEMENT = f"""{HOSPITAL} provides imaging services that comply with legal and other requirements, are commensurate with its scope, and have adequate infrastructure and qualified personnel. Results are available in a standardised manner within defined TAT. Critical results are communicated immediately. Tests not available in-house are outsourced based on quality assurance. A quality assurance programme is implemented, including peer review and periodic calibration and maintenance.

{HOSPITAL} does not report an imaging result without quality assurance, and does not delay a critical result."""

NON_NEGOTIABLES = f"""1. Do not operate imaging equipment without current legal registrations and licences (AERB licence for radiation equipment; PC-PNDT registration for ultrasound where applicable).
2. Do not report an imaging result that has not passed quality-assurance checks.
3. Do not delay communication of a critical imaging result beyond the defined time limit.
4. Do not outsource imaging to a provider that has no documented quality assurance system.
5. Do not operate imaging equipment that is overdue for calibration or maintenance.
6. Staff who see an imaging rule broken report it the same shift to the {D('Imaging In-Charge')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Legal and regulatory compliance

Imaging services at {HOSPITAL} comply with legal and other requirements:

- Atomic Energy (Radiation Protection) Rules, 2004: licence for radiation-emitting equipment, radiation-safety officer where required, dose monitoring.
- Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994: registration of ultrasound equipment, Form F maintenance, display of the Act's provisions.
- {D('State-specific radiology or imaging rules where applicable')}.

The imaging in-charge maintains a register of licences, registrations and their renewal dates. Renewal is initiated {D('60 days before expiry')}.""",

f"""5.2 Scope of imaging services

The scope of imaging services at {HOSPITAL} is commensurate with the clinical services the hospital provides. The imaging in-charge maintains a service menu listing every modality and examination available in-house and every examination outsourced. The menu is reviewed {D('annually')} and whenever clinical services change.""",

f"""5.3 Infrastructure and human resources

The imaging infrastructure — rooms, equipment, lead shielding, utilities — is adequate for the defined scope. Equipment is listed in an inventory with model, serial number, date of installation and maintenance schedule.

Human resources are adequate: qualified radiographers and an imaging in-charge with qualifications as required under {D('State rules and AERB norms')}. Staff-to-workload ratios are reviewed {D('annually')}.""",

f"""5.4 Standardised results within defined turnaround time

Imaging results are available in the standardised manner within a defined TAT:

- Routine in-patient imaging: {D('within four hours of examination')}.
- Urgent / stat imaging: {D('within one hour')}.
- Routine out-patient imaging: {D('same day or next morning as defined per modality')}.

Reports follow a standardised format: patient identification, examination, clinical indication, technique, findings, impression and reporting radiologist/doctor. The imaging in-charge monitors TAT {D('monthly')}.""",

f"""5.5 Critical imaging results

Critical imaging results are intimated immediately to the personnel concerned. The imaging department maintains a written critical-finding list — {D('the list approved by the Medical Superintendent and treating doctors')}.

When a critical finding is detected:

- the radiographer or reporting doctor telephones the treating doctor or the nurse caring for the patient within {D('30 minutes')} of finding;
- the call is documented: patient name, unique identification number, examination, finding, caller, receiver, date and time;
- a read-back is obtained from the receiver.""",

f"""5.6 Outsourced imaging tests

Imaging tests not available in-house are outsourced to organisation(s) based on their quality assurance system. The hospital maintains a panel selected on documented criteria: {D('NABL/NABH accreditation or equivalent quality assurance, TAT, cost, radiation safety and reliability')}.

Outsourced results are reviewed by the imaging in-charge before release to the patient file. The outsourced origin is recorded. The panel is reviewed {D('annually')}.""",

f"""5.7 Quality assurance programme

The quality assurance programme for imaging services is implemented. It includes:

- image quality checks {D('daily before patient examinations begin')};
- reject/repeat analysis {D('monthly')};
- pre-examination, examination and post-examination error tracking;
- corrective action when image quality or equipment performance falls below acceptable limits;
- review of quality data {D('monthly')} by the imaging in-charge and {D('quarterly')} by the Quality Coordinator.""",

f"""5.8 Peer review of imaging protocols and results

The quality assurance programme addresses periodic internal or external peer review of imaging protocols and results using appropriate sampling:

- internal peer review: {D('the imaging in-charge or a designated senior doctor reviews a random sample of reports quarterly')};
- external peer review: {D('where available, participation in an external audit or tele-radiology peer review annually')};
- discrepancies are discussed, documented and feed back into training and protocol revision.""",

f"""5.9 Calibration and maintenance of imaging equipment

The quality assurance programme includes periodic calibration and maintenance of all imaging equipment. Each instrument has a maintenance schedule specifying:

- frequency of calibration (as per manufacturer recommendation and {D('AERB requirements for radiation equipment')});
- frequency of preventive maintenance;
- person responsible;
- acceptable tolerance limits.

Calibration and maintenance are recorded in an equipment log. Equipment that fails calibration is taken out of service until repaired and recalibrated. Breakdown maintenance is recorded with downtime and impact on service.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that imaging services comply with law, are quality-assured and meet TAT.

Imaging / Radiology In-Charge
- Manages imaging services, maintains service menu, monitors TAT, runs the quality assurance programme, manages outsourced panel and maintains licence register.

Radiographers
- Perform examinations, run image quality checks, communicate critical results and maintain equipment logs.

Treating doctors
- Request imaging appropriately and respond to critical results.

Nurses
- Accompany patients to imaging as required and assist with patient preparation.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when imaging defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Legal registrations and licences current and displayed.
- Service menu current and commensurate with clinical services.
- Infrastructure and staffing adequate for scope.
- TAT compliance by modality.
- Critical-result communication within time limit, with documentation and read-back.
- Outsourced panel current and based on quality criteria.
- Image quality, reject/repeat analysis and corrective actions.
- Peer review records and feedback.
- Calibration and maintenance logs; no overdue equipment.

Root-cause analysis is required when the same imaging defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when modalities, equipment or legal requirements change."""

TRAINING_ACKNOWLEDGEMENT = f"""All imaging staff, nurses who accompany patients and treating doctors are trained on this policy at induction and {D('once a year')} after that. Training covers imaging processes, critical-result communication, quality assurance, peer review and calibration.

Staff acknowledgement

I have read this Imaging Services policy of {HOSPITAL}. I will follow the imaging, TAT, critical-result, quality assurance and calibration processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/05')}
Issue number: {D('01')}
Version: {VERSION} (AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Imaging In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.5.
- Atomic Energy (Radiation Protection) Rules, 2004 — licensing and radiation safety for imaging equipment.
- Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994 — registration and use of ultrasound equipment.
- Internal documents of {HOSPITAL}: imaging service menu; equipment inventory; critical-finding list; outsourced imaging agreements; quality assurance records; calibration and maintenance logs; licence register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: imaging/radiology department; emergency; every in-patient ward; out-patient; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
AERB — Atomic Energy Regulatory Board
CAPA — corrective and preventive action
HIC — Hospital Infection Control (NABH SHCO chapter 3)
NABL — National Accreditation Board for Testing and Calibration Laboratories
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994
PPE — personal protective equipment
PSQ — Patient Safety and Quality (NABH SHCO chapter)
SHCO — Standards for Small Healthcare Organisations
TAT — turnaround time"""

STATUTE_CLAUSE = (
    "the Atomic Energy (Radiation Protection) Rules, 2004, insofar as radiation-emitting "
    "imaging equipment is installed, operated and monitored under those rules, and the "
    "Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, "
    "1994, insofar as ultrasound and prenatal imaging equipment is registered, used and "
    "reported under that Act"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "AAC.5.a",
        "requirement": "Imaging services comply with legal and other requirements.",
        "steps": "Section 3; 5.1 Legal and regulatory compliance; Section 4 item 1",
        "responsible": "Imaging In-Charge (maintain licences); Medical Superintendent (accountable)",
        "records": [
            "Register of licences, registrations and renewal dates.",
            "Current AERB licence for radiation equipment.",
            "PC-PNDT registration and Form F records where applicable.",
        ],
    },
    {
        "oe_code": "AAC.5.b",
        "requirement": "Scope of the imaging services is commensurate to the services provided by the organization.",
        "steps": "Section 3; 5.2 Scope of imaging services",
        "responsible": "Imaging In-Charge (maintain menu); Medical Superintendent (approve)",
        "records": [
            "Imaging service menu listing in-house and outsourced modalities.",
            "Annual review record of service menu against clinical services.",
            "Record of modality additions or withdrawals.",
        ],
    },
    {
        "oe_code": "AAC.5.c",
        "requirement": "The infrastructure (physical and equipment) and human resources are adequate to provide for its defined scope of services.",
        "steps": "Section 3; 5.3 Infrastructure and human resources",
        "responsible": "Imaging In-Charge (manage); Medical Superintendent (resource)",
        "records": [
            "Equipment inventory with model, serial number, installation date and maintenance schedule.",
            "Staff list with qualifications and staff-to-workload review.",
            "Infrastructure adequacy assessment including lead shielding.",
        ],
    },
    {
        "oe_code": "AAC.5.d",
        "requirement": "Imaging results are available in the standardised manner within a defined time frame.",
        "steps": "Section 3; 5.4 Standardised results within defined TAT; Section 4 item 2",
        "responsible": "Imaging In-Charge (monitor TAT); radiographers (report); Quality Coordinator (audit)",
        "records": [
            "Defined TAT for each modality category.",
            "Monthly TAT compliance report.",
            "Standardised report format with required fields.",
        ],
    },
    {
        "oe_code": "AAC.5.e",
        "requirement": "Critical results are intimated immediately to the personnel concerned.",
        "steps": "Section 3; 5.5 Critical imaging results; Section 4 item 3",
        "responsible": "Radiographers or reporting doctor (call); treating doctors (respond); Imaging In-Charge (escalate)",
        "records": [
            "Critical-finding list approved by Medical Superintendent.",
            "Critical-result communication log with caller, receiver, read-back, date and time.",
            "Escalation records when treating doctor was unreachable.",
        ],
    },
    {
        "oe_code": "AAC.5.f",
        "requirement": "Imaging tests not available in the organization are outsourced to organization(s) based on their quality assurance system.",
        "steps": "Section 3; 5.6 Outsourced imaging tests; Section 4 item 4",
        "responsible": "Imaging In-Charge (manage panel); Quality Coordinator (audit criteria)",
        "records": [
            "Outsourced imaging panel with selection criteria.",
            "Agreements specifying TAT, critical-result communication and quality assurance.",
            "Annual review of outsourced panel.",
        ],
    },
    {
        "oe_code": "AAC.5.g",
        "requirement": "The quality assurance programme for imaging services is implemented.",
        "steps": "Section 3; 5.7 Quality assurance programme; Section 4 item 2",
        "responsible": "Imaging In-Charge (run programme); Quality Coordinator (quarterly review)",
        "records": [
            "Daily image quality check records.",
            "Monthly reject/repeat analysis.",
            "Corrective action records for quality failures.",
        ],
    },
    {
        "oe_code": "AAC.5.h",
        "requirement": "The programme addresses periodic internal / external peer review of imaging protocols and results using appropriate sampling.",
        "steps": "Section 3; 5.8 Peer review of imaging protocols and results",
        "responsible": "Imaging In-Charge (organise); designated senior doctor (review); Quality Coordinator (track)",
        "records": [
            "Internal peer review records with sample size and findings.",
            "External peer review or audit records where available.",
            "Discrepancy log and feedback to training and protocols.",
        ],
    },
    {
        "oe_code": "AAC.5.i",
        "requirement": "The programme includes periodic calibration and maintenance of all equipment.",
        "steps": "Section 3; 5.9 Calibration and maintenance of imaging equipment; Section 4 item 5",
        "responsible": "Radiographers (perform); Imaging In-Charge (schedule); Quality Coordinator (audit)",
        "records": [
            "Calibration and maintenance schedule for each instrument.",
            "Equipment log with calibration results and maintenance records.",
            "Record of equipment taken out of service for failed calibration.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.5 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. AAC.5.d, AAC.5.e, AAC.5.f, AAC.5.g, AAC.5.i asterisked. No stop-work. P2: AERP Rules 2004 and PC-PNDT Act 1994. Nine OEs, nine What-we-do subsections."""


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
        "subtitle": "Imaging services, quality assurance and turnaround time.",
        "doc_no": D("AAC/POL/05"),
    }
    emit_pre_v2(
        draft,
        "aac5_v2_draft.json",
        "AAC.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
