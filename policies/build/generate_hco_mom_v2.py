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
BUILD = Path(__file__).resolve().parent

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
    if len(t) > 72:
        t = t[:69] + "..."
    return f"5.{i} {t}"


def build_steps(n: int, oes: list[dict], bodies: dict[str, str]) -> list[str]:
    steps = []
    for i, oe in enumerate(oes, start=1):
        title = step_title(i, oe["text"] or oe["oe_code"])
        body = bodies.get(oe["oe_code"])
        if not body:
            raise KeyError(f"Missing method body for {oe['oe_code']}")
        extras = []
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
        f"{len(items)+1}. Staff who see a MOM.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Medication Safety Officer')}."
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
            f"Records showing MOM.{n}.{oe['letter']} was followed for sampled patients/cases.",
            "Written guidance / protocol referenced for this element (where required).",
            f"Audit sample notes for MOM.{n}.{oe['letter']} reviewed {D('quarterly')}.",
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


def build_one(n: int, inv: dict, bodies: dict[str, str]) -> tuple:
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
    steps = build_steps(n, oes, bodies)
    oe_codes = [o["oe_code"] for o in oes]
    letters = f"{oes[0]['letter']}–{oes[-1]['letter']}"

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard MOM.{n}: {std_title}

It covers objective elements MOM.{n}.{letters} ({len(oes)} elements).

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

This policy owns MOM.{n}. Related AAC, COP, PRE, IPC/HIC and HRM duties stay with those policies — cross-reference only. Other MOM standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to staff who prescribe, dispense, administer, store, monitor or oversee medications (or, for MOM.10–11, implants / medical devices / medical supplies) at {HOSPITAL}, including the {prepared}, pharmacy, nursing, treating doctors and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

Boundaries: do not copy SHCO MOM wording. Do not overwrite HCO AAC or COP policies. Spell out abbreviations on first use in training materials. Guidebook Interpretation paragraphs were not available for MOM in this drafting environment — methods follow official OE text and chapter intent."""

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

    monitoring = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sample of records for each OE MOM.{n}.{letters}.
- Asterisked elements ({stars}) have document evidence as required.
- CORE elements ({cores}) show no critical gaps in the sample.
- Stop-work events (if any) are logged with outcome.

This policy is reviewed {D('annually')}, and sooner after a related adverse event or recall."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Management of Medication, standard MOM.{n}. Official portal PDF.
- Internal documents of {HOSPITAL}: written guidance, formulary, high-risk and emergency-medication lists, registers and incident forms named for MOM.{n}."""

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
Stop-work: {"YES — JUDGMENT CALL: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/MOM/POL/{n:02d}.
Official chapter is 11 standards / 68 OEs — not the SHCO 9-standard MOM set. Guidebook Interpretation paragraphs not available; methods from OE text + chapter intent.
Do not copy SHCO MOM wording. Do not touch AAC or COP."""

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
                "description": f"HCO Full 6th Edition MOM.{n} v2 draft from official Standards PDF OE text + chapter intent; draft_label={DRAFT_LABEL}.",
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
    draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, bodies)
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
    expected = [oe["oe_code"] for n in range(1, 12) for oe in inv[str(n)]["oes"]]
    missing = [c for c in expected if c not in bodies]
    extra = [c for c in bodies if c not in expected]
    if missing or extra:
        raise SystemExit(f"method body mismatch missing={missing} extra={extra}")
    for n in range(1, 12):
        write_builder(n)
        draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, bodies)
        assert "not an approved master" not in draft["resources_required"]
        assert "not an approved master" not in json.dumps(draft)
        assert DRAFT_LABEL in draft["resources_required"]
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
