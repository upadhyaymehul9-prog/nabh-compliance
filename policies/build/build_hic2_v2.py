# -*- coding: utf-8 -*-
"""HIC.2 v2 — infection prevention and control in clinical areas.

Shape follows PRE.2 v2 (section list and order only). Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 99–100.
Chapter intent: PDF index 98.

No stop-work section. Seven OEs mapped to seven What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HIC.2"
CHAPTER = "HIC"
OE_CODES = [
    "HIC.2.a", "HIC.2.b", "HIC.2.c", "HIC.2.d", "HIC.2.e", "HIC.2.f", "HIC.2.g",
]
POLICY_TITLE = "Infection Prevention and Control in Clinical Areas"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HIC v2 template: adoptable shape, plain English, HIC roles, seven steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation implements the infection prevention and control programme in clinical "
    "areas — through standard precautions, hand hygiene, transmission-based precautions, safe "
    "injection practices, and antimicrobial stewardship."
)

PURPOSE = f"""This policy describes how {HOSPITAL} implements infection prevention and control in clinical areas through adherence to standard precautions, hand-hygiene guidelines, transmission-based precautions, safe injection and infusion practices, antimicrobial usage policy, monitoring of rational antimicrobial use, and an antibiotic stewardship programme.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical areas of {HOSPITAL} and to every healthcare provider who delivers patient care — doctors, nurses, technicians, phlebotomists, and allied health professionals.

It covers the seven elements HIC.2.a–g name: standard precautions, hand hygiene, transmission-based precautions, safe injection/infusion, antimicrobial usage policy, monitoring rational use, and antibiotic stewardship.

Boundaries with other policies of {HOSPITAL}:

- HIC.1 owns programme governance, committee structure and resources.
- HIC.3 owns support-service infection control (housekeeping, BMW, laundry, kitchen, engineering).
- HIC.4 owns prevention of specific HAI (CAUTI, VAP, CLABSI, SSI) and occupational safety.
- HIC.5 owns surveillance including hand-hygiene compliance monitoring.
- HIC.6 owns sterilisation and disinfection of instruments and devices."""

POLICY_STATEMENT = f"""{HOSPITAL} adheres to standard precautions at all times in all clinical areas. Hand-hygiene guidelines are followed by all healthcare providers. Transmission-based precautions are applied when indicated. Safe injection and infusion practices are maintained.

An antimicrobial usage policy based on local sensitivity data is established and documented. Rational use of antimicrobial agents is monitored. An antibiotic stewardship programme is implemented to optimise antimicrobial use and reduce resistance."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Providing patient care without applying standard precautions (gloves for contact with blood/body fluids, gown/eye protection when splash is anticipated).
2. Skipping hand hygiene at any of the WHO five moments.
3. Recapping needles by hand after use.
4. Using multi-dose vials without following aseptic technique or beyond the labelled expiry after opening.
5. Prescribing restricted antimicrobials without authorisation from the antimicrobial stewardship team.
6. Failing to apply transmission-based precautions when the patient's condition or laboratory results indicate an airborne, droplet or contact transmission risk.
7. Reusing single-use injection or infusion devices."""

PROCEDURE_STEPS = [
f"""5.1 Standard precautions

All healthcare providers at {HOSPITAL} adhere to standard precautions at all times regardless of the patient's diagnosis or presumed infection status. Standard precautions include:

- Hand hygiene before and after patient contact.
- Use of personal protective equipment (PPE) — gloves, gown, mask, eye protection — based on anticipated exposure.
- Safe handling and disposal of sharps.
- Respiratory hygiene and cough etiquette.
- Safe handling of patient-care equipment and linen.
- Environmental cleaning.
- Safe waste management (cross-reference HIC.3.d).

PPE is available at point of use in every clinical area. Correct donning and doffing sequences are displayed.""",

f"""5.2 Hand-hygiene guidelines

{HOSPITAL} adheres to the WHO five moments for hand hygiene: before patient contact, before aseptic task, after body-fluid exposure risk, after patient contact, and after contact with patient surroundings.

Alcohol-based hand rub (ABHR) dispensers are placed at {D('every bed, procedure area entry and nursing station')}. Soap and running water are available at all hand-wash sinks. Hand-hygiene technique posters (WHO or equivalent) are displayed at every sink and ABHR station.

Hand-hygiene compliance is monitored under HIC.5.b. Feedback is shared {D('monthly')} with each clinical unit.""",

f"""5.3 Transmission-based precautions

In addition to standard precautions, {HOSPITAL} applies transmission-based precautions (contact, droplet, airborne) when indicated by the patient's condition, culture results or epidemiological assessment.

- Contact precautions: gown and gloves for all contact; dedicated equipment; single room or cohorting.
- Droplet precautions: surgical mask within {D('1 metre')} of the patient; single room preferred.
- Airborne precautions: N95 respirator; negative-pressure room where available (HIC.1.f); door closed.

Signage is placed at the room/bed indicating the precaution type. De-escalation criteria are documented.""",

f"""5.4 Safe injection and infusion practices

{HOSPITAL} adheres to safe injection and infusion practices:

- Use a new sterile syringe and needle for each injection.
- Never recap needles by hand; use a needle destroyer or safety-engineered device.
- Use single-dose vials whenever possible; if multi-dose vials are used, maintain aseptic technique and label with date of opening and discard after {D('28 days or manufacturer instruction, whichever is shorter')}.
- Prepare injections in a clean, designated area away from contaminated items.
- Use aseptic technique for all intravenous access and infusion preparation.
- Change IV administration sets per protocol — {D('every 72–96 hours for continuous infusions; immediately after blood products or lipids')}.

Phlebotomy and IV cannulation follow a written aseptic insertion and maintenance bundle.""",

f"""5.5 Antimicrobial usage policy

{HOSPITAL} has an antimicrobial usage policy that is established and documented. The policy is based on:

- Local antibiogram data (updated {D('annually')} from the hospital's own culture and sensitivity results or, where volume is insufficient, from regional data).
- National treatment guidelines (ICMR / IDSA or equivalent).
- Classification of antimicrobials into unrestricted, restricted and reserve categories.

The policy defines empirical therapy recommendations for common infections, criteria for escalation/de-escalation, duration guidance, and surgical prophylaxis protocols. The policy is approved by the Infection Control Committee and available to all prescribers.""",

f"""5.6 Monitoring rational antimicrobial use

The Infection Control Committee and the antimicrobial stewardship team monitor rational use of antimicrobial agents at {HOSPITAL}:

- Prescription audits are conducted {D('monthly')} on a sample of inpatient records.
- Compliance with the antimicrobial usage policy (empirical choice, de-escalation, duration) is measured.
- Restricted-category antimicrobial usage is tracked by volume and indication.
- Feedback is provided to prescribers {D('quarterly')}.
- Non-compliance trends are escalated to the Medical Superintendent.""",

f"""5.7 Antibiotic stewardship programme

{HOSPITAL} implements an antibiotic stewardship programme (ASP) to optimise antimicrobial therapy, improve patient outcomes and reduce antimicrobial resistance.

The ASP includes:

- Prospective audit with intervention and feedback (stewardship rounds {D('twice a week')}).
- Formulary restriction and pre-authorisation for reserve antimicrobials.
- Automatic stop orders and mandatory review at {D('72 hours')} for empirical therapy.
- Education of prescribers on resistance patterns and appropriate prescribing.
- Monitoring of defined daily dose (DDD) / days of therapy (DOT) trends.
- Annual review of the programme's impact on resistance patterns, consumption and clinical outcomes.

The ASP team includes at minimum the Infection Control Officer, a clinical pharmacist (or the {D('senior nurse trained in antibiotic stewardship')}), and a microbiologist (or access to microbiology consultation).""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for resources, antimicrobial policy approval, and stewardship programme support.

Infection Control Officer (doctor)
- Leads the antimicrobial stewardship programme; chairs stewardship rounds.

Infection Control Nurse
- Monitors hand-hygiene and standard-precaution compliance; supports training.

Infection Control Committee
- Approves the antimicrobial usage policy; reviews audit findings and resistance data.

Treating doctors
- Prescribe antimicrobials per the approved policy; comply with stewardship recommendations.

Nurses
- Apply standard and transmission-based precautions; maintain hand hygiene; administer injections/infusions safely.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA closure."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

- Standard-precaution compliance observations in clinical areas.
- Hand-hygiene compliance rates (data from HIC.5.b).
- Transmission-based precaution appropriateness and signage.
- Safe injection/infusion practice observations.
- Antimicrobial prescription audit results and stewardship intervention acceptance rate.
- ASP outcome metrics (DDD/DOT trends, resistance patterns).

Root-cause analysis is required when hand-hygiene compliance falls below {D('80 %')} in any unit for two consecutive months, or when a restricted antimicrobial is used without authorisation.

This policy is reviewed {D('annually')}, and sooner when local antibiogram data changes significantly or after an outbreak."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff are trained on this policy at induction and {D('once a year')} after that. Training covers standard precautions, hand hygiene, transmission-based precautions, safe injection practices, and the antimicrobial usage policy.

Staff acknowledgement

I have read this Infection Prevention and Control in Clinical Areas policy of {HOSPITAL}. I will adhere to standard precautions, hand-hygiene guidelines, and the antimicrobial usage policy.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Infection Control Nurse holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="HIC/POL/02",
    version=VERSION,
    prepared_by=D("Infection Control Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — HIC chapter, standard HIC.2.
- WHO Guidelines on Hand Hygiene in Health Care (2009).
- WHO Guidelines on Core Components of Infection Prevention and Control Programmes (2016).
- Indian Council of Medical Research (ICMR), Treatment Guidelines for Antimicrobial Use in Common Syndromes (2019).
- Internal documents of {HOSPITAL}: antimicrobial usage policy, local antibiogram, injection safety protocol, transmission-based precaution guidelines."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Infection Control Officer and the Quality Coordinator.

Copies issued to: all clinical areas (OPD, IPD, emergency, OT, ICU where available), nursing administration, pharmacy.

The current version is available to all staff at the {D('infection control manual / staff intranet')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """ABHR — alcohol-based hand rub
ASP — antibiotic stewardship programme
CAPA — corrective and preventive action
DDD — defined daily dose
DOT — days of therapy
HAI — healthcare-associated infection
HIC — Hospital Infection Prevention and Control (NABH SHCO chapter)
ICMR — Indian Council of Medical Research
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PPE — personal protective equipment
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HIC.2.a",
        "requirement": "The organisation adheres to standard precautions at all times.",
        "steps": "Section 3; 5.1 Standard precautions; Section 4 item 1",
        "responsible": "All clinical staff (apply); Infection Control Nurse (monitor)",
        "records": [
            "Written standard-precaution protocol available in all clinical areas.",
            "PPE stock and availability records at point of use.",
            "Compliance observation records (direct observation or audit tool).",
            "Training records showing all clinical staff trained on standard precautions.",
        ],
    },
    {
        "oe_code": "HIC.2.b",
        "requirement": "The organisation adheres to hand-hygiene guidelines.",
        "steps": "Section 3; 5.2 Hand-hygiene guidelines; Section 4 item 2",
        "responsible": "All healthcare providers (comply); Infection Control Nurse (audit and feedback)",
        "records": [
            "Written hand-hygiene protocol aligned with WHO five moments.",
            "ABHR dispenser and soap availability audit records.",
            "Hand-hygiene compliance rates by unit (data from HIC.5.b).",
            "Feedback shared with clinical units showing compliance trends.",
        ],
    },
    {
        "oe_code": "HIC.2.c",
        "requirement": "The organisation adheres to transmission-based precautions.",
        "steps": "Section 3; 5.3 Transmission-based precautions; Section 4 item 6",
        "responsible": "Treating doctors (initiate); nurses (implement); Infection Control Officer (oversee criteria)",
        "records": [
            "Written transmission-based precaution guidelines (contact, droplet, airborne).",
            "Signage logs showing precaution type displayed at room/bed.",
            "De-escalation criteria and records of de-escalation decisions.",
            "Training records for staff assigned to isolation/precaution areas.",
        ],
    },
    {
        "oe_code": "HIC.2.d",
        "requirement": "The organisation adheres to safe injection and infusion practices.",
        "steps": "Section 3; 5.4 Safe injection and infusion practices; Section 4 items 3, 4, 7",
        "responsible": "Nurses (administer); treating doctors (prescribe); Infection Control Nurse (audit)",
        "records": [
            "Written safe injection and infusion protocol.",
            "Multi-dose vial labelling and discard log.",
            "IV administration set change records per protocol.",
            "Safe injection practice observation audit results.",
        ],
    },
    {
        "oe_code": "HIC.2.e",
        "requirement": "Appropriate antimicrobial usage policy is established and documented.",
        "steps": "Section 3; 5.5 Antimicrobial usage policy; Section 4 item 5",
        "responsible": "Infection Control Committee (approve); Infection Control Officer (draft); pharmacy (implement formulary)",
        "records": [
            "Documented antimicrobial usage policy with empirical therapy recommendations.",
            "Local antibiogram updated at defined frequency.",
            "Classification of antimicrobials into unrestricted, restricted and reserve.",
            "ICC minutes showing policy approval and review.",
        ],
    },
    {
        "oe_code": "HIC.2.f",
        "requirement": "The organisation implements the antimicrobial usage policy and monitors the rational use of antimicrobial agents.",
        "steps": "Section 3; 5.6 Monitoring rational antimicrobial use",
        "responsible": "Antimicrobial stewardship team (audit); treating doctors (prescribe per policy); Infection Control Committee (review)",
        "records": [
            "Monthly prescription audit reports with compliance rates.",
            "Restricted antimicrobial usage log with indications.",
            "Feedback records shared with prescribers.",
            "Escalation records for non-compliance trends.",
        ],
    },
    {
        "oe_code": "HIC.2.g",
        "requirement": "The organisation implements an antibiotic stewardship programme.",
        "steps": "Section 3; 5.7 Antibiotic stewardship programme",
        "responsible": "Infection Control Officer (lead ASP); clinical pharmacist or trained nurse (support); Infection Control Committee (oversight)",
        "records": [
            "ASP charter with team composition, scope, goals and meeting schedule.",
            "Stewardship round records (prospective audit with intervention).",
            "Pre-authorisation and automatic stop-order implementation records.",
            "Annual ASP outcome report (DDD/DOT trends, resistance pattern changes, intervention acceptance rate).",
            "Education session records for prescribers on resistance and prescribing.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HIC.2 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation implements the infection prevention and control programme in clinical areas." HIC.2.a–g PDF indices 99–100. Five asterisked OEs: HIC.2.a, HIC.2.b, HIC.2.d (Core), HIC.2.e (Commitment), HIC.2.g (Excellence). No stop-work.

SHAPE: Seven What-we-do subsections (5.1–5.7). No stop-work. Disclaimer accreditation-only. HIC roles."""


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
        "subtitle": "Clinical infection prevention practices and antimicrobial stewardship.",
        "doc_no": "HIC/POL/02",
    }
    emit_pre_v2(
        draft,
        "hic2_v2_draft.json",
        "HIC.2_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
