# -*- coding: utf-8 -*-
"""Generate HCO Full COP.1–COP.20 v2 builders and drafts from official inventory + OCR.

Usage (from policies/build):
  python3 generate_hco_cop_v2.py

Does not touch AAC or SHCO. Always sets explicit HCO draft_label via
hco_cop_v2_common.hco_document_control (no \"not an approved master\" leftover).
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
    BLANK,
    CHAPTER,
    D,
    DRAFT_LABEL,
    HCO_EDITION_LABEL,
    HOSPITAL,
    PROGRAMME,
    STOP_WORK_PROPOSALS,
    VERSION,
    hco_boundaries_clause,
    hco_document_control,
    stop_work_text,
    truncate_word_safe,
)
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_cop_inventory.json"
OCR = ROOT / "policies/source/hco6_cop_ocr.txt"
BUILD = Path(__file__).resolve().parent

# Statute P2 only where COP OEs clearly name legal duties in OE text.
STATUTE_BY_STD: dict[int, str | None] = {
    2: "applicable laws and regulations governing emergency services as named in NABH COP.2",
    3: "statutory requirements for ambulance vehicles and drivers as named in NABH COP.3",
    8: "applicable laws and regulations for transfusion services as named in NABH COP.8",
    15: "legal requirements for organ transplant programmes as named in NABH COP.15",
}

PREPARED_BY: dict[int, str] = {
    1: "Quality Coordinator",
    2: "Emergency In-Charge",
    3: "Ambulance / Transport In-Charge",
    4: "Medical Superintendent",
    5: "CPR Committee Chair",
    6: "Nursing Superintendent",
    7: "Quality Coordinator",
    8: "Transfusion / Blood Bank In-Charge",
    9: "ICU In-Charge",
    10: "Obstetric In-Charge",
    11: "Paediatric In-Charge",
    12: "Anaesthesia / Sedation In-Charge",
    13: "Anaesthesia In-Charge",
    14: "OT In-Charge",
    15: "Transplant Programme In-Charge",
    16: "Quality Coordinator",
    17: "Pain Management Lead",
    18: "Rehabilitation In-Charge",
    19: "Dietetics In-Charge",
    20: "Palliative / End-of-Life Care Lead",
}

POLICY_TITLES: dict[int, str] = {
    1: "Uniform Care Guided by Written Guidance",
    2: "Emergency Services",
    3: "Ambulance Services and Safe Transportation",
    4: "Community Emergencies, Epidemics and Disasters",
    5: "Cardio-Pulmonary Resuscitation Services",
    6: "Nursing Care in Consonance with Clinical Protocols",
    7: "Safe Clinical Procedures",
    8: "Safe Transfusion Services",
    9: "Intensive Care and High Dependency Units",
    10: "Safe Obstetric Care",
    11: "Safe Paediatric Services",
    12: "Procedural Sedation",
    13: "Anaesthesia Services",
    14: "Surgical Services",
    15: "Organ Transplant Programme",
    16: "High-Risk Patients — Identification and Management",
    17: "Pain Management",
    18: "Rehabilitation Services",
    19: "Nutritional Therapy",
    20: "End-of-Life Care",
}


def clean_text(s: str) -> str:
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_ocr_interpretations() -> dict[int, list[str]]:
    """Best-effort list of Interpretation paragraphs per standard, in OE order."""
    if not OCR.exists():
        return {}
    text = OCR.read_text(encoding="utf-8", errors="replace")
    # Split roughly by Standard markers / COP.N headings in OCR
    chunks: dict[int, str] = {}
    # Find page regions after "Standards and Objective Elements"
    parts = re.split(r"(?i)(?:Standard\s*\n|COP\.?\s*(\d+))", text)
    # Simpler: find Interpretation blocks and assign by nearest preceding OE letter line
    by_std: dict[int, list[str]] = {n: [] for n in range(1, 21)}
    current = 1
    for line in text.splitlines():
        m = re.search(r"COP\.?\s*(\d+)", line, re.I)
        if m and re.search(r"Standard|guided|services|care|provided|management|programme", line, re.I):
            try:
                current = int(m.group(1))
            except ValueError:
                pass
        if re.match(r"(?i)^\s*Interpretation:", line):
            by_std.setdefault(current, []).append(clean_text(re.sub(r"(?i)^Interpretation:\s*", "", line)))
    return by_std


def step_title(i: int, oe_text: str) -> str:
    # Short title from first clause
    t = oe_text.split(".")[0].strip()
    t = truncate_word_safe(t, 72)
    return f"5.{i} {t}"


def build_steps(n: int, oes: list[dict], interps: list[str]) -> list[str]:
    steps = []
    for i, oe in enumerate(oes, start=1):
        title = step_title(i, oe["text"] or oe["oe_code"])
        body = clean_text(oe["text"] or "")
        extra = ""
        if oe.get("star") and i - 1 < len(interps) and interps[i - 1]:
            # Tier-1: weave a short interpretation-derived method note
            note = truncate_word_safe(interps[i - 1], 420)
            extra = f"\n\nMethod note (from guidebook interpretation): {note}"
        elif oe.get("star"):
            extra = (
                "\n\nMethod note: Follow the organisation's written guidance for this asterisked "
                "element; keep records that show the guidance was followed for the sampled cases."
            )
        else:
            extra = (
                "\n\nStaff follow the written guidance and record the action in the medical record "
                "or the department register named for this element."
            )
        if oe["level"] == "CORE":
            extra += "\n\nThis is a CORE objective element — non-compliance is not acceptable for accreditation."
        steps.append(f"""{title}

{body}.{extra}""".replace("..", "."))
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
        f"{len(items)+1}. Staff who see a COP.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Medical Superintendent')}."
    )
    return "\n".join(items)


# Fix #5 — hand-authored per-OE evidence records, matching the quality bar
# AAC.1 / SHCO HIC.1 / HCO ROM / HCO FMS / HCO PSQ / HCO IPC / HCO PRE /
# HCO MOM / HCO HRM already demonstrate. COP has no standalone hco_cop_v2_methods.py
# (procedure-step bodies are built from OE text directly in build_steps()), so these
# records are grounded in the OE requirement text and standard clinical/documentation
# practice for that subject, following the same pattern used for AAC.1 and ROM.
COP_RECORDS: dict[str, list[str]] = {
    "COP.1.a": [
        "Written uniform-care guidance or protocol document.",
        "Staff training record on the guidance.",
        "Cross-setting consistency-check record (OPD, IPD, emergency).",
    ],
    "COP.1.b": [
        "Written patient-identification procedure naming the two identifiers used.",
        "Identification-practice observation record for a sampled encounter.",
        "Wristband or ID-card record, where used.",
    ],
    "COP.1.c": [
        "Adopted clinical practice guideline or protocol list.",
        "Reference-source record (professional body, national or international guideline).",
        "Staff-access record to the current guidelines.",
    ],
    "COP.1.d": [
        "Developed care-pathway document for a selected condition.",
        "Consistency-check record across care settings.",
        "Periodic-review record of the pathway.",
    ],
    "COP.1.e": [
        "Multi-disciplinary care-planning record for a sampled complex case.",
        "Best-practice or guideline reference used.",
        "Uniform-delivery record across the organisation.",
    ],
    "COP.1.f": [
        "Written telemedicine guidance covering safety and security.",
        "Telemedicine Practice Guidelines (MoHFW) compliance record.",
        "Consultation-documentation record for a sampled telemedicine encounter.",
    ],
    "COP.2.a": [
        "Emergency-area location and resource-inventory record.",
        "Accessibility-confirmation record.",
        "Resource-adequacy check against service scope.",
    ],
    "COP.2.b": [
        "Written overcrowding-management plan.",
        "Crowd-management measure implementation record.",
        "Overcrowding-incident log and response record.",
    ],
    "COP.2.c": [
        "Written emergency-care guidance covering medico-legal case handling.",
        "Medico-legal case register with statutory-notification record.",
        "Staff training record on the medico-legal case procedure.",
    ],
    "COP.2.d": [
        "Written triage protocol or system document.",
        "Triage-category assignment record for a sampled patient.",
        "Triage-training record for emergency staff.",
    ],
    "COP.2.e": [
        "Re-assessment record for a waiting emergency patient.",
        "Documented trigger or frequency for re-assessment.",
        "Status-change escalation record.",
    ],
    "COP.2.f": [
        "Documented admission, discharge-to-home or transfer record.",
        "Disposition-decision documentation.",
        "Record-completeness check.",
    ],
    "COP.2.g": [
        "Discharge or transfer note issued to the patient, on file.",
        "Content-completeness record — diagnosis, treatment given, follow-up.",
        "Receiving-organisation transfer-note record, where applicable.",
    ],
    "COP.2.h": [
        "Written emergency-department quality assurance programme.",
        "Indicator-monitoring record for the programme.",
        "Improvement-action record from QA findings.",
    ],
    "COP.2.i": [
        "Written system for managing patients found dead on arrival or who die within minutes of arrival.",
        "Documentation record for a sampled such case.",
        "Family-communication and statutory-notification record.",
    ],
    "COP.3.a": [
        "Ambulance-service agreement or ownership record matched to service scope.",
        "Access-arrangement record — owned, contracted, or on-call.",
        "Scope-matching confirmation record.",
    ],
    "COP.3.b": [
        "Ambulance bay or access-route layout record.",
        "Space-adequacy confirmation record.",
        "Unobstructed-access check record.",
    ],
    "COP.3.c": [
        "Ambulance equipment inventory matching purpose.",
        "Vehicle fitness or registration record.",
        "Equipment-adequacy check record.",
    ],
    "COP.3.d": [
        "Training record for ambulance driver and attendant staff.",
        "Competency-verification record.",
        "Currency-of-training record.",
    ],
    "COP.3.e": [
        "Daily ambulance-check log — functioning status, medical equipment, medications, consumables.",
        "Defect or deficiency-reporting record.",
        "Corrective-action record for a failed check.",
    ],
    "COP.3.f": [
        "Ambulance communication-system record — radio, mobile, GPS tracking.",
        "Functionality-check record.",
        "Control-room or hospital contact-log record.",
    ],
    "COP.3.g": [
        "Written protocol for initiating treatment during transit.",
        "Pre-arrival-notification record from ambulance to emergency department.",
        "Sample record of treatment initiated in transit.",
    ],
    "COP.4.a": [
        "Written community emergency, epidemic or disaster risk-identification record.",
        "Local hazard-assessment record.",
        "Periodic-review record of identified risks.",
    ],
    "COP.4.b": [
        "Documented community-emergency management plan.",
        "Roles-and-responsibilities record within the plan.",
        "Activation record for a real event, where applicable.",
    ],
    "COP.4.c": [
        "Emergency-supply and equipment-provision record for community emergencies.",
        "Stock-adequacy check record.",
        "Replenishment record after use.",
    ],
    "COP.4.d": [
        "Mock-drill or test record, at least twice a year.",
        "Debrief and corrective-action record.",
        "Test-schedule tracking record.",
    ],
    "COP.5.a": [
        "CPR-availability record across all areas and shifts.",
        "Response-time record for a sampled call.",
        "Trained-responder roster.",
    ],
    "COP.5.b": [
        "Written CPR-team role-assignment record.",
        "Role-compliance observation or debrief record.",
        "Team-composition record for a sampled event.",
    ],
    "COP.5.c": [
        "Crash-cart or emergency-equipment inventory by area.",
        "Medication-stock record matching the emergency-medication list (MOM.3.f).",
        "Availability-check record.",
    ],
    "COP.5.d": [
        "CPR event record — time, interventions, outcome.",
        "Documentation-completeness check.",
        "Record filed in the patient's medical record.",
    ],
    "COP.5.e": [
        "Multi-disciplinary CPR-committee post-event analysis record.",
        "Analysis-timeliness record.",
        "Findings documentation.",
    ],
    "COP.5.f": [
        "CAPA record from CPR post-event analysis, with owner and due date.",
        "Closure-tracking record.",
        "Repeat-event trend record.",
    ],
    "COP.6.a": [
        "Written nursing-care guidance or protocol.",
        "Nursing documentation record confirming the guidance was followed.",
        "Staff training record on the guidance.",
    ],
    "COP.6.b": [
        "Patient-care assignment record — nurse-to-patient ratio, competency match.",
        "Assignment-policy document.",
        "Shift-roster record.",
    ],
    "COP.6.c": [
        "Acuity-scoring tool and record.",
        "Staffing-adjustment record based on acuity.",
        "Outcome-tracking record linked to acuity-based staffing.",
    ],
    "COP.6.d": [
        "Nursing-care-plan documentation integrated with the overall patient-care plan.",
        "Multidisciplinary care-record cross-reference.",
        "Documentation-completeness check.",
    ],
    "COP.6.e": [
        "Nursing-equipment inventory and adequacy record.",
        "Equipment-maintenance record.",
        "Equipment-availability check by unit.",
    ],
    "COP.6.f": [
        "Written scope-of-practice document for nursing decision-making.",
        "Example decision record within that scope.",
        "Nurse-empowerment policy reference.",
    ],
    "COP.7.a": [
        "Clinical-indication documentation for a sampled procedure.",
        "Justification record in the medical record.",
        "Confirmation the procedure matched clinical need.",
    ],
    "COP.7.b": [
        "Written procedure-specific guidance or protocol.",
        "Safety-checklist record for the procedure.",
        "Staff-training record on the guidance.",
    ],
    "COP.7.c": [
        "Credentialing or privileging cross-reference (HRM.11–13) for personnel performing the procedure.",
        "Order and performer-identification record.",
        "Assisting-personnel qualification record.",
    ],
    "COP.7.d": [
        "Site, procedure and patient verification checklist for a sampled procedure.",
        "Time-out record before the procedure.",
        "Near-miss or adverse-event record, where applicable.",
    ],
    "COP.7.e": [
        "Consent form signed by the performing personnel.",
        "Cross-reference to the PRE.4/PRE.2.g consent process.",
        "Consent-completeness check.",
    ],
    "COP.7.f": [
        "Intra- and post-procedure monitoring record.",
        "Monitoring-parameter documentation.",
        "Escalation record for an abnormal finding.",
    ],
    "COP.7.g": [
        "Procedure-note documentation in the patient record.",
        "Documentation-completeness and accuracy check.",
        "Timeliness-of-entry record.",
    ],
    "COP.8.a": [
        "Transfusion-service scope document matched to services provided.",
        "Service-scope review record.",
        "Cross-reference to the AAC.1 service definition.",
    ],
    "COP.8.b": [
        "Written guidance for blood/component collection, testing, storage and distribution.",
        "Process-compliance record for a sampled unit.",
        "National Blood Transfusion Standards reference.",
    ],
    "COP.8.c": [
        "Blood-storage temperature log and equipment-monitoring record.",
        "Cold-chain maintenance record from collection to transfusion.",
        "Storage-condition compliance check.",
    ],
    "COP.8.d": [
        "Two-identifier patient-verification and compatibility-check record before transfusion.",
        "Rational-use or blood-utilisation review record.",
        "Informed-consent record for transfusion.",
    ],
    "COP.8.e": [
        "Blood or component availability record for emergency and routine requests.",
        "Turnaround-time log against the defined timeframe.",
        "Escalation record for a delayed request.",
    ],
    "COP.8.f": [
        "Post-transfusion form collected for a sampled transfusion.",
        "Transfusion-reaction identification and analysis record.",
        "CAPA record from reaction analysis.",
    ],
    "COP.8.g": [
        "Written transfusion-service quality assurance programme.",
        "Indicator-monitoring record for the programme.",
        "Improvement-action record from QA findings.",
    ],
    "COP.9.a": [
        "Written ICU/HDU care guidance.",
        "Documentation record confirming the guidance was followed.",
        "Staff training record.",
    ],
    "COP.9.b": [
        "Written ICU/HDU admission and discharge criteria.",
        "Criteria-application record for a sampled admission or discharge.",
        "Criteria-review record.",
    ],
    "COP.9.c": [
        "Staffing-ratio record for ICU/HDU.",
        "Equipment inventory and adequacy record.",
        "Availability-check record.",
    ],
    "COP.9.d": [
        "Written bed-shortage procedure.",
        "Activation record for a bed-shortage event.",
        "Triage or prioritisation record during shortage.",
    ],
    "COP.9.e": [
        "IPC-practice compliance record for ICU/HDU (cross-reference the IPC chapter).",
        "Surveillance-data record for the unit.",
        "Hand-hygiene compliance record.",
    ],
    "COP.9.f": [
        "Written ICU/HDU quality assurance programme.",
        "Indicator-monitoring record.",
        "Improvement-action record.",
    ],
    "COP.9.g": [
        "Periodic counselling record for patient/family.",
        "Counselling-frequency documentation.",
        "Named responsible person for counselling.",
    ],
    "COP.10.a": [
        "Written obstetric-service organisation document.",
        "Safety-protocol compliance record.",
        "Staff-competency record.",
    ],
    "COP.10.b": [
        "High-risk obstetric-case identification record.",
        "Referral record to an appropriate centre where needed.",
        "Care-plan record for identified high-risk cases.",
    ],
    "COP.10.c": [
        "Competency or training record for staff caring for high-risk obstetric cases.",
        "Credentialing cross-reference.",
        "Case-assignment record.",
    ],
    "COP.10.d": [
        "Ante-natal care record and visit schedule.",
        "Ante-natal service documentation.",
        "Risk-screening record during ante-natal visits.",
    ],
    "COP.10.e": [
        "Birth-companion policy document.",
        "Birth-companion-presence record for a sampled labour case.",
        "Staff-awareness record of the policy.",
    ],
    "COP.10.f": [
        "Privacy-and-dignity practice record for obstetric patients.",
        "Patient-feedback record on treatment and privacy.",
        "Confidentiality-practice observation record.",
    ],
    "COP.10.g": [
        "Documented explanation-of-danger-signs record.",
        "Patient or companion education record.",
        "Treating-doctor documentation of the explanation.",
    ],
    "COP.10.h": [
        "Nutritional-assessment record within obstetric assessment.",
        "Cross-reference to COP.19 nutritional therapy.",
        "Documentation-completeness check.",
    ],
    "COP.10.i": [
        "Peri-natal monitoring record.",
        "Post-natal monitoring record.",
        "Monitoring-parameter documentation.",
    ],
    "COP.10.j": [
        "Neonatal-care facility or equipment record for high-risk obstetric cases.",
        "Staff-availability record for neonatal care.",
        "Referral-arrangement record where facilities are insufficient.",
    ],
    "COP.10.k": [
        "Documented adherence record to legal and defined ART practices.",
        "ART registration or licence record, where applicable.",
        "Compliance-review record.",
    ],
    "COP.11.a": [
        "Written paediatric-service organisation document.",
        "Safety-protocol compliance record.",
        "Staff-competency record.",
    ],
    "COP.11.b": [
        "National or international neonatal-care guideline reference.",
        "Neonatal-care protocol compliance record.",
        "Staff-training record on the guidelines.",
    ],
    "COP.11.c": [
        "Age-specific competency-training record for staff caring for children.",
        "Competency-verification record.",
        "Training-currency record.",
    ],
    "COP.11.d": [
        "Special-care facility or equipment record for children.",
        "Provision-adequacy check.",
        "Age-appropriate-care record.",
    ],
    "COP.11.e": [
        "Paediatric assessment record covering growth, development, immunisation and nutrition.",
        "Assessment-completeness check.",
        "Growth-chart documentation.",
    ],
    "COP.11.f": [
        "Written child or neonate security measures — access control, identification bands, alarm systems.",
        "Abduction-drill record.",
        "Abuse-identification and reporting record.",
    ],
    "COP.11.g": [
        "Family-education record on nutrition, immunisation and safe parenting.",
        "Education-material record.",
        "Documentation of education delivered.",
    ],
    "COP.11.h": [
        "Adolescent-friendly service provision record.",
        "Dedicated space or counselling record for adolescents.",
        "Staff-training record on adolescent-friendly care.",
    ],
    "COP.12.a": [
        "Written procedural-sedation protocol.",
        "Consistency-check record across sedation locations.",
        "Staff-training record.",
    ],
    "COP.12.b": [
        "Sedation-specific consent form on file.",
        "Consent-process documentation.",
        "Cross-reference to PRE.4.",
    ],
    "COP.12.c": [
        "Sedation-privileging or training record for personnel administering sedation.",
        "Competency-verification record.",
        "Currency-of-training record.",
    ],
    "COP.12.d": [
        "Role-separation record — monitoring person distinct from the procedure performer.",
        "Staffing record for a sampled sedation case.",
        "Confirmation of role separation in practice.",
    ],
    "COP.12.e": [
        "Intra-procedure monitoring record — heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, sedation level.",
        "Monitoring-frequency documentation.",
        "Equipment-availability record.",
    ],
    "COP.12.f": [
        "Post-sedation monitoring record.",
        "Documentation-completeness check.",
        "Recovery-status tracking record.",
    ],
    "COP.12.g": [
        "Written discharge or recovery criteria for sedation.",
        "Criteria-application record for a sampled discharge.",
        "Discharge-authorisation record.",
    ],
    "COP.12.h": [
        "Rescue-equipment inventory for deeper-than-intended sedation.",
        "Trained-workforce availability record for airway rescue.",
        "Emergency-response record for a sampled deeper-sedation event.",
    ],
    "COP.13.a": [
        "Written anaesthesia-service protocol.",
        "Consistency-check record.",
        "Staff-credentialing record.",
    ],
    "COP.13.b": [
        "Documented pre-anaesthesia assessment and anaesthesia plan.",
        "Plan-completeness check.",
        "Assessment-timing record before the procedure.",
    ],
    "COP.13.c": [
        "Documented pre-induction assessment.",
        "Assessment-timing record immediately before induction.",
        "Completeness check.",
    ],
    "COP.13.d": [
        "Anaesthesia consent form signed by the anaesthesiologist.",
        "Consent-process documentation.",
        "Cross-reference to PRE.4.",
    ],
    "COP.13.e": [
        "Intra-anaesthesia monitoring record — temperature, heart rate, cardiac rhythm, respiratory rate, blood pressure, oxygen saturation, end-tidal CO2.",
        "Monitoring-frequency documentation.",
        "Equipment-calibration record.",
    ],
    "COP.13.f": [
        "Post-anaesthesia monitoring record.",
        "Documentation-completeness check.",
        "Recovery-status tracking record.",
    ],
    "COP.13.g": [
        "Written recovery-transfer criteria.",
        "Criteria-application record for a sampled transfer.",
        "Anaesthesiologist sign-off record.",
    ],
    "COP.13.h": [
        "Anaesthesia-type and medication documentation in the patient record.",
        "Record-completeness check.",
        "Batch or dose documentation, where applicable.",
    ],
    "COP.13.i": [
        "IPC-compliance record for anaesthesia procedures (cross-reference the IPC chapter).",
        "Equipment sterilisation or disinfection record.",
        "Cross-infection-prevention observation record.",
    ],
    "COP.13.j": [
        "Adverse-anaesthesia-event log.",
        "Monitoring and analysis record.",
        "CAPA record, where applicable.",
    ],
    "COP.14.a": [
        "Written surgical-service protocol.",
        "Consistency-check record.",
        "Staff-credentialing record.",
    ],
    "COP.14.b": [
        "Pre-operative assessment record.",
        "Documented pre-operative diagnosis.",
        "Pre-operative instruction record given to the patient.",
    ],
    "COP.14.c": [
        "Surgical consent form signed by the surgeon.",
        "Consent-process documentation.",
        "Cross-reference to PRE.4.",
    ],
    "COP.14.d": [
        "Site, patient and procedure verification checklist.",
        "Surgical time-out record.",
        "Near-miss or adverse-event record, where applicable.",
    ],
    "COP.14.e": [
        "Operative note documented before transfer out of recovery.",
        "Note-completeness check.",
        "Timeliness-of-documentation record.",
    ],
    "COP.14.f": [
        "Documented post-operative care plan.",
        "Plan-implementation record.",
        "Post-operative monitoring record.",
    ],
    "COP.14.g": [
        "Patient, personnel and material-flow IPC-compliance record for the OT.",
        "Traffic-control observation record.",
        "Cross-reference to IPC.4.",
    ],
    "COP.14.h": [
        "OT facility, equipment, instrument and supply inventory.",
        "Availability-and-readiness check record.",
        "Pre-list equipment-check record.",
    ],
    "COP.14.i": [
        "Written OT quality assurance programme.",
        "Indicator-monitoring record.",
        "Improvement-action record.",
    ],
    "COP.14.j": [
        "OT environmental-surveillance record — air quality, surface swabs as applicable.",
        "Surveillance-frequency documentation.",
        "Corrective-action record for a surveillance finding.",
    ],
    "COP.15.a": [
        "Transplant-programme documentation confirming legal-requirement compliance (Transplantation of Human Organs Act).",
        "Ethics-committee approval record.",
        "Compliance-review record.",
    ],
    "COP.15.b": [
        "Adopted transplant clinical-practice-guideline reference.",
        "Guideline-compliance record for a sampled case.",
        "Staff-training record.",
    ],
    "COP.15.c": [
        "Trained-counsellor education and counselling record for recipient and donor.",
        "Counselling-documentation record before transplantation.",
        "Counsellor-qualification record.",
    ],
    "COP.15.d": [
        "Organ-donation awareness-activity record.",
        "IEC-material record.",
        "Awareness-campaign documentation.",
    ],
    "COP.16.a": [
        "Written vulnerable-patient identification criteria.",
        "Identification and management-plan record for a sampled vulnerable patient.",
        "Staff-training record.",
    ],
    "COP.16.b": [
        "Fall-risk-assessment tool and record.",
        "Fall-prevention-measure implementation record.",
        "Fall-incident log and analysis.",
    ],
    "COP.16.c": [
        "Pressure-ulcer-risk-assessment tool and record.",
        "Prevention-measure implementation record.",
        "Pressure-ulcer-incidence tracking record.",
    ],
    "COP.16.d": [
        "DVT-risk-assessment tool and record.",
        "Prophylaxis-measure implementation record.",
        "DVT-incidence tracking record.",
    ],
    "COP.16.e": [
        "Written restraint-need identification criteria.",
        "Documented restraint order with periodic review.",
        "Restraint-monitoring record.",
    ],
    "COP.17.a": [
        "Written pain-management guidance.",
        "Pain-management outcome record for a sampled patient.",
        "Staff-training record.",
    ],
    "COP.17.b": [
        "Pain-screening record at defined points (for example admission).",
        "Screening-tool documentation.",
        "Screening-frequency record.",
    ],
    "COP.17.c": [
        "Detailed pain-assessment record for a screened-positive patient.",
        "Periodic-reassessment record.",
        "Assessment-tool documentation.",
    ],
    "COP.17.d": [
        "Pain-alleviation or medication record titrated to patient need and response.",
        "Titration-documentation record.",
        "Response-monitoring record.",
    ],
    "COP.18.a": [
        "Rehabilitation-service scope document matched to services provided.",
        "Service-scope review record.",
        "Cross-reference to AAC.1.",
    ],
    "COP.18.b": [
        "Written rehabilitation-service protocol.",
        "Consistency-check record.",
        "Staff-training record.",
    ],
    "COP.18.c": [
        "Multi-disciplinary rehabilitation care-plan record.",
        "Collaborative-planning documentation.",
        "Care-provider-involvement record.",
    ],
    "COP.18.d": [
        "Rehabilitation space and equipment inventory.",
        "Adequacy-check record.",
        "Equipment-maintenance record.",
    ],
    "COP.18.e": [
        "Functional-assessment record at admission.",
        "Periodic-reassessment record.",
        "Documentation-completeness check.",
    ],
    "COP.18.f": [
        "IPC and safety-practice compliance record for rehabilitation.",
        "Equipment cleaning or disinfection record.",
        "Safety-observation record.",
    ],
    "COP.18.g": [
        "Developed rehabilitation care-pathway document.",
        "Implementation and consistency-check record.",
        "Periodic-review record.",
    ],
    "COP.19.a": [
        "Nutritional-screening record at admission.",
        "Screening-tool documentation.",
        "Screening-completion-rate record.",
    ],
    "COP.19.b": [
        "Nutritional-assessment record for screened-positive patients.",
        "Assessment-tool documentation.",
        "Dietitian-involvement record.",
    ],
    "COP.19.c": [
        "Multi-disciplinary therapeutic-diet plan record.",
        "Diet-plan documentation.",
        "Care-provider-involvement record.",
    ],
    "COP.19.d": [
        "Written diet-order record.",
        "Food-service-versus-order matching record.",
        "Order-change tracking record.",
    ],
    "COP.19.e": [
        "Family-education record on diet limitations when families provide food.",
        "Education-material record.",
        "Documentation of education delivered.",
    ],
    "COP.20.a": [
        "Written end-of-life-care guidance.",
        "Consistency-check record across settings.",
        "Staff-training record.",
    ],
    "COP.20.b": [
        "Multi-disciplinary end-of-life-care team record.",
        "Team-involvement documentation for a sampled case.",
        "Care-coordination record.",
    ],
    "COP.20.c": [
        "End-of-life-care documentation confirming legal-requirement compliance.",
        "Consent or advance-directive record, where applicable.",
        "Compliance-review record.",
    ],
    "COP.20.d": [
        "Unique-needs identification record for patient and family — cultural, spiritual, psychosocial.",
        "Needs-addressed documentation.",
        "Family-involvement record.",
    ],
    "COP.20.e": [
        "Symptomatic-treatment and pain-alleviation record.",
        "Cross-reference to COP.17 pain management.",
        "Comfort-care documentation.",
    ],
}


def oe_mapping(n: int, oes: list[dict], has_stop: bool) -> list[dict]:
    mapping = []
    for i, oe in enumerate(oes, start=1):
        short = clean_text(oe["text"] or "")
        steps = f"Section 3; 5.{i}"
        if has_stop and n in STOP_WORK_PROPOSALS and i <= 3:
            steps += "; Section 6 Stop-work"
        records = COP_RECORDS.get(oe["oe_code"])
        if not records:
            raise KeyError(f"Missing hand-authored evidence records for {oe['oe_code']}")
        mapping.append(
            {
                "oe_code": oe["oe_code"],
                "requirement": short or oe["oe_code"],
                "steps": steps,
                "responsible": PREPARED_BY.get(n, "Quality Coordinator"),
                "records": records,
            }
        )
    return mapping


def build_one(n: int, inv: dict, interps: dict[int, list[str]]) -> dict:
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

    doc_no = D(f"HCO/COP/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, interps.get(n, []))
    oe_codes = [o["oe_code"] for o in oes]

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard COP.{n}: {std_title}

It covers objective elements COP.{n}.{oes[0]['letter']}–{oes[-1]['letter']} ({len(oes)} elements).

This policy owns COP.{n}. Related AAC, PRE, IPC/HIC, HRM and MOM duties stay with those policies — cross-reference only.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to staff who deliver or oversee the care described in COP.{n} at {HOSPITAL}, including the {prepared}, treating doctors, nurses and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

{hco_boundaries_clause(["AAC"])} Spell out abbreviations on first use in training materials."""

    policy_statement = f"""{HOSPITAL} implements COP.{n} so that {std_title[0].lower() + std_title[1:] if std_title else "care is safe and uniform"}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work triggers fire (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that COP.{n} is resourced and followed.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Treating doctors / nurses / technicians (as applicable)
- Deliver care as written; escalate stop-work triggers without delay.

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

This policy is reviewed {D('annually')}, and sooner after a related adverse event."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Care of Patients, standard COP.{n}.
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — COP.{n} interpretations (source PDF md5 2c4489ee98de4ae9b49cba168ea9f42a).
- Internal documents of {HOSPITAL}: written guidance and registers named for COP.{n}."""

    abbreviations = f"""COP — Care of Patients (NABH Hospitals chapter)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — Objective Element
CORE — Core objective element (NABH)
RCA — Root Cause Analysis
CAPA — Corrective and Preventive Action"""

    ufg = f"""HCO COP.{n} v2 (2026-08-20). Official Standards PDF OE count {len(oes)}; levels from portal text-layer matrix (COP.13.b/c corrected to body: b=CORE, c=Commitment). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — JUDGMENT CALL: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted"}.
draft_label={DRAFT_LABEL!r} via hco_document_control (no 'not an approved master' leftover). chapter=HCO. doc_no HCO/COP/POL/{n:02d}.
Do not touch AAC."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "Quality Coordinator",
            f"department clinical staff covered by COP.{n}",
        ]
    )

    draft = {
        "standard_code": f"COP.{n}",
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
                "date": "20-08-2026",
                "description": f"HCO Full 6th Edition COP.{n} v2 draft from official Standards PDF + guidebook OCR; draft_label={DRAFT_LABEL}.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_cop_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — COP.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.COP.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    """Thin builder that re-emits from inventory via generate module."""
    path = BUILD / f"build_hco_cop{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO COP.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_cop_v2.py
Explicit draft_label via hco_cop_v2_common.hco_document_control.
Does NOT overwrite SHCO COP or HCO AAC files.
"""
from __future__ import annotations

import sys
from generate_hco_cop_v2 import emit_standard

if __name__ == "__main__":
    sys.exit(emit_standard({n}))
''',
        encoding="utf-8",
    )


def emit_standard(n: int) -> int:
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    interps = load_ocr_interpretations()
    draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, interps)
    emit_pre_v2(
        draft,
        f"hco_cop{n}_v2_draft.json",
        f"HCO.COP.{n}_v2_preview.md",
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
    assert sum(inv[str(n)]["count"] for n in range(1, 21)) == 136
    interps = load_ocr_interpretations()
    for n in range(1, 21):
        write_builder(n)
        draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, interps)
        # Guard: never emit leftover phrase
        assert "not an approved master" not in draft["resources_required"]
        assert DRAFT_LABEL in draft["resources_required"]
        emit_pre_v2(
            draft,
            f"hco_cop{n}_v2_draft.json",
            f"HCO.COP.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(f"COP.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
