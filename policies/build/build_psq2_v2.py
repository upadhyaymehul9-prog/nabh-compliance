# -*- coding: utf-8 -*-
"""PSQ.2 v2 — key indicators for structures, processes and outcomes.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed pages 108–109.

No stop-work section. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PSQ.2"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.2.a", "PSQ.2.b", "PSQ.2.c", "PSQ.2.d", "PSQ.2.e",
]
POLICY_TITLE = "Key Indicators for Structures, Processes and Outcomes"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PSQ v2 template: PRE v2 shape, plain English, PSQ roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation identifies key indicators to monitor the structures, processes "
    "and outcomes which are used as tools for continual improvement."
)

PURPOSE = f"""This policy describes how {HOSPITAL} identifies, monitors and uses key indicators across clinical, infection-control, managerial and patient-safety domains as tools for continual improvement, satisfying PSQ.2.a–e.

It covers five elements: clinical indicators for structures, processes and outcomes; infection-control indicators; managerial indicators; patient-safety indicators; and regular data verification and analysis by the quality team.

PSQ.2 owns indicator identification, monitoring, verification and analysis. PSQ.1 owns the programmes that consume indicator data. PSQ.3 owns the clinical audit system. PSQ.5 owns incident data that may feed patient-safety indicators.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all departments at {HOSPITAL} that generate or use indicator data: clinical departments, infection-control function, nursing, administration, the {D('Quality Coordinator')} and the patient-safety / QI committee.

It covers the five objective elements PSQ.2.a–e. It does not cover the programmes that act on indicator findings (PSQ.1), the clinical audit system (PSQ.3), management support (PSQ.4), or incident analysis (PSQ.5).

Boundaries with other policies of {HOSPITAL}:

- PSQ.1 owns the patient-safety and QI programmes. PSQ.2 feeds indicator data into those programmes.
- PSQ.3 owns clinical audits. PSQ.2 clinical indicators may trigger an audit but the audit method is PSQ.3.
- PSQ.5 owns incident collection. Incident rates may appear as patient-safety indicators under PSQ.2.d.
- ROM.4 owns leadership risk registers. PSQ.2 managerial indicators feed risk discussions but ROM.4 owns the register."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies and monitors key indicators to oversee clinical structures, processes and outcomes, infection-control activities, managerial structures, processes and outcomes, and patient-safety activities.

Data collected through these indicators is regularly verified by the quality team and analysed to identify opportunities for improvement.

{HOSPITAL} uses indicator data as a tool for continual improvement, not as a filing exercise for external assessment."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Clinical indicators covering structures, processes and outcomes are identified and monitored — not only outcome indicators.
2. Infection-control indicators are identified and monitored, aligned with the infection-control programme.
3. Managerial indicators covering structures, processes and outcomes are identified and monitored.
4. Patient-safety indicators are identified and monitored, linked to the patient-safety programme (PSQ.1).
5. Data is regularly verified by the quality team before analysis — unverified data is not used for improvement decisions.
6. Data is analysed to identify opportunities for improvement, not merely collected and filed.

Staff responsible for data collection report data integrity concerns to the {D('Quality Coordinator')} within {D('one working day')}."""

PROCEDURE_STEPS = [
f"""5.1 Clinical indicators for structures, processes and outcomes

{HOSPITAL} identifies and monitors key indicators to oversee clinical structures, processes and outcomes. The {D('Quality Coordinator')} maintains a clinical indicator register that includes {D('at least: bed occupancy rate, average length of stay, readmission rate within 30 days, surgical-site infection rate, return to OT within the same admission, and clinical documentation completeness')}.

Each indicator has a defined numerator, denominator, data source, collection frequency ({D('monthly')}), target or benchmark, and responsible department. Structure indicators assess resources and capacity; process indicators assess how care is delivered; outcome indicators assess results of care. The indicator register is reviewed {D('annually')} by the QI committee for relevance.""",

f"""5.2 Infection-control indicators

{HOSPITAL} identifies and monitors key indicators to oversee infection-control activities. The infection-control indicators are aligned with the infection-control programme and include {D('hand-hygiene compliance rate, hospital-associated infection rate, needle-stick injury rate, biomedical-waste segregation compliance and antibiotic stewardship indicators where applicable')}.

The {D('infection-control nurse or designated person')} collects data {D('monthly')} and reports to the QI committee. Trends are tracked and any indicator breaching its threshold triggers a review under the infection-control programme and is reported to the patient-safety committee.""",

f"""5.3 Managerial indicators for structures, processes and outcomes

{HOSPITAL} identifies and monitors key indicators to oversee managerial structures, processes and outcomes. Managerial indicators include {D('staff turnover rate, staff training completion rate, equipment downtime, patient waiting time in OPD, patient satisfaction score and financial indicators relevant to service delivery')}.

Each indicator has a defined data source, collection frequency ({D('monthly or quarterly as appropriate')}), and responsible department or person. The {D('Quality Coordinator')} consolidates managerial indicator data for committee review. Managerial indicators feed into ROM.4 leadership risk discussions where relevant.""",

f"""5.4 Patient-safety indicators

{HOSPITAL} identifies and monitors key indicators to oversee patient-safety activities. Patient-safety indicators include {D('patient fall rate, medication error rate, transfusion reaction rate, unplanned return to OT, sentinel event count, near-miss reporting rate and patient-safety goal compliance')}.

Indicators are linked to the patient-safety programme (PSQ.1) and to incident data (PSQ.5). The {D('Quality Coordinator')} reports patient-safety indicator trends to the patient-safety committee {D('quarterly')}. Any adverse trend triggers a proactive risk review under PSQ.1.c.""",

f"""5.5 Data verification and analysis for improvement

Data is regularly verified by the quality team and analysed to identify opportunities for improvement. The {D('Quality Coordinator')} or designated quality team member verifies data {D('monthly')} by checking completeness, accuracy and consistency before analysis.

Verified data is analysed using {D('trend charts, run charts or statistical process control charts as appropriate')}. Analysis results are presented to the QI committee with identified opportunities for improvement. Each opportunity is logged, prioritised and tracked under the QI programme (PSQ.1). Data that fails verification is returned to the source department for correction before use.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that key indicators are identified, monitored and used for improvement.

Quality Coordinator
- Maintains indicator registers across all four domains.
- Verifies data, performs analysis and presents findings to the committee.
- Tracks identified opportunities to closure under PSQ.1.

Patient-Safety / QI Committee
- Reviews indicator data at pre-defined intervals and approves improvement actions.

Department Heads
- Ensure timely and accurate data collection for indicators assigned to their department.

Infection-Control Nurse / Designated Person
- Collects and reports infection-control indicator data.

Nursing In-Charge
- Supports collection of clinical and patient-safety indicators at ward level."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers indicator identification, monitoring, verification and analysis.

What is monitored each quarter:

- Clinical, infection-control, managerial and patient-safety indicator registers are current and complete.
- Data collection is happening at defined frequencies with no gaps exceeding {D('one month')}.
- Data verification is documented before analysis.
- Analysis reports presented to committee with identified opportunities.
- Opportunities logged and tracked under QI programme.

Root-cause analysis is required when an indicator has no data for two consecutive collection periods or when verified data shows a sustained adverse trend over {D('three months')}.

This policy is reviewed {D('annually')}, and sooner when PSQ.1, PSQ.3, PSQ.4 or PSQ.5 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff involved in data collection or indicator monitoring are trained on this policy at induction and {D('once a year')} after that. Training covers indicator definitions, data collection methods, verification requirements and how indicator data feeds into the QI programme.

Staff acknowledgement

I have read this Key Indicators for Structures, Processes and Outcomes policy of {HOSPITAL}. I understand the indicators relevant to my department and my role in data collection and quality.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PSQ/POL/02"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Safety and Quality Improvement chapter, standard PSQ.2.
- Internal documents of {HOSPITAL}: clinical indicator register; infection-control indicator register; managerial indicator register; patient-safety indicator register; data verification records; QI committee minutes (PSQ.1)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: patient-safety / QI committee members; department heads; infection-control function; nursing administration.

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OPD — out-patient department
OT — operation theatre
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
QI — quality improvement
SHCO — Standards for Small Healthcare Organisations
SPC — statistical process control"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.2.a",
        "requirement": "The organisation identifies and monitors key indicators to oversee the clinical structures, processes and outcomes.",
        "steps": "Statement of intent; Section 3; 5.1 Clinical indicators; Section 4 items 1, 6",
        "responsible": "Quality Coordinator (register and analyse); department heads (collect data); QI committee (review)",
        "records": [
            "Clinical indicator register with numerator, denominator, data source, frequency, target.",
            "Monthly clinical indicator data sheets or dashboard entries.",
            "Committee minutes showing clinical indicator review and actions.",
        ],
    },
    {
        "oe_code": "PSQ.2.b",
        "requirement": "The organisation identifies and monitors the key indicators to oversee infection control activities.",
        "steps": "Section 3; 5.2 Infection-control indicators; Section 4 item 2",
        "responsible": "Infection-control nurse (collect); Quality Coordinator (consolidate); QI committee (review)",
        "records": [
            "Infection-control indicator register aligned with the infection-control programme.",
            "Monthly infection-control data and trend reports.",
            "Committee minutes showing infection-control indicator review and threshold-breach actions.",
        ],
    },
    {
        "oe_code": "PSQ.2.c",
        "requirement": "The organisation identifies and monitors the key indicators to oversee the managerial structures, processes and outcomes.",
        "steps": "Section 3; 5.3 Managerial indicators; Section 4 items 3, 6",
        "responsible": "Quality Coordinator (consolidate); department heads and administration (collect); QI committee (review)",
        "records": [
            "Managerial indicator register with data source, frequency and responsible person.",
            "Periodic managerial indicator data and trend reports.",
            "Committee minutes showing managerial indicator review and actions.",
        ],
    },
    {
        "oe_code": "PSQ.2.d",
        "requirement": "The organisation identifies and monitors the key indicators to oversee patient safety activities.",
        "steps": "Section 3; 5.4 Patient-safety indicators; Section 4 items 4, 6",
        "responsible": "Quality Coordinator (report trends); patient-safety committee (review and act)",
        "records": [
            "Patient-safety indicator register linked to the patient-safety programme (PSQ.1).",
            "Quarterly patient-safety indicator trend reports to the committee.",
            "Records of proactive risk reviews triggered by adverse indicator trends.",
        ],
    },
    {
        "oe_code": "PSQ.2.e",
        "requirement": "Data is regularly verified by the quality team and is analysed to identify the opportunities for improvement.",
        "steps": "Section 3; 5.5 Data verification and analysis; Section 4 items 5, 6",
        "responsible": "Quality Coordinator / quality team (verify and analyse); QI committee (act on findings)",
        "records": [
            "Data verification log showing date, verifier, issues found and resolution.",
            "Analysis reports with trend charts and identified opportunities for improvement.",
            "QI programme opportunity log entries traced from indicator analysis.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PSQ.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation identifies key indicators to monitor the structures, processes and outcomes which are used as tools for continual improvement." PSQ.2.a–e PDF pages 108–109. No asterisked OEs. PSQ.2.a/c/d/e Commitment; PSQ.2.b Core.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. PSQ roles only."""


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
        "template_test": "pre_v2_adoptable_shape",
        "subtitle": "Key indicators as tools for continual improvement.",
        "doc_no": D("PSQ/POL/02"),
    }
    emit_pre_v2(
        draft,
        "psq2_v2_draft.json",
        "PSQ.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
