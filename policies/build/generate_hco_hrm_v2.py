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
    if len(t) > 72:
        t = t[:69] + "..."
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
        if len(short) > 110:
            short = short[:107] + "..."
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


def oe_mapping(n: int, oes: list[dict], has_stop: bool) -> list[dict]:
    mapping = []
    prepared = PREPARED_BY[n]
    for i, oe in enumerate(oes, start=1):
        short = clean_text(oe["text"] or "")
        steps = f"Section 3; 5.{i}"
        if has_stop and n in STOP_WORK_PROPOSALS:
            steps += "; Section 6 Stop-work"
        records = [
            f"Records showing HRM.{n}.{oe['letter']} was followed for sampled cases.",
            "Written guidance / protocol referenced for this element (where required).",
            f"Audit sample notes for HRM.{n}.{oe['letter']} reviewed {D('quarterly')}.",
        ]
        if oe.get("star"):
            records.append("Documented evidence specifically required by the asterisked objective element.")
        if oe["level"] == "CORE":
            records.append("CORE-element sample with no critical gaps in the quarter under review.")
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
    letters = f"{oes[0]['letter']}–{oes[-1]['letter']}"
    hr = D("HR In-Charge / Personnel Officer")
    gov_scope = (
        "human resources, nursing, medical, and departmental leaders, and all staff of "
        f"{HOSPITAL}"
    )

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard HRM.{n}: {std_title}

It covers objective elements HRM.{n}.{letters} ({len(oes)} elements).

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

This policy owns HRM.{n}. Related AAC, COP, MOM, PRE, IPC, PSQ, ROM and FMS duties stay with those policies — cross-reference only. Other HRM standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to {gov_scope}, including the {prepared}, the {D('Medical Superintendent')}, departmental leaders and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

Boundaries: do not copy SHCO equivalent-chapter wording (including the already-deployed SHCO 3rd Edition HRM chapter). Do not overwrite HCO AAC, COP, MOM, PRE, IPC, PSQ, ROM or FMS policies. Spell out abbreviations on first use in training materials. OE counts/levels/asterisks stay with the official portal Standards PDF. Method notes come from the Guidebook Interpretation paragraphs (scanned PDF; no text layer, transcribed and verified against rendered page images — see policies/source/hco6_hrm_chapter_notes.md)."""

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

    monitoring = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sample of records for each OE HRM.{n}.{letters}.
- Asterisked elements ({stars}) have document evidence as required.
- CORE elements ({cores}) show no critical gaps in the sample.
- Stop-work events (if any) are logged with outcome.

This policy is reviewed {D('annually')}, and sooner after a related credentialing, staffing or disciplinary-process change."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Human Resource Management, standard HRM.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.{n} interpretations (source PDF has no text layer; transcribed and verified against rendered page images — policies/source/hco6_hrm_guidebook_ocr.txt).
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
Do not copy SHCO equivalent-chapter wording — including the already-deployed SHCO 3rd Edition HRM chapter (build_hrm1_v2.py..build_hrm9_v2.py, policies/drafts/hrm*_v2_draft.json), a separate programme and edition. Do not touch AAC, COP, MOM, PRE, IPC, PSQ, ROM or FMS."""

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
                "description": f"HCO Full 6th Edition HRM.{n} v2 draft: portal PDF OE data + Guidebook interpretations (verified visual transcription, no text layer in source PDF); draft_label={DRAFT_LABEL}.",
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
