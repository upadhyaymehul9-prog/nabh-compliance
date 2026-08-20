# -*- coding: utf-8 -*-
"""IMS.2 v2 — complete and accurate medical record.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 138.
No stop-work. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only plus a light data-protection forward-note.
"""
from __future__ import annotations

import sys

from ims_v2_disclaimer import make_ims_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "IMS.2"
CHAPTER = "IMS"
OE_CODES = [
    "IMS.2.a", "IMS.2.b", "IMS.2.c", "IMS.2.d", "IMS.2.e",
]
POLICY_TITLE = "Complete and Accurate Medical Record"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "IMS v2 template: PRE v2 shape, plain English, IMS roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Every patient cared for by the organisation has a complete and accurate medical "
    "record — uniquely identified, chronological, made only by authorised staff, "
    "named, signed, dated and timed, and using only authorised abbreviations."
)

PURPOSE = f"""This policy describes how {HOSPITAL} assigns a unique identifier to every medical record; identifies and documents the contents so the record is a complete, up-to-date and chronological account of patient care; restricts entries to authorised staff whose identity can be established; requires every entry to be named, signed, dated and timed; and permits only authorised abbreviations.

IMS.2 owns the medical-record system: structure, who may write, and how an entry is authenticated. Care chapters own the clinical content of those entries. IMS.3 owns continuity items (admission reason, assessments, transfer, discharge-summary copy, cause-of-death copy, access). AAC.2 owns generation of the unique identification number at registration.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors, nurses and other authorised record-writers, the {D('Medical Records Officer')}, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the five elements IMS.2.a–e. It does not cover continuity-of-care contents (IMS.3), confidentiality and disclosure (IMS.4), retention (IMS.5), or medical-record review (IMS.6).

Boundaries with other policies of {HOSPITAL}:

- AAC.2.b generates the unique identification number at the end of registration. This policy assigns that unique identifier to the medical record so every record is the same number as the registration identifier.
- Care chapters (AAC, COP, MOM, HIC) own what is clinically written. This policy owns that the record is complete, chronological and authenticated.
- IMS.3 owns specific continuity items (discharge-summary copy, cause-of-death copy, transfer details). This policy owns the general content list and entry rules.
- HRM.6 owns staff personal files. This policy owns the patient medical record."""

POLICY_STATEMENT = f"""Every patient cared for by {HOSPITAL} has a complete and accurate medical record.

A unique identifier is assigned to the medical record. Contents are identified and documented and provide a complete, up-to-date and chronological account of patient care. Authorised staff make the entry; the author of the entry can be identified. Every entry is named, signed, dated and timed. The medical record has only authorised abbreviations.

{HOSPITAL} does not keep an unidentified record, an unsigned or undated entry, or an abbreviation that is not on the authorised list."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Opening or filing a medical record without the unique identifier generated at registration (AAC.2.b).
2. An unauthorised person making an entry in a medical record.
3. An entry that is not named, signed, dated and timed.
4. Using an abbreviation that is not on the authorised-abbreviations list.
5. Leaving the record without a complete, up-to-date and chronological account of the care given.

Staff who find an unauthorised, unsigned, undated or unidentified entry report it the same shift to the {D('Medical Records Officer')} or the {D('treating doctor')}."""

PROCEDURE_STEPS = [
f"""5.1 Unique identifier assigned to the medical record

The unique identifier is assigned to the medical record.

The identifier is the unique identification number generated at the end of registration under AAC.2.b. The {D('Medical Records Officer')} confirms that the same number appears on the record cover (paper) or the patient header (electronic health record (EHR)), on every continuation sheet, and on every form filed in that record.

A record without the unique identifier is not filed. Duplicate numbers are investigated the same working day. Temporary or "unknown" identifiers used in an unidentified-patient emergency are replaced with the registration number as soon as identity is established, with the replacement recorded.""",

f"""5.2 Contents identified, documented and chronological

The contents of the medical record are identified, documented and provide a complete, up-to-date and chronological account of patient care.

{HOSPITAL} maintains a written contents list for the medical record. The list names the sections the hospital uses — {D('face sheet, consent forms, initial assessment, progress notes, medication record, investigation reports, operative notes, nursing notes, and discharge or death documents')}. Forms are filed in that order, or the EHR equivalent is structured to the same list.

Entries are chronological. Late entries are marked as late, timed at the time of writing, and cross-referenced to the event they describe. The record is updated during the episode, not assembled only at discharge.

IMS.2.b is asterisked: a contents list that is not followed, or a record that cannot be read in time order, fails the OE. IMS.3 adds specific continuity items on top of this structure.""",

f"""5.3 Authorised staff make entries; the author can be identified

Authorised staff make the entry in the medical record. The author of the entry can be identified.

The {D('Medical Superintendent')} holds a list of staff categories authorised to write in the medical record — {D('treating doctors, nurses, the pharmacist for medication-reconciliation entries, and named allied-health professionals for their own notes')}. A person not on that list does not write in the record.

Each author is identifiable: printed name and designation with a signature (paper), or a unique user identity that is not shared (EHR). Shared logins are prohibited. Students and trainees write only under a named supervisor who countersigns.""",

f"""5.4 Named, signed, dated and timed entries

Every entry in the medical record is named, signed, dated and timed.

The writer prints or types their name, signs (or authenticates electronically), and records the date and time of the entry. Time is recorded to the minute using the {D('24-hour clock')}.

A correction is made by a single line through the error, the word "error", the correct text, and the writer's name, signature, date and time. Correction fluid, obliteration and deletion of an electronic entry without an amendment trail are prohibited.

A verbal order is written by the receiving nurse, named, signed, dated and timed, and countersigned by the ordering doctor within {D('24 hours')}. MOM.4 owns the medication-order format; this step owns the authentication of the record entry.""",

f"""5.5 Authorised abbreviations only

The medical record has only authorised abbreviations.

The {D('Medical Records Officer')} holds the authorised-abbreviations list, approved by the Medical Superintendent. The list is available at every nursing station and in the EHR. Abbreviations not on the list are written out in full.

Dangerous abbreviations (for example those that can be read as a different dose or drug) are not authorised. The list is reviewed {D('annually')} or when a near-miss related to an abbreviation is reported under PSQ.5.

IMS.6 reviews a sample of records against this list.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Approves the authorised-writer list and the authorised-abbreviations list.
- Accountable for the medical-record system.

Medical Records Officer (or the person carrying that role)
- Assigns the unique identifier to the record and checks filing order.
- Holds the contents list and the authorised-abbreviations list.

Treating doctors and nurses
- Make named, signed, dated and timed entries for the care they give.
- Do not use unauthorised abbreviations.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Feeds abbreviation and authentication findings to IMS.6 review."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Sample of records: unique identifier present on cover/header and continuation sheets.
- Sample of entries: author identifiable; named, signed, dated and timed.
- Unauthorised abbreviations counted against the authorised list.
- Contents list followed; chronology intact including late-entry marking.

Root-cause analysis is required when an unauthorised person is found to have written in a record, or when a sampled record has no unique identifier.

This policy is reviewed {D('annually')}, and sooner when the EHR or the forms set changes."""

TRAINING_ACKNOWLEDGEMENT = f"""Treating doctors, nurses, the Medical Records Officer and other authorised writers are trained on this policy at induction and {D('once a year')} after that. Training covers the unique identifier, who may write, authentication of entries, and the authorised-abbreviations list.

Staff acknowledgement

I have read this Complete and Accurate Medical Record policy of {HOSPITAL}. I understand that only authorised staff write in the record, that every entry is named, signed, dated and timed, and that only authorised abbreviations are used.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The Medical Records Officer holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("IMS/POL/02"),
    version=VERSION,
    prepared_by=D("Medical Records Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Information Management System chapter, standard IMS.2.
- Electronic Health Record (EHR) Standards for India, 2016 — guidance cited by the chapter.
- Internal documents of {HOSPITAL}: medical-record contents list; authorised-writer list; authorised-abbreviations list; unique-identifier assignment check."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Medical Records Officer and the Quality Coordinator.

Copies issued to: all clinical departments; nursing stations; records office.

The current version is available to all staff at the {D('records-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
EHR — electronic health record
IMS — Information Management System (NABH SHCO chapter 10)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_ims_disclaimer()

OE_MAPPING = [
    {
        "oe_code": "IMS.2.a",
        "requirement": "The unique identifier is assigned to the medical record.",
        "steps": "Statement of intent; Section 3; 5.1 Unique identifier assigned to the medical record; Section 4 item 1",
        "responsible": "Medical Records Officer (assign and check); registration (source number from AAC.2.b)",
        "records": [
            "Medical record showing the unique identification number on cover/header and continuation sheets.",
            "Same-day investigation record for any duplicate number.",
            "Quarterly audit sample of identifier presence.",
        ],
    },
    {
        "oe_code": "IMS.2.b",
        "requirement": "The contents of the medical record are identified, documented and provide a complete, up-to-date and chronological account of patient care.",
        "steps": "Section 3; 5.2 Contents identified, documented and chronological; Section 4 item 5",
        "responsible": "Medical Records Officer (contents list); treating doctors and nurses (keep the record current)",
        "records": [
            "Written medical-record contents list.",
            "Sample records filed or structured in that order, chronological, with late entries marked.",
            "Quarterly audit of completeness against the contents list.",
        ],
    },
    {
        "oe_code": "IMS.2.c",
        "requirement": "Authorised staff make the entry in the medical record; the author of the entry can be identified.",
        "steps": "Section 3; 5.3 Authorised staff make entries; Section 4 item 2",
        "responsible": "Medical Superintendent (authorised-writer list); each writer (identifiable entry)",
        "records": [
            "Approved list of staff categories authorised to write in the medical record.",
            "Sample entries with identifiable author (name/designation or unique user identity).",
            "Evidence that shared logins are not in use.",
        ],
    },
    {
        "oe_code": "IMS.2.d",
        "requirement": "Entry in the medical record is named, signed, dated and timed.",
        "steps": "Section 3; 5.4 Named, signed, dated and timed entries; Section 4 item 3",
        "responsible": "Treating doctors and nurses (authenticate every entry)",
        "records": [
            "Sample entries showing name, signature, date and time.",
            "Correction samples showing single-line strike-through and re-authentication.",
            "Verbal-order countersignature records within the defined time.",
        ],
    },
    {
        "oe_code": "IMS.2.e",
        "requirement": "The medical record has only authorised abbreviations.",
        "steps": "Section 3; 5.5 Authorised abbreviations only; Section 4 item 4",
        "responsible": "Medical Records Officer (hold list); Medical Superintendent (approve list)",
        "records": [
            "Approved authorised-abbreviations list available at nursing stations and in the EHR.",
            "Annual review of the list.",
            "IMS.6 sample findings on unauthorised abbreviations.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """IMS.2 v2 template test (2026-08-20). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: IMS.2.a–e PDF index 138. IMS.2.b is asterisked (Tier 1). IMS.2.a/c/d/e are not asterisked (Tier 2). IMS.2.a and IMS.2.b are Core. Source grammar "provides a complete" cleaned to "provide a complete".

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only plus data-protection forward-note.

BOUNDARY: AAC.2.b generates the unique identification number; IMS.2.a assigns it to the medical record."""


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
        "subtitle": "Unique identifier, contents, authorised writers and authenticated entries.",
        "doc_no": D("IMS/POL/02"),
        "acknowledgement_note": "The Medical Records Officer holds signed acknowledgements.",
    }
    emit_pre_v2(
        draft,
        "ims2_v2_draft.json",
        "IMS.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
