# -*- coding: utf-8 -*-
"""COP.5 v2 — transfusion services.

Shape follows PRE v2 adoptable-policy template. Wording from NABH SHCO 3rd Edition
PDF (md5 39e3bc86d73d651b9cfef283bbf018a9), PDF indices 69–70.
Stop-work section present. Six OEs (COP.5.a–f).
Disclaimer P2 names the Drugs and Cosmetics Act, 1940 / Rules, 1945.
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "COP.5"
CHAPTER = "COP"
OE_CODES = [
    "COP.5.a", "COP.5.b", "COP.5.c", "COP.5.d", "COP.5.e", "COP.5.f",
]
POLICY_TITLE = "Transfusion Services"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "COP v2 template: adoptable shape, plain English, stop-work, Drugs and Cosmetics Act disclaimer.",
    },
]

STATEMENT_OF_INTENT = (
    "Transfusion services are provided as per the scope of services of the organization, "
    "safely — not a blood bank that issues units without identity verification or "
    "compatibility testing."
)

PURPOSE = f"""This policy defines how {HOSPITAL} provides transfusion services safely, in accordance with applicable laws and regulations.

It covers six elements: transfusion services commensurate with the services provided and governed by applicable laws and regulations; safe transfusion of blood and blood components; rational use of blood and blood components; informed consent for transfusion and donation; availability of blood and blood components for emergencies within a defined time frame; and post-transfusion form collection with reaction identification and analysis.

Boundaries: MOM owns medication management; this policy owns blood and blood-component transfusion. COP.2 owns emergency clinical care; this policy owns emergency blood availability.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to all staff at {HOSPITAL} involved in transfusion services: treating doctors who order transfusions, nurses who administer them, laboratory staff who perform compatibility testing, and the blood bank or blood-storage centre where one exists.

It covers the six elements COP.5.a–f name. It does not cover medication management (MOM) or emergency clinical care (COP.2).

Boundaries with other policies of {HOSPITAL}:

- MOM owns medication management. This policy owns blood and blood-component transfusion as a clinical service.
- COP.2 owns emergency clinical care. This policy owns that blood and blood components are available for emergencies within a defined time frame.
- PRE.3 owns the consent method. This policy owns that informed consent is obtained for transfusion and for donation."""

POLICY_STATEMENT = f"""{HOSPITAL} provides transfusion services commensurate with the services it provides. Transfusion services are governed by the applicable laws and regulations, including the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, insofar as blood and blood components are procured, stored and transfused under those rules.

{HOSPITAL} transfuses blood and blood components safely. Every transfusion follows identity verification, compatibility testing, and monitoring for reactions. No unit is transfused without verification of the patient's identity using at least two identifiers, cross-match or compatibility confirmation, and visual inspection of the unit.

{HOSPITAL} uses blood and blood components rationally. Blood is not ordered when alternatives exist, and components are used rather than whole blood when clinically appropriate. A blood-utilisation review is conducted {D('quarterly')}.

Informed consent is obtained before transfusion and before donation. Consent covers the purpose, risks, benefits, and alternatives. Consent is documented in the patient record.

Blood and blood components are available for use in emergency situations within {D('30 minutes')} of a validated request. The emergency blood release process is documented.

Post-transfusion forms are collected, reactions are identified and analysed, and corrective and preventive actions are taken.

{HOSPITAL} does not treat any of these as meeting this policy: a transfusion without identity verification; a unit issued without compatibility testing; blood ordered without clinical justification; or a transfusion reaction that is not investigated."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no convenience exception.

1. Transfusing blood or blood components without verifying the patient's identity using at least two identifiers at the bedside.
2. Transfusing blood or blood components without a completed compatibility test or cross-match, except in a documented life-threatening emergency with the treating doctor's written authorisation.
3. Issuing or transfusing a unit that has not been visually inspected for discolouration, clots, or damage.
4. Ordering whole blood when component therapy is clinically appropriate and available.
5. Transfusing without documented informed consent, except in a documented life-threatening emergency.
6. Failing to monitor the patient during the first {D('15 minutes')} of a transfusion.
7. Failing to report and investigate a suspected transfusion reaction.

Staff who see one of these acts report it the same shift to the {D('blood bank in-charge')} or the Medical Superintendent."""

PROCEDURE_STEPS = [
f"""5.1 Transfusion services commensurate with scope and governed by law

{HOSPITAL} provides transfusion services commensurate with the services it provides. Where a blood bank is operated, it is licensed as required. Where blood is procured from an external licensed blood bank, there is a documented agreement that includes supply, quality, traceability and recall.

The {D('blood bank in-charge or pathologist')} ensures compliance with the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, insofar as they apply. Compliance records are maintained and reviewed {D('annually')}.

The Medical Superintendent holds overall accountability for transfusion services.""",

f"""5.2 Safe transfusion of blood and blood components

Every transfusion follows a bedside verification process: the administering nurse verifies the patient's identity using at least two identifiers, confirms compatibility with the cross-match report, and visually inspects the unit. A second person ({D('another nurse or the treating doctor')}) independently verifies before the transfusion begins.

The patient is monitored during the first {D('15 minutes')} of transfusion and at intervals thereafter as per the hospital protocol. Vital signs are recorded before, during, and after transfusion.

Blood and blood components are stored, transported and handled as per the manufacturer's or blood bank's instructions. The cold chain is maintained and documented.""",

f"""5.3 Rational use of blood and blood components

Blood and blood components are used rationally. The treating doctor documents the clinical indication for every transfusion order. Blood is not ordered when alternatives such as iron infusion or erythropoietin exist and are clinically appropriate. Components are preferred over whole blood when clinically appropriate.

A blood-utilisation review committee or the {D('Quality Coordinator')} reviews transfusion appropriateness {D('quarterly')}. Findings of inappropriate use are fed back to the ordering doctor and used for education.

The {D('blood bank in-charge')} maintains a transfusion register that links patient, indication, component, and outcome.""",

f"""5.4 Informed consent for transfusion and donation

Informed consent is obtained before transfusion of blood and blood products and before donation. Consent for transfusion covers: the purpose of transfusion, the blood component to be transfused, common risks and potential reactions, alternatives, and the right to refuse. Consent for donation covers: the donation process, potential side-effects, and the tests that will be performed on donated blood.

Consent is obtained by the treating doctor or a trained nurse and documented in the patient record. For donation, consent is documented in the donation record.

Emergency transfusion without prior consent is permitted only when a delay would endanger the patient's life, and the treating doctor documents the justification.""",

f"""5.5 Emergency blood availability

Blood and blood components are available for use in emergency situations within {D('30 minutes')} of a validated request. The emergency blood release process is documented and covers: who may request emergency release, verification steps that may be abbreviated, documentation of the abbreviated process, and retrospective completion of compatibility testing.

The {D('blood bank in-charge')} ensures that emergency stock ({D('at least 2 units of O-negative packed red cells or as defined by the hospital')}) is maintained at all times. Stock levels are checked {D('every shift')}.

The emergency release process is drilled {D('annually')} and results are documented.""",

f"""5.6 Post-transfusion form and reaction management

A post-transfusion form is collected for every transfusion. The form records: patient identification, component transfused, start and end times, volume transfused, vital signs, and whether a reaction occurred.

Transfusion reactions are identified, graded, reported to the {D('blood bank in-charge')} immediately, and investigated. Investigation includes: type of reaction, clinical management, blood bank investigation (re-cross-match, direct antiglobulin test, culture if febrile), and root-cause determination.

Reaction data is analysed {D('quarterly')} by the {D('Quality Coordinator')} for trends. Corrective and preventive actions are implemented and tracked to closure.""",
]

STOP_WORK = f"""Do not go ahead if you are about to do any of the following:

- transfuse blood or a blood component without verifying the patient's identity using at least two identifiers;
- transfuse without a completed compatibility test or cross-match (except documented life-threatening emergency with written authorisation);
- continue a transfusion when a reaction is suspected — stop the transfusion, maintain IV access, and notify the treating doctor immediately.

If you can do so safely, keep the patient monitored and the unit preserved for investigation. Tell the {D('blood bank in-charge')} the same shift. If that person is not on site, tell the Medical Superintendent.

Refusing in good faith to transfuse without proper verification is not a disciplinary matter."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Accountable that transfusion services are provided safely and in accordance with applicable laws.
- Holds overall governance of transfusion services.

{D('Blood bank in-charge or pathologist')}
- Ensures compliance with the Drugs and Cosmetics Act and Rules.
- Maintains the transfusion register, emergency stock, and reaction investigation records.
- Reviews emergency blood release drill results.

Treating doctors
- Document clinical indication for every transfusion order.
- Obtain informed consent for transfusion.
- Respond to transfusion reactions.

Nurses
- Perform bedside identity verification and compatibility confirmation before transfusion.
- Monitor the patient during and after transfusion.
- Collect the post-transfusion form.
- Report suspected reactions immediately.

{D('Quality Coordinator')}
- Audits this policy {D('quarterly')} (see monitoring section).
- Reviews blood-utilisation data and reaction trends.
- Tracks CAPA for transfusion safety defects."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit covers:

- Bedside identity verification and compatibility confirmation documented for sampled transfusions.
- Clinical indication documented for every transfusion order (sample).
- Informed consent for transfusion and donation documented.
- Emergency blood availability within the defined time frame tested or drilled.
- Post-transfusion forms collected for all transfusions.
- Transfusion reactions reported, investigated, and CAPA implemented.
- Blood-utilisation review findings and follow-up actions.

Root-cause analysis is required when a transfusion safety event (wrong blood, missed reaction, compatibility failure) occurs or when the same finding recurs within six months.

This policy is reviewed {D('annually')}, and sooner when the Drugs and Cosmetics Rules are amended or the scope of transfusion services changes."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff involved in transfusion services are trained on this policy at induction and {D('once a year')} after that. Training covers bedside verification, safe transfusion, rational use, consent, emergency release, and reaction identification and reporting.

Staff acknowledgement

I have read this Transfusion Services policy of {HOSPITAL}. I will verify patient identity and compatibility before every transfusion. I will report suspected transfusion reactions immediately.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The blood bank in-charge holds signed acknowledgements with the training file.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("COP/POL/05"),
    version=VERSION,
    prepared_by=D("Blood bank in-charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Care of Patients chapter, standard COP.5.
- Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, insofar as blood and blood components are procured, stored and transfused under those rules.
- Internal documents of {HOSPITAL}: transfusion protocol, blood-bank agreement (if external), emergency blood release process, blood-utilisation review records, transfusion reaction investigation records, transfusion consent form, donation consent form."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('blood bank in-charge')} and the Quality Coordinator.

Copies issued to: blood bank or blood-storage centre; every in-patient ward; ICU; emergency department; operation theatre; nursing administration.

The current version is available to all staff at the {D('blood bank policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """CAPA — corrective and preventive action
COP — Care of Patients (NABH SHCO chapter 5)
DVT — deep vein thrombosis
ICU — intensive care unit
IV — intravenous
MOM — Management of Medication (NABH SHCO chapter 6)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = "the Drugs and Cosmetics Act, 1940 and the Drugs and Cosmetics Rules, 1945, insofar as blood and blood components are procured, stored and transfused under those rules"
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "COP.5.a",
        "requirement": "Transfusion services are commensurate with the services provided by the organization, and are governed by the applicable laws and regulations.",
        "steps": "Section 3; 5.1 Transfusion services commensurate with scope and governed by law",
        "responsible": "Medical Superintendent (accountability); blood bank in-charge (compliance)",
        "records": [
            "Blood bank licence or documented agreement with external licensed blood bank.",
            "Compliance records with the Drugs and Cosmetics Act and Rules reviewed annually.",
            "Transfusion register linking patient, indication, component, and outcome.",
        ],
    },
    {
        "oe_code": "COP.5.b",
        "requirement": "Transfusion of blood and blood components is done safely.",
        "steps": "Section 3; 5.2 Safe transfusion of blood and blood components; Section 4 items 1–3; Section 6 stop-work",
        "responsible": "Nurses (bedside verification and monitoring); treating doctors (order and respond to reactions)",
        "records": [
            "Bedside verification checklist for each transfusion documenting two-identifier check, compatibility confirmation, and visual inspection.",
            "Vital signs recorded before, during, and after transfusion.",
            "Cold-chain maintenance and transport records.",
            "Second-person independent verification documented.",
        ],
    },
    {
        "oe_code": "COP.5.c",
        "requirement": "Blood and blood components are used rationally.",
        "steps": "Section 3; 5.3 Rational use of blood and blood components; Section 4 item 4",
        "responsible": "Treating doctors (clinical indication); Quality Coordinator (utilisation review)",
        "records": [
            "Clinical indication documented for each transfusion order.",
            "Quarterly blood-utilisation review findings and feedback records.",
            "Records of component therapy preference over whole blood where appropriate.",
        ],
    },
    {
        "oe_code": "COP.5.d",
        "requirement": "Informed consent is obtained for transfusion of blood and blood products, and for donation.",
        "steps": "Section 3; 5.4 Informed consent for transfusion and donation; Section 4 item 5",
        "responsible": "Treating doctors (obtain consent); nurses (verify and document)",
        "records": [
            "Signed transfusion consent form in the patient record covering purpose, risks, benefits, and alternatives.",
            "Signed donation consent form in the donation record.",
            "Emergency transfusion without consent: treating doctor's written justification documented.",
        ],
    },
    {
        "oe_code": "COP.5.e",
        "requirement": "Blood/blood components are available for use in emergency situations within a defined time frame.",
        "steps": "Section 3; 5.5 Emergency blood availability",
        "responsible": "Blood bank in-charge (stock and release process); emergency department (request)",
        "records": [
            "Emergency blood stock levels checked and documented every shift.",
            "Emergency release process document with defined time frame.",
            "Annual drill of emergency blood release with results documented.",
        ],
    },
    {
        "oe_code": "COP.5.f",
        "requirement": "Post-transfusion form is collected, reactions if any identified and are analysed for corrective and preventive actions.",
        "steps": "Section 3; 5.6 Post-transfusion form and reaction management; Section 4 item 7",
        "responsible": "Nurses (collect form, report reactions); blood bank in-charge (investigate); Quality Coordinator (trend analysis)",
        "records": [
            "Post-transfusion form for every transfusion with patient ID, component, times, volume, vitals, and reaction status.",
            "Transfusion reaction investigation records with re-cross-match and root-cause determination.",
            "Quarterly reaction trend analysis with CAPA records.",
            "Training records on reaction identification and reporting.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """COP.5 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Transfusion services are provided as per the scope of services of the organization, safely." COP.5.a–f PDF indices 69–70. Asterisked OEs: b, c, e. Levels: b Core, rest Commitment except f Achievement.

SHAPE: Six What-we-do subsections (5.1–5.6). Stop-work present. Disclaimer names Drugs and Cosmetics Act 1940 / Rules 1945. COP clinical roles."""


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
        "subtitle": "Safe transfusion services governed by applicable laws.",
        "doc_no": D("COP/POL/05"),
    }
    emit_pre_v2(
        draft,
        "cop5_v2_draft.json",
        "COP.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
