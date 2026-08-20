# -*- coding: utf-8 -*-
"""IMS.4 v2 — confidentiality, integrity and security of records, data and information.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 139.
HAS stop-work: do not disclose privileged health information without patient
authorisation or a documented lawful basis (IMS.4.d).
Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only plus a light data-protection forward-note.
Does not cite DPDP Act 2023 as a requirement of this standard.
"""
from __future__ import annotations

import sys

from ims_v2_disclaimer import make_ims_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "IMS.4"
CHAPTER = "IMS"
OE_CODES = [
    "IMS.4.a", "IMS.4.b", "IMS.4.c", "IMS.4.d", "IMS.4.e",
]
POLICY_TITLE = "Confidentiality, Integrity and Security of Records, Data and Information"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "IMS v2 template: PRE v2 shape, plain English, IMS roles, five steps, stop-work for unauthorised disclosure.",
    },
]

STATEMENT_OF_INTENT = (
    "Confidentiality, integrity and security of records, data and information are "
    "maintained. Privileged health information is disclosed only as authorised by the "
    "patient and/or as required by law. Requests for access are addressed consistently."
)

PURPOSE = f"""This policy describes how {HOSPITAL} maintains the confidentiality, integrity and security of records, data and information; discloses privileged health information only as authorised by the patient and/or as required by law; and addresses requests for access to information in the medical records by patients, physicians and other public agencies consistently.

The chapter intent is that confidentiality of protected health information is paramount and is safeguarded across all information processing, storing and disseminating platforms.

IMS.4 owns patient medical records and general organisational information. HRM.6 owns confidentiality of staff personal files. PRE.2 owns the patient's right of access to records; this policy owns how access requests are processed.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every staff member at {HOSPITAL} who processes, stores or disseminates records, data or information — treating doctors, nurses, the {D('Medical Records Officer')}, the {D('IT / information-systems in-charge')}, the Medical Superintendent and the Quality Coordinator.

It covers the five elements IMS.4.a–e. It does not cover medical-record contents (IMS.2), continuity items (IMS.3), retention and destruction (IMS.5), or medical-record review (IMS.6).

Boundaries with other policies of {HOSPITAL}:

- HRM.6 owns confidentiality of staff personal files. This policy owns patient medical records and general information (not staff HR files).
- PRE.2 owns the patient's right of access to records. This policy owns the consistent process for access requests by patients, physicians and public agencies (IMS.4.e).
- IMS.1.d owns contribution to external databases in accordance with law and regulations. A contribution that includes privileged health information also meets this policy's disclosure gate (IMS.4.d).
- IMS.3.f owns care-provider access for care. This policy owns that such access is confidential, integral and secure."""

POLICY_STATEMENT = f"""{HOSPITAL} maintains the confidentiality, integrity and security of records, data and information.

Privileged health information is disclosed as authorised by the patient and/or as required by law. Requests for access to information in the medical records by patients, physicians and other public agencies are addressed consistently.

{HOSPITAL} does not release a patient's confidential record without the patient's authorisation or a documented lawful basis."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Disclosing privileged health information without the patient's authorisation or a documented requirement of law.
2. Sharing electronic-health-record (EHR) passwords or leaving a logged-in session unattended.
3. Altering a record so that the original entry cannot be reconstructed (integrity failure).
4. Leaving paper records unattended in a public or uncontrolled area.
5. Handling an access request from a patient, physician or public agency by an ad-hoc method instead of the consistent process.

Staff who cannot confirm authorisation or a lawful basis do not release the record. They invoke stop-work (section 6) and report to the {D('Medical Records Officer')} or the {D('Medical Superintendent')} the same shift."""

PROCEDURE_STEPS = [
f"""5.1 Confidentiality of records, data and information

{HOSPITAL} maintains the confidentiality of records, data and information.

Privileged health information — the medical record and any data that identifies a patient and their care — is available only to staff who need it for care, for authorised review, or for a disclosure that meets step 5.4. Casual discussion of a patient's condition in corridors, lifts or public areas is prohibited.

Paper records are stored in the records room or a locked department cupboard when not in use. Electronic records are role-restricted. Visitors, vendors and unauthorised staff are not left alone with records.

IMS.4.a is asterisked: confidentiality is a documented method (need-to-know, storage, role restriction), not a poster.

HRM.6 remains the home of staff-personal-file confidentiality.""",

f"""5.2 Integrity of records, data and information

{HOSPITAL} maintains the integrity of records, data and information.

Integrity means the record remains complete and unaltered except by an authenticated correction. Paper corrections follow IMS.2.d (single line, named, signed, dated and timed). Electronic corrections leave an amendment trail showing the original, the change, who changed it and when.

Backups of electronic records are checked {D('monthly')} for restorability. Paper records are protected from loss, mixing and unauthorised removal by the issue/return log.

IMS.4.b is asterisked: a missing amendment trail or an unrestorable backup is an integrity failure.""",

f"""5.3 Security of records, data and information

{HOSPITAL} maintains the security of records, data and information.

Physical security: the records room is locked when unattended; keys or access cards are held by named persons; after-hours access is logged. Electronic security: unique user identities, passwords that are not shared, role-based access, automatic session timeout of {D('fifteen minutes')}, and malware protection on machines that hold health information.

The {D('IT / information-systems in-charge')} holds the access-control list and reviews it {D('quarterly')} when staff join, leave or change role. Guidance the PDF cites (EHR Standards for India 2016; ISO 27001 / ISO 27799) is used as guidance for security controls, not as a copied statute.

IMS.4.c is asterisked: security is implemented, not only described.""",

f"""5.4 Disclosure as authorised by the patient and/or as required by law

{HOSPITAL} discloses privileged health information as authorised by the patient and/or as required by law.

A disclosure happens only when:

- the patient (or a person legally authorised to act for the patient) has given documented authorisation for that disclosure; or
- a written legal or regulatory requirement to disclose is recorded (for example a court order or a statutory return). The PDF states this as "as required by law" — this step stays at that general level and does not import a named data-protection Act as a checklist.

Every disclosure is logged: what was disclosed, to whom, the authorisation or lawful basis, date, and who released it. Stop-work (section 6) applies when neither authorisation nor a documented lawful basis exists.

IMS.1.d contributions to external databases that include privileged health information are logged here as well.""",

f"""5.5 Access requests addressed consistently

Requests for access to information in the medical records by patients, physicians and other public agencies are addressed consistently.

The {D('Medical Records Officer')} receives every request on the {D('medical-record access request form')}. The same steps apply whoever asks:

1. Identify the requester and the record.
2. Decide the pathway: patient (or authorised representative) — PRE.2 right of access, processed here; treating physician involved in care — IMS.3.f; other physician or public agency — step 5.4 authorisation or lawful basis.
3. Record the decision (grant, grant in part, or refuse with reason) within {D('seven working days')}.
4. Release only copies, never the original, unless a lawful process requires the original and a copy is retained.

IMS.4.e is asterisked: an ad-hoc release to a known doctor or a visiting official, bypassing the form, fails the OE.""",
]

STOP_WORK = f"""Do not go ahead with a disclosure or release if you are about to do any of the following:

1. Release or disclose a patient's privileged health information without the patient's (or legally authorised representative's) documented authorisation and without a documented lawful basis.
2. Hand over an original medical record to a requester when a copy would suffice, unless a recorded lawful process requires the original.
3. Send privileged health information by an uncontrolled channel (unencrypted personal messaging, an unnamed USB drive, an unattended fax) when a controlled channel exists.

When you invoke stop-work:

1. Do not release the record or the data.
2. Make the information safe (return paper to the locked store; close the electronic session).
3. Report to the {D('Medical Records Officer')} or the {D('Medical Superintendent')} the same shift.

No approval is needed to invoke stop-work. Confidentiality of protected health information overrides convenience."""

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for confidentiality, integrity and security of records, data and information.
- Decides disputed access requests.

Medical Records Officer (or the person carrying that role)
- Operates the records room, issue/return log and access-request process.
- Logs every disclosure with authorisation or lawful basis.

IT / information-systems in-charge
- Holds the access-control list, backups and electronic security controls.
- Reviews user access when staff join, leave or change role.

Treating doctors and nurses
- Access records only for care or authorised review.
- Do not disclose privileged health information in public or uncontrolled settings.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks stop-work invocations and disclosure-log completeness."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Issue/return log and after-hours records-room access log.
- Sample of EHR users: unique identity, no shared passwords, role matches current post.
- Backup restorability check.
- Disclosure log: every sampled disclosure has authorisation or a documented lawful basis.
- Access-request forms processed by the same steps for patients, physicians and public agencies.
- Stop-work invocations and their outcomes.

Root-cause analysis is required when a disclosure without authorisation or lawful basis is found, or when a shared login is in use.

This policy is reviewed {D('annually')}, and sooner when electronic systems or access pathways change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff who handle records, data or information are trained on this policy at induction and {D('once a year')} after that. Training covers confidentiality, integrity, security, the disclosure gate and stop-work.

Staff acknowledgement

I have read this Confidentiality, Integrity and Security of Records policy of {HOSPITAL}. I understand that I must not disclose privileged health information without patient authorisation or a documented lawful basis, and that I may invoke stop-work.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The Medical Records Officer holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("IMS/POL/04"),
    version=VERSION,
    prepared_by=D("Medical Records Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Information Management System chapter, standard IMS.4.
- Electronic Health Record (EHR) Standards for India, 2016 — guidance cited by the chapter.
- Ayushman Bharat Digital Mission (ABDM) Health Data Management Policy — guidance cited by the chapter.
- ISO/IEC 27001 and ISO 27799:2016 — guidance cited by the chapter.
- Internal documents of {HOSPITAL}: records-room access rules; EHR access-control list; disclosure log; medical-record access request form."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Medical Records Officer and the Quality Coordinator.

Copies issued to: all departments; IT / information-systems in-charge; nursing administration; records office.

The current version is available to all staff at the {D('records-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """ABDM — Ayushman Bharat Digital Mission
CAPA — corrective and preventive action
EHR — electronic health record
IMS — Information Management System (NABH SHCO chapter 10)
IT — information technology
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_ims_disclaimer()

OE_MAPPING = [
    {
        "oe_code": "IMS.4.a",
        "requirement": "The organisation maintains the confidentiality of records, data and information.",
        "steps": "Statement of intent; Section 3; 5.1 Confidentiality of records, data and information; Section 4 items 1, 4; Section 6 (stop-work)",
        "responsible": "All staff (need-to-know); Medical Records Officer (storage); IT in-charge (role restriction)",
        "records": [
            "Written need-to-know and records-handling rules.",
            "Locked storage for paper records; role-restricted electronic access.",
            "Quarterly audit sample of storage practice.",
            "Stop-work invocation records where a disclosure was halted.",
        ],
    },
    {
        "oe_code": "IMS.4.b",
        "requirement": "The organisation maintains the integrity of records, data and information.",
        "steps": "Section 3; 5.2 Integrity of records, data and information; Section 4 item 3",
        "responsible": "Record-writers (authenticated corrections); IT in-charge (backups)",
        "records": [
            "Sample corrections showing the original remains reconstructable.",
            "Electronic amendment-trail samples.",
            "Monthly backup restorability check.",
            "Paper issue/return log.",
        ],
    },
    {
        "oe_code": "IMS.4.c",
        "requirement": "The organisation maintains the security of records, data and information.",
        "steps": "Section 3; 5.3 Security of records, data and information; Section 4 items 2, 4",
        "responsible": "IT / information-systems in-charge (electronic controls); Medical Records Officer (physical controls)",
        "records": [
            "Records-room lock and after-hours access log.",
            "EHR access-control list reviewed when staff join, leave or change role.",
            "Evidence of unique user identities and session timeout.",
            "Quarterly access-control review.",
        ],
    },
    {
        "oe_code": "IMS.4.d",
        "requirement": "The organisation discloses privileged health information as authorised by the patient and/or as required by law.",
        "steps": "Section 3; 5.4 Disclosure as authorised by the patient and/or as required by law; Section 4 item 1; Section 6 (stop-work)",
        "responsible": "Medical Records Officer (log disclosure); Medical Superintendent (lawful-basis decisions)",
        "records": [
            "Disclosure log with what, whom, authorisation or lawful basis, date and releaser.",
            "Patient authorisation forms or recorded lawful-basis documents.",
            "Stop-work records for halted releases.",
        ],
    },
    {
        "oe_code": "IMS.4.e",
        "requirement": "Requests for access to information in the medical records by patients, physicians and other public agencies are addressed consistently.",
        "steps": "Section 3; 5.5 Access requests addressed consistently; Section 4 item 5",
        "responsible": "Medical Records Officer (receive and process); Medical Superintendent (disputed decisions)",
        "records": [
            "Completed medical-record access request forms for patients, physicians and public agencies.",
            "Decision recorded (grant, grant in part, or refuse) within the defined time.",
            "Evidence that the same steps were used regardless of requester.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """IMS.4 v2 template test (2026-08-20). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: IMS.4.a–e PDF index 139. IMS.4.a, IMS.4.b, IMS.4.c and IMS.4.e are asterisked (Tier 1). IMS.4.d is not asterisked (Tier 2). IMS.4.a/b/c are Core.

SHAPE: Five What-we-do subsections (5.1–5.5). Stop-work YES — do not disclose privileged health information without patient authorisation or a documented lawful basis. Disclaimer accreditation-only plus data-protection forward-note. DPDP Act 2023 not cited. IMS.4.d kept at PDF's "as required by law" general level.

BOUNDARY: HRM.6 owns staff personal files; PRE.2 owns the right of access; IMS.4 owns the records disclosure and access-request process."""


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
        "subtitle": "Confidentiality, integrity, security, disclosure gate and consistent access requests.",
        "doc_no": D("IMS/POL/04"),
        "stop_work": STOP_WORK,
        "acknowledgement_note": "The Medical Records Officer holds signed acknowledgements.",
    }
    emit_pre_v2(
        draft,
        "ims4_v2_draft.json",
        "IMS.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
