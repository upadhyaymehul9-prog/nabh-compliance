# -*- coding: utf-8 -*-
"""IMS.1 v2 — information needs of stakeholders; data captured and analysed.

Shape follows PRE v2 (section list and order only). Wording from NABH SHCO
3rd Edition PDF (August 2022, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed page 132 / PDF index 138. Chapter intent: printed page 131 / PDF index 137.

No stop-work. Five OEs in five What-we-do subsections.
Disclaimer P2 is accreditation-only plus a light data-protection forward-note.
"""
from __future__ import annotations

import sys

from ims_v2_disclaimer import make_ims_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "IMS.1"
CHAPTER = "IMS"
OE_CODES = [
    "IMS.1.a", "IMS.1.b", "IMS.1.c", "IMS.1.d", "IMS.1.e",
]
POLICY_TITLE = "Information Needs of Stakeholders — Capture and Analysis of Data"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "IMS v2 template: PRE v2 shape, plain English, IMS roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The right information is available to the right person at the right time — "
    "stakeholder information needs are identified, captured and disseminated, and "
    "data is stored, retrieved and analysed against those needs."
)

PURPOSE = f"""This policy describes how {HOSPITAL} identifies, captures and disseminates the information needs of patients, visitors, staff, management, external agencies and the community; aligns information-management and technology acquisitions with those needs; stores and retrieves data accordingly; contributes to external databases in accordance with law and regulations; and standardises data collection so that data can be analysed.

The chapter intent is that the right information is available to the right person at the right time, in an authenticated, secure and accurate manner.

IMS.1 owns the information-needs system and the data-capture/analysis method. IMS.2 owns the medical record itself. IMS.4 owns confidentiality, integrity and security. IMS.5 owns document control and retention.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the {D('Medical Records Officer')} (or the person carrying that role), the {D('IT / information-systems in-charge')}, the Medical Superintendent, the Quality Coordinator, and staff who collect or use organisational information at {HOSPITAL}.

It covers the five elements IMS.1.a–e. It does not cover medical-record contents (IMS.2), continuity entries (IMS.3), confidentiality/security mechanics (IMS.4), retention and destruction (IMS.5), or medical-record review (IMS.6).

Boundaries with other policies of {HOSPITAL}:

- IMS.2 owns the complete and accurate medical record. This policy owns organisation-wide information needs and data analysis, not the clinical-record form.
- PSQ.2 owns key indicators. This policy owns that data collection is standardised so those indicators (and other needs) can be met.
- IMS.4 owns confidentiality when information is disseminated. This policy owns who needs what information, not the disclosure gate.
- External-database contribution is done in accordance with law and regulations. This policy does not import a named Act as a checklist."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies, captures and disseminates the information needs of patients, visitors, staff, management, external agencies and the community.

Information-management and technology acquisitions and the maintenance plan are in consonance with those identified needs. Data is stored and retrieved according to those needs.

{HOSPITAL} contributes to external databases in accordance with law and regulations. Processes for data collection are standardised, and data is analysed to meet the information needs.

{HOSPITAL} does not buy or keep an information system that does not match identified needs, and does not collect data that nobody uses."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating without a current, documented map of information needs covering patients, visitors, staff, management, external agencies and the community.
2. Acquiring or maintaining an information-management or technology system that is not matched to the identified information needs.
3. Storing data that cannot be retrieved when a documented information need requires it.
4. Contributing patient or organisational data to an external database without a recorded legal or regulatory basis.
5. Collecting the same data by different methods in different departments so that it cannot be analysed.

Staff who identify one of these gaps report it to the {D('Medical Records Officer')} or the {D('Quality Coordinator')} within the same working week."""

PROCEDURE_STEPS = [
f"""5.1 Identify, capture and disseminate information needs

{HOSPITAL} identifies, captures and disseminates the information needs of patients, visitors, staff, management, external agencies and the community.

The {D('Medical Records Officer')} holds an information-needs register. The register lists, for each stakeholder group:

- what information they need (for example waiting times and visiting hours for patients and visitors; duty rosters and protocols for staff; occupancy and quality indicators for management; statutory returns for external agencies; public-health notices for the community);
- the source of that information;
- who disseminates it, by what channel (notice board, counselling, intranet, statutory portal), and how often.

The register is reviewed {D('annually')} and when a new service, a new statutory return or a significant change in patient mix is introduced. Obsolete information is withdrawn so that staff, patients and visitors are not confused by out-of-date notices (chapter intent).

IMS.1.a is asterisked: the register is a documented method, not a remembered list.""",

f"""5.2 Information-management and technology acquisitions and maintenance

Information management and technology acquisitions and the maintenance plan are in consonance with the identified information needs.

Before {HOSPITAL} buys, upgrades or renews a hospital information system, electronic health record (EHR) module, laboratory or imaging interface, or related hardware, the {D('IT / information-systems in-charge')} checks the proposal against the information-needs register. A purchase that does not serve a documented need is not approved.

A maintenance plan covers backups, user support, version control and planned downtime. The plan is held by the {D('IT / information-systems in-charge')} and reviewed {D('annually')} with the Medical Records Officer.

Guidance the PDF cites for this chapter (EHR Standards for India 2016; Ayushman Bharat Digital Mission (ABDM) Health Data Management Policy; ISO 27001 / ISO 27799) is used as guidance for acquisitions, not as a copied statute.""",

f"""5.3 Store and retrieve data according to information needs

{HOSPITAL} stores and retrieves data according to its information needs.

Each entry on the information-needs register names where the data lives (paper file, EHR module, indicator spreadsheet, statutory portal) and how an authorised person retrieves it. Retrieval is tested {D('quarterly')} for a sample of needs — including at least one clinical retrieval and one management retrieval.

Storage media, whether paper or electronic, are labelled and indexed so that a named record can be found without searching the whole store. IMS.5 owns retention periods and document control; this step owns that stored data can be retrieved to meet a current need.

IMS.1.c is asterisked: storage without retrievability fails the OE.""",

f"""5.4 Contribute to external databases in accordance with law and regulations

{HOSPITAL} contributes to external databases in accordance with the law and regulations.

The {D('Medical Records Officer')} keeps a register of external databases the hospital contributes to. Each entry states: the database, the data sent, the frequency, the legal or regulatory basis, and who submits it. Contribution without a recorded basis does not occur.

The PDF frames contribution as "in accordance with the law and regulations." This step stays at that general level. It does not import a named data-protection Act as a checklist. Examples of databases a small hospital may be required or authorised to contribute to include {D('notifiable-disease reporting and haemovigilance returns where those programmes apply')}. The hospital verifies which returns apply to it.

IMS.4 owns the disclosure gate for privileged health information. A contribution that includes patient-identifiable data also meets IMS.4.d (patient authorisation and/or as required by law).""",

f"""5.5 Standardised data collection and analysis

Processes for data collection are standardised and data is analysed to meet the information needs.

The {D('Quality Coordinator')} and the {D('Medical Records Officer')} issue a data-definition sheet for each data item used to meet an information need: definition, source, collector, frequency, and the analysis it feeds. Departments do not invent parallel definitions.

Data is analysed at the interval the information-needs register sets — {D('monthly')} for operational needs and {D('quarterly')} for management and quality needs. Analysis output is disseminated to the stakeholder named on the register.

PSQ.2 owns the key-indicator set. This step owns that collection is standardised so analysis is possible. Indicator choice stays with PSQ.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Approves the information-needs register and technology-acquisition decisions that depend on it.
- Accountable for lawful contribution to external databases.

Medical Records Officer (or the person carrying that role)
- Holds the information-needs register and the external-database register.
- Tests storage and retrieval with the IT in-charge.

IT / information-systems in-charge
- Matches acquisitions and the maintenance plan to identified needs.
- Operates backups and retrieval for electronic stores.

Quality Coordinator
- Holds data-definition sheets and oversees analysis against information needs.
- Audits this policy {D('quarterly')} (see section 7)."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit checks records and practice.

What is monitored each quarter:

- Information-needs register is current and covers all six stakeholder groups.
- A sample technology acquisition or maintenance item is matched to a documented need.
- Retrieval test passed for the sampled needs.
- External-database register entries have a recorded legal or regulatory basis.
- Data-definition sheets exist for analysed items; parallel definitions are absent.

Root-cause analysis is required when a documented information need cannot be met from stored data, or when a contribution to an external database has no recorded basis.

This policy is reviewed {D('annually')}, and sooner when a new service or a new statutory return is introduced."""

TRAINING_ACKNOWLEDGEMENT = f"""The Medical Records Officer, the IT / information-systems in-charge, department heads and the Quality Coordinator are briefed on this policy at appointment and {D('once a year')} after that. Briefing covers the information-needs register, retrieval tests and the external-database register.

Staff acknowledgement

I have read this Information Needs of Stakeholders policy of {HOSPITAL}. I understand the information-needs register, standardised data collection and the rule that external-database contribution requires a recorded legal or regulatory basis.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per person. The Medical Records Officer holds signed acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("IMS/POL/01"),
    version=VERSION,
    prepared_by=D("Medical Records Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Information Management System chapter, standard IMS.1.
- Electronic Health Record (EHR) Standards for India, 2016 (Ministry of Health and Family Welfare) — guidance cited by the chapter, not a copied statute.
- Ayushman Bharat Digital Mission (ABDM) Health Data Management Policy (National Health Authority) — guidance cited by the chapter.
- ISO/IEC 27001 and ISO 27799:2016 — guidance cited by the chapter for information-security management.
- Internal documents of {HOSPITAL}: information-needs register; technology acquisition and maintenance plan; external-database contribution register; data-definition sheets."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Medical Records Officer and the Quality Coordinator.

Copies issued to: IT / information-systems in-charge; department heads; quality office.

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
        "oe_code": "IMS.1.a",
        "requirement": "The organisation identifies, captures and disseminates the information needs of the patients, visitors, staff, management, external agencies and community.",
        "steps": "Statement of intent; Section 3; 5.1 Identify, capture and disseminate information needs; Section 4 item 1",
        "responsible": "Medical Records Officer (hold register); Medical Superintendent (approve)",
        "records": [
            "Information-needs register covering patients, visitors, staff, management, external agencies and community.",
            "Annual review record and evidence that obsolete notices were withdrawn.",
            "Sample of disseminated information matched to a register entry (channel and frequency).",
            "Quarterly audit sample of stakeholder coverage.",
        ],
    },
    {
        "oe_code": "IMS.1.b",
        "requirement": "Information management and technology acquisitions and maintenance plan are in consonance with the identified information needs.",
        "steps": "Section 3; 5.2 Information-management and technology acquisitions and maintenance; Section 4 item 2",
        "responsible": "IT / information-systems in-charge (match acquisitions); Medical Superintendent (approve purchases)",
        "records": [
            "Written check of each acquisition against the information-needs register.",
            "Current technology maintenance plan (backups, support, version control, downtime).",
            "Annual review of the maintenance plan with the Medical Records Officer.",
        ],
    },
    {
        "oe_code": "IMS.1.c",
        "requirement": "The organisation stores and retrieves data according to its information needs.",
        "steps": "Section 3; 5.3 Store and retrieve data according to information needs; Section 4 item 3",
        "responsible": "Medical Records Officer (index stores); IT / information-systems in-charge (electronic retrieval)",
        "records": [
            "Storage location and retrieval method named on each information-needs register entry.",
            "Quarterly retrieval-test log covering at least one clinical and one management retrieval.",
            "Index or labelling scheme for paper and electronic stores.",
        ],
    },
    {
        "oe_code": "IMS.1.d",
        "requirement": "The organisation contributes to external databases in accordance with the law and regulations.",
        "steps": "Section 3; 5.4 Contribute to external databases; Section 4 item 4",
        "responsible": "Medical Records Officer (hold register); Medical Superintendent (accountable for basis)",
        "records": [
            "External-database contribution register with database, data, frequency, basis and submitter.",
            "Submission receipts or logs for each contribution.",
            "Evidence that patient-identifiable contributions also meet IMS.4.d.",
        ],
    },
    {
        "oe_code": "IMS.1.e",
        "requirement": "Processes for data collection are standardised and data is analysed to meet the information needs.",
        "steps": "Section 3; 5.5 Standardised data collection and analysis; Section 4 item 5",
        "responsible": "Quality Coordinator (data-definition sheets and analysis); Medical Records Officer (collection method)",
        "records": [
            "Data-definition sheet for each analysed data item.",
            "Analysis outputs at the interval set on the information-needs register.",
            "Evidence that department-level parallel definitions were not in use.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """IMS.1 v2 template test (2026-08-20). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Chapter intent PDF index 137. IMS.1.a–e PDF index 138. IMS.1.a and IMS.1.c are asterisked (Tier 1). IMS.1.b, IMS.1.d, IMS.1.e are not asterisked (Tier 2). IMS.1.a is Core.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only plus data-protection forward-note (hospital duty to check; DPDP Act 2023 not cited). IMS roles only.

FLAG: IMS.1.d "in accordance with the law and regulations" kept at that general level — no named Act imported as a checklist."""


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
        "subtitle": "Information needs, data capture, storage, retrieval and analysis.",
        "doc_no": D("IMS/POL/01"),
        "acknowledgement_note": "The Medical Records Officer holds signed acknowledgements.",
    }
    emit_pre_v2(
        draft,
        "ims1_v2_draft.json",
        "IMS.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
