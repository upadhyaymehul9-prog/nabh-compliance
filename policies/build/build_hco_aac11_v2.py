# -*- coding: utf-8 -*-
"""HCO AAC.11 v2 — preventive and promotive health services.

Shape: pre_v2_common.emit_pre_v2 + hco_v2_disclaimer accreditation-only.
Wording from NABH HCO Full Accreditation 6th Edition Guidebook
(PDF md5 2c4489ee98de4ae9b49cba168ea9f42a), PDF indices ~88–90 /
policies/source/hco6_aac_ocr.txt. Do not copy SHCO AAC wording.

Five OEs a–e. Asterisk: a. No stop-work. Accreditation-only.
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

STANDARD_CODE = "AAC.11"
CHAPTER = "HCO"
OE_CODES = [
    "AAC.11.a", "AAC.11.b", "AAC.11.c", "AAC.11.d", "AAC.11.e",
]
POLICY_TITLE = "Preventive and Promotive Health Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "20-08-2026",
        "description": (
            "HCO Full 6th Edition AAC.11 v2 draft from guidebook OCR; "
            "five steps; asterisk a; no stop-work; accreditation-only P2."
        ),
    },
]

STATEMENT_OF_INTENT = (
    "Preventive and promotive health services are provided in a safe, collaborative "
    "and consistent manner — as part of patient care, not as a poster campaign alone."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides preventive and promotive health services in a safe, collaborative and consistent manner within its scope of services.

It covers five jobs that match the standard:

- written guidance governing preventive and promotive care as per scope (immunization, screening, education, lifestyle counselling and related measures);
- evidenced-based, contextual, age-appropriate screening for non-communicable diseases;
- mental health screening and appropriate intervention wherever applicable;
- evidence-based, contextual paediatric and adult immunisation wherever applicable;
- a multi-disciplinary approach to health education on lifestyle modifications.

The chapter intent is that preventive and promotive healthcare services are part of patient care and that continuity of care extends to the community where the organisation provides such services.

This policy owns preventive and promotive method within scope. AAC.1 owns the defined scope of services. AAC.4 / AAC.5 own clinical assessment and re-assessment. AAC.10 owns continuity and multi-disciplinary coordination during clinical care. This policy does not invent a community programme this hospital does not offer.

Words marked {D('like this')} are defaults a hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies at {HOSPITAL} wherever preventive or promotive care is offered within the organisation's scope: out-patient, in-patient, emergency discharge advice, day-care, and community or domiciliary touchpoints if this hospital provides them.

It binds:

- treating doctors who advise screening, immunisation and lifestyle measures;
- nurses who support education and immunisation where applicable;
- registration staff who schedule or direct patients to preventive clinics where used;
- the {D('Medical Superintendent')} who holds written guidance and scope alignment;
- the {D('Quality Coordinator')} who audits records;
- multi-disciplinary contributors named in section 5.5 (for example dietician, physiotherapist, psychologist, medico-social worker) where those roles exist.

Boundaries with other policies of {HOSPITAL}:

- AAC.1 owns what clinical services are in scope and displayed. This policy owns preventive and promotive practice inside that scope.
- AAC.4 / AAC.5 own initial assessment and re-assessment. Screening advice under this policy may appear in those assessments; the screening method is owned here.
- AAC.10 owns multi-disciplinary continuity of clinical care. Multi-disciplinary lifestyle education is owned here.
- AAC.12.f owns domiciliary visits for care after discharge where applicable. Community preventive outreach, if any, stays under this policy's written guidance.
- Mental health screening here is an accreditation method. It does not import a statutory Mental Healthcare Act checklist into this document."""

POLICY_STATEMENT = f"""{HOSPITAL} uses written guidance to implement preventive and promotive care as per its scope of services. Preventive care focuses on measures that prevent onset of disease or health conditions — for example immunization, health screening, health education and lifestyle counselling based on age, gender and medical history. Promotive care promotes overall health and well-being among patients, families and community through education, health literacy and activities this hospital actually offers.

{HOSPITAL} defines evidenced-based, contextual, age-appropriate non-communicable disease screening; advises mental health screening and appropriate intervention wherever applicable; advises evidence-based paediatric and adult immunisation wherever applicable; and uses a multi-disciplinary approach to lifestyle-modification education.

{HOSPITAL} does not claim preventive services outside its scope, and does not treat a single poster as written guidance."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no clinic convenience exception.

1. Delivering preventive or promotive care without current written guidance aligned to this hospital's scope.
2. Advising NCD screening that is not evidenced-based, not contextual, or not age-appropriate for the patient.
3. Ignoring mental health screening and appropriate intervention where the clinical context makes them applicable.
4. Advising paediatric or adult immunisation that ignores the Universal Immunisation Programme for neonates and children, or ignores evidence-based adult preventable-disease guidance where adult immunisation is offered.
5. Delivering lifestyle-modification education as a single-discipline lecture when a multi-disciplinary approach is available and applicable.
6. Advertising community preventive services this hospital does not actually provide.

Staff who see one of these acts report it the same shift to the {D('treating doctor')} or the {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Written guidance for preventive and promotive care

Written guidance governs the implementation of preventive and promotive care at {HOSPITAL} as per the scope of services.

Preventive care focuses on measures taken to prevent the onset of diseases or health conditions before they occur — for example immunization, health screening, health education and lifestyle counselling — based on age, gender and medical history.

Promotive care involves efforts to promote overall health and well-being among patients, families and community — for example promoting healthy diet, regular exercise, stress management, mental health support and initiatives to improve quality of life through patient and family education, health literacy and community activities this hospital offers.

The {D('Medical Superintendent')} holds the current written guidance. The guidance names which preventive and promotive services are in scope, who delivers them, and how they are documented. Services outside scope are not promised.""",

f"""5.2 Age-appropriate NCD screening

{HOSPITAL} defines evidenced-based and contextual age-appropriate screening for non-communicable diseases.

For prevention of non-communicable diseases, evidence-based screening of patients at an appropriate age is advised — for example screening for various cancers, diabetes and osteoporosis — as listed in the written guidance. Frequency of screening may increase when predisposing factors apply. Treating doctors document the screening advised, accepted or declined, and the basis (age, risk factors, guidance reference).""",

f"""5.3 Mental health screening and intervention

Mental health screening and appropriate intervention are advised for patients wherever applicable at {HOSPITAL}.

Screening may use validated tools — for example {D('PHQ-9 for depression, or a distress thermometer for oncology patients')} — as named in the written guidance. De-stressing interventions may be considered for patients seeking healthcare — for example yoga and meditation — where this hospital offers or refers for them. Positive screens lead to documented advice, referral or intervention appropriate to the finding and to this hospital's scope.""",

f"""5.4 Paediatric and adult immunisation

Evidence-based and contextual paediatric and adult immunisation is advised wherever applicable at {HOSPITAL}.

The Universal Immunisation Programme is adhered to for all neonates and paediatric patients, including catch-up immunisation for children. Adult immunisation, where offered, focuses on preventable diseases such as pneumococcal pneumonia, HPV, influenza, COVID and meningococcal disease, adhering to evidence-based guidelines named in the written guidance. Advice, administration and refusals are recorded in the patient record or immunisation register.""",

f"""5.5 Multi-disciplinary lifestyle education

A multi-disciplinary approach is adopted in imparting health education on lifestyle modifications at {HOSPITAL}.

Contributors may include the clinician, nurse, dietician, physiotherapist, occupational therapist, psychologist and medico-social worker where those roles exist. Education may incorporate exercises, training in activities of daily living, and effective pain and inflammation management. Healthcare providers educate to optimise health and well-being, particularly in geriatric care. Family members are also educated towards cessation of tobacco, alcohol and substance abuse where relevant.

Therapeutic exercises are planned and systematic, tailored to the patient's needs, and may be used for rehabilitation after surgery or for chronic conditions. The education given and the disciplines involved are recorded.""",
]

RESPONSIBILITY = f"""Medical Superintendent
- Holds written guidance for preventive and promotive care aligned to scope.
- Accountable that screening, immunisation and lifestyle education methods are defined.

Treating doctors
- Advise NCD screening, mental health screening, immunisation and lifestyle measures as applicable; document advice and follow-up.

Nurses
- Support education, immunisation and screening workflows where assigned; document patient education.

Registration / front-office
- Direct patients to preventive clinics or slots where this hospital uses them.

Multi-disciplinary contributors (where roles exist)
- Deliver their part of lifestyle education (diet, exercise, psychology, social support) and record it.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when preventive or promotive defects recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Current written guidance exists and matches the scope of services.
- Sampled records show age-appropriate NCD screening advice where applicable.
- Mental health screening and intervention documented where clinically applicable.
- Paediatric UIP adherence and adult immunisation advice where applicable.
- Lifestyle education involving more than one discipline where multi-disciplinary input was available and needed.

Root-cause analysis is required when the same preventive or promotive defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when scope of services, national immunisation schedules or screening guidance this hospital adopts changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All treating doctors, nurses and multi-disciplinary contributors named in this policy are trained on it at induction and {D('once a year')} after that. Training covers the written guidance, NCD screening expectations, mental health screening tools in use, immunisation advice and lifestyle education roles.

Staff acknowledgement

I have read this Preventive and Promotive Health Services policy of {HOSPITAL}. I will follow the written guidance for screening, immunisation and lifestyle education within this hospital's scope.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("HCO/AAC/POL/11"),
    version=VERSION,
    prepared_by=D("Medical Superintendent"),
    draft_label="HCO Full v2 draft",
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Guidebook to Accreditation Standards for Hospitals, 6th Edition — Access, Assessment and Continuity of Care chapter, standard AAC.11 (PDF indices ~88–90; source OCR policies/source/hco6_aac_ocr.txt; PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Universal Immunisation Programme (UIP) schedule as adopted by this hospital for neonates and paediatric patients.
- Internal documents of {HOSPITAL}: preventive and promotive written guidance; screening schedules; immunisation register; patient education records."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Quality Coordinator.

Copies issued to: out-patient; in-patient wards; emergency; immunisation or preventive clinic if separate; nursing administration; allied health leads where lifestyle education is delivered.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AAC — Access, Assessment and Continuity of Care (NABH HCO chapter)
ADL — activities of daily living
CAPA — corrective and preventive action
HCO — Hospital Accreditation Programme (NABH Full Accreditation)
HPV — human papillomavirus
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NCD — non-communicable disease
OE — objective element
PHQ-9 — Patient Health Questionnaire-9
UIP — Universal Immunisation Programme"""

DISCLAIMER, STATUTE_CLAUSE = make_hco_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "AAC.11.a",
        "requirement": (
            "Written guidance governs the implementation of preventive and promotive "
            "care as per the scope of services."
        ),
        "steps": "Section 3; 5.1 Written guidance for preventive and promotive care; Section 4 item 1",
        "responsible": "Medical Superintendent (holds guidance); treating doctors and nurses (follow); Quality Coordinator (audit)",
        "records": [
            "Current written guidance for preventive and promotive care aligned to scope.",
            "Version control and issue date of that written guidance.",
            "Quarterly audit confirming practice matches the guidance and scope.",
        ],
    },
    {
        "oe_code": "AAC.11.b",
        "requirement": (
            "Organisation shall define evidenced based and contextual age-appropriate "
            "screening for non-communicable diseases."
        ),
        "steps": "Section 3; 5.2 Age-appropriate NCD screening; Section 4 item 2",
        "responsible": "Treating doctors (advise and document); Medical Superintendent (defines in guidance)",
        "records": [
            "Defined NCD screening list with age and risk-context criteria.",
            "Patient record entries of screening advised, accepted or declined.",
            "Quarterly sample of age-appropriate screening documentation.",
        ],
    },
    {
        "oe_code": "AAC.11.c",
        "requirement": (
            "Mental health screening and appropriate intervention is advised for patients "
            "wherever applicable."
        ),
        "steps": "Section 3; 5.3 Mental health screening and intervention; Section 4 item 3",
        "responsible": "Treating doctors (screen and intervene or refer); Quality Coordinator (audit)",
        "records": [
            "Documented use of validated screening tools where applicable.",
            "Record of intervention, advice or referral after a positive screen.",
            "Quarterly sample of applicable patients with mental health screening documented.",
        ],
    },
    {
        "oe_code": "AAC.11.d",
        "requirement": (
            "Evidence based and contextual paediatric and adult immunisation shall be "
            "advised wherever applicable."
        ),
        "steps": "Section 3; 5.4 Paediatric and adult immunisation; Section 4 item 4",
        "responsible": "Treating doctors and nurses (advise/administer); Medical Superintendent (guidance)",
        "records": [
            "Paediatric immunisation records aligned to UIP including catch-up where needed.",
            "Adult immunisation advice or administration records where adult immunisation is offered.",
            "Immunisation register or patient-file entries with vaccine, date and clinician.",
        ],
    },
    {
        "oe_code": "AAC.11.e",
        "requirement": (
            "A multi-disciplinary approach is adopted in imparting health education on "
            "life-style modifications."
        ),
        "steps": "Section 3; 5.5 Multi-disciplinary lifestyle education; Section 4 item 5",
        "responsible": "Treating doctors, nurses and allied contributors; Quality Coordinator (audit)",
        "records": [
            "Patient education record naming disciplines involved in lifestyle education.",
            "Documentation of diet, exercise, ADL, pain or substance-cessation education where given.",
            "Quarterly sample showing multi-disciplinary input where available and applicable.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """HCO AAC.11 v2 (2026-08-20). PDF md5 2c4489ee98de4ae9b49cba168ea9f42a. Source OCR policies/source/hco6_aac_ocr.txt (PDF idxs ~88–90). Five OEs a–e. Asterisk: a (written guidance) — fuller procedure and evidence. No Core flag in guidebook inventory for this standard. No stop-work. P2: accreditation-only; no MHCA/CPA/CEA checklist import. chapter=HCO. doc_no «HCO/AAC/POL/11». UIP named as programme method for paediatric immunisation, not as disclaimer statute. Do not copy SHCO wording."""


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
        "prepared_by": D("Medical Superintendent"),
        "stop_work": "",
        "template_test": "hco_aac_v2_adoptable_shape",
        "subtitle": "Preventive and promotive care within scope of services.",
        "doc_no": D("HCO/AAC/POL/11"),
        "programme": "HCO Full Accreditation, 6th Edition",
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": "HCO.AAC.11",
    }
    emit_pre_v2(
        draft,
        "hco_aac11_v2_draft.json",
        "HCO.AAC.11_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
        edition_label=HCO_EDITION_LABEL,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
