# -*- coding: utf-8 -*-
"""COP.7 v2 — safe obstetric care.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 70–71.
No stop-work section. Five OEs (COP.7.a–e).
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.7"
CHAPTER = "COP"
OE_CODES = [
    "COP.7.a", "COP.7.b", "COP.7.c", "COP.7.d", "COP.7.e",
]
POLICY_TITLE = "Safe Obstetric Care"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, no stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "The organization provides safe obstetric care — not a labour room that runs "
    "on habit without written guidance, nutritional assessment, or a referral plan "
    "for high-risk cases."
)

PURPOSE = f"""This policy defines how {HOSPITAL} provides safe obstetric care.

It covers five elements: obstetric services organised and provided safely; identification and care of high-risk obstetric cases with competent staff and referral where needed; antenatal assessment including maternal nutrition; appropriate peri-natal and post-natal monitoring; and human resources and facilities to take care of neonates of high-risk obstetric cases.

Boundaries: COP.8 owns paediatric and neonatal care as a standalone policy; this policy owns neonatal readiness for high-risk obstetric cases. COP.4 owns nursing care; this policy owns obstetric nursing within the labour room and maternity ward.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff involved in obstetric care at {HOSPITAL}: obstetricians or treating doctors, midwives, labour room nurses, maternity ward nurses, and support staff.

It covers the five elements COP.7.a–e name. It does not cover paediatric and neonatal care as a standalone programme (COP.8), nursing care policy (COP.4), or medication management (MOM).

Boundaries with other policies of {HOSPITAL}:

- COP.8 owns paediatric and neonatal care. This policy owns that the organization caring for high-risk obstetric cases has neonatal readiness.
- COP.4 owns nursing care. This policy owns obstetric nursing standards within the labour room and maternity ward.
- PRE.3 owns informed consent. This policy owns that consent is obtained for obstetric procedures as part of safe obstetric care.
- COP.2 owns emergency clinical care. This policy owns obstetric emergencies within the obstetric service."""

POLICY_STATEMENT = f"""{HOSPITAL} organises and provides obstetric services safely. Obstetric services follow written guidance covering antenatal, intra-natal, and post-natal care.

{HOSPITAL} identifies high-risk obstetric cases and provides care with competent doctors and nurses. Where the hospital cannot manage a high-risk case, it refers the patient to another appropriate centre. Referral criteria and processes are documented.

Antenatal assessment includes maternal nutrition. Nutritional screening is performed at the first antenatal visit and at defined intervals. Nutritional counselling and supplementation are provided as indicated.

Appropriate peri-natal and post-natal monitoring is performed, including {D('partograph use during labour, foetal heart rate monitoring, APGAR scoring, post-partum haemorrhage surveillance, and post-natal maternal and neonatal observations')}.

Where {HOSPITAL} cares for high-risk obstetric cases, it has the human resources and facilities to take care of neonates of such cases, including {D('a neonatal resuscitation area, trained staff for neonatal resuscitation, and essential neonatal equipment')}.

{HOSPITAL} does not treat any of these as meeting this policy: a labour room without a partograph; a high-risk case managed without competent staff; antenatal care without nutritional assessment; or a hospital that takes high-risk deliveries without neonatal readiness."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Conducting a delivery without a partograph or equivalent documented labour monitoring tool.
2. Managing a high-risk obstetric case without a doctor competent in obstetric care being available, or failing to refer when the hospital cannot manage the case.
3. Completing antenatal assessment without documenting maternal nutritional screening.
4. Failing to perform post-natal maternal and neonatal observations at defined intervals.
5. Taking high-risk deliveries without neonatal resuscitation equipment and trained staff available.

Staff who see one of these acts report it the same shift to the {D('obstetric department in-charge')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Obstetric services organised and provided safely

{HOSPITAL} organises obstetric services with written guidance covering antenatal, intra-natal, and post-natal care. The guidance is reviewed {D('annually')} by the {D('obstetric department in-charge in consultation with treating doctors')}.

The labour room is equipped with {D('delivery table, resuscitation equipment for mother and neonate, partograph forms, emergency medications, and infection prevention supplies')}. Equipment is checked {D('at the start of each shift')}.

Obstetric protocols cover: {D('normal delivery, assisted delivery, caesarean section criteria, induction of labour, management of obstetric emergencies including eclampsia, post-partum haemorrhage, and cord prolapse')}.""",

f"""5.2 High-risk obstetric cases: identification, care and referral

{HOSPITAL} identifies high-risk obstetric cases at the earliest antenatal visit and at each subsequent visit. High-risk criteria include {D('pre-eclampsia, gestational diabetes, multiple pregnancy, previous caesarean section, placenta praevia, severe anaemia, and any condition the treating doctor identifies as high risk')}.

High-risk cases are managed by competent doctors and nurses. Where the hospital cannot manage a case, it is referred to another appropriate centre. Referral criteria are documented and include: {D('condition requiring referral, receiving centre, stabilisation before transfer, and communication with the receiving centre')}.

The {D('obstetric department in-charge')} maintains a register of high-risk cases and their outcomes.""",

f"""5.3 Antenatal assessment including maternal nutrition

Antenatal assessment follows a structured protocol that includes maternal nutritional screening at the first antenatal visit. Nutritional screening uses {D('a structured questionnaire or BMI-based assessment')}.

Nutritional counselling is provided to all antenatal patients. Supplementation with {D('iron, folic acid, and calcium as per national guidelines')} is prescribed where indicated. Nutritional reassessment is performed at {D('each trimester')}.

The antenatal record documents nutritional screening, counselling, supplementation, and reassessment findings.""",

f"""5.4 Peri-natal and post-natal monitoring

Appropriate peri-natal monitoring is performed during labour: {D('partograph use, foetal heart rate monitoring at defined intervals, maternal vital signs, and progress of labour')}. APGAR scoring is performed at one and five minutes after birth.

Post-natal monitoring covers the mother and the neonate. Maternal monitoring includes: {D('vital signs, uterine involution, lochia assessment, breast-feeding support, and post-partum haemorrhage surveillance')}. Neonatal monitoring includes: {D('weight, feeding, jaundice screening, cord care, and immunisation as per national schedule')}.

Monitoring intervals are documented and followed. Deviations from expected progress are escalated to the treating doctor.""",

f"""5.5 Neonatal readiness for high-risk obstetric cases

Where {HOSPITAL} cares for high-risk obstetric cases, it has the human resources and facilities to take care of neonates of such cases. A neonatal resuscitation area is available adjacent to or within the labour room.

Neonatal resuscitation equipment includes {D('radiant warmer, bag and mask, suction, oxygen supply, pulse oximeter, and emergency medications')}. Equipment is checked {D('at the start of each shift')}.

At least {D('one person trained in neonatal resuscitation')} is available for every high-risk delivery. Training is refreshed {D('annually')}. If the hospital does not have neonatal intensive care, referral arrangements with a facility that does are documented.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that obstetric care is provided safely as this policy requires.
- Receives escalations for high-risk cases and neonatal readiness.

{D('Obstetric department in-charge')}
- Holds written guidance, high-risk register, referral criteria, and equipment checklists.
- Reviews protocols annually.

Obstetricians / treating doctors
- Identify and manage high-risk cases. Conduct deliveries following written guidance.
- Perform antenatal nutritional screening and prescribe supplementation.

Labour room and maternity ward nurses / midwives
- Use partograph during labour. Perform peri-natal and post-natal monitoring.
- Assist with neonatal resuscitation as trained.

{D('Quality Coordinator')}
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA for obstetric findings."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Partograph or equivalent labour monitoring documented for sampled deliveries.
- High-risk cases identified, managed, and referred where needed (register review).
- Antenatal nutritional screening documented at first visit and at defined intervals.
- Peri-natal and post-natal monitoring at defined intervals documented.
- Neonatal resuscitation equipment checked and trained staff available for high-risk deliveries.

Root-cause analysis is required when an obstetric or neonatal adverse event occurs or when the same finding recurs within six months.

This policy is reviewed {D('annually')}, and sooner when obstetric guidelines change or the scope of obstetric services changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All obstetric care staff are trained on this policy at induction and {D('once a year')} after that. Training covers labour monitoring, high-risk identification and referral, nutritional screening, peri-natal and post-natal monitoring, and neonatal resuscitation.

Staff acknowledgement

I have read this Safe Obstetric Care policy of {HOSPITAL}. I will follow written obstetric guidance, identify high-risk cases, perform nutritional screening, and ensure neonatal readiness for high-risk deliveries.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The obstetric department in-charge holds signed acknowledgements with the training file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/07"),
    version=VERSION,
    prepared_by=D("Obstetric department in-charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.7.
- Internal documents of {HOSPITAL}: obstetric protocols (normal delivery, assisted delivery, caesarean section, obstetric emergencies), partograph forms, high-risk obstetric register, referral criteria and agreements, antenatal nutritional screening tool, neonatal resuscitation equipment checklist, COP.8 paediatric and neonatal care policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('obstetric department in-charge')} and the Quality Coordinator.

Copies issued to: labour room; maternity ward; antenatal clinic; neonatal area; nursing administration.

The current version is available to all obstetric care staff at the {D('labour room policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """APGAR — Appearance, Pulse, Grimace, Activity, Respiration (neonatal scoring)
BMI — body mass index
CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
HDU — high dependency unit
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.7.a",
        "requirement": "Obstetric services are organised and provided safely.",
        "steps": "Section 3; 5.1 Obstetric services organised and provided safely; Section 4 item 1",
        "responsible": "Obstetric department in-charge (guidance and equipment); treating doctors (deliver care); nurses/midwives (assist)",
        "records": [
            "Written obstetric guidance documents reviewed annually.",
            "Labour room equipment checklist completed each shift.",
            "Obstetric protocols covering normal delivery, assisted delivery, caesarean section, and emergencies.",
            "Sample delivery records showing protocol adherence.",
        ],
    },
    {
        "oe_code": "COP.7.b",
        "requirement": "The organization identifies and provides care to high risk obstetric cases with competent doctors and nurses, and where needed, refers them to another appropriate centre.",
        "steps": "Section 3; 5.2 High-risk obstetric cases: identification, care and referral; Section 4 item 2",
        "responsible": "Treating doctors (identify and manage); obstetric department in-charge (register and referral criteria)",
        "records": [
            "High-risk obstetric register with identification criteria, management plans, and outcomes.",
            "Referral criteria document with receiving centres and communication records.",
            "Competency records for doctors and nurses managing high-risk cases.",
        ],
    },
    {
        "oe_code": "COP.7.c",
        "requirement": "Antenatal assessment also includes maternal nutrition.",
        "steps": "Section 3; 5.3 Antenatal assessment including maternal nutrition; Section 4 item 3",
        "responsible": "Treating doctors (screen and prescribe); nurses (counsel and document)",
        "records": [
            "Nutritional screening documented at first antenatal visit.",
            "Nutritional counselling and supplementation records.",
            "Reassessment findings documented at each trimester.",
        ],
    },
    {
        "oe_code": "COP.7.d",
        "requirement": "Appropriate peri-natal and post-natal monitoring is performed.",
        "steps": "Section 3; 5.4 Peri-natal and post-natal monitoring; Section 4 item 4",
        "responsible": "Nurses/midwives (monitor and document); treating doctors (escalation and intervention)",
        "records": [
            "Partograph completed for each labour.",
            "APGAR scores at one and five minutes documented.",
            "Post-natal maternal and neonatal observation records at defined intervals.",
        ],
    },
    {
        "oe_code": "COP.7.e",
        "requirement": "The organization caring for high risk obstetric cases has the human resources and facilities to take care of neonates of such cases.",
        "steps": "Section 3; 5.5 Neonatal readiness for high-risk obstetric cases; Section 4 item 5",
        "responsible": "Obstetric department in-charge (equipment and staffing); trained staff (neonatal resuscitation)",
        "records": [
            "Neonatal resuscitation equipment checklist completed each shift.",
            "Training records for neonatal resuscitation refreshed annually.",
            "Referral arrangement documentation with neonatal intensive care facility where applicable.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.7 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Organization provides safe obstetric care." COP.7.a–e PDF indices 70–71. Asterisked OEs: a, c. Levels: all Commitment.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. COP clinical roles."""


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
        "subtitle": "Safe obstetric care with nutritional assessment and neonatal readiness.",
        "doc_no": D("COP/POL/07"),
    }
    emit_pre_v2(
        draft,
        "cop7_v2_draft.json",
        "COP.7_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
