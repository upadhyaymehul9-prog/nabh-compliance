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

CHAPTER_INTENT = (
    "The standards guide the provision of a safe and secure environment for patients, "
    "their families, staff and visitors. The organisation attends to the facility, "
    "equipment, and internal physical environment for improving patient safety and "
    "quality of services by consistently addressing issues that may arise out of the "
    "same. The organisation does this through proactive risk analysis, safety rounds, "
    "training of staff on the enhancement of safety and management of disasters. To "
    "ensure this, the organisation conducts regular facility inspection rounds and "
    "takes the appropriate action to ensure safety. The organisation provides for "
    "safe water, electricity, medical gases and vacuum systems. The organisation has "
    "a programme for medical and utility equipment management. The organisation plans "
    "for fire and non-fire emergencies within the facilities. The organisation is a "
    "no-smoking area. The organisation safely manages hazardous materials. The "
    "organisation works towards measures on being energy efficient."
)


def clean_text(s: str) -> str:
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = s.replace("\uf001", "fi").replace("\uf002", "fl")
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
        f"{len(items)+1}. Staff who see a FMS.{n} rule broken report it the same shift to the "
        f"{D('Engineering In-Charge')} or the {D('Medical Superintendent')}."
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
            f"Records showing FMS.{n}.{oe['letter']} was followed for sampled cases.",
            "Written guidance / protocol referenced for this element (where required).",
            f"Audit sample notes for FMS.{n}.{oe['letter']} reviewed {D('quarterly')}.",
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

    doc_no = D(f"HCO/FMS/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    letters = f"{oes[0]['letter']}–{oes[-1]['letter']}"
    eng = D("Engineering In-Charge")
    gov_scope = (
        "engineering, biomedical, nursing and departmental leaders, and staff who run "
        "facilities, utilities, medical gases, fire and non-fire emergencies"
    )

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard FMS.{n}: {std_title}

It covers objective elements FMS.{n}.{letters} ({len(oes)} elements).

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

This policy owns FMS.{n}. Related AAC, COP, MOM, PRE, IPC, PSQ and ROM duties stay with those policies — cross-reference only. Other FMS standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to {gov_scope} at {HOSPITAL}, including the {prepared}, the {D('Medical Superintendent')}, departmental leaders and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

Boundaries: do not copy SHCO equivalent-chapter wording. Do not overwrite HCO AAC, COP, MOM, PRE, IPC, PSQ or ROM policies. Spell out abbreviations on first use in training materials. OE counts/levels/asterisks stay with the official portal Standards PDF. Method notes come from the Guidebook Interpretation paragraphs (scanned PDF md5 {GUIDEBOOK_MD5})."""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "facility management and safety requirements are implemented"
    policy_statement = f"""{HOSPITAL} implements FMS.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work conditions are met (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that FMS.{n} is resourced and followed.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Quality Coordinator
- Audits this policy {D('quarterly')}; holds training acknowledgements.

departmental leaders
- Run the department-level duties this standard names."""

    monitoring = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sample of records for each OE FMS.{n}.{letters}.
- Asterisked elements ({stars}) have document evidence as required.
- CORE elements ({cores}) show no critical gaps in the sample.
- Stop-work events (if any) are logged with outcome.

This policy is reviewed {D('annually')}, and sooner after a related facility change, utility failure, equipment recall or fire-plan change."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Facility Management and Safety, standard FMS.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — FMS.{n} interpretations (source PDF md5 {GUIDEBOOK_MD5}; OCR policies/source/hco6_fms_guidebook_ocr.txt).
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
Do not copy SHCO equivalent-chapter wording. Do not touch AAC, COP, MOM, PRE, IPC, PSQ or ROM."""

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
                "description": f"HCO Full 6th Edition FMS.{n} v2 draft: portal PDF OE data + Guidebook interpretations (md5 {GUIDEBOOK_MD5}); draft_label={DRAFT_LABEL}.",
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
        "subtitle": f"{PROGRAMME} — FMS.{n}.",
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
