# -*- coding: utf-8 -*-
"""PSQ.4 v2 — management support for patient safety and quality improvement.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed pages 109–110.

No stop-work section. Four OEs in four What-we-do subsections.
Disclaimer P2 is accreditation-only.
NOTE: PDF uses "program" (not "programme") for PSQ.4.b; we use "programme" in our wording.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PSQ.4"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.4.a", "PSQ.4.b", "PSQ.4.c", "PSQ.4.d",
]
POLICY_TITLE = "Management Support for Patient Safety and Quality Improvement"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PSQ v2 template: PRE v2 shape, plain English, PSQ roles, four steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The patient safety and quality improvement programme are supported by the "
    "management — not as a signature on a quality manual but as culture, awareness, "
    "resources and feedback-driven improvement."
)

PURPOSE = f"""This policy describes how management at {HOSPITAL} supports the patient-safety and quality improvement programmes, satisfying PSQ.4.a–d.

It covers four elements: management creating a culture of safety; leaders at all levels aware of programme intent and implementation approach; adequate resources and earmarked budget; and management using workforce feedback to improve the programmes.

PSQ.4 owns management's role in supporting the programmes. PSQ.1 owns the programmes themselves. ROM.4 owns leadership ownership of organisational risk. PSQ.4 is the bridge: management enables PSQ.1 through culture, awareness, resources and feedback.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the Medical Superintendent, department heads, the {D('Quality Coordinator')} and all leaders at {HOSPITAL} who have a role in supporting patient safety and quality improvement.

It covers the four objective elements PSQ.4.a–d. It does not cover the programmes themselves (PSQ.1), key indicators (PSQ.2), the clinical audit system (PSQ.3), or incident analysis (PSQ.5).

Boundaries with other policies of {HOSPITAL}:

- PSQ.1 owns the patient-safety and QI programmes, their committees and their reviews. PSQ.4 ensures management supports those programmes.
- ROM.4 owns leadership ownership of organisational risk. PSQ.4.a (culture of safety) and ROM.4 leadership risk are complementary. Cross-reference ROM.4.
- PSQ.4.c resources include budget for PSQ.2 indicators, PSQ.3 audits and PSQ.5 incident management."""

POLICY_STATEMENT = f"""Management at {HOSPITAL} creates a culture of safety where staff can report errors and near-misses without fear of punitive action for honest reporting.

Leaders at all levels are aware of the intent of the patient-safety and quality improvement programme and the approach to its implementation.

Management makes available adequate resources required for patient safety and quality improvement and earmarks adequate funds from the annual budget.

Management uses workforce feedback to improve the patient-safety and quality improvement programme."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Management creates a culture of safety — staff can report errors and near-misses without fear of blame for honest reporting.
2. Leaders at all levels are aware of the programme intent and implementation approach — awareness is documented, not assumed.
3. Adequate resources are made available and adequate funds are earmarked from the annual budget for patient safety and quality improvement.
4. Workforce feedback is collected and used by management to improve the programmes — feedback is not collected and filed without action.

Any leader who discourages honest incident reporting or withholds budgeted safety resources is reported to the {D('Medical Superintendent')} by the {D('Quality Coordinator')}."""

PROCEDURE_STEPS = [
f"""5.1 Creating a culture of safety

Management at {HOSPITAL} creates a culture of safety. The Medical Superintendent and department heads communicate that honest reporting of errors, near-misses and safety concerns is expected and will not attract punitive action for the reporter when the report is made in good faith.

The culture of safety is demonstrated by: {D('a non-punitive reporting policy communicated at induction and annually; visible leadership participation in patient-safety committee meetings; management response to safety reports documented and fed back to staff; and recognition of departments or individuals who contribute to safety improvement')}.

A culture of safety does not mean absence of accountability for wilful harm, substance abuse or repeated negligence. It means honest reporters are protected.""",

f"""5.2 Leader awareness of programme intent and implementation

Leaders at all levels in {HOSPITAL} are aware of the intent of the patient-safety and quality improvement programme and the approach to its implementation. Awareness is ensured through {D('an annual leadership briefing by the Quality Coordinator, inclusion of programme updates in department-head meetings, and documented acknowledgement by each leader')}.

New leaders (department heads, section in-charges) receive a programme orientation within {D('30 days')} of appointment. Awareness covers: programme objectives, committee structure, indicator framework (PSQ.2), audit system (PSQ.3), incident reporting (PSQ.5), and how the leader's department contributes.""",

f"""5.3 Adequate resources and earmarked budget

Management makes available adequate resources required for patient safety and quality improvement and earmarks adequate funds from the annual budget. Resources include: {D('dedicated Quality Coordinator time, audit tools, indicator data collection systems, training materials, incident reporting forms or software, and committee meeting facilities')}.

The annual budget includes a line item or identified allocation for patient safety and quality improvement activities. The {D('Quality Coordinator')} prepares a resource plan {D('annually')} and presents it to the Medical Superintendent for approval. Shortfalls that compromise programme effectiveness are escalated to management in writing.""",

f"""5.4 Workforce feedback to improve the programmes

Management uses the feedback obtained from the workforce to improve the patient-safety and quality improvement programme. Workforce feedback is collected through {D('annual staff surveys on safety culture, suggestion boxes, department meetings, and direct reports to the Quality Coordinator or patient-safety committee')}.

Feedback is reviewed by the QI committee {D('quarterly')} and used to identify barriers, improve processes, adjust training and refine programme design. Actions taken in response to feedback are communicated back to staff. Feedback that is collected but not acted upon or communicated is a defect.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Creates and sustains a culture of safety at the institutional level.
- Approves resource allocation and earmarked budget for the programmes.
- Ensures leaders at all levels are aware of programme intent.

Quality Coordinator
- Prepares resource plans and presents to management.
- Facilitates leadership briefings and awareness orientation.
- Collects and consolidates workforce feedback for committee review.

Department Heads
- Demonstrate culture of safety within their departments.
- Participate in programme awareness activities.
- Report resource shortfalls and relay workforce feedback upward.

Patient-Safety / QI Committee
- Reviews workforce feedback and recommends programme improvements.
- Reports resource gaps to management."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers management support: culture, awareness, resources and feedback.

What is monitored each quarter:

- Culture of safety communicated and demonstrated; no punitive action for honest reporting documented.
- Leader awareness documented through briefings and acknowledgements.
- Budget allocation for safety and QI activities available and utilised.
- Workforce feedback collected, reviewed by committee and acted upon.

Root-cause analysis is required when workforce feedback indicates fear of reporting or when budgeted safety resources are not released for {D('two consecutive quarters')}.

This policy is reviewed {D('annually')}, and sooner when PSQ.1, PSQ.2, PSQ.3 or PSQ.5 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All leaders and department heads are trained on this policy at appointment and {D('once a year')} after that. Training covers culture of safety, programme awareness, resource planning and feedback mechanisms.

Staff acknowledgement

I have read this Management Support for Patient Safety and Quality Improvement policy of {HOSPITAL}. I understand management's role in creating a culture of safety and supporting the programmes.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PSQ/POL/04"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Safety and Quality Improvement chapter, standard PSQ.4.
- Internal documents of {HOSPITAL}: patient-safety and QI programme documents (PSQ.1); annual budget with safety/QI allocation; workforce feedback records; leadership briefing and acknowledgement records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: Medical Superintendent; department heads; patient-safety / QI committee members; nursing administration.

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
QI — quality improvement
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.4.a",
        "requirement": "The management creates a culture of safety.",
        "steps": "Statement of intent; Section 3; 5.1 Creating a culture of safety; Section 4 items 1, 4",
        "responsible": "Medical Superintendent (create and sustain); department heads (demonstrate in departments)",
        "records": [
            "Non-punitive reporting policy communicated at induction and annually.",
            "Records of management participation in patient-safety committee meetings.",
            "Feedback to staff on management response to safety reports.",
        ],
    },
    {
        "oe_code": "PSQ.4.b",
        "requirement": "The leaders at all levels in the organisation are aware of the intent of the patient safety quality improvement programme and the approach to its implementation.",
        "steps": "Section 3; 5.2 Leader awareness of programme intent and implementation; Section 4 item 2",
        "responsible": "Quality Coordinator (facilitate briefings); Medical Superintendent (ensure awareness)",
        "records": [
            "Annual leadership briefing records with attendance.",
            "Documented acknowledgement from each leader of programme intent and approach.",
            "New-leader orientation records within defined period of appointment.",
        ],
    },
    {
        "oe_code": "PSQ.4.c",
        "requirement": "The management makes available adequate resources required for patient safety and quality improvement programme, earmarks adequate funds from its annual budget in this regard.",
        "steps": "Section 3; 5.3 Adequate resources and earmarked budget; Section 4 item 3",
        "responsible": "Medical Superintendent (approve); Quality Coordinator (plan and report shortfalls)",
        "records": [
            "Annual resource plan for patient safety and QI activities.",
            "Budget line item or identified allocation for safety/QI in the annual budget.",
            "Escalation records where resource shortfalls compromise programme effectiveness.",
        ],
    },
    {
        "oe_code": "PSQ.4.d",
        "requirement": "The management uses the feedback obtained from the workforce to improve patient safety and quality improvement programme.",
        "steps": "Section 3; 5.4 Workforce feedback to improve the programmes; Section 4 item 4",
        "responsible": "Quality Coordinator (collect and consolidate); QI committee (review and act); Medical Superintendent (approve actions)",
        "records": [
            "Workforce feedback collection records (surveys, suggestion boxes, meeting notes).",
            "QI committee minutes showing feedback reviewed and actions taken.",
            "Communication records showing actions fed back to staff.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PSQ.4 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The patient safety and quality improvement programme are supported by the management." PSQ.4.a–d PDF pages 109–110. No asterisked OEs. PSQ.4.a Achievement; PSQ.4.b/c Commitment; PSQ.4.d Excellence. PDF uses "program" for PSQ.4.b; our wording uses "programme".

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only. PSQ roles only."""


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
        "subtitle": "Management support for patient safety and quality improvement.",
        "doc_no": D("PSQ/POL/04"),
    }
    emit_pre_v2(
        draft,
        "psq4_v2_draft.json",
        "PSQ.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
