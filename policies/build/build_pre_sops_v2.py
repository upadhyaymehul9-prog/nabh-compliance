# -*- coding: utf-8 -*-
"""Builds the 6 PRE (Patient Rights and Education) SOPs -- plus their Records
and manifest.json -- in the plain-body + audit-appendix format used for
FMS, ROM, AAC, HRM, COP and MOM (2026-10-12).

Like MOM, NO SOP/Record pack existed for PRE before this script:
policies/build/sop_record_masters/PRE/ is created fresh here. The content
is not invented -- it is drawn directly from the SHCO 3rd Edition PRE
Master Policy pipeline that was already built and approved for this
hospital (policies/drafts/pre{1..6}_v2_draft.json, masters at
policies/build/masters/PRE.{1..6}_v2_master.docx), which carries the
correct SHCO scope (6 standards, 39 OEs across PRE.1-PRE.6 -- NOT the HCO
6th-edition PRE inventory, which is 8 standards / 52 OEs and is explicitly
a different programme per policies/source/hco6_pre_chapter_notes.md), the
real statutory citations, and the already-approved responsibility/record
mapping. This script recasts that content into the plain-body-with-Why-
lines + appendix template -- it is adaptation of already-approved
material into a new template, not fresh authorship of requirements.

Source of truth for every fact below: policies/drafts/pre{N}_v2_draft.json
(fields: scope, policy_statement, procedure_steps, responsibility,
oe_mapping, references_text, stop_work). Nothing here was invented beyond
template prose (the "Why:" framing lines, which restate the same
consequence already stated in each draft's own text).

Writes:
  policies/build/sop_record_masters/PRE/SOP_PRE.N...docx   (6 files)
  policies/build/sop_record_masters/PRE/Records/PRE.N_Record_NN_*.docx
  policies/build/sop_record_masters/PRE/manifest.json
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

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "PRE"
RECORDS_ROOT = OUT_ROOT / "Records"

NABH_PRE_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Patient Rights and Education chapter, standard {code}."
)

MHCA_SRC = (
    "Government of India. (2017). [The Mental Healthcare "
    "Act, 2017](https://www.indiacode.nic.in/handle/123456789/2249) "
    "(Act No. 10 of 2017) — governs who may consent on behalf of a "
    "person with mental illness as defined in the Act, including the "
    "nominated representative and advance directive provisions."
)
NMC_ACT_SRC = (
    "Government of India. (2019). [The National Medical Commission "
    "Act, 2019](https://www.indiacode.nic.in/handle/123456789/11820) "
    "(Act No. 30 of 2019) — requires a registered medical practitioner "
    "to obtain informed consent consistent with professional practice."
)
READER_COMPLAINT_SRC = (
    "Reader, T. W., Gillespie, A., & Roberts, J. (2014). Patient complaints "
    "in healthcare systems: a systematic review and coding taxonomy. "
    "[BMJ Quality & Safety, 23(8), 678–689]"
    "(https://qualitysafety.bmj.com/content/23/8/678) — the complaint "
    "taxonomy framework this hospital's complaint categories draw on; not "
    "a pasted coding protocol."
)
WHO_RIGHTS_SRC = (
    "World Health Organization. (2023, December 1). [Human rights and "
    "health](https://www.who.int/news-room/fact-sheets/detail/human-rights-and-health) "
    "(Fact sheet). Geneva: WHO — the framework context for why a "
    "documented rights set exists; not pasted as this hospital's "
    "charter."
)
OLEJARCZYK_YOUNG_SRC = (
    "Olejarczyk, J. P., & Young, M. (2021). Patient Rights and Ethics. "
    "In StatPearls. StatPearls Publishing — context for rights as an "
    "ethical and clinical practice, not a protocol."
)
KUMAR_CONSENT_SRC = (
    "Kumar, A., et al. (2015). Informed consent: Issues and challenges. "
    "Journal of Advanced Pharmaceutical Technology & Research — a "
    "framework for consent practice, not a pasted protocol."
)
NANDIMATH_SRC = (
    "Nandimath, O. V. (2009). Consent and medical treatment: The legal "
    "paradigm in India. Indian Journal of Urology, 25(3), 343–347 — "
    "a framework for statutory norms around consent, not a pasted protocol."
)
HA_LONGNECKER_SRC = (
    "Ha, J. F., & Longnecker, N. (2010). Doctor-patient communication: "
    "a review. The Ochsner Journal, 10(1), 38–43 — the doctor-patient "
    "communication framework referred to in staff training; not a "
    "pasted protocol."
)
MARCUS_EDUCATE_SRC = (
    "Marcus, C. (2014). Strategies to improve the quality of verbal "
    "patient and family education: a review of the literature and "
    "creation of the EDUCATE model. Health Psychology and Behavioral "
    "Medicine, 2(1), 482–495 — the verbal-education framework referred "
    "to in staff training; not a pasted protocol."
)
NOURI_RUDD_SRC = (
    "Nouri, S. S., & Rudd, R. E. (2015). Health literacy in the \"oral "
    "exchange\": An important element of patient-provider communication. "
    "Patient Education and Counseling, 98(5), 565–571 — an oral health "
    "literacy framework referred to in staff training; not a pasted "
    "protocol."
)
BADARUDEEN_SABHARWAL_SRC = (
    "Badarudeen, S., & Sabharwal, S. (2010). Assessing readability of "
    "patient education materials: current role in orthopaedics. "
    "Clinical Orthopaedics and Related Research, 468(10), 2572–2580 — "
    "a readability framework referred to in staff training; not a "
    "pasted protocol."
)

SOPS: list[tuple[str, SOPSpecV2]] = []
RECORDS: list[tuple[str, int, str, RecordSpec]] = []


def _add(sop_code: str, idx: int, spec: RecordSpec, slug: str) -> None:
    RECORDS.append((sop_code, idx, slug, spec))


# ============================================================== PRE.1 ====
PRE1 = SOPSpecV2(
    sop_no="SOP-PRE.1",
    title="Patient and Family Rights and Responsibilities",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» documents a current set of "
        "patient and family rights and responsibilities, displays and "
        "explains them to every patient and family at entry, actively "
        "promotes them in the course of care rather than only on a wall, "
        "protects them day to day, gives patients and families a way to "
        "report a violation that does not route only to the person "
        "accused, and has top leadership actually review those reports "
        "and act."
    ),
    purpose_trigger=(
        "A patient is examined behind a thin curtain while a diagnosis is "
        "discussed within earshot of the next bed. This SOP is what makes "
        "sure that patient already knew they had a right to privacy and "
        "dignity, and that someone above the person who breached it finds "
        "out and fixes the pattern -- not a one-off apology nobody tracks."
    ),
    purpose_why=(
        "We do this because a rights charter that lives only in the "
        "quality office protects no one, and a violation that can only be "
        "reported to the very person accused of it will almost never be "
        "reported at all."
    ),
    purpose_text=(
        "To define how «Hospital Name» documents, displays and makes "
        "patients and families aware of their rights and responsibilities; "
        "actively promotes those rights in the course of care; protects "
        "them; gives a mechanism to report a violation; and ensures top "
        "leadership monitors violations and acts on them."
    ),
    scope_why="so entry, ward care and leadership review all work from the same current rights set, not separate private understandings of what patients are owed.",
    scope_text=(
        "Applies at every point a patient or family enters or is cared "
        "for at «Hospital Name»: registration and front office, "
        "out-patient, emergency, day-care, in-patient wards, intensive or "
        "high-dependency areas where they exist, and the operation "
        "theatre insofar as rights are displayed and staff must protect "
        "them. It binds front-office and registration staff who display "
        "and explain rights at entry; treating doctors and nurses who "
        "protect rights during care; the Patient Rights Officer who holds "
        "the documented set, display, awareness method, promotion method "
        "and violation-report route; billing and front-desk staff who "
        "must not withhold cost information that is a patient right; top "
        "leadership who review violations; and the Quality Coordinator "
        "who audits records. It covers documentation, display and "
        "awareness; active promotion; protection; a violation-report "
        "mechanism; and leadership monitoring with corrective and "
        "preventive action. This SOP owns that a current documented set "
        "exists, is displayed, is made known, is promoted and is "
        "protected -- not the content of the rights list itself, how "
        "consent is obtained, how education is given, how costs are "
        "explained, or how complaints are redressed, each of which is "
        "owned by a sibling SOP in this chapter or elsewhere."
    ),
    responsibility_why="a rights charter nobody at the top ever reviews is a poster, not a governance system -- the point of leadership review is that a repeated violation gets caught and fixed, not quietly absorbed.",
    responsibilities=[
        ("Medical Superintendent (Head of the Institution)", "Is accountable that this SOP is issued, resourced and followed; reviews the violation log and signs leadership corrective and preventive action."),
        ("Patient Rights Officer", "Authors and keeps current the documented set, display, awareness method, promotion method and violation-report mechanism; receives violation reports unless the alleged violator is this officer, in which case the Medical Superintendent receives them; prepares the quarterly violation summary for leadership review."),
        ("Front-office / Registration In-Charge", "Makes patients and families aware at entry; keeps display boards current and readable at points of entry."),
        ("Nursing Superintendent", "Ensures ward entrances display the set and that nurses protect rights at the bedside; holds signed staff acknowledgements with the induction record."),
        ("Treating Doctors and Ward Nurses", "Protect the rights in the documented set during examination, treatment and conversation; refer to rights when consent, refusal, complaint or cost is discussed."),
        ("Billing / Front-desk Lead", "Does not withhold cost information that is a patient right."),
        ("Quality Coordinator", "Audits this SOP quarterly and tracks corrective and preventive action to closure."),
    ],
    items=[
        PlainItem(
            heading="Document, display and make patients and families aware at entry",
            why="A rights charter that only the quality office has ever seen, or a board behind the clerk that patients never pass, protects no one -- a right a patient was never told about is not a right they can exercise.",
            body=[
                "Patient and family rights and responsibilities are "
                "documented, displayed, and patients and families are "
                "made aware of the same. All three acts matter together "
                "-- none substitutes for the others.",
                "The documented set is held by the Patient Rights "
                "Officer and matches the current rights list. "
                "Responsibilities are what this hospital asks of the "
                "patient and family during care -- for example, giving "
                "an accurate history, keeping agreed appointments, and "
                "treating staff without violence. The set is dated, "
                "version-controlled, and withdrawn from display when "
                "superseded.",
                "Display uses boards, printed material and any online "
                "presence this hospital maintains, in «Hindi and "
                "English», at «the registration counter, the emergency "
                "waiting area, and each in-patient ward entrance». A "
                "board only in a language patients do not use is not "
                "display for those patients.",
                "Awareness at entry is carried out by «registration "
                "staff and the admitting nurse» at out-patient first "
                "contact, emergency arrival and in-patient admission. "
                "The staff member names the language used, gives time "
                "for questions, and records the date and their name -- "
                "not only a signature. An unconscious or severely "
                "distressed arrival is made aware as soon as the "
                "patient or accompanying family can receive it; the "
                "delay and reason are recorded.",
            ],
            oe_code="PRE.1.a",
            boundary=[
                "The content of the rights list itself is owned by the sibling policy on Beliefs, Values and Decision-Making (PRE.2); this SOP owns that a current documented set exists, is displayed, is made known, is promoted and is protected.",
                "Registration and the unique identification number are owned by the Registration, Admission and Transfer SOP (AAC.2); awareness of rights happens at or beside registration but does not generate the number.",
            ],
        ),
        PlainItem(
            heading="Actively promote rights and responsibilities in the course of care",
            why="A poster read once at induction and never mentioned again is not promotion -- a right only becomes real for a patient when it is named at the moment it actually matters: before consent, during a refusal, when a complaint is invited, when cost is explained.",
            body=[
                "Patient and family rights and responsibilities are "
                "actively promoted, meaning the set is used in the "
                "course of care, not only displayed on the wall at the "
                "door.",
                "Promotion to staff happens at induction and «once a "
                "year» after that. Staff are shown the documented set "
                "and the violation-report route. Ward briefings refer "
                "to rights when consent, refusal, a complaint or a cost "
                "question is about to arise.",
                "Promotion to patients and families happens after entry "
                "when a right is about to be exercised -- before "
                "consent, when a refusal is discussed, when a complaint "
                "is invited, when cost is explained. Referring to the "
                "right by name is promotion; a once-a-year seminar with "
                "no ward follow-up is not.",
            ],
            oe_code="PRE.1.b",
            boundary=[
                "This step does not rewrite the informed-consent method, the expected-cost explanation, or the complaint mechanism owned by sibling SOPs in this chapter -- it requires that those processes are spoken of as rights, not as favours.",
            ],
        ),
        PlainItem(
            heading="Protect patient and family rights day to day",
            why="Protection is not a quality slogan -- it is the daily discipline of not doing what the documented set forbids: not examining without privacy, not ignoring a refusal, not withholding the treating doctor's name, not punishing a complaint.",
            body=[
                "The organisation protects patient and family rights. "
                "Protection is the daily work of not doing what the "
                "documented set forbids.",
                "Treating doctors and nurses protect rights at the "
                "bedside. The Patient Rights Officer holds a short "
                "written expectation of protection in each care setting "
                "-- out-patient, emergency, ward and theatre reception.",
                "A failure of protection is a violation and is reported "
                "under the mechanism in the next step. Protection is "
                "how staff actually behave, not a separate document.",
            ],
            oe_code="PRE.1.c",
        ),
        PlainItem(
            heading="Give a mechanism to report a rights violation that does not route only to the person accused",
            why="A report that can only be made to the very person alleged to have committed the violation is not a mechanism -- it is a dead end that teaches patients and staff that reporting is pointless.",
            body=[
                "The organisation has a mechanism to report a violation "
                "of patient and family rights. A patient, family member "
                "or staff member may report using «the complaint box, "
                "the patient-rights helpline number on the display "
                "board, or a written form at registration».",
                "Reports are received by the Patient Rights Officer. If "
                "the alleged violator is that officer, the report goes "
                "to the Medical Superintendent instead.",
                "Each report is logged with five pieces of information:",
                "1. Date.",
                "2. Reporter (name or \"anonymous\").",
                "3. The right said to be violated.",
                "4. A short statement.",
                "5. Who received it.",
                "A complaint that "
                "alleges a rights violation, wherever it is first "
                "lodged, also enters this violation log so the same "
                "facts reach leadership review.",
            ],
            oe_code="PRE.1.d",
            boundary=[
                "A complaint lodged through the feedback-and-complaint mechanism (PRE.6) that alleges a rights violation also enters this violation log; PRE.6 owns redressal of the complaint as a complaint, this SOP owns that the same facts reach leadership review.",
            ],
        ),
        PlainItem(
            heading="Leadership monitors violations and acts",
            why="A violation file nobody above the ward ever opens is not monitoring -- the point of leadership review is catching a repeated setting or a repeated right before it becomes a pattern no one noticed.",
            body=[
                "Violations of patient and family rights are monitored, "
                "analysed and acted on by top leadership. The Medical "
                "Superintendent reviews the violation log «quarterly» "
                "(four times a year).",
                "The review looks for repeated settings, repeated "
                "rights, and whether display or promotion failed. "
                "Findings produce dated corrective and preventive "
                "action with a named owner. An open action older than "
                "«thirty days» is escalated to the governing body or "
                "owner, where this hospital has one.",
                "A rights violation that never became a formal patient "
                "complaint still comes to this review -- the review "
                "does not depend on a complaint having been filed "
                "separately.",
            ],
            oe_code="PRE.1.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-5 (see the PRE.1 Records folder).",
    related_documents=[
        "Policy on Beliefs, Values and Involvement in Decision-Making (PRE.2)",
        "Hospital's Patient Feedback and Complaint Redressal SOP (PRE.6)",
        "Hospital's Registration, Admission and Transfer SOP (AAC.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a display gap, a "
        "violation report that could only reach the accused, or an open "
        "corrective action older than thirty days exposes a gap, or if "
        "the sibling PRE policies this SOP points to are revised."
    ),
    full_reference_list=[
        NABH_PRE_CITE.format(code="PRE.1"),
        WHO_RIGHTS_SRC,
        OLEJARCZYK_YOUNG_SRC,
    ],
)

SOPS.append(("SOP_PRE.1.a_to_e_patient_family_rights_responsibilities.docx", PRE1))

# ---- PRE.1 Records -------------------------------------------------
_add("PRE.1", 1, RecordSpec(
    oe_code="PRE.1.a",
    oe_requirement="Patient and family rights and responsibilities are documented, displayed, and they are made aware of the same.",
    record_title="PRE.1 Record 01 — Awareness-at-entry record",
    what_is_this="This record is the proof every patient or family was actually told their rights and responsibilities at entry, in a language they understand -- not handed a form to sign without explanation.",
    real_example="At admission, the registration clerk walks a patient's family through the displayed rights set in Hindi, answers a question about visiting hours, and records the date and her name.",
    why_nabh_asks="A right a patient was never told about is not a right they can exercise -- awareness at entry is what makes the documented set real rather than decorative.",
    how_to_fill=[
        ("Date/Time", "When awareness was given."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Entry Point", "Out-patient, emergency, or in-patient admission."),
        ("Language Used / Staff Name", "As given."),
        ("Delay (if any) / Reason", "For an unconscious or distressed arrival."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.1")],
    column_headers=["Date/Time", "Patient (Identifier 1) / UID (Identifier 2)", "Entry Point", "Language Used / Staff Name", "Delay (if any) / Reason"],
    worked_example_row=["WORKED EXAMPLE — 02-Jun-2026, 10:15 AM", "Sunita Rao / UID-00901", "In-patient admission", "Hindi / Registration Clerk P. Jadhav", "None"],
), "awareness_at_entry_record")

_add("PRE.1", 2, RecordSpec(
    oe_code="PRE.1.b",
    oe_requirement="Patient and family rights and responsibilities are actively promoted.",
    record_title="PRE.1 Record 02 — Staff induction and annual rights-briefing record",
    what_is_this="This record is the proof staff were actually briefed on the rights set and the violation-report route at induction and every year after -- not shown a poster once and never again.",
    real_example="A new nurse completes rights-and-responsibilities induction training within her first week, and existing staff attend the annual refresher.",
    why_nabh_asks="A right only becomes real for a patient when staff are the ones who name it at the moment it matters -- a staff member who was never briefed cannot promote what they do not know.",
    how_to_fill=[
        ("Staff Name / Role", "Who was briefed."),
        ("Briefing Type", "Induction or annual refresher."),
        ("Date", "When completed."),
        ("Topics Covered", "Rights set, violation-report route."),
        ("Signed Acknowledgement (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.1")],
    column_headers=["Staff Name / Role", "Briefing Type", "Date", "Topics Covered", "Signed Acknowledgement (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — Staff Nurse K. Fernandes", "Induction", "05-Jun-2026", "Rights set; violation-report route", "Y"],
), "staff_induction_annual_briefing_record")

_add("PRE.1", 3, RecordSpec(
    oe_code="PRE.1.c",
    oe_requirement="The organisation protects patient and family rights.",
    record_title="PRE.1 Record 03 — Bedside rights-protection audit sample",
    what_is_this="This record is the proof privacy, dignity and refusal were actually respected at the bedside when checked -- not assumed because no one complained.",
    real_example="A quarterly audit of ten random patient encounters confirms screens were used during examination and no diagnosis was discussed within earshot of other patients.",
    why_nabh_asks="Protection is the daily discipline of not doing what the documented set forbids -- an audit is how the hospital finds out whether that discipline is actually happening, not just assumed.",
    how_to_fill=[
        ("Audit Date", "Date of the audit."),
        ("Setting", "Out-patient, emergency, ward, or theatre reception."),
        ("Encounters Sampled", "Number checked."),
        ("Privacy/Dignity Respected (Y/N)", "Result."),
        ("Finding / Action (if any)", "Any defect and its fix."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.1")],
    column_headers=["Audit Date", "Setting", "Encounters Sampled", "Privacy/Dignity Respected (Y/N)", "Finding / Action (if any)"],
    worked_example_row=["WORKED EXAMPLE — 10-Jun-2026", "General ward", "10", "Y", "None"],
), "bedside_rights_protection_audit_sample")

_add("PRE.1", 4, RecordSpec(
    oe_code="PRE.1.d",
    oe_requirement="The organisation has a mechanism to report a violation of patient and family rights.",
    record_title="PRE.1 Record 04 — Rights-violation log",
    what_is_this="This record is the proof every reported violation was actually logged with who received it -- not handled quietly and left untraceable.",
    real_example="A family reports through the complaint box that a curtain was not drawn during an examination; the Patient Rights Officer logs it the same day.",
    why_nabh_asks="A report that goes nowhere traceable teaches patients and staff that reporting is pointless -- the log is what proves the mechanism actually receives and keeps reports.",
    how_to_fill=[
        ("Date", "When reported."),
        ("Reporter (Name or Anonymous)", "Who reported."),
        ("Right Said to Be Violated", "Which right."),
        ("Statement (Short)", "What happened."),
        ("Received By", "Patient Rights Officer, or Medical Superintendent if that officer is the one accused."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.1")],
    column_headers=["Date", "Reporter (Name or Anonymous)", "Right Said to Be Violated", "Statement (Short)", "Received By"],
    worked_example_row=["WORKED EXAMPLE — 12-Jun-2026", "Anonymous", "Privacy during examination", "Curtain not drawn during examination", "Patient Rights Officer"],
), "rights_violation_log")

_add("PRE.1", 5, RecordSpec(
    oe_code="PRE.1.e",
    oe_requirement="Violation of patient and family rights are monitored, analysed and corrective/preventive action taken by the top leadership of the organisation.",
    record_title="PRE.1 Record 05 — Quarterly leadership violation review and CAPA log",
    what_is_this="This record is the proof top leadership actually reviewed the violation log every quarter and produced dated corrective action with an owner -- not a file that sits untouched between audits.",
    real_example="The quarterly review finds two privacy violations in the same ward; the Medical Superintendent orders a refresher briefing for that ward's nursing staff, tracked to closure.",
    why_nabh_asks="A violation file nobody above the ward ever opens cannot catch a repeated pattern -- leadership review is what turns an isolated incident into a system fix before it happens again.",
    how_to_fill=[
        ("Review Quarter", "Which quarter."),
        ("Violations Reviewed", "Number in the log."),
        ("Pattern Found (if any)", "Repeated setting or right."),
        ("CAPA / Owner / Due Date", "Action decided."),
        ("Escalated (Y/N, if open >30 days)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.1")],
    column_headers=["Review Quarter", "Violations Reviewed", "Pattern Found (if any)", "CAPA / Owner / Due Date", "Escalated (Y/N, if open >30 days)"],
    worked_example_row=["WORKED EXAMPLE — Q2 2026", "2", "Privacy violations, same ward", "Refresher briefing; Nursing Superintendent / 30-Jun-2026", "N"],
), "quarterly_leadership_violation_review_capa_log")


# ============================================================== PRE.2 ====
PRE2 = SOPSpecV2(
    sop_no="SOP-PRE.2",
    title="Beliefs, Values and Involvement in Decision-Making",
    purpose_plain=(
        "This SOP sets out the sixteen rights and involvement elements "
        "«Hospital Name» exercises in the course of care -- respecting "
        "values, beliefs and spiritual needs; dignity, privacy, protection "
        "and confidentiality; refusal and a second opinion; the pointer to "
        "informed consent; the pointer to complaint and cost rights; "
        "access to records and control over who is told what; being told "
        "the treating doctor's name, the care plan and progress; being "
        "explained proposed care and expected results; and being "
        "consulted on the care plan with multidisciplinary counselling "
        "when appropriate."
    ),
    purpose_trigger=(
        "A family member is told, over the patient's own objection, "
        "exactly what is wrong with the patient. This SOP is what makes "
        "sure the patient's own choice about who is told what is actually "
        "the one that is followed -- not whichever relative asks loudest."
    ),
    purpose_why=(
        "We do this because a right that is only printed on a charter in "
        "the quality office protects no one -- these sixteen elements "
        "have to be exercised in the room, at the bedside, in the "
        "conversation, not only displayed on a board at the door."
    ),
    purpose_text=(
        "To define the rights and involvement elements «Hospital Name» "
        "includes in patient and family rights and exercises in the "
        "course of care, and to describe how the patient and/or family "
        "are involved in decision-making, including the care plan and "
        "multidisciplinary counselling when appropriate."
    ),
    scope_why="so every patient-facing right in this list is exercised the same way by every member of staff, not interpreted differently ward to ward.",
    scope_text=(
        "Applies to every patient and family at «Hospital Name» and to "
        "every staff member who must respect the rights listed here: "
        "registration, treating doctors, nurses, the Patient Rights "
        "Officer, billing staff where cost is a right, and the "
        "counsellor where multidisciplinary counselling is provided. It "
        "covers the sixteen rights and involvement elements this SOP "
        "names. It does not cover how the set is displayed, how consent "
        "is obtained, how expected costs are explained, or how "
        "complaints are redressed -- each of those is owned by a sibling "
        "SOP in this chapter."
    ),
    responsibility_why="a right that is listed but never exercised in the room is a charter, not a practice -- the point of naming who is responsible for each element is that someone is actually accountable for it happening.",
    responsibilities=[
        ("Medical Superintendent (Head of the Institution)", "Is accountable that these rights are exercised in care, not only displayed."),
        ("Patient Rights Officer", "Keeps the documented rights set aligned with the display SOP and holds the methods for identifying and responding to each element below."),
        ("Front-office / Registration In-Charge", "Helps identify values, beliefs and language needs at entry."),
        ("Treating Doctors and Ward Nurses", "Protect dignity, privacy, confidentiality, refusal, consultation and the pointers to consent, costs and complaints."),
        ("Counsellor (where provided)", "Provides multidisciplinary counselling when appropriate."),
        ("Billing / Front-desk Lead", "Does not withhold cost information that is a patient right."),
        ("Quality Coordinator", "Audits this SOP quarterly and tracks corrective action when the same right is not exercised twice in the same setting."),
    ],
    items=[
        PlainItem(
            heading="Respect values, beliefs, special preferences, culture and spiritual needs",
            why="A patient whose spiritual request is dismissed as \"not medical\" is being told their beliefs do not count in the one place they most need to -- while they are unwell and dependent on this hospital's care.",
            body=[
                "Patient and family rights include respecting values and "
                "beliefs, any special preferences, cultural needs, and "
                "responding to requests for spiritual needs.",
                "Registration staff and nurses ask at or after entry in "
                "«Hindi and English», or the language the patient uses. "
                "Spiritual requests are passed to «the ward nurse or the "
                "counsellor», not ignored.",
            ],
            oe_code="PRE.2.a",
            technical_sources=[WHO_RIGHTS_SRC],
        ),
        PlainItem(
            heading="Respect dignity and privacy during examination, procedures and treatment",
            why="A corridor discussion of a diagnosis, overheard by the next patient in line, is a defect that costs a patient their dignity for no clinical reason at all.",
            body=[
                "Patient and family rights include respect for personal "
                "dignity and privacy during examination, procedures and "
                "treatment.",
                "Treating doctors and nurses protect dignity and privacy "
                "with screens, closed doors and low voices. A corridor "
                "discussion of diagnosis is a defect.",
            ],
            oe_code="PRE.2.b",
        ),
        PlainItem(
            heading="Protect from neglect or abuse",
            why="A suspicion of neglect or abuse that is noticed and then quietly let go is the moment that allows it to happen again to the next patient.",
            body=[
                "Patient and family rights include protection from "
                "neglect or abuse. A suspicion is reported through the "
                "violation-report mechanism as soon as it is noticed.",
            ],
            oe_code="PRE.2.c",
            boundary=[
                "A suspicion of neglect or abuse is reported as a rights violation under the Patient and Family Rights and Responsibilities SOP (PRE.1.d).",
            ],
        ),
        PlainItem(
            heading="Treat patient information as confidential",
            why="Patient information left open at a public desk is a breach a patient never consented to and often never even learns happened.",
            body=[
                "Patient and family rights include treating patient "
                "information as confidential. Patient information is "
                "not left open at a public desk, and conversations about "
                "a patient's condition are kept out of earshot of other "
                "patients and visitors.",
            ],
            oe_code="PRE.2.d",
            boundary=[
                "How the clinical record itself is kept confidential as a stored file is an Information Management System matter; this right is about information being treated as confidential in the course of care.",
            ],
        ),
        PlainItem(
            heading="Receive a refusal of treatment without punishment",
            why="A patient who is made to feel punished for refusing a treatment will stop telling staff the truth about what they will and will not accept -- which is far more dangerous than the refusal itself.",
            body=[
                "Patient and family rights include the refusal of "
                "treatment. Refusal is received without punishment and "
                "recorded as refusal, not chased as an unsigned form.",
            ],
            oe_code="PRE.2.e",
            boundary=[
                "The informed-consent policy (PRE.3) records that consent was not given when a patient refuses.",
            ],
        ),
        PlainItem(
            heading="Facilitate a right to seek an additional opinion",
            why="A patient denied even the chance to ask someone else is a patient whose trust in this hospital was never actually earned, only assumed.",
            body=[
                "Patient and family rights include a right to seek an "
                "additional opinion regarding clinical care. An "
                "additional opinion is facilitated as this hospital can "
                "arrange -- «a referral letter and appointment where the "
                "hospital has a tie-up; otherwise an honest statement of "
                "what the hospital cannot arrange». This hospital does "
                "not print a named second-hospital list as a mandatory "
                "requirement.",
            ],
            oe_code="PRE.2.f",
        ),
        PlainItem(
            heading="Carry the right that informed consent is obtained before named high-risk acts",
            why="A patient who is never told that consent is their right, and not merely a form to sign, has no way of knowing they could have asked questions or said no.",
            body=[
                "Patient and family rights include informed consent "
                "before the transfusion of blood and blood components, "
                "anaesthesia, surgery, initiation of any research "
                "protocol and any other invasive or high-risk procedure "
                "or treatment. Staff name this right when consent is "
                "about to be taken.",
            ],
            oe_code="PRE.2.g",
            boundary=[
                "This is a pointer only. The consent method is owned by the Informed Consent SOP (PRE.3); that consent actually happened before transfusion, sedation, anaesthesia or surgery is owned by the relevant Care of Patients SOPs (COP.5, COP.9, COP.10, COP.11).",
            ],
        ),
        PlainItem(
            heading="Carry the right to complain and to know how to voice a complaint",
            why="A patient who does not know a complaint route exists will simply leave dissatisfied and never tell this hospital why -- losing the one chance to fix the problem for the next patient.",
            body=[
                "Patient and family rights include a right to complain "
                "and information on how to voice a complaint. Staff name "
                "this right when a complaint is invited.",
            ],
            oe_code="PRE.2.h",
            boundary=[
                "The complaint mechanism and awareness of the procedure are owned by the Patient Feedback and Complaint Redressal SOP (PRE.6).",
            ],
        ),
        PlainItem(
            heading="Carry the right to information on expected cost",
            why="A patient billed for something they were never told the cost of beforehand has no way to make an informed choice about their own care -- billing staff withholding that information takes the choice away from them.",
            body=[
                "Patient and family rights include information on the "
                "expected cost of the treatment. Staff name this right "
                "when a cost question arises, and billing staff do not "
                "withhold cost information.",
            ],
            oe_code="PRE.2.i",
            boundary=[
                "Pricing policy, tariff and expected-cost explanation are owned by the Information on Expected Costs SOP (PRE.5).",
            ],
        ),
        PlainItem(
            heading="Give access to clinical records during care",
            why="A patient who cannot see their own record has no way to check it is accurate, or even to understand what is being done to them.",
            body=[
                "Patient and family rights include access to their "
                "clinical records. Access during care is given by «the "
                "treating doctor or the Patient Rights Officer on "
                "request», in a place that protects privacy.",
            ],
            oe_code="PRE.2.j",
            boundary=[
                "The discharge summary the patient takes away is owned by the Discharge Process SOP (AAC.8); the clinical record as a stored file is an Information Management System matter.",
            ],
        ),
        PlainItem(
            heading="Be told the treating doctor's name, care plan, progress and healthcare needs",
            why="A patient who does not know who is treating them, or how the plan is progressing, is left to guess at their own care -- that guess is often wrong and always unnecessary.",
            body=[
                "Patient and family rights include information on the "
                "name of the treating doctor, care plan, progress and "
                "information on their health care needs. The treating "
                "team tells the patient and family who is treating them, "
                "how the plan is progressing, and what healthcare needs "
                "apply.",
            ],
            oe_code="PRE.2.k",
            boundary=[
                "Ongoing education about healthcare needs as a teaching method is owned by the Information, Education and Communication SOP (PRE.4); this right is being told who is treating them and how they are doing.",
            ],
        ),
        PlainItem(
            heading="Let the patient determine what information is given to self and to family",
            why="A relative who demands information against the patient's own wishes, and is given it anyway, has just overridden the one person whose information it actually is.",
            body=[
                "Patient rights include determining what information "
                "regarding their care would be provided to self and "
                "family. Staff who disclose information apply the "
                "patient's determination, even against a relative's "
                "demand.",
            ],
            oe_code="PRE.2.l",
        ),
        PlainItem(
            heading="Explain the proposed care, including risks, alternatives and benefits",
            why="A patient who agrees to a procedure without ever hearing the alternatives has not actually made a choice -- they have only signed one.",
            body=[
                "The patient and/or family members are explained about "
                "the proposed care, including the risks, alternatives "
                "and benefits. Clinicians give those explanations in the "
                "course of decision-making.",
            ],
            oe_code="PRE.2.m",
            boundary=[
                "The consent conversation that must include procedure, risks, benefits, alternatives and who will perform is owned by the Informed Consent SOP (PRE.3.b); disease-process education is owned by the Information, Education and Communication SOP (PRE.4.d). They may use the same language; this right is not only the consent form.",
            ],
        ),
        PlainItem(
            heading="Explain the expected results and complications",
            why="A patient who is told only that a procedure will \"help\" and never told what could go wrong is being prepared for success and nothing else -- which leaves them and their family blindsided if it does not go as hoped.",
            body=[
                "The patient and/or family members are explained about "
                "the expected results and complications of the proposed "
                "care.",
            ],
            oe_code="PRE.2.n",
        ),
        PlainItem(
            heading="Consult the patient and/or family when the care plan is prepared or modified",
            why="A care plan changed without telling the family is a decision made about them without them -- even when the clinical reasoning behind it was sound.",
            body=[
                "The care plan is prepared and modified in consultation "
                "with the patient and/or family members. The treating "
                "team consults the patient and/or family when the plan "
                "is prepared or modified.",
            ],
            oe_code="PRE.2.o",
            boundary=[
                "The care plan as a clinical document is owned by the Assessment SOP (AAC.3); the financial implications of a plan change are owned by the Information on Expected Costs SOP (PRE.5.d).",
            ],
        ),
        PlainItem(
            heading="Provide multidisciplinary counselling when appropriate",
            why="A family facing a major surgery or a difficult diagnosis, with no one offering them a structured conversation about it, is left to process it alone when this hospital could have offered support.",
            body=[
                "The patient and/or family members are provided "
                "multidisciplinary counselling when appropriate -- for "
                "example, before major surgery, on request, or when the "
                "treating doctor documents that it is needed. The "
                "counsellor or treating team provides this counselling.",
            ],
            oe_code="PRE.2.p",
            boundary=[
                "Periodic ICU family counselling, where intensive care exists, is owned by the Care of Patients SOP (COP.6.e). Unused ICU is a recorded absence, not a copied procedure.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-16 (see the PRE.2 Records folder).",
    related_documents=[
        "Hospital's Patient and Family Rights and Responsibilities SOP (PRE.1)",
        "Hospital's Informed Consent SOP (PRE.3)",
        "Hospital's Information on Expected Costs SOP (PRE.5)",
        "Hospital's Patient Feedback and Complaint Redressal SOP (PRE.6)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an audit finds the "
        "same right was not exercised twice in the same setting, or if "
        "the sibling PRE, AAC or COP policies this SOP points to are "
        "revised."
    ),
    full_reference_list=[
        NABH_PRE_CITE.format(code="PRE.2"),
        WHO_RIGHTS_SRC,
        OLEJARCZYK_YOUNG_SRC,
    ],
)

SOPS.append(("SOP_PRE.2.a_to_p_beliefs_values_decision_making.docx", PRE2))

# ---- PRE.2 Records -------------------------------------------------
_add("PRE.2", 1, RecordSpec(
    oe_code="PRE.2.a",
    oe_requirement="Patients and family rights include respecting values and beliefs, any special preferences, cultural needs, and responding to requests for spiritual needs.",
    record_title="PRE.2 Record 01 — Values, beliefs and spiritual-needs response record",
    what_is_this="This record is the proof a patient's values, beliefs, cultural needs or spiritual request was actually identified and responded to -- not dismissed as \"not medical\".",
    real_example="A patient requests a visit from a religious counsellor before a procedure; the ward nurse passes the request to the hospital counsellor the same day.",
    why_nabh_asks="A patient whose spiritual request is ignored is told their beliefs do not count in the one place they most need to.",
    how_to_fill=[
        ("Date", "Date of the request or identification."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Need Identified", "Value, belief, preference, cultural or spiritual need."),
        ("Response / Action", "What was done."),
        ("Identified By", "Registration staff or nurse."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2"), WHO_RIGHTS_SRC],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Need Identified", "Response / Action", "Identified By"],
    worked_example_row=["WORKED EXAMPLE — 14-Jun-2026", "Ibrahim Sheikh / UID-00912", "Request for prayer space before surgery", "Quiet room arranged, counsellor informed", "Ward Nurse S. Pillai"],
), "values_beliefs_spiritual_needs_response_record")

_add("PRE.2", 2, RecordSpec(
    oe_code="PRE.2.b",
    oe_requirement="Patient and family rights include respect for personal dignity and privacy during examination, procedures and treatment.",
    record_title="PRE.2 Record 02 — Dignity and privacy audit sample",
    what_is_this="This record is the proof screens, closed doors or low voices were actually used during examination -- not assumed because no complaint was made.",
    real_example="A quarterly sample of ten examinations confirms a screen was drawn in every case and no diagnosis was discussed in a shared corridor.",
    why_nabh_asks="A corridor discussion overheard by the next patient costs someone their dignity for no clinical reason at all.",
    how_to_fill=[
        ("Audit Date", "Date of the audit."),
        ("Setting", "Out-patient, ward, or emergency."),
        ("Encounters Sampled", "Number checked."),
        ("Privacy Respected (Y/N)", "Result."),
        ("Finding / Action (if any)", "Any defect and its fix."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Audit Date", "Setting", "Encounters Sampled", "Privacy Respected (Y/N)", "Finding / Action (if any)"],
    worked_example_row=["WORKED EXAMPLE — 15-Jun-2026", "Out-patient", "10", "Y", "None"],
), "dignity_privacy_audit_sample")

_add("PRE.2", 3, RecordSpec(
    oe_code="PRE.2.c",
    oe_requirement="Patient and family rights include protection from neglect or abuse.",
    record_title="PRE.2 Record 03 — Neglect/abuse suspicion report log",
    what_is_this="This record is the proof every suspicion of neglect or abuse was actually reported the moment it was noticed -- not quietly let go.",
    real_example="A nurse notices unexplained bruising on an elderly patient and reports the suspicion to the Patient Rights Officer the same shift.",
    why_nabh_asks="A suspicion that is noticed and then let go is the moment that allows it to happen again to the next patient.",
    how_to_fill=[
        ("Date/Time", "When noticed."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Suspicion Noted", "What was observed."),
        ("Reported By / To", "Staff member and receiver."),
        ("Entered in PRE.1.d Violation Log (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date/Time", "Patient (Identifier 1) / UID (Identifier 2)", "Suspicion Noted", "Reported By / To", "Entered in PRE.1.d Violation Log (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 16-Jun-2026, 2:00 PM", "Kamala Devi / UID-00918", "Unexplained bruising", "Staff Nurse R. Menon / Patient Rights Officer", "Y"],
), "neglect_abuse_suspicion_report_log")

_add("PRE.2", 4, RecordSpec(
    oe_code="PRE.2.d",
    oe_requirement="Patient and family rights include treating patient information as confidential.",
    record_title="PRE.2 Record 04 — Confidentiality defect and correction log",
    what_is_this="This record is the proof any confidentiality defect noticed -- such as a record left open at a public desk -- was actually caught and corrected.",
    real_example="A patient's file is found open at the registration desk; it is closed and staff are reminded the same day.",
    why_nabh_asks="Information left open at a public desk is a breach a patient never consented to and often never even learns happened.",
    how_to_fill=[
        ("Date", "When noticed."),
        ("Defect Observed", "What was found open or disclosed."),
        ("Location", "Where it happened."),
        ("Corrected By / Action", "What was done."),
        ("Staff Reminded (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Defect Observed", "Location", "Corrected By / Action", "Staff Reminded (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 17-Jun-2026", "Patient file left open at desk", "Registration counter", "File closed, Registration In-Charge notified", "Y"],
), "confidentiality_defect_correction_log")

_add("PRE.2", 5, RecordSpec(
    oe_code="PRE.2.e",
    oe_requirement="Patient and family rights include the refusal of treatment.",
    record_title="PRE.2 Record 05 — Treatment refusal record",
    what_is_this="This record is the proof a refusal was actually received and recorded as refusal, without punishment -- not chased as an unsigned form.",
    real_example="A patient declines a recommended procedure; the treating doctor records the refusal and cross-references the consent record.",
    why_nabh_asks="A patient made to feel punished for refusing will stop telling staff the truth about what they will and will not accept.",
    how_to_fill=[
        ("Date", "Date of refusal."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Treatment Refused", "What was declined."),
        ("Recorded By", "Treating doctor."),
        ("PRE.3 Consent Record Cross-Reference", "Reference."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Treatment Refused", "Recorded By", "PRE.3 Consent Record Cross-Reference"],
    worked_example_row=["WORKED EXAMPLE — 18-Jun-2026", "Prakash Jain / UID-00924", "Recommended biopsy", "Dr. Varma", "Consent-not-given record dated 18-Jun-2026"],
), "treatment_refusal_record")

_add("PRE.2", 6, RecordSpec(
    oe_code="PRE.2.f",
    oe_requirement="Patient and family rights include a right to seek an additional opinion regarding clinical care.",
    record_title="PRE.2 Record 06 — Additional-opinion facilitation record",
    what_is_this="This record is the proof a request for a second opinion was actually facilitated or honestly explained -- not refused outright.",
    real_example="A family asks for a second opinion before a major surgery; the hospital arranges a referral letter and appointment with a tie-up specialist.",
    why_nabh_asks="A patient denied even the chance to ask someone else is a patient whose trust in this hospital was never actually earned.",
    how_to_fill=[
        ("Date", "Date of request."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Request", "What was asked."),
        ("Facilitated How", "Referral arranged, or honest statement of what could not be arranged."),
        ("Facilitated By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Request", "Facilitated How", "Facilitated By"],
    worked_example_row=["WORKED EXAMPLE — 19-Jun-2026", "Geeta Nair / UID-00930", "Second opinion before cardiac surgery", "Referral letter and appointment arranged with tie-up cardiologist", "Dr. Varma"],
), "additional_opinion_facilitation_record")

_add("PRE.2", 7, RecordSpec(
    oe_code="PRE.2.g",
    oe_requirement="Patient and family rights include informed consent before the transfusion of blood and blood components, anaesthesia, surgery, initiation of any research protocol and any other invasive/high-risk procedures/treatment.",
    record_title="PRE.2 Record 07 — Consent-right awareness pointer record",
    what_is_this="This record is the proof staff actually named informed consent as a right before taking it -- not only presented the form.",
    real_example="Before a surgical consent is taken, the surgeon tells the patient this is their right, not only a formality to sign.",
    why_nabh_asks="A patient who is never told that consent is their right has no way of knowing they could have asked questions or said no.",
    how_to_fill=[
        ("Date", "Date of the encounter."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Act Requiring Consent", "Transfusion, anaesthesia, surgery, research, or other invasive/high-risk act."),
        ("Right Named Before Consent Taken (Y/N)", "Confirmed."),
        ("Consent Record Cross-Reference", "PRE.3 record."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Act Requiring Consent", "Right Named Before Consent Taken (Y/N)", "Consent Record Cross-Reference"],
    worked_example_row=["WORKED EXAMPLE — 20-Jun-2026", "Ramesh Gupta / UID-00936", "Surgery (appendectomy)", "Y", "PRE.3 consent record dated 20-Jun-2026"],
), "consent_right_awareness_pointer_record")

_add("PRE.2", 8, RecordSpec(
    oe_code="PRE.2.h",
    oe_requirement="Patient and family rights include a right to complain and information on how to voice a complaint.",
    record_title="PRE.2 Record 08 — Complaint-right awareness pointer record",
    what_is_this="This record is the proof staff actually named the right to complain when a complaint was invited -- not left the patient to find the route on their own.",
    real_example="During a dissatisfaction conversation, the ward nurse tells the family about the complaint box and helpline number.",
    why_nabh_asks="A patient who does not know a complaint route exists will simply leave dissatisfied and never tell this hospital why.",
    how_to_fill=[
        ("Date", "Date of the encounter."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Situation", "What prompted naming the right."),
        ("Right Named (Y/N)", "Confirmed."),
        ("Named By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Situation", "Right Named (Y/N)", "Named By"],
    worked_example_row=["WORKED EXAMPLE — 21-Jun-2026", "Anita Shah / UID-00942", "Family expressed dissatisfaction with wait time", "Y", "Ward Nurse T. Kulkarni"],
), "complaint_right_awareness_pointer_record")

_add("PRE.2", 9, RecordSpec(
    oe_code="PRE.2.i",
    oe_requirement="Patient and family rights include information on the expected cost of the treatment.",
    record_title="PRE.2 Record 09 — Cost-right awareness and non-withholding record",
    what_is_this="This record is the proof billing staff actually named the cost-information right and did not withhold it -- not left the patient to ask repeatedly.",
    real_example="At admission, billing staff proactively explain the expected cost of a procedure without the family having to ask.",
    why_nabh_asks="A patient billed for something they were never told the cost of beforehand has no way to make an informed choice about their own care.",
    how_to_fill=[
        ("Date", "Date of the encounter."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Billable Event", "Procedure or admission."),
        ("Cost Right Named (Y/N)", "Confirmed."),
        ("Named By", "Billing staff."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Billable Event", "Cost Right Named (Y/N)", "Named By"],
    worked_example_row=["WORKED EXAMPLE — 22-Jun-2026", "Vikram Oza / UID-00948", "Elective surgery admission", "Y", "Billing Staff N. Desai"],
), "cost_right_awareness_non_withholding_record")

_add("PRE.2", 10, RecordSpec(
    oe_code="PRE.2.j",
    oe_requirement="Patient and family rights include access to their clinical records.",
    record_title="PRE.2 Record 10 — Clinical-record access log",
    what_is_this="This record is the proof a patient's request to see their own clinical record was actually honoured, in a place that protected privacy -- not refused or delayed without reason.",
    real_example="A patient asks to review their progress notes mid-stay; the treating doctor reviews them with the patient in a private consultation room.",
    why_nabh_asks="A patient who cannot see their own record has no way to check it is accurate, or even to understand what is being done to them.",
    how_to_fill=[
        ("Date", "Date of the request."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Records Requested", "What was asked for."),
        ("Given By", "Treating doctor or Patient Rights Officer."),
        ("Privacy Protected (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Records Requested", "Given By", "Privacy Protected (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 23-Jun-2026", "Deepak Mehra / UID-00954", "Progress notes", "Dr. Nair", "Y"],
), "clinical_record_access_log")

_add("PRE.2", 11, RecordSpec(
    oe_code="PRE.2.k",
    oe_requirement="Patient and family rights include information on the name of the treating doctor, care plan, progress and information on their health care needs.",
    record_title="PRE.2 Record 11 — Treating-doctor and progress information record",
    what_is_this="This record is the proof the patient and family were actually told who is treating them and how the plan is progressing -- not left to guess.",
    real_example="At each ward round, the nurse confirms the family knows the treating doctor's name and current plan.",
    why_nabh_asks="A patient who does not know who is treating them is left to guess at their own care -- that guess is often wrong and always unnecessary.",
    how_to_fill=[
        ("Date", "Date informed."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Treating Doctor Named (Y/N)", "Confirmed."),
        ("Progress/Plan Shared (Y/N)", "Confirmed."),
        ("Informed By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Treating Doctor Named (Y/N)", "Progress/Plan Shared (Y/N)", "Informed By"],
    worked_example_row=["WORKED EXAMPLE — 24-Jun-2026", "Shalini Rao / UID-00960", "Y", "Y", "Staff Nurse A. Pillai"],
), "treating_doctor_progress_information_record")

_add("PRE.2", 12, RecordSpec(
    oe_code="PRE.2.l",
    oe_requirement="Patient rights include determining what information regarding their care would be provided to self and family.",
    record_title="PRE.2 Record 12 — Patient information-disclosure determination record",
    what_is_this="This record is the proof the patient's own choice about who is told what was actually recorded and followed -- not overridden by a relative's demand.",
    real_example="A patient asks that her diagnosis not be shared with a specific relative; staff honour that determination when the relative later asks.",
    why_nabh_asks="A relative who demands information against the patient's own wishes, and is given it anyway, has just overridden the one person whose information it actually is.",
    how_to_fill=[
        ("Date", "Date recorded."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Determination", "Who may or may not be told."),
        ("Recorded By", "Staff member."),
        ("Honoured When Tested (Y/N/NA)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Determination", "Recorded By", "Honoured When Tested (Y/N/NA)"],
    worked_example_row=["WORKED EXAMPLE — 25-Jun-2026", "Nisha Patel / UID-00966", "Diagnosis not to be shared with a named relative", "Dr. Iyer", "Y"],
), "patient_information_disclosure_determination_record")

_add("PRE.2", 13, RecordSpec(
    oe_code="PRE.2.m",
    oe_requirement="The patient and/or family members are explained about the proposed care, including the risks, alternatives and benefits.",
    record_title="PRE.2 Record 13 — Proposed-care explanation record",
    what_is_this="This record is the proof the patient was actually explained the proposed care, its risks, alternatives and benefits -- not only handed a consent form to sign.",
    real_example="Before a scheduled surgery, the surgeon explains the procedure, its risks, alternatives (medical management) and expected benefit.",
    why_nabh_asks="A patient who agrees to a procedure without ever hearing the alternatives has not actually made a choice -- they have only signed one.",
    how_to_fill=[
        ("Date", "Date of explanation."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Proposed Care", "What was proposed."),
        ("Risks/Alternatives/Benefits Covered (Y/N)", "Confirmed."),
        ("Explained By", "Clinician."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Proposed Care", "Risks/Alternatives/Benefits Covered (Y/N)", "Explained By"],
    worked_example_row=["WORKED EXAMPLE — 26-Jun-2026", "Arjun Reddy / UID-00972", "Laparoscopic cholecystectomy", "Y", "Dr. Varma"],
), "proposed_care_explanation_record")

_add("PRE.2", 14, RecordSpec(
    oe_code="PRE.2.n",
    oe_requirement="The patient and/or family members are explained about the expected results and complications.",
    record_title="PRE.2 Record 14 — Expected results and complications explanation record",
    what_is_this="This record is the proof the patient was actually told what could go wrong, not only that the procedure would help.",
    real_example="The surgeon explains the expected recovery timeline and possible complications of the cholecystectomy before consent is taken.",
    why_nabh_asks="A patient prepared only for success is left blindsided if a complication occurs that they were never warned about.",
    how_to_fill=[
        ("Date", "Date of explanation."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Expected Results", "What was explained."),
        ("Complications Covered (Y/N)", "Confirmed."),
        ("Explained By", "Clinician."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Expected Results", "Complications Covered (Y/N)", "Explained By"],
    worked_example_row=["WORKED EXAMPLE — 26-Jun-2026", "Arjun Reddy / UID-00972", "Full recovery expected in 2 weeks", "Y", "Dr. Varma"],
), "expected_results_complications_explanation_record")

_add("PRE.2", 15, RecordSpec(
    oe_code="PRE.2.o",
    oe_requirement="The care plan is prepared and modified in consultation with the patient and/or family members.",
    record_title="PRE.2 Record 15 — Care-plan consultation record",
    what_is_this="This record is the proof the patient or family was actually consulted when the care plan was prepared or changed -- not informed after the fact.",
    real_example="When a treatment plan is revised mid-admission, the treating doctor discusses the change with the family before implementing it.",
    why_nabh_asks="A care plan changed without telling the family is a decision made about them without them, even when the clinical reasoning was sound.",
    how_to_fill=[
        ("Date", "Date of consultation."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Plan Prepared or Modified", "Which."),
        ("Consulted (Y/N)", "Confirmed."),
        ("Consulted By", "Treating team."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Plan Prepared or Modified", "Consulted (Y/N)", "Consulted By"],
    worked_example_row=["WORKED EXAMPLE — 27-Jun-2026", "Meera Joshi / UID-00978", "Modified — added physiotherapy", "Y", "Dr. Iyer"],
), "care_plan_consultation_record")

_add("PRE.2", 16, RecordSpec(
    oe_code="PRE.2.p",
    oe_requirement="The patient and/or family members are provided multidisciplinary counselling when appropriate.",
    record_title="PRE.2 Record 16 — Multidisciplinary counselling record",
    what_is_this="This record is the proof counselling was actually offered and provided when the situation called for it -- not left to the family to request on their own.",
    real_example="Before a major cardiac surgery, the counsellor meets with the patient and family to discuss the procedure and answer questions.",
    why_nabh_asks="A family facing a major surgery with no one offering them a structured conversation about it is left to process it alone when this hospital could have offered support.",
    how_to_fill=[
        ("Date", "Date of counselling."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Reason Counselling Was Appropriate", "What prompted it."),
        ("Provided By", "Counsellor or treating team."),
        ("Outcome / Follow-up (if any)", "Result."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.2")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Reason Counselling Was Appropriate", "Provided By", "Outcome / Follow-up (if any)"],
    worked_example_row=["WORKED EXAMPLE — 28-Jun-2026", "Harish Chandra / UID-00984", "Major cardiac surgery", "Hospital Counsellor", "Family questions addressed; follow-up scheduled pre-op"],
), "multidisciplinary_counselling_record")

# ============================================================== PRE.3 ====
PRE3 = SOPSpecV2(
    sop_no="SOP-PRE.3",
    title="Informed Consent",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» obtains informed consent "
        "wherever it is required -- transfusion, anaesthesia, surgery, "
        "research and other invasive or high-risk procedures -- what that "
        "consent must actually include, who may give it when a patient "
        "cannot decide for themselves, and that it is the person "
        "performing the procedure who takes it, not a clerk or nurse on "
        "their behalf."
    ),
    purpose_trigger=(
        "A nurse is asked to get a signature on a surgical consent form "
        "because the surgeon is busy. This SOP is what makes sure that "
        "does not happen -- consent for an elective procedure is taken by "
        "the person who will actually perform it, every time."
    ),
    purpose_why=(
        "We do this because a form signed without the procedure, its "
        "risks, benefits and alternatives actually being explained is not "
        "consent -- it is a signature, and a patient who signed a "
        "signature instead of giving consent can rightly say later that "
        "they were never asked."
    ),
    purpose_text=(
        "To define when informed consent is required at «Hospital Name», "
        "what it must include, who may give it when the patient is "
        "incapable of deciding, and that it is taken by the person "
        "performing the procedure, adhering to statutory norms."
    ),
    scope_why="so every situation requiring consent across this hospital follows the same statutory-compliant process, not a different informal practice ward to ward.",
    scope_text=(
        "Applies to every situation at «Hospital Name» in which informed "
        "consent is required: transfusion of blood and blood components, "
        "anaesthesia, surgery, initiation of any research protocol this "
        "hospital runs, and any other invasive or high-risk procedure or "
        "treatment this hospital has named. It binds the person who "
        "performs the procedure, doctors and nurses who explain consent, "
        "registration staff who schedule elective work, and the Patient "
        "Rights Officer who holds the list and process."
    ),
    responsibility_why="a consent process that exists on paper but is actually carried out by whoever is free at the time is not informed consent -- the person performing the procedure is the one who can actually answer the patient's questions.",
    responsibilities=[
        ("Medical Superintendent", "Is accountable that informed consent is obtained where required, by the person performing, under a process that adheres to statutory norms."),
        ("Patient Rights Officer", "Authors and keeps current the list of situations, the process, the information method and the incapacity description."),
        ("Person Performing the Procedure", "Takes the consent; staff who explain or witness do not replace that person on elective work."),
        ("Doctors and Nurses", "Record refusal as refusal, not as a missing signature to be fetched later."),
        ("Quality Coordinator", "Audits consent records quarterly."),
    ],
    items=[
        PlainItem(
            heading="Obtain informed consent wherever it is required, following statutory norms",
            why="A patient treated with an invasive or high-risk procedure they never actually agreed to has been treated without their consent, whatever paperwork exists afterward.",
            body=[
                "The organisation obtains informed consent from the "
                "patient or family for situations where it is required, "
                "and the process adheres to statutory norms.",
                "Situations where informed consent is required at "
                "«Hospital Name» include at least these five:",
                "1. Transfusion of blood and blood components.",
                "2. Anaesthesia.",
                "3. Surgery.",
                "4. Initiation of any research protocol this hospital "
                "actually runs.",
                "5. Any other invasive or high-risk procedure or "
                "treatment named in the consent situations list held by "
                "the Patient Rights Officer.",
                "A class the service "
                "directory does not provide is a recorded absence, not "
                "a copied consent procedure.",
                "The consent process -- when it is obtained, how it is "
                "recorded, how refusal is recorded, and how a "
                "documented emergency that made prior consent "
                "impossible is recorded -- is held by the Patient "
                "Rights Officer. Emergency means delay would endanger "
                "life or limb; it is not a label for convenience on "
                "elective work.",
                "A registered medical practitioner obtains consent "
                "consistent with professional practice under national "
                "medical regulation. Published consent-practice "
                "frameworks may inform this process; they are not "
                "pasted in as this hospital's protocol.",
            ],
            oe_code="PRE.3.a",
            technical_sources=[NMC_ACT_SRC, KUMAR_CONSENT_SRC, NANDIMATH_SRC],
        ),
        PlainItem(
            heading="Include the procedure, risks, benefits, alternatives and performer in a language they understand",
            why="A form that lists only \"surgery\" with nothing about who will perform it or what could go wrong gives the patient nothing real to agree to.",
            body=[
                "Informed consent includes information on five things, "
                "in a language that they can understand:",
                "1. The procedure.",
                "2. Its risks.",
                "3. Benefits.",
                "4. Alternatives.",
                "5. Who will perform the procedure.",
                "The consent form and conversation cover those elements "
                "in «Hindi and English» or the language the patient or "
                "family can understand. A form that lists only "
                "\"surgery\", or that is silent on who will perform it, "
                "is incomplete.",
            ],
            oe_code="PRE.3.b",
            boundary=[
                "Ongoing education about healthcare needs in the same language is owned by the Information, Education and Communication SOP (PRE.4); this step is the consent conversation itself.",
            ],
        ),
        PlainItem(
            heading="Describe who can give consent when the patient is incapable, and apply it",
            why="A single next-of-kin signature used for a child, an unconscious adult, an emergency and a person with mental illness all alike is not a description of who may consent -- it is a shortcut that can go wrong in exactly the case it matters most.",
            body=[
                "The organisation describes who can give consent when a "
                "patient is incapable of independent decision-making, "
                "and implements that description.",
                "The description distinguishes four categories:",
                "1. A child.",
                "2. An unconscious or otherwise non-communicating "
                "adult.",
                "3. A documented emergency.",
                "4. A person with mental illness as defined "
                "in national mental healthcare law where that law "
                "applies. For that specific legal category, the "
                "nominated representative and advance directive "
                "provisions of that law are used without reprinting "
                "them here; for other incapacity, this hospital's own "
                "written description, held by the Patient Rights "
                "Officer, applies.",
            ],
            oe_code="PRE.3.c",
            technical_sources=[MHCA_SRC],
        ),
        PlainItem(
            heading="Ensure consent is taken by the person performing the procedure",
            why="A clerk or nurse taking consent \"for\" the surgeon on an elective case means no one who can actually answer the patient's questions was ever in the room when they were asked.",
            body=[
                "Informed consent is taken by the person performing the "
                "procedure.",
                "For surgery, the doctor who will perform the "
                "procedure, or a doctor of the same surgical team who "
                "will be present and responsible, takes consent. For "
                "other classes of procedure requiring consent, the "
                "named performer is the doctor who will perform the "
                "act. A clerk or nurse taking consent on an elective "
                "case does not meet this standard.",
            ],
            oe_code="PRE.3.d",
        ),
        PlainItem(
            heading="Know when to stop — and what happens next",
            why="Proceeding with an elective or planned high-risk act without valid consent is not a scheduling convenience -- it is treating a patient without their agreement, and that does not become acceptable because the list was already full for the day.",
            body=[
                "Do not start an elective or planned transfusion, "
                "anaesthesia, surgery, research protocol or other "
                "invasive or high-risk procedure without valid informed "
                "consent from the patient or a person authorised to "
                "give it on their behalf.",
                "Emergency exception: when delay would endanger life or "
                "limb, treatment may proceed under the documented "
                "emergency method. The reason, who decided, and when "
                "consent was obtained or renewed as soon as the patient "
                "or family could give it, are all recorded. Emergency "
                "is not a standing exemption for work that was "
                "scheduled.",
                "Stopping applies to the act itself, not to "
                "stabilisation before the consent conversation can "
                "happen in a true emergency.",
                "The person performing tells the Medical Superintendent "
                "or Patient Rights Officer the same shift. Refusing to "
                "proceed without consent on an elective case is not a "
                "disciplinary matter -- it is the correct call.",
            ],
            oe_code="PRE.3",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the PRE.3 Records folder).",
    related_documents=[
        "Policy on Beliefs, Values and Involvement in Decision-Making (PRE.2)",
        "Hospital's Information, Education and Communication SOP (PRE.4)",
        "Hospital's Surgical Safety SOP (COP.11)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a consent was taken "
        "by someone other than the performer, an incapacity description "
        "gap is found, or statutory norms under national medical or "
        "mental healthcare law change."
    ),
    full_reference_list=[
        NABH_PRE_CITE.format(code="PRE.3"),
        NMC_ACT_SRC,
        MHCA_SRC,
        KUMAR_CONSENT_SRC,
        NANDIMATH_SRC,
    ],
)

SOPS.append(("SOP_PRE.3.a_to_d_informed_consent.docx", PRE3))

# ---- PRE.3 Records -------------------------------------------------
_add("PRE.3", 1, RecordSpec(
    oe_code="PRE.3.a",
    oe_requirement="The organisation obtains informed consent from the patient or family for situations where informed consent is required. Informed consent process adhered to statutory norms.",
    record_title="PRE.3 Record 01 — Consent situations list and process audit sample",
    what_is_this="This record is the proof a quarterly sample of listed situations was actually checked to confirm no elective procedure went ahead without consent -- not assumed compliant.",
    real_example="A quarterly sample of ten surgical cases confirms every one has a valid signed consent matching the unique identification number.",
    why_nabh_asks="A patient treated with an invasive or high-risk procedure they never actually agreed to has been treated without their consent, whatever paperwork exists afterward.",
    how_to_fill=[
        ("Audit Date", "Date of the audit."),
        ("Situation Class", "Transfusion, anaesthesia, surgery, research, or other."),
        ("Cases Sampled", "Number checked."),
        ("Valid Consent Present (Y/N, all)", "Result."),
        ("Finding / Action (if any)", "Any gap and its fix."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.3"), NMC_ACT_SRC],
    column_headers=["Audit Date", "Situation Class", "Cases Sampled", "Valid Consent Present (Y/N, all)", "Finding / Action (if any)"],
    worked_example_row=["WORKED EXAMPLE — 29-Jun-2026", "Surgery", "10", "Y", "None"],
), "consent_situations_process_audit_sample")

_add("PRE.3", 2, RecordSpec(
    oe_code="PRE.3.b",
    oe_requirement="Informed consent includes information regarding the procedure, its risks, benefits, alternatives and as to who will perform the procedure in a language that they can understand.",
    record_title="PRE.3 Record 02 — Consent content completeness record",
    what_is_this="This record is the proof each consent actually named the procedure, risks, benefits, alternatives and performer -- not a form that says only \"surgery\".",
    real_example="A review of a surgical consent form confirms it names the specific procedure, its risks, the non-surgical alternative, and the operating surgeon by name.",
    why_nabh_asks="A form silent on who will perform the procedure or what could go wrong gives the patient nothing real to agree to.",
    how_to_fill=[
        ("Date", "Date of consent."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Procedure Named (Y/N)", "Confirmed."),
        ("Risks/Benefits/Alternatives/Performer Named (Y/N)", "Confirmed."),
        ("Language Used", "As given."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.3")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Procedure Named (Y/N)", "Risks/Benefits/Alternatives/Performer Named (Y/N)", "Language Used"],
    worked_example_row=["WORKED EXAMPLE — 30-Jun-2026", "Sanjay Kapoor / UID-00990", "Y", "Y", "Hindi"],
), "consent_content_completeness_record")

_add("PRE.3", 3, RecordSpec(
    oe_code="PRE.3.c",
    oe_requirement="The organisation describes who can give consent when a patient is incapable of independent decision making and implements the same.",
    record_title="PRE.3 Record 03 — Incapacity-consent signer verification record",
    what_is_this="This record is the proof the signer on a consent for an incapable patient actually matched the written description -- not a single next-of-kin stamp used for every case alike.",
    real_example="For an unconscious trauma patient, the accompanying spouse signs consent and the record notes the basis -- unconscious adult, not mental illness.",
    why_nabh_asks="A single next-of-kin signature used for a child, an unconscious adult, an emergency and a person with mental illness alike can go wrong in exactly the case it matters most.",
    how_to_fill=[
        ("Date", "Date of consent."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Incapacity Basis", "Child, unconscious adult, documented emergency, or mental illness under law."),
        ("Signer / Relationship", "Who signed."),
        ("Matches Description (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.3"), MHCA_SRC],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Incapacity Basis", "Signer / Relationship", "Matches Description (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 01-Jul-2026", "Mohan Lal / UID-00996", "Unconscious adult", "Spouse — Sunita Lal", "Y"],
), "incapacity_consent_signer_verification_record")

_add("PRE.3", 4, RecordSpec(
    oe_code="PRE.3.d",
    oe_requirement="Informed consent is taken by the person performing the procedure.",
    record_title="PRE.3 Record 04 — Performer-took-consent verification record",
    what_is_this="This record is the proof the person who signed as having taken consent actually matches the person who performed the procedure -- not a clerk on an elective case.",
    real_example="A review of the operative register confirms the consent-taking doctor and the operating surgeon are the same named person.",
    why_nabh_asks="A clerk or nurse taking consent \"for\" the surgeon means no one who can actually answer the patient's questions was in the room when they were asked.",
    how_to_fill=[
        ("Date", "Date of the procedure."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Consent Taken By", "Named doctor."),
        ("Procedure Performed By", "Named doctor."),
        ("Match (Y/N)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.3")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Consent Taken By", "Procedure Performed By", "Match (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 02-Jul-2026", "Farida Khan / UID-01002", "Dr. Bhatt", "Dr. Bhatt", "Y"],
), "performer_took_consent_verification_record")

_add("PRE.3", 5, RecordSpec(
    oe_code="PRE.3",
    oe_requirement="Elective or planned transfusion, anaesthesia, surgery, research or other invasive/high-risk procedure is not started without valid informed consent; a documented emergency is the only exception.",
    record_title="PRE.3 Record 05 — Consent stop-work and emergency-exception log",
    what_is_this="This record is the proof an elective act was actually stopped when consent was not yet valid, and that any emergency exception was properly documented with reason and decider -- not treated as a routine shortcut.",
    real_example="A scheduled procedure is halted when the consent form is found incomplete; the surgeon notifies the Medical Superintendent the same shift and the case is rescheduled once consent is properly taken.",
    why_nabh_asks="Proceeding with an elective act without valid consent is treating a patient without their agreement -- that does not become acceptable because the schedule was full.",
    how_to_fill=[
        ("Date/Time", "When stopped or exception invoked."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Reason Stopped / Emergency Basis", "Why."),
        ("Decided By", "Who decided."),
        ("Reported To (Same Shift)", "Medical Superintendent or Patient Rights Officer."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.3")],
    column_headers=["Date/Time", "Patient (Identifier 1) / UID (Identifier 2)", "Reason Stopped / Emergency Basis", "Decided By", "Reported To (Same Shift)"],
    worked_example_row=["WORKED EXAMPLE — 03-Jul-2026, 9:00 AM", "Rohit Verma / UID-01008", "Consent form incomplete — procedure not named", "Dr. Bhatt (stopped elective case)", "Medical Superintendent"],
), "consent_stop_work_emergency_exception_log")

# ============================================================== PRE.4 ====
PRE4 = SOPSpecV2(
    sop_no="SOP-PRE.4",
    title="Information, Education and Communication about Healthcare Needs",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» educates patients and "
        "families in a language and format they can understand, covering "
        "medicines and side effects, food-drug interaction and diet, "
        "their specific disease process, preventing healthcare-associated "
        "infections, and doing all of this through communication that "
        "actually works -- checked for understanding, not just delivered."
    ),
    purpose_trigger=(
        "A patient is handed a printed leaflet about their new medication "
        "and sent home. This SOP is what makes sure someone actually "
        "talked them through it in a language they understand, and "
        "checked they could repeat back the key point -- not that a "
        "leaflet changed hands."
    ),
    purpose_why=(
        "We do this because a harvested signature on an education form is "
        "not proof anyone learned anything, and a patient who leaves not "
        "understanding their own medicines, diet restrictions or warning "
        "signs is a patient this hospital will likely see again, sicker, "
        "for a problem that could have been prevented."
    ),
    purpose_text=(
        "To define how «Hospital Name» educates the patient and/or family "
        "in a language and format they can understand, about medication "
        "safety and side effects, food-drug interaction and diet, their "
        "specific disease process, preventing healthcare-associated "
        "infections, and does so through communication that is actually "
        "effective."
    ),
    scope_why="so teaching happens wherever a patient is cared for, not only as a one-time discharge formality.",
    scope_text=(
        "Applies wherever a patient or family is taught about healthcare "
        "needs: registration after stabilisation, out-patient, "
        "emergency, in-patient, day-care, intensive care where it "
        "exists, and at discharge. It binds treating doctors, nurses, "
        "the Patient Rights Officer as education lead where named, and "
        "the Quality Coordinator who audits."
    ),
    responsibility_why="education that is assigned to \"whoever is free\" rather than a named role tends to become the first thing skipped when the ward gets busy.",
    responsibilities=[
        ("Medical Superintendent", "Is accountable for education and effective communication."),
        ("Patient Rights Officer (or named education lead)", "Holds language-and-format method, topic methods and effective-communication method."),
        ("Doctors and Nurses", "Teach and check understanding."),
        ("Quality Coordinator", "Audits this SOP quarterly."),
    ],
    items=[
        PlainItem(
            heading="Educate in a language and format the patient and family can understand",
            why="A patient taught in a language they do not follow has not actually been taught anything, whatever the record says.",
            body=[
                "Patient and/or family are educated in a language and "
                "format that they can understand.",
                "Language and format are chosen from five options and "
                "recorded in «Hindi and English» or the patient's own "
                "language:",
                "1. Spoken language.",
                "2. Written material.",
                "3. Interpreter use.",
                "4. An accompanying family member as translator.",
                "5. What is done when the patient cannot read.",
            ],
            oe_code="PRE.4.a",
            boundary=[
                "The consent conversation that uses the same language is owned by the Informed Consent SOP (PRE.3.b); this step is ongoing education.",
            ],
        ),
        PlainItem(
            heading="Educate about medicines and potential side effects, when appropriate",
            why="A patient who starts a new medicine without being told what to watch for has no way of recognising a side effect before it becomes an emergency.",
            body=[
                "Patient and/or family are educated about the safe and "
                "effective use of medication and the potential side "
                "effects, when appropriate. Education is given at the "
                "start of a medicine, at a dose change, and again at "
                "discharge if the medicine continues.",
            ],
            oe_code="PRE.4.b",
            boundary=[
                "Administration of the medicine is owned by the Safe Administration SOP (MOM.6); capturing a medication error or adverse reaction is owned by the Monitoring SOP (MOM.7).",
            ],
        ),
        PlainItem(
            heading="Educate about food-drug interaction, diet, nutrition and immunisations",
            why="A patient who is not told a new medicine interacts with a food they eat daily can undo the medicine's effect, or worse, without ever knowing why.",
            body=[
                "Patient and/or family are educated about food-drug "
                "interaction and about diet, nutrition and "
                "immunisations. Teaching for each topic this hospital "
                "actually uses is recorded; a topic not provided as a "
                "service is a recorded absence, not a copied teaching "
                "record.",
            ],
            oe_code="PRE.4.c",
            boundary=[
                "Nutritional-risk screening and therapeutic diet are owned by the Care of Patients SOP (COP.13); paediatric immunisation assessment is owned by COP.8; kitchen method is owned by the infection-control team.",
            ],
        ),
        PlainItem(
            heading="Educate about the specific disease process, complications and prevention strategies",
            why="A generic poster about a condition is not education about this patient's condition -- a patient needs to hear what applies to them specifically, not what applies to everyone with that diagnosis in general.",
            body=[
                "Patient and/or family are educated about their "
                "specific disease process, complications and prevention "
                "strategies. Teaching covers the condition this patient "
                "actually has, not only a generic handout.",
            ],
            oe_code="PRE.4.d",
            boundary=[
                "The diagnosis and care plan themselves are owned by the Assessment SOP (AAC.3).",
            ],
        ),
        PlainItem(
            heading="Educate about preventing healthcare-associated infections",
            why="A patient who does not know to tell staff about a fever, or not to touch an IV line, cannot help protect themselves from an infection this hospital is also working to prevent.",
            body=[
                "Patient and/or family are educated about preventing "
                "healthcare-associated infections -- hand hygiene, not "
                "touching devices, telling staff of fever -- through a "
                "short ward talk at admission and a reminder at "
                "discharge.",
            ],
            oe_code="PRE.4.e",
            boundary=[
                "Infection-prevention bundles and surveillance themselves are owned by the hospital's infection control and prevention programme.",
            ],
        ),
        PlainItem(
            heading="Communicate effectively — checked, not assumed",
            why="A harvested signature on an education form proves nothing was explained badly enough for the patient to notice -- it does not prove they understood.",
            body=[
                "Communication with the patients and/or families is done "
                "effectively. Understanding is checked -- the patient or "
                "family repeats the key point back in their own words. "
                "If they cannot, staff adapt the explanation and record "
                "that it was adapted.",
                "Published communication and health-literacy frameworks "
                "may inform how staff structure these conversations; "
                "they are not mandated acronyms this hospital must print "
                "on a form.",
            ],
            oe_code="PRE.4.f",
            technical_sources=[HA_LONGNECKER_SRC, MARCUS_EDUCATE_SRC, NOURI_RUDD_SRC, BADARUDEEN_SABHARWAL_SRC],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-6 (see the PRE.4 Records folder).",
    related_documents=[
        "Hospital's Informed Consent SOP (PRE.3)",
        "Hospital's Safe Administration of Medication SOP (MOM.6)",
        "Hospital's Assessment SOP (AAC.3)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an audit finds "
        "teaching was recorded without an understanding check, or if the "
        "sibling MOM, AAC or infection-control policies this SOP points "
        "to are revised."
    ),
    full_reference_list=[
        NABH_PRE_CITE.format(code="PRE.4"),
        HA_LONGNECKER_SRC,
        MARCUS_EDUCATE_SRC,
        NOURI_RUDD_SRC,
        BADARUDEEN_SABHARWAL_SRC,
    ],
)

SOPS.append(("SOP_PRE.4.a_to_f_information_education_communication.docx", PRE4))

# ---- PRE.4 Records -------------------------------------------------
_add("PRE.4", 1, RecordSpec(
    oe_code="PRE.4.a",
    oe_requirement="Patient and/or family are educated in a language and format that they can understand.",
    record_title="PRE.4 Record 01 — Language and format education record",
    what_is_this="This record is the proof the language and format actually used for teaching was recorded, including what was done for a patient who cannot read.",
    real_example="A patient who cannot read is taught verbally with family present as translator; the method is recorded.",
    why_nabh_asks="A patient taught in a language they do not follow has not actually been taught anything, whatever the record says.",
    how_to_fill=[
        ("Date", "Date of teaching."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Language Used", "As given."),
        ("Format", "Spoken, written, interpreter, family translator."),
        ("Taught By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.4")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Language Used", "Format", "Taught By"],
    worked_example_row=["WORKED EXAMPLE — 04-Jul-2026", "Lata Deshmukh / UID-01014", "Marathi", "Spoken, with family as translator", "Staff Nurse V. Joshi"],
), "language_format_education_record")

_add("PRE.4", 2, RecordSpec(
    oe_code="PRE.4.b",
    oe_requirement="Patient and/or family are educated about the safe and effective use of medication and the potential side effects of the medication, when appropriate.",
    record_title="PRE.4 Record 02 — Medication and side-effect education record",
    what_is_this="This record is the proof medication education was actually given at start, dose change or discharge -- not assumed because the prescription was written.",
    real_example="A patient started on a new antihypertensive is taught about the medicine, dosing and possible dizziness side effect before discharge.",
    why_nabh_asks="A patient who starts a new medicine without being told what to watch for has no way of recognising a side effect before it becomes an emergency.",
    how_to_fill=[
        ("Date", "Date of teaching."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Medicine", "What was taught about."),
        ("Occasion", "Start, dose change, or discharge."),
        ("Taught By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.4")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Medicine", "Occasion", "Taught By"],
    worked_example_row=["WORKED EXAMPLE — 05-Jul-2026", "Ganesh Pillai / UID-01020", "Amlodipine", "Discharge", "Pharmacist R. Shah"],
), "medication_side_effect_education_record")

_add("PRE.4", 3, RecordSpec(
    oe_code="PRE.4.c",
    oe_requirement="Patient and/or family are educated about food-drug interaction and about diet, nutrition and immunisations.",
    record_title="PRE.4 Record 03 — Food-drug, diet, nutrition and immunisation education record",
    what_is_this="This record is the proof teaching on food-drug interaction, diet or immunisation was actually given for the topics this hospital provides.",
    real_example="A patient on warfarin is taught about vitamin K-rich foods to moderate, and a diet chart is provided.",
    why_nabh_asks="A patient not told a new medicine interacts with a food they eat daily can undo the medicine's effect, or worse, without ever knowing why.",
    how_to_fill=[
        ("Date", "Date of teaching."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Topic", "Food-drug interaction, diet, nutrition, or immunisation."),
        ("Teaching Given (Y/N or Recorded Absence)", "Confirmed."),
        ("Taught By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.4")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Topic", "Teaching Given (Y/N or Recorded Absence)", "Taught By"],
    worked_example_row=["WORKED EXAMPLE — 06-Jul-2026", "Rekha Iyer / UID-01026", "Food-drug interaction (warfarin)", "Y", "Dietitian / Dr. Shah"],
), "food_drug_diet_nutrition_immunisation_education_record")

_add("PRE.4", 4, RecordSpec(
    oe_code="PRE.4.d",
    oe_requirement="Patient and/or family are educated about their specific disease process, complications and prevention strategies.",
    record_title="PRE.4 Record 04 — Disease-process education record",
    what_is_this="This record is the proof teaching was actually specific to this patient's condition -- not a generic handout counted as teaching.",
    real_example="A newly diagnosed diabetic patient is taught about their specific disease process, warning signs and prevention strategies, not handed a generic pamphlet alone.",
    why_nabh_asks="A generic poster about a condition is not education about this patient's condition -- a patient needs to hear what applies to them specifically.",
    how_to_fill=[
        ("Date", "Date of teaching."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Disease/Condition", "Specific to this patient."),
        ("Complications/Prevention Covered (Y/N)", "Confirmed."),
        ("Taught By", "Clinician."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.4")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Disease/Condition", "Complications/Prevention Covered (Y/N)", "Taught By"],
    worked_example_row=["WORKED EXAMPLE — 07-Jul-2026", "Suresh Pawar / UID-01032", "Type 2 diabetes (newly diagnosed)", "Y", "Dr. Nair"],
), "disease_process_education_record")

_add("PRE.4", 5, RecordSpec(
    oe_code="PRE.4.e",
    oe_requirement="Patient and/or family are educated about preventing healthcare associated infections.",
    record_title="PRE.4 Record 05 — HAI-prevention education record",
    what_is_this="This record is the proof patients and families were actually taught what they can do to help prevent healthcare-associated infection, at admission and again at discharge.",
    real_example="At admission, a patient is taught hand hygiene and to tell staff of any fever; the teaching is reinforced at discharge.",
    why_nabh_asks="A patient who does not know to tell staff about a fever or not to touch an IV line cannot help protect themselves from an infection this hospital is also working to prevent.",
    how_to_fill=[
        ("Date", "Date of teaching."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Occasion", "Admission or discharge."),
        ("Topics Covered", "Hand hygiene, device caution, fever reporting."),
        ("Taught By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.4")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Occasion", "Topics Covered", "Taught By"],
    worked_example_row=["WORKED EXAMPLE — 08-Jul-2026", "Anjali Kulkarni / UID-01038", "Admission", "Hand hygiene; fever reporting", "Ward Nurse D. Rao"],
), "hai_prevention_education_record")

_add("PRE.4", 6, RecordSpec(
    oe_code="PRE.4.f",
    oe_requirement="Communication with the patients and/or families is done effectively.",
    record_title="PRE.4 Record 06 — Communication effectiveness check record",
    what_is_this="This record is the proof understanding was actually checked by having the patient or family repeat the key point back -- not a harvested signature alone.",
    real_example="After discharge teaching, the patient repeats back the medication schedule correctly in her own words; where she could not, the nurse re-explained and re-checked.",
    why_nabh_asks="A harvested signature proves nothing was explained badly enough for the patient to notice -- it does not prove they understood.",
    how_to_fill=[
        ("Date", "Date of the encounter."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Topic Taught", "What was explained."),
        ("Understanding Confirmed (Y/N — Teach-back)", "Result."),
        ("Adapted If Not Understood (Y/N/NA)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.4"), HA_LONGNECKER_SRC],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Topic Taught", "Understanding Confirmed (Y/N — Teach-back)", "Adapted If Not Understood (Y/N/NA)"],
    worked_example_row=["WORKED EXAMPLE — 09-Jul-2026", "Pooja Mishra / UID-01044", "Discharge medication schedule", "Y", "NA"],
), "communication_effectiveness_check_record")

# ============================================================== PRE.5 ====
PRE5 = SOPSpecV2(
    sop_no="SOP-PRE.5",
    title="Information on Expected Costs",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» makes its pricing policy "
        "known across every setting, keeps a tariff list patients can "
        "actually see, explains expected costs before a patient enters a "
        "billable pathway, and tells families the same day when a change "
        "in the care plan changes the cost."
    ),
    purpose_trigger=(
        "A family receives a bill at discharge far larger than they "
        "expected, for a package procedure that was never explained "
        "beforehand. This SOP is what makes sure that conversation "
        "happens before the procedure, not as a surprise at the end."
    ),
    purpose_why=(
        "We do this because a signed consent form is not agreement to an "
        "unnamed bill, and a tariff hidden behind an accounts-office "
        "escort is not a tariff available to patients."
    ),
    purpose_text=(
        "To define how «Hospital Name» makes patients and families aware "
        "of its pricing policy across settings, keeps the relevant tariff "
        "list available, explains expected costs, and informs families "
        "about the financial implications when the care plan changes."
    ),
    scope_why="so a patient's expectation of cost is set honestly before they commit to care, not discovered only at the billing counter.",
    scope_text=(
        "Applies wherever a patient may incur a charge: registration, "
        "out-patient, emergency, intensive care where it exists, and "
        "in-patient. It binds billing and front-desk staff, registration, "
        "treating doctors when a plan change affects cost, the Patient "
        "Rights Officer as cost-information lead, and the Quality "
        "Coordinator."
    ),
    responsibility_why="a pricing policy that only billing staff know about is not awareness -- the patient has to actually be told before the bill arrives, not handed it afterward as a surprise.",
    responsibilities=[
        ("Medical Superintendent", "Is accountable for patient-facing cost information."),
        ("Patient Rights Officer (with Billing Lead)", "Holds pricing policy, tariff availability and explanation methods."),
        ("Billing / Front-desk Staff", "Make policy and tariff visible; explain expected costs."),
        ("Doctors and Nurses", "Tell financial implications when a plan change changes cost."),
        ("Quality Coordinator", "Audits this SOP quarterly."),
    ],
    items=[
        PlainItem(
            heading="Make the pricing policy known in every setting",
            why="A patient who finds out the pricing structure only after the bill arrives had no real chance to plan for it.",
            body=[
                "The patient and/or family members are made aware of "
                "the pricing policy in different settings -- out-"
                "patient, emergency, intensive care and in-patient.",
                "The pricing policy for each setting this hospital runs "
                "-- itemised, package, or a mix -- is held by billing "
                "and front-desk staff with the Patient Rights Officer. "
                "Patients are told at «registration or admission» in "
                "«Hindi and English». Intensive care not provided is a "
                "recorded absence. Emergency awareness may follow "
                "stabilisation; the delay and reason are recorded.",
            ],
            oe_code="PRE.5.a",
        ),
        PlainItem(
            heading="Keep the relevant tariff list available to patients",
            why="A tariff that exists but can only be seen with an accounts-office escort is not actually available to the patient who needs to see it.",
            body=[
                "The relevant tariff list is available to patients at "
                "«registration, the billing counter, and a board "
                "patients can read without an accounts-office escort as "
                "the only route». Which list applies in each setting is "
                "named on the board or handout.",
            ],
            oe_code="PRE.5.b",
        ),
        PlainItem(
            heading="Explain expected costs before the patient commits",
            why="\"Charges extra\" with no figure and no route to the tariff tells the patient nothing useful -- it is not an explanation, it is a warning with the actual information left out.",
            body=[
                "The patient and/or family members are explained about "
                "the expected costs. This happens when the patient "
                "enters a billable pathway, before a package procedure, "
                "and when asked -- by billing staff or the admitting "
                "nurse.",
                "A range or a package with inclusions and exclusions is "
                "an explanation; \"charges extra\" without a figure or a "
                "route to the tariff is not. The language used is one "
                "the family can understand.",
            ],
            oe_code="PRE.5.c",
        ),
        PlainItem(
            heading="Inform the family the same day when the care plan changes the cost",
            why="A family who learns about a cost change only at the final bill had no chance to ask questions or plan for it while the plan was still being decided.",
            body=[
                "Patient and/or family are informed about the financial "
                "implications when there is a change in the care plan. "
                "When the treating doctor changes the plan in a way "
                "that changes cost, the nurse or doctor tells the "
                "family the same day, and billing records it.",
            ],
            oe_code="PRE.5.d",
            boundary=[
                "The clinical decision to modify the care plan is owned by the Assessment SOP (AAC.3) and the Beliefs, Values and Decision-Making policy (PRE.2.o); this step is the money, not the clinical reasoning.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the PRE.5 Records folder).",
    related_documents=[
        "Policy on Beliefs, Values and Involvement in Decision-Making (PRE.2)",
        "Hospital's Assessment SOP (AAC.3)",
        "Hospital's Patient and Family Rights and Responsibilities SOP (PRE.1)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if an audit finds a "
        "cost explanation that was not actually given, or if the "
        "hospital's pricing structure or tariff changes."
    ),
    full_reference_list=[
        NABH_PRE_CITE.format(code="PRE.5"),
    ],
)

SOPS.append(("SOP_PRE.5.a_to_d_information_expected_costs.docx", PRE5))

# ---- PRE.5 Records -------------------------------------------------
_add("PRE.5", 1, RecordSpec(
    oe_code="PRE.5.a",
    oe_requirement="The patient and/or family members are made aware of the pricing policy in different settings (out-patient, emergency, ICU and in-patient).",
    record_title="PRE.5 Record 01 — Pricing-policy awareness record",
    what_is_this="This record is the proof the pricing policy was actually made known to the patient at registration or admission -- not left for the patient to discover on their own.",
    real_example="At admission, billing staff explain whether the stay will be itemised or package-billed.",
    why_nabh_asks="A patient who finds out the pricing structure only after the bill arrives had no real chance to plan for it.",
    how_to_fill=[
        ("Date", "Date of awareness."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Setting", "Out-patient, emergency, ICU, or in-patient."),
        ("Policy Explained (Itemised/Package/Mix)", "As given."),
        ("Informed By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.5")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Setting", "Policy Explained (Itemised/Package/Mix)", "Informed By"],
    worked_example_row=["WORKED EXAMPLE — 10-Jul-2026", "Yogesh Trivedi / UID-01050", "In-patient admission", "Package billing explained", "Billing Staff M. Shah"],
), "pricing_policy_awareness_record")

_add("PRE.5", 2, RecordSpec(
    oe_code="PRE.5.b",
    oe_requirement="The relevant tariff list is available to patients.",
    record_title="PRE.5 Record 02 — Tariff availability verification record",
    what_is_this="This record is the proof the current tariff list was actually visible and accessible at named locations -- not kept behind an accounts-office escort.",
    real_example="A monthly check confirms the current-dated tariff board at the billing counter is legible and up to date.",
    why_nabh_asks="A tariff that can only be seen with an accounts-office escort is not actually available to the patient who needs to see it.",
    how_to_fill=[
        ("Check Date", "Date of the check."),
        ("Location", "Registration, billing counter, board."),
        ("Tariff Version Date Current (Y/N)", "Confirmed."),
        ("Legible/Accessible (Y/N)", "Confirmed."),
        ("Checked By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.5")],
    column_headers=["Check Date", "Location", "Tariff Version Date Current (Y/N)", "Legible/Accessible (Y/N)", "Checked By"],
    worked_example_row=["WORKED EXAMPLE — 11-Jul-2026", "Billing counter board", "Y", "Y", "Billing Lead S. Rao"],
), "tariff_availability_verification_record")

_add("PRE.5", 3, RecordSpec(
    oe_code="PRE.5.c",
    oe_requirement="The patient and/or family members are explained about the expected costs.",
    record_title="PRE.5 Record 03 — Expected-cost explanation record",
    what_is_this="This record is the proof an actual cost explanation -- a range or package with inclusions and exclusions -- was given before the patient entered a billable pathway, not a vague \"charges extra\".",
    real_example="Before a package delivery procedure, billing staff explain the package price, what is included, and what is billed separately.",
    why_nabh_asks="\"Charges extra\" with no figure and no route to the tariff tells the patient nothing useful.",
    how_to_fill=[
        ("Date", "Date of explanation."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Billable Event", "Procedure or admission."),
        ("Range/Package Given (Y/N)", "Confirmed."),
        ("Explained By", "Billing staff or admitting nurse."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.5")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Billable Event", "Range/Package Given (Y/N)", "Explained By"],
    worked_example_row=["WORKED EXAMPLE — 12-Jul-2026", "Preeti Saxena / UID-01056", "Normal delivery package", "Y", "Billing Staff M. Shah"],
), "expected_cost_explanation_record")

_add("PRE.5", 4, RecordSpec(
    oe_code="PRE.5.d",
    oe_requirement="Patient and/or family are informed about the financial implications when there is a change in the care plan.",
    record_title="PRE.5 Record 04 — Care-plan-change financial implication record",
    what_is_this="This record is the proof the family was actually told the same day when a care-plan change affected the cost -- not left to discover it at the final bill.",
    real_example="When a patient's plan is revised to add an ICU stay, the nurse informs the family of the added cost the same day and billing updates the estimate.",
    why_nabh_asks="A family who learns about a cost change only at the final bill had no chance to ask questions or plan for it while the plan was still being decided.",
    how_to_fill=[
        ("Date", "Date of the plan change."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Plan Change", "What changed."),
        ("Family Informed Same Day (Y/N)", "Confirmed."),
        ("Informed By / Billing Updated (Y/N)", "Staff member and confirmation."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.5")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Plan Change", "Family Informed Same Day (Y/N)", "Informed By / Billing Updated (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 13-Jul-2026", "Ashwin Bhatt / UID-01062", "ICU stay added to plan", "Y", "Dr. Nair / Billing Staff M. Shah — Y"],
), "care_plan_change_financial_implication_record")

# ============================================================== PRE.6 ====
PRE6 = SOPSpecV2(
    sop_no="SOP-PRE.6",
    title="Patient Feedback and Complaint Redressal",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» captures patient feedback "
        "and patient experience, redresses complaints through a route "
        "that does not go only to the person complained of, makes "
        "patients and families aware of how to give feedback or lodge a "
        "complaint, and reviews and analyses feedback and complaints "
        "within a defined time frame with corrective action where it is "
        "warranted."
    ),
    purpose_trigger=(
        "A patient wants to complain about a nurse's conduct, and the "
        "only person who would receive that complaint is the nurse "
        "herself. This SOP is what makes sure there is always another "
        "route -- the complaint reaches someone other than the person it "
        "is about."
    ),
    purpose_why=(
        "We do this because an unopened complaint box is not a mechanism, "
        "and a complaint route that goes only to the person complained of "
        "will almost never actually be used."
    ),
    purpose_text=(
        "To define how «Hospital Name» captures feedback including "
        "patient satisfaction, captures the patient experience, redresses "
        "complaints as per a defined mechanism, makes patients and "
        "families aware of that procedure, and reviews and analyses "
        "feedback and complaints within a defined time frame with "
        "corrective and preventive action where appropriate."
    ),
    scope_why="so every patient knows there is a real route for feedback and complaints, not a box that is never opened.",
    scope_text=(
        "Applies wherever a patient or family can give feedback or lodge "
        "a complaint: registration, out-patient, emergency, in-patient, "
        "day-care, and after discharge if this hospital accepts "
        "post-discharge feedback. It binds staff who collect feedback, "
        "the grievance and feedback officer who receives complaints, the "
        "Patient Rights Officer, and the Medical Superintendent who "
        "reviews analysis."
    ),
    responsibility_why="a complaint route that depends on the complained-of person forwarding it themselves is not a route at all -- it needs a named alternative receiver built in from the start.",
    responsibilities=[
        ("Medical Superintendent", "Is accountable for capture, redressal, awareness and analysis; reviews the complaint log monthly and signs corrective action."),
        ("Grievance and Feedback Officer", "Receives complaints unless the alleged actor is this officer, in which case the Medical Superintendent receives them; authors feedback, experience, redressal and awareness methods with the Patient Rights Officer."),
        ("Patient Rights Officer", "Holds display of the procedure and links rights-violation complaints to the violation log."),
        ("Registration and Ward Staff", "Collect feedback and tell patients the procedure."),
        ("Quality Coordinator", "Audits this SOP quarterly."),
    ],
    items=[
        PlainItem(
            heading="Capture feedback, including patient satisfaction",
            why="Feedback that is never asked for is feedback this hospital will never get -- a dissatisfied patient who is never asked simply leaves and tells someone else instead.",
            body=[
                "The organisation has a mechanism to capture feedback "
                "from patients, which includes patient satisfaction. "
                "Feedback is captured by «a form at registration, a "
                "post-discharge phone call, and a conversation when the "
                "patient is leaving the ward».",
                "Dissatisfied feedback that asks for redressal is also "
                "treated as a complaint and enters the complaint route "
                "below.",
            ],
            oe_code="PRE.6.a",
        ),
        PlainItem(
            heading="Capture the patient experience, not only a satisfaction score",
            why="A patient can be satisfied overall and still have waited three hours in pain -- a satisfaction score alone hides exactly the detail this hospital needs to fix.",
            body=[
                "The organisation has a mechanism to capture the patient "
                "experience -- what actually happened to this patient, "
                "covering four things:",
                "1. Wait time.",
                "2. Dignity.",
                "3. Communication.",
                "4. Pain control.",
                "This is not only whether they would recommend the "
                "hospital, and is distinct from the satisfaction score "
                "above.",
            ],
            oe_code="PRE.6.b",
        ),
        PlainItem(
            heading="Redress complaints through a route not limited to the person complained of, and make patients aware of it",
            why="A patient who does not know a complaint route exists, or who can only reach the person they want to complain about, will simply stay silent and leave dissatisfied.",
            body=[
                "The organisation redresses patient complaints as per "
                "the defined mechanism. Patients and family members are "
                "made aware of the procedure for giving feedback and/or "
                "lodging complaints.",
                "Complaints are received by the grievance and feedback "
                "officer using «the complaint box, the helpline number "
                "on the display board, and a written form at "
                "registration». The route is not only the person "
                "complained of. Investigation, the outcome communicated "
                "to the complainant, and the record of both are defined "
                "in writing held with the Patient Rights Officer.",
                "Patients and families are told the procedure at entry, "
                "during stay, and at discharge if post-discharge "
                "feedback is accepted, in «Hindi and English».",
            ],
            oe_code="PRE.6.c",
            technical_sources=[READER_COMPLAINT_SRC],
            boundary=[
                "A complaint that alleges a rights violation also enters the violation log under the Patient and Family Rights and Responsibilities SOP (PRE.1.d); that SOP's leadership review still owns rights-violation review specifically.",
            ],
        ),
        PlainItem(
            heading="Review and analyse within a defined time frame, with corrective action where warranted",
            why="A complaint log that nobody above the front desk ever opens cannot catch a pattern -- a single complaint is one patient's bad experience, but a repeated one is a system this hospital needs to fix.",
            body=[
                "Feedback and complaints are reviewed and/or analysed "
                "within a defined time frame, and corrective and/or "
                "preventive action is taken based on the analysis where "
                "appropriate.",
                "The Medical Superintendent reviews the complaint log "
                "«monthly». Corrective and preventive action is dated "
                "with a named owner.",
            ],
            oe_code="PRE.6.d",
            boundary=[
                "Rights violations are analysed separately as violations under PRE.1.e; this step analyses feedback and complaints as feedback and complaints.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-4 (see the PRE.6 Records folder).",
    related_documents=[
        "Hospital's Patient and Family Rights and Responsibilities SOP (PRE.1)",
        "Hospital's Information on Expected Costs SOP (PRE.5)",
        "Hospital's Beliefs, Values and Involvement in Decision-Making policy (PRE.2)",
    ],
    review_text=(
        "This SOP is reviewed annually, or sooner if a complaint could "
        "only reach the person complained of, a monthly review was "
        "missed, or the sibling PRE.1 violation-log process this SOP "
        "links to is revised."
    ),
    full_reference_list=[
        NABH_PRE_CITE.format(code="PRE.6"),
        READER_COMPLAINT_SRC,
    ],
)

SOPS.append(("SOP_PRE.6.a_to_d_patient_feedback_complaint_redressal.docx", PRE6))

# ---- PRE.6 Records -------------------------------------------------
_add("PRE.6", 1, RecordSpec(
    oe_code="PRE.6.a",
    oe_requirement="The organisation has a mechanism to capture feedback from patients, which includes patient satisfaction.",
    record_title="PRE.6 Record 01 — Patient feedback and satisfaction capture log",
    what_is_this="This record is the proof feedback was actually collected through the defined channels -- not left to whichever patient happened to volunteer an opinion.",
    real_example="A post-discharge phone call collects a satisfaction rating and a free-text comment, logged the same day.",
    why_nabh_asks="Feedback that is never asked for is feedback this hospital will never get -- a dissatisfied patient who is never asked simply leaves and tells someone else instead.",
    how_to_fill=[
        ("Date", "Date of capture."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Channel", "Form, phone call, or ward conversation."),
        ("Satisfaction Rating / Comment", "As given."),
        ("Flagged as Complaint (Y/N)", "If dissatisfied feedback asked for redressal."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.6")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Channel", "Satisfaction Rating / Comment", "Flagged as Complaint (Y/N)"],
    worked_example_row=["WORKED EXAMPLE — 14-Jul-2026", "Nikhil Bose / UID-01068", "Post-discharge phone call", "4/5 — \"staff were attentive\"", "N"],
), "patient_feedback_satisfaction_capture_log")

_add("PRE.6", 2, RecordSpec(
    oe_code="PRE.6.b",
    oe_requirement="The organisation has a mechanism to capture the patient experience.",
    record_title="PRE.6 Record 02 — Patient experience capture record",
    what_is_this="This record is the proof experience detail -- wait time, dignity, communication, pain control -- was actually captured, distinct from the satisfaction score alone.",
    real_example="A ward exit conversation captures that a patient waited 90 minutes for pain medication, flagged separately from their overall satisfaction rating.",
    why_nabh_asks="A patient can be satisfied overall and still have waited three hours in pain -- a satisfaction score alone hides exactly the detail this hospital needs to fix.",
    how_to_fill=[
        ("Date", "Date of capture."),
        ("Patient (Identifier 1) / UID (Identifier 2)", "The patient."),
        ("Experience Dimension", "Wait time, dignity, communication, pain control."),
        ("What Happened", "Specific detail."),
        ("Captured By", "Staff member."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.6")],
    column_headers=["Date", "Patient (Identifier 1) / UID (Identifier 2)", "Experience Dimension", "What Happened", "Captured By"],
    worked_example_row=["WORKED EXAMPLE — 15-Jul-2026", "Swati Kapoor / UID-01074", "Pain control / wait time", "Waited 90 minutes for pain medication after request", "Ward Nurse T. Kulkarni"],
), "patient_experience_capture_record")

_add("PRE.6", 3, RecordSpec(
    oe_code="PRE.6.c",
    oe_requirement="The organisation redresses patient complaints as per the defined mechanism. Patient and/or family members are made aware of the procedure for giving feedback and/or lodging complaints.",
    record_title="PRE.6 Record 03 — Complaint redressal and awareness log",
    what_is_this="This record is the proof every complaint was actually investigated and given an outcome communicated back to the complainant -- not logged and left open indefinitely.",
    real_example="A complaint about delayed response to a call bell is investigated, found accurate, and the family is told the corrective action taken.",
    why_nabh_asks="A patient who does not know a complaint route exists, or who can only reach the person they want to complain about, will simply stay silent and leave dissatisfied.",
    how_to_fill=[
        ("Date Received", "Date lodged."),
        ("Complaint (Short)", "What was alleged."),
        ("Received By", "Grievance and feedback officer, or Medical Superintendent if officer is the one accused."),
        ("Investigation / Outcome", "Finding and action."),
        ("Communicated to Complainant (Y/N, Date)", "Confirmed."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.6"), READER_COMPLAINT_SRC],
    column_headers=["Date Received", "Complaint (Short)", "Received By", "Investigation / Outcome", "Communicated to Complainant (Y/N, Date)"],
    worked_example_row=["WORKED EXAMPLE — 16-Jul-2026", "Delayed response to call bell", "Grievance and Feedback Officer A. Kulkarni", "Confirmed — short-staffed shift; roster adjusted", "Y — 20-Jul-2026"],
), "complaint_redressal_awareness_log")

_add("PRE.6", 4, RecordSpec(
    oe_code="PRE.6.d",
    oe_requirement="Feedback and complaints are reviewed and/or analysed within a defined time frame. Corrective and/or preventive action(s) are taken based on the analysis where appropriate.",
    record_title="PRE.6 Record 04 — Monthly feedback and complaint review and CAPA log",
    what_is_this="This record is the proof the Medical Superintendent actually reviewed the complaint log every month and produced dated corrective action with an owner -- not a log that sits unreviewed between complaints.",
    real_example="The monthly review finds three complaints about wait time in the same month; the Medical Superintendent orders a staffing review for the affected shift.",
    why_nabh_asks="A complaint log that nobody above the front desk ever opens cannot catch a pattern -- a repeated complaint is a system this hospital needs to fix, not just one patient's bad day.",
    how_to_fill=[
        ("Review Month", "Which month."),
        ("Complaints/Feedback Reviewed", "Number."),
        ("Pattern Found (if any)", "Repeated issue."),
        ("CAPA / Owner / Due Date", "Action decided."),
        ("Reviewed By", "Medical Superintendent."),
    ],
    verified_sources=[NABH_PRE_CITE.format(code="PRE.6")],
    column_headers=["Review Month", "Complaints/Feedback Reviewed", "Pattern Found (if any)", "CAPA / Owner / Due Date", "Reviewed By"],
    worked_example_row=["WORKED EXAMPLE — June 2026", "3", "Wait-time complaints, same evening shift", "Staffing review; Nursing Superintendent / 31-Jul-2026", "Medical Superintendent"],
), "monthly_feedback_complaint_review_capa_log")

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
