# -*- coding: utf-8 -*-
"""HCO AAC.9 v2 — imaging quality assurance and safety (Full Accreditation 6th Edition).

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer.
Content from NABH HCO 6th Edition PDF (md5 2c4489ee98de4ae9b49cba168ea9f42a),
OCR policies/source/hco6_aac_ocr.txt PDF idxs ~82–86. No SHCO AAC wording.
Stop-work: incomplete screening / failed devices; pregnancy hold-for-review is
hospital safety practice (not an NABH OE requirement). Disclaimer P2: AERB Rules 2004.
"""
from __future__ import annotations

import sys

from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW
from hco_v2_disclaimer import make_hco_disclaimer_statute
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, emit_pre_v2

STANDARD_CODE = "AAC.9"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.9.a", "AAC.9.b", "AAC.9.c", "AAC.9.d", "AAC.9.e", "AAC.9.f",
    "AAC.9.g", "AAC.9.h", "AAC.9.i", "AAC.9.j", "AAC.9.k",
]
POLICY_TITLE = "Imaging Quality Assurance and Safety Programme"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO AAC.9 v2: imaging QA and safety a–k from 6th Edition OCR; AERB P2; stop-work for screening/devices; pregnancy hold framed as hospital safety practice (not NABH OE).",
    },
]

STATEMENT_OF_INTENT = (
    "There is an established quality assurance and safety programme for imaging services — "
    "so that investigations are appropriate and quality-assured, radiation exposure follows "
    "ALARA, and patients and staff are screened and protected before imaging."
)

PURPOSE = f"""This policy says how {HOSPITAL} implements a quality assurance programme for imaging (equipment tests, protocol review, AERB duties, nuclear medicine and radiotherapy per AERB where present), ensures appropriateness of investigations, conducts periodic peer review of CT/MRI results (minimum one percent), holds clinico-radiological meetings, documents corrective and preventive action (CAPA), implements a radiation-safety programme under ALARA aligned with organisation safety, screens patients (and attendants) for safety/risk before imaging, ensures use and periodic testing of radiation-safety and monitoring devices, trains imaging and ancillary personnel, and displays imaging signage.

The chapter intent is that imaging is quality-assured and safe for patients and staff.

This policy owns imaging QA and imaging/radiation safety (AAC.9). AAC.8 owns legal licences, service scope, TAT, critical results, reporting format and outsourcing MoUs. PRE owns informed-consent method referenced for contrast, sedation and interventional procedures (PRE.4.a in the guidebook).

ALARA — As Low As Reasonably Achievable. TLD — thermo-luminescent dosimeter. RSO — Radiation Safety Officer. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the imaging/radiology in-charge, Radiation Safety Officer (RSO), radiographers and technologists, reporting doctors, ancillary staff posted in imaging (nurses, helpers, stretcher-bearers, housekeeping, security), treating doctors who request imaging, patients and attendants entering imaging areas, and the Quality Coordinator at {HOSPITAL}.

It covers the eleven objective elements AAC.9.a–k: QA programme; appropriateness of investigations; peer review of CT/MRI; clinico-radiological meetings; CAPA documentation; radiation-safety programme; patient screening; use of radiation-safety devices; periodic testing of devices; training; signage.

Boundaries:

- AAC.8 owns AERB clearance/PC-PNDT registration as service legal compliance, TAT and critical intimation. This policy owns ongoing QA tests, ALARA protocols, screening before each examination, device testing and safety training.
- PRE owns the informed-consent process; this policy requires consent for contrast, moderate–deep sedation, interventional procedures and higher-risk findings on screening, by reference to PRE.
- Organisation safety programme owns hospital-wide safety governance; radiation-safety here is aligned with it.
- Spell out: As Low As Reasonably Achievable (ALARA), thermo-luminescent dosimeter (TLD), Radiation Safety Officer (RSO), corrective and preventive action (CAPA), computed tomography (CT), magnetic resonance imaging (MRI)."""

POLICY_STATEMENT = f"""{HOSPITAL} implements a comprehensive quality assurance programme for imaging services addressing equipment, protocols, surveillance and safety, meeting AERB requirements and covering nuclear medicine and radiotherapy where those services exist. Appropriateness of investigations is checked before performance. Periodic internal or external peer review of CT and MRI results uses defined sampling of at least one percent. Clinico-radiological meetings and CAPA documentation support continuous improvement. A radiation-safety programme implementing ALARA is aligned with the organisation’s safety programme. Patients (and attendants entering imaging areas) are screened for safety and risk before imaging; personnel and patients use radiation-safety and monitoring devices; those devices are periodically tested and documented; imaging and ancillary personnel are trained; and imaging signage is prominently displayed.

{HOSPITAL} does not expose a patient to radiation or MRI without required screening, and does not continue imaging when a required safety or monitoring device has failed its periodic check."""

NON_NEGOTIABLES = f"""1. Do not perform imaging or interventional procedures that have not been screened for appropriateness to the clinical indication when the appropriateness system flags a mismatch — resolve with the treating doctor first.
2. Do not skip defined CT/MRI peer-review sampling (minimum one percent).
3. Do not leave QA or radiation-safety deviations without documented CAPA.
4. Do not justify routine unnecessary radiation (for example routine daily chest radiograph for all ICU patients without clinical indication), contrary to ALARA.
5. Do not image without completing required pregnancy screening (child-bearing age, radiation) or MRI magnetic-substance screening, including attendants who enter the area.
6. Do not proceed without required consent for contrast, moderate–deep sedation, interventional procedures, or higher risk found on screening (PRE method).
7. Do not work with radiation sources without required TLD/personnel monitoring and appropriate aprons/shields when applicable.
8. Do not use lead aprons or monitoring devices that have failed periodic testing until repaired or replaced.
9. Do not remove or obscure required imaging safety and regulatory signage.
10. Staff who see an imaging QA or safety rule broken report it the same shift to the {D('Imaging In-Charge')}, the {D('Radiation Safety Officer')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not proceed with radiation or MRI exposure when required safety/risk screening has not been completed and documented for the patient (and for any attendant entering the imaging area).

As hospital safety practice (not an NABH objective-element requirement), do not proceed when pregnancy status is positive or uncertain for a radiation examination until the {D('radiologist or imaging in-charge')} has reviewed and documented the decision. Do not proceed with MRI when magnetic-substance screening is incomplete or positive for a contraindication.

Do not proceed when a required radiation-safety or monitoring device has failed its periodic test (for example cracked lead apron) or when required TLD badges are not available for staff working with radiation sources.

Stop-work applies to the imaging exposure or MRI examination, not to emergency clinical stabilisation outside the imaging room.

The person who stops tells the {D('Imaging In-Charge')} or the {D('Radiation Safety Officer')} the same shift. Refusing to expose without screening or with failed safety devices is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Quality assurance programme for imaging

The quality assurance programme for imaging services is implemented. It is comprehensive — addressing equipment, protocols, surveillance and safety — and meets statutory AERB requirements.

The programme includes tests for imaging equipment. Examples include congruence of optical and radiation field, focal spot size, output consistency, leakage rate, magnetic field homogeneity, slice position accuracy, phantom checks and other tests as applicable. Tests are performed as applicable to the modalities present.

Quality assurance for nuclear medicine (PET / gamma camera / SPECT CT) and radiotherapy (linear accelerator, brachytherapy) is implemented as per AERB guidelines where those services exist. Safety equipment testing is performed as stated in section 5.9 (AAC.9.i).

The programme includes review of imaging protocols to ensure optimum image quality with minimum possible dosage. Protocols follow professional-body / academic guidance and, where relevant, the clinical diagnosis.

The imaging in-charge and RSO own the QA schedule; results are reviewed {D('monthly')}.""",

f"""5.2 Appropriateness of investigations and procedures

A system is in place to ensure the appropriateness of investigations and procedures for the clinical indication. Investigation orders are screened before imaging or interventional procedures to ensure they are appropriate (current best-practice guidelines and patient safety) for the clinical indication; otherwise alternate investigations are offered in consultation with the treating doctor.

Example from the standard: if breast abscess is suspected as the cause of fever and breast lump in a lactating 25-year-old woman, mammography is inappropriate; ultrasound of the breast is appropriate.

The organisation maintains a record of instances where the requested test was modified after consultation and may audit effectiveness, discussing findings in clinico-radiological meetings (section 5.4).""",

f"""5.3 Peer review of CT and MRI results

The programme addresses periodic internal / external peer review of imaging results using appropriate sampling. A peer review system reviews imaging results of CT and MRI in a structured manner. Sample size and periodicity for each modality are defined by the organisation; at a minimum this is one percent.

Peer review may be performed by the head of department or a group of peers, with blinding of original reports. Discrepancies are graded on severity and impact on patient management; CAPA to minimise recurrence is documented. RADPEER is one such scoring scale. The purpose is prevention of future errors and continuous quality improvement, not computation of individual error rates. Results may be discussed in discrepancy meetings and documented.""",

f"""5.4 Clinico-radiological meetings

The programme addresses clinico-radiological meeting(s). The organisation conducts clinico-radiological meetings at pre-defined intervals for correlating imaging results (at a minimum CT and MRI) with referring clinicians and uses them to improve quality of imaging results.

Meetings are scheduled {D('at least quarterly')} unless the Medical Superintendent defines a different interval. Minutes record correlations, discrepancies and actions.""",

f"""5.5 Corrective and preventive action documentation

The programme includes documentation of corrective and preventive actions. When deviations from the laid-down quality assurance programme are noted, the organisation institutes CAPA as appropriate.

CAPA from equipment-test failures, protocol deviations, peer-review discrepancies, appropriateness audits and radiation-safety incidents is logged with owner, due date and closure evidence. Open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.""",

f"""5.6 Radiation-safety programme

The radiation-safety programme is implemented. It follows guidelines laid down by AERB and implements the As Low As Reasonably Achievable (ALARA) principle in investigations involving radiation, including screening of patients at high risk for radiation.

Routine unjustified radiation is avoided — for example routine daily chest radiograph for all ICU patients cannot be justified, more so in paediatric or neonatal ICUs. CT protocols are modified to use the lowest exposure parameters that maintain image quality appropriate for the clinical indication (for example low-dose CT for ureteric calculi versus higher dose for renal tumour).

Appropriate safety precautions per AERB guidelines for nuclear medicine and radiation oncology are followed where those services exist. This programme is aligned with the organisation’s safety programme. The RSO owns day-to-day radiation-safety implementation with the imaging in-charge.""",

f"""5.7 Patient screening before imaging

Patients are appropriately screened for safety / risk before imaging. Patients in the child-bearing age group who need radiation exposure are screened for pregnancy. Patients undergoing MRI are screened for any magnetic substance. Screening is documented. Screening also applies to attendants accompanying the patient or child into the imaging area.

As hospital safety practice (not an NABH objective-element requirement), when pregnancy screening is positive or uncertain for a radiation examination, do not proceed until the {D('radiologist or imaging in-charge')} has reviewed and documented the decision.

Informed consent is taken for contrast injection, moderate–deep sedation, interventional procedures, and whenever higher risk due to imaging is found on risk screening. Refer to PRE for consent method.

Incomplete screening triggers stop-work until screening is complete and documented.""",

f"""5.8 Use of radiation-safety and monitoring devices

Imaging personnel and patients use appropriate radiation-safety and monitoring devices where applicable. Shielding of body parts of staff, patients and attendants uses appropriate aprons and shields. The number of devices is adequate so that all workers have proper protection. Staff directly working with radiation sources possess and use thermo-luminescent dosimeter (TLD) badges.

The RSO issues and tracks TLD badges and apron assignment. Missing required devices for a radiation examination trigger stop-work.""",

f"""5.9 Periodic testing of radiation-safety and monitoring devices

Radiation-safety and monitoring devices are periodically tested, and results are documented. Protective devices such as lead aprons are exposed to X-ray, fluoroscopy or CT scout view to verify cracks and damage. Monitoring is done periodically as per national guidelines. Images of the checks are stored (physical or electronic). Corrective and/or preventive action is taken and documented where appropriate.

TLD badges are replaced by fresh badges supplied by accredited laboratories according to the frequency recommended by AERB.

A failed device is removed from use until repaired or replaced — stop-work applies to examinations that would have relied on that device.""",

f"""5.10 Training in imaging and radiation safety

Imaging and ancillary personnel are trained in imaging safety practices and radiation-safety measures. Imaging safety practices include training on MRI safety, kinking of tubes, fall prevention and handling patients in imaging areas. Radiation-safety measures protect patient and staff from unwanted radiation.

Ancillary staff are those posted in imaging who support the radiologist, radiographers and MRI/CT technologists — including nurses, helpers, stretcher-bearers, housekeeping and security as applicable.

Training is at induction and {D('annually')}, with records held by the imaging in-charge.""",

f"""5.11 Imaging signage

Imaging signage is prominently displayed in all appropriate locations. This includes safety signage and display of signage required by regulatory authorities. It includes procedure rooms (for example ERCP) and operation theatres where imaging equipment is used.

The imaging in-charge and RSO check that signage remains visible and current {D('monthly')}. Obscured or missing required signage is restored the same shift.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that imaging QA and radiation-safety programmes are resourced and aligned with organisation safety.

Imaging / Radiology In-Charge
- Owns QA schedules, protocol review, appropriateness system, peer review, clinico-radiological meetings, CAPA log, screening SOPs, training and signage checks.

Radiation Safety Officer (RSO)
- Implements AERB-aligned radiation-safety and ALARA; manages TLD and protective-device testing; supports stop-work on device or screening failures.

Radiographers / technologists
- Perform equipment QA tests as assigned; apply protocols and ALARA; complete screening; use monitoring devices; stop when screening or devices fail.

Reporting doctors
- Participate in peer review and clinico-radiological meetings; support appropriateness decisions.

Ancillary imaging staff
- Follow imaging safety training (MRI safety, falls, tubes); respect signage and controlled areas.

Treating doctors
- Respond to appropriateness queries; provide clinical indication quality that supports ALARA.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA to closure."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Equipment QA tests performed as scheduled; nuclear medicine/radiotherapy QA per AERB where applicable.
- Protocol review records and dose-optimisation notes.
- Appropriateness modification log and audit findings.
- CT/MRI peer review meeting minimum one percent sample with discrepancy grading and CAPA.
- Clinico-radiological meeting minutes.
- CAPA log currency for QA and radiation-safety deviations.
- ALARA evidence (protocol settings; avoidance of unjustified routine films).
- Screening documentation completeness; consent linkage to PRE where required.
- TLD issue/return; apron/shield inventory; periodic device-test images and CAPA.
- Training records for imaging and ancillary staff; signage check log.

Root-cause analysis is required when the same safety or QA defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner after a radiation incident, failed device cluster or major modality change."""

TRAINING_ACKNOWLEDGEMENT = f"""All imaging staff, RSO, ancillary staff posted in imaging and doctors who request or report imaging are trained on this policy at induction and {D('once a year')} after that. Training covers QA tests, appropriateness, peer review, ALARA, screening, device use and testing, stop-work and signage.

Staff acknowledgement

I have read this Imaging Quality Assurance and Safety Programme policy of {HOSPITAL}. I will follow the QA, ALARA, screening, device and stop-work processes described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('HCO/AAC/POL/09')}
Issue number: {D('01')}
Version: {VERSION} (HCO AAC v2 draft — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Imaging In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.9 (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Atomic Energy (Radiation Protection) Rules, 2004 — radiation protection, monitoring and related duties for imaging.
- AERB guidelines — equipment QA, nuclear medicine, radiotherapy and radiation-safety practice.
- Internal documents of {HOSPITAL}: imaging QA schedules and phantom/test records; protocol review file; appropriateness log; CT/MRI peer-review records; clinico-radiological minutes; CAPA log; radiation-safety manual; screening forms; TLD and lead-apron test records; training records; signage checklist; PRE consent procedures."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: imaging/radiology; RSO; emergency; intensive-care areas if present; operation theatre / ERCP rooms with imaging; nursing administration.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
AERB — Atomic Energy Regulatory Board
ALARA — As Low As Reasonably Achievable
CAPA — corrective and preventive action
CT — computed tomography
HCO — Hospital (Full Accreditation programme)
MRI — magnetic resonance imaging
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PET — positron emission tomography
PRE — Patient Rights and Education
QA — quality assurance
RSO — Radiation Safety Officer
SPECT — single-photon emission computed tomography
TLD — thermo-luminescent dosimeter"""

STATUTE_CLAUSE = (
    "the Atomic Energy (Radiation Protection) Rules, 2004, insofar as radiation "
    "protection, monitoring devices and related imaging safety duties arise under those rules"
)
DISCLAIMER, _ = make_hco_disclaimer_statute(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "AAC.9.a",
        "requirement": "The quality assurance programme for imaging services is implemented.",
        "steps": "Section 3; 5.1 Quality assurance programme for imaging",
        "responsible": "Imaging In-Charge and RSO (run QA); Quality Coordinator (audit)",
        "records": [
            "QA programme document covering equipment, protocols, surveillance and safety.",
            "Equipment test records (field congruence, output, phantoms, etc. as applicable).",
            "Protocol review records; nuclear medicine/radiotherapy QA per AERB where applicable.",
        ],
    },
    {
        "oe_code": "AAC.9.b",
        "requirement": "A system is in place to ensure the appropriateness of the investigations and procedures for the clinical indication.",
        "steps": "Section 3; 5.2 Appropriateness of investigations and procedures; Section 4 item 1",
        "responsible": "Imaging In-Charge / reporting doctor (screen orders); treating doctor (consult)",
        "records": [
            "Appropriateness screening method / checklist.",
            "Log of modified investigations after consultation.",
            "Internal audit notes on effectiveness discussed in clinico-radiological meetings.",
        ],
    },
    {
        "oe_code": "AAC.9.c",
        "requirement": "The programme addresses periodic internal / external peer review of imaging results using appropriate sampling.",
        "steps": "Section 3; 5.3 Peer review of CT and MRI results; Section 4 item 2",
        "responsible": "Imaging In-Charge / HOD (organise); peer reviewers (blind review); Quality Coordinator (track)",
        "records": [
            "Defined sample size and periodicity (minimum one percent) for CT and MRI.",
            "Blinded peer-review records with discrepancy grading.",
            "Discrepancy meeting notes and related CAPA.",
        ],
    },
    {
        "oe_code": "AAC.9.d",
        "requirement": "The programme addresses the clinico-radiological meeting(s).",
        "steps": "Section 3; 5.4 Clinico-radiological meetings",
        "responsible": "Imaging In-Charge (convene); referring clinicians (participate)",
        "records": [
            "Meeting schedule at pre-defined intervals.",
            "Minutes covering CT/MRI correlation with clinicians.",
            "Follow-up actions for quality improvement.",
        ],
    },
    {
        "oe_code": "AAC.9.e",
        "requirement": "The programme includes the documentation of corrective and preventive actions.",
        "steps": "Section 3; 5.5 Corrective and preventive action documentation; Section 4 item 3",
        "responsible": "Imaging In-Charge (log CAPA); Quality Coordinator (closure tracking)",
        "records": [
            "CAPA log for QA and radiation-safety deviations.",
            "Root-cause notes and assigned owners with due dates.",
            "Closure evidence and escalation of overdue CAPA.",
        ],
    },
    {
        "oe_code": "AAC.9.f",
        "requirement": "The radiation-safety programme is implemented.",
        "steps": "Section 3; 5.6 Radiation-safety programme; Section 4 item 4",
        "responsible": "RSO (implement ALARA/AERB); Imaging In-Charge (protocols); Medical Superintendent (alignment)",
        "records": [
            "Radiation-safety programme document aligned with organisation safety.",
            "ALARA protocol examples and unjustified-exposure avoidance notes.",
            "Nuclear medicine / radiation-oncology AERB precaution records where applicable.",
        ],
    },
    {
        "oe_code": "AAC.9.g",
        "requirement": "Patients are appropriately screened for safety / risk before imaging.",
        "steps": "Section 3; 5.7 Patient screening before imaging; Section 4 items 5–6; Section 6 Stop-work",
        "responsible": "Radiographers/technologists (screen); reporting doctor (review uncertain pregnancy); PRE process (consent)",
        "records": [
            "Documented pregnancy screening for radiation in child-bearing age.",
            "Documented MRI magnetic-substance screening for patients and attendants entering the area.",
            "Consent records for contrast, sedation, interventional and higher-risk findings (PRE).",
        ],
    },
    {
        "oe_code": "AAC.9.h",
        "requirement": "Imaging personnel and patients use appropriate radiation-safety and monitoring devices where applicable.",
        "steps": "Section 3; 5.8 Use of radiation-safety and monitoring devices; Section 4 item 7",
        "responsible": "RSO (issue devices); imaging personnel (wear/use); Imaging In-Charge (adequacy)",
        "records": [
            "Apron and shield inventory adequate for all workers.",
            "TLD badge issue and wear records for staff working with radiation sources.",
            "Observation/audit notes on shielding of patients and attendants.",
        ],
    },
    {
        "oe_code": "AAC.9.i",
        "requirement": "Radiation-safety and monitoring devices are periodically tested, and results are documented.",
        "steps": "Section 3; 5.9 Periodic testing of radiation-safety and monitoring devices; Section 4 item 8; Section 6 Stop-work",
        "responsible": "RSO (test and document); Imaging In-Charge (remove failed devices)",
        "records": [
            "Periodic lead-apron/shield test images and results.",
            "TLD replacement records per AERB-recommended frequency.",
            "CAPA and removal-from-use records for failed devices.",
        ],
    },
    {
        "oe_code": "AAC.9.j",
        "requirement": "Imaging and ancillary personnel are trained in imaging safety practices and radiation-safety measures.",
        "steps": "Section 3; 5.10 Training in imaging and radiation safety",
        "responsible": "Imaging In-Charge (train); ancillary supervisors (ensure attendance)",
        "records": [
            "Induction and annual training records for imaging and ancillary staff.",
            "Training content covering MRI safety, tubes, falls, patient handling and radiation safety.",
            "Attendance lists for helpers, housekeeping, security and nurses posted in imaging.",
        ],
    },
    {
        "oe_code": "AAC.9.k",
        "requirement": "Imaging signage is prominently displayed in all appropriate locations.",
        "steps": "Section 3; 5.11 Imaging signage; Section 4 item 9",
        "responsible": "Imaging In-Charge and RSO (maintain displays)",
        "records": [
            "Signage location checklist including procedure rooms and OTs with imaging.",
            "Monthly signage visibility check log.",
            "Regulatory display evidence as required by authorities.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.9 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Asterisked: a,e,f,i. Achievement: b,c. Excellence: d. Eleven OEs, eleven What-we-do subsections. Stop-work owns screening/device gates (moved from AAC.8). Pregnancy hold-for-review is hospital safety practice, not an NABH OE requirement. P2: Atomic Energy (Radiation Protection) Rules, 2004."""


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
        "prepared_by": D("Imaging In-Charge"),
        "stop_work": STOP_WORK,
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Imaging quality assurance, ALARA and radiation safety.",
        "doc_no": D("HCO/AAC/POL/09"),
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.9",
    }
    emit_pre_v2(
        draft,
        "hco_aac9_v2_draft.json",
        "HCO.AAC.9_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
        edition_label=HCO_EDITION_LABEL,
        drafts_dir=HCO_DRAFTS,
        preview_dir=HCO_PREVIEW,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
