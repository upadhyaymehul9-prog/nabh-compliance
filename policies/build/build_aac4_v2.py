# -*- coding: utf-8 -*-
"""AAC.4 v2 — laboratory services.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.4 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 57–58.
No stop-work. Disclaimer P2 names Drugs and Cosmetics Act 1940.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.4"
CHAPTER = "AAC"
OE_CODES = [
    "AAC.4.a", "AAC.4.b", "AAC.4.c", "AAC.4.d",
    "AAC.4.e", "AAC.4.f", "AAC.4.g", "AAC.4.h",
]
POLICY_TITLE = "Laboratory Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, eight steps, no stop-work, D&C Act P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Laboratory services are provided as per the scope of services of the organisation "
    "and adhere to best practices — so that results are reliable, timely and safe."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides laboratory services commensurate with its scope, ensures adequate infrastructure and human resources, manages the specimen journey from requisition to disposal, delivers results within defined turnaround time (TAT), communicates critical results, outsources tests based on quality assurance, and implements a quality assurance programme including calibration and maintenance.

The chapter intent is that laboratory services are reliable, timely and quality-assured.

This policy owns laboratory services. AAC.6 owns laboratory safety. AAC.3 owns clinical assessment that laboratory results inform. PSQ.2 owns quality indicators; laboratory TAT and quality-assurance data feed PSQ.2.

TAT — turnaround time. PPE — personal protective equipment. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the laboratory in-charge, laboratory technicians, treating doctors who requisition tests, nurses who collect and transport specimens, and the Quality Coordinator at {HOSPITAL}.

It covers the eight elements AAC.4.a–h: scope of services, infrastructure and human resources, specimen handling, TAT, critical results, outsourcing, quality assurance programme, and calibration and maintenance.

Boundaries:

- AAC.6 owns laboratory safety (safety programme, training, safe practices). This policy owns the laboratory service process.
- AAC.5 owns imaging services. Where both laboratory and imaging share equipment (e.g. point-of-care), the service-specific policy owns the quality assurance for that equipment.
- HIC owns infection control in the laboratory. This policy owns specimen handling as a service process.
- PSQ.2 owns quality indicators. Laboratory TAT and quality-assurance data feed PSQ.2.
- Spell out: turnaround time (TAT), personal protective equipment (PPE)."""

POLICY_STATEMENT = f"""{HOSPITAL} provides laboratory services commensurate with its defined scope, with adequate infrastructure and qualified personnel. Specimens are requisitioned, collected, identified, handled, transported, processed and disposed of according to written guidance. Results are available within a defined TAT. Critical results are communicated immediately. Tests not available in-house are outsourced to organisations with a quality assurance system. A quality assurance programme is implemented, including periodic calibration and maintenance.

{HOSPITAL} does not report a result without quality assurance, and does not delay a critical result."""

NON_NEGOTIABLES = f"""1. Do not report a laboratory result that has not passed quality-assurance checks.
2. Do not delay communication of a critical result beyond the defined time limit.
3. Do not accept a specimen that is unlabelled, mislabelled or collected without following written guidance.
4. Do not outsource tests to a laboratory that has no documented quality assurance system.
5. Do not operate laboratory equipment that is overdue for calibration or maintenance.
6. Staff who see a laboratory rule broken report it the same shift to the {D('Laboratory In-Charge')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Scope of laboratory services

The scope of laboratory services at {HOSPITAL} is commensurate with the clinical services the hospital provides. The laboratory in-charge maintains a test menu that lists every test available in-house and every test outsourced. The menu is reviewed {D('annually')} and whenever clinical services change.

Tests not in the menu are not offered. When a treating doctor needs a test not in the menu, it is discussed with the laboratory in-charge and, if appropriate, added to the menu or arranged as an outsourced test under section 5.6.""",

f"""5.2 Infrastructure and human resources

The laboratory infrastructure — physical space, equipment and utilities — is adequate for the defined scope. Equipment is listed in an inventory with model, serial number, date of installation and maintenance schedule.

Human resources are adequate: qualified laboratory technicians and a laboratory in-charge with qualifications as required under {D('State rules and NABL norms where applicable')}. Staff-to-workload ratios are reviewed {D('annually')}.""",

f"""5.3 Specimen requisition, collection, handling, transport, processing and disposal

Requisition: the treating doctor raises a requisition specifying the test, clinical indication and urgency. The requisition form bears the patient's unique identification number.

Collection: the specimen is collected by a trained person, labelled immediately at the point of collection with patient name, unique identification number, date, time and specimen type. Two-patient identifiers are checked before collection.

Handling and transport: specimens are transported to the laboratory in appropriate containers, at the correct temperature, within {D('30 minutes of collection')}. A specimen log tracks receipt.

Processing: the laboratory processes specimens according to the standard operating procedure for each test. Rejected specimens (haemolysed, clotted, insufficient volume, mislabelled) are documented with the reason and a fresh specimen is requested.

Disposal: specimens after processing are disposed of as per Bio-Medical Waste Management Rules, 2016 (AAC.6 owns laboratory safety; disposal is a service step here).""",

f"""5.4 Turnaround time

Laboratory results are available within a defined TAT. The TAT for each category of test is:

- Routine in-patient tests: {D('within four hours of receipt in the laboratory')}.
- Urgent / stat tests: {D('within one hour of receipt')}.
- Routine out-patient tests: {D('same day or next morning as defined per test')}.

The laboratory in-charge monitors TAT compliance {D('monthly')} and reports exceptions to the Quality Coordinator. Persistent TAT breaches trigger root-cause analysis.""",

f"""5.5 Critical results communication

Critical results are intimated to the person concerned at the earliest. The laboratory maintains a written critical-value list — {D('the list approved by the Medical Superintendent and treating doctors')}.

When a critical value is detected:

- the laboratory technician telephones the treating doctor or the nurse caring for the patient within {D('30 minutes')} of result validation;
- the call is documented: patient name, unique identification number, test, result, caller, receiver, date and time;
- a read-back is obtained from the receiver.

If the treating doctor or nurse is unreachable within the time limit, the laboratory in-charge or the {D('Medical Superintendent')} is contacted.""",

f"""5.6 Outsourced laboratory tests

Tests not available in-house are outsourced to organisation(s) based on their quality assurance system. The hospital maintains a panel of outsourced laboratories selected on documented criteria: {D('NABL accreditation or equivalent quality assurance, TAT, cost and reliability')}.

The outsourced laboratory agreement includes TAT, critical-result communication, quality-assurance evidence, and specimen transport requirements. The laboratory in-charge reviews the panel {D('annually')}.

Outsourced results are reviewed by the laboratory in-charge before release to the patient file. The outsourced origin is recorded.""",

f"""5.7 Quality assurance programme

The laboratory quality assurance programme is implemented. It includes:

- internal quality control (IQC) run {D('daily for each analyte or batch')};
- external quality assurance scheme (EQAS) participation {D('as available for the test menu')};
- pre-analytical, analytical and post-analytical error tracking;
- corrective action when IQC is out of range or EQAS performance is unsatisfactory;
- review of quality data {D('monthly')} by the laboratory in-charge and {D('quarterly')} by the Quality Coordinator.

Results from a run where IQC failed are not reported until the failure is resolved and the run is repeated.""",

f"""5.8 Calibration and maintenance of equipment

The quality assurance programme includes periodic calibration and maintenance of all laboratory equipment. Each instrument has a maintenance schedule that specifies:

- frequency of calibration (as per manufacturer recommendation and {D('at minimum annually')});
- frequency of preventive maintenance;
- person responsible for calibration and maintenance;
- acceptable tolerance limits.

Calibration and maintenance are recorded in an equipment log. Equipment that fails calibration is taken out of service until repaired and recalibrated. Breakdown maintenance is recorded with downtime and impact on service.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that laboratory services are provided as per scope, are quality-assured and meet TAT.

Laboratory In-Charge
- Manages the laboratory, maintains the test menu, monitors TAT, runs the quality assurance programme, and manages outsourced panel.

Laboratory technicians
- Perform tests, run IQC, communicate critical results, and maintain equipment logs.

Treating doctors
- Requisition tests appropriately, respond to critical results, and participate in critical-value list review.

Nurses
- Collect specimens, label at point of collection, and transport safely.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when laboratory defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Test menu current and commensurate with clinical services.
- Infrastructure and staffing adequate for scope.
- Specimen handling: labelling, transport time, rejection rate and reasons.
- TAT compliance by test category.
- Critical-result communication within time limit, with documentation and read-back.
- Outsourced panel current and based on quality criteria.
- IQC and EQAS records; corrective actions for failures.
- Calibration and maintenance logs; no overdue equipment.

Root-cause analysis is required when the same laboratory defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the test menu, equipment or quality assurance programme changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All laboratory staff, nurses who collect specimens, and treating doctors are trained on this policy at induction and {D('once a year')} after that. Training covers specimen handling, critical-result communication, quality assurance and calibration.

Staff acknowledgement

I have read this Laboratory Services policy of {HOSPITAL}. I will follow the specimen, TAT, critical-result, quality assurance and calibration processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/04')}
Issue number: {D('01')}
Version: {VERSION} (AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Laboratory In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.4.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945 — procurement and storage of reagents and diagnostic kits.
- Bio-Medical Waste Management Rules, 2016 — specimen disposal (safety programme is AAC.6).
- Internal documents of {HOSPITAL}: test menu; specimen handling SOP; critical-value list; outsourced laboratory agreements; IQC and EQAS records; equipment inventory and maintenance logs."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: laboratory; emergency; every in-patient ward; out-patient; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
CAPA — corrective and preventive action
EQAS — external quality assurance scheme
HIC — Hospital Infection Control (NABH SHCO chapter 3)
IQC — internal quality control
NABL — National Accreditation Board for Testing and Calibration Laboratories
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PPE — personal protective equipment
PSQ — Patient Safety and Quality (NABH SHCO chapter)
SHCO — Standards for Small Healthcare Organisations
TAT — turnaround time"""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, "
    "insofar as laboratory reagents and diagnostic kits are procured and stored under those rules"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "AAC.4.a",
        "requirement": "Scope of the laboratory services is commensurate to the services provided by the organization.",
        "steps": "Section 3; 5.1 Scope of laboratory services",
        "responsible": "Laboratory In-Charge (maintain test menu); Medical Superintendent (approve)",
        "records": [
            "Test menu listing in-house and outsourced tests.",
            "Annual review record of test menu against clinical services.",
            "Record of test additions or withdrawals.",
        ],
    },
    {
        "oe_code": "AAC.4.b",
        "requirement": "The infrastructure (physical and equipment) and human resources are adequate to provide the defined scope of services.",
        "steps": "Section 3; 5.2 Infrastructure and human resources",
        "responsible": "Laboratory In-Charge (manage); Medical Superintendent (resource)",
        "records": [
            "Equipment inventory with model, serial number, installation date and maintenance schedule.",
            "Staff list with qualifications and staff-to-workload review.",
            "Infrastructure adequacy assessment.",
        ],
    },
    {
        "oe_code": "AAC.4.c",
        "requirement": "Requisition for tests, collection, identification, handling, safe transportation, processing and disposal of specimens is performed according to written guidance.",
        "steps": "Section 3; 5.3 Specimen requisition, collection, handling, transport, processing and disposal; Section 4 item 3",
        "responsible": "Laboratory technicians (process); nurses (collect and transport); treating doctors (requisition)",
        "records": [
            "Written specimen handling SOP covering requisition through disposal.",
            "Specimen log with receipt time and two-patient-identifier check.",
            "Rejection log with reason and re-collection record.",
        ],
    },
    {
        "oe_code": "AAC.4.d",
        "requirement": "Laboratory results are available within a defined time frame.",
        "steps": "Section 3; 5.4 Turnaround time; Section 4 item 2",
        "responsible": "Laboratory In-Charge (monitor TAT); Quality Coordinator (audit)",
        "records": [
            "Defined TAT for each test category.",
            "Monthly TAT compliance report.",
            "Root-cause analysis for persistent TAT breaches.",
        ],
    },
    {
        "oe_code": "AAC.4.e",
        "requirement": "Critical results are intimated to the person concerned at the earliest.",
        "steps": "Section 3; 5.5 Critical results communication; Section 4 item 2",
        "responsible": "Laboratory technicians (call); treating doctors (respond); Laboratory In-Charge (escalate)",
        "records": [
            "Critical-value list approved by Medical Superintendent.",
            "Critical-result communication log with caller, receiver, read-back, date and time.",
            "Escalation records when treating doctor was unreachable.",
        ],
    },
    {
        "oe_code": "AAC.4.f",
        "requirement": "Laboratory tests not available in the organization are outsourced to organization(s) based on their quality assurance system.",
        "steps": "Section 3; 5.6 Outsourced laboratory tests; Section 4 item 4",
        "responsible": "Laboratory In-Charge (manage panel); Quality Coordinator (audit criteria)",
        "records": [
            "Outsourced laboratory panel with selection criteria.",
            "Agreements specifying TAT, critical-result communication and quality assurance.",
            "Annual review of outsourced panel.",
        ],
    },
    {
        "oe_code": "AAC.4.g",
        "requirement": "The laboratory quality assurance programme is implemented.",
        "steps": "Section 3; 5.7 Quality assurance programme; Section 4 item 1",
        "responsible": "Laboratory In-Charge (run programme); Quality Coordinator (quarterly review)",
        "records": [
            "IQC records for each analyte or batch.",
            "EQAS participation and performance records.",
            "Corrective action records for IQC out-of-range or EQAS unsatisfactory.",
        ],
    },
    {
        "oe_code": "AAC.4.h",
        "requirement": "The programme includes periodic calibration and maintenance of all equipment.",
        "steps": "Section 3; 5.8 Calibration and maintenance of equipment; Section 4 item 5",
        "responsible": "Laboratory technicians (perform); Laboratory In-Charge (schedule); Quality Coordinator (audit)",
        "records": [
            "Calibration and maintenance schedule for each instrument.",
            "Equipment log with calibration results and maintenance records.",
            "Record of equipment taken out of service for failed calibration.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.4 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. AAC.4.c, AAC.4.d, AAC.4.e, AAC.4.f, AAC.4.g, AAC.4.h asterisked. No stop-work. P2: D&C Act 1940. Eight OEs, eight What-we-do subsections."""


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
        "subtitle": "Laboratory services, quality assurance and turnaround time.",
        "doc_no": D("AAC/POL/04"),
    }
    emit_pre_v2(
        draft,
        "aac4_v2_draft.json",
        "AAC.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
