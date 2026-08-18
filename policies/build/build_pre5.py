# -*- coding: utf-8 -*-
"""Builds the PRE.5 master policy draft: JSON for review + SQL for later insert.

UNAPPROVED DRAFT. Do not insert, approve, or write this to Supabase until the
owner confirms.

THIS IS DRAFTED UNDER THE TWO-TIER DEPTH STANDING RULE (2026-08-10) AND THE
DISCLAIMER STATUTE-MATCHING STANDING RULE (2026-08-17), both in
scripts/master-policy-todos.md.

NO OE CARRIES THE ASTERISK. The whole standard is Tier 2.

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition
(August 2022), Chapter 4, standard PRE.5 and OEs PRE.5.a-d, printed page 89,
PDF page index 95. Chapter intent printed page 85, PDF page index 91: expected
costs of treatment and care are explained clearly to the patient and/or family.

Asterisks verified 2026-08-17: none of PRE.5.a-d is asterisked in the PDF or in
scripts/shco_oe_asterisks.json.
"""
from policy_build_common import emit_and_verify, make_disclaimer

STANDARD_CODE = "PRE.5"
CHAPTER = "PRE"
OE_CODES = [
    "PRE.5.a", "PRE.5.b", "PRE.5.c", "PRE.5.d",
]
TIER1_OES = []

POLICY_TITLE = "Information on Expected Costs"

VERSION = "1.0"
REVISION_HISTORY = [
    {"version": "1.0", "date": "17-08-2026", "description": "Initial release."},
]

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} makes patients and families aware of the pricing policy in different settings; how the relevant tariff list is available to patients; how expected costs are explained; and how they are informed of the financial implications when the care plan changes.

The chapter intent is that expected costs of treatment and care are explained clearly. A tariff in the accounts office that the family never sees, or a package price that silently grows when the plan changes, is not that intent.

This document is patient-facing cost information. It is not the billing ledger, the accounts process, or a facility-management tariff file. Those remain ROM/FMS when drafted."""

SCOPE = """This policy applies to every setting in which a patient at {{HOSPITAL_NAME}} incurs or may incur a charge: out-patient, emergency, ICU where it exists, and in-patient. It binds the staff who explain prices, who make the tariff list available, and who tell the family when a change in the care plan changes the cost.

It covers: awareness of the pricing policy in different settings; availability of the relevant tariff list; explanation of expected costs; and information on financial implications when the care plan changes.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- The right to information on expected cost of treatment is listed under PRE.2.i. This document owns the pricing policy, the tariff list and the explanation. PRE.2 does not write the tariff.
- Promotion of that right is PRE.1.b. This document owns the figures and the explanation.
- Care-plan changes as a clinical act are governed by the assessment and care-planning policies of {{HOSPITAL_NAME}} (AAC.3) and by PRE.2.o (care plan prepared and modified in consultation). This document owns only the financial implications of that change.
- Discharge-summary medication and follow-up instructions are AAC.8. This document does not put a bill on the discharge summary unless this hospital has defined that; AAC.8 does not own expected-cost explanation at admission.
- Billing, accounts, insurance claims and facility tariffs as a finance function are governed by ROM/FMS policies of {{HOSPITAL_NAME}} (not yet drafted). This document owns what the patient and family are told. It does not write the ledger, the GST treatment, or a package-contract with a payer.
- Informed consent (PRE.3) is not a substitute for cost explanation, and a signed consent is not agreement to an unnamed bill."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} makes the patient and/or family members aware of the pricing policy in out-patient, emergency, ICU (where it exists) and in-patient settings.

{{HOSPITAL_NAME}} makes the relevant tariff list available to patients.

{{HOSPITAL_NAME}} explains expected costs to the patient and/or family members.

{{HOSPITAL_NAME}} informs the patient and/or family about the financial implications when there is a change in the care plan.

{{HOSPITAL_NAME}} does not treat a signed consent, or a tariff locked in accounts, as a substitute for that explanation."""

PROCEDURE_STEPS = [
"""1. Pricing policy in different settings

The patient and/or family members are made aware of the pricing policy in different settings (out-patient, emergency, ICU and in-patient).

The pricing policy for each of those settings this hospital actually runs — what is charged how (for example itemised, package, or a mix), and how the family is made aware of that policy — is [Hospital to define — the pricing policy for out-patient, emergency, ICU where it exists, and in-patient, and how patients and families are made aware of it]. A setting the service directory does not provide (for example ICU) is a recorded absence, not a copied ICU package tariff. Emergency awareness may follow stabilisation; the delay and the reason are recorded.

This step does not print rupee figures as a NABH mandate.""",

"""2. Relevant tariff list available to patients

The relevant tariff list is available to patients.

Where the tariff list is held so that a patient can see the relevant part, and which list is 'relevant' in each setting, are [Hospital to define — where the relevant tariff list is available to patients, and which list applies in each setting]. Availability means a patient or family can see it without an accounts-office escort as the only route. A list only in the finance folder is not available to patients.

Where the State has adopted the Clinical Establishments Act, 2010, the Clinical Establishments (Central Government) Rules, 2012 display-of-rates requirements inform this availability. They are not pasted as a board layout, and they are not applied as if the State had adopted the Act when it has not. Whether this hospital's State has adopted that Act, and how display then meets those rules, are [Hospital to define — whether the Clinical Establishments Act, 2010 has been adopted in this State, and how tariff display meets the 2012 Rules if it has].""",

"""3. Expected costs explained

The patient and/or family members are explained about the expected costs.

How expected costs are explained — when, by whom, and how the explanation is recorded — is [Hospital to define — how expected costs are explained, when, by whom, and how the explanation is recorded]. Explanation is in a language they can understand. A range or a package with what it includes and what it does not is an explanation; a sentence that says "charges extra" without a figure or a route to the tariff is not.

The Consumer Protection Act, 2019 informs that a consumer of a healthcare service is entitled not to be misled on price. This document does not copy District Commission procedure.""",

"""4. Financial implications when the care plan changes

Patient and/or family are informed about the financial implications when there is a change in the care plan.

How that information is given when the plan changes, and how it is recorded, are [Hospital to define — how patients and families are informed of the financial implications of a care-plan change, and how that is recorded]. A change that does not change cost is recorded as such if the hospital's method requires it. A change that increases cost and is not told is a defect. Clinical modification of the plan remains AAC.3 / PRE.2.o; this step is the money.""",

"""5. Records, review and the order of operations

The pricing policy, the tariff-availability method, expected-cost explanations, and financial-implication notices when the plan changes, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for expected-cost information records] for: awareness of the pricing policy in the settings this hospital runs; a tariff list a patient can actually see; expected-cost explanation recorded; financial implications told when the plan changed cost; and no signed consent offered as the cost conversation.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a family was billed against a plan they were not told had changed, or a tariff was only in accounts, or when ROM/FMS billing policies or PRE.2 that this document hands work to are revised.""",
]

RESPONSIBILITY = """The head of the institution is accountable for {{HOSPITAL_NAME}} telling patients and families the pricing policy, making the tariff available, explaining expected costs, and telling them when a care-plan change changes the bill.

The named lead for expected-cost information authors and keeps current the pricing policy, the tariff-availability method and the explanation method. The named lead is [Hospital to define — the named lead for expected-cost information].

Staff who admit, who explain packages, and who tell a family of a plan change that changes cost, apply those methods. Finance/accounts produce the tariff; they do not replace the explanation to the family.

The quality or accreditation coordinator audits the records at step 5 and reports findings to the head of the institution.

All staff are expected to treat a hidden tariff and an unexplained increase when the plan changed, as defects, and to report them."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Rights and Education chapter, standard PRE.5.
- Consumer Protection Act, 2019 — insofar as a consumer of a healthcare service is entitled not to be misled on price; this document does not copy District Commission procedure.
- Clinical Establishments Act, 2010, and the Clinical Establishments (Central Government) Rules, 2012, insofar as the State has adopted that Act and those rules require display of rates. Not applied as if the State had adopted the Act when it has not. Not pasted as a board layout.
- Internal documents of {{HOSPITAL_NAME}}: the pricing policy; the tariff list and where it is available; the expected-cost explanation method; the care-plan-change financial-implication method; the beliefs-values policy; the consent policy; the assessment policy; and ROM/FMS billing policies when drafted."""

DISTRIBUTION = """Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the quality or accreditation coordinator.

Copies issued to: registration and billing/accounts; out-patient; emergency; in-patient wards; ICU where it exists; nursing administration; and the named lead.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. The pricing policy and the tariff list — the working documents this policy requires — are held where patients are admitted and billed.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

CEA — Clinical Establishments Act, 2010
ICU — intensive care unit
ROM — Resource Management (NABH chapter; not yet drafted)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

STATUTE_CLAUSE = (
    "the Consumer Protection Act, 2019, insofar as a consumer of a healthcare service "
    "is entitled not to be misled on price, and the Clinical Establishments Act, 2010 "
    "and the Clinical Establishments (Central Government) Rules, 2012, insofar as the "
    "State has adopted that Act and those rules require display of rates"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "PRE.5.a",
        "requirement": "The patient and/or family members are made aware of the pricing policy in different settings (out-patient, emergency, ICU and in-patient).",
        "steps": "Steps 1, 5",
        "evidence": "The written pricing policy for each setting this hospital runs, or a recorded absence for a setting it does not (for example ICU); the method of making patients and families aware; sample records of awareness at those settings, including delayed emergency awareness with reason; the audit sample at step 5",
        "responsible": "Named lead holds the pricing policy; staff at those settings make families aware; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PRE.5.b",
        "requirement": "The relevant tariff list is available to patients.",
        "steps": "Steps 2, 1, 5",
        "evidence": "Where the relevant tariff list is available to patients in each setting, showing a route that is not only an accounts-office escort; the recorded decision whether CEA 2010 is adopted in this State and how display meets the 2012 Rules if it is, rather than a copied CEA board in a State that has not adopted the Act; the audit sample at step 5 of a list a patient can actually see",
        "responsible": "Named lead holds the tariff-availability method; finance produces the list; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PRE.5.c",
        "requirement": "The patient and/or family members are explained about the expected costs.",
        "steps": "Steps 3, 1, 5",
        "evidence": "The written explanation method (when, by whom, how recorded); sample explanations against the unique identification number showing a range or package with inclusions/exclusions rather than only 'charges extra'; the recorded statement that a signed consent is not this explanation; the audit sample at step 5",
        "responsible": "Named staff explain expected costs; named lead holds the method; quality or accreditation coordinator audits",
    },
    {
        "oe_code": "PRE.5.d",
        "requirement": "Patient and/or family are informed about the financial implications when there is a change in the care plan.",
        "steps": "Steps 4, 5",
        "evidence": "The written method for informing of financial implications when the care plan changes; sample records of plan changes that changed cost being told; the recorded split that AAC.3/PRE.2.o own the clinical modification; the audit sample at step 5",
        "responsible": "Staff who know the plan changed cost tell the family; clinicians own the clinical change; quality or accreditation coordinator audits",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. PRE.5 standard text and all four OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (August 2022), Chapter 4, printed page 89 (PDF page index 95). Header: "Patients and families have a right to information on expected costs." PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: PRE.5.a Core, PRE.5.b Commitment, PRE.5.c Commitment, PRE.5.d Achievement.
   NO OE CARRIES THE ASTERISK. Whole standard is Tier 2. Verified against asterisk_extract.py and the PRE.5 page.

TIERING UNDER THE STANDING RULE
1. Two-tier depth standing rule of 2026-08-10 applies. If a standard carries no asterisked OE at all, the whole standard is Tier 2. PRE.5 carries no asterisked OE. TIER1_OES = []. Every OE is Tier 2. Reviewer to note the shallower treatment of the WHOLE STANDARD is a DECISION UNDER THE STANDING RULE, not an omission.

CROSS-REFERENCE AND OVERLAP CHECK
2. T2 quick check (2026-08-17). PRE.2.i right vs this method -- flagged. PRE.1.b promotion -- flagged. AAC.3 / PRE.2.o care-plan change vs financial implications -- flagged. AAC.8 discharge summary -- not this explanation. PRE.3 consent is not a bill. ROM/FMS billing undrafted -- this document owns patient-facing information, not the ledger. Flagged for the ROM/FMS pass.
3. FORWARD REFERENCES: ROM/FMS billing; IMS record.
4. Nothing added to the HIC reconciliation list.

STATUTORY AND EXTERNAL FACTS
5. Consumer Protection Act, 2019 -- named in P2 insofar as a consumer must not be misled on price. No District Commission procedure copied.
6. CEA 2010 and Clinical Establishments (Central Government) Rules, 2012 -- named in P2 only insofar as the State has adopted the Act and those rules require display of rates. Not applied where the State has not adopted. Not a numbered PRE chapter reference; used because PRE.5.b is tariff availability. The AAC.1 defaulted-statute bug is refused by fencing adoption.
7. MHCA 2017 is NOT named. BMW/FSS are NOT named in P2.
8. NO rupee figures or package prices as NABH mandates.

EDITORIAL POSITIONS TAKEN
9. Split that ROM/FMS will own the ledger and this document owns what the family is told, is an editorial position required because those chapters are undrafted.
10. Step 2's State-adoption fence for CEA is an editorial position required by the owner's instruction not to default CEA.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
11. P1/P3/P4 shared. P2 names CPA 2019 and CEA 2010 / 2012 Rules only as fenced above. Not BMW, FSS, or MHCA.

DELIBERATELY NOT INCLUDED
- Rights list -- PRE.2.i. Consent -- PRE.3. Care-plan clinical content -- AAC.3 / PRE.2.o.
- Billing ledger, GST, payer contracts -- ROM/FMS.
- Printed rupee tariffs as NABH mandates.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 11 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 9 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 11; a search for "Hospital to define" without brackets finds all 11, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: pricing policy per setting; tariff availability and which list; whether CEA 2010 is adopted in this State and how display meets the 2012 Rules if so; how expected costs are explained; how financial implications of a plan change are told; the named lead; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation."""

SQL_HEADER = """-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 4, printed page 89
-- (PDF page index 95). Levels: a Core, b Commitment, c Commitment, d Achievement.
-- NO OE CARRIES THE ASTERISK. Whole standard is Tier 2.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.
"""

if __name__ == "__main__":
    emit_and_verify(
        standard_code=STANDARD_CODE,
        chapter=CHAPTER,
        oe_codes=OE_CODES,
        policy_title=POLICY_TITLE,
        purpose=PURPOSE,
        scope=SCOPE,
        policy_statement=POLICY_STATEMENT,
        procedure_steps=PROCEDURE_STEPS,
        responsibility=RESPONSIBILITY,
        references_text=REFERENCES,
        distribution=DISTRIBUTION,
        abbreviations=ABBREVIATIONS,
        disclaimer=DISCLAIMER,
        oe_mapping=OE_MAPPING,
        universal_facts_checklist=UNIVERSAL_FACTS_CHECKLIST,
        version=VERSION,
        revision_history=REVISION_HISTORY,
        tier1_oes=TIER1_OES,
        statute_clause=STATUTE_CLAUSE,
        sql_header=SQL_HEADER,
        json_name="pre5_draft.json",
        sql_name="pre5_insert.sql",
    )
