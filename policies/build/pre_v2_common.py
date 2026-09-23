# -*- coding: utf-8 -*-
"""Shared emit + numbering checks for PRE v2 (adoptable-policy shape).

PRE.1 v2 keeps its own builder so the approved template file stays byte-stable.
Used by build_pre2_v2.py … build_pre6_v2.py. Does not write SQL.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from policy_build_common import (
    DISCLAIMER_P1_MD5,
    DISCLAIMER_P3_MD5,
    DISCLAIMER_P4_MD5,
    HIC_BOILERPLATE_STATUTES,
    POLICIES,
)

D = lambda s: f"«{s}»"
BLANK = "«________»"
HOSPITAL = "{{HOSPITAL_NAME}}"

BANNED_FRAMING = re.compile(
    r"assessor|this OE|common error|how to satisfy|HANDOFF",
    re.I,
)

BANNED_PRE = re.compile(
    r"Maintenance In-Charge|Night Duty Officer|Gas-Plant|Floor Fire Warden"
    r"|titles, not vacancies",
    re.I,
)

AFTER_WHAT_WE_DO = [
    "Stop-work authority",
    "Governance and responsibility",
    "Quality monitoring (RCA → CAPA)",
    "Training and staff acknowledgement",
    "References",
    "Distribution",
    "Abbreviations",
]

DEFAULT_EDITION_LABEL = "NABH SHCO 3rd Edition"
HCO_EDITION_LABEL = "NABH HCO Full Accreditation 6th Edition"


def numbered_headings(
    standard_code: str,
    n_steps: int,
    has_stop_work: bool,
    *,
    edition_label: str = DEFAULT_EDITION_LABEL,
) -> list[str]:
    heads = [
        "## 1. Purpose",
        "## 2. Scope",
        "## 3. Policy standards",
        "## 4. Non-negotiable rules",
        "## 5. What we do",
    ]
    for i in range(1, n_steps + 1):
        heads.append(f"### 5.{i} ")
    n = 6
    rest = list(AFTER_WHAT_WE_DO)
    if not has_stop_work:
        rest = rest[1:]
    labels = {
        "Stop-work authority": "## {n}. Stop-work authority",
        "Governance and responsibility": "## {n}. Governance and responsibility",
        "Quality monitoring (RCA → CAPA)": "## {n}. Quality monitoring (RCA → CAPA)",
        "Training and staff acknowledgement": "## {n}. Training and staff acknowledgement",
        "References": "## {n}. References",
        "Distribution": "## {n}. Distribution",
        "Abbreviations": "## {n}. Abbreviations",
    }
    for label in rest:
        heads.append(labels[label].format(n=n))
        n += 1
    heads.append(f"## {n}. Traceability to {edition_label} {standard_code}")
    n += 1
    heads.append(f"## {n}. Required Records / Evidence Checklist")
    return heads


def section_numbers(has_stop_work: bool) -> dict[str, int]:
    n = 6
    out: dict[str, int] = {}
    rest = list(AFTER_WHAT_WE_DO)
    if not has_stop_work:
        rest = rest[1:]
    keys = [
        "stop_work",
        "governance",
        "monitoring",
        "training",
        "references",
        "distribution",
        "abbreviations",
    ]
    if not has_stop_work:
        keys = keys[1:]
    for key, _label in zip(keys, rest):
        out[key] = n
        n += 1
    out["traceability"] = n
    out["records"] = n + 1
    return out


def verify_disclaimer(
    disclaimer: str,
    statute_clause: str | None,
    *,
    accreditation_only: bool,
) -> None:
    parts = disclaimer.split("\n\n")
    assert len(parts) == 4, f"disclaimer is not four paragraphs: {len(parts)}"
    assert hashlib.md5(parts[0].encode("utf-8")).hexdigest() == DISCLAIMER_P1_MD5
    assert hashlib.md5(parts[2].encode("utf-8")).hexdigest() == DISCLAIMER_P3_MD5
    assert hashlib.md5(parts[3].encode("utf-8")).hexdigest() == DISCLAIMER_P4_MD5
    if accreditation_only:
        assert "named Act of Parliament" in parts[1]
        assert statute_clause is None or statute_clause in parts[1]
    else:
        assert statute_clause, "statute_clause required"
        assert statute_clause in parts[1]
    for banned in HIC_BOILERPLATE_STATUTES:
        if statute_clause and banned in statute_clause:
            continue
        assert banned not in parts[1]
    print("disclaimer P1/P3/P4 shared; P2 statute-matched:", True)


def verify_shape(
    draft: dict,
    *,
    oe_codes: list[str],
    statute_clause: str | None,
    accreditation_only: bool,
    edition_label: str = DEFAULT_EDITION_LABEL,
) -> str:
    steps = draft["procedure_steps"]
    has_stop = bool((draft.get("stop_work") or "").strip())
    n_steps = len(steps)
    assert 1 <= n_steps <= 12, f"What-we-do subsection count follows the OEs; got {n_steps}"
    for i, s in enumerate(steps, start=1):
        prefix = f"5.{i} "
        assert s.startswith(prefix), f"step {i} must start with {prefix!r}, got {s.splitlines()[0]!r}"

    nn_items = re.findall(r"(?m)^\d+\. ", draft["exceptions"])
    assert 1 <= len(nn_items) <= 20, f"non-negotiable count follows the OEs; got {len(nn_items)}"

    mapping = draft["oe_mapping"]
    assert [m["oe_code"] for m in mapping] == oe_codes
    for m in mapping:
        assert m.get("steps") and m.get("responsible")
        assert "evidence" not in m
        recs = m.get("records") or []
        assert isinstance(recs, list) and len(recs) >= 3, f"{m['oe_code']} records too thin"
        for r in recs:
            assert r.strip() and not r.strip().startswith("-")
            assert BANNED_FRAMING.search(r) is None, f"assessor framing in records: {r}"

    body_parts = [
        draft["purpose"],
        draft["scope"],
        draft["policy_statement"],
        draft["responsibility"],
        draft["references_text"],
        draft["distribution"],
        draft["abbreviations"],
        draft.get("definitions") or "",
        draft.get("training_competency") or "",
        draft.get("monitoring_audit") or "",
        draft.get("exceptions") or "",
        draft.get("resources_required") or "",
        draft.get("stop_work") or "",
    ] + steps + [json.dumps(mapping, ensure_ascii=False)]
    body = " ".join(body_parts)
    assert "[Hospital to define" not in body
    assert "«________»" in body
    assert re.search(r"«[^_»][^»]*»", body), "expected at least one «editable default» besides a true blank"
    assert "{{HOSPITAL_NAME}}" in body
    assert BANNED_FRAMING.search(body) is None
    pre_ban = BANNED_PRE.search(body)
    assert pre_ban is None, f"banned PRE wording in {draft['standard_code']}: {pre_ban.group(0)!r}"
    assert draft["status"] == "draft"

    verify_disclaimer(draft["disclaimer"], statute_clause, accreditation_only=accreditation_only)
    print("defaults marked « »; no body [Hospital to define]; no assessor framing:", True)

    md = build_markdown(draft, edition_label=edition_label)
    expected = numbered_headings(
        draft["standard_code"], n_steps, has_stop, edition_label=edition_label
    )
    numbered = [ln for ln in md.splitlines() if re.match(r"^#{2,3} \d", ln)]
    got_norm = []
    for ln in numbered:
        m = re.match(r"^(### 5\.\d+) ", ln)
        got_norm.append(m.group(1) + " " if m else ln)
    assert got_norm == expected, (
        "heading sequence drifted:\n"
        + "\n".join(f"  exp {e!r}\n  got {g!r}" for e, g in zip(expected, got_norm))
    )
    nums = []
    for ln in numbered:
        if ln.startswith("## "):
            m = re.match(r"^## (\d+)\.", ln)
            if m:
                nums.append(int(m.group(1)))
    assert nums == list(range(1, nums[-1] + 1)), f"top-level numbers not a clean run: {nums}"
    print(f"markdown heading sequence is 1–{nums[-1]} with 5.1–5.{n_steps}:", True)
    return md


def build_markdown(draft: dict, *, edition_label: str = DEFAULT_EDITION_LABEL) -> str:
    has_stop = bool((draft.get("stop_work") or "").strip())
    nums = section_numbers(has_stop)
    code = draft["standard_code"]
    lines = [
        f"# {draft['policy_title']}",
        f"**{HOSPITAL}**",
        "",
        f"*{draft.get('subtitle') or 'Patient rights in day-to-day care.'}*",
        "",
        "## Document control",
        "",
        draft["resources_required"],
        "",
        "## Statement of intent",
        "",
        draft["definitions"],
        "",
        "## 1. Purpose",
        "",
        draft["purpose"],
        "",
        "## 2. Scope",
        "",
        draft["scope"],
        "",
        "## 3. Policy standards",
        "",
        draft["policy_statement"],
        "",
        "## 4. Non-negotiable rules",
        "",
        draft["exceptions"],
        "",
        "## 5. What we do",
        "",
    ]
    for step in draft["procedure_steps"]:
        num_title, _, body = step.partition("\n\n")
        lines += [f"### {num_title}", "", body, ""]
    if has_stop:
        lines += [
            f"## {nums['stop_work']}. Stop-work authority",
            "",
            draft["stop_work"],
            "",
        ]
    lines += [
        f"## {nums['governance']}. Governance and responsibility",
        "",
        draft["responsibility"],
        "",
        f"## {nums['monitoring']}. Quality monitoring (RCA → CAPA)",
        "",
        draft["monitoring_audit"],
        "",
        f"## {nums['training']}. Training and staff acknowledgement",
        "",
        draft["training_competency"],
        "",
        f"## {nums['references']}. References",
        "",
        draft["references_text"],
        "",
        f"## {nums['distribution']}. Distribution",
        "",
        draft["distribution"],
        "",
        f"## {nums['abbreviations']}. Abbreviations",
        "",
        draft["abbreviations"],
        "",
        f"## {nums['traceability']}. Traceability to {edition_label} {code}",
        "",
        "This table is an index. It is not how the policy is organised.",
        "",
        "| OE | Requirement | Where this policy addresses it | Responsible |",
        "| --- | --- | --- | --- |",
    ]
    for m in draft["oe_mapping"]:
        req = m["requirement"].replace("|", "/")
        lines.append(f"| {m['oe_code']} | {req} | {m['steps']} | {m['responsible']} |")
    lines += [
        "",
        f"## {nums['records']}. Required Records / Evidence Checklist",
        "",
        "Records the hospital holds under this policy, listed by objective element.",
        "",
    ]
    for m in draft["oe_mapping"]:
        lines.append(f"### {m['oe_code']} — {m['requirement']}")
        lines.append("")
        for rec in m.get("records") or []:
            lines.append(f"- {rec}")
        lines.append("")
    lines += ["## Disclaimer", "", draft["disclaimer"], ""]
    return "\n".join(lines).replace("{{HOSPITAL_NAME}}", "Preview Hospital")


def emit_pre_v2(
    draft: dict,
    json_name: str,
    md_name: str,
    *,
    oe_codes: list[str],
    statute_clause: str | None,
    accreditation_only: bool,
    edition_label: str = DEFAULT_EDITION_LABEL,
    drafts_dir: Path | None = None,
    preview_dir: Path | None = None,
) -> None:
    # Normalize NABH PDF PUA fi/fl ligatures before shape checks and write-out
    # so masters never carry invisible U+F001/U+F002 glyphs.
    from nabh_text_normalize import normalize_nabh_obj

    draft = normalize_nabh_obj(draft)
    md = verify_shape(
        draft,
        oe_codes=oe_codes,
        statute_clause=statute_clause,
        accreditation_only=accreditation_only,
        edition_label=edition_label,
    )
    # HCO Full output is physically separate from SHCO. HCO builders pass
    # drafts_dir/preview_dir; if a caller forgets, json_name "hco_*" still
    # must not land in the SHCO folders.
    is_hco = json_name.startswith("hco_") or str(draft.get("chapter", "")).upper() == "HCO"
    if is_hco:
        from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW
        out_json_dir = drafts_dir or HCO_DRAFTS
        out_md_dir = preview_dir or HCO_PREVIEW
    else:
        out_json_dir = drafts_dir or (POLICIES / "drafts")
        out_md_dir = preview_dir or (POLICIES / "build" / "preview")
    out_json = out_json_dir / json_name
    out_md = out_md_dir / md_name
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    out_md.write_text(md, encoding="utf-8")
    print(f"wrote {out_json}")
    print(f"wrote {out_md} ({len(md.splitlines())} lines)")
    print("status is draft; no SQL written:", True)


def document_control(
    *,
    doc_no: str,
    version: str,
    prepared_by: str,
    extra_lines: str = "",
    draft_label: str = "PRE v2 draft",
) -> str:
    base = f"""Document number: {doc_no}
Issue number: {D('01')}
Version: {version} ({draft_label} — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {prepared_by}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}"""
    if extra_lines:
        base += f"\n\n{extra_lines}"
    base += """

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """
    return base
