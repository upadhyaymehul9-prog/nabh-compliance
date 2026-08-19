# -*- coding: utf-8 -*-
"""PRE.4 v2 — information, education and communication about healthcare needs.

Wording from PRE.4 OEs (NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed pages 88–89 / PDF indices 94–95. No stop-work. Disclaimer accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PRE.4"
CHAPTER = "PRE"
OE_CODES = ["PRE.4.a", "PRE.4.b", "PRE.4.c", "PRE.4.d", "PRE.4.e", "PRE.4.f"]
POLICY_TITLE = "Information, Education and Communication about Healthcare Needs"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PRE v2 template: six steps, plain English, PRE roles, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Patients and families have a right to information, education and communication about "
    "their healthcare needs in a language and manner that is understood by them — "
    "not a leaflet they cannot read and never hear explained again."
)

PURPOSE = f"""This policy says how {HOSPITAL} educates the patient and/or family in a language and format they can understand; covers medicines and side effects when appropriate, food-drug interaction, diet, nutrition and immunisations, the specific disease process with complications and prevention, preventing healthcare-associated infections; and communicates effectively.

Rights at entry are PRE.1. The consent conversation is PRE.3. Follow-up advice on the discharge summary is AAC.8.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies wherever a patient or family is taught about healthcare needs: registration after stabilisation, out-patient, emergency, in-patient, day-care, ICU if it exists, and at discharge.

It binds treating doctors, nurses, the {D('Patient Rights Officer')} as education lead where named, and the {D('Quality Coordinator')} who audits.

Boundaries:

- PRE.3.b is the consent conversation; this policy is ongoing education in the same language.
- AAC.8 owns follow-up advice on the discharge summary and hands teaching method to PRE.
- MOM.6 administers; MOM.7 captures NM/ME/ADR; PRE.4.b teaches about medicines and side effects.
- COP.13, COP.8 and HIC.3 own clinical diet, immunisation and kitchen method; PRE.4.c teaches.
- HIC.2/HIC.4/HIC.5 own IPC method; PRE.4.e teaches how patients can help prevent HAI.
- PRE.2.j access to records; IMS owns the file."""

POLICY_STATEMENT = f"""{HOSPITAL} educates the patient and/or family in a language and format that they can understand.

{HOSPITAL} educates about safe and effective use of medication and potential side effects when appropriate.

{HOSPITAL} educates about food-drug interaction and about diet, nutrition and immunisations.

{HOSPITAL} educates about the specific disease process, complications and prevention strategies.

{HOSPITAL} educates about preventing healthcare-associated infections.

{HOSPITAL} communicates with patients and/or families effectively. A leaflet unread, or a monologue without checking understanding, is not effective communication."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Handing education material only in a language or format the patient cannot use.
2. Starting or changing a medicine without side-effect education when this hospital's method says it is appropriate.
3. Treating a generic "be healthy" poster as education about this patient's specific disease process.
4. Counting a harvested signature as proof the patient understood.
5. Rewriting MOM.6, MOM.7, COP.13, COP.8 or HIC bundles as this education policy.

Staff report defects to the {D('Patient Rights Officer')} or {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Education in a language and format they can understand

Patient and/or family are educated in a language and format that they can understand.

Language and format — spoken language, written material, interpreter, accompanying family as translator, and what is done when the patient cannot read — are chosen and recorded in {D('Hindi and English')} or the patient's language. PRE.3.b uses the same language for consent; this step is ongoing education.""",

f"""5.2 Medicines and potential side effects, when appropriate

Patient and/or family are educated about the safe and effective use of medication and the potential side effects of the medication, when appropriate.

Education is given at start of a medicine, at a change, or at discharge as this hospital defines — {D('at start and at any dose change, and again at discharge if the medicine continues')}. Administration remains MOM.6. Event capture remains MOM.7.""",

f"""5.3 Food-drug interaction, diet, nutrition and immunisations

Patient and/or family are educated about food-drug interaction and about diet, nutrition and immunisations.

Teaching for each topic this hospital uses is recorded. Nutritional-risk screen and therapeutic diet remain COP.13. Paediatric immunisation assessment remains COP.8. Unused immunisation as a service is a recorded absence.""",

f"""5.4 Specific disease process, complications and prevention

Patient and/or family are educated about their specific disease process, complications and prevention strategies.

Teaching covers the condition this patient has, not only a generic poster. Diagnosis and care plan remain AAC.3.""",

f"""5.5 Preventing healthcare-associated infections

Patient and/or family are educated about preventing healthcare associated infections.

Patients and families are told what they can do — hand hygiene, not touching devices, telling staff of fever — as {D('a short ward talk at admission and a reminder at discharge')}. Bundles and surveillance remain HIC.""",

f"""5.6 Communication done effectively

Communication with the patients and/or families is done effectively.

Understanding is checked — {D('the patient or family repeats the key point in their own words')}. If they cannot, staff adapt and record that. Marcus (2014) EDUCATE and Nouri and Rudd (2015) are frameworks, not mandated acronyms on a form. A harvested signature is not a check of understanding.""",
]

RESPONSIBILITY = f"""Medical Superintendent — accountable for education and effective communication.

Patient Rights Officer (or named education lead)
- Holds language-and-format method, topic methods and effective-communication method.

Doctors and nurses — teach and check understanding.

Quality Coordinator — audits {D('quarterly')}."""

MONITORING_AUDIT = f"""The Quality Coordinator audits {D('quarterly')} for language and format; medicines when appropriate; food-drug, diet, nutrition and immunisations; disease process; HAI prevention teaching; and evidence communication was effective, not only a leaflet or signature.

Reviewed {D('annually')} or sooner when AAC.8, MOM or HIC policies change."""

TRAINING_ACKNOWLEDGEMENT = f"""Clinical staff train at induction and {D('once a year')} on language choice, teach-back, and when to escalate if the family cannot understand.

Staff acknowledgement — I will check understanding, not only hand a leaflet.


Name: ___________________________    Designation: ___________________________

Date: ____________    Signature: ___________________________


(Patient Rights Officer holds acknowledgements.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PRE/POL/04"),
    version=VERSION,
    prepared_by=D("Patient Rights Officer"),
)

REFERENCES = f"""- NABH SHCO 3rd Edition — standard PRE.4.
- Badarudeen and Sabharwal (2010) — ch 1; readability framework.
- Marcus C (2014) EDUCATE — ch 11; verbal education framework.
- Nouri SS and Rudd RE (2015) — ch 14; oral health literacy framework.
- Ha JF and Longnecker N (2010) — ch 7; doctor-patient communication framework.
- Internal documents of {HOSPITAL}: education methods; rights, consent, discharge, medication and infection-prevention policies."""

DISTRIBUTION = f"""Master copy: Medical Superintendent, Patient Rights Officer, Quality Coordinator.

Copies: out-patient, emergency, wards, ICU if exists, nursing administration.

Available at {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """HAI — healthcare-associated infection
NABH — National Accreditation Board for Hospitals and Healthcare Providers
PRE — Patient Rights and Education
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PRE.4.a",
        "requirement": "Patient and/or family are educated in a language and format that they can understand.",
        "steps": "Statement of intent; Section 3; 5.1 Language and format; 5.6 Effective communication",
        "responsible": "Patient Rights Officer (method); doctors and nurses (teach)",
        "records": [
            "Written language-and-format method including illiteracy and interpreter use.",
            "Sample teaching records in the language used.",
            "Recorded split that PRE.3.b is the consent conversation.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.4.b",
        "requirement": "Patient and/or family are educated about the safe and effective use of medication and the potential side effects of the medication, when appropriate.",
        "steps": "Section 3; 5.2 Medicines and side effects; Section 4 item 2",
        "responsible": "Staff who start or change medicines; MOM.6/MOM.7 (administration and events)",
        "records": [
            "Written method for medication and side-effect education including when appropriate.",
            "Sample teaching records at start, change or discharge.",
            "Recorded split that MOM.7 still captures NM/ME/ADR.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.4.c",
        "requirement": "Patient and/or family are educated about food-drug interaction and about diet, nutrition and immunisations.",
        "steps": "Section 3; 5.3 Food-drug, diet, nutrition and immunisations",
        "responsible": "Staff who teach; COP.13/COP.8/HIC.3 (clinical and kitchen acts)",
        "records": [
            "Written method for food-drug, diet, nutrition and immunisation education.",
            "Recorded absence for topics not provided.",
            "Sample teaching records.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.4.d",
        "requirement": "Patient and/or family are educated about their specific disease process, complications and prevention strategies.",
        "steps": "Section 3; 5.4 Disease process, complications and prevention",
        "responsible": "Treating clinicians; AAC.3 (care plan)",
        "records": [
            "Written method for disease-process education specific to the patient's condition.",
            "Sample records — not a generic poster counted as teaching.",
            "Quarterly audit sample.",
            "Review when AAC.3 is revised.",
        ],
    },
    {
        "oe_code": "PRE.4.e",
        "requirement": "Patient and/or family are educated about preventing healthcare associated infections.",
        "steps": "Section 3; 5.5 Preventing healthcare-associated infections",
        "responsible": "Ward nurses and doctors; HIC (IPC method)",
        "records": [
            "Written method for patient/family HAI-prevention teaching.",
            "Sample admission and discharge teaching records.",
            "Recorded split that HIC owns bundles and surveillance.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.4.f",
        "requirement": "Communication with the patients and/or families is done effectively.",
        "steps": "Section 3; 5.6 Communication done effectively; Sections 5.1–5.5",
        "responsible": "Patient Rights Officer (method); all staff who teach",
        "records": [
            "Written effective-communication method with teach-back and adaptation when not understood.",
            "Sample encounters recording understanding check, not only signature.",
            "Framework use of Marcus 2014, Ha and Longnecker 2010, Nouri and Rudd 2015 — not pasted protocols.",
            "Quarterly audit sample of communication that worked.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PRE.4 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. PRE.4.f asterisked. PRE.4.e uses "healthcare associated infections" (no hyphen). Accreditation-only P2. No stop-work."""


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
        "subtitle": "Teaching patients and families about healthcare needs.",
    }
    emit_pre_v2(
        draft,
        "pre4_v2_draft.json",
        "PRE.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
