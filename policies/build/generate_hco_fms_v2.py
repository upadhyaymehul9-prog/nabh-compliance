# -*- coding: utf-8 -*-
"""Generate HCO Full FMS.1–FMS.7 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_fms_v2.py

Official portal PDF has 7 FMS standards / 43 OEs. All 7 are drafted.
Does not touch AAC, COP, MOM, PRE, IPC, PSQ, ROM, or SHCO. Always sets explicit HCO
draft_label via hco_document_control (no "not an approved master" leftover).
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
    hco_related_duties_clause,
    truncate_word_safe,
)
from hco_fms_v2_common import (  # noqa: E402
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
from hco_fms_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_fms_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_fms_interpretations.json"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 where Guidebook names a statute. Proposed default: FMS.5 and FMS.6.
STATUTE_BY_STD: dict[int, str | None] = {
    5: (
        "the Medical Devices Rules as cited in NABH FMS.5 (Gazette of India GSR 78(E) "
        "2023) including adverse-event monitoring, hazard notices and recalls"
    ),
    6: (
        "statutory provisions for medical gases as named in NABH FMS.6, including the "
        "Explosives Act, Gas Cylinder Rules and Static and Mobile Pressure Vessels "
        "(Unfired) Rules where they apply to this hospital's gases"
    ),
}

PREPARED_BY: dict[int, str] = {
    1: "Engineering In-Charge",
    2: "Engineering In-Charge",
    3: "Engineering In-Charge",
    4: "Engineering In-Charge",
    5: "Engineering In-Charge",
    6: "Engineering In-Charge",
    7: "Engineering In-Charge",
}

POLICY_TITLES: dict[int, str] = {
    1: "Safe and Secure Environment",
    2: "Planned Facilities and Environment-Friendly Measures",
    3: "Safety of Patients, Families, Staff and Visitors",
    4: "Facility, Engineering Support and Utility Systems",
    5: "Medical Equipment Management",
    6: "Medical Gases, Vacuum and Compressed Air",
    7: "Fire and Non-Fire Emergencies",
}


# ── Per-standard hand-authored content ──────────────────────────────────────
# Non-negotiable rules: real prohibitions derived from OE + Guidebook modals.
# Every entry is the complete numbered-list body for Section 4 of that standard.
FMS_NON_NEGOTIABLES: dict[int, str] = {
    1: """\
1. Do not run a patient-care area that lacks required patient-safety devices (grab bars, bed rails, call bells, alarms, warning signs and fire-safety devices as applicable to that area) or for which no periodic inspection record exists.
2. Do not operate without providing at minimum the accessibility facilities for differently-abled persons that applicable regulatory requirements mandate — a wheelchair-accessible entrance and an adapted toilet at minimum.
3. Do not let a calendar month pass without a completed, checklist-based facility-inspection round; a round without a completed checklist is not a round for this purpose.
4. Do not leave a finding from a facility inspection round without a documented corrective and preventive action and a safety-committee review within the same calendar month.
5. Do not start construction, renovation or expansion of the existing hospital without a completed risk assessment covering noise, vibration and infection prevention and control in place before work begins.
6. Staff who see a FMS.1 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",

    2: """\
1. Do not operate a clinical service without matching facility space; any service without a corresponding documented space is not available from this hospital for accreditation purposes.
2. Do not let the as-built and updated drawing set become incomplete or without a named custodian; a drawing that does not reflect the current facility is not an as-built drawing.
3. Do not allow signage that cannot be understood by patients, families or the community, or that does not meet applicable statutory posting requirements.
4. Do not leave a care area without potable water or electricity; test potable-water quality biochemically at least once in three months and microbiologically at least once a month, collected at the tap.
5. Do not operate without identified backup electricity and water sources available for every critical area.
6. Do not count an alternate source as available if it has not been tested at the defined frequency with documented results.
7. Do not bypass the stop-work authority in section 6 when the trigger conditions are met.
8. Staff who see a FMS.2 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",

    3: """\
1. Do not operate critical areas (operating theatre, ICUs including NICU, labour room, emergency) without a written security plan defining access for staff, patients and visitors; designated extra-security areas must have documented controls such as CCTV.
2. Do not start or continue using a hazardous material that has not been identified and documented, or for which a sorting, storage, handling, transport and disposal procedure does not exist.
3. Do not use a hazardous material in an area where the summarised Material Safety Data Sheet is not accessible to floor staff and the hazardous-materials spill kit is not reachable.
4. Do not condemn or dispose of material not in use without following the written identification-and-disposal procedure.
5. Do not allow a calendar year to pass without a completed electrical safety audit of the facility with documented actions.
6. Do not bypass the stop-work authority in section 6 when the trigger conditions are met.
7. Staff who see a FMS.3 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",

    4: """\
1. Do not run utility or engineering equipment that is not in the current equipment inventory with a unique identifier.
2. Do not run critical utility equipment (diesel generator, lifts, uninterruptible power supply, fire-related equipment, dialysis reverse-osmosis plant, water pumps) without an implemented, documented operational and maintenance plan.
3. Do not let utility equipment become overdue for calibration without a corrective action in place.
4. Do not operate a shift without a named competent person available for each plant system that is running.
5. Do not leave the maintenance escalation matrix unavailable at the nursing station and departments during any shift.
6. Do not condemn or dispose of utility or engineering equipment without following the written equipment-replacement and disposal guidance.
7. Do not bypass the stop-work authority in section 6 when the trigger conditions are met.
8. Staff who see a FMS.4 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",

    5: """\
1. Do not put medical equipment into clinical use without a unique identifier and an entry in the medical-equipment inventory.
2. Do not use medical equipment that does not have an implemented, documented operational and maintenance plan.
3. Do not use medical equipment that measures patient parameters past its scheduled calibration due date; remove it from clinical use until calibration is complete.
4. Do not allow an operator to use a medical device they have not been trained for; do not allow maintenance by personnel who are not a biomedical or instrumentation engineer or technologist with relevant training and experience.
5. Do not continue clinical use of any medical device subject to an open manufacturer or regulatory recall or hazard notice.
6. Do not condemn or dispose of medical equipment without following the written replacement-and-disposal guidance.
7. Do not bypass the stop-work authority in section 6 when the trigger conditions are met.
8. Staff who see a FMS.5 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",

    6: """\
1. Do not procure, store, distribute or use any medical gas without written guidance covering colour coding, signage, handling and replenishment in place for that gas.
2. Do not use a medical-gas outlet or manifold that lacks the required colour coding, alarm, valve box, pin-indexed outlet or automatic changeover to the alternate source.
3. Do not silence a plant-room alarm for a medical-gas system without a documented reason and corrective action.
4. Do not operate piped medical gas, compressed air or vacuum without an implemented operational, inspection, testing and maintenance plan following the manufacturer.
5. Do not operate without a required alternate source (stand-by compressor, stand-by vacuum pump, stand-by manifold or bulk cylinders) for each gas, compressed air and vacuum line in use.
6. Do not count an alternate source as available if it has not been tested at the defined frequency with documented results.
7. Do not bypass the stop-work authority in section 6 when the trigger conditions are met.
8. Staff who see a FMS.6 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",

    7: """\
1. Do not occupy a patient-care floor without an implemented fire plan covering detection, abatement, containment and evacuation — with qualified personnel, current NABH fire-safety measures, smoke-control provisions and emergency illumination in place.
2. Do not occupy a patient-care floor without a documented and displayed exit plan on that floor, including near lifts and inside enclosed rooms and laboratories; exit doors must remain open or have push bars.
3. Do not operate without written plans for the non-fire emergencies this hospital has identified (at minimum earthquake, flood, structural collapse, utility failure and toxic leak), developed with reference to NDMA/State/District guidelines.
4. Do not let six months pass without at least one mock drill testing the full fire or non-fire emergency plan; each drill uses simulated, not real, patients and is followed by a debrief and corrective action.
5. Do not operate fire-related equipment and infrastructure without an implemented maintenance plan covering inspection, testing, preventive and breakdown maintenance.
6. Do not bypass the stop-work authority in section 6 when the trigger conditions are met.
7. Staff who see a FMS.7 rule broken report it the same shift to the Engineering In-Charge or the Medical Superintendent.""",
}

# Per-standard Purpose paragraphs (replaces the restated-OE opener).
FMS_PURPOSE: dict[int, str] = {
    1: (
        "This policy defines how {hospital} installs and inspects patient-safety devices and "
        "infrastructure, provides accessible facilities for differently-abled persons, conducts "
        "monthly safety-inspection rounds, documents findings and acts on them, and carries out "
        "risk assessments before any construction, renovation or expansion of the facility."
    ),
    2: (
        "This policy defines how {hospital} ensures facilities and space match services, keeps "
        "as-built drawings current, maintains comprehensible signage, provides potable water and "
        "electricity around the clock, and provides and regularly tests backup sources for both."
    ),
    3: (
        "This policy defines how {hospital} controls access to high-security areas, identifies "
        "and safely manages hazardous materials, implements spill-response plans, conducts "
        "electrical safety audits, and manages material not in use."
    ),
    4: (
        "This policy defines how {hospital} plans, inventories, operates and maintains utility "
        "and engineering equipment, keeps competent maintenance personnel available round the "
        "clock, and guides equipment replacement and disposal."
    ),
    5: (
        "This policy defines how {hospital} plans medical-equipment procurement, inventories "
        "and identifies every device, implements operational and maintenance plans, keeps "
        "calibration current, ensures only qualified personnel operate and maintain equipment, "
        "monitors adverse events and recalls, and guides replacement and disposal."
    ),
    6: (
        "This policy defines how {hospital} governs the procurement, handling, storage, "
        "distribution, use and replenishment of medical gases, compressed air and vacuum; "
        "maintains safety measures at every level; keeps operational and maintenance plans "
        "current; and provides and tests backup sources."
    ),
    7: (
        "This policy defines how {hospital} plans and maintains provisions for fire and "
        "non-fire emergencies — including fire detection, abatement, containment and "
        "evacuation; non-fire emergency identification and management; displayed exit plans; "
        "regular mock drills; and maintenance of fire-related equipment and infrastructure."
    ),
}

# Per-standard Policy standards paragraphs (replaces the restated-OE sentence).
FMS_POLICY_STATEMENT: dict[int, str] = {
    1: (
        "Patient-safety devices and infrastructure are installed and periodically inspected "
        "across {hospital}. Accessibility facilities meet regulatory minimums for differently-abled "
        "persons. Monthly facility-inspection rounds identify and monitor safety, security-risk "
        "and restricted areas. Every finding is documented, acted on and reviewed by the safety "
        "committee. No construction, renovation or expansion begins without a completed risk "
        "assessment covering noise, vibration and infection prevention and control."
    ),
    2: (
        "Facilities and space at {hospital} match the services offered. As-built and updated "
        "drawings are maintained by a named custodian. Internal and external signage is in a "
        "form patients, families and the community can understand, and meets statutory posting "
        "requirements. Potable water and electricity are available round the clock with tested "
        "backup sources for any failure."
    ),
    3: (
        "{hospital} defines extra-security areas and controls access for staff, patients and "
        "visitors. Hazardous materials are identified, documented and handled safely at every "
        "stage. Spill plans are implemented with floor-accessible summaries and kits. Electrical "
        "safety audits are conducted annually. Material not in use is systematically identified "
        "and disposed of."
    ),
    4: (
        "{hospital} plans utility and engineering equipment against services and the strategic "
        "plan. All equipment is inventoried with unique identifiers. Implemented operational and "
        "maintenance plans cover every system. Calibration is kept current. Competent personnel "
        "are available for every shift. Maintenance is contactable round the clock. Downtime on "
        "critical equipment is tracked from complaint to completion. Equipment replacement and "
        "disposal follows written guidance."
    ),
    5: (
        "{hospital} plans medical equipment against services and the strategic plan. Every "
        "device is inventoried, classified by risk and given a unique identifier. Implemented "
        "operational and maintenance plans cover operator training, daily checks and breakdown "
        "response. Calibration is current before commissioning and after every repair. Operators "
        "and maintainers are qualified. Adverse events and recalls are monitored and acted on "
        "without delay. Disposal follows written guidance."
    ),
    6: (
        "Written guidance governs every stage of medical-gas management at {hospital}. Gases "
        "are handled, stored and distributed with standardised colour coding, alarms, valve "
        "boxes, pin-indexed outlets and automatic changeover. An operational, inspection, "
        "testing and maintenance plan follows the manufacturer. Backup sources are in place "
        "and tested regularly."
    ),
    7: (
        "{hospital} has implemented fire plans covering detection, abatement, containment and "
        "evacuation, with qualified personnel and current NABH fire-safety measures. Non-fire "
        "emergencies are identified and planned for, with NDMA/State/District guidelines as a "
        "reference. Exit plans are documented and displayed on every floor. Mock drills are "
        "held at least twice a year. Fire-related equipment and infrastructure are maintained "
        "under an active plan."
    ),
}


def clean_text(s: str) -> str:
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = s.replace("\uf001", "fi").replace("\uf002", "fl")
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
        steps.append(f"{title}\n\n{body}")
    return steps


def non_negotiables(n: int, oes: list[dict]) -> str:
    text = FMS_NON_NEGOTIABLES.get(n)
    if not text:
        raise KeyError(f"Missing hand-authored non-negotiables for FMS.{n}")
    return text


# Fix #5 — hand-authored per-OE evidence records, matching the quality bar
# AAC.1 / SHCO HIC.1 / HCO ROM already demonstrate: concrete, subject-specific
# documents a hospital would actually hold, not a generic template restating
# the OE code.
FMS_RECORDS: dict[str, list[str]] = {
    "FMS.1.a": [
        "Current inventory of patient-safety devices and infrastructure (grab bars, bed rails, call bells, fire-safety devices) by area.",
        "Inspection log showing the last-inspection date for each device or area.",
        "Escalation record for any missing device found in an in-use care area.",
    ],
    "FMS.1.b": [
        "Facility list showing the wheelchair-accessible entrance and toilet location(s).",
        "Regulatory-requirement reference for the accessibility provision made.",
        "Documented alternative arrangement for any area with step-only access.",
    ],
    "FMS.1.c": [
        "Monthly facility-inspection-round checklist, completed and dated.",
        "Round calendar showing no missed month.",
        "List of identified safety, security-risk or restricted areas being monitored.",
    ],
    "FMS.1.d": [
        "Documented inspection reports of facility rounds.",
        "Corrective and preventive action record for each finding.",
        "Safety-committee review record of the reports.",
    ],
    "FMS.1.e": [
        "Dated risk-assessment record covering noise, vibration and infection prevention, completed before work started.",
        "Engineering In-Charge sign-off before construction, renovation or expansion began.",
        "Cross-reference to the IPC.4 construction-infection-control measures applied alongside.",
    ],
    "FMS.2.a": [
        "Current space-versus-services map for each department.",
        "National or international guidance reference used (for example AERB guidance for a radiation area).",
        "Escalation record for any service listed without matching space.",
    ],
    "FMS.2.b": [
        "Current as-built and updated drawing set: site layout, floor plans, floor-wise evacuation plans, and separate civil, electrical, ELV, plumbing, HVAC, medical-gas and IT drawings.",
        "Named custodian record for the drawing set.",
        "Date of last update against a facility change.",
    ],
    "FMS.2.c": [
        "Signage inventory or walk log by area, noting language and/or pictorial form and bilingual coverage.",
        "Statutory posting-requirement reference applicable to this site.",
        "Quarterly signage-walk record.",
    ],
    "FMS.2.d": [
        "Potable-water test results: biochemical at least quarterly and microbiological at least monthly, against IS 10500.",
        "Dialysis reverse-osmosis inlet-water endotoxin test record, where dialysis is in scope.",
        "Continuity log confirming no unplanned water or power outage in a care area without the FMS.7 continuity plan activating.",
    ],
    "FMS.2.e": [
        "Backup-source inventory: diesel generator, solar, uninterruptible power supply, bore/tanker/extra tanks as named.",
        "Electric-load calculation matching demand.",
        "Continuity-action record naming each critical area's backup path.",
    ],
    "FMS.2.f": [
        "Diesel-generator test log at the defined frequency (default monthly).",
        "Water-acceptance test record for any occasion an emergency water source was used.",
        "Corrective-action record for any failed alternate-source test.",
    ],
    "FMS.3.a": [
        "Written security operational plan naming extra-security areas (operating theatre, ICU/NICU, labour room, emergency) and access rules for staff, patients and visitors.",
        "Vulnerable-spot control record — closed-circuit television coverage or equivalent for dark areas and long corridors.",
        "Review or update record of the security plan.",
    ],
    "FMS.3.b": [
        "Structural-safety design reference actually applied (for example Indian Seismic Code IS 1893 Part 1) for the specific building project.",
        "Engineering sign-off record for that construction, re-planning or retrofit project.",
        "Evidence of what was applied to real building work, not a policy statement alone.",
    ],
    "FMS.3.c": [
        "Completed electrical safety audit report, at least annually.",
        "Action-taken record against audit findings.",
        "Reference to the National Electrical Code or thermal-imaging method used.",
    ],
    "FMS.3.d": [
        "Written procedure for identifying and disposing of material not in use.",
        "Condemnation register listing items, dates and disposal method.",
        "Engineering In-Charge sign-off on the register.",
    ],
    "FMS.3.e": [
        "Current hazardous-materials inventory (for example chemicals, blood/cultures, mercury, isotopes, medical gases, LPG, steam, ethylene oxide).",
        "Material Safety Data Sheet on file for each identified material.",
        "Handling, storage, transport and disposal record for a sample of materials.",
    ],
    "FMS.3.f": [
        "Summarised Material Safety Data Sheet accessible on the floor where the material is stored.",
        "Hazardous-materials spill-kit inventory and location log.",
        "Training record for staff handling that material.",
    ],
    "FMS.4.a": [
        "Written utility and engineering equipment plan matched to services and the strategic plan, including future needs (for example diesel generator, chiller).",
        "Periodic review record of the plan.",
        "Record showing collaborative selection (end-user, management, finance, engineering) for equipment decisions.",
    ],
    "FMS.4.b": [
        "Equipment inventory with a unique identifier per item.",
        "Quality-conformance, factory test or installation certificate on file where applicable.",
        "Log-completeness check confirming no item without an identity.",
    ],
    "FMS.4.c": [
        "Documented operational and maintenance (preventive and breakdown) plan for utility and engineering equipment.",
        "Preventive-maintenance schedule and completion log for the critical-equipment list.",
        "Breakdown-response record showing the plan was actually followed.",
    ],
    "FMS.4.d": [
        "Calibration schedule for utility equipment (for example steam-steriliser pressure gauges, medication-refrigerator temperature gauges).",
        "Calibration certificate with traceability to a prescribed standard.",
        "In-house or outsourced calibration record.",
    ],
    "FMS.4.e": [
        "Competency or training record for staff operating utility equipment.",
        "Roster showing a named competent person for each shift.",
        "Escalation record for any shift with no competent person named.",
    ],
    "FMS.4.f": [
        "Escalation matrix displayed at the nursing station and departments.",
        "On-call roster for maintenance staff, round the clock.",
        "Night-call response-time log.",
    ],
    "FMS.4.g": [
        "Complaint register logging receipt, job allotment and user-ratified completion for critical equipment (diesel generator, lifts, UPS, fire-related, dialysis RO, water pumps).",
        "Downtime-duration record from complaint time to ratified completion.",
        "Trend report reviewed against the critical-equipment list.",
    ],
    "FMS.4.h": [
        "Written equipment-replacement and disposal guidance.",
        "Condemnation record for utility and engineering equipment.",
        "Systematic disposal log.",
    ],
    "FMS.5.a": [
        "Written medical-equipment plan matched to services and the strategic plan, referencing the Indian Public Health Standards minimum set.",
        "Collaborative-selection record (end-user, management, finance, engineering, biomedical).",
        "Periodic review record of the plan.",
    ],
    "FMS.5.b": [
        "Medical-equipment inventory classified by device risk, with a unique identifier including rental and demonstration items.",
        "Factory test or conformance certificate on file.",
        "In-use device check confirming no device without an identity.",
    ],
    "FMS.5.c": [
        "Documented operational and maintenance (preventive and breakdown) plan for medical equipment.",
        "Operator-training record and daily operating-check log.",
        "Breakdown-response record, including nights and weekends.",
    ],
    "FMS.5.d": [
        "Calibration schedule (weekly, monthly or annual as the manufacturer defines) with traceability.",
        "Pre-commissioning and post-repair conformance-check record.",
        "Calibration-due tracking log confirming no overdue device in clinical use.",
    ],
    "FMS.5.e": [
        "Operator-training record per device type (for example blood-gas analyser, electrocardiograph, syringe pump).",
        "Biomedical or instrumentation engineer/technologist qualification record for maintenance staff.",
        "Training-currency check for operators and maintainers.",
    ],
    "FMS.5.f": [
        "Written medical-equipment replacement and disposal guidance.",
        "Condemnation record, systematically applied.",
        "Disposal log.",
    ],
    "FMS.5.g": [
        "Adverse-event and hazard-notice/recall log for medical equipment and devices.",
        "Record showing a recalled device was withdrawn from clinical use until the issue closed.",
        "Materiovigilance Programme of India participation record, where applicable.",
    ],
    "FMS.5.h": [
        "Complaint register for critical medical equipment (ventilators, X-ray, MRI, cath lab, CT, anaesthesia machines, monitors, laboratory, ultrasound).",
        "Downtime-duration record from reporting to corrective action.",
        "Alternative-equipment-use record where no backup device exists.",
    ],
    "FMS.6.a": [
        "Written medical-gas procurement, handling, storage, distribution, usage and replenishment guidance, including colour-coding and signage.",
        "Reference used (for example HTM 02-01 or the NFPA medical-gas handbook).",
        "Statutory-provision record (Explosives Act, Gas Cylinder Rules, Static and Mobile Pressure Vessels Rules) where those apply to this hospital's gases.",
    ],
    "FMS.6.b": [
        "Colour-coded cylinder and pipeline inventory with alarm and valve-box log.",
        "Twenty-four-hour plant-alarm monitoring record.",
        "Pin-indexed outlet and automatic-changeover verification record.",
    ],
    "FMS.6.c": [
        "Documented operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum.",
        "Compressed-air purity test record, at least annually, at operating-theatre and intensive-care terminal outlets.",
        "Manufacturer-following maintenance log.",
    ],
    "FMS.6.d": [
        "Stand-by compressor/vacuum-pump and stand-by manifold or bulk-cylinder inventory.",
        "Automatic-changeover test record.",
        "Alternate-source readiness confirmation log.",
    ],
    "FMS.6.e": [
        "Test log for alternate medical-gas sources at the defined interval (default monthly).",
        "Manufacturer or written-plan interval reference used.",
        "Corrective-action record for any failed test.",
    ],
    "FMS.7.a": [
        "Written fire-safety plan covering detection, abatement, containment and evacuation, naming qualified personnel and current NABH minimum fire-safety measures.",
        "Mock-drill schedule and drill record, including table-top exercises.",
        "Displayed evacuation plan and emergency-illumination check record.",
    ],
    "FMS.7.b": [
        "Written non-fire-emergency plan (for example earthquake, flood, toxic leak, structural collapse, utility failure, boiler burst, violence, stray animals).",
        "NDMA, State or District guideline reference used.",
        "Liaison record with civil, police and fire authorities.",
    ],
    "FMS.7.c": [
        "Exit plan displayed on each floor, near lifts and inside enclosed rooms and laboratories.",
        "Exit-door check record (open or push-bar) and fire-signage reference (fire service or National Building Code).",
        "Refuge-area signage and maintenance record, where applicable.",
    ],
    "FMS.7.d": [
        "Mock-drill record showing at least two drills a year covering fire and the named non-fire events.",
        "Debrief and corrective-action record for variations found.",
        "Confirmation that simulated, not real, patients were used.",
    ],
    "FMS.7.e": [
        "Written maintenance plan for fire-related equipment and infrastructure.",
        "Inspection, testing, preventive and breakdown maintenance log following manufacturer and statutory recommendations.",
        "Last-service evidence on file.",
    ],
}


# Maps each standard to the specific OE codes that actually trigger stop-work.
# Only these OEs show "Section 6 Stop-work" in the traceability table steps column.
# Derived from the method body sentences that say "is a stop-work trigger (section 6)".
STOP_WORK_OES: dict[int, frozenset[str]] = {
    2: frozenset({"FMS.2.d"}),
    3: frozenset({"FMS.3.e"}),
    4: frozenset({"FMS.4.c"}),
    5: frozenset({"FMS.5.c", "FMS.5.d", "FMS.5.g"}),
    6: frozenset({"FMS.6.b", "FMS.6.d"}),
    7: frozenset({"FMS.7.a", "FMS.7.c"}),
}


def oe_mapping(n: int, oes: list[dict], has_stop: bool) -> list[dict]:
    mapping = []
    prepared = PREPARED_BY[n]
    sw_oes = STOP_WORK_OES.get(n, frozenset())
    for i, oe in enumerate(oes, start=1):
        short = clean_text(oe["text"] or "")
        steps = f"Section 3; 5.{i}"
        if oe["oe_code"] in sw_oes:
            steps += "; Section 6 Stop-work"
        records = FMS_RECORDS.get(oe["oe_code"])
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

    doc_no = D(f"HCO/FMS/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    eng = D("Engineering In-Charge")
    gov_scope = (
        "engineering, biomedical, nursing and departmental leaders, and staff who run "
        "facilities, utilities, medical gases, fire and non-fire emergencies"
    )
    own_topic = POLICY_TITLES[n].lower()
    related_chapters = ["AAC", "COP", "MOM", "PRE", "IPC", "PSQ", "ROM"]

    purpose_body = FMS_PURPOSE[n].format(hospital=HOSPITAL)
    purpose = f"""{purpose_body}

{hco_related_duties_clause(own_topic, related_chapters)} Other FMS standards have their own policies too.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to {gov_scope} at {HOSPITAL}, including the {prepared}, the {D('Medical Superintendent')}, departmental leaders and the Quality Coordinator.

{hco_related_duties_clause(own_topic, related_chapters)} Other FMS standards have their own policies too."""

    ps_body = FMS_POLICY_STATEMENT[n].format(hospital=HOSPITAL)
    policy_statement = f"""{ps_body}

Staff follow written guidance and keep the records listed in the traceability table."""

    responsibility = f"""Medical Superintendent
- Accountable that FMS.{n} is resourced and followed.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Quality Coordinator
- Audits this policy {D('quarterly')}; holds training acknowledgements.

departmental leaders
- Run the department-level duties this standard names."""

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

This policy is reviewed {D('annually')}, and sooner after a related facility change, utility failure, equipment recall or fire-plan change."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read the Policy on {title} of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Facility Management and Safety, standard FMS.{n}.
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — FMS.{n} interpretations.
- Internal documents of {HOSPITAL}: facility-inspection records, as-built drawings, utility and medical-equipment logs, medical-gas records, fire and non-fire plans named for FMS.{n}."""

    abbreviations = f"""AHU — Air Handling Unit
CAPA — Corrective and Preventive Action
CORE — Core objective element (NABH)
DG — Diesel Generator
ELV — Extra Low Voltage
FMS — Facility Management and Safety (NABH Hospitals 6th Edition chapter)
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
HVAC — Heating, Ventilation and Air Conditioning
MSDS — Material Safety Data Sheet
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — Objective Element
PPE — Personal Protective Equipment
RO — Reverse Osmosis
STP — Sewage Treatment Plant"""

    ufg = f"""HCO FMS.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (matrix agrees on levels). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — proposed: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (proposed default: no stop-work on this standard)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/FMS/POL/{n:02d}.
Official chapter is 7 standards / 43 OEs (confirmed against portal summary). Guidebook interpretations from scanned PDF md5 {GUIDEBOOK_MD5}. Statute P2 proposed on FMS.5 (Medical Devices Rules as cited) and FMS.6 (Explosives Act / Gas Cylinder Rules / SMPV).
Do not touch AAC, COP, MOM, PRE, IPC, PSQ or ROM."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "Engineering In-Charge",
            "Quality Coordinator",
            "departmental leaders",
            f"staff covered by FMS.{n}",
        ]
    )

    draft = {
        "standard_code": f"FMS.{n}",
        "chapter": CHAPTER,
        "oe_codes": oe_codes,
        "policy_title": f"Policy on {title}",
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
                "description": f"HCO Full 6th Edition FMS.{n} v2 draft: portal PDF OE data + Guidebook interpretations.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_fms_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — {title.lower()}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.FMS.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_fms{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO FMS.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_fms_v2.py
Explicit draft_label via hco_fms_v2_common.hco_document_control.
Does NOT overwrite SHCO, HCO AAC, HCO COP, HCO MOM, HCO PRE, HCO IPC, HCO PSQ or HCO ROM files.
"""
from __future__ import annotations

import sys
from generate_hco_fms_v2 import emit_standard

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
        f"hco_fms{n}_v2_draft.json",
        f"HCO.FMS.{n}_v2_preview.md",
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
    total = sum(inv[str(n)]["count"] for n in range(1, 8))
    assert total == 43, total
    bodies = method_bodies(D=D, HOSPITAL=HOSPITAL, BLANK=BLANK)
    interps = load_interpretations()
    expected = [oe["oe_code"] for n in range(1, 8) for oe in inv[str(n)]["oes"]]
    missing = [c for c in expected if c not in bodies]
    extra = [c for c in bodies if c not in expected]
    if missing or extra:
        raise SystemExit(f"method body mismatch missing={missing} extra={extra}")
    missing_i = [c for c in expected if not (interps.get(c) or "").strip()]
    if missing_i:
        raise SystemExit(f"missing guidebook interpretations: {missing_i}")
    for n in range(1, 8):
        write_builder(n)
        draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, bodies, interps)
        blob = json.dumps(draft)
        assert "not an approved master" not in draft["resources_required"]
        assert "not an approved master" not in blob
        assert DRAFT_LABEL in draft["resources_required"]
        joined = "\n".join(draft["procedure_steps"])
        assert joined.count("Method note (from guidebook interpretation):") == len(oe_codes)
        assert "Prepared by (designation):" in draft["resources_required"]
        dist_parts = [x.strip() for x in re.split(r"[,;\n]", draft["distribution"]) if x.strip()]
        assert len(dist_parts) == len(set(p.casefold() for p in dist_parts)), dist_parts
        emit_pre_v2(
            draft,
            f"hco_fms{n}_v2_draft.json",
            f"HCO.FMS.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"FMS.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
