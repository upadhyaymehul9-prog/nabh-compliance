# -*- coding: utf-8 -*-
"""HCO AAC.10 v2 — patient care continuous and multi-disciplinary.

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer accreditation-only.
Wording from NABH HCO Full Accreditation 6th Edition Guidebook
(PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices ~86–88 /
policies/source/hco6_aac_ocr.txt. Do not copy SHCO AAC wording.

Eight OEs a–h. Core: d. Asterisk: f. No stop-work.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_accreditation_only
from pre_v2_common import (
    BLANK,
    D,
    HCO_EDITION_LABEL,
    HOSPITAL,
    document_control,
    emit_pre_v2,
)

STANDARD_CODE = "AAC.10"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.10.a", "AAC.10.b", "AAC.10.c", "AAC.10.d",
    "AAC.10.e", "AAC.10.f", "AAC.10.g", "AAC.10.h",
]
POLICY_TITLE = "Continuous and Multi-Disciplinary Patient Care"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": (
            "HCO Full 6th Edition AAC.10 v2 draft from guidebook OCR; "
            "eight steps; Core d; asterisk f; no stop-work; accreditation-only P2."
        ),
    },
]

STATEMENT_OF_INTENT = (
    "Patient care is continuous and multi-disciplinary — a named doctor holds "
    "responsibility in every phase, care is coordinated across settings, and "
    "handover, transfer and referral keep the team aligned."
)

PURPOSE = f"""This policy says how {HOSPITAL} keeps patient care continuous and multi-disciplinary across all phases and care settings.

It covers eight jobs that match the standard:

- identify a qualified doctor as responsible for the patient's care during all phases;
- coordinate care in every care setting within the organisation;
- share information about care and response to treatment among medical, nursing and other providers;
- implement standardised hand-over communication at each staffing shift, between shifts and on transfers between units;
- transfer patients within the organisation safely (including to and from imaging, and unstable patients);
- refer to other departments and specialities under written guidance;
- deliver services to defined timelines and inform the patient, family or caregiver when the schedule changes;
- monitor that an adequate clinical intervention follows a critical value alert.

The chapter intent is that patient care is continuous and multi-disciplinary, and that continuity extends through handover, transfer and referral.

This policy owns continuity, coordination, hand-over, intra-organisation transfer, internal referral, service timelines and critical-value response monitoring. AAC.3 owns transfer-in and transfer-out to another facility. AAC.12 owns discharge process. AAC.13 owns discharge-summary content. COP.1.e owns the multi-disciplinary care-plan discussion this standard cross-refers for information sharing.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies at {HOSPITAL} in out-patient, emergency, in-patient wards, intensive or high-dependency areas, day-care, imaging and any other care setting where the organisation provides clinical care.

It binds:

- treating doctors identified as responsible for the patient;
- nurses who hand over at shift change and accompany internal transfers;
- registration and front-office staff who support schedule communication where applicable;
- the {D('Medical Superintendent')} who is accountable that continuity processes are defined and followed;
- the {D('Quality Coordinator')} who audits records;
- other care providers (allied health, imaging, laboratory) who share care information and receive referrals.

Boundaries with other policies of {HOSPITAL}:

- AAC.3 owns transfer-in and transfer-out / referral to another facility. This policy owns transfer within the organisation and referral to other departments or specialities inside the organisation.
- COP.1.e owns multi-disciplinary care planning. This policy owns that care and response information is shared among providers (AAC.10.c).
- AAC.12 owns the discharge process. This policy owns continuity until discharge begins.
- AAC.6 / AAC.8 own laboratory and imaging service delivery. This policy owns safe transport to and from imaging and monitoring of clinical response to critical value alerts.
- PRE owns patient rights and consent. This policy owns clinical continuity and hand-over method."""

POLICY_STATEMENT = f"""{HOSPITAL} identifies a qualified doctor as responsible for each patient's care during all phases of care. Care is coordinated in all care settings. Information about care and response to treatment is shared among medical, nursing and other care providers.

{HOSPITAL} implements standardised hand-over communication during each staffing shift, between shifts and during transfers between units and departments. Intra-organisation transfer is done safely. Referral to other departments and specialities follows written guidance.

{HOSPITAL} defines service timelines, informs the patient, family or caregiver when a schedule changes, and monitors whether an adequate clinical intervention has taken place after a critical value alert.

{HOSPITAL} does not leave a patient without a named responsible doctor, and does not hand over or transfer without documented, standardised communication."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no ward convenience exception.

1. Leaving a patient at any phase of care without a qualified doctor identified in the record as responsible for care.
2. Coordinating care in only one setting while omitting OPD, emergency, in-patient or ICU communication when the patient moves across those settings.
3. Withholding care and response information from authorised medical, nursing or other care providers who need it for that patient.
4. Handing over at shift change, between shifts or on unit transfer without the standardised hand-over method.
5. Moving a patient within the organisation — including to or from imaging, or an unstable patient — without safe transport, documented hand-over and takeover.
6. Referring to another department or speciality without written guidance, without stating opinion / co-management / takeover, without an urgency grade, or outside the defined timeframe for that grade.
7. Changing a defined service schedule without informing the patient, family or caregiver.
8. Receiving a critical value alert without a documented clinical response and without a mechanism to review whether the intervention was adequate.

Staff who see one of these acts report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Responsible doctor identified for all phases of care

During all phases of care at {HOSPITAL}, a qualified individual is identified as responsible for the patient's care. That individual is a qualified doctor. A team may deliver care; the hospital record still names one doctor as responsible.

The responsible doctor's name is recorded in the patient record at first contact and updated when responsibility changes. When the named doctor is off duty, the covering doctor is identified and the change is recorded. Out-patient, emergency, in-patient, intensive care and day-care each keep the same rule: no patient is without a named responsible doctor.""",

f"""5.2 Care coordinated in all care settings

Patient care is coordinated among care providers in each care setting within {HOSPITAL}: out-patient, emergency, in-patient, intensive care and any other setting this hospital uses.

Coordination means the patient's requirements are communicated to the providers working in that setting so that orders, observations and pending tasks are not lost when the patient moves from one setting to another. The {D('treating doctor and the nurse in charge of the area')} ensure the receiving setting knows the clinical status and the next required actions before the patient arrives or as soon as care begins there.""",

f"""5.3 Sharing care and response information among providers

Information about the patient's care and response to treatment is shared among medical, nursing and other care providers at {HOSPITAL}.

Sharing is done through entries in the case sheet or electronic medical record so that authorised care providers can read the same clinical picture. Other modalities this hospital uses include {D('team meetings and grand rounds')} where they are part of practice. The patient record remains available to authorised providers. Cross-reference COP.1.e for multi-disciplinary care-plan discussion; this step owns the day-to-day sharing of care and response information.""",

f"""5.4 Standardised hand-over communication

{HOSPITAL} implements standardised hand-over communication during each staffing shift, between shifts and during transfers between units and departments. Change-of-shift and change-of-unit hand-over by doctors and nurses in direct patient care is standardised and documented.

Information shared covers the patient's current condition, recent changes, ongoing treatment and possible changes or complications. The hand-over framework is {D('SBAR (Situation, Background, Assessment, Recommendation)')}. Read-back, multidisciplinary rounds, teach-back and involving patients and families may be used to strengthen the same hand-over. The receiving clinician acknowledges the hand-over. Interruptions during hand-over are minimised.""",

f"""5.5 Safe transfer within the organisation

Patient transfer within {HOSPITAL} is done safely. Patients are transported in a safe and timely manner. Proper hand-over and takeover are documented.

Transfers to and from imaging follow the same rule so that imaging is not delayed by transport failure. Unstable patients are transferred with the accompaniment and monitoring this hospital defines for their clinical status — {D('a doctor accompanies unstable patients')} — and the receiving area confirms readiness before departure.""",

f"""5.6 Referral to other departments and specialities under written guidance

Referral of patients to other departments or specialities at {HOSPITAL} follows written guidance. Referral may be for opinion, co-management or takeover. The referral note states the reason for referral.

Urgency is graded as {D('immediate, urgent, priority or routine')}. Every referral is based on clinical significance and intended outcome. Every referral is seen within a defined timeframe; the timeframe differs by urgency grade. Written guidance holds the grades, the timeframes and who may accept a referral. The {D('Medical Superintendent')} holds the current written guidance; treating doctors follow it when they refer.""",

f"""5.7 Predictable service delivery and schedule changes

{HOSPITAL} ensures predictable service delivery by adhering to defined timelines and informs the patient, family and/or caregiver whenever there is a change in schedule.

Defined timelines cover services such as {D('laboratory, radiology and OPD waiting time')}. Patients are informed of the applicable timelines. When delivery will deviate, the patient or family is told of the changed schedule, and the caregiver is informed so that effectiveness of care is not compromised. Front-office or the service area records that the change was communicated.""",

f"""5.8 Monitoring clinical intervention after critical value alerts

{HOSPITAL} has a mechanism to monitor whether an adequate clinical intervention has taken place in response to a critical value alert.

The attending clinician responds to the alert. Evidence of the response is documented in progress notes or medication orders. The organisation periodically reviews interventions for timeliness and appropriateness. For out-patients, efforts are taken to alert the patient or family about critical values. The {D('Quality Coordinator')} samples critical-value responses {D('quarterly')} under the monitoring section.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that continuity, hand-over, internal transfer and referral written guidance are defined and followed.
- Holds the current referral written guidance (urgency grades and timeframes).

Treating doctors
- Named as responsible for the patient; hand over to covering doctors; share care information; write and accept referrals within timeframes; respond to critical value alerts.

Nurses
- Perform shift and transfer hand-over using the standardised method; accompany internal transfers; document hand-over and takeover.

Registration / front-office
- Support communication of service timelines and schedule changes where the service area asks them to.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when continuity, hand-over, transfer or critical-value response defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Responsible doctor named in the record for sampled patients in each care setting.
- Coordination evidence when patients move across OPD, emergency, in-patient or ICU.
- Information sharing in the case sheet / EMR among authorised providers.
- Standardised hand-over documentation at shift change and on unit transfer.
- Safe internal transfer records, including imaging transfers and unstable-patient transfers.
- Referral notes with reason, type (opinion / co-management / takeover), urgency grade and response within timeframe.
- Service-timeline adherence and record that schedule changes were communicated.
- Critical value alerts with documented clinical intervention and periodic review of adequacy.

Root-cause analysis is required when the same continuity or hand-over defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when ward layout, hand-over tools, referral timeframes or critical-value routes change."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors, nurses and other care providers who hand over, transfer or refer patients are trained on this policy at induction and {D('once a year')} after that. Training covers responsible-doctor identification, the hand-over framework, safe internal transfer, referral grades and timeframes, schedule communication and critical-value response.

Staff acknowledgement

I have read this Continuous and Multi-Disciplinary Patient Care policy of {HOSPITAL}. I will keep a named responsible doctor, hand over using the standardised method, transfer and refer safely, and respond to critical value alerts.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/10"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.10 (PDF indices ~86–88; source OCR policies/source/hco6_aac_ocr.txt; PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Cross-reference within the same guidebook: COP.1.e (information sharing / multi-disciplinary care).
- Internal documents of {HOSPITAL}: hand-over tool or register; internal transfer checklist; referral written guidance; service timeline definitions; critical value alert and response log."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; emergency; out-patient; intensive care; imaging; day-care; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
CAPA — corrective and preventive action
COP — Care of Patients (NABH HCO chapter)
EMR — electronic medical record
HCO — Hospital Accreditation Programme (NABH Full Accreditation)
ICU — intensive care unit
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
OPD — out-patient department
SBAR — Situation, Background, Assessment, Recommendation"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.10.a",
        "requirement": (
            "During all phases of care, there is a qualified individual identified as "
            "responsible for the patient's care."
        ),
        "steps": "Section 3; 5.1 Responsible doctor identified for all phases of care; Section 4 item 1",
        "responsible": "Treating doctors (named in record); Medical Superintendent (accountable)",
        "records": [
            "Patient record entry naming the responsible doctor for each phase of care.",
            "Covering-doctor record when the named doctor is off duty.",
            "Quarterly audit sample of responsible-doctor documentation across care settings.",
        ],
    },
    {
        "oe_code": "AAC.10.b",
        "requirement": "Patient care is coordinated in all care settings within the organisation.",
        "steps": "Section 3; 5.2 Care coordinated in all care settings; Section 4 item 2",
        "responsible": "Treating doctors and nurses in charge of each setting; Medical Superintendent (accountable)",
        "records": [
            "Communication or transfer note when a patient moves between OPD, emergency, IP or ICU.",
            "Ward or area handover listing pending requirements for patients newly arrived in the setting.",
            "Quarterly audit sample of cross-setting coordination.",
        ],
    },
    {
        "oe_code": "AAC.10.c",
        "requirement": (
            "Information about the patient's care and response to treatment is shared among "
            "medical, nursing and other care providers."
        ),
        "steps": "Section 3; 5.3 Sharing care and response information among providers; Section 4 item 3",
        "responsible": "Treating doctors, nurses and other authorised care providers",
        "records": [
            "Case sheet or EMR entries by medical, nursing and other providers on the same patient.",
            "Record of team meeting or grand round where used for sharing.",
            "Quarterly audit sample of information-sharing completeness.",
        ],
    },
    {
        "oe_code": "AAC.10.d",
        "requirement": (
            "The organisation implements standardised hand-over communication during each "
            "staffing shift, between shifts and during transfers between units / departments."
        ),
        "steps": "Section 3; 5.4 Standardised hand-over communication; Section 4 item 4",
        "responsible": "Nurses (shift hand-over); treating doctors (doctor-to-doctor); Quality Coordinator (audit)",
        "records": [
            "Documented hand-over using the standardised framework for each staffing shift sampled.",
            "Transfer hand-over between units with acknowledgement by the receiving team.",
            "Quarterly audit of hand-over content (condition, changes, treatment, complications).",
        ],
    },
    {
        "oe_code": "AAC.10.e",
        "requirement": "Patient transfer within the organisation is done safely.",
        "steps": "Section 3; 5.5 Safe transfer within the organisation; Section 4 item 5",
        "responsible": "Treating doctors (authorise unstable transfers); nurses (accompany and document); Quality Coordinator (audit)",
        "records": [
            "Internal transfer record with reason, clinical status, times, hand-over and takeover.",
            "Imaging transfer records showing timely transport to and from imaging.",
            "Unstable-patient transfer records showing accompaniment and monitoring.",
        ],
    },
    {
        "oe_code": "AAC.10.f",
        "requirement": "Referral of patients to other departments / specialities follow written guidance.",
        "steps": "Section 3; 5.6 Referral to other departments and specialities under written guidance; Section 4 item 6",
        "responsible": "Treating doctors (refer and respond); Medical Superintendent (holds written guidance); Quality Coordinator (audit)",
        "records": [
            "Current written guidance for internal referral (opinion / co-management / takeover; urgency grades; timeframes).",
            "Referral notes stating reason, type and urgency grade.",
            "Response-time log showing referral seen within the timeframe for that grade.",
        ],
    },
    {
        "oe_code": "AAC.10.g",
        "requirement": (
            "The organisation ensures predictable service delivery by adhering to defined "
            "timelines and informs the patient / family and / or caregiver whenever there is a change in schedule."
        ),
        "steps": "Section 3; 5.7 Predictable service delivery and schedule changes; Section 4 item 7",
        "responsible": "Service-area leads and registration/front-office; treating doctors where clinical schedule changes; Quality Coordinator (audit)",
        "records": [
            "Defined service timelines (for example laboratory, radiology, OPD waiting time).",
            "Record that patients were informed of applicable timelines.",
            "Record of schedule-change communication to patient, family or caregiver.",
        ],
    },
    {
        "oe_code": "AAC.10.h",
        "requirement": (
            "The organisation has a mechanism in place to monitor whether an adequate clinical "
            "intervention has taken place in response to a critical value alert."
        ),
        "steps": "Section 3; 5.8 Monitoring clinical intervention after critical value alerts; Section 4 item 8",
        "responsible": "Attending clinicians (respond and document); Quality Coordinator (periodic review)",
        "records": [
            "Critical value alert log with time of alert and clinician notified.",
            "Progress notes or medication orders documenting the clinical intervention.",
            "Periodic review record of timeliness and appropriateness of responses, including out-patient alerts to patient or family.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.10 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Source OCR policies/source/hco6_aac_ocr.txt (PDF idxs ~86–88). Eight OEs a–h. Core: d (standardised hand-over). Asterisk: f (referral written guidance) — fuller procedure and evidence. No stop-work (not a facilities hazard standard). P2: accreditation-only via make_hco_disclaimer_accreditation_only. chapter=HCO. doc_no «HCO/AAC/POL/10». Cross-ref COP.1.e for information sharing; AAC.3 owns external transfer; AAC.12/13 own discharge. HCO tiering: asterisked OE f given Tier-1-style depth; remaining OEs accurate Tier-2 prose from guidebook. Do not copy SHCO AAC.7 wording."""


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
        "subtitle": "Continuous, coordinated care, hand-over, internal transfer and referral.",
        "doc_no": D("HCO/AAC/POL/10"),
        "programme": "HCO Full Accreditation, 6th Edition",
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.10",
    }
    emit_pre_v2(
        draft,
        "hco_aac10_v2_draft.json",
        "HCO.AAC.10_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
