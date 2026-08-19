# -*- coding: utf-8 -*-
"""HIC.4 v2 — prevention of HAI in patients and staff.

Shape follows PRE.2 v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 100–101.
Chapter intent: PDF index 98.

HAS stop-work section. Six OEs mapped to six What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HIC.4"
CHAPTER = "HIC"
OE_CODES = ["HIC.4.a", "HIC.4.b", "HIC.4.c", "HIC.4.d", "HIC.4.e", "HIC.4.f"]
POLICY_TITLE = "Prevention of Healthcare Associated Infections in Patients and Staff"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HIC v2 template: adoptable shape, plain English, HIC roles, six steps, stop-work for sharps/PEP.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation takes actions to prevent healthcare associated infections (HAI) in "
    "patients and staff working in the hospital — catheter-associated UTI, ventilator-associated "
    "complications, catheter-linked BSI, surgical site infections, occupational health practices "
    "and post-exposure prophylaxis."
)

PURPOSE = f"""This policy describes the actions {HOSPITAL} takes to prevent specific healthcare-associated infections (HAI) in patients and to reduce occupational infection risk to staff.

It covers prevention of catheter-associated urinary tract infection (CAUTI), infection-related ventilator-associated complication / ventilator-associated pneumonia (IVAC/VAP), catheter-linked blood stream infection (CLABSI), surgical site infection (SSI), occupational health and safety practices for healthcare providers, and post-exposure prophylaxis (PEP).

Boundaries: infection-control occupational response (needlestick, sharps, splash) is owned here; general staff health programmes stay with HRM (not yet built). HIC.5 owns surveillance data that feeds these prevention bundles.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff at {HOSPITAL} who insert, maintain or remove invasive devices, who perform surgical procedures, or who are at risk of occupational exposure to blood and body fluids.

It covers the six elements HIC.4.a–f name: CAUTI prevention, IVAC/VAP prevention, CLABSI prevention, SSI prevention, occupational health/safety practices, and PEP.

Boundaries with other policies of {HOSPITAL}:

- HIC.1 owns programme governance.
- HIC.2 owns standard precautions, hand hygiene and safe injection practices (upstream of device bundles).
- HIC.3 owns support-service infection control (OT housekeeping stays HIC.3).
- HIC.5 owns surveillance of infection rates and trends.
- HIC.6 owns sterilisation of instruments used in procedures.
- HRM (not yet built) owns general staff health; this policy owns infection-control occupational response."""

POLICY_STATEMENT = f"""{HOSPITAL} implements evidence-based bundles to prevent CAUTI, IVAC/VAP, CLABSI and SSI. Occupational health and safety practices reduce the risk of transmitting microorganisms among healthcare providers. Post-exposure prophylaxis is provided to all staff members concerned after a significant exposure.

A needlestick or sharps exposure triggers the stop-work authority defined in this policy."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Inserting a urinary catheter without a documented clinical indication.
2. Leaving a urinary catheter in place beyond the documented need without daily reassessment.
3. Inserting a central venous catheter without full barrier precautions (cap, mask, sterile gown, sterile gloves, large sterile drape).
4. Operating without the SSI prevention bundle (appropriate antibiotic prophylaxis timing, skin preparation, normothermia maintenance, glycaemic control where applicable).
5. Resuming the task that caused a needlestick/sharps/splash exposure before first aid is completed, the incident is reported and PEP assessment has begun.
6. Denying or delaying post-exposure prophylaxis to any staff member who has had a significant exposure."""

PROCEDURE_STEPS = [
f"""5.1 Prevention of catheter-associated urinary tract infection (CAUTI)

{HOSPITAL} takes action to prevent CAUTI through an insertion and maintenance bundle:

- Insert urinary catheters only for accepted indications (documented in the clinical record).
- Use aseptic technique for insertion: hand hygiene, sterile gloves, sterile drape, antiseptic peri-urethral cleaning, sterile closed drainage system.
- Secure the catheter to prevent movement and urethral trauma.
- Maintain a closed drainage system; do not disconnect unless clinically necessary.
- Daily reassessment of continued need; remove as soon as indication no longer exists.
- Document insertion date, indication, and daily reassessment in the patient record.

The Infection Control Nurse monitors CAUTI rates (data from HIC.5) and provides unit-level feedback {D('monthly')}.""",

f"""5.2 Prevention of ventilator-associated complication / VAP

{HOSPITAL} takes action to prevent infection-related ventilator-associated complication (IVAC) and ventilator-associated pneumonia (VAP) where mechanical ventilation is provided:

- Head-of-bed elevation to {D('30–45 degrees')} unless contraindicated.
- Daily sedation vacation and assessment of readiness to extubate.
- Oral care with {D('chlorhexidine 0.12 %')} per protocol.
- Peptic ulcer prophylaxis per clinical indication.
- Deep vein thrombosis prophylaxis per clinical indication.
- Subglottic secretion drainage where available.
- Hand hygiene before and after contact with ventilator circuit.

Where {HOSPITAL} does not provide mechanical ventilation, this is a recorded absence against the service directory, not a copied SOP.""",

f"""5.3 Prevention of catheter-linked blood stream infection (CLABSI)

{HOSPITAL} takes action to prevent CLABSI through a central-line insertion and maintenance bundle:

- Hand hygiene and maximal sterile barrier precautions for insertion.
- Chlorhexidine-based skin antisepsis at the insertion site.
- Optimal catheter site selection (subclavian preferred where clinically appropriate; avoid femoral where possible).
- Daily review of line necessity; remove as soon as no longer required.
- Standardised dressing changes using aseptic technique.
- Hub/port scrub before every access.

Where {HOSPITAL} does not insert central lines, this is a recorded absence against the service directory. Peripheral IV care follows aseptic insertion and maintenance bundles (HIC.2.d).""",

f"""5.4 Prevention of surgical site infection (SSI)

{HOSPITAL} takes action to prevent SSI through pre-operative, intra-operative and post-operative measures:

Pre-operative:
- Appropriate antibiotic prophylaxis administered within {D('60 minutes')} before incision (per antimicrobial policy HIC.2.e).
- Surgical-site skin preparation with {D('chlorhexidine-alcohol or povidone-iodine')}.
- Patient bathing/showering before surgery where feasible.
- Avoid routine hair removal; if required, use clippers (not razors).

Intra-operative:
- Maintain normothermia (core temperature ≥ 36 °C).
- Glycaemic control in diabetic patients.
- Sterile technique throughout; instrument sterility per HIC.6.

Post-operative:
- Sterile wound dressing change with hand hygiene and aseptic non-touch technique.
- Surveillance for SSI up to {D('30 days')} (or {D('90 days')} for implant surgery).
- SSI rates reported to the Infection Control Committee.""",

f"""5.5 Occupational health and safety — reducing transmission among healthcare providers

{HOSPITAL} implements occupational health and safety practices to reduce the risk of transmitting microorganisms among healthcare providers:

- Standard precautions and PPE use as per HIC.2.a.
- Immunisation of staff: hepatitis B vaccination (and titre confirmation), annual influenza vaccination (where available), and any outbreak-specific vaccination.
- Sharps safety: needle-free systems where feasible, safety-engineered devices, no manual recapping.
- Fit-testing for N95 respirators for staff in airborne-precaution areas.
- Staff with transmissible infections (active TB, chickenpox, measles, conjunctivitis) are restricted from patient contact per written guidance.

A sharps injury or significant mucocutaneous exposure triggers the stop-work authority in section 6.""",

f"""5.6 Post-exposure prophylaxis (PEP)

Appropriate post-exposure prophylaxis is provided to all staff members concerned after a significant exposure (needlestick, sharps injury, splash to mucous membrane or non-intact skin from blood or body fluid of a source patient):

- Immediate first aid: wash the wound with soap and water (do not squeeze); flush mucous membrane with water.
- Report the incident to the {D('Infection Control Officer or the duty medical officer')} within {D('1 hour')}.
- Risk assessment: source-patient status (HIV, HBV, HCV), nature of exposure, staff vaccination status.
- PEP initiation: HIV PEP within {D('2 hours')} (and no later than 72 hours); HBV immunoglobulin/booster as indicated.
- Counselling, baseline blood draw and follow-up testing at {D('6 weeks, 3 months and 6 months')}.
- Confidential documentation in the staff occupational health record.

PEP medications are available {D('24 hours a day, 7 days a week')} — stocked in the {D('emergency pharmacy or the emergency department')}.""",
]

STOP_WORK = f"""Any staff member who sustains a needlestick injury, sharps injury or significant splash exposure to blood or body fluid must STOP the task immediately.

Do not resume the task until:
1. First aid has been completed (wash with soap and water; flush mucous membrane).
2. The incident has been reported to the {D('Infection Control Officer or duty medical officer')}.
3. PEP assessment has begun (risk assessment and decision on prophylaxis).

The exposed staff member's patient care responsibility is handed over to another qualified person for the duration of first aid and reporting. No disciplinary action follows from invoking stop-work for a genuine exposure.

The Infection Control Officer may also invoke stop-work authority if a pattern of sharps injuries in a unit indicates an unsafe device or procedure that requires immediate investigation before further use."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for device-bundle implementation, PEP availability and occupational health resources.

Infection Control Officer
- Oversees bundle compliance, PEP protocol, and occupational exposure investigations.

Infection Control Nurse
- Monitors bundle compliance, device-day data, and provides unit-level feedback.

Treating doctors
- Insert and maintain devices per bundles; prescribe prophylaxis per policy; report exposures.

Nurses
- Maintain devices per bundles; perform daily reassessment; administer PEP; report exposures.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA closure."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

- CAUTI bundle compliance and catheter-day rates.
- VAP bundle compliance and ventilator-day rates (where applicable).
- CLABSI bundle compliance and line-day rates (where applicable).
- SSI rates by procedure category.
- Occupational exposure reports and PEP timeliness.
- Stop-work invocations and their outcomes.

Root-cause analysis is required when a device-associated infection rate exceeds the {D('national benchmark')} for two consecutive quarters, or when PEP was delayed beyond 2 hours.

This policy is reviewed {D('annually')}, and sooner when bundle evidence is updated or after a cluster of device-associated infections."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff are trained on this policy at induction and {D('once a year')} after that. Training covers insertion and maintenance bundles, sharps safety, exposure reporting, PEP access and the stop-work authority.

Staff acknowledgement

I have read this Prevention of HAI in Patients and Staff policy of {HOSPITAL}. I understand the device bundles, the stop-work authority for sharps exposure, and how to access PEP.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Infection Control Officer holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="HIC/POL/04",
    version=VERSION,
    prepared_by=D("Infection Control Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — HIC chapter, standard HIC.4.
- CDC/HICPAC Guidelines for Prevention of Catheter-Associated Urinary Tract Infections (2009, updated 2017).
- CDC Guidelines for Prevention of Intravascular Catheter-Related Infections (2011).
- WHO Global Guidelines for the Prevention of Surgical Site Infection (2018).
- NACO Guidelines on Post-Exposure Prophylaxis (updated 2018).
- Internal documents of {HOSPITAL}: CAUTI bundle protocol, CLABSI bundle, SSI bundle, VAP bundle (where applicable), PEP protocol, sharps injury register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Infection Control Officer and the Quality Coordinator.

Copies issued to: all clinical areas (OPD, IPD, emergency, OT, ICU where available), CSSD, nursing administration, pharmacy (PEP stock).

The current version is available to all staff at the {D('infection control manual / staff intranet')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAUTI — catheter-associated urinary tract infection
CAPA — corrective and preventive action
CLABSI — central-line-associated blood stream infection
HAI — healthcare-associated infection
HBV — hepatitis B virus
HCV — hepatitis C virus
HIC — Hospital Infection Prevention and Control (NABH SHCO chapter)
HIV — human immunodeficiency virus
HRM — Human Resource Management (NABH SHCO chapter; not yet built)
IVAC — infection-related ventilator-associated complication
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NACO — National AIDS Control Organisation
OE — objective element
PEP — post-exposure prophylaxis
PPE — personal protective equipment
SHCO — Standards for Small Healthcare Organisations
SSI — surgical site infection
VAP — ventilator-associated pneumonia
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HIC.4.a",
        "requirement": "The organisation takes action to prevent catheter-associated urinary tract infections.",
        "steps": "Section 3; 5.1 Prevention of CAUTI",
        "responsible": "Treating doctors and nurses (bundle compliance); Infection Control Nurse (monitor rates)",
        "records": [
            "CAUTI bundle insertion checklist (indication, aseptic technique, securing).",
            "Daily catheter reassessment records in patient chart.",
            "CAUTI rate per 1000 catheter-days reported to ICC.",
            "Unit-level feedback records on bundle compliance.",
        ],
    },
    {
        "oe_code": "HIC.4.b",
        "requirement": "The organisation takes action to prevent infection-related ventilator associated complication/ventilator-associated pneumonia.",
        "steps": "Section 3; 5.2 Prevention of ventilator-associated complication / VAP",
        "responsible": "ICU doctors and nurses (bundle compliance); Infection Control Nurse (monitor); or recorded absence",
        "records": [
            "VAP bundle checklist (head elevation, sedation vacation, oral care, DVT/PUD prophylaxis).",
            "VAP rate per 1000 ventilator-days reported to ICC.",
            "Recorded absence where mechanical ventilation is not provided.",
            "Unit-level feedback on bundle compliance.",
        ],
    },
    {
        "oe_code": "HIC.4.c",
        "requirement": "The organisation takes action to prevent catheter linked blood stream infections.",
        "steps": "Section 3; 5.3 Prevention of CLABSI",
        "responsible": "Treating doctors (insertion bundle); nurses (maintenance bundle); Infection Control Nurse (monitor); or recorded absence",
        "records": [
            "Central-line insertion bundle checklist (barrier precautions, skin antisepsis, site selection).",
            "Daily line necessity review records.",
            "CLABSI rate per 1000 line-days reported to ICC.",
            "Recorded absence where central lines are not inserted.",
        ],
    },
    {
        "oe_code": "HIC.4.d",
        "requirement": "The organisation takes action to prevent surgical site infections.",
        "steps": "Section 3; 5.4 Prevention of SSI",
        "responsible": "Surgeons (pre-/intra-operative bundle); nurses (post-operative wound care); Infection Control Nurse (surveillance)",
        "records": [
            "SSI prevention bundle checklist (prophylaxis timing, skin prep, normothermia, glucose control).",
            "SSI surveillance records up to 30/90 days post-procedure.",
            "SSI rates by procedure category reported to ICC.",
            "RCA for SSI clusters or rates above benchmark.",
        ],
    },
    {
        "oe_code": "HIC.4.e",
        "requirement": "The organisation implements occupational health and safety practices to reduce the risk of transmitting microorganisms among health care providers.",
        "steps": "Section 3; 5.5 Occupational health and safety; Section 6 (stop-work)",
        "responsible": "Infection Control Officer (programme); all staff (comply); Medical Superintendent (resources)",
        "records": [
            "Staff immunisation register (hepatitis B titre, influenza, others).",
            "Sharps injury register and trend analysis.",
            "Fit-test records for N95 respirators.",
            "Work-restriction log for staff with transmissible infections.",
        ],
    },
    {
        "oe_code": "HIC.4.f",
        "requirement": "Appropriate post-exposure prophylaxis is provided to all staff members concerned.",
        "steps": "Section 3; 5.6 Post-exposure prophylaxis; Section 6 (stop-work); Section 4 items 5, 6",
        "responsible": "Infection Control Officer or duty medical officer (assess and initiate PEP); pharmacy (stock PEP medicines 24/7)",
        "records": [
            "Exposure incident report with first-aid and reporting timestamps.",
            "Risk assessment form (source status, exposure type, staff vaccination).",
            "PEP prescription and initiation time record.",
            "Follow-up blood test results at 6 weeks, 3 months and 6 months.",
            "Confidential occupational health file for each exposed staff member.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HIC.4 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation takes actions to prevent healthcare associated infections (HAI) in patients and staff working in the hospital." HIC.4.a–f PDF indices 100–101. One asterisked OE: HIC.4.f (Commitment). Stop-work YES (needlestick/sharps → stop, PEP, report).

SHAPE: Six What-we-do subsections (5.1–5.6). Stop-work section present. Disclaimer accreditation-only. HIC roles."""


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
        "template_test": "hic_v2_adoptable_shape",
        "subtitle": "Preventing device-associated infections and occupational exposure.",
        "doc_no": "HIC/POL/04",
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "hic4_v2_draft.json",
        "HIC.4_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
