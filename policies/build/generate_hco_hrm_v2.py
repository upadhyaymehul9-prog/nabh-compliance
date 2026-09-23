# -*- coding: utf-8 -*-
"""Generate HCO Full HRM.1–HRM.13 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_hrm_v2.py

Official portal PDF has 13 HRM standards / 76 OEs. All 13 are drafted.
Does not touch AAC, COP, MOM, PRE, IPC, PSQ, ROM, FMS, or SHCO (including the
already-deployed SHCO 3rd Edition HRM chapter — separate programme/edition).
Always sets explicit HCO draft_label via hco_document_control (no "not an
approved master" leftover). HCO drafts/previews write to policies/drafts_hco
and policies/build/preview_hco.
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
from hco_hrm_v2_common import (  # noqa: E402
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
from hco_hrm_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_hrm_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_hrm_interpretations.json"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 where the Guidebook names an on-point statute. Proposed default:
# HRM.12 only (Indian Nursing Council Act, 1947). See chapter notes for why
# HRM.8's "relevant labour laws and CCS (CCA) rules" stays a method note.
STATUTE_BY_STD: dict[int, str | None] = {
    12: (
        "the Indian Nursing Council Act, 1947, as cited in NABH HRM.12 for identifying "
        "nursing professionals permitted to provide patient care without supervision"
    ),
}

PREPARED_BY: dict[int, str] = {n: "HR In-Charge / Personnel Officer" for n in range(1, 14)}

POLICY_TITLES: dict[int, str] = {
    1: "Human Resource Planning and Governance",
    2: "Staff Recruitment",
    3: "Staff Induction Training",
    4: "Professional Training and Development",
    5: "Job-Specific Staff Training",
    6: "Safety and Quality-Related Staff Training",
    7: "Staff Performance Appraisal",
    8: "Disciplinary and Grievance Handling",
    9: "Staff Health and Safety",
    10: "Staff Personal Information and Records",
    11: "Credentialing and Privileging of Medical Professionals",
    12: "Credentialing and Privileging of Nursing Professionals",
    13: "Credentialing and Privileging of Para-Clinical Professionals",
}

CHAPTER_INTENT = (
    "The most important resource of the organisation is its human resource. Human resources "
    "are an asset for the effective and efficient functioning of the organisation. The "
    "management plans on identifying the right number and skill mix of staff required to "
    "render safe care to the patients. Recruitment of staff is accomplished by having a "
    "uniform and standardised system. The organisation must orient the staff including "
    "outsourced staff, volunteers, students and trainees to its environment and also orient "
    "them to specific duties and responsibilities related to their position. The organisation "
    "should plan to have an ongoing professional training / in-service education to enhance "
    "the competencies and skills of the staff continually. A systematic and structured "
    "appraisal system must be used for staff development. The organisation uses this as an "
    "opportunity to discuss, motivate, identify gaps in the performance of the staff. The "
    "organisation promotes the physical and mental well-being of staff. A grievance handling "
    "mechanism and disciplinary procedure should be in place. Credentialing and privileging "
    "of health-care professionals (medical, nursing and other para-clinical professional) are "
    "done to ensure patient safety. A document containing all such personal information has "
    "to be maintained for all staff."
)


def clean_text(s: str) -> str:
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    s = s.replace("", "fi").replace("", "fl")
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
        f"{len(items)+1}. Staff who see a HRM.{n} rule broken report it the same shift to the "
        f"{D('HR In-Charge / Personnel Officer')} or the {D('Medical Superintendent')}."
    )
    return "\n".join(items)


# Fix #5 — hand-authored per-OE evidence records, matching the quality bar
# AAC.1 / SHCO HIC.1 / HCO ROM / HCO FMS / HCO PSQ / HCO IPC / HCO PRE /
# HCO MOM already demonstrate.
HRM_RECORDS: dict[str, list[str]] = {
    "HRM.1.a": [
        "Annual workforce plan comparing current and projected staffing against services and patient volume.",
        "Department-head input record into the plan.",
        "Corrective-action record for a variance found during the year.",
    ],
    "HRM.1.b": [
        "Sanctioned-versus-actual staffing comparison record by department.",
        "Staffing-norm reference used (for example the WHO WISN method for nursing).",
        "Escalation record for an unresolved shortfall.",
    ],
    "HRM.1.c": [
        "Written contingency plan for long- and short-term workforce shortages, including unplanned shortages.",
        "Shortage-event log with cause, measure used and outcome.",
        "Test record of the contingency plan, at least twice a year.",
    ],
    "HRM.1.d": [
        "Job description on file for each staff category, including qualification, skill and experience requirements.",
        "Signed acknowledgement record from a new hire receiving their job description.",
        "Minimum-qualification exemption record, where applicable.",
    ],
    "HRM.1.e": [
        "Background-check register recording method, date and outcome per new hire.",
        "Completion record before or within one month of joining.",
        "Escalation record for any staff member with no background check on file.",
    ],
    "HRM.1.f": [
        "Current organisation structure or chart showing hierarchy and reporting lines.",
        "Department- or service-level reporting-relationship record.",
        "Dissemination record to stakeholders.",
    ],
    "HRM.1.g": [
        "Completed exit-interview record for a departing staff member.",
        "Quarterly trend report compiled from exit interviews.",
        "HR-improvement action record from exit-interview findings.",
    ],
    "HRM.2.a": [
        "Written recruitment guidance document.",
        "Recruitment register — vacancy, candidates, selection rationale, fill date.",
        "Statutory-requirement compliance record where applicable.",
    ],
    "HRM.2.b": [
        "Pre-employment medical examination record on file.",
        "Consent record for any testing performed, confirming no non-consensual testing.",
        "Fitness-to-work determination record.",
    ],
    "HRM.2.c": [
        "Written code of conduct document.",
        "Signed staff acknowledgement at joining.",
        "Confidentiality-protection clause record within the code.",
    ],
    "HRM.2.d": [
        "Documented administrative procedures — attendance, leave, conduct, replacement.",
        "Current-version record held by HR.",
        "Cross-reference to induction training covering these procedures (HRM.3.h).",
    ],
    "HRM.3.a": [
        "Induction-training record within one month of joining.",
        "Attendance record covering doctors, consultants, outsourced staff, volunteers, students and trainees.",
        "Induction-content record covering HRM.3.b–h and hospital-specific requirements.",
    ],
    "HRM.3.b": [
        "Vision, mission and values orientation record within induction training.",
        "Staff-awareness confirmation record.",
        "Outsourced-staff inclusion record.",
    ],
    "HRM.3.c": [
        "Staff-rights-and-responsibilities and patient-rights-and-responsibilities training record.",
        "Violation-identification-and-reporting awareness confirmation.",
        "Induction attendance record.",
    ],
    "HRM.3.d": [
        "Safety training record within induction — patient, visitor and staff safety, emergency codes.",
        "Emergency-code awareness confirmation.",
        "Induction attendance record.",
    ],
    "HRM.3.e": [
        "CPR/BLS training record within induction.",
        "Advanced-training record for ICU or high-dependency-unit staff (ACLS/PALS/NRP or equivalent).",
        "Valid-certificate exemption record, where applicable.",
    ],
    "HRM.3.f": [
        "Hospital infection prevention and control training record within induction.",
        "Content record covering IPC programme policies and practices.",
        "Induction attendance record.",
    ],
    "HRM.3.g": [
        "Service-standards orientation record within induction.",
        "Staff-awareness confirmation.",
        "Induction attendance record.",
    ],
    "HRM.3.h": [
        "Administrative-procedures orientation record within induction — attendance, leave, conduct.",
        "Organisation-wide policy-awareness record.",
        "Cross-reference to HRM.2.d.",
    ],
    "HRM.3.i": [
        "Department, unit, service or programme-level policy-and-procedure orientation record.",
        "Delivery-location record confirming it was given at that level.",
        "Induction attendance record.",
    ],
    "HRM.3.j": [
        "Information-systems, information-security and data-use training record.",
        "Job-responsibility-matched training-content record.",
        "EMR-access training record, where the hospital uses electronic health records.",
    ],
    "HRM.4.a": [
        "Written training and development policy or manual.",
        "Training-needs-identification, methodology, assessment and calendar record.",
        "Coverage record for all staff categories, including doctors and outsourced staff.",
    ],
    "HRM.4.b": [
        "Training record with title, trainer, date, duration and trainee list with signatures.",
        "Digital or physical training-record system.",
        "Content-capture record where possible.",
    ],
    "HRM.4.c": [
        "Training record triggered by a job-responsibility change or new-equipment introduction.",
        "Operational-and-maintenance training record for new equipment.",
        "Training-completion confirmation before independent use.",
    ],
    "HRM.4.d": [
        "Feedback-mechanism record for training-programme improvement.",
        "Feedback data on course material, facilities and trainer capability.",
        "Both internal and external training coverage record.",
    ],
    "HRM.4.e": [
        "Immediate post-training evaluation record — pre/post-test.",
        "Later workplace-effectiveness evaluation record.",
        "Retraining record where the evaluation showed a need.",
    ],
    "HRM.4.f": [
        "Continuing-professional-development support record — courses, conferences, e-learning access.",
        "Minimum mandatory annual training-hours specification record.",
        "Staff-participation record against the mandatory hours.",
    ],
    "HRM.5.a": [
        "Blood-and-blood-product handling training record for relevant staff (doctors, nurses, technicians, transport staff).",
        "Cross-reference to COP.8 blood transfusion service practice.",
        "Training-content record — safe transport, informed consent, documentation, transfusion-reaction handling.",
    ],
    "HRM.5.b": [
        "Vulnerable-patient identification-and-care training record.",
        "Cross-reference to COP.16.a.",
        "Relevant-staff coverage record.",
    ],
    "HRM.5.c": [
        "Control-and-restraint-technique training record.",
        "Cross-reference to COP.16.e.",
        "Relevant-staff coverage record.",
    ],
    "HRM.5.d": [
        "Healthcare-communication-technique training record.",
        "Training-needs source record — complaints, incident reports, appraisals, feedback.",
        "Cross-reference to PRE.8.e.",
    ],
    "HRM.5.e": [
        "Periodic CPR-training record for direct-patient-care staff, at least once in two years or sooner after protocol change.",
        "Advanced-training record for emergency, ICU or high-dependency staff.",
        "Refresher-schedule tracking record.",
    ],
    "HRM.5.f": [
        "Infection-prevention-and-control training record at least annually.",
        "Antimicrobial-stewardship-content record for medical professionals, IPC nurses, clinical pharmacist and support staff.",
        "Attendance record.",
    ],
    "HRM.6.a": [
        "Safety-programme training record.",
        "Laboratory- or imaging-specific safety-training record where applicable.",
        "Cross-reference to PSQ.1.a.",
    ],
    "HRM.6.b": [
        "Risk-detection-and-handling training record — physical, chemical, environmental, process-related risks.",
        "Practical-demonstration record — blood-spill management, hazardous-material handling.",
        "Training-content coverage record.",
    ],
    "HRM.6.c": [
        "Incident-procedure awareness record.",
        "Staff confirmation of knowing the sequence of actions to take.",
        "Training or briefing record.",
    ],
    "HRM.6.d": [
        "Occupational-safety-aspect training record — needle-stick, radiation, laser, medical-gas, chemotherapy, noise exposure.",
        "Cross-reference to IPC.8.a.",
        "Area-specific hazard-training record.",
    ],
    "HRM.6.e": [
        "Disaster-management-plan training record.",
        "Specific-role training record for an external or internal disaster.",
        "Attendance record.",
    ],
    "HRM.6.f": [
        "Fire-and-non-fire-emergency training record.",
        "Fire-extinguisher and evacuation-procedure demonstration record.",
        "Specific-role training record for non-fire emergencies.",
    ],
    "HRM.6.g": [
        "Quality-improvement-programme training record.",
        "Role-in-programme awareness record.",
        "Department-specific quality-assurance training record where applicable (laboratory, imaging, emergency, ICU, blood centre, surgical services).",
    ],
    "HRM.7.a": [
        "Performance-appraisal record for all staff categories, including the organisation head and doctors.",
        "Competency-assessment record where appropriate.",
        "Contractor-conducted appraisal record for outsourced staff.",
    ],
    "HRM.7.b": [
        "Appraisal-system-awareness record at induction.",
        "Service-booklet or induction-material reference.",
        "Staff-acknowledgement record.",
    ],
    "HRM.7.c": [
        "Pre-determined-criteria document — key performance indicators or key result areas derived from the job description.",
        "Evaluation record against those criteria.",
        "Job-description cross-reference record.",
    ],
    "HRM.7.d": [
        "Development-action record from the appraisal — training requirement identified.",
        "Key-result-area and training-need-assessment record.",
        "Underperformance-management written-guidance record.",
    ],
    "HRM.7.e": [
        "Dated performance-appraisal record, at least annually.",
        "Documentation-completeness record.",
        "Appraisal-cycle-tracking record confirming no missed year.",
    ],
    "HRM.8.a": [
        "Written disciplinary and grievance handling guidance.",
        "Coverage record for the HRM.8.c–e elements.",
        "Workplace-issue inclusion record — bullying, harassment.",
    ],
    "HRM.8.b": [
        "Staff-awareness record of the disciplinary and grievance mechanism.",
        "Communication record — induction, notice board, policy circulation.",
        "Confirmation across all staff categories.",
    ],
    "HRM.8.c": [
        "Natural-justice-principle record — both parties heard before a decision.",
        "Disciplinary case record demonstrating the principle applied.",
        "Policy-document reference.",
    ],
    "HRM.8.d": [
        "Labour-law compliance record for the disciplinary and grievance procedure.",
        "Internal Complaints Committee constitution record for sexual-harassment complaints.",
        "Legal-currency review record of the procedure.",
    ],
    "HRM.8.e": [
        "Appellate-authority designation record, higher than the disciplinary authority.",
        "Appeal-case record showing the provision was used.",
        "Policy-document reference.",
    ],
    "HRM.8.f": [
        "Grievance-redress action record.",
        "Documentation and communication record to the aggrieved staff member.",
        "Closure-tracking record.",
    ],
    "HRM.9.a": [
        "Written staff health and safety policy covering physical and mental health.",
        "Staff vaccination and immunisation programme record.",
        "PPE-provision and second-victim-support record.",
    ],
    "HRM.9.b": [
        "Annual health-check record for direct-patient-care staff.",
        "Findings and results documentation in the personal file.",
        "No-charge-to-staff confirmation record.",
    ],
    "HRM.9.c": [
        "Workplace-injury treatment record — needlestick, patient-transport injury, noise-related, etc.",
        "Counselling record where appropriate.",
        "Workplace-violence-injury inclusion record.",
    ],
    "HRM.9.d": [
        "Workplace-violence risk-assessment record.",
        "Written security guidance covering workplace-violence prevention and handling.",
        "Law-enforcement-liaison and counselling record for affected staff.",
    ],
    "HRM.10.a": [
        "Personal-file maintenance record for all staff, current and updated.",
        "Confidentiality and access-restriction record.",
        "Electronic-format record, where used.",
    ],
    "HRM.10.b": [
        "Personal-file content record — qualification, job description, credential verification, health status.",
        "Completeness-check record.",
        "Update-currency record.",
    ],
    "HRM.10.c": [
        "In-service training and education record maintained in, or traceable from, the personal file.",
        "Annual training-summary record for internal training.",
        "Attendance-verification supporting document.",
    ],
    "HRM.10.d": [
        "Personal-file record of evaluation results and remarks — appraisals, training assessment, health-check outcome, achievement/complaint/warning/memo.",
        "Completeness-check record.",
        "Confidential-handling record.",
    ],
    "HRM.11.a": [
        "Identified-medical-professional list permitted to provide unsupervised patient care.",
        "Qualification, training and experience verification record.",
        "Cross-reference to the HRM.11 stop-work trigger for unlisted practice.",
    ],
    "HRM.11.b": [
        "Education, registration, training and experience documentation record, updated periodically.",
        "Personal-file record of the update.",
        "New-qualification acquisition update record.",
    ],
    "HRM.11.c": [
        "Verification record with the awarding organisation.",
        "National Medical Commission or equivalent reference-check record.",
        "Verification-completeness record.",
    ],
    "HRM.11.d": [
        "Granted-privilege record naming the clinical services each professional is authorised for.",
        "Annual privilege-review record.",
        "Cross-reference to the HRM.11 stop-work trigger for privileging outside this record.",
    ],
    "HRM.11.e": [
        "Communicated-service record to the professional and to relevant departments.",
        "Admission-rights or surgical-rights notification record (front desk, OT, etc.).",
        "Internal-communication record.",
    ],
    "HRM.11.f": [
        "Standardised privileging-format record.",
        "Proctorship record for new faculty until independent privileges are granted.",
        "Mechanism-confirmation record that professionals provide only privileged services.",
    ],
    "HRM.12.a": [
        "Identified-nursing-professional list permitted to provide unsupervised patient care.",
        "Qualification, training and experience verification record, referencing the Indian Nursing Council Act, 1947.",
        "Cross-reference to the HRM.12 stop-work trigger for unlisted practice.",
    ],
    "HRM.12.b": [
        "Education, registration, training and experience documentation record, updated periodically.",
        "Personal-file record of the update.",
        "New-qualification acquisition update record.",
    ],
    "HRM.12.c": [
        "Verification record with the awarding organisation.",
        "Verification-completeness record.",
        "Cross-reference to HRM.12.b.",
    ],
    "HRM.12.d": [
        "Granted-privilege record naming what each nurse is authorised to do.",
        "Annual privilege-review record.",
        "Cross-reference to the HRM.12 stop-work trigger for privileging outside this record.",
    ],
    "HRM.12.e": [
        "Communicated-service record to the nurse and to nursing services and concerned departments.",
        "Internal-communication record.",
        "Confirmation record of awareness.",
    ],
    "HRM.12.f": [
        "Supervision record for new staff until independent privileges are granted.",
        "Mechanism-confirmation record that nurses provide only privileged services.",
        "Privileging-compliance spot-check record.",
    ],
    "HRM.13.a": [
        "Identified-para-clinical-professional list permitted to provide unsupervised patient care.",
        "Qualification, training and experience verification record.",
        "Cross-reference to the HRM.13 stop-work trigger for unlisted practice.",
    ],
    "HRM.13.b": [
        "Education, registration, training and experience verification and documentation record, updated periodically.",
        "Personal-file record of the update.",
        "Verification-with-awarding-organisation record.",
    ],
    "HRM.13.c": [
        "Granted-privilege record naming what each para-clinical professional is authorised to do.",
        "Registration or licence-on-file record, where applicable.",
        "Cross-reference to the HRM.13 stop-work trigger for privileging outside this record.",
    ],
    "HRM.13.d": [
        "Communicated-service record to the professional and to concerned departments.",
        "Internal-communication record.",
        "Confirmation record of awareness.",
    ],
    "HRM.13.e": [
        "Supervision record for new staff until independent privileges are granted.",
        "Mechanism-confirmation record that para-clinical professionals provide only privileged services.",
        "Privileging-compliance spot-check record.",
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
        records = HRM_RECORDS.get(oe["oe_code"])
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

    doc_no = D(f"HCO/HRM/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    hr = D("HR In-Charge / Personnel Officer")
    gov_scope = (
        "human resources, nursing, medical, and departmental leaders, and all staff of "
        f"{HOSPITAL}"
    )
    own_topic = POLICY_TITLES[n].lower()
    related_chapters = ["AAC", "COP", "MOM", "PRE", "IPC", "PSQ", "ROM", "FMS"]

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard HRM.{n}: {std_title}

{hco_oe_count_clause(len(oes))}

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

{hco_related_duties_clause(own_topic, related_chapters)} Other HRM standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to {gov_scope}, including the {prepared}, the {D('Medical Superintendent')}, departmental leaders and the Quality Coordinator.

{hco_oe_count_clause(len(oes))}

{hco_related_duties_clause(own_topic, related_chapters)}"""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "human resource management requirements are implemented"
    policy_statement = f"""{HOSPITAL} implements HRM.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work conditions are met (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that HRM.{n} is resourced and followed.

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

This policy is reviewed {D('annually')}, and sooner after a related credentialing, staffing or disciplinary-process change."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Human Resource Management, standard HRM.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.{n} interpretations (source PDF has no text layer; transcribed and verified against rendered page images).
- Internal documents of {HOSPITAL}: workforce plan, recruitment and induction records, training records, appraisal records, disciplinary and grievance registers, staff health records, personal files, and credentialing/privileging files named for HRM.{n}."""

    abbreviations = f"""ACLS — Advanced Cardiac Life Support
BLS — Basic Life Support
CAPA — Corrective and Preventive Action
CORE — Core objective element (NABH)
CPR — Cardio-Pulmonary Resuscitation
EMR — Electronic Medical Record
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
HR — Human Resource(s)
HRM — Human Resource Management (NABH Hospitals 6th Edition chapter)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NRP — Neonatal Resuscitation Program
OE — Objective Element
PALS — Paediatric Advanced Life Support
PPE — Personal Protective Equipment
WISN — Workload Indicators of Staffing Need (WHO method)"""

    ufg = f"""HCO HRM.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (Guidebook's own copy of the OE matrix agrees on every letter). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — proposed: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (proposed default: no stop-work on this standard)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/HRM/POL/{n:02d}.
Official chapter is 13 standards / 76 OEs (confirmed against portal summary and against the Guidebook's own copy of the same matrix). Guidebook interpretations transcribed from a scanned PDF with no text layer — verified against rendered page images (no tesseract/pdftoppm available on this machine), not run through a mechanical OCR pass; see policies/source/hco6_hrm_chapter_notes.md. Statute P2 proposed on HRM.12 only (Indian Nursing Council Act, 1947).
Not the same as the already-deployed SHCO 3rd Edition HRM chapter (build_hrm1_v2.py..build_hrm9_v2.py, policies/drafts/hrm*_v2_draft.json) — separate programme and edition, not touched. Do not touch AAC, COP, MOM, PRE, IPC, PSQ, ROM or FMS."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "HR In-Charge / Personnel Officer",
            "Quality Coordinator",
            "departmental leaders",
            f"staff covered by HRM.{n}",
        ]
    )

    draft = {
        "standard_code": f"HRM.{n}",
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
                "description": f"HCO Full 6th Edition HRM.{n} v2 draft: portal PDF OE data + Guidebook interpretations (verified visual transcription, no text layer in source PDF).",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_hrm_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — HRM.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.HRM.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_hrm{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO HRM.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_hrm_v2.py
Explicit draft_label via hco_hrm_v2_common.hco_document_control.
Does NOT overwrite SHCO (including SHCO's own HRM chapter), HCO AAC, HCO COP,
HCO MOM, HCO PRE, HCO IPC, HCO PSQ, HCO ROM or HCO FMS files.
"""
from __future__ import annotations

import sys
from generate_hco_hrm_v2 import emit_standard

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
        f"hco_hrm{n}_v2_draft.json",
        f"HCO.HRM.{n}_v2_preview.md",
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
    total = sum(inv[str(n)]["count"] for n in range(1, 14))
    assert total == 76, total
    bodies = method_bodies(D=D, HOSPITAL=HOSPITAL, BLANK=BLANK)
    interps = load_interpretations()
    expected = [oe["oe_code"] for n in range(1, 14) for oe in inv[str(n)]["oes"]]
    missing = [c for c in expected if c not in bodies]
    extra = [c for c in bodies if c not in expected]
    if missing or extra:
        raise SystemExit(f"method body mismatch missing={missing} extra={extra}")
    missing_i = [c for c in expected if not (interps.get(c) or "").strip()]
    if missing_i:
        raise SystemExit(f"missing guidebook interpretations: {missing_i}")
    for n in range(1, 14):
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
            f"hco_hrm{n}_v2_draft.json",
            f"HCO.HRM.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"HRM.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
