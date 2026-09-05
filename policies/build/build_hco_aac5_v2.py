# -*- coding: utf-8 -*-
"""HCO AAC.5 v2 — re-assessment (HCO Full, 6th Edition).

Shape follows PRE/SHCO v2 adoptable-policy shape via pre_v2_common.
Wording from NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition
— AAC chapter (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices 72–73.
OCR source: policies/source/hco6_aac_ocr.txt.

Five OEs (a–e). Asterisk on e. Core on a. Stop-work INCLUDED for early-warning
trigger not escalated (do not leave a deteriorating patient without escalation).
Correlate COP.5, COP.6, HRM.1, HRM.5 — note boundary, do not duplicate.
Does NOT overwrite SHCO AAC builders or drafts.
"""
from __future__ import annotations

import sys

from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW
from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, document_control, emit_pre_v2

STANDARD_CODE = "AAC.5"
CHAPTER = "HCO"
OE_CODES = ["AAC.5.a", "AAC.5.b", "AAC.5.c", "AAC.5.d", "AAC.5.e"]
POLICY_TITLE = "Re-assessment"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO Full 6th Edition AAC.5 v2 draft: plain English, five steps, stop-work (do not defer escalation for non-urgent work), accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "After the first assessment, patients are reassessed often enough to see whether "
    "treatment is working — the care plan moves with the patient, notes are real "
    "clinical notes, and early warning signs trigger prompt action."
)

PURPOSE = f"""This policy says how {HOSPITAL} reassesses patients at appropriate intervals to determine response to treatment and to plan further treatment or discharge; informs out-patients of the next follow-up where appropriate; monitors and modifies the in-patient care plan during re-assessment; requires direct clinical care staff to document re-assessments properly; and lays down guidelines to identify early warning signs of change or deterioration for prompt intervention.

The chapter intent is that patients undergo initial assessment and periodic reassessments resulting in a care plan.

This policy owns re-assessment after AAC.4 initial assessment. AAC.4 owns the first assessment and the initial care plan. Early-warning mechanics correlate with COP.5, COP.6, HRM.1 and HRM.5 as the guidebook states — this policy owns the AAC.5.e requirement to identify deterioration and escalate; those COP/HRM policies own the related clinical and human-resource detail.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors, nurses and other caregivers who reassess patients at {HOSPITAL} in out-patient, day-care, in-patient wards, ICU/high-dependency and areas where patients await admission or a bed. It binds the Medical Superintendent, department heads, Medical Records, and the Quality Coordinator.

It covers AAC.5.a–e.

Boundaries:

- AAC.4 owns initial assessment and creation of the care plan; this policy owns monitoring and modifying that plan at re-assessment.
- AAC.12 owns the discharge process; this policy owns re-assessment that informs the decision to discharge.
- COP.5 / COP.6 own related clinical emergency and acute-care pathways named in the guidebook correlation; this policy owns early-warning identification and escalation under AAC.5.e.
- HRM.1 / HRM.5 own staffing competence and related HR elements named in the guidebook correlation; this policy requires trained staff to use early-warning parameters, not the full HRM programme.
- Lab and imaging own critical-result reporting; critical values that change the plan are acted on at re-assessment here and under AAC.10 where continuous care applies."""

POLICY_STATEMENT = f"""{HOSPITAL} reassesses patients at appropriate intervals to determine response to treatment and to plan further treatment or discharge. Out-patients are informed of their next follow-up where appropriate. For in-patients, the care plan is monitored and modified during re-assessment where necessary. Staff involved in direct clinical care document re-assessments. The organisation lays down guidelines and implements processes to identify early warning signs of change or deterioration for prompt intervention.

{HOSPITAL} does not leave a deteriorating patient without escalation when early-warning triggers fire, and does not accept reassessment notes that say only “patient well” or “condition better”."""

NON_NEGOTIABLES = f"""1. Do not go a calendar day without re-assessment of an in-patient by the treating doctor or a doctor from the treating team; reassess more often in ICU and when the condition changes; reassess day-care patients before discharge.
2. Do not send an out-patient away without documenting the next follow-up where a repeat visit is appropriate.
3. Do not leave an ineffective in-patient care plan unchanged when re-assessment shows it must be modified.
4. Do not document re-assessment with only phrases such as “patient well” or “condition better” — include vitals, systemic findings and medication orders at minimum (nurses may document vitals).
5. Do not ignore early-warning triggers — escalate to appropriate medical personnel and intervene promptly.
6. Staff who find re-assessment or early-warning rules not followed report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not leave a deteriorating patient without escalation when early-warning signs or defined physiological triggers indicate change or deterioration.

If a trigger is met and appropriate medical personnel have not yet been informed and acted, do not defer escalation for non-urgent work; escalate immediately per the early-warning guideline, start prompt intervention within your scope, and document the trigger, time of escalation, responder and actions.

Stop-work applies to failure to escalate a deteriorating patient. It does not block emergency life-saving measures — those continue while escalation happens.

The person responsible tells the {D('treating doctor')} and, if there is no timely response, the {D('Medical Superintendent')} the same shift. Refusing to leave a deteriorating patient unescalated is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Re-assess at appropriate intervals

After initial assessment, every patient is reassessed periodically and the re-assessment is documented in the case sheet. Re-assessment is done by all applicable caregivers within their scope of practice, registration and applicable laws.

Frequency differs by setting and condition: ICU and high-dependency patients are reassessed more frequently than ward patients. Re-assessment is also done when the patient's condition changes significantly.

Every patient is reassessed at least once every day by the treating doctor or a doctor from the treating team. Day-care patients are reassessed before discharge. Patients awaiting admission or a bed are also reassessed as applicable.

Default ward interval beyond the daily medical re-assessment: {D('nursing observations at the frequency set on the care plan, at least once per shift')}. Default ICU: {D('as per ICU protocol, not less than every 1–2 hours for unstable patients')}. """,

f"""5.2 Inform out-patients of next follow-up where appropriate

Out-patients are informed of their next follow-up where appropriate. The information is a specific date or a period (weeks/months) and is documented in the medical record or OP consultation sheet.

Follow-up information may be omitted when the patient came only for an opinion or when the condition does not warrant a repeat visit — note that reason briefly in the OP record.""",

f"""5.3 Monitor and modify the in-patient care plan during re-assessment

For in-patients, during re-assessment the care plan is monitored for effectiveness in achieving the desired results of treatment, care or service. The care plan is dynamic. The treating doctor or a doctor member of the treating team modifies it where necessary according to the patient's condition.

Changes are documented in the medical record. Progress notes, doctor's orders or medication charts may show the change — the change must be findable, not only spoken.""",

f"""5.4 Direct clinical care staff document re-assessments

Actions taken under re-assessment are documented by the treating doctor or any member of the team per their domain of responsibility. At a minimum, documentation includes vitals, systemic examination findings and medication orders. Nursing staff may document the patient's vitals.

Phrases alone such as “patient well” or “condition better” are not acceptable as a re-assessment note.""",

f"""5.5 Early warning signs — guidelines and prompt intervention

{HOSPITAL} lays down guidelines and implements processes to identify early warning signs of change or deterioration in clinical condition and to initiate prompt intervention.

Staff use defined physiological parameters — which may include vital parameters, airway, circulation, neurological status, and any other concerns felt by staff or the patient/family. Parameters may be tailored to speciality and age group.

There is a mechanism to make this information available to appropriate medical personnel to initiate prompt and appropriate actions. Effectiveness of the early-warning system is monitored {D('monthly')} by the Quality Coordinator with clinical leads.

Correlate with COP.5, COP.6, HRM.1 and HRM.5 for related clinical and staffing requirements; do not duplicate those policies here. This section owns the AAC.5.e identification-and-escalation duty and the stop-work rule when escalation does not happen.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable for re-assessment intervals, documentation standards and early-warning guidelines.
- Receives escalation when treating-doctor response is not timely.

Treating doctors / treating team
- Daily medical re-assessment at minimum; more often as needed; modify care plans; respond to early-warning alerts.

Nurses and other direct clinical caregivers
- Reassess within scope; document vitals and nursing findings; trigger early-warning escalation; never rely on “patient well” alone.

OPD doctors
- Document next follow-up where appropriate.

Department heads / ICU in-charge
- Set area-specific frequencies and early-warning parameter sets for speciality and age group.

Quality Coordinator
- Audits daily re-assessment, follow-up documentation, care-plan changes, note quality and early-warning effectiveness {D('quarterly')} (early-warning effectiveness also reviewed {D('monthly')}).

Medical Records
- Flag missing daily notes and inadequate re-assessment phrases during record review."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')} and reviews early-warning effectiveness {D('monthly')}.

What is monitored:

- IP sample shows at least daily medical re-assessment; ICU more frequent; day-care re-assessed before discharge.
- OP sample shows follow-up documented where appropriate, or a brief reason when not.
- Care-plan modifications documented when re-assessment required change.
- Re-assessment notes include vitals, systemic findings and medication orders — not only “patient well”.
- Early-warning triggers escalated with time, responder and action documented; failed escalations treated as incidents.

Root-cause analysis is required when a deteriorating patient was not escalated, or when inadequate re-assessment notes recur within six months.

This policy is reviewed {D('annually')}, and sooner after any failure-to-escalate event."""

TRAINING_ACKNOWLEDGEMENT = f"""Doctors, nurses and other direct clinical caregivers are informed of this policy at induction and {D('once a year')} after that. Training covers interval rules, OP follow-up documentation, care-plan modification, acceptable re-assessment content, early-warning parameters, escalation routes and stop-work.

Staff acknowledgement

I have read this Re-assessment policy of {HOSPITAL}. I will reassess at the required intervals, document real clinical findings, modify the care plan when needed, and escalate early-warning triggers without delay.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with clinical induction records.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/05"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care (AAC), standard AAC.5.
- Correlated standards named in the guidebook interpretation: COP.5; COP.6; HRM.1; HRM.5.
- Internal documents of {HOSPITAL}: re-assessment interval guidance by area; early-warning / track-and-trigger guideline; care-plan modification method; AAC.4 initial-assessment policy; related COP and HRM policies (cross-reference)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every ward and ICU; day-care; OPD; emergency; nursing administration; medical records.

The current version is available to all staff at the {D('clinical policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH Hospitals chapter)
CAPA — corrective and preventive action
COP — Care of Patients (NABH chapter)
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
HRM — Human Resource Management (NABH chapter)
ICU — intensive care unit
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OP / OPD — out-patient / out-patient department"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.5.a",
        "requirement": "Patients are re-assessed at appropriate intervals to determine their response to treatment and to plan further treatment or discharge.",
        "steps": "Section 3; 5.1 Re-assess at appropriate intervals; Section 4 item 1",
        "responsible": "Treating doctors (daily medical re-assessment); nurses and caregivers (within scope); ICU in-charge (ICU frequency)",
        "records": [
            "IP case sheets showing at least daily re-assessment by treating doctor or treating-team doctor.",
            "ICU observation charts showing more frequent re-assessment than ward.",
            "Day-care records showing re-assessment before discharge.",
            "Re-assessment notes after significant change in condition.",
        ],
    },
    {
        "oe_code": "AAC.5.b",
        "requirement": "Out-patients are informed of their next follow-up, where appropriate.",
        "steps": "Section 3; 5.2 Inform out-patients of next follow-up where appropriate; Section 4 item 2",
        "responsible": "OPD treating doctors (inform and document)",
        "records": [
            "OP consultation sheets with next follow-up date or interval documented.",
            "Sample where follow-up was not applicable with brief reason noted (opinion-only or no repeat visit warranted).",
            "Audit of OP records for follow-up documentation completeness.",
        ],
    },
    {
        "oe_code": "AAC.5.c",
        "requirement": "For in-patients during re-assessment, the care plan is monitored and modified, where found necessary.",
        "steps": "Section 3; 5.3 Monitor and modify the in-patient care plan during re-assessment; Section 4 item 3",
        "responsible": "Treating doctor or doctor member of treating team (monitor and modify)",
        "records": [
            "Progress notes, doctor's orders or medication charts showing care-plan changes.",
            "Sample where ineffective plan was modified with clinical reason.",
            "Audit linking re-assessment findings to documented plan changes.",
        ],
    },
    {
        "oe_code": "AAC.5.d",
        "requirement": "Staff involved in direct clinical care document re-assessments.",
        "steps": "Section 3; 5.4 Direct clinical care staff document re-assessments; Section 4 item 4",
        "responsible": "Treating doctors and team members (document per domain); nurses (vitals)",
        "records": [
            "Re-assessment notes including vitals, systemic examination findings and medication orders.",
            "Nursing vital-sign charts contributing to re-assessment documentation.",
            "Record-review log rejecting notes that only say “patient well” / “condition better”.",
        ],
    },
    {
        "oe_code": "AAC.5.e",
        "requirement": "The organisation lays down guidelines and implements processes to identify early warning signs of change or deterioration in clinical conditions for initiating prompt intervention.",
        "steps": "Section 3; 5.5 Early warning signs — guidelines and prompt intervention; Section 4 item 5; Section 6 Stop-work",
        "responsible": "Medical Superintendent (approve guideline); treating doctors (respond); nurses (trigger); Quality Coordinator (monitor effectiveness)",
        "records": [
            "Written early-warning guideline with physiological parameters (speciality/age tailored where used).",
            "Escalation records showing trigger, time informed, responder and actions.",
            "Monthly early-warning effectiveness review notes.",
            "Incident/RCA records for failure-to-escalate events.",
            "Cross-reference note to COP.5, COP.6, HRM.1 and HRM.5 owners.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.5 v2 (2026-08-20). HCO Full Accreditation, NABH Hospitals 6th Edition.
PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. OCR: policies/source/hco6_aac_ocr.txt (PDF indices 72–73).

OE COUNT: 5 (a–e). Asterisked: AAC.5.e (Tier 1). Core: AAC.5.a. AAC.5.b–d Commitment without asterisk (Tier 2).

SHAPE: Five What-we-do subsections (5.1–5.5). Stop-work YES — early-warning trigger not escalated / deteriorating patient without escalation. Disclaimer accreditation-only. chapter=HCO, doc_no HCO/AAC/POL/05.

GUIDEBOOK CORRELATION: COP.5, COP.6, HRM.1, HRM.5 — boundary noted; not duplicated.

FLAG: none after OCR clean-up (patientis→patient is; CQRE chrome ignored)."""


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
        "prepared_by": D("Quality Coordinator"),
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "HCO Full Accreditation, 6th Edition — re-assessment.",
        "doc_no": D("HCO/AAC/POL/05"),
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with clinical induction records.",
        "stop_work": STOP_WORK,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.5",
    }
    emit_pre_v2(
        draft,
        "hco_aac5_v2_draft.json",
        "HCO.AAC.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
        drafts_dir=HCO_DRAFTS,
        preview_dir=HCO_PREVIEW,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
