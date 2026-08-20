# -*- coding: utf-8 -*-
"""IMS.5 v2 — availability of current documents/records and retention.

Shape follows PRE v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 140.
No stop-work. Four OEs in four What-we-do subsections.
Disclaimer P2 is accreditation-only plus a light data-protection forward-note.
Retention period is an editable hospital default — the PDF gives no number.
"""
from __future__ import annotations

import sys

from ims_v2_disclaimer import make_ims_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "IMS.5"
CHAPTER = "IMS"
OE_CODES = [
    "IMS.5.a", "IMS.5.b", "IMS.5.c", "IMS.5.d",
]
POLICY_TITLE = "Availability, Document Control and Retention of Records, Data and Information"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "IMS v2 template: PRE v2 shape, plain English, IMS roles, four steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Current and relevant documents, records, data and information are available; "
    "they are retained according to the organisation's requirements; retention "
    "protects confidentiality and security; and destruction follows the laid-down policy."
)

PURPOSE = f"""This policy describes how {HOSPITAL} keeps an effective process for document control; retains patients' clinical records, data and information according to its requirements; ensures the retention process provides the expected confidentiality and security; and destroys medical records, data and information only in accordance with the laid-down policy.

The chapter intent includes periodic review, revision and withdrawal of obsolete information so that staff, patients and visitors are not confused.

The PDF gives no retention period. The period is set by {HOSPITAL} after legal advice, in line with applicable National Medical Commission (NMC) and State rules. This policy does not assert a number of years.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the {D('Medical Records Officer')}, the {D('IT / information-systems in-charge')}, department heads who issue controlled documents, the Medical Superintendent and the Quality Coordinator at {HOSPITAL}.

It covers the four elements IMS.5.a–d. It does not cover medical-record contents (IMS.2), continuity items (IMS.3), the disclosure gate (IMS.4), or medical-record review (IMS.6).

Boundaries with other policies of {HOSPITAL}:

- IMS.4 owns confidentiality and security while records are in active use and when they are disclosed. This policy owns confidentiality and security during retention and destruction (IMS.5.c–d).
- HRM.6 owns retention of staff personal files. This policy owns patient clinical records and general controlled documents.
- Each chapter's policy is a controlled document under this process. This policy does not rewrite those policies' content."""

POLICY_STATEMENT = f"""{HOSPITAL} has an effective process for document control. Current and relevant documents, records, data and information are available to those who need them.

Patients' clinical records, data and information are retained according to the organisation's requirements. The retention process provides the expected confidentiality and security. Destruction of medical records, data and information is in accordance with the laid-down policy.

{HOSPITAL} does not leave obsolete documents in use, and does not destroy a medical record outside the laid-down policy."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Issuing or using a controlled document that is not on the current-document register.
2. Leaving an obsolete document in circulation after a new version is issued.
3. Destroying a patient's clinical record, data or information before the retention period set in this policy, or without a destruction record.
4. Storing retained records without the confidentiality and security expected under IMS.4.
5. Inventing a retention period at the point of destruction instead of using the laid-down policy.

Staff who find an obsolete document in use, or a proposed destruction that is not on the policy, report it to the {D('Medical Records Officer')} or the {D('Quality Coordinator')} the same working day."""

PROCEDURE_STEPS = [
f"""5.1 Effective process for document control

{HOSPITAL} has an effective process for document control.

The {D('Quality Coordinator')} holds the current-document register. Every controlled document (policy, procedure, form, protocol) has: document number, title, version, date of issue, owner, and review due date. Only the current version is available at the point of use.

When a new version is issued, old copies are taken out of use the same day (see Distribution in each policy). Obsolete master copies are marked "obsolete" and stored or destroyed per the register — they are not left on a notice board or shared drive as if current.

IMS.5.a is asterisked: a folder of policies without a register, or a ward copy that does not match the register, fails the OE.

Chapter intent: obsolete information is withdrawn so that staff, patients and visitors are not confused.""",

f"""5.2 Retention of patients' clinical records, data and information

{HOSPITAL} retains patients' clinical records, data and information according to its requirements.

The PDF requires retention "according to its requirements" and does not state a number of years. {HOSPITAL} sets the retention period after legal advice, in line with applicable NMC and State rules. The period used is {D('the period the hospital sets after legal advice, in line with applicable NMC and State rules')}. Write the decided period into this default before the document is signed. Do not treat a remembered number as the policy.

The {D('Medical Records Officer')} holds a retention schedule listing: record type (in-patient record, out-patient record, diagnostic report, electronic backup), the retention period, and where the record is stored during retention (active shelf, archive, electronic archive).

IMS.5.b is asterisked: retention without a written schedule, or a schedule that asserts a period the hospital has not decided, fails the OE.""",

f"""5.3 Confidentiality and security during retention

The retention process provides expected confidentiality and security.

Archived paper records are kept in a locked archive with an issue/return log, the same confidentiality standard as active records (IMS.4.a and IMS.4.c). Electronic archives are access-restricted, backed up, and protected from unauthorised alteration (IMS.4.b).

Staff who do not need an archived record for care, authorised review or a disclosure under IMS.4.d do not retrieve it. Retrieval of an archived record is logged.

This step does not duplicate IMS.4's disclosure gate. It extends confidentiality and security to the retained store.""",

f"""5.4 Destruction in accordance with the laid-down policy

The destruction of medical records, data and information is in accordance with the laid-down policy.

Destruction happens only when:

- the retention period on the schedule has ended; and
- the {D('Medical Superintendent')} has authorised that batch; and
- a destruction record is completed (record identifiers or batch description, method, date, two persons present).

Method: paper is shredded or otherwise made unreadable; electronic media are wiped or physically destroyed so that data cannot be reconstructed. Destruction is not dumping intact records in general waste.

A record that is the subject of a pending legal process, complaint (PRE.6) or incident review (PSQ.5) is not destroyed until that process is closed, even if the retention period has ended.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Approves the retention schedule and authorises each destruction batch.
- Accountable for document control.

Quality Coordinator
- Holds the current-document register.
- Withdraws obsolete versions.
- Audits this policy {D('quarterly')} (see section 7).

Medical Records Officer (or the person carrying that role)
- Holds the retention schedule and the archive.
- Prepares destruction batches and destruction records.

IT / information-systems in-charge
- Operates electronic archive, backups and electronic destruction.

Department heads
- Keep only current controlled documents at the point of use."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Current-document register matches what is at the point of use (sample of wards and offices).
- No obsolete version found in circulation.
- Retention schedule present; no destruction before the stated period.
- Archive confidentiality and security (lock, log, electronic access restriction).
- Destruction records complete for any batch destroyed in the period.

Root-cause analysis is required when an obsolete document is found in use, or when a record is destroyed outside the laid-down policy.

This policy is reviewed {D('annually')}, and sooner when NMC or State retention rules that apply to the hospital change. The hospital verifies those rules; this document does not assert a period."""

TRAINING_ACKNOWLEDGEMENT = f"""The Medical Records Officer, the Quality Coordinator, department heads and the IT / information-systems in-charge are trained on this policy at appointment and {D('once a year')} after that. Training covers the current-document register, the retention schedule, archive security and destruction rules.

Staff acknowledgement

I have read this Availability, Document Control and Retention policy of {HOSPITAL}. I understand that only current controlled documents are used, that retention follows the written schedule, and that destruction requires authorisation and a record.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The Medical Records Officer holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("IMS/POL/05"),
    version=VERSION,
    prepared_by=D("Medical Records Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Information Management System chapter, standard IMS.5.
- Applicable NMC and State rules on clinical-record retention — verified by {HOSPITAL}; not restated as a number in this template.
- Electronic Health Record (EHR) Standards for India, 2016 — guidance cited by the chapter.
- Internal documents of {HOSPITAL}: current-document register; retention schedule; archive issue/return log; destruction records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Medical Records Officer and the Quality Coordinator.

Copies issued to: all department heads; IT / information-systems in-charge; records office.

The current version is available to all staff at the {D('records-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
EHR — electronic health record
IMS — Information Management System (NABH SHCO chapter 10)
IT — information technology
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NMC — National Medical Commission
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_ims_disclaimer()

OE_MAPPING = [
    {
        "oe_code": "IMS.5.a",
        "requirement": "The organisation has an effective process for document control.",
        "steps": "Statement of intent; Section 3; 5.1 Effective process for document control; Section 4 items 1, 2",
        "responsible": "Quality Coordinator (current-document register); department heads (point-of-use copies)",
        "records": [
            "Current-document register with number, title, version, issue date, owner and review due date.",
            "Evidence that obsolete copies were withdrawn when a new version was issued.",
            "Quarterly point-of-use sample matching the register.",
        ],
    },
    {
        "oe_code": "IMS.5.b",
        "requirement": "The organisation retains patients' clinical records, data and information, according to its requirements.",
        "steps": "Section 3; 5.2 Retention of patients' clinical records; Section 4 items 3, 5",
        "responsible": "Medical Superintendent (set period after legal advice); Medical Records Officer (schedule and store)",
        "records": [
            "Written retention schedule with record type, period and storage location.",
            "Evidence the period was set after legal advice in line with applicable NMC and State rules — no invented number in this template.",
            "Archive inventory or electronic-archive index.",
        ],
    },
    {
        "oe_code": "IMS.5.c",
        "requirement": "The retention process provides expected confidentiality and security.",
        "steps": "Section 3; 5.3 Confidentiality and security during retention; Section 4 item 4",
        "responsible": "Medical Records Officer (paper archive); IT / information-systems in-charge (electronic archive)",
        "records": [
            "Locked archive with issue/return log.",
            "Electronic-archive access restriction and backup evidence.",
            "Logged retrieval of archived records.",
        ],
    },
    {
        "oe_code": "IMS.5.d",
        "requirement": "The destruction of medical records, data and information is in accordance with the laid-down policy.",
        "steps": "Section 3; 5.4 Destruction in accordance with the laid-down policy; Section 4 items 3, 5",
        "responsible": "Medical Superintendent (authorise batch); Medical Records Officer (carry out and record)",
        "records": [
            "Destruction records (batch, method, date, two persons present, authorisation).",
            "Hold list for records in a pending legal, complaint or incident process.",
            "Evidence that intact records were not placed in general waste.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """IMS.5 v2 template test (2026-08-20). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: IMS.5.a–d PDF index 140. IMS.5.a and IMS.5.b are asterisked (Tier 1). IMS.5.c and IMS.5.d are not asterisked (Tier 2). IMS.5.a and IMS.5.b are Core.

SHAPE: Four What-we-do subsections (5.1–5.4). No stop-work. Disclaimer accreditation-only plus data-protection forward-note.

RETENTION: PDF says "according to its requirements" / "laid-down policy" — no number. Editable guillemets default; hospital sets period after legal advice in line with NMC and State rules. No "5 years" or similar invented period.

BOUNDARY: HRM.6 owns staff personal files; IMS.4 owns active confidentiality; IMS.5 owns retention and destruction."""


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
        "subtitle": "Document control, retention schedule and authorised destruction.",
        "doc_no": D("IMS/POL/05"),
        "acknowledgement_note": "The Medical Records Officer holds signed acknowledgements.",
    }
    emit_pre_v2(
        draft,
        "ims5_v2_draft.json",
        "IMS.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
