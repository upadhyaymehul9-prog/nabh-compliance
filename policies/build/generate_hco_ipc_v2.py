# -*- coding: utf-8 -*-
"""Generate HCO Full IPC.1–IPC.8 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_ipc_v2.py

Official portal PDF has 8 IPC standards / 49 OEs. All 8 are drafted.
Does not touch AAC, COP, MOM, PRE, or SHCO. Always sets explicit HCO draft_label via
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
from hco_ipc_v2_common import (  # noqa: E402
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
from hco_ipc_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_ipc_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_ipc_interpretations.json"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 proposed where Guidebook names statutory BMW handling. Default: IPC.4.
STATUTE_BY_STD: dict[int, str | None] = {
    4: (
        "statutory provisions for biomedical waste handling as named in NABH IPC.4, "
        "including colour-coded segregation, storage, authorised vendor and monitoring "
        "as required under applicable Biomedical Waste Management Rules"
    ),
}

PREPARED_BY: dict[int, str] = {
    1: "Infection Prevention and Control Officer",
    2: "Medical Superintendent",
    3: "Infection Prevention and Control Officer",
    4: "Infection Prevention and Control Officer",
    5: "Infection Prevention and Control Officer",
    6: "Infection Prevention and Control Officer",
    7: "CSSD In-Charge",
    8: "Occupational Health Physician",
}

POLICY_TITLES: dict[int, str] = {
    1: "Infection Prevention and Control Programme",
    2: "Resources for Infection Prevention and Control",
    3: "Infection Prevention and Control in Clinical Areas",
    4: "Infection Prevention and Control in Support Services",
    5: "Prevention of Healthcare Associated Infections in Patients",
    6: "Infection Prevention and Control Surveillance",
    7: "Sterilisation and Disinfection of Instruments, Equipment and Devices",
    8: "Prevention of Healthcare Associated Infections in Staff",
}

CHAPTER_INTENT = (
    "The organisation implements an effective healthcare associated infection "
    "prevention and control programme. The programme is documented and aims at "
    "reducing / eliminating infection risks to patients, visitors and providers of "
    "care. The programme is implemented across the organisation, including clinical "
    "areas and support services. The organisation provides proper facilities and "
    "adequate resources to support the infection prevention and control programme. "
    "The organisation measures and acts to prevent or reduce the risk of healthcare "
    "associated infection in patients and staff. The organisation has an effective "
    "antimicrobial management programme through regularly updated antimicrobial "
    "policy based on local data and monitors its implementation. Programme also "
    "includes monitoring of antimicrobials usage in the organisation. Surveillance "
    "activities are incorporated in the infection prevention and control programme. "
    "The programme includes disinfection / sterilisation activities and biomedical "
    "waste (BMW) management."
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
        f"{len(items)+1}. Staff who see an IPC.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Infection Prevention and Control Officer')}."
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
            f"Records showing IPC.{n}.{oe['letter']} was followed for sampled patients/cases.",
            "Written guidance / protocol referenced for this element (where required).",
            f"Audit sample notes for IPC.{n}.{oe['letter']} reviewed {D('quarterly')}.",
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

    doc_no = D(f"HCO/IPC/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    letters = f"{oes[0]['letter']}–{oes[-1]['letter']}"

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard IPC.{n}: {std_title}

It covers objective elements IPC.{n}.{letters} ({len(oes)} elements).

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

This policy owns IPC.{n}. Related AAC, COP, MOM and PRE duties stay with those policies — cross-reference only. Other IPC standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to staff who deliver clinical care, run support services (housekeeping, laundry, kitchen, CSSD, engineering), handle biomedical waste, or hold occupational-health duties at {HOSPITAL}, including the {prepared}, the Infection Prevention and Control Officer and Nurse, treating doctors, nursing, CSSD, Occupational Health and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

Boundaries: do not copy SHCO equivalent-chapter wording. Do not overwrite HCO AAC, COP, MOM or PRE policies. Spell out abbreviations on first use in training materials. OE counts/levels/asterisks stay with the official portal Standards PDF. Method notes come from the Guidebook Interpretation paragraphs (scanned PDF md5 {GUIDEBOOK_MD5})."""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "infection prevention and control is implemented"
    policy_statement = f"""{HOSPITAL} implements IPC.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work triggers fire (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that IPC.{n} is resourced and followed.
- Acts on outbreaks, sterilisation recalls and exposure events that reach top leadership.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Infection Prevention and Control Officer
- Coordinates the IPC programme across standards; brings surveillance and incidents to the Infection Prevention and Control Committee.

Infection Prevention and Control Nurse
- Runs day-to-day surveillance, hand-hygiene audit and staff education as this standard requires.

Quality Coordinator
- Audits this policy {D('quarterly')}; holds training acknowledgements."""

    monitoring = f"""The Quality Coordinator audits this policy {D('quarterly')}.

What is monitored each quarter:

- Sample of records for each OE IPC.{n}.{letters}.
- Asterisked elements ({stars}) have document evidence as required.
- CORE elements ({cores}) show no critical gaps in the sample.
- Stop-work events (if any) are logged with outcome.

This policy is reviewed {D('annually')}, and sooner after a related outbreak, sterilisation failure or exposure cluster."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Infection Prevention and Control, standard IPC.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — IPC.{n} interpretations (source PDF md5 {GUIDEBOOK_MD5}; OCR policies/source/hco6_ipc_guidebook_ocr.txt).
- Internal documents of {HOSPITAL}: Infection Prevention and Control Manual, antimicrobial policy, BMW and housekeeping procedures, CSSD sterilisation records, occupational-health and PEP guidance named for IPC.{n}."""

    abbreviations = f"""AMS — Antimicrobial Stewardship
BMW — Biomedical Waste
CAPA — Corrective and Preventive Action
CLABSI — Central Line Associated Bloodstream Infection
CORE — Core objective element (NABH)
CSSD — Central Sterile Services Department
CAUTI — Catheter-Associated Urinary Tract Infection
HAI — Healthcare Associated Infection
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
IPC — Infection Prevention and Control (NABH Hospitals 6th Edition chapter)
MDRO — Multi-Drug-Resistant Organism
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — Objective Element
PEP — Post-Exposure Prophylaxis
PPE — Personal Protective Equipment
SSI — Surgical Site Infection
VAP — Ventilator-Associated Pneumonia
WHO — World Health Organization"""

    ufg = f"""HCO IPC.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (matrix agrees on levels). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — proposed: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (proposed default: no stop-work on this standard)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/IPC/POL/{n:02d}.
Official chapter is 8 standards / 49 OEs (confirmed against portal summary). Guidebook interpretations from scanned PDF md5 {GUIDEBOOK_MD5}. IPC.4 statute P2 proposed (BMW statutory provisions).
Do not copy SHCO equivalent-chapter wording. Do not touch AAC, COP, MOM or PRE."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "Infection Prevention and Control Officer",
            "Infection Prevention and Control Nurse",
            "Nursing Superintendent",
            "CSSD In-Charge",
            "Occupational Health Physician",
            "Quality Coordinator",
            f"department clinical and support staff covered by IPC.{n}",
        ]
    )

    draft = {
        "standard_code": f"IPC.{n}",
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
                "description": f"HCO Full 6th Edition IPC.{n} v2 draft: portal PDF OE data + Guidebook interpretations (md5 {GUIDEBOOK_MD5}); draft_label={DRAFT_LABEL}.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_ipc_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — IPC.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.IPC.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_ipc{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO IPC.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_ipc_v2.py
Explicit draft_label via hco_ipc_v2_common.hco_document_control.
Does NOT overwrite SHCO equivalent-chapter, HCO AAC, HCO COP or HCO MOM files.
"""
from __future__ import annotations

import sys
from generate_hco_ipc_v2 import emit_standard

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
        f"hco_ipc{n}_v2_draft.json",
        f"HCO.IPC.{n}_v2_preview.md",
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
    total = sum(inv[str(n)]["count"] for n in range(1, 9))
    assert total == 49, total
    bodies = method_bodies(D=D, HOSPITAL=HOSPITAL, BLANK=BLANK)
    interps = load_interpretations()
    expected = [oe["oe_code"] for n in range(1, 9) for oe in inv[str(n)]["oes"]]
    missing = [c for c in expected if c not in bodies]
    extra = [c for c in bodies if c not in expected]
    if missing or extra:
        raise SystemExit(f"method body mismatch missing={missing} extra={extra}")
    missing_i = [c for c in expected if not (interps.get(c) or "").strip()]
    if missing_i:
        raise SystemExit(f"missing guidebook interpretations: {missing_i}")
    for n in range(1, 9):
        write_builder(n)
        draft, statute_clause, accreditation_only, oe_codes = build_one(n, inv, bodies, interps)
        blob = json.dumps(draft)
        assert "not an approved master" not in draft["resources_required"]
        assert "not an approved master" not in blob
        if re.search(r"\bHIC\b", blob):
            raise SystemExit(f"HIC leaked into IPC.{n} draft")
        assert DRAFT_LABEL in draft["resources_required"]
        joined = "\n".join(draft["procedure_steps"])
        assert joined.count("Method note (from guidebook interpretation):") == len(oe_codes)
        assert "Prepared by (designation):" in draft["resources_required"]
        dist_parts = [x.strip() for x in re.split(r"[,;\n]", draft["distribution"]) if x.strip()]
        assert len(dist_parts) == len(set(p.casefold() for p in dist_parts)), dist_parts
        emit_pre_v2(
            draft,
            f"hco_ipc{n}_v2_draft.json",
            f"HCO.IPC.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"IPC.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
