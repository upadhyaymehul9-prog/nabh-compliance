# -*- coding: utf-8 -*-
"""COP.13 v2 — pain management, rehabilitation services and nutritional therapy.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 74–75.
No stop-work section. Six OEs in six What-we-do subsections.
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
        "description": "COP v2 template: adoptable shape, plain English, no stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Pain management, rehabilitation services and nutritional therapy are provided "
    "to the patients in a safe, collaborative and consistent manner — effective pain "
    "management, titrated alleviation, commensurate rehabilitation, collaborative "
    "rehabilitation planning, nutritional screening and assessment, and collaborative "
    "therapeutic diet."
)

PURPOSE = f"""This policy defines how {HOSPITAL} manages pain effectively, provides rehabilitation services commensurate with its service scope, plans rehabilitation collaboratively, screens patients for nutritional risk with assessment for those at risk, and plans therapeutic diets collaboratively.

Boundaries: AAC.3 owns initial patient assessment; this policy owns nutritional screening and nutritional therapy. Rehabilitation scope is limited to services provided per the hospital's service directory.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all clinical staff at {HOSPITAL} involved in pain management, rehabilitation, and nutritional care: treating doctors, nurses, physiotherapists, rehabilitation therapists, dietitians/nutritionists, and support staff.

It covers pain assessment and management, rehabilitation services, and nutritional screening/therapy. It does not own the initial assessment (AAC.3) or services the hospital does not provide (recorded absences)."""

POLICY_STATEMENT = f"""{HOSPITAL} manages pain effectively and titrates alleviation measures according to the patient's need and response. Rehabilitation services are commensurate with the services provided and are planned collaboratively. Patients are screened for nutritional risk, assessed where at risk, and receive collaboratively planned therapeutic diets.

{HOSPITAL} does not leave pain unassessed, rehabilitation unplanned, or nutritional risk unscreened."""

NON_NEGOTIABLES = f"""1. Every patient is assessed for pain using {D('a validated pain scale appropriate to age and cognition')} at admission, at defined intervals, and after intervention.
2. Pain alleviation is initiated when pain is identified; it is not deferred to the next round.
3. Rehabilitation goals are set collaboratively with the patient and/or family.
4. Nutritional screening is completed for every admitted patient within {D('24 hours')} of admission.
5. A patient found at nutritional risk receives a documented nutritional assessment and a therapeutic diet plan."""

PROCEDURE_STEPS = [
f"""5.1 Effective pain management

Patients in pain at {HOSPITAL} are effectively managed. Pain is assessed using {D('the Numeric Rating Scale (NRS) for adults and the Wong-Baker FACES scale for children or cognitively impaired patients')}.

Pain is assessed at admission, at defined intervals ({D('every shift and after intervention')}), and whenever the patient reports pain. The treating team documents pain scores and initiates or adjusts management. Unrelieved pain triggers escalation to the {D('treating doctor')} within {D('30 minutes')}. A multidisciplinary approach (pharmacological and non-pharmacological) is used where appropriate.""",

f"""5.2 Pain alleviation titrated to patient need and response

Pain alleviation measures or medications are initiated and titrated according to the patient's need and response. The treating doctor prescribes analgesia according to {D('the WHO analgesic ladder or equivalent stepwise approach')}.

Nurses administer as prescribed and reassess within {D('30 minutes for parenteral and 60 minutes for oral')} administration. Dose adjustments are communicated to the prescribing doctor. Adverse effects of analgesics are monitored and documented. Non-pharmacological measures ({D('positioning, cold/heat, distraction, relaxation techniques')}) are offered and documented.""",

f"""5.3 Rehabilitation services commensurate with hospital scope

The scope of rehabilitation services at {HOSPITAL} is at a minimum commensurate with the services provided by the organisation. Services include {D('physiotherapy, and other rehabilitation disciplines as per the service directory')}.

Services not in the service directory are recorded absences, not copied SOPs. The {D('Physiotherapy In-Charge')} maintains the scope document and referral pathways for services this hospital cannot provide internally.""",

f"""5.4 Collaborative rehabilitation planning

Care providers collaboratively plan rehabilitation services. Rehabilitation goals are set with the patient and/or family. The rehabilitation plan documents current functional status, goals, interventions, responsible therapist, and review timeline.

The treating doctor, physiotherapist/rehabilitation therapist, nurse, and patient/family participate in planning. Progress is reviewed at {D('weekly')} intervals or more frequently if clinically indicated. Discharge rehabilitation advice is documented.""",

f"""5.5 Nutritional screening and assessment

Patients admitted to {HOSPITAL} are screened for nutritional risk within {D('24 hours')} of admission using {D('the Malnutrition Universal Screening Tool (MUST) or equivalent validated tool')}. AAC.3 owns initial assessment; this step owns nutritional screening and the follow-on assessment.

Patients found at nutritional risk receive a documented nutritional assessment by the {D('dietitian/nutritionist')} covering anthropometry, dietary history, biochemical markers, clinical signs, and functional capacity. The assessment results in a nutritional care plan.""",

f"""5.6 Collaborative therapeutic diet planning

The therapeutic diet is planned and provided collaboratively. The dietitian/nutritionist, treating doctor, and nursing staff plan the diet together based on the nutritional assessment, diagnosis, and patient preferences.

The diet plan documents calorie/protein targets, consistency, allergens, supplements where indicated, and monitoring schedule. Diet is reviewed on clinical change or at {D('weekly')} intervals. Patient/family education on the diet is provided and documented. Kitchen staff receive written diet orders; delivery is verified by the nurse.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that pain management, rehabilitation and nutritional therapy are provided safely and collaboratively.

Treating doctors
- Prescribe and adjust pain management; refer for rehabilitation and nutritional assessment; participate in collaborative planning.

Nurses
- Assess pain; administer analgesia; reassess; deliver diet; screen nutritional risk; communicate.

Physiotherapist / Rehabilitation therapist
- Provide rehabilitation services within scope; set goals collaboratively; document progress.

Dietitian / Nutritionist
- Perform nutritional assessment for at-risk patients; plan therapeutic diets collaboratively; educate patients/families.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when a pain/rehabilitation/nutrition defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Pain assessment documented at admission and defined intervals (sample charts).
- Pain reassessment after intervention within defined timeframe.
- Rehabilitation plans documented with collaborative goals.
- Nutritional screening completed within 24 hours of admission.
- Nutritional assessment and diet plan for at-risk patients.
- Therapeutic diet orders communicated to kitchen and verified on delivery.

Root-cause analysis is required when a pain/rehabilitation/nutrition defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when pain guidelines, rehabilitation scope, or nutritional tools change."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff are trained on this policy at induction and {D('once a year')} after that. Training covers pain assessment tools, analgesic titration, rehabilitation referral and collaborative planning, nutritional screening, and therapeutic diet processes.

Staff acknowledgement

I have read this Pain Management, Rehabilitation Services and Nutritional Therapy policy of {HOSPITAL}. I will assess pain, plan rehabilitation collaboratively, screen for nutritional risk, and plan therapeutic diets in accordance with this policy.


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
- World Health Organization (WHO), WHO Analgesic Ladder — pain management framework.
- British Association for Parenteral and Enteral Nutrition (BAPEN), Malnutrition Universal Screening Tool (MUST) — nutritional screening.
- Internal documents of {HOSPITAL}: pain assessment forms, analgesic protocols, rehabilitation scope document, nutritional screening tool, therapeutic diet order forms, kitchen communication process."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: every in-patient ward; ICU; emergency department; physiotherapy; dietetics/nutrition; kitchen (diet orders section); nursing administration.

The current version is available to all staff at the {D('ward policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """CAPA — corrective and preventive action
ICU — intensive care unit
MUST — Malnutrition Universal Screening Tool
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NRS — Numeric Rating Scale
OE — objective element
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.13.a",
        "requirement": "Patients in pain are effectively managed.",
        "steps": "Section 3; 5.1 Effective pain management; Section 4 items 1–2",
        "responsible": "Treating doctors (prescribe); nurses (assess and administer); Quality Coordinator (audit)",
        "records": [
            "Pain assessment records using validated scale at admission, defined intervals, and after intervention.",
            "Documentation of pain management initiated when pain identified.",
            "Escalation records for unrelieved pain.",
            "Multidisciplinary pain-management plans where applicable.",
        ],
    },
    {
        "oe_code": "COP.13.b",
        "requirement": "Pain alleviation measures or medications are initiated and titrated according to the patient's need and response.",
        "steps": "Section 3; 5.2 Pain alleviation titrated to patient need and response; Section 4 item 2",
        "responsible": "Treating doctors (prescribe and adjust); nurses (administer, reassess, communicate)",
        "records": [
            "Analgesic prescriptions with stepwise approach documented.",
            "Reassessment records within defined timeframe after administration.",
            "Dose-adjustment communications documented.",
            "Non-pharmacological measures offered and documented.",
        ],
    },
    {
        "oe_code": "COP.13.c",
        "requirement": "Scope of rehabilitation services at a minimum is commensurate to the services provided by the organization.",
        "steps": "Section 3; 5.3 Rehabilitation services commensurate with hospital scope",
        "responsible": "Physiotherapy In-Charge (scope document); Medical Superintendent (resource allocation)",
        "records": [
            "Rehabilitation scope document aligned with hospital service directory.",
            "Referral pathways for services not available internally.",
            "Recorded absences against service directory for services not provided.",
        ],
    },
    {
        "oe_code": "COP.13.d",
        "requirement": "Care providers collaboratively plan rehabilitation services.",
        "steps": "Section 3; 5.4 Collaborative rehabilitation planning; Section 4 item 3",
        "responsible": "Treating doctor, physiotherapist, nurse (plan together); patient/family (participate)",
        "records": [
            "Rehabilitation plans with collaborative goals documented.",
            "Patient/family participation in goal-setting documented.",
            "Progress reviews at defined intervals.",
            "Discharge rehabilitation advice documented.",
        ],
    },
    {
        "oe_code": "COP.13.e",
        "requirement": "Patients admitted to the organization are screened for nutritional risk, and assessment is done for patients found at risk during nutritional screening.",
        "steps": "Section 3; 5.5 Nutritional screening and assessment; Section 4 items 4–5",
        "responsible": "Nurses (screen); dietitian/nutritionist (assess at-risk patients)",
        "records": [
            "Nutritional screening completed within 24 hours of admission using validated tool.",
            "Nutritional assessment by dietitian for patients identified at risk.",
            "Nutritional care plan documented for at-risk patients.",
            "Audit sample confirming screening-to-assessment pathway completed.",
        ],
    },
    {
        "oe_code": "COP.13.f",
        "requirement": "The therapeutic diet is planned and provided collaboratively.",
        "steps": "Section 3; 5.6 Collaborative therapeutic diet planning; Section 4 item 5",
        "responsible": "Dietitian/nutritionist (plan); treating doctor (approve); nurses (verify delivery); kitchen (prepare)",
        "records": [
            "Therapeutic diet plans with calorie/protein targets, consistency and monitoring schedule.",
            "Collaborative planning documented (dietitian, doctor, nursing input).",
            "Diet orders communicated to kitchen with delivery verification.",
            "Patient/family education on diet documented.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.13 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Pain management, rehabilitation services and nutritional therapy are provided to the patients in a safe, collaborative and consistent manner." COP.13.a–f PDF indices 74–75. Asterisked OEs: a, e. All Commitment level.

SHAPE: Six What-we-do subsections (5.1–5.6). No stop-work. Disclaimer accreditation-only. COP clinical/rehabilitation/nutrition roles."""


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
        "subtitle": "Pain, rehabilitation and nutritional therapy in day-to-day care.",
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
