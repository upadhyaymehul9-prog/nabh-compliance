# -*- coding: utf-8 -*-
"""COP.12 v2 — identifies and manages patients at higher risk of morbidity and mortality.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 74.
No stop-work section. Six OEs in six What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.12"
CHAPTER = "COP"
OE_CODES = [
    "COP.12.a", "COP.12.b", "COP.12.c", "COP.12.d", "COP.12.e", "COP.12.f",
]
POLICY_TITLE = "Higher-Risk Patients: Identification and Management"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation identifies and manages patients who are at higher risk of morbidity "
    "and mortality — vulnerable patients, fall risk, pressure ulcers, deep vein thrombosis, "
    "and patients who need restraints."
)

PURPOSE = f"""This policy defines how {HOSPITAL} identifies and manages vulnerable patients, provides a safe and secure environment for them, and identifies and manages patients at risk of falls, pressure ulcers, deep vein thrombosis, and patients who need restraints.

Boundaries: PSQ owns patient safety goals; this policy owns clinical identification and management of higher-risk patients. COP.8 owns paediatric-specific safety; this policy owns the broader vulnerable-patient framework.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical staff at {HOSPITAL}: treating doctors, nurses, physiotherapists, and support staff who encounter patients at higher risk of morbidity and mortality.

It covers identification and management of vulnerable patients, fall risk, pressure ulcers, deep vein thrombosis, and restraint use. It does not own patient safety goals (PSQ) or paediatric-specific safety (COP.8)."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies and manages vulnerable patients and provides a safe and secure environment for them. {HOSPITAL} identifies and manages patients at risk of falls, pressure ulcers, and deep vein thrombosis. Where restraints are needed, they are applied safely with documented justification.

{HOSPITAL} does not leave higher-risk patients unidentified or unmanaged because identification tools are absent or staff are untrained."""

NON_NEGOTIABLES = f"""1. Every admitted patient is screened for vulnerability, fall risk, pressure-ulcer risk, and DVT risk using the tools this hospital has adopted.
2. A patient identified at risk has a documented management plan initiated within {D('4 hours')} of identification.
3. Restraints are not applied without documented clinical justification, a doctor's order, and time-limited review.
4. A vulnerable patient is not left in an environment that has been identified as unsafe for that category of vulnerability.
5. Risk reassessment occurs at defined intervals and on clinical change."""

PROCEDURE_STEPS = [
f"""5.1 Identification and management of vulnerable patients

{HOSPITAL} identifies vulnerable patients at or soon after admission. Vulnerable categories include {D('elderly, paediatric (cross-reference COP.8), mentally ill, physically disabled, patients with communication barriers, and any patient the treating team identifies as at higher risk')}.

Identification uses {D('a vulnerability screening tool completed by the admitting nurse')}. For each vulnerable patient a documented management plan covers the specific risks, interventions, environment checks, and communication needs. The {D('ward nurse in-charge')} ensures the plan is initiated and communicated to the treating team.""",

f"""5.2 Safe and secure environment for vulnerable patients

{HOSPITAL} provides a safe and secure environment for vulnerable patients. Environmental measures include {D('bed-rail use, call-bell accessibility, adequate lighting, non-slip flooring, visual cues for cognitively impaired patients, and secure unit access where needed')}.

The {D('ward nurse in-charge')} verifies the environment for each identified vulnerable patient on admission and at each shift change. Deficiencies are escalated to the {D('facility manager')} for correction.""",

f"""5.3 Fall-risk identification and management

{HOSPITAL} identifies and manages patients at risk of falls. Screening uses {D('the Morse Fall Scale or equivalent validated tool')} at admission, at defined intervals ({D('every shift for high-risk patients')}), and on clinical change.

Management includes {D('fall-risk signage, bed-rail protocol, footwear check, medication review for fall-contributing drugs, mobility assessment, toileting assistance, and patient/family education')}. Falls are reported, investigated, and entered into the incident register. PSQ owns the safety-goal target; this policy owns clinical identification and management.""",

f"""5.4 Pressure-ulcer risk identification and management

{HOSPITAL} identifies and manages patients at risk of developing or worsening of pressure ulcers. Screening uses {D('the Braden Scale or equivalent validated tool')} at admission and at defined intervals ({D('daily for at-risk patients')}).

Management includes {D('repositioning schedule, pressure-relieving devices, skin inspection, nutrition optimisation, moisture management, and documentation of skin status')}. New or worsening pressure ulcers are reported and investigated. PSQ owns the safety-goal target; this policy owns clinical identification and management.""",

f"""5.5 Deep vein thrombosis risk identification and management

{HOSPITAL} identifies and manages patients at risk of developing or worsening of deep vein thrombosis. Screening uses {D('the Caprini Score or equivalent validated tool')} at admission and before surgical procedures.

Management includes {D('early mobilisation, mechanical prophylaxis (graduated compression stockings, intermittent pneumatic compression), pharmacological prophylaxis where indicated and not contraindicated, hydration, and patient education')}. VTE events are reported and investigated. PSQ owns the safety-goal target; this policy owns clinical identification and management.""",

f"""5.6 Patients who need restraints

{HOSPITAL} identifies and manages patients who need restraints. Restraints are a last resort used only when less restrictive alternatives have failed or are clinically inappropriate.

Restraints require: {D("a documented doctor's order specifying indication, type, and maximum duration; patient/family informed; time-limited review (at least every 2 hours); neurovascular and skin checks at defined intervals; documented release and reassessment; and discontinuation as soon as the indication resolves")}.

The {D('ward nurse in-charge')} monitors restraint compliance each shift. Prolonged or repeated restraint use is reviewed by the treating team and Quality Coordinator.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that higher-risk patients are identified and managed and that the environment is safe.

Treating doctors
- Order risk-specific interventions, restraint orders, and DVT prophylaxis.

Nurses (ward and ICU)
- Screen patients using adopted tools; initiate management plans; monitor restraints; report incidents.

Physiotherapist / rehabilitation team
- Contribute to fall-prevention and mobility interventions.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when a higher-risk patient safety defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Vulnerability screening completed on admitted patients (sample charts).
- Management plans initiated within the defined timeframe.
- Fall-risk screening and interventions documented.
- Pressure-ulcer screening and repositioning schedules in place.
- DVT-risk screening and prophylaxis documented.
- Restraint use: order, time-limit, checks, and discontinuation documented.
- Environment safety checks for vulnerable patients completed.

Root-cause analysis is required when a higher-risk patient safety event (fall, new pressure ulcer, VTE, restraint injury) recurs within six months.

This policy is reviewed {D('annually')}, and sooner when screening tools or evidence-based guidelines change."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff are trained on this policy at induction and {D('once a year')} after that. Training covers screening tools, management plans, environmental safety, fall prevention, pressure-ulcer prevention, DVT prophylaxis, and safe restraint use.

Staff acknowledgement

I have read this Higher-Risk Patients policy of {HOSPITAL}. I will identify and manage patients at higher risk in accordance with the standards described and will report safety events promptly.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The ward nurse in-charge holds signed acknowledgements with the training file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/12"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.12.
- Morse JM, Morse Fall Scale — validated fall-risk screening tool.
- Braden B and Bergstrom N, Braden Scale for Predicting Pressure Sore Risk — adopted edition.
- Caprini JA, Caprini Risk Assessment Model for VTE — adopted edition.
- Internal documents of {HOSPITAL}: vulnerability screening tool, fall-risk protocol, pressure-ulcer prevention bundle, DVT prophylaxis protocol, restraint policy and order form, incident register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; ICU; emergency department; nursing administration; physiotherapy.

The current version is available to all staff at the {D('ward policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """CAPA — corrective and preventive action
DVT — deep vein thrombosis
ICU — intensive care unit
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter)
SHCO — Standards for Small Healthcare Organisations
VTE — venous thromboembolism"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.12.a",
        "requirement": "The organization identifies and manages vulnerable patients.",
        "steps": "Section 3; 5.1 Identification and management of vulnerable patients; Section 4 items 1–2",
        "responsible": "Admitting nurse (screen); treating team (management plan); ward nurse in-charge (initiation)",
        "records": [
            "Vulnerability screening completed on admission for all patients.",
            "Documented management plan for each identified vulnerable patient.",
            "Audit sample confirming plan initiated within defined timeframe.",
            "Communication of vulnerability status to treating team documented.",
        ],
    },
    {
        "oe_code": "COP.12.b",
        "requirement": "The organization provides for a safe and secure environment for the vulnerable patient.",
        "steps": "Section 3; 5.2 Safe and secure environment for vulnerable patients; Section 4 item 4",
        "responsible": "Ward nurse in-charge (verify); facility manager (correct deficiencies)",
        "records": [
            "Environmental safety checks documented per shift for vulnerable patients.",
            "Deficiency escalation and correction records.",
            "Audit sample showing environment verified on admission.",
        ],
    },
    {
        "oe_code": "COP.12.c",
        "requirement": "The organization identifies and manages patients who are at risk of fall.",
        "steps": "Section 3; 5.3 Fall-risk identification and management; Section 4 item 1",
        "responsible": "Nurses (screen and intervene); treating doctors (medication review); physiotherapist (mobility)",
        "records": [
            "Fall-risk screening using validated tool on admission and at defined intervals.",
            "Documented fall-prevention interventions for at-risk patients.",
            "Fall incident reports with investigation and CAPA.",
            "Patient/family education records on fall prevention.",
        ],
    },
    {
        "oe_code": "COP.12.d",
        "requirement": "The organization identifies and manages patients who are at risk of developing / worsening of pressure ulcers.",
        "steps": "Section 3; 5.4 Pressure-ulcer risk identification and management; Section 4 item 1",
        "responsible": "Nurses (screen and reposition); treating doctors (nutrition, wound care orders)",
        "records": [
            "Pressure-ulcer risk screening using validated tool on admission and daily for at-risk patients.",
            "Repositioning schedule documented and adhered to.",
            "Skin inspection records.",
            "New or worsening pressure-ulcer incident reports with investigation.",
        ],
    },
    {
        "oe_code": "COP.12.e",
        "requirement": "The organization identifies and manages patients who are at risk of developing or worsening of deep vein thrombosis.",
        "steps": "Section 3; 5.5 Deep vein thrombosis risk identification and management; Section 4 item 1",
        "responsible": "Treating doctors (screen and prescribe prophylaxis); nurses (apply mechanical measures)",
        "records": [
            "DVT risk screening using validated tool on admission and pre-surgery.",
            "Documented prophylaxis plan (mechanical and/or pharmacological).",
            "VTE event reports with investigation.",
            "Patient education records on DVT prevention.",
        ],
    },
    {
        "oe_code": "COP.12.f",
        "requirement": "The organization identifies and manages patients who need restraints.",
        "steps": "Section 3; 5.6 Patients who need restraints; Section 4 item 3",
        "responsible": "Treating doctor (order); nurses (apply, monitor, release); ward nurse in-charge (compliance)",
        "records": [
            "Restraint order with indication, type, and maximum duration documented.",
            "Patient/family informed and documentation of discussion.",
            "Neurovascular and skin checks at defined intervals documented.",
            "Discontinuation documented when indication resolved.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.12 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organization identifies and manages patients who are at higher risk of morbidity and mortality." COP.12.a–f PDF index 74. Asterisked OEs: a, f. Levels: c/d/e Core, rest Commitment. PDF has "worsening of developing" in COP.12.e — clean grammar used.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer accreditation-only. COP clinical roles."""


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
        "template_test": "cop_v2_adoptable_shape",
        "subtitle": "Identifying and managing patients at higher risk.",
        "doc_no": D("COP/POL/12"),
    }
    emit_pre_v2(
        draft,
        "cop12_v2_draft.json",
        "COP.12_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
