# -*- coding: utf-8 -*-
"""HIC.3 v2 — infection prevention and control in support services.

Shape follows PRE.2 v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 100.
Chapter intent: PDF index 98.

No stop-work section. Six OEs mapped to six What-we-do subsections.
Disclaimer P2 uses make_disclaimer with BMW statute clause.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HIC.3"
CHAPTER = "HIC"
OE_CODES = ["HIC.3.a", "HIC.3.b", "HIC.3.c", "HIC.3.d", "HIC.3.e", "HIC.3.f"]
POLICY_TITLE = "Infection Prevention and Control in Support Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HIC v2 template: adoptable shape, plain English, HIC roles, six steps, no stop-work.",
    },
]

STATUTE_CLAUSE = "the Bio-Medical Waste Management Rules, 2016, insofar as biomedical waste is segregated, treated and disposed of under those rules"
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

STATEMENT_OF_INTENT = (
    "The organisation implements the infection prevention and control programme in support "
    "services — engineering controls, construction/renovation infection risk, housekeeping, "
    "bio-medical waste (BMW), laundry/linen and kitchen sanitation."
)

PURPOSE = f"""This policy describes how {HOSPITAL} implements infection prevention and control in support services: engineering controls, infection risk during construction/renovation, housekeeping, bio-medical waste (BMW) management, laundry and linen management, and kitchen sanitation and food handling.

Boundaries: waste/linen/kitchen infection mechanics are owned here; facilities environment engineering stays with FMS. BMW segregation, treatment and disposal under the Bio-Medical Waste Management Rules, 2016 are addressed here to the extent they are an infection-control requirement.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all support service areas of {HOSPITAL}: maintenance/engineering, housekeeping, bio-medical waste handling, laundry, kitchen/pantry, and any construction/renovation project.

It covers the six elements HIC.3.a–f name: engineering controls, construction/renovation ICRA, housekeeping procedures, BMW handling, laundry/linen management, and kitchen sanitation.

Boundaries with other policies of {HOSPITAL}:

- FMS owns the built environment, HVAC maintenance schedules and fire safety; this policy owns infection-prevention engineering controls.
- HIC.1 owns programme governance.
- HIC.2 owns clinical practices (hand hygiene, standard precautions, antimicrobials).
- HIC.4 owns prevention of specific HAI and occupational health.
- HIC.5 owns surveillance including housekeeping effectiveness monitoring.
- HIC.6 owns sterilisation/disinfection of instruments and devices.
- MOM.9 owns implant procurement/traceability; this policy does not cover procurement."""

POLICY_STATEMENT = f"""{HOSPITAL} ensures appropriate engineering controls to prevent infections. Construction and renovation projects are planned with an infection control risk assessment (ICRA). Housekeeping procedures follow defined protocols. BMW is handled safely under the Bio-Medical Waste Management Rules, 2016. Laundry and linen management and kitchen sanitation processes are followed to prevent cross-contamination."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Undertaking construction or renovation in or adjacent to patient-care areas without a documented infection control risk assessment (ICRA) and mitigation plan.
2. Mixing BMW colour-coded categories during segregation at source.
3. Storing untreated BMW beyond {D('48 hours')} (or the time limit prescribed under the BMW Rules, 2016).
4. Using visibly soiled or damp linen on patient beds.
5. Allowing kitchen staff to handle food without hand washing, hair covering, and clean protective clothing.
6. Disabling or bypassing engineering controls (negative-pressure, HEPA filtration, air changes) without written authorisation from the Infection Control Officer."""

PROCEDURE_STEPS = [
f"""5.1 Engineering controls to prevent infections

{HOSPITAL} maintains appropriate engineering controls including:

- Adequate ventilation and air changes in clinical areas per ASHRAE/ISHRAE or national guidelines — {D('minimum 6 air changes per hour in general wards, 12 in OT, negative pressure in isolation rooms')}.
- HEPA filtration where required (OT, isolation).
- Potable water quality monitoring and storage tank cleaning {D('quarterly')}.
- Sewage treatment / effluent management to prevent environmental contamination.

The Infection Control Officer and the maintenance team conduct a joint round {D('monthly')} to verify engineering controls are functioning. Deficiencies are reported to FMS for correction and tracked to closure.""",

f"""5.2 Infection control risk during construction and renovation

Before any construction or renovation in or adjacent to patient-care areas, the Infection Control Officer completes an Infection Control Risk Assessment (ICRA). The ICRA classifies project type and patient-risk group to determine required precautions:

- Dust barriers, negative-pressure in construction zone, sealed windows.
- Alternate traffic routes for construction workers and debris.
- Air monitoring during and after the project.
- Terminal cleaning before the area is returned to clinical use.

The ICRA and mitigation plan are approved by the {D('Medical Superintendent')} before work begins. Compliance is monitored by the Infection Control Nurse during the project.""",

f"""5.3 Housekeeping procedures

{HOSPITAL} adheres to housekeeping procedures that prevent cross-contamination:

- Cleaning schedules define frequency for each area (high-risk areas {D('three times a day plus terminal cleaning after discharge')}).
- Colour-coded cleaning equipment (mops, buckets, cloths) prevents cross-contamination between areas.
- Disinfectant selection and dilution are per the Infection Control Committee's approved list.
- Spill management protocol: contain, disinfect, clean, dispose.
- Terminal cleaning after isolation/barrier nursing discharge.
- Housekeeping staff are trained in infection-control cleaning methods at induction and {D('annually')}.

Effectiveness is monitored under HIC.5.e (surveillance of housekeeping).""",

f"""5.4 Bio-medical waste handling

BMW at {HOSPITAL} is segregated at point of generation into colour-coded categories per the Bio-Medical Waste Management Rules, 2016:

- Yellow: human anatomical waste, soiled waste, expired medicines, chemical waste (cytotoxic).
- Red: contaminated recyclable waste (tubing, syringes without needles, gloves).
- White (puncture-proof): sharps (needles, blades, glass).
- Blue: glassware waste (where applicable).

BMW is stored in a designated, secured intermediate storage area for no longer than {D('48 hours')}. Collection, transport, treatment and disposal are handled by the {D('authorised common biomedical waste treatment facility (CBWTF)')} under a valid agreement. Records include daily segregation logs, transport manifests, monthly returns and the annual report to the State Pollution Control Board.""",

f"""5.5 Laundry and linen management

{HOSPITAL} adheres to laundry and linen management processes that prevent infection transmission:

- Soiled linen is collected in leak-proof bags/containers at the point of use; colour coding distinguishes infectious linen from routine soiled linen.
- Transport to the laundry is in covered trolleys on a defined route that avoids clean areas.
- Washing uses thermal disinfection ({D('65 °C for 10 minutes or 71 °C for 3 minutes')}) or chemical disinfection for heat-sensitive items.
- Clean linen is stored in a covered, designated area separate from soiled holding.
- Linen inventory and replacement schedule ensure no visibly damaged or stained linen is in circulation.

The laundry area layout follows a one-way dirty-to-clean flow. Staff handling infectious linen wear PPE (heavy-duty gloves, gown, mask).""",

f"""5.6 Kitchen sanitation and food handling

{HOSPITAL} adheres to kitchen sanitation and food-handling practices that prevent foodborne infection:

- Kitchen staff undergo pre-employment and {D('annual')} medical fitness screening (stool culture, skin examination).
- Personal hygiene: hand washing before handling food, hair covering, clean uniform, no jewellery in food-prep areas.
- Food storage: cold chain maintained ({D('below 5 °C for perishables')}); dry stores above floor level; FIFO rotation.
- Cooking: core temperature of cooked food reaches {D('74 °C')}.
- Serving: food served within {D('2 hours')} of cooking or kept hot at ≥ 63 °C; therapeutic diets labelled and dispatched per dietitian order.
- Cleaning: kitchen surfaces and equipment sanitised {D('after every meal service')}; pest control {D('monthly')}.
- Water used in kitchen is tested for potability {D('quarterly')}.

Records include food-handler medical clearance, daily temperature logs, pest control reports and cleaning schedules.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for resources, ICRA approval and support-service standards.

Infection Control Officer
- Conducts ICRA, approves disinfectant list, oversees engineering controls jointly with maintenance.

Infection Control Nurse
- Monitors housekeeping, laundry and kitchen practices; trains support staff.

Infection Control Committee
- Reviews audit findings, approves BMW SOPs and cleaning protocols.

Housekeeping In-Charge
- Implements cleaning schedules, spill management and colour-coding compliance.

BMW handler / waste management coordinator
- Ensures segregation, storage, transport and disposal per the BMW Rules, 2016.

Laundry In-Charge
- Maintains dirty-to-clean flow, thermal/chemical disinfection parameters and linen inventory.

Kitchen / Dietetics In-Charge
- Ensures food-handler hygiene, cold chain, cooking temperatures and kitchen cleaning.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA closure."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

- Engineering control verification records (ventilation, water quality).
- ICRA completion and compliance for any ongoing construction/renovation.
- Housekeeping schedule adherence and colour-coding compliance.
- BMW segregation accuracy, storage time compliance, CBWTF records.
- Laundry process parameters (temperature logs, clean-linen culture results where done).
- Kitchen sanitation: food-handler medicals, temperature logs, pest control.

Root-cause analysis is required when BMW segregation errors exceed {D('5 %')} in a monthly audit or when a foodborne illness cluster is traced to the kitchen.

This policy is reviewed {D('annually')}, and sooner when the BMW Rules are amended or after an infection linked to a support service."""

TRAINING_ACKNOWLEDGEMENT = f"""All support-service staff (housekeeping, BMW handlers, laundry, kitchen) are trained on this policy at induction and {D('once a year')} after that. Training covers colour coding, PPE use, hand hygiene, cleaning methods, and reporting spills or breaches.

Staff acknowledgement

I have read this Infection Prevention and Control in Support Services policy of {HOSPITAL}. I will follow the procedures for my area and report breaches immediately.


Name: ___________________________    Designation: ___________________________

Department / area: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Infection Control Nurse holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="HIC/POL/03",
    version=VERSION,
    prepared_by=D("Infection Control Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — HIC chapter, standard HIC.3.
- Bio-Medical Waste Management Rules, 2016, and amendments (Ministry of Environment, Forest and Climate Change, India).
- Guidelines on Airborne Infection Control, National Centre for Disease Control, India.
- WHO Best Practices for Environmental Cleaning in Healthcare Facilities (2019).
- Internal documents of {HOSPITAL}: housekeeping SOP, BMW SOP, laundry SOP, kitchen sanitation SOP, ICRA template."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Infection Control Officer and the Quality Coordinator.

Copies issued to: housekeeping, BMW room, laundry, kitchen, maintenance/engineering, nursing administration.

The current version is available to all staff at the {D('infection control manual / staff intranet')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """BMW — bio-medical waste
CAPA — corrective and preventive action
CBWTF — common biomedical waste treatment facility
FMS — Facility Management and Safety (NABH SHCO chapter)
HAI — healthcare-associated infection
HEPA — high-efficiency particulate air
HIC — Hospital Infection Prevention and Control (NABH SHCO chapter)
ICRA — infection control risk assessment
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PPE — personal protective equipment
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

OE_MAPPING = [
    {
        "oe_code": "HIC.3.a",
        "requirement": "The organisation has appropriate engineering controls to prevent infections.",
        "steps": "Section 3; 5.1 Engineering controls to prevent infections",
        "responsible": "Infection Control Officer (specify requirements); maintenance team (implement); FMS (infrastructure)",
        "records": [
            "Engineering control specifications (air changes, filtration, water treatment) per area.",
            "Joint monthly verification round records (ICO + maintenance).",
            "Deficiency reports and closure tracking.",
            "Water quality test reports (potability, storage tank cleaning).",
        ],
    },
    {
        "oe_code": "HIC.3.b",
        "requirement": "The organisation designs and implements a plan to reduce the risk of infection during construction and renovation.",
        "steps": "Section 3; 5.2 Infection control risk during construction and renovation; Section 4 item 1",
        "responsible": "Infection Control Officer (ICRA); Medical Superintendent (approve); project contractor (comply)",
        "records": [
            "Completed ICRA form for each project with risk classification and precautions.",
            "Approval record signed before work commences.",
            "Compliance monitoring records during the project.",
            "Terminal cleaning verification before area returned to clinical use.",
        ],
    },
    {
        "oe_code": "HIC.3.c",
        "requirement": "The organisation adheres to housekeeping procedures.",
        "steps": "Section 3; 5.3 Housekeeping procedures",
        "responsible": "Housekeeping In-Charge (implement); Infection Control Nurse (monitor); HIC.5.e (surveillance)",
        "records": [
            "Area-wise cleaning schedule with frequency and method.",
            "Colour-coded equipment allocation register.",
            "Disinfectant dilution and usage log.",
            "Spill management incident records.",
            "Terminal cleaning records after isolation discharge.",
        ],
    },
    {
        "oe_code": "HIC.3.d",
        "requirement": "Biomedical waste (BMW) is handled appropriately and safely.",
        "steps": "Section 3; 5.4 Bio-medical waste handling; Section 4 items 2, 3",
        "responsible": "BMW handler/coordinator (day-to-day); Infection Control Officer (oversee); all staff (segregate at source)",
        "records": [
            "Daily BMW segregation log by category and weight.",
            "CBWTF agreement and collection manifests.",
            "Monthly returns and annual report to State Pollution Control Board.",
            "Training records for BMW handlers.",
            "Incident reports for segregation breaches.",
        ],
    },
    {
        "oe_code": "HIC.3.e",
        "requirement": "The organisation adheres to laundry and linen management processes.",
        "steps": "Section 3; 5.5 Laundry and linen management; Section 4 item 4",
        "responsible": "Laundry In-Charge (process); Infection Control Nurse (audit); housekeeping (collection at ward)",
        "records": [
            "Laundry process protocol with thermal/chemical disinfection parameters.",
            "Temperature log of wash cycles.",
            "Linen inventory and replacement schedule.",
            "Layout diagram showing dirty-to-clean one-way flow.",
        ],
    },
    {
        "oe_code": "HIC.3.f",
        "requirement": "The organisation adheres to kitchen sanitation and food-handling issues.",
        "steps": "Section 3; 5.6 Kitchen sanitation and food handling; Section 4 item 5",
        "responsible": "Kitchen/Dietetics In-Charge (implement); Infection Control Nurse (audit); Medical Superintendent (medical clearance oversight)",
        "records": [
            "Food-handler medical fitness records (pre-employment and annual).",
            "Daily food temperature logs (storage, cooking, serving).",
            "Pest control schedule and reports.",
            "Kitchen cleaning schedule and surface sanitisation records.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HIC.3 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation implements the infection prevention and control programme in support services." HIC.3.a–f PDF index 100. Three asterisked OEs: HIC.3.a, HIC.3.b, HIC.3.e (Commitment). No stop-work.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer with BMW statute clause. HIC roles."""


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
        "subtitle": "Infection control in engineering, housekeeping, waste, laundry and kitchen.",
        "doc_no": "HIC/POL/03",
    }
    emit_pre_v2(
        draft,
        "hic3_v2_draft.json",
        "HIC.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
