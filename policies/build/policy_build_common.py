# -*- coding: utf-8 -*-
"""Shared emit + verification for SHCO Full master-policy build scripts (AAC.2 onward).

Extracted from the AAC.1 verification battery in build_aac1.py so seven sibling
drafts do not each re-derive the same assertions. Content stays in the per-standard
build file; this module writes the JSON/SQL and fails loudly if structure drifts.

Disclaimer (standing rule 2026-08-17, scripts/master-policy-todos.md): paragraphs 1, 3
and 4 of the shared HIC.3-6 block stay byte-identical; only paragraph 2's named
statutes change per standard. make_disclaimer() enforces that split.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from policy_placeholder_audit import audit

_HERE = Path(__file__).resolve().parent
POLICIES = _HERE.parent
DRAFTS = POLICIES / "drafts"
SQL_OUT = POLICIES / "sql"

# Paragraphs 1, 3, 4 of the approved HIC.3/4/5/6 / AAC.1 disclaimer. Do not edit
# here — a change belongs in a deliberate pass across all masters.
DISCLAIMER_P1 = (
    "This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be "
    "reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked "
    "[Hospital to define] must be replaced with the hospital's own decision; a document issued "
    "with those markers left in place is not an approved policy."
)
DISCLAIMER_P3 = (
    "The clinical and technical content reflects recognised national and international guidance "
    "current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that "
    "it is current and consistent with the edition of the accreditation standard against which it "
    "is being assessed."
)
DISCLAIMER_P4 = (
    "This document is not issued by, endorsed by, or affiliated with NABH, the World Health "
    "Organization, the National Centre for Disease Control, the Food Safety and Standards "
    "Authority of India, any Pollution Control Board, or any other body named in it. Wording is "
    "original; no text has been reproduced from the standards, rules or guidelines referenced."
)

DISCLAIMER_P1_MD5 = hashlib.md5(DISCLAIMER_P1.encode("utf-8")).hexdigest()
DISCLAIMER_P3_MD5 = hashlib.md5(DISCLAIMER_P3.encode("utf-8")).hexdigest()
DISCLAIMER_P4_MD5 = hashlib.md5(DISCLAIMER_P4.encode("utf-8")).hexdigest()

# The HIC wholesale inherit that this rule exists to stop. Named in a draft's
# paragraph 2 only when that draft's References actually rely on them.
HIC_BOILERPLATE_STATUTES = (
    "Bio-Medical Waste Management Rules, 2016",
    "Food Safety and Standards Act, 2006",
)


def make_disclaimer(statute_clause: str) -> str:
    """Four-paragraph disclaimer with a per-standard statutory paragraph 2.

    `statute_clause` is the text that follows 'in particular those arising under '
    and precedes the full stop before 'Statutory requirements change'. It must name
    real statutes from the draft's own References — never the HIC BMW/FSS pair
    unless those statutes are actually cited there.
    """
    statute_clause = statute_clause.strip()
    assert statute_clause, "statute_clause is empty"
    assert not statute_clause.endswith("."), "statute_clause should not end with a period"
    p2 = (
        "Several requirements in this document are statutory rather than advisory — in particular "
        f"those arising under {statute_clause}. Statutory requirements change, and State "
        "authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible "
        "for verifying the current text of any rule cited here and the conditions attached to its "
        "own authorisations and licences; this document does not constitute legal advice."
    )
    return "\n\n".join([DISCLAIMER_P1, p2, DISCLAIMER_P3, DISCLAIMER_P4])


def dollar(s, tag="q"):
    assert f"${tag}$" not in s, f"delimiter collision in: {s[:60]}"
    return f"${tag}${s}${tag}$"


def pg_array(items):
    return "array[" + ", ".join("'" + i.replace("'", "''") + "'" for i in items) + "]"


def steps_array(steps):
    return "array[\n    " + ",\n    ".join(dollar(s, "s") for s in steps) + "\n  ]"


def emit_and_verify(
    *,
    standard_code: str,
    chapter: str,
    oe_codes: list[str],
    policy_title: str,
    purpose: str,
    scope: str,
    policy_statement: str,
    procedure_steps: list[str],
    responsibility: str,
    references_text: str,
    distribution: str,
    abbreviations: str,
    disclaimer: str,
    oe_mapping: list[dict],
    universal_facts_checklist: str,
    version: str,
    revision_history: list[dict],
    tier1_oes: list[str],
    statute_clause: str,
    sql_header: str,
    json_name: str,
    sql_name: str,
):
    """Write draft JSON + insert SQL and run the AAC.1-grade verification battery."""
    draft = {
        "standard_code": standard_code,
        "chapter": chapter,
        "oe_codes": oe_codes,
        "policy_title": policy_title,
        "purpose": purpose,
        "scope": scope,
        "policy_statement": policy_statement,
        "procedure_steps": procedure_steps,
        "responsibility": responsibility,
        "references_text": references_text,
        "distribution": distribution,
        "abbreviations": abbreviations,
        "disclaimer": disclaimer,
        "oe_mapping": oe_mapping,
        "universal_facts_checklist": universal_facts_checklist,
        "version": version,
        "revision_history": revision_history,
        "status": "draft",
    }

    DRAFTS.mkdir(parents=True, exist_ok=True)
    SQL_OUT.mkdir(parents=True, exist_ok=True)

    with open(DRAFTS / json_name, "w", encoding="utf-8", newline="\n") as f:
        json.dump(draft, f, ensure_ascii=False, indent=2)

    sql = f"""-- {standard_code} master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
{sql_header}

insert into public.shco_policy_masters (
  standard_code,
  chapter,
  oe_codes,
  policy_title,
  purpose,
  scope,
  policy_statement,
  procedure_steps,
  responsibility,
  references_text,
  distribution,
  abbreviations,
  disclaimer,
  oe_mapping,
  universal_facts_checklist,
  version,
  revision_history,
  status
) values (
  '{standard_code}',
  '{chapter}',
  {pg_array(oe_codes)},
  {dollar(policy_title)},
  {dollar(purpose)},
  {dollar(scope)},
  {dollar(policy_statement)},
  {steps_array(procedure_steps)},
  {dollar(responsibility)},
  {dollar(references_text)},
  {dollar(distribution)},
  {dollar(abbreviations)},
  {dollar(disclaimer)},
  {dollar(json.dumps(oe_mapping, ensure_ascii=False))}::jsonb,
  {dollar(universal_facts_checklist)},
  '{version}',
  {dollar(json.dumps(revision_history, ensure_ascii=False))}::jsonb,
  'draft'
);
"""
    with open(SQL_OUT / sql_name, "w", encoding="utf-8", newline="\n") as f:
        f.write(sql)

    print(f"=== {standard_code} UNAPPROVED DRAFT ===")
    print("steps:", len(procedure_steps))

    bad = []
    for i, s in enumerate(procedure_steps, start=1):
        m = re.match(r"^(\d+)\.\s", s)
        if not m or int(m.group(1)) != i:
            bad.append((i, s[:50]))
    assert not bad, f"step numbering broken: {bad}"
    print("step numbering contiguous from 1:", True)

    text_fields = [
        purpose, scope, policy_statement, responsibility, references_text,
        distribution, abbreviations, disclaimer, universal_facts_checklist,
    ]
    assert not any("\r" in v for v in text_fields + procedure_steps), "CR found"
    print("no CR in any field:", True)

    assert sorted(m["oe_code"] for m in oe_mapping) == sorted(oe_codes)
    print(f"mapping covers all {len(oe_codes)} OEs:", True)
    assert all(m.get("evidence") and m.get("responsible") for m in oe_mapping)
    print("every mapping row has evidence + responsible:", True)

    for m in oe_mapping:
        records = [r.strip() for r in m["evidence"].split(";")]
        assert all(records), f"{m['oe_code']}: evidence contains an empty record"
    print("no empty evidence records:", True)

    referenced = set()
    for m in oe_mapping:
        for a, b in re.findall(r"(\d+)-(\d+)", m["steps"]):
            referenced.update(range(int(a), int(b) + 1))
        for n in re.findall(r"(?<![\d-])(\d+)(?![\d-])", m["steps"]):
            referenced.add(int(n))
    assert referenced, "no steps referenced"
    assert max(referenced) <= len(procedure_steps)
    print("mapped step numbers all exist:", True)
    print("steps not mapped to any OE:", sorted(set(range(1, len(procedure_steps) + 1)) - referenced))

    optional = [
        "definitions", "training_competency", "resources_required",
        "monitoring_audit", "exceptions",
    ]
    assert not any(k in draft for k in optional)
    print("optional sections left unset:", True)
    assert draft["status"] == "draft"
    print("status is draft:", True)

    _ev = {m["oe_code"]: len(m["evidence"]) for m in oe_mapping}
    if tier1_oes:
        missing = [c for c in tier1_oes if c not in _ev]
        assert not missing, f"tier1 OE missing from mapping: {missing}"
        t1 = [_ev[c] for c in tier1_oes]
        t2 = [_ev[c] for c in oe_codes if c not in tier1_oes]
        if t2:
            assert min(t1) > max(t2), (
                f"a Tier 2 evidence column is as deep as or deeper than a Tier 1 column: {_ev}"
            )
        print("Tier 1 evidence columns deeper than Tier 2:", _ev)
    else:
        print("whole standard is Tier 2 (no asterisked OE):", _ev)

    assert re.fullmatch(r"\d+\.\d+", version), f"version not semantic text: {version}"
    assert isinstance(revision_history, list) and revision_history
    for r in revision_history:
        assert set(r) == {"version", "date", "description"}, f"bad revision entry keys: {r}"
        assert re.fullmatch(r"\d{2}-\d{2}-\d{4}", r["date"]), f"date not DD-MM-YYYY: {r['date']}"
    assert revision_history[-1]["version"] == version
    print("version + revision_history populated and well-formed:", version, revision_history)

    _all_text = " ".join(
        [purpose, scope, policy_statement, responsibility, references_text,
         distribution, abbreviations, disclaimer]
        + procedure_steps + [json.dumps(oe_mapping, ensure_ascii=False)]
    )
    assert "{{HOSPITAL_NAME}}" in _all_text, "no template token found at all"
    assert not re.search(r"(?<!\{)\{HOSPITAL_NAME\}(?!\})", _all_text), (
        "single-braced {HOSPITAL_NAME} found -- str.format() collapse"
    )
    print("placeholder integrity (double braces intact):", True)

    parts = disclaimer.split("\n\n")
    assert len(parts) == 4, f"disclaimer is not four paragraphs: {len(parts)}"
    assert hashlib.md5(parts[0].encode("utf-8")).hexdigest() == DISCLAIMER_P1_MD5, (
        "disclaimer paragraph 1 drifted from the shared block"
    )
    assert hashlib.md5(parts[2].encode("utf-8")).hexdigest() == DISCLAIMER_P3_MD5, (
        "disclaimer paragraph 3 drifted from the shared block"
    )
    assert hashlib.md5(parts[3].encode("utf-8")).hexdigest() == DISCLAIMER_P4_MD5, (
        "disclaimer paragraph 4 drifted from the shared block"
    )
    assert statute_clause in parts[1], "disclaimer paragraph 2 is missing the statute_clause"
    for banned in HIC_BOILERPLATE_STATUTES:
        if banned not in statute_clause:
            assert banned not in parts[1], (
                f"disclaimer paragraph 2 inherited HIC boilerplate statute not in this "
                f"standard's statute_clause: {banned}"
            )
    print("disclaimer P1/P3/P4 shared; P2 statute-matched:", True)

    _exact, _variant, _total, _problems = audit(draft)
    assert not _problems, _problems
    _claim = f"{_total} fillable blanks"
    assert _claim in universal_facts_checklist, f"checklist does not state '{_claim}'"
    assert f"{_exact} in the exact form" in universal_facts_checklist, (
        f"checklist exact-form figure disagrees with audit ({_exact})"
    )
    assert f"finds {_exact} of {_total}" in universal_facts_checklist, (
        f"checklist search-count sentence disagrees with audit ({_exact} of {_total})"
    )
    print("checklist placeholder figures agree with the audit:", _exact, _variant, _total)
    print(f"wrote {json_name} and {sql_name}")
    return draft
