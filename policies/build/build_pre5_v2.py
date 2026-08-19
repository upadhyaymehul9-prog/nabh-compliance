# -*- coding: utf-8 -*-
"""PRE.5 v2 — information on expected costs.

Wording from PRE.5 OEs (NABH SHCO 3rd Edition PDF, md5 39e3bc86d73d651b9cfef283bbf018a9),
printed page 89 / PDF index 95. No stop-work. Disclaimer accreditation-only (v2 template).
"""
from __future__ import annotations

import sys

from policy_build_common import make_disclaimer_accreditation_only
from pre_v2_common import BLANK, D, HOSPITAL, document_control, emit_pre_v2

STANDARD_CODE = "PRE.5"
CHAPTER = "PRE"
OE_CODES = ["PRE.5.a", "PRE.5.b", "PRE.5.c", "PRE.5.d"]
POLICY_TITLE = "Information on Expected Costs"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PRE v2 template: four steps, billing role, no stop-work, accreditation-only P2.",
    },
]

STATEMENT_OF_INTENT = (
    "Expected costs of treatment and care are explained clearly — "
    "not a tariff locked in accounts that the family never sees."
)

PURPOSE = f"""This policy says how {HOSPITAL} makes patients and families aware of the pricing policy in different settings; makes the relevant tariff list available; explains expected costs; and informs them of financial implications when the care plan changes.

The right to cost information is PRE.2.i. Promotion of that right is PRE.1. This policy owns the figures and the explanation. It is not the billing ledger.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

SCOPE = f"""This policy applies wherever a patient may incur a charge: registration, out-patient, emergency, ICU if it exists, and in-patient.

It binds {D('billing and front-desk staff')}, registration, treating doctors when a plan change affects cost, the {D('Patient Rights Officer')} as cost-information lead, and the {D('Quality Coordinator')}.

Boundaries:

- PRE.2.i lists the right; this policy owns tariff and explanation.
- AAC.3 and PRE.2.o own clinical care-plan change; PRE.5.d owns the money of that change.
- PRE.3 signed consent is not agreement to an unnamed bill.
- ROM/FMS billing ledger is not this patient-facing explanation."""

POLICY_STATEMENT = f"""{HOSPITAL} makes the patient and/or family aware of the pricing policy in out-patient, emergency, ICU (where it exists) and in-patient settings.

{HOSPITAL} makes the relevant tariff list available to patients.

{HOSPITAL} explains expected costs to the patient and/or family.

{HOSPITAL} informs the patient and/or family about financial implications when there is a change in the care plan.

{HOSPITAL} does not treat a signed consent or a hidden tariff as a substitute for that explanation."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Withholding the pricing policy or tariff from a patient who asks.
2. Keeping the only tariff copy in finance where patients cannot see it without an escort as the only route.
3. Changing the care plan in a way that increases cost without telling the family.
4. Offering signed consent as the cost conversation.
5. Printing rupee figures as NABH mandates in this policy.

Staff report defects to the {D('Patient Rights Officer')} or {D('Medical Superintendent')}."""

PROCEDURE_STEPS = [
f"""5.1 Pricing policy in different settings

The patient and/or family members are made aware of the pricing policy in different settings (out-patient, emergency, ICU and in-patient).

The pricing policy for each setting this hospital runs — itemised, package, or mix — is held by {D('billing and front-desk staff')} with the Patient Rights Officer. Patients are told at {D('registration or admission')} in {D('Hindi and English')}. ICU not provided is a recorded absence. Emergency awareness may follow stabilisation; delay and reason are recorded.""",

f"""5.2 Relevant tariff list available to patients

The relevant tariff list is available to patients.

The list is at {D('registration, billing counter, and a board patients can read without an accounts-office escort as the only route')}. Which list applies in each setting is named on the board or handout.""",

f"""5.3 Expected costs explained

The patient and/or family members are explained about the expected costs.

Explanation is when the patient enters a billable pathway, before a package procedure, and when asked — by {D('billing staff or the admitting nurse')}. A range or package with inclusions and exclusions is an explanation; "charges extra" without a figure or route to the tariff is not. Language is one the family can understand.""",

f"""5.4 Financial implications when the care plan changes

Patient and/or family are informed about the financial implications when there is a change in the care plan.

When the treating doctor changes the plan in a way that changes cost, {D('the nurse or doctor tells the family the same day')} and billing records it. Clinical modification remains AAC.3 / PRE.2.o; this step is the money.""",
]

RESPONSIBILITY = f"""Medical Superintendent — accountable for patient-facing cost information.

Patient Rights Officer (with billing lead)
- Holds pricing policy, tariff availability and explanation methods.

Billing / front-desk staff — make policy and tariff visible; explain expected costs.

Doctors and nurses — tell financial implications when the plan change changes cost.

Quality Coordinator — audits {D('quarterly')}."""

MONITORING_AUDIT = f"""The Quality Coordinator audits {D('quarterly')} for: pricing-policy awareness per setting; tariff a patient can actually see; expected-cost explanation recorded; financial implications told when plan changed cost; no consent offered as the cost talk.

Reviewed {D('annually')} or when PRE.2 or AAC.3 change."""

TRAINING_ACKNOWLEDGEMENT = f"""Registration and billing staff train at induction and {D('once a year')} on pricing policy, tariff location and how to explain a package.

Staff acknowledgement — I will not hide the tariff or bill against a plan the family was not told had changed.


Name: ___________________________    Designation: ___________________________

Date: ____________    Signature: ___________________________


(Billing lead holds acknowledgements with Patient Rights Officer.)"""

DOCUMENT_CONTROL = document_control(
    doc_no=D("PRE/POL/05"),
    version=VERSION,
    prepared_by=D("Patient Rights Officer"),
    extra_lines=f"Tariff display locations: {D('registration and billing counter')}",
)

REFERENCES = f"""- NABH SHCO 3rd Edition — standard PRE.5.
- Internal documents of {HOSPITAL}: pricing policy; tariff list; expected-cost explanation method; care-plan-change financial method; PRE.2 and PRE.3 policies."""

DISTRIBUTION = f"""Master copy: Medical Superintendent, Patient Rights Officer, Quality Coordinator.

Copies: registration, billing, out-patient, emergency, wards, ICU if exists.

Tariff and pricing policy at {D('registration and billing counter')}. Policy file at {D('front-office policy file')}."""

ABBREVIATIONS = """ICU — intensive care unit
NABH — National Accreditation Board for Hospitals and Healthcare Providers
PRE — Patient Rights and Education
SHCO — Standards for Small Healthcare Organisations"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PRE.5.a",
        "requirement": "The patient and/or family members are made aware of the pricing policy in different settings (out-patient, emergency, ICU and in-patient).",
        "steps": "Statement of intent; Section 3; 5.1 Pricing policy in different settings",
        "responsible": "Billing staff and Patient Rights Officer (policy); registration (awareness at entry)",
        "records": [
            "Written pricing policy for each setting run, or recorded absence for ICU etc.",
            "Method of making patients and families aware at those settings.",
            "Sample awareness records including delayed emergency awareness with reason.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.5.b",
        "requirement": "The relevant tariff list is available to patients.",
        "steps": "Section 3; 5.2 Tariff list available",
        "responsible": "Billing lead (tariff); Patient Rights Officer (availability method)",
        "records": [
            "Named locations where tariff is available in each setting.",
            "Evidence route is not only accounts-office escort.",
            "Current tariff version date on display.",
            "Quarterly audit sample of a list patients can actually see.",
        ],
    },
    {
        "oe_code": "PRE.5.c",
        "requirement": "The patient and/or family members are explained about the expected costs.",
        "steps": "Section 3; 5.3 Expected costs explained",
        "responsible": "Billing staff or admitting nurse (explain); Patient Rights Officer (method)",
        "records": [
            "Written explanation method — when, by whom, how recorded.",
            "Sample explanations with range or package inclusions/exclusions.",
            "Record that signed consent is not this explanation.",
            "Quarterly audit sample.",
        ],
    },
    {
        "oe_code": "PRE.5.d",
        "requirement": "Patient and/or family are informed about the financial implications when there is a change in the care plan.",
        "steps": "Section 3; 5.4 Financial implications of care-plan change",
        "responsible": "Doctor or nurse (tell when cost changes); billing (record)",
        "records": [
            "Written method for informing when care-plan change changes cost.",
            "Sample records of plan changes that changed cost being told same day.",
            "Recorded split that AAC.3/PRE.2.o own clinical modification.",
            "Quarterly audit sample.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PRE.5 v2 (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9. No asterisked OEs. Accreditation-only P2 (v2 template). No stop-work. Patient-facing cost only — not ledger."""


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
        "template_test": "pre_v2_adoptable_shape",
        "subtitle": "Expected costs explained clearly to patients and families.",
        "doc_no": D("PRE/POL/05"),
    }
    emit_pre_v2(
        draft,
        "pre5_v2_draft.json",
        "PRE.5_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
