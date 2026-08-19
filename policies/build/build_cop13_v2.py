# -*- coding: utf-8 -*-
"""COP.13 v2 — pain management, rehabilitation services and nutritional therapy.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 74–75.
No stop-work section. Six OEs (COP.13.a–f).
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.13"
CHAPTER = "COP"
OE_CODES = [
    "COP.13.a", "COP.13.b", "COP.13.c", "COP.13.d", "COP.13.e", "COP.13.f",
]
POLICY_TITLE = "Pain Management, Rehabilitation Services and Nutritional Therapy"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, no stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Pain management, rehabilitation services and nutritional therapy are provided to "
    "the patients in a safe, collaborative and consistent manner — not a pain score "
    "that is documented but never acted upon, rehabilitation that is ordered but never "
    "coordinated, or a diet that arrives without clinical input."
)

PURPOSE = f"""This policy defines how {HOSPITAL} provides pain management, rehabilitation services and nutritional therapy to patients in a safe, collaborative and consistent manner.

It covers six elements: effective management of patients in pain; pain alleviation measures or medications initiated and titrated according to the patient's need and response; rehabilitation services commensurate with services provided; collaborative planning of rehabilitation services; nutritional risk screening and assessment for at-risk patients; and collaborative planning and provision of therapeutic diets.

Boundaries: MOM owns medication management; this policy owns pain-specific medication initiation and titration. COP.4 owns nursing care; this policy owns the pain assessment and nutritional screening that nurses perform. COP.6 owns ICU care; this policy owns pain management and nutritional therapy within ICU.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical staff at {HOSPITAL} involved in pain management, rehabilitation and nutritional therapy: treating doctors, nurses, physiotherapists, occupational therapists, dietitians or nutrition staff, and the {D('Quality Coordinator')}.

It covers the six elements COP.13.a–f name. It does not cover medication management as a system (MOM), nursing care policy (COP.4), or ICU-specific care (COP.6).

Boundaries with other policies of {HOSPITAL}:

- MOM owns medication management. This policy owns initiation and titration of pain alleviation measures or medications.
- COP.4 owns nursing care. This policy owns pain assessment, nutritional screening and diet delivery that nurses perform.
- COP.6 owns ICU care. This policy owns pain management and nutritional therapy within the ICU context.
- COP.12 owns higher-risk patient management. This policy owns nutritional risk screening and therapeutic diet for at-risk patients."""

POLICY_STATEMENT = f"""{HOSPITAL} manages patients in pain effectively. Every patient is assessed for pain using a validated pain assessment tool. Pain is treated promptly and reassessed at defined intervals.

Pain alleviation measures or medications are initiated and titrated according to the patient's need and response. Non-pharmacological measures are considered alongside medications. The patient's response to pain management is documented.

The scope of rehabilitation services at a minimum is commensurate with the services provided by {HOSPITAL}. Where rehabilitation services are not available on site, referral arrangements are documented.

Care providers collaboratively plan rehabilitation services. Rehabilitation goals are set with the patient, documented, and progress is reviewed.

Patients admitted to {HOSPITAL} are screened for nutritional risk. Assessment is done for patients found at risk during nutritional screening. The screening tool is {D('a validated nutritional screening tool such as the Malnutrition Universal Screening Tool (MUST) or Nutritional Risk Screening (NRS-2002)')}.

The therapeutic diet is planned and provided collaboratively by the treating doctor, nursing staff, and dietitian or nutrition-trained staff. Diet orders are documented and communicated to the kitchen.

{HOSPITAL} does not treat any of these as meeting this policy: a pain score documented but not acted upon; rehabilitation ordered without goals or coordination; nutritional screening performed without follow-up assessment for at-risk patients; or a diet order that does not reach the kitchen."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Leaving a patient in pain unassessed or untreated when the patient reports pain or when clinical signs indicate pain.
2. Initiating or titrating pain medication without documenting the patient's response and reassessing at the defined interval.
3. Providing rehabilitation services without documented goals set collaboratively with the patient and the treating team.
4. Failing to screen an admitted patient for nutritional risk using the adopted screening tool.
5. Failing to perform a nutritional assessment for a patient found at risk during nutritional screening.
6. Issuing a therapeutic diet order without communicating it to the kitchen and verifying it reaches the patient.

Staff who see one of these acts report it the same shift to the {D('department in-charge')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Effective pain management

Every patient is assessed for pain using a validated pain assessment tool — {D('the Numeric Rating Scale (NRS) for adults or the Wong-Baker FACES scale for children or cognitively impaired patients')}. Pain assessment is performed at admission, at defined intervals ({D('every 4 hours for in-patients or as clinically indicated')}), and whenever the patient reports pain.

A pain score that triggers action ({D('NRS ≥ 4 or equivalent')}) leads to treatment within the same shift. The treating doctor prescribes pain alleviation measures. The nurse administers and documents.

Pain management covers acute, chronic and procedural pain. The {D('Quality Coordinator')} monitors pain assessment and treatment compliance {D('quarterly')}.""",

f"""5.2 Pain alleviation: initiation and titration

Pain alleviation measures or medications are initiated and titrated according to the patient's need and response. The treating doctor selects the agent and route based on the type and severity of pain, patient condition, and contraindications.

Non-pharmacological measures — {D('positioning, hot/cold application, relaxation techniques, and distraction')} — are considered alongside medications. The patient's response is documented at each reassessment. The dose or agent is adjusted when the response is inadequate or adverse effects occur.

MOM owns medication management as a system; this policy owns that pain-specific initiation and titration follow the patient's response.""",

f"""5.3 Rehabilitation services commensurate with scope

The scope of rehabilitation services at a minimum is commensurate with the services provided by {HOSPITAL}. Rehabilitation includes {D('physiotherapy, occupational therapy, speech therapy, and post-surgical mobilisation as applicable to the hospital service directory')}.

Where a rehabilitation service is not available on site, referral arrangements with an appropriate provider are documented and communicated to the patient.

The {D('rehabilitation in-charge or physiotherapist')} holds the scope document and reviews it {D('annually')} against the hospital's service directory.""",

f"""5.4 Collaborative planning of rehabilitation services

Care providers collaboratively plan rehabilitation services. Rehabilitation goals are set with the patient, documented in the patient record, and reviewed at defined intervals ({D('weekly for in-patients')}).

The rehabilitation plan includes: the clinical indication, specific goals, interventions, frequency, expected duration, and outcome measures. The plan is developed by the {D('physiotherapist or rehabilitation team')} in consultation with the treating doctor.

Progress notes and outcome measures are documented. When goals are met or revised, the change is communicated to the patient and the treating team.""",

f"""5.5 Nutritional risk screening and assessment

Patients admitted to {HOSPITAL} are screened for nutritional risk within {D('24 hours of admission')} using {D('the adopted validated nutritional screening tool')}. Screening is performed by {D('the admitting nurse')}.

Patients found at risk during nutritional screening receive a nutritional assessment by the {D('dietitian or nutrition-trained staff')} within {D('48 hours')}. The assessment covers: current nutritional status, dietary intake, clinical condition, and nutritional requirements.

Nutritional reassessment is performed at {D('defined intervals for patients with a hospital stay exceeding 7 days')} or on clinical change. Results are documented in the patient record.""",

f"""5.6 Therapeutic diet planning and provision

The therapeutic diet is planned and provided collaboratively. The treating doctor orders the diet based on the clinical condition and the nutritional assessment. The {D('dietitian or nutrition-trained staff')} translates the order into a meal plan. The nursing staff communicates the diet order to the kitchen and verifies that the correct diet reaches the patient.

Diet orders are documented in the patient record and updated when the clinical condition changes. The kitchen maintains a diet register that matches the patient record.

Patient and family education on dietary needs is provided before discharge where the therapeutic diet continues at home.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that pain management, rehabilitation services and nutritional therapy are provided as this policy requires.

Treating doctors
- Assess and treat pain. Prescribe pain medications and titrate based on response.
- Order rehabilitation and set goals collaboratively.
- Order therapeutic diets based on clinical condition.

Nurses
- Assess pain using the validated tool at defined intervals and report untreated pain.
- Screen admitted patients for nutritional risk within the defined timeframe.
- Communicate diet orders to the kitchen and verify delivery.

{D('Physiotherapist / rehabilitation team')}
- Develop and implement rehabilitation plans collaboratively.
- Document progress and outcomes.

{D('Dietitian or nutrition-trained staff')}
- Perform nutritional assessments for at-risk patients.
- Plan therapeutic diets collaboratively and provide patient education.

{D('Quality Coordinator')}
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA for pain management, rehabilitation and nutritional therapy findings."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Pain assessment documented at admission and at defined intervals (sample charts).
- Pain treated within the same shift when the score triggers action.
- Pain medication response documented and dose adjusted when needed.
- Rehabilitation goals set collaboratively and progress documented.
- Nutritional risk screening completed within defined timeframe for admitted patients.
- Nutritional assessment completed for at-risk patients within defined timeframe.
- Therapeutic diet orders documented, communicated to kitchen, and verified at bedside.

Root-cause analysis is required when the same pain management gap, rehabilitation coordination failure, or nutritional screening omission recurs within six months.

This policy is reviewed {D('annually')}, and sooner when pain management guidelines, rehabilitation scope, or nutritional standards change."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff are trained on this policy at induction and {D('once a year')} after that. Training covers pain assessment tools, pain medication titration, rehabilitation goal-setting, nutritional risk screening, and therapeutic diet processes.

Staff acknowledgement

I have read this Pain Management, Rehabilitation Services and Nutritional Therapy policy of {HOSPITAL}. I will assess and manage pain, collaborate on rehabilitation planning, screen for nutritional risk, and ensure therapeutic diets are correctly ordered and delivered.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the training file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/13"),
    version=VERSION,
    prepared_by=D("Quality Coordinator"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.13.
- Internal documents of {HOSPITAL}: pain assessment protocol, pain management guidelines, rehabilitation scope document, rehabilitation referral arrangements, nutritional screening tool, nutritional assessment form, therapeutic diet protocol, MOM medication management policy, COP.4 nursing care policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; ICU; emergency department; physiotherapy; dietary/kitchen; nursing administration.

The current version is available to all staff at the {D('ward policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
ICU — intensive care unit
MOM — Management of Medication (NABH SHCO chapter 6)
MUST — Malnutrition Universal Screening Tool
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NRS — Numeric Rating Scale (pain) / Nutritional Risk Screening (nutrition)
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.13.a",
        "requirement": "Patients in pain are effectively managed.",
        "steps": "Section 3; 5.1 Effective pain management; Section 4 items 1–2",
        "responsible": "Treating doctors (prescribe); nurses (assess and administer); Quality Coordinator (monitor compliance)",
        "records": [
            "Pain assessment using validated tool documented at admission and defined intervals.",
            "Treatment initiated within the same shift when pain score triggers action.",
            "Quarterly audit of pain assessment and treatment compliance.",
            "Training records on pain assessment tools.",
        ],
    },
    {
        "oe_code": "COP.13.b",
        "requirement": "Pain alleviation measures or medications are initiated and titrated according to the patient's need and response.",
        "steps": "Section 3; 5.2 Pain alleviation: initiation and titration; Section 4 item 2",
        "responsible": "Treating doctors (select agent and titrate); nurses (administer and document response)",
        "records": [
            "Pain medication orders with clinical justification documented.",
            "Patient response documented at each reassessment.",
            "Dose adjustments or agent changes documented with rationale.",
        ],
    },
    {
        "oe_code": "COP.13.c",
        "requirement": "Scope of rehabilitation services at a minimum is commensurate to the services provided by the organization.",
        "steps": "Section 3; 5.3 Rehabilitation services commensurate with scope",
        "responsible": "Rehabilitation in-charge (scope document); Medical Superintendent (approve scope)",
        "records": [
            "Rehabilitation scope document reviewed annually against service directory.",
            "Referral arrangements documented where services are not available on site.",
            "Service directory showing rehabilitation services available.",
        ],
    },
    {
        "oe_code": "COP.13.d",
        "requirement": "Care providers collaboratively plan rehabilitation services.",
        "steps": "Section 3; 5.4 Collaborative planning of rehabilitation services; Section 4 item 3",
        "responsible": "Physiotherapist/rehabilitation team (develop plan); treating doctor (consultation); patient (goal setting)",
        "records": [
            "Rehabilitation plans with goals set collaboratively documented in the patient record.",
            "Progress notes and outcome measures documented at defined intervals.",
            "Communication records between rehabilitation team and treating doctor.",
        ],
    },
    {
        "oe_code": "COP.13.e",
        "requirement": "Patients admitted to the organization are screened for nutritional risk, and assessment is done for patients found at risk during nutritional screening.",
        "steps": "Section 3; 5.5 Nutritional risk screening and assessment; Section 4 items 4–5",
        "responsible": "Admitting nurse (screen); dietitian or nutrition-trained staff (assess); treating doctor (order)",
        "records": [
            "Nutritional risk screening completed within defined timeframe for admitted patients.",
            "Nutritional assessment completed for at-risk patients within defined timeframe.",
            "Reassessment records for patients with extended stays or clinical change.",
            "Training records on the adopted nutritional screening tool.",
        ],
    },
    {
        "oe_code": "COP.13.f",
        "requirement": "The therapeutic diet is planned and provided collaboratively.",
        "steps": "Section 3; 5.6 Therapeutic diet planning and provision; Section 4 item 6",
        "responsible": "Treating doctor (order); dietitian (meal plan); nurses (communicate to kitchen and verify delivery)",
        "records": [
            "Diet orders documented in patient record and updated on clinical change.",
            "Kitchen diet register matching patient records.",
            "Bedside verification records that correct diet reached the patient.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.13 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Pain management, rehabilitation services and nutritional therapy are provided to the patients in a safe, collaborative and consistent manner." COP.13.a–f PDF indices 74–75. Asterisked OEs: a, e. Levels: all Commitment.

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
        "subtitle": "Pain management, rehabilitation and nutritional therapy.",
        "doc_no": D("COP/POL/13"),
    }
    emit_pre_v2(
        draft,
        "cop13_v2_draft.json",
        "COP.13_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
