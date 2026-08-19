# -*- coding: utf-8 -*-
"""PRE.2 v2 — beliefs, values and involvement in decision-making.

Shape follows PRE.1 v2 / FMS.5 v2.2 (section list and order only). Wording is built
from PRE.2 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed pages 86–87 / PDF indices 92–93.
Chapter intent: printed page 85 / PDF index 91.

Does NOT overwrite pre2_draft.json or build_pre2.py. No SQL. No Supabase insert.
No stop-work section. Sixteen OEs clustered into nine What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PRE.2"
CHAPTER = "PRE"
OE_CODES = [
    "PRE.2.a", "PRE.2.b", "PRE.2.c", "PRE.2.d", "PRE.2.e", "PRE.2.f",
    "PRE.2.g", "PRE.2.h", "PRE.2.i", "PRE.2.j", "PRE.2.k", "PRE.2.l",
    "PRE.2.m", "PRE.2.n", "PRE.2.o", "PRE.2.p",
]
POLICY_TITLE = "Beliefs, Values and Involvement in Decision-Making"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PRE v2 template: FMS.5 v2.2 shape, plain English, PRE roles, nine steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Patient and family rights support individual beliefs and values and involve the patient "
    "and family in decision-making — not only on a display board they never read again."
)

PURPOSE = f"""This policy says what patient and family rights include at {HOSPITAL} when beliefs, values and decision-making are in question, and how those rights are exercised in care.

It covers sixteen elements the standard lists: values and spiritual needs; dignity and privacy; protection from neglect or abuse; confidentiality; refusal and additional opinion; the right that consent is obtained before named high-risk acts; complaint and cost information rights; access to records; treating-doctor and care-plan information; control of what is told to family; explanations of proposed care and expected results; care-plan consultation; and multidisciplinary counselling when appropriate.

The chapter intent is that patient and family rights support individual beliefs, values and involve the patient and family in decision-making processes. A list that exists only so PRE.1 can display it, or a care plan written without the patient, is not that intent.

This policy owns what the rights include and how they are exercised. PRE.1 owns that a documented set exists, is displayed, promoted and protected. PRE.3 owns consent method. PRE.5 owns cost information. PRE.6 owns complaint redressal.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every patient and family at {HOSPITAL} and to every staff member who must respect the rights listed here: registration, treating doctors, nurses, the {D('Patient Rights Officer')}, billing staff where cost is a right, and the {D('counsellor')} where multidisciplinary counselling is provided.

It covers the sixteen rights and involvement elements PRE.2.a–p name. It does not cover how the set is displayed (PRE.1), how consent is obtained (PRE.3), how expected costs are explained (PRE.5), or how complaints are redressed (PRE.6).

Boundaries with other policies of {HOSPITAL}:

- PRE.1 owns documentation, display, awareness, promotion, protection, violation report and leadership CAPA. This policy owns the content of the list PRE.1 displays.
- PRE.2.g is the right that informed consent is obtained before transfusion, anaesthesia, surgery, research and other invasive or high-risk treatment. PRE.3 owns the method. COP.5, COP.9, COP.10 and COP.11 own that the relevant consent happened before those acts.
- PRE.2.e refusal is the right. PRE.3 records that consent was not given.
- PRE.2.h is the right to complain and to information on how to voice a complaint. PRE.6 owns the mechanism.
- PRE.2.i is the right to information on expected cost. PRE.5 owns the pricing policy and explanation.
- PRE.2.j access to clinical records during care. IMS owns the record file. AAC.8 owns the discharge summary the patient takes away.
- PRE.2.o care plan prepared and modified in consultation. AAC.3 owns the clinical care plan. PRE.5.d owns financial implications of a change.
- PRE.2.p multidisciplinary counselling when appropriate. COP.6.e owns periodic ICU family counselling where ICU exists.
- PRE.2.d confidentiality as a patient right. IMS owns how the record is kept confidential as a file.
- Capacity and who may consent when the patient cannot are PRE.3.c. The Mental Healthcare Act, 2017 is not applied as a blanket to this rights list."""

POLICY_STATEMENT = f"""{HOSPITAL} includes in patient and family rights the elements PRE.2.a–p name, and exercises them in the course of care — not only on a charter in the quality office.

{HOSPITAL} involves the patient and/or family in decision-making, including the care plan and multidisciplinary counselling when appropriate.

{HOSPITAL} does not treat the PRE.1 display board as a substitute for these rights being exercised, and does not rewrite PRE.3, PRE.5, PRE.6, COP.5/9/10/11, AAC.3 or AAC.8 inside this list."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no ward convenience exception.

1. Keeping the rights list only in an office patients never enter, or displaying rights this hospital's patients cannot read or hear.
2. Examining or discussing a patient without dignity or privacy when those are rights in the documented set.
3. Ignoring a refusal of treatment after information, or punishing a patient for asking for another opinion.
4. Withholding the treating doctor's name, care-plan information, or access to records when those are rights — except where the patient determines that information is not given to family (PRE.2.l).
5. Preparing or changing a care plan without consulting the patient and/or family when consultation is required.
6. Sending a complaint or cost question only to the person the patient is complaining about, when those are rights listed here and PRE.6 or PRE.5 own the method.
7. Applying a Mental Healthcare Act process to every unconscious patient instead of the incapacity description in PRE.3.
8. Counting a poster as exercise of the right to be explained about proposed care, expected results, or multidisciplinary counselling.

Staff who see one of these acts report it the same shift to the {D('Patient Rights Officer')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Values, beliefs, preferences, culture and spiritual needs

Patients and family rights include respecting values and beliefs, any special preferences, cultural needs, and responding to requests for spiritual needs.

The {D('Patient Rights Officer')} holds how those are identified and responded to in the course of care. Registration staff and nurses ask at or after entry in {D('Hindi and English')} (or the language the patient uses). Spiritual requests are passed to the person this hospital names — {D('the ward nurse or the counsellor')} — not ignored as "not medical."

WHO Human rights and health (2017), chapter 9, and Olejarczyk and Young (2021), chapter 15, may inform why a rights document exists. They are not pasted as this hospital's charter. A copied religion table is not a NABH mandate.""",

f"""5.2 Dignity, privacy, protection and confidentiality

Patient and family rights include respect for personal dignity and privacy during examination, procedures and treatment; protection from neglect or abuse; and treating patient information as confidential.

Treating doctors and nurses protect dignity and privacy with screens, closed doors and low voices. A corridor discussion of diagnosis is a defect. A suspicion of neglect or abuse is reported under PRE.1.d when it is a rights violation. Confidentiality as a record-keeping system remains IMS; this step is the right. Patient information is not left open at a public desk.""",

f"""5.3 Refusal of treatment and additional opinion

Patient and family rights include the refusal of treatment and a right to seek an additional opinion regarding clinical care.

Refusal is received without punishment and recorded as refusal — PRE.3 records that consent was not given. An additional opinion is facilitated as this hospital can arrange: {D('referral letter and appointment where the hospital has a tie-up; otherwise an honest statement of what the hospital cannot arrange')}. This hospital does not print a named second-hospital list as a NABH mandate.""",

f"""5.4 Right that informed consent is obtained before named acts

Patient and family rights include informed consent before the transfusion of blood and blood components, anaesthesia, surgery, initiation of any research protocol and any other invasive/high-risk procedures/treatment.

This step is a pointer. The method is PRE.3. That consent happened before transfusion, sedation, anaesthesia or surgery remains COP.5, COP.9, COP.10 and COP.11. Staff name this right when consent is about to be taken. A class the service directory does not provide is a recorded absence, not a copied consent-right SOP.""",

f"""5.5 Right to complain and to expected-cost information

Patient and family rights include a right to complain and information on how to voice a complaint, and information on the expected cost of the treatment.

This step is a pointer. Complaint mechanism and awareness of the procedure are PRE.6. Pricing policy, tariff and expected-cost explanation are PRE.5. Staff name these rights when a complaint or cost question arises. Billing staff do not withhold cost information that is a patient right.""",

f"""5.6 Access to records and who receives information

Patient and family rights include access to their clinical records, and determining what information regarding their care would be provided to self and family.

Access during care is given by {D('the treating doctor or the Patient Rights Officer on request')}, in a place that protects privacy. The discharge summary the patient takes away remains AAC.8. The record as a file remains IMS. A relative who demands information against the patient's determination does not meet PRE.2.l.""",

f"""5.7 Treating doctor, care plan, progress and healthcare needs

Patient and family rights include information on the name of the treating doctor, care plan, progress and information on their health care needs.

The treating team tells the patient and family who is treating them, how the plan is progressing, and what healthcare needs apply. Ongoing education about healthcare needs as a teaching method remains PRE.4. This step is the right to be told who is treating them and how they are doing.""",

f"""5.8 Explanation of proposed care and expected results

The patient and/or family members are explained about the proposed care, including the risks, alternatives and benefits, and about the expected results and complications.

Clinicians give those explanations in the course of decision-making. The consent conversation that must include procedure, risks, benefits, alternatives and who will perform remains PRE.3.b. Disease-process education remains PRE.4.d. They may use the same language; they are not only the consent form.""",

f"""5.9 Care plan consultation and multidisciplinary counselling

The care plan is prepared and modified in consultation with the patient and/or family members. The patient and/or family members are provided multidisciplinary counselling when appropriate.

The treating team consults the patient and/or family when the plan is prepared or modified. AAC.3 owns the care plan as a clinical document. PRE.5.d owns the financial implications of a change. The {D('counsellor')} or treating team provides multidisciplinary counselling when appropriate — {D('for example before major surgery, on request, or when the treating doctor documents that it is needed')}. COP.6.e owns periodic ICU family counselling where ICU exists. Unused ICU is a recorded absence, not a copied SOP.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that rights PRE.2.a–p are exercised in care, not only displayed.

Patient Rights Officer
- Keeps the documented rights set aligned with PRE.1's display and holds the methods in sections 5.1–5.9.
- Receives reports when a listed right was displayed but not exercised.

Front-office / Registration In-Charge
- Helps identify values, beliefs and language needs at entry.

Treating doctors and ward nurses
- Protect dignity, privacy, confidentiality, refusal, consultation and the pointers to consent, costs and complaints.

Counsellor (where this hospital provides counselling)
- Provides multidisciplinary counselling when appropriate under section 5.9.

Billing / front-desk lead
- Does not withhold cost information that is a patient right; detailed tariff method stays with PRE.5.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA when the same right is not exercised twice in the same setting."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at records and at the floor.

What is monitored each quarter:

- Sample charts showing rights were exercised, not only displayed.
- Dignity and privacy at examination; refusal received without punishment.
- Pointers to PRE.3, PRE.5 and PRE.6 not rewritten as those methods.
- Care-plan consultation and counselling records where appropriate.
- No MHCA process applied as a blanket to this list.

Root-cause analysis is required when the same right is not exercised twice in the same setting within six months.

This policy is reviewed {D('annually')}, and sooner when PRE.1, PRE.3, PRE.4, PRE.5, PRE.6 or AAC.3 are revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff and registration staff are trained on this policy at induction and {D('once a year')} after that. Training covers the rights list, how to exercise it in care, and where PRE.3, PRE.5 and PRE.6 own the method.

Staff acknowledgement

I have read this Beliefs, Values and Involvement in Decision-Making policy of {HOSPITAL}. I will exercise the rights in the documented set during care, not only point to the display board.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Patient Rights Officer holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PRE/POL/02"),
    version=VERSION,
    prepared_by=D("Patient Rights Officer"),
    extra_lines=f"Display languages: {D('Hindi and English')}",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Rights and Education chapter, standard PRE.2.
- Human rights and health, World Health Organization (2017) — chapter 9; framework for rights content; not pasted as this hospital's charter.
- Olejarczyk JP and Young M, Patient Rights and Ethics (2021) — chapter 15; framework; not pasted as a protocol.
- Internal documents of {HOSPITAL}: the documented rights set (with PRE.1); methods at sections 5.1–5.9; informed-consent, expected-costs, feedback-and-complaints, education, assessment, discharge, transfusion, sedation, anaesthesia, procedures and ICU policies."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Patient Rights Officer and the Quality Coordinator.

Copies issued to: registration; out-patient; emergency; every in-patient ward; ICU where it exists; nursing administration; counselling room where it exists.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

The documented rights set is held at points of entry and on the wards. When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
ICU — intensive care unit
IMS — Information Management System (NABH chapter; not yet drafted)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH SHCO chapter 4)
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PRE.2.a",
        "requirement": "Patients and family rights include respecting values and beliefs, any special preferences, cultural needs, and responding to requests for spiritual needs.",
        "steps": "Statement of intent; Section 3; 5.1 Values, beliefs, preferences, culture and spiritual needs; Section 4 items 1, 8",
        "responsible": "Patient Rights Officer (method); registration staff and nurses (identify and respond)",
        "records": [
            "Written method for identifying and responding to values, beliefs, special preferences, cultural needs and spiritual-need requests.",
            "Sample records showing a response rather than a copied religion table.",
            "Induction and annual briefing records for staff who receive patients.",
            "Quarterly audit sample showing the right was exercised in care.",
        ],
    },
    {
        "oe_code": "PRE.2.b",
        "requirement": "Patient and family rights include respect for personal dignity and privacy during examination, procedures and treatment.",
        "steps": "Section 3; 5.2 Dignity, privacy, protection and confidentiality; Section 4 item 2",
        "responsible": "Treating doctors and nurses (apply); Patient Rights Officer (method)",
        "records": [
            "Written expectation of dignity and privacy during examination, procedures and treatment.",
            "Sample practice notes or incident files showing a screen or equivalent.",
            "Quarterly audit sample at bedside.",
            "Violation log entries where dignity or privacy failed.",
        ],
    },
    {
        "oe_code": "PRE.2.c",
        "requirement": "Patient and family rights include protection from neglect or abuse.",
        "steps": "Section 3; 5.2 Dignity, privacy, protection and confidentiality; Section 4 item 2",
        "responsible": "All staff (protect); Patient Rights Officer (method); PRE.1.d (violation report)",
        "records": [
            "Written method for protection from neglect or abuse and how a suspicion is reported.",
            "Records showing a rights-violation suspicion also entered PRE.1.d where applicable.",
            "Quarterly audit sample.",
            "CAPA when neglect or abuse was suspected and not reported.",
        ],
    },
    {
        "oe_code": "PRE.2.d",
        "requirement": "Patient and family rights include treating patient information as confidential.",
        "steps": "Section 3; 5.2 Dignity, privacy, protection and confidentiality; Section 4 item 2",
        "responsible": "All staff (confidentiality); IMS owns the record file",
        "records": [
            "Written method for confidentiality as a patient right.",
            "Recorded split that IMS owns the record as a file.",
            "Sample defects (open record at a public desk) treated as violations.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.2.e",
        "requirement": "Patient and family rights include the refusal of treatment.",
        "steps": "Section 3; 5.3 Refusal and additional opinion; Section 4 item 3",
        "responsible": "Treating doctors (receive refusal); PRE.3 (consent not given record)",
        "records": [
            "Written method for receiving and recording refusal without punishment.",
            "Sample refusal records with PRE.3 cross-reference.",
            "Quarterly audit sample.",
            "Staff briefing that refusal is a right, not a discipline matter.",
        ],
    },
    {
        "oe_code": "PRE.2.f",
        "requirement": "Patient and family rights include a right to seek an additional opinion regarding clinical care.",
        "steps": "Section 3; 5.3 Refusal and additional opinion; Section 4 item 3",
        "responsible": "Treating doctor (facilitate); Patient Rights Officer (method)",
        "records": [
            "Written method for facilitating an additional opinion, including what this hospital can and cannot arrange.",
            "Sample referral or facilitation records.",
            "Quarterly audit sample.",
            "Record that no named second-hospital list is printed as a NABH mandate.",
        ],
    },
    {
        "oe_code": "PRE.2.g",
        "requirement": "Patient and family rights include informed consent before the transfusion of blood and blood components, anaesthesia, surgery, initiation of any research protocol and any other invasive/high-risk procedures/treatment.",
        "steps": "Section 3; 5.4 Right that informed consent is obtained; Section 4 item 4",
        "responsible": "PRE.3 (method); COP.5/9/10/11 (consent happened); Patient Rights Officer (pointer)",
        "records": [
            "Recorded pointer that PRE.3 owns consent method and COP.5/9/10/11 own that consent happened.",
            "Method for making this right known as a right without rewriting PRE.3.",
            "Recorded absence against service directory for a class not provided.",
            "Quarterly audit sample of the pointer, not a copied consent SOP.",
        ],
    },
    {
        "oe_code": "PRE.2.h",
        "requirement": "Patient and family rights include a right to complain and information on how to voice a complaint.",
        "steps": "Section 3; 5.5 Complaint and cost rights; Section 4 item 5",
        "responsible": "PRE.6 (mechanism); Patient Rights Officer (pointer)",
        "records": [
            "Recorded pointer that PRE.6 owns complaint mechanism and awareness.",
            "Method for making this right known as a right.",
            "Quarterly audit sample.",
            "Evidence staff name the right when a complaint is invited.",
        ],
    },
    {
        "oe_code": "PRE.2.i",
        "requirement": "Patient and family rights include information on the expected cost of the treatment.",
        "steps": "Section 3; 5.5 Complaint and cost rights; Section 4 item 5",
        "responsible": "PRE.5 (method); billing staff (do not withhold); Patient Rights Officer (pointer)",
        "records": [
            "Recorded pointer that PRE.5 owns pricing policy, tariff and explanation.",
            "Method for making this right known as a right.",
            "Quarterly audit sample.",
            "Evidence billing did not withhold cost information.",
        ],
    },
    {
        "oe_code": "PRE.2.j",
        "requirement": "Patient and family rights include access to their clinical records.",
        "steps": "Section 3; 5.6 Access to records and who receives information; Section 4 item 6",
        "responsible": "Treating doctor or Patient Rights Officer (access); IMS/AAC.8 (file and summary)",
        "records": [
            "Written method for access to clinical records during care.",
            "Recorded split that AAC.8 owns discharge summary and IMS owns the file.",
            "Sample access records with privacy protected.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.2.k",
        "requirement": "Patient and family rights include information on the name of the treating doctor, care plan, progress and information on their health care needs.",
        "steps": "Section 3; 5.7 Treating doctor, care plan, progress; Section 4 item 7",
        "responsible": "Treating team (inform); PRE.4 (education method)",
        "records": [
            "Written method for telling treating doctor's name, care plan, progress and healthcare needs.",
            "Recorded split that PRE.4 owns ongoing education method.",
            "Sample ward or clinic notes.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.2.l",
        "requirement": "Patient rights include determining what information regarding their care would be provided to self and family.",
        "steps": "Section 3; 5.6 Access to records and who receives information; Section 4 item 6",
        "responsible": "Staff who disclose information (apply patient's determination)",
        "records": [
            "Written method for the patient determining what information is provided to self and family.",
            "Sample records showing a relative's demand against that determination was refused.",
            "Quarterly audit sample.",
            "Staff briefing on PRE.2.l versus PRE.2.j.",
        ],
    },
    {
        "oe_code": "PRE.2.m",
        "requirement": "The patient and/or family members are explained about the proposed care, including the risks, alternatives and benefits.",
        "steps": "Section 3; 5.8 Explanation of proposed care and expected results; Section 4 item 8",
        "responsible": "Clinicians (explain); PRE.3/PRE.4 (consent and education splits)",
        "records": [
            "Written method for explaining proposed care including risks, alternatives and benefits.",
            "Recorded split that PRE.3.b is the consent conversation and PRE.4.d is disease-process education.",
            "Sample explanation notes.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.2.n",
        "requirement": "The patient and/or family members are explained about the expected results and complications.",
        "steps": "Section 3; 5.8 Explanation of proposed care and expected results; Section 4 item 8",
        "responsible": "Clinicians (explain expected results and complications)",
        "records": [
            "Written method for explaining expected results and complications.",
            "Same PRE.3.b/PRE.4.d split as PRE.2.m.",
            "Sample explanation notes.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.2.o",
        "requirement": "The care plan is prepared and modified in consultation with the patient and/or family members.",
        "steps": "Section 3; 5.9 Care plan consultation and counselling; Section 4 item 8",
        "responsible": "Treating team (consult); AAC.3 (plan document); PRE.5.d (financial implications)",
        "records": [
            "Written method for consulting patient and/or family when the plan is prepared or modified.",
            "Sample care plans showing consultation.",
            "Recorded split that AAC.3 owns clinical plan and PRE.5.d owns money of a change.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.2.p",
        "requirement": "The patient and/or family members are provided multidisciplinary counselling when appropriate.",
        "steps": "Section 3; 5.9 Care plan consultation and counselling; Section 4 item 8",
        "responsible": "Counsellor or treating team (when appropriate); COP.6.e (ICU periodicity)",
        "records": [
            "Written description of when multidisciplinary counselling is provided and by whom.",
            "Recorded split that COP.6.e owns periodic ICU family counselling where ICU exists.",
            "Recorded absence against service directory if ICU is not provided.",
            "Quarterly audit sample of counselling when documented as appropriate.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PRE.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Patient and family rights support individual beliefs, values and involve the patient and family in decision-making processes." PRE.2.a–e PDF page 92; PRE.2.f–p PDF page 93. PRE.2.k uses "health care needs" (two words). PRE.2.p requirement ends with a full stop (clean wording). No asterisked OEs.

SHAPE: Nine What-we-do subsections (5.1–5.9). No stop-work. Disclaimer accreditation-only. PRE roles only."""


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
        "subtitle": "Beliefs, values and decision-making in day-to-day care.",
        "doc_no": D("PRE/POL/02"),
    }
    emit_pre_v2(
        draft,
        "pre2_v2_draft.json",
        "PRE.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
