# -*- coding: utf-8 -*-
"""COP.3 v2 — cardiopulmonary resuscitation services.

Shape follows PRE.1 v2 (section list and order only). Wording from COP.3 OEs
(NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed pages 68–69 / PDF indices 68–69.

Stop-work section present. Disclaimer accreditation-only. Four OEs (COP.3.a–d).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.3"
CHAPTER = "COP"
OE_CODES = ["COP.3.a", "COP.3.b", "COP.3.c", "COP.3.d"]
POLICY_TITLE = "Cardiopulmonary Resuscitation Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: plain English, COP roles, four OEs, stop-work, accreditation-only disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Cardiopulmonary resuscitation services are provided uniformly across the organization — "
    "not a crash cart that is sealed but never checked, and not a code team that has never drilled together."
)

PURPOSE = f"""This policy says how {HOSPITAL} provides cardiopulmonary resuscitation (CPR) services uniformly across the organisation.

It covers four elements: availability of resuscitation services at all times; assigned roles and responsibilities during CPR with recorded events; equipment and medications for CPR available in various areas; and a multidisciplinary committee that does post-event analysis with corrective and preventive measures.

The chapter intent is that CPR is available, structured, equipped, and reviewed — not a crash cart gathering dust.

This policy owns CPR. COP.2 owns emergency department operations. MOM owns medication management. COP.6 owns ICU care.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to every area of {HOSPITAL} where a patient or visitor may suffer a cardiopulmonary arrest, and to every staff member who may respond: treating doctors, nurses, the {D('CPR committee')}, anaesthetists where available, and the Medical Superintendent.

It covers the four elements COP.3.a–d name. It does not cover emergency department operations (COP.2), medication management (MOM), or ICU care (COP.6).

Boundaries with other policies of {HOSPITAL}:

- COP.2 owns emergency department operations. This policy owns CPR wherever it occurs, including in the emergency department.
- MOM owns medication management. This policy owns that CPR medications are available and checked on the crash cart.
- COP.6 owns ICU care. This policy owns CPR in the ICU as in any other area."""

POLICY_STATEMENT = f"""{HOSPITAL} makes resuscitation services available to patients at all times in every area of the hospital. A code can be called from any ward, out-patient area, emergency department or corridor.

During CPR, assigned roles and responsibilities are complied with, and the events during CPR are recorded. The code team has defined roles: {D('team leader, airway, chest compressions, medications, recorder')}. Events are recorded contemporaneously, not reconstructed after the fact.

Equipment and medications for use during CPR are available in various areas of the organisation. Crash carts are placed at {D('emergency department, each in-patient ward and ICU where it exists')}. Each crash cart is checked {D('daily')} for seal, expiry and completeness. A crash cart that is sealed but never checked is not compliant.

A multidisciplinary {D('CPR committee')} does a post-event analysis of all cardiopulmonary resuscitations, and corrective and preventive measures are taken based on this analysis.

{HOSPITAL} does not treat any of these as meeting this policy: a crash cart that has not been checked since the last seal was placed; a CPR event with no contemporaneous record; or a post-event analysis that leads to no corrective action."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no shift convenience exception.

1. Leaving a patient in cardiac arrest without initiating CPR while waiting for the code team to arrive. Any trained staff member initiates basic life support immediately.
2. Using a CPR crash cart without checking that it is stocked, sealed and within expiry. A cart found unstocked or with expired medications is a finding.
3. Conducting CPR without a contemporaneous record of events, interventions, medications given and times.
4. Omitting post-event analysis for any CPR event, or conducting an analysis that identifies no corrective or preventive measures when deficiencies existed.

Staff who see one of these acts report it the same shift to the {D('CPR committee chairperson')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Availability of resuscitation services at all times

Resuscitation services are available to patients at all times — day, night, weekends and holidays. A code can be called from any area by any staff member using {D('the code announcement system or emergency extension number')}.

The code team responds within {D('the defined response time')}. The team includes at least {D('one doctor trained in advanced life support and one nurse trained in basic life support')}. Where an anaesthetist is available, the anaesthetist leads airway management.

All clinical staff are trained in basic life support at induction and {D('annually')}. The {D('CPR committee')} holds the training records and the code-call protocol.""",

f"""5.2 Assigned roles, compliance and event recording during CPR

During CPR, the code team follows assigned roles: {D('team leader, airway, chest compressions, medications, recorder')}. The team leader directs the resuscitation. Each member knows their role before the code begins.

Events during CPR are recorded contemporaneously by the recorder: time of arrest, time of code call, interventions, medications given with dose and time, rhythm checks, and outcome. The record is completed before the team disperses. A record reconstructed from memory hours later is not contemporaneous.

The completed CPR record is filed in the patient's medical record and a copy sent to the {D('CPR committee')} for post-event analysis.""",

f"""5.3 CPR equipment and medications in various areas

Equipment and medications for use during CPR are available in various areas of the organisation. Crash carts are placed at {D('emergency department, each in-patient ward and ICU where it exists')}.

Each crash cart contains at minimum: {D('bag-valve-mask, oropharyngeal airways, laryngoscope, endotracheal tubes, suction, defibrillator or access to defibrillator, IV cannulae, syringes, and emergency medications as per the hospital CPR drug list')}.

Each crash cart is checked {D('daily')} by the duty nurse for: seal intact, all items present, no expired medications, defibrillator functional. The check is recorded on a dated log attached to the cart.

Medications on the crash cart follow the {D('hospital CPR drug list reviewed annually')} by the CPR committee. MOM owns medication management as a system; this policy owns that CPR medications are on the cart and within expiry.""",

f"""5.4 Post-event analysis by a multidisciplinary committee

A multidisciplinary {D('CPR committee')} does a post-event analysis of all cardiopulmonary resuscitations. The committee includes at least {D('one physician, one nurse and the Quality Coordinator')}.

The analysis reviews: response time; adherence to assigned roles; quality of chest compressions and airway management; appropriateness of medications; accuracy of the contemporaneous record; and outcome. The committee identifies what went well and what needs corrective or preventive action.

Corrective and preventive actions are documented, assigned an owner and a due date, and tracked to closure. The committee meets {D('within one week of each CPR event')} and reports findings to the Medical Superintendent {D('quarterly')}.

Aggregate trends — survival rates, common deficiencies, equipment failures — are reviewed {D('annually')} to inform training and equipment decisions.""",
]

STOP_WORK = f"""Do not go ahead if you are about to do any of the following:

- leave a patient in cardiac arrest without initiating CPR;
- use a CPR crash cart without checking that it is stocked and sealed;
- continue a resuscitation using a defibrillator known to be non-functional without obtaining a replacement;
- sign a crash-cart check sheet for a cart you did not actually check.

If you find a crash cart unstocked or with expired medications, remove the cart from service and replace it. Tell the {D('CPR committee chairperson')} the same shift. If that person is not on site, tell the {D('duty medical officer')}.

Refusing in good faith to use an unchecked or unstocked crash cart is not a disciplinary matter."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that CPR services are available, equipped and reviewed as this policy requires.

{D('CPR committee')} (multidisciplinary)
- Holds the code-call protocol, training records, crash-cart placement plan and CPR drug list.
- Conducts post-event analysis of every CPR event.
- Tracks corrective and preventive actions to closure.
- Reports findings to the Medical Superintendent quarterly.

Treating doctors
- Respond to code calls and fulfil assigned roles during CPR.
- Complete the contemporaneous CPR record.

Nurses
- Check crash carts daily and record the check.
- Initiate basic life support when a cardiac arrest is identified.
- Call the code and assist during CPR in assigned roles.

Anaesthetists (where available)
- Lead airway management during CPR.

Quality Coordinator
- Participates in the CPR committee.
- Audits this policy {D('quarterly')} (see monitoring section)."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at records and at the floor.

What is monitored each quarter:

- Code-call system is functional and known to all clinical staff.
- Code team response times are within the defined target.
- Crash carts at all designated locations are checked daily with a dated log.
- No expired medications or missing items on crash carts.
- CPR records are contemporaneous and complete.
- Post-event analysis is conducted for every CPR event with documented corrective and preventive actions.

Root-cause analysis is required when: a crash cart is found unstocked or expired at the time of a code; the code team response time exceeds the target; or the same deficiency recurs in two consecutive post-event analyses.

This policy is reviewed {D('annually')}, and sooner when the CPR committee identifies a systemic issue or the CPR drug list is revised."""

TRAINING_ACKNOWLEDGEMENT = f"""All clinical staff are trained in basic life support at induction and {D('once a year')} after that. Code team members are trained in advanced life support. Training covers assigned roles, the code-call protocol, crash-cart checking, contemporaneous recording, and stop-work authority.

Staff acknowledgement

I have read this Cardiopulmonary Resuscitation Services policy of {HOSPITAL}. I will initiate basic life support immediately on identifying a cardiac arrest. I will not use a crash cart without checking that it is stocked and sealed.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The CPR committee holds signed acknowledgements with the training record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/03"),
    version=VERSION,
    prepared_by=D("CPR committee chairperson"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.3.
- Internal documents of {HOSPITAL}: code-call protocol; crash-cart placement plan and daily check log; CPR drug list; post-event analysis records; training records; COP.2 emergency department policy; MOM medication management policy; COP.6 ICU policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the CPR committee chairperson and the Quality Coordinator.

Copies issued to: emergency department; each in-patient ward; ICU where it exists; nursing administration; anaesthesia department where it exists.

The current version is available to all staff at the {D('quality office policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """BLS — basic life support
CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
CPR — cardiopulmonary resuscitation
ICU — intensive care unit
IV — intravenous
MOM — Management of Medication (NABH SHCO chapter 6)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "COP.3.a",
        "requirement": "Resuscitation services are available to patients at all times.",
        "steps": "Section 3; 5.1 Availability of resuscitation services at all times",
        "responsible": "CPR committee (protocol and training); all clinical staff (respond)",
        "records": [
            "Code-call protocol naming the announcement system and response time.",
            "Code team roster showing coverage at all times.",
            "Basic life support training records for all clinical staff at induction and annually.",
        ],
    },
    {
        "oe_code": "COP.3.b",
        "requirement": "During cardiopulmonary resuscitation, assigned roles and responsibilities are complied with, and the events during cardiopulmonary resuscitation are recorded.",
        "steps": "Section 3; 5.2 Assigned roles, compliance and event recording during CPR; Section 4 item 3",
        "responsible": "Code team members (assigned roles); recorder (contemporaneous record); CPR committee (review)",
        "records": [
            "Defined role assignments for the code team.",
            "Contemporaneous CPR event records filed in patient records.",
            "Copy of each CPR record sent to the CPR committee.",
        ],
    },
    {
        "oe_code": "COP.3.c",
        "requirement": "The equipment and medications for use during cardiopulmonary resuscitation are available in various areas of the organization.",
        "steps": "Section 3; 5.3 CPR equipment and medications in various areas; Section 4 item 2",
        "responsible": "CPR committee (drug list and placement plan); duty nurse (daily check); MOM (medication system)",
        "records": [
            "Crash-cart placement plan naming locations.",
            "Daily crash-cart check logs with date, seal, expiry and completeness.",
            "Hospital CPR drug list reviewed annually.",
            "Defibrillator functional check records.",
        ],
    },
    {
        "oe_code": "COP.3.d",
        "requirement": "A multidisciplinary committee does a post-event analysis of all cardiopulmonary resuscitations, and corrective and preventive measures are taken based on this.",
        "steps": "Section 3; 5.4 Post-event analysis by a multidisciplinary committee; Section 4 item 4",
        "responsible": "CPR committee (analysis and CAPA); Medical Superintendent (quarterly review)",
        "records": [
            "Post-event analysis report for every CPR event within one week.",
            "Corrective and preventive action records with owner, due date and closure.",
            "Quarterly report to Medical Superintendent.",
            "Annual aggregate trend review.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.3 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Cardio-pulmonary resuscitation services are provided uniformly across the organization." COP.3.a–d PDF pages 68–69. COP.3.d Core. All others Commitment. No asterisked OEs.

SHAPE: Four What-we-do subsections (5.1–5.4). Stop-work present. Disclaimer accreditation-only. COP roles only."""


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
        "stop_work": STOP_WORK,
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
        "subtitle": "CPR services uniformly across the organisation.",
        "doc_no": D("COP/POL/03"),
    }
    emit_pre_v2(
        draft,
        "cop3_v2_draft.json",
        "COP.3_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
