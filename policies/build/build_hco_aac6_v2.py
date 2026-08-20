# -*- coding: utf-8 -*-
"""HCO AAC.6 v2 — laboratory services (Full Accreditation 6th Edition).

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer.
Content from NABH HCO 6th Edition PDF (md5 2c4489ee98de4ae9b49cba168ea9f42a),
OCR policies/source/hco6_aac_ocr.txt PDF idxs ~74–76. No SHCO AAC wording.
No stop-work. Disclaimer: accreditation-only; BMW cited in body as cross-ref only.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, emit_pre_v2

STANDARD_CODE = "AAC.6"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.6.a", "AAC.6.b", "AAC.6.c", "AAC.6.d", "AAC.6.e",
    "AAC.6.f", "AAC.6.g", "AAC.6.h", "AAC.6.i", "AAC.6.j",
]
POLICY_TITLE = "Laboratory Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO AAC.6 v2: lab services a–j from 6th Edition OCR; accreditation-only P2; no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Laboratory services are provided as per the scope of services of the organisation — "
    "so that results are available round the clock where clinical care needs them, "
    "handled safely from requisition to disposal, reported on time, and quality-assured."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides laboratory services commensurate with its clinical scope, keeps infrastructure and human resources adequate, uses qualified staff under pathologist/microbiologist/biochemist supervision, follows written guidance for the specimen journey, delivers results within defined turnaround time (TAT), intimates critical results within one hour with read-back, reports in a standardised manner, recalls or amends reports when needed, and outsources unavailable tests under a quality-assured MoU.

The chapter intent is that laboratory services are provided by competent staff so that patient care is continuous and diagnostic results support safe clinical decisions.

This policy owns laboratory service delivery (AAC.6). AAC.7 owns laboratory quality assurance and laboratory safety programmes. HIC / biomedical-waste policies own hospital-wide waste streams; specimen disposal here follows those duties without restating statute in the disclaimer. ROM.6.e owns MoU quality content for outsourced services. PSQ owns quality indicators; laboratory TAT and critical-result data feed those indicators.

TAT — turnaround time. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the laboratory in-charge, pathologist, microbiologist, biochemist, laboratory technologists, treating doctors who requisition tests, nurses who collect or transport specimens, and the Quality Coordinator at {HOSPITAL}.

It covers the ten objective elements AAC.6.a–j: scope and round-the-clock availability; infrastructure and layout; human resources; qualified performance and supervision; written specimen guidance; TAT; critical results; standardised reporting; recall/amendment; outsourcing with MoU.

Boundaries:

- AAC.7 owns the laboratory quality assurance programme and the laboratory safety programme (IQC/EQA, MSDS, PPE training). This policy owns service scope, specimen process, TAT, critical intimation, reporting and outsourcing.
- HIC and the organisation’s biomedical-waste / infection-control documents own waste segregation categories and statutory waste compliance. This policy requires disposal per those documents when citing Bio-Medical Waste Management Rules, 2016 duties in procedure — without importing that statute into paragraph 2 of the disclaimer.
- ROM.6.e owns MoU structure for outsourced diagnostic services; this policy requires an MoU that incorporates quality assurance for laboratory outsourcing.
- AAC.1 / AAC.2 own displayed clinical services and registration identity; the unique identification number used on specimens comes from registration.
- Spell out: turnaround time (TAT), Laboratory Information System (LIS), Hospital Information System (HIS), Memorandum of Understanding (MoU)."""

POLICY_STATEMENT = f"""{HOSPITAL} provides laboratory services commensurate with the healthcare services it offers, available round the clock so that patient care is not disrupted, with emergency-management test results available on its premises. Infrastructure, layout, human resources and qualified supervision are adequate for the defined scope. Specimens are requisitioned, collected, identified, handled, transported, processed and disposed of according to written guidance. Results are available within a defined TAT, critical results are intimated within one hour with documented read-back, and reports follow a standardised format. There is a mechanism to recall or amend reports. Tests not available in-house are outsourced only to organisations with a quality assurance system under a written MoU.

{HOSPITAL} does not delay a critical laboratory result, and does not release an altered outsourced report as if it were an in-house result."""

NON_NEGOTIABLES = f"""1. Do not offer a laboratory service outside the approved test menu without laboratory in-charge agreement and menu update or a documented outsourced arrangement.
2. Do not accept or process a specimen that is unlabelled, mislabelled, or collected without following written guidance.
3. Do not report a result without the authorised signatory required by statute and by this hospital’s authorisation list.
4. Do not leave a critical result uncommunicated beyond one hour after the report is ready.
5. Do not alter or modify content of an outsourced laboratory report.
6. Do not outsource a test to a laboratory that has no documented quality assurance system and no MoU with this hospital.
7. Do not leave a recalled report in clinical areas, the medical record, LIS or HIS after recall without replacement by the amended report.
8. Staff who see a laboratory service rule broken report it the same shift to the {D('Laboratory In-Charge')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Scope of laboratory services

Scope of the laboratory services at {HOSPITAL} is commensurate with the healthcare services the organisation provides. The laboratory in-charge maintains a test menu listing every test available in-house and every test outsourced. The menu is reviewed {D('annually')} and whenever clinical services change. Example from the standard: a cardiac care organisation must have facilities for cardiac enzymes.

Laboratory services are available round the clock so that patient care is not disrupted. Test results required for emergency management are available within the premises. Where a modality is not on site for non-emergency work, the outsourced path in section 5.10 applies; emergency-management tests that this hospital’s clinical scope requires remain on premises.

Tests not on the menu are not offered as in-house services.""",

f"""5.2 Infrastructure and layout

The infrastructure — physical space and equipment — is adequate to provide the defined scope of services. Reports must not be delayed for lack of adequate equipment. Equipment is listed in an inventory with model, serial number, installation date and maintenance schedule held under AAC.7 calibration duties.

The layout of the laboratory prevents cross-contamination. Clean and dirty workflows are separated; specimen receipt, processing and reporting areas are arranged so that contamination routes are interrupted. The laboratory in-charge reviews layout fitness {D('annually')} and after any renovation or major equipment change.""",

f"""5.3 Human resources

Human resource is adequate to provide the defined scope of services. The number of laboratory personnel is commensurate with workload, with sufficient staff for each shift and for emergencies. Reports must not be delayed for lack of adequate human resource, including personnel authorised to report results.

The laboratory in-charge and the {D('Medical Superintendent')} review staffing against workload {D('annually')} and after sustained TAT breaches linked to staffing.""",

f"""5.4 Qualified performance and supervision

Qualified and trained personnel perform and supervise the investigations and report the results. Staff employed in the laboratory hold an appropriate degree and are trained to carry out the tests they perform.

A Pathologist, Microbiologist and Biochemist supervise the staff for their respective disciplines as this hospital’s scope requires. Statutory requirements regarding the authorised signatory are adhered to. The laboratory in-charge keeps the current list of authorised signatories and does not release reports outside that list.""",

f"""5.5 Written guidance for requisition through disposal

Requisition for tests, collection, identification, handling, safe transportation, processing and disposal of a specimen is performed according to written guidance.

The organisation has documented guidance for requisition, collection, identification, handling, safe transportation, processing and disposal of the specimen, to ensure safety of the specimen until tests and retests (if required) are completed, observing standard and special precautions.

The unique identification number from registration is used for identification of the patient. The laboratory may also use another number (for example a lab number) to identify the sample. Two-patient identifiers are checked at collection and at receipt.

Disposal of waste follows the statutory biomedical-waste duties already owned by this hospital’s infection-control / waste documents (Bio-Medical Waste Management Rules, 2016, as applied in those documents). This step requires laboratory staff to segregate and hand over laboratory waste under those documents; it does not restate the Rules as this policy’s disclaimer statute.

Rejected specimens (haemolysed, clotted, insufficient, mislabelled) are logged with reason and a fresh specimen is requested.""",

f"""5.6 Results within defined turnaround time

Laboratory results are available within a defined time frame. The organisation defines the turnaround time for all tests and ensures adequate staff, materials and equipment so that results are available within that frame.

TAT may differ by test and is decided on the nature of the test, criticality and urgency desired by the treating doctor. Default categories unless the menu states otherwise:

- Emergency / stat tests required for immediate management: {D('within one hour of receipt in the laboratory')}.
- Routine in-patient tests: {D('within four hours of receipt')}.
- Routine out-patient tests: {D('same day or next morning as defined per test')}.

Infrastructure, human resources and supervision (sections 5.2–5.4) are maintained so that defined TAT is achievable. The laboratory in-charge monitors TAT {D('monthly')} and escalates persistent breaches to the Quality Coordinator.""",

f"""5.7 Critical results intimated within one hour

Critical results are intimated to the person concerned at the earliest.

The laboratory establishes biological reference intervals for different tests, or carefully evaluates published data where establishing an interval is not practical. Critical limits for tests that require immediate attention for patient management are documented. Critical results of outsourced investigations are included.

The laboratory in-charge identifies suitable personnel to report critical results. Critical test results are communicated to a person from the treating team (treating doctor, doctor member of the treating team, or ward nurse) at the earliest, and not later than one hour after completion of the test or the report being ready.

The intimation includes: name of the patient; unique ID; date and time of sample collection; test name, result, measure unit and reference range; identity of who communicated the value; identity of the recipient; read-back; and date and time of acknowledgement. The intimation is documented.

In electronic health systems, system-generated critical-result reporting may supplement physical reporting; it does not replace documentation of recipient acknowledgement when the treating team must act.""",

f"""5.8 Standardised reporting

Results are reported in a standardised manner. At a minimum the report includes: the name of the organisation (or, for an outsourced laboratory, the name of that laboratory); the patient’s name; the unique identification number; the reference range of the test where applicable; and the name and signature of the person reporting the test result.

All reports from an outsourced laboratory incorporate these features. The organisation does not alter or modify anything in the outsourced report. Outsourced test results appear either on the outsourced laboratory’s letterhead or on this organisation’s letterhead. If on this organisation’s letterhead, the report includes at least the name of the outsourced laboratory, the date and the reference number of the report given by the outsourced laboratory.""",

f"""5.9 Recall and amendment of reports

There is a mechanism to address the recall or amendment of reports whenever applicable. Recall may address errors from pre-analytical, analytical and post-analytical factors.

When a particular report is recalled, it is withdrawn from clinical areas, medical records, the Laboratory Information System (LIS) and the Hospital Information System (HIS). If already issued to the patient, the amended report is made available with a caution to ignore the earlier one. The recall and amendment are documented. Placement of the corrected report in all those areas is evidenced. Corrective and preventive action is implemented as appropriate based on detailed analysis, coordinated with AAC.7 quality assurance where the cause is a quality-system failure.""",

f"""5.10 Outsourced laboratory tests

Laboratory tests not available in the organisation are outsourced to organisation(s) based on their quality assurance system.

Written guidance for outsourcing includes:

- a list of tests for outsourcing;
- identity of personnel in the outsourced facilities to ensure safe and timely transportation of specimens, completion of tests as required for the patient, and receipt of results;
- manner of packaging and labelling of specimens, with the test requisition containing all details required for testing;
- a methodology to check the performance of the service rendered by the outsourced laboratory against this organisation’s requirements.

The organisation has a Memorandum of Understanding (MoU) / agreement that incorporates quality assurance and the requirements of this standard. Refer to ROM.6.e for MoU quality content. The panel and MoUs are reviewed {D('annually')}. Critical results from outsourced tests follow section 5.7.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that laboratory services match clinical scope, remain available round the clock for defined emergency tests, and meet TAT and critical-result duties.

Laboratory In-Charge
- Maintains the test menu, staffing plan, authorised-signatory list, written specimen guidance, TAT definitions, critical-limit list, standardised report format, recall mechanism and outsourced panel with MoUs.

Pathologist / Microbiologist / Biochemist
- Supervise investigations and reporting in their disciplines; act as or nominate authorised signatories as statute and hospital authorisation require.

Laboratory technologists
- Perform tests they are trained for; follow specimen guidance; communicate critical results when designated; do not alter outsourced reports.

Treating doctors and ward nurses
- Requisition appropriately; receive critical-result intimation with read-back; act on amended reports after recall.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA when TAT, critical-result or recall defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Test menu current and commensurate with clinical services; emergency tests available on premises.
- Infrastructure, layout and staffing adequate for scope.
- Authorised-signatory list current; unqualified reporting absent.
- Specimen guidance followed; rejection log reviewed.
- TAT compliance by category.
- Critical-result communication within one hour with full documentation and read-back.
- Standardised report format; outsourced letterhead rules followed; no alteration of outsourced content.
- Recall/amendment log complete with withdrawal evidence and CAPA.
- Outsourced panel and MoUs current and quality-based.

Root-cause analysis is required when the same laboratory service defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when clinical scope, equipment or outsourcing arrangements change."""

TRAINING_ACKNOWLEDGEMENT = f"""All laboratory staff, nurses who collect or transport specimens and doctors who requisition tests are trained on this policy at induction and {D('once a year')} after that. Training covers specimen guidance, TAT, critical-result intimation with read-back, standardised reporting, recall/amendment and outsourcing rules.

Staff acknowledgement

I have read this Laboratory Services policy of {HOSPITAL}. I will follow the specimen, TAT, critical-result, reporting, recall and outsourcing processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('HCO/AAC/POL/06')}
Issue number: {D('01')}
Version: {VERSION} (HCO AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Laboratory In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.6 (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- ISO 15189:2022 and NABL 112 — guidance references for laboratory quality systems owned under AAC.7; cited here only as boundary.
- Internal documents of {HOSPITAL}: laboratory test menu; specimen SOPs; critical-limit list; authorised-signatory list; TAT definitions; recall/amendment log; outsourced laboratory MoUs (ROM.6.e); infection-control / biomedical-waste procedures for disposal."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: laboratory; emergency; every in-patient ward; out-patient; nursing administration; intensive-care areas if present.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
CAPA — corrective and preventive action
HCO — Hospital (Full Accreditation programme)
HIS — Hospital Information System
HIC — Hospital Infection Control
LIS — Laboratory Information System
MoU — Memorandum of Understanding
NABL — National Accreditation Board for Testing and Calibration Laboratories
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PPE — personal protective equipment
PSQ — Patient Safety and Quality
ROM — Responsibilities of Management
TAT — turnaround time"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.6.a",
        "requirement": "Scope of the laboratory services is commensurate to the services provided by the organisation.",
        "steps": "Section 3; 5.1 Scope of laboratory services",
        "responsible": "Laboratory In-Charge (maintain menu); Medical Superintendent (approve scope)",
        "records": [
            "Laboratory test menu listing in-house and outsourced tests.",
            "Annual review of menu against clinical services.",
            "Record that emergency-management tests required by scope are available on premises.",
        ],
    },
    {
        "oe_code": "AAC.6.b",
        "requirement": "The infrastructure (physical and equipment) is adequate to provide the defined scope of services; layout prevents cross-contamination.",
        "steps": "Section 3; 5.2 Infrastructure and layout",
        "responsible": "Laboratory In-Charge (manage); Medical Superintendent (resource)",
        "records": [
            "Equipment inventory with model, serial and maintenance schedule link.",
            "Layout / workflow description showing separation that prevents cross-contamination.",
            "Annual infrastructure adequacy review.",
        ],
    },
    {
        "oe_code": "AAC.6.c",
        "requirement": "Human resource is adequate to provide the defined scope of services.",
        "steps": "Section 3; 5.3 Human resources",
        "responsible": "Laboratory In-Charge (roster); Medical Superintendent (resource)",
        "records": [
            "Staff list by shift including emergency cover.",
            "Annual staff-to-workload review.",
            "List of personnel authorised to report results.",
        ],
    },
    {
        "oe_code": "AAC.6.d",
        "requirement": "Qualified and trained personnel perform and supervise the investigations and report the results.",
        "steps": "Section 3; 5.4 Qualified performance and supervision; Section 4 item 3",
        "responsible": "Pathologist/Microbiologist/Biochemist (supervise); Laboratory In-Charge (authorised signatories)",
        "records": [
            "Qualification and training records for laboratory staff.",
            "Supervision arrangement by Pathologist, Microbiologist and Biochemist as applicable.",
            "Current authorised-signatory list meeting statutory requirements.",
        ],
    },
    {
        "oe_code": "AAC.6.e",
        "requirement": "Requisition for tests, collection, identification, handling, safe transportation, processing and disposal of a specimen is performed according to written guidance.",
        "steps": "Section 3; 5.5 Written guidance for requisition through disposal; Section 4 item 2",
        "responsible": "Laboratory In-Charge (own SOPs); technologists and collecting nurses (follow)",
        "records": [
            "Written guidance covering requisition, collection, identification, handling, transport, processing and disposal.",
            "Specimen rejection log with reasons.",
            "Evidence of unique ID (and lab number if used) on specimens and requisitions.",
        ],
    },
    {
        "oe_code": "AAC.6.f",
        "requirement": "Laboratory results are available within a defined time frame.",
        "steps": "Section 3; 5.6 Results within defined turnaround time",
        "responsible": "Laboratory In-Charge (define and monitor TAT); Quality Coordinator (audit)",
        "records": [
            "Defined TAT for all tests or test categories.",
            "Monthly TAT compliance report.",
            "Escalation records for persistent TAT breaches.",
        ],
    },
    {
        "oe_code": "AAC.6.g",
        "requirement": "Critical results are intimated to the person concerned at the earliest.",
        "steps": "Section 3; 5.7 Critical results intimated within one hour; Section 4 item 4",
        "responsible": "Designated laboratory personnel (intimate); treating team (read-back); Laboratory In-Charge (limits list)",
        "records": [
            "Documented critical limits and biological reference intervals (or evaluated published intervals).",
            "Critical-result communication log with patient ID, result, caller, recipient, read-back, date and time.",
            "List of personnel authorised to report critical results.",
        ],
    },
    {
        "oe_code": "AAC.6.h",
        "requirement": "Results are reported in a standardised manner.",
        "steps": "Section 3; 5.8 Standardised reporting; Section 4 item 5",
        "responsible": "Laboratory In-Charge (format); authorised signatory (sign); technologists (do not alter outsourced content)",
        "records": [
            "Standardised report template with minimum required fields.",
            "Sample outsourced reports on outsourced letterhead or organisation letterhead with required attribution.",
            "Audit finding that outsourced report content was not altered.",
        ],
    },
    {
        "oe_code": "AAC.6.i",
        "requirement": "There is a mechanism to address the recall / amendment of reports whenever applicable.",
        "steps": "Section 3; 5.9 Recall and amendment of reports; Section 4 item 7",
        "responsible": "Laboratory In-Charge (run mechanism); Quality Coordinator (CAPA)",
        "records": [
            "Recall/amendment log with reason and date.",
            "Evidence of withdrawal from clinical areas, medical records, LIS and HIS.",
            "Amended report issued to patient with caution where previously issued; CAPA record.",
        ],
    },
    {
        "oe_code": "AAC.6.j",
        "requirement": "Laboratory tests not available in the organisation are outsourced to organisation(s) based on their quality assurance system.",
        "steps": "Section 3; 5.10 Outsourced laboratory tests; Section 4 item 6",
        "responsible": "Laboratory In-Charge (panel and MoU); Medical Superintendent (approve MoU)",
        "records": [
            "Written outsourcing guidance with test list, transport contacts, packaging and performance checks.",
            "Current MoU/agreement incorporating quality assurance (ROM.6.e).",
            "Annual review of outsourced laboratory performance.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.6 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Asterisked: e,f,g,i,j. Ten OEs, ten What-we-do subsections. No stop-work. P2 accreditation-only (BMW disposal cross-ref in body only)."""


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
        "stop_work": "",
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Laboratory services commensurate with clinical scope.",
        "doc_no": D("HCO/AAC/POL/06"),
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.6",
    }
    emit_pre_v2(
        draft,
        "hco_aac6_v2_draft.json",
        "HCO.AAC.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
