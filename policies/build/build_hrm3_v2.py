# -*- coding: utf-8 -*-
"""HRM.3 v2 — safety, disaster, fire and quality-improvement training.

Shape follows PRE v2 (section list and order only). Wording is built
from HRM.3 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 124 / PDF index 130.

No stop-work section. Seven OEs mapped to seven What-we-do subsections.
Cross-references owning programmes — does not duplicate ROM/COP/FMS/PSQ content.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.3"
CHAPTER = "HRM"
OE_CODES = [
    "HRM.3.a", "HRM.3.b", "HRM.3.c", "HRM.3.d",
    "HRM.3.e", "HRM.3.f", "HRM.3.g",
]
POLICY_TITLE = "Safety, Disaster, Fire and Quality-Improvement Training"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v3 template: PRE v2 shape, cross-ref programmes, seven steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Staff are trained in the organisation's safety, disaster, emergency and quality "
    "improvement programmes — so they know how to detect and handle risks, respond to "
    "incidents and participate in continuous improvement, without duplicating the "
    "programmes those other policies own."
)

PURPOSE = f"""This policy describes how {HOSPITAL} trains staff in the safety programme, risk detection and handling, incident procedures, occupational safety, disaster management, fire and non-fire emergencies, and the quality improvement programme.

It covers seven training-delivery elements. Each element cross-references the owning policy for programme content — this document owns that staff are trained, not the programme itself.

HRM.2 owns the training framework, calendar and effectiveness evaluation. ROM/COP own the hospital safety programme. PSQ.5 owns the incident system. COP.2 owns the disaster management plan. FMS.5 owns fire and non-fire emergency plans. PSQ.1 owns the QI programme.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff at {HOSPITAL}. It applies to the {D('Training Coordinator')}, department heads, the {D('Medical Superintendent')} and the {D('Quality Coordinator')}.

It covers HRM.3.a–g as training-delivery requirements. It does not own: the safety programme content (ROM.4 / COP standards); the incident reporting and analysis system (PSQ.5); the disaster management plan (COP.2); fire and non-fire emergency plans (FMS.5); or the QI programme structure (PSQ.1).

Boundaries with other policies of {HOSPITAL}:

- ROM.4 and COP standards own the hospital safety programme. HRM.3.a owns that staff are trained in it.
- PSQ.5 owns incident collection, analysis and CAPA. HRM.3.c owns that staff know procedures to follow in the event of an incident.
- COP.2 owns the disaster management plan. HRM.3.e owns staff training on that plan.
- FMS.5 owns fire and non-fire emergency plans and drills. HRM.3.f owns staff training on handling those emergencies.
- PSQ.1 owns the patient-safety and QI programmes. HRM.3.g owns that staff are trained in the QI programme."""

POLICY_STATEMENT = f"""{HOSPITAL} trains staff in the organisation's safety programme, in detection, handling, minimisation and elimination of identified risks, and in occupational safety aspects.

Staff members are made aware of procedures to follow in the event of an incident (per PSQ.5). Staff are trained in the disaster management plan (per COP.2), in handling fire and non-fire emergencies (per FMS.5), and in the quality improvement programme (per PSQ.1).

This policy delivers training. It does not rewrite the programmes those policies own."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. All staff complete safety-programme training at induction and {D('annually')} — not only clinical staff.
2. Risk detection and handling training covers the hospital environment — not only fire drills.
3. Every staff member knows how to report an incident per PSQ.5 — not only department heads.
4. Occupational safety training covers hazards relevant to each role — not a generic lecture.
5. Disaster management plan training follows the COP.2 plan — not an improvised briefing.
6. Fire and non-fire emergency training follows the FMS.5 plans — not only a video.
7. QI programme training ensures staff can participate in improvement activities per PSQ.1 — not only the Quality Coordinator.

Staff who identify a training gap report it to the {D('Training Coordinator')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Safety programme training

Staff are trained in the organisation's safety programme at {HOSPITAL}. The safety programme is owned by ROM.4 (organisational risk) and COP standards (clinical safety). This step owns training delivery, not programme content.

The {D('Training Coordinator')} schedules safety-programme training at induction and {D('annually')}. Content covers: the hospital safety structure; staff roles in safety; reporting channels; and key safety policies the hospital has adopted. Training attendance is recorded in the training matrix (HRM.2.c).""",

f"""5.2 Risk detection, handling, minimisation and elimination

Staff are provided training in the detection, handling, minimisation and elimination of identified risks within the organisation's environment at {HOSPITAL}. Training covers: hazard identification in the workplace; near-miss reporting (PSQ.5); basic risk assessment; and escalation paths.

Department heads tailor content to unit-specific risks (for example medication errors in pharmacy, falls in wards, sharps in procedure areas). Training is refreshed {D('annually')} or when a new risk is identified through PSQ.5 or ROM.4.""",

f"""5.3 Incident procedures awareness

Staff members are made aware of procedures to follow in the event of an incident at {HOSPITAL}. PSQ.5 owns the incident reporting and analysis system. This step owns that every staff member knows how to report, what to do immediately after an incident, and whom to notify.

Training at induction covers: incident definition; reporting form or channel; immediate patient safety actions; preservation of evidence; and non-retaliation for reporting. Refresher training is conducted {D('annually')}. Incident reporting posters are displayed in clinical areas.""",

f"""5.4 Occupational safety aspects

Staff are trained in occupational safety aspects at {HOSPITAL}. Training covers hazards relevant to healthcare workers: manual handling and ergonomics; chemical exposure (pointer to FMS.2.g); electrical safety (pointer to FMS.2.e); workplace violence (pointer to HRM.5.d); and infection-control occupational practices (pointer to HIC.4 for exposure response).

The {D('Training Coordinator')} maintains role-specific occupational safety modules. Department heads confirm unit hazards are covered. Training records are filed per HRM.2.""",

f"""5.5 Disaster management plan training

Staff are trained in the organisation's disaster management plan at {HOSPITAL}. COP.2 owns the disaster management plan. This step owns that all staff know the plan's activation triggers, their role in the plan, evacuation or shelter procedures and communication channels.

Disaster training is conducted at induction and {D('annually')}. A tabletop exercise or drill is conducted {D('once a year')} per the COP.2 plan. Attendance and drill outcomes are recorded.""",

f"""5.6 Fire and non-fire emergency training

Staff are trained in handling fire and non-fire emergencies at {HOSPITAL}. FMS.5 owns fire and non-fire emergency plans, exit routes and drill schedules. This step owns that all staff know: alarm signals; evacuation routes; assembly points; use of fire extinguishers where trained; and non-fire emergency responses (for example utility failure, gas leak — per FMS.5).

Fire and non-fire emergency training is conducted at induction and refreshed after each FMS.5 drill or {D('annually')}, whichever is sooner. Drill attendance is cross-checked with FMS.5 records.""",

f"""5.7 Quality improvement programme training

Staff are trained in the organisation's quality improvement programme at {HOSPITAL}. PSQ.1 owns the patient-safety and QI programmes. This step owns that staff understand: the purpose of QI; how to identify improvement opportunities; how to participate in audits (PSQ.1.h); and how CAPA works (PSQ.5).

Department heads and clinical staff receive QI training at induction and {D('annually')}. The {D('Quality Coordinator')} delivers or coordinates sessions. Training covers the indicator dashboard (PSQ.2) at a level appropriate to each role.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Ensures safety, disaster and emergency training is resourced and conducted.
- Participates in disaster and fire drills per COP.2 and FMS.5.

Training Coordinator
- Schedules and records all HRM.3 training sessions.
- Coordinates with Quality Coordinator for QI and incident-awareness training.

Quality Coordinator
- Delivers or coordinates QI programme and incident-awareness training (PSQ.1 / PSQ.5).
- Audits this policy {D('quarterly')} (see section 7).

Department Heads
- Ensure unit-specific risk and occupational safety content is covered.
- Confirm all department staff complete required training.

All Staff
- Complete safety, incident, disaster, fire and QI training at induction and refreshers."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers training delivery across all seven elements and cross-checks with owning policies.

What is monitored each quarter:

- Safety-programme training attendance at induction and annual refresh.
- Risk-handling training current for a sample of departments.
- All staff can describe incident reporting per PSQ.5 (spot check).
- Occupational safety training mapped to role-specific hazards.
- Disaster management training aligned with current COP.2 plan.
- Fire/non-fire training aligned with current FMS.5 plans and drill records.
- QI programme training attendance and participation evidence.

Root-cause analysis is required when a staff member involved in an incident could not describe the reporting procedure.

This policy is reviewed {D('annually')}, and sooner when COP.2, FMS.5 or PSQ.1/PSQ.5 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff complete the training elements in this policy at induction and at the refresh intervals stated in each subsection. Staff acknowledge completion on the training attendance record maintained by the {D('Training Coordinator')}.

Staff acknowledgement

I have received training on safety, incident reporting, occupational safety, disaster management, fire and non-fire emergencies, and the quality improvement programme at {HOSPITAL}. I know how to report an incident and whom to notify in an emergency.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Training Coordinator holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/03"),
    version=VERSION,
    prepared_by=D("Training Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.3.
- Internal documents of {HOSPITAL}: hospital safety programme (ROM.4 / COP); incident management system (PSQ.5); disaster management plan (COP.2); fire and non-fire emergency plans (FMS.5); patient-safety and QI programmes (PSQ.1); training attendance records (HRM.2)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Training Coordinator.

Copies issued to: department heads; quality office; all clinical and support areas.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
FMS — Facility Management and Safety (NABH SHCO chapter 7)
HRM — Human Resource Management (NABH SHCO chapter 8)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
QI — quality improvement
ROM — Responsibilities of Management (NABH SHCO chapter 6)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HRM.3.a",
        "requirement": "Staff are trained in the organisation's safety programme.",
        "steps": "Statement of intent; Section 3; 5.1 Safety programme training; Section 4 item 1",
        "responsible": "Training Coordinator (schedule and record); department heads (ensure attendance)",
        "records": [
            "Safety-programme training curriculum cross-referencing ROM.4 / COP.",
            "Induction and annual safety training attendance records.",
            "Training matrix entries linking safety training to each staff category.",
        ],
    },
    {
        "oe_code": "HRM.3.b",
        "requirement": "Staff are provided training in the detection, handling, minimisation and elimination of identified risks within the organisation's environment.",
        "steps": "Section 3; 5.2 Risk detection, handling, minimisation and elimination; Section 4 item 2",
        "responsible": "Training Coordinator (curriculum); department heads (unit-specific hazards)",
        "records": [
            "Risk-handling training module with hazard identification content.",
            "Department-specific hazard training records.",
            "Annual refresher attendance records.",
        ],
    },
    {
        "oe_code": "HRM.3.c",
        "requirement": "Staff members are made aware of procedures to follow in the event of an incident.",
        "steps": "Section 3; 5.3 Incident procedures awareness; Section 4 item 3",
        "responsible": "Quality Coordinator (content from PSQ.5); Training Coordinator (delivery and record)",
        "records": [
            "Incident-awareness training content aligned with PSQ.5 procedures.",
            "Induction and annual refresher attendance records.",
            "Incident reporting posters displayed in clinical areas.",
        ],
    },
    {
        "oe_code": "HRM.3.d",
        "requirement": "Staff are trained in occupational safety aspects.",
        "steps": "Section 3; 5.4 Occupational safety aspects; Section 4 item 4",
        "responsible": "Training Coordinator (modules); department heads (role-specific hazards)",
        "records": [
            "Occupational safety training modules covering relevant healthcare hazards.",
            "Role-specific training completion records.",
            "Cross-reference to HRM.5 and HIC.4 for violence and exposure response.",
        ],
    },
    {
        "oe_code": "HRM.3.e",
        "requirement": "Staff are trained in the organisation's disaster management plan.",
        "steps": "Section 3; 5.5 Disaster management plan training; Section 4 item 5",
        "responsible": "Training Coordinator (schedule); Medical Superintendent (drill participation)",
        "records": [
            "Disaster training content aligned with current COP.2 plan.",
            "Induction and annual disaster training attendance records.",
            "Annual tabletop exercise or drill record with outcomes.",
        ],
    },
    {
        "oe_code": "HRM.3.f",
        "requirement": "Staff are trained in handling fire and non-fire emergencies.",
        "steps": "Section 3; 5.6 Fire and non-fire emergency training; Section 4 item 6",
        "responsible": "Training Coordinator (schedule); cross-check with FMS.5 drill records",
        "records": [
            "Fire and non-fire emergency training content aligned with FMS.5 plans.",
            "Induction and post-drill refresher attendance records.",
            "Cross-check record matching FMS.5 drill attendance.",
        ],
    },
    {
        "oe_code": "HRM.3.g",
        "requirement": "Staff are trained in the organisation's quality improvement programme.",
        "steps": "Section 3; 5.7 Quality improvement programme training; Section 4 item 7",
        "responsible": "Quality Coordinator (content from PSQ.1); Training Coordinator (schedule and record)",
        "records": [
            "QI training content aligned with PSQ.1 programmes.",
            "Induction and annual QI training attendance records.",
            "Evidence of staff participation in QI activities after training.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.3 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: HRM.3.a–g PDF index 130. No asterisked OEs. All Commitment except HRM.3.e/f Core.

SHAPE: Seven What-we-do subsections (5.1–5.7). No stop-work. Disclaimer accreditation-only. Cross-ref ROM/COP/PSQ/FMS — does not duplicate owning programmes. HRM.3.e/f forward-ref from FMS.5 deferred items now landed as training delivery only."""


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
        "subtitle": "Safety, disaster, fire and QI training — delivery only, programmes owned elsewhere.",
        "doc_no": D("HRM/POL/03"),
    }
    emit_pre_v2(
        draft,
        "hrm3_v2_draft.json",
        "HRM.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
