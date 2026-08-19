# -*- coding: utf-8 -*-
"""FMS.4 v2 — medical gases, vacuum and compressed air.

Shape follows FMS.5 v2.2 (section list and order only). Wording is this
standard's OEs and v1 substance. Does not overwrite fms4_draft.json or
build_fms4.py. No SQL. No Supabase insert.

Disclaimer P2 is accreditation-only (same statute scoping as v1). PESO / Gas
Cylinder Rules are not in P2. FMS.4.b and FMS.4.c requirement strings have
no terminal period in the book — preserved in the traceability table.
"""
from __future__ import annotations

import sys

from fms_v2_common import (
    BLANK,
    D,
    HOSPITAL,
    emit_v2,
    verify_shape,
)
from policy_build_common import make_disclaimer_accreditation_only

STANDARD_CODE = "FMS.4"
CHAPTER = "FMS"
OE_CODES = ["FMS.4.a", "FMS.4.b", "FMS.4.c", "FMS.4.d"]
POLICY_TITLE = "Medical Gases, Vacuum and Compressed Air"
VERSION = "2.1"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "First v2 shape pass (withdrawn: fire-cloned wording).",
    },
    {
        "version": "2.1",
        "date": "19-08-2026",
        "description": "Same section skeleton as FMS.5 v2.2; wording rebuilt from FMS.4 OEs and v1. Not an approved master.",
    },
]

PURPOSE = f"""This policy governs how {HOSPITAL} runs its programme for medical gases, vacuum and compressed air: the written guidance that covers procurement, handling, storage, distribution, usage and replenishment; safe handling, storage, distribution and use; alternate sources in case of failure and tests of those sources at a predefined frequency; and the operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation where a piped system exists.

It is the gas, vacuum and compressed-air programme. It is not the utilities programme's electrical backup (though medical-gas plant may be an essential circuit there), not the equipment programme's preventive maintenance of a flowmeter inventoried as a device, and not the fire plan — though a gas leak is a named emergency that plan must list.

Editable defaults in this document are marked {D('like this')}. A hospital that adopts the default keeps the wording. A hospital that needs a different owner, interval or arrangement replaces the marked text before issue. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """The gas at the workstation is the gas that was intended. Full and empty are not mixed. A paper changeover is not a functioning test. A copied pipeline manual is not a plan for a hospital that only uses cylinders."""

SCOPE = f"""This policy applies to medical gases, medical vacuum and medical compressed air used at {HOSPITAL}, whether supplied from portable cylinders, a manifold, or a piped medical gas pipeline system, and to the people who procure, handle, store, distribute, use, replenish, test backups and maintain those systems.

It covers: written guidance for procurement, handling, storage, distribution, usage and replenishment of medical gases; safe handling, storage, distribution and use; alternate sources for gases, vacuum and compressed air and tests at a predefined frequency; and operational, inspection, testing and maintenance of piped installation where one exists.

If this hospital has no piped medical gas pipeline system, the piped-installation plan is a recorded absence against the service directory, not a copied pipeline SOP. Cylinder and manifold duties still apply if gases are used. If a gas, vacuum or compressed air is not in the service directory (for example piped vacuum in a hospital that uses portable suction only), that is a recorded absence, not a copied intensive-care pipeline SOP.

Essential-circuit electricity may include medical-gas plant, manifold alarms and vacuum pumps. Plant power is the utilities programme; the gas path is here.

A leaking cylinder found on a monthly facility round is closed here. Building hazardous materials are housekeeping chemicals, fuels and mercury; cylinders as medical gas are this policy. A surplus regulator leaves this inventory then follows the unused-material route.

Flowmeters, regulators and suction units may be inventoried as devices under the equipment programme. ISO 10524-1/2/3 are the regulator frameworks this programme uses; the equipment programme still holds the device file if this hospital lists the regulator as equipment.

A medical-gas leak, manifold-room fire, or oxygen-enriched fire is a named emergency in the fire-and-non-fire programme; this policy owns prevention, detection at the plant, isolation and backup supply. Laboratory fire is that fire plan; oxygen handling is here.

Clinical use of gases at the anaesthesia or critical-care workstation remains those care policies. This policy owns that the gas that arrives is the gas that was intended, at a pressure the workstation can use.

Procurement of medical gases is this written guidance. A cylinder that is also a store item still follows this handling method.

PESO, Gas Cylinder Rules or the Explosives Act appear on the applicable-legislation register if they apply to this occupancy. They are not numbered FMS chapter references and are not in this document's disclaimer paragraph 2.

Outsourced filling or pipeline-maintenance agreements with service parameters remain that management-agreement programme. The technical tests remain here.

An empty cylinder is not a biomedical-waste bag. Patient-facing expected cost is not a gas tariff.

UK DH HTM Medical Gas Pipeline Systems, NFPA medical gas and cylinder storage, BCGA, BS EN 12021, BOC handling and Sarangi et al. are frameworks, not pasted protocols and not a mandate to hold a UK HTM certificate."""

POLICY_STATEMENT = f"""{HOSPITAL} uses written guidance that governs procurement, handling, storage, distribution, usage and replenishment of the medical gases it actually uses. All six acts are in the guidance. A supplier brochure, or a pocket guide offered as the hospital SOP, is not that guidance. A gas the service directory does not use is a recorded absence.

{HOSPITAL} handles, stores, distributes and uses medical gases in a safe manner: full and empty segregated; cylinders chained or nested, upright, away from oil, grease, heaters and electrical panels; pin-index, DISS or NIST connections not forced; identity checked at the point of use. A cylinder used as a doorstop is not storage.

{HOSPITAL} provides alternate sources for medical gases, vacuum and compressed air in case of failure, and tests their functioning at {D('monthly')} frequency. Gas actually flows from the reserve to a defined point of use; vacuum actually aspirates; alarms actually annunciate. A paper changeover checklist with no flow is not a test.

{HOSPITAL} maintains an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation where a piped system exists. If none exists, that is a recorded absence signed by the named lead, not a pipeline SOP invented for a file. HTM, ISO 10524, NFPA and BS EN 12021 are frameworks, not UK or US certificate mandates.

{HOSPITAL} does not treat a copied HTM manual for a cylinder-only hospital, mixed full and empty cylinders, or an untested manifold reserve, as that duty."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no operational exception and no "until the vendor comes" exception.

1. Connecting a cylinder, manifold or terminal whose gas identity has not been checked, or forcing a mismatched pin-index, DISS or NIST connector.
2. Mixing full and empty cylinders on the same rack, or using a cylinder as a doorstop.
3. Storing cylinders against a heater, electrical panel, oil or grease, or rolling a portable cylinder on its side down a stair.
4. Treating a paper changeover checklist with no flow as a functioning test of the reserve.
5. Signing a backup-test sheet for a reserve bank that has never been opened on test, or for portable suction that is in a locked room.
6. Offering a copied HTM 02-01 manual as the piped-installation plan of a hospital that has no piped system, or as this hospital's certificate.
7. Working on a live oxygen pipe without a planned isolation and clinical notice.
8. Putting an empty cylinder into the biomedical-waste stream, or rewriting PESO / Gas Cylinder Rules into this policy's disclaimer paragraph 2. Those instruments, if they apply, live on the applicable-legislation register.
9. Leaving a piped-versus-absence decision unrecorded. Either the piped plan is operated, or the named lead has signed that no piped system exists.

A person who finds mixed full and empty cylinders, an untested reserve, a forced connector, or a piped terminal that is unlabelled, reports it the same shift to the {D('Gas-Plant In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Govern procurement, handling, storage, distribution, use and replenishment

The book lists six acts because a hospital can buy oxygen correctly and still store it against a heater, or use it correctly at the theatre table and never replenish the reserve. BCGA, BOC Handle medical gases safely, and NFPA Medical Gas Cylinder Storage are handling and storage frameworks. ISO 10524-1/2/3 are regulator frameworks. They are not pasted as this hospital's guidance.

Which gases this hospital actually uses (oxygen as a minimum if any medical gas is used; nitrous oxide, medical air, carbon dioxide, vacuum, compressed air only if in the service directory), who may procure from which licensed source, how a delivery is accepted (identity, pressure, pin-index or DISS, expiry or batch as the supplier provides), and how storage, distribution, use and replenishment are each governed, are held by the {D('Gas-Plant In-Charge')} as written guidance.

Gases in use: {BLANK}. A gas the directory does not use is a recorded absence. Guidance that covers cylinders in stores and is silent on who changes a cylinder at 02:00, or that names medical air and vacuum in the title for a hospital that has neither, is not this guidance.

The named competent person who changes a cylinder after hours is {D('the named person on the after-hours cylinder roster')}. That is a gas-handling competence, not an emergency-command title imported from the fire programme.""",

f"""5.2 Handle, store, distribute and use medical gases safely

Full and empty are segregated. Cylinders are chained or nested, upright, away from oil, grease, heaters and electrical panels. Pin-index, DISS or NIST connections are not forced. Regulators match ISO 10524 as the framework. Oxygen-enriched areas are not the place a sparking tool is used. Portable cylinders in transit are capped and not rolled on their side down a stair.

NFPA cylinder storage and BOC inform those rules; they are not a NABH cubic-metre threshold for every small hospital. The local fire authority's conditions on the occupancy may add store-room conditions; this section still owns how a porter moves a cylinder.

The failure this handling exists to catch is a "full" rack that contains empties, a cylinder used as a doorstop, a grease-on-oxygen regulator, or a theatre that opens a new cylinder without a second person to check the gas identity. How staff handle, store, distribute and use, including the check that the gas at the workstation is the gas intended, are held by the {D('Gas-Plant In-Charge')} with clinical users at the point of use.

PESO / Gas Cylinder Rules, if they apply, live on the applicable-legislation register; they are not restated as a NABH protocol here.""",

f"""5.3 Prove alternate sources by a functioning test

Alternate oxygen is the reserve that will supply the points of use when the primary manifold bank, primary cylinders at the bedside, or primary concentrator fails: a second manifold bank, a reserve cylinder set sized for the duration this hospital has defined, or a documented diversion. Alternate vacuum is a portable suction on every critical point of use if the piped vacuum fails, or a second pump. Alternate compressed air or medical air is the reserve this hospital has defined, or a recorded absence if that gas is not used.

HTM Medical Gas Pipeline Systems and Sarangi et al. are pipeline-safety frameworks for changeover and alarm; they are not a mandate to install a piped system.

The failure this test exists to catch is a reserve bank that has never been opened on test, a changeover that is manual at 03:00 with no one trained, or "portable suction available" that is in a locked sterile-supply room. The test is a functioning test: gas actually flows from the alternate source to a defined point of use, vacuum actually aspirates, alarms actually annunciate. A paper changeover checklist with no flow is not a test.

Which alternate source exists for each gas, vacuum and air this hospital uses, the functioning-test method, and the predefined frequency {D('monthly')}, are held by the {D('Gas-Plant In-Charge')}. Plant electricity remains the utilities programme's backup test; this section is the gas path.""",

f"""5.4 Maintain the piped installation, or record that none exists

If this hospital has no piped medical gas pipeline system, this section is a recorded absence against the service directory, signed by the {D('Gas-Plant In-Charge')}, not a pipeline SOP invented for a file.

If a piped system exists, HTM Medical Gas Pipeline Systems is the inspection, test and maintenance framework (identity, pressure, alarm, isolation, anti-confusion, oil-free air as BS EN 12021 where medical air is piped). ISO 10524-2 is the line-regulator framework. NFPA Medical Gas and Vacuum Systems Handbook is a further framework. None of these is a UK or US certificate mandate for an Indian small hospital.

The operational plan (who may isolate a zone, who may open a plant room), the inspection plan (plant, alarms, terminal units, labelling), the testing plan (pressure, identity after work, alarm function), the maintenance plan (filters, dryers, pumps, manifolds), and the rule that work on a live oxygen pipe is a planned isolation with clinical notice, are held by the {D('Gas-Plant In-Charge')}.

A commissioning certificate from the year the pipe was laid is not this plan. A terminal unit that delivers the wrong gas after a repair is a failure of this policy and a fire-and-non-fire emergency if patients are on the line. The equipment programme may still hold a regulator device file; the pipeline is here.""",
]

STOP_WORK = f"""A person who is about to do any of the following does not proceed:

- connect a cylinder, manifold or terminal whose identity has not been checked;
- force a mismatched pin-index, DISS or NIST connector;
- use a piped terminal after work on that zone until identity and pressure have been tested;
- sign a backup-test sheet for a reserve that did not flow, a vacuum that did not aspirate, or an alarm that did not annunciate;
- start work on a live oxygen pipe without a planned isolation and clinical notice.

They cap the cylinder, leave the connector unforced, leave the zone out of use, leave the test unsigned, and tell the {D('Gas-Plant In-Charge')} the same shift — or, if that person is not on site, the {D('named person on the after-hours cylinder roster')}.

A good-faith refusal to connect an unidentified cylinder, or to sign a paper changeover as a functioning test, is not a disciplinary matter. The connection or the test is not recorded as done until identity was checked or flow was seen."""

RESPONSIBILITY = f"""These are the jobs this medical-gas programme needs. In a small hospital the gas-plant lead may be the same person as the facilities Maintenance In-Charge; they still keep this file as the gas file, not as a combined fire-and-cylinder binder.

Medical Superintendent (head of the institution)
- Accountable that medical gases, vacuum and compressed air are managed as this policy requires.
- Signs the recorded absence if no piped system exists, or accepts the piped plan if one does.

{D('Gas-Plant In-Charge')} (named engineering or gas-plant lead)
- Holds the written guidance covering the six acts, store checks, identity-check method, functioning-test records, and the piped-system file or the recorded absence.
- Names the {D('named person on the after-hours cylinder roster')} who is competent to change a cylinder when the lead is not on site.
- Orders planned isolation of a live oxygen pipe with clinical notice.

Clinical users (theatre, intensive or high-dependency care, emergency, labour if gases are used there)
- Check gas identity at the point of use.
- Do not force a mismatched connector.
- Report a hiss, a manifold alarm, or a terminal that is unlabelled.

Quality Coordinator
- Audits the records in section 8.

Contracted pipeline maintainer, if outsourced
- Works to the inspection, test and maintenance plan in this policy. Outsourcing agreements remain that management-agreement programme.

All staff who move or store cylinders
- Keep full and empty segregated; do not use a cylinder as a doorstop; do not put an empty cylinder in the biomedical-waste stream.

A RACI snapshot:

- Written guidance (six acts): Gas-Plant In-Charge (R/A)
- Safe handling and identity check: Gas-Plant In-Charge (R for store); clinical user (R at the point of use)
- Functioning tests of alternate sources: Gas-Plant In-Charge (R/A)
- Piped plan or recorded absence: Gas-Plant In-Charge (R); Medical Superintendent (A)
- After-hours cylinder change: named person on the after-hours cylinder roster (R); Gas-Plant In-Charge (A)
- Audit: Quality Coordinator (R); Medical Superintendent (A)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit looks at the store, the plant and the records, not at a binder.

What is monitored each quarter:

- Written guidance covers procurement through replenishment of the gases actually used, including who changes a cylinder after hours. Unused gases are recorded as absences.
- Full and empty are segregated; cylinders are chained upright; identity is checked at use. A cylinder used as a doorstop is a finding.
- Functioning backup tests show flow from the reserve, vacuum that aspirates, and alarms that annunciate, at the predefined frequency. A paper changeover is a finding.
- Piped-system maintenance is last inspection, pressure and alarm test and maintenance, not a commissioning certificate — or a signed recorded absence if no piped system exists.
- Plant electricity is left with the utilities programme. A leak or wrong-gas event is left with the fire-and-non-fire programme as the emergency action, and closed here as the gas path.
- PESO is not invented in disclaimer paragraph 2. Biomedical-waste colours are not used as cylinder disposal.

Any non-conformity is a finding. The Gas-Plant In-Charge owns the corrective action. Root-cause analysis is required when: a wrong gas reached a workstation; a reserve was signed as tested without flow; full and empty were found mixed; a live oxygen pipe was worked without isolation; or a piped terminal was unlabelled.

Corrective and preventive action is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a wrong-gas or empty-reserve event, a change to the service directory that adds or withdraws a gas, or a decision to install or decommission a piped system."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who procure, store, change, or use medical gases, and staff who may isolate a piped zone, are trained against this policy at induction, before first unsupervised cylinder change or piped use, and {D('once a year')} thereafter. Training covers: the six acts in the written guidance; full and empty segregation; identity check at use; not forcing a connector; the functioning test of the reserve; and, if a piped system exists, planned isolation with clinical notice. The after-hours cylinder roster is held by the Gas-Plant In-Charge.

Staff acknowledgement

I have read this Medical Gases, Vacuum and Compressed Air policy of {HOSPITAL}. I will not connect a cylinder whose identity I have not checked. I will not force a mismatched connector. I will not sign a paper changeover as a functioning test. I will not put an empty cylinder in the biomedical-waste stream.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/04')}
Issue number: {D('01')}
Version: 2.1 (template test — standard-specific wording; not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Gas-Plant In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Piped MGPS exists: {D('no — recorded absence')} / {BLANK} if yes
Gases actually used: {BLANK}
After-hours cylinder roster: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.4 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Medical Gases. British Compressed Gases Association — handling framework.
- Respiratory equipment. Compressed gases for breathing apparatus. BS EN 12021:2014 — medical-air quality framework where medical air is supplied.
- Medical Gas Pipeline Systems. (2006). Department of Health: Estates and Facilities Division (HTM) — piped-system inspection, test and maintenance framework, not a UK certificate mandate.
- Pressure regulators for use with medical gases — ISO 10524-1:2018, ISO 10524-2:2018, ISO 10524-3:2019 — regulator frameworks.
- Hart, J. R. (2018). Medical Gas and Vacuum Systems Handbook. National Fire Protection Association — framework.
- Medical Gas Cylinder Storage. (2018). National Fire Protection Association — cylinder-storage framework, not a NABH cubic-metre mandate.
- Sarangi, S., Babbar, S., & Taneja, D. Safety of the medical gas pipeline system. J Anaesthesiol Clin Pharmacol, 34(1), 99-102 — framework.
- Handle medical gases safely. BOC. (2017) — handling framework, not this hospital's SOP.
- Internal documents of this hospital: medical-gas written guidance; cylinder-store checks; backup-test records; piped-system file or recorded absence; utilities, facility-safety, equipment and fire programmes; service directory; applicable-legislation register."""

DISTRIBUTION = f"""Controlled master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Gas-Plant In-Charge')} and the Quality Coordinator.

Copies issued to: staff who change cylinders; theatre, intensive-care and emergency leads who use piped or cylinder gas; contracted pipeline maintainer if outsourced.

The current version is available to all staff at the {D('gas-plant / engineering office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

Superseded versions are withdrawn from all points of use on issue of a revision. One dated copy of each is retained by the Quality Coordinator."""

ABBREVIATIONS = """MGPS — medical gas pipeline system
HTM — Health Technical Memorandum (UK Department of Health medical-gas pipeline guidance; framework only)
DISS — Diameter Index Safety System
NIST — Non-Interchangeable Screw Thread
ISO — International Organization for Standardization
NFPA — National Fire Protection Association
BCGA — British Compressed Gases Association
PESO — Petroleum and Explosives Safety Organisation (applicable-legislation register if it applies; not a paragraph-2 statute of this document)
CAPA — corrective and preventive action
RCA — root-cause analysis
SOP — standard operating procedure"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "FMS.4.a",
        "requirement": "Written guidance governs the implementation of procurement, handling, storage, distribution, usage and replenishment of medical gases.",
        "steps": "Section 3; 5.1 Govern procurement, handling, storage, distribution, use and replenishment",
        "responsible": "Gas-Plant In-Charge; Medical Superintendent (accountable)",
        "records": [
            "Written guidance covering procurement, handling, storage, distribution, usage and replenishment of the gases this hospital actually uses.",
            "Sample records of a delivery accepted, a store check, a distribution and a replenishment that followed the guidance.",
            "Recorded absences for gases not in the service directory.",
            "After-hours cylinder roster.",
        ],
    },
    {
        "oe_code": "FMS.4.b",
        "requirement": "Medical gases are handled, stored, distributed and used in a safe manner",
        "steps": "Section 3; 5.2 Handle, store, distribute and use medical gases safely",
        "responsible": "Gas-Plant In-Charge (store); clinical users (identity check at use)",
        "records": [
            "Store checks showing full and empty segregation, chained upright cylinders, and matched regulators.",
            "Identity-check record at the point of use.",
            "Record that PESO, if it applies, lives on the applicable-legislation register and not in disclaimer paragraph 2.",
        ],
    },
    {
        "oe_code": "FMS.4.c",
        "requirement": "Alternate sources for medical gases, vacuum and compressed air are provided for, in case of failure and their functioning is tested at a predefined frequency",
        "steps": "Section 3; 5.3 Prove alternate sources by a functioning test",
        "responsible": "Gas-Plant In-Charge",
        "records": [
            "Named alternate sources for each gas, vacuum and air actually used, or a recorded absence where a gas is not used.",
            "Functioning-test records: flow from the reserve, vacuum that aspirates, alarms that annunciate, at the predefined frequency.",
            "Record that plant electricity remains the utilities programme's backup test.",
        ],
    },
    {
        "oe_code": "FMS.4.d",
        "requirement": "There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation.",
        "steps": "Section 3; 5.4 Maintain the piped installation, or record that none exists",
        "responsible": "Gas-Plant In-Charge; Medical Superintendent (signs absence or accepts the piped plan)",
        "records": [
            "Piped-system operational, inspection, testing and maintenance file showing last inspection, pressure and alarm test and maintenance — or the signed recorded absence if no piped system exists.",
            "Planned-isolation and clinical-notice records for work on a live oxygen pipe.",
            "Terminal-unit identity and pressure check after work.",
            "Record that HTM, ISO 10524, NFPA and BS EN 12021 are used as frameworks, not as foreign certificates.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.4 v2.1 uses the FMS.5 v2.2 section skeleton.
Wording is this standard's four OEs and v1 substance. Fire-cloned stop-work,
Night Duty Officer as emergency command, Floor Fire Warden, and "roles are
titles not vacancies" do not appear. Gas-Plant In-Charge is the lead; the
after-hours cylinder roster is a gas-handling competence.

Technical substance retained from v1: six acts; HTM / ISO 10524 / NFPA /
BCGA / BS EN 12021 / BOC / Sarangi as frameworks not certificates;
functioning test not paper changeover; piped plan or recorded absence;
PESO not in P2; FMS.4.b and FMS.4.c requirement strings have no terminal
period in the book — preserved in mapping.

Length follows the four OEs (four 5.x subsections). Stop-work is the
genuine do-not-proceed acts for unidentified connection, forced connector,
untested terminal after work, paper changeover, and live-pipe work without
isolation. Disclaimer P2 accreditation-only. No SQL. Status remains draft.
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
        "subtitle": "Standards for medical gases, vacuum and compressed air.",
        "footer_label": "Medical gases, vacuum and compressed air",
        "prepared_by": "«Gas-Plant In-Charge»",
        "acknowledgement_note": "The Gas-Plant In-Charge holds signed acknowledgements of staff who change cylinders or use piped gas, with the induction record. The after-hours cylinder roster is held with those acknowledgements.",
        "control_extra_rows": [
            ["Piped MGPS exists", "«no — recorded absence»", "Gases actually used", "«________»"],
            ["After-hours cylinder roster", "«________»", "Identity check at use", "«second person at the workstation»"],
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
