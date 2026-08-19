# -*- coding: utf-8 -*-
"""COP.10 v2 — anaesthesia services provided consistently and safely.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 72–73.
Has stop-work section. Eight OEs in eight What-we-do subsections.
Disclaimer P2 is accreditation-only.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.10"
CHAPTER = "COP"
OE_CODES = [
    "COP.10.a", "COP.10.b", "COP.10.c", "COP.10.d",
    "COP.10.e", "COP.10.f", "COP.10.g", "COP.10.h",
]
POLICY_TITLE = "Anaesthesia Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, stop-work authority included.",
    },
]

STATEMENT_OF_INTENT = (
    "Anaesthesia services are provided consistently and safely — with pre-anaesthesia "
    "assessment, documented plan, pre-induction check, consent, intra-operative monitoring, "
    "post-anaesthesia recovery with objective discharge, documentation of agents used, "
    "and adverse-event recording."
)

PURPOSE = f"""This policy defines how {HOSPITAL} provides anaesthesia services consistently and safely, covering pre-anaesthesia assessment and plan, pre-induction assessment, informed consent, intra-operative monitoring, post-anaesthesia recovery and discharge, documentation of anaesthetic agents, and recording of intra-operative adverse anaesthesia events.

Boundaries: PRE.3 owns the consent method; this policy owns that consent was obtained before anaesthesia. COP.9 owns procedural sedation; this policy owns general, regional and local anaesthesia provided in the operating theatre or equivalent.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff involved in anaesthesia services at {HOSPITAL}: anaesthetists, OT nurses, recovery-area nurses, and treating surgeons insofar as they interact with the anaesthesia plan.

It covers anaesthesia from pre-assessment through recovery discharge. It does not cover procedural sedation outside the OT (COP.9) or the consent method (PRE.3)."""

POLICY_STATEMENT = f"""{HOSPITAL} administers anaesthesia in a consistent and safe manner. Every patient receiving anaesthesia has a pre-anaesthesia assessment documented, a formulated anaesthesia plan, a pre-induction assessment, informed consent, continuous intra-operative monitoring, post-anaesthesia monitoring with objective discharge criteria, documentation of anaesthetic type and medications, and recording of any adverse anaesthesia event.

{HOSPITAL} does not induce anaesthesia without pre-anaesthesia assessment documented, consent obtained, and monitoring in place."""

NON_NEGOTIABLES = f"""1. No anaesthesia is induced without a documented pre-anaesthesia assessment and formulated anaesthesia plan.
2. A pre-induction assessment is performed and documented immediately before induction.
3. No anaesthesia is administered without documented informed consent specific to anaesthesia.
4. Continuous monitoring (minimum: ECG, pulse oximetry, NIBP, capnography, temperature) is confirmed functional before induction.
5. No patient leaves recovery without meeting documented objective discharge criteria.
6. Every intra-operative adverse anaesthesia event is recorded and reported to the {D('Anaesthesia In-Charge')} within the same shift.
7. Staff who see a violation of items 1–4 invoke stop-work authority immediately."""

PROCEDURE_STEPS = [
f"""5.1 Consistent and safe anaesthesia administration

Anaesthesia services at {HOSPITAL} follow a documented protocol covering pre-assessment, planning, induction, maintenance, emergence and recovery. The {D('Anaesthesia In-Charge')} holds the protocol and reviews it {D('annually')}.

Anaesthesia is administered only in locations with appropriate infrastructure: {D('the operation theatre and designated procedure rooms with anaesthesia capability')}.""",

f"""5.2 Pre-anaesthesia assessment and anaesthesia plan

Every patient scheduled for anaesthesia undergoes a pre-anaesthesia assessment that results in a documented anaesthesia plan. The assessment covers airway, ASA physical status, comorbidities, medications, allergy history, previous anaesthesia history, fasting status, and relevant investigations.

The anaesthesia plan documents the anaesthesia type, technique, drugs, monitoring plan, anticipated difficulties, and contingency. The plan is documented in the patient record before induction.""",

f"""5.3 Pre-induction assessment

A pre-induction assessment is performed and documented immediately before induction in the OT or procedure room. It confirms identity, consent, fasting, airway re-check, IV access, monitoring connected, and any interval change since the pre-anaesthesia assessment.

The anaesthetist signs the pre-induction record before proceeding.""",

f"""5.4 Informed consent for anaesthesia

Informed consent specific to anaesthesia is obtained and documented before administration. The consent includes explanation of anaesthesia type, risks, alternatives, and the anaesthetist who will administer.

PRE.3 owns the consent method. This step owns that consent was obtained and is documented in the patient record. Consent is taken by the {D('anaesthetist')}.""",

f"""5.5 Intra-operative monitoring

Patients are monitored continuously while under anaesthesia. Minimum monitoring: ECG, pulse oximetry, non-invasive blood pressure, capnography (where general anaesthesia with intubation), and temperature.

Parameters are recorded at intervals of {D('every five minutes')} in the anaesthesia record. Alarms are set and not silenced. Any deviation triggers the escalation pathway.""",

f"""5.6 Post-anaesthesia monitoring and discharge

Post-anaesthesia monitoring is documented in the recovery area. Patients are discharged from recovery based on objective criteria using {D('the Modified Aldrete Score or equivalent tool')}.

Discharge criteria include {D('stable vital signs for at least 30 minutes, return to baseline consciousness, pain controlled, no active bleeding, and adequate neuromuscular recovery')}. The discharging anaesthetist or recovery doctor signs the discharge record.""",

f"""5.7 Documentation of anaesthesia type and medications

The type of anaesthesia administered (general, regional, local, combined) and all anaesthetic medications used (including doses, routes, and times) are documented in the patient record in the anaesthesia chart.

The anaesthesia chart is completed before the patient leaves the operating theatre.""",

f"""5.8 Intra-operative adverse anaesthesia events

Intra-operative adverse anaesthesia events are recorded in the anaesthesia record and in the {D('adverse event register')}. Events include but are not limited to: difficult intubation, bronchospasm, laryngospasm, anaphylaxis, hypotension requiring intervention, cardiac arrest, awareness under anaesthesia.

Events are reported to the {D('Anaesthesia In-Charge')} within the same shift. Monitoring and trend analysis are conducted {D('quarterly')} by the Quality Coordinator.""",
]

STOP_WORK = f"""Any staff member shall invoke stop-work authority and halt anaesthesia induction when:

- Pre-anaesthesia assessment is not documented or no anaesthesia plan exists.
- Informed consent for anaesthesia has not been obtained or documented.
- Minimum monitoring equipment is not available, not functional, or not connected to the patient.
- Emergency airway and resuscitation equipment is not present or not checked.

Stop-work is reported to the {D('Anaesthesia In-Charge')} immediately. Induction does not proceed until all conditions are met. No punitive action is taken against a person who invokes stop-work in good faith."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that anaesthesia services are provided consistently and safely.

Anaesthesia In-Charge
- Holds the anaesthesia protocol; maintains equipment, credentialling and adverse-event review.
- Reviews protocol and adverse-event trends annually.

Anaesthetists
- Perform pre-anaesthesia assessment, plan, pre-induction check, administer anaesthesia, monitor, and document.
- Obtain consent (that it was obtained); record adverse events same shift.

OT nurses
- Assist with monitoring setup; confirm equipment checks documented.

Recovery nurses
- Monitor post-anaesthesia; apply objective discharge criteria.

Quality Coordinator
- Audits this policy {D('quarterly')} (see monitoring section).
- Tracks CAPA when an anaesthesia safety defect recurs."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Pre-anaesthesia assessment and plan documented before induction (sample charts).
- Pre-induction assessment completed and signed.
- Consent documented before anaesthesia.
- Intra-operative monitoring records complete with all minimum parameters.
- Post-anaesthesia discharge criteria documented and met.
- Anaesthesia type and medications documented in patient record.
- Adverse events recorded and reported within same shift.
- Stop-work events reviewed; no punitive action taken.

Root-cause analysis is required when an anaesthesia safety defect recurs within six months.

This policy is reviewed {D('annually')}, and sooner when anaesthesia guidelines or equipment standards change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff involved in anaesthesia services are trained on this policy at induction and {D('once a year')} after that. Training covers the anaesthesia protocol, consent requirements, monitoring standards, adverse-event reporting, and stop-work authority.

Staff acknowledgement

I have read this Anaesthesia Services policy of {HOSPITAL}. I will provide anaesthesia services only in accordance with this policy and will invoke stop-work authority when safety conditions are not met.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Anaesthesia In-Charge holds signed acknowledgements with the credentialling file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/10"),
    version=VERSION,
    prepared_by=D("Anaesthesia In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.10.
- Indian Society of Anaesthesiologists (ISA), Minimum Monitoring Standards — adopted edition.
- World Federation of Societies of Anaesthesiologists (WFSA), International Standards for a Safe Practice of Anaesthesia — 2018 revision or later.
- Internal documents of {HOSPITAL}: anaesthesia protocol, anaesthesia chart, pre-anaesthesia assessment form, recovery discharge form, adverse-event register, equipment-check log, stop-work register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Anaesthesia In-Charge and Quality Coordinator.

Copies issued to: operation theatre; pre-anaesthesia clinic; recovery area; OT nursing station.

The current version is available to all staff at the {D('policy file in the OT')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}."""

ABBREVIATIONS = """ASA — American Society of Anesthesiologists
CAPA — corrective and preventive action
ECG — electrocardiogram
ISA — Indian Society of Anaesthesiologists
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NIBP — non-invasive blood pressure
OE — objective element
OT — operation theatre
SHCO — Standards for Small Healthcare Organisations
WFSA — World Federation of Societies of Anaesthesiologists"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.10.a",
        "requirement": "Anaesthesia services are administered in a consistent and safe manner.",
        "steps": "Section 3; 5.1 Consistent and safe anaesthesia administration; Section 4 items 1–7",
        "responsible": "Anaesthesia In-Charge (protocol); anaesthetists (administer)",
        "records": [
            "Documented anaesthesia protocol with annual review record.",
            "Infrastructure and location verification for anaesthesia capability.",
            "Sample anaesthesia charts showing protocol adherence.",
            "Credentialling list of anaesthetists.",
        ],
    },
    {
        "oe_code": "COP.10.b",
        "requirement": "The pre-anaesthesia assessment results in the formulation of an anaesthesia plan which is documented.",
        "steps": "Section 3; 5.2 Pre-anaesthesia assessment and anaesthesia plan; Section 4 item 1",
        "responsible": "Anaesthetist (assess and plan); Anaesthesia In-Charge (form design)",
        "records": [
            "Pre-anaesthesia assessment forms completed with airway, ASA status, comorbidities, fasting, allergies.",
            "Documented anaesthesia plan including type, technique, drugs, contingency.",
            "Audit sample confirming plan documented before induction.",
            "Anticipated-difficulty documentation where applicable.",
        ],
    },
    {
        "oe_code": "COP.10.c",
        "requirement": "A pre-induction assessment is performed and documented.",
        "steps": "Section 3; 5.3 Pre-induction assessment; Section 4 item 2",
        "responsible": "Anaesthetist (perform and sign)",
        "records": [
            "Pre-induction assessment record signed by anaesthetist.",
            "Confirmation of identity, consent, fasting, airway recheck, IV access, monitoring connected.",
            "Audit sample confirming pre-induction done immediately before induction.",
        ],
    },
    {
        "oe_code": "COP.10.d",
        "requirement": "Informed consent for administration of anaesthesia, is obtained.",
        "steps": "Section 3; 5.4 Informed consent for anaesthesia; Section 4 item 3",
        "responsible": "Anaesthetist (obtain consent); PRE.3 (method)",
        "records": [
            "Signed anaesthesia-specific consent forms in patient records.",
            "Audit sample confirming consent documented before anaesthesia.",
            "Recorded boundary that PRE.3 owns consent method.",
        ],
    },
    {
        "oe_code": "COP.10.e",
        "requirement": "Patients are monitored while under anaesthesia.",
        "steps": "Section 3; 5.5 Intra-operative monitoring; Section 4 item 4",
        "responsible": "Anaesthetist (monitor and record); OT nurse (equipment setup)",
        "records": [
            "Anaesthesia monitoring records with ECG, SpO2, NIBP, capnography, temperature at defined intervals.",
            "Pre-induction equipment-check log confirming monitors functional.",
            "Escalation records where deviation occurred.",
            "Alarm-management documentation.",
        ],
    },
    {
        "oe_code": "COP.10.f",
        "requirement": "Post anaesthesia monitoring is documented, and patients are discharged from the recovery area based on objective criteria.",
        "steps": "Section 3; 5.6 Post-anaesthesia monitoring and discharge; Section 4 item 5",
        "responsible": "Recovery nurses (monitor); anaesthetist or recovery doctor (discharge sign-off)",
        "records": [
            "Post-anaesthesia monitoring records in recovery area.",
            "Objective discharge scoring (Modified Aldrete or equivalent) documented.",
            "Signed discharge record by authorised clinician.",
            "Audit sample confirming criteria met before discharge.",
        ],
    },
    {
        "oe_code": "COP.10.g",
        "requirement": "The type of anaesthesia and anaesthetic medications used are documented in the patient record.",
        "steps": "Section 3; 5.7 Documentation of anaesthesia type and medications",
        "responsible": "Anaesthetist (document); OT nurse (verify chart complete before patient leaves OT)",
        "records": [
            "Anaesthesia chart with type, all medications, doses, routes and times.",
            "Chart completion verified before patient leaves OT.",
            "Audit sample confirming documentation in patient record.",
        ],
    },
    {
        "oe_code": "COP.10.h",
        "requirement": "Intra-operative adverse anaesthesia events are recorded and monitored.",
        "steps": "Section 3; 5.8 Intra-operative adverse anaesthesia events; Section 4 item 6",
        "responsible": "Anaesthetist (record and report); Quality Coordinator (trend analysis)",
        "records": [
            "Adverse-event entries in anaesthesia record and adverse-event register.",
            "Same-shift reporting to Anaesthesia In-Charge documented.",
            "Quarterly trend analysis by Quality Coordinator.",
            "CAPA records where events recurred.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.10 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Anaesthesia services are provided consistently and safely." COP.10.a–h PDF indices 72–73. Asterisked OEs: a, b, e, f. Levels: b Core, h Achievement, rest Commitment.

SHAPE: Eight What-we-do subsections (5.1–5.8). Stop-work: YES. Disclaimer accreditation-only. COP anaesthesia roles."""


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
        "subtitle": "Consistent and safe anaesthesia services.",
        "doc_no": D("COP/POL/10"),
        "stop_work": STOP_WORK,
    }
    emit_pre_v2(
        draft,
        "cop10_v2_draft.json",
        "COP.10_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
