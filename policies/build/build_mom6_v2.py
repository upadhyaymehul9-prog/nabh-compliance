# -*- coding: utf-8 -*-
"""MOM.6 v2 — medications are administered safely.

PDF index 85. Stop-work: do not administer without patient ID, order verification,
physical inspection. Nine OEs, nine What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer_accreditation_only

STANDARD_CODE = "MOM.6"
CHAPTER = "MOM"
OE_CODES = [
    "MOM.6.a", "MOM.6.b", "MOM.6.c", "MOM.6.d", "MOM.6.e",
    "MOM.6.f", "MOM.6.g", "MOM.6.h", "MOM.6.i",
]
POLICY_TITLE = "Medications Are Administered Safely"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, nine steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Every medication is administered safely — right patient, right drug, right dose, right route, "
    "right time — with labelling of prepared drugs, patient identification, order verification, "
    "physical inspection, documentation, and governance of self-administration and outside medications."
)

PURPOSE = f"""This policy describes how {HOSPITAL} administers medications safely: safe administration practice, labelling of prepared medications, patient identification, order and physical verification, strength-route-timing verification, catheter and tubing mis-connection prevention, documentation, self-administration governance, and governance of medications brought from outside.

It covers MOM.6.a–i.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to nurses, treating doctors, the Pharmacy In-Charge, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.6.a–i: safe administration; prepared medication labelling; patient identification before administration; medication and physical inspection verification; strength, route and timing verification; catheter and tubing mis-connection measures; documentation; self-administration governance; and outside-medication governance.

Boundaries with other policies of {HOSPITAL}:

- MOM.5 owns dispensing. This policy begins when the medication reaches the administering staff.
- MOM.7 owns monitoring after administration and adverse-event reporting.
- PSQ (patient safety goals) owns the patient-identification system. This policy applies it at the point of medication administration."""

POLICY_STATEMENT = f"""{HOSPITAL} administers medications safely. The patient is identified, the medication is verified against the order and physically inspected, and the administration is documented.

Prepared medications are labelled before a second drug is prepared. Catheter and tubing mis-connection measures are in place. Self-administration and outside medications are governed."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. The patient is identified using {D('two identifiers (name and unique ID number)')} before every medication administration.
2. The medication is verified against the medication order before administration: drug name, strength, route, frequency and timing.
3. The medication is physically inspected for expiry, discolouration, particulate matter and packaging integrity before administration.
4. A prepared medication is labelled with drug name and strength before preparation of a second drug begins.
5. The route of administration is verified against the order. Catheter and tubing connections are traced from the patient to the source before connecting.
6. Every administration is documented: drug, dose, route, time and administering staff.
7. Self-administration by the patient is permitted only when authorised by the treating doctor and the patient is assessed as competent.
8. Medications brought from outside the organisation are permitted only when approved by the treating doctor and verified by the pharmacist.
9. An administering nurse who cannot verify the patient, the order, or the medication's physical integrity does not administer. The nurse contacts the prescriber or Pharmacy In-Charge.

Staff who cannot complete verification do not administer. They report to the {D('ward in-charge nurse')} immediately."""

PROCEDURE_STEPS = [
f"""5.1 Safe medication administration

Administration of medication is done in a safe manner.

The administering nurse follows the {D('five rights: right patient, right drug, right dose, right route, right time')}. The nurse washes hands, prepares the medication at the bedside or medication preparation area, and administers while the patient is identified and the order is open.

If any element cannot be confirmed, the nurse does not administer and contacts the prescriber or Pharmacy In-Charge.""",

f"""5.2 Labelling of prepared medications

Prepared medication is labelled before preparation of a second drug.

When a nurse draws up or reconstitutes a medication, the syringe or container is labelled immediately with drug name and strength. A second drug is not prepared until the first is labelled.

This rule applies to all settings: wards, emergency, operation theatre, and procedure rooms.""",

f"""5.3 Patient identification before administration

The patient is identified before administration.

The nurse confirms the patient's identity using {D('two identifiers: patient name (asked, not assumed) and unique identification number (wristband or bedhead ticket)')} immediately before administration.

A medication is never administered to a patient whose identity cannot be confirmed.""",

f"""5.4 Medication and physical verification

Medication is verified from the medication order and physically inspected before administration.

The nurse checks the medication against the written order: drug name, strength, dose, route, frequency. The nurse physically inspects the medication for expiry date, discolouration, particulate matter, and packaging integrity.

Any discrepancy or defect: the medication is not administered. The nurse contacts the prescriber (order discrepancy) or the Pharmacy In-Charge (physical defect).""",

f"""5.5 Strength, route and timing verification

Strength, route and timing is verified from the order before administration.

The nurse confirms the strength to be administered matches the order. The route (oral, IV, IM, SC, topical, etc.) is verified against the order. The timing matches the prescribed frequency or specified time.

A wrong-strength, wrong-route, or wrong-time event is a medication error reported under MOM.7.""",

f"""5.6 Catheter and tubing mis-connection prevention

Measures to avoid catheter and tubing mis-connections during medication administration are implemented.

Before connecting any line, the nurse traces the tubing from the patient to the infusion source. Enteral and parenteral lines use different connectors where available. Lines are labelled at both ends.

The {D('ward in-charge nurse')} conducts a {D('monthly')} spot-check of tubing labelling and connection practices.""",

f"""5.7 Documentation of administration

Medication administration is documented.

The administering nurse records: drug name, dose, route, time of administration, and initials or signature in the {D('medication administration record (MAR)')}. For withheld or omitted doses, the reason is documented.

Documentation occurs immediately after administration, not in advance.""",

f"""5.8 Self-administration governance

Measures to govern patient's self-administration of medications are implemented.

Self-administration is permitted only when:
1. The treating doctor authorises it in writing.
2. The nurse assesses the patient as competent to self-administer (oriented, physically able, understands dosing).
3. The medication and schedule are documented in the MAR.

The nurse checks self-administered doses at {D('each medication round')} and documents compliance or variance.""",

f"""5.9 Outside-medication governance

Measures to govern patient's medications brought from outside the organisation are implemented.

Medications brought by the patient or family are permitted only when:
1. The treating doctor approves their use in writing.
2. The pharmacist verifies the medication (identity, expiry, storage condition).
3. The medication is recorded in the MAR alongside hospital-dispensed medications.

Unapproved outside medications are stored separately by the nurse and returned to the family at discharge.""",
]

STOP_WORK = f"""Any nurse or staff member who cannot confirm patient identity, cannot verify the medication against the order, or finds a physical defect in the medication:

1. Does not administer the medication.
2. Sets the medication aside (does not return it to stock without pharmacist assessment).
3. Contacts the prescriber (order issue) or Pharmacy In-Charge (physical defect).
4. Documents the event in the {D('medication administration record')} with the reason for withholding.

No approval is needed to withhold. Patient safety overrides schedule pressure."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for safe administration standards across the organisation.

Treating doctors (prescribers)
- Authorise self-administration and outside medications in writing.

Nurses
- Administer medications safely following the five rights; label, identify, verify, document; govern self-administration and outside medications.

Ward in-charge nurse
- Spot-checks tubing labelling and administration practices.

Pharmacy In-Charge
- Verifies outside medications; assesses returned or defective medications.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when administration lapses recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at administration records and bedside practices.

What is monitored each quarter:

- Sample MARs checked for completeness and timeliness of documentation.
- Bedside observation of patient identification, five-rights check, and prepared-medication labelling.
- Tubing labelling and connection practices (spot-check).
- Self-administration authorisation and compliance records.
- Outside-medication approval and pharmacist-verification records.
- Administration errors and near-misses reported under MOM.7.

Root-cause analysis is required when the same administration lapse recurs within six months.

This policy is reviewed {D('annually')}, and sooner when MOM.5 or MOM.7 is revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All nurses and clinical staff who administer medications are trained on this policy at induction and {D('once a year')} after that. Training covers the five rights, labelling, patient identification, verification, documentation, tubing safety, self-administration and outside-medication governance.

Staff acknowledgement

I have read this Medications Are Administered Safely policy of {HOSPITAL}. I will follow the five rights, verify before administering, and never administer when identity or order cannot be confirmed.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The ward in-charge nurse holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/06",
    version=VERSION,
    prepared_by=D("Nursing Superintendent / Ward In-Charge Nurse"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.6.
- Internal documents of {HOSPITAL}: medication administration record (MAR); patient identification policy (PSQ); MOM.7 monitoring and reporting; tubing labelling protocol."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the ward in-charge nurse and the Quality Coordinator.

Copies issued to: every in-patient ward; emergency room; operation theatre; ICU where it exists; nursing administration; pharmacy.

The current version is available to all staff at the {D('nursing station policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
IM — intramuscular
IV — intravenous
MAR — medication administration record
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 3)
SC — subcutaneous
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "MOM.6.a",
        "requirement": "Administration of medication is done in a safe manner.",
        "steps": "Statement of intent; Section 3; 5.1 Safe medication administration",
        "responsible": "Nurses (administer); prescribers (order); Pharmacy In-Charge (supply)",
        "records": [
            "Medication administration records (MARs) showing five-rights compliance.",
            "Quarterly bedside observation audit results.",
            "Incident reports for administration errors.",
            "Training records for all administering staff.",
        ],
    },
    {
        "oe_code": "MOM.6.b",
        "requirement": "Prepared medication is labelled before preparation of a second drug.",
        "steps": "Section 4 item 4; 5.2 Labelling of prepared medications",
        "responsible": "Nurses (label immediately after preparation)",
        "records": [
            "Bedside observation audit showing labelling before second-drug preparation.",
            "Incident reports for unlabelled preparations.",
            "Training records covering prepared-medication labelling.",
        ],
    },
    {
        "oe_code": "MOM.6.c",
        "requirement": "The patient is identified before administration.",
        "steps": "Section 3; Section 4 item 1; 5.3 Patient identification before administration",
        "responsible": "Nurses (identify using two identifiers)",
        "records": [
            "Bedside observation audit of patient identification at administration.",
            "Patient-identification system records (wristbands or bedhead tickets).",
            "Incident reports for identification failures.",
        ],
    },
    {
        "oe_code": "MOM.6.d",
        "requirement": "Medication is verified from the medication order and physically inspected before administration.",
        "steps": "Section 4 items 2–3; 5.4 Medication and physical verification",
        "responsible": "Nurses (verify and inspect before administering)",
        "records": [
            "MAR entries showing verification against the order.",
            "Incident reports for physical defects found at administration.",
            "Quarterly audit sample of verification compliance.",
        ],
    },
    {
        "oe_code": "MOM.6.e",
        "requirement": "Strength, route and timing is verified from the order before administration.",
        "steps": "Section 4 item 2; 5.5 Strength, route and timing verification",
        "responsible": "Nurses (verify strength, route, timing)",
        "records": [
            "MAR entries showing strength, route and time match the order.",
            "Incident reports for wrong-strength, wrong-route or wrong-time events.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "MOM.6.f",
        "requirement": "Measures to avoid catheter and tubing mis-connections during medication administration are implemented.",
        "steps": "Section 4 item 5; 5.6 Catheter and tubing mis-connection prevention",
        "responsible": "Nurses (trace and label); ward in-charge (spot-check)",
        "records": [
            "Spot-check records of tubing labelling and connection practices.",
            "Incident reports for tubing mis-connections or near-misses.",
            "Evidence of different connectors or labelling at both ends.",
        ],
    },
    {
        "oe_code": "MOM.6.g",
        "requirement": "Medication administration is documented.",
        "steps": "Section 4 item 6; 5.7 Documentation of administration",
        "responsible": "Nurses (document immediately after administration)",
        "records": [
            "Completed MARs with drug, dose, route, time and initials.",
            "Documentation of withheld or omitted doses with reason.",
            "Quarterly audit of MAR completeness and timeliness.",
        ],
    },
    {
        "oe_code": "MOM.6.h",
        "requirement": "Measures to govern patient's self-administration of medications are implemented.",
        "steps": "Section 4 item 7; 5.8 Self-administration governance",
        "responsible": "Treating doctor (authorise); nurse (assess competence and monitor)",
        "records": [
            "Written authorisation by the treating doctor for self-administration.",
            "Competence assessment by the nurse.",
            "MAR entries showing self-administered doses checked at medication rounds.",
        ],
    },
    {
        "oe_code": "MOM.6.i",
        "requirement": "Measures to govern patient's medications brought from outside the organisation are implemented.",
        "steps": "Section 4 item 8; 5.9 Outside-medication governance",
        "responsible": "Treating doctor (approve); pharmacist (verify); nurse (record and store)",
        "records": [
            "Written approval by the treating doctor for outside medications.",
            "Pharmacist verification record (identity, expiry, storage condition).",
            "MAR entries showing outside medications alongside hospital-dispensed medications.",
            "Records of unapproved medications stored separately and returned at discharge.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.6 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Medications are administered safely." MOM.6.a–i PDF index 85. MOM.6.a, MOM.6.f, MOM.6.h, MOM.6.i asterisked. MOM.6.c and MOM.6.d Core. MOM.6.h Achievement.

SHAPE: Nine What-we-do subsections (5.1–5.9). Stop-work yes (do not administer without patient ID, order verification, physical inspection). Disclaimer accreditation-only. MOM roles only."""


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
        "template_test": "mom_v2_adoptable_shape",
        "subtitle": "Safe administration: five rights, verification, documentation and governance.",
        "doc_no": "MOM/POL/06",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom6_v2_draft.json",
        "MOM.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
