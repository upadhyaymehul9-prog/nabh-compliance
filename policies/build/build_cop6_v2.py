# -*- coding: utf-8 -*-
"""COP.6 v2 — intensive care and high dependency units.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF index 70.
No stop-work section. Six OEs (COP.6.a–f).
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.6"
CHAPTER = "COP"
OE_CODES = [
    "COP.6.a", "COP.6.b", "COP.6.c", "COP.6.d", "COP.6.e", "COP.6.f",
]
POLICY_TITLE = "Intensive Care and High Dependency Units"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, no stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Care in the intensive care and high dependency units is provided in a systematic "
    "manner — not an ICU that admits without criteria or discharges without a plan."
)

PURPOSE = f"""This policy defines how {HOSPITAL} provides care in its intensive care and high dependency units in a systematic manner.

It covers six elements: defined admission and discharge criteria with procedures for bed shortages; care based on written guidance by adequately available staff and equipment; documented infection control practices; a quality-assurance programme; a mechanism to counsel the patient and/or family periodically; and end of life care in consonance with legal requirements.

Boundaries: HIC owns the hospital-wide infection-control programme; this policy owns ICU/HDU-specific infection control practices. COP.2 owns emergency clinical care; this policy owns ICU/HDU care after admission.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff working in the intensive care unit (ICU) and high dependency unit (HDU) of {HOSPITAL}: intensivists or treating doctors, ICU/HDU nurses, physiotherapists, and support staff.

It covers the six elements COP.6.a–f name. It does not cover the hospital-wide infection-control programme (HIC), emergency clinical care (COP.2), or general ward care.

Boundaries with other policies of {HOSPITAL}:

- HIC owns the hospital-wide infection-control programme. This policy owns that infection control practices specific to ICU/HDU are documented and followed.
- COP.2 owns emergency clinical care. This policy owns care within ICU/HDU after admission.
- PRE.3 owns informed consent. This policy owns periodic counselling of patient and/or family in the ICU/HDU context.
- COP.13 owns pain management. This policy owns that pain is managed in ICU/HDU as part of systematic care."""

POLICY_STATEMENT = f"""{HOSPITAL} defines admission and discharge criteria for its ICU and HDU. These criteria are implemented. When beds are not available, defined procedures for bed shortages are followed, including prioritisation and escalation.

Care in ICU and HDU is based on written guidance. Staff are adequately available and competent. Equipment is appropriate for the level of care. The nurse-to-patient ratio is {D('1:1 in ICU and 1:2 in HDU or as defined by the hospital')}.

Infection control practices in ICU and HDU are documented and followed, including {D('hand hygiene compliance, ventilator bundle, central-line bundle, catheter-care bundle, and antibiotic stewardship')}. Compliance is monitored and findings are acted upon.

{HOSPITAL} implements a quality-assurance programme for ICU and HDU that includes {D('monitoring of ventilator-associated events, central-line-associated bloodstream infections, catheter-associated urinary tract infections, ICU length of stay, and unplanned readmissions within 48 hours')}.

{HOSPITAL} has a mechanism to counsel the patient and/or family periodically about the patient's condition, prognosis, treatment plan, and care decisions.

End of life care is provided in a consistent manner and in consonance with legal requirements. Decisions about withholding or withdrawing life-sustaining treatment follow written guidance and applicable law.

{HOSPITAL} does not treat any of these as meeting this policy: admitting to ICU without meeting admission criteria; discharging without meeting discharge criteria; an ICU without documented infection control bundles; or counselling the family once on admission and never again."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no staffing convenience exception.

1. Admitting a patient to ICU or HDU who does not meet the defined admission criteria, or retaining a patient who meets discharge criteria without documented clinical justification.
2. Operating ICU or HDU without the defined minimum nurse-to-patient ratio without immediate escalation to the {D('ICU in-charge or Medical Superintendent')}.
3. Failing to document and follow infection control practices, including the defined care bundles.
4. Failing to counsel the patient and/or family at least {D('once daily and on any significant change')} in condition.
5. Making a decision about withholding or withdrawing life-sustaining treatment without documented clinical justification, family discussion, and compliance with applicable law.

Staff who see one of these acts report it the same shift to the {D('ICU in-charge')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Admission and discharge criteria and bed-shortage procedures

{HOSPITAL} defines admission and discharge criteria for ICU and HDU. Criteria are based on {D('physiological parameters, diagnosis, and level of care required')}. Criteria are reviewed {D('annually')} by the {D('ICU in-charge in consultation with treating doctors')}.

Admission is documented with the criteria met. Discharge is documented with criteria met and a discharge or step-down plan. Patients are not retained in ICU or HDU when they meet discharge criteria unless a documented clinical reason exists.

When ICU or HDU beds are not available, the bed-shortage procedure is followed: {D('prioritisation by clinical severity, discussion with the treating doctor and the ICU in-charge, documentation of the decision, and escalation to the Medical Superintendent when needed')}.""",

f"""5.2 Care based on written guidance with adequate staff and equipment

Care in ICU and HDU is based on written guidance that covers {D('admission assessment, ongoing monitoring, ventilator management, sedation protocols, nutrition, fluid balance, and daily goals of care')}.

Staff are available in numbers adequate for the level of care. The nurse-to-patient ratio is {D('1:1 in ICU and 1:2 in HDU')}. A doctor is available {D('24 hours')} for ICU/HDU patients. Equipment is checked {D('at the start of each shift')} using a documented checklist.

Written guidance is reviewed {D('annually')} and updated when evidence or practice changes.""",

f"""5.3 Infection control practices documented and followed

Infection control practices specific to ICU and HDU are documented and followed. Practices include: {D('hand hygiene compliance monitoring, ventilator-associated pneumonia prevention bundle, central-line-associated bloodstream infection prevention bundle, catheter-associated urinary tract infection prevention bundle, and antibiotic stewardship')}.

Compliance with each bundle is monitored {D('monthly')} by the {D('ICU nurse in-charge')} and reviewed with the infection-control team. Non-compliance is treated as a finding with corrective action.

HIC owns the hospital-wide infection-control programme. This policy owns that ICU/HDU-specific bundles are documented, followed, and monitored.""",

f"""5.4 Quality-assurance programme

{HOSPITAL} implements a quality-assurance programme for ICU and HDU. Indicators include: {D('ventilator-associated event rate, central-line-associated bloodstream infection rate, catheter-associated urinary tract infection rate, ICU length of stay, unplanned readmissions within 48 hours, and ICU mortality')}.

Indicators are collected {D('monthly')} by the {D('ICU nurse in-charge')} and reviewed {D('quarterly')} with the Quality Coordinator and the Medical Superintendent. Trends are identified and improvement actions are tracked to closure.

The programme is reviewed {D('annually')} and benchmarked where possible.""",

f"""5.5 Patient and family counselling

{HOSPITAL} has a mechanism to counsel the patient and/or family periodically. Counselling covers: the patient's current condition, prognosis, treatment plan, care decisions, and expected outcomes.

Counselling occurs at least {D('once daily')} and on any significant change in the patient's condition. The counselling is documented in the patient record, including who was counselled, by whom, and what was communicated.

The {D('treating doctor or ICU in-charge')} leads counselling. A nurse may be present to support.""",

f"""5.6 End of life care

End of life care is provided in a consistent manner and in consonance with legal requirements. When a patient is at the end of life, the treating team discusses goals of care with the patient (where possible) and the family.

Decisions about withholding or withdrawing life-sustaining treatment follow written guidance that includes: {D('documented clinical justification, family discussion and agreement, ethics committee consultation where available, and compliance with applicable law')}. The decision and the discussion are documented in the patient record.

Comfort care, pain management, dignity, and family support are provided. COP.13 owns pain management; this policy owns that end of life care in ICU/HDU is consistent and lawful.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that ICU and HDU care is provided as this policy requires.
- Receives escalations for bed shortages and end of life decisions.

{D('ICU in-charge')}
- Holds admission and discharge criteria, written guidance, bed-shortage procedures, and end of life guidance.
- Reviews quality-assurance programme results quarterly.
- Leads or participates in family counselling.

ICU/HDU doctors
- Deliver care based on written guidance. Order admission and discharge per criteria.
- Lead counselling on prognosis and end of life decisions.

ICU/HDU nurses
- Deliver bedside care following written guidance and infection control bundles.
- Monitor compliance with nurse-to-patient ratios and escalate shortfalls.
- Document counselling sessions.

{D('Quality Coordinator')}
- Audits this policy {D('quarterly')} (see monitoring section).
- Reviews quality-assurance indicators and infection-control compliance.
- Tracks CAPA for ICU/HDU findings."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Admission and discharge criteria implemented and documented (sample charts).
- Bed-shortage procedure followed and documented when triggered.
- Nurse-to-patient ratio maintained and escalations documented.
- Infection control bundles documented and compliance monitored monthly.
- Quality-assurance indicators collected monthly and reviewed quarterly.
- Patient/family counselling documented at least daily and on significant change.
- End of life decisions documented with clinical justification, family discussion, and legal compliance.

Root-cause analysis is required when an ICU/HDU safety event (bundle non-compliance, unplanned readmission, restraint injury) recurs within six months.

This policy is reviewed {D('annually')}, and sooner when ICU/HDU scope changes or evidence-based guidance is updated."""

TRAINING_ACKNOWLEDGEMENT = f"""All ICU/HDU staff are trained on this policy at induction and {D('once a year')} after that. Training covers admission/discharge criteria, written guidance, infection control bundles, quality indicators, family counselling, and end of life care.

Staff acknowledgement

I have read this Intensive Care and High Dependency Units policy of {HOSPITAL}. I will follow admission and discharge criteria, infection control bundles, and end of life guidance as described.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The ICU in-charge holds signed acknowledgements with the training file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/06"),
    version=VERSION,
    prepared_by=D("ICU in-charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.6.
- Internal documents of {HOSPITAL}: ICU/HDU admission and discharge criteria, bed-shortage procedure, infection control bundles, quality-assurance programme indicators, family counselling documentation template, end of life care guidance, COP.13 pain management policy, HIC infection-control programme."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('ICU in-charge')} and the Quality Coordinator.

Copies issued to: ICU; HDU; nursing administration; emergency department (for admission criteria reference).

The current version is available to all ICU/HDU staff at the {D('ICU policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
HDU — high dependency unit
HIC — Hospital Infection Control (NABH SHCO chapter 7)
ICU — intensive care unit
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.6.a",
        "requirement": "The defined admission and discharge criteria for its intensive care and high dependency units are implemented, and defined procedures for the situation of bed shortages are followed.",
        "steps": "Section 3; 5.1 Admission and discharge criteria and bed-shortage procedures; Section 4 item 1",
        "responsible": "ICU in-charge (criteria and procedures); treating doctors (order admission/discharge); nurses (document)",
        "records": [
            "Admission and discharge criteria document reviewed annually.",
            "Sample charts showing admission criteria met and documented.",
            "Discharge or step-down plans documented in the patient record.",
            "Bed-shortage procedure activation and escalation records.",
        ],
    },
    {
        "oe_code": "COP.6.b",
        "requirement": "The care is provided in intensive care and high dependency units based on written guidance by adequately available staff and equipment.",
        "steps": "Section 3; 5.2 Care based on written guidance with adequate staff and equipment; Section 4 item 2",
        "responsible": "ICU in-charge (guidance and staffing); ICU/HDU nurses (deliver and monitor ratios)",
        "records": [
            "Written guidance documents for ICU/HDU care reviewed annually.",
            "Nurse-to-patient ratio records per shift with escalation records when breached.",
            "Equipment checklist completed at the start of each shift.",
        ],
    },
    {
        "oe_code": "COP.6.c",
        "requirement": "Infection control practices are documented and followed.",
        "steps": "Section 3; 5.3 Infection control practices documented and followed; Section 4 item 3",
        "responsible": "ICU nurse in-charge (monitor compliance); infection-control team (review); Quality Coordinator (audit)",
        "records": [
            "Documented infection control bundles for ICU/HDU (VAP, CLABSI, CAUTI).",
            "Monthly compliance monitoring records for each bundle.",
            "Non-compliance findings with corrective action documented.",
            "Antibiotic stewardship records.",
        ],
    },
    {
        "oe_code": "COP.6.d",
        "requirement": "The organization shall implement a quality-assurance programme.",
        "steps": "Section 3; 5.4 Quality-assurance programme",
        "responsible": "ICU nurse in-charge (data collection); Quality Coordinator (review and trends); Medical Superintendent (oversight)",
        "records": [
            "Monthly quality-assurance indicator data for ICU/HDU.",
            "Quarterly review minutes with trends and improvement actions.",
            "Annual programme review and benchmark report.",
        ],
    },
    {
        "oe_code": "COP.6.e",
        "requirement": "The organisation has a mechanism to counsel the patient and/or family periodically.",
        "steps": "Section 3; 5.5 Patient and family counselling; Section 4 item 4",
        "responsible": "Treating doctor or ICU in-charge (lead counselling); nurses (support and document)",
        "records": [
            "Daily counselling entries in the patient record noting who was counselled, by whom, and content.",
            "Counselling documented on significant change in condition.",
            "Sample audit of counselling completeness quarterly.",
        ],
    },
    {
        "oe_code": "COP.6.f",
        "requirement": "End of life care is provided in a consistent manner in the organization, and is in consonance with legal requirements.",
        "steps": "Section 3; 5.6 End of life care; Section 4 item 5",
        "responsible": "Treating team (goals of care discussion); ICU in-charge (guidance); Medical Superintendent (escalation)",
        "records": [
            "End of life care guidance document reviewed annually.",
            "Documented goals-of-care discussions with patient/family in the patient record.",
            "Decisions on withholding/withdrawing treatment with clinical justification and family agreement documented.",
            "Comfort care and pain management documented.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.6 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Organization provides care in the intensive care and high dependency units, in a systematic manner." COP.6.a–f PDF index 70. Asterisked OEs: a, c, d, f. Levels: c Achievement, rest Commitment.

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
        "subtitle": "Systematic care in ICU and high dependency units.",
        "doc_no": D("COP/POL/06"),
    }
    emit_pre_v2(
        draft,
        "cop6_v2_draft.json",
        "COP.6_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
