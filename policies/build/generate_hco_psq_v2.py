# -*- coding: utf-8 -*-
"""Generate HCO Full PSQ.1–PSQ.7 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_psq_v2.py

Official portal PDF has 7 PSQ standards / 46 OEs. All 7 are drafted.
Does not touch AAC, COP, MOM, PRE, IPC, or SHCO. Always sets explicit HCO
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
    hco_oe_count_clause,
    hco_related_duties_clause,
    truncate_word_safe,
)
from hco_psq_v2_common import (  # noqa: E402
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
from hco_psq_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_psq_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_psq_interpretations.json"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 only where Guidebook names a statute. Proposed default: none.
STATUTE_BY_STD: dict[int, str | None] = {}

PREPARED_BY: dict[int, str] = {
    1: "Patient Safety Officer",
    2: "Quality Coordinator",
    3: "Quality Coordinator",
    4: "Quality Coordinator",
    5: "Quality Coordinator",
    6: "Medical Superintendent",
    7: "Patient Safety Officer",
}

POLICY_TITLES: dict[int, str] = {
    1: "Patient Safety Programme",
    2: "Quality Improvement and Continuous Monitoring Programme",
    3: "Key Indicators for Continual Improvement",
    4: "Quality Improvement Tools and Projects",
    5: "Clinical Audit",
    6: "Management Support for Patient Safety and Quality",
    7: "Incident Collection and Analysis",
}

CHAPTER_INTENT = (
    "The standards encourage an environment of patient safety and continual "
    "quality improvement. The patient safety and quality programme should be "
    "documented and involve all areas of the organisation and all staff members. "
    "The management creates a culture of safety in the organisation. Patient "
    "safety officer(s) shall be designated for the implementation of "
    "patient-safety programme. National / International patient-safety goals / "
    "solutions / framework shall be implemented. The organisation shall collect "
    "data on structures, processes and outcomes, especially in areas of "
    "high-risk situations. Quality indicators specific to clinical specialities "
    "shall be used to involve clinical departments in the quality improvement "
    "programme. The collected data shall be collated, analysed and trends are "
    "used for further improvement. Appropriate quality tools shall be used for "
    "carrying out quality improvement projects. Clinical audits shall be used as "
    "a tool to improve the quality of patient care in a sustained manner. "
    "Department leaders play an active role in patient safety and quality "
    "improvement. The organisation has a mechanism to capture patient reported "
    "outcome measures. The organisation shall have a robust incident reporting "
    "system. Sentinel events shall be defined. All incidents are investigated "
    "and appropriate action is taken. The management shall support the patient "
    "safety and quality programme."
)


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
        f"{len(items)+1}. Staff who see a PSQ.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Patient Safety Officer')} / {D('Quality Coordinator')}."
    )
    return "\n".join(items)


# Fix #5 — hand-authored per-OE evidence records, matching the quality bar
# AAC.1 / SHCO HIC.1 / HCO ROM / HCO FMS already demonstrate.
PSQ_RECORDS: dict[str, list[str]] = {
    "PSQ.1.a": [
        "Documented patient safety programme in the Patient Safety Manual.",
        "Patient Safety Committee terms of reference, membership list and meeting-frequency record.",
        "Minutes showing the committee actually developed and maintains the programme, not minutes-only notes.",
    ],
    "PSQ.1.b": [
        "Current element list in the manual (identification, communication, medication safety, procedure safety, falls/high-risk care, infection-related safety, incident reporting).",
        "Training record for staff working in those areas.",
        "Cross-reference record to IPC for the infection-related-safety element.",
    ],
    "PSQ.1.c": [
        "Written definitions of no-harm event, near miss, adverse event and sentinel event in the manual.",
        "Incident-system report samples showing each defined class was actually reported.",
        "Confirmation the programme is not limited to death or major-harm events only.",
    ],
    "PSQ.1.d": [
        "Designation letter for the Patient Safety Officer(s) with time allocation and reporting line.",
        "Written role description for the position.",
        "List of named patient-safety champions across departments.",
    ],
    "PSQ.1.e": [
        "Completed proactive risk-analysis file for at least one patient-safety risk in the year (for example HIRA, FMEA, HVA or fault-tree analysis).",
        "Improvement actions from that analysis with owner and due date.",
        "Quality Coordinator's analysis-file record.",
    ],
    "PSQ.1.f": [
        "Dated review minute of the patient safety programme.",
        "Record of the change made to the manual or element list at that review.",
        "Evidence of an earlier review after a sentinel event, new service, or national-goal change, where applicable.",
    ],
    "PSQ.1.g": [
        "Current adopted list of national/international patient-safety goals or solutions (for example the National Patient Safety Framework, WHO Patient Safety Solutions, International Patient Safety Goals).",
        "Local-adaptation record showing how each goal is implemented for this hospital's scope.",
        "Measurement record for each adopted goal.",
    ],
    "PSQ.2.a": [
        "Documented quality improvement programme in the Quality Manual.",
        "Quality Improvement Committee terms of reference, membership list and meeting-frequency record.",
        "Minutes showing the committee actually developed and maintains the programme.",
    ],
    "PSQ.2.b": [
        "Current element list (indicator monitoring, QI projects and tools, clinical audit, incident learning, department-level review).",
        "Record confirming each element has its own active file.",
        "Review record confirming the list stays comprehensive at each update.",
    ],
    "PSQ.2.c": [
        "Completed QI project file with aim, measure and before/after result focused on process efficiency.",
        "Record of the process improved (time, waste, reliability of a defined process).",
        "Quality Coordinator's project-outcome file.",
    ],
    "PSQ.2.d": [
        "Completed QI project file focused on appropriateness of clinical care (indicated care, protocol variation).",
        "Topic-selection record showing the source — clinical indicator, audit or incident.",
        "Results-communication record to the clinical department.",
    ],
    "PSQ.2.e": [
        "Designation letter for the QI coordinator with time allocation and reporting line to top management.",
        "Training-completion record (for example the NABH Programme on Implementation of NABH Standards).",
        "List of named quality-improvement champions across departments.",
    ],
    "PSQ.2.f": [
        "Quality Improvement Committee review minutes at least once in three months.",
        "List of identified improvement opportunities with owner and next step.",
        "Record showing audits, organisational performance and key indicators were part of that review.",
    ],
    "PSQ.2.g": [
        "Dated review minute of the QI programme.",
        "Record of the change made to the manual, indicator set or audit calendar.",
        "Trigger record for any earlier review after a major service change or a cluster of failed audits.",
    ],
    "PSQ.2.h": [
        "Audit calendar covering priority areas and areas of concern from indicators or risk.",
        "Hospital-wide internal audit report completed at least once in six months, by trained multi-disciplinary staff.",
        "CAPA and verification-of-change record for the audit findings.",
    ],
    "PSQ.2.i": [
        "Written nursing-audit and/or competency-evaluation process for key procedures.",
        "Nursing quality-indicator set and results.",
        "Nursing Superintendent's record showing integration with the quality improvement programme.",
    ],
    "PSQ.3.a": [
        "Current clinical-indicator set with numerator, denominator and multiplier defined.",
        "Record confirming any Government of India, State Government or NABH-mandated indicator is included.",
        "Quality Improvement Committee presentation record at the defined interval.",
    ],
    "PSQ.3.b": [
        "Current infection-prevention-and-control indicator set (for example CAUTI, CLABSI, SSI, VAP as applicable) following CDC NHSN definitions.",
        "Mandated-indicator inclusion record.",
        "Joint review record between the Quality Improvement Committee and the infection committee.",
    ],
    "PSQ.3.c": [
        "Current managerial-indicator set with numerator, denominator and multiplier defined.",
        "Mandated-indicator inclusion record, including digital-health indicators where applicable.",
        "Results record shared with the relevant departmental leader.",
    ],
    "PSQ.3.d": [
        "Current patient-safety-indicator set (safety goals, risk management) with numerator, denominator and multiplier defined.",
        "Mandated-indicator inclusion record.",
        "Quality Improvement Committee review record of results.",
    ],
    "PSQ.3.e": [
        "Monthly sample-check record of source data versus the reported figure.",
        "Quarterly deeper-verification record of a rotating indicator subset.",
        "Record confirming unverified data were not used on dashboards or management targets.",
    ],
    "PSQ.3.f": [
        "Written analysis mechanism (trend, target, outlier or comparison as defined).",
        "Quality Improvement Committee minutes recording the analysis.",
        "Record of each identified opportunity, or a documented \"no action needed\" conclusion.",
    ],
    "PSQ.3.g": [
        "Action-tracking log from indicator analysis through to closure.",
        "Later evaluation record confirming the measure moved as intended.",
        "Quality Coordinator's tracking file.",
    ],
    "PSQ.3.h": [
        "Sample of shared feedback materials (dashboard, huddle notes, meeting minutes) with dates.",
        "Record of the channel used — department meeting, huddle or dashboard.",
        "Confirmation feedback reached staff level, not only committee minutes.",
    ],
    "PSQ.4.a": [
        "Live quality-improvement project register with aim, owner, start date and status.",
        "Evidence of at least two quality-improvement projects undertaken in the year.",
        "Before/after measurement record for each project.",
    ],
    "PSQ.4.b": [
        "Project register tagged against the six quality domains (patient safety, cost-effectiveness, patient-centredness, timeliness, efficiency, equity).",
        "Completed-project evidence covering those domains over the review period.",
        "Cost or efficiency impact record where applicable.",
    ],
    "PSQ.4.c": [
        "Project file showing the analytical, managerial or statistical tool used (for example PDCA, run chart, Pareto, fishbone, 5-Why).",
        "Record of what the tool's output showed.",
        "Confirmation the project is not a memo without a tool.",
    ],
    "PSQ.4.d": [
        "Written patient-reported-outcome-measure collection method, frequency and defined conditions or pathways.",
        "PROM data-collection record.",
        "Record showing PROM results fed an improvement action.",
    ],
    "PSQ.5.a": [
        "Clinical-audit calendar with at least one audit per clinical department once in two years.",
        "Completed audit report on file.",
        "Topic record — disease-based, cost-based, community-based or morbidity-based.",
    ],
    "PSQ.5.b": [
        "Written pre-audit parameter document: objectives, standards/criteria, sample, period and exclusions.",
        "Sign-off record between the audit lead and the Quality Coordinator.",
        "Record of any audit restarted for missing predefined parameters.",
    ],
    "PSQ.5.c": [
        "Attendance and role record for medical and nursing staff in each audit.",
        "Audit-lead or data-collector assignment record.",
        "Confirmation clinical participation occurred, not a quality-office-only audit.",
    ],
    "PSQ.5.d": [
        "De-identified or coded audit report and presentation.",
        "Key-holder record showing the identifier key is held separately by the Quality Coordinator.",
        "Confirmation open-meeting materials do not name patients or staff.",
    ],
    "PSQ.5.e": [
        "Complete audit pack: protocol/parameters, data, findings, recommendations, attendees and date.",
        "Filed record with the Quality Coordinator.",
        "Confirmation no undocumented verbal audit was treated as complete.",
    ],
    "PSQ.5.f": [
        "Recommendation-tracking log with owner and due date per audit finding.",
        "Later-check record confirming the remedy was actually done.",
        "Quality Improvement Committee open-action review record.",
    ],
    "PSQ.6.a": [
        "Signed safety-culture statement in the patient-safety manual.",
        "Validated safety-culture survey result at least annually (for example MaPSaF, Safety Attitudes Questionnaire, AHRQ SOPS).",
        "Management action record responding to the survey results.",
    ],
    "PSQ.6.b": [
        "Department-head briefing record at induction to the role and annually thereafter.",
        "Acknowledgement or attendance record held by the Quality Coordinator.",
        "Confirmation floor leaders can describe the programme's intent and implementation approach.",
    ],
    "PSQ.6.c": [
        "Committee attendance or named-delegate record for departmental leaders.",
        "Department quality file showing owned indicators or projects.",
        "Team-briefing record from the departmental leader.",
    ],
    "PSQ.6.d": [
        "Signed annual budget line for patient safety and quality (training, audit time, safety equipment, projects, information systems).",
        "Record of any mid-year stock-out of a funded safety item, reported to management.",
        "Budget-utilisation record for the year.",
    ],
    "PSQ.6.e": [
        "Current organisational and department-level performance-improvement target set.",
        "Review record at least once in three months and modification record at least annually.",
        "Record of targets shared with faculty and staff with feedback.",
    ],
    "PSQ.6.f": [
        "Staff-feedback source record (survey, safety-huddle theme log, suggestion scheme).",
        "Minuted record of feedback themes considered.",
        "Record of a programme change resulting from that feedback — the closed loop.",
    ],
    "PSQ.7.a": [
        "Written incident-management guidance covering identification, reporting, review and action.",
        "Reporting-channel record (form or digital) and recipient list.",
        "Sample of captured incidents showing all severities reported, not filtered by harm level.",
    ],
    "PSQ.7.b": [
        "Written sentinel-event definition and hospital-specific examples.",
        "Same-shift flagging record in the incident system for a recognised sentinel event.",
        "Notification record to the Patient Safety Officer and Medical Superintendent.",
    ],
    "PSQ.7.c": [
        "Root-cause-analysis record for a sampled incident, led by the Patient Safety Committee.",
        "Timeliness record for sentinel events — correction within 24 working hours, analysis within 7 working days.",
        "Open-analysis tracking log held by the Patient Safety Officer.",
    ],
    "PSQ.7.d": [
        "CAPA record with owner, due date and effectiveness check.",
        "Communication record to the personnel concerned.",
        "Confirmation no process continued after analysis showed it caused a sentinel event, before controls were in place.",
    ],
    "PSQ.7.e": [
        "Risk-register update record from incident-analysis findings.",
        "Residual-risk and owner assignment.",
        "Cross-reference record between the CAPA and the risk register.",
    ],
    "PSQ.7.f": [
        "Written communication process naming who is told, by whom, and within what time for a near miss, adverse event or sentinel event.",
        "Communication log for sentinel and defined serious events.",
        "Confirmation the process sits beside, not in place of, any statutory notification requirement.",
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
        records = PSQ_RECORDS.get(oe["oe_code"])
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

    doc_no = D(f"HCO/PSQ/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    own_topic = POLICY_TITLES[n].lower()
    related_chapters = ["AAC", "COP", "MOM", "PRE", "IPC"]

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard PSQ.{n}: {std_title}

{hco_oe_count_clause(len(oes))}

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

{hco_related_duties_clause(own_topic, related_chapters)} Other PSQ standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to staff who deliver care, run quality or patient-safety work, lead departments, or hold management duties for safety and quality at {HOSPITAL}, including the {prepared}, the Patient Safety Officer, the Quality Coordinator, departmental leaders, treating doctors, nursing and the Medical Superintendent.

{hco_oe_count_clause(len(oes))}

{hco_related_duties_clause(own_topic, related_chapters)} Spell out abbreviations on first use in training materials. OE counts/levels/asterisks stay with the official portal Standards PDF. Method notes come from the Guidebook Interpretation paragraphs (scanned PDF md5 {GUIDEBOOK_MD5})."""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "patient safety and quality improvement is implemented"
    policy_statement = f"""{HOSPITAL} implements PSQ.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work triggers fire (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that PSQ.{n} is resourced and followed.
- Acts on sentinel events, safety-culture failures and quality-programme gaps that reach top leadership.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Patient Safety Officer
- Coordinates the patient-safety programme and incident/sentinel-event path across standards.

Quality Coordinator
- Coordinates the quality-improvement programme, indicators, audits and projects as this standard requires.
- Audits this policy {D('quarterly')}; holds training acknowledgements.

Nursing Superintendent
- Owns nursing-care quality monitoring where this standard requires it."""

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

This policy is reviewed {D('annually')}, and sooner after a related sentinel event, indicator failure cluster or failed clinical-audit cycle."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Patient Safety and Quality Improvement, standard PSQ.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — PSQ.{n} interpretations (source PDF md5 {GUIDEBOOK_MD5}; OCR policies/source/hco6_psq_guidebook_ocr.txt).
- Internal documents of {HOSPITAL}: Patient Safety Manual, Quality Manual, indicator definitions, clinical-audit calendar, incident and sentinel-event guidance named for PSQ.{n}."""

    abbreviations = f"""CAPA — Corrective and Preventive Action
CORE — Core objective element (NABH)
FMEA — Failure Mode and Effects Analysis
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
IPC — Infection Prevention and Control (NABH Hospitals 6th Edition chapter)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — Objective Element
PDCA — Plan-Do-Check-Act
PROM — Patient-Reported Outcome Measure
PSQ — Patient Safety and Quality Improvement (NABH Hospitals 6th Edition chapter)
WHO — World Health Organization"""

    ufg = f"""HCO PSQ.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (matrix agrees on levels). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — proposed: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (proposed default: no stop-work on this standard)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/PSQ/POL/{n:02d}.
Official chapter is 7 standards / 46 OEs (confirmed against portal summary). Guidebook interpretations from scanned PDF md5 {GUIDEBOOK_MD5}. No statute P2 proposed (accreditation-only).
Do not touch AAC, COP, MOM, PRE or IPC."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "Patient Safety Officer",
            "Quality Coordinator",
            "Nursing Superintendent",
            "departmental leaders",
            f"department clinical and support staff covered by PSQ.{n}",
        ]
    )

    draft = {
        "standard_code": f"PSQ.{n}",
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
                "description": f"HCO Full 6th Edition PSQ.{n} v2 draft: portal PDF OE data + Guidebook interpretations (md5 {GUIDEBOOK_MD5}); draft_label={DRAFT_LABEL}.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_psq_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — PSQ.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.PSQ.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_psq{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO PSQ.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_psq_v2.py
Explicit draft_label via hco_psq_v2_common.hco_document_control.
Does NOT overwrite SHCO, HCO AAC, HCO COP, HCO MOM, HCO PRE or HCO IPC files.
"""
from __future__ import annotations

import sys
from generate_hco_psq_v2 import emit_standard

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
        f"hco_psq{n}_v2_draft.json",
        f"HCO.PSQ.{n}_v2_preview.md",
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
    assert total == 46, total
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
            f"hco_psq{n}_v2_draft.json",
            f"HCO.PSQ.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"PSQ.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
