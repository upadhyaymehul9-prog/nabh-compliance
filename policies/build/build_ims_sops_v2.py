# -*- coding: utf-8 -*-
"""Builds the 6 IMS (Information Management System) SOPs -- plus their
Records and manifest.json -- in the plain-body + audit-appendix format
used for FMS, ROM, AAC, HRM, COP, MOM, PRE, PSQ and HIC (2026-10-13).

This is the final chapter of the 10-chapter SHCO SOP/Record rebuild.

No SOP/Record pack existed for IMS before this script:
policies/build/sop_record_masters/IMS/ is created fresh here. The content
is drawn directly from the SHCO 3rd Edition IMS Master Policy pipeline
already built and approved for this hospital
(policies/drafts/ims{1..6}_v2_draft.json) -- 6 standards, 30 OEs across
IMS.1-IMS.6, already-concrete procedure detail (named registers, timed
entries, sampling method). Every bare cross-reference the draft's own
procedure_steps used as shorthand (e.g. "AAC.2.b", "PSQ.5", "IMS.4.a")
is removed from body prose here and, where it matters, moved to the
Appendix-only `boundary` field -- the same fix PSQ and HIC went through.

IMS.5's retention-period step deliberately asserts no number of years --
the source draft is explicit that this is set by the hospital after legal
advice (NMC/State rules vary), not a number NABH or this script invents.
That design is kept and explained in the body, not papered over.

External technical sources (EHR Standards for India 2016, ABDM Health
Data Management Policy, ISO/IEC 27001, ISO 27799:2016) were verified
live via WebSearch on 2026-10-13 before being written in here.

Writes:
  policies/build/sop_record_masters/IMS/SOP_IMS.N...docx   (6 files)
  policies/build/sop_record_masters/IMS/Records/IMS.N_Record_NN_*.docx
  policies/build/sop_record_masters/IMS/manifest.json
"""
from __future__ import annotations

import json
from pathlib import Path

from sop_record_common import (
    PlainItem,
    SOPSpecV2,
    RecordSpec,
    build_sop_v2,
    build_record,
)

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "IMS"
RECORDS_ROOT = OUT_ROOT / "Records"

NABH_IMS_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Information Management System chapter, standard {code}."
)
EHR_STANDARDS_INDIA_SRC = (
    "Ministry of Health and Family Welfare, Government of India. (2016). "
    "[Electronic Health Record (EHR) Standards for "
    "India](https://esanjeevani.mohfw.gov.in/assets/guidelines/ehr_guidlines.pdf). "
    "New Delhi: MoHFW -- guidance this hospital's record-structure and "
    "data-standardisation steps are built on, cited as guidance, not as a "
    "copied statute."
)
ABDM_HDM_POLICY_SRC = (
    "National Health Authority, Government of India. (2022). [Health Data "
    "Management "
    "Policy](https://abdm.gov.in:8081/uploads/health_management_policy_bac9429a79.pdf) "
    "(Ayushman Bharat Digital Mission). New Delhi: NHA -- guidance this "
    "hospital's confidentiality and disclosure steps are built on."
)
ISO_27001_SRC = (
    "International Organization for Standardization. (2022). [ISO/IEC "
    "27001:2022 -- Information security management "
    "systems](https://www.iso.org/standard/27001) -- Requirements. Geneva: "
    "ISO -- the internationally recognised framework this hospital's "
    "information-security controls (access control, role restriction) "
    "are built on."
)
ISO_27799_SRC = (
    "International Organization for Standardization. (2016). [ISO "
    "27799:2016 -- Health informatics -- Information security management "
    "in health using ISO/IEC 27002](https://www.iso.org/standard/62777.html). "
    "Geneva: ISO -- the health-sector-specific security guidance this "
    "hospital's records-security measures are built on."
)

SOPS: list[tuple[str, SOPSpecV2]] = []
RECORDS: list[tuple[str, int, str, RecordSpec]] = []


def _add(sop_code: str, idx: int, spec: RecordSpec, slug: str) -> None:
    RECORDS.append((sop_code, idx, slug, spec))

# ============================================================== IMS.1 ====
IMS1 = SOPSpecV2(
    sop_no="SOP-IMS.1",
    title="Information Needs of Stakeholders — Capture and Analysis of Data",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» finds out what "
        "information its patients, visitors, staff, management, "
        "external agencies and the community actually need, keeps a "
        "written record of those needs, buys and maintains information "
        "technology that actually serves them, stores and retrieves data "
        "accordingly, contributes to external databases only on a "
        "recorded legal basis, and standardises how data is collected so "
        "it can actually be analysed."
    ),
    purpose_trigger=(
        "A new lab interface is bought because a vendor made a good "
        "pitch, not because any department actually asked for it -- six "
        "months later it sits unused while the information need that "
        "prompted the original budget request is still unmet. This SOP "
        "is what makes sure spending on information systems follows a "
        "documented need, not a sales pitch."
    ),
    purpose_why=(
        "We do this because the point of all of this is simple: the "
        "right information has to reach the right person at the right "
        "time, accurately and securely -- and that only happens if this "
        "hospital actually knows, in writing, what each group of people "
        "needs to know."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies, captures and "
        "disseminates the information needs of patients, visitors, "
        "staff, management, external agencies and the community; aligns "
        "information-management and technology acquisitions with those "
        "needs; stores and retrieves data accordingly; contributes to "
        "external databases in accordance with law and regulations; and "
        "standardises data collection so that data can be analysed."
    ),
    scope_why=(
        "so every department that generates, holds or needs information "
        "-- not only the Medical Records Officer -- knows there is one "
        "documented method behind what gets communicated to whom, and "
        "that a new system is only bought because a real need already "
        "exists."
    ),
    scope_text=(
        "Applies to all departments at «Hospital Name» and to the "
        "Medical Records Officer, the IT or information-systems in-"
        "charge, the Quality Coordinator and management. It covers how "
        "information needs are identified and met, how technology is "
        "acquired against those needs, how data is stored, retrieved and "
        "standardised, and how external-database contribution is "
        "governed. It does not cover the medical record itself, "
        "confidentiality and security of records, or document control "
        "and retention -- each of those is set out in its own separate "
        "SOP in this chapter."
    ),
    responsibility_why=(
        "an information need that nobody is named to capture, and a "
        "technology purchase that nobody is named to check against a "
        "real need, both tend to happen by default rather than by "
        "decision."
    ),
    responsibilities=[
        ("Medical Records Officer", "Holds the information-needs register and the external-database contribution register; reviews both annually."),
        ("IT / Information-Systems In-Charge", "Checks technology proposals against the information-needs register before approval; holds the maintenance plan."),
        ("Quality Coordinator", "Issues data-definition sheets jointly with the Medical Records Officer; tracks data analysis against the register's schedule."),
        ("Management", "Approves technology acquisitions that serve a documented information need."),
    ],
    items=[
        PlainItem(
            heading="Keep a written register of what every stakeholder group actually needs to know",
            why=(
                "A hospital that never wrote down what patients, staff "
                "or the community actually need to know ends up guessing "
                "-- and guessing produces out-of-date notices nobody "
                "reads and real needs nobody ever meets."
            ),
            body=[
                "«Hospital Name» identifies, captures and disseminates "
                "the information needs of patients, visitors, staff, "
                "management, external agencies and the community.",
                "The «Medical Records Officer» holds an information-"
                "needs register. For each stakeholder group, the "
                "register names:",
                "1. What information they need -- for example, waiting "
                "times and visiting hours for patients and visitors; "
                "duty rosters and protocols for staff; occupancy and "
                "quality indicators for management; statutory returns "
                "for external agencies; public-health notices for the "
                "community.",
                "2. Where that information comes from.",
                "3. Who disseminates it, through which channel -- "
                "notice board, counselling, intranet, statutory portal "
                "-- and how often.",
                "The register is reviewed «annually», and whenever a "
                "new service, a new statutory return, or a significant "
                "change in patient mix is introduced. Out-of-date "
                "information is withdrawn, so staff, patients and "
                "visitors are never left reading a notice that no "
                "longer applies.",
            ],
            oe_code="IMS.1.a (ASTERISKED)",
        ),
        PlainItem(
            heading="Buy and maintain information technology only against a documented need",
            why=(
                "A system bought because it looked impressive in a demo, "
                "rather than because a real information need called for "
                "it, is money spent without actually solving anything."
            ),
            body=[
                "Information-management and technology acquisitions, "
                "and the maintenance plan behind them, are matched to "
                "the information needs this hospital has already "
                "identified.",
                "Before «Hospital Name» buys, upgrades or renews a "
                "hospital information system, an electronic health "
                "record module, a laboratory or imaging interface, or "
                "related hardware, the «IT / information-systems in-"
                "charge» checks the proposal against the information-"
                "needs register. A purchase that does not serve a "
                "documented need is not approved.",
                "A maintenance plan covers backups, user support, "
                "version control and planned downtime. The plan is held "
                "by the «IT / information-systems in-charge» and "
                "reviewed «annually» with the Medical Records Officer.",
            ],
            oe_code="IMS.1.b",
        ),
        PlainItem(
            heading="Store data so it can actually be found again when it is needed",
            why=(
                "Data that is stored but cannot be retrieved when "
                "someone actually needs it has failed at the one thing "
                "storage was for -- storing and retrieving are the same "
                "requirement, not two separate ones."
            ),
            body=[
                "«Hospital Name» stores and retrieves data according to "
                "its information needs.",
                "Each entry on the information-needs register names "
                "where that data actually lives -- a paper file, an EHR "
                "module, an indicator spreadsheet, a statutory portal -- "
                "and how an authorised person retrieves it. Retrieval "
                "is tested «quarterly» on a sample of needs, including "
                "at least one clinical retrieval and one management "
                "retrieval.",
                "Storage media, whether paper or electronic, are "
                "labelled and indexed so a named record can be found "
                "without searching the entire store. How long data is "
                "kept and how it is controlled as a document is covered "
                "separately, under this hospital's document-control and "
                "retention process -- this step is only about whether "
                "stored data can actually be retrieved for a current "
                "need.",
            ],
            oe_code="IMS.1.c (ASTERISKED)",
            boundary=[
                "Document control and retention periods are owned by IMS.5; this step owns that stored data remains retrievable for a current need, not how long it is kept.",
            ],
        ),
        PlainItem(
            heading="Contribute to external databases only on a recorded legal basis",
            why=(
                "Sending patient data out to an external database "
                "\"because it was asked for\" with no written check of "
                "the legal basis is exactly the kind of casual "
                "disclosure that turns into a real confidentiality "
                "breach."
            ),
            body=[
                "«Hospital Name» contributes to external databases in "
                "accordance with law and regulations.",
                "The «Medical Records Officer» keeps a register of "
                "every external database this hospital contributes to. "
                "Each entry states: the database, the data sent, the "
                "frequency, the legal or regulatory basis, and who "
                "submits it. A contribution is never made without a "
                "recorded basis.",
                "Examples of databases a small hospital may be required "
                "or authorised to contribute to include «notifiable-"
                "disease reporting and haemovigilance returns, where "
                "those programmes apply». This hospital checks which "
                "returns actually apply to it rather than assuming.",
                "A contribution that includes patient-identifiable data "
                "also has to meet this hospital's own authorisation-or-"
                "lawful-basis requirement for disclosing privileged "
                "health information.",
            ],
            oe_code="IMS.1.d",
            boundary=[
                "The general disclosure gate for privileged health information is owned by IMS.4.d; this step is specifically about registering and justifying contribution to an external database.",
            ],
        ),
        PlainItem(
            heading="Standardise how data is collected so it can actually be analysed",
            why=(
                "If three departments each invent their own definition "
                "of the same data point, the numbers cannot honestly be "
                "added together or compared -- standardising the "
                "definition is what makes analysis possible at all."
            ),
            body=[
                "Processes for data collection are standardised, and "
                "data is analysed to meet this hospital's information "
                "needs.",
                "The «Quality Coordinator» and the «Medical Records "
                "Officer» issue a data-definition sheet for every data "
                "item used to meet an information need: its definition, "
                "its source, who collects it, how often, and what "
                "analysis it feeds. Departments do not invent their own "
                "parallel definitions.",
                "Data is analysed at the interval set on the "
                "information-needs register -- «monthly» for "
                "operational needs and «quarterly» for management and "
                "quality needs. The analysis is then disseminated to "
                "the stakeholder named on that same register.",
            ],
            oe_code="IMS.1.e",
            boundary=[
                "Which key indicators the hospital actually tracks is owned by PSQ.2; this step owns that collection of any data item, indicator or otherwise, follows one standard definition rather than several competing ones.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the IMS.1 Records folder).",
    related_documents=[
        "Hospital's Complete and Accurate Medical Record SOP (IMS.2)",
        "Hospital's Confidentiality, Integrity and Security of Records SOP (IMS.4)",
        "Hospital's Availability, Document Control and Retention of Records SOP (IMS.5)",
        "Hospital's Key Indicators SOP (PSQ.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, alongside the information-needs "
        "register's own annual review, or sooner if a new service, a new "
        "statutory return, or a related policy named above in this "
        "chapter is introduced or revised."
    ),
    full_reference_list=[
        NABH_IMS_CITE.format(code="IMS.1"),
        EHR_STANDARDS_INDIA_SRC,
        ABDM_HDM_POLICY_SRC,
        ISO_27001_SRC,
        ISO_27799_SRC,
    ],
)

SOPS.append(("SOP_IMS.1.a_to_e_information_needs_stakeholders_capture_analysis_data.docx", IMS1))

# ---- IMS.1 Records -------------------------------------------------
_add("IMS.1", 1, RecordSpec(
    oe_code="IMS.1.a (ASTERISKED)",
    oe_requirement="The organisation identifies, captures and disseminates the information needs of patients, visitors, staff, management, external agencies and the community.",
    record_title="IMS.1 Record 01 — Information-needs register",
    what_is_this="This record is the proof each stakeholder group's information needs were actually written down -- what they need, where it comes from, who sends it and how -- not assumed to be common knowledge.",
    real_example="The register shows patients and visitors need visiting hours, sourced from the admissions office, disseminated via the notice board and reception counselling, reviewed annually.",
    why_nabh_asks="A hospital that never wrote down what patients, staff or the community actually need to know ends up guessing -- and guessing produces out-of-date notices nobody reads and real needs nobody ever meets.",
    how_to_fill=[
        ("Stakeholder Group", "Patients, staff, management, etc."),
        ("Information Need", "What they need to know."),
        ("Source", "Where it comes from."),
        ("Dissemination Channel / Frequency", "How and how often."),
        ("Last Review Date", "Annual review tracking."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.1")],
    column_headers=["Stakeholder Group", "Information Need", "Source", "Dissemination Channel / Frequency", "Last Review Date"],
    worked_example_row=["WORKED EXAMPLE — Patients/Visitors", "Visiting hours, waiting times", "Admissions office", "Notice board + reception counselling / ongoing", "10-Jan-2026"],
), "information_needs_register")

_add("IMS.1", 2, RecordSpec(
    oe_code="IMS.1.b",
    oe_requirement="Information management and technology acquisitions and the maintenance plan are in consonance with the identified information needs.",
    record_title="IMS.1 Record 02 — Technology acquisition needs-check record",
    what_is_this="This record is the proof a technology purchase was actually checked against a real, documented information need before approval -- not approved on a vendor's pitch alone.",
    real_example="A proposed laboratory interface upgrade is checked against the register's entry for faster result turnaround for clinicians, confirmed as a documented need, and approved.",
    why_nabh_asks="A system bought because it looked impressive in a demo, rather than because a real information need called for it, is money spent without actually solving anything.",
    how_to_fill=[
        ("Proposed Acquisition", "What is being bought/upgraded."),
        ("Matched Need (Register Reference)", "Which documented need it serves."),
        ("Approved (Y/N)", "Decision."),
        ("Approving Authority / Date", "Who and when."),
    ],
    verified_sources=[EHR_STANDARDS_INDIA_SRC, NABH_IMS_CITE.format(code="IMS.1")],
    column_headers=["Proposed Acquisition", "Matched Need (Register Reference)", "Approved (Y/N)", "Approving Authority / Date"],
    worked_example_row=["WORKED EXAMPLE — Laboratory interface upgrade", "Faster result turnaround for clinicians", "Y", "IT In-Charge — 05-Feb-2026"],
), "technology_acquisition_needs_check_record")

_add("IMS.1", 3, RecordSpec(
    oe_code="IMS.1.c (ASTERISKED)",
    oe_requirement="The organisation stores and retrieves data according to its information needs.",
    record_title="IMS.1 Record 03 — Quarterly data-retrieval test record",
    what_is_this="This record is the proof a sample of stored data was actually tested for retrievability every quarter -- not assumed retrievable because it was stored somewhere.",
    real_example="The Q1 retrieval test confirms a clinical record and a management indicator spreadsheet were both located within minutes of a simulated request.",
    why_nabh_asks="Data that is stored but cannot be retrieved when someone actually needs it has failed at the one thing storage was for -- storing and retrieving are the same requirement, not two separate ones.",
    how_to_fill=[
        ("Test Date", "When tested."),
        ("Data Item Tested (Clinical / Management)", "What was retrieved."),
        ("Retrieved Successfully (Y/N)", "Confirmed."),
        ("Time Taken / Issue Found", "How long, or what went wrong."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.1")],
    column_headers=["Test Date", "Data Item Tested (Clinical / Management)", "Retrieved Successfully (Y/N)", "Time Taken / Issue Found"],
    worked_example_row=["WORKED EXAMPLE — 15-Mar-2026", "Clinical record (sample patient file)", "Y", "4 minutes"],
), "quarterly_data_retrieval_test_record")

_add("IMS.1", 4, RecordSpec(
    oe_code="IMS.1.d",
    oe_requirement="The organisation contributes to external databases in accordance with the law and regulations.",
    record_title="IMS.1 Record 04 — External-database contribution register",
    what_is_this="This record is the proof every external database contribution actually has a recorded legal basis -- not a submission made because an outside party asked for it.",
    real_example="The register shows monthly notifiable-disease reporting to the district health office, submitted by the Medical Records Officer under the Epidemic Diseases Act reporting requirement.",
    why_nabh_asks="Sending patient data out to an external database \"because it was asked for\" with no written check of the legal basis is exactly the kind of casual disclosure that turns into a real confidentiality breach.",
    how_to_fill=[
        ("Database / Recipient", "Who receives it."),
        ("Data Sent / Frequency", "What and how often."),
        ("Legal / Regulatory Basis", "Why this is required or authorised."),
        ("Submitted By", "Who sends it."),
    ],
    verified_sources=[ABDM_HDM_POLICY_SRC, NABH_IMS_CITE.format(code="IMS.1")],
    column_headers=["Database / Recipient", "Data Sent / Frequency", "Legal / Regulatory Basis", "Submitted By"],
    worked_example_row=["WORKED EXAMPLE — District health office", "Notifiable-disease case counts / monthly", "Statutory notifiable-disease reporting requirement", "Medical Records Officer"],
), "external_database_contribution_register")

_add("IMS.1", 5, RecordSpec(
    oe_code="IMS.1.e",
    oe_requirement="Processes for data collection are standardised and data is analysed to meet the information needs.",
    record_title="IMS.1 Record 05 — Data-definition sheet and analysis-dissemination log",
    what_is_this="This record is the proof every data item has one standard definition that every department actually uses, and that analysis was actually sent to the stakeholder who needed it -- not a chart produced and left unseen.",
    real_example="The data-definition sheet for \"average length of stay\" fixes its exact formula and source; the Q1 analysis is disseminated to management per the register's quarterly schedule.",
    why_nabh_asks="If three departments each invent their own definition of the same data point, the numbers cannot honestly be added together or compared -- standardising the definition is what makes analysis possible at all.",
    how_to_fill=[
        ("Data Item", "What is defined."),
        ("Definition / Source / Collector", "Standard definition."),
        ("Analysis Frequency", "Monthly/quarterly."),
        ("Disseminated To / Date", "Who received the analysis and when."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.1")],
    column_headers=["Data Item", "Definition / Source / Collector", "Analysis Frequency", "Disseminated To / Date"],
    worked_example_row=["WORKED EXAMPLE — Average length of stay", "Total patient-days / discharges; source: EHR; collector: Medical Records Officer", "Quarterly", "Management — 10-Apr-2026"],
), "data_definition_sheet_analysis_dissemination_log")

# ============================================================== IMS.2 ====
IMS2 = SOPSpecV2(
    sop_no="SOP-IMS.2",
    title="Complete and Accurate Medical Record",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» assigns one unique "
        "identifier to every medical record, keeps the record's contents "
        "organised and in time order, restricts who may write in it, "
        "requires every entry to carry a name, signature, date and time, "
        "and permits only a written list of approved abbreviations."
    ),
    purpose_trigger=(
        "A chart has two different numbers on two different pages "
        "because a temporary identifier used during an emergency "
        "admission was never replaced -- and a lab result meant for one "
        "patient nearly gets filed under the other. This SOP exists so "
        "that one identifier, consistently applied, is what keeps every "
        "page of a record unmistakably tied to the right patient."
    ),
    purpose_why=(
        "We do this because a medical record is only useful if the next "
        "clinician who opens it can trust that every page belongs to "
        "this patient, every entry happened when it says it did, and "
        "every entry was written by someone who can actually be "
        "identified and asked about it."
    ),
    purpose_text=(
        "To define how «Hospital Name» assigns a unique identifier to "
        "every medical record; identifies and documents the contents so "
        "the record is a complete, up-to-date and chronological account "
        "of patient care; restricts entries to authorised staff whose "
        "identity can be established; requires every entry to be named, "
        "signed, dated and timed; and permits only authorised "
        "abbreviations."
    ),
    scope_why=(
        "so every person who writes in a medical record -- doctor, "
        "nurse, pharmacist, allied-health professional -- knows exactly "
        "what makes an entry acceptable, not just clinically correct."
    ),
    scope_text=(
        "Applies to every medical record at «Hospital Name» and to "
        "every staff member authorised to write in one: treating "
        "doctors, nurses, the pharmacist for medication-reconciliation "
        "entries, named allied-health professionals, the Medical "
        "Superintendent and the Medical Records Officer. It covers the "
        "medical record's structure, who may write in it, and how an "
        "entry is authenticated. It does not cover the clinical content "
        "of any entry -- that stays with the relevant care SOP -- or the "
        "continuity-of-care items such as transfer and discharge-summary "
        "copies, which are set out in their own separate SOP in this "
        "chapter."
    ),
    responsibility_why=(
        "a record that nobody is named to check for the unique "
        "identifier, the contents list, or an authorised writer quietly "
        "accumulates exactly the gaps that make it unreliable later."
    ),
    responsibilities=[
        ("Medical Records Officer", "Confirms the unique identifier is consistent across the record; maintains the contents list and authorised-abbreviations list; investigates duplicate numbers."),
        ("Medical Superintendent", "Holds the list of staff categories authorised to write in the medical record; approves the authorised-abbreviations list."),
        ("Treating Doctors / Nurses / Pharmacist / Allied-Health Professionals", "Write entries only within their authorised scope; name, sign, date and time every entry; countersign verbal orders within the defined window."),
        ("Students / Trainees", "Write only under a named supervisor who countersigns."),
    ],
    items=[
        PlainItem(
            heading="Give every medical record one unique identifier, and keep it consistent on every page",
            why=(
                "A record with two numbers on two different pages, or a "
                "temporary identifier from an emergency admission that "
                "was never corrected, is a record a future clinician can "
                "no longer fully trust belongs to one patient."
            ),
            body=[
                "A unique identifier is assigned to every medical "
                "record.",
                "The identifier is the unique identification number "
                "generated at the end of registration. The «Medical "
                "Records Officer» confirms that the same number appears "
                "on the record cover (paper) or the patient header "
                "(electronic health record), on every continuation "
                "sheet, and on every form filed in that record.",
                "A record without the unique identifier is not filed. "
                "A duplicate number is investigated the same working "
                "day it is noticed. A temporary or \"unknown\" "
                "identifier used for an unidentified patient in an "
                "emergency is replaced with the real registration "
                "number as soon as the patient's identity is "
                "established, and that replacement is recorded.",
            ],
            oe_code="IMS.2.a",
        ),
        PlainItem(
            heading="Keep the record's contents organised and in true time order",
            why=(
                "A record assembled only at discharge, or one where "
                "entries are not actually in the order they happened, "
                "cannot be read as a reliable account of what was "
                "actually done and when -- it becomes a reconstruction, "
                "not a record."
            ),
            body=[
                "The contents of the medical record are identified, "
                "documented and provide a complete, up-to-date and "
                "chronological account of patient care.",
                "«Hospital Name» keeps a written contents list for the "
                "medical record, naming the sections this hospital "
                "uses -- «face sheet, consent forms, initial assessment, "
                "progress notes, medication record, investigation "
                "reports, operative notes, nursing notes, and discharge "
                "or death documents». Forms are filed in that order, or "
                "the electronic health record is structured to the same "
                "list.",
                "Entries are chronological. A late entry is marked as "
                "late, timed at the actual time of writing, and cross-"
                "referenced to the event it describes. The record is "
                "updated as the episode happens, not assembled only at "
                "discharge.",
            ],
            oe_code="IMS.2.b (ASTERISKED)",
            boundary=[
                "The specific continuity-of-care items this structure must contain (admission reason, transfer details, discharge-summary copy, and so on) are owned by IMS.3; this step owns the structure and chronological discipline itself.",
            ],
        ),
        PlainItem(
            heading="Only let authorised staff write in the record, and make sure every author can be identified",
            why=(
                "A shared login or an unsupervised trainee's entry means "
                "nobody can say, with confidence, exactly who wrote what "
                "-- and that uncertainty undermines every entry in the "
                "record, not just the one in question."
            ),
            body=[
                "Authorised staff make the entry in the medical record, "
                "and the author of any entry can be identified.",
                "The «Medical Superintendent» holds a list of staff "
                "categories authorised to write in the medical record "
                "-- «treating doctors, nurses, the pharmacist for "
                "medication-reconciliation entries, and named allied-"
                "health professionals for their own notes». A person "
                "not on that list does not write in the record.",
                "Each author is identifiable: a printed name and "
                "designation with a signature on paper, or a unique "
                "user identity that is never shared, in the electronic "
                "health record. Shared logins are prohibited. A student "
                "or trainee writes only under a named supervisor who "
                "countersigns the entry.",
            ],
            oe_code="IMS.2.c",
        ),
        PlainItem(
            heading="Name, sign, date and time every entry -- and correct mistakes the right way",
            why=(
                "An unsigned, undated entry cannot be verified later -- "
                "and correction fluid or a deleted electronic entry with "
                "no trail destroys the very thing a medical record "
                "exists to preserve: an honest account of what actually "
                "happened."
            ),
            body=[
                "Every entry in the medical record is named, signed, "
                "dated and timed.",
                "The writer prints or types their name, signs (or "
                "authenticates electronically), and records the date "
                "and time of the entry, to the minute, using the «24-"
                "hour clock».",
                "A correction is made by a single line through the "
                "error, the word \"error\", the correct text, and the "
                "writer's name, signature, date and time. Correction "
                "fluid, obliteration, and deleting an electronic entry "
                "without an amendment trail are all prohibited.",
                "A verbal order is written by the receiving nurse, "
                "named, signed, dated and timed, and countersigned by "
                "the ordering doctor within «24 hours». The exact "
                "format a medication order has to follow is covered "
                "elsewhere; this step is only about authenticating the "
                "record entry itself.",
            ],
            oe_code="IMS.2.d",
            boundary=[
                "The medication-order format itself is owned by MOM.4; this step owns the authentication (name/signature/date/time) of the record entry that carries it.",
            ],
        ),
        PlainItem(
            heading="Use only approved abbreviations, and never a dangerous one",
            why=(
                "An abbreviation that can be misread as a different dose "
                "or a different drug does not save time -- it creates "
                "exactly the kind of ambiguity a medical record exists "
                "to remove."
            ),
            body=[
                "The medical record has only authorised abbreviations.",
                "The «Medical Records Officer» holds the authorised-"
                "abbreviations list, approved by the Medical "
                "Superintendent. The list is available at every nursing "
                "station and in the electronic health record. An "
                "abbreviation not on the list is written out in full.",
                "A dangerous abbreviation -- one that can be read as a "
                "different dose or a different drug -- is never "
                "authorised. The list is reviewed «annually», or "
                "immediately if a near-miss linked to an abbreviation is "
                "reported through this hospital's incident-reporting "
                "process.",
            ],
            oe_code="IMS.2.e",
            boundary=[
                "A sample of records is checked against this list as part of the periodic medical-record review owned by IMS.6.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the IMS.2 Records folder).",
    related_documents=[
        "Hospital's Medical Record Reflects Continuity of Care SOP (IMS.3)",
        "Hospital's Regular Review of Medical Records SOP (IMS.6)",
        "Hospital's registration / unique identification SOP (AAC.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a duplicate-"
        "identifier investigation, a shared-login discovery, or a near-"
        "miss linked to an unauthorised abbreviation is reported, or if "
        "a related policy named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_IMS_CITE.format(code="IMS.2"),
        EHR_STANDARDS_INDIA_SRC,
    ],
)

SOPS.append(("SOP_IMS.2.a_to_e_complete_accurate_medical_record.docx", IMS2))

# ---- IMS.2 Records -------------------------------------------------
_add("IMS.2", 1, RecordSpec(
    oe_code="IMS.2.a",
    oe_requirement="The unique identifier is assigned to the medical record.",
    record_title="IMS.2 Record 01 — Unique-identifier consistency and duplicate-investigation log",
    what_is_this="This record is the proof the same identifier actually appears on every page of a record, and that a duplicate number was actually investigated the same day -- not a number that was assigned once and never checked again.",
    real_example="A spot check confirms the identifier is consistent across all 14 pages of a sampled record; a duplicate number flagged in March is investigated and resolved the same working day.",
    why_nabh_asks="A record with two numbers on two different pages, or a temporary identifier from an emergency admission that was never corrected, is a record a future clinician can no longer fully trust belongs to one patient.",
    how_to_fill=[
        ("Check Date / Record Sampled", "When and which record."),
        ("Identifier Consistent Across Record (Y/N)", "Confirmed."),
        ("Duplicate Found (Y/N, Date)", "If applicable."),
        ("Resolution / Date", "How and when resolved."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.2")],
    column_headers=["Check Date / Record Sampled", "Identifier Consistent Across Record (Y/N)", "Duplicate Found (Y/N, Date)", "Resolution / Date"],
    worked_example_row=["WORKED EXAMPLE — 10-Mar-2026 / UID-00620", "Y", "Y — 12-Mar-2026", "Resolved same day — registration office corrected index"],
), "unique_identifier_consistency_duplicate_investigation_log")

_add("IMS.2", 2, RecordSpec(
    oe_code="IMS.2.b (ASTERISKED)",
    oe_requirement="The contents of the medical record are identified, documented and provide a complete, up-to-date and chronological account of patient care.",
    record_title="IMS.2 Record 02 — Medical-record contents list and chronology spot-check",
    what_is_this="This record is the proof the record's sections actually follow the written contents list, and entries actually sit in true time order -- not a record where a late entry was slipped in without being marked as late.",
    real_example="A spot check of a discharged patient's record confirms all nine listed sections are present and in order, with one late progress note correctly marked \"late entry\" and cross-referenced.",
    why_nabh_asks="A record assembled only at discharge, or one where entries are not actually in the order they happened, cannot be read as a reliable account of what was actually done and when -- it becomes a reconstruction, not a record.",
    how_to_fill=[
        ("Check Date / Record Sampled", "When and which record."),
        ("All Listed Sections Present (Y/N)", "Confirmed."),
        ("Chronological Order Confirmed (Y/N)", "Confirmed."),
        ("Late Entries Correctly Marked (Y/N)", "Confirmed."),
    ],
    verified_sources=[EHR_STANDARDS_INDIA_SRC, NABH_IMS_CITE.format(code="IMS.2")],
    column_headers=["Check Date / Record Sampled", "All Listed Sections Present (Y/N)", "Chronological Order Confirmed (Y/N)", "Late Entries Correctly Marked (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026 / UID-00633", "Y", "Y", "Y — 1 late entry, correctly marked"],
), "medical_record_contents_list_chronology_spot_check")

_add("IMS.2", 3, RecordSpec(
    oe_code="IMS.2.c",
    oe_requirement="Authorised staff makes the entry in the medical record. The author of the entry can be identified.",
    record_title="IMS.2 Record 03 — Authorised-writer list and shared-login check record",
    what_is_this="This record is the proof only staff on the authorised list actually wrote in the record, and that no shared login was used -- not an assumption that only the right people have access.",
    real_example="A quarterly access-log review confirms all EHR entries in the sample were made under individually identifiable logins, with no shared accounts found.",
    why_nabh_asks="A shared login or an unsupervised trainee's entry means nobody can say, with confidence, exactly who wrote what -- and that uncertainty undermines every entry in the record, not just the one in question.",
    how_to_fill=[
        ("Review Date / Period", "When and what period."),
        ("Entries Checked", "Sample size."),
        ("Shared Login Found (Y/N)", "Confirmed."),
        ("Trainee Entries Countersigned (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.2")],
    column_headers=["Review Date / Period", "Entries Checked", "Shared Login Found (Y/N)", "Trainee Entries Countersigned (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — Q1 2026", "20 entries sampled", "N", "Y — 2 trainee entries, both countersigned"],
), "authorised_writer_list_shared_login_check_record")

_add("IMS.2", 4, RecordSpec(
    oe_code="IMS.2.d",
    oe_requirement="Every entry in the medical record is named, signed, dated and timed.",
    record_title="IMS.2 Record 04 — Entry-authentication and correction-practice spot-check",
    what_is_this="This record is the proof entries actually carry a name, signature, date and time, and that any correction actually followed the single-line-through method -- not correction fluid or an untraceable deletion.",
    real_example="A spot check finds all sampled entries fully authenticated; one correction uses the single-line-through method with the writer's initials, date and time.",
    why_nabh_asks="An unsigned, undated entry cannot be verified later -- and correction fluid or a deleted electronic entry with no trail destroys the very thing a medical record exists to preserve: an honest account of what actually happened.",
    how_to_fill=[
        ("Check Date / Record Sampled", "When and which record."),
        ("Entries Fully Authenticated (Y/N)", "Confirmed."),
        ("Correction Found / Method Used", "If any, how it was done."),
        ("Verbal Order Countersigned Within 24h (Y/N, if applicable)", "Confirmed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.2")],
    column_headers=["Check Date / Record Sampled", "Entries Fully Authenticated (Y/N)", "Correction Found / Method Used", "Verbal Order Countersigned Within 24h (Y/N, if applicable)"],
    worked_example_row=["WORKED EXAMPLE — 14-Mar-2026 / UID-00633", "Y", "1 correction — single line through, initialled, dated, timed", "Y"],
), "entry_authentication_correction_practice_spot_check")

_add("IMS.2", 5, RecordSpec(
    oe_code="IMS.2.e",
    oe_requirement="The medical record has only authorised abbreviations.",
    record_title="IMS.2 Record 05 — Authorised-abbreviations list and near-miss review record",
    what_is_this="This record is the proof the abbreviations list is actually current, approved, and was actually reviewed after any abbreviation-linked near-miss -- not a list copied once and forgotten.",
    real_example="The abbreviations list, approved by the Medical Superintendent in January, excludes \"U\" for units after a near-miss report; the list is reviewed again the same month the near-miss was logged.",
    why_nabh_asks="An abbreviation that can be misread as a different dose or a different drug does not save time -- it creates exactly the kind of ambiguity a medical record exists to remove.",
    how_to_fill=[
        ("List Version / Approval Date", "Current version."),
        ("Dangerous Abbreviation Excluded (Example)", "What is deliberately not allowed."),
        ("Near-Miss Triggered Review (Y/N, Date)", "If applicable."),
        ("Next Scheduled Review", "Annual or triggered."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.2")],
    column_headers=["List Version / Approval Date", "Dangerous Abbreviation Excluded (Example)", "Near-Miss Triggered Review (Y/N, Date)", "Next Scheduled Review"],
    worked_example_row=["WORKED EXAMPLE — v3.0 / 10-Jan-2026", "\"U\" for units — excluded, write \"units\" in full", "Y — 18-Mar-2026 near-miss review", "Jan-2027 or next trigger"],
), "authorised_abbreviations_list_near_miss_review_record")

# ============================================================== IMS.3 ====
IMS3 = SOPSpecV2(
    sop_no="SOP-IMS.3",
    title="Medical Record Reflects Continuity of Care",
    purpose_plain=(
        "This SOP sets out the specific items that have to be present "
        "in every medical record at «Hospital Name» so the record "
        "actually shows the whole arc of a patient's care: the reason "
        "for admission and the plan of care, every assessment and "
        "procedure that happened, transfer details if the patient moved "
        "to another hospital, a copy of the discharge summary, a copy "
        "of the cause-of-death certificate where the patient died, and "
        "access to the record for the care providers who need it."
    ),
    purpose_trigger=(
        "A patient is transferred to another hospital, and the record "
        "left behind says nothing about why, what condition they were "
        "in, or what was sent with them -- if that patient is ever "
        "transferred back, or a complaint is raised, this hospital's own "
        "record cannot answer basic questions about its own care. This "
        "SOP is what makes sure that never happens."
    ),
    purpose_why=(
        "We do this because a record that is technically well-formed -- "
        "properly identified, properly authenticated -- can still fail "
        "to actually tell the story of the patient's care if these "
        "specific items are missing, and a record that cannot tell that "
        "story cannot support the next decision made from it."
    ),
    purpose_text=(
        "To define that the medical record at «Hospital Name» contains: "
        "the reasons for admission, diagnosis and plan of care; details "
        "of assessments, reassessments, consultations, investigation "
        "results, operative and other procedures, and the care provided; "
        "transfer details when a patient is transferred to another "
        "hospital; a copy of the discharge summary; a copy of the "
        "cause-of-death certificate in case of death; and access for "
        "care providers to current and past medical records."
    ),
    scope_why=(
        "so the Medical Records Officer and every treating doctor and "
        "nurse know exactly which items make a record complete, and "
        "that a record missing any one of them is not closed until it "
        "is fixed."
    ),
    scope_text=(
        "Applies to every medical record at «Hospital Name» and to "
        "treating doctors, nurses, the Medical Records Officer and the "
        "nursing supervisor on duty after hours. It covers the specific "
        "continuity-of-care items this chapter requires to be present in "
        "the record. It does not cover how assessment, handover, "
        "transfer-out or the discharge summary itself are actually "
        "carried out clinically -- those methods are set out in their "
        "own separate care SOPs; this SOP owns only that the resulting "
        "documents and details end up in the record."
    ),
    responsibility_why=(
        "a record that is \"probably complete\" because the care itself "
        "went well is not the same as a record actually checked for "
        "every required item -- someone has to be named to check, "
        "every time."
    ),
    responsibilities=[
        ("Treating Doctors", "Record the reason for admission, diagnosis and plan of care; ensure operative and procedure notes are completed; certify cause of death where applicable."),
        ("Nurses", "Record assessments, reassessments and the nursing care provided."),
        ("Medical Records Officer", "Checks presence of every continuity item at filing after discharge or death; does not close a record missing a required item; manages after-hours retrieval during the day."),
        ("Nursing Supervisor on Duty", "Manages after-hours record retrieval for care providers who need it."),
    ],
    items=[
        PlainItem(
            heading="Record why the patient was admitted, the diagnosis, and the plan of care",
            why=(
                "A record that does not say why a patient was admitted "
                "or what the plan of care actually was forces anyone "
                "who reads it later to reconstruct the episode from "
                "memory or guesswork -- exactly what a medical record "
                "exists to prevent."
            ),
            body=[
                "The medical record contains the reasons for admission "
                "(or the presenting problem, for an ambulatory visit), "
                "the working or confirmed diagnosis, and the plan of "
                "care.",
                "The treating doctor records these three items. How "
                "the assessment and care plan are actually developed is "
                "covered elsewhere; this step is only about making sure "
                "those three items are present in the record and can be "
                "found without reconstructing the episode from memory.",
                "The «Medical Records Officer» checks that these items "
                "are present when the record is filed after discharge "
                "or death.",
            ],
            oe_code="IMS.3.a",
            boundary=[
                "How assessment and care planning are actually carried out is owned by AAC.3; this step owns that the reason for admission, diagnosis and plan end up documented in the record.",
            ],
        ),
        PlainItem(
            heading="Record every assessment, investigation, procedure and the care actually provided",
            why=(
                "A procedure with no note, or an investigation ordered "
                "with no result ever filed, leaves a gap in the record "
                "that looks exactly like care that never happened, even "
                "when it did."
            ),
            body=[
                "The medical record contains the details of "
                "assessments, reassessments, consultations, "
                "investigation results, operative and other procedures, "
                "and the care actually provided.",
                "Treating doctors and nurses record: the initial "
                "assessment and every reassessment; any consultation "
                "requested and the consultant's opinion; investigation "
                "results, filed or electronically linked; operative "
                "notes and other procedure notes; and the care actually "
                "provided, including nursing care.",
                "A gap in this chain -- a procedure with no note, or an "
                "investigation with no result in the record -- is "
                "treated as an incomplete record, and is completed "
                "before the record is closed.",
            ],
            oe_code="IMS.3.b",
            boundary=[
                "How assessments, investigations and operative procedures are carried out clinically is owned by AAC and COP; this step owns that the resulting notes and results end up in the record, with no gap.",
            ],
        ),
        PlainItem(
            heading="Record transfer details when a patient moves to another hospital",
            why=(
                "If this hospital's own record says nothing about why a "
                "patient was transferred or what condition they were in, "
                "this hospital has no answer of its own if that care is "
                "ever questioned later."
            ),
            body=[
                "When a patient is transferred to another hospital, the "
                "medical record contains the details of that transfer.",
                "Those details are: the reason for transfer, the "
                "receiving organisation, the date and time of transfer, "
                "the patient's clinical condition at the time of "
                "transfer, the documents sent with the patient, and the "
                "name of the transferring doctor.",
                "A copy of the transfer note stays in the record after "
                "the patient has left -- it is not sent away with the "
                "patient and nothing kept behind.",
            ],
            oe_code="IMS.3.c",
            boundary=[
                "The transfer-out decision and the safety criteria for making it are owned by AAC.2; this step owns that the resulting details end up in this hospital's own record.",
            ],
        ),
        PlainItem(
            heading="File a copy of the discharge summary before the record is closed",
            why=(
                "A discharge summary that was handed to the patient but "
                "never kept on file leaves this hospital with no record "
                "of its own account of how the episode ended."
            ),
            body=[
                "The medical record contains a copy of the discharge "
                "summary.",
                "How the discharge summary is written and given to the "
                "patient -- including a patient who leaves against "
                "medical advice -- is covered elsewhere. This step owns "
                "that a copy, paper or electronic, is filed in the "
                "medical record before the record is closed.",
                "The «Medical Records Officer» does not file a "
                "discharged patient's record as complete until the "
                "discharge-summary copy is present.",
            ],
            oe_code="IMS.3.d",
            boundary=[
                "Writing the discharge summary and giving it to the patient is owned by AAC.8; this step owns that a copy of it is also filed in the record.",
            ],
        ),
        PlainItem(
            heading="File a copy of the cause-of-death certificate when a patient dies",
            why=(
                "A death record with no copy of the cause-of-death "
                "certificate leaves this hospital unable to show, from "
                "its own file, what it formally certified as the cause "
                "of death."
            ),
            body=[
                "In case of death, the medical record contains a copy "
                "of the cause-of-death certificate.",
                "The treating doctor, or the doctor who certifies the "
                "death, ensures a copy of that certificate is filed in "
                "the record. What is told to the family through the "
                "death summary is covered elsewhere; this step owns "
                "that the certificate copy itself is also in the "
                "record.",
                "The «Medical Records Officer» does not file a "
                "deceased patient's record as complete until the cause-"
                "of-death certificate copy is present.",
            ],
            oe_code="IMS.3.e",
            boundary=[
                "The death summary given to the family is owned by AAC.8; this step owns that a copy of the certificate itself is also filed in the record.",
            ],
        ),
        PlainItem(
            heading="Give care providers access to the current and past medical record when they need it",
            why=(
                "A doctor who cannot retrieve a patient's past record "
                "during an after-hours emergency is making decisions "
                "blind to history that might change what they do -- "
                "access has to work at 3 a.m. as reliably as at 3 p.m."
            ),
            body=[
                "Care providers have access to current and past medical "
                "records.",
                "A treating doctor or nurse responsible for the patient "
                "can obtain the current record and the previous-episode "
                "records needed for care, during working hours and "
                "after hours. The «Medical Records Officer» (during the "
                "day) and the «nursing supervisor on duty» (after "
                "hours) know how to retrieve a record.",
                "Access under this step is for care providers who "
                "actually need the record to care for the patient -- "
                "not open browsing. Confidentiality, security and the "
                "general disclosure gate are covered separately. "
                "After-hours retrieval is logged.",
            ],
            oe_code="IMS.3.f",
            boundary=[
                "Confidentiality, security and the disclosure gate for anyone who is not a treating care provider are owned by IMS.4; this step owns access for the care providers actually treating the patient.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the IMS.3 Records folder).",
    related_documents=[
        "Hospital's Complete and Accurate Medical Record SOP (IMS.2)",
        "Hospital's Confidentiality, Integrity and Security of Records SOP (IMS.4)",
        "Hospital's transfer-out, assessment and discharge-summary SOPs (AAC.2, AAC.3, AAC.8)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a filed record is "
        "found missing a discharge-summary copy, a cause-of-death "
        "certificate copy, or transfer details, or if a related policy "
        "named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_IMS_CITE.format(code="IMS.3"),
    ],
)

SOPS.append(("SOP_IMS.3.a_to_f_medical_record_reflects_continuity_of_care.docx", IMS3))

# ---- IMS.3 Records -------------------------------------------------
_add("IMS.3", 1, RecordSpec(
    oe_code="IMS.3.a",
    oe_requirement="The medical record contains information regarding reasons for admission, diagnosis and plan of care.",
    record_title="IMS.3 Record 01 — Admission-reason, diagnosis and care-plan presence check",
    what_is_this="This record is the proof these three items were actually checked present in the record at filing -- not assumed present because the care itself was good.",
    real_example="At filing, the Medical Records Officer confirms the admission reason, working diagnosis and care plan are all documented in the sampled discharged record.",
    why_nabh_asks="A record that does not say why a patient was admitted or what the plan of care actually was forces anyone who reads it later to reconstruct the episode from memory or guesswork -- exactly what a medical record exists to prevent.",
    how_to_fill=[
        ("Patient / Record No.", "Who."),
        ("Admission Reason Present (Y/N)", "Confirmed."),
        ("Diagnosis Present (Y/N)", "Confirmed."),
        ("Plan of Care Present (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.3")],
    column_headers=["Patient / Record No.", "Admission Reason Present (Y/N)", "Diagnosis Present (Y/N)", "Plan of Care Present (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — UID-00647", "Y", "Y", "Y"],
), "admission_reason_diagnosis_care_plan_presence_check")

_add("IMS.3", 2, RecordSpec(
    oe_code="IMS.3.b",
    oe_requirement="The medical record contains the details of assessments, reassessments, consultations, results of investigations, operative and other procedures, and the details of the care provided.",
    record_title="IMS.3 Record 02 — Completeness-chain check for assessments, investigations and procedures",
    what_is_this="This record is the proof a filed record was actually checked for gaps -- a procedure with no note, an investigation with no filed result -- before being treated as complete.",
    real_example="A gap is found: an ultrasound was ordered but the result was never filed; the Medical Records Officer holds the record open until the report is retrieved and filed.",
    why_nabh_asks="A procedure with no note, or an investigation ordered with no result ever filed, leaves a gap in the record that looks exactly like care that never happened, even when it did.",
    how_to_fill=[
        ("Patient / Record No.", "Who."),
        ("Items Checked (Assessments/Investigations/Procedures)", "What was reviewed."),
        ("Gap Found (Y/N, Description)", "If any."),
        ("Closure (Y/N, Date)", "Record held open or closed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.3")],
    column_headers=["Patient / Record No.", "Items Checked (Assessments/Investigations/Procedures)", "Gap Found (Y/N, Description)", "Closure (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — UID-00652", "Investigations, operative notes", "Y — ultrasound result not filed", "Y — filed and closed 16-Mar-2026"],
), "completeness_chain_check_assessments_investigations_procedures")

_add("IMS.3", 3, RecordSpec(
    oe_code="IMS.3.c",
    oe_requirement="When a patient is transferred to another hospital, the medical record contains the details of the transfer.",
    record_title="IMS.3 Record 03 — Transfer-details presence check",
    what_is_this="This record is the proof a transfer's reason, condition at transfer, receiving organisation and transferring doctor were actually documented and retained in this hospital's own record -- not sent away entirely with the patient.",
    real_example="A patient transferred to a tertiary centre has a transfer note on file naming the reason, receiving hospital, clinical condition at transfer, and the transferring doctor, with a copy retained here.",
    why_nabh_asks="If this hospital's own record says nothing about why a patient was transferred or what condition they were in, this hospital has no answer of its own if that care is ever questioned later.",
    how_to_fill=[
        ("Patient / Transfer Date", "Who and when."),
        ("Reason / Receiving Organisation", "Why and where."),
        ("Condition at Transfer / Documents Sent", "Clinical detail."),
        ("Copy Retained in Record (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.3")],
    column_headers=["Patient / Transfer Date", "Reason / Receiving Organisation", "Condition at Transfer / Documents Sent", "Copy Retained in Record (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — UID-00658 / 18-Mar-2026", "Higher level of ICU care needed / City Tertiary Hospital", "Stable, on oxygen; summary + investigation copies sent", "Y"],
), "transfer_details_presence_check")

_add("IMS.3", 4, RecordSpec(
    oe_code="IMS.3.d",
    oe_requirement="The medical record contains a copy of the discharge summary.",
    record_title="IMS.3 Record 04 — Discharge-summary-copy filing confirmation",
    what_is_this="This record is the proof a discharged record was not closed until the discharge-summary copy was actually confirmed present -- not assumed filed because the patient received their own copy.",
    real_example="A record held pending for two days until the discharge-summary copy is confirmed filed, then closed.",
    why_nabh_asks="A discharge summary that was handed to the patient but never kept on file leaves this hospital with no record of its own account of how the episode ended.",
    how_to_fill=[
        ("Patient / Discharge Date", "Who and when."),
        ("Discharge-Summary Copy Present (Y/N)", "Confirmed."),
        ("Record Closure Date", "When the record was closed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.3")],
    column_headers=["Patient / Discharge Date", "Discharge-Summary Copy Present (Y/N)", "Record Closure Date"],
    worked_example_row=["WORKED EXAMPLE — UID-00661 / 16-Mar-2026", "Y", "18-Mar-2026"],
), "discharge_summary_copy_filing_confirmation")

_add("IMS.3", 5, RecordSpec(
    oe_code="IMS.3.e",
    oe_requirement="In case of death, the medical record contains a copy of the cause-of-death certificate.",
    record_title="IMS.3 Record 05 — Cause-of-death-certificate-copy filing confirmation",
    what_is_this="This record is the proof a deceased patient's record was not closed until the cause-of-death certificate copy was actually confirmed present -- not assumed filed because the family received the original.",
    real_example="A deceased patient's record is held pending until the certifying doctor's cause-of-death certificate copy is confirmed filed, then closed.",
    why_nabh_asks="A death record with no copy of the cause-of-death certificate leaves this hospital unable to show, from its own file, what it formally certified as the cause of death.",
    how_to_fill=[
        ("Patient / Date of Death", "Who and when."),
        ("Certificate Copy Present (Y/N)", "Confirmed."),
        ("Record Closure Date", "When the record was closed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.3")],
    column_headers=["Patient / Date of Death", "Certificate Copy Present (Y/N)", "Record Closure Date"],
    worked_example_row=["WORKED EXAMPLE — UID-00665 / 20-Mar-2026", "Y", "22-Mar-2026"],
), "cause_of_death_certificate_copy_filing_confirmation")

_add("IMS.3", 6, RecordSpec(
    oe_code="IMS.3.f",
    oe_requirement="Care providers have access to current and past medical records.",
    record_title="IMS.3 Record 06 — After-hours medical-record retrieval log",
    what_is_this="This record is the proof a care provider who needed a record outside working hours could actually get it, with the retrieval logged -- not access that only works during the day.",
    real_example="A night-duty doctor retrieves a past-episode record at 2 AM through the nursing supervisor on duty, logged with the time and reason for retrieval.",
    why_nabh_asks="A doctor who cannot retrieve a patient's past record during an after-hours emergency is making decisions blind to history that might change what they do -- access has to work at 3 a.m. as reliably as at 3 p.m.",
    how_to_fill=[
        ("Date/Time", "When retrieved."),
        ("Requested By / Patient", "Who needed it and for whom."),
        ("Reason", "Why it was needed."),
        ("Retrieved By / Time Taken", "Who provided it, how fast."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.3")],
    column_headers=["Date/Time", "Requested By / Patient", "Reason", "Retrieved By / Time Taken"],
    worked_example_row=["WORKED EXAMPLE — 20-Mar-2026, 2:10 AM", "Dr. Iyer (night duty) / UID-00670", "Past-episode history needed for acute decompensation", "Nursing Supervisor R. Nair / 10 minutes"],
), "after_hours_medical_record_retrieval_log")

# ============================================================== IMS.4 ====
IMS4 = SOPSpecV2(
    sop_no="SOP-IMS.4",
    title="Confidentiality, Integrity and Security of Records, Data and Information",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» keeps patient "
        "information confidential, keeps records accurate and "
        "unaltered except through a proper correction, secures both "
        "paper and electronic records, discloses privileged health "
        "information only with authorisation or a recorded legal basis, "
        "and handles every request for access to a medical record in "
        "the same consistent way."
    ),
    purpose_trigger=(
        "A staff member discusses a patient's diagnosis in the lift "
        "where a visitor can overhear, or hands a photocopied chart to "
        "someone who asked nicely without checking who they actually "
        "are -- neither looks like a dramatic breach, but both are "
        "exactly how confidentiality actually fails in practice. This "
        "SOP exists to make the careful response the automatic one."
    ),
    purpose_why=(
        "We do this because confidentiality of protected health "
        "information is paramount -- it has to be safeguarded "
        "everywhere information is processed, stored or shared, not "
        "only in the records room."
    ),
    purpose_text=(
        "To define how «Hospital Name» maintains the confidentiality, "
        "integrity and security of records, data and information; "
        "discloses privileged health information only as authorised by "
        "the patient and/or as required by law; and addresses requests "
        "for access to information in the medical records by patients, "
        "physicians and other public agencies consistently."
    ),
    scope_why=(
        "so every staff member who can see, touch or access a medical "
        "record -- not only the Medical Records Officer -- knows "
        "confidentiality is something they personally safeguard every "
        "day, not a rule that lives in a policy folder."
    ),
    scope_text=(
        "Applies to all records, data and information at «Hospital "
        "Name», in paper and electronic form, and to every staff "
        "member, the Medical Records Officer, and the IT or "
        "information-systems in-charge. It covers confidentiality, "
        "integrity and security of this hospital's medical records and "
        "general organisational information, how disclosure is "
        "authorised, and how access requests are processed. It does "
        "not cover confidentiality of staff personal files, which is "
        "set out in its own separate SOP, and it does not cover how "
        "the patient's own right of access is first recognised -- only "
        "how a request is processed once received."
    ),
    responsibility_why=(
        "confidentiality that depends on \"everyone being careful\" "
        "with no named owner for storage, access control and the "
        "disclosure log tends to fail exactly at the busy moment nobody "
        "stops to think."
    ),
    responsibilities=[
        ("Medical Records Officer", "Receives and processes every access request through the standard form; keeps the disclosure log; manages physical storage security."),
        ("IT / Information-Systems In-Charge", "Holds and reviews the access-control list; manages electronic security -- unique logins, session timeout, malware protection."),
        ("All Staff", "Treat patient information as need-to-know only; never discuss a patient's condition in a public area; invoke stop-work when a disclosure lacks authorisation or lawful basis."),
        ("Medical Superintendent", "Receives stop-work escalations; is accountable for confidentiality, integrity and security overall."),
    ],
    items=[
        PlainItem(
            heading="Treat patient information as need-to-know, everywhere, every time",
            why=(
                "A corridor conversation about a patient's diagnosis "
                "within earshot of a visitor is a confidentiality "
                "breach exactly as real as handing over the wrong file "
                "-- it just feels more casual while it is happening."
            ),
            body=[
                "«Hospital Name» maintains the confidentiality of "
                "records, data and information.",
                "Privileged health information -- the medical record "
                "and any data that identifies a patient and their care "
                "-- is available only to staff who need it for care, "
                "for an authorised review, or for a disclosure that "
                "meets this hospital's disclosure requirement. Casual "
                "discussion of a patient's condition in corridors, "
                "lifts or other public areas is prohibited.",
                "Paper records are stored in the records room or a "
                "locked department cupboard when not in use. Electronic "
                "records are restricted by role. A visitor, vendor or "
                "unauthorised staff member is never left alone with a "
                "record.",
            ],
            oe_code="IMS.4.a (ASTERISKED)",
            boundary=[
                "Confidentiality of staff personal files is owned by HRM.6; this step covers patient medical records and general organisational information.",
            ],
        ),
        PlainItem(
            heading="Keep records accurate and unaltered, except through a proper correction",
            why=(
                "A record that can be silently altered with no trail "
                "cannot be trusted by the next clinician who reads it, "
                "or defended later if the care it documents is ever "
                "questioned."
            ),
            body=[
                "«Hospital Name» maintains the integrity of records, "
                "data and information.",
                "Integrity means the record stays complete and "
                "unaltered except by an authenticated correction. A "
                "paper correction follows the single-line-through "
                "method described in this hospital's medical-record "
                "SOP. An electronic correction leaves an amendment "
                "trail showing the original entry, the change made, "
                "who made it, and when.",
                "Backups of electronic records are checked «monthly» "
                "for restorability. Paper records are protected from "
                "loss, mixing and unauthorised removal through an "
                "issue/return log.",
            ],
            oe_code="IMS.4.b (ASTERISKED)",
            boundary=[
                "The exact correction method for a paper entry is owned by IMS.2.d; this step owns that integrity is maintained system-wide, including backup restorability.",
            ],
        ),
        PlainItem(
            heading="Secure records physically and electronically, not just describe how they should be secured",
            why=(
                "A policy that says records are secure means nothing if "
                "the records room is routinely left unlocked, or if "
                "staff who left the hospital two years ago still have "
                "an active login."
            ),
            body=[
                "«Hospital Name» maintains the security of records, "
                "data and information.",
                "Physical security: the records room is locked when "
                "unattended; keys or access cards are held by named "
                "persons; after-hours access is logged.",
                "Electronic security: every user has a unique identity "
                "with a password that is never shared, access is "
                "restricted by role, sessions time out automatically "
                "after «fifteen minutes», and machines that hold health "
                "information carry malware protection.",
                "The «IT / information-systems in-charge» holds the "
                "access-control list and reviews it «quarterly», and "
                "immediately whenever a staff member joins, leaves or "
                "changes role.",
            ],
            oe_code="IMS.4.c (ASTERISKED)",
            technical_sources=[ISO_27001_SRC, ISO_27799_SRC],
        ),
        PlainItem(
            heading="Disclose privileged health information only with authorisation or a recorded legal basis",
            why=(
                "A disclosure made because someone asked, with no "
                "documented authorisation and no recorded legal basis, "
                "is the single most common way a hospital loses control "
                "of a patient's own information."
            ),
            body=[
                "«Hospital Name» discloses privileged health "
                "information only as authorised by the patient and/or "
                "as required by law.",
                "A disclosure happens only when the patient, or someone "
                "legally authorised to act for the patient, has given "
                "documented authorisation for that specific disclosure; "
                "or when a written legal or regulatory requirement to "
                "disclose is recorded, such as a court order or a "
                "statutory return.",
                "Every disclosure is logged: what was disclosed, to "
                "whom, the authorisation or lawful basis it relied on, "
                "the date, and who released it. A contribution to an "
                "external database that includes privileged health "
                "information is logged here as well, in addition to "
                "that database's own contribution register.",
                "Where neither a documented authorisation nor a "
                "recorded lawful basis exists, the stop-work authority "
                "described below applies.",
            ],
            oe_code="IMS.4.d",
            boundary=[
                "The external-database contribution register itself is owned by IMS.1.d; this step is the general disclosure gate that any contribution of patient-identifiable data must also clear.",
            ],
        ),
        PlainItem(
            heading="Handle every access request the same documented way, whoever is asking",
            why=(
                "Treating a request from a familiar doctor casually, "
                "while making a stranger fill out the full form, is how "
                "an \"exception made this once\" quietly becomes the "
                "real policy -- the form exists precisely so there are "
                "no quiet exceptions."
            ),
            body=[
                "Requests for access to information in the medical "
                "records, by patients, physicians and other public "
                "agencies, are addressed consistently.",
                "The «Medical Records Officer» receives every request "
                "on the «medical-record access request form». The same "
                "steps apply, whoever is asking:",
                "1. Identify the requester and the record.",
                "2. Decide the pathway -- a patient or their authorised "
                "representative follows this hospital's own right-of-"
                "access process; a treating physician involved in the "
                "patient's care follows the continuity-of-care access "
                "rule; any other physician or public agency needs the "
                "authorisation or lawful basis this SOP already "
                "requires for disclosure.",
                "3. Record the decision -- grant, grant in part, or "
                "refuse with a stated reason -- within «seven working "
                "days».",
                "4. Release only a copy, never the original, unless a "
                "lawful process specifically requires the original and "
                "a copy is kept on file.",
                "An ad-hoc release to a doctor who happens to be known "
                "to staff, or to a visiting official, that bypasses "
                "this form, fails this requirement regardless of how "
                "well-intentioned it was.",
            ],
            oe_code="IMS.4.e (ASTERISKED)",
        ),
        PlainItem(
            heading="Stop before releasing anything that does not have documented authorisation or a recorded legal basis",
            why=(
                "A disclosure, once made, cannot be undone -- the moment "
                "to catch a missing authorisation is before the record "
                "leaves the building, not after."
            ),
            body=[
                "Do not go ahead with a disclosure or release if any of "
                "the following is about to happen:",
                "1. Releasing or disclosing a patient's privileged "
                "health information without the patient's (or legally "
                "authorised representative's) documented authorisation, "
                "and without a documented lawful basis.",
                "2. Handing over an original medical record to a "
                "requester when a copy would do, unless a recorded "
                "lawful process requires the original.",
                "3. Sending privileged health information through an "
                "uncontrolled channel -- unencrypted personal "
                "messaging, an unnamed USB drive, an unattended fax -- "
                "when a controlled channel exists.",
                "When stop-work is invoked: the record or data is not "
                "released; the information is made safe (paper "
                "returned to the locked store, an electronic session "
                "closed); and it is reported to the «Medical Records "
                "Officer» or the «Medical Superintendent» the same "
                "shift.",
                "No approval is needed to invoke this stop-work "
                "authority. Confidentiality of protected health "
                "information overrides convenience.",
            ],
            oe_code="IMS.4.d (stop-work authority)",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the IMS.4 Records folder).",
    related_documents=[
        "Hospital's Information Needs of Stakeholders SOP (IMS.1)",
        "Hospital's Availability, Document Control and Retention SOP (IMS.5)",
        "Hospital's staff-confidentiality SOP (HRM.6)",
        "Hospital's patient rights and right-of-access policy (PRE.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a stop-work "
        "disclosure event is invoked, if an access-request decision "
        "misses the seven-working-day window, or if a related policy "
        "named above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_IMS_CITE.format(code="IMS.4"),
        EHR_STANDARDS_INDIA_SRC,
        ABDM_HDM_POLICY_SRC,
        ISO_27001_SRC,
        ISO_27799_SRC,
    ],
)

SOPS.append(("SOP_IMS.4.a_to_e_confidentiality_integrity_security_records_data_information.docx", IMS4))

# ---- IMS.4 Records -------------------------------------------------
_add("IMS.4", 1, RecordSpec(
    oe_code="IMS.4.a (ASTERISKED)",
    oe_requirement="The organisation maintains the confidentiality of records, data and information.",
    record_title="IMS.4 Record 01 — Records-storage confidentiality spot-check",
    what_is_this="This record is the proof the records room was actually found locked, and no record was actually left with an unattended visitor or vendor -- not a confidentiality rule that exists on paper only.",
    real_example="A March spot check finds the records room locked when unattended, with no visitor or vendor found alone with a record during the check.",
    why_nabh_asks="A corridor conversation about a patient's diagnosis within earshot of a visitor is a confidentiality breach exactly as real as handing over the wrong file -- it just feels more casual while it is happening.",
    how_to_fill=[
        ("Check Date", "When checked."),
        ("Records Room Locked (Y/N)", "Confirmed."),
        ("Unauthorised Person With Record Found (Y/N)", "Confirmed."),
        ("Corrective Action (if any)", "What was done."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.4")],
    column_headers=["Check Date", "Records Room Locked (Y/N)", "Unauthorised Person With Record Found (Y/N)", "Corrective Action (if any)"],
    worked_example_row=["WORKED EXAMPLE — 10-Mar-2026", "Y", "N", "N/A"],
), "records_storage_confidentiality_spot_check")

_add("IMS.4", 2, RecordSpec(
    oe_code="IMS.4.b (ASTERISKED)",
    oe_requirement="The organisation maintains the integrity of records, data and information.",
    record_title="IMS.4 Record 02 — Monthly backup-restorability test log",
    what_is_this="This record is the proof an electronic backup was actually tested for restorability every month -- not a backup that runs automatically and is never verified to actually work.",
    real_example="The March backup restorability test successfully restores a sample patient record from the previous night's backup within 20 minutes.",
    why_nabh_asks="A record that can be silently altered with no trail cannot be trusted by the next clinician who reads it, or defended later if the care it documents is ever questioned.",
    how_to_fill=[
        ("Test Date", "When tested."),
        ("Backup Dataset Tested", "What was restored."),
        ("Restoration Successful (Y/N)", "Confirmed."),
        ("Time Taken / Issue Found", "How long, or what failed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.4")],
    column_headers=["Test Date", "Backup Dataset Tested", "Restoration Successful (Y/N)", "Time Taken / Issue Found"],
    worked_example_row=["WORKED EXAMPLE — 10-Mar-2026", "Sample patient record from previous night's backup", "Y", "20 minutes"],
), "monthly_backup_restorability_test_log")

_add("IMS.4", 3, RecordSpec(
    oe_code="IMS.4.c (ASTERISKED)",
    oe_requirement="The organisation maintains the security of records, data and information.",
    record_title="IMS.4 Record 03 — Quarterly access-control-list review record",
    what_is_this="This record is the proof the electronic access-control list was actually reviewed every quarter, with leavers and role changes actually removed or updated -- not a list left stale after someone's last day.",
    real_example="The Q1 review finds one former employee's login still active, deactivated the same day it is found, and two role changes updated to the correct access level.",
    why_nabh_asks="A policy that says records are secure means nothing if the records room is routinely left unlocked, or if staff who left the hospital two years ago still have an active login.",
    how_to_fill=[
        ("Review Date / Quarter", "When reviewed."),
        ("Accounts Reviewed", "How many checked."),
        ("Stale / Incorrect Access Found (Y/N)", "Confirmed."),
        ("Corrective Action / Date", "What was fixed, when."),
    ],
    verified_sources=[ISO_27001_SRC, NABH_IMS_CITE.format(code="IMS.4")],
    column_headers=["Review Date / Quarter", "Accounts Reviewed", "Stale / Incorrect Access Found (Y/N)", "Corrective Action / Date"],
    worked_example_row=["WORKED EXAMPLE — Q1 2026", "42 accounts", "Y — 1 former employee login active", "Deactivated same day — 14-Mar-2026"],
), "quarterly_access_control_list_review_record")

_add("IMS.4", 4, RecordSpec(
    oe_code="IMS.4.d",
    oe_requirement="The organisation discloses privileged health information as authorised by the patient and/or as required by law.",
    record_title="IMS.4 Record 04 — Disclosure log",
    what_is_this="This record is the proof every disclosure of privileged health information actually had a documented authorisation or a recorded legal basis -- not a disclosure made because someone asked.",
    real_example="A disclosure to an insurance company is logged with the patient's signed authorisation attached, the date released, and the name of the releasing staff member.",
    why_nabh_asks="A disclosure made because someone asked, with no documented authorisation and no recorded legal basis, is the single most common way a hospital loses control of a patient's own information.",
    how_to_fill=[
        ("Date", "When disclosed."),
        ("What Was Disclosed / To Whom", "Content and recipient."),
        ("Authorisation / Lawful Basis", "What permitted it."),
        ("Released By", "Who released it."),
    ],
    verified_sources=[ABDM_HDM_POLICY_SRC, NABH_IMS_CITE.format(code="IMS.4")],
    column_headers=["Date", "What Was Disclosed / To Whom", "Authorisation / Lawful Basis", "Released By"],
    worked_example_row=["WORKED EXAMPLE — 18-Mar-2026", "Discharge summary copy / ABC Insurance Co.", "Patient's signed authorisation on file", "Medical Records Officer"],
), "disclosure_log")

_add("IMS.4", 5, RecordSpec(
    oe_code="IMS.4.e (ASTERISKED)",
    oe_requirement="Requests for access to information in the medical records by patients, physicians and other public agencies are addressed consistently.",
    record_title="IMS.4 Record 05 — Medical-record access request form and decision log",
    what_is_this="This record is the proof every access request actually went through the same form and the same decision timeline -- not an ad-hoc release to someone staff happened to know.",
    real_example="A physician's request for a prior patient's records is logged, the pathway correctly identified as requiring authorisation, and a decision (granted, copy only) recorded within five working days.",
    why_nabh_asks="Treating a request from a familiar doctor casually, while making a stranger fill out the full form, is how an \"exception made this once\" quietly becomes the real policy -- the form exists precisely so there are no quiet exceptions.",
    how_to_fill=[
        ("Request Date / Requester", "Who asked and when."),
        ("Pathway Identified", "Patient / treating physician / other."),
        ("Decision (Grant/Partial/Refuse) / Date", "Within seven working days."),
        ("Copy or Original Released", "Should be copy unless lawfully required otherwise."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.4")],
    column_headers=["Request Date / Requester", "Pathway Identified", "Decision (Grant/Partial/Refuse) / Date", "Copy or Original Released"],
    worked_example_row=["WORKED EXAMPLE — 15-Mar-2026 / Dr. Kamath (external physician)", "Other physician — authorisation required", "Granted — 20-Mar-2026", "Copy"],
), "medical_record_access_request_form_decision_log")

_add("IMS.4", 6, RecordSpec(
    oe_code="IMS.4.d (stop-work authority)",
    oe_requirement="A disclosure is not made without documented patient authorisation or a documented lawful basis; stop-work applies when neither exists.",
    record_title="IMS.4 Record 06 — Disclosure stop-work log",
    what_is_this="This record is the proof a disclosure that lacked authorisation or a lawful basis was actually stopped before it happened -- not released because the requester seemed legitimate.",
    real_example="A phone caller claiming to be a relative asks for a patient's diagnosis; the receiving staff member invokes stop-work, declines to disclose, and reports it to the Medical Records Officer the same shift.",
    why_nabh_asks="A disclosure, once made, cannot be undone -- the moment to catch a missing authorisation is before the record leaves the building, not after.",
    how_to_fill=[
        ("Date/Time", "When stopped."),
        ("Staff Member / Requester", "Who stopped it, who asked."),
        ("Reason Stop-Work Invoked", "What was missing."),
        ("Reported To / Outcome", "Same-shift report and result."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.4")],
    column_headers=["Date/Time", "Staff Member / Requester", "Reason Stop-Work Invoked", "Reported To / Outcome"],
    worked_example_row=["WORKED EXAMPLE — 18-Mar-2026, 3:40 PM", "Reception staff S. Rao / phone caller claiming to be relative", "No documented authorisation; identity not verifiable by phone", "Medical Records Officer — caller advised to submit written request"],
), "disclosure_stop_work_log")

# ============================================================== IMS.5 ====
IMS5 = SOPSpecV2(
    sop_no="SOP-IMS.5",
    title="Availability, Document Control and Retention of Records, Data and Information",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» keeps an effective "
        "document-control process so only the current version of a "
        "policy or form is ever in use, retains clinical records for "
        "the period this hospital has actually decided on after legal "
        "advice, keeps that retained information just as confidential "
        "and secure as active records, and destroys records only "
        "through a controlled, documented process."
    ),
    purpose_trigger=(
        "A ward is still using a printed copy of a policy that was "
        "superseded eight months ago, because nobody told them the "
        "version changed -- and in an emergency, staff follow the wrong, "
        "outdated instructions. This SOP exists so an obsolete document "
        "cannot quietly stay in circulation."
    ),
    purpose_why=(
        "We do this because obsolete information left in circulation "
        "confuses staff, patients and visitors just as much as missing "
        "information does -- and records destroyed too early, or kept "
        "insecurely while they wait to be destroyed, both put this "
        "hospital and its patients at risk."
    ),
    purpose_text=(
        "To define how «Hospital Name» keeps an effective process for "
        "document control; retains patients' clinical records, data and "
        "information according to its requirements; ensures the "
        "retention process provides the expected confidentiality and "
        "security; and destroys medical records, data and information "
        "only in accordance with the laid-down policy."
    ),
    scope_why=(
        "so every department that holds a controlled document or an "
        "archived record -- not only the Quality Coordinator -- knows "
        "an old version has to be taken out of use the same day a new "
        "one is issued, and a record is never destroyed on anyone's "
        "individual say-so."
    ),
    scope_text=(
        "Applies to every controlled document (policy, procedure, form, "
        "protocol) and every clinical record, in paper or electronic "
        "form, at «Hospital Name», and to the Quality Coordinator, the "
        "Medical Records Officer and the Medical Superintendent. It "
        "covers document control, retention, the confidentiality and "
        "security of records while they are retained, and destruction. "
        "It does not cover the day-to-day confidentiality and security "
        "measures used on active records -- that is set out in its own "
        "separate SOP in this chapter, which this SOP extends to the "
        "retained store."
    ),
    responsibility_why=(
        "document control and destruction without a single named owner "
        "each quietly drift -- an obsolete copy stays on a shelf, or a "
        "batch gets destroyed without anyone checking whether it was "
        "actually due."
    ),
    responsibilities=[
        ("Quality Coordinator", "Holds the current-document register; marks and removes obsolete copies the same day a new version is issued."),
        ("Medical Records Officer", "Holds the retention schedule; manages the archive issue/return log; completes destruction records."),
        ("Medical Superintendent", "Sets the retention period after legal advice; authorises every destruction batch."),
    ],
    items=[
        PlainItem(
            heading="Keep one current-document register, and remove obsolete copies the same day",
            why=(
                "A ward following a printed policy that was superseded "
                "months ago is following instructions this hospital no "
                "longer stands behind -- and in an emergency, that gap "
                "can matter."
            ),
            body=[
                "«Hospital Name» has an effective process for document "
                "control.",
                "The «Quality Coordinator» holds the current-document "
                "register. Every controlled document -- policy, "
                "procedure, form, protocol -- has a document number, "
                "title, version, date of issue, owner, and a review-due "
                "date. Only the current version is available at the "
                "point of use.",
                "When a new version is issued, old copies are taken out "
                "of use the same day. An obsolete master copy is marked "
                "\"obsolete\" and either stored or destroyed per the "
                "register -- it is never left on a notice board or a "
                "shared drive as though it were still current.",
            ],
            oe_code="IMS.5.a (ASTERISKED)",
        ),
        PlainItem(
            heading="Retain clinical records for a period this hospital has actually decided, not a remembered guess",
            why=(
                "A retention period nobody actually decided, or "
                "destruction carried out on a vaguely remembered "
                "number, puts this hospital at legal risk either way -- "
                "destroying too early loses evidence a patient or this "
                "hospital may need; keeping too long creates "
                "unnecessary exposure."
            ),
            body=[
                "«Hospital Name» retains patients' clinical records, "
                "data and information according to its own "
                "requirements.",
                "There is no single number of years that applies to "
                "every hospital. «Hospital Name» sets its retention "
                "period after legal advice, in line with applicable "
                "National Medical Commission and State rules, and "
                "writes that decided period into its own retention "
                "schedule before this policy is signed. A remembered "
                "number is never treated as the policy -- only the "
                "number this hospital has actually decided on, in "
                "writing, after that advice.",
                "The «Medical Records Officer» holds a retention "
                "schedule listing each record type -- in-patient "
                "record, out-patient record, diagnostic report, "
                "electronic backup -- its decided retention period, and "
                "where it is stored during that period: active shelf, "
                "archive, or electronic archive.",
            ],
            oe_code="IMS.5.b (ASTERISKED)",
        ),
        PlainItem(
            heading="Keep retained records just as confidential and secure as active ones",
            why=(
                "A record that is perfectly secure while active and "
                "then left loosely accessible once it is archived has "
                "not actually protected the patient -- the risk does "
                "not end the moment a record moves to storage."
            ),
            body=[
                "The retention process provides the confidentiality "
                "and security this hospital expects.",
                "Archived paper records are kept in a locked archive "
                "with an issue/return log, held to the same "
                "confidentiality standard as active records. Electronic "
                "archives are access-restricted, backed up, and "
                "protected from unauthorised alteration.",
                "A staff member who does not need an archived record "
                "for care, an authorised review, or a disclosure that "
                "meets this hospital's disclosure requirement, does not "
                "retrieve it. Every retrieval of an archived record is "
                "logged.",
            ],
            oe_code="IMS.5.c",
            boundary=[
                "The confidentiality and security standard itself is set by IMS.4; this step owns extending that same standard to the retained archive.",
            ],
        ),
        PlainItem(
            heading="Destroy records only through a controlled, authorised and documented process",
            why=(
                "Dumping intact records in general waste, or destroying "
                "a batch nobody checked was actually due, can both "
                "expose patient information and destroy evidence a "
                "pending legal process or complaint still needs."
            ),
            body=[
                "The destruction of medical records, data and "
                "information follows the laid-down policy.",
                "Destruction happens only when the retention period on "
                "the schedule has actually ended, the «Medical "
                "Superintendent» has authorised that specific batch, "
                "and a destruction record is completed -- naming the "
                "record identifiers or batch description, the method "
                "used, the date, and the two people present.",
                "Paper is shredded or otherwise made unreadable; "
                "electronic media is wiped or physically destroyed so "
                "the data cannot be reconstructed. Destruction is never "
                "dumping intact records in general waste.",
                "A record that is the subject of a pending legal "
                "process, a complaint, or an incident review is not "
                "destroyed until that process is closed -- even if its "
                "retention period has already ended.",
            ],
            oe_code="IMS.5.d",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the IMS.5 Records folder).",
    related_documents=[
        "Hospital's Confidentiality, Integrity and Security of Records SOP (IMS.4)",
        "Hospital's complaint-handling policy (PRE.6)",
        "Hospital's Incident Collection and Analysis SOP (PSQ.5)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an obsolete "
        "document is found still in use, if a destruction is identified "
        "that bypassed authorisation, or if a related policy named "
        "above in this chapter is revised."
    ),
    full_reference_list=[
        NABH_IMS_CITE.format(code="IMS.5"),
        EHR_STANDARDS_INDIA_SRC,
    ],
)

SOPS.append(("SOP_IMS.5.a_to_d_availability_document_control_retention_records_data_information.docx", IMS5))

# ---- IMS.5 Records -------------------------------------------------
_add("IMS.5", 1, RecordSpec(
    oe_code="IMS.5.a (ASTERISKED)",
    oe_requirement="The organisation has an effective process for document control.",
    record_title="IMS.5 Record 01 — Current-document register and obsolete-copy withdrawal record",
    what_is_this="This record is the proof every controlled document has a current version tracked on the register, and that an old version was actually withdrawn the same day a new one was issued -- not left in circulation.",
    real_example="The hand-hygiene protocol is revised to v2.1 on 10-March; the register shows the previous v2.0 copies withdrawn from all three nursing stations that same day.",
    why_nabh_asks="A ward following a printed policy that was superseded months ago is following instructions this hospital no longer stands behind -- and in an emergency, that gap can matter.",
    how_to_fill=[
        ("Document / Version", "Which document, which version."),
        ("Date of Issue / Owner", "When issued, who owns it."),
        ("Review Due Date", "Next review."),
        ("Previous Version Withdrawn (Y/N, Date)", "Confirmed same-day withdrawal."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.5")],
    column_headers=["Document / Version", "Date of Issue / Owner", "Review Due Date", "Previous Version Withdrawn (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — Hand-hygiene protocol / v2.1", "10-Mar-2026 / Infection Control Officer", "Mar-2027", "Y — 10-Mar-2026, all 3 nursing stations"],
), "current_document_register_obsolete_copy_withdrawal_record")

_add("IMS.5", 2, RecordSpec(
    oe_code="IMS.5.b (ASTERISKED)",
    oe_requirement="The organisation retains patients' clinical records, data and information according to its requirements.",
    record_title="IMS.5 Record 02 — Retention schedule",
    what_is_this="This record is the proof this hospital actually decided, in writing, its own retention period after legal advice -- not a number recalled from memory or copied from elsewhere.",
    real_example="The retention schedule lists in-patient records at the period decided after legal advice, consistent with applicable NMC and State rules, stored in the active archive for that period.",
    why_nabh_asks="A retention period nobody actually decided, or destruction carried out on a vaguely remembered number, puts this hospital at legal risk either way -- destroying too early loses evidence a patient or this hospital may need; keeping too long creates unnecessary exposure.",
    how_to_fill=[
        ("Record Type", "In-patient, out-patient, diagnostic report, backup, etc."),
        ("Retention Period (As Decided After Legal Advice)", "This hospital's own decided number."),
        ("Legal Basis Verified (Y/N, Date)", "Confirmed advice was actually taken."),
        ("Storage Location During Retention", "Active shelf, archive, electronic archive."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.5")],
    column_headers=["Record Type", "Retention Period (As Decided After Legal Advice)", "Legal Basis Verified (Y/N, Date)", "Storage Location During Retention"],
    worked_example_row=["WORKED EXAMPLE — In-patient record", "«________» (fill in after legal advice, per NMC/State rules)", "Y — 05-Jan-2026", "Electronic archive + physical archive"],
), "retention_schedule")

_add("IMS.5", 3, RecordSpec(
    oe_code="IMS.5.c",
    oe_requirement="The retention process provides the expected confidentiality and security.",
    record_title="IMS.5 Record 03 — Archive issue/return log",
    what_is_this="This record is the proof every retrieval of an archived record was actually logged, with only staff who genuinely needed it for care, review or a lawful disclosure retrieving it -- not open access to the archive.",
    real_example="A past-episode record is issued to a treating doctor for continuity of care, logged with issue and return dates, and confirmed returned to the locked archive the same week.",
    why_nabh_asks="A record that is perfectly secure while active and then left loosely accessible once it is archived has not actually protected the patient -- the risk does not end the moment a record moves to storage.",
    how_to_fill=[
        ("Record / Issue Date", "Which record, when issued."),
        ("Issued To / Reason", "Who and why."),
        ("Return Date", "When returned."),
        ("Confirmed Returned to Locked Archive (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.5")],
    column_headers=["Record / Issue Date", "Issued To / Reason", "Return Date", "Confirmed Returned to Locked Archive (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — UID-00610 / 12-Mar-2026", "Dr. Patel / continuity-of-care review for new admission", "15-Mar-2026", "Y"],
), "archive_issue_return_log")

_add("IMS.5", 4, RecordSpec(
    oe_code="IMS.5.d",
    oe_requirement="The destruction of medical records, data and information is in accordance with the laid-down policy.",
    record_title="IMS.5 Record 04 — Destruction authorisation and completion record",
    what_is_this="This record is the proof a destruction batch was actually authorised by the Medical Superintendent, confirmed past its retention period, checked against pending legal holds, and carried out by a documented method with two people present.",
    real_example="A batch of out-patient records past their retention period is checked against the complaint and incident logs for any pending hold, authorised by the Medical Superintendent, and shredded with two staff present, recorded on the destruction log.",
    why_nabh_asks="Dumping intact records in general waste, or destroying a batch nobody checked was actually due, can both expose patient information and destroy evidence a pending legal process or complaint still needs.",
    how_to_fill=[
        ("Batch Description / Record Type", "What is being destroyed."),
        ("Retention Period Confirmed Ended (Y/N)", "Confirmed."),
        ("Pending Legal/Complaint/Incident Hold Checked (Y/N)", "Confirmed clear."),
        ("MS Authorisation / Date", "Approval."),
        ("Method / Two Persons Present", "How destroyed and witnessed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.5")],
    column_headers=["Batch Description / Record Type", "Retention Period Confirmed Ended (Y/N)", "Pending Legal/Complaint/Incident Hold Checked (Y/N)", "MS Authorisation / Date", "Method / Two Persons Present"],
    worked_example_row=["WORKED EXAMPLE — Out-patient records, 2015 batch", "Y", "Y — no holds found", "Dr. Rao (MS) — 10-Mar-2026", "Shredded; Medical Records Officer + Quality Coordinator present"],
), "destruction_authorisation_completion_record")

# ============================================================== IMS.6 ====
IMS6 = SOPSpecV2(
    sop_no="SOP-IMS.6",
    title="Regular Review of Medical Records",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» reviews its own medical "
        "records on a planned schedule, using a genuinely representative "
        "sample of both active and discharged patients, reviewed by "
        "named individuals against a fixed list of parameters, with "
        "every deficiency the review finds actually tracked through to "
        "a corrective or preventive action."
    ),
    purpose_trigger=(
        "A record review happens only in the week before an "
        "accreditation assessment, using whichever files look the most "
        "complete -- which tells this hospital nothing real about how "
        "its records actually look the rest of the year. This SOP is "
        "what makes the review a genuine, ongoing check, not a pre-"
        "assessment performance."
    ),
    purpose_why=(
        "We do this because a medical record's quality is not "
        "something to discover for the first time during an "
        "accreditation visit -- regular review is what catches a "
        "recurring documentation gap while it is still a training fix, "
        "not a pattern spanning years of records."
    ),
    purpose_text=(
        "To define how «Hospital Name» reviews medical records "
        "periodically, using a representative sample of both active "
        "and discharged patients based on statistical principles, "
        "conducted by identified individuals, based on identified "
        "parameters, and undertakes appropriate corrective and "
        "preventive action on deficiencies the review finds."
    ),
    scope_why=(
        "so the named reviewers, the Quality Coordinator and every "
        "treating team know this review happens on a fixed calendar, "
        "not only when an assessment is approaching."
    ),
    scope_text=(
        "Applies to every medical record at «Hospital Name» and to the "
        "named reviewers, the Quality Coordinator, the Medical Records "
        "Officer and the Medical Superintendent. It covers how the "
        "periodic review itself is planned, sampled, conducted and "
        "acted on. It does not cover the medical-record structure and "
        "authentication requirements being reviewed against, or the "
        "wider quality-improvement programme and clinical audit system "
        "-- each of those is set out in its own separate SOP, and "
        "findings from this review feed that wider programme without "
        "replacing it."
    ),
    responsibility_why=(
        "a review that is not planned on a calendar, sampled by a fixed "
        "method, and conducted by named people drifts into reviewing "
        "whichever records happen to be convenient -- which defeats the "
        "entire purpose of reviewing at all."
    ),
    responsibilities=[
        ("Medical Superintendent", "Names the reviewers in writing; receives root-cause-analysis reports for recurring deficiencies."),
        ("Quality Coordinator", "Holds the review calendar and the parameter list; tracks CAPA to closure; reports aggregate findings to the quality programme quarterly."),
        ("Named Reviewers (Quality Coordinator, Medical Records Officer, one treating doctor who did not write the sampled record)", "Conduct the review against the fixed parameter list each cycle."),
        ("Treating Team", "Completes immediate corrections identified by the review."),
    ],
    items=[
        PlainItem(
            heading="Review medical records on a fixed, planned schedule — not only before an assessment",
            why=(
                "A review that only ever happens the week before an "
                "assessment shows this hospital what it wants an "
                "assessor to see, not what its records actually look "
                "like the rest of the year."
            ),
            body=[
                "Medical records are reviewed periodically.",
                "The review is conducted «monthly». The «Quality "
                "Coordinator» holds the review calendar. A missed "
                "month is recorded as a non-conformity and made up in "
                "the following period -- it is never simply skipped.",
                "\"Periodically\" means a planned interval, decided in "
                "advance, not an exercise run only when an assessment "
                "is approaching.",
            ],
            oe_code="IMS.6.a",
        ),
        PlainItem(
            heading="Sample both active and discharged records, drawn by a method that cannot be gamed",
            why=(
                "A sample of only the most complete-looking files, or "
                "only one department, tells this hospital what it "
                "wants to hear -- a genuinely representative sample is "
                "the only kind that tells the truth."
            ),
            body=[
                "The review uses a representative sample of both "
                "active and discharged patients, based on statistical "
                "principles.",
                "Every review cycle draws from both: active records, "
                "for patients currently admitted or currently under "
                "care; and discharged records, including deaths and "
                "transfers-out.",
                "The sample is drawn using «systematic sampling from "
                "the unique-identifier list, or another documented "
                "method that does not let the reviewer pick favourite "
                "files». The sample size is «at least ten records per "
                "month, or all records if fewer than ten were opened "
                "in the period», with both active and discharged "
                "records represented.",
                "A sample of only complete-looking files, or of one "
                "department only, is not representative, and does not "
                "satisfy this requirement.",
            ],
            oe_code="IMS.6.b",
        ),
        PlainItem(
            heading="Have named individuals conduct the review — never an unnamed \"quality team\"",
            why=(
                "\"The quality team reviewed it\" tells this hospital "
                "nothing about who actually looked, whether they were "
                "qualified to judge what they were looking at, or "
                "whether a reviewer ever marked their own work."
            ),
            body=[
                "The review is conducted by identified individuals.",
                "The Medical Superintendent names the reviewers in "
                "writing. Reviewers are «the Quality Coordinator, the "
                "Medical Records Officer, and at least one treating "
                "doctor who did not write the sampled record». Names, "
                "designations and the period of appointment are "
                "recorded.",
                "A person never reviews a record they themselves "
                "wrote. The named reviewer group meets «monthly» to "
                "confirm the sample, the findings, and the corrective "
                "and preventive action.",
                "\"Identified\" means named -- not an unnamed group "
                "such as \"the quality team\".",
            ],
            oe_code="IMS.6.c",
        ),
        PlainItem(
            heading="Review against a fixed, identified list of parameters — not whatever the reviewer happens to notice",
            why=(
                "Reviewing against whatever catches a reviewer's eye on "
                "the day produces different results from one month to "
                "the next, for reasons that have nothing to do with "
                "whether the records actually improved."
            ),
            body=[
                "The review of records is based on identified "
                "parameters.",
                "The parameter list is approved by the Medical "
                "Superintendent and held by the Quality Coordinator. "
                "It includes, at minimum: the unique identifier is "
                "present; contents are complete, up-to-date and "
                "chronological; the author is identifiable and every "
                "entry is named, signed, dated and timed; only "
                "authorised abbreviations are used; the continuity "
                "items this hospital requires -- admission reason, "
                "diagnosis, plan, assessments, investigations, "
                "procedures, care provided -- are present; a discharge-"
                "summary copy or, in death, a cause-of-death "
                "certificate copy is present; and transfer details are "
                "present where applicable.",
                "Each sampled record is scored against this same list. "
                "Parameters are never invented on the day of the "
                "review.",
            ],
            oe_code="IMS.6.d",
        ),
        PlainItem(
            heading="Track every deficiency the review finds through to a real fix",
            why=(
                "A deficiency that is noted in a review report and "
                "never followed up is no different, in practice, from "
                "a review that was never done at all."
            ),
            body=[
                "Appropriate corrective and preventive action is "
                "undertaken on the deficiencies the review points out.",
                "Every deficiency is logged: the record identifier, "
                "which parameter failed, who will act, the due date, "
                "and when it is closed. An immediate correction -- "
                "completing a missing signature, filing a missing "
                "copy -- is done by the treating team. A preventive "
                "action -- re-briefing a department, changing a form, "
                "adding a prompt in the electronic health record -- is "
                "decided by the review committee.",
                "The «Quality Coordinator» tracks every corrective and "
                "preventive action to closure. The same parameter "
                "failing again in «two consecutive months» triggers a "
                "root-cause analysis and a report to the Medical "
                "Superintendent, rather than being logged again as if "
                "it were new.",
                "Aggregate findings -- the deficiency rate by parameter "
                "-- are reported to this hospital's wider quality "
                "programme «quarterly», as an input. This review does "
                "not replace the hospital's own clinical-audit system; "
                "it feeds it.",
            ],
            oe_code="IMS.6.e",
            boundary=[
                "The wider quality-improvement programme and clinical-audit system are owned by PSQ.1 and PSQ.3; this step owns the medical-record review itself and feeds its aggregate findings into that programme.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the IMS.6 Records folder).",
    related_documents=[
        "Hospital's Complete and Accurate Medical Record SOP (IMS.2)",
        "Hospital's Medical Record Reflects Continuity of Care SOP (IMS.3)",
        "Hospital's Patient-Safety Programme and Quality Improvement Programme SOP (PSQ.1)",
        "Hospital's Clinical Audit and Quality Improvement Programmes SOP (PSQ.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a review month is "
        "missed and not made up, if a reviewer is found to have "
        "reviewed their own record, or if a related policy named above "
        "in this chapter is revised."
    ),
    full_reference_list=[
        NABH_IMS_CITE.format(code="IMS.6"),
    ],
)

SOPS.append(("SOP_IMS.6.a_to_e_regular_review_medical_records.docx", IMS6))

# ---- IMS.6 Records -------------------------------------------------
_add("IMS.6", 1, RecordSpec(
    oe_code="IMS.6.a",
    oe_requirement="Medical records are reviewed periodically.",
    record_title="IMS.6 Record 01 — Medical-record review calendar and non-conformity log",
    what_is_this="This record is the proof the review actually happened every planned month, and that a missed month was actually logged as a non-conformity and made up -- not quietly skipped.",
    real_example="The 2026 calendar shows reviews completed January through March on schedule; April's review is logged as missed due to a staffing gap and made up in the first week of May.",
    why_nabh_asks="A review that only ever happens the week before an assessment shows this hospital what it wants an assessor to see, not what its records actually look like the rest of the year.",
    how_to_fill=[
        ("Month", "Which month."),
        ("Review Completed (Y/N)", "Confirmed."),
        ("If Missed — Reason / Made Up By", "What happened and when caught up."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.6")],
    column_headers=["Month", "Review Completed (Y/N)", "If Missed — Reason / Made Up By"],
    worked_example_row=["WORKED EXAMPLE — April 2026", "N — missed", "Staffing gap; made up 05-May-2026"],
), "medical_record_review_calendar_non_conformity_log")

_add("IMS.6", 2, RecordSpec(
    oe_code="IMS.6.b",
    oe_requirement="The review uses a representative sample of both active and discharged patients, based on statistical principles.",
    record_title="IMS.6 Record 02 — Sample-selection record",
    what_is_this="This record is the proof the sample was actually drawn by a documented method covering both active and discharged records -- not hand-picked complete-looking files.",
    real_example="March's sample of 12 records is drawn by systematic sampling from the unique-identifier list, with 7 discharged and 5 active records represented.",
    why_nabh_asks="A sample of only the most complete-looking files, or only one department, tells this hospital what it wants to hear -- a genuinely representative sample is the only kind that tells the truth.",
    how_to_fill=[
        ("Review Month", "Which cycle."),
        ("Sampling Method", "Systematic or other documented method."),
        ("Sample Size / Active vs Discharged", "Breakdown."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.6")],
    column_headers=["Review Month", "Sampling Method", "Sample Size / Active vs Discharged"],
    worked_example_row=["WORKED EXAMPLE — March 2026", "Systematic sampling from unique-identifier list", "12 total — 5 active, 7 discharged"],
), "sample_selection_record")

_add("IMS.6", 3, RecordSpec(
    oe_code="IMS.6.c",
    oe_requirement="The review is conducted by identified individuals.",
    record_title="IMS.6 Record 03 — Named-reviewer appointment record",
    what_is_this="This record is the proof the reviewers are actually named in writing by the Medical Superintendent, and that no reviewer ever reviewed a record they themselves wrote.",
    real_example="The appointment record names the Quality Coordinator, the Medical Records Officer and Dr. Mehta as reviewers for 2026, with Dr. Mehta's own-record conflict checked and found clear each cycle.",
    why_nabh_asks="\"The quality team reviewed it\" tells this hospital nothing about who actually looked, whether they were qualified to judge what they were looking at, or whether a reviewer ever marked their own work.",
    how_to_fill=[
        ("Reviewer Name / Designation", "Who."),
        ("Appointment Period", "When appointed."),
        ("Own-Record Conflict Checked Each Cycle (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.6")],
    column_headers=["Reviewer Name / Designation", "Appointment Period", "Own-Record Conflict Checked Each Cycle (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — Dr. S. Mehta, treating doctor", "Jan-Dec 2026", "Y"],
), "named_reviewer_appointment_record")

_add("IMS.6", 4, RecordSpec(
    oe_code="IMS.6.d",
    oe_requirement="The review of records is based on identified parameters.",
    record_title="IMS.6 Record 04 — Parameter-scored review sheet",
    what_is_this="This record is the proof each sampled record was actually scored against the same fixed, approved parameter list -- not judged against whatever the reviewer happened to notice that day.",
    real_example="A sampled record scores pass on 6 of 7 parameters, failing only on \"authorised abbreviations only\" where one unlisted abbreviation is found.",
    why_nabh_asks="Reviewing against whatever catches a reviewer's eye on the day produces different results from one month to the next, for reasons that have nothing to do with whether the records actually improved.",
    how_to_fill=[
        ("Record Sampled", "Which record."),
        ("Parameter List Version", "Which approved version used."),
        ("Parameters Passed / Failed", "Score detail."),
        ("Reviewer / Date", "Who scored it, when."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.6")],
    column_headers=["Record Sampled", "Parameter List Version", "Parameters Passed / Failed", "Reviewer / Date"],
    worked_example_row=["WORKED EXAMPLE — UID-00701", "v2.0 (approved Jan-2026)", "6 of 7 passed; failed — unauthorised abbreviation found", "Medical Records Officer — 14-Mar-2026"],
), "parameter_scored_review_sheet")

_add("IMS.6", 5, RecordSpec(
    oe_code="IMS.6.e",
    oe_requirement="Appropriate corrective and preventive measures are undertaken on the deficiencies pointed out in the review.",
    record_title="IMS.6 Record 05 — Deficiency CAPA tracking log",
    what_is_this="This record is the proof a deficiency the review found was actually tracked to a named owner and a closure date -- and that a deficiency repeating for two months actually triggered a root-cause analysis rather than being logged again as new.",
    real_example="An unauthorised-abbreviation deficiency is assigned to the ward in-charge for correction and staff re-briefing, closed within two weeks; the same parameter failing again the following month triggers an RCA reported to the Medical Superintendent.",
    why_nabh_asks="A deficiency that is noted in a review report and never followed up is no different, in practice, from a review that was never done at all.",
    how_to_fill=[
        ("Record / Parameter Failed", "What and where."),
        ("Immediate Correction / Owner", "Quick fix and who."),
        ("Preventive Action / Owner / Due Date", "Longer-term fix."),
        ("Closure Date / Recurrence (2 Consecutive Months, Y/N)", "Tracked to closure."),
    ],
    verified_sources=[NABH_IMS_CITE.format(code="IMS.6")],
    column_headers=["Record / Parameter Failed", "Immediate Correction / Owner", "Preventive Action / Owner / Due Date", "Closure Date / Recurrence (2 Consecutive Months, Y/N)"],
    worked_example_row=["WORKED EXAMPLE — UID-00701 / authorised abbreviations", "Entry corrected by writer same day", "Ward re-briefing; Ward In-Charge / 28-Mar-2026", "28-Mar-2026 / N — no recurrence"],
), "deficiency_capa_tracking_log")


def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path}")

    manifest: list[dict] = []
    for fname, spec in SOPS:
        manifest.append({
            "file": fname,
            "document_type": "sop",
            "standard_code": spec.sop_no.replace("SOP-", ""),
            "title": f"SOP — {spec.title} ({spec.sop_no.replace('SOP-', '')})",
        })
        sop_records = [r for r in RECORDS if r[0] == spec.sop_no.replace("SOP-", "")]
        for sop_code, idx, slug, rspec in sorted(sop_records, key=lambda r: r[1]):
            rel_path = f"Records/{sop_code}_Record_{idx:02d}_{slug}.docx"
            out_path = RECORDS_ROOT.parent / rel_path
            build_record(rspec, out_path)
            print(f"built {out_path}")
            manifest.append({
                "file": rel_path,
                "document_type": "record",
                "standard_code": sop_code,
                "record_index": idx,
                "title": rspec.record_title.split("—", 1)[-1].strip(),
            })

    manifest_path = OUT_ROOT / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {manifest_path} ({len(manifest)} entries)")


if __name__ == "__main__":
    main()
