# -*- coding: utf-8 -*-
"""HIC.5 v2 — infection surveillance.

Shape follows PRE.2 v2. Wording from NABH SHCO 3rd Edition PDF
(md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 101.
Chapter intent: PDF index 98.

No stop-work section. Six OEs mapped to six What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "HIC.5"
CHAPTER = "HIC"
OE_CODES = ["HIC.5.a", "HIC.5.b", "HIC.5.c", "HIC.5.d", "HIC.5.e", "HIC.5.f"]
POLICY_TITLE = "Infection Prevention and Control Surveillance"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "HIC v2 template: adoptable shape, plain English, HIC roles, six steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "The organisation performs surveillance to capture and monitor infection prevention "
    "and control data — tracking risks, rates and trends; hand-hygiene compliance; "
    "multi-drug-resistant organisms; outbreak identification; housekeeping effectiveness; "
    "and corrective/preventive action from analysed data."
)

PURPOSE = f"""This policy describes how {HOSPITAL} performs surveillance to capture and monitor infection prevention and control data: tracking and analysing infection risks, rates and trends; monitoring hand-hygiene compliance; capturing multi-drug-resistant organisms (MDRO) and highly virulent infections; identifying and controlling outbreaks; monitoring housekeeping effectiveness; and analysing data for corrective and preventive action with feedback to the healthcare team.

Surveillance data feeds the PSQ quality indicator framework (PSQ.2 owns the indicator framework); this policy owns the surveillance methodology and data generation.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the Infection Control Team, the Infection Control Committee, the Quality Coordinator and all clinical and support staff who generate or use infection surveillance data at {HOSPITAL}.

It covers the six elements HIC.5.a–f name: infection risk/rate/trend tracking, hand-hygiene compliance monitoring, MDRO and virulent infection capture, outbreak identification and control, housekeeping surveillance, and data analysis with CAPA and feedback.

Boundaries with other policies of {HOSPITAL}:

- HIC.1 owns programme governance; this policy owns the surveillance component of that programme.
- HIC.2 owns clinical practices; HIC.5.b monitors hand-hygiene compliance for HIC.2.b.
- HIC.3 owns support-service procedures; HIC.5.e monitors housekeeping effectiveness for HIC.3.c.
- HIC.4 owns device-bundle prevention; surveillance rates feed those bundles.
- PSQ.2 owns the quality indicator framework; surveillance data is reported into that framework."""

POLICY_STATEMENT = f"""{HOSPITAL} maintains an active infection surveillance programme that tracks infection risks, rates and trends, monitors hand-hygiene compliance, captures MDRO and highly virulent infections, identifies and controls outbreaks, monitors housekeeping effectiveness, and analyses data to drive corrective and preventive actions with regular feedback to the healthcare team."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Operating without active infection surveillance (passive reporting alone is insufficient).
2. Failing to report a suspected MDRO or highly virulent infection to the Infection Control Officer within {D('24 hours')} of laboratory confirmation or clinical suspicion.
3. Ignoring an outbreak signal (unusual cluster of similar infections in time/place) without investigation.
4. Withholding surveillance data or feedback from the clinical team responsible for the area.
5. Counting housekeeping visual inspection alone as effectiveness monitoring (microbiological or ATP sampling required at defined frequency).
6. Closing a CAPA arising from surveillance data without evidence of effectiveness."""

PROCEDURE_STEPS = [
f"""5.1 Tracking and analysing infection risks, rates and trends

The Infection Control Team maintains surveillance that incorporates tracking and analysing of infection risks, rates and trends at {HOSPITAL}:

- Numerator data: laboratory-confirmed infections, clinically diagnosed infections (using standard case definitions).
- Denominator data: patient-days, device-days (catheter-days, ventilator-days, line-days where applicable).
- Rates calculated: CAUTI, CLABSI, SSI, VAP (where applicable), and overall HAI rate per 1000 patient-days.
- Trends analysed {D('monthly')} and presented to the ICC {D('quarterly')}.
- Risk stratification: high-risk areas (OT, ICU, labour room) receive targeted surveillance.

Data sources include microbiology laboratory reports, clinical records, nursing documentation and discharge summaries.""",

f"""5.2 Monitoring hand-hygiene compliance

Surveillance includes monitoring compliance with hand-hygiene guidelines (HIC.2.b):

- Direct observation audits using the WHO hand-hygiene observation tool (or equivalent) conducted {D('monthly')} in each clinical unit.
- Observers are trained and validated using the WHO training module.
- Compliance rate = (hand-hygiene actions performed / opportunities observed) × 100.
- Results reported by unit, professional category and moment.
- Feedback shared with unit leads {D('within one week')} of the audit.
- Trend analysis and benchmarking against the hospital target of {D('≥ 80 %')}.

Product consumption (ABHR litres per 1000 patient-days) is tracked as a surrogate indicator alongside direct observation.""",

f"""5.3 Multi-drug-resistant organisms and highly virulent infections

Surveillance includes mechanisms to capture the occurrence of multi-drug-resistant organisms (MDRO) and highly virulent infections:

- The microbiology laboratory flags MDRO results (MRSA, VRE, ESBL, CRE, multi-drug-resistant Acinetobacter, and others per the ICC's MDRO list) and communicates them to the Infection Control Officer {D('on the same day')}.
- Alert organisms and notifiable diseases are reported to public health authorities as required.
- A line-list of MDRO cases is maintained with patient demographics, organism, resistance pattern, location, and date.
- Highly virulent infections (novel influenza, viral haemorrhagic fever, suspected outbreak pathogen) trigger immediate notification to the Infection Control Officer and activation of transmission-based precautions.
- Antibiogram data is compiled {D('annually')} and shared with prescribers to inform antimicrobial policy (HIC.2.e).""",

f"""5.4 Outbreak identification and control

The organisation identifies and takes appropriate action to control outbreaks of infections:

- An outbreak is suspected when the number of infections of a similar type in a defined area/time exceeds the baseline (or ≥ 2 cases of an unusual organism in a unit within {D('7 days')}).
- The Infection Control Officer investigates: confirm cases, identify the source, implement control measures (cohorting, enhanced cleaning, contact tracing), and communicate to the ICC and administration.
- An outbreak log documents timeline, case count, source hypothesis, control measures taken and outcome.
- The outbreak is declared over when no new cases occur for two incubation periods.
- A post-outbreak report with lessons learned and preventive recommendations is submitted to the ICC within {D('2 weeks')} of closure.
- {HOSPITAL} participates in community outbreak investigation when requested by district health authorities (HIC.1.d).""",

f"""5.5 Housekeeping effectiveness monitoring

Surveillance activities include monitoring the effectiveness of the housekeeping services (HIC.3.c):

- Visual inspection audits of cleanliness are conducted {D('daily')} by the Housekeeping In-Charge and {D('weekly')} by the Infection Control Nurse.
- Objective monitoring: {D('ATP bioluminescence testing or microbiological swab cultures')} on high-touch surfaces {D('monthly')} in high-risk areas and {D('quarterly')} in general areas.
- Results are compared against defined benchmarks ({D('< 250 RLU for ATP; < 5 CFU/cm² for aerobic colony count')}).
- Non-conformances trigger re-cleaning, RCA (if repeated) and CAPA.
- Housekeeping effectiveness trends are reported to the ICC {D('quarterly')}.""",

f"""5.6 Data analysis, CAPA and feedback

Surveillance data is analysed, and appropriate corrective and preventive actions are taken and feedback regarding the same is provided regularly to the appropriate health care team:

- The Infection Control Team compiles and analyses surveillance data {D('monthly')}.
- Analysis includes trend comparison, benchmarking, identification of clusters or rising rates.
- When rates exceed thresholds or trends worsen, RCA is initiated and CAPA is defined with timelines and responsibility.
- Feedback is provided to unit heads and the healthcare team {D('monthly')} (unit-specific dashboards or reports).
- A consolidated surveillance report is presented to the ICC {D('quarterly')} and to the Medical Superintendent.
- Data feeds the hospital quality indicators under PSQ.2.
- CAPA effectiveness is verified by monitoring the metric in subsequent periods; closure requires evidence that the rate returned to acceptable levels.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for surveillance resources and for acting on outbreak notifications.

Infection Control Officer
- Leads surveillance methodology, outbreak investigation, MDRO tracking, and data analysis.

Infection Control Nurse
- Conducts hand-hygiene audits, housekeeping monitoring, and maintains surveillance databases.

Infection Control Committee
- Reviews surveillance reports, approves thresholds, monitors CAPA closure.

Microbiology laboratory
- Flags MDRO results and communicates to the Infection Control Officer on the same day.

Treating doctors and nurses
- Report suspected infections; comply with outbreak control measures.

Quality Coordinator
- Audits this policy {D('quarterly')}; ensures surveillance data feeds PSQ indicators; tracks CAPA."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

- Surveillance data completeness and timeliness (rates calculated monthly, trends presented quarterly).
- Hand-hygiene audit completion and feedback timeliness.
- MDRO line-list currency and laboratory notification compliance.
- Outbreak log entries and post-outbreak report completion.
- Housekeeping objective monitoring records and benchmark comparisons.
- CAPA register linked to surveillance findings and evidence of effectiveness.

Root-cause analysis is required when surveillance data is incomplete for more than one month, or when an outbreak investigation is not initiated within {D('48 hours')} of the signal.

This policy is reviewed {D('annually')}, and sooner when a new surveillance methodology is adopted or after a major outbreak."""

TRAINING_ACKNOWLEDGEMENT = f"""The Infection Control Team and all unit leads are trained on this policy at induction and {D('once a year')} after that. Training covers surveillance definitions, data collection methods, hand-hygiene audit technique, outbreak recognition, and the feedback loop.

Staff acknowledgement

I have read this Infection Prevention and Control Surveillance policy of {HOSPITAL}. I understand my role in reporting infections and using surveillance feedback to improve practice.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Infection Control Officer holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="HIC/POL/05",
    version=VERSION,
    prepared_by=D("Infection Control Officer"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — HIC chapter, standard HIC.5.
- CDC/NHSN Surveillance Definitions for Specific Types of Infections (current edition).
- WHO Guidelines on Core Components of Infection Prevention and Control Programmes (2016) — surveillance component.
- ICMR Antimicrobial Resistance Surveillance Network reports.
- Internal documents of {HOSPITAL}: surveillance protocol, hand-hygiene audit tool, MDRO line-list, outbreak SOP, housekeeping monitoring protocol, ICC reporting template."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Infection Control Officer and the Quality Coordinator.

Copies issued to: microbiology laboratory, all clinical unit leads, housekeeping, nursing administration.

The current version is available to all staff at the {D('infection control manual / staff intranet')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """ABHR — alcohol-based hand rub
ATP — adenosine triphosphate
CAPA — corrective and preventive action
CAUTI — catheter-associated urinary tract infection
CFU — colony-forming units
CLABSI — central-line-associated blood stream infection
CRE — carbapenem-resistant Enterobacterales
ESBL — extended-spectrum beta-lactamase
HAI — healthcare-associated infection
HIC — Hospital Infection Prevention and Control (NABH SHCO chapter)
ICC — Infection Control Committee
ICMR — Indian Council of Medical Research
MDRO — multi-drug-resistant organism
MRSA — methicillin-resistant Staphylococcus aureus
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality (NABH SHCO chapter)
RCA — root-cause analysis
RLU — relative light units
SHCO — Standards for Small Healthcare Organisations
SSI — surgical site infection
VAP — ventilator-associated pneumonia
VRE — vancomycin-resistant Enterococcus
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "HIC.5.a",
        "requirement": "The scope of surveillance incorporates tracking and analysing of infection risks, rates and trends.",
        "steps": "Section 3; 5.1 Tracking and analysing infection risks, rates and trends",
        "responsible": "Infection Control Team (collect and calculate); ICC (review trends)",
        "records": [
            "Monthly infection rate calculations (numerator/denominator) by type and area.",
            "Trend charts presented to the ICC quarterly.",
            "Surveillance database or register with case definitions applied.",
            "Risk stratification showing targeted surveillance in high-risk areas.",
        ],
    },
    {
        "oe_code": "HIC.5.b",
        "requirement": "Surveillance includes monitoring compliance with hand-hygiene guidelines.",
        "steps": "Section 3; 5.2 Monitoring hand-hygiene compliance",
        "responsible": "Infection Control Nurse (audit); unit leads (receive feedback and act)",
        "records": [
            "Completed hand-hygiene observation audit forms (WHO tool or equivalent).",
            "Monthly compliance rates by unit and professional category.",
            "Feedback records shared with unit leads within one week.",
            "ABHR consumption data (litres per 1000 patient-days) tracked as surrogate indicator.",
        ],
    },
    {
        "oe_code": "HIC.5.c",
        "requirement": "Surveillance includes mechanisms to capture the occurrence of multi-drug-resistant organisms and highly virulent infections.",
        "steps": "Section 3; 5.3 Multi-drug-resistant organisms and highly virulent infections; Section 4 item 2",
        "responsible": "Microbiology laboratory (flag and notify); Infection Control Officer (line-list and action)",
        "records": [
            "MDRO line-list with patient demographics, organism, resistance pattern, location and date.",
            "Laboratory same-day notification records to the Infection Control Officer.",
            "Annual antibiogram compiled and shared with prescribers.",
            "Notification records to public health authorities for notifiable diseases.",
        ],
    },
    {
        "oe_code": "HIC.5.d",
        "requirement": "The organisation identifies and takes appropriate action to control outbreaks of infections.",
        "steps": "Section 3; 5.4 Outbreak identification and control; Section 4 item 3",
        "responsible": "Infection Control Officer (investigate and control); ICC (oversight); Medical Superintendent (resource allocation)",
        "records": [
            "Outbreak log with timeline, case count, source hypothesis, control measures and outcome.",
            "Post-outbreak report with lessons learned submitted to ICC.",
            "Communication records to administration and (where applicable) district health authority.",
            "Evidence of control measures implemented (cohorting, enhanced cleaning, contact tracing).",
        ],
    },
    {
        "oe_code": "HIC.5.e",
        "requirement": "Surveillance activities include monitoring the effectiveness of the housekeeping services.",
        "steps": "Section 3; 5.5 Housekeeping effectiveness monitoring; Section 4 item 5",
        "responsible": "Infection Control Nurse (objective monitoring); Housekeeping In-Charge (daily visual); ICC (review trends)",
        "records": [
            "Visual inspection audit records (daily/weekly).",
            "Objective monitoring results (ATP or microbiological) with benchmark comparison.",
            "Non-conformance and re-cleaning records.",
            "Quarterly housekeeping effectiveness trend report to ICC.",
        ],
    },
    {
        "oe_code": "HIC.5.f",
        "requirement": "Surveillance data is analysed, and appropriate corrective and preventive actions are taken and feedback regarding the same is provided regularly to the appropriate health care team.",
        "steps": "Section 3; 5.6 Data analysis, CAPA and feedback; Section 4 item 6",
        "responsible": "Infection Control Team (analyse); Quality Coordinator (CAPA tracking); unit leads (receive feedback and implement actions)",
        "records": [
            "Monthly surveillance analysis reports.",
            "CAPA register linked to surveillance findings with timelines and responsibility.",
            "Unit-level feedback records (dashboards or reports shared monthly).",
            "Consolidated quarterly surveillance report presented to ICC and Medical Superintendent.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HIC.5 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "The organisation performs surveillance to capture and monitor infection prevention and control data." HIC.5.a–f PDF index 101. One asterisked OE: HIC.5.d (Commitment). No stop-work.

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
        "subtitle": "Surveillance of infection risks, rates, trends and outcomes.",
        "doc_no": "HIC/POL/05",
    }
    emit_pre_v2(
        draft,
        "hic5_v2_draft.json",
        "HIC.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
