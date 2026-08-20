# -*- coding: utf-8 -*-
"""HCO AAC.8 v2 — imaging services (Full Accreditation 6th Edition).

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer.
Content from NABH HCO 6th Edition PDF (md5 2c4489ee98de4ae9b49cba168ea9f42a),
OCR policies/source/hco6_aac_ocr.txt PDF idxs ~79–82. No SHCO AAC wording.
Stop-work: do not scan without required safety/pregnancy/MRI screening / legal
compliance checks. Disclaimer P2: AERB Rules 2004 + PC-PNDT Act 1994.
"""
from __future__ import annotations

import sys

from hco_v2_disclaimer import make_hco_disclaimer_statute
from pre_v2_common import BLANK, D, HOSPITAL, HCO_EDITION_LABEL, emit_pre_v2

STANDARD_CODE = "AAC.8"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.8.a", "AAC.8.b", "AAC.8.c", "AAC.8.d", "AAC.8.e",
    "AAC.8.f", "AAC.8.g", "AAC.8.h", "AAC.8.i",
]
POLICY_TITLE = "Imaging Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": "HCO AAC.8 v2: imaging a–i from 6th Edition OCR; AERB/PC-PNDT P2; stop-work for legal/safety checks.",
    },
]

STATEMENT_OF_INTENT = (
    "Imaging services are provided as per the scope of services of the organisation — "
    "complying with legal requirements, available when clinical care needs them, "
    "reported on time, and quality-assured when outsourced."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides imaging services that comply with legal requirements (including Atomic Energy Regulatory Board (AERB) clearance and Pre-Conception and Pre-Natal Diagnostic Techniques (PC-PNDT) duties), keeps scope, infrastructure and human resources commensurate with clinical services, uses qualified personnel to perform, supervise and interpret investigations, delivers results within defined turnaround time (TAT) while monitoring waiting, performance and report times, intimates critical results within one hour with read-back, reports in a standardised manner (including teleradiology naming), recalls or amends reports when needed, and outsources unavailable tests under a quality-assured MoU.

The chapter intent is that imaging services are reliable, timely, legally compliant and continuous with patient care.

This policy owns imaging service delivery (AAC.8). AAC.9 owns imaging quality assurance and radiation/imaging safety programmes (screening, ALARA, device testing, signage). AAC.3.c and ROM.6.e own safe transfer/referral and MoU quality content referenced for outsourcing. PRE owns informed consent method for contrast, sedation and interventional procedures when those consents are required under AAC.9.

TAT — turnaround time. RSO — Radiation Safety Officer. Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies to the imaging/radiology in-charge, Radiation Safety Officer (RSO), radiographers and technologists, reporting doctors (including teleradiology reporters), treating doctors who request imaging, nurses who accompany patients, and the Quality Coordinator at {HOSPITAL}.

It covers the nine objective elements AAC.8.a–i: legal compliance; scope; infrastructure and human resources (with round-the-clock availability / safe transfer when outsourced); qualified performance, supervision and interpretation; TAT with time monitoring; critical results; standardised reporting; recall/amendment; outsourcing with MoU.

Boundaries:

- AAC.9 owns the imaging QA programme, radiation-safety programme, patient screening before imaging, radiation-safety devices, training and signage. This policy owns legal licences, service scope, TAT, critical intimation, reporting format and outsourcing MoUs.
- AAC.3.c owns appropriateness of accompanying staff during transfer; safe transfer of patients to outsourced imaging is required here as part of availability.
- ROM.6.e owns MoU quality content; this policy requires an MoU incorporating quality assurance for imaging outsourcing.
- Spell out: turnaround time (TAT), Atomic Energy Regulatory Board (AERB), Pre-Conception and Pre-Natal Diagnostic Techniques (PC-PNDT), Radiation Safety Officer (RSO), Radiology Information System (RIS), Hospital Information System (HIS), Memorandum of Understanding (MoU)."""

POLICY_STATEMENT = f"""{HOSPITAL} provides imaging services that comply with legal and other requirements, including AERB clearance, dosimeters, lead shields and aprons, PC-PNDT displays and reports, and a Radiation Safety Officer of appropriate level. Scope, infrastructure and human resources are commensurate with clinical services; imaging is available round the clock, with safe transfer and timely reports when a modality is outsourced. Qualified and trained personnel perform, supervise and interpret investigations. Results are available within defined TAT with monitoring of waiting, performance and report times. Critical results are intimated immediately and not later than one hour with documented read-back. Reports follow a standardised format including teleradiology naming. There is a mechanism to recall or amend reports. Tests not available in-house are outsourced only under a quality-assured MoU.

{HOSPITAL} does not operate radiation imaging without current legal compliance, and does not delay a critical imaging result beyond one hour after the report is ready."""

NON_NEGOTIABLES = f"""1. Do not operate radiation-emitting imaging equipment without current AERB clearance and a named Radiation Safety Officer of appropriate level.
2. Do not operate ultrasound used for prenatal diagnosis without current PC-PNDT registration, required displays and reports to the competent authority.
3. Do not report an imaging examination without qualified interpretation as required for the modality.
4. Do not leave a critical imaging result uncommunicated beyond one hour after the report is ready.
5. Do not alter or modify content of an outsourced imaging report.
6. Do not outsource imaging to a provider that has no documented quality assurance system and no MoU with this hospital.
7. Do not leave a recalled report in clinical areas, the medical record, RIS or HIS after recall without replacement by the amended report.
8. Do not proceed with imaging when required legal compliance checks for the modality are missing — stop-work applies.
9. Staff who see an imaging service rule broken report it the same shift to the {D('Imaging In-Charge')}, the {D('Radiation Safety Officer')} or the {D('Medical Superintendent')}."""

STOP_WORK = f"""Do not scan or expose a patient when required legal compliance for the modality is missing — AERB clearance and RSO cover for radiation equipment; PC-PNDT registration and displays for covered ultrasound.

Do not proceed with radiation or MRI examinations when the safety/pregnancy/MRI screening required under AAC.9 has not been completed for the patient (and attendant entering the area). Complete screening before exposure.

Do not use radiation-emitting equipment when mandatory personnel monitoring (dosimeter/TLD) or required lead protection for the examination is unavailable.

Stop-work applies to the imaging examination, not to emergency clinical stabilisation outside the imaging room.

The person who stops tells the {D('Imaging In-Charge')} or the {D('Radiation Safety Officer')} the same shift, and the {D('Medical Superintendent')} if legal clearance is the barrier. Refusing to scan without required checks is not a disciplinary matter."""

PROCEDURE_STEPS = [
f"""5.1 Legal and other requirements

Imaging services comply with legal and other requirements. The organisation is aware of legal and other requirements for imaging, documents them for information and compliance, and maintains and updates compliance status regularly.

Statutory requirements met include: Atomic Energy Regulatory Board (AERB) clearance; dosimeters; lead shields; lead aprons; signage; display as per the Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994; reports to the competent authority; and a Radiation Safety Officer (RSO) of appropriate level.

The imaging in-charge and RSO maintain a register of licences, registrations, RSO appointment and renewal dates. Renewal is initiated {D('60 days before expiry')}. Equipment is not used when clearance has lapsed — stop-work applies.""",

f"""5.2 Scope of imaging services

Scope of the imaging services is commensurate with the services provided by the organisation. Example from the standard: an organisation providing neurosurgery services including head injuries shall have facilities for CT (Computed Tomography) scan.

Imaging may be provided within the organisation, outsourced, or both. The key aspects ensured are safe transfer of the patient and imaging reports available on time. Services are available round the clock so that patient care is not disrupted. Imaging modalities required for emergency management are preferably available within the premises.

The imaging in-charge maintains a service menu of in-house and outsourced modalities, reviewed {D('annually')} and whenever clinical services change.""",

f"""5.3 Infrastructure and human resources

The infrastructure (physical and equipment) and human resources are adequate to provide for the defined scope of services. Imaging has adequate space and equipment; reports must not be delayed for lack of equipment or human resources, including personnel authorised to report results.

Round-the-clock availability is organised by roster for in-house modalities and by documented safe-transfer and turnaround arrangements for outsourced emergency modalities (see section 5.9). Equipment inventory lists model, serial number, installation date and maintenance links held under AAC.9.

Staffing and authorised reporters are reviewed {D('annually')} against workload.""",

f"""5.4 Qualified performance, supervision and interpretation

Qualified and trained personnel perform, supervise and interpret the investigations. AERB guidelines are used as a reference document for radiation-based imaging.

The imaging in-charge keeps competency records for radiographers/technologists and the list of doctors authorised to interpret and report each modality, including teleradiology reporters. Unauthorised staff do not release reports.""",

f"""5.5 Results within defined turnaround time

Imaging results are available within a defined time frame. The organisation documents TAT of imaging results for all modalities and monitors waiting times, time taken to perform the tests, and time taken to prepare the reports for all modalities — for in-patient, out-patient and emergency.

Defined timeframes may differ by test and are decided on nature, modality, criticality and urgency required by the treating doctor. Default categories unless the menu states otherwise:

- Emergency / stat imaging: {D('within one hour of examination completion for the report')}.
- Urgent in-patient imaging: {D('within four hours')}.
- Routine out-patient imaging: {D('same day or next morning as defined per modality')}.

The imaging in-charge reviews waiting/perform/report-time data {D('monthly')}.""",

f"""5.6 Critical imaging results

Critical results are intimated immediately to the personnel concerned. The organisation defines and documents critical results that require immediate attention for patient management for each modality (for example ectopic pregnancy). Critical results of outsourced investigations are also intimated.

Critical results are communicated to a person from the treating team (treating doctor, doctor member of the treating team, or ward nurse) at the earliest, and not later than one hour after completion of the test or the report being ready. The imaging services in-charge identifies suitable personnel to report critical results.

The intimation includes: name of the patient; unique ID; date and time of imaging; investigation name and result; identity of who communicated; identity of the recipient; read-back; and date and time of acknowledgement. This is documented. System-generated critical-result reporting may supplement physical reporting in electronic systems.""",

f"""5.7 Standardised reporting

Results are reported in a standardised manner. At a minimum the report includes: the name of the organisation (or outsourced imaging centre); the patient’s name; the unique identification number; and the name and signature of the person reporting the result.

For teleradiology, the report includes the name of the reporting doctor and a remark to that effect, and the name of the reporting organisation if outsourced to an organisation. All reports from an outsourced imaging centre incorporate these features; the hospital does not alter or modify anything in the report. The report is written in the prevailing clinical context, taking into account clinical details and results of any previous imaging.""",

f"""5.8 Recall and amendment of reports

There is a mechanism to address the recall or amendment of reports whenever applicable. Recall may address errors at all levels. When a report is recalled, withdrawal from clinical areas, medical records, RIS and HIS is ensured. If already issued to the patient, the amended report is made available with a caution to ignore the earlier one. The same is documented. Placement of the corrected report in all those areas is evidenced. Corrective and preventive action is implemented as appropriate based on detailed analysis, coordinated with AAC.9 CAPA where the cause is a quality-system failure.""",

f"""5.9 Outsourced imaging tests

Imaging tests not available in the organisation are outsourced to organisation(s) based on their quality assurance system.

Written guidance includes: list of tests for outsourcing; identity of personnel in outsourced facilities to ensure safe transportation of patients and completion of imaging results; manner of identification of patients and test requisition details; methodology to check selection and performance of the outsourced facility; reporting of critical results; TAT for emergency and routine requests; and prioritisation for urgent investigations.

The organisation has an MoU/agreement that incorporates quality assurance and the requirements of this standard. Refer to AAC.3.c (accompanying staff / safe transfer) and ROM.6.e (MoU quality). The panel and MoUs are reviewed {D('annually')}.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Accountable that imaging services are legally compliant, available as scoped, and meet TAT and critical-result duties.

Imaging / Radiology In-Charge
- Maintains service menu, licence register (with RSO), staffing, TAT definitions, critical-result list, report format, recall mechanism and outsourced panel with MoUs.

Radiation Safety Officer (RSO)
- Holds AERB-facing compliance for radiation equipment, dosimetry and related statutory duties under this policy’s legal section; coordinates with AAC.9 radiation-safety programme.

Radiographers / technologists
- Perform examinations they are trained for; monitor times; communicate critical results when designated; do not alter outsourced reports.

Reporting doctors (including teleradiology)
- Interpret and report within authorisation; support recall/amendment.

Treating doctors and accompanying nurses
- Request appropriately; complete transfer safely when imaging is off-site; receive critical-result intimation with read-back.

Quality Coordinator
- Audits this policy {D('quarterly')}; tracks CAPA when TAT, critical-result or legal-compliance defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- AERB clearance, PC-PNDT registration, RSO appointment and dosimeter/lead-protection status current.
- Service menu commensurate with clinical services; round-the-clock arrangements documented.
- Infrastructure and staffing adequate; authorised reporters listed.
- Waiting, performance and report-time monitoring against defined TAT.
- Critical-result communication within one hour with read-back documentation.
- Standardised reports including teleradiology naming; no alteration of outsourced content.
- Recall/amendment log complete with RIS/HIS withdrawal evidence.
- Outsourced MoUs current and quality-based.

Root-cause analysis is required when the same imaging service defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when modalities, legal registrations or outsourcing arrangements change."""

TRAINING_ACKNOWLEDGEMENT = f"""All imaging staff, RSO, nurses who accompany patients to imaging and doctors who request or report imaging are trained on this policy at induction and {D('once a year')} after that. Training covers legal compliance triggers for stop-work, TAT monitoring, critical-result intimation with read-back, standardised reporting, recall/amendment and outsourcing rules.

Staff acknowledgement

I have read this Imaging Services policy of {HOSPITAL}. I will follow the legal-compliance, TAT, critical-result, reporting, recall and outsourcing processes described, including stop-work.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('HCO/AAC/POL/08')}
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

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.8 (PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Atomic Energy (Radiation Protection) Rules, 2004 — licensing, radiation protection and related duties for radiation-emitting imaging.
- Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994 — registration, display and reporting for covered prenatal diagnostic imaging.
- AERB guidelines — reference for radiation-based imaging practice (AAC.8.d).
- Internal documents of {HOSPITAL}: imaging service menu; licence and RSO register; critical-result list; TAT and time-monitoring records; recall/amendment log; outsourced imaging MoUs (AAC.3.c, ROM.6.e)."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: imaging/radiology; RSO; emergency; every in-patient ward; out-patient; nursing administration; intensive-care areas if present.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
AERB — Atomic Energy Regulatory Board
CAPA — corrective and preventive action
CT — computed tomography
HCO — Hospital (Full Accreditation programme)
HIS — Hospital Information System
MoU — Memorandum of Understanding
MRI — magnetic resonance imaging
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
PC-PNDT — Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994
PRE — Patient Rights and Education
RIS — Radiology Information System
ROM — Responsibilities of Management
RSO — Radiation Safety Officer
TAT — turnaround time
TLD — thermo-luminescent dosimeter"""

STATUTE_CLAUSE = (
    "the Atomic Energy (Radiation Protection) Rules, 2004, and the "
    "Pre-Conception and Pre-Natal Diagnostic Techniques (Prohibition of Sex Selection) Act, 1994"
)
DISCLAIMER, _ = make_hco_disclaimer_statute(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "AAC.8.a",
        "requirement": "Imaging services comply with legal and other requirements.",
        "steps": "Section 3; 5.1 Legal and other requirements; Section 4 items 1–2, 8; Section 6 Stop-work",
        "responsible": "Imaging In-Charge and RSO (maintain compliance); Medical Superintendent (accountable)",
        "records": [
            "Register of AERB clearances, dosimeters, lead protection and RSO appointment.",
            "PC-PNDT registration, displays and reports to competent authority where applicable.",
            "Periodic update of legal-compliance status.",
        ],
    },
    {
        "oe_code": "AAC.8.b",
        "requirement": "Scope of the imaging services is commensurate to the services provided by the organisation.",
        "steps": "Section 3; 5.2 Scope of imaging services",
        "responsible": "Imaging In-Charge (maintain menu); Medical Superintendent (approve)",
        "records": [
            "Imaging service menu listing in-house and outsourced modalities.",
            "Annual review of menu against clinical services.",
            "Round-the-clock availability / safe-transfer arrangement note.",
        ],
    },
    {
        "oe_code": "AAC.8.c",
        "requirement": "The infrastructure (physical and equipment) and human resources are adequate to provide for its defined scope of services.",
        "steps": "Section 3; 5.3 Infrastructure and human resources",
        "responsible": "Imaging In-Charge (manage); Medical Superintendent (resource)",
        "records": [
            "Equipment inventory linked to maintenance/QA under AAC.9.",
            "Staff and authorised-reporter list with shift cover.",
            "Annual adequacy review of space, equipment and human resources.",
        ],
    },
    {
        "oe_code": "AAC.8.d",
        "requirement": "Qualified and trained personnel perform, supervise and interpret the investigations.",
        "steps": "Section 3; 5.4 Qualified performance, supervision and interpretation; Section 4 item 3",
        "responsible": "Imaging In-Charge (competency records); reporting doctors (interpret); radiographers (perform)",
        "records": [
            "Qualification and training records for imaging personnel.",
            "List of doctors authorised to interpret/report by modality (including teleradiology).",
            "Note of AERB guidance used as reference for radiation-based imaging.",
        ],
    },
    {
        "oe_code": "AAC.8.e",
        "requirement": "Imaging results are available within a defined time frame.",
        "steps": "Section 3; 5.5 Results within defined turnaround time",
        "responsible": "Imaging In-Charge (define and monitor); Quality Coordinator (audit)",
        "records": [
            "Defined TAT for all modalities.",
            "Monitoring records of waiting, performance and report times for IP/OP/emergency.",
            "Monthly TAT exception/escalation records.",
        ],
    },
    {
        "oe_code": "AAC.8.f",
        "requirement": "Critical results are intimated immediately to the personnel concerned.",
        "steps": "Section 3; 5.6 Critical imaging results; Section 4 item 4",
        "responsible": "Designated imaging personnel (intimate); treating team (read-back); Imaging In-Charge (critical list)",
        "records": [
            "Documented critical-result definitions per modality.",
            "Critical-result communication log with patient ID, result, caller, recipient, read-back, date and time.",
            "List of personnel authorised to report critical imaging results.",
        ],
    },
    {
        "oe_code": "AAC.8.g",
        "requirement": "Results are reported in a standardised manner.",
        "steps": "Section 3; 5.7 Standardised reporting; Section 4 item 5",
        "responsible": "Imaging In-Charge (format); reporting doctor (sign); staff (no alteration of outsourced content)",
        "records": [
            "Standardised report template with minimum required fields.",
            "Teleradiology reports naming reporting doctor and organisation as required.",
            "Audit finding that outsourced report content was not altered.",
        ],
    },
    {
        "oe_code": "AAC.8.h",
        "requirement": "There is a mechanism to address the recall / amendment of reports whenever applicable.",
        "steps": "Section 3; 5.8 Recall and amendment of reports; Section 4 item 7",
        "responsible": "Imaging In-Charge (run mechanism); Quality Coordinator (CAPA)",
        "records": [
            "Recall/amendment log with reason and date.",
            "Evidence of withdrawal from clinical areas, medical records, RIS and HIS.",
            "Amended report issued to patient with caution where previously issued; CAPA record.",
        ],
    },
    {
        "oe_code": "AAC.8.i",
        "requirement": "Imaging tests not available in the organisation are outsourced to organisation(s) based on their quality assurance system.",
        "steps": "Section 3; 5.9 Outsourced imaging tests; Section 4 item 6",
        "responsible": "Imaging In-Charge (panel and MoU); Medical Superintendent (approve MoU)",
        "records": [
            "Written outsourcing guidance including critical-result and TAT/prioritisation rules.",
            "Current MoU/agreement incorporating quality assurance (AAC.3.c, ROM.6.e).",
            "Annual review of outsourced imaging performance.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.8 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Core: a. Asterisked: e,f,h. Nine OEs, nine What-we-do subsections. Stop-work present. P2: Atomic Energy (Radiation Protection) Rules, 2004 and PC-PNDT Act 1994."""


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
        "stop_work": STOP_WORK,
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Imaging services, legal compliance and turnaround time.",
        "doc_no": D("HCO/AAC/POL/08"),
    }
    emit_pre_v2(
        draft,
        "hco_aac8_v2_draft.json",
        "HCO.AAC.8_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
