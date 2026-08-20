# -*- coding: utf-8 -*-
"""IMS.6 v2 — regular review of medical records.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 140.
No stop-work. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only plus a light data-protection forward-note.
"""
from __future__ import annotations

import sys

from ims_v2_disclaimer import make_ims_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "IMS.6"
CHAPTER = "IMS"
OE_CODES = [
    "IMS.6.a", "IMS.6.b", "IMS.6.c", "IMS.6.d", "IMS.6.e",
]
POLICY_TITLE = "Regular Review of Medical Records"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "IMS v2 template: PRE v2 shape, plain English, IMS roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation regularly reviews medical records — a representative sample of "
    "active and discharged patients, by identified reviewers, against identified "
    "parameters — and takes corrective and preventive action on deficiencies."
)

PURPOSE = f"""This policy describes how {HOSPITAL} reviews medical records periodically; uses a representative sample of both active and discharged patients based on statistical principles; has identified individuals conduct the review; reviews against identified parameters; and undertakes appropriate corrective and preventive action (CAPA) on deficiencies pointed out in the review.

IMS.6 owns the medical-record review itself. PSQ owns the wider quality programme (PSQ.1 committees, PSQ.3 clinical audit). Record-review findings may feed PSQ; they do not replace clinical audit.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the medical-record review committee (or the identified reviewers), the {D('Medical Records Officer')}, treating doctors, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the five elements IMS.6.a–e. It does not cover record structure and entry rules (IMS.2), continuity items (IMS.3), confidentiality (IMS.4), or retention (IMS.5).

Boundaries with other policies of {HOSPITAL}:

- PSQ.1 owns the quality improvement programme and its committees. PSQ.3 owns clinical audit. This policy owns medical-record review as a records-completeness and records-quality exercise. Findings may be referred to PSQ; the review method stays here.
- IMS.2 and IMS.3 supply the parameters (unique identifier, authentication, abbreviations, continuity items). This policy owns that those parameters are applied to a sample on a schedule.
- PRE.6 owns patient complaints. A complaint that reveals a record deficiency may trigger a targeted review; it does not replace the periodic sample."""

POLICY_STATEMENT = f"""{HOSPITAL} reviews medical records periodically. The review uses a representative sample of both active and discharged patients, based on statistical principles. Identified individuals conduct the review against identified parameters. Appropriate corrective and preventive measures are undertaken on the deficiencies pointed out in the review.

{HOSPITAL} does not treat a one-off look at a few files before an assessment as a review programme, and does not leave deficiencies without CAPA."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Going more than the defined review interval without a documented medical-record review.
2. Sampling only discharged patients, or only active patients, or only "good" files.
3. Allowing unidentified persons to conduct the review.
4. Reviewing without a written parameter list.
5. Recording deficiencies without corrective and preventive action and follow-up.

Staff who find that a scheduled review was skipped report it to the {D('Quality Coordinator')} or the {D('Medical Superintendent')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Periodic review of medical records

Medical records are reviewed periodically.

The review is conducted {D('monthly')}. The {D('Quality Coordinator')} holds the review calendar. A missed month is recorded as a non-conformity and is made up in the following period — it is not skipped.

"Periodically" means a planned interval, not an assessment-eve exercise. IMS.6.a is the requirement that the review happens on that interval.""",

f"""5.2 Representative sample of active and discharged patients

The review uses a representative sample of both active and discharged patients, based on statistical principles.

Each review cycle draws:

- active (currently admitted or currently under care) records; and
- discharged (including deaths and transfers-out) records.

The sample is drawn from the records register using {D('systematic sampling from the unique-identifier list, or another documented method that does not let the reviewer pick favourite files')}. The sample size is {D('at least ten records per month, or all records if fewer than ten were opened in the period')}, with both active and discharged represented.

A sample of only complete-looking files, or of one department only, is not representative.""",

f"""5.3 Review conducted by identified individuals

The review is conducted by identified individuals.

The Medical Superintendent names the reviewers in writing. Reviewers are {D('the Quality Coordinator, the Medical Records Officer, and at least one treating doctor who did not write the sampled record')}. Names, designations and the period of appointment are recorded.

A person does not review a record they wrote. The medical-record review committee (or the named reviewer group) meets {D('monthly')} to confirm the sample, the findings and the CAPA.

Identified means named — not "the quality team" as an unnamed group.""",

f"""5.4 Review based on identified parameters

The review of records is based on identified parameters.

The parameter list is approved by the Medical Superintendent and held by the Quality Coordinator. It includes at least:

- unique identifier present (IMS.2.a);
- contents complete, up-to-date and chronological (IMS.2.b);
- author identifiable; entry named, signed, dated and timed (IMS.2.c–d);
- authorised abbreviations only (IMS.2.e);
- continuity items: admission reason, diagnosis, plan, assessments, investigations, procedures, care provided (IMS.3.a–b);
- discharge-summary copy or, in death, cause-of-death certificate copy (IMS.3.d–e);
- transfer details where applicable (IMS.3.c).

Each sampled record is scored against the list. Parameters are not invented on the day of review.""",

f"""5.5 Corrective and preventive action on deficiencies

Appropriate corrective and preventive measures are undertaken on the deficiencies pointed out in the review.

Every deficiency is logged: record identifier, parameter failed, who will act, due date, and closure. Immediate correction (complete a missing signature, file a missing copy) is done by the treating team. Preventive action (re-brief a department, change a form, add a prompt in the electronic health record (EHR)) is decided by the review committee.

The Quality Coordinator tracks CAPA to closure. Recurring deficiencies of the same parameter in {D('two consecutive months')} trigger root-cause analysis and a report to the Medical Superintendent.

Aggregate findings (deficiency rate by parameter) are reported to the PSQ quality programme {D('quarterly')} as input — they do not replace PSQ.3 clinical audit.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Names the reviewers and approves the parameter list.
- Receives reports of recurring deficiencies.

Medical-record review committee (identified reviewers)
- Draws the sample, scores records against parameters, and decides CAPA.

Medical Records Officer (or the person carrying that role)
- Produces the records register for sampling.
- Supports retrieval of active and discharged records for review.

Quality Coordinator
- Holds the review calendar, parameter list and CAPA tracker.
- Reports aggregate findings to the PSQ programme.
- Audits this policy {D('quarterly')} (see section 7).

Treating doctors
- Complete immediate corrections on records they own.
- Do not review their own sampled records."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Review calendar: no skipped interval.
- Sample composition: active and discharged both present; method documented.
- Reviewers named and current; no self-review.
- Parameter list used as written.
- CAPA log: deficiencies closed or escalated.

Root-cause analysis is required when a scheduled review is skipped, or when the same parameter fails for two consecutive months without CAPA.

This policy is reviewed {D('annually')}, and sooner when IMS.2 or IMS.3 parameters change."""

TRAINING_ACKNOWLEDGEMENT = f"""Named reviewers, the Medical Records Officer, treating doctors and the Quality Coordinator are trained on this policy at appointment to the review role and {D('once a year')} after that. Training covers sampling, the parameter list, self-review prohibition and CAPA.

Staff acknowledgement

I have read this Regular Review of Medical Records policy of {HOSPITAL}. I understand the sampling rule, the identified-reviewer rule, the parameter list and that deficiencies require CAPA.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The Quality Coordinator holds signed acknowledgements with the Medical Records Officer.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("IMS/POL/06"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Information Management System chapter, standard IMS.6.
- Internal documents of {HOSPITAL}: medical-record review calendar; named-reviewer list; parameter list; sample sheets; CAPA log.
- Cross-referenced policies: IMS.2 and IMS.3 (parameters); PSQ.1 and PSQ.3 (quality programme and clinical audit — not duplicated here)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator and the Medical Records Officer.

Copies issued to: named reviewers; department heads; records office.

The current version is available to all staff at the {D('records-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
EHR — electronic health record
IMS — Information Management System (NABH SHCO chapter 10)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality (NABH SHCO chapter)
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_ims_disclaimer()

OE_MAPPING = [
    {
        "oe_code": "IMS.6.a",
        "requirement": "The medical records are reviewed periodically.",
        "steps": "Statement of intent; Section 3; 5.1 Periodic review of medical records; Section 4 item 1",
        "responsible": "Quality Coordinator (calendar); medical-record review committee (conduct)",
        "records": [
            "Review calendar with the defined interval.",
            "Minutes or review sheets for each scheduled cycle.",
            "Record of any missed cycle and the make-up review.",
        ],
    },
    {
        "oe_code": "IMS.6.b",
        "requirement": "The review uses a representative sample of both active and discharged patients, based on statistical principles.",
        "steps": "Section 3; 5.2 Representative sample of active and discharged patients; Section 4 item 2",
        "responsible": "Medical Records Officer (records register); identified reviewers (draw sample)",
        "records": [
            "Documented sampling method.",
            "Each cycle's sample list showing active and discharged records.",
            "Evidence the reviewer did not hand-pick files.",
        ],
    },
    {
        "oe_code": "IMS.6.c",
        "requirement": "The review is conducted by identified individuals.",
        "steps": "Section 3; 5.3 Review conducted by identified individuals; Section 4 item 3",
        "responsible": "Medical Superintendent (name reviewers); named reviewers (conduct)",
        "records": [
            "Written appointment of named reviewers with designation and period.",
            "Attendance of named reviewers at each review cycle.",
            "Evidence that a writer did not review their own record.",
        ],
    },
    {
        "oe_code": "IMS.6.d",
        "requirement": "The review of records is based on identified parameters.",
        "steps": "Section 3; 5.4 Review based on identified parameters; Section 4 item 4",
        "responsible": "Medical Superintendent (approve list); Quality Coordinator (hold list); reviewers (score)",
        "records": [
            "Approved parameter list covering IMS.2 and IMS.3 items.",
            "Scored sheets for each sampled record against that list.",
            "Evidence parameters were not invented on the day of review.",
        ],
    },
    {
        "oe_code": "IMS.6.e",
        "requirement": "Appropriate corrective and preventive measures are undertaken on the deficiencies pointed out in the review.",
        "steps": "Section 3; 5.5 Corrective and preventive action on deficiencies; Section 4 item 5",
        "responsible": "Review committee (decide CAPA); Quality Coordinator (track to closure); treating doctors (immediate correction)",
        "records": [
            "CAPA log with deficiency, owner, due date and closure.",
            "Root-cause analysis when the same parameter fails two consecutive months.",
            "Quarterly aggregate report to the PSQ programme.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """IMS.6 v2 template test (2026-08-20). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: IMS.6.a–e PDF index 140. No asterisked OEs — whole standard is Tier 2. IMS.6.a is Core.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only plus data-protection forward-note.

BOUNDARY: IMS.6 owns medical-record review; PSQ.1/PSQ.3 own the wider quality programme and clinical audit. Parameters drawn from IMS.2 and IMS.3; methods not duplicated."""


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
        "template_test": "ims_v2_adoptable_shape",
        "subtitle": "Periodic medical-record review, sampling, parameters and CAPA.",
        "doc_no": D("IMS/POL/06"),
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the Medical Records Officer.",
    }
    emit_pre_v2(
        draft,
        "ims6_v2_draft.json",
        "IMS.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
