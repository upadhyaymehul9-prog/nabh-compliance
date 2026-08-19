# -*- coding: utf-8 -*-
"""MOM.9 v2 — implantable prosthesis and medical devices are used in accordance
with laid down criteria.

PDF index 87. No stop-work. Three OEs, three What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.9"
CHAPTER = "MOM"
OE_CODES = ["MOM.9.a", "MOM.9.b", "MOM.9.c"]
POLICY_TITLE = (
    "Implantable Prostheses and Medical Devices Are Used in Accordance "
    "with Laid Down Criteria"
)
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, three steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Implantable prostheses and medical devices are procured through written guidance, "
    "the patient and family are counselled, and batch and serial numbers are traced in "
    "the medical record, master logbook and discharge summary."
)

PURPOSE = f"""This policy describes how {HOSPITAL} manages implantable prostheses and medical devices: procurement through written guidance, patient and family counselling, and traceability of batch and serial numbers in the medical record, master logbook and discharge summary.

It covers MOM.9.a–c. MOM.1.e places implants within the Multidisciplinary Medication Committee's scope; this policy owns the operational detail.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors (surgeons and implanting clinicians), the Pharmacy In-Charge, nurses, the store or procurement officer, the Multidisciplinary Medication Committee, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.9.a–c: procurement guidance; patient and family counselling; and batch/serial-number traceability.

Boundaries with other policies of {HOSPITAL}:

- MOM.1.e lists implants in the committee's scope. This policy owns the procurement guidance, counselling and traceability.
- PRE.3 owns informed consent for surgery and invasive procedures. This policy owns the implant-specific counselling (including precautions).
- COP.10 owns surgical safety. This policy owns the implant record in the medical record and discharge summary."""

POLICY_STATEMENT = f"""{HOSPITAL} procures implantable prostheses and medical devices through written guidance approved by the Multidisciplinary Medication Committee.

The patient and family are counselled before use, including precautions. The batch and serial number of every implant and medical device are recorded in the patient's medical record, the master logbook and the discharge summary."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Every implantable prosthesis and medical device used at {HOSPITAL} is procured from {D('suppliers approved by the committee and licensed under the Medical Devices Rules, 2017')}.
2. The patient and family are counselled before the implant procedure, including the nature of the device, expected outcome, precautions, and potential complications.
3. The batch number and serial number of every implant and medical device are recorded in the patient's medical record, the master logbook and the discharge summary — no exceptions.

Staff who find an implant without a traceable batch or serial number do not use it. They report to the {D('Pharmacy In-Charge')} or the operating surgeon immediately."""

PROCEDURE_STEPS = [
f"""5.1 Procurement of implantable prostheses and medical devices

Written guidance addresses procurement and usage of implantable prostheses.

The Multidisciplinary Medication Committee approves the list of implantable prostheses and medical devices used at {HOSPITAL}. Procurement criteria include: clinical indication, supplier licence under the {D('Medical Devices Rules, 2017')}, batch traceability, storage requirements, and cost.

The {D('store or procurement officer')} procures only from the approved-supplier list. On receipt, the Pharmacy In-Charge verifies batch number, serial number, expiry (where applicable), packaging integrity and storage instructions. A goods-receipt entry is made in the implant register.""",

f"""5.2 Patient and family counselling

Patient and family are counselled for the usage of the implantable prosthesis and medical devices including precautions if any.

Before the procedure, the treating doctor (or a {D('trained counsellor or nurse')}) explains to the patient and family: the nature and purpose of the implant or device; expected outcome; precautions after implantation (activity restrictions, MRI compatibility, follow-up schedule); and potential complications.

Counselling is documented in the medical record. A signed acknowledgement by the patient or authorised representative is obtained. Informed consent for the surgical procedure remains PRE.3; this step covers the implant-specific counselling.""",

f"""5.3 Batch and serial number traceability

The batch and the serial number of the implantable prosthesis and medical devices are recorded in the patient's medical records, the master logbook and the discharge summary.

Immediately after implantation, the operating team records the following in three places:

1. **Patient's medical record**: implant name, manufacturer, batch number, serial number, date of implantation, and implanting surgeon.
2. **Master logbook** (maintained by the {D('Pharmacy In-Charge or store officer')}): patient name and ID, implant name, manufacturer, batch number, serial number, date of implantation, and implanting surgeon.
3. **Discharge summary** (AAC.8): implant name, batch number, serial number, and any precautions for the patient.

The Pharmacy In-Charge reconciles the master logbook against goods-receipt and theatre records {D('monthly')}. A discrepancy triggers investigation.""",
]

STOP_WORK = ""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for implant governance and traceability.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Approves the implant list, procurement criteria and supplier list.

Treating doctors (surgeons / implanting clinicians)
- Counsel the patient and family; record batch and serial number in the medical record.

Pharmacy In-Charge
- Verifies receipt; maintains the master logbook; reconciles monthly.

Store or procurement officer
- Procures from the approved-supplier list only.

Nurses (operating theatre)
- Assist in recording the implant details at the time of implantation.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA when traceability gaps are found."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at procurement, counselling and traceability records.

What is monitored each quarter:

- Implant register: goods-receipt entries verified against supplier approval.
- Sample medical records checked for batch and serial number documentation.
- Master logbook reconciliation against theatre records.
- Discharge summaries checked for implant details.
- Patient counselling documentation in sample records.

Root-cause analysis is required when the same traceability gap recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the Medical Devices Rules or the implant list changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All operating-theatre staff, surgeons, pharmacy staff and nursing staff involved in implant procedures are trained on this policy at induction and {D('once a year')} after that. Training covers procurement, counselling, and the three-point traceability requirement.

Staff acknowledgement

I have read this Implantable Prostheses and Medical Devices policy of {HOSPITAL}. I will follow procurement guidance, counsel patients, and record batch and serial numbers in three places.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the training record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/09",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.9.
- Medical Devices Rules, 2017 — procurement, tracking and adverse-event reporting for implantable devices.
- Internal documents of {HOSPITAL}: implant register; master logbook; approved-supplier list; MOM.1.e committee scope; PRE.3 informed consent; AAC.8 discharge summary."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; operation theatre; orthopaedic and surgical wards where implants are used; store or procurement.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 5)
CAPA — corrective and preventive action
MOM — Management of Medication (NABH SHCO chapter 7)
MRI — magnetic resonance imaging
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PRE — Patient Rights and Education (NABH SHCO chapter 4)
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Medical Devices Rules, 2017, insofar as implantable prostheses and medical "
    "devices are procured, tracked and reported under those rules"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.9.a",
        "requirement": "Written guidance addresses procurement and usage of implantable prostheses.",
        "steps": "Statement of intent; Section 3; 5.1 Procurement of implantable prostheses and medical devices",
        "responsible": "Committee (approve list and criteria); store officer (procure); Pharmacy In-Charge (verify receipt)",
        "records": [
            "Committee-approved implant list and procurement criteria.",
            "Approved-supplier list with licence verification.",
            "Goods-receipt entries in the implant register.",
            "Pharmacy In-Charge verification records (batch, serial, expiry, packaging).",
        ],
    },
    {
        "oe_code": "MOM.9.b",
        "requirement": "Patient and family are counselled for the usage of the implantable prosthesis and medical devices including precautions if any.",
        "steps": "Section 3; Section 4 item 2; 5.2 Patient and family counselling",
        "responsible": "Treating doctor (counsel); nurse or counsellor (assist); PRE.3 (surgical consent)",
        "records": [
            "Counselling documentation in the medical record.",
            "Signed acknowledgement by patient or authorised representative.",
            "Quarterly audit sample of counselling records.",
        ],
    },
    {
        "oe_code": "MOM.9.c",
        "requirement": "The batch and the serial number of the implantable prosthesis and medical devices are recorded in the patients' medical records, the master logbook and the discharge summary.",
        "steps": "Section 3; Section 4 item 3; 5.3 Batch and serial number traceability",
        "responsible": "Operating team (record in medical record); Pharmacy In-Charge (master logbook); AAC.8 (discharge summary)",
        "records": [
            "Patient medical record entry with implant name, manufacturer, batch, serial, date, surgeon.",
            "Master logbook entry with the same details plus patient name and ID.",
            "Discharge summary (AAC.8) with implant name, batch, serial and precautions.",
            "Monthly reconciliation records (logbook vs goods-receipt and theatre records).",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.9 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Implantable prosthesis and medical devices are used in accordance with laid down criteria." MOM.9.a–c PDF index 87. MOM.9.a asterisked. All Commitment level. PDF has "devises" in MOM.9.b and MOM.9.c — corrected to "devices" in clean wording.

SHAPE: Three What-we-do subsections (5.1–5.3). No stop-work. Disclaimer names Medical Devices Rules 2017. MOM roles only."""


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
        "subtitle": "Implant procurement, counselling and batch/serial traceability.",
        "doc_no": "MOM/POL/09",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom9_v2_draft.json",
        "MOM.9_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
