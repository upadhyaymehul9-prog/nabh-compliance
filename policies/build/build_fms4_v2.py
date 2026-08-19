# -*- coding: utf-8 -*-
"""Template-test rebuild of FMS.4 as an adoptable hospital policy.

Does NOT overwrite policies/drafts/fms4_draft.json or build_fms4.py.
Writes policies/drafts/fms4_v2_draft.json only. No SQL. No Supabase insert.
"""
from __future__ import annotations

import sys

from fms_v2_common import BLANK, D, HOSPITAL, emit_v2, verify_shape
from policy_build_common import make_disclaimer_accreditation_only

STANDARD_CODE = "FMS.4"
CHAPTER = "FMS"
OE_CODES = ["FMS.4.a", "FMS.4.b", "FMS.4.c", "FMS.4.d"]
POLICY_TITLE = "Medical Gases, Vacuum and Compressed Air"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "Template rebuild to FMS.5 v2.2 shape. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} procures, handles, stores, distributes, uses and replenishes medical gases, and how it proves backup supply and — where a piped system exists — inspects and maintains that installation.

It is the gas, vacuum and compressed-air programme. It is not the electrical backup of the plant, the equipment PPM of a flowmeter inventoried as a device, or the fire plan. A gas leak, manifold-room fire or oxygen-enriched fire is a named emergency there; this policy owns prevention, isolation and backup supply. A copied HTM manual for a hospital that only uses portable cylinders is not this policy.

Editable defaults are marked {D('like this')}. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """Full and empty are not mixed. The reserve has been opened on test. A copied pipeline manual is not a cylinder-only hospital's plan."""

SCOPE = f"""This policy applies to medical gases, medical vacuum and medical compressed air used at {HOSPITAL}, whether from portable cylinders, a manifold or a piped medical gas pipeline system (MGPS), and to the people who procure, handle, store, distribute, use, replenish, test backups and maintain those systems.

Oxygen is in scope if any medical gas is used. Nitrous oxide, medical air, carbon dioxide, vacuum and compressed air are in scope only if the service directory offers them; otherwise they are recorded as not applicable. If this hospital has no piped MGPS, the piped-installation plan is a recorded absence, not a copied pipeline SOP. Cylinder and manifold duties still apply.

Plant electricity for manifolds, alarms and vacuum pumps is the utilities programme. A leaking cylinder found on a monthly round is a finding the facility-safety programme records and this programme closes. Building hazardous materials are chemicals and fuels; cylinders as medical gas are here. A flowmeter or regulator may sit on the equipment inventory; ISO 10524 remains this programme's regulator framework. Clinical use at the anaesthesia workstation stays that care policy; this policy owns that the gas that arrives is the gas that was intended. PESO, Gas Cylinder Rules or the Explosives Act, if they apply to this occupancy, live on the applicable-legislation register — not in this disclaimer. Empty cylinders are not biomedical waste.

UK DH HTM Medical Gas Pipeline Systems, ISO 10524-1/2/3, NFPA medical gas and cylinder storage, BCGA, BS EN 12021, BOC handling guidance and Sarangi et al. are frameworks, not pasted protocols and not a mandate to hold a UK or US certificate."""

POLICY_STATEMENT = f"""Written guidance covers six acts for the gases this hospital actually uses: procurement, handling, storage, distribution, usage and replenishment. A licensed source, an identity and pin-index or DISS check on delivery, and a named person who changes a cylinder at 02:00, are all in that guidance. A supplier brochure is not that guidance.

Cylinders are segregated full and empty, chained or nested upright, away from oil, grease, heaters and electrical panels. Pin-index, DISS or NIST connections are not forced. Regulators match ISO 10524 as the framework. Portable cylinders in transit are capped and not rolled on their side down a stair. Oxygen-enriched areas are not the place a sparking tool is used. A "full" rack that contains empties, or a cylinder used as a doorstop, is a failure of this policy. NFPA cylinder storage and BOC handling inform those rules; they are not a NABH cubic-metre threshold for every small hospital.

Alternate oxygen is the reserve that will supply the points of use when the primary bank, primary bedside cylinders or primary concentrator fails: a second manifold bank, a reserve cylinder set sized for {D('the duration the Medical Superintendent has named')}, or a documented diversion. Alternate vacuum is portable suction at every critical point of use, or a second pump. Alternate medical air or compressed air is the reserve this hospital has defined, or not applicable if that gas is not used. The test is a functioning test: gas actually flows from the alternate source to a defined point of use, vacuum actually aspirates, alarms actually annunciate. Frequency: {D('monthly')}. A paper changeover checklist with no flow is not a test. Plant electricity stays the utilities programme.

Where a piped system exists, the operational, inspection, testing and maintenance plan names who may isolate a zone, who may open a plant room, and how identity, pressure, alarm, isolation, labelling, filters, dryers, pumps and manifolds are inspected and tested. Work on a live oxygen pipe is a planned isolation with clinical notice. HTM medical-gas pipeline, ISO 10524-2, NFPA handbook and BS EN 12021 (where medical air is piped) are the frameworks. A commissioning certificate from the year the pipe was laid is not this plan. A terminal that delivers the wrong gas after a repair is a failure of this policy and an emergency if patients are on the line. If there is no piped system, the Medical Superintendent signs a dated absence against the service directory."""

NON_NEGOTIABLES = f"""The following are prohibited.

1. Mixing full and empty cylinders, using a cylinder as a doorstop, or putting oil or grease on an oxygen regulator.
2. Forcing a mismatched pin-index, DISS or NIST connector.
3. Treating an untested reserve, or a paper changeover with no flow, as backup.
4. Copying a pipeline manual as this hospital's plan when no piped system exists, instead of a signed recorded absence.
5. Using sparking tools in an oxygen-enriched area or manifold room.

Anyone who sees a prohibited act stops it under the stop-work clause and reports it the same shift to the {D('Maintenance In-Charge')} or, at night, the Night Duty Officer."""

PROCEDURE_STEPS = [
f"""5.1 Written guidance — six acts

The Maintenance In-Charge holds written guidance covering procurement, handling, storage, distribution, usage and replenishment for each gas this hospital uses. Delivery acceptance checks identity, pressure, pin-index or DISS, and batch or expiry as the supplier provides. Who may procure, who may change a cylinder at night, and how the reserve is replenished, are named. A gas the directory does not use is recorded as not applicable.""",

f"""5.2 Safe handling, storage, distribution and use

Store checks, {D('weekly')}, confirm full/empty segregation, upright chaining, clearance from heat and electrics, and matched regulators. At the point of use, two people check gas identity before a new cylinder is opened on a theatre list. Clinical users do not force a connector. A porter does not roll a cylinder on its side down a stair.""",

f"""5.3 Alternate sources — functioning tests

Each gas, vacuum and compressed air actually used has a named alternate source. {D('Monthly')}, the Maintenance In-Charge runs a functioning test: flow from the reserve to a defined point of use, suction that aspirates, alarms that annunciate. Staff who may change over at night are on the trained-operator list. Portable suction said to be "available" is not in a locked CSSD.""",

f"""5.4 Piped installation — or recorded absence

If a piped MGPS exists, the operational plan, inspection plan, testing plan and maintenance plan are in one file. Zone isolation is only by a named person, with clinical notice. Identity is rechecked after work. Last inspection, last pressure and alarm test, and last maintenance are retrievable.

If no piped system exists, the Medical Superintendent signs a dated recorded absence. That signature is this section. A copied HTM 02-01 is not.""",
]

STOP_WORK = f"""Every person has the authority and the duty to stop an act that breaches a non-negotiable rule: mixed full and empty; a cylinder as a doorstop; a forced connector; sparking tools in oxygen; a reserve being counted as backup that has never been opened on test.

The person says "stop", makes the immediate safe condition they are competent to make, and reports the same shift to the {D('Maintenance In-Charge')} or the Night Duty Officer. There is no retaliation for a good-faith stop-work. A vendor who refuses to stop is required to leave the area."""

RESPONSIBILITY = f"""Roles below are titles, not vacancies.

Medical Superintendent
- Accountable that this policy is issued and followed.
- Signs the recorded absence if no piped system exists.
- Names the reserve duration.

Maintenance In-Charge
- Owns written guidance, store checks, functioning tests, and the MGPS file or absence record.

Nursing Superintendent
- Ensures ward cylinders in use follow full/empty segregation and identity check.

Night Duty Officer
- Holds changeover authority overnight; does not open a cylinder without identity check.

Quality Coordinator
- Audits this policy {D('quarterly')}.

Clinical users (theatre, ICU, emergency)
- Check gas identity at the workstation; do not force a connector.

A RACI snapshot:
- Written guidance: Maintenance In-Charge (R/A)
- Store and handling: Maintenance In-Charge (R); Nursing Superintendent (A on the ward)
- Functioning tests: Maintenance In-Charge (R/A)
- Piped plan or absence: Maintenance In-Charge (R); Medical Superintendent (A)
- Stop-work: all staff (R); Maintenance In-Charge (A for restart)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored:
- Guidance covers all six acts for gases actually used; unused gases are not-applicable.
- Store: full/empty segregated; no cylinder as a doorstop.
- Last functioning test flowed; it was not a paper changeover.
- Piped file shows last inspection, pressure/alarm test and maintenance — or a signed absence if no MGPS.
- Trained-operator list for night changeover and zone isolation.
- Plant electricity left with the utilities programme; a leak emergency left with the fire programme.

Root-cause analysis is required when: a wrong-gas or empty-reserve event occurs; a functioning test finds no flow; a forced connector is found; a terminal is unlabelled after work. CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a wrong-gas or empty-reserve event."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who change cylinders, work in the manifold room, or use piped terminals are trained against this policy at induction and {D('once a year')} thereafter. Staff who may isolate a zone or change over the reserve are named on the trained-operator list.

Staff acknowledgement

I have read this Medical Gases, Vacuum and Compressed Air policy of {HOSPITAL}. I will not mix full and empty. I will not force a connector. I will not treat an untested reserve as backup.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/04')}
Issue number: {D('01')}
Version: 2.0 (template test — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Maintenance In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Piped MGPS: {D('installed / recorded absence')}
Reserve duration: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- Medical Gases. British Compressed Gases Association — handling framework.
- Respiratory equipment. Compressed gases for breathing apparatus. BS EN 12021:2014 — medical-air quality framework where medical air is supplied.
- Medical Gas Pipeline Systems. (2006). Department of Health: Estates and Facilities Division (HTM) — piped-system inspection, test and maintenance framework, not a UK certificate mandate.
- Pressure regulators for use with medical gases — ISO 10524-1:2018, ISO 10524-2:2018, ISO 10524-3:2019 — regulator frameworks.
- Hart, J. R. (2018). Medical Gas and Vacuum Systems Handbook. National Fire Protection Association — framework.
- Medical Gas Cylinder Storage. (2018). National Fire Protection Association — cylinder-storage framework, not a NABH cubic-metre mandate.
- Sarangi, S., Babbar, S., & Taneja, D. Safety of the medical gas pipeline system. J Anaesthesiol Clin Pharmacol — framework.
- Handle medical gases safely. BOC. (2017) — handling framework, not this hospital's SOP.
- NABH Standards for Small Healthcare Organisations, 3rd Edition, Chapter 8, standard FMS.4 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Internal: written gas guidance; cylinder-store checks; backup-test records; MGPS file or recorded absence; utilities, facility-safety, equipment and fire programmes; service directory."""

DISTRIBUTION = f"""Controlled master: office of the Medical Superintendent, {HOSPITAL}, with a working copy held by the Maintenance In-Charge and the Quality Coordinator.

Issued to: Nursing Superintendent, Night Duty Officer folder, theatre / ICU / emergency in-charges, staff who change cylinders, contracted pipeline maintainer if outsourced.

Available to all staff at the {D('Nursing Station policy folder')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

On revision, every displayed copy is withdrawn the same day. One dated superseded copy is retained by the Quality Coordinator."""

ABBREVIATIONS = """MGPS — medical gas pipeline system
HTM — Health Technical Memorandum (UK medical-gas pipeline guidance; framework only)
DISS — Diameter Index Safety System
NIST — Non-Interchangeable Screw Thread
ISO — International Organization for Standardization
NFPA — National Fire Protection Association
BCGA — British Compressed Gases Association
CAPA — corrective and preventive action
RCA — root-cause analysis

Night Duty Officer — the senior doctor or senior nurse holding emergency command overnight
Maintenance In-Charge — the person accountable for the gas programme under this policy"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "FMS.4.a",
        "requirement": "Written guidance governs the implementation of procurement, handling, storage, distribution, usage and replenishment of medical gases.",
        "steps": "Section 3; 5.1 Written guidance — six acts",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Written guidance covering procurement, handling, storage, distribution, usage and replenishment.",
            "Delivery-acceptance records (identity, pressure, connector, batch).",
            "Recorded not-applicable for gases the directory does not use.",
        ],
    },
    {
        "oe_code": "FMS.4.b",
        "requirement": "Medical gases are handled, stored, distributed and used in a safe manner",
        "steps": "Section 3; 5.2 Safe handling, storage, distribution and use",
        "responsible": "Maintenance In-Charge; clinical users at the point of use",
        "records": [
            "Weekly store checks: full/empty segregation, chaining, matched regulators.",
            "Identity check at use (two-person check on a theatre list).",
            "Record that a cylinder was not used as a doorstop.",
        ],
    },
    {
        "oe_code": "FMS.4.c",
        "requirement": "Alternate sources for medical gases, vacuum and compressed air are provided for, in case of failure and their functioning is tested at a predefined frequency",
        "steps": "Section 3; 5.3 Alternate sources — functioning tests",
        "responsible": "Maintenance In-Charge",
        "records": [
            "Named alternate source for each gas, vacuum and air actually used.",
            "Monthly functioning-test records (flow, suction, alarm).",
            "Trained-operator list for night changeover.",
        ],
    },
    {
        "oe_code": "FMS.4.d",
        "requirement": "There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation.",
        "steps": "Section 3; 5.4 Piped installation — or recorded absence",
        "responsible": "Maintenance In-Charge; Medical Superintendent (signs absence)",
        "records": [
            "Piped operational, inspection, testing and maintenance file with last inspection, pressure/alarm test and maintenance — or the signed recorded absence if no piped system exists.",
            "Named persons who may isolate a zone.",
            "Identity recheck after work on a live line.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.4 v2 to the FMS.5 v2.2 shape.

Technical substance retained from v1: six acts; HTM/ISO 10524/NFPA/BCGA/BS EN
12021/BOC/Sarangi as frameworks not certificates; functioning test not paper
changeover; piped plan or AAC.1 recorded absence; PESO not in P2;
accreditation-only disclaimer; FMS.1.e plant electricity vs gas path;
FMS.5 leak emergency; cylinder-only hospitals still owe a, b, c.

FMS.4.b and FMS.4.c requirement fields keep the book's missing terminal period.

Four 5.x subsections, five non-negotiables. Stop-work included. No SQL. Draft.
"""


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
        "definitions": SAFETY_OBJECTIVE,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "fms_v2_adoptable_shape",
        "doc_no": "«FMS/POL/04»",
        "subtitle": "Standards for cylinders, reserves and piped installation — or a signed absence.",
        "footer_label": "Medical gases",
        "acknowledgement_note": "The Nursing Superintendent holds signed acknowledgements with the induction record. Staff who isolate a zone or change over the reserve are named on the trained-operator list.",
        "control_extra_rows": [
            ["Piped MGPS", "«installed / recorded absence»", "Reserve duration", "«________»"],
        ],
    }
    md = verify_shape(
        draft,
        oe_codes=OE_CODES,
        statute_clause=STATUTE_CLAUSE,
        accreditation_only=True,
    )
    emit_v2(draft, "fms4_v2_draft.json", "FMS.4_v2_preview.md", md)
    return 0


if __name__ == "__main__":
    sys.exit(main())
