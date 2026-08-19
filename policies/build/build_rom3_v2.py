# -*- coding: utf-8 -*-
"""ROM.3 v2 — strategic plans, operational plans, committees, service standards and staff rights.

Shape follows PRE.2 v2 (section list and order only). Wording is built
from ROM.3 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 111 / PDF index 117.
Chapter intent: printed page 109 / PDF index 115.

Does NOT overwrite rom3_draft.json or build_rom3.py. No SQL. No Supabase insert.
No stop-work section. Five OEs clustered into five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "ROM.3"
CHAPTER = "ROM"
OE_CODES = [
    "ROM.3.a", "ROM.3.b", "ROM.3.c", "ROM.3.d", "ROM.3.e",
]
POLICY_TITLE = "Strategic Plans, Operational Plans, Committees, Service Standards and Staff Rights"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "ROM v2 template: PRE v2 shape, plain English, governance roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Those responsible for governance approve strategic and operational plans and the budget. "
    "The organisation coordinates functioning, monitors progress, reviews committees, "
    "documents measurable service standards and documents staff rights and responsibilities."
)

PURPOSE = f"""This policy establishes how {HOSPITAL} approves strategic and operational plans and the annual budget, coordinates functioning with departments and external agencies, reviews committees for effectiveness, documents measurable service standards, and documents staff rights and responsibilities.

It covers five elements: governance approval of plans and budget; coordination and progress monitoring; committee effectiveness review; measurable service standards; and staff rights and responsibilities.

The chapter intent is that the responsibilities of management are defined. The responsibilities of the leaders at all levels are defined.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the governing body, the Medical Superintendent, department and service heads, committee chairpersons, and the Quality Coordinator at {HOSPITAL}.

It covers the five elements ROM.3.a–e name. It does not cover governance roles and mission (ROM.1), leader qualifications and performance (ROM.2), or risk management and outsourced services (ROM.4).

Boundaries with other policies of {HOSPITAL}:

- ROM.1 owns governance roles, vision, mission, values and mission-level performance monitoring. This policy owns operational plans, budgets and the service-standard documents.
- ROM.2 owns the leader's qualifications, experience and performance review. This policy owns committee review and staff rights documentation.
- ROM.4 owns risk management and outsourced services. This policy owns strategic planning within which risk management sits.
- HRM owns detailed staff management. This policy owns the documented statement of staff rights and responsibilities."""

POLICY_STATEMENT = f"""{HOSPITAL} submits strategic and operational plans and the annual budget for governing-body approval before each planning cycle.

{HOSPITAL} coordinates functioning with departments and external agencies and monitors progress towards defined goals. Committees are reviewed for effectiveness. Service standards are documented as measurable indicators and monitored. Staff rights and responsibilities are documented.

{HOSPITAL} does not treat a plan that was never approved as a strategic plan, or a committee that was never reviewed as effective."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating on a strategic or operational plan that was not approved by those responsible for governance.
2. Failing to present the annual budget for governing-body approval before the financial year begins.
3. Allowing a committee to operate for more than {D('one year')} without a documented review of its effectiveness.
4. Defining service standards that are not measurable or that are never monitored.
5. Operating without a documented statement of staff rights and responsibilities.

Staff who see one of these acts report it the same day to the {D('Medical Superintendent')} or the {D('chairperson of the governing body')}."""

PROCEDURE_STEPS = [
f"""5.1 Approval of strategic and operational plans and the budget

Those responsible for governance approve the strategic and operational plans and the organisation's annual budget. The {D('Medical Superintendent')} prepares the plans and budget and presents them to the governing body for approval {D('before the start of each financial year')}.

The approved plans state the organisation's goals and objectives for the period. The budget supports those goals. Approval is recorded in the governing body's meeting minutes.

Plans are living documents; material changes during the year are re-submitted for approval.""",

f"""5.2 Coordination and progress monitoring

The organisation coordinates the functioning with departments and external agencies and monitors the progress in achieving the defined goals and objectives. The {D('Medical Superintendent')} holds a coordination mechanism — {D('monthly operational meetings with department heads and quarterly reviews with external agencies where applicable')}.

Progress against defined goals is compiled by the {D('Quality Coordinator')} and reported {D('quarterly')} to the Medical Superintendent and {D('half-yearly')} to the governing body.

This is distinct from ROM.1.c's mission-level performance monitoring. ROM.3.b monitors operational progress against specific goals and objectives.""",

f"""5.3 Committee effectiveness review

The functioning of committees is reviewed for their effectiveness. Each committee at {HOSPITAL} has documented terms of reference, membership and a meeting schedule.

The {D('Medical Superintendent')} or designated committee coordinator reviews every committee {D('annually')} for effectiveness: whether the committee met as scheduled, whether its terms of reference were fulfilled, and whether its recommendations were acted upon.

The review outcome is recorded. A committee that did not meet or whose recommendations were not followed up is flagged for corrective action.""",

f"""5.4 Measurable service standards

The organisation documents the service standards that are measurable and monitors them. Service standards are defined for {D('each department and service')}, stating the indicator, the target, the data source and the monitoring frequency.

The {D('Quality Coordinator')} compiles service-standard data {D('quarterly')} and presents it to the Medical Superintendent. Standards that are not met trigger root-cause analysis and corrective action.

Service standards are reviewed {D('annually')} or when a service changes. A standard that cannot be measured is replaced with one that can.""",

f"""5.5 Staff rights and responsibilities

The organisation documents staff rights and responsibilities. The documented statement covers {D('the right to a safe working environment, the right to be treated with dignity, the right to training and development, the right to raise concerns without retaliation, and the responsibilities that accompany those rights')}.

The {D('Medical Superintendent')} approves the statement. It is communicated to all staff at induction and is available at {D('each department notice board and the staff intranet where it exists')}.

This is the governance-level document. HRM owns detailed staff policies, grievance procedures and employment terms. ROM.3.e owns the statement that these rights and responsibilities exist as a documented set.""",
]

RESPONSIBILITY = f"""Governing body (owner(s) / board of directors / trustees)
- Approves strategic and operational plans and the annual budget.
- Receives progress reports and committee effectiveness reviews.

Medical Superintendent (Head of the Institution)
- Prepares plans and budget for governing-body approval.
- Coordinates functioning with departments and external agencies.
- Reviews or designates review of committee effectiveness.
- Approves the documented staff rights and responsibilities statement.

Quality Coordinator
- Compiles progress data against goals and service-standard data.
- Audits this policy {D('quarterly')} (see section 7).

Department / service heads
- Participate in coordination and progress monitoring.
- Define and monitor service standards within their area.

Committee chairpersons
- Ensure committees operate within terms of reference and meet as scheduled."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Strategic and operational plans and budget approved and current.
- Coordination meetings held and progress compiled.
- Committee effectiveness reviews completed on schedule.
- Service standards documented, measurable and monitored.
- Staff rights and responsibilities statement documented and communicated.

Root-cause analysis is required when plans are unapproved, a committee review is overdue by more than {D('one quarter')}, or service standards are not monitored.

This policy is reviewed {D('annually')}, and sooner when the strategic plan, committee structure or service portfolio changes."""

TRAINING_ACKNOWLEDGEMENT = f"""The Medical Superintendent, department heads, committee chairpersons and the Quality Coordinator are trained on this policy at induction and {D('once a year')} after that. Training covers plan approval, coordination, committee review, service standards and staff rights.

Staff acknowledgement

I have read this Strategic Plans, Operational Plans, Committees, Service Standards and Staff Rights policy of {HOSPITAL}. I understand the planning, coordination and monitoring requirements.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Medical Superintendent holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("ROM/POL/03"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Responsibilities of Management chapter, standard ROM.3.
- Internal documents of {HOSPITAL}: strategic plan; operational plan; annual budget; committee terms of reference and review records; service-standard register; staff rights and responsibilities statement."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: governing body members; department and service heads; committee chairpersons; nursing administration; quality office.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
HRM — Human Resource Management (NABH SHCO chapter 8)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
ROM — Responsibilities of Management (NABH SHCO chapter 7)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "ROM.3.a",
        "requirement": "Those responsible for governance approve the strategic and operational plans and the organisation's annual budget.",
        "steps": "Statement of intent; Section 3; 5.1 Approval of strategic and operational plans and the budget; Section 4 items 1, 2",
        "responsible": "Medical Superintendent (prepare); governing body (approve)",
        "records": [
            "Approved strategic and operational plans with governing-body signature or minutes.",
            "Approved annual budget with governing-body signature or minutes.",
            "Quarterly audit sample showing plans and budget are current.",
        ],
    },
    {
        "oe_code": "ROM.3.b",
        "requirement": "The organisation coordinates the functioning with departments and external agencies and monitors the progress in achieving the defined goals and objectives.",
        "steps": "Section 3; 5.2 Coordination and progress monitoring",
        "responsible": "Medical Superintendent (coordinate); Quality Coordinator (compile progress data)",
        "records": [
            "Minutes of coordination meetings with departments.",
            "Quarterly progress reports against defined goals and objectives.",
            "Records of engagement with external agencies where applicable.",
        ],
    },
    {
        "oe_code": "ROM.3.c",
        "requirement": "The functioning of committees is reviewed for their effectiveness.",
        "steps": "Section 3; 5.3 Committee effectiveness review; Section 4 item 3",
        "responsible": "Medical Superintendent or committee coordinator (review); committee chairpersons (operate)",
        "records": [
            "Terms of reference for each committee.",
            "Annual committee effectiveness review with outcome documented.",
            "Corrective actions for committees that did not meet or follow up on recommendations.",
        ],
    },
    {
        "oe_code": "ROM.3.d",
        "requirement": "The organisation documents the service standards that are measurable and monitors them.",
        "steps": "Statement of intent; Section 3; 5.4 Measurable service standards; Section 4 item 4",
        "responsible": "Quality Coordinator (compile and monitor); department heads (define within their area)",
        "records": [
            "Service-standard register with indicator, target, data source and monitoring frequency.",
            "Quarterly service-standard data compilation and trend analysis.",
            "Root-cause analysis and CAPA for standards not met.",
            "Annual review of service standards for relevance and measurability.",
        ],
    },
    {
        "oe_code": "ROM.3.e",
        "requirement": "The organisation documents staff rights and responsibilities.",
        "steps": "Section 3; 5.5 Staff rights and responsibilities; Section 4 item 5",
        "responsible": "Medical Superintendent (approve statement); HRM (detailed policies)",
        "records": [
            "Documented staff rights and responsibilities statement approved by the Medical Superintendent.",
            "Evidence of communication to all staff at induction.",
            "Display or availability records showing the statement is accessible.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """ROM.3 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Chapter intent PDF index 115. ROM.3.a–e PDF page 117. Asterisked OE: ROM.3.d. ROM.3.b and ROM.3.c are Achievement, ROM.3.a, ROM.3.d and ROM.3.e are Commitment. Note: PDF uses "organization" in ROM.3.e; clean grammar "organisation" used in this policy.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. Governance roles only."""


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
        "template_test": "rom_v2_adoptable_shape",
        "subtitle": "Plans, budgets, committees, service standards and staff rights.",
        "doc_no": D("ROM/POL/03"),
    }
    emit_pre_v2(
        draft,
        "rom3_v2_draft.json",
        "ROM.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
