# -*- coding: utf-8 -*-
"""HRM.2 v2 — induction, training and development.

Shape follows PRE v2 (section list and order only). Wording is built
from HRM.2 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 123–124 / PDF index 129–130.

No stop-work section. Five OEs mapped to five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.2"
CHAPTER = "HRM"
OE_CODES = [
    "HRM.2.a", "HRM.2.b", "HRM.2.c", "HRM.2.d", "HRM.2.e",
]
POLICY_TITLE = "Induction, Training and Development"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: PRE v2 shape, plain English, HR roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Staff are inducted, trained and developed through an ongoing professional programme — "
    "so that every person can perform their job safely and competently, including "
    "cardiopulmonary resuscitation for direct patient care staff."
)

PURPOSE = f"""This policy describes how {HOSPITAL} provides induction training, governs training and development through an ongoing professional programme, ensures job-description-based training, delivers CPR training to direct patient care staff, and evaluates training effectiveness.

It covers five elements: induction training; written training and development policy; job-description-based training; CPR at induction and periodically; and evaluation of training effectiveness.

HRM.1 owns recruitment and job descriptions. HRM.3 owns safety-programme, disaster, fire and QI training delivery (cross-referenced programmes). HRM.4 owns performance appraisal used for development planning.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff at {HOSPITAL}: clinical, nursing, administrative and support. It applies to the {D('Training Coordinator')}, the {D('HR In-Charge / Personnel Officer')}, department heads, the {D('Medical Superintendent')} and the {D('Quality Coordinator')}.

It covers HRM.2.a–e. It does not cover safety-programme training content owned by ROM, COP, FMS and PSQ (HRM.3), performance appraisal (HRM.4) or credentialing verification (HRM.7–9).

Boundaries with other policies of {HOSPITAL}:

- HRM.1 owns recruitment and hands new hires to induction. This policy owns the induction curriculum and ongoing training programme.
- HRM.3 owns training delivery for safety, disaster, fire and QI programmes defined elsewhere. This policy owns the training framework, calendar and effectiveness evaluation.
- PSQ.4 owns management support for training resources. This policy owns the training policy and calendar."""

POLICY_STATEMENT = f"""{HOSPITAL} provides induction training to all new staff.

Written guidance governs training and development policy for staff through an ongoing programme for professional training and development.

Staff are appropriately trained based on their specific job description. Staff involved in direct patient care receive training on cardiopulmonary resuscitation at induction and periodically thereafter.

{HOSPITAL} evaluates training effectiveness and uses findings to improve the programme."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Every new staff member completes induction training within {D('the first week')} of joining — not after they have worked unsupervised.
2. A written training and development policy governs the ongoing professional programme — not only ad-hoc sessions when a problem arises.
3. Training is mapped to each role's job description — not a one-size-fits-all lecture for all departments.
4. Direct patient care staff hold current CPR certification from induction onward — not expired cards on file.
5. Training effectiveness is evaluated at least {D('annually')} — not assumed because attendance was recorded.

Staff who identify a training gap report it to the {D('Training Coordinator')} or the {D('HR In-Charge / Personnel Officer')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Induction training

Staff are provided with induction training at {HOSPITAL}. The induction checklist covers: hospital mission and policies (including HRM.1 code of conduct and grievance mechanism); department orientation; role-specific briefing; infection-control basics (pointer to HIC.1); patient rights (pointer to PRE.1); and safety reporting (pointer to PSQ.5).

Induction is completed within {D('the first week')} of joining. The new hire and supervisor sign an induction completion form filed in the personnel file. Department heads confirm role-specific items are covered.""",

f"""5.2 Training and development policy and ongoing programme

Written guidance governs training and development policy for staff through an ongoing programme for professional training and development at {HOSPITAL}. The policy covers: training needs assessment; mandatory training frequencies; nomination and approval; budget provision; documentation requirements; and external training approval.

The {D('Training Coordinator')} maintains an annual training calendar shared with all departments. The calendar lists topics, target groups, trainers, dates and venues. The policy is reviewed {D('annually')} and approved by the Medical Superintendent.""",

f"""5.3 Job-description-based training

Staff are appropriately trained based on their specific job description at {HOSPITAL}. The {D('Training Coordinator')} maintains a training matrix that maps each staff category's job description to mandatory competencies and corresponding training programmes.

Before each training cycle, HR cross-checks completed training against the matrix and schedules gaps. Training completion certificates are filed in personnel files. Department heads confirm role-specific competencies are met {D('quarterly')}.""",

f"""5.4 Cardiopulmonary resuscitation training

Staff involved in direct patient care are provided training on cardiopulmonary resuscitation at the time of induction and periodically thereafter at {HOSPITAL}. CPR training follows {D('AHA / Indian Resuscitation Council guidelines or equivalent')} and includes adult BLS and AED use where equipment is available.

A master CPR competency register tracks certification date and expiry. Refresher training is scheduled {D('every 12 months')}. Reminders are sent {D('30 days')} before expiry. No direct patient care staff member works with an expired CPR certification.""",

f"""5.5 Evaluation of training effectiveness

Evaluation of training effectiveness is done by the organisation at {HOSPITAL}. Methods include: post-training knowledge checks; supervisor observation of practice change; training feedback forms; and {D('annual')} review of training completion rates against the matrix.

The {D('Training Coordinator')} prepares an annual training effectiveness report for the Medical Superintendent and governing body. Findings drive updates to the training calendar, curriculum and delivery methods.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Approves the training and development policy and annual calendar.
- Reviews the annual training effectiveness report.

Training Coordinator
- Maintains induction checklist, training calendar, training matrix and CPR register.
- Coordinates training sessions and evaluates effectiveness.

HR In-Charge / Personnel Officer
- Ensures induction is completed; files certificates in personnel files.
- Supports training needs assessment from exit interviews and recruitment (HRM.1).

Department Heads
- Confirm role-specific induction and job-description-based training for their staff.
- Report training gaps and supervise practice change after training.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7)."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers induction, the training programme, job-description mapping, CPR and effectiveness evaluation.

What is monitored each quarter:

- Induction completed within the first week for all new hires in the quarter.
- Training and development policy current; annual calendar published.
- Training matrix current; role-specific gaps scheduled and tracked.
- CPR register current; no direct patient care staff with expired certification.
- Training effectiveness evaluation conducted and findings acted upon.

Root-cause analysis is required when a new hire worked without completed induction or when CPR certification lapsed for direct patient care staff.

This policy is reviewed {D('annually')}, and sooner when HRM.3 safety training programmes are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff receive induction training per this policy. Staff acknowledge the training and development policy at induction and {D('once a year')} after that.

Staff acknowledgement

I have read this Induction, Training and Development policy of {HOSPITAL}. I understand the induction requirements, training programme and my role-specific training obligations.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Training Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/02"),
    version=VERSION,
    prepared_by=D("Training Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.2.
- Internal documents of {HOSPITAL}: induction checklist; training and development policy; annual training calendar; role-based training matrix; CPR competency register; training effectiveness reports."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Training Coordinator.

Copies issued to: HR office; department heads; all clinical and nursing areas.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AED — automated external defibrillator
BLS — basic life support
CPR — cardiopulmonary resuscitation
HRM — Human Resource Management (NABH SHCO chapter 8)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HRM.2.a",
        "requirement": "Staff are provided with induction training.",
        "steps": "Statement of intent; Section 3; 5.1 Induction training; Section 4 item 1",
        "responsible": "Training Coordinator (curriculum); department heads (role-specific items); HR (filing)",
        "records": [
            "Structured induction checklist covering hospital policies and role orientation.",
            "Signed induction completion form in each new hire's personnel file.",
            "Supervisor confirmation of role-specific induction items.",
        ],
    },
    {
        "oe_code": "HRM.2.b",
        "requirement": "Written guidance governs training and development policy for the staff through an on-going programme for professional training and development of the staff.",
        "steps": "Section 3; 5.2 Training and development policy and ongoing programme; Section 4 item 2",
        "responsible": "Medical Superintendent (approve policy); Training Coordinator (calendar and delivery)",
        "records": [
            "Approved training and development policy document.",
            "Annual training calendar with topics, target groups and dates.",
            "Annual policy review record.",
        ],
    },
    {
        "oe_code": "HRM.2.c",
        "requirement": "Staff are appropriately trained based on their specific job description.",
        "steps": "Section 3; 5.3 Job-description-based training; Section 4 item 3",
        "responsible": "Training Coordinator (matrix); department heads (confirm competencies)",
        "records": [
            "Training matrix mapping job descriptions to mandatory competencies.",
            "Training completion certificates filed in personnel files.",
            "Quarterly compliance review showing role-specific training completion rates.",
        ],
    },
    {
        "oe_code": "HRM.2.d",
        "requirement": "Staff involved in direct patient care are provided training on cardiopulmonary resuscitation at the time of induction and periodically thereafter.",
        "steps": "Section 3; 5.4 Cardiopulmonary resuscitation training; Section 4 item 4",
        "responsible": "Training Coordinator (schedule and register); department heads (ensure compliance)",
        "records": [
            "CPR training records at induction for each direct patient care staff member.",
            "Master CPR competency register with certification and expiry dates.",
            "Periodic refresher training attendance records.",
        ],
    },
    {
        "oe_code": "HRM.2.e",
        "requirement": "Evaluation of training effectiveness is done by the organisation.",
        "steps": "Section 3; 5.5 Evaluation of training effectiveness; Section 4 item 5",
        "responsible": "Training Coordinator (evaluate and report); Medical Superintendent (review findings)",
        "records": [
            "Post-training knowledge checks and feedback forms.",
            "Supervisor observation records of practice change after training.",
            "Annual training effectiveness report with improvement actions.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: HRM.2.a–e PDF indices 129–130. No asterisked OEs. HRM.2.a/b/d Core; HRM.2.c Commitment; HRM.2.e Excellence.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. HR and training roles only."""


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
        "subtitle": "Induction, professional development and CPR in day-to-day practice.",
        "doc_no": D("HRM/POL/02"),
    }
    emit_pre_v2(
        draft,
        "hrm2_v2_draft.json",
        "HRM.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
