# -*- coding: utf-8 -*-
"""HRM.4 v2 — performance appraisal.

Shape follows PRE v2 (section list and order only). Wording is built
from HRM.4 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 124 / PDF index 130.

No stop-work section. Four OEs mapped to four What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HRM.4"
CHAPTER = "HRM"
OE_CODES = [
    "HRM.4.a", "HRM.4.b", "HRM.4.c", "HRM.4.d",
]
POLICY_TITLE = "Performance Appraisal"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HRM v2 template: PRE v2 shape, plain English, HR roles, four steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Performance appraisal is done for staff, evaluated against pre-determined criteria at "
    "defined intervals, used for further development, and made known to staff at induction — "
    "so that performance is managed, not assumed."
)

PURPOSE = f"""This policy describes how {HOSPITAL} conducts performance appraisal for staff: making staff aware of the appraisal system at induction, evaluating performance against pre-determined criteria, using appraisal for further development, and documenting appraisals at defined intervals.

It covers four elements: performance appraisal with induction awareness; pre-determined evaluation criteria; appraisal as a development tool; and defined-interval documented appraisal.

HRM.1 owns job descriptions that feed appraisal criteria. HRM.2 owns training triggered by appraisal outcomes. ROM.2.d owns performance review of the person heading the organisation.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff categories at {HOSPITAL} except the person heading the organisation (ROM.2.d owns that review). It applies to the {D('HR In-Charge / Personnel Officer')}, department heads, the {D('Medical Superintendent')} and the {D('Quality Coordinator')}.

It covers HRM.4.a–d. It does not cover the governing body's review of the Medical Superintendent (ROM.2.d), recruitment (HRM.1) or the training programme (HRM.2).

Boundaries with other policies of {HOSPITAL}:

- ROM.2.d owns performance review of the person heading the organisation. HRM.4 owns appraisal of all other staff.
- HRM.1.e owns job descriptions that define role expectations used as appraisal criteria.
- HRM.2 owns training and development delivered after appraisal identifies gaps."""

POLICY_STATEMENT = f"""{HOSPITAL} conducts performance appraisal for staff within the organisation. Staff are made aware of the appraisal system at the time of induction.

Performance is evaluated based on pre-determined criteria linked to job descriptions. The appraisal system is used as a tool for further development. Performance appraisal is carried out at defined intervals and is documented."""

NON_NEGOTIABLES = f"""The following are required. There is no convenience exception.

1. Every staff member is informed of the appraisal system at induction — not only when the first appraisal is due.
2. Appraisal criteria are pre-determined and linked to the job description — not improvised at the review meeting.
3. Appraisal outcomes drive development actions — not only a form filed and forgotten.
4. Appraisal is conducted at defined intervals for every active staff member — not only when a promotion is considered.
5. Every appraisal is documented and signed by the appraiser and appraisee.

Staff who identify a missed appraisal report it to the {D('HR In-Charge / Personnel Officer')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Performance appraisal and induction awareness

Performance appraisal is done for staff within the organisation and staff are made aware of the same at the time of induction at {HOSPITAL}. Induction covers: the purpose of appraisal; the appraisal cycle; who conducts the appraisal; how criteria are set; and how outcomes link to development (HRM.2) and disciplinary action (HRM.1.i).

The new hire signs an induction acknowledgement that includes appraisal awareness. The signed form is filed in the personnel file.""",

f"""5.2 Pre-determined evaluation criteria

Performance is evaluated based on pre-determined criteria at {HOSPITAL}. Criteria are derived from the job description (HRM.1.e) and include: key responsibilities; quality and safety behaviours; teamwork and communication; attendance and punctuality; and {D('patient satisfaction or clinical indicators where applicable')}.

Criteria are documented in the appraisal form template before the review cycle begins. Criteria are reviewed {D('annually')} when job descriptions are updated. The appraiser and appraisee discuss criteria at the start of each appraisal cycle.""",

f"""5.3 Appraisal for further development

The appraisal system is used as a tool for further development at {HOSPITAL}. Each appraisal identifies strengths, areas for improvement and a development plan. Development actions may include: training (HRM.2); mentoring; role adjustment; or performance improvement plans.

Department heads and the {D('HR In-Charge / Personnel Officer')} track development actions to completion. The next appraisal cycle reviews progress on the development plan.""",

f"""5.4 Defined intervals and documentation

Performance appraisal is carried out at defined intervals and is documented at {HOSPITAL}. The appraisal cycle is {D('annually')} for all staff categories. Probationary staff receive an additional appraisal at {D('three months')} and {D('six months')}.

Each appraisal uses the standard form: criteria scores or ratings; narrative comments; development plan; and signatures of appraiser and appraisee. Completed forms are filed in the personnel file within {D('two weeks')} of the review meeting. The HR office maintains an appraisal schedule and tracks overdue appraisals {D('monthly')}.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Approves the appraisal policy and form template.
- Conducts appraisal of department heads.

HR In-Charge / Personnel Officer
- Maintains appraisal schedule, form template and personnel files.
- Tracks overdue appraisals and escalates to the Medical Superintendent.

Department Heads
- Conduct appraisals for staff in their departments.
- Implement development plans and track actions to completion.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).

All Staff
- Participate in appraisal; acknowledge awareness at induction; work on development plans."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers induction awareness, criteria, development use and documentation.

What is monitored each quarter:

- Induction includes appraisal awareness for all new hires in the quarter.
- Appraisal form template has pre-determined criteria linked to job descriptions.
- Sample of completed appraisals shows development plans with tracked actions.
- Appraisal schedule shows no staff overdue by more than {D('one month')}.
- All completed forms signed and filed within two weeks.

Root-cause analysis is required when an active staff member has no appraisal on file for more than {D('13 months')}.

This policy is reviewed {D('annually')}, and sooner when HRM.1 job description templates change."""

TRAINING_ACKNOWLEDGEMENT = f"""Department heads and the HR In-Charge / Personnel Officer are briefed on this policy at appointment and {D('once a year')} after that. All staff are made aware of the appraisal system at induction per step 5.1.

Staff acknowledgement

I have been informed of the performance appraisal system at {HOSPITAL}. I understand the appraisal cycle, criteria and how outcomes link to my development.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The HR office holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HRM/POL/04"),
    version=VERSION,
    prepared_by=D("HR In-Charge / Personnel Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Human Resource Management chapter, standard HRM.4.
- Internal documents of {HOSPITAL}: appraisal form template; appraisal schedule; job descriptions (HRM.1.e); development plan records; personnel files."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the HR office.

Copies issued to: department heads; HR In-Charge / Personnel Officer; quality office.

The current version is available to all staff at the {D('HR office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """HRM — Human Resource Management (NABH SHCO chapter 8)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HRM.4.a",
        "requirement": "Performance appraisal is done for staff within the organisation and staff are made aware of the same at the time of induction.",
        "steps": "Statement of intent; Section 3; 5.1 Performance appraisal and induction awareness; Section 4 item 1",
        "responsible": "HR In-Charge / Personnel Officer (induction content); department heads (conduct appraisals)",
        "records": [
            "Induction checklist item covering appraisal system awareness.",
            "Signed induction acknowledgement including appraisal awareness.",
            "Appraisal schedule showing all active staff on cycle.",
        ],
    },
    {
        "oe_code": "HRM.4.b",
        "requirement": "Performance is evaluated based on pre-determined criteria.",
        "steps": "Section 3; 5.2 Pre-determined evaluation criteria; Section 4 item 2",
        "responsible": "HR In-Charge / Personnel Officer (form template); department heads (apply criteria)",
        "records": [
            "Appraisal form template with pre-determined criteria linked to job descriptions.",
            "Annual criteria review record when job descriptions are updated.",
            "Sample completed appraisals showing criteria applied before the review meeting.",
        ],
    },
    {
        "oe_code": "HRM.4.c",
        "requirement": "The appraisal system is used as a tool for further development.",
        "steps": "Section 3; 5.3 Appraisal for further development; Section 4 item 3",
        "responsible": "Department heads (development plans); HR In-Charge / Personnel Officer (track actions)",
        "records": [
            "Completed appraisals with documented development plans.",
            "Training or mentoring records linked to appraisal outcomes (HRM.2).",
            "Next-cycle appraisal showing progress on development plan.",
        ],
    },
    {
        "oe_code": "HRM.4.d",
        "requirement": "Performance appraisal is carried out at defined intervals and is documented.",
        "steps": "Section 3; 5.4 Defined intervals and documentation; Section 4 items 4 and 5",
        "responsible": "Department heads (conduct and sign); HR In-Charge / Personnel Officer (schedule and filing)",
        "records": [
            "Appraisal schedule with defined intervals (annual and probationary).",
            "Signed appraisal forms filed in personnel files within two weeks.",
            "Monthly overdue-appraisal tracking report.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HRM.4 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: HRM.4.a–d PDF index 130. HRM.4.a is asterisked. HRM.4.a/b/d Commitment; HRM.4.b Commitment; HRM.4.c Excellence.

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only. HR roles only. ROM.2.d boundary stated for head-of-organisation review."""


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
        "subtitle": "Performance appraisal, criteria and development in day-to-day practice.",
        "doc_no": D("HRM/POL/04"),
    }
    emit_pre_v2(
        draft,
        "hrm4_v2_draft.json",
        "HRM.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
