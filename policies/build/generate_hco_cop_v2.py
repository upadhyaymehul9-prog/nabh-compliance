# -*- coding: utf-8 -*-
"""Generate HCO Full COP.1–COP.20 v2 builders and drafts from official inventory + OCR.

Usage (from policies/build):
  python3 generate_hco_cop_v2.py

Does not touch AAC or SHCO. Always sets explicit HCO draft_label via
hco_cop_v2_common.hco_document_control (no \"not an approved master\" leftover).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))

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
    hco_document_control,
    stop_work_text,
)
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
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
    if len(t) > 72:
        t = t[:69] + "..."
    return f"5.{i} {t}"


def build_steps(n: int, oes: list[dict], interps: list[str]) -> list[str]:
    steps = []
    for i, oe in enumerate(oes, start=1):
        title = step_title(i, oe["text"] or oe["oe_code"])
        body = clean_text(oe["text"] or "")
        extra = ""
        if oe.get("star") and i - 1 < len(interps) and interps[i - 1]:
            # Tier-1: weave a short interpretation-derived method note
            note = interps[i - 1]
            if len(note) > 420:
                note = note[:417] + "..."
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
        if len(short) > 110:
            short = short[:107] + "..."
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


def oe_mapping(n: int, oes: list[dict], has_stop: bool) -> list[dict]:
    mapping = []
    for i, oe in enumerate(oes, start=1):
        short = clean_text(oe["text"] or "")
        steps = f"Section 3; 5.{i}"
        if has_stop and n in STOP_WORK_PROPOSALS and i <= 3:
            steps += "; Section 6 Stop-work"
        records = [
            f"Records showing COP.{n}.{oe['letter']} was followed for sampled patients/cases.",
            "Written guidance / protocol referenced for this element (where required).",
            f"Audit sample notes for COP.{n}.{oe['letter']} reviewed {D('quarterly')}.",
        ]
        if oe.get("star"):
            records.append("Documented evidence specifically required by the asterisked interpretation.")
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

Boundaries: do not copy SHCO COP wording. Do not overwrite AAC policies. Spell out abbreviations on first use in training materials."""

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

    monitoring = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sample of records for each OE COP.{n}.{oes[0]['letter']}–{oes[-1]['letter']}.
- Asterisked elements ({stars}) have document evidence as required.
- CORE elements ({cores}) show no critical gaps in the sample.
- Stop-work events (if any) are logged with outcome.

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
Do not copy SHCO COP wording. Do not touch AAC."""

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
        "distribution": f"Medical Superintendent; {PREPARED_BY[n]}; Quality Coordinator; department clinical staff covered by COP.{n}.",
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
        )
        print(f"COP.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
