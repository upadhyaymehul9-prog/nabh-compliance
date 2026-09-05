# -*- coding: utf-8 -*-
"""Generate HCO Full MOM.1–MOM.11 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_mom_v2.py

Official portal PDF has 11 MOM standards / 68 OEs (not 9). All 11 are drafted.
Does not touch AAC, COP, or SHCO. Always sets explicit HCO draft_label via
hco_document_control (no "not an approved master" leftover).
HCO drafts/previews write to policies/drafts_hco and policies/build/preview_hco.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from nabh_text_normalize import distribution_dedupe  # noqa: E402
from hco_cop_v2_common import (  # noqa: E402
    hco_oe_count_clause,
    hco_related_duties_clause,
    truncate_word_safe,
)
from hco_mom_v2_common import (  # noqa: E402
    BLANK,
    CHAPTER,
    D,
    DRAFT_LABEL,
    HCO_EDITION_LABEL,
    HOSPITAL,
    PROGRAMME,
    STOP_WORK_PROPOSALS,
    VERSION,
    hco_document_control,
    stop_work_text,
)
from hco_mom_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_mom_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_mom_interpretations.json"
GUIDEBOOK_OCR = ROOT / "policies/source/hco6_mom_guidebook_ocr.txt"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 only where MOM OE text names legal duties.
# MOM.9: OE line does not cite NDPS; chapter references do. See judgment flags.
STATUTE_BY_STD: dict[int, str | None] = {
    7: "applicable laws governing who may administer medications as named in NABH MOM.7.a",
    9: "the Narcotic Drugs and Psychotropic Substances Act, 1985, and applicable rules for chemotherapeutic agents and radio-pharmaceuticals as referenced for NABH MOM.9",
}

PREPARED_BY: dict[int, str] = {
    1: "Medication Safety Officer",
    2: "Drug and Therapeutics Committee Chair",
    3: "Pharmacy In-Charge",
    4: "Medical Superintendent",
    5: "Medical Superintendent",
    6: "Pharmacy In-Charge",
    7: "Nursing Superintendent",
    8: "Medication Safety Officer",
    9: "Pharmacy In-Charge",
    10: "OT In-Charge",
    11: "Stores In-Charge",
}

POLICY_TITLES: dict[int, str] = {
    1: "Safe Pharmacy Services and Medication Management",
    2: "Hospital Formulary",
    3: "Storage and Availability of Medications",
    4: "Safe and Rational Prescription of Medications",
    5: "Uniform Medication Orders",
    6: "Safe Dispensing of Medications",
    7: "Safe Administration of Medications",
    8: "Monitoring after Medication Administration",
    9: "Narcotics, Psychotropics, Chemotherapy and Radio-pharmaceuticals",
    10: "Implantable Prosthesis and Medical Devices",
    11: "Storage and Availability of Medical Supplies and Consumables",
}

CHAPTER_INTENT = (
    "The organisation has a safe and organised medication management process. "
    "Availability, safe storage, prescription, dispensing and administration of "
    "medications are governed by written guidance. A medication safety officer "
    "is designated. The hospital formulary is developed, implemented and updated. "
    "Pharmacy has oversight of medications stocked out of the pharmacy. "
    "Reconciliation occurs at transition points. Patients are monitored after "
    "administration. Near misses, medication errors and adverse drug reactions "
    "are reported and analysed. Medications also include blood, implants and "
    "devices. Medical supplies and consumables are available for use."
)


def clean_text(s: str) -> str:
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def step_title(i: int, oe_text: str) -> str:
    t = oe_text.split(".")[0].strip()
    t = truncate_word_safe(t, 72)
    return f"5.{i} {t}"


def load_interpretations() -> dict[str, str]:
    if not INTERP_JSON.exists():
        raise FileNotFoundError(INTERP_JSON)
    data = json.loads(INTERP_JSON.read_text(encoding="utf-8"))
    return {k: clean_text(v) for k, v in data.items()}


def build_steps(n: int, oes: list[dict], bodies: dict[str, str], interps: dict[str, str]) -> list[str]:
    steps = []
    for i, oe in enumerate(oes, start=1):
        title = step_title(i, oe["text"] or oe["oe_code"])
        body = bodies.get(oe["oe_code"])
        if not body:
            raise KeyError(f"Missing method body for {oe['oe_code']}")
        extras = []
        note = (interps.get(oe["oe_code"]) or "").strip()
        if note:
            extras.append(f"Method note (from guidebook interpretation): {note}")
        elif oe.get("star"):
            extras.append(
                "Method note: Follow the organisation's written guidance for this asterisked "
                "element; keep records that show the guidance was followed for the sampled cases."
            )
        if oe.get("star"):
            extras.append(
                "This objective element is asterisked in the official Standards PDF "
                "— documentation of the process is required."
            )
        if oe["level"] == "CORE":
            extras.append(
                "This is a CORE objective element — non-compliance is not acceptable for accreditation."
            )
        extra = ("\n\n" + "\n\n".join(extras)) if extras else ""
        steps.append(f"{title}\n\n{body}{extra}")
    return steps


def non_negotiables(n: int, oes: list[dict]) -> str:
    items = []
    for i, oe in enumerate(oes, start=1):
        short = clean_text(oe["text"] or oe["oe_code"])
        short = truncate_word_safe(short, 110)
        items.append(f"{i}. Do not skip: {short}")
    if n in STOP_WORK_PROPOSALS:
        items.append(
            f"{len(items)+1}. Do not bypass the stop-work authority in section 6 when the trigger conditions are met."
        )
    items.append(
        f"{len(items)+1}. Staff who see a MOM.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Medication Safety Officer')}."
    )
    return "\n".join(items)


# Fix #5 — hand-authored per-OE evidence records, matching the quality bar
# AAC.1 / SHCO HIC.1 / HCO ROM / HCO FMS / HCO PSQ / HCO IPC / HCO PRE already
# demonstrate.
MOM_RECORDS: dict[str, list[str]] = {
    "MOM.1.a": [
        "Documented Medication Management Manual covering procurement through administration, monitoring and error reporting.",
        "Drug and Therapeutics Committee approval record for the guidance.",
        "Staff training record at induction and annually, with current copies available in pharmacy, emergency, ICU, OT and wards.",
    ],
    "MOM.1.b": [
        "DTC constitution record naming pharmacy, medical, nursing and specialty representation.",
        "Written terms of reference covering formulary, high-risk/emergency lists, storage oversight, verbal-order/reconciliation rules and error review.",
        "Quarterly meeting minutes naming decisions, owners and due dates.",
    ],
    "MOM.1.c": [
        "Annual, or sooner, process-review record by the DTC.",
        "Written change record to a specific process, not a restatement of the same rule.",
        "Open-action tracking record until closure by the Medication Safety Officer.",
    ],
    "MOM.1.d": [
        "Written after-hours/stock-out procedure naming who is authorised and how a second-person check is used.",
        "Reconciliation record showing after-hours issues entered the next working day.",
        "Quarterly test record of the after-hours path by the Pharmacy In-Charge.",
    ],
    "MOM.1.e": [
        "Dated circular or briefing record for a medication-management process, formulary, high-risk/emergency list or recall change.",
        "Distribution list and acknowledgement record held by the Quality Coordinator.",
        "Confirmation the change was communicated before it took effect, not only filed in minutes.",
    ],
    "MOM.2.a": [
        "Formulary list built collaboratively by pharmacy, clinicians and nursing, matched to the defined clinical scope (AAC.1).",
        "Formulary entries recording generic name, strength, dosage form and high-risk flag.",
        "Medical Superintendent's approval record for the first issue.",
    ],
    "MOM.2.b": [
        "Annual formulary review record with additions, deletions and restrictions minuted with clinical reason.",
        "Urgent-addition or shortage-substitution record ratified at the next meeting.",
        "Dated current-formulary cover record.",
    ],
    "MOM.2.c": [
        "Formulary availability record at prescribing locations — OPD, wards, ICU, emergency, OT, HIS/intranet.",
        "Outdated-copy removal record when a new version is issued.",
        "Quarterly availability spot-check record by the Quality Coordinator.",
    ],
    "MOM.2.d": [
        "Prescription-versus-formulary audit record.",
        "Non-formulary-prescribing flag record from pharmacy to the Medication Safety Officer.",
        "DTC record of any department's repeated non-adherence tabled for review.",
    ],
    "MOM.2.e": [
        "Procurement record showing approved supplier, receipt quality checks, batch and expiry logged.",
        "Rejected-delivery record for any item failing identity, integrity or cold-chain check.",
        "Cross-reference to the MOM.1.d stock-out procedure for any off-procedure purchase.",
    ],
    "MOM.2.f": [
        "Written non-formulary request record — clinical justification, approval, source, batch and indication.",
        "Formulary-amendment consideration record where an item is needed routinely.",
        "Same-shift retrospective documentation record for emergency non-formulary use.",
    ],
    "MOM.3.a": [
        "Storage-condition record (temperature, light, humidity) against manufacturer recommendation.",
        "Twice-daily refrigerator-temperature log with excursion-reporting record.",
        "Access-control record for the main pharmacy and controlled-drug cupboards.",
    ],
    "MOM.3.b": [
        "Documented inventory-control method — FEFO, maximum/minimum levels, indent cycle.",
        "Monthly expiry and slow-moving-stock review record.",
        "Stock-movement traceability record from receipt to issue for a sampled item.",
    ],
    "MOM.3.c": [
        "Current DTC-defined high-risk medication list, updated at least annually and after a related incident.",
        "Posted-list record at pharmacy and every location storing high-risk items.",
        "Staff training record on the high-risk list.",
    ],
    "MOM.3.d": [
        "DTC record naming locations where each high-risk medication is clinically necessary.",
        "Pharmacy issue record confirming no high-risk floor stock went to an unlisted area.",
        "Walk-round record matching the location list to actual storage.",
    ],
    "MOM.3.e": [
        "Physical-separation record for LASA items and different concentrations — separate bins/shelves, tall-man lettering where used.",
        "Monthly storage-round check record by the Pharmacy In-Charge.",
        "Escalation record for any LASA pair or concentration found stored together.",
    ],
    "MOM.3.f": [
        "DTC-defined emergency-medication list with uniform layout across crash carts and trolleys.",
        "Sealed or checklist-controlled trolley-inventory record.",
        "Nursing Superintendent and Pharmacy In-Charge layout-agreement record.",
    ],
    "MOM.3.g": [
        "Twenty-four-hour availability confirmation record for emergency medications at every defined location.",
        "Immediate-replenishment log after use, before the trolley returns to service.",
        "Each-shift nursing check record against the emergency-medication list.",
    ],
    "MOM.4.a": [
        "DTC-named rational-prescribing reference (for example WHO/national essential-medicines principles, hospital antimicrobial policy).",
        "Prescription-audit record sampled against this guidance.",
        "Training record on rational prescribing.",
    ],
    "MOM.4.b": [
        "Published minimum-prescription-requirement list — patient name/ID, generic name, route, strength, frequency, date/time, prescriber signature.",
        "Pharmacy/nursing hold record for any order failing the minimum, except through the documented emergency path.",
        "Sample-prescription record confirming the minimum was met.",
    ],
    "MOM.4.c": [
        "Drug-allergy and previous-ADR ascertainment record before prescribing, including \"none known\" entries.",
        "Red-alert allergy-band record where an allergy is recorded.",
        "Allergy-status carry-forward record on admission and transfer notes.",
    ],
    "MOM.4.d": [
        "Prescribing-assistance mechanism record — formulary access, dose-range information, pharmacy clarification of unclear orders, or e-prescribing/CDS where used.",
        "Record of orders clarified by pharmacy before dispensing.",
        "Confirmation the mechanism is working, not a static poster.",
    ],
    "MOM.4.e": [
        "Reconciled-medication-list record at admission, unit transfer and discharge.",
        "Discrepancy-resolution record between the reconciling clinician and the prescriber.",
        "Pharmacy support record for high-risk or polypharmacy reconciliations.",
    ],
    "MOM.4.f": [
        "Verbal-order record showing read-back — drug, dose, route, frequency, patient — before administration.",
        "Prescriber countersignature record within 24 hours, or before the next dose.",
        "Confirmation verbal orders were not used for excluded categories except under the documented emergency rule.",
    ],
    "MOM.4.g": [
        "Quarterly prescription-audit record — minimum requirements, allergy documentation, formulary adherence, high-risk dose checks.",
        "Sample-size record meeting the defined minimum per quarter.",
        "DTC presentation record of audit results.",
    ],
    "MOM.4.h": [
        "CAPA record from audit findings with owner and due date.",
        "Closure-tracking record by the Medication Safety Officer.",
        "Example action record — prescriber feedback, guidance change, or training.",
    ],
    "MOM.5.a": [
        "Authorised-prescriber list held by the Medical Superintendent.",
        "Supervised-order record for interns/residents naming a supervisor.",
        "Confirmation an order from a person not on the list was not acted on.",
    ],
    "MOM.5.b": [
        "Medication-chart/order-sheet record showing the uniform location with patient name and unique ID.",
        "Same-shift transcription record for any sticker or loose-slip order onto the uniform chart.",
        "Nursing Superintendent's record-audit check for location uniformity.",
    ],
    "MOM.5.c": [
        "Legible, dated, timed and signed (or authenticated) order sample.",
        "Illegible-order contact-and-rewrite record.",
        "Late-entry record following medical-record rules — timed and marked as late.",
    ],
    "MOM.5.d": [
        "Order-content completeness record — medicine name, route, strength, frequency/time.",
        "PRN-order record including indication and maximum frequency.",
        "Cross-reference to the MOM.4.b minimum-requirement check.",
    ],
    "MOM.6.a": [
        "Dispensing record confirming right patient, drug, dose, route and frequency against a valid order.",
        "Product-inspection record — integrity, expiry, storage condition — before issue.",
        "Floor-stock issue-to-ward dispensing record.",
    ],
    "MOM.6.b": [
        "Recall-notice file with affected batch(es), quarantine record and date.",
        "Patient-identification record where the recalled batch was administered.",
        "Medication Safety Officer and treating-team notification record.",
    ],
    "MOM.6.c": [
        "FEFO and monthly expiry-round record.",
        "Withdrawal-from-clinical-area record for near-expiry items.",
        "Emergency-trolley short-dated-item replacement record before expiry.",
    ],
    "MOM.6.d": [
        "Labelled-dispensed-medication sample — patient identity where applicable, medicine name, strength, route, frequency, expiry.",
        "Ward floor-stock multi-dose container labelling record — drug name, strength, expiry, date opened.",
        "Confirmation no unlabelled syringe, cup or strip was issued.",
    ],
    "MOM.6.e": [
        "High-risk dispensing-verification record — second pharmacist or trained second checker against the order and patient record.",
        "Recorded verification for a sampled high-risk dispense.",
        "Escalation record for any single-unchecked-reading dispense.",
    ],
    "MOM.6.f": [
        "Written medication-return procedure — identity/integrity check, restock-or-destroy decision, record of return.",
        "Confirmation controlled drugs, reconstituted items and temperature-excursion items were not restocked.",
        "Cross-reference to the MOM.7.k patient's-own-medicines process.",
    ],
    "MOM.7.a": [
        "Authorised-administration-personnel list held by the Nursing Superintendent and Medical Superintendent.",
        "Documented-supervision record for student administration.",
        "Confirmation no unlisted person administered a drug.",
    ],
    "MOM.7.b": [
        "Prepared-medication labelling record — drug, strength, patient, route, time prepared — before a second drug preparation.",
        "Observation record confirming no two unlabelled syringes on one tray.",
        "Applicability record across OT, ICU, emergency and wards.",
    ],
    "MOM.7.c": [
        "Patient-identification record using at least two identifiers immediately before administration.",
        "Confirmation identification was not based on bed number or attendant statement alone.",
        "Stopped-administration record where identity could not be confirmed.",
    ],
    "MOM.7.d": [
        "Medication-verification-against-order record before administration.",
        "Physical-inspection record — clarity, integrity, expiry, formulation.",
        "Stopped-administration record for a mismatch or defect found.",
    ],
    "MOM.7.e": [
        "Strength/dose verification-from-order record, including calculation check for weight-based or infusion doses.",
        "Second-check record for high-risk medications.",
        "Confirmation no bedside conversion occurred outside a documented pharmacy-prepared change.",
    ],
    "MOM.7.f": [
        "Route-verification-from-order record before administration.",
        "Confirmation oral products were not given intravenously.",
        "Stopped-administration record for a route mismatch.",
    ],
    "MOM.7.g": [
        "Timing-verification-from-order record — scheduled time, interval, hold instructions.",
        "Prescriber-review record for a dose given outside the allowed window, except documented emergency use.",
        "Administration-time entry on the medication chart.",
    ],
    "MOM.7.h": [
        "Line-tracing record from patient to source before injecting or infusing into a catheter or tubing.",
        "Line-labelling record where more than one lumen or device is in use.",
        "Training record for ICU, OT, emergency and ward staff on catheter/tubing mis-connection prevention.",
    ],
    "MOM.7.i": [
        "Medication-chart documentation record at time of giving — drug, dose, route, time, administrator identifier.",
        "Omitted or held-dose record with reason.",
        "Confirmation documentation was not left to end of shift.",
    ],
    "MOM.7.j": [
        "Written self-administration measures naming which drugs, bedside storage and nursing-recording method.",
        "DTC or treating-team decision record on when self-administration is allowed.",
        "Confirmation no uncontrolled bedside hoarding of hospital stock occurred.",
    ],
    "MOM.7.k": [
        "Declared-outside-medication record at admission.",
        "Pharmacy or treating-doctor identification record for the brought-in medication.",
        "Patient's-own-medicines documentation — labelled, stored securely, charted — or sent-home record.",
    ],
    "MOM.8.a": [
        "Written monitoring guidance naming what to watch and when to escalate, matched to drug and clinical setting.",
        "Recorded post-administration monitoring for a sampled case (for example post-opioid sedation/respiration, post-chemotherapy).",
        "Escalation record where monitoring triggered a response.",
    ],
    "MOM.8.b": [
        "Medication-change record based on monitoring findings — drug changed, held or dose-adjusted.",
        "Rewritten-order record under MOM.5 for the change.",
        "Confirmation the treating doctor was informed, not silently continued.",
    ],
    "MOM.8.c": [
        "Defined near-miss, medication-error and ADR reporting system — incident form or electronic equivalent, plus pharmacovigilance reporting where applicable.",
        "Sample of captured near-miss and error reports.",
        "Medication Safety Officer's ownership record of the capture system.",
    ],
    "MOM.8.d": [
        "Reporting-timeframe record — immediate for unsafe situations, same-shift for other incidents, within 24 hours for ADRs.",
        "Delayed-discovery record marked as delayed when found late.",
        "DTC record of any tightened reporting time.",
    ],
    "MOM.8.e": [
        "Quarterly analysis record by the DTC — type, stage, high-risk-drug involvement, harm.",
        "System-cause analysis record, not individual-blame-only.",
        "Medication Safety Officer's collected-report file.",
    ],
    "MOM.8.f": [
        "CAPA record from analysis, timed and closed (for example storage separation, second-check rule, formulary restriction).",
        "Quarterly audit inclusion record for open medication CAPA.",
        "Deeper-review record triggered by repeat events of the same type.",
    ],
    "MOM.9.a": [
        "Combined-programme ownership record by the Pharmacy In-Charge and Medication Safety Officer for narcotics/psychotropics, chemotherapy and radio-pharmaceuticals.",
        "Out-of-scope declaration record for any class not provided, confirming it is not stocked.",
        "Confirmation the full chain (9.b–9.e) applies where in scope.",
    ],
    "MOM.9.b": [
        "Authorised-prescriber record by class — narcotics/psychotropics, chemotherapy, radio-pharmaceuticals.",
        "Confirmation no verbal chemotherapy order was used except under the documented emergency rule.",
        "Pharmacy dispensing-refusal record for an unauthorised signature.",
    ],
    "MOM.9.c": [
        "Locked, access-controlled storage record with register for narcotics and psychotropics.",
        "Separate-storage record for chemotherapeutic agents and radio-pharmaceuticals per licence/manufacturer instruction.",
        "Named key/access-rights record.",
    ],
    "MOM.9.d": [
        "Required-facility preparation record — cytotoxic cabinet or designated hot lab — by qualified personnel.",
        "PPE, spill-kit and waste-stream readiness record before preparation.",
        "Contracted-provider receipt-check record where preparation is off-site.",
    ],
    "MOM.9.e": [
        "Narcotic/psychotropic register — receipt, issue, administration, wastage, balance.",
        "Chemotherapy administration record — protocol, dose, batch, given-by.",
        "Radio-pharmaceutical log and biomedical-waste/AERB disposal record.",
    ],
    "MOM.10.a": [
        "Approved-item list against national/international recognised guidelines or approvals (for example CDSCO/Medical Devices Rules).",
        "OT/cath-lab and Biomedical ownership record of the list.",
        "Documented trial or compassionate-pathway approval record for any item without recognised approval.",
    ],
    "MOM.10.b": [
        "Written mechanism for implant/device use — request and approval, sterile-supply chain, intra-operative timeout confirming the implant.",
        "OT In-Charge or relevant lab in-charge ownership record.",
        "Identifier-recording record — cross-reference MOM.10.d.",
    ],
    "MOM.10.c": [
        "Pre-implant counselling record — expected benefit, material risks, alternatives, post-implant precautions.",
        "Medical-record entry confirming counselling occurred.",
        "Emergency-implant as-soon-as-practicable counselling record.",
    ],
    "MOM.10.d": [
        "Batch/serial number recorded in the patient's medical record.",
        "Same identifier recorded in the master implant logbook.",
        "Same identifier recorded in the discharge summary.",
    ],
    "MOM.10.e": [
        "Recall-trace record from the master logbook for every affected batch.",
        "Treating-team and patient-contact record where required.",
        "Recall-file closure record — notice, patients identified, actions taken.",
    ],
    "MOM.11.a": [
        "Defined acquisition process — approved vendors, specifications, receipt check.",
        "Stores In-Charge ownership record.",
        "Next-working-day entry record for any documented emergency purchase.",
    ],
    "MOM.11.b": [
        "Intended-use record — sterile items kept sterile, single-use items not reused, opening-date on multi-use bottles.",
        "Incident record for any unsafe-use event reported.",
        "Confirmation no improvised off-label device use occurred.",
    ],
    "MOM.11.c": [
        "Clean, safe, secure storage record following manufacturer recommendation.",
        "Sterile-store physical-separation record from dirty utility.",
        "Confirmation food and medications were not mixed into general consumable racks.",
    ],
    "MOM.11.d": [
        "Documented inventory-control method — stock levels, FEFO, indent cycle.",
        "Monthly stores-round expiry/damaged-stock removal record.",
        "Stock-movement traceability record from receipt to issue for a sampled item.",
    ],
    "MOM.11.e": [
        "Pre-issue condition-verification record — package integrity, sterility indicator, expiry, cold-chain logger where needed.",
        "Quarantine record for any failed item.",
        "User-department return-with-note record for a failed pack.",
    ],
}


def oe_mapping(n: int, oes: list[dict], has_stop: bool) -> list[dict]:
    mapping = []
    prepared = PREPARED_BY[n]
    for i, oe in enumerate(oes, start=1):
        short = clean_text(oe["text"] or "")
        steps = f"Section 3; 5.{i}"
        if has_stop and n in STOP_WORK_PROPOSALS:
            steps += "; Section 6 Stop-work"
        records = MOM_RECORDS.get(oe["oe_code"])
        if not records:
            raise KeyError(f"Missing hand-authored evidence records for {oe['oe_code']}")
        mapping.append(
            {
                "oe_code": oe["oe_code"],
                "requirement": short or oe["oe_code"],
                "steps": steps,
                "responsible": prepared,
                "records": records,
            }
        )
    return mapping


def build_one(n: int, inv: dict, bodies: dict[str, str], interps: dict[str, str]) -> tuple:
    data = inv[str(n)]
    oes = data["oes"]
    title = POLICY_TITLES[n]
    std_title = data["title"]
    has_stop = n in STOP_WORK_PROPOSALS
    sw = stop_work_text(n) if has_stop else ""
    stars = "".join(o["letter"] for o in oes if o.get("star")) or "none"
    cores = "".join(o["letter"] for o in oes if o["level"] == "CORE") or "none"
    ach = "".join(o["letter"] for o in oes if o["level"] == "Achievement") or "none"
    exc = "".join(o["letter"] for o in oes if o["level"] == "Excellence") or "none"

    statute = STATUTE_BY_STD.get(n)
    if statute:
        disclaimer, statute_clause = make_hco_disclaimer_statute(statute)
        accreditation_only = False
    else:
        disclaimer, statute_clause = make_hco_disclaimer_accreditation_only()
        accreditation_only = True

    doc_no = D(f"HCO/MOM/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    own_topic = POLICY_TITLES[n].lower()
    related_chapters = ["AAC", "COP", "PRE", "IPC", "HRM"]

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard MOM.{n}: {std_title}

{hco_oe_count_clause(len(oes))}

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

{hco_related_duties_clause(own_topic, related_chapters)} Other MOM standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to staff who prescribe, dispense, administer, store, monitor or oversee medications (or, for MOM.10–11, implants / medical devices / medical supplies) at {HOSPITAL}, including the {prepared}, pharmacy, nursing, treating doctors and the Quality Coordinator.

{hco_oe_count_clause(len(oes))}

{hco_related_duties_clause(own_topic, related_chapters)}"""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "medication management is safe"
    policy_statement = f"""{HOSPITAL} implements MOM.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work triggers fire (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that MOM.{n} is resourced and followed.
- Designates the Medication Safety Officer (chapter intent) where that role is required for this standard.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Medication Safety Officer
- Coordinates medication-safety processes that cut across MOM standards; brings incidents and audits to the Drug and Therapeutics Committee.

Pharmacy / nursing / treating doctors (as applicable)
- Deliver the process as written; escalate stop-work triggers without delay.

Quality Coordinator
- Audits this policy {D('quarterly')}; holds training acknowledgements."""

    monitoring_bullets = ["Records for a sample of this standard's objective elements, checked against the What-we-do steps."]
    if stars != "none":
        monitoring_bullets.append("Documentary evidence is on file for each asterisked objective element in the sample.")
    if cores != "none":
        monitoring_bullets.append("CORE objective elements show no critical gaps in the sample.")
    monitoring_bullets.append("Stop-work events (if any) are logged with outcome.")
    monitoring_bullet_text = "\n".join(f"- {b}" for b in monitoring_bullets)

    monitoring = f"""The Quality Coordinator audits this policy {D('quarterly')}. The audit reviews:

{monitoring_bullet_text}

Root-cause analysis is required when a gap found in this audit remains open beyond {D('90 days')}.

This policy is reviewed {D('annually')}, and sooner after a related adverse event or recall."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Management of Medication, standard MOM.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — MOM.{n} interpretations (source PDF md5 {GUIDEBOOK_MD5}).
- Internal documents of {HOSPITAL}: Medication Management Manual, formulary, high-risk and emergency-medication lists, registers and incident forms named for MOM.{n}."""

    abbreviations = f"""ADR — adverse drug reaction
CAPA — Corrective and Preventive Action
CORE — Core objective element (NABH)
DTC — Drug and Therapeutics Committee (or the organisation's equivalent multi-disciplinary pharmacy committee)
FEFO — first expiry, first out
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
LASA — look-alike, sound-alike
MOM — Management of Medication (NABH Hospitals chapter)
MSO — Medication Safety Officer
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — Objective Element"""

    ufg = f"""HCO MOM.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (matrix agrees on levels). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — approved: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (MOM.8 confirmed: no stop-work)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/MOM/POL/{n:02d}.
Official chapter is 11 standards / 68 OEs (confirmed). Guidebook interpretations from scanned PDF md5 {GUIDEBOOK_MD5}. MOM.9 statute P2 approved.
Do not touch AAC or COP."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "Medication Safety Officer",
            "Pharmacy In-Charge",
            "Nursing Superintendent",
            "Quality Coordinator",
            f"department clinical staff covered by MOM.{n}",
        ]
    )

    draft = {
        "standard_code": f"MOM.{n}",
        "chapter": CHAPTER,
        "oe_codes": oe_codes,
        "policy_title": title,
        "purpose": purpose,
        "scope": scope,
        "policy_statement": policy_statement,
        "procedure_steps": steps,
        "responsibility": responsibility,
        "references_text": references,
        "distribution": distribution,
        "abbreviations": abbreviations,
        "disclaimer": disclaimer,
        "oe_mapping": oe_mapping(n, oes, has_stop),
        "universal_facts_checklist": ufg,
        "version": VERSION,
        "revision_history": [
            {
                "version": "2.0",
                "date": "21-08-2026",
                "description": f"HCO Full 6th Edition MOM.{n} v2 draft: portal PDF OE data + Guidebook interpretations.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_mom_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — MOM.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.MOM.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_mom{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO MOM.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_mom_v2.py
Explicit draft_label via hco_mom_v2_common.hco_document_control.
Does NOT overwrite SHCO MOM, HCO AAC or HCO COP files.
"""
from __future__ import annotations

import sys
from generate_hco_mom_v2 import emit_standard

if __name__ == "__main__":
    sys.exit(emit_standard({n}))
''',
        encoding="utf-8",
    )


def emit_standard(n: int) -> int:
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    bodies = method_bodies(D=D, HOSPITAL=HOSPITAL, BLANK=BLANK)
    interps = load_interpretations()
    draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, bodies, interps)
    emit_pre_v2(
        draft,
        f"hco_mom{n}_v2_draft.json",
        f"HCO.MOM.{n}_v2_preview.md",
        oe_codes=oe_codes,
        statute_clause=statute_clause,
        accreditation_only=accreditation_only,
        edition_label=HCO_EDITION_LABEL,
        drafts_dir=HCO_DRAFTS,
        preview_dir=HCO_PREVIEW,
    )
    return 0


def main() -> int:
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    total = sum(inv[str(n)]["count"] for n in range(1, 12))
    assert total == 68, total
    bodies = method_bodies(D=D, HOSPITAL=HOSPITAL, BLANK=BLANK)
    interps = load_interpretations()
    expected = [oe["oe_code"] for n in range(1, 12) for oe in inv[str(n)]["oes"]]
    missing = [c for c in expected if c not in bodies]
    extra = [c for c in bodies if c not in expected]
    if missing or extra:
        raise SystemExit(f"method body mismatch missing={missing} extra={extra}")
    missing_i = [c for c in expected if not (interps.get(c) or "").strip()]
    if missing_i:
        raise SystemExit(f"missing guidebook interpretations: {missing_i}")
    for n in range(1, 12):
        write_builder(n)
        draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, bodies, interps)
        assert "not an approved master" not in draft["resources_required"]
        assert "not an approved master" not in json.dumps(draft)
        assert DRAFT_LABEL in draft["resources_required"]
        joined = "\n".join(draft["procedure_steps"])
        assert joined.count("Method note (from guidebook interpretation):") == len(oe_codes)
        dist = draft["distribution"]
        names = [x.strip() for x in re.split(r"[,;\n]", dist) if x.strip()]
        # prepared_by role must appear once in document control
        assert "Prepared by (designation):" in draft["resources_required"]
        emit_pre_v2(
            draft,
            f"hco_mom{n}_v2_draft.json",
            f"HCO.MOM.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"MOM.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
