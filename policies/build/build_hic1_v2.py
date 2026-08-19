# -*- coding: utf-8 -*-
"""HIC.1 v2 — hospital infection prevention and control programme.

Shape follows PRE.2 v2 (section list and order only). Wording is built from HIC.1
OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 99.
Chapter intent: PDF index 98.

No stop-work section. Six OEs mapped to six What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HIC.1"
CHAPTER = "HIC"
OE_CODES = ["HIC.1.a", "HIC.1.b", "HIC.1.c", "HIC.1.d", "HIC.1.e", "HIC.1.f"]
POLICY_TITLE = "Hospital Infection Prevention and Control Programme"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HIC v2 template: adoptable shape, plain English, HIC roles, six steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation has a comprehensive and coordinated Hospital Infection Prevention "
    "and Control (HIC) programme aimed at reducing/eliminating risks to patients, visitors, "
    "providers of care and community."
)

PURPOSE = f"""This policy establishes the hospital infection prevention and control (HIC) programme at {HOSPITAL}, aimed at reducing and eliminating the risk of healthcare-associated infection (HAI) to patients, visitors, providers of care and the community.

It covers the programme document, its review using an infection control assessment tool, the multidisciplinary infection control committee and team, information-education-communication (IEC) for the community and pandemic preparedness, resources for infection control, and isolation/barrier nursing facilities.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical and support service areas of {HOSPITAL} and to every staff member, visitor and contractor whose activities affect infection risk.

It covers the six elements HIC.1.a–f name: programme documentation, assessment-tool-based review, committee/team coordination, community IEC and pandemic participation, resource provision, and isolation/barrier nursing.

Boundaries with other policies of {HOSPITAL}:

- HIC.2 owns clinical infection prevention practices (hand hygiene, standard precautions, antimicrobial stewardship).
- HIC.3 owns infection control in support services (engineering controls, housekeeping, bio-medical waste, laundry, kitchen).
- HIC.4 owns actions to prevent specific HAI in patients and occupational health/safety for staff.
- HIC.5 owns surveillance of infection data.
- HIC.6 owns sterilisation and disinfection of instruments and devices.
- FMS owns the built environment and engineering infrastructure; this policy owns infection-prevention programme design."""

POLICY_STATEMENT = f"""{HOSPITAL} maintains a documented infection prevention and control programme that aims at preventing and reducing the risk of HAI across all services.

The programme is reviewed periodically using an infection control assessment tool. A multidisciplinary infection control committee and an infection control team coordinate all infection prevention and control activities.

{HOSPITAL} participates in managing community outbreaks and pandemics through IEC activities. Management provides the resources required for the programme, and isolation/barrier nursing facilities are available."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating without a documented infection prevention and control programme.
2. Failing to review the programme against an infection control assessment tool at the frequency defined.
3. Running infection control activities without a multidisciplinary committee and a designated team.
4. Withholding resources that the infection control committee has identified as required for the programme.
5. Admitting patients requiring isolation when no isolation/barrier nursing facility is available and no alternative arrangement has been documented.
6. Ignoring a community outbreak or pandemic notification when {HOSPITAL} has been requested to participate."""

PROCEDURE_STEPS = [
f"""5.1 Documented infection prevention and control programme

The Infection Control Officer and the Infection Control Committee maintain a documented HIC programme that aims at preventing and reducing the risk of HAI in {HOSPITAL}. The programme covers all clinical and support service areas.

The programme document includes: objectives, scope, surveillance plan, antimicrobial stewardship references, BMW management references, disinfection and sterilisation references, outbreak response, training schedule and resource requirements.

The programme is approved by the {D('Medical Superintendent')} and is available to all staff at {D('the infection control manual / staff intranet')}.""",

f"""5.2 Programme review using infection control assessment tool

The Infection Control Committee reviews the programme {D('annually')} using an infection control assessment tool (such as the NABH infection control assessment checklist or an equivalent validated tool).

Findings from the review are documented, gaps are identified, and a corrective action plan with timelines and responsibility is prepared. The {D('Quality Coordinator')} tracks closure of gaps.""",

f"""5.3 Multidisciplinary infection control committee and team

{HOSPITAL} has a multidisciplinary Infection Control Committee (ICC) that includes representatives from medical, nursing, administration, housekeeping, CSSD, kitchen, laundry and laboratory services. The committee meets {D('quarterly')} or more often when required.

An Infection Control Team (ICT) comprising the Infection Control Officer (a doctor) and the Infection Control Nurse coordinates day-to-day implementation of all infection prevention and control activities. The ICT reports to the ICC.

Minutes of ICC meetings, attendance, decisions and action items are documented.""",

f"""5.4 Information, education and communication for community and pandemic preparedness

{HOSPITAL} implements an IEC programme for infection prevention and control directed at the community — including patients, visitors and caregivers — covering hand hygiene, respiratory etiquette, immunisation awareness and seasonal infection alerts.

{HOSPITAL} participates in managing community outbreaks and pandemics as requested by local/district health authorities. The response plan is documented and reviewed {D('annually')} or after every activation.""",

f"""5.5 Resources for infection control

The management of {HOSPITAL} makes available the resources required for the infection control programme. Resources include: trained manpower (Infection Control Officer, Infection Control Nurse), personal protective equipment (PPE), hand-hygiene consumables, disinfectants, sterilisation equipment, isolation facilities, signage, and budget allocation for surveillance and training.

The Infection Control Committee submits a resource requirement plan {D('annually')} to the {D('Medical Superintendent')}. Shortfalls are escalated formally.""",

f"""5.6 Isolation and barrier nursing facilities

{HOSPITAL} provides isolation/barrier nursing facilities for patients with communicable or highly transmissible infections. Facilities include {D('a single room with dedicated toilet, negative-pressure ventilation where feasible, and PPE supplies at the entry')}.

Where a dedicated isolation room is not available, barrier nursing precautions are applied at the bedside with documented protocols. Criteria for isolation, de-isolation and transfer are defined. Staff assigned to isolation areas are trained in transmission-based precautions (HIC.2.c).""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for the HIC programme, resource allocation and committee constitution.

Infection Control Officer (doctor)
- Leads the Infection Control Team; coordinates day-to-day programme implementation.

Infection Control Nurse
- Supports the Infection Control Officer in surveillance, training, audits and outbreak response.

Infection Control Committee (multidisciplinary)
- Reviews the programme, approves the annual plan, monitors outcomes and escalates resource gaps.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section); tracks CAPA closure.

All staff
- Comply with the infection control programme and report breaches."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

- Programme document currency and completeness.
- Assessment-tool review completion within defined frequency.
- ICC meeting minutes, quorum and action-item closure.
- IEC activities conducted and community outbreak participation records.
- Resource availability against the annual plan.
- Isolation/barrier nursing facility readiness and utilisation.

Root-cause analysis is required when a programme gap identified by the assessment tool remains open beyond {D('90 days')}.

This policy is reviewed {D('annually')}, and sooner when the assessment-tool review or an outbreak triggers revision."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff are trained on this policy at induction and {D('once a year')} after that. Training covers the HIC programme scope, committee structure, reporting lines, IEC expectations and isolation procedures.

Staff acknowledgement

I have read this Hospital Infection Prevention and Control Programme policy of {HOSPITAL}. I understand the programme, my role in it, and how to report infection control concerns.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Infection Control Officer holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="HIC/POL/01",
    version=VERSION,
    prepared_by=D("Infection Control Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Healthcare Associated Infection chapter, standard HIC.1.
- Guidelines on Infection Prevention and Control, National Centre for Disease Control, India.
- WHO Guidelines on Core Components of Infection Prevention and Control Programmes at the Facility Level (2016).
- Internal documents of {HOSPITAL}: HIC programme manual, ICC terms of reference, IEC plan, isolation protocols."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Infection Control Officer and the Quality Coordinator.

Copies issued to: all clinical areas, CSSD, housekeeping, kitchen, laundry, laboratory, nursing administration.

The current version is available to all staff at the {D('infection control manual / staff intranet')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """BMW — bio-medical waste
CAPA — corrective and preventive action
CSSD — central sterile services department
HAI — healthcare-associated infection
HIC — Hospital Infection Prevention and Control (NABH SHCO chapter)
ICC — Infection Control Committee
ICT — Infection Control Team
IEC — information, education and communication
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PPE — personal protective equipment
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HIC.1.a",
        "requirement": "The hospital infection prevention and control programme is documented, which aims at preventing and reducing the risk of healthcare associated infections in the hospital.",
        "steps": "Section 3; 5.1 Documented infection prevention and control programme",
        "responsible": "Infection Control Officer (document and maintain); Medical Superintendent (approve)",
        "records": [
            "Documented HIC programme with objectives, scope, surveillance plan, antimicrobial stewardship references, BMW references, disinfection/sterilisation references, outbreak response and training schedule.",
            "Approval record signed by the Medical Superintendent.",
            "Annual review and update records.",
            "Distribution register showing availability to all areas.",
        ],
    },
    {
        "oe_code": "HIC.1.b",
        "requirement": "The infection prevention and control programme is reviewed based on infection control assessment tool.",
        "steps": "Section 3; 5.2 Programme review using infection control assessment tool",
        "responsible": "Infection Control Committee (conduct review); Quality Coordinator (track gaps)",
        "records": [
            "Completed infection control assessment tool with scores and findings.",
            "Gap analysis and corrective action plan with timelines and responsibility.",
            "Evidence of gap closure tracked by the Quality Coordinator.",
            "Minutes showing review findings presented to the ICC.",
        ],
    },
    {
        "oe_code": "HIC.1.c",
        "requirement": "The organisation has a multidisciplinary infection control committee and an infection control team, which coordinate the implementation of all infection prevention and control activities.",
        "steps": "Section 3; 5.3 Multidisciplinary infection control committee and team",
        "responsible": "Infection Control Committee (oversight); Infection Control Officer and Nurse (day-to-day coordination)",
        "records": [
            "Committee constitution order naming members from medical, nursing, administration, housekeeping, CSSD, kitchen, laundry and laboratory.",
            "ICC meeting minutes with attendance, quorum, decisions and action items.",
            "ICT activity log showing day-to-day coordination.",
            "Annual report from the ICC summarising activities and outcomes.",
        ],
    },
    {
        "oe_code": "HIC.1.d",
        "requirement": "The organisation implements information, education and communication programme for infection prevention and control activities for the community and participates in managing community outbreaks and pandemics.",
        "steps": "Section 3; 5.4 Information, education and communication for community and pandemic preparedness",
        "responsible": "Infection Control Officer (plan and implement IEC); Medical Superintendent (liaison with district health authority)",
        "records": [
            "Annual IEC plan with topics, target audience, frequency and responsibility.",
            "Records of IEC sessions conducted — attendance, materials used, photographs where applicable.",
            "Community outbreak/pandemic participation records with correspondence from health authorities.",
            "Post-activation review and lessons-learnt document.",
        ],
    },
    {
        "oe_code": "HIC.1.e",
        "requirement": "The management makes available resources required for the infection control programme.",
        "steps": "Section 3; 5.5 Resources for infection control",
        "responsible": "Medical Superintendent (allocate); Infection Control Committee (plan and escalate shortfalls)",
        "records": [
            "Annual resource requirement plan submitted by the ICC.",
            "Budget allocation records showing management approval.",
            "Stock and consumption records for PPE, hand-hygiene consumables, disinfectants.",
            "Escalation correspondence when shortfalls are identified.",
        ],
    },
    {
        "oe_code": "HIC.1.f",
        "requirement": "Isolation/barrier nursing facilities are available.",
        "steps": "Section 3; 5.6 Isolation and barrier nursing facilities",
        "responsible": "Infection Control Officer (criteria and protocols); Nursing In-Charge (readiness); Medical Superintendent (facility provision)",
        "records": [
            "Isolation/barrier nursing facility inventory and readiness checklist.",
            "Written criteria for isolation, de-isolation and transfer.",
            "Barrier nursing protocol for use when a dedicated room is unavailable.",
            "Training records of staff assigned to isolation duties.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HIC.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation has a comprehensive and coordinated Hospital Infection Prevention and Control (HIC) programme aimed at reducing/eliminating risks to patients, visitors, providers of care and community." HIC.1.a–f PDF index 99. Two asterisked OEs: HIC.1.a (Commitment), HIC.1.b (Achievement). No stop-work.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer accreditation-only. HIC roles."""


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
        "subtitle": "Infection prevention and control programme governance.",
        "doc_no": "HIC/POL/01",
    }
    emit_pre_v2(
        draft,
        "hic1_v2_draft.json",
        "HIC.1_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
