# -*- coding: utf-8 -*-
"""MOM.7 v2 — patients are monitored after medication administration.

PDF indices 85–86. No stop-work. Five OEs, five What-we-do subsections.
Disclaimer accreditation-only.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer_accreditation_only

STANDARD_CODE = "MOM.7"
CHAPTER = "MOM"
OE_CODES = ["MOM.7.a", "MOM.7.b", "MOM.7.c", "MOM.7.d", "MOM.7.e"]
POLICY_TITLE = "Patients Are Monitored After Medication Administration"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, five steps, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Patients are monitored after medication administration, medications are changed where "
    "appropriate, and near-misses, medication errors and adverse drug reactions are captured, "
    "reported, analysed and acted upon."
)

PURPOSE = f"""This policy describes how {HOSPITAL} monitors patients after medication administration, changes medications based on monitoring, captures near-misses, medication errors and adverse drug reactions, reports and analyses them within a specified time frame, and takes corrective and preventive action.

It covers MOM.7.a–e.

Boundary: medication events captured here feed into the PSQ.5 general incident reporting system. This policy owns the medication-specific capture and analysis; PSQ.5 owns the organisation-wide incident system.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to nurses, treating doctors, the Pharmacy In-Charge, the Multidisciplinary Medication Committee, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.7.a–e: post-administration monitoring; medication changes; capture of near-misses, medication errors and adverse drug reactions; reporting and analysis; and corrective and preventive action.

Boundaries with other policies of {HOSPITAL}:

- MOM.6 owns administration. This policy begins after the medication has been administered.
- PSQ.5 owns the general incident reporting and analysis system. Medication events (near-misses, errors, ADRs) captured here are also entered into the PSQ.5 system. This policy owns the medication-specific detail; PSQ.5 owns the aggregate incident picture.
- MOM.3.f–g owns prescription audit. Findings from this policy's analysis may trigger prescription-audit action under MOM.3."""

POLICY_STATEMENT = f"""{HOSPITAL} monitors every patient after medication administration for the expected therapeutic effect and for adverse reactions.

{HOSPITAL} captures near-misses, medication errors and adverse drug reactions, reports and analyses them within a defined time frame, and takes corrective and preventive action. Medication events also feed into PSQ.5."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Patients receiving high-risk medications, IV medications, or first doses of a new medication are monitored within {D('30 minutes')} of administration.
2. An adverse drug reaction is documented and reported to the {D('Pharmacy In-Charge')} and the treating doctor within {D('one hour')} of identification.
3. A medication error is documented and reported within {D('one hour')} of discovery, regardless of whether the patient was harmed.
4. Near-misses (caught before reaching the patient) are documented and reported within {D('24 hours')}.
5. Analysis of medication errors and ADRs is completed within {D('seven days')} of the report.
6. No staff member is punished for reporting a near-miss or medication error in good faith. A blame culture destroys the reporting system.

Staff who witness a medication event report it to the {D('ward in-charge nurse')} or {D('Pharmacy In-Charge')} without delay."""

PROCEDURE_STEPS = [
f"""5.1 Post-administration monitoring

Patients are monitored after medication administration.

The administering nurse observes the patient for the expected therapeutic effect and for adverse reactions. Monitoring intensity depends on risk: high-risk medications, IV medications and first doses of a new medication are monitored within {D('30 minutes')}. Routine oral medications are monitored at the next scheduled round.

Observations are documented in the {D('medication administration record (MAR) or nursing notes')}. Abnormal observations trigger immediate notification of the treating doctor.""",

f"""5.2 Medication changes based on monitoring

Medications are changed where appropriate based on the monitoring.

When monitoring reveals an adverse effect, inadequate response or a change in patient condition, the treating doctor reviews the medication order and makes changes as clinically appropriate. Changes are documented as a new order (MOM.4) and communicated to the nurse and pharmacist.

The reason for the change is documented in the clinical notes.""",

f"""5.3 Capture of near-misses, medication errors and adverse drug reactions

{HOSPITAL} captures near-miss, medication error and adverse drug reaction events.

A near-miss is a medication event caught before reaching the patient (wrong drug selected but intercepted at verification). A medication error is an event that reached the patient (wrong dose administered). An adverse drug reaction (ADR) is an unwanted or harmful reaction to a medication at normal doses.

Every event is documented on the {D('medication incident form')} which includes: patient name and ID, date and time, medication involved, description of event, severity assessment, and immediate action taken. The form is submitted to the {D('Pharmacy In-Charge')} and a copy entered into the PSQ.5 incident system.""",

f"""5.4 Reporting and analysis within a specified time frame

Near-miss, medication error and adverse drug reaction are reported and analysed within a specified time frame.

Reporting time frames: ADR within {D('one hour')}; medication error within {D('one hour')}; near-miss within {D('24 hours')}. Analysis is completed within {D('seven days')} by the Pharmacy In-Charge (or a pharmacist delegate) with the Quality Coordinator.

Analysis uses {D('root-cause analysis for serious events and trend analysis for aggregate data')}. Findings are presented to the Multidisciplinary Medication Committee {D('quarterly')} and to PSQ.5 as applicable.

Pharmacovigilance reporting to the {D('ADR Monitoring Centre (AMC) under the Pharmacovigilance Programme of India')} is completed for serious or unexpected ADRs within the regulatory time frame.""",

f"""5.5 Corrective and preventive action

Corrective and preventive action is taken based on the analysis.

The Multidisciplinary Medication Committee reviews analysis findings and decides CAPA: system redesign, process change, education, formulary restriction, or individual feedback.

Actions are tracked to closure by the Quality Coordinator. Root-cause analysis is required when the same event type recurs within six months. Aggregate trends (medication-error rate, ADR rate) are reported to the committee {D('quarterly')} and used to set improvement targets.""",
]

STOP_WORK = ""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable for a functioning medication-event reporting and analysis system.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Reviews medication-event analysis and decides CAPA; sets improvement targets.

Pharmacy In-Charge
- Receives medication incident forms; leads or participates in analysis; submits pharmacovigilance reports.

Treating doctors (prescribers)
- Change medications based on monitoring; report ADRs.

Nurses
- Monitor patients after administration; document observations; capture and report events.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA to closure; maintains aggregate trend data; links to PSQ.5."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at monitoring records, incident forms and analysis.

What is monitored each quarter:

- Sample MARs checked for post-administration monitoring documentation.
- Medication incident forms reviewed for completeness and timeliness.
- Analysis completion within the defined time frame.
- CAPA closure from previous analysis findings.
- Aggregate trends: medication-error rate, ADR rate, near-miss rate.
- PSQ.5 cross-reference: medication events entered into the general system.

Root-cause analysis is required when the same event type recurs within six months.

This policy is reviewed {D('annually')}, and sooner when MOM.6 or PSQ.5 is revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All nurses, prescribers and pharmacy staff are trained on this policy at induction and {D('once a year')} after that. Training covers post-administration monitoring, event capture, reporting time frames, and the no-blame reporting culture.

Staff acknowledgement

I have read this Patients Are Monitored After Medication Administration policy of {HOSPITAL}. I will monitor, document, and report medication events without delay and without fear of punishment.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/07",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.7.
- Pharmacovigilance Programme of India (PvPI) — ADR reporting requirements.
- Internal documents of {HOSPITAL}: medication administration record (MAR); medication incident form; PSQ.5 incident reporting system; MOM.3 prescription audit; committee meeting minutes."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; every in-patient ward; emergency room; ICU where it exists; nursing administration.

The current version is available to all staff at the {D('nursing station policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """ADR — adverse drug reaction
AMC — ADR Monitoring Centre
CAPA — corrective and preventive action
IV — intravenous
MAR — medication administration record
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PSQ — Patient Safety and Quality Improvement (NABH SHCO chapter 3)
PvPI — Pharmacovigilance Programme of India
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "MOM.7.a",
        "requirement": "Patients are monitored after medication administration.",
        "steps": "Statement of intent; Section 3; 5.1 Post-administration monitoring",
        "responsible": "Nurses (monitor and document); treating doctor (review abnormal observations)",
        "records": [
            "MAR entries showing post-administration monitoring.",
            "Nursing notes for abnormal observations and doctor notification.",
            "Quarterly audit sample of monitoring documentation.",
            "High-risk medication monitoring records within the defined time.",
        ],
    },
    {
        "oe_code": "MOM.7.b",
        "requirement": "Medications are changed where appropriate based on the monitoring.",
        "steps": "5.2 Medication changes based on monitoring",
        "responsible": "Treating doctor (review and change); nurse and pharmacist (implement)",
        "records": [
            "Clinical notes documenting the reason for medication change.",
            "New medication orders following the change.",
            "Communication records to nurse and pharmacist.",
        ],
    },
    {
        "oe_code": "MOM.7.c",
        "requirement": "The organisation captures near miss, medication error and adverse drug reaction.",
        "steps": "Section 3; Section 4 items 2–4; 5.3 Capture of near-misses, medication errors and ADRs",
        "responsible": "All staff (capture and report); Pharmacy In-Charge (receive forms); PSQ.5 (cross-reference)",
        "records": [
            "Medication incident forms with all required fields completed.",
            "PSQ.5 incident-system entries for medication events.",
            "Quarterly count of near-misses, errors and ADRs reported.",
            "Evidence of no-blame reporting culture (no punitive actions for good-faith reports).",
        ],
    },
    {
        "oe_code": "MOM.7.d",
        "requirement": "Near miss, medication error and adverse drug reaction are reported and analysed within a specified time frame.",
        "steps": "Section 4 items 2–5; 5.4 Reporting and analysis within a specified time frame",
        "responsible": "Pharmacy In-Charge (analysis); Quality Coordinator (track); committee (review)",
        "records": [
            "Reporting time-stamp evidence (form submission time vs event time).",
            "Analysis records completed within the defined time frame.",
            "Pharmacovigilance reports submitted to the ADR Monitoring Centre where applicable.",
            "Committee meeting minutes reviewing analysis findings.",
        ],
    },
    {
        "oe_code": "MOM.7.e",
        "requirement": "Corrective and/or preventive action(s) are taken based on the analysis.",
        "steps": "5.5 Corrective and preventive action",
        "responsible": "Committee (decide CAPA); Quality Coordinator (track closure)",
        "records": [
            "CAPA log linked to medication-event analysis.",
            "Root-cause analysis records for recurring events.",
            "Closure evidence for each action item.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.7 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Patients are monitored after medication administration." MOM.7.a–e PDF indices 85–86. MOM.7.a, MOM.7.c, MOM.7.d asterisked. MOM.7.e Core.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. MOM roles only. PSQ.5 cross-reference for incident system."""


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
        "subtitle": "Post-administration monitoring, event capture, reporting and CAPA.",
        "doc_no": "MOM/POL/07",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom7_v2_draft.json",
        "MOM.7_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
