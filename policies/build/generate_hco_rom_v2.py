# -*- coding: utf-8 -*-
"""Generate HCO Full ROM.1–ROM.6 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_rom_v2.py

Official portal PDF has 6 ROM standards / 37 OEs. All 6 are drafted.
Does not touch AAC, COP, MOM, PRE, IPC, PSQ, or SHCO. Always sets explicit HCO
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
from hco_cop_v2_common import hco_boundaries_clause, truncate_word_safe  # noqa: E402
from hco_rom_v2_common import (  # noqa: E402
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
from hco_rom_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_rom_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_rom_interpretations.json"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 only where Guidebook names a statute. Proposed default: none.
STATUTE_BY_STD: dict[int, str | None] = {}

PREPARED_BY: dict[int, str] = {
    1: "Medical Superintendent",
    2: "Medical Superintendent",
    3: "Medical Superintendent",
    4: "Medical Superintendent",
    5: "Quality Coordinator",
    6: "Medical Superintendent",
}

POLICY_TITLES: dict[int, str] = {
    1: "Those Responsible for Governance",
    2: "Ethical Management of the Organisation",
    3: "Sustainability, Social Responsibility and Staff Well-being",
    4: "Day-to-Day Leadership of the Organisation",
    5: "Professional Functioning of the Organisation",
    6: "Patient Safety, Risk Management and Outsourced Services",
}

CHAPTER_INTENT = (
    "The management of the healthcare organisation is aware of and manages all "
    "the key components of governance. Those responsible for governance are "
    "identified and their roles defined. The standards encourage the governance "
    "of the organisation professionally and ethically. Clinical governance "
    "framework is established, that includes clinical audits, clinical pathways, "
    "education and research. The responsibilities of management are defined. The "
    "responsibilities of the leaders at all levels are defined. The management "
    "executes its responsibility for compliance with all applicable regulations. "
    "Those responsible for governance address the organisations social "
    "responsibility. Leaders ensure that patient-safety and risk-management "
    "issues are an integral part of patient care and hospital management. The "
    "Organisation has a written guidance in place for change management and "
    "service continuity plan."
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
        f"{len(items)+1}. Staff who see a ROM.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Medical Superintendent')}."
    )
    return "\n".join(items)


# Fix #5 pilot chapter — hand-authored per-OE evidence records, matching the
# quality bar AAC.1 and SHCO HIC.1 already demonstrate: concrete, subject-
# specific documents a hospital would actually hold, not a generic template
# restating the OE code. See policies/build/generate_hco_rom_v2.py review
# notes / handoff for the before/after sample used to approve this approach
# before it is repeated for the remaining 7 chapters.
ROM_RECORDS: dict[str, list[str]] = {
    "ROM.1.a": [
        "Named list of those responsible for governance, with each member's role and responsibility documented.",
        "Governance resolution or minute formally identifying the list.",
        "Dated record of the last review or update of the list.",
    ],
    "ROM.1.b": [
        "Governance-approved vision, mission and values statement, with approval date.",
        "Evidence of public display — photograph or location log, website page, or induction-pack copy.",
        "Record of when the statement was last reviewed or reaffirmed.",
    ],
    "ROM.1.c": [
        "Governance minutes approving the strategic plan, operational plan and annual budget before the cycle starts.",
        "The approved strategic plan, operational plan and budget documents themselves.",
        "Dated resolution or sign-off evidencing approval, not just circulation.",
    ],
    "ROM.1.d": [
        "Quarterly performance dashboard pack presented to governance.",
        "Governance minutes recording what was reviewed and any decision taken.",
        "Annual performance-review report measured against the stated mission.",
    ],
    "ROM.1.e": [
        "Appointment letters for senior leaders, including the person heading the organisation, with dates.",
        "Governance minutes recording the appointment decision.",
        "Current reporting-line document naming who each senior leader reports to.",
    ],
    "ROM.1.f": [
        "Governance minutes showing safety, clinical-governance or quality-improvement reports were received.",
        "Budget line or resource allocation record supporting those initiatives.",
        "Decisions recorded in minutes in response to those reports.",
    ],
    "ROM.1.g": [
        "The written clinical-governance framework document (clinical audit, clinical pathways, education, research).",
        "Dated approval record naming who owns the framework.",
        "Evidence of periodic review or update of the framework.",
    ],
    "ROM.1.h": [
        "Governance minutes showing an ethics issue was escalated to and considered by governance.",
        "Resource allocation record supporting the ethical-management framework.",
        "Decisions recorded on ethics matters raised.",
    ],
    "ROM.1.i": [
        "Published quality/performance indicators, accreditation status, or the defined public-information set.",
        "Dated samples of what was published (display photograph, website snapshot, or notice).",
        "Record of the feedback channel offered to the public and how it is publicised.",
    ],
    "ROM.2.a": [
        "The written ethical-management framework: principles, decision authority and escalation path.",
        "Dated approval record naming who owns the framework.",
        "Evidence the framework is a standing document, not minutes-only notes.",
    ],
    "ROM.2.b": [
        "Named escalation path and timeline for handling an ethical issue, dilemma or concern.",
        "Log of ethical issues raised, with resolution and date.",
        "At least one example case record showing the process was actually used.",
    ],
    "ROM.2.c": [
        "Current ownership-disclosure text.",
        "Evidence of public display — reception, website, or the statutory board where applicable.",
        "Annual check or update record for the disclosure.",
    ],
    "ROM.2.d": [
        "Current list of affiliations and accreditations shown in public materials.",
        "Quarterly review record confirming no expired or applied-for status is shown as awarded.",
        "Correction record for any instance found and fixed.",
    ],
    "ROM.3.a": [
        "Written ESG (Environment, Social and Governance) sustainability programme with a named owner.",
        "Governance-meeting agenda or minutes tabling the programme.",
        "Annual review record of the programme.",
    ],
    "ROM.3.b": [
        "Dated log of energy-efficiency and environmental initiatives and their results.",
        "Cross-reference to the ESG/engineering file (FMS owns the engineering controls; this is the initiative record).",
        "Before/after data or savings evidence where available.",
    ],
    "ROM.3.c": [
        "Documented social-responsibility programme (community access, charity care, local health initiatives).",
        "Annual activity report for the programme.",
        "Governance minutes noting the programme.",
    ],
    "ROM.3.d": [
        "Documented work-hour monitoring method for staff.",
        "Record of healthy-lifestyle support and scheduled-break arrangements.",
        "Record of the channel for raising workload concerns and any concerns logged through it.",
    ],
    "ROM.3.e": [
        "Purchase policy naming environmental and social tender criteria.",
        "Completed procurement file showing those criteria were applied.",
        "At least one tender evaluation reflecting the sustainable-procurement criteria.",
    ],
    "ROM.3.f": [
        "Current staff communication promoting common or public transport for commuting.",
        "Documentation of any incentive scheme offered.",
        "Record that the offer was communicated to staff (not that every staff member complied).",
    ],
    "ROM.3.g": [
        "Budget-versus-actual review document.",
        "Record of cash and credit discipline for the period.",
        "Annual financial-sustainability view tabled to governance.",
    ],
    "ROM.4.a": [
        "Qualification certificates and CV of the person heading the organisation, on file.",
        "Governance record confirming the qualification/experience check at appointment.",
        "Updated record if the role-holder changes.",
    ],
    "ROM.4.b": [
        "Current applicable-legislation register for this hospital's legal form and services actually run.",
        "Evidence of compliance against each item on the register.",
        "Dated review or update record of the register.",
    ],
    "ROM.4.c": [
        "Appointment file for each department leader showing the organisation-head's role in the decision.",
        "Current list of department leaders with appointment dates.",
        "Escalation record for any department without an identified leader.",
    ],
    "ROM.4.d": [
        "Leadership map naming a person, time allocation and reporting line for each programme, service, site or department.",
        "Vacancy-coverage record for any gap.",
        "Dated review of the leadership map.",
    ],
    "ROM.4.e": [
        "Dated annual performance-review record for the organisation's leader.",
        "Review criteria or method used.",
        "Filed outcome and any follow-up action.",
    ],
    "ROM.5.a": [
        "Strategic and operational plan documents naming owners and timeframes.",
        "Stakeholder-consultation record for plan development.",
        "Current approved plan set held by the Quality Coordinator and Medical Superintendent.",
    ],
    "ROM.5.b": [
        "Coordination minutes with departments and external agencies.",
        "Progress-tracking report against defined goals and objectives.",
        "Corrective-action record where progress lagged.",
    ],
    "ROM.5.c": [
        "Annual operational plan linked to the strategic plan.",
        "Annual budget document.",
        "Governance approval record for the plan and budget (cross-reference ROM.1.c).",
    ],
    "ROM.5.d": [
        "Committee list with defined meeting frequency.",
        "Effectiveness-review report — whether each committee met, decided and closed actions.",
        "Action-item closure log.",
    ],
    "ROM.5.e": [
        "Documented measurable service-standard set (the measure and review interval) for selected services.",
        "Monitoring results log against each standard.",
        "Review record showing the standards were actually checked.",
    ],
    "ROM.5.f": [
        "Written change-management guidance: approval authority, staff communication method, continuity method.",
        "A completed change record following that guidance.",
        "Service-continuity evidence for a change actually made.",
    ],
    "ROM.6.a": [
        "Risk-management system document.",
        "Risk register showing identified clinical and organisational risks (for example falls, infection, vulnerable-patient risks such as DVT, clinical alarms).",
        "Assessment, action and review log for a sample of risks on the register.",
    ],
    "ROM.6.b": [
        "Budget or resource-allocation record for risk-assessment and risk-reduction activity.",
        "Training record for staff involved in risk activities.",
        "Contingency-allocation evidence for preventive action.",
    ],
    "ROM.6.c": [
        "Quality Improvement Committee minutes showing risk findings feeding the plan.",
        "Strategic plan referencing risk-management and quality work.",
        "Governance pack showing the link between risk, quality and planning.",
    ],
    "ROM.6.d": [
        "Reporting-system document naming what is reported, to whom internally, and to which external agency, with timelines.",
        "Sampled internal and external failure reports (for example equipment breakdown, an external-agency notification such as AERB for a radiation-source event).",
        "Tested service-continuity plan covering fire and non-fire emergencies for critical operations.",
    ],
    "ROM.6.e": [
        "Signed agreement for each outsourced service naming service parameters (quality, numbers, reports, timelines) and dispute-resolution method.",
        "Current list of outsourced services.",
        "Evidence any affiliate or group-firm arrangement also has an agreement on file.",
    ],
    "ROM.6.f": [
        "Periodic quality-monitoring review per outsourced service, at a frequency matched to how critical that service is.",
        "Vendor improvement-action record where a gap was found.",
        "Documented exemption record for any service outsourced solely under prescribed statutory norms (where the Guidebook does not require monitoring).",
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
        records = ROM_RECORDS.get(oe["oe_code"])
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

    doc_no = D(f"HCO/ROM/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    letters = f"{oes[0]['letter']}–{oes[-1]['letter']}"
    gov = D("those responsible for governance")
    gov_scope = (
        "those responsible for governance, the person heading the organisation, "
        "departmental leaders, and staff who run ethics, sustainability, risk or outsourcing"
    )

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard ROM.{n}: {std_title}

It covers objective elements ROM.{n}.{letters} ({len(oes)} elements).

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

This policy owns ROM.{n}. Related AAC, COP, MOM, PRE, IPC and PSQ duties stay with those policies — cross-reference only. Other ROM standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to {gov_scope} at {HOSPITAL}, including the {prepared}, {gov} as identified under ROM.1, departmental leaders and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

{hco_boundaries_clause(["AAC", "COP", "MOM", "PRE", "IPC", "PSQ"])} Spell out abbreviations on first use in training materials. OE counts/levels/asterisks stay with the official portal Standards PDF. Method notes come from the Guidebook Interpretation paragraphs (scanned PDF md5 {GUIDEBOOK_MD5})."""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "responsibilities of management are implemented"
    policy_statement = f"""{HOSPITAL} implements ROM.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work triggers fire (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that ROM.{n} is resourced and followed.
- Acts as the person heading the organisation unless {gov} have appointed another leader.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

those responsible for governance
- Hold the duties ROM.1 assigns to the governing entity.

Quality Coordinator
- Audits this policy {D('quarterly')}; holds training acknowledgements; supports dashboards and committee reviews as this standard requires.

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

This policy is reviewed {D('annually')}, and sooner after a related governance change, statutory-register gap or outsourced-service failure."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Responsibilities of Management, standard ROM.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — ROM.{n} interpretations (source PDF md5 {GUIDEBOOK_MD5}; OCR policies/source/hco6_rom_guidebook_ocr.txt).
- Internal documents of {HOSPITAL}: governance role document, ethical-management framework, ESG / social-responsibility programme, applicable-legislation register, risk-management plan, outsourcing agreements named for ROM.{n}."""

    abbreviations = f"""AERB — Atomic Energy Regulatory Board
CAPA — Corrective and Preventive Action
CORE — Core objective element (NABH)
ESG — Environment, Social and Governance
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — Objective Element
ROM — Responsibilities of Management (NABH Hospitals 6th Edition chapter)
SWOT — Strengths, Weaknesses, Opportunities and Threats"""

    ufg = f"""HCO ROM.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (matrix agrees on levels). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — proposed: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (proposed default: no stop-work on this standard)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/ROM/POL/{n:02d}.
Official chapter is 6 standards / 37 OEs (confirmed against portal summary). Guidebook interpretations from scanned PDF md5 {GUIDEBOOK_MD5}. No statute P2 proposed (accreditation-only); ROM.4.b legislations and ROM.6.d AERB example stay in method notes.
Do not touch AAC, COP, MOM, PRE, IPC or PSQ."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "those responsible for governance",
            "Quality Coordinator",
            "departmental leaders",
            f"staff covered by ROM.{n}",
        ]
    )

    draft = {
        "standard_code": f"ROM.{n}",
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
                "description": f"HCO Full 6th Edition ROM.{n} v2 draft: portal PDF OE data + Guidebook interpretations (md5 {GUIDEBOOK_MD5}); draft_label={DRAFT_LABEL}.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_rom_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — ROM.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.ROM.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_rom{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO ROM.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_rom_v2.py
Explicit draft_label via hco_rom_v2_common.hco_document_control.
Does NOT overwrite SHCO, HCO AAC, HCO COP, HCO MOM, HCO PRE, HCO IPC or HCO PSQ files.
"""
from __future__ import annotations

import sys
from generate_hco_rom_v2 import emit_standard

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
        f"hco_rom{n}_v2_draft.json",
        f"HCO.ROM.{n}_v2_preview.md",
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
    total = sum(inv[str(n)]["count"] for n in range(1, 7))
    assert total == 37, total
    bodies = method_bodies(D=D, HOSPITAL=HOSPITAL, BLANK=BLANK)
    interps = load_interpretations()
    expected = [oe["oe_code"] for n in range(1, 7) for oe in inv[str(n)]["oes"]]
    missing = [c for c in expected if c not in bodies]
    extra = [c for c in bodies if c not in expected]
    if missing or extra:
        raise SystemExit(f"method body mismatch missing={missing} extra={extra}")
    missing_i = [c for c in expected if not (interps.get(c) or "").strip()]
    if missing_i:
        raise SystemExit(f"missing guidebook interpretations: {missing_i}")
    for n in range(1, 7):
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
            f"hco_rom{n}_v2_draft.json",
            f"HCO.ROM.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"ROM.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
