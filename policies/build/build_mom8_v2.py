# -*- coding: utf-8 -*-
"""MOM.8 v2 — narcotic drugs and psychotropic substances, chemotherapeutic agents
and radioactive agents are used in a safe manner.

PDF index 86. Stop-work: do not proceed without mandated controls (register, PPE,
authorisation). Five OEs, five What-we-do subsections.
"""
from __future__ import annotations

import sys

from mom_v2_common import BLANK, D, HOSPITAL, document_control, emit_mom_v2
from policy_build_common import make_disclaimer

STANDARD_CODE = "MOM.8"
CHAPTER = "MOM"
OE_CODES = ["MOM.8.a", "MOM.8.b", "MOM.8.c", "MOM.8.d", "MOM.8.e"]
POLICY_TITLE = (
    "Narcotic Drugs and Psychotropic Substances, Chemotherapeutic Agents "
    "and Radioactive Agents Are Used in a Safe Manner"
)
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "MOM v2 template: adoptable shape, plain English, MOM roles, five steps, stop-work.",
    },
]

STATEMENT_OF_INTENT = (
    "Narcotic drugs, psychotropic substances, chemotherapeutic agents and radioactive agents "
    "are used safely — prescribed by appropriate caregivers, stored securely, prepared and "
    "administered by qualified personnel with proper PPE, and recorded from procurement to disposal."
)

PURPOSE = f"""This policy describes how {HOSPITAL} ensures the safe use of narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents: safe use, prescription by appropriate caregivers, secure storage, proper preparation and administration, and record-keeping from procurement to disposal.

It covers MOM.8.a–e.

Words marked {D('like this')} are defaults a small hospital can keep. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies to treating doctors (prescribers), the Pharmacy In-Charge, pharmacy staff, nurses, oncology and radiology staff where applicable, the Medical Superintendent and Quality Coordinator at {HOSPITAL}.

It covers MOM.8.a–e: safe use; prescription by appropriate caregivers; secure storage; safe preparation and administration of chemotherapy and radioactive agents; and record-keeping.

Boundaries with other policies of {HOSPITAL}:

- MOM.2 owns general medication storage. This policy adds the specific security, register and PPE requirements for narcotics, psychotropics, chemotherapeutic and radioactive agents.
- MOM.6 owns general administration safety. This policy adds the qualified-personnel and safety requirements specific to these agents.
- If {HOSPITAL} does not provide chemotherapy or radioactive therapy services, those sections are recorded absences against the service directory."""

POLICY_STATEMENT = f"""{HOSPITAL} uses narcotic drugs, psychotropic substances, chemotherapeutic agents and radioactive agents safely.

Only appropriate caregivers prescribe them. They are stored securely with a register. Chemotherapy and radioactive agents are prepared and administered by qualified personnel with proper protective equipment. A complete record is kept from procurement through administration to disposal."""

NON_NEGOTIABLES = f"""The following rules are non-negotiable.

1. Narcotic drugs and psychotropic substances are prescribed only by {D('doctors authorised under the NDPS Act, 1985 and listed by the Medical Superintendent')}.
2. Narcotic drugs and psychotropic substances are stored in a double-locked cupboard. The register is reconciled at every shift change.
3. Chemotherapeutic agents are prepared in a {D('designated preparation area with biological safety cabinet or equivalent containment')} by trained personnel wearing appropriate PPE (gown, gloves, mask, eye protection).
4. Radioactive agents are handled only by personnel authorised under the {D('Atomic Energy (Radiation Protection) Rules, 2004')} with dosimetry monitoring.
5. A complete record of procurement, receipt, storage, prescription, administration and disposal is maintained for every narcotic, psychotropic, chemotherapeutic and radioactive agent.
6. Disposal of narcotic and psychotropic substances follows the NDPS Act procedure. Cytotoxic waste follows the Bio-Medical Waste Management Rules, 2016.

Staff who cannot confirm authorisation, register entry, PPE availability or containment do not proceed. They report to the {D('Pharmacy In-Charge')} or {D('Medical Superintendent')} immediately."""

PROCEDURE_STEPS = [
f"""5.1 Safe use of narcotic drugs, psychotropic substances, chemotherapeutic agents and radioactive agents

Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used safely.

{HOSPITAL} maintains a written procedure for the safe use of each category. The procedure covers prescription, storage, preparation, administration, monitoring, and disposal. Staff are trained before handling any of these agents.

Where {HOSPITAL} does not provide chemotherapy or radioactive therapy services, the absence is recorded against the service directory and reviewed {D('annually')} by the Multidisciplinary Medication Committee.""",

f"""5.2 Prescription by appropriate caregivers

Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are prescribed by appropriate caregivers.

Narcotic drugs and psychotropic substances are prescribed only by doctors listed by the {D('Medical Superintendent')} as authorised under the NDPS Act, 1985. The authorised-prescriber list is available at the pharmacy.

Chemotherapeutic agents are prescribed by {D('the treating oncologist or a doctor trained in chemotherapy protocols')}. Radioactive agents are prescribed by {D('the radiation oncologist or nuclear medicine physician authorised under the AERB rules')}.""",

f"""5.3 Secure storage

Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are stored securely.

Narcotic drugs and psychotropic substances are stored in a double-locked cupboard in the pharmacy. Two keys are held by {D('the Pharmacy In-Charge and the duty pharmacist')}. The register is reconciled at every shift change; discrepancies trigger an immediate investigation and an incident report.

Chemotherapeutic agents are stored separately from other medications in {D('a clearly labelled, restricted-access area with spill kit accessible')}.

Radioactive agents are stored in {D('the designated radiation-safe area with shielding, signage and access limited to authorised personnel')}. Storage conditions follow AERB requirements.""",

f"""5.4 Safe preparation and administration of chemotherapy and radioactive agents

Chemotherapy and radioactive agents are prepared properly and safely, and administered by qualified personnel.

Chemotherapeutic agents are prepared in a {D('biological safety cabinet or designated preparation area')} by trained personnel wearing PPE (gown, double gloves, mask, eye protection). A spill kit is immediately accessible.

Radioactive agents are prepared and administered by personnel authorised under the AERB rules with dosimetry badges. Preparation follows the {D('radiation safety manual of the hospital')}.

Administration follows MOM.6 (patient identification, order verification) plus agent-specific protocols. The treating doctor is available during administration for management of acute reactions.""",

f"""5.5 Record-keeping from procurement to disposal

A proper record is kept of the usage, administration and disposal of narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents.

For narcotics and psychotropics: the NDPS register records procurement, receipt, batch, issue to ward, administration to patient (with patient name and prescription reference), balance, and disposal. The register is available for inspection by the licensing authority.

For chemotherapeutic agents: the cytotoxic medication log records receipt, batch, preparation, administration and waste disposal (cytotoxic waste stream per BMW Rules, 2016).

For radioactive agents: the radioactive materials log records receipt, activity, use, administration to patient, decay and disposal. Records are maintained per AERB requirements.

The Pharmacy In-Charge reconciles all registers {D('monthly')} and presents a summary to the Multidisciplinary Medication Committee.""",
]

STOP_WORK = f"""Any staff member who cannot confirm authorisation (prescriber not on the authorised list), register entry, PPE availability, or containment conditions:

1. Does not proceed with prescription, dispensing, preparation, or administration.
2. Secures the agent in its current storage.
3. Reports to the Pharmacy In-Charge or Medical Superintendent immediately.

For a register discrepancy (narcotic or psychotropic count does not match):

1. Does not issue further stock from the affected batch.
2. Notifies the Pharmacy In-Charge and the Medical Superintendent the same shift.
3. Investigation is completed within {D('24 hours')}.

No approval is needed to stop. Regulatory compliance overrides convenience."""

RESPONSIBILITY = f"""Medical Superintendent (Head of the Institution)
- Maintains the authorised-prescriber list for narcotics and psychotropics; accountable for regulatory compliance.

Multidisciplinary Medication Committee (Pharmacy and Therapeutics)
- Reviews usage data, register summaries and incident trends for narcotics, cytotoxics and radioactive agents.

Pharmacy In-Charge
- Manages secure storage, registers, reconciliation and disposal procedures.

Treating doctors (appropriate caregivers)
- Prescribe within their authorisation; are available during administration of chemotherapy and radioactive agents.

Nurses and oncology/radiology staff
- Prepare and administer with PPE and containment; maintain shift-change register reconciliation.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 8).
- Tracks CAPA when register discrepancies or safety lapses recur."""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at registers, storage and safety practices.

What is monitored each quarter:

- NDPS register reconciliation records and discrepancies.
- Authorised-prescriber list currency.
- Secure-storage compliance (double lock, restricted access, spill kit, shielding).
- PPE usage and containment during preparation and administration (observation or record).
- Cytotoxic and radioactive materials log completeness.
- Disposal records per NDPS Act, BMW Rules, and AERB requirements.

Root-cause analysis is required when the same safety lapse recurs within six months.

This policy is reviewed {D('annually')}, and sooner when NDPS, AERB or BMW regulations change."""

TRAINING_ACKNOWLEDGEMENT = f"""All staff who handle narcotic drugs, psychotropic substances, chemotherapeutic agents or radioactive agents are trained on this policy at induction and {D('once a year')} after that. Training covers safe use, secure storage, PPE, register maintenance, and disposal.

Staff acknowledgement

I have read this Safe Use of Narcotic, Psychotropic, Chemotherapeutic and Radioactive Agents policy of {HOSPITAL}. I will follow authorisation, storage, preparation, administration and disposal requirements.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Pharmacy In-Charge holds signed acknowledgements with the training record.)"""

DOCUMENT_CONTROL = document_control(
    doc_no="MOM/POL/08",
    version=VERSION,
    prepared_by=D("Pharmacy In-Charge"),
)

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Management of Medication chapter, standard MOM.8.
- Narcotic Drugs and Psychotropic Substances Act, 1985 — procurement, storage, prescribing, administration, record-keeping and disposal of narcotics and psychotropic substances.
- Atomic Energy (Radiation Protection) Rules, 2004 — handling, storage, administration and disposal of radioactive agents.
- Bio-Medical Waste Management Rules, 2016 — cytotoxic waste disposal.
- Internal documents of {HOSPITAL}: NDPS register; cytotoxic medication log; radioactive materials log; authorised-prescriber list; radiation safety manual where applicable."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the Pharmacy In-Charge and the Quality Coordinator.

Copies issued to: pharmacy; oncology unit where it exists; radiology and nuclear medicine where it exists; operation theatre; ICU where it exists.

The current version is available to all staff at the {D('pharmacy counter policy file')} and, if the hospital keeps an intranet, at {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use."""

ABBREVIATIONS = """AERB — Atomic Energy Regulatory Board
BMW — Bio-Medical Waste
CAPA — corrective and preventive action
MOM — Management of Medication (NABH SHCO chapter 7)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NDPS — Narcotic Drugs and Psychotropic Substances
OE — objective element
PPE — personal protective equipment
SHCO — Standards for Small Healthcare Organisations"""

STATUTE_CLAUSE = (
    "the Narcotic Drugs and Psychotropic Substances Act, 1985, insofar as narcotic "
    "and psychotropic substances are procured, stored, administered, recorded and "
    "disposed of under that Act, and the Atomic Energy (Radiation Protection) Rules, "
    "2004, insofar as radioactive agents are handled under those rules"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

OE_MAPPING = [
    {
        "oe_code": "MOM.8.a",
        "requirement": "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used safely.",
        "steps": "Statement of intent; Section 3; 5.1 Safe use overview",
        "responsible": "All staff handling these agents (follow procedure); Pharmacy In-Charge (oversee)",
        "records": [
            "Written procedure for safe use of each category of agent.",
            "Recorded absence against the service directory where chemotherapy or radioactive therapy is not provided.",
            "Training records for all staff handling these agents.",
            "Incident reports related to unsafe use.",
        ],
    },
    {
        "oe_code": "MOM.8.b",
        "requirement": "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are prescribed by appropriate caregivers.",
        "steps": "Section 4 item 1; 5.2 Prescription by appropriate caregivers",
        "responsible": "Medical Superintendent (authorised-prescriber list); prescribers (prescribe within authorisation)",
        "records": [
            "Authorised-prescriber list for narcotics and psychotropics.",
            "Evidence the list is available at the pharmacy.",
            "Sample prescriptions verified against the authorised list.",
        ],
    },
    {
        "oe_code": "MOM.8.c",
        "requirement": "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are stored securely.",
        "steps": "Section 4 items 2–3; 5.3 Secure storage",
        "responsible": "Pharmacy In-Charge (manage storage and register); duty pharmacist (second key)",
        "records": [
            "NDPS register with shift-change reconciliation records.",
            "Evidence of double-locked cupboard for narcotics and psychotropics.",
            "Chemotherapy storage area inspection records (labelling, restricted access, spill kit).",
            "Radioactive-agent storage compliance records (shielding, signage, access log).",
        ],
    },
    {
        "oe_code": "MOM.8.d",
        "requirement": "Chemotherapy and radioactive agents are prepared properly and safely, and administered by qualified personnel.",
        "steps": "Section 4 items 3–4; 5.4 Safe preparation and administration",
        "responsible": "Trained oncology/radiology staff (prepare and administer); treating doctor (available for reactions)",
        "records": [
            "Preparation records showing containment and PPE used.",
            "Administration records with patient identification and protocol reference.",
            "Dosimetry records for personnel handling radioactive agents.",
        ],
    },
    {
        "oe_code": "MOM.8.e",
        "requirement": "A proper record is kept of the usage, administration and disposal of narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents.",
        "steps": "Section 4 items 5–6; 5.5 Record-keeping from procurement to disposal",
        "responsible": "Pharmacy In-Charge (reconcile registers); all handling staff (maintain entries)",
        "records": [
            "NDPS register (procurement to disposal).",
            "Cytotoxic medication log (receipt to waste disposal).",
            "Radioactive materials log (receipt to decay/disposal).",
            "Monthly reconciliation summaries presented to the committee.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """MOM.8 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE: Header "Narcotic drugs and psychotropic substances, chemotherapeutic agents and radioactive agents are used in a safe manner." MOM.8.a–e PDF index 86. MOM.8.a asterisked. All Commitment level.

SHAPE: Five What-we-do subsections (5.1–5.5). Stop-work yes (do not proceed without mandated controls). Disclaimer names NDPS Act 1985 and Atomic Energy Rules 2004. MOM roles only."""


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
        "template_test": "mom_v2_adoptable_shape",
        "subtitle": "Safe use of narcotics, psychotropics, chemotherapeutic and radioactive agents.",
        "doc_no": "MOM/POL/08",
        "stop_work": STOP_WORK,
    }
    emit_mom_v2(
        draft,
        "mom8_v2_draft.json",
        "MOM.8_v2_preview.md",
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=False,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
