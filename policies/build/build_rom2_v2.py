# -*- coding: utf-8 -*-
"""ROM.2 v2 — qualifications, experience and performance of the organisation's leader.

Shape follows PRE.2 v2 (section list and order only). Wording is built
from ROM.2 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 110 / PDF index 116.
Chapter intent: printed page 109 / PDF index 115.

Does NOT overwrite rom2_draft.json or build_rom2.py. No SQL. No Supabase insert.
No stop-work section. Four OEs clustered into four What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "ROM.2"
CHAPTER = "ROM"
OE_CODES = [
    "ROM.2.a", "ROM.2.b", "ROM.2.c", "ROM.2.d",
]
POLICY_TITLE = "Organisation's Leader — Qualifications, Experience and Performance"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "ROM v2 template: PRE v2 shape, plain English, governance roles, four steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The person heading the organisation has the appropriate qualifications and experience "
    "to lead it, complies with applicable legislation, and is reviewed for effectiveness."
)

PURPOSE = f"""This policy establishes that the person heading {HOSPITAL} has appropriate administrative qualifications and experience, complies with applicable legislation, and is reviewed for effectiveness.

It covers four elements: administrative qualifications of the leader; administrative experience; compliance with laid-down and applicable legislations, regulations and notifications; and performance review.

The chapter intent is that the responsibilities of management are defined. The responsibilities of the leaders at all levels are defined. Management executes its responsibility for compliance with all applicable regulations.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the person heading {HOSPITAL} (the Medical Superintendent or equivalent), the governing body that appoints and reviews that person, and the Quality Coordinator.

It covers the four elements ROM.2.a–d name. It does not cover governance roles and responsibilities (ROM.1), strategic and operational plans (ROM.3), or risk management and outsourced services (ROM.4).

Boundaries with other policies of {HOSPITAL}:

- ROM.1 owns identification of governance roles and appointment of senior leaders. This policy owns the qualifications and experience of the person heading the organisation (the appointee).
- ROM.3 owns strategic and operational plans and service standards. This policy owns the leader's compliance with legislation relevant to those plans.
- HRM owns general staff qualifications and credentialling. This policy is specific to the person heading the organisation."""

POLICY_STATEMENT = f"""{HOSPITAL} ensures that the person heading the organisation has requisite and appropriate administrative qualifications and experience.

The leader complies with laid-down and applicable legislations, regulations and notifications. The governing body reviews the leader's performance for effectiveness.

{HOSPITAL} does not treat a qualification certificate on file as a substitute for verified appropriateness, or a job description as a substitute for a performance review."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating without documented evidence that the person heading the organisation holds requisite and appropriate administrative qualifications.
2. Operating without documented evidence that the person heading the organisation has requisite and appropriate administrative experience.
3. Failing to maintain a documented register of applicable legislations, regulations and notifications with which the leader must comply.
4. Omitting the performance review of the organisation's leader for more than {D('one year')}.

Staff who become aware of one of these gaps report it to the {D('chairperson of the governing body')}."""

PROCEDURE_STEPS = [
f"""5.1 Administrative qualifications of the leader

The person heading {HOSPITAL} has requisite and appropriate administrative qualifications. The governing body documents the qualifications required for the role and verifies that the incumbent holds them.

The {D('Medical Superintendent')} maintains a file of qualification certificates and the governing body's verification record. The file is reviewed when the incumbent changes or when qualifications are re-verified.

«Requisite qualifications» means the qualifications the governing body defines as necessary for the administrative leadership of a small healthcare organisation — {D('MBBS with a hospital administration diploma or equivalent, or as the governing body determines')}.""",

f"""5.2 Administrative experience of the leader

The person heading {HOSPITAL} has requisite and appropriate administrative experience. The governing body documents the experience required and verifies that the incumbent has it.

The experience record includes years of administrative service, the nature of organisations previously led or managed, and any relevant governance or management training. The record is held alongside the qualifications file.

«Requisite experience» means the experience the governing body defines as necessary — {D('at least three years of healthcare administration or as the governing body determines')}.""",

f"""5.3 Compliance with applicable legislation

The leader is responsible for and complies with the laid-down and applicable legislations, regulations and notifications. A register of applicable legislation is maintained and reviewed {D('annually')} or when a new regulation or notification is issued.

The {D('Medical Superintendent')} holds the compliance register. Each entry states the legislation or regulation, the requirement, the compliance status and the date of last verification. Non-compliance is escalated to the governing body.

This step does not duplicate the detailed statutory requirements addressed in other policies of {HOSPITAL} (for example FMS for fire and safety, HIC for biomedical waste). It records that the leader is responsible for overall compliance and that a register exists.""",

f"""5.4 Performance review of the leader

The performance of the organisation's leader is reviewed for effectiveness. The governing body conducts a documented performance review {D('annually')}.

The review considers {D('achievement against the organisation mission and strategic plan, compliance status, quality indicators, patient-safety record and leadership competencies')}. The review outcome and any improvement actions are recorded in the governing body's minutes.

ROM.1.c monitors organisation performance against mission. This step reviews the leader's personal effectiveness in delivering that performance.""",
]

RESPONSIBILITY = f"""Governing body (owner(s) / board of directors / trustees)
- Defines required qualifications and experience for the leader role.
- Verifies qualifications and experience of the incumbent.
- Conducts and documents annual performance review.

Medical Superintendent (person heading the organisation)
- Maintains the qualifications and experience file.
- Holds the compliance register and ensures it is current.
- Participates in the performance review process.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Supports compilation of quality indicators for the leader's performance review."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Qualifications and experience file is current and verified.
- Compliance register is current with no overdue items.
- Annual performance review is on schedule.
- No prohibited gaps from section 4 exist.

Root-cause analysis is required when the compliance register is overdue by more than {D('one quarter')} or the performance review is overdue.

This policy is reviewed {D('annually')}, and sooner when the leader changes or applicable legislation changes significantly."""

TRAINING_ACKNOWLEDGEMENT = f"""The Medical Superintendent, governing body members and the Quality Coordinator are briefed on this policy at the leader's appointment and {D('once a year')} after that. Briefing covers qualifications, experience, compliance and performance review requirements.

Staff acknowledgement

I have read this Organisation's Leader — Qualifications, Experience and Performance policy of {HOSPITAL}. I understand the requirements for the leadership role and the review process.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The governing body holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("ROM/POL/02"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Responsibilities of Management chapter, standard ROM.2.
- Internal documents of {HOSPITAL}: leader's qualifications and experience file; compliance register; governing-body meeting minutes with performance review records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: governing body members; Medical Superintendent; quality office.

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
        "oe_code": "ROM.2.a",
        "requirement": "The person heading the organisation has requisite and appropriate administrative qualifications.",
        "steps": "Statement of intent; Section 3; 5.1 Administrative qualifications of the leader; Section 4 item 1",
        "responsible": "Governing body (define and verify); Medical Superintendent (maintain file)",
        "records": [
            "Documented qualifications required for the leader role.",
            "Qualification certificates on file with governing-body verification record.",
            "Quarterly audit sample showing file is current.",
        ],
    },
    {
        "oe_code": "ROM.2.b",
        "requirement": "The person heading the organisation has requisite and appropriate administrative experience.",
        "steps": "Statement of intent; Section 3; 5.2 Administrative experience of the leader; Section 4 item 2",
        "responsible": "Governing body (define and verify); Medical Superintendent (maintain file)",
        "records": [
            "Documented experience required for the leader role.",
            "Experience record on file with governing-body verification.",
            "Quarterly audit sample showing file is current.",
        ],
    },
    {
        "oe_code": "ROM.2.c",
        "requirement": "The leader is responsible for and complies with the laid-down and applicable legislations, regulations and notifications.",
        "steps": "Section 3; 5.3 Compliance with applicable legislation; Section 4 item 3",
        "responsible": "Medical Superintendent (hold register and comply); governing body (escalation)",
        "records": [
            "Compliance register with legislation, requirement, status and last-verification date.",
            "Evidence of annual review or update when new regulation is issued.",
            "Escalation records for non-compliance items.",
        ],
    },
    {
        "oe_code": "ROM.2.d",
        "requirement": "The performance of the organisation's leader is reviewed for effectiveness.",
        "steps": "Section 3; 5.4 Performance review of the leader; Section 4 item 4",
        "responsible": "Governing body (conduct review); Quality Coordinator (quality indicators)",
        "records": [
            "Documented annual performance review with criteria and outcome.",
            "Governing-body meeting minutes recording the review.",
            "Improvement actions and follow-up where applicable.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """ROM.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Chapter intent PDF index 115. ROM.2.a–d PDF page 116. No asterisked OEs. ROM.2.c is Core, ROM.2.d is Achievement, ROM.2.a and ROM.2.b are Commitment.

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only. Governance roles only."""


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
        "subtitle": "Leader qualifications, experience, compliance and performance review.",
        "doc_no": D("ROM/POL/02"),
    }
    emit_pre_v2(
        draft,
        "rom2_v2_draft.json",
        "ROM.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
