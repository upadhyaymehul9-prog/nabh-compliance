# -*- coding: utf-8 -*-
"""COP.7 v2 — safe obstetric care.

Shape follows PRE.1 v2 (section list and order only). Wording from COP.7 OEs
(NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed pages 70–71 / PDF indices 70–71.

No stop-work. Disclaimer accreditation-only. Five OEs (COP.7.a–e).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.7"
CHAPTER = "COP"
OE_CODES = ["COP.7.a", "COP.7.b", "COP.7.c", "COP.7.d", "COP.7.e"]
POLICY_TITLE = "Safe Obstetric Care"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: plain English, COP roles, five OEs, no stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Organization provides safe obstetric care — not a labour room that runs on individual "
    "habit, and not a high-risk case kept without the competence to manage it."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides safe obstetric care.

It covers five elements: obstetric services organised and provided safely; identification and care of high-risk obstetric cases with competent doctors and nurses, and referral where needed; antenatal assessment that includes maternal nutrition; appropriate peri-natal and post-natal monitoring; and human resources and facilities to take care of neonates of high-risk obstetric cases.

The chapter intent is that obstetric care is safe, competent, nutritionally aware, monitored and neonatally supported.

This policy owns obstetric care. COP.1 owns uniform care. PRE.3 owns informed consent. COP.3 owns CPR. COP.5 owns transfusion.

If this hospital does not provide obstetric services, record that as a written absence. Do not copy an obstetric SOP from another hospital.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to the obstetric services of {HOSPITAL} — antenatal clinics, labour room, post-natal ward and neonatal care area — and to every staff member who provides obstetric care: obstetricians, treating doctors, nurses and midwives, paediatricians or neonatologists where available, anaesthetists where available, and the Medical Superintendent.

It covers the five elements COP.7.a–e name. It does not cover uniform care (COP.1), informed consent (PRE.3), CPR (COP.3), or transfusion (COP.5).

Boundaries with other policies of {HOSPITAL}:

- COP.1 owns uniform care. This policy owns that obstetric care follows adopted guidelines.
- PRE.3 owns the consent method. This policy owns that consent is obtained for obstetric procedures.
- COP.3 owns CPR. This policy owns that CPR-trained staff and neonatal resuscitation equipment are available in the labour room.
- COP.5 owns transfusion. This policy owns that blood is available for obstetric emergencies.
- If this hospital does not provide obstetric services, record that as a written absence."""

POLICY_STATEMENT = f"""{HOSPITAL} organises and provides obstetric services safely. The labour room, antenatal clinic and post-natal ward are staffed, equipped and guided by written protocols.

{HOSPITAL} identifies high-risk obstetric cases and provides care with competent doctors and nurses. Where the hospital cannot manage a high-risk case, it refers the patient to another appropriate centre. Referral criteria are defined in writing.

Antenatal assessment includes maternal nutrition. Nutritional status is assessed and counselling is provided at every antenatal visit.

Appropriate peri-natal and post-natal monitoring is performed. Monitoring follows written protocols that cover labour progress, foetal heart rate, maternal vitals, and post-natal observations.

{HOSPITAL} caring for high-risk obstetric cases has the human resources and facilities to take care of neonates of such cases. This includes neonatal resuscitation equipment and staff trained in neonatal resuscitation.

{HOSPITAL} does not treat any of these as meeting this policy: a labour room without a written partograph protocol; a high-risk case kept without competent staff; nutrition advice given only on a poster; or neonatal resuscitation equipment that has never been checked."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no staffing convenience exception.

1. Providing obstetric services without written protocols for labour management, high-risk identification, and neonatal resuscitation.
2. Keeping a high-risk obstetric case that exceeds the competence of the available doctors and nurses, without documenting the clinical reason and arranging referral.
3. Omitting maternal nutrition assessment from antenatal care.
4. Conducting labour without peri-natal monitoring (partograph, foetal heart rate monitoring, maternal vitals) as the written protocol requires.
5. Caring for high-risk obstetric cases without neonatal resuscitation equipment and staff trained in neonatal resuscitation available in the labour room.

Staff who see one of these acts report it the same shift to the {D('obstetric department in-charge')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Obstetric services organised and provided safely

{HOSPITAL} organises obstetric services with written protocols, adequate staffing and appropriate equipment. The labour room is equipped with at minimum: {D('delivery table, radiant warmer, neonatal resuscitation equipment, partograph charts, foetal Doppler or cardiotocograph, suction, oxygen, emergency medications, and crash cart access (COP.3)')}.

Staffing includes at minimum: {D('one obstetrician or trained doctor and one nurse or midwife available for every delivery')}. Anaesthetic support is available for operative deliveries.

Written protocols cover at minimum: {D('normal labour management, operative delivery indications, post-partum haemorrhage, eclampsia, and shoulder dystocia')}. Protocols are reviewed {D('annually')} by the {D('obstetric department in-charge')}.

The {D('obstetric department in-charge')} holds the protocols, staffing roster and equipment inventory.""",

f"""5.2 High-risk obstetric identification, competent care and referral

{HOSPITAL} identifies high-risk obstetric cases at antenatal registration and at every subsequent visit. High-risk criteria include at minimum: {D('previous caesarean section, pre-eclampsia, gestational diabetes, multiple pregnancy, preterm labour, antepartum haemorrhage, foetal growth restriction, and maternal age above 35 or below 18')}.

High-risk cases are managed by competent doctors and nurses. Competence means the doctor has training and experience in managing the identified risk. Where the hospital cannot manage a high-risk case, it refers the patient to another appropriate centre. Referral criteria and the list of referral centres are defined in writing and reviewed {D('annually')}.

The referral decision, the reason, the receiving centre and the patient's condition at transfer are documented. COP.2 and AAC.2 own the transfer process; this policy owns the clinical decision to refer.""",

f"""5.3 Antenatal assessment including maternal nutrition

Antenatal assessment includes maternal nutrition. Nutritional status is assessed at the first antenatal visit and at each subsequent visit using {D('weight, haemoglobin, dietary history and BMI or mid-upper arm circumference')}.

Counselling on nutrition is provided at every antenatal visit. Counselling covers: {D('adequate caloric intake, iron and folic acid supplementation, calcium supplementation, and locally available nutritious foods')}. Counselling is documented in the antenatal record.

The {D('obstetric department in-charge')} holds the antenatal assessment protocol including the nutrition component.""",

f"""5.4 Peri-natal and post-natal monitoring

Appropriate peri-natal and post-natal monitoring is performed. Peri-natal monitoring includes: partograph for labour progress; foetal heart rate monitoring at intervals defined by the protocol; maternal vitals (pulse, blood pressure, temperature); and recognition of danger signs.

Post-natal monitoring includes: maternal observations for the first {D('24 hours')} (pulse, blood pressure, bleeding, uterine tone); neonatal observations (breathing, colour, temperature, feeding); and early identification of post-partum complications.

Monitoring follows written protocols held by the {D('obstetric department in-charge')} and reviewed {D('annually')}.""",

f"""5.5 Neonatal care for high-risk obstetric cases

{HOSPITAL} caring for high-risk obstetric cases has the human resources and facilities to take care of neonates of such cases. This includes: {D('neonatal resuscitation equipment (bag-valve-mask, laryngoscope, endotracheal tubes, suction, radiant warmer, pulse oximeter)')}, a paediatrician or doctor trained in neonatal resuscitation available at every high-risk delivery, and nurses trained in basic neonatal care.

Neonatal resuscitation equipment is checked {D('daily')} and after every use. The check is recorded on a dated log.

If the hospital identifies a high-risk case whose neonate will require a level of care this hospital cannot provide, the referral decision under 5.2 includes neonatal capability at the receiving centre.

The {D('obstetric department in-charge')} and {D('paediatrician or neonatal care lead')} hold the neonatal care arrangements and review them {D('annually')}.""",
]

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that obstetric services are safe and compliant as this policy requires.
- Approves obstetric protocols and referral criteria.

{D('Obstetric department in-charge')}
- Holds protocols, staffing roster, equipment inventory, high-risk criteria, referral criteria and antenatal assessment protocol.
- Reviews all of the above annually.

Obstetricians and treating doctors
- Follow written protocols for labour management and high-risk care.
- Identify high-risk cases and arrange referral where needed.
- Assess maternal nutrition at every antenatal visit.

Nurses and midwives
- Perform peri-natal and post-natal monitoring as per written protocols.
- Check neonatal resuscitation equipment daily.
- Document all monitoring and counselling.

Paediatricians (where available)
- Available at every high-risk delivery for neonatal care.
- Participate in neonatal resuscitation and post-natal assessment.

Anaesthetists (where available)
- Available for operative deliveries and obstetric emergencies.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when obstetric findings recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at records and at the labour room.

What is monitored each quarter:

- Written protocols are current and staff are trained.
- High-risk identification is performed at registration and at subsequent visits.
- Referral criteria are current and referrals are documented.
- Maternal nutrition is assessed and counselled at every antenatal visit.
- Peri-natal monitoring (partograph, foetal heart rate, maternal vitals) follows written protocols.
- Post-natal monitoring is completed for all deliveries.
- Neonatal resuscitation equipment is checked daily with a dated log.
- Staffing meets the defined requirements for every delivery.

Root-cause analysis is required when: a high-risk case is kept without competent staff and the patient suffers harm; peri-natal monitoring is omitted and an adverse outcome occurs; or neonatal resuscitation equipment is found non-functional at the time of a delivery.

This policy is reviewed {D('annually')}, and sooner when obstetric services change or a maternal or neonatal adverse event triggers a review."""

TRAINING_ACKNOWLEDGEMENT = f"""All obstetric care staff are trained on this policy at induction and {D('once a year')} after that. Training covers labour protocols, high-risk identification and referral, maternal nutrition, peri-natal and post-natal monitoring, and neonatal resuscitation.

Staff acknowledgement

I have read this Safe Obstetric Care policy of {HOSPITAL}. I will follow written protocols for labour management. I will identify high-risk cases and arrange referral where this hospital cannot manage them. I will assess maternal nutrition at every antenatal visit.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The obstetric department in-charge holds signed acknowledgements with the training record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/07"),
    version=VERSION,
    prepared_by=D("Obstetric department in-charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.7.
- Internal documents of {HOSPITAL}: obstetric protocols (labour management, operative delivery, emergencies); high-risk criteria and referral criteria; antenatal assessment protocol with nutrition; peri-natal and post-natal monitoring protocols; neonatal resuscitation equipment check log; staffing roster; COP.1 uniform care policy; PRE.3 consent policy; COP.3 CPR policy; COP.5 transfusion policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the obstetric department in-charge and the Quality Coordinator.

Copies issued to: labour room; antenatal clinic; post-natal ward; neonatal care area; nursing administration.

The current version is available to all staff at the {D('obstetric department policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """BMI — body mass index
CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
CPR — cardiopulmonary resuscitation
MUAC — mid-upper arm circumference
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
        "responsible": "Obstetric department in-charge (protocols, staffing, equipment); Medical Superintendent (accountable)",
        "records": [
            "Written obstetric protocols reviewed annually.",
            "Staffing roster showing coverage for every delivery.",
            "Equipment inventory for the labour room.",
            "Annual review records for protocols, staffing and equipment.",
        ],
    },
    {
        "oe_code": "COP.7.b",
        "requirement": "The organization identifies and provides care to high risk obstetric cases with competent doctors and nurses, and where needed, refers them to another appropriate centre.",
        "steps": "Section 3; 5.2 High-risk obstetric identification, competent care and referral; Section 4 item 2",
        "responsible": "Obstetricians and treating doctors (identify and manage or refer); obstetric department in-charge (criteria)",
        "records": [
            "Written high-risk criteria and referral criteria reviewed annually.",
            "High-risk case register showing identification, management and referral decisions.",
            "Referral documentation with reason, receiving centre and condition at transfer.",
            "List of referral centres reviewed annually.",
        ],
    },
    {
        "oe_code": "COP.7.c",
        "requirement": "Antenatal assessment also includes maternal nutrition.",
        "steps": "Section 3; 5.3 Antenatal assessment including maternal nutrition; Section 4 item 3",
        "responsible": "Obstetricians and treating doctors (assess); nurses (counsel and document); obstetric department in-charge (protocol)",
        "records": [
            "Antenatal assessment protocol including nutrition component.",
            "Nutritional status records at each antenatal visit (weight, haemoglobin, dietary history).",
            "Nutrition counselling records documented in the antenatal record.",
        ],
    },
    {
        "oe_code": "COP.7.d",
        "requirement": "Appropriate peri-natal and post-natal monitoring is performed.",
        "steps": "Section 3; 5.4 Peri-natal and post-natal monitoring; Section 4 item 4",
        "responsible": "Nurses and midwives (monitor); treating doctors (respond to danger signs)",
        "records": [
            "Partograph records for labour progress.",
            "Foetal heart rate monitoring records at protocol-defined intervals.",
            "Post-natal maternal and neonatal observation records.",
        ],
    },
    {
        "oe_code": "COP.7.e",
        "requirement": "The organization caring for high risk obstetric cases has the human resources and facilities to take care of neonates of such cases.",
        "steps": "Section 3; 5.5 Neonatal care for high-risk obstetric cases; Section 4 item 5",
        "responsible": "Paediatrician or neonatal care lead (neonatal care); obstetric department in-charge (arrangements); nurses (check equipment)",
        "records": [
            "Neonatal resuscitation equipment inventory and daily check log.",
            "Training records for neonatal resuscitation for doctors and nurses.",
            "Paediatrician or trained doctor availability records for high-risk deliveries.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.7 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Organization provides safe obstetric care." COP.7.a–d PDF page 70; COP.7.e PDF page 71. COP.7.a asterisked (Commitment). COP.7.c asterisked (Commitment). COP.7.b Commitment. COP.7.d Commitment. COP.7.e Commitment.

SHAPE: Five What-we-do subsections (5.1–5.5). No stop-work. Disclaimer accreditation-only. COP roles only."""


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
        "subtitle": "Safe obstetric care in day-to-day work.",
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
