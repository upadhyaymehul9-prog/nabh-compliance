# -*- coding: utf-8 -*-
"""Builds the 5 PSQ (Patient Safety and Quality Improvement) SOPs -- plus
their Records and manifest.json -- in the plain-body + audit-appendix
format used for FMS, ROM, AAC, HRM, COP, MOM and PRE (2026-10-13).

Like MOM and PRE, NO SOP/Record pack existed for PSQ before this script:
policies/build/sop_record_masters/PSQ/ is created fresh here. The content
is not invented -- it is drawn directly from the SHCO 3rd Edition PSQ
Master Policy pipeline that was already built and approved for this
hospital (policies/drafts/psq{1..5}_v2_draft.json), which carries the
correct SHCO scope (5 standards, 28 OEs across PSQ.1-PSQ.5), the
already-approved responsibility/record mapping, and NABH citation
wording. This script recasts that content into the plain-body-with-Why-
lines + appendix template -- it is adaptation of already-approved
material into a new template, not fresh authorship of requirements.

Source of truth for every fact below: policies/drafts/psq{N}_v2_draft.json
(fields: scope, policy_statement, procedure_steps, responsibility,
oe_mapping, references_text). Nothing here was invented beyond template
prose (the "Why:" framing lines, which restate the same consequence
already stated in each draft's own text).

Writes:
  policies/build/sop_record_masters/PSQ/SOP_PSQ.N...docx   (5 files)
  policies/build/sop_record_masters/PSQ/Records/PSQ.N_Record_NN_*.docx
  policies/build/sop_record_masters/PSQ/manifest.json
"""
from __future__ import annotations

import json
from pathlib import Path

from sop_record_common import (
    PlainItem,
    SOPSpecV2,
    RecordSpec,
    build_sop_v2,
    build_record,
)

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "PSQ"
RECORDS_ROOT = OUT_ROOT / "Records"

NABH_PSQ_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Patient Safety and Quality Improvement chapter, standard {code}."
)

WHO_NINE_SOLUTIONS_SRC = (
    "World Health Organization. (2007, May 2). [WHO launches 'Nine "
    "patient safety "
    "solutions'](https://www.who.int/news/item/02-05-2007-who-launches-nine-patient-safety-solutions). "
    "Geneva: WHO -- the internationally recognised starting list of "
    "patient-safety goals this hospital adapts and implements."
)
JOINT_COMMISSION_SENTINEL_SRC = (
    "The Joint Commission. (n.d.). [Sentinel "
    "event](https://www.jointcommission.org/resources/sentinel-event/). "
    "Oakbrook Terrace, IL: The Joint Commission -- defines a sentinel "
    "event as a patient safety event that reaches a patient and results "
    "in death, permanent harm, or severe temporary harm; the globally "
    "cited framework this hospital's own always-sentinel event list is "
    "built on. Consulted as general background on the sentinel-event "
    "concept, not as a document this hospital is accredited against."
)
WHO_RCA_CURRICULUM_SRC = (
    "World Health Organization. (2021, February 23). [Multi-professional "
    "patient safety curriculum guide -- Topic 5: Learning from errors to "
    "prevent "
    "harm](https://www.who.int/teams/integrated-health-services/quality-of-care-and-patient-safety/patient-safety-guidance-and-tools/education-and-training/multi-professional-curriculum-guide), "
    "Course 05a: Root cause analysis. Geneva: WHO -- the root-cause-"
    "analysis teaching material this hospital's RCA method (five-whys, "
    "fishbone diagram, timeline analysis) is grounded in."
)

SOPS: list[tuple[str, SOPSpecV2]] = []
RECORDS: list[tuple[str, int, str, RecordSpec]] = []


def _add(sop_code: str, idx: int, spec: RecordSpec, slug: str) -> None:
    RECORDS.append((sop_code, idx, slug, spec))


# ============================================================== PSQ.1 ====
PSQ1 = SOPSpecV2(
    sop_no="SOP-PSQ.1",
    title="Patient-Safety Programme and Quality Improvement Programme",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» runs two multi-disciplinary "
        "programmes -- a patient-safety programme and a quality "
        "improvement programme -- that each identify opportunities at "
        "defined intervals, how proactive risk analysis and adopted "
        "national/international safety goals feed the first, how a "
        "designated coordinator and regular audits drive the second, and "
        "how nursing care quality is monitored and improved as its own "
        "named process."
    ),
    purpose_trigger=(
        "A near-miss happens on a ward and nobody looks at it again until "
        "the same mistake happens for real six months later. This SOP is "
        "what makes sure a standing committee actually reviews safety "
        "opportunities at a defined interval, not only after something "
        "goes wrong twice."
    ),
    purpose_why=(
        "We do this because a patient-safety programme that exists only "
        "as a folder in the quality office protects no one -- these two "
        "programmes have to actually meet, actually review, and actually "
        "act, on a schedule someone can be held to."
    ),
    purpose_text=(
        "To define how «Hospital Name» maintains a patient-safety "
        "programme and a quality improvement programme, each developed "
        "and maintained by "
        "a multi-disciplinary committee, each reviewed for improvement "
        "opportunities at pre-defined intervals, with proactive risk "
        "analysis, adopted national/international safety goals, a "
        "designated QI coordinator, regular audits, and a named process "
        "for monitoring and improving nursing care quality."
    ),
    scope_why="so every department knows which committee owns which part of patient safety and quality, instead of assuming it is someone else's job.",
    scope_text=(
        "Applies to all clinical and non-clinical departments at "
        "«Hospital Name» and to every staff member involved in patient "
        "safety or quality improvement: the patient-safety committee, "
        "the quality improvement committee, the Quality Coordinator, "
        "department heads, treating clinicians, nursing staff and the "
        "Medical Superintendent. It covers how the two programmes "
        "themselves are run. It does not cover how indicator data is "
        "chosen and tracked, how the clinical audit system works as its "
        "own process, how management funds and supports the "
        "programmes, or how an incident is investigated after it "
        "happens -- each of those is set out in its own separate SOP in "
        "this chapter."
    ),
    responsibility_why="a programme that is \"everyone's responsibility\" in practice belongs to no one -- a designated coordinator and a chairing Medical Superintendent are what make sure these programmes actually run on schedule.",
    responsibilities=[
        ("Medical Superintendent (Head of the Institution)", "Chairs or sponsors the patient-safety and QI committees; accountable that both programmes are implemented, not only documented."),
        ("Quality Coordinator", "Designated individual for coordinating and implementing the QI programme; maintains the audit schedule, indicator dashboard and opportunity logs; prepares committee agendas and tracks CAPA to closure."),
        ("Patient-Safety / QI Committee", "Multi-disciplinary body that develops, implements and maintains both programmes; reviews opportunities at pre-defined intervals and approves improvement actions."),
        ("Department Heads", "Participate in committee meetings and own department-level improvement actions; ensure staff cooperate with audits and report risks."),
        ("Nursing In-Charge / Nursing Quality Lead", "Monitors and reports nursing care quality indicators; participates in committee meetings and leads nursing improvement actions."),
        ("Treating Clinicians", "Participate in clinical audits and report patient-safety risks and near-misses."),
    ],
    items=[
        PlainItem(
            heading="Develop, implement and maintain the patient-safety programme through a multi-disciplinary committee",
            why="A patient-safety programme written by one person in an office, without the departments that actually face the risk in the room, misses the risks only the ward floor can see.",
            body=[
                "The patient safety programme is developed, implemented "
                "and maintained by a multi-disciplinary committee.",
                "The patient-safety committee, chaired or sponsored by "
                "the Medical Superintendent, includes «representation "
                "from nursing, medical staff, and at least one other "
                "clinical or support department» and meets «quarterly» "
                "to develop, implement and maintain the programme.",
            ],
            oe_code="PSQ.1.a",
        ),
        PlainItem(
            heading="Identify improvement opportunities at pre-defined intervals",
            why="A programme that only reacts after an incident report arrives is always one step behind -- a defined review interval is what catches a risk before it becomes an incident.",
            body=[
                "The patient safety programme identifies opportunities "
                "for improvement based on review at pre-defined "
                "intervals.",
                "The committee reviews the opportunity log at «each "
                "quarterly meeting». The interval is fixed in the "
                "committee's terms of reference, not left to whenever "
                "there happens to be time.",
            ],
            oe_code="PSQ.1.b",
        ),
        PlainItem(
            heading="Perform proactive analysis of patient-safety risks and act on it",
            why="Waiting for a risk to cause harm before analysing it means the analysis always arrives too late to help the patient it was about.",
            body=[
                "The organisation performs proactive analysis of "
                "patient safety risks and makes improvement "
                "accordingly.",
                "The Quality Coordinator facilitates a proactive risk "
                "analysis -- «failure mode and effects analysis (FMEA) "
                "or an equivalent structured method» -- on at least "
                "«one high-risk process per year», and the committee "
                "approves the resulting actions.",
            ],
            oe_code="PSQ.1.c",
        ),
        PlainItem(
            heading="Adapt and implement national/international patient-safety goals",
            why="A safety goal copied word for word from a large tertiary hospital's programme, without checking whether it even applies to what this hospital actually does, is a goal in name only.",
            body=[
                "The organisation adapts and implements "
                "national/international patient-safety goals/solutions.",
                "The World Health Organization's Nine Patient Safety "
                "Solutions is the internationally recognised starting "
                "list this hospital works from:",
                "1. Telling apart medicines with look-alike or "
                "sound-alike names, so the wrong drug is not picked off "
                "the shelf by mistake.",
                "2. Correctly identifying the patient before any "
                "procedure, test or medicine, using at least two "
                "identifiers.",
                "3. Communicating clearly at every handover between "
                "shifts or departments, so nothing is lost in the "
                "handoff.",
                "4. Performing the correct procedure at the correct "
                "body site, confirmed before the procedure starts.",
                "5. Controlling concentrated electrolyte solutions so "
                "they cannot be given at the wrong strength by "
                "accident.",
                "6. Keeping medication records accurate when a patient "
                "moves between departments or is discharged, so nothing "
                "is missed or duplicated.",
                "7. Avoiding catheter and tubing misconnections, so one "
                "line is never mistakenly connected to the wrong port.",
                "8. Using injection devices only once per patient, "
                "never reused.",
                "9. Improving hand hygiene to prevent "
                "healthcare-associated infection.",
                "The Quality Coordinator checks each solution against "
                "what this hospital actually does -- a solution about a "
                "service this hospital does not provide is a recorded "
                "absence, not an adopted goal in name only -- and the "
                "committee approves and monitors implementation of the "
                "ones that apply.",
            ],
            oe_code="PSQ.1.d",
            technical_sources=[WHO_NINE_SOLUTIONS_SRC],
        ),
        PlainItem(
            heading="Develop, implement and maintain the quality improvement programme through a multi-disciplinary committee",
            why="A quality improvement programme run by one department in isolation cannot see the handoffs between departments where most real quality problems actually happen.",
            body=[
                "A comprehensive quality improvement programme is "
                "developed, implemented and maintained by a "
                "multi-disciplinary committee.",
                "The QI committee, sponsored by the Medical "
                "Superintendent, includes «representation from nursing, "
                "medical staff, and at least one other clinical or "
                "support department» and meets «quarterly» to develop, "
                "implement and maintain the programme. The same "
                "committee may serve both the patient-safety and QI "
                "programmes at a small organisation, provided both "
                "programmes are actually covered.",
            ],
            oe_code="PSQ.1.e",
        ),
        PlainItem(
            heading="Designate an individual to coordinate and implement the QI programme",
            why="A quality programme with no one individually accountable for running it tends to drift to whoever is least busy that week -- which in practice means it does not run at all.",
            body=[
                "There is a designated individual for coordinating and "
                "implementing the quality improvement programme.",
                "The Medical Superintendent appoints a named Quality "
                "Coordinator in writing, with documented responsibility "
                "for the QI programme.",
            ],
            oe_code="PSQ.1.f",
        ),
        PlainItem(
            heading="Identify QI opportunities at pre-defined intervals",
            why="A quality improvement log that is only ever added to and never reviewed is not an improvement process -- it is a list nobody acts on.",
            body=[
                "The quality improvement programme identifies "
                "opportunities for improvement based on review at "
                "pre-defined intervals.",
                "The Quality Coordinator logs QI opportunities with "
                "source, priority and owner; the committee reviews the "
                "log at «each quarterly meeting» and tracks closure.",
            ],
            oe_code="PSQ.1.g",
        ),
        PlainItem(
            heading="Conduct audits at regular intervals as continuous monitoring",
            why="An audit schedule that exists on paper but is never actually run leaves this hospital finding out about a gap only when NABH does.",
            body=[
                "Audits are conducted at regular intervals as a means "
                "of continuous monitoring.",
                "The Quality Coordinator maintains an annual audit "
                "schedule approved by the committee, covering «hand "
                "hygiene, medication safety, documentation and at "
                "least one department-level process». Findings are "
                "tracked to CAPA closure.",
            ],
            oe_code="PSQ.1.h",
            boundary=[
                "The clinical audit system as its own standard -- scope, methodology and frequency across clinical processes -- is owned by the Clinical Audit and Quality Improvement Programmes SOP (PSQ.3); this step is audits used as one monitoring tool within the patient-safety and QI programmes.",
            ],
        ),
        PlainItem(
            heading="Establish a process to monitor and improve nursing care quality",
            why="Nursing care quality folded silently into general ward statistics never gets looked at on its own -- a problem specific to nursing care can hide for months inside numbers that look fine overall.",
            body=[
                "There is an established process in the organisation to "
                "monitor and improve quality of nursing care.",
                "The Nursing In-Charge or nursing quality lead defines "
                "nursing quality indicators -- «pressure-injury rate, "
                "fall rate, medication-administration accuracy» -- with "
                "targets, reports monthly data and trends to the "
                "committee, and leads improvement actions on findings.",
            ],
            oe_code="PSQ.1.i",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-9 (see the PSQ.1 Records folder).",
    related_documents=[
        "Hospital's Key Indicators SOP (PSQ.2)",
        "Hospital's Clinical Audit and Quality Improvement Programmes SOP (PSQ.3)",
        "Hospital's Management Support for Patient Safety and Quality Improvement SOP (PSQ.4)",
        "Hospital's Incident Collection and Analysis SOP (PSQ.5)",
        "Hospital's Leadership ownership of organisational risk SOP (ROM.4)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a quarterly committee "
        "meeting is missed twice running, a proactive risk analysis has "
        "not been done in the preceding year, or the sibling PSQ or ROM "
        "policies this SOP points to are revised."
    ),
    full_reference_list=[
        NABH_PSQ_CITE.format(code="PSQ.1"),
        WHO_NINE_SOLUTIONS_SRC,
    ],
)

SOPS.append(("SOP_PSQ.1.a_to_i_patient_safety_quality_improvement_programme.docx", PSQ1))

# ---- PSQ.1 Records -------------------------------------------------
_add("PSQ.1", 1, RecordSpec(
    oe_code="PSQ.1.a",
    oe_requirement="The patient safety programme is developed, implemented and maintained by a multi-disciplinary committee.",
    record_title="PSQ.1 Record 01 — Patient-safety committee terms of reference and membership",
    what_is_this="This record is the proof the patient-safety committee is actually multi-disciplinary, with named members from nursing, medicine and at least one other department -- not a committee that exists in name only.",
    real_example="The committee's terms of reference list the Medical Superintendent as chair, the Nursing In-Charge, a ward physician and the laboratory lead as members.",
    why_nabh_asks="A patient-safety programme written by one person in an office, without the departments that actually face the risk, misses the risks only the ward floor can see.",
    how_to_fill=[
        ("Member Name", "Full name."),
        ("Department/Role", "Nursing, medical, support department."),
        ("Committee Role", "Chair, member, secretary."),
        ("Date Appointed", "When joined."),
        ("Terms of Reference Version", "Document version."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Member Name", "Department/Role", "Committee Role", "Date Appointed", "Terms of Reference Version"],
    worked_example_row=["WORKED EXAMPLE — Dr. Suresh Nair", "Medical Superintendent", "Chair", "01-Jan-2026", "v2 (01-Jan-2026)"],
), "patient_safety_committee_terms_membership")

_add("PSQ.1", 2, RecordSpec(
    oe_code="PSQ.1.a",
    oe_requirement="The patient safety programme is developed, implemented and maintained by a multi-disciplinary committee.",
    record_title="PSQ.1 Record 02 — Patient-safety committee meeting minutes",
    what_is_this="This record is the proof the committee actually met, who attended, and what was decided -- not a meeting that was scheduled but never held.",
    real_example="Quarterly minutes record attendance, agenda items reviewed, decisions taken and the owner and due date for each follow-up action.",
    why_nabh_asks="A committee that exists on paper but never meets cannot develop, implement or maintain anything.",
    how_to_fill=[
        ("Meeting Date", "Date held."),
        ("Attendance", "Who was present."),
        ("Agenda Items", "What was discussed."),
        ("Decisions / Follow-up Actions", "What was decided and by whom."),
        ("Next Meeting Date", "Scheduled."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Meeting Date", "Attendance", "Agenda Items", "Decisions / Follow-up Actions", "Next Meeting Date"],
    worked_example_row=["WORKED EXAMPLE — 10-Apr-2026", "5 of 5 members", "Programme review; risk analysis update", "Approved Q2 opportunity log; Dr. Nair to review by 30-Apr", "10-Jul-2026"],
), "patient_safety_committee_meeting_minutes")

_add("PSQ.1", 3, RecordSpec(
    oe_code="PSQ.1.b",
    oe_requirement="The patient safety programme identifies opportunities for improvement based on review at pre-defined intervals.",
    record_title="PSQ.1 Record 03 — Patient-safety opportunity log",
    what_is_this="This record is the proof improvement opportunities were actually logged with a source, owner and target date, and reviewed on schedule -- not a list that was started and abandoned.",
    real_example="An opportunity identified from a near-miss report is logged, assigned to the ward in-charge, and closed within the target date.",
    why_nabh_asks="A programme that only reacts after an incident report arrives is always one step behind -- a defined review interval is what catches a risk before it becomes an incident.",
    how_to_fill=[
        ("Date Logged", "When identified."),
        ("Opportunity / Source", "What and where from."),
        ("Owner", "Who is responsible."),
        ("Target Date", "Deadline."),
        ("Status", "Open, in progress, closed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Date Logged", "Opportunity / Source", "Owner", "Target Date", "Status"],
    worked_example_row=["WORKED EXAMPLE — 15-Apr-2026", "IV line mislabelling (near-miss report)", "Ward In-Charge R. Patel", "15-May-2026", "Closed"],
), "patient_safety_opportunity_log")

_add("PSQ.1", 4, RecordSpec(
    oe_code="PSQ.1.c",
    oe_requirement="The organisation performs proactive analysis of patient safety risks and makes improvement accordingly.",
    record_title="PSQ.1 Record 04 — Proactive risk analysis report",
    what_is_this="This record is the proof a structured proactive analysis -- such as FMEA -- was actually performed on a high-risk process, with a risk score and resulting action, not only discussed informally.",
    real_example="An FMEA on the medication-dispensing process identifies a high-risk failure mode (look-alike packaging) and the committee approves a shelf-labelling fix.",
    why_nabh_asks="Waiting for a risk to cause harm before analysing it means the analysis always arrives too late to help the patient it was about.",
    how_to_fill=[
        ("Date", "Date of analysis."),
        ("Process Analysed", "What was studied."),
        ("Method", "FMEA or equivalent."),
        ("Risk Score / Finding", "Result."),
        ("Action Approved", "What was done."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Date", "Process Analysed", "Method", "Risk Score / Finding", "Action Approved"],
    worked_example_row=["WORKED EXAMPLE — 20-Apr-2026", "Medication dispensing", "FMEA", "High risk — look-alike packaging", "Shelf re-labelling and separation implemented"],
), "proactive_risk_analysis_report")

_add("PSQ.1", 5, RecordSpec(
    oe_code="PSQ.1.d",
    oe_requirement="The organisation adapts and implements national/international patient-safety goals/solutions.",
    record_title="PSQ.1 Record 05 — Adopted patient-safety goals and implementation evidence",
    what_is_this="This record is the proof each adopted safety goal was actually checked for relevance to this hospital's real services and then implemented -- not copied wholesale from a larger hospital's programme.",
    real_example="A goal on correct patient identification is adopted and implemented with a two-identifier check at every encounter; a goal on blood-bank safety is recorded as not applicable since the hospital does not run a blood bank.",
    why_nabh_asks="A safety goal copied word for word without checking whether it applies to what this hospital actually does is a goal in name only.",
    how_to_fill=[
        ("Goal", "National/international safety goal considered."),
        ("Relevance to This Hospital", "Applicable or recorded absence with reason."),
        ("Implementation Evidence", "What was done."),
        ("Reviewed By", "Committee."),
        ("Review Date", "When checked."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Goal", "Relevance to This Hospital", "Implementation Evidence", "Reviewed By", "Review Date"],
    worked_example_row=["WORKED EXAMPLE — Correct patient identification", "Applicable", "Two-identifier check at every encounter", "Patient-Safety Committee", "22-Apr-2026"],
), "adopted_safety_goals_implementation_evidence")

_add("PSQ.1", 6, RecordSpec(
    oe_code="PSQ.1.e",
    oe_requirement="A comprehensive quality improvement programme is developed, implemented and maintained by a multi-disciplinary committee.",
    record_title="PSQ.1 Record 06 — QI committee terms of reference and programme document",
    what_is_this="This record is the proof the QI programme has a written scope, objectives and a multi-disciplinary committee behind it -- not an informal arrangement nobody wrote down.",
    real_example="The QI programme document names its scope, objectives and maintenance schedule, with the committee's multi-disciplinary membership attached.",
    why_nabh_asks="A quality improvement programme run by one department in isolation cannot see the handoffs between departments where most real quality problems happen.",
    how_to_fill=[
        ("Document Version", "Version number."),
        ("Scope", "What the programme covers."),
        ("Objectives", "Stated goals."),
        ("Committee Membership", "Reference to membership list."),
        ("Maintenance Schedule", "Review frequency."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Document Version", "Scope", "Objectives", "Committee Membership", "Maintenance Schedule"],
    worked_example_row=["WORKED EXAMPLE — v2 (01-Jan-2026)", "All clinical and non-clinical departments", "Reduce preventable adverse events; improve nursing care quality", "See PSQ.1 Record 01 (shared committee)", "Quarterly"],
), "qi_committee_terms_programme_document")

_add("PSQ.1", 7, RecordSpec(
    oe_code="PSQ.1.f",
    oe_requirement="There is a designated individual for coordinating and implementing the quality improvement programme.",
    record_title="PSQ.1 Record 07 — QI coordinator appointment record",
    what_is_this="This record is the proof a specific named person was actually appointed in writing to coordinate the QI programme -- not a role left informally to whoever picks it up.",
    real_example="A written appointment letter names the Quality Coordinator and lists their documented responsibilities for the QI programme.",
    why_nabh_asks="A quality programme with no one individually accountable for running it tends to drift to whoever is least busy that week.",
    how_to_fill=[
        ("Name", "Appointed coordinator."),
        ("Date Appointed", "When."),
        ("Appointed By", "Medical Superintendent."),
        ("Documented Responsibilities", "Summary."),
        ("Appointment Letter Reference", "Document reference."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Name", "Date Appointed", "Appointed By", "Documented Responsibilities", "Appointment Letter Reference"],
    worked_example_row=["WORKED EXAMPLE — Anjali Deshmukh", "01-Jan-2026", "Dr. Suresh Nair, Medical Superintendent", "Coordinate QI programme; maintain audit schedule and indicator dashboard; track CAPA", "Appointment Letter Ref QI-001"],
), "qi_coordinator_appointment_record")

_add("PSQ.1", 8, RecordSpec(
    oe_code="PSQ.1.g",
    oe_requirement="The quality improvement programme identifies opportunities for improvement based on review at pre-defined intervals.",
    record_title="PSQ.1 Record 08 — QI opportunity log",
    what_is_this="This record is the proof QI opportunities were actually logged with source, priority and owner, and reviewed at each quarterly meeting -- not a list that grows but is never closed.",
    real_example="An opportunity identified from a patient feedback trend is logged, prioritised, assigned, and tracked to closure at the next quarterly meeting.",
    why_nabh_asks="A quality improvement log that is only ever added to and never reviewed is not an improvement process -- it is a list nobody acts on.",
    how_to_fill=[
        ("Date Logged", "When identified."),
        ("Opportunity / Source", "What and where from."),
        ("Priority", "High, medium, low."),
        ("Owner", "Who is responsible."),
        ("Status / Closure Date", "Current state."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Date Logged", "Opportunity / Source", "Priority", "Owner", "Status / Closure Date"],
    worked_example_row=["WORKED EXAMPLE — 25-Apr-2026", "Discharge summary delay (feedback trend)", "Medium", "Dr. Nair", "Closed — 20-Jun-2026"],
), "qi_opportunity_log")

_add("PSQ.1", 9, RecordSpec(
    oe_code="PSQ.1.h",
    oe_requirement="Audits are conducted at regular intervals as a means of continuous monitoring. There is an established process in the organisation to monitor and improve quality of nursing care.",
    record_title="PSQ.1 Record 09 — Audit schedule and nursing-quality indicator tracker",
    what_is_this="This record is the proof the annual audit schedule was actually followed and nursing quality indicators were actually tracked monthly with trend review -- not a schedule and indicator set that exist only as templates.",
    real_example="The audit schedule shows hand hygiene and medication safety audits completed on time; the nursing-quality tracker shows the monthly pressure-injury rate reviewed by the committee.",
    why_nabh_asks="An audit schedule that is never actually run, or nursing quality folded silently into general ward statistics, leaves this hospital finding out about a gap only when NABH does.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Audit Completed (Y/N, Topic)", "Confirmed."),
        ("Nursing Indicator Reported", "Pressure-injury rate, fall rate, medication-administration accuracy."),
        ("Trend Reviewed By Committee (Y/N)", "Confirmed."),
        ("Action (if any)", "Improvement action taken."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.1")],
    column_headers=["Month", "Audit Completed (Y/N, Topic)", "Nursing Indicator Reported", "Trend Reviewed By Committee (Y/N)", "Action (if any)"],
    worked_example_row=["WORKED EXAMPLE — April 2026", "Y — Hand hygiene", "Fall rate: 0.8 per 1,000 patient-days", "Y", "None — within target"],
), "audit_schedule_nursing_quality_tracker")

# ============================================================== PSQ.2 ====
PSQ2 = SOPSpecV2(
    sop_no="SOP-PSQ.2",
    title="Key Indicators for Structures, Processes and Outcomes",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» identifies and monitors "
        "key indicators across four domains -- clinical, infection "
        "control, managerial and patient safety -- and how that indicator "
        "data is actually verified by the quality team and analysed for "
        "improvement opportunities, not just collected and filed."
    ),
    purpose_trigger=(
        "A clinical indicator is collected every month for a year, and "
        "nobody ever looks back at whether it is trending up or down. "
        "This SOP is what makes sure data turns into analysis, and "
        "analysis turns into an action someone owns."
    ),
    purpose_why=(
        "We do this because a dashboard nobody reads is not monitoring -- "
        "an indicator only earns its place if someone actually checks it "
        "against a target and does something when it drifts."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies and monitors key "
        "indicators to oversee clinical, infection-control, managerial "
        "and patient-safety structures, processes and outcomes, and how "
        "that data is regularly verified by the quality team and "
        "analysed to identify improvement opportunities."
    ),
    scope_why="so every department that generates or uses indicator data knows its indicators are actually reviewed, not just reported into a void.",
    scope_text=(
        "Applies to all departments at «Hospital Name» that generate or "
        "use indicator data: clinical departments, the infection-control "
        "function, nursing, administration, the Quality Coordinator and "
        "the patient-safety/QI committee. It covers how key indicators "
        "across all four domains are chosen, tracked and verified. It "
        "does not cover the programmes that act on indicator findings, "
        "the clinical audit system, management support, or incident "
        "analysis -- each of those is set out in its own separate SOP "
        "in this chapter."
    ),
    responsibility_why="indicator data that nobody is named to verify tends to drift silently wrong -- a named quality team checking it is what keeps the numbers trustworthy enough to act on.",
    responsibilities=[
        ("Medical Superintendent", "Accountable that key indicators are identified, monitored and used for improvement."),
        ("Quality Coordinator", "Maintains indicator registers across all four domains; verifies data, performs analysis and presents findings to the committee; tracks identified opportunities to closure through the quality improvement programme."),
        ("Patient-Safety / QI Committee", "Reviews indicator data at pre-defined intervals and approves improvement actions."),
        ("Department Heads", "Ensure timely and accurate data collection for indicators assigned to their department."),
        ("Infection-Control Nurse / Designated Person", "Collects and reports infection-control indicator data."),
        ("Nursing In-Charge", "Supports collection of clinical and patient-safety indicators at ward level."),
    ],
    items=[
        PlainItem(
            heading="Identify and monitor key clinical indicators",
            why="A hospital that cannot point to its own clinical outcome numbers has no way of knowing whether its care is actually getting better, worse, or staying the same.",
            body=[
                "The organisation identifies and monitors key indicators "
                "to oversee the clinical structures, processes and "
                "outcomes.",
                "The clinical indicator register names each indicator's "
                "numerator, denominator, data source, frequency and "
                "target. Department heads collect the data; the "
                "Quality Coordinator consolidates and analyses it; the "
                "committee reviews it at «each quarterly meeting».",
            ],
            oe_code="PSQ.2.a",
        ),
        PlainItem(
            heading="Identify and monitor key infection-control indicators",
            why="An infection-control programme that is not actually measured by its own indicators cannot tell the difference between a programme that is working and one that only looks like it is.",
            body=[
                "The organisation identifies and monitors the key "
                "indicators to oversee infection control activities.",
                "The infection-control indicator register aligns with "
                "the hospital's infection-control programme. The "
                "infection-control nurse or designated person collects "
                "data; the Quality Coordinator consolidates it; the "
                "committee reviews trends and acts on any threshold "
                "breach.",
            ],
            oe_code="PSQ.2.b",
        ),
        PlainItem(
            heading="Identify and monitor key managerial indicators",
            why="A hospital that only measures clinical outcomes and never its own management -- turnaround time, complaint volume, staff vacancy -- is blind to the half of its problems that are administrative, not clinical.",
            body=[
                "The organisation identifies and monitors the key "
                "indicators to oversee the managerial structures, "
                "processes and outcomes.",
                "The managerial indicator register names each "
                "indicator's data source, frequency and responsible "
                "person. Department heads and administration collect "
                "data; the Quality Coordinator consolidates it; the "
                "committee reviews it «quarterly».",
            ],
            oe_code="PSQ.2.c",
        ),
        PlainItem(
            heading="Identify and monitor key patient-safety indicators",
            why="A patient-safety programme that cannot point to its own trend data is relying on impression rather than evidence that safety is actually improving.",
            body=[
                "The organisation identifies and monitors the key "
                "indicators to oversee patient safety activities.",
                "The patient-safety indicator register links directly "
                "to the patient-safety programme. The Quality "
                "Coordinator reports trends «quarterly»; the "
                "patient-safety committee reviews them and triggers a "
                "proactive risk review when an indicator trends "
                "adversely.",
            ],
            oe_code="PSQ.2.d",
            boundary=[
                "The patient-safety programme itself and its proactive risk analysis method are owned by PSQ.1; this step is the indicator data that feeds that programme.",
            ],
        ),
        PlainItem(
            heading="Verify data regularly and analyse it for improvement opportunities",
            why="An indicator built on data nobody ever checked for errors can point this hospital in exactly the wrong direction -- a wrong number acted on confidently is worse than no number at all.",
            body=[
                "Data is regularly verified by the quality team and is "
                "analysed to identify opportunities for improvement.",
                "The Quality Coordinator or quality team verifies a "
                "sample of indicator data «monthly» against source "
                "records, documents what was checked and any "
                "correction made, and analyses trends to identify "
                "opportunities. Identified opportunities are traced "
                "into the quality improvement programme's opportunity "
                "log for review at the committee's next meeting.",
            ],
            oe_code="PSQ.2.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the PSQ.2 Records folder).",
    related_documents=[
        "Hospital's Patient-Safety Programme and Quality Improvement Programme SOP (PSQ.1)",
        "Hospital's Clinical Audit and Quality Improvement Programmes SOP (PSQ.3)",
        "Hospital's Incident Collection and Analysis SOP (PSQ.5)",
        "Hospital's Leadership ownership of organisational risk SOP (ROM.4)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a data verification "
        "check finds a sustained error in an indicator register, or if "
        "a related policy named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_PSQ_CITE.format(code="PSQ.2"),
    ],
)

SOPS.append(("SOP_PSQ.2.a_to_e_key_indicators_structures_processes_outcomes.docx", PSQ2))

# ---- PSQ.2 Records -------------------------------------------------
_add("PSQ.2", 1, RecordSpec(
    oe_code="PSQ.2.a",
    oe_requirement="The organisation identifies and monitors key indicators to oversee the clinical structures, processes and outcomes.",
    record_title="PSQ.2 Record 01 — Clinical indicator register",
    what_is_this="This record is the proof each clinical indicator actually has a numerator, denominator, data source, frequency and target defined -- not just a name with no way to measure it.",
    real_example="The register defines \"surgical site infection rate\" with its numerator (SSI cases), denominator (surgeries performed), monthly frequency and a target below 2%.",
    why_nabh_asks="A hospital that cannot point to its own clinical outcome numbers has no way of knowing whether its care is actually getting better, worse, or staying the same.",
    how_to_fill=[
        ("Indicator Name", "What is measured."),
        ("Numerator / Denominator", "Definition."),
        ("Data Source", "Where data comes from."),
        ("Frequency", "How often collected."),
        ("Target", "Defined threshold."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Indicator Name", "Numerator / Denominator", "Data Source", "Frequency", "Target"],
    worked_example_row=["WORKED EXAMPLE — Surgical site infection rate", "SSI cases / surgeries performed", "OT register + ward follow-up", "Monthly", "< 2%"],
), "clinical_indicator_register")

_add("PSQ.2", 2, RecordSpec(
    oe_code="PSQ.2.a",
    oe_requirement="The organisation identifies and monitors key indicators to oversee the clinical structures, processes and outcomes.",
    record_title="PSQ.2 Record 02 — Monthly clinical indicator data sheet",
    what_is_this="This record is the proof clinical indicator data was actually collected every month and reviewed by the committee -- not a register that exists with no data behind it.",
    real_example="The April data sheet shows the surgical site infection rate at 1.5%, within target, reviewed at the quarterly committee meeting.",
    why_nabh_asks="A register with no monthly data behind it is a template, not a monitoring system.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Indicator", "Which one."),
        ("Value", "Measured result."),
        ("Within Target (Y/N)", "Confirmed."),
        ("Reviewed By Committee (Y/N, Date)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Month", "Indicator", "Value", "Within Target (Y/N)", "Reviewed By Committee (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — April 2026", "Surgical site infection rate", "1.5%", "Y", "Y — 10-Jul-2026"],
), "monthly_clinical_indicator_data_sheet")

_add("PSQ.2", 3, RecordSpec(
    oe_code="PSQ.2.b",
    oe_requirement="The organisation identifies and monitors the key indicators to oversee infection control activities.",
    record_title="PSQ.2 Record 03 — Infection-control indicator register and monthly data",
    what_is_this="This record is the proof infection-control indicators are actually defined, aligned to the infection-control programme, and tracked monthly -- not assumed covered because a programme exists.",
    real_example="Hand hygiene compliance is tracked monthly at 88%, below the 90% target, triggering a committee-reviewed action.",
    why_nabh_asks="An infection-control programme that is not actually measured by its own indicators cannot tell the difference between a programme that is working and one that only looks like it is.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Indicator", "Hand hygiene, SSI, catheter-associated infection, etc."),
        ("Value", "Measured result."),
        ("Threshold Breached (Y/N)", "Confirmed."),
        ("Action Taken (if breached)", "What was done."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Month", "Indicator", "Value", "Threshold Breached (Y/N)", "Action Taken (if breached)"],
    worked_example_row=["WORKED EXAMPLE — April 2026", "Hand hygiene compliance", "88%", "Y — below 90% target", "Re-training session scheduled for ward staff"],
), "infection_control_indicator_register_monthly_data")

_add("PSQ.2", 4, RecordSpec(
    oe_code="PSQ.2.c",
    oe_requirement="The organisation identifies and monitors the key indicators to oversee the managerial structures, processes and outcomes.",
    record_title="PSQ.2 Record 04 — Managerial indicator register and periodic data",
    what_is_this="This record is the proof managerial indicators -- not only clinical ones -- are actually defined and tracked, with a data source and responsible person for each.",
    real_example="Average outpatient waiting time is tracked quarterly at 35 minutes, reviewed against a 30-minute target.",
    why_nabh_asks="A hospital that only measures clinical outcomes and never its own management is blind to the half of its problems that are administrative, not clinical.",
    how_to_fill=[
        ("Indicator", "What is measured."),
        ("Data Source / Responsible Person", "Where from and who."),
        ("Frequency", "How often."),
        ("Period Value", "Measured result."),
        ("Reviewed By Committee (Y/N, Date)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Indicator", "Data Source / Responsible Person", "Frequency", "Period Value", "Reviewed By Committee (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — Average OPD waiting time", "Registration log / Front-office In-Charge", "Quarterly", "35 minutes (target: 30)", "Y — 10-Jul-2026"],
), "managerial_indicator_register_periodic_data")

_add("PSQ.2", 5, RecordSpec(
    oe_code="PSQ.2.d",
    oe_requirement="The organisation identifies and monitors the key indicators to oversee patient safety activities.",
    record_title="PSQ.2 Record 05 — Patient-safety indicator register and trend report",
    what_is_this="This record is the proof patient-safety indicators are actually linked to the patient-safety programme and reported in trend form -- not single data points with no comparison over time.",
    real_example="The fall-rate indicator, reported quarterly, shows a rising trend that triggers a proactive risk review under the patient-safety programme.",
    why_nabh_asks="A patient-safety programme that cannot point to its own trend data is relying on impression rather than evidence that safety is actually improving.",
    how_to_fill=[
        ("Quarter", "Reporting period."),
        ("Indicator", "What is measured."),
        ("Value", "Measured result."),
        ("Trend (Up/Down/Stable)", "Compared to prior quarter."),
        ("Proactive Risk Review Triggered (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Quarter", "Indicator", "Value", "Trend (Up/Down/Stable)", "Proactive Risk Review Triggered (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — Q2 2026", "Fall rate", "1.2 per 1,000 patient-days", "Up from 0.8", "Y — referred to PSQ.1.c"],
), "patient_safety_indicator_register_trend_report")

_add("PSQ.2", 6, RecordSpec(
    oe_code="PSQ.2.e",
    oe_requirement="Data is regularly verified by the quality team and is analysed to identify the opportunities for improvement.",
    record_title="PSQ.2 Record 06 — Data verification log",
    what_is_this="This record is the proof indicator data was actually checked against source records for accuracy -- not assumed correct because it was reported.",
    real_example="A monthly sample check of the surgical site infection rate against OT and ward records finds one miscounted case and corrects it.",
    why_nabh_asks="An indicator built on data nobody ever checked for errors can point this hospital in exactly the wrong direction.",
    how_to_fill=[
        ("Date", "Date of verification."),
        ("Indicator Checked", "Which one."),
        ("Verifier", "Quality Coordinator or team member."),
        ("Issues Found", "Discrepancy, if any."),
        ("Resolution", "Correction made."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Date", "Indicator Checked", "Verifier", "Issues Found", "Resolution"],
    worked_example_row=["WORKED EXAMPLE — 05-May-2026", "Surgical site infection rate", "Quality Coordinator A. Deshmukh", "One case miscounted in April data", "Corrected and re-reported"],
), "data_verification_log")

_add("PSQ.2", 7, RecordSpec(
    oe_code="PSQ.2.e",
    oe_requirement="Data is regularly verified by the quality team and is analysed to identify the opportunities for improvement.",
    record_title="PSQ.2 Record 07 — Indicator analysis and improvement-opportunity trace",
    what_is_this="This record is the proof indicator trends were actually analysed and, where warranted, traced into the QI opportunity log -- not left as a chart nobody acted on.",
    real_example="Analysis of a rising OPD waiting-time trend identifies a registration bottleneck, logged as a QI opportunity and assigned an owner.",
    why_nabh_asks="A chart that is produced but never acted on is analysis in name only.",
    how_to_fill=[
        ("Date", "Date of analysis."),
        ("Indicator(s) Analysed", "What was reviewed."),
        ("Finding", "Trend or pattern identified."),
        ("Opportunity Identified (Y/N)", "Confirmed."),
        ("QI Opportunity Log Reference (if any)", "Cross-reference."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.2")],
    column_headers=["Date", "Indicator(s) Analysed", "Finding", "Opportunity Identified (Y/N)", "QI Opportunity Log Reference (if any)"],
    worked_example_row=["WORKED EXAMPLE — 12-May-2026", "OPD waiting time", "Rising trend linked to registration bottleneck at peak hours", "Y", "QI Opportunity Log entry 25-Apr-2026"],
), "indicator_analysis_improvement_opportunity_trace")

# ============================================================== PSQ.3 ====
PSQ3 = SOPSpecV2(
    sop_no="SOP-PSQ.3",
    title="Clinical Audit and Quality Improvement Programmes",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» runs clinical audits "
        "against defined parameters, with medical and nursing staff "
        "actually participating as auditors rather than only being "
        "audited, how remedial measures are tracked to completion, and "
        "how quality improvement projects are run as their own "
        "structured exercise."
    ),
    purpose_trigger=(
        "An audit finds a documentation gap, writes it up, and files the "
        "report -- and six months later the same gap is found again "
        "because nobody ever checked whether the remedial measure "
        "actually happened. This SOP is what makes sure an audit finding "
        "is tracked until it is closed, not just written down."
    ),
    purpose_why=(
        "We do this because an audit conducted entirely by the quality "
        "department, on parameters nobody approved in advance, with "
        "findings that are never followed up, produces a report but not "
        "an improvement."
    ),
    purpose_text=(
        "To define how «Hospital Name» conducts clinical audits with "
        "defined parameters and medical and nursing staff participation, "
        "tracks remedial measures to completion, and undertakes quality "
        "improvement projects."
    ),
    scope_why="so every clinical department knows audits are a shared clinical responsibility, not something done to them by the quality office alone.",
    scope_text=(
        "Applies to all clinical departments at «Hospital Name» and to "
        "medical staff, nursing staff, the Quality Coordinator and the "
        "patient-safety/QI committee. It covers how clinical audits and "
        "quality improvement projects are actually run. It does not "
        "cover the patient-safety and QI programmes as a whole, how "
        "indicator data is chosen and tracked, how management funds and "
        "supports the programmes, or how an incident is investigated "
        "after it happens -- each of those is set out in its own "
        "separate SOP in this chapter."
    ),
    responsibility_why="an audit system where only the quality department ever audits is not the multi-disciplinary participation NABH asks for -- clinicians have to actually be in the audit team, not just the subject of it.",
    responsibilities=[
        ("Medical Superintendent", "Accountable that the clinical audit system and QI projects are implemented."),
        ("Quality Coordinator", "Maintains the audit plan, audit reports and QI project register; tracks remedial measures and re-audits to completion; reports to the QI committee."),
        ("Patient-Safety / QI Committee", "Approves the annual audit plan and QI project charters; reviews findings, remedial measures and project outcomes."),
        ("Treating Clinicians (Medical Staff)", "Serve as audit leads or team members; own clinical findings."),
        ("Nursing Staff", "Participate in audits relevant to nursing care and documentation."),
        ("Department Heads", "Support audit access and implement department-level remedial measures."),
    ],
    items=[
        PlainItem(
            heading="Perform and document clinical audits to improve patient care",
            why="An audit that is done but never written down leaves no trail to check whether the same problem comes back later.",
            body=[
                "Clinical audits are performed to improve the quality "
                "of patient care and documented.",
                "Each audit report names the topic, criteria, method, "
                "findings and remedial measures, filed by the Quality "
                "Coordinator and reviewed by the committee.",
            ],
            oe_code="PSQ.3.a",
        ),
        PlainItem(
            heading="Define the audit parameters before data collection",
            why="An audit that starts collecting data before anyone agreed what \"good\" looks like cannot tell a real finding from an opinion formed after the fact.",
            body=[
                "The parameters to be audited are defined by the "
                "organisation.",
                "The annual audit plan names topics, parameters, "
                "frequency and auditors, approved by the committee "
                "before the audit year begins. An ad-hoc audit "
                "requested mid-year states its rationale and "
                "parameters up front, the same way.",
            ],
            oe_code="PSQ.3.b",
        ),
        PlainItem(
            heading="Ensure medical and nursing staff participate in the audit system",
            why="An audit team made up entirely of the quality department, auditing clinicians from the outside, misses the clinical judgement only a treating doctor or nurse can bring to reading the finding correctly.",
            body=[
                "Medical and nursing staff participate in this system.",
                "Each audit team includes at least one treating "
                "clinician and, where the topic involves nursing care "
                "or documentation, at least one nurse. The Quality "
                "Coordinator ensures this participation before the "
                "audit begins, not after.",
            ],
            oe_code="PSQ.3.c",
        ),
        PlainItem(
            heading="Implement remedial measures and track them to completion",
            why="A remedial action that is agreed in a meeting and never checked again is indistinguishable from a remedial action that was never agreed at all.",
            body=[
                "Remedial measures are implemented.",
                "Each finding's remedial measure has a named "
                "responsible person and target date, tracked by the "
                "Quality Coordinator to completion. A re-audit confirms "
                "the improvement; a gap that persists is escalated to "
                "the committee rather than quietly dropped.",
            ],
            oe_code="PSQ.3.d",
        ),
        PlainItem(
            heading="Undertake quality improvement projects",
            why="A chronic problem that keeps surfacing in audit after audit needs a structured project to actually fix it, not another audit that documents the same gap one more time.",
            body=[
                "The organisation undertakes quality improvement "
                "projects.",
                "A QI project charter names the problem statement, aim, "
                "measures and intervention, approved by the committee. "
                "The Quality Coordinator registers and facilitates each "
                "project; the outcome report states results and a plan "
                "for sustaining the gain.",
            ],
            oe_code="PSQ.3.e",
            boundary=[
                "QI project governance sits under the quality improvement programme (PSQ.1.e-g); this step is the project method itself.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the PSQ.3 Records folder).",
    related_documents=[
        "Hospital's Patient-Safety Programme and Quality Improvement Programme SOP (PSQ.1)",
        "Hospital's Key Indicators SOP (PSQ.2)",
        "Hospital's Management Support for Patient Safety and Quality Improvement SOP (PSQ.4)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an audit team is "
        "found to have no clinician member, a remedial measure is found "
        "untracked past its target date, or a related policy named "
        "above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_PSQ_CITE.format(code="PSQ.3"),
    ],
)

SOPS.append(("SOP_PSQ.3.a_to_e_clinical_audit_quality_improvement_programmes.docx", PSQ3))

# ---- PSQ.3 Records -------------------------------------------------
_add("PSQ.3", 1, RecordSpec(
    oe_code="PSQ.3.a",
    oe_requirement="Clinical audits are performed to improve the quality of patient care and documented.",
    record_title="PSQ.3 Record 01 — Clinical audit report",
    what_is_this="This record is the proof an audit was actually performed and written up with topic, criteria, method, findings and remedial measures -- not a verbal discussion that left no trail.",
    real_example="An audit of discharge-summary completeness finds 3 of 20 sampled summaries missing the follow-up plan, with a remedial measure assigned to the ward doctor.",
    why_nabh_asks="An audit that is done but never written down leaves no trail to check whether the same problem comes back later.",
    how_to_fill=[
        ("Audit Topic", "What was audited."),
        ("Criteria", "What standard was checked against."),
        ("Method / Sample Size", "How it was done."),
        ("Findings", "Result."),
        ("Remedial Measures", "What was decided."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.3")],
    column_headers=["Audit Topic", "Criteria", "Method / Sample Size", "Findings", "Remedial Measures"],
    worked_example_row=["WORKED EXAMPLE — Discharge summary completeness", "Follow-up plan present in every summary", "Retrospective review, 20 summaries", "3 of 20 missing follow-up plan", "Doctor training on discharge template; re-audit in 3 months"],
), "clinical_audit_report")

_add("PSQ.3", 2, RecordSpec(
    oe_code="PSQ.3.b",
    oe_requirement="The parameters to be audited are defined by the organisation.",
    record_title="PSQ.3 Record 02 — Annual audit plan",
    what_is_this="This record is the proof audit topics and parameters were actually defined and approved before the audit year began -- not chosen on the fly as audits happened.",
    real_example="The approved annual plan lists discharge-summary completeness, medication-chart accuracy and hand-hygiene compliance as the year's audit topics, each with defined parameters and auditors.",
    why_nabh_asks="An audit that starts collecting data before anyone agreed what \"good\" looks like cannot tell a real finding from an opinion formed after the fact.",
    how_to_fill=[
        ("Audit Topic", "Planned topic."),
        ("Parameters", "What will be checked."),
        ("Frequency", "How often."),
        ("Assigned Auditor(s)", "Named."),
        ("Committee Approval Date", "When approved."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.3")],
    column_headers=["Audit Topic", "Parameters", "Frequency", "Assigned Auditor(s)", "Committee Approval Date"],
    worked_example_row=["WORKED EXAMPLE — Medication-chart accuracy", "Dose, route, time correctly recorded", "Quarterly", "Dr. Nair, Nursing In-Charge R. Patel", "15-Jan-2026"],
), "annual_audit_plan")

_add("PSQ.3", 3, RecordSpec(
    oe_code="PSQ.3.c",
    oe_requirement="Medical and nursing staff participates in this system.",
    record_title="PSQ.3 Record 03 — Audit team composition record",
    what_is_this="This record is the proof each audit team actually included a treating clinician or nurse, not a team made up entirely of the quality department.",
    real_example="The audit team for discharge-summary completeness lists a ward doctor and the Quality Coordinator as joint auditors.",
    why_nabh_asks="An audit team made up entirely of the quality department, auditing clinicians from the outside, misses the clinical judgement only a treating doctor or nurse can bring to reading the finding correctly.",
    how_to_fill=[
        ("Audit Topic", "Which audit."),
        ("Team Members", "Named, with role."),
        ("Clinician/Nurse Member (Y/N)", "Confirmed."),
        ("Date", "Audit date."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.3")],
    column_headers=["Audit Topic", "Team Members", "Clinician/Nurse Member (Y/N)", "Date"],
    worked_example_row=["WORKED EXAMPLE — Discharge summary completeness", "Dr. Varma (ward doctor), Quality Coordinator A. Deshmukh", "Y", "05-May-2026"],
), "audit_team_composition_record")

_add("PSQ.3", 4, RecordSpec(
    oe_code="PSQ.3.d",
    oe_requirement="Remedial measures are implemented.",
    record_title="PSQ.3 Record 04 — Remedial measure tracking and re-audit log",
    what_is_this="This record is the proof a remedial measure was actually tracked to completion and confirmed by re-audit, or escalated if the gap persisted -- not an action item that was agreed and forgotten.",
    real_example="A remedial measure on discharge-summary completeness is tracked to completion; the re-audit three months later finds 0 of 20 summaries missing the follow-up plan.",
    why_nabh_asks="A remedial action that is agreed in a meeting and never checked again is indistinguishable from a remedial action that was never agreed at all.",
    how_to_fill=[
        ("Finding", "What was found."),
        ("Remedial Measure / Owner / Target Date", "Action and accountability."),
        ("Completion Status", "Done, in progress, overdue."),
        ("Re-audit Result (if done)", "Confirmed improvement or not."),
        ("Escalated If Gap Persists (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.3")],
    column_headers=["Finding", "Remedial Measure / Owner / Target Date", "Completion Status", "Re-audit Result (if done)", "Escalated If Gap Persists (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — Missing follow-up plan in discharge summaries", "Doctor training on template; Dr. Varma / 05-Aug-2026", "Done", "0 of 20 missing at re-audit", "N"],
), "remedial_measure_tracking_re_audit_log")

_add("PSQ.3", 5, RecordSpec(
    oe_code="PSQ.3.e",
    oe_requirement="The organisation undertakes quality improvement projects.",
    record_title="PSQ.3 Record 05 — QI project charter",
    what_is_this="This record is the proof a QI project actually has a defined problem statement, aim, measures and intervention approved by the committee -- not a project that started without a plan.",
    real_example="A QI project charter on reducing OPD waiting time names the problem, a target of 30 minutes, the measure used, and the intervention (a second registration counter at peak hours).",
    why_nabh_asks="A chronic problem that keeps surfacing in audit after audit needs a structured project to actually fix it, not another audit that documents the same gap one more time.",
    how_to_fill=[
        ("Project Title", "Name."),
        ("Problem Statement / Aim", "What and target."),
        ("Measure", "How progress is tracked."),
        ("Intervention", "What was done."),
        ("Committee Approval Date", "When chartered."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.3")],
    column_headers=["Project Title", "Problem Statement / Aim", "Measure", "Intervention", "Committee Approval Date"],
    worked_example_row=["WORKED EXAMPLE — Reducing OPD waiting time", "Average wait 45 min; aim to reach 30 min", "Average waiting time per week", "Second registration counter opened 9am-12pm", "20-May-2026"],
), "qi_project_charter")

_add("PSQ.3", 6, RecordSpec(
    oe_code="PSQ.3.e",
    oe_requirement="The organisation undertakes quality improvement projects.",
    record_title="PSQ.3 Record 06 — QI project outcome report and register",
    what_is_this="This record is the proof a QI project's outcome was actually measured against its aim, with a plan for keeping the gain -- not a project that was declared done without checking the result.",
    real_example="The OPD waiting-time project outcome report shows the average wait fell to 28 minutes, with the second counter made a permanent peak-hour fixture to sustain the gain.",
    why_nabh_asks="A project that is declared finished without measuring its actual result cannot tell this hospital whether anything really improved.",
    how_to_fill=[
        ("Project Title", "Name."),
        ("Result Achieved", "Measured outcome."),
        ("Aim Met (Y/N)", "Confirmed."),
        ("Sustainability Plan", "How the gain is kept."),
        ("Register Entry Date", "When closed and logged."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.3")],
    column_headers=["Project Title", "Result Achieved", "Aim Met (Y/N)", "Sustainability Plan", "Register Entry Date"],
    worked_example_row=["WORKED EXAMPLE — Reducing OPD waiting time", "Average wait reduced to 28 minutes", "Y", "Second counter made permanent fixture 9am-12pm", "15-Aug-2026"],
), "qi_project_outcome_report_register")

# ============================================================== PSQ.4 ====
PSQ4 = SOPSpecV2(
    sop_no="SOP-PSQ.4",
    title="Management Support for Patient Safety and Quality Improvement",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» management actually "
        "supports the patient-safety and QI programmes it has set up -- "
        "building a non-punitive culture of safety, making sure leaders "
        "at every level understand the programme's intent, earmarking "
        "real budget for it, and acting on the feedback staff give "
        "about it."
    ),
    purpose_trigger=(
        "A nurse who reports a near-miss is quietly blamed for it in the "
        "next shift handover. This SOP is what makes sure that does not "
        "happen -- a non-punitive reporting culture is something "
        "management builds and sustains on purpose, not something that "
        "is assumed to exist."
    ),
    purpose_why=(
        "We do this because a patient-safety programme with no budget, "
        "no leadership awareness and a punitive culture around reporting "
        "exists in name only -- management support is what turns the "
        "programme from a document into something staff actually trust."
    ),
    purpose_text=(
        "To define how management at «Hospital Name» creates a culture "
        "of safety, ensures leaders at all levels are aware of the "
        "patient-safety and quality improvement programme's intent and "
        "implementation approach, makes available and earmarks adequate "
        "resources for the programme, and uses workforce feedback to "
        "improve it."
    ),
    scope_why="so every leader in this hospital, not only the Medical Superintendent, knows they are expected to actively support these programmes.",
    scope_text=(
        "Applies to the Medical Superintendent, department heads, the "
        "Quality Coordinator and all leaders at «Hospital Name» who "
        "have a role in supporting patient safety and quality "
        "improvement. It covers how management actually supports the "
        "programmes -- culture, awareness, resources and feedback. It "
        "does not cover how the programmes themselves are run, how "
        "indicator data is chosen and tracked, how the clinical audit "
        "system works, or how an incident is investigated -- each of "
        "those is set out in its own separate SOP in this chapter."
    ),
    responsibility_why="support that is assumed to come from \"management\" in the abstract, with no named accountability, tends not to show up when the budget is actually being decided.",
    responsibilities=[
        ("Medical Superintendent (Head of the Institution)", "Creates and sustains a culture of safety at the institutional level; approves resource allocation and earmarked budget for the programmes; ensures leaders at all levels are aware of programme intent."),
        ("Quality Coordinator", "Prepares resource plans and presents to management; facilitates leadership briefings and awareness orientation; collects and consolidates workforce feedback for committee review."),
        ("Department Heads", "Demonstrate culture of safety within their departments; participate in programme awareness activities; report resource shortfalls and relay workforce feedback upward."),
        ("Patient-Safety / QI Committee", "Reviews workforce feedback and recommends programme improvements; reports resource gaps to management."),
    ],
    items=[
        PlainItem(
            heading="Create a culture of safety",
            why="A staff member who is blamed for reporting a near-miss will simply stop reporting -- and a hospital that cannot see its near-misses cannot prevent the real incident that follows.",
            body=[
                "The management creates a culture of safety.",
                "A non-punitive reporting policy is communicated at "
                "induction and «annually», management attends "
                "patient-safety committee meetings, and staff who "
                "report a safety concern receive feedback on what "
                "management did with it.",
            ],
            oe_code="PSQ.4.a",
            boundary=[
                "Leadership ownership of organisational risk more broadly is owned by ROM.4; this step is the culture of safety specific to patient-safety reporting.",
            ],
        ),
        PlainItem(
            heading="Ensure leaders at all levels are aware of the programme's intent and approach",
            why="A department head who has never heard what the QI programme is actually trying to achieve cannot lead their team toward it, however good the programme document is.",
            body=[
                "The leaders at all levels in the organisation are "
                "aware of the intent of the patient safety quality "
                "improvement programme and the approach to its "
                "implementation.",
                "The Quality Coordinator facilitates an annual "
                "leadership briefing with attendance recorded and each "
                "leader's documented acknowledgement of the programme's "
                "intent and approach. A newly appointed leader receives "
                "this orientation within «30 days» of appointment.",
            ],
            oe_code="PSQ.4.b",
        ),
        PlainItem(
            heading="Make available and earmark adequate resources",
            why="A programme management says it supports but never actually funds is a programme that will quietly starve the moment a budget decision has to be made.",
            body=[
                "The management makes available adequate resources "
                "required for the patient safety and quality "
                "improvement programme, and earmarks adequate funds "
                "from its annual budget in this regard.",
                "The Quality Coordinator prepares an annual resource "
                "plan; the Medical Superintendent approves a budget "
                "line item or identified allocation. A resource "
                "shortfall that compromises programme effectiveness is "
                "escalated in writing, not absorbed silently.",
            ],
            oe_code="PSQ.4.c",
        ),
        PlainItem(
            heading="Use workforce feedback to improve the programme",
            why="A suggestion box that is collected but never opened tells staff their input does not actually matter -- and they stop giving it.",
            body=[
                "The management uses the feedback obtained from the "
                "workforce to improve patient safety and quality "
                "improvement programme.",
                "The Quality Coordinator collects workforce feedback "
                "through «surveys, a suggestion box, and staff meeting "
                "notes», consolidates it for the committee, and the "
                "committee's resulting actions are communicated back to "
                "staff.",
            ],
            oe_code="PSQ.4.d",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the PSQ.4 Records folder).",
    related_documents=[
        "Hospital's Patient-Safety Programme and Quality Improvement Programme SOP (PSQ.1)",
        "Hospital's Leadership ownership of organisational risk SOP (ROM.4)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a staff member "
        "reports feeling penalised for a safety report, the annual "
        "leadership briefing is missed, or a related policy named "
        "above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_PSQ_CITE.format(code="PSQ.4"),
    ],
)

SOPS.append(("SOP_PSQ.4.a_to_d_management_support_patient_safety_quality_improvement.docx", PSQ4))

# ---- PSQ.4 Records -------------------------------------------------
_add("PSQ.4", 1, RecordSpec(
    oe_code="PSQ.4.a",
    oe_requirement="The management creates a culture of safety.",
    record_title="PSQ.4 Record 01 — Non-punitive reporting communication and management participation record",
    what_is_this="This record is the proof the non-punitive reporting policy was actually communicated, management actually attended committee meetings, and a reporting staff member actually got feedback -- not a policy that exists only on paper.",
    real_example="The non-punitive policy is communicated at induction and the annual refresher; the Medical Superintendent attends 3 of 4 quarterly committee meetings this year.",
    why_nabh_asks="A staff member who is blamed for reporting a near-miss will simply stop reporting -- and a hospital that cannot see its near-misses cannot prevent the real incident that follows.",
    how_to_fill=[
        ("Date", "Date of activity."),
        ("Activity", "Induction briefing, annual refresher, committee attendance."),
        ("Attended/Communicated By", "Who."),
        ("Staff Feedback Given (Y/N/NA)", "If a report was followed up."),
        ("Notes", "Any detail."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.4")],
    column_headers=["Date", "Activity", "Attended/Communicated By", "Staff Feedback Given (Y/N/NA)", "Notes"],
    worked_example_row=["WORKED EXAMPLE — 10-Jul-2026", "Quarterly committee meeting", "Medical Superintendent Dr. Nair attended", "Y — nurse who reported near-miss told of shelf re-labelling action", "None"],
), "non_punitive_reporting_management_participation_record")

_add("PSQ.4", 2, RecordSpec(
    oe_code="PSQ.4.b",
    oe_requirement="The leaders at all levels in the organisation are aware of the intent of the patient safety quality improvement programme and the approach to its implementation.",
    record_title="PSQ.4 Record 02 — Leadership briefing and acknowledgement record",
    what_is_this="This record is the proof every leader actually attended a briefing and acknowledged understanding the programme's intent -- not assumed aware because they hold a leadership title.",
    real_example="The annual leadership briefing is attended by all 8 department heads, each signing an acknowledgement of the programme's intent and approach.",
    why_nabh_asks="A department head who has never heard what the QI programme is actually trying to achieve cannot lead their team toward it, however good the programme document is.",
    how_to_fill=[
        ("Leader Name", "Named."),
        ("Department", "Theirs."),
        ("Briefing Date", "When attended."),
        ("Acknowledgement Signed (Y/N)", "Confirmed."),
        ("New Leader — Orientation Within 30 Days (Y/N/NA)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.4")],
    column_headers=["Leader Name", "Department", "Briefing Date", "Acknowledgement Signed (Y/N)", "New Leader — Orientation Within 30 Days (Y/N/NA)"],
    worked_example_row=["WORKED EXAMPLE — Dr. Priya Shah", "Laboratory", "15-Jan-2026", "Y", "NA"],
), "leadership_briefing_acknowledgement_record")

_add("PSQ.4", 3, RecordSpec(
    oe_code="PSQ.4.c",
    oe_requirement="The management makes available adequate resources required for patient safety and quality improvement programme, earmarks adequate funds from its annual budget in this regard.",
    record_title="PSQ.4 Record 03 — Annual resource plan and budget allocation record",
    what_is_this="This record is the proof a specific budget line was actually approved for patient safety and QI activities -- not a programme expected to run on goodwill alone.",
    real_example="The annual budget shows a specific allocation for audit-related training, indicator software and committee-related printing.",
    why_nabh_asks="A programme management says it supports but never actually funds is a programme that will quietly starve the moment a budget decision has to be made.",
    how_to_fill=[
        ("Budget Year", "Which year."),
        ("Resource Plan Item", "What is needed."),
        ("Allocated Amount / Line Item", "Budget detail."),
        ("Approved By", "Medical Superintendent."),
        ("Approval Date", "When approved."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.4")],
    column_headers=["Budget Year", "Resource Plan Item", "Allocated Amount / Line Item", "Approved By", "Approval Date"],
    worked_example_row=["WORKED EXAMPLE — FY 2026-27", "Audit training and indicator tracking tools", "Budget line PSQ-01", "Medical Superintendent Dr. Nair", "01-Apr-2026"],
), "annual_resource_plan_budget_allocation_record")

_add("PSQ.4", 4, RecordSpec(
    oe_code="PSQ.4.c",
    oe_requirement="The management makes available adequate resources required for patient safety and quality improvement programme, earmarks adequate funds from its annual budget in this regard.",
    record_title="PSQ.4 Record 04 — Resource shortfall escalation record",
    what_is_this="This record is the proof a resource shortfall that actually compromised programme effectiveness was escalated in writing -- not absorbed silently by whoever was short-staffed that quarter.",
    real_example="A shortage of trained auditors is escalated to the Medical Superintendent, who approves funding for an additional staff member's audit training.",
    why_nabh_asks="A shortfall nobody escalates in writing gets treated as normal, and a resource gap that becomes normal never gets fixed.",
    how_to_fill=[
        ("Date", "Date raised."),
        ("Shortfall Identified", "What is missing."),
        ("Impact on Programme", "Effect."),
        ("Escalated By / To", "Who raised it and to whom."),
        ("Resolution", "What was decided."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.4")],
    column_headers=["Date", "Shortfall Identified", "Impact on Programme", "Escalated By / To", "Resolution"],
    worked_example_row=["WORKED EXAMPLE — 10-Jun-2026", "Only 1 trained auditor for 3 planned clinical audits", "Audit plan at risk of delay", "Quality Coordinator / Medical Superintendent", "Funded audit-training for a second staff member"],
), "resource_shortfall_escalation_record")

_add("PSQ.4", 5, RecordSpec(
    oe_code="PSQ.4.d",
    oe_requirement="The management uses the feedback obtained from the workforce to improve patient safety and quality improvement programme.",
    record_title="PSQ.4 Record 05 — Workforce feedback collection and action record",
    what_is_this="This record is the proof workforce feedback was actually collected, reviewed by the committee, and acted on with the action communicated back to staff -- not collected and filed without a response.",
    real_example="Suggestion-box feedback about unclear incident-reporting forms leads the committee to revise the form, and the change is announced at the next staff meeting.",
    why_nabh_asks="A suggestion box that is collected but never opened tells staff their input does not actually matter -- and they stop giving it.",
    how_to_fill=[
        ("Date Collected", "When."),
        ("Feedback Source", "Survey, suggestion box, meeting notes."),
        ("Feedback Summary", "What was said."),
        ("Committee Action", "What was decided."),
        ("Communicated Back to Staff (Y/N, Date)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.4")],
    column_headers=["Date Collected", "Feedback Source", "Feedback Summary", "Committee Action", "Communicated Back to Staff (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — 15-Jun-2026", "Suggestion box", "Incident-reporting form unclear on where to submit", "Form revised with clear submission instructions", "Y — announced 01-Jul-2026 staff meeting"],
), "workforce_feedback_collection_action_record")

# ============================================================== PSQ.5 ====
PSQ5 = SOPSpecV2(
    sop_no="SOP-PSQ.5",
    title="Incident Collection and Analysis for Continual Quality Improvement",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» runs an incident "
        "management system that actually captures every incident, "
        "identifies sentinel events through a mechanism every clinical "
        "staff member knows, analyses incidents through root-cause "
        "analysis or trend analysis depending on severity, turns that "
        "analysis into corrective and preventive action, and informs the "
        "patient, family and any regulator who needs to know -- so the "
        "patient and family are never the last to find out."
    ),
    purpose_trigger=(
        "A serious adverse event happens, and the patient's family finds "
        "out what actually went wrong only by piecing it together "
        "themselves weeks later. This SOP is what makes sure that never "
        "happens -- the patient and family are informed through a "
        "defined process, not left to guess."
    ),
    purpose_why=(
        "We do this because an incident that is handled informally, with "
        "no documentation and no analysis, teaches this hospital nothing "
        "-- and an analysis that produces no corrective action is "
        "finished paperwork, not an improvement."
    ),
    purpose_text=(
        "To define how «Hospital Name» implements an incident management "
        "system, identifies sentinel events, analyses incidents, takes "
        "corrective and preventive action, and informs stakeholders in "
        "case of a near-miss, adverse event or sentinel event."
    ),
    scope_why="so every member of staff who may witness or be involved in an incident knows how and when to report it, not just the quality team.",
    scope_text=(
        "Applies to all staff at «Hospital Name» who may witness, be "
        "involved in, or need to report an incident, near-miss or "
        "sentinel event: treating clinicians, nursing staff, department "
        "heads, the Quality Coordinator, the patient-safety committee "
        "and the Medical Superintendent. It covers how incidents are "
        "collected, analysed and acted on. It does not cover patient "
        "complaints and feedback, medication-specific incident "
        "analysis, or the patient-safety and QI programmes as a whole "
        "-- each of those has its own separate policy at this "
        "hospital, named in the Related SOPs section below."
    ),
    responsibility_why="an incident system where reporting is \"everyone's job\" in the abstract tends to produce silence -- a named same-shift reporting duty and a named Quality Coordinator holding the register are what actually get incidents captured.",
    responsibilities=[
        ("Medical Superintendent (Head of the Institution)", "Receives immediate notification of sentinel events and serious adverse events; decides whether a procedure halt continues beyond the initial stop; ensures regulatory reporting where required."),
        ("Quality Coordinator", "Maintains the incident management system and incident register; classifies incidents, initiates investigation and facilitates RCA; tracks CAPA to completion and reports to the patient-safety committee."),
        ("Treating Clinicians", "Report incidents within the same shift; participate in root-cause analysis for events in their practice area; inform the patient and family about adverse events and sentinel events."),
        ("Department Heads", "Support investigation and implement department-level CAPA; ensure staff know how to report and recognise sentinel events."),
        ("Nursing Staff", "Report incidents and near-misses within the same shift; preserve the scene and quarantine devices under stop-work."),
        ("Patient-Safety Committee", "Reviews incident trends, RCA reports and CAPA status."),
    ],
    items=[
        PlainItem(
            heading="Implement an incident management system",
            why="An incident that is handled informally -- a quiet word in the corridor, never written down -- teaches this hospital nothing and leaves no trail for the next person who hits the same problem.",
            body=[
                "The organisation implements an incident management "
                "system.",
                "Staff who witness or are involved in an incident "
                "report it to the Quality Coordinator and the treating "
                "clinician within «the same shift», using the defined "
                "incident form. The Quality Coordinator maintains the "
                "incident register and acknowledges and classifies "
                "each report within «24 hours».",
            ],
            oe_code="PSQ.5.a",
        ),
        PlainItem(
            heading="Have a mechanism to identify sentinel events",
            why="A sentinel event that is treated as just another incident, with no one trained to recognise it as sentinel, delays the immediate response that a sentinel event specifically requires.",
            body=[
                "The organisation has a mechanism to identify sentinel "
                "events.",
                "A sentinel event is an unexpected occurrence involving "
                "death, or serious physical or psychological injury, or "
                "the risk of either -- not an outcome connected to the "
                "natural course of the patient's own illness. This "
                "hospital treats the following five categories as "
                "always sentinel, whatever department they occur in:",
                "1. Unexpected death unrelated to the natural course of "
                "the patient's illness -- a patient dies and the death "
                "cannot be explained by the condition they were already "
                "being treated for.",
                "2. Major permanent loss of function not present on "
                "admission -- a patient leaves with a serious, lasting "
                "disability they did not have when they arrived, caused "
                "by something that happened during their care.",
                "3. Surgery performed on the wrong patient, the wrong "
                "body part, or the wrong side of the body -- including "
                "a correct procedure started on the wrong person, or "
                "the right procedure done on the wrong site.",
                "4. An instrument, sponge, or other surgical item left "
                "inside a patient after a procedure and only discovered "
                "later.",
                "5. An infant abducted from this hospital, or "
                "discharged to the wrong family by mistake.",
                "All clinical staff are trained to recognise these five "
                "categories at induction and «annually», not only the "
                "Quality Coordinator. When a potential sentinel event is "
                "identified, it is reported immediately to the Quality "
                "Coordinator and the Medical Superintendent -- the same "
                "shift, not at the next convenient moment -- flagged as "
                "sentinel in the incident register, and escalated "
                "straight to root-cause analysis.",
            ],
            oe_code="PSQ.5.b",
            technical_sources=[JOINT_COMMISSION_SENTINEL_SRC],
        ),
        PlainItem(
            heading="Have an established process for analysis of incidents",
            why="Treating a sentinel event and a minor near-miss with the same light-touch review misses the depth a serious event actually needs, while treating every minor near-miss with a full investigation would bury the system in paperwork and slow down the events that matter most.",
            body=[
                "The organisation has an established process for "
                "analysis of incidents. Which method applies is decided "
                "by severity, not by how busy the department is that "
                "week:",
                "A sentinel event or serious adverse event receives a "
                "root-cause analysis (RCA) by a multi-disciplinary "
                "team, completed within «72 hours» of the event. The "
                "team uses a recognised RCA technique -- repeatedly "
                "asking \"why\" until the underlying system cause is "
                "reached (the five-whys method), or a fishbone "
                "(Ishikawa) diagram to sort contributing factors into "
                "categories such as people, process, equipment and "
                "environment, or a timeline reconstruction of exactly "
                "what happened and when. The resulting report names the "
                "event, the timeline, the contributing factors, the "
                "root cause identified, and the corrective and "
                "preventive actions recommended.",
                "A moderate incident receives a structured investigation "
                "by the department head and the Quality Coordinator, "
                "completed within «one week», using the same timeline "
                "and contributing-factors approach at a lighter depth.",
                "Near-misses and minor incidents are not investigated "
                "one by one. Instead, the Quality Coordinator reviews "
                "them together as an aggregate trend analysis every "
                "«month», looking for a repeated pattern -- the same "
                "location, the same shift, the same type of error -- "
                "and reports the pattern to the patient-safety "
                "committee.",
            ],
            oe_code="PSQ.5.c",
            technical_sources=[WHO_RCA_CURRICULUM_SRC],
        ),
        PlainItem(
            heading="Take corrective and preventive action based on the analysis",
            why="An RCA report that names a root cause and recommends nothing is a document, not an improvement -- the whole point of the analysis is the action that follows it.",
            body=[
                "Corrective and preventive actions are taken based on "
                "the findings of such analysis.",
                "Each analysis produces a CAPA action plan with a "
                "responsible person, target date and expected outcome. "
                "The Quality Coordinator tracks it to completion and "
                "verifies effectiveness; the committee reviews CAPA "
                "status «quarterly».",
            ],
            oe_code="PSQ.5.d",
        ),
        PlainItem(
            heading="Inform stakeholders in case of a near-miss, adverse event or sentinel event",
            why="A patient or family who learns what happened only by piecing it together themselves, weeks later, has been failed twice -- once by the event, and once by this hospital's silence about it.",
            body=[
                "The organisation has a process for informing various "
                "stakeholders in case of a near miss / adverse event / "
                "sentinel event.",
                "The treating clinician informs the patient and family "
                "about an adverse event or sentinel event, documenting "
                "the date, clinician and content communicated. The "
                "Medical Superintendent ensures regulatory reporting "
                "where required by law. A near-miss with no patient "
                "harm is communicated internally to the committee, not "
                "necessarily to the patient.",
            ],
            oe_code="PSQ.5.e",
        ),
        PlainItem(
            heading="Know when to stop — and what happens next",
            why="Continuing a procedure or process after a sentinel event has just occurred in it, on the assumption that the investigation can happen later, risks the same mechanism causing harm again before anyone has looked at what went wrong.",
            body=[
                "Any staff member who identifies a sentinel event stops "
                "the procedure or process in which it occurred, where "
                "continuing could cause further harm, and preserves "
                "the scene -- the equipment, devices, and physical "
                "setting -- without cleaning, discarding or returning "
                "anything to use.",
                "The event is reported to the Quality Coordinator and "
                "the Medical Superintendent immediately, not at the end "
                "of the shift. No approval is needed to stop and "
                "preserve the scene.",
                "The Medical Superintendent decides whether the halt "
                "continues beyond the immediate stop, and the stop-work "
                "invocation is recorded in the incident register. "
                "Reporting honestly is protected -- punitive action for "
                "good-faith reporting is prohibited under this "
                "hospital's culture-of-safety commitment.",
            ],
            oe_code="PSQ.5",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-7 (see the PSQ.5 Records folder).",
    related_documents=[
        "Hospital's Patient-Safety Programme and Quality Improvement Programme SOP (PSQ.1)",
        "Hospital's Key Indicators SOP (PSQ.2)",
        "Hospital's Management Support for Patient Safety and Quality Improvement SOP (PSQ.4)",
        "Hospital's Patient Feedback and Complaint Redressal SOP (PRE.6)",
        "Hospital's Monitoring SOP (MOM.7)",
        "Hospital's Leadership ownership of organisational risk SOP (ROM.4)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a sentinel event is "
        "found to have been treated as a routine incident, a CAPA is "
        "found untracked past its target date, or a related policy "
        "named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_PSQ_CITE.format(code="PSQ.5"),
        JOINT_COMMISSION_SENTINEL_SRC,
        WHO_RCA_CURRICULUM_SRC,
    ],
)

SOPS.append(("SOP_PSQ.5.a_to_e_incident_collection_analysis_continual_quality_improvement.docx", PSQ5))

# ---- PSQ.5 Records -------------------------------------------------
_add("PSQ.5", 1, RecordSpec(
    oe_code="PSQ.5.a",
    oe_requirement="The organisation implements an incident management system.",
    record_title="PSQ.5 Record 01 — Incident register",
    what_is_this="This record is the proof every reported incident was actually logged with date, time, description, severity and reporter -- not handled informally with no trail.",
    real_example="A medication near-miss reported by a nurse is logged within the shift, classified as a near-miss, and acknowledged by the Quality Coordinator within 24 hours.",
    why_nabh_asks="An incident that is handled informally teaches this hospital nothing and leaves no trail for the next person who hits the same problem.",
    how_to_fill=[
        ("Date/Time", "When it happened."),
        ("Description", "What occurred."),
        ("Severity", "Near-miss, minor, moderate, serious, sentinel."),
        ("Reported By", "Named."),
        ("Acknowledged/Classified By (Within 24h)", "Quality Coordinator and date."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5")],
    column_headers=["Date/Time", "Description", "Severity", "Reported By", "Acknowledged/Classified By (Within 24h)"],
    worked_example_row=["WORKED EXAMPLE — 12-Jun-2026, 3:00 PM", "Wrong-dose medication caught before administration", "Near-miss", "Staff Nurse R. Menon", "Quality Coordinator A. Deshmukh — 13-Jun-2026"],
), "incident_register")

_add("PSQ.5", 2, RecordSpec(
    oe_code="PSQ.5.b",
    oe_requirement="The organisation has a mechanism to identify sentinel events.",
    record_title="PSQ.5 Record 02 — Sentinel-event recognition training record",
    what_is_this="This record is the proof clinical staff were actually trained to recognise a sentinel event -- not assumed to know because a definition exists in a policy folder.",
    real_example="All clinical staff complete annual sentinel-event recognition training, with the hospital's five-category always-sentinel list (unexpected death unrelated to illness, major permanent loss of function, wrong-patient/wrong-site surgery, retained instrument, infant abduction or wrong-family discharge) reviewed.",
    why_nabh_asks="A sentinel event that is treated as just another incident, with no one trained to recognise it, delays the immediate response it specifically requires.",
    how_to_fill=[
        ("Staff Name", "Named."),
        ("Department", "Theirs."),
        ("Training Date", "When."),
        ("Five-Category Sentinel List Reviewed (Y/N)", "Confirmed."),
        ("Trainer", "Who delivered it."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5"), JOINT_COMMISSION_SENTINEL_SRC],
    column_headers=["Staff Name", "Department", "Training Date", "Five-Category Sentinel List Reviewed (Y/N)", "Trainer"],
    worked_example_row=["WORKED EXAMPLE — Dr. Kavita Rao", "Surgery", "10-Jan-2026", "Y", "Quality Coordinator A. Deshmukh"],
), "sentinel_event_recognition_training_record")

_add("PSQ.5", 3, RecordSpec(
    oe_code="PSQ.5.c",
    oe_requirement="The organisation has an established process for analysis of incidents.",
    record_title="PSQ.5 Record 03 — Root-cause analysis report",
    what_is_this="This record is the proof a sentinel or serious adverse event actually received a root-cause analysis by a multi-disciplinary team, with a timeline and named root causes -- not a light-touch review mismatched to its severity.",
    real_example="A serious adverse event receives an RCA by a 4-person multi-disciplinary team within 72 hours, using the five-whys method to trace a system root cause back to handover communication.",
    why_nabh_asks="Treating a sentinel event with the same light-touch review as a minor near-miss misses the depth a serious event actually needs.",
    how_to_fill=[
        ("Event Date", "When it occurred."),
        ("RCA Team Members", "Named, multi-disciplinary."),
        ("Method Used", "Five-whys, fishbone diagram, or timeline reconstruction."),
        ("Timeline / Root Cause(s) Identified", "Sequence of events and result."),
        ("RCA Completion Date (Within 72 Hours)", "When finished."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5"), WHO_RCA_CURRICULUM_SRC],
    column_headers=["Event Date", "RCA Team Members", "Method Used", "Timeline / Root Cause(s) Identified", "RCA Completion Date (Within 72 Hours)"],
    worked_example_row=["WORKED EXAMPLE — 20-Jun-2026", "Dr. Nair, Nursing In-Charge R. Patel, Quality Coordinator A. Deshmukh, Pharmacist S. Joshi", "Five-whys", "Handover at 7am missed critical allergy information — system root cause: verbal-only handover with no written checklist", "22-Jun-2026 (within 72 hours)"],
), "root_cause_analysis_report")

_add("PSQ.5", 4, RecordSpec(
    oe_code="PSQ.5.c",
    oe_requirement="The organisation has an established process for analysis of incidents.",
    record_title="PSQ.5 Record 04 — Monthly near-miss and minor-incident trend analysis",
    what_is_this="This record is the proof near-misses and minor incidents were actually reviewed in aggregate every month -- not left unreviewed because no single one seemed serious enough on its own.",
    real_example="The June trend analysis finds 3 medication near-misses, all at shift handover, prompting a review of the handover process.",
    why_nabh_asks="Treating every minor near-miss with a full investigation would bury the system in paperwork, but never aggregating them at all hides the pattern a single incident can't show.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Near-Misses/Minor Incidents Count", "Total."),
        ("Pattern Identified", "Common thread, if any."),
        ("Reviewed By", "Quality Coordinator / committee."),
        ("Follow-up Action (if any)", "What was decided."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5")],
    column_headers=["Month", "Near-Misses/Minor Incidents Count", "Pattern Identified", "Reviewed By", "Follow-up Action (if any)"],
    worked_example_row=["WORKED EXAMPLE — June 2026", "3 medication near-misses", "All occurred at shift handover", "Quality Coordinator A. Deshmukh", "Handover process review scheduled"],
), "monthly_near_miss_minor_incident_trend_analysis")

_add("PSQ.5", 5, RecordSpec(
    oe_code="PSQ.5.d",
    oe_requirement="Corrective and preventive actions are taken based on the findings of such analysis.",
    record_title="PSQ.5 Record 05 — CAPA tracking register",
    what_is_this="This record is the proof each CAPA actually had a responsible person and target date, was tracked to completion, and had its effectiveness verified -- not an action plan that stopped at being written.",
    real_example="A CAPA on handover communication is tracked to completion with a written checklist introduced, and effectiveness confirmed by zero handover-related near-misses the following quarter.",
    why_nabh_asks="An RCA report that names a root cause and recommends nothing is a document, not an improvement.",
    how_to_fill=[
        ("CAPA Description", "What action."),
        ("Responsible Person / Target Date", "Accountability."),
        ("Completion Status", "Done, in progress, overdue."),
        ("Effectiveness Verification", "How confirmed."),
        ("Committee Reviewed (Y/N, Date)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5")],
    column_headers=["CAPA Description", "Responsible Person / Target Date", "Completion Status", "Effectiveness Verification", "Committee Reviewed (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — Written handover checklist introduction", "Nursing In-Charge R. Patel / 15-Jul-2026", "Done", "Zero handover-related near-misses in Q3", "Y — 10-Oct-2026"],
), "capa_tracking_register")

_add("PSQ.5", 6, RecordSpec(
    oe_code="PSQ.5.e",
    oe_requirement="The organisation shall have a process for informing various stakeholders in case of a near miss / adverse event / sentinel event.",
    record_title="PSQ.5 Record 06 — Patient/family disclosure and regulatory notification record",
    what_is_this="This record is the proof the patient and family were actually informed about an adverse or sentinel event, and any required regulatory notification actually happened -- not left for them to find out on their own.",
    real_example="Following a serious adverse event, the treating clinician discloses it to the family the same day, documenting what was communicated.",
    why_nabh_asks="A patient or family who learns what happened only by piecing it together themselves has been failed twice -- once by the event, and once by this hospital's silence about it.",
    how_to_fill=[
        ("Event Date", "When it occurred."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Disclosed By / Date", "Clinician and when."),
        ("Content Communicated", "Summary."),
        ("Regulatory Notification (Y/N/NA)", "Confirmed."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5")],
    column_headers=["Event Date", "Patient (Identifier 1) / UID (Identifier 2)", "Disclosed By / Date", "Content Communicated", "Regulatory Notification (Y/N/NA)"],
    worked_example_row=["WORKED EXAMPLE — 20-Jun-2026", "Ramesh Gupta / UID-01090", "Dr. Nair — 20-Jun-2026", "Explained the event, its cause so far understood, and next steps", "N — not legally required for this event"],
), "patient_family_disclosure_regulatory_notification_record")

_add("PSQ.5", 7, RecordSpec(
    oe_code="PSQ.5",
    oe_requirement="Any staff member who identifies a sentinel event stops the procedure or process in which it occurred and preserves the scene; a documented Medical Superintendent decision is required to continue beyond the immediate stop.",
    record_title="PSQ.5 Record 07 — Sentinel-event stop-work and scene-preservation log",
    what_is_this="This record is the proof a sentinel event was actually stopped and the scene actually preserved for investigation -- not cleaned up or continued on the assumption the investigation could happen later.",
    real_example="A wrong-site surgical near-miss is stopped before incision; the operating theatre and instrument tray are preserved untouched, and the Medical Superintendent is notified immediately.",
    why_nabh_asks="Continuing a procedure after a sentinel event has just occurred in it risks the same mechanism causing harm again before anyone has looked at what went wrong.",
    how_to_fill=[
        ("Date/Time", "When stopped."),
        ("Event", "What was identified as sentinel."),
        ("Stopped By", "Who invoked the stop."),
        ("Scene Preserved (Y/N, How)", "What was kept untouched."),
        ("Medical Superintendent Notified / Decision", "Immediate notification and continuation decision."),
    ],
    verified_sources=[NABH_PSQ_CITE.format(code="PSQ.5")],
    column_headers=["Date/Time", "Event", "Stopped By", "Scene Preserved (Y/N, How)", "Medical Superintendent Notified / Decision"],
    worked_example_row=["WORKED EXAMPLE — 25-Jun-2026, 10:15 AM", "Wrong-site surgical near-miss identified before incision", "Dr. Varma (surgeon)", "Y — OT and instrument tray preserved untouched", "Notified immediately; halt continued pending RCA"],
), "sentinel_event_stop_work_scene_preservation_log")

def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path}")

    manifest: list[dict] = []
    for fname, spec in SOPS:
        manifest.append({
            "file": fname,
            "document_type": "sop",
            "standard_code": spec.sop_no.replace("SOP-", ""),
            "title": f"SOP — {spec.title} ({spec.sop_no.replace('SOP-', '')})",
        })
        sop_records = [r for r in RECORDS if r[0] == spec.sop_no.replace("SOP-", "")]
        for sop_code, idx, slug, rspec in sorted(sop_records, key=lambda r: r[1]):
            rel_path = f"Records/{sop_code}_Record_{idx:02d}_{slug}.docx"
            out_path = RECORDS_ROOT.parent / rel_path
            build_record(rspec, out_path)
            print(f"built {out_path}")
            manifest.append({
                "file": rel_path,
                "document_type": "record",
                "standard_code": sop_code,
                "record_index": idx,
                "title": rspec.record_title.split("—", 1)[-1].strip(),
            })

    manifest_path = OUT_ROOT / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {manifest_path} ({len(manifest)} entries)")


if __name__ == "__main__":
    main()
