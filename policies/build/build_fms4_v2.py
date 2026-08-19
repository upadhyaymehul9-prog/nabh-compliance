# -*- coding: utf-8 -*-
"""FMS.4 v2 — medical gases, vacuum and compressed air.

Shape follows FMS.5 v2.2 (section list and order only). Wording is this
standard's OEs and v1 substance, in plain English. Does not overwrite
fms4_draft.json or build_fms4.py. No SQL. No Supabase insert.

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
VERSION = "2.2"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "First v2 shape pass (withdrawn: fire-cloned wording).",
    },
    {
        "version": "2.1",
        "date": "19-08-2026",
        "description": "Same section skeleton as FMS.5 v2.2; wording rebuilt from FMS.4 OEs and v1.",
    },
    {
        "version": "2.2",
        "date": "19-08-2026",
        "description": "Plain-English rewrite. Same rules, facts and intervals. Not an approved master.",
    },
]

PURPOSE = f"""This policy says how {HOSPITAL} runs its programme for medical gases, vacuum (suction) and compressed air.

It covers four jobs:

- written guidance that covers buying, handling, storage, distribution, use and topping up of medical gases;
- handling, storing, distributing and using those gases safely;
- backup sources if the main supply fails, and tests of those sources at a set frequency;
- a plan to operate, inspect, test and maintain a piped medical gas, compressed air and vacuum installation, where a piped system exists.

This is the gas, vacuum and compressed-air programme. It is not the utilities policy's electrical backup (though medical-gas plant may be an essential circuit there). It is not the equipment policy's planned maintenance of a flowmeter listed as a device. It is not the fire plan — though a gas leak is a named emergency that plan must list.

Words marked {D('like this')} are defaults a small hospital can keep. Change the marked text before issue if this hospital needs a different owner, interval or arrangement. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SAFETY_OBJECTIVE = """The gas at the bedside must be the gas that was meant to be there. Do not mix full and empty cylinders. A paper checklist is not a working test of the backup. A copied pipeline manual is not a plan if this hospital only uses cylinders."""

SCOPE = f"""This policy applies to medical gases, medical vacuum and medical compressed air used at {HOSPITAL}. That includes supply from portable cylinders, a manifold (a bank of cylinders feeding a line), or a piped medical gas pipeline system (MGPS — pipes that take gas to wall outlets). It also applies to the people who buy, handle, store, distribute, use, top up, test backups and maintain those systems.

It covers:

- written guidance for buying, handling, storage, distribution, use and topping up of medical gases;
- safe handling, storage, distribution and use;
- backup sources for gases, vacuum and compressed air, and tests at a set frequency;
- operating, inspecting, testing and maintaining piped installation where one exists.

If this hospital has no piped MGPS, the piped-installation plan is a written note against the service directory that no piped system exists. Do not copy a pipeline procedure. Cylinder and manifold duties still apply if gases are used.

If a gas, vacuum or compressed air is not on the service directory (for example piped vacuum in a hospital that uses portable suction only), write down that this hospital does not offer it. Do not copy an intensive-care pipeline procedure.

Essential-circuit electricity may include medical-gas plant, manifold alarms and vacuum pumps. Plant power belongs to the utilities policy. The gas path belongs here.

A leaking cylinder found on a monthly facility round is closed here. Building hazardous materials are housekeeping chemicals, fuels and mercury. Cylinders as medical gas belong to this policy. A surplus regulator leaves this inventory, then follows the unused-material route.

Flowmeters, regulators and suction units may be listed as devices under the equipment policy. ISO 10524-1/2/3 (International Organization for Standardization regulator standards) are the regulator guides this programme uses. The equipment policy still holds the device file if this hospital lists the regulator as equipment.

A medical-gas leak, manifold-room fire, or oxygen-enriched fire is a named emergency in the fire-and-non-fire policy. This policy covers prevention, detection at the plant, isolation and backup supply. Laboratory fire belongs to that fire plan. Oxygen handling belongs here.

Clinical use of gases at the anaesthesia or critical-care workstation stays with those care policies. This policy covers that the gas that arrives is the gas that was meant to arrive, at a pressure the workstation can use.

Buying medical gases is this written guidance. A cylinder that is also a store item still follows this handling method.

The Petroleum and Explosives Safety Organisation (PESO), Gas Cylinder Rules or the Explosives Act appear on the applicable-legislation register if they apply to this occupancy. They are not numbered FMS chapter references. They are not in this document's disclaimer paragraph 2.

Outsourced filling or pipeline-maintenance agreements with service parameters stay with that management-agreement policy. The technical tests remain here.

An empty cylinder is not a biomedical-waste bag. What a patient is told about cost is not a gas tariff.

UK Department of Health Health Technical Memorandum (HTM) Medical Gas Pipeline Systems, National Fire Protection Association (NFPA) medical gas and cylinder storage, British Compressed Gases Association (BCGA), BS EN 12021, BOC handling and Sarangi et al. are guides. They are not pasted protocols. They are not a requirement to hold a UK HTM certificate."""

POLICY_STATEMENT = f"""{HOSPITAL} uses written guidance that covers buying, handling, storage, distribution, use and topping up of the medical gases it actually uses. All six acts are in the guidance. A supplier brochure is not that guidance. A pocket guide used as the hospital standard operating procedure (SOP) is not that guidance. A gas the service directory does not use is written down as not offered.

{HOSPITAL} handles, stores, distributes and uses medical gases safely. Full and empty are kept apart. Cylinders are chained or nested, upright, away from oil, grease, heaters and electrical panels. Pin-index, Diameter Index Safety System (DISS) or Non-Interchangeable Screw Thread (NIST) connections — fittings that only accept the matching gas — are not forced. Identity is checked at the point of use. A cylinder used as a doorstop is not storage.

{HOSPITAL} provides backup sources for medical gases, vacuum and compressed air in case of failure, and tests that they work {D('monthly')}. Gas actually flows from the reserve to a named point of use. Vacuum actually sucks. Alarms actually sound. A paper changeover checklist with no flow is not a test.

{HOSPITAL} keeps an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation where a piped system exists. If none exists, that is a written note signed by the named lead. It is not a pipeline SOP invented for a file. HTM, ISO 10524, NFPA and BS EN 12021 are guides. They are not UK or US certificate requirements.

{HOSPITAL} does not treat these as meeting this policy: a copied HTM manual for a cylinder-only hospital; mixed full and empty cylinders; an untested manifold reserve."""

NON_NEGOTIABLES = f"""These acts are banned. There is no operational exception. "Until the vendor comes" is not an exception.

1. Connecting a cylinder, manifold or wall outlet whose gas identity has not been checked, or forcing a mismatched pin-index, DISS or NIST connector.
2. Mixing full and empty cylinders on the same rack, or using a cylinder as a doorstop.
3. Storing cylinders against a heater, electrical panel, oil or grease, or rolling a portable cylinder on its side down a stair.
4. Treating a paper changeover checklist with no flow as a working test of the reserve.
5. Signing a backup-test sheet for a reserve bank that has never been opened on test, or for portable suction that is in a locked room.
6. Offering a copied HTM 02-01 manual as the piped-installation plan of a hospital that has no piped system, or as this hospital's certificate.
7. Working on a live oxygen pipe without a planned isolation and clinical notice.
8. Putting an empty cylinder into the biomedical-waste stream, or writing PESO / Gas Cylinder Rules into this policy's disclaimer paragraph 2. Those instruments, if they apply, live on the applicable-legislation register.
9. Leaving the piped-versus-no-piped decision unrecorded. Either the piped plan is operated, or the named lead has signed that no piped system exists.

If you find mixed full and empty cylinders, an untested reserve, a forced connector, or a piped outlet that has no label, report it the same shift to the {D('Gas-Plant In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Govern procurement, handling, storage, distribution, use and replenishment

The six acts are listed because a hospital can buy oxygen correctly and still store it against a heater, or use it correctly at the theatre table and never top up the reserve. BCGA, BOC Handle medical gases safely, and NFPA Medical Gas Cylinder Storage are handling and storage guides. ISO 10524-1/2/3 are regulator guides. They are not pasted as this hospital's guidance.

The {D('Gas-Plant In-Charge')} holds written guidance covering: which gases this hospital actually uses (oxygen as a minimum if any medical gas is used; nitrous oxide, medical air, carbon dioxide, vacuum, compressed air only if on the service directory); who may buy from which licensed source; how a delivery is accepted (identity, pressure, pin-index or DISS, expiry or batch as the supplier provides); and how storage, distribution, use and topping up are each governed.

Gases in use: {BLANK}. If the directory does not list a gas, write down that this hospital does not use it. Guidance that covers cylinders in stores and is silent on who changes a cylinder at 2 a.m. is not this guidance. Guidance that names medical air and vacuum in the title for a hospital that has neither is not this guidance.

The named competent person who changes a cylinder after hours is {D('the named person on the after-hours cylinder roster')}. That is a gas-handling skill. It is not an emergency-command title taken from the fire policy.""",

f"""5.2 Handle, store, distribute and use medical gases safely

Keep full and empty apart. Chain or nest cylinders, upright, away from oil, grease, heaters and electrical panels. Do not force pin-index, DISS or NIST connections. Regulators match ISO 10524 as the guide. Do not use a sparking tool in an oxygen-enriched area. Cap portable cylinders in transit. Do not roll them on their side down a stair.

NFPA cylinder storage and BOC inform those rules. They are not a NABH cubic-metre threshold for every small hospital. The local fire authority's conditions on the occupancy may add store-room conditions. This section still covers how a porter moves a cylinder.

Watch for: a "full" rack that contains empties; a cylinder used as a doorstop; grease on an oxygen regulator; a theatre that opens a new cylinder without a second person to check the gas identity.

The {D('Gas-Plant In-Charge')} holds, with clinical users at the point of use, how staff handle, store, distribute and use, including the check that the gas at the workstation is the gas intended.

PESO / Gas Cylinder Rules, if they apply, live on the applicable-legislation register. They are not restated as a NABH protocol here.""",

f"""5.3 Prove alternate sources by a functioning test

Backup oxygen is the reserve that will supply the points of use when the primary manifold bank, primary cylinders at the bedside, or primary concentrator fails. That may be a second manifold bank, a reserve cylinder set sized for the duration this hospital has defined, or a documented diversion.

Backup vacuum is portable suction on every critical point of use if the piped vacuum fails, or a second pump. Backup compressed air or medical air is the reserve this hospital has defined, or a written note that that gas is not used.

HTM Medical Gas Pipeline Systems and Sarangi et al. are pipeline-safety guides for changeover and alarm. They are not a requirement to install a piped system.

Watch for: a reserve bank that has never been opened on test; a changeover that is manual at 3 a.m. with no one trained; "portable suction available" that is in a locked sterile-supply room.

The test is a functioning test. Gas actually flows from the backup source to a named point of use. Vacuum actually sucks. Alarms actually sound. A paper changeover checklist with no flow is not a test.

The {D('Gas-Plant In-Charge')} holds which backup source exists for each gas, vacuum and air this hospital uses, the functioning-test method, and the set frequency {D('monthly')}. Plant electricity remains the utilities policy's backup test. This section is the gas path.""",

f"""5.4 Maintain the piped installation, or record that none exists

If this hospital has no piped medical gas pipeline system, this section is a written note against the service directory, signed by the {D('Gas-Plant In-Charge')}. It is not a pipeline SOP invented for a file.

If a piped system exists, HTM Medical Gas Pipeline Systems is the inspection, test and maintenance guide (identity, pressure, alarm, isolation, anti-confusion, oil-free air as BS EN 12021 where medical air is piped). ISO 10524-2 is the line-regulator guide. NFPA Medical Gas and Vacuum Systems Handbook is a further guide. None of these is a UK or US certificate requirement for an Indian small hospital.

The {D('Gas-Plant In-Charge')} holds: the operational plan (who may isolate a zone, who may open a plant room); the inspection plan (plant, alarms, wall outlets, labelling); the testing plan (pressure, identity after work, alarm function); the maintenance plan (filters, dryers, pumps, manifolds); and the rule that work on a live oxygen pipe is a planned isolation with clinical notice.

A commissioning certificate from the year the pipe was laid is not this plan. A wall outlet that delivers the wrong gas after a repair is a failure of this policy. It is also a fire-and-non-fire emergency if patients are on the line. The equipment policy may still hold a regulator device file. The pipeline is here.""",
]

STOP_WORK = f"""Do not go ahead if you are about to do any of the following:

- connect a cylinder, manifold or wall outlet whose identity has not been checked;
- force a mismatched pin-index, DISS or NIST connector;
- use a piped outlet after work on that zone until identity and pressure have been tested;
- sign a backup-test sheet for a reserve that did not flow, a vacuum that did not suck, or an alarm that did not sound;
- start work on a live oxygen pipe without a planned isolation and clinical notice.

Cap the cylinder. Leave the connector unforced. Leave the zone out of use. Leave the test unsigned. Tell the {D('Gas-Plant In-Charge')} the same shift. If that person is not on site, tell the {D('named person on the after-hours cylinder roster')}.

Refusing in good faith to connect an unidentified cylinder, or to sign a paper changeover as a working test, is not a disciplinary matter. Do not record the connection or the test as done until identity was checked or flow was seen."""

RESPONSIBILITY = f"""These are the jobs this medical-gas programme needs. In a small hospital the gas-plant lead may be the same person as the facilities Maintenance In-Charge. They still keep this file as the gas file. Do not merge it into a combined fire-and-cylinder binder.

RACI in the snapshot below means: R = does the work; A = accountable (the person who must make sure it is done); C = consulted.

Medical Superintendent (head of the institution)
- Accountable that medical gases, vacuum and compressed air are managed as this policy requires.
- Signs the written note if no piped system exists, or accepts the piped plan if one does.

{D('Gas-Plant In-Charge')} (named engineering or gas-plant lead)
- Holds the written guidance covering the six acts, store checks, identity-check method, functioning-test records, and the piped-system file or the written note that none exists.
- Names the {D('named person on the after-hours cylinder roster')} who is competent to change a cylinder when the lead is not on site.
- Orders planned isolation of a live oxygen pipe with clinical notice.

Clinical users (theatre, intensive or high-dependency care, emergency, labour if gases are used there)
- Check gas identity at the point of use.
- Do not force a mismatched connector.
- Report a hiss, a manifold alarm, or an outlet that has no label.

Quality Coordinator
- Audits the records in section 8.

Contracted pipeline maintainer, if outsourced
- Works to the inspection, test and maintenance plan in this policy. Outsourcing agreements stay with that management-agreement policy.

All staff who move or store cylinders
- Keep full and empty apart. Do not use a cylinder as a doorstop. Do not put an empty cylinder in the biomedical-waste stream.

A RACI snapshot:

- Written guidance (six acts): Gas-Plant In-Charge (R/A)
- Safe handling and identity check: Gas-Plant In-Charge (R for store); clinical user (R at the point of use)
- Functioning tests of backup sources: Gas-Plant In-Charge (R/A)
- Piped plan or written note that none exists: Gas-Plant In-Charge (R); Medical Superintendent (A)
- After-hours cylinder change: named person on the after-hours cylinder roster (R); Gas-Plant In-Charge (A)
- Audit: Quality Coordinator (R); Medical Superintendent (A)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')} (four times a year). The audit looks at the store, the plant and the records. Looking only at a binder is not enough.

What is checked each quarter:

- Written guidance covers buying through topping up of the gases actually used, including who changes a cylinder after hours. Unused gases are written down as not used.
- Full and empty are kept apart. Cylinders are chained upright. Identity is checked at use. A cylinder used as a doorstop is a finding.
- Functioning backup tests show flow from the reserve, vacuum that sucks, and alarms that sound, at the set frequency. A paper changeover is a finding.
- Piped-system maintenance is last inspection, pressure and alarm test and maintenance, not a commissioning certificate — or a signed written note if no piped system exists.
- Plant electricity is left with the utilities policy. A leak or wrong-gas event is left with the fire-and-non-fire policy as the emergency action, and closed here as the gas path.
- PESO is not invented in disclaimer paragraph 2. Biomedical-waste colours are not used as cylinder disposal.

Any failure to meet this policy is a finding. The Gas-Plant In-Charge owns the corrective action.

Root-cause analysis (RCA — finding why something went wrong) is required when: a wrong gas reached a workstation; a reserve was signed as tested without flow; full and empty were found mixed; a live oxygen pipe was worked without isolation; or a piped outlet had no label.

Corrective and preventive action (CAPA — the fix and the step that stops it happening again) is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')} (once a year), and sooner after a wrong-gas or empty-reserve event, a change to the service directory that adds or withdraws a gas, or a decision to install or decommission a piped system."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who buy, store, change or use medical gases, and staff who may isolate a piped zone, are trained on this policy at induction, before first unsupervised cylinder change or piped use, and {D('once a year')} after that. Training covers: the six acts in the written guidance; keeping full and empty apart; identity check at use; not forcing a connector; the functioning test of the reserve; and, if a piped system exists, planned isolation with clinical notice. The after-hours cylinder roster is held by the Gas-Plant In-Charge.

Staff acknowledgement

I have read this Medical Gases, Vacuum and Compressed Air policy of {HOSPITAL}. I will not connect a cylinder whose identity I have not checked. I will not force a mismatched connector. I will not sign a paper changeover as a working test. I will not put an empty cylinder in the biomedical-waste stream.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/04')}
Issue number: {D('01')}
Version: 2.2 (template test — plain English; not an approved master)
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

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.4 (this policy is written so those requirements are met in day-to-day work; it is not a commentary on the standard).
- Medical Gases. British Compressed Gases Association — handling guide.
- Respiratory equipment. Compressed gases for breathing apparatus. BS EN 12021:2014 — medical-air quality guide where medical air is supplied.
- Medical Gas Pipeline Systems. (2006). Department of Health: Estates and Facilities Division (HTM) — piped-system inspection, test and maintenance guide, not a UK certificate requirement.
- Pressure regulators for use with medical gases — ISO 10524-1:2018, ISO 10524-2:2018, ISO 10524-3:2019 — regulator guides.
- Hart, J. R. (2018). Medical Gas and Vacuum Systems Handbook. National Fire Protection Association — guide.
- Medical Gas Cylinder Storage. (2018). National Fire Protection Association — cylinder-storage guide, not a NABH cubic-metre rule.
- Sarangi, S., Babbar, S., & Taneja, D. Safety of the medical gas pipeline system. J Anaesthesiol Clin Pharmacol, 34(1), 99-102 — guide.
- Handle medical gases safely. BOC. (2017) — handling guide, not this hospital's SOP.
- Internal documents of this hospital: medical-gas written guidance; cylinder-store checks; backup-test records; piped-system file or written note that none exists; utilities, facility-safety, equipment and fire policies; service directory; applicable-legislation register."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Gas-Plant In-Charge')} and the Quality Coordinator.

Copies issued to: staff who change cylinders; theatre, intensive-care and emergency leads who use piped or cylinder gas; contracted pipeline maintainer if outsourced.

The current version is available to all staff at the {D('gas-plant / engineering office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

When a new version is issued, take old copies out of use. The Quality Coordinator keeps one dated copy of each old version."""

ABBREVIATIONS = """MGPS — medical gas pipeline system
HTM — Health Technical Memorandum (UK Department of Health medical-gas pipeline guidance; guide only)
DISS — Diameter Index Safety System
NIST — Non-Interchangeable Screw Thread
ISO — International Organization for Standardization
NFPA — National Fire Protection Association
BCGA — British Compressed Gases Association
PESO — Petroleum and Explosives Safety Organisation (applicable-legislation register if it applies; not a paragraph-2 statute of this document)
SOP — standard operating procedure
CAPA — corrective and preventive action
RCA — root-cause analysis
RACI — Responsible, Accountable, Consulted, Informed"""

DISCLAIMER, STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "FMS.4.a",
        "requirement": "Written guidance governs the implementation of procurement, handling, storage, distribution, usage and replenishment of medical gases.",
        "steps": "Section 3; 5.1 Govern procurement, handling, storage, distribution, use and replenishment",
        "responsible": "Gas-Plant In-Charge; Medical Superintendent (accountable)",
        "records": [
            "Written guidance covering buying, handling, storage, distribution, use and topping up of the gases this hospital actually uses.",
            "Sample records of a delivery accepted, a store check, a distribution and a top-up that followed the guidance.",
            "Written notes for gases not on the service directory.",
            "After-hours cylinder roster.",
        ],
    },
    {
        "oe_code": "FMS.4.b",
        "requirement": "Medical gases are handled, stored, distributed and used in a safe manner",
        "steps": "Section 3; 5.2 Handle, store, distribute and use medical gases safely",
        "responsible": "Gas-Plant In-Charge (store); clinical users (identity check at use)",
        "records": [
            "Store checks showing full and empty kept apart, chained upright cylinders, and matched regulators.",
            "Identity-check record at the point of use.",
            "Note that PESO, if it applies, lives on the applicable-legislation register and not in disclaimer paragraph 2.",
        ],
    },
    {
        "oe_code": "FMS.4.c",
        "requirement": "Alternate sources for medical gases, vacuum and compressed air are provided for, in case of failure and their functioning is tested at a predefined frequency",
        "steps": "Section 3; 5.3 Prove alternate sources by a functioning test",
        "responsible": "Gas-Plant In-Charge",
        "records": [
            "Named backup sources for each gas, vacuum and air actually used, or a written note where a gas is not used.",
            "Functioning-test records: flow from the reserve, vacuum that sucks, alarms that sound, at the set frequency.",
            "Note that plant electricity remains the utilities policy's backup test.",
        ],
    },
    {
        "oe_code": "FMS.4.d",
        "requirement": "There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum installation.",
        "steps": "Section 3; 5.4 Maintain the piped installation, or record that none exists",
        "responsible": "Gas-Plant In-Charge; Medical Superintendent (signs absence or accepts the piped plan)",
        "records": [
            "Piped-system operational, inspection, testing and maintenance file showing last inspection, pressure and alarm test and maintenance — or the signed written note if no piped system exists.",
            "Planned-isolation and clinical-notice records for work on a live oxygen pipe.",
            "Wall-outlet identity and pressure check after work.",
            "Note that HTM, ISO 10524, NFPA and BS EN 12021 are used as guides, not as foreign certificates.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-19). FMS.4 v2.2 is a plain-English rewrite of v2.1.
Same rules, facts, intervals and statute scoping. FMS.4.b and FMS.4.c
requirement strings have no terminal period. No SQL. Status remains draft.
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
        "subtitle": "How this hospital buys, stores, uses and backs up medical gases.",
        "footer_label": "Medical gases, vacuum and compressed air",
        "prepared_by": "«Gas-Plant In-Charge»",
        "acknowledgement_note": "The Gas-Plant In-Charge keeps signed acknowledgements of staff who change cylinders or use piped gas, with the induction record. The after-hours cylinder roster is held with those acknowledgements.",
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
