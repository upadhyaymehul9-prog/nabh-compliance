# -*- coding: utf-8 -*-
"""ROM.1 v2 — governance roles, responsibilities and ethical management.

Shape follows PRE.2 v2 (section list and order only). Wording is built
from ROM.1 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 110 / PDF index 116.
Chapter intent: printed page 109 / PDF index 115.

Does NOT overwrite rom1_draft.json or build_rom1.py. No SQL. No Supabase insert.
No stop-work section. Five OEs clustered into five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "ROM.1"
CHAPTER = "ROM"
OE_CODES = [
    "ROM.1.a", "ROM.1.b", "ROM.1.c", "ROM.1.d", "ROM.1.e",
]
POLICY_TITLE = "Governance — Roles, Responsibilities and Ethical Management"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "ROM v2 template: PRE v2 shape, plain English, governance roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Those responsible for governance are identified and their roles defined. "
    "The organisation is governed professionally and ethically, with a clear vision, "
    "mission and values that guide performance and accountability."
)

PURPOSE = f"""This policy identifies who is responsible for governance at {HOSPITAL}, defines their roles and responsibilities, and establishes the ethical management framework.

It covers five elements: identification and documentation of governance roles; vision, mission and values; performance monitoring against mission; appointment of senior leaders; and the ethical management framework.

The chapter intent is that the management of the healthcare organisation is aware of and manages all key components of governance. Those responsible for governance are identified and their roles defined. The standards encourage the governance of the organisation professionally and ethically.

Note: "Responsible for Governance" refers to the governing entity and can exist in many configurations — owner(s), board of directors, public hospital ministry.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the governing body (owner(s), board of directors, trustees or equivalent), the Medical Superintendent, department and service heads, and the Quality Coordinator at {HOSPITAL}.

It covers the five governance elements ROM.1.a–e name. It does not cover the qualifications or performance of the organisation's leader (ROM.2), strategic and operational plans (ROM.3), or risk management and outsourced services (ROM.4).

Boundaries with other policies of {HOSPITAL}:

- ROM.2 owns the qualifications, experience and performance review of the person heading the organisation. This policy owns who appoints that person (ROM.1.d).
- ROM.3 owns strategic and operational plans, budgets, committee effectiveness, service standards and staff rights. This policy owns monitoring performance against mission (ROM.1.c).
- ROM.4 owns risk management, reporting of system failures, and outsourced services. This policy owns the ethical framework within which those activities sit (ROM.1.e).
- HRM owns staff-level human-resource management. This policy owns appointment of senior leaders by the governing body (ROM.1.d)."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies those responsible for governance, documents their roles and responsibilities, and makes the organisation's vision, mission and values public.

{HOSPITAL} monitors and measures organisational performance against the stated mission, appoints senior leaders through the governing body, and supports an ethical management framework.

{HOSPITAL} does not treat a vision-mission poster as a substitute for governance roles being defined, performance being measured, or ethics being managed."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating without a documented identification of who is responsible for governance and what their roles are.
2. Keeping the vision, mission and values as an internal document that patients, families and staff cannot see.
3. Failing to monitor or measure the performance of the organisation against the stated mission for more than {D('one year')}.
4. Appointing a senior leader without the documented involvement or approval of those responsible for governance.
5. Operating without a documented ethical management framework, or treating a code of ethics display as a substitute for a framework that is supported and monitored.

Staff who see one of these acts report it the same day to the {D('Medical Superintendent')} or the {D('chairperson of the governing body')}."""

PROCEDURE_STEPS = [
f"""5.1 Identification of governance roles and responsibilities

Those responsible for governance at {HOSPITAL} are identified, and their roles and responsibilities are defined and documented. The governing entity may be an owner, a board of directors, trustees or equivalent.

The {D('Medical Superintendent')} holds the current governance register that names each governance role holder, their designation, and their documented responsibilities. The register is reviewed {D('annually')} or when a governance role changes.

The governance structure is communicated to department and service heads so that reporting lines are understood.""",

f"""5.2 Vision, mission, values and public display

Those responsible for governance lay down the organisation's vision, mission and values and make them public. The vision, mission and values are displayed at {D('the main entrance, reception and each patient-care area')} in {D('Hindi and English')}.

The {D('Medical Superintendent')} confirms that the current version is displayed and that staff can explain the mission in their own words during induction and {D('annual refresher')} training.

A poster alone does not meet this requirement if staff cannot relate it to their daily work.""",

f"""5.3 Performance monitoring against mission

Those responsible for governance monitor and measure the performance of the organisation against the stated mission. Performance indicators are defined, collected {D('quarterly')} and presented to the governing body {D('at least twice a year')}.

The {D('Quality Coordinator')} compiles the performance report. The governing body records its review and any corrective direction in meeting minutes.

This step is distinct from ROM.3's operational-plan monitoring. ROM.1.c measures whether the organisation is achieving its stated mission; ROM.3.b monitors progress against defined goals and objectives.""",

f"""5.4 Appointment of senior leaders

Those responsible for governance appoint the senior leaders in the organisation. Appointment is documented with the governing body's approval, including the criteria used.

Senior leaders at {HOSPITAL} include the {D('Medical Superintendent, Nursing Superintendent and Quality Coordinator')} — or equivalent designations as the governing body determines. The governing body records the appointment decision and the qualifications or experience considered.

This step does not cover the qualifications or performance of the organisation's leader — those are ROM.2.""",

f"""5.5 Ethical management framework

Those responsible for governance support the ethical management framework of the organisation. The framework includes {D('a code of ethics, a conflict-of-interest declaration for governance members, a mechanism for reporting ethical concerns, and a review of ethical compliance')}.

The {D('Medical Superintendent')} is accountable for operating within the framework. The governing body reviews ethical compliance {D('annually')} and when a concern is reported.

This is not a display-only code of ethics. The framework must include a mechanism for reporting and a review cycle. ROM.4's risk-management scope does not replace the ethical framework; the two are complementary.""",
]

RESPONSIBILITY = f"""Governing body (owner(s) / board of directors / trustees)
- Accountable for governance roles being identified, documented and fulfilled.
- Lays down vision, mission and values and makes them public.
- Monitors performance against mission.
- Appoints senior leaders.
- Supports the ethical management framework.

Medical Superintendent (Head of the Institution)
- Holds the governance register and keeps it current.
- Ensures vision, mission and values are displayed and understood by staff.
- Operates within the ethical management framework.
- Compiles or coordinates performance reports for the governing body.

Quality Coordinator
- Compiles performance data for mission monitoring (section 5.3).
- Audits this policy {D('quarterly')} (see section 7).

Department / service heads
- Understand governance structure and reporting lines.
- Participate in performance monitoring within their area."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Governance register current and complete.
- Vision, mission and values displayed and staff can explain them.
- Performance indicators collected and presented to the governing body on schedule.
- Senior-leader appointments documented with governing-body approval.
- Ethical management framework in operation, not display only.

Root-cause analysis is required when a governance role is undocumented or the performance report is overdue by more than {D('one quarter')}.

This policy is reviewed {D('annually')}, and sooner when governance composition, vision, mission or values change."""

TRAINING_ACKNOWLEDGEMENT = f"""All senior leaders, department heads and the Quality Coordinator are trained on this policy at induction and {D('once a year')} after that. Training covers governance roles, mission monitoring, appointment process and the ethical framework.

Staff acknowledgement

I have read this Governance — Roles, Responsibilities and Ethical Management policy of {HOSPITAL}. I understand the governance structure and my accountability within it.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Medical Superintendent holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("ROM/POL/01"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Responsibilities of Management chapter, standard ROM.1.
- Internal documents of {HOSPITAL}: governance register; vision, mission and values display; performance monitoring reports; senior-leader appointment records; ethical management framework and code of ethics."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: governing body members; department and service heads; nursing administration; quality office.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
ROM — Responsibilities of Management (NABH SHCO chapter 7)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "ROM.1.a",
        "requirement": "Those responsible for governance are identified, and their roles and responsibilities are defined and documented.",
        "steps": "Statement of intent; Section 3; 5.1 Identification of governance roles and responsibilities; Section 4 items 1, 6",
        "responsible": "Governing body (identify); Medical Superintendent (register and communicate)",
        "records": [
            "Governance register naming each role holder, designation and documented responsibilities.",
            "Evidence of annual review or update when a governance role changes.",
            "Communication to department and service heads of governance structure.",
            "Quarterly audit sample showing register is current.",
        ],
    },
    {
        "oe_code": "ROM.1.b",
        "requirement": "Those responsible for governance lay down the organisation's vision, mission and values and make them public.",
        "steps": "Statement of intent; Section 3; 5.2 Vision, mission, values and public display; Section 4 item 2",
        "responsible": "Governing body (lay down); Medical Superintendent (display and staff understanding)",
        "records": [
            "Approved vision, mission and values document signed by the governing body.",
            "Photographs or log showing public display at defined locations.",
            "Induction and annual training records showing staff can explain the mission.",
            "Quarterly audit sample showing display is current and legible.",
        ],
    },
    {
        "oe_code": "ROM.1.c",
        "requirement": "Those responsible for governance monitor and measure the performance of the organisation against the stated mission.",
        "steps": "Section 3; 5.3 Performance monitoring against mission",
        "responsible": "Quality Coordinator (compile); governing body (review and direct)",
        "records": [
            "Defined performance indicators linked to the stated mission.",
            "Quarterly performance data compilation.",
            "Meeting minutes showing governing-body review and corrective direction.",
        ],
    },
    {
        "oe_code": "ROM.1.d",
        "requirement": "Those responsible for governance appoint the senior leaders in the organisation.",
        "steps": "Section 3; 5.4 Appointment of senior leaders; Section 4 item 4",
        "responsible": "Governing body (appoint); Medical Superintendent (hold records)",
        "records": [
            "Appointment letters for senior leaders with governing-body approval documented.",
            "Record of criteria used for each appointment.",
            "Quarterly audit sample showing appointments are documented.",
        ],
    },
    {
        "oe_code": "ROM.1.e",
        "requirement": "Those responsible for governance support the ethical management framework of the organisation.",
        "steps": "Statement of intent; Section 3; 5.5 Ethical management framework; Section 4 items 5, 6",
        "responsible": "Governing body (support); Medical Superintendent (operate within framework)",
        "records": [
            "Documented ethical management framework including code of ethics, conflict-of-interest declarations and reporting mechanism.",
            "Governing-body review of ethical compliance at least annually.",
            "Records of ethical concerns reported and actions taken.",
            "Quarterly audit sample showing framework is in operation, not display only.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """ROM.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Chapter intent PDF index 115. ROM.1.a–e PDF page 116. Asterisked OEs: ROM.1.a, ROM.1.b, ROM.1.e. ROM.1.c Achievement, ROM.1.d Commitment, rest Commitment.

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
        "subtitle": "Governance roles, mission, performance and ethical management.",
        "doc_no": D("ROM/POL/01"),
    }
    emit_pre_v2(
        draft,
        "rom1_v2_draft.json",
        "ROM.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
