# -*- coding: utf-8 -*-
"""MOM.4 v2 — medication orders are written in a uniform manner.

PDF index 84. Stop-work: do not dispense against illegible, unsigned, or incomplete order.
Four OEs, four What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.4"
CHAPTER = "MOM"
OE_CODES = ["MOM.4.a", "MOM.4.b", "MOM.4.c", "MOM.4.d"]
POLICY_TITLE = "Medication Orders Are Written in a Uniform Manner"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, four steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Every medication order is written uniformly — authorised personnel, uniform location, "
    "legible, dated, timed, signed, and containing all required details — so that the dispensing "
    "and administering staff never have to guess."
)

PURPOSE = f"""This policy describes how {HOSPITAL} ensures medication orders are written uniformly: only authorised personnel write orders; orders are in a uniform location in the medical record; orders are legible, dated, timed and signed; and orders contain the required medication details.

It covers MOM.4.a–d.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors (prescribers), the Pharmacy In-Charge, nurses, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.4.a–d: authorised personnel; uniform location with patient identification; legibility, date, time and signature; and required medication details.

Boundaries with other policies of {HOSPITAL}:

- MOM.3 owns rational prescribing and minimum prescription requirements. This policy owns the format and uniformity of the written order.
- MOM.5 owns dispensing. The pharmacist verifies order completeness before dispensing.
- MOM.3.e owns verbal orders. This policy applies to written (and transcribed verbal) orders."""

POLICY_STATEMENT = f"""{HOSPITAL} requires that medication orders are written only by authorised personnel, in a uniform location in the medical record, and that every order is legible, dated, timed, signed and contains the name of the medicine, route, strength and frequency.

An illegible, unsigned or incomplete medication order is not dispensed; it is returned to the prescriber."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Only personnel authorised by {HOSPITAL} write medication orders. The list of authorised personnel is maintained by the {D('Medical Superintendent')}.
2. Medication orders are written in the designated section of the medical record, not on loose paper or verbal instruction alone.
3. Every medication order includes the patient's name and unique identification number.
4. Every medication order is legible, dated, timed and signed by the prescriber.
5. Every medication order includes: name of the medicine, route of administration, strength to be administered, and frequency or time of administration.
6. An illegible, unsigned, or incomplete medication order is not dispensed. The pharmacist or nurse returns it to the prescriber for correction.

Staff who see a non-compliant order do not dispense against it. They return it to the prescriber and report to the {D('Pharmacy In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Authorised personnel

{HOSPITAL} ensures that only authorised personnel write medication orders.

The {D('Medical Superintendent')} maintains a list of personnel authorised to write medication orders. The list includes name, designation, registration number and specimen signature. The list is available at the pharmacy and at each nursing station.

Personnel not on the list are not permitted to write medication orders. A verbal order received from an authorised prescriber is transcribed under MOM.3.e.""",

f"""5.2 Uniform location and patient identification

Medication orders are written in a uniform location in the medical records, which also reflects the patient's name and unique identification number.

The designated location is the {D('medication order sheet in the in-patient file and the prescription pad for out-patients')}. Every page of the medication order section carries the patient's name and unique identification number (pre-printed or hand-written at the top).

Orders written outside the designated location are invalid for dispensing and must be re-written in the correct place.""",

f"""5.3 Legibility, date, time and signature

Medication orders are legible, dated, timed and signed.

Every order is written in {D('block capitals or clearly legible handwriting')}. The date (DD/MM/YYYY), time (24-hour clock) and prescriber's signature appear on every order line.

A pharmacist or nurse who cannot read an order does not guess. The order is returned to the prescriber for clarification before dispensing or administration.""",

f"""5.4 Required medication details

Medication orders contain the name of the medicine, route of administration, strength to be administered and frequency or time of administration.

Abbreviations for route and frequency follow the {D('approved abbreviation list maintained by the Pharmacy In-Charge')}. Unapproved or ambiguous abbreviations are flagged and the order is returned.

Where additional details are clinically necessary (duration, dilution, infusion rate), the prescriber adds them. The four mandatory elements (name, route, strength, frequency/time) are non-negotiable.""",
]

STOP_WORK = f"""Any pharmacist, nurse or other staff member who receives a medication order that is illegible, unsigned, incomplete, or written by unauthorised personnel:

1. Does not dispense or administer the medication.
2. Returns the order to the prescriber for correction or re-writing.
3. Documents the return in the {D('returned-order log')} at the pharmacy or nursing station.
4. Reports to the Pharmacy In-Charge if the pattern recurs.

No approval is needed to return a non-compliant order. Patient safety overrides convenience."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Maintains the authorised-personnel list; accountable for order-writing standards.

Treating doctors (prescribers)
- Write legible, complete, dated, timed and signed medication orders in the designated location.

Pharmacy In-Charge
- Verifies order completeness at dispensing; maintains the approved abbreviation list; tracks returned orders.

Nurses
- Verify order completeness before administration; return non-compliant orders to prescriber.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when order-writing defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at medication orders in medical records.

What is monitored each quarter:

- Sample medication orders checked for authorised personnel, uniform location, patient identification, legibility, date, time, signature, and all four required elements.
- Returned-order log reviewed for patterns.
- Authorised-personnel list currency.
- Approved-abbreviation list compliance.

Root-cause analysis is required when the same order-writing defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when MOM.3 or MOM.5 is revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All prescribers, pharmacy staff and nursing staff are trained on this policy at induction and {D('once a year')} after that. Training covers uniform order writing, the four mandatory elements, and the return procedure for non-compliant orders.

Staff acknowledgement

I have read this Medication Orders Are Written in a Uniform Manner policy of {HOSPITAL}. I will write complete orders and will not dispense or administer against illegible or incomplete orders.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/04",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.4.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945 — prescription requirements.
- Internal documents of {HOSPITAL}: authorised-personnel list; approved abbreviation list; medication order sheet template; returned-order log."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; every in-patient ward; out-patient clinics; emergency room; nursing administration.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, "
    "insofar as medication orders meet legal prescription requirements"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.4.a",
        "requirement": "The organisation ensures that only authorised personnel write orders.",
        "steps": "Section 3; Section 4 item 1; 5.1 Authorised personnel",
        "responsible": "Medical Superintendent (maintain list); prescribers (write orders)",
        "records": [
            "Authorised-personnel list with name, designation, registration number and specimen signature.",
            "Evidence the list is available at the pharmacy and nursing stations.",
            "Audit sample confirming orders are by authorised personnel only.",
        ],
    },
    {
        "oe_code": "MOM.4.b",
        "requirement": "Medication orders are written in a uniform location in the medical records, which also reflects the patient's name and unique identification number.",
        "steps": "Section 3; Section 4 items 2–3; 5.2 Uniform location and patient identification",
        "responsible": "Prescribers (write in designated section); nursing staff (verify)",
        "records": [
            "Defined designation of the medication order section in the medical record.",
            "Sample medical records showing orders in the uniform location with patient name and ID.",
            "Returned-order records for orders written outside the designated location.",
        ],
    },
    {
        "oe_code": "MOM.4.c",
        "requirement": "Medication orders are legible, dated, timed and signed.",
        "steps": "Section 3; Section 4 items 4–6; 5.3 Legibility, date, time and signature",
        "responsible": "Prescribers (write legibly, date, time, sign); pharmacy and nurses (verify)",
        "records": [
            "Sample medication orders showing legible writing, date (DD/MM/YYYY), time (24-hour) and signature.",
            "Returned-order log entries for illegible or unsigned orders.",
            "Quarterly audit sample results.",
        ],
    },
    {
        "oe_code": "MOM.4.d",
        "requirement": "Medication orders contain the name of the medicine, route of administration, strength to be administered and frequency/time of administration.",
        "steps": "Section 3; Section 4 item 5; 5.4 Required medication details",
        "responsible": "Prescribers (include all elements); Pharmacy In-Charge (verify and maintain abbreviation list)",
        "records": [
            "Sample medication orders showing all four mandatory elements.",
            "Approved abbreviation list maintained by the pharmacy.",
            "Returned-order log entries for incomplete orders.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.4 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Medication orders are written in a uniform manner." MOM.4.a–d PDF index 84. MOM.4.a asterisked. All Commitment level.

SHAPE: Four What-we-do subsections (5.1–5.4). Stop-work yes (do not dispense illegible/unsigned/incomplete order). Disclaimer names Drugs and Cosmetics Act 1940. MOM roles only."""


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
        "subtitle": "Uniform order writing: authorised, legible, complete, signed.",
        "doc_no": "MOM/POL/04",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom4_v2_draft.json",
        "MOM.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
