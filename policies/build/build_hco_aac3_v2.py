# -*- coding: utf-8 -*-
"""HCO AAC.3 v2 — transfer in/out and referral (HCO Full, 6th Edition).

Shape follows PRE/SHCO v2 adoptable-policy shape via pre_v2_common.
Wording from NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition
— AAC chapter (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices 68–69.
OCR source: policies/source/hco6_aac_ocr.txt.

Four OEs (a–d). Asterisk on a, b. Stop-work INCLUDED for unstable transfer without
criteria / stabilisation / appropriate accompanying staff.
Does NOT overwrite SHCO AAC builders or drafts.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, document_control, emit_pre_v2

STANDARD_CODE = "AAC.3"
CHAPTER = "HCO"
OE_CODES = ["AAC.3.a", "AAC.3.b", "AAC.3.c", "AAC.3.d"]
POLICY_TITLE = "Transfer In, Transfer Out and Referral"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO Full 6th Edition AAC.3 v2 draft: plain English, four steps, stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Patients who arrive by transfer, leave by transfer or referral, or move for "
    "diagnostics do so safely — stabilised where needed, accompanied by the right "
    "staff, with a written summary of condition and treatment."
)

PURPOSE = f"""This policy says how {HOSPITAL} receives transfer-in patients appropriately (planned and unplanned); transfers out or refers patients to another facility appropriately; assigns accompanying staff appropriate to the clinical condition; and gives a summary of the patient's condition and treatment given.

The chapter intent is that emergency patients receive life-stabilising treatment and are then either admitted or transferred appropriately, and that transfer and discharge protocols are well defined.

This policy owns transfer-in, transfer-out, referral for care elsewhere, and transfers for diagnostic or therapeutic purposes outside the organisation's immediate capability. AAC.2 owns registration and admission of patients who stay. AAC.12–AAC.13 own routine discharge content. AAC.10 owns intra-organisation continuity.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to emergency, wards, intensive care, day-care and any unit at {HOSPITAL} that receives a transfer-in or initiates transfer-out or referral. It binds treating doctors, accompanying nurses and technologists, ambulance coordinators, registration staff who receive transfer-in patients, Medical Records, the Medical Superintendent, and the Quality Coordinator.

It covers AAC.3.a–d.

Boundaries:

- AAC.2 owns bed non-availability holding; once the decision is to transfer out, this policy owns the transfer.
- AAC.12 / AAC.13 own discharge-summary content for patients discharged and transferred (including LAMA); this policy requires that a discharge or transfer summary is given and a copy retained.
- COP standards own clinical stabilisation techniques; this policy owns that stabilisation, mode, equipment, monitoring and accompanying staff are decided and documented before transfer.
- Lab and imaging own the receiving diagnostic service when a patient is shifted for tests; this policy owns safe transfer to that service when it is outside the immediate unit."""

POLICY_STATEMENT = f"""{HOSPITAL} receives transfer-in patients appropriately for both planned and unplanned transfers. Transfer-out and referral to another facility are done appropriately, including pre-transfer stabilisation where appropriate, choice of mode and vehicle, equipment and monitoring, with gaps documented when requirements cannot be met. Accompanying staff match the patient's clinical condition. A transfer summary — or a discharge summary when the patient is discharged and transferred, including leaving against medical advice — is given, and a copy is retained.

{HOSPITAL} does not transfer an unstable patient without meeting transfer criteria, completing appropriate stabilisation, and assigning appropriate accompanying staff."""

NON_NEGOTIABLES = f"""1. Do not accept or dispatch a transfer-in without recording planned versus unplanned status and the clinical information received.
2. Do not transfer out or refer a patient without consulting the patient and/or family where they can be consulted, and without addressing stabilisation, mode, equipment and monitoring — or documenting why a stated requirement could not be met.
3. Do not send an unstable admitted patient for transfer-out or for diagnostic shift without a doctor accompanying.
4. Do not send any transfer or referral without accompanying staff who are at least a trained trauma technologist, emergency technologist or nurse with basic or advanced cardiopulmonary resuscitation training as appropriate, and who know the transfer procedure.
5. Do not complete a transfer without giving a transfer summary (or discharge summary if discharged and transferred, including LAMA) and retaining a copy.
6. Staff who find transfer rules not followed report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not transfer an unstable patient out of {HOSPITAL}, or shift an unstable admitted patient for diagnostics, unless transfer criteria are met, appropriate pre-transfer stabilisation has been done, and accompanying staff appropriate to the clinical condition (including a doctor for an unstable admitted patient) are assigned and ready.

If those conditions are not met, stop the transfer, continue stabilisation and escalate to the {D('treating doctor')} and the {D('Medical Superintendent')} the same shift. Document why the transfer was held.

Stop-work does not block emergency life-saving measures. It blocks unsafe transfer movement until criteria, stabilisation and accompanying staff are in place.

Refusing an unsafe transfer is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Transfer-in done appropriately

Transfer-in covers planned and unplanned arrivals. For unplanned transfers and suspected unstable patients, {HOSPITAL} may send a suitably trained person with the ambulance, guided by the information received. Feedback on the patient's clinical status is provided to the referring organisation or doctor as good practice.

On arrival, registration under AAC.2 applies. The receiving doctor documents the transfer-in, clinical status on arrival, and whether the transfer was planned or unplanned. The {D('Emergency In-Charge')} owns the unplanned transfer-in pathway; department heads own planned specialty transfer-ins.""",

f"""5.2 Transfer-out and referral done appropriately

Patients needing transfer-out or referral include those who present to emergency but need another organisation, those already admitted who now need care elsewhere, and patients being shifted for diagnostic tests outside the unit's immediate capability.

Transfer is done in consultation with the patient and/or family, in a safe manner that includes:

- pre-transfer stabilisation where appropriate;
- choice of mode and vehicle for transport;
- equipment required during transfer;
- monitoring required during transfer.

If {HOSPITAL} cannot meet some of these stated requirements, the reasons are documented in the transfer record before the patient leaves. The treating doctor authorises the transfer-out or referral.""",

f"""5.3 Accompanying staff appropriate to clinical condition

Staff accompanying a transfer or referral are at least a trained trauma technologist, emergency technologist or nurse. That person has undergone training in basic or advanced cardiopulmonary resuscitation as appropriate to the role, and knows the transfer procedure.

A doctor accompanies an unstable admitted patient who is being transferred out or being shifted for diagnostic purposes. Stability is judged by the treating doctor against {D('airway, breathing, circulation, conscious level and any specialty-specific instability criteria')} written in the transfer guidance.

The names and roles of accompanying staff are recorded on the transfer summary.""",

f"""5.4 Summary of condition and treatment given

{HOSPITAL} gives a transfer summary stating significant findings and treatment given to every patient transferred from the emergency ward or transferred for diagnostic or therapeutic purposes.

When a patient is discharged from the organisation and transferred out, a discharge summary is given — including patients leaving against medical advice (LAMA). A copy of the transfer or discharge summary is retained by {HOSPITAL} in the medical record.

Medical Records verifies that the retained copy is filed under the unique identification number before the record is closed for that episode.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for transfer-in/out and referral written guidance and stop-work enforcement.
- Approves ambulance and accompanying-staff arrangements.

Treating doctors
- Authorise transfer-out and referral; judge stability; accompany unstable admitted patients; write or approve transfer/discharge summaries.

Emergency In-Charge / department heads
- Own unplanned and planned transfer-in pathways respectively.
- Ensure feedback to referring organisations where practicable.

Accompanying nurses / technologists
- Hold current CPR training appropriate to role; know the transfer procedure; monitor during transfer.

Registration / front office
- Register transfer-in patients under AAC.2; assist family communication for transfer-out.

Medical Records
- Retain copies of transfer and discharge summaries under the unique number.

Quality Coordinator
- Audits transfer documentation, accompanying-staff fitness and stop-work events {D('quarterly')}."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sample of transfer-in records shows planned/unplanned status and clinical information on arrival.
- Sample of transfer-out/referral records shows stabilisation, mode, equipment, monitoring, and documented gaps where requirements were not met.
- Accompanying staff match clinical condition; doctor accompanies unstable admitted transfers in the sample.
- Transfer or discharge summary (including LAMA where applicable) given and copy retained.
- Stop-work events (held unsafe transfers) are logged with outcome.

Root-cause analysis is required when an unstable transfer proceeds without criteria, stabilisation or appropriate accompanying staff.

This policy is reviewed {D('annually')}, and sooner after any adverse event during transfer."""

TRAINING_ACKNOWLEDGEMENT = f"""Doctors, nurses and technologists who accompany transfers, emergency staff and medical records staff are informed of this policy at induction and {D('once a year')} after that. Training covers planned/unplanned transfer-in, stabilisation and documentation of gaps, accompanying-staff rules including doctor for unstable patients, CPR expectations, transfer/discharge summaries including LAMA, and stop-work.

Staff acknowledgement

I have read this Transfer In, Transfer Out and Referral policy of {HOSPITAL}. I will not transfer an unstable patient without criteria, stabilisation and appropriate accompanying staff, and I will give and retain the required summary.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with clinical induction records.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/03"),
    version=VERSION,
    prepared_by=D("Emergency In-Charge"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care (AAC), standard AAC.3.
- Internal documents of {HOSPITAL}: transfer-in/out and referral written guidance; ambulance and accompanying-staff roster; CPR training records; transfer-summary and discharge-summary templates; AAC.12/AAC.13 discharge policies (cross-reference)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: emergency; every ward and ICU; day-care; ambulance coordination; medical records; registration; nursing administration.

The current version is available to all staff at the {D('clinical policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH Hospitals chapter)
CAPA — corrective and preventive action
CPR — cardiopulmonary resuscitation
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
ICU — intensive care unit
LAMA — left against medical advice
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.3.a",
        "requirement": "Transfer-in of patients to the organisation is done appropriately.",
        "steps": "Section 3; 5.1 Transfer-in done appropriately; Section 4 item 1",
        "responsible": "Emergency In-Charge (unplanned); department heads (planned); treating doctors (receive); registration (AAC.2)",
        "records": [
            "Transfer-in records showing planned or unplanned status and clinical information received.",
            "Ambulance crew or escort assignment notes for unplanned/suspected unstable transfer-ins where used.",
            "Feedback notes to referring organisation/doctor where provided.",
            "Registration of transfer-in patients under the unique identification number.",
        ],
    },
    {
        "oe_code": "AAC.3.b",
        "requirement": "Transfer-out / referral of patients to another facility is done appropriately.",
        "steps": "Section 3; 5.2 Transfer-out and referral done appropriately; Section 4 item 2; Section 6 Stop-work",
        "responsible": "Treating doctors (authorise); accompanying clinical staff (execute); Medical Superintendent (accountable)",
        "records": [
            "Transfer-out/referral orders with patient/family consultation noted where consulted.",
            "Documentation of pre-transfer stabilisation, mode/vehicle, equipment and monitoring.",
            "Documented reasons when stated transfer requirements could not be met.",
            "Log of transfers for emergency, admitted patients and diagnostic shifts.",
        ],
    },
    {
        "oe_code": "AAC.3.c",
        "requirement": "During transfer or referral, accompanying staff are appropriate to the clinical condition of the patient.",
        "steps": "Section 3; 5.3 Accompanying staff appropriate to clinical condition; Section 4 items 3–4; Section 6 Stop-work",
        "responsible": "Treating doctors (judge stability and assign); accompanying nurses/technologists (execute)",
        "records": [
            "Transfer records naming accompanying staff and role.",
            "Evidence of CPR training (basic or advanced as appropriate) for accompanying staff.",
            "Records showing a doctor accompanied unstable admitted patients transferred out or shifted for diagnostics.",
            "Written stability/transfer criteria used to decide accompanying level.",
        ],
    },
    {
        "oe_code": "AAC.3.d",
        "requirement": "The organisation gives a summary of the patient's condition and the treatment given.",
        "steps": "Section 3; 5.4 Summary of condition and treatment given; Section 4 item 5",
        "responsible": "Treating doctors (write/approve summary); Medical Records (retain copy)",
        "records": [
            "Transfer summaries for emergency and diagnostic/therapeutic transfers.",
            "Discharge summaries for patients discharged and transferred out, including LAMA.",
            "Retained copies filed under the unique identification number.",
            "Audit sample confirming summary given before departure.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.3 v2 (2026-08-20). HCO Full Accreditation, NABH Hospitals 6th Edition.
PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. OCR: policies/source/hco6_aac_ocr.txt (PDF indices 68–69).

OE COUNT: 4 (a–d). Asterisked: AAC.3.a, AAC.3.b (Tier 1). AAC.3.c, AAC.3.d Commitment without asterisk (Tier 2).

SHAPE: Four What-we-do subsections (5.1–5.4). Stop-work YES — unstable transfer without criteria/stabilisation/appropriate accompanying staff. Disclaimer accreditation-only. chapter=HCO, doc_no HCO/AAC/POL/03.

FLAG: none after OCR clean-up. Interpretation 'emergency ward/or' read as emergency, ward, or diagnostic/therapeutic transfer contexts."""


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
        "prepared_by": D("Emergency In-Charge"),
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "HCO Full Accreditation, 6th Edition — transfer in/out and referral.",
        "doc_no": D("HCO/AAC/POL/03"),
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with clinical induction records.",
        "stop_work": STOP_WORK,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.3",
    }
    emit_pre_v2(
        draft,
        "hco_aac3_v2_draft.json",
        "HCO.AAC.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
