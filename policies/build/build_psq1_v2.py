# -*- coding: utf-8 -*-
"""PSQ.1 v2 — patient-safety programme and quality improvement programme.

Shape follows PRE v2 (section list and order only). Wording is built from PSQ.1 OEs
read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 108 / PDF index 108.

No stop-work section. Nine OEs clustered into seven What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PSQ.1"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.1.a", "PSQ.1.b", "PSQ.1.c", "PSQ.1.d", "PSQ.1.e",
    "PSQ.1.f", "PSQ.1.g", "PSQ.1.h", "PSQ.1.i",
]
POLICY_TITLE = "Patient-Safety Programme and Quality Improvement Programme"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PSQ v2 template: PRE v2 shape, plain English, PSQ roles, seven steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation implements a patient-safety programme and a structured quality "
    "improvement programme — not as filing exercises but as real systems that identify "
    "risks, set goals, audit performance and improve nursing care."
)

PURPOSE = f"""This policy describes how {HOSPITAL} maintains a patient-safety programme and a structured quality improvement programme that together satisfy PSQ.1.a–i.

It covers nine elements: multi-disciplinary patient-safety committee; opportunity identification at defined intervals; proactive risk analysis; national/international safety goals; multi-disciplinary QI committee; designated QI coordinator; QI opportunity review; regular audits; and a process for monitoring and improving nursing care quality.

PSQ.1 owns the programmes, their committees, their reviews and their audits. ROM.4 owns leadership ownership of organisational risk. PSQ.2 owns the key indicators. PSQ.3 owns the clinical audit system. PSQ.4 owns management support. PSQ.5 owns incident analysis.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical and non-clinical departments at {HOSPITAL} and to every staff member involved in patient safety or quality improvement activities: the patient-safety committee, the quality improvement committee, the {D('Quality Coordinator')}, department heads, treating clinicians, nursing staff and the Medical Superintendent.

It covers the nine objective elements PSQ.1.a–i. It does not cover key indicators (PSQ.2), the clinical audit system (PSQ.3), management support for the programmes (PSQ.4), or incident analysis (PSQ.5).

Boundaries with other policies of {HOSPITAL}:

- ROM.4 owns leadership ownership of organisational risk; PSQ.1 owns the actual patient-safety programme, safety goals, QI programme, audits and nursing quality monitoring. Cross-reference ROM.4 for leadership risk registers.
- PSQ.2 owns clinical, infection-control, managerial and patient-safety indicators. PSQ.1 uses indicator data as input to opportunity identification.
- PSQ.3 owns the clinical audit system. PSQ.1.h is regular audits as a monitoring tool within the programmes.
- PSQ.4 owns management support and resources. PSQ.1 committees report to management under PSQ.4.
- PSQ.5 owns incident collection and analysis. PSQ.1 uses incident trends as input to the patient-safety programme."""

POLICY_STATEMENT = f"""{HOSPITAL} implements a patient-safety programme developed, implemented and maintained by a multi-disciplinary committee that identifies improvement opportunities at pre-defined intervals and performs proactive risk analysis.

{HOSPITAL} adapts and implements national/international patient-safety goals and solutions relevant to a small healthcare organisation.

{HOSPITAL} implements a comprehensive quality improvement programme developed, implemented and maintained by a multi-disciplinary committee with a designated coordinator, that identifies improvement opportunities at pre-defined intervals and uses regular audits as a monitoring tool.

{HOSPITAL} monitors and improves the quality of nursing care through an established process."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. The patient-safety programme is developed, implemented and maintained by a multi-disciplinary committee, not by one person writing minutes alone.
2. The patient-safety programme identifies improvement opportunities at pre-defined intervals, not only after an incident.
3. Proactive risk analysis is performed and acted upon — not only reactive investigation after harm.
4. National/international patient-safety goals are adapted and implemented, not merely listed in a poster.
5. The quality improvement programme is developed, implemented and maintained by a multi-disciplinary committee, not by a single coordinator without committee governance.
6. A designated individual coordinates and implements the QI programme; this role is named and filled.
7. The QI programme identifies improvement opportunities at pre-defined intervals, not only when an external assessment is due.
8. Audits are conducted at regular intervals as a means of continuous monitoring, not only before accreditation visits.
9. There is an established process to monitor and improve quality of nursing care — not only a committee that does not reach the ward.

Staff who identify a gap in any of the above report it to the {D('Quality Coordinator')} or the {D('Medical Superintendent')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Patient-safety committee and programme development

The patient-safety programme at {HOSPITAL} is developed, implemented and maintained by a multi-disciplinary committee chaired by {D('the Medical Superintendent')}. Members include {D('a senior clinician, a senior nurse, the Quality Coordinator, a pharmacist representative and an administrator')}. The committee meets {D('quarterly')} and keeps minutes with attendance, agenda, decisions and follow-up actions.

The programme covers: proactive risk identification, reactive incident review (using PSQ.5 data), patient-safety goals, improvement actions and their outcomes. The committee reviews the programme at each meeting and updates it {D('annually')} or sooner when a significant risk or incident trend emerges.""",

f"""5.2 Opportunity identification at pre-defined intervals

The patient-safety programme identifies opportunities for improvement based on review at pre-defined intervals: {D('quarterly')} committee meetings, {D('monthly')} incident-trend reports from PSQ.5, and {D('six-monthly')} proactive risk assessments.

Sources of opportunity include incident data (PSQ.5), indicator trends (PSQ.2), clinical audit findings (PSQ.3), patient complaints that reveal clinical risk (PRE.6 → PSQ.5 crossover), and staff-reported near-misses. Each identified opportunity is logged with owner, target date and status.""",

f"""5.3 Proactive risk analysis and national/international safety goals

{HOSPITAL} performs proactive analysis of patient-safety risks using {D('failure mode and effect analysis (FMEA) or a simplified risk-priority matrix')} for {D('at least one high-risk process per year')}. Results are documented with risk scores, actions taken and re-assessment dates.

{HOSPITAL} adapts and implements national/international patient-safety goals and solutions relevant to its services — including {D('NABH patient-safety goals, WHO patient-safety challenges and IPSG-equivalent goals applicable to a small hospital')}. Goals are reviewed {D('annually')} for continued relevance and documented evidence of implementation.""",

f"""5.4 Quality improvement committee and designated coordinator

A comprehensive quality improvement programme at {HOSPITAL} is developed, implemented and maintained by a multi-disciplinary committee. The QI committee may overlap with the patient-safety committee or be the same committee with a distinct agenda item; {D('at this hospital the patient-safety and QI committees are combined with separate agenda sections')}.

A designated individual — the {D('Quality Coordinator')} — coordinates and implements the QI programme. This person is named in the appointment register and has documented responsibilities including: coordinating QI projects, maintaining the indicator dashboard (PSQ.2), facilitating audits, and reporting to the committee and management.""",

f"""5.5 QI programme opportunity identification and review

The quality improvement programme identifies opportunities for improvement based on review at pre-defined intervals: {D('quarterly')} committee meetings and {D('monthly')} indicator reviews.

Sources include key indicator data (PSQ.2), audit findings (PSQ.1.h / PSQ.3), incident trends (PSQ.5), patient feedback (PRE.6), and department self-assessments. Each identified opportunity is logged, prioritised, assigned an owner and tracked to closure. The committee reviews progress at each meeting.""",

f"""5.6 Regular audits as continuous monitoring

Audits are conducted at regular intervals as a means of continuous monitoring. The audit schedule is prepared {D('annually')} by the {D('Quality Coordinator')} and approved by the committee. Audit topics cover clinical processes, infection control, safety practices, documentation and managerial processes.

Each audit has a defined scope, criteria, method, findings and recommendations. Findings feed into the patient-safety and QI programmes as opportunities for improvement. Audit reports are presented to the committee and tracked for CAPA closure. PSQ.3 owns the clinical audit system in detail; this step is audits as a QI monitoring tool.""",

f"""5.7 Monitoring and improving quality of nursing care

{HOSPITAL} has an established process to monitor and improve the quality of nursing care. The {D('Nursing In-Charge')} or designated nursing quality lead participates in the QI committee and reports on nursing indicators {D('monthly')}.

Nursing quality monitoring includes: {D('medication administration accuracy, patient-fall rates, nursing documentation completeness, hand-hygiene compliance and pressure-injury prevention')}. Findings are reviewed in the QI committee, and improvement actions are assigned, implemented and tracked. Nursing staff participate in audits relevant to their practice.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Chairs or sponsors the patient-safety and QI committees.
- Accountable that both programmes are implemented, not only documented.

Quality Coordinator
- Designated individual for coordinating and implementing the QI programme.
- Maintains audit schedule, indicator dashboard and opportunity logs.
- Prepares committee agendas and tracks CAPA to closure.

Patient-Safety / QI Committee
- Multi-disciplinary body that develops, implements and maintains both programmes.
- Reviews opportunities at pre-defined intervals and approves improvement actions.

Department Heads
- Participate in committee meetings and own department-level improvement actions.
- Ensure staff cooperate with audits and report risks.

Nursing In-Charge / Nursing Quality Lead
- Monitors and reports nursing care quality indicators.
- Participates in committee meetings and leads nursing improvement actions.

Treating Clinicians
- Participate in clinical audits and report patient-safety risks and near-misses."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers programmes, committees and floor practice.

What is monitored each quarter:

- Patient-safety committee met as scheduled with multi-disciplinary attendance and documented minutes.
- Opportunities for improvement identified and logged at pre-defined intervals.
- Proactive risk analysis performed and documented with actions taken.
- National/international safety goals adapted and evidence of implementation recorded.
- QI committee met as scheduled; designated coordinator role filled and active.
- QI opportunities identified, assigned, tracked to closure.
- Audit schedule maintained; audits conducted; findings fed back into programmes.
- Nursing quality indicators monitored and reported; improvement actions tracked.

Root-cause analysis is required when two consecutive quarterly reviews show no new improvement opportunities identified or when an audit finding remains open beyond {D('90 days')}.

This policy is reviewed {D('annually')}, and sooner when PSQ.2, PSQ.3, PSQ.4 or PSQ.5 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff involved in patient-safety and QI activities are trained on this policy at induction and {D('once a year')} after that. Training covers the patient-safety programme, QI programme, audit participation, incident reporting (pointer to PSQ.5) and nursing quality monitoring.

Staff acknowledgement

I have read this Patient-Safety Programme and Quality Improvement Programme policy of {HOSPITAL}. I understand the patient-safety and QI programmes and my role in them.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PSQ/POL/01"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Safety and Quality Improvement chapter, standard PSQ.1.
- Internal documents of {HOSPITAL}: patient-safety committee terms of reference; QI committee terms of reference; audit schedule; indicator dashboard (PSQ.2); clinical audit system (PSQ.3); incident management system (PSQ.5); nursing quality monitoring records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: patient-safety / QI committee members; department heads; nursing administration; all clinical areas.

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
FMEA — failure mode and effect analysis
IPSG — International Patient Safety Goals
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
QI — quality improvement
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.1.a",
        "requirement": "The patient safety programme is developed, implemented and maintained by a multi-disciplinary committee.",
        "steps": "Statement of intent; Section 3; 5.1 Patient-safety committee and programme development; Section 4 item 1",
        "responsible": "Medical Superintendent (chair); patient-safety committee (develop and maintain)",
        "records": [
            "Patient-safety committee terms of reference with multi-disciplinary membership list.",
            "Committee meeting minutes with attendance, agenda, decisions and follow-up.",
            "Patient-safety programme document with development, implementation and maintenance evidence.",
            "Annual programme review record.",
        ],
    },
    {
        "oe_code": "PSQ.1.b",
        "requirement": "The patient-safety programme identifies opportunities for improvement based on review at pre-defined intervals.",
        "steps": "Section 3; 5.2 Opportunity identification at pre-defined intervals; Section 4 item 2",
        "responsible": "Quality Coordinator (log and track); patient-safety committee (review at intervals)",
        "records": [
            "Defined review intervals documented in programme or committee terms of reference.",
            "Opportunity log with source, owner, target date and status.",
            "Committee minutes showing review of opportunities at each meeting.",
        ],
    },
    {
        "oe_code": "PSQ.1.c",
        "requirement": "The organisation performs proactive analysis of patient safety risks and makes improvement accordingly.",
        "steps": "Section 3; 5.3 Proactive risk analysis and national/international safety goals; Section 4 item 3",
        "responsible": "Quality Coordinator (facilitate analysis); patient-safety committee (approve actions)",
        "records": [
            "Proactive risk analysis reports (FMEA or equivalent) with risk scores and actions.",
            "Re-assessment records showing risk reduction after actions.",
            "Committee minutes approving risk analysis scope and results.",
        ],
    },
    {
        "oe_code": "PSQ.1.d",
        "requirement": "The organisation adapts and implements national/international patient-safety goals/solutions.",
        "steps": "Section 3; 5.3 Proactive risk analysis and national/international safety goals; Section 4 item 4",
        "responsible": "Quality Coordinator (adapt goals); patient-safety committee (approve and monitor)",
        "records": [
            "List of adopted national/international patient-safety goals with relevance rationale.",
            "Implementation evidence for each adopted goal.",
            "Annual review record of goal relevance and implementation status.",
        ],
    },
    {
        "oe_code": "PSQ.1.e",
        "requirement": "A comprehensive quality improvement programme is developed, implemented and maintained by a multi-disciplinary committee.",
        "steps": "Statement of intent; Section 3; 5.4 QI committee and designated coordinator; Section 4 item 5",
        "responsible": "Medical Superintendent (sponsor); QI committee (develop and maintain)",
        "records": [
            "QI committee terms of reference with multi-disciplinary membership list.",
            "QI programme document with scope, objectives and maintenance schedule.",
            "Committee meeting minutes showing programme governance.",
        ],
    },
    {
        "oe_code": "PSQ.1.f",
        "requirement": "There is a designated individual for coordinating and implementing the quality improvement programme.",
        "steps": "Section 3; 5.4 QI committee and designated coordinator; Section 4 item 6",
        "responsible": "Quality Coordinator (designated individual); Medical Superintendent (appoint)",
        "records": [
            "Appointment letter or register entry naming the designated QI coordinator.",
            "Documented responsibilities of the QI coordinator role.",
            "Evidence of coordinator activity: reports, dashboards, meeting preparation.",
        ],
    },
    {
        "oe_code": "PSQ.1.g",
        "requirement": "The quality improvement programme identifies opportunities for improvement based on review at pre-defined intervals.",
        "steps": "Section 3; 5.5 QI programme opportunity identification and review; Section 4 item 7",
        "responsible": "Quality Coordinator (log and track); QI committee (review at intervals)",
        "records": [
            "Defined QI review intervals documented in programme or committee terms of reference.",
            "QI opportunity log with source, priority, owner and closure status.",
            "Committee minutes showing review of QI opportunities at each meeting.",
            "Trend analysis of QI opportunity sources across quarters.",
        ],
    },
    {
        "oe_code": "PSQ.1.h",
        "requirement": "Audits are conducted at regular intervals as a means of continuous monitoring.",
        "steps": "Section 3; 5.6 Regular audits as continuous monitoring; Section 4 item 8",
        "responsible": "Quality Coordinator (schedule and track); department heads (cooperate); committee (review findings)",
        "records": [
            "Annual audit schedule approved by the committee.",
            "Individual audit reports with scope, criteria, findings and recommendations.",
            "CAPA records linked to audit findings.",
            "Committee minutes showing audit findings reviewed and tracked.",
        ],
    },
    {
        "oe_code": "PSQ.1.i",
        "requirement": "There is an established process in the organisation to monitor and improve quality of nursing care.",
        "steps": "Section 3; 5.7 Monitoring and improving quality of nursing care; Section 4 item 9",
        "responsible": "Nursing In-Charge / nursing quality lead (monitor and report); QI committee (review and act)",
        "records": [
            "Nursing quality indicator definitions and targets.",
            "Monthly nursing quality indicator data and trend reports.",
            "Improvement action records for nursing quality findings.",
            "Committee minutes showing nursing quality reviewed and actions tracked.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PSQ.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation implements a patient-safety programme and a structured quality improvement programme." PSQ.1.a–i PDF page 108. PSQ.1.a, PSQ.1.g, PSQ.1.h, PSQ.1.i are asterisked. PSQ.1.a/b Commitment; PSQ.1.c/d/e Core; PSQ.1.f/g Commitment; PSQ.1.h Commitment; PSQ.1.i Core.

SHAPE: Seven What-we-do subsections (5.1–5.7). No stop-work. Disclaimer accreditation-only. PSQ roles only."""


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
        "subtitle": "Patient safety and quality improvement in day-to-day practice.",
        "doc_no": D("PSQ/POL/01"),
    }
    emit_pre_v2(
        draft,
        "psq1_v2_draft.json",
        "PSQ.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
