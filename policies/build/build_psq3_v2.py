# -*- coding: utf-8 -*-
"""PSQ.3 v2 — clinical audit and quality improvement programmes.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 109.

No stop-work section. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PSQ.3"
CHAPTER = "PSQ"
OE_CODES = [
    "PSQ.3.a", "PSQ.3.b", "PSQ.3.c", "PSQ.3.d", "PSQ.3.e",
]
POLICY_TITLE = "Clinical Audit and Quality Improvement Programmes"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PSQ v2 template: PRE v2 shape, plain English, PSQ roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "There is an established system for clinical audit and quality improvement "
    "programmes — audits that improve patient care, not audits that exist only in "
    "a register."
)

PURPOSE = f"""This policy describes how {HOSPITAL} maintains an established system for clinical audit and quality improvement programmes, satisfying PSQ.3.a–e.

It covers five elements: clinical audits performed to improve patient care; audit parameters defined by the organisation; medical and nursing staff participation; remedial measures implemented; and quality improvement projects undertaken.

PSQ.3 owns the clinical audit system and QI projects. PSQ.1.h owns regular audits as a monitoring tool within the programmes. PSQ.2 owns indicators that may trigger an audit topic. PSQ.1 owns the QI programme under which QI projects operate.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical departments at {HOSPITAL} and to medical staff, nursing staff, the {D('Quality Coordinator')} and the patient-safety / QI committee.

It covers the five objective elements PSQ.3.a–e. It does not cover the patient-safety and QI programmes as a whole (PSQ.1), key indicators (PSQ.2), management support (PSQ.4), or incident analysis (PSQ.5).

Boundaries with other policies of {HOSPITAL}:

- PSQ.1 owns the patient-safety and QI programmes. PSQ.3 is the clinical audit system that feeds findings into those programmes.
- PSQ.1.h is regular audits as a monitoring tool. PSQ.3 owns the detailed clinical audit methodology and documentation.
- PSQ.2 owns indicators. An indicator breach may trigger a clinical audit topic under PSQ.3.
- PSQ.3.e (QI projects) operates under the QI programme (PSQ.1.e–g). The project method is here; the programme governance is PSQ.1."""

POLICY_STATEMENT = f"""{HOSPITAL} performs clinical audits to improve the quality of patient care and documents the audit cycle from parameter selection through findings, remedial measures and re-audit.

Medical and nursing staff participate in the clinical audit system. Remedial measures are implemented based on audit findings. {HOSPITAL} undertakes quality improvement projects that follow a structured methodology.

Clinical audits and QI projects exist to change practice, not to fill a register before an external visit."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Clinical audits are performed and documented — an undocumented audit does not count.
2. Audit parameters are defined by the organisation before the audit begins, not chosen retroactively to match available data.
3. Medical and nursing staff participate in the clinical audit system — audits are not conducted solely by the quality department.
4. Remedial measures are implemented based on audit findings — a finding without a corrective action is incomplete.
5. Quality improvement projects are undertaken with a structured methodology — not labelled as QI without a plan, measure, analysis and outcome.

Staff who identify that an audit finding has not been acted upon report it to the {D('Quality Coordinator')} within {D('one working week')}."""

PROCEDURE_STEPS = [
f"""5.1 Clinical audits to improve patient care

Clinical audits are performed at {HOSPITAL} to improve the quality of patient care and are documented. Each audit follows the audit cycle: select topic, define criteria and standards, collect data, analyse findings, implement changes, and re-audit to confirm improvement.

Audit reports include: topic and rationale, parameters audited, method, sample, findings, gaps identified, remedial measures recommended, responsible person, target date and re-audit date. Completed audits are filed with the {D('Quality Coordinator')} and findings are reported to the QI committee.""",

f"""5.2 Audit parameters defined by the organisation

The parameters to be audited are defined by {HOSPITAL} before each audit begins. Parameter selection is based on {D('clinical risk areas, indicator trends (PSQ.2), incident patterns (PSQ.5), national guidelines, patient feedback and committee priorities')}.

The QI committee approves the annual audit plan that lists topics, parameters, frequency and responsible auditors. Ad-hoc audits may be added when an indicator breach, incident cluster or committee decision requires it. Parameters are documented in the audit plan and in each audit report.""",

f"""5.3 Medical and nursing staff participation

Medical and nursing staff participate in the clinical audit system. Clinicians serve as audit leads or team members for topics within their practice area. Nursing staff participate in audits related to nursing care, documentation, infection control and medication administration.

Participation is documented in audit team composition records and meeting attendance. The {D('Quality Coordinator')} ensures that audits are not conducted solely by the quality department and that clinical ownership of audit findings is maintained.""",

f"""5.4 Remedial measures implemented

Remedial measures are implemented based on clinical audit findings. Each audit report includes specific remedial actions with a responsible person and target date. The {D('Quality Coordinator')} tracks remedial measures to completion and reports status to the QI committee.

Re-audit is scheduled to verify that remedial measures have achieved the intended improvement. If a re-audit shows that the gap persists, the committee escalates the issue and assigns additional measures. Remedial measures that require resources beyond the department are escalated to management under PSQ.4.""",

f"""5.5 Quality improvement projects

{HOSPITAL} undertakes quality improvement projects using a structured methodology — {D('Plan-Do-Study-Act (PDSA) cycles or an equivalent method documented in the project charter')}.

Each QI project has a charter that includes: problem statement, aim, measures, baseline data, intervention, results and sustainability plan. Projects operate under the QI programme (PSQ.1.e–g) and are reported to the QI committee at {D('each quarterly meeting')}. Completed projects are documented with outcomes and lessons learned. The {D('Quality Coordinator')} maintains a QI project register.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that the clinical audit system and QI projects are implemented.

Quality Coordinator
- Maintains audit plan, audit reports and QI project register.
- Tracks remedial measures and re-audits to completion.
- Reports to the QI committee.

Patient-Safety / QI Committee
- Approves annual audit plan and QI project charters.
- Reviews findings, remedial measures and project outcomes.

Treating Clinicians (Medical Staff)
- Serve as audit leads or team members; own clinical findings.

Nursing Staff
- Participate in audits relevant to nursing care and documentation.

Department Heads
- Support audit access and implement department-level remedial measures."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers the clinical audit system and QI projects.

What is monitored each quarter:

- Clinical audits performed and documented per the annual plan.
- Parameters defined before each audit, not retroactively.
- Medical and nursing staff participation documented.
- Remedial measures assigned, tracked and re-audited.
- QI projects chartered, measured and reported to committee.

Root-cause analysis is required when no clinical audit has been completed in a quarter or when remedial measures remain open beyond {D('90 days')}.

This policy is reviewed {D('annually')}, and sooner when PSQ.1, PSQ.2, PSQ.4 or PSQ.5 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All medical and nursing staff are trained on the clinical audit system at induction and {D('once a year')} after that. Training covers audit methodology, participation expectations, remedial measures and QI project methodology.

Staff acknowledgement

I have read this Clinical Audit and Quality Improvement Programmes policy of {HOSPITAL}. I understand the audit system and my role in clinical audits and quality improvement.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PSQ/POL/03"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Safety and Quality Improvement chapter, standard PSQ.3.
- Internal documents of {HOSPITAL}: annual clinical audit plan; audit reports; QI project charters and registers; QI committee minutes (PSQ.1); indicator dashboard (PSQ.2)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: patient-safety / QI committee members; department heads; nursing administration; all clinical areas.

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PDSA — Plan-Do-Study-Act
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 9)
QI — quality improvement
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PSQ.3.a",
        "requirement": "Clinical audits are performed to improve the quality of patient care and documented.",
        "steps": "Statement of intent; Section 3; 5.1 Clinical audits to improve patient care; Section 4 items 1, 4",
        "responsible": "Quality Coordinator (file and report); treating clinicians (conduct); QI committee (review)",
        "records": [
            "Clinical audit reports with topic, criteria, method, findings and remedial measures.",
            "Audit cycle completion records showing re-audit where applicable.",
            "QI committee minutes showing audit findings reviewed.",
        ],
    },
    {
        "oe_code": "PSQ.3.b",
        "requirement": "The parameters to be audited are defined by the organisation.",
        "steps": "Section 3; 5.2 Audit parameters defined; Section 4 item 2",
        "responsible": "QI committee (approve plan); Quality Coordinator (document parameters)",
        "records": [
            "Annual audit plan with topics, parameters, frequency and auditors approved by committee.",
            "Individual audit reports showing parameters defined before data collection.",
            "Ad-hoc audit requests with rationale and parameter definitions.",
        ],
    },
    {
        "oe_code": "PSQ.3.c",
        "requirement": "Medical and nursing staff participates in this system.",
        "steps": "Section 3; 5.3 Medical and nursing staff participation; Section 4 item 3",
        "responsible": "Treating clinicians and nursing staff (participate); Quality Coordinator (ensure participation)",
        "records": [
            "Audit team composition records showing medical and nursing members.",
            "Meeting attendance records for audit-related discussions.",
            "Evidence that audits are not conducted solely by the quality department.",
        ],
    },
    {
        "oe_code": "PSQ.3.d",
        "requirement": "Remedial measures are implemented.",
        "steps": "Section 3; 5.4 Remedial measures implemented; Section 4 item 4",
        "responsible": "Quality Coordinator (track); department heads (implement); QI committee (escalate)",
        "records": [
            "Remedial measure action plans with responsible person and target date.",
            "Tracking records showing completion status and committee reporting.",
            "Re-audit reports confirming improvement or escalation records where gap persists.",
        ],
    },
    {
        "oe_code": "PSQ.3.e",
        "requirement": "The organisation undertakes quality improvement projects.",
        "steps": "Section 3; 5.5 Quality improvement projects; Section 4 item 5",
        "responsible": "Quality Coordinator (register and facilitate); QI committee (charter and review)",
        "records": [
            "QI project charters with problem statement, aim, measures and intervention.",
            "Project outcome reports with results and sustainability plan.",
            "QI project register maintained by the Quality Coordinator.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PSQ.3 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "There is an established system for clinical audit and quality improvement programmes." PSQ.3.a–e PDF page 109. No asterisked OEs. PSQ.3.a/b/c/d Commitment; PSQ.3.e Core.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. PSQ roles only."""


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
        "subtitle": "Clinical audit and quality improvement in day-to-day practice.",
        "doc_no": D("PSQ/POL/03"),
    }
    emit_pre_v2(
        draft,
        "psq3_v2_draft.json",
        "PSQ.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
