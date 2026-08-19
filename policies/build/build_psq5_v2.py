# -*- coding: utf-8 -*-
"""PSQ.5 v2 — incident collection and analysis for continual quality improvement.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 110.

WITH stop-work section. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only.
NOTE: PDF header has no terminal period — our wording adds one.
NOTE: PDF uses "organization" for PSQ.5.e — our wording uses "organisation".
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PSQ.5"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.5.a", "PSQ.5.b", "PSQ.5.c", "PSQ.5.d", "PSQ.5.e",
]
POLICY_TITLE = "Incident Collection and Analysis for Continual Quality Improvement"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PSQ v2 template: PRE v2 shape, plain English, PSQ roles, five steps, WITH stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Incidents are collected and analysed to ensure continual quality improvement — "
    "not filed in a register that no one reads after the event."
)

PURPOSE = f"""This policy describes how {HOSPITAL} collects and analyses incidents to ensure continual quality improvement, satisfying PSQ.5.a–e.

It covers five elements: incident management system implementation; sentinel event identification mechanism; established analysis process for incidents; corrective and preventive actions based on analysis findings; and a process for informing stakeholders in case of a near miss, adverse event or sentinel event.

PSQ.5 owns incident collection, sentinel event identification, incident analysis, CAPA from analysis, and stakeholder communication. PRE.6 handles patient complaints and feedback; a complaint that reveals a clinical incident enters both PSQ.5 and PRE.6. MOM.7 owns medication incidents; PSQ.5 is the general incident system that receives medication incident data.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff at {HOSPITAL} who may witness, be involved in, or need to report an incident, near-miss or sentinel event: treating clinicians, nursing staff, department heads, the {D('Quality Coordinator')}, the patient-safety committee and the Medical Superintendent.

It covers the five objective elements PSQ.5.a–e. It does not cover patient complaints and feedback (PRE.6), medication-specific incident analysis (MOM.7), or the patient-safety and QI programmes as a whole (PSQ.1).

Boundaries with other policies of {HOSPITAL}:

- PRE.6 owns patient complaints and feedback. A complaint that reveals a clinical incident enters both PRE.6 and PSQ.5.
- MOM.7 owns medication incidents. Medication incident data is shared with PSQ.5 for the general incident register.
- PSQ.1 owns the patient-safety programme. PSQ.5 incident trends feed into PSQ.1 opportunity identification.
- PSQ.2 owns indicators. Incident rates may appear as patient-safety indicators under PSQ.2.d.
- ROM.4 owns leadership risk registers. Sentinel events are escalated to ROM.4 where they represent an organisational risk."""

POLICY_STATEMENT = f"""{HOSPITAL} implements an incident management system that captures incidents, near-misses and sentinel events, analyses them through an established process, and drives corrective and preventive actions.

{HOSPITAL} has a mechanism to identify sentinel events and a defined process for root-cause analysis of serious incidents.

{HOSPITAL} has a process for informing stakeholders — including the patient and family, regulatory bodies where required, and internal leadership — in case of a near miss, adverse event or sentinel event.

Honest incident reporting is protected under the culture of safety (PSQ.4.a). This system exists to learn and improve, not to punish reporters."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. An incident management system is implemented and used — incidents are not handled informally without documentation.
2. A mechanism to identify sentinel events exists and is known to all clinical staff.
3. Incidents are analysed through an established process — root-cause analysis for serious incidents, aggregate trend analysis for all incidents.
4. Corrective and preventive actions are taken based on analysis findings — an analysis without action is incomplete.
5. Stakeholders are informed in case of a near miss, adverse event or sentinel event through a defined process — the patient and family are not the last to know.
6. Honest reporting is protected; punitive action for good-faith reporting is prohibited (see PSQ.4.a culture of safety).

Staff who witness or are involved in an incident report it to the {D('Quality Coordinator')} and the treating clinician within {D('the same shift')}."""

STOP_WORK = f"""Any staff member has the authority and the duty to invoke stop-work when a serious adverse event or sentinel event occurs or is imminent.

Stop-work means:

- Quarantine the device, equipment or product involved — remove from service, label and secure for investigation.
- Halt the specific procedure type if there is reason to believe the procedure itself (not only the patient) is the cause, until the Quality Coordinator or Medical Superintendent clears it.
- Secure the scene — do not discard packaging, consumables, syringes or documentation until released by the investigating team.

Emergency patient care continues. Stop-work does not mean abandoning a patient in crisis. Resuscitation, emergency surgery and life-saving treatment proceed while the scene around the event is preserved.

Report to the {D('Quality Coordinator')} and the {D('Medical Superintendent')} the same shift. The Quality Coordinator initiates the incident report and root-cause analysis. The Medical Superintendent decides whether the procedure halt continues beyond the initial stop."""

PROCEDURE_STEPS = [
f"""5.1 Incident management system

{HOSPITAL} implements an incident management system. All incidents — including clinical incidents, near-misses, adverse events and sentinel events — are reported using {D('a standardised incident report form (paper or electronic)')} and entered into the incident register maintained by the {D('Quality Coordinator')}.

The system captures: date, time, location, persons involved, description of what happened, immediate actions taken, severity classification and reporter identity (protected under PSQ.4.a culture of safety). Reports are submitted within {D('the same shift')} of occurrence or discovery. The {D('Quality Coordinator')} acknowledges receipt and initiates classification and investigation within {D('24 hours')}.""",

f"""5.2 Sentinel event identification

{HOSPITAL} has a mechanism to identify sentinel events. A sentinel event is defined as an unexpected occurrence involving death or serious physical or psychological injury, or the risk thereof. The organisation maintains a list of events that are always treated as sentinel, including {D('unexpected death unrelated to the natural course of illness, major permanent loss of function, surgery on the wrong patient or site, retained instrument or sponge after surgery, and infant abduction or discharge to the wrong family')}.

All clinical staff are trained to recognise sentinel events. When a potential sentinel event is identified, it is reported immediately to the {D('Quality Coordinator')} and the {D('Medical Superintendent')}. Stop-work authority applies (see section 6). The event is flagged in the incident register as sentinel and escalated for root-cause analysis.""",

f"""5.3 Incident analysis process

{HOSPITAL} has an established process for analysis of incidents. The analysis method is determined by severity:

- Sentinel events and serious adverse events: root-cause analysis (RCA) conducted by a multi-disciplinary team within {D('72 hours')} of the event, using {D('the five-why method, fishbone diagram or timeline analysis')}.
- Moderate incidents: structured investigation by the department head and the Quality Coordinator within {D('one week')}.
- Near-misses and minor incidents: aggregate trend analysis {D('monthly')} by the Quality Coordinator, reported to the patient-safety committee.

RCA reports include: event description, timeline, contributing factors, root causes identified, and recommended corrective and preventive actions. All analysis records are filed in the incident register.""",

f"""5.4 Corrective and preventive actions

Corrective and preventive actions (CAPA) are taken based on the findings of incident analysis. Each analysis report includes specific actions with a responsible person, target date and expected outcome.

The {D('Quality Coordinator')} tracks CAPA to completion and reports status to the patient-safety committee {D('quarterly')}. Completed actions are verified for effectiveness — has the root cause been addressed? Actions that require resources beyond the department are escalated to management under PSQ.4.c. CAPA that remains open beyond {D('90 days')} triggers escalation to the Medical Superintendent.

Trend analysis of CAPA identifies systemic issues that require programme-level change under PSQ.1.""",

f"""5.5 Informing stakeholders

{HOSPITAL} has a process for informing various stakeholders in case of a near miss, adverse event or sentinel event.

Stakeholders and communication approach:

- Patient and family: the treating clinician informs the patient and/or family about the event, what happened, what is being done and what will be done to prevent recurrence, within {D('24 hours')} of the event or as soon as the patient's condition permits. This is honest disclosure, not a legal admission.
- Internal leadership: the Medical Superintendent is informed of all sentinel events and serious adverse events the same shift. The patient-safety committee receives a summary at its next meeting.
- Regulatory bodies: where reporting is required by law or regulation ({D('e.g. state health authority, drug controller for adverse drug reactions')}), the Medical Superintendent ensures the report is filed within the mandated timeframe.
- Staff involved: feedback on incident investigation findings and CAPA is shared with the reporting staff and involved team to close the learning loop.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Receives immediate notification of sentinel events and serious adverse events.
- Decides whether a procedure halt continues beyond the initial stop.
- Ensures regulatory reporting where required.

Quality Coordinator
- Maintains the incident management system and incident register.
- Classifies incidents, initiates investigation and facilitates RCA.
- Tracks CAPA to completion and reports to the patient-safety committee.

Treating Clinicians
- Report incidents within the same shift.
- Participate in root-cause analysis for events in their practice area.
- Inform the patient and family about adverse events and sentinel events.

Department Heads
- Support investigation and implement department-level CAPA.
- Ensure staff know how to report and recognise sentinel events.

Nursing Staff
- Report incidents and near-misses within the same shift.
- Preserve the scene and quarantine devices under stop-work.

Patient-Safety Committee
- Reviews incident trends, RCA reports and CAPA status."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers the incident management system, analysis, CAPA and stakeholder communication.

What is monitored each quarter:

- Incidents reported and entered into the register with no reporting gaps.
- Sentinel event identification mechanism known to staff and sentinel events flagged correctly.
- Analysis completed within defined timeframes: RCA for serious events, trend analysis for others.
- CAPA assigned, tracked to completion and verified for effectiveness.
- Stakeholder communication completed: patient/family informed, committee briefed, regulatory reports filed where required.

Root-cause analysis is required when incident reporting drops unexpectedly (suggesting under-reporting) or when CAPA remains open beyond {D('90 days')}.

This policy is reviewed {D('annually')}, and sooner when PSQ.1, PSQ.2, PSQ.3 or PSQ.4 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff are trained on incident reporting and this policy at induction and {D('once a year')} after that. Training covers: how to report, sentinel event recognition, the non-punitive reporting culture (PSQ.4.a), stop-work authority, and stakeholder communication expectations.

Staff acknowledgement

I have read this Incident Collection and Analysis for Continual Quality Improvement policy of {HOSPITAL}. I understand how to report incidents, when to invoke stop-work, and the non-punitive reporting culture.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PSQ/POL/05"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Safety and Quality Improvement chapter, standard PSQ.5.
- Internal documents of {HOSPITAL}: incident report forms; incident register; sentinel event list; RCA templates; CAPA tracking register; patient-safety committee minutes (PSQ.1); patient complaints system (PRE.6); medication incident records (MOM.7)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: all clinical areas; nursing stations; emergency department; department heads; patient-safety / QI committee members; pharmacy (cross-reference MOM.7).

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH SHCO chapter 4)
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
QI — quality improvement
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.5.a",
        "requirement": "The organisation implements an incident management system.",
        "steps": "Statement of intent; Section 3; 5.1 Incident management system; Section 4 items 1, 6",
        "responsible": "Quality Coordinator (maintain system); all staff (report); Medical Superintendent (oversight)",
        "records": [
            "Incident management system documentation (forms, register, classification criteria).",
            "Incident reports filed with date, time, description, severity and reporter.",
            "Acknowledgement and classification records within defined timeframes.",
            "Incident register showing all reported events.",
        ],
    },
    {
        "oe_code": "PSQ.5.b",
        "requirement": "The organisation has a mechanism to identify sentinel events.",
        "steps": "Section 3; 5.2 Sentinel event identification; Section 6 Stop-work; Section 4 item 2",
        "responsible": "All clinical staff (identify and report); Quality Coordinator (flag and escalate); Medical Superintendent (receive notification)",
        "records": [
            "Sentinel event definition and list of events always treated as sentinel.",
            "Staff training records on sentinel event recognition.",
            "Sentinel event flags in the incident register with immediate notification records.",
            "Stop-work invocation records where applicable.",
        ],
    },
    {
        "oe_code": "PSQ.5.c",
        "requirement": "The organisation has an established process for analysis of incidents.",
        "steps": "Section 3; 5.3 Incident analysis process; Section 4 item 3",
        "responsible": "Quality Coordinator (facilitate analysis); multi-disciplinary team (RCA); department heads (investigate moderate incidents)",
        "records": [
            "RCA reports for sentinel and serious adverse events with timeline and root causes.",
            "Structured investigation reports for moderate incidents.",
            "Monthly trend analysis reports for near-misses and minor incidents.",
        ],
    },
    {
        "oe_code": "PSQ.5.d",
        "requirement": "Corrective and preventive actions are taken based on the findings of such analysis.",
        "steps": "Section 3; 5.4 Corrective and preventive actions; Section 4 item 4",
        "responsible": "Quality Coordinator (track); department heads (implement); patient-safety committee (review)",
        "records": [
            "CAPA action plans with responsible person, target date and expected outcome.",
            "CAPA tracking register showing completion status and effectiveness verification.",
            "Committee minutes showing CAPA status reviewed quarterly.",
        ],
    },
    {
        "oe_code": "PSQ.5.e",
        "requirement": "The organisation shall have a process for informing various stakeholders in case of a near miss / adverse event / sentinel event.",
        "steps": "Section 3; 5.5 Informing stakeholders; Section 4 item 5",
        "responsible": "Treating clinician (inform patient/family); Medical Superintendent (regulatory reporting); Quality Coordinator (internal communication)",
        "records": [
            "Patient and family disclosure records with date, clinician and content communicated.",
            "Regulatory body notification records where reporting is required by law.",
            "Patient-safety committee meeting minutes showing event summaries received.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PSQ.5 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Incidents are collected and analysed to ensure continual quality improvement" (no terminal period in PDF; our wording adds one). PSQ.5.a–e PDF page 110. PSQ.5.a/b asterisked. PSQ.5.a/b/c/d Commitment; PSQ.5.e Excellence. PDF uses "organization" for PSQ.5.e; our wording uses "organisation".

SHAPE: Five What-we-do subsections (5.1–5.5). WITH stop-work. Disclaimer accreditation-only. PSQ roles only."""


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
        "subtitle": "Incident collection and analysis for continual quality improvement.",
        "doc_no": D("PSQ/POL/05"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "psq5_v2_draft.json",
        "PSQ.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
