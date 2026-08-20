# -*- coding: utf-8 -*-
"""HCO AAC.7 v2 — laboratory quality assurance and safety (Full Accreditation 6th Edition).

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer.
Content from NABH HCO 6th Edition PDF (md5 2c4489ee98de4ae9b49cba168ea9f42a),
OCR policies/source/hco6_aac_ocr.txt PDF idxs ~77–79. No SHCO AAC wording.
Stop-work omitted (no genuine unsafe-act stop beyond AAC.6 service rules).
Disclaimer: accreditation-only.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, emit_pre_v2

STANDARD_CODE = "AAC.7"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.7.a", "AAC.7.b", "AAC.7.c", "AAC.7.d",
    "AAC.7.e", "AAC.7.f", "AAC.7.g",
]
POLICY_TITLE = "Laboratory Quality Assurance and Safety Programme"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO AAC.7 v2: lab QA and safety a–g from 6th Edition OCR; accreditation-only P2; no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "There is an established laboratory quality assurance and safety programme — "
    "so that test results are accurate and precise, and laboratory staff work under "
    "documented safety controls aligned with the organisation’s safety programme."
)

PURPOSE = f"""This policy says how {HOSPITAL} implements a laboratory quality assurance programme covering point-of-care testing (POCT), pre-analytic, analytic and post-analytic phases, internal quality control (IQC), external quality assurance (EQA) / proficiency testing (PT), calibration, corrective and preventive action (CAPA), clinico-pathological meetings, and a laboratory safety programme with Material Safety Data Sheets (MSDS), training and appropriate safety measures including personal protective equipment (PPE) and immunisation.

The chapter intent is that laboratory services are quality-assured and safe for staff and patients.

This policy owns laboratory QA and laboratory safety (AAC.7). AAC.6 owns laboratory service scope, specimen journey, TAT, critical results, reporting and outsourcing. Organisation-wide safety and infection-control programmes own hospital-level alignment; this policy aligns the laboratory programme with them.

IQC — internal quality control. EQA — external quality assurance. PT — proficiency testing. POCT — point-of-care testing. MSDS — Material Safety Data Sheet. PPE — personal protective equipment. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the laboratory in-charge, pathologist, microbiologist, biochemist, laboratory technologists, POCT operators outside the central laboratory where laboratory QA covers them, and the Quality Coordinator at {HOSPITAL}.

It covers the seven objective elements AAC.7.a–g: QA programme implementation; IQC; PT/EQA participation; clinico-pathological meetings; laboratory safety programme; training in safe practices; appropriate safety measures.

Boundaries:

- AAC.6 owns service delivery (menu, specimen process, TAT, critical intimation, reporting, outsourcing). Quality failures discovered under this policy feed AAC.6 recall/amendment when a released report is wrong.
- Organisation safety / occupational health documents own hospital-wide safety governance; this laboratory safety programme is aligned with them and does not replace them.
- HIC owns hospital infection-control and biomedical-waste streams; laboratory PPE and standard precautions here are the laboratory application of those duties.
- ISO 15189:2022 and NABL 112 are guidance references for the QA programme, not this policy’s disclaimer statutes.
- Spell out: internal quality control (IQC), external quality assurance (EQA), proficiency testing (PT), point-of-care testing (POCT), Material Safety Data Sheet (MSDS), personal protective equipment (PPE), corrective and preventive action (CAPA)."""

POLICY_STATEMENT = f"""{HOSPITAL} implements a documented laboratory quality assurance programme that covers POCT and the pre-analytic, analytic and post-analytic phases; uses IQC to ensure quality of test results; participates in PT/EQA or documented alternate approaches where formal PT is unavailable; documents CAPA for deviations; conducts clinico-pathological meetings at defined intervals; and implements a laboratory safety programme with MSDS, staff training and appropriate safety measures including PPE, immunisation and standard precautions, aligned with the organisation’s safety programme.

{HOSPITAL} does not release patient results from a measuring system that has failed IQC without documented override and CAPA, and does not leave laboratory staff without required PPE and safety training for the work they perform."""

NON_NEGOTIABLES = f"""1. Do not operate a test method without verification or validation as required by the QA programme.
2. Do not ignore an IQC failure: stop patient reporting for the affected parameter until IQC is restored or a documented clinical override with CAPA is recorded.
3. Do not skip scheduled PT/EQA enrolment for analytes where a formal programme exists and this hospital performs the test.
4. Do not leave laboratory chemicals or hazards without accessible MSDS for the reagents in use.
5. Do not allow laboratory personnel to work without induction training in safe practices and the relevant MSDS for their job.
6. Do not work without required PPE or without documented immunisation status as required for laboratory staff.
7. Staff who see a laboratory QA or safety rule broken report it the same shift to the {D('Laboratory In-Charge')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Laboratory quality assurance programme

The laboratory quality assurance programme is implemented. The organisation has a documented programme to ensure accuracy and precision. The programme includes point-of-care testing (POCT).

Written guidance covers pre-analytic, analytic and post-analytic phases of the testing cycle. The programme includes test standardisation, internal quality control and external quality assurance or inter-laboratory testing as applicable. There is a mechanism to obtain feedback from stakeholders to evaluate laboratory services at least once a year.

The programme addresses verification and/or validation of test methods. It includes periodic calibration and maintenance of equipment. It includes documentation of corrective and preventive actions whenever deviations are observed.

ISO 15189:2022 and NABL 112 are good reference guides for designing and reviewing this programme; they are guidance, not a substitute for this hospital’s documented SOPs.

The laboratory in-charge owns the programme document; the Quality Coordinator reviews it {D('annually')}.""",

f"""5.2 Internal quality control

The programme ensures the quality of test results through internal quality control.

Ensuring quality includes performing IQC to ensure precision and repeatability for all test parameters (quantitative and qualitative) and peer review where relevant. The programme includes comparability of results when more than one measuring system is used.

NABL 112 is a good reference guide. Corrective and preventive actions are taken to address deviations. Patient results for a parameter with failed IQC are not released until IQC is acceptable or a documented override authorised by the {D('Laboratory In-Charge or supervising Pathologist/Biochemist/Microbiologist')} is recorded with CAPA.

IQC schedules and acceptance criteria are defined per analyte in the QA manual. IQC records are retained {D('for the period defined in the laboratory record-retention schedule')}.""",

f"""5.3 Proficiency testing and external quality assurance

The laboratory participates in proficiency testing / external quality assurance schemes. Based on the EQA/PT evaluation report, the laboratory implements and documents corrective actions for outliers.

Where formal EQA/PT is not a practical option — for example non-availability of a formal national PT programme for the analyte; only few laboratories performing the test; unstable analyte (for example blood gases, ammonia, G6PD); or control material of the same matrix not available — the laboratory adopts alternate approaches to validate performance. Alternate approaches may include replicate testing, examination of split samples within the laboratory, use of reference methods and materials where available, and exchange of samples with other accredited laboratories for inter-laboratory comparisons.

NABL 112 is a good reference guide. The laboratory in-charge keeps an enrolment matrix showing which analytes use formal PT and which use alternate approaches.""",

f"""5.4 Clinico-pathological meetings

The programme addresses clinico-pathological meeting(s). The organisation conducts clinico-pathological meetings at pre-defined intervals for correlating histopathology reports with referring clinicians and uses them as a tool for improving quality.

Meetings are scheduled {D('at least quarterly')} unless the Medical Superintendent defines a different interval suited to case volume. Minutes record cases discussed, correlations, discrepancies and actions. Actions feed CAPA under section 5.1 where quality-system change is required.""",

f"""5.5 Laboratory safety programme

The laboratory safety programme is implemented. A laboratory safety manual is available in the laboratory. It addresses safety of the workforce and of equipment, in consonance with identified risks and hazards. The manual incorporates appropriate Material Safety Data Sheets (MSDS).

The safety programme includes safe handling of equipment and accessories including their disinfection. The programme may follow an Occupational Health and Safety Management System approach. It is aligned with the organisation’s safety programme.

The laboratory in-charge reviews the safety manual {D('annually')} and after any significant incident or new hazardous reagent introduction.""",

f"""5.6 Training in safe practices

Laboratory personnel are appropriately trained in safe practices. All laboratory staff undergo training regarding safe practices in the laboratory and in the relevant MSDS. Training-need identification is commensurate with the job description of the staff.

Training is provided at induction and {D('annually')}, and when new hazards or equipment are introduced. Training records are held by the laboratory in-charge.""",

f"""5.7 Appropriate safety measures

Laboratory personnel are provided with appropriate safety measures. Adequate safety measures are available in the laboratory — for example PPE, dressing materials, disinfectants, fire extinguishers — addressing safety issues at all levels.

All laboratory personnel always adhere to standard precautions. All laboratory staff are appropriately immunised ({D('hepatitis B at minimum; other immunisations as per the organisation occupational-health schedule')}).

PPE for routine work includes {D('gloves, laboratory coat, eye protection, and face shield where splash risk exists')}. Spill kits are available and staff are trained in their use.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that laboratory QA and safety programmes are resourced and aligned with organisation safety.

Laboratory In-Charge
- Authors and keeps current the QA programme, IQC/EQA matrix, safety manual, MSDS set, training records and CAPA log.

Pathologist / Microbiologist / Biochemist
- Supervise technical quality in their disciplines; authorise IQC overrides; contribute to clinico-pathological meetings.

Laboratory technologists and POCT operators
- Perform IQC as scheduled; follow safety manual and PPE rules; report deviations the same shift.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA to closure; reviews annual stakeholder feedback on laboratory services."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- QA programme document current; POCT included; method verification/validation records present.
- IQC performance and CAPA for failures; multi-instrument comparability where applicable.
- PT/EQA enrolment and outlier CAPA; alternate-approach records where PT unavailable.
- Clinico-pathological meeting minutes and follow-up actions.
- Laboratory safety manual and MSDS current; alignment with organisation safety.
- Training and immunisation records complete.
- PPE and safety equipment available and used.

Root-cause analysis is required when the same IQC failure mode or safety incident recurs within six months.

This policy is reviewed {D('annually')}, and sooner after a serious laboratory incident or major method change."""

TRAINING_ACKNOWLEDGEMENT = f"""All laboratory staff and POCT operators covered by this programme are trained on this policy at induction and {D('once a year')} after that. Training covers QA phases, IQC, PT/EQA, CAPA, the safety manual, MSDS relevant to their job, PPE and standard precautions.

Staff acknowledgement

I have read this Laboratory Quality Assurance and Safety Programme policy of {HOSPITAL}. I will follow the IQC, EQA, safety and PPE processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('HCO/AAC/POL/07')}
Issue number: {D('01')}
Version: {VERSION} (HCO AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Laboratory In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.7 (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- ISO 15189:2022 — Medical laboratories — Requirements for quality and competence (guidance).
- NABL 112 — Specific criteria for accreditation of medical laboratories (guidance).
- Internal documents of {HOSPITAL}: laboratory QA manual; IQC/EQA records; calibration and maintenance logs; laboratory safety manual and MSDS file; clinico-pathological meeting minutes; organisation safety programme; occupational-health immunisation records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: laboratory; POCT locations covered by this programme; nursing administration for ward-based POCT operators.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
CAPA — corrective and preventive action
EQA — external quality assurance
HCO — Hospital (Full Accreditation programme)
IQC — internal quality control
MSDS — Material Safety Data Sheet
NABL — National Accreditation Board for Testing and Calibration Laboratories
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
POCT — point-of-care testing
PPE — personal protective equipment
PT — proficiency testing
QA — quality assurance"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.7.a",
        "requirement": "The laboratory quality assurance programme is implemented.",
        "steps": "Section 3; 5.1 Laboratory quality assurance programme; Section 4 items 1–2",
        "responsible": "Laboratory In-Charge (own programme); Quality Coordinator (annual review)",
        "records": [
            "Documented QA programme covering POCT and pre-/analytic/post-analytic phases.",
            "Method verification/validation records; calibration and maintenance schedule.",
            "Annual stakeholder feedback on laboratory services; CAPA for deviations.",
        ],
    },
    {
        "oe_code": "AAC.7.b",
        "requirement": "The programme ensures the quality of test results through Internal quality control.",
        "steps": "Section 3; 5.2 Internal quality control; Section 4 item 2",
        "responsible": "Laboratory technologists (perform IQC); Laboratory In-Charge (CAPA); supervising Pathologist/Biochemist/Microbiologist (overrides)",
        "records": [
            "IQC schedules and results for quantitative and qualitative parameters.",
            "Comparability records when more than one measuring system is used.",
            "CAPA and documented overrides for IQC failures.",
        ],
    },
    {
        "oe_code": "AAC.7.c",
        "requirement": "Laboratory participates in proficiency testing / external quality assurance scheme.",
        "steps": "Section 3; 5.3 Proficiency testing and external quality assurance",
        "responsible": "Laboratory In-Charge (enrolment and alternate approaches); Quality Coordinator (audit)",
        "records": [
            "PT/EQA enrolment matrix by analyte.",
            "EQA/PT evaluation reports with corrective actions for outliers.",
            "Documented alternate approaches where formal PT is unavailable.",
        ],
    },
    {
        "oe_code": "AAC.7.d",
        "requirement": "The programme addresses the clinico-pathological meeting(s).",
        "steps": "Section 3; 5.4 Clinico-pathological meetings",
        "responsible": "Pathologist (convene); referring clinicians (participate); Laboratory In-Charge (minutes)",
        "records": [
            "Meeting schedule at pre-defined intervals.",
            "Minutes with cases, correlations and discrepancies.",
            "Follow-up actions linked to quality improvement or CAPA.",
        ],
    },
    {
        "oe_code": "AAC.7.e",
        "requirement": "The laboratory safety programme is implemented.",
        "steps": "Section 3; 5.5 Laboratory safety programme; Section 4 item 4",
        "responsible": "Laboratory In-Charge (safety manual); Medical Superintendent (alignment with organisation safety)",
        "records": [
            "Laboratory safety manual available in the laboratory.",
            "MSDS set for reagents in use.",
            "Annual review record and alignment note with organisation safety programme.",
        ],
    },
    {
        "oe_code": "AAC.7.f",
        "requirement": "Laboratory personnel are appropriately trained in safe practices.",
        "steps": "Section 3; 5.6 Training in safe practices; Section 4 item 5",
        "responsible": "Laboratory In-Charge (training); staff (attend)",
        "records": [
            "Training-need identification by job description.",
            "Induction and annual safe-practice training records.",
            "MSDS training records for reagents handled by each role.",
        ],
    },
    {
        "oe_code": "AAC.7.g",
        "requirement": "Laboratory personnel are provided with appropriate safety measures.",
        "steps": "Section 3; 5.7 Appropriate safety measures; Section 4 item 6",
        "responsible": "Laboratory In-Charge (provide measures); staff (use PPE and standard precautions)",
        "records": [
            "PPE and safety-equipment inventory (including spill kit and extinguishers).",
            "Immunisation records for laboratory staff.",
            "Observation or audit notes on adherence to standard precautions.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.7 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Asterisked: a,b,e. Seven OEs, seven What-we-do subsections. Stop-work omitted. P2 accreditation-only. ISO 15189/NABL 112 as guidance only."""


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
        "stop_work": "",
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Laboratory quality assurance, IQC/EQA and safety.",
        "doc_no": D("HCO/AAC/POL/07"),
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.7",
    }
    emit_pre_v2(
        draft,
        "hco_aac7_v2_draft.json",
        "HCO.AAC.7_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
