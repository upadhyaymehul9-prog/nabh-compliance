# -*- coding: utf-8 -*-
"""HRM.1 v2 — human resource planning, recruitment and staff governance.

Shape follows PRE v2 (section list and order only). Wording is built
from HRM.1 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 123 / PDF index 129.
Chapter intent: printed page 122 / PDF index 128.

No stop-work section. Nine OEs mapped to nine What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.1"
CHAPTER = "HRM"
OE_CODES = [
    "HRM.1.a", "HRM.1.b", "HRM.1.c", "HRM.1.d", "HRM.1.e",
    "HRM.1.f", "HRM.1.g", "HRM.1.h", "HRM.1.i",
]
POLICY_TITLE = "Human Resource Planning, Recruitment and Staff Governance"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: PRE v2 shape, plain English, HR roles, nine steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Human resource planning supports the organisation's current and future ability to meet "
    "the care, treatment and service needs of the patient — through adequate staffing, "
    "documented recruitment and governance, and a workforce that is verified, oriented and "
    "held to a code of conduct."
)

PURPOSE = f"""This policy describes how {HOSPITAL} plans its workforce, recruits staff, maintains adequate numbers and mix, manages shortages, defines roles, verifies new hires, governs conduct, learns from exits and handles discipline and grievance.

It covers nine elements: HR planning for current and future patient-care needs; written recruitment guidance; adequate staff number and mix; contingency plans for workforce shortages; reporting relationships with job specifications and job descriptions; background checks; code of conduct; exit interviews; and written disciplinary and grievance guidance.

HRM.2 owns training and development. HRM.4 owns performance appraisal. HRM.6 owns personal files. ROM.1 owns appointment of senior leaders by the governing body.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff categories at {HOSPITAL}: clinical, nursing, administrative and support. It applies to the {D('HR In-Charge / Personnel Officer')}, the {D('Medical Superintendent')}, department heads, the governing body and the {D('Quality Coordinator')}.

It covers HRM.1.a–i. It does not cover induction and ongoing training (HRM.2), safety-programme training delivery (HRM.3), performance appraisal (HRM.4), staff health programmes (HRM.5), personal files (HRM.6) or credentialing of clinical staff (HRM.7–9).

Boundaries with other policies of {HOSPITAL}:

- ROM.1 owns appointment of senior leaders by the governing body. HRM.1 owns the recruitment process and employment file for all staff categories.
- ROM.3 owns the documented statement of staff rights and responsibilities. HRM.1 owns job descriptions and the grievance mechanism as HR processes.
- AAC.1.b and COP.4.b use credentialing verification when assigning staff to services; HRM.7–9 (when drafted) own the credentialing method."""

POLICY_STATEMENT = f"""{HOSPITAL} plans human resources to support current and future ability to meet patient care, treatment and service needs.

{HOSPITAL} maintains an adequate number and mix of staff. Written guidance governs recruitment, job definitions, disciplinary action and grievance handling.

{HOSPITAL} performs background checks on new staff, defines and implements a code of conduct, conducts exit interviews to improve HR practices, and has contingency plans for long- and short-term workforce shortages including unplanned shortages."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Human resource planning is documented and reviewed at least {D('annually')} — not only when a vacancy arises.
2. Recruitment follows written guidance approved by management — not ad-hoc hiring without a documented process.
3. Staffing levels meet the care, treatment and service needs of patients at all times — not only during accreditation visits.
4. Contingency plans for workforce shortages exist and are tested — not only a verbal agreement to call someone in.
5. Every staff category has a defined reporting relationship, job specification and job description on file.
6. No new staff member handles patients or accesses confidential records until background verification is complete.
7. The code of conduct is defined, signed at induction and enforced — not only a poster on the notice board.
8. Exit interviews are conducted for every departing staff member and findings feed into HR improvement.
9. Disciplinary and grievance handling follows written guidance with documented case records.

Staff who identify a gap in any of the above report it to the {D('HR In-Charge / Personnel Officer')} or the {D('Medical Superintendent')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Human resource planning for patient-care needs

Human resource planning at {HOSPITAL} supports the organisation's current and future ability to meet the care, treatment and service needs of the patient.

The {D('HR In-Charge / Personnel Officer')} prepares a workforce plan {D('annually')} that compares current staff numbers and skill mix against projected patient load, service expansion and known departures. Department heads provide input on clinical and operational needs.

The plan identifies gaps, proposed recruitment, redeployment and training needs (cross-reference HRM.2). The Medical Superintendent and governing body review and approve the plan. The approved plan is the basis for recruitment requisitions and budget requests.""",

f"""5.2 Written guidance for recruitment

Written guidance governs the process of recruitment at {HOSPITAL}. The recruitment procedure covers: vacancy identification and approval; advertising or sourcing; shortlisting criteria; interview panel composition; selection and offer; pre-employment checks (step 5.6); and onboarding handover to induction (HRM.2.a).

The procedure is approved by the Medical Superintendent and reviewed {D('annually')}. A recruitment register logs each vacancy with date opened, candidates considered, selection rationale and date filled.""",

f"""5.3 Adequate number and mix of staff

{HOSPITAL} maintains an adequate number and mix of staff to meet the care, treatment and service needs of the patient. Sanctioned strength is defined per department and shift based on the workforce plan and service scope (AAC.1).

Department heads maintain duty rosters showing actual staff on each shift. The {D('HR In-Charge / Personnel Officer')} compares sanctioned versus actual strength {D('monthly')} and escalates shortfalls to the Medical Superintendent with a corrective action plan.

A department-wise staff strength chart is posted in each clinical area and updated {D('monthly')}.""",

f"""5.4 Contingency plans for workforce shortages

{HOSPITAL} has contingency plans to manage long- and short-term workforce shortages, including unplanned shortages. The plan covers: mass leave or epidemic-related absences; sudden surge in admissions; unexpected resignations; and key-person unavailability.

Each department maintains a pre-approved on-call list that can be activated within {D('two hours')}. Activation triggers, escalation paths and temporary redeployment rules are documented. The plan is tested {D('twice a year')} through a tabletop exercise or mock activation.

Each shortage event is logged with date, cause, measure used, resolution time and outcome.""",

f"""5.5 Reporting relationships, job specification and job description

The reporting relationships, job specification and job description are defined for each category of staff at {HOSPITAL}. A job description template includes: designation; department; reporting line; key responsibilities; qualifications required; and performance indicators.

Each employee's personnel file (HRM.6 when drafted) contains a signed copy of the current job description and an org-chart position. Job descriptions are reviewed {D('annually')} or when the role changes. New hires sign that they have received and understood their job description at induction.""",

f"""5.6 Background check of new staff

{HOSPITAL} performs a background check of new staff before they begin patient-facing or confidential-access duties. The check covers: identity verification; previous employment confirmation; credential authenticity (cross-reference HRM.7–9 for clinical staff); and {D('police verification where the hospital policy requires it')}.

A background-check register logs each new hire, verification method, date completed and outcome. Verification certificates are filed in the personnel file. No staff member begins duties until clearance is recorded.""",

f"""5.7 Code of conduct

{HOSPITAL} defines and implements a code of conduct for its staff. The code covers: patient interaction and dignity; confidentiality; professional behaviour; dress code; social media use; and conflict-of-interest rules.

All staff sign the code at induction and at {D('annual')} refresher. Summarised conduct norms are displayed in staff areas. Breaches are handled through the disciplinary procedure (step 5.9).""",

f"""5.8 Exit interviews

Exit interviews are conducted and used as a tool to improve human resource practices at {HOSPITAL}. The {D('HR In-Charge / Personnel Officer')} conducts a standardised exit interview on the last working day of every departing staff member.

Findings are compiled {D('quarterly')} into a trend report by department. The report is presented to the Medical Superintendent and governing body with proposed HR improvements. Corrective actions are tracked to closure.""",

f"""5.9 Disciplinary and grievance handling

Written guidance governs disciplinary and grievance handling mechanisms at {HOSPITAL}. The procedure defines: types of misconduct; investigation steps; timelines; hearing process; penalties; appeal route; and confidentiality rules.

A grievance register assigns a unique case number to each complaint with date received, nature, actions taken and closure date. Disciplinary proceedings are recorded in a secure register. Staff are informed of the mechanism at induction and via the staff notice board.""",
]

RESPONSIBILITY = f"""Governing body
- Approves the annual workforce plan and HR policies.
- Reviews exit-interview trends and HR improvement actions.

Medical Superintendent
- Approves recruitment procedure, code of conduct and disciplinary/grievance guidance.
- Escalation point for staffing shortfalls and HR governance matters.

HR In-Charge / Personnel Officer
- Maintains workforce plan, recruitment register, job descriptions, background-check register, exit interviews and grievance register.
- Coordinates recruitment and onboarding handover.

Department Heads
- Provide workforce-plan input; maintain duty rosters; escalate staffing gaps.
- Ensure staff know reporting lines and job descriptions.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Verifies HR records during internal audits."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers planning, recruitment, staffing, contingency, job descriptions, background checks, conduct, exits and grievance handling.

What is monitored each quarter:

- Workforce plan is current and approved.
- Recruitment follows written guidance; register is complete.
- Sanctioned versus actual staffing reviewed monthly; no unresolved critical shortfall.
- Contingency plan tested within the last {D('six months')}.
- Job descriptions current for a sample of staff categories.
- Background checks complete before duty start for recent hires.
- Code of conduct signed by all active staff.
- Exit interviews conducted for all departures in the quarter.
- Grievance register shows cases handled per written guidance.

Root-cause analysis is required when a staffing shortfall affected patient care or when a background check was bypassed.

This policy is reviewed {D('annually')}, and sooner when HRM.6 or HRM.7–9 are drafted."""

TRAINING_ACKNOWLEDGEMENT = f"""The HR In-Charge / Personnel Officer, department heads and the Medical Superintendent are briefed on this policy at appointment and {D('once a year')} after that. All staff receive the code of conduct and grievance mechanism at induction (HRM.2.a).

Staff acknowledgement

I have read this Human Resource Planning, Recruitment and Staff Governance policy of {HOSPITAL}. I understand the code of conduct, my job description and the grievance mechanism.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The HR office holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/01"),
    version=VERSION,
    prepared_by=D("HR In-Charge / Personnel Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.1.
- Internal documents of {HOSPITAL}: workforce plan; recruitment procedure; contingency staffing plan; job description templates; code of conduct; exit interview form; disciplinary and grievance procedure."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the HR office.

Copies issued to: governing body members; HR In-Charge / Personnel Officer; department heads; quality office.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
HRM — Human Resource Management (NABH SHCO chapter 8)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HRM.1.a",
        "requirement": "Human resource planning supports the organisation's current and future ability to meet the care, treatment and service needs of the patient.",
        "steps": "Statement of intent; Section 3; 5.1 Human resource planning for patient-care needs; Section 4 item 1",
        "responsible": "HR In-Charge / Personnel Officer (prepare plan); Medical Superintendent and governing body (approve)",
        "records": [
            "Annual workforce plan with current and projected staffing analysis.",
            "Department-head input on clinical and operational needs.",
            "Governing-body approval minutes for the workforce plan.",
        ],
    },
    {
        "oe_code": "HRM.1.b",
        "requirement": "Written guidance governs the process of recruitment.",
        "steps": "Section 3; 5.2 Written guidance for recruitment; Section 4 item 2",
        "responsible": "Medical Superintendent (approve procedure); HR In-Charge / Personnel Officer (maintain register)",
        "records": [
            "Approved recruitment procedure with all process steps defined.",
            "Recruitment register with vacancy, candidates, selection rationale and fill date.",
            "Annual review record of the recruitment procedure.",
        ],
    },
    {
        "oe_code": "HRM.1.c",
        "requirement": "The organisation maintains an adequate number and mix of staff to meet the care, treatment and service needs of the patient.",
        "steps": "Section 3; 5.3 Adequate number and mix of staff; Section 4 item 3",
        "responsible": "Department heads (rosters); HR In-Charge / Personnel Officer (monthly comparison)",
        "records": [
            "Sanctioned strength chart per department and shift.",
            "Monthly duty rosters showing actual staff on shift.",
            "Monthly sanctioned-versus-actual review with escalation for shortfalls.",
        ],
    },
    {
        "oe_code": "HRM.1.d",
        "requirement": "The organisation has contingency plans to manage long- and short-term workforce shortages, including unplanned shortages.",
        "steps": "Section 3; 5.4 Contingency plans for workforce shortages; Section 4 item 4",
        "responsible": "HR In-Charge / Personnel Officer (maintain plan); department heads (on-call lists)",
        "records": [
            "Documented contingency staffing plan with activation triggers.",
            "Pre-approved on-call staff list per department.",
            "Shortage event log and twice-yearly test or mock activation record.",
        ],
    },
    {
        "oe_code": "HRM.1.e",
        "requirement": "The reporting relationships, job specification and job description are defined for each category of staff.",
        "steps": "Section 3; 5.5 Reporting relationships, job specification and job description; Section 4 item 5",
        "responsible": "HR In-Charge / Personnel Officer (templates and files); department heads (role content)",
        "records": [
            "Job description template with reporting line, responsibilities and qualifications.",
            "Signed job description in each employee's personnel file.",
            "Annual job-description review record.",
        ],
    },
    {
        "oe_code": "HRM.1.f",
        "requirement": "The organisation performs a background check of new staff.",
        "steps": "Section 3; 5.6 Background check of new staff; Section 4 item 6",
        "responsible": "HR In-Charge / Personnel Officer (conduct checks); Medical Superintendent (policy approval)",
        "records": [
            "Background-check procedure with verification items listed.",
            "Background-check register with method, date and outcome per hire.",
            "Verification certificates filed in personnel files before duty start.",
        ],
    },
    {
        "oe_code": "HRM.1.g",
        "requirement": "The organisation defines and implements a code of conduct for its staff.",
        "steps": "Section 3; 5.7 Code of conduct; Section 4 item 7",
        "responsible": "Medical Superintendent (approve code); HR In-Charge / Personnel Officer (distribution and enforcement)",
        "records": [
            "Approved code of conduct document.",
            "Signed code-of-conduct acknowledgements at induction and annual refresher.",
            "Display of summarised conduct norms in staff areas.",
        ],
    },
    {
        "oe_code": "HRM.1.h",
        "requirement": "Exit interviews are conducted and used as a tool to improve human resource practices.",
        "steps": "Section 3; 5.8 Exit interviews; Section 4 item 8",
        "responsible": "HR In-Charge / Personnel Officer (conduct interviews); Medical Superintendent (review trends)",
        "records": [
            "Standardised exit interview form completed for each departure.",
            "Quarterly exit-interview trend report with proposed improvements.",
            "Corrective action records linked to exit feedback.",
        ],
    },
    {
        "oe_code": "HRM.1.i",
        "requirement": "Written guidance governs disciplinary and grievance handling mechanisms.",
        "steps": "Section 3; 5.9 Disciplinary and grievance handling; Section 4 item 9",
        "responsible": "Medical Superintendent (approve procedure); HR In-Charge / Personnel Officer (maintain register)",
        "records": [
            "Approved disciplinary and grievance handling procedure.",
            "Grievance register with case number, nature, actions and closure.",
            "Secure disciplinary proceedings register with outcomes.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Chapter intent PDF index 128. HRM.1.a–i PDF index 129. HRM.1.b, HRM.1.e, HRM.1.i are asterisked. HRM.1.a Excellence; HRM.1.b/c Core; HRM.1.d Achievement; HRM.1.e/f/g Commitment/Core; HRM.1.h Achievement; HRM.1.i Commitment.

SHAPE: Nine What-we-do subsections (5.1–5.9). No stop-work. Disclaimer accreditation-only. HR and governance roles only."""


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
        "subtitle": "Workforce planning, recruitment and staff governance in day-to-day practice.",
        "doc_no": D("HRM/POL/01"),
    }
    emit_pre_v2(
        draft,
        "hrm1_v2_draft.json",
        "HRM.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
