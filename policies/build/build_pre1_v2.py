# -*- coding: utf-8 -*-
"""PRE.1 v2 template test — patient and family rights and responsibilities.

Shape follows FMS.5 v2.2 (section list and order only). Wording is built from
PRE.1 OEs read directly from the NABH SHCO 3rd Edition PDF (August 2022,
md5 39e3bc86d73d651b9cfef283bbf018a9), printed page 86 / PDF index 93.
Chapter intent: printed page 85 / PDF index 92.

Does NOT overwrite pre1_draft.json or build_pre1.py. No SQL. No Supabase insert.
No stop-work section — not a facilities standard.

Disclaimer P2 is accreditation-only (patient-rights charter method; no NBC,
Medical Devices Rules, D&C Act, CPA/CEA/MHCA checklist import).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from policy_build_common import (
    DISCLAIMER_P1_MD5,
    DISCLAIMER_P3_MD5,
    DISCLAIMER_P4_MD5,
    HIC_BOILERPLATE_STATUTES,
    POLICIES,
    make_disclaimer_accreditation_only,
)

STANDARD_CODE = "PRE.1"
CHAPTER = "PRE"
OE_CODES = ["PRE.1.a", "PRE.1.b", "PRE.1.c", "PRE.1.d", "PRE.1.e"]
POLICY_TITLE = "Patient and Family Rights and Responsibilities"
VERSION = "2.0"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "19-08-2026",
        "description": "PRE chapter template test: FMS.5 v2.2 shape, plain English, PRE roles, no stop-work.",
    },
]

D = lambda s: f"«{s}»"
BLANK = "«________»"
HOSPITAL = "{{HOSPITAL_NAME}}"

# PDF page 92 — chapter intent (abridged for policy use; full intent in universal_facts)
STATEMENT_OF_INTENT = (
    "A person who walks in must know their rights and their responsibilities before care begins — "
    "not from a poster they cannot read, and not from a form they signed without hearing."
)

PURPOSE = f"""This policy says how {HOSPITAL} protects and promotes patient and family rights and informs patients and families about their responsibilities during care.

It covers five jobs that match the standard:

- document, display and make patients and families aware of rights and responsibilities;
- actively promote those rights and responsibilities;
- protect patient and family rights in daily care;
- give a way to report a violation of those rights;
- have top leadership monitor violations, analyse them and take corrective and preventive action.

The chapter intent is that the organisation defines, protects and promotes patient and family rights and responsibilities, that staff know them and are trained to protect them, and that patients are told their rights and educated about their responsibilities at the time of entering the organisation.

This policy owns that a documented set exists, is displayed, is made known, is promoted and is protected. The beliefs-values-and-decision-making policy (PRE.2) owns what is in the rights list. This policy does not print that list as a NABH mandate.

Words marked {D('like this')} are defaults a small hospital can keep. Change the marked text before issue if this hospital needs a different owner, interval or arrangement. A blank marked {BLANK} has no sensible default. Fill it in before this document is signed."""

SCOPE = f"""This policy applies at every point where a patient or family enters or is cared for at {HOSPITAL}: registration and front office, out-patient, emergency, day-care, in-patient wards, intensive or high-dependency areas if they exist, and the operation theatre insofar as rights are displayed and staff must protect them.

It binds:

- front-office and registration staff who display and explain rights at entry;
- treating doctors and nurses who protect rights during care;
- the {D('Patient Rights Officer')} who holds the documented set, display, awareness method, promotion method and violation-report route;
- billing and front-desk staff who must not withhold cost information that is a patient right under PRE.2;
- top leadership who review violations;
- the {D('Quality Coordinator')} who audits records.

It covers documentation, display and awareness; active promotion; protection; a violation-report mechanism; and leadership monitoring with corrective and preventive action.

Boundaries with other policies of {HOSPITAL}:

- PRE.2 owns the content of the rights list. This policy owns that a current documented set exists, is displayed, is made known, is promoted and is protected.
- PRE.3 owns informed-consent method. A right to consent is in the PRE.2 list; obtaining consent is PRE.3.
- PRE.4 owns education about healthcare needs. Telling a patient their rights at entry is this policy. Teaching about disease, medicines and infection prevention is PRE.4.
- PRE.5 owns expected costs and the pricing policy. A right to cost information is in PRE.2; the tariff method is PRE.5.
- PRE.6 owns feedback and complaint redressal. A complaint about a rights violation is received under PRE.6 and is also a report under this policy. PRE.6 does not replace leadership review here.
- AAC.2 owns registration and the unique identification number. Awareness of rights happens at or beside registration; this policy does not generate the number.
- AAC.8 owns discharge-summary advice on paper. This policy owns rights at entry, not the discharge paper.
- Clinical consent for surgery, anaesthesia, sedation and transfusion (COP.5, COP.9, COP.10, COP.11) own that the relevant consent happened. This policy does not decide whether a unit was hung with consent."""

POLICY_STATEMENT = f"""{HOSPITAL} documents patient and family rights and responsibilities, displays them where a person entering can see or hear them, and makes patients and families aware of them at entry. A charter that lives only in the quality office is not documentation. A board behind the clerk that patients never pass is not display. A tick-box without explanation is not awareness.

{HOSPITAL} actively promotes those rights and responsibilities to staff and to patients and families after entry. A poster that is never mentioned again is not active promotion.

{HOSPITAL} protects patient and family rights in the course of care — privacy, dignity, refusal, confidentiality, access to the treating doctor's name, and the other rights in the documented set held under PRE.2.

{HOSPITAL} has a mechanism to report a violation of patient and family rights that does not send the report only to the person alleged to have committed the violation.

{HOSPITAL} requires top leadership to monitor and analyse violations and to take corrective and preventive action. A dormant violation file is not monitoring."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no ward convenience exception and no "we will explain later" exception.

1. Denying a patient or family access to the documented rights-and-responsibilities set, or keeping the only copy in an office patients never enter.
2. Displaying rights only in a language or format this hospital's patients cannot use.
3. Recording "rights explained" with no named person, no language noted, and no time when the patient or accompanying family could actually hear the explanation.
4. Counting the step-1 display board as the year's active promotion.
5. Examining, exposing or discussing a patient without privacy when privacy is a right in the documented set.
6. Punishing, dismissing or delaying care because a patient refused treatment, asked for another opinion, asked the doctor's name, or made a complaint.
7. Requiring a violation report to go only to the person alleged to have committed the violation.
8. Opening a violation file and never reviewing it at top leadership level.
9. Withholding the documented responsibilities from the patient and family — the standard requires that patients are informed about their responsibilities during care, not only about rights.

Staff who see one of these acts report it the same shift to the {D('Patient Rights Officer')} or, if that person is not available, the {D('Front-office In-Charge')}."""

PROCEDURE_STEPS = [
f"""5.1 Document, display and make patients and families aware

Patient and family rights and responsibilities are documented, displayed, and patients and families are made aware of the same at {HOSPITAL}. The book names these three acts together. Each act fails if treated as a substitute for the others.

The documented set is held by the {D('Patient Rights Officer')}. It matches the current rights list owned by PRE.2. Responsibilities are what this hospital asks of the patient and family during care (for example to give accurate history, to keep agreed appointments, to treat staff without violence). The set is dated, version-controlled, and withdrawn from use when superseded.

Display uses boards, printed material and any online presence this hospital actually maintains. Display languages: {D('Hindi and English')}. Display locations include {D('registration counter, emergency waiting area, and each in-patient ward entrance')}. A board only in a language patients do not use is not display for those patients.

Awareness at entry is carried out by {D('registration staff and the admitting nurse')}. Entry includes out-patient first contact, emergency arrival and in-patient admission. The staff member names the language used, gives time for questions, and records the date and their name — not only a signature. An unconscious or severely distressed arrival is made aware as soon as the patient or accompanying family can receive it; the delay and reason are recorded.

WHO Human rights and health (2017), chapter 9, may inform why a rights document exists. It is not pasted as this hospital's charter.""",

f"""5.2 Actively promote rights and responsibilities

Patient and family rights and responsibilities are actively promoted at {HOSPITAL}. Active promotion means the set is used in the course of care, not only on the wall at the door.

Promotion to staff happens at induction and {D('once a year')} after that. Staff are shown the documented set, the violation-report route in section 5.4, and that PRE.2 lists what the rights include. Ward briefings refer to rights when consent, refusal, a complaint or a cost question is about to arise.

Promotion to patients and families happens after entry when a right is about to be exercised — before consent, when a refusal is discussed, when a complaint is invited, when cost is explained. Referring to the right by name is promotion. A once-a-year seminar with no ward follow-up is not.

This step does not rewrite PRE.3 consent method, PRE.5 cost explanation or PRE.6 complaint method. It requires those processes are spoken of as rights, not as favours.""",

f"""5.3 Protect patient and family rights

The organisation protects patient and family rights. Protection is the daily work of not doing what the documented set forbids: not examining without privacy, not ignoring a refusal, not withholding the treating doctor's name, not punishing a complaint.

Treating doctors and nurses protect rights at the bedside. The {D('Patient Rights Officer')} holds a short written expectation of protection in each care setting — out-patient, emergency, ward and theatre reception — without reprinting the PRE.2 list.

A failure of protection is a violation and is reported under section 5.4. Protection is not a separate quality slogan; it is how staff actually behave.""",

f"""5.4 Report a violation of patient and family rights

The organisation has a mechanism to report a violation of patient and family rights.

A patient, family member or staff member may report using {D('the complaint box, the patient-rights helpline number on the display board, or a written form at registration')}. Reports are received by the {D('Patient Rights Officer')}. If the alleged violator is that officer, the report goes to the {D('Medical Superintendent')}.

Each report is logged with date, reporter (name or "anonymous"), the right said to be violated, a short statement, and who received it. A complaint lodged under PRE.6 that alleges a rights violation also enters this violation log. PRE.6 owns redressal of the complaint as a complaint. This step owns that the same facts are available for leadership review in section 5.5.

A report that can be made only to the person alleged to have committed the violation is not a mechanism.""",

f"""5.5 Leadership monitors violations and acts

Violation of patient and family rights are monitored, analysed and corrective/preventive action taken by the top leadership of the organisation.

The {D('Medical Superintendent')} reviews the violation log {D('quarterly')} (four times a year). The review looks for repeated settings, repeated rights, and whether display or promotion failed. Findings produce dated corrective and preventive action (CAPA — the fix and the step that stops it happening again) with an owner. An open CAPA older than {D('thirty days')} is escalated to the governing body or owner if the hospital has one.

A complaint that is not a rights violation stays with PRE.6. A rights violation that never became a patient complaint still comes to this review.""",
]

RESPONSIBILITY = f"""Roles below are titles, not vacancies. If one person holds two titles in a small hospital, both duties still apply.

Medical Superintendent (Head of the Institution)
- Accountable that this policy is issued, resourced and followed.
- Reviews the violation log and signs leadership CAPA under section 5.5.

Patient Rights Officer (named lead for patient and family rights)
- Authors and keeps current the documented set, display, awareness method, promotion method and violation-report mechanism.
- Receives violation reports unless the alleged violator is this officer — then the Medical Superintendent receives them.
- Prepares the quarterly violation summary for leadership review.

Front-office / Registration In-Charge
- Makes patients and families aware at entry as section 5.1 requires.
- Keeps display boards current and readable at points of entry.

Nursing Superintendent
- Ensures ward entrances display the set and that nurses protect rights at the bedside.
- Holds signed staff acknowledgements with the induction record.

Treating doctors and ward nurses
- Protect the rights in the documented set during examination, treatment and conversation.
- Refer to rights when consent, refusal, complaint or cost is discussed.

Billing / front-desk lead
- Does not withhold cost information that is a patient right under PRE.2; detailed tariff method stays with PRE.5.

Quality Coordinator
- Audits this policy {D('quarterly')} (see section 7).
- Tracks CAPA to closure.

A RACI snapshot:

- Documented set and display: Patient Rights Officer (R/A); Front-office In-Charge (R for entry points)
- Awareness at entry: registration staff and admitting nurse (R); Patient Rights Officer (A)
- Active promotion: all clinical staff (R); Patient Rights Officer (A for method)
- Protection at bedside: treating doctor and nurse (R); Nursing Superintendent (A)
- Violation report received: Patient Rights Officer or Medical Superintendent (R/A)
- Leadership review and CAPA: Medical Superintendent (R/A); Quality Coordinator (R for audit trail)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')} (four times a year). The audit looks at records and at the floor, not only at a binder.

What is monitored each quarter:

- A current documented set that matches PRE.2.
- Display a person entering can actually use (language and location).
- Sample awareness records at entry with a named person and language — not only a signature.
- Promotion evidence beyond the display board (briefing notes, ward examples).
- Violation reports with a route that did not go only to the alleged violator.
- Leadership review minutes with CAPA assigned and dated.
- Open CAPA older than {D('thirty days')} escalated to the Medical Superintendent.

Root-cause analysis is required when the same right is violated twice in the same setting within six months, or when awareness at entry was missing in a sample of new admissions.

Corrective and preventive action is dated, has an owner, and is checked at the next quarterly audit.

This policy is reviewed {D('annually')} (once a year), and sooner when a patient was not made aware at entry, a display was only in an unused language, a violation had no report route, or leadership review did not happen."""

TRAINING_ACKNOWLEDGEMENT = f"""Staff who receive patients at entry, and all clinical staff who examine or treat patients, are trained on this policy at induction, before first unsupervised patient contact, and {D('once a year')} after that. Training covers: where the documented set is; how to make a patient aware at entry; how to promote rights during care; how to protect privacy and dignity; and how to report a violation.

Staff acknowledgement

I have read this Patient and Family Rights and Responsibilities policy of {HOSPITAL}. I will not hide the rights charter from a patient. I will not record "rights explained" without actually explaining. I will not send a violation report only to the person alleged to have committed the violation.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Nursing Superintendent holds signed acknowledgements with the induction record.)"""

DOCUMENT_CONTROL = f"""Document number: {D('PRE/POL/01')}
Issue number: {D('01')}
Version: 2.0 (PRE chapter template test — not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}

Prepared by (designation): {D('Patient Rights Officer')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Display languages: {D('Hindi and English')}
Violation report route: {D('complaint box / helpline / registration form')}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Patient Rights and Education chapter, standard PRE.1 (this policy is written so those requirements are met in day-to-day work; it is not a commentary on the standard).
- Human rights and health, World Health Organization (2017) — chapter 9; a framework for why a rights document exists; not pasted as this hospital's charter.
- Olejarczyk JP and Young M, Patient Rights and Ethics (2021) — chapter 15; context for rights as an ethical and clinical practice, not a protocol.
- Internal documents of {HOSPITAL}: the documented rights and responsibilities set; display boards; awareness and promotion methods; violation log; leadership-review records; PRE.2 beliefs-values-and-decision-making policy; PRE.3–PRE.6 sibling policies; AAC.2 registration policy."""

DISTRIBUTION = f"""Official master copy: office of the Medical Superintendent, {HOSPITAL}, with the {D('Patient Rights Officer')} and the Quality Coordinator.

Copies issued to: registration and front office; every out-patient and emergency point of entry; every in-patient ward; nursing administration; billing desk.

The current version is available to all staff at the {D('front-office policy file')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

The documented rights set and the violation-report method are held at points of entry and on the wards.

When a new version is issued, take old copies out of use. The Quality Coordinator keeps one dated copy of each old version."""

ABBREVIATIONS = """CAPA — corrective and preventive action
NABH — National Accreditation Board for Hospitals and Healthcare Providers
OE — objective element (a measurable part of a NABH standard)
PRE — Patient Rights and Education (NABH SHCO chapter 4)
RCA — root-cause analysis
SHCO — Standards for Small Healthcare Organisations
WHO — World Health Organization

Patient Rights Officer — the named lead who holds the documented set, display, awareness, promotion and violation-report mechanism"""

DISCLAIMER, _STATUTE_CLAUSE = make_disclaimer_accreditation_only()

OE_MAPPING = [
    {
        "oe_code": "PRE.1.a",
        "requirement": "Patient and family rights and responsibilities are documented, displayed, and they are made aware of the same.",
        "steps": "Statement of intent; Section 3; 5.1 Document, display and make aware; Section 4 item 1–3",
        "responsible": "Patient Rights Officer (document and display); registration staff and admitting nurse (awareness at entry)",
        "records": [
            "Current documented rights-and-responsibilities set, version-controlled, matching PRE.2.",
            "Display boards or printed material at registration, emergency and ward entrances, in named languages.",
            "Awareness-at-entry records with date, staff name and language — not only an unexplained signature.",
            "Record of delayed awareness for an unconscious or distressed arrival, with reason.",
            "Withdrawal of superseded display copies when the set is updated.",
        ],
    },
    {
        "oe_code": "PRE.1.b",
        "requirement": "Patient and family rights and responsibilities are actively promoted.",
        "steps": "Section 3; 5.2 Actively promote; Section 4 item 4",
        "responsible": "Patient Rights Officer (method); all clinical staff (promotion in care)",
        "records": [
            "Written promotion method for staff and for patients after entry.",
            "Induction and annual briefing records showing staff know the set and the violation-report route.",
            "Sample ward or clinic notes where a right was named before consent, refusal, complaint or cost discussion.",
            "Evidence that promotion is not only the step-1 display board.",
        ],
    },
    {
        "oe_code": "PRE.1.c",
        "requirement": "The organisation protects patient and family rights.",
        "steps": "Section 3; 5.3 Protect rights; Section 4 items 5–6",
        "responsible": "Treating doctors and nurses (protection); Patient Rights Officer (written expectation)",
        "records": [
            "Short written expectation of how staff protect rights in each care setting.",
            "Violation log entries where a failure of protection was reported.",
            "Quarterly audit sample showing privacy, dignity and refusal were respected at bedside.",
        ],
    },
    {
        "oe_code": "PRE.1.d",
        "requirement": "The organisation has a mechanism to report a violation of patient and family rights.",
        "steps": "Section 3; 5.4 Report a violation; Section 4 item 7",
        "responsible": "Patient Rights Officer (receiver); Medical Superintendent (if alleged violator is the officer)",
        "records": [
            "Written violation-report mechanism: complaint box, helpline and/or form, with named receiver.",
            "Violation log with date, reporter, right cited, statement and receiver.",
            "Records showing PRE.6 complaints alleging a rights violation also entered the violation log.",
            "Evidence the route is not only to the alleged violator.",
        ],
    },
    {
        "oe_code": "PRE.1.e",
        "requirement": "Violation of patient and family rights are monitored, analysed and corrective/preventive action taken by the top leadership of the organisation.",
        "steps": "Section 3; 5.5 Leadership monitors and acts; Section 7 Quality monitoring",
        "responsible": "Medical Superintendent (accountable); Quality Coordinator (audit trail)",
        "records": [
            "Quarterly leadership review minutes of the violation log.",
            "Dated CAPA with owner for each significant violation or repeat pattern.",
            "Escalation record for open CAPA older than thirty days.",
            "Evidence that rights violations not lodged as PRE.6 complaints still reached leadership review.",
        ],
    },
]

UNIVERSAL_FACTS_CHECKLIST = """PRE.1 v2 template test (2026-08-19). PDF md5 39e3bc86d73d651b9cfef283bbf018a9.

SOURCE — read from PDF on 2026-08-19:
- Chapter intent: PDF page 92 (index 91): organisation defines, protects and promotes patient and family rights and responsibilities; staff aware and trained; patients informed of rights and educated about responsibilities at entry.
- Summary header PRE.1: PDF page 92: "The organisation protects and promotes patient and family rights and informs them about their responsibilities during care."
- OE page header: same wording on PDF page 93 (index 92).
- PRE.1.a (Commitment, asterisked): Patient and family rights and responsibilities are documented, displayed, and they are made aware of the same.
- PRE.1.b (Achievement, asterisked): Patient and family rights and responsibilities are actively promoted.
- PRE.1.c (Core): The organisation protects patient and family rights.
- PRE.1.d (Core): The organisation has a mechanism to report a violation of patient and family rights.
- PRE.1.e (Core): Violation of patient and family rights are monitored, analysed and corrective/preventive action taken by the top leadership of the organisation.

SHAPE: FMS.5 v2.2 section skeleton. Five What-we-do subsections (5.1–5.5). Stop-work OMITTED — no section 6 stop-work; top-level sections run 1–13. Statement of intent replaces safety objective. PRE roles only (no facilities roles).

Disclaimer: accreditation-only P2. No NBC, Medical Devices Rules, D&C Act, CPA/CEA/MHCA checklist in P2.

No SQL. Status draft. Not an approved master."""


def _verify_disclaimer(disclaimer: str) -> None:
    parts = disclaimer.split("\n\n")
    assert len(parts) == 4
    assert hashlib.md5(parts[0].encode()).hexdigest() == DISCLAIMER_P1_MD5
    assert hashlib.md5(parts[2].encode()).hexdigest() == DISCLAIMER_P3_MD5
    assert hashlib.md5(parts[3].encode()).hexdigest() == DISCLAIMER_P4_MD5
    assert "no named Act of Parliament" in parts[1]
    for banned in HIC_BOILERPLATE_STATUTES:
        assert banned not in parts[1]
    print("disclaimer P1/P3/P4 shared; P2 accreditation-only:", True)


def build_markdown(draft: dict) -> str:
    lines = [
        f"# {draft['policy_title']}",
        f"**{HOSPITAL}**",
        "",
        "*Patient and family rights at entry and through care. Not a drill script.*",
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
    lines += [
        "## 6. Governance and responsibility",
        "",
        draft["responsibility"],
        "",
        "## 7. Quality monitoring (RCA → CAPA)",
        "",
        draft["monitoring_audit"],
        "",
        "## 8. Training and staff acknowledgement",
        "",
        draft["training_competency"],
        "",
        "## 9. References",
        "",
        draft["references_text"],
        "",
        "## 10. Distribution",
        "",
        draft["distribution"],
        "",
        "## 11. Abbreviations",
        "",
        draft["abbreviations"],
        "",
        f"## 12. Traceability to NABH SHCO 3rd Edition {draft['standard_code']}",
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
        "## 13. Required Records / Evidence Checklist",
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


def main() -> int:
    draft = {
        "standard_code": STANDARD_CODE,
        "chapter": CHAPTER,
        "oe_codes": OE_CODES,
        "policy_title": POLICY_TITLE,
        "purpose": PURPOSE,
        "scope": SCOPE,
        "policy_statement": POLICY_STATEMENT,
        "procedure_steps": PROCEDURE_STEPS,
        "responsibility": RESPONSIBILITY,
        "references_text": REFERENCES,
        "distribution": DISTRIBUTION,
        "abbreviations": ABBREVIATIONS,
        "disclaimer": DISCLAIMER,
        "oe_mapping": OE_MAPPING,
        "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
        "version": VERSION,
        "revision_history": REVISION_HISTORY,
        "status": "draft",
        "definitions": STATEMENT_OF_INTENT,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "pre1_v2_adoptable_shape",
        "subtitle": "Patient and family rights at entry and through care.",
    }

    assert len(PROCEDURE_STEPS) == 5
    for i, s in enumerate(PROCEDURE_STEPS, start=1):
        assert s.startswith(f"5.{i} "), f"step {i} numbering wrong"
    banned = re.compile(r"assessor|this OE|common error|Maintenance In-Charge|Night Duty Officer|Floor Fire Warden|Gas-Plant", re.I)
    body_parts = [
        draft["purpose"], draft["scope"], draft["policy_statement"], draft["responsibility"],
        draft["references_text"], draft["distribution"], draft["abbreviations"],
        draft["definitions"], draft["exceptions"], draft["monitoring_audit"],
        draft["training_competency"], draft["resources_required"],
    ] + draft["procedure_steps"] + [json.dumps(draft["oe_mapping"])]
    body = " ".join(body_parts)
    assert banned.search(body) is None, "banned framing or facilities role found"
    assert "[Hospital to define" not in body
    assert draft.get("stop_work") in (None, "")
    _verify_disclaimer(DISCLAIMER)

    md = build_markdown(draft)
    expected = [
        "## 1. Purpose", "## 2. Scope", "## 3. Policy standards", "## 4. Non-negotiable rules",
        "## 5. What we do",
        "### 5.1 Document, display and make patients and families aware",
        "### 5.2 Actively promote rights and responsibilities",
        "### 5.3 Protect patient and family rights",
        "### 5.4 Report a violation of patient and family rights",
        "### 5.5 Leadership monitors violations and acts",
        "## 6. Governance and responsibility", "## 7. Quality monitoring (RCA → CAPA)",
        "## 8. Training and staff acknowledgement", "## 9. References", "## 10. Distribution",
        "## 11. Abbreviations", "## 12. Traceability to NABH SHCO 3rd Edition PRE.1",
        "## 13. Required Records / Evidence Checklist",
    ]
    numbered = [ln for ln in md.splitlines() if re.match(r"^#{2,3} \d", ln)]
    assert numbered == expected, f"heading drift:\n{numbered}"
    print("markdown heading sequence is 1–13 with 5.1–5.5; no stop-work:", True)

    out_json = POLICIES / "drafts" / "pre1_v2_draft.json"
    out_md = POLICIES / "build" / "preview" / "PRE.1_v2_preview.md"
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    out_md.write_text(md, encoding="utf-8")
    print(f"wrote {out_json}")
    print(f"wrote {out_md} ({len(md.splitlines())} lines)")
    print("status is draft; no SQL written:", True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
