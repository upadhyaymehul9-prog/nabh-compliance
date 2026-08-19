# -*- coding: utf-8 -*-
"""AAC.6 v2 — safety programme in laboratory and imaging services.

Shape follows PRE v2 adoptable-policy shape. Wording from AAC.6 OEs (NABH SHCO
3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 59.
Stop-work section 6. Disclaimer P2 names AERP Rules 2004 and BMW Rules 2016.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, emit_pre_v2

STANDARD_CODE = "AAC.6"
CHAPTER = "AAC"
OE_CODES = ["AAC.6.a", "AAC.6.b", "AAC.6.c", "AAC.6.d", "AAC.6.e"]
POLICY_TITLE = "Safety Programme in Laboratory and Imaging Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "AAC v2 template: plain English, AAC roles, five steps, stop-work, AERP/BMW P2.",
    },
]

STATEMENT_OF_INTENT = (
    "There is an established safety programme in the laboratory and imaging services — "
    "so that staff and patients are protected from laboratory hazards and radiation."
)

PURPOSE = f"""This policy says how {HOSPITAL} implements a laboratory safety programme, trains laboratory personnel in safe practices with appropriate safety measures, screens patients before imaging, equips imaging personnel and patients with radiation safety and monitoring devices and trains them in safety practices, and displays imaging signage.

The chapter intent is that laboratory and imaging staff and patients are safe from hazards specific to those services.

This policy owns laboratory and imaging safety. AAC.4 owns laboratory services (the service process). AAC.5 owns imaging services (the service process). HIC owns hospital-wide infection control; this policy owns specimen safety and radiation safety specific to lab and imaging.

PPE — personal protective equipment. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the laboratory in-charge, laboratory technicians, imaging/radiology in-charge, radiographers, treating doctors, nurses, patients undergoing imaging, and the Quality Coordinator at {HOSPITAL}.

It covers the five elements AAC.6.a–e: laboratory safety programme, laboratory safe practices and safety measures, patient screening before imaging, radiation safety devices and training, and imaging signage.

Boundaries:

- HIC owns infection control in laboratory and imaging (hand hygiene, waste segregation categories, sharps policy). This policy owns specimen-handling safety and radiation safety.
- AAC.4 owns the laboratory service process. This policy owns the safety programme that wraps it.
- AAC.5 owns the imaging service process. This policy owns the safety programme that wraps it.
- Spell out: personal protective equipment (PPE)."""

POLICY_STATEMENT = f"""{HOSPITAL} implements a safety programme in laboratory and imaging services. Laboratory personnel are trained in safe practices and provided appropriate safety measures. Patients are screened before imaging for safety and risk. Imaging personnel and patients use appropriate radiation safety and monitoring devices, and are trained in imaging safety practices and radiation-safety measures. Imaging signage is prominently displayed.

{HOSPITAL} does not image without required safety checks, and does not allow laboratory or imaging staff to work without appropriate PPE and training."""

NON_NEGOTIABLES = f"""1. Do not image a patient without completing the required safety screening (pregnancy screening for radiation, allergy history for contrast, implant check for MRI where applicable).
2. Do not allow laboratory or imaging staff to handle specimens or operate equipment without appropriate PPE and training.
3. Do not operate radiation-emitting equipment without radiation monitoring devices (TLD badges or equivalent) for personnel.
4. Do not remove or obscure imaging safety signage from designated locations.
5. Staff who see a safety rule broken report it the same shift to the {D('Laboratory In-Charge')}, {D('Imaging In-Charge')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not image without required safety checks — complete pregnancy screening for radiation examinations and all other required safety screening before the examination proceeds.

Do not operate radiation-emitting equipment without radiation monitoring devices for personnel — obtain and issue devices before the equipment is used.

Stop-work applies to the imaging examination or laboratory procedure, not to emergency stabilisation.

The person responsible tells the {D('Medical Superintendent')} or the {D('Imaging In-Charge')} the same shift. Refusing to image without safety checks is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Laboratory safety programme

The laboratory safety programme at {HOSPITAL} is implemented. It covers:

- chemical safety: handling, storage and spill management for reagents and chemicals;
- biological safety: safe handling of blood, body fluids and infectious specimens;
- fire safety in the laboratory: extinguisher location, evacuation route, no food or drink in the lab;
- electrical safety: equipment earthing, no wet hands near electrical panels;
- waste management: segregation at source per Bio-Medical Waste Management Rules, 2016 (HIC owns the hospital-wide waste stream; this step owns the laboratory source segregation).

The laboratory in-charge reviews the safety programme {D('annually')} and after any safety incident. Safety incidents are reported, investigated and corrective action is taken.""",

f"""5.2 Laboratory safe practices and safety measures

Laboratory personnel are appropriately trained in safe practices and are provided with appropriate safety measures:

- PPE: {D('gloves, lab coat, eye protection, face shield where splash risk exists')};
- hand hygiene before and after specimen handling;
- no mouth pipetting;
- needle-stick and sharps injury protocol posted and practised;
- vaccination (hepatitis B at minimum) documented for all laboratory staff;
- spill kit available and staff trained in its use.

Training is provided at induction and {D('annually')}. Training records are maintained by the laboratory in-charge.""",

f"""5.3 Patient screening before imaging

Patients are appropriately screened for safety and risk before imaging:

- pregnancy screening: every female patient of childbearing age is asked about pregnancy before any radiation examination; a positive or uncertain answer triggers the {D('radiologist or imaging in-charge')} review before proceeding;
- allergy history for contrast media where contrast is planned;
- implant and device check for MRI where MRI is provided;
- renal function check where contrast nephrotoxicity is a risk;
- patient identification confirmed with two identifiers before the examination.

Screening results are documented in the imaging request or a screening checklist.""",

f"""5.4 Radiation safety devices and training

Imaging personnel and patients use appropriate radiation safety and monitoring devices where applicable, and are trained in imaging safety practices and radiation-safety measures:

- personnel monitoring: TLD badges (or equivalent dosimeters) issued to all staff working with radiation-emitting equipment, read {D('quarterly')} by the approved dosimetry service;
- patient shielding: lead aprons, gonad shields and thyroid shields used where applicable;
- protective equipment for staff: lead aprons, gloves and thyroid collars available and inspected {D('annually')} for cracks;
- ALARA principle (as low as reasonably achievable) applied in technique selection;
- training at induction and {D('annually')} covering radiation physics basics, dose limits, ALARA, emergency procedures and the hospital's radiation-safety manual.

A radiation-safety officer (where AERB requires one) or the imaging in-charge holds the safety manual and dose records.""",

f"""5.5 Imaging signage

Imaging signage is prominently displayed in all appropriate locations:

- radiation warning signs (trefoil symbol) at entrances to rooms housing radiation-emitting equipment;
- "No entry during exposure" signs on X-ray room doors;
- PC-PNDT Act notice (prohibition of sex determination) displayed where ultrasound is provided;
- pregnancy warning notice at imaging reception and inside examination rooms;
- emergency contact number for radiation incidents displayed inside each radiation room.

The imaging in-charge checks signage {D('quarterly')} and replaces damaged or missing signs within {D('seven working days')}.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that laboratory and imaging safety programmes are implemented and resourced.

Laboratory In-Charge
- Manages the laboratory safety programme, PPE provision, training, and safety-incident investigation.

Imaging / Radiology In-Charge
- Manages radiation safety, patient screening, TLD badges, signage, and safety-incident investigation.

Laboratory technicians
- Follow safe practices, use PPE, report safety incidents.

Radiographers
- Follow radiation safety practices, use monitoring devices, screen patients, maintain signage.

Treating doctors and nurses
- Cooperate with safety screening and follow safety rules when in laboratory or imaging areas.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when safety defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Laboratory safety programme current and reviewed after incidents.
- PPE available and used; training records current.
- Patient screening completed and documented before imaging.
- TLD badges issued, read on schedule, dose within limits.
- Patient and staff shielding available and inspected.
- Imaging signage in place at every required location.
- Safety incidents reported, investigated and corrective action taken.

Root-cause analysis is required when the same safety defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when safety incidents, equipment changes or regulatory changes occur."""

TRAINING_ACKNOWLEDGEMENT = f"""All laboratory staff, imaging staff, nurses and treating doctors who work in laboratory or imaging areas are trained on this policy at induction and {D('once a year')} after that. Training covers laboratory safety, PPE, patient screening, radiation safety, ALARA, monitoring devices and signage.

Staff acknowledgement

I have read this Safety Programme in Laboratory and Imaging Services policy of {HOSPITAL}. I will follow the safety, screening, PPE and radiation-safety processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('AAC/POL/06')}
Issue number: {D('01')}
Version: {VERSION} (AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Laboratory In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Access, Assessment and Continuity of Care chapter, standard AAC.6.
- Atomic Energy (Radiation Protection) Rules, 2004 — radiation safety in imaging.
- Bio-Medical Waste Management Rules, 2016 — laboratory waste segregation, treatment and disposal.
- Internal documents of {HOSPITAL}: laboratory safety manual; radiation-safety manual; PPE inventory; TLD dose records; safety-incident register; signage maintenance log."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: laboratory; imaging/radiology department; emergency; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH SHCO chapter 2)
AERB — Atomic Energy Regulatory Board
ALARA — as low as reasonably achievable
BMW — Bio-Medical Waste Management Rules, 2016
CAPA — corrective and preventive action
HIC — Hospital Infection Control (NABH SHCO chapter 3)
MRI — magnetic resonance imaging
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994
PPE — personal protective equipment
SHCO — Standards for Small Healthcare Organisations
TLD — thermoluminescent dosimeter"""

STATUTE_CLAUSE = (
    "the Atomic Energy (Radiation Protection) Rules, 2004, insofar as radiation safety "
    "in imaging is governed under those rules, and the Bio-Medical Waste Management Rules, "
    "2016, insofar as laboratory waste is segregated, treated and disposed of under those rules"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "AAC.6.a",
        "requirement": "The laboratory-safety programme is implemented.",
        "steps": "Section 3; 5.1 Laboratory safety programme; Section 4 items 1, 2",
        "responsible": "Laboratory In-Charge (implement); Medical Superintendent (resource)",
        "records": [
            "Written laboratory safety programme document.",
            "Annual review record and post-incident review records.",
            "Safety-incident reports with investigation and corrective action.",
        ],
    },
    {
        "oe_code": "AAC.6.b",
        "requirement": "Laboratory personnel are appropriately trained in safe practices and are provided with appropriate safety measures.",
        "steps": "Section 3; 5.2 Laboratory safe practices and safety measures; Section 4 item 2",
        "responsible": "Laboratory In-Charge (train and equip); laboratory technicians (comply)",
        "records": [
            "PPE inventory and issue records.",
            "Training records for laboratory safety at induction and annually.",
            "Vaccination records for laboratory staff.",
        ],
    },
    {
        "oe_code": "AAC.6.c",
        "requirement": "Patients are appropriately screened for safety / risk before imaging.",
        "steps": "Section 3; 5.3 Patient screening before imaging; Section 4 item 1",
        "responsible": "Radiographers (screen); Imaging In-Charge (method); treating doctors (provide clinical info)",
        "records": [
            "Screening checklist or imaging request with screening questions completed.",
            "Pregnancy screening records for female patients of childbearing age.",
            "Contrast allergy and renal function check records where applicable.",
        ],
    },
    {
        "oe_code": "AAC.6.d",
        "requirement": "Imaging personnel and patients use appropriate radiation safety and monitoring devices where applicable, and are trained in imaging safety practices and radiation-safety measures.",
        "steps": "Section 3; 5.4 Radiation safety devices and training; Section 4 items 1, 3",
        "responsible": "Imaging In-Charge (manage devices and training); radiographers (use and comply)",
        "records": [
            "TLD badge issue register and quarterly dose reports.",
            "Lead apron and shielding inspection records.",
            "Training records for radiation safety at induction and annually.",
            "Radiation-safety manual held by imaging in-charge or radiation-safety officer.",
        ],
    },
    {
        "oe_code": "AAC.6.e",
        "requirement": "Imaging signage is prominently displayed in all appropriate locations.",
        "steps": "Section 3; 5.5 Imaging signage; Section 4 item 4",
        "responsible": "Imaging In-Charge (maintain signage); Quality Coordinator (audit)",
        "records": [
            "Signage inventory listing each required sign and its location.",
            "Quarterly signage check log.",
            "Replacement records for damaged or missing signs.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """AAC.6 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. AAC.6.a asterisked. Stop-work section 6. P2: AERP Rules 2004 and BMW Rules 2016. Five OEs, five What-we-do subsections."""


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
        "stop_work": STOP_WORK,
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
        "template_test": "aac_v2_adoptable_shape",
        "subtitle": "Laboratory and imaging safety programme.",
        "doc_no": D("AAC/POL/06"),
    }
    emit_pre_v2(
        draft,
        "aac6_v2_draft.json",
        "AAC.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
