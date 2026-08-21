# -*- coding: utf-8 -*-
"""Generate HCO Full PRE.1–PRE.8 v2 builders and drafts from official inventory.

Usage (from policies/build):
  python3 generate_hco_pre_v2.py

Official portal PDF has 8 PRE standards / 52 OEs. All 8 are drafted.
Does not touch AAC, COP, MOM, or SHCO. Always sets explicit HCO draft_label via
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
from hco_cop_v2_common import hco_boundaries_clause, truncate_word_safe  # noqa: E402
from hco_pre_v2_common import (  # noqa: E402
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
from hco_pre_v2_methods import method_bodies  # noqa: E402
from hco_v2_disclaimer import (  # noqa: E402
    make_hco_disclaimer_accreditation_only,
    make_hco_disclaimer_statute,
)
from hco_v2_paths import HCO_DRAFTS, HCO_PREVIEW  # noqa: E402
from pre_v2_common import emit_pre_v2  # noqa: E402

INVENTORY = ROOT / "policies/source/hco6_pre_inventory.json"
INTERP_JSON = ROOT / "policies/source/hco6_pre_interpretations.json"
BUILD = Path(__file__).resolve().parent
GUIDEBOOK_MD5 = "2c4489ee98de4ae9b49cba168ea9f42a"

# Statute P2 only where PRE OE/guidebook names legal duties. Proposed default: PRE.4.
STATUTE_BY_STD: dict[int, str | None] = {
    4: (
        "statutory norms for informed consent as named in NABH PRE.4, including "
        "where applicable the Medical Termination of Pregnancy Act, the "
        "Pre-Conception and Pre-Natal Diagnostic Techniques Act, the "
        "Transplantation of Human Organs Act, and the Human Immunodeficiency "
        "Virus and Acquired Immune Deficiency Syndrome (Prevention and Control) "
        "Act, 2017 / NACO HIV-testing policy as referenced in the Guidebook "
        "interpretation of PRE.4.a"
    ),
}

PREPARED_BY: dict[int, str] = {
    1: "Quality Coordinator",
    2: "Medical Superintendent",
    3: "Medical Superintendent",
    4: "Medical Superintendent",
    5: "Nursing Superintendent",
    6: "Patient Accounts In-Charge",
    7: "Quality Coordinator",
    8: "Quality Coordinator",
}

POLICY_TITLES: dict[int, str] = {
    1: "Protecting and Promoting Patient and Family Rights",
    2: "Patient and Family Rights in Care and Decision-Making",
    3: "Informed Decisions and Involvement in the Care Plan",
    4: "Informed Consent for Care",
    5: "Information and Education about Healthcare Needs",
    6: "Information on Expected Costs",
    7: "Patient Feedback, Experience and Complaint Redressal",
    8: "Effective Communication with Patients and Families",
}

CHAPTER_INTENT = (
    "The organisation defines, protects and promotes the patient and family's "
    "rights and responsibilities. The staff is aware of these rights and is "
    "trained to protect them. Patients are informed of their rights and educated "
    "about their responsibilities at the time of entering the organisation. "
    "The expected costs of treatment and care are explained clearly to the "
    "patient and / or family. The organisation encourages patient engagement to "
    "enhance clinical outcomes, safety and quality. Patients are educated about "
    "the mechanisms available for addressing grievances. Informed consent is "
    "obtained from the patient or family for specified procedures / care. The "
    "key components of information shall include risks, benefits and alternatives. "
    "Patients and families have a right to get information and education about "
    "their healthcare needs in a language and manner that is understood by them. "
    "The organisation has a mechanism to capture the patient experience including "
    "patient reported experience measures (PREM). The organisation develops "
    "effective patient-centred communication."
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
        f"{len(items)+1}. Staff who see a PRE.{n} rule broken report it the same shift to the "
        f"{D('department in-charge')} or the {D('Quality Coordinator')}."
    )
    return "\n".join(items)


# Fix #5 — hand-authored per-OE evidence records, matching the quality bar
# AAC.1 / SHCO HIC.1 / HCO ROM / HCO FMS / HCO PSQ / HCO IPC already demonstrate.
PRE_RECORDS: dict[str, list[str]] = {
    "PRE.1.a": [
        "Current documented patient-and-family rights-and-responsibilities text.",
        "Display record at registration, OPD waiting, ward notice boards and emergency.",
        "Bilingual pamphlet or IEC material on file.",
    ],
    "PRE.1.b": [
        "Admission-counselling record showing rights and responsibilities were explained to an in-patient.",
        "OPD display/access record for educational material.",
        "Quarterly spot-check record of display and counselling.",
    ],
    "PRE.1.c": [
        "Induction and annual training record on protecting patient and family rights.",
        "Named Guest Relations / Patient Rights Officer record as day-to-day owner.",
        "Conduct-observation record confirming staff practice matches the duty.",
    ],
    "PRE.1.d": [
        "Written list of rights-infringement examples.",
        "Incident-form record for a reported violation.",
        "Patient- or family-reported violation log (feedback form or direct report), including anonymous reports.",
    ],
    "PRE.1.e": [
        "Investigation record for each logged rights violation.",
        "Top-leadership (Medical Superintendent with Quality Coordinator) documented outcome and CAPA assignment.",
        "Open-action tracking record to closure within the defined timeframe.",
    ],
    "PRE.2.a": [
        "Recorded patient preference (form of address, diet, worship, post-death requirement) on the kardex or admission sheet.",
        "Record of action taken on the preference by the treating doctor or nurse.",
        "Spiritual-need-request routing record.",
    ],
    "PRE.2.b": [
        "Privacy-and-dignity guideline document held by the Nursing Superintendent.",
        "Screen, drape or closed-door practice-observation record.",
        "Consent record for any photograph or recording of a procedure.",
    ],
    "PRE.2.c": [
        "Extra-precaution record for vulnerable patients (elderly, neonate, physically or mentally challenged, comatose, anaesthetised).",
        "Incident record for any suspected neglect or abuse, reported the same shift.",
        "Confirmation the incident routed through the PRE.1.d violation mechanism.",
    ],
    "PRE.2.d": [
        "Confidentiality training record within the annual rights training.",
        "Record confirming HIV status or other confidential information is not visible on the record cover.",
        "Disclosure-without-permission incident record, where applicable.",
    ],
    "PRE.2.e": [
        "Documented discussion-of-refusal note — options offered, consequences explained.",
        "Record of who witnessed the explanation.",
        "Confirmation the refusal was respected after explanation, not overridden.",
    ],
    "PRE.2.f": [
        "Record of facilitation for a second-opinion request — records, imaging or reports copied.",
        "Credential-file response record for a physician-qualification query.",
        "Named internal second-opinion arrangement record.",
    ],
    "PRE.2.g": [
        "Informed-consent record for transfusion, anaesthesia, surgery, research or an invasive/high-risk procedure.",
        "Cross-reference to the PRE.4 consent process and list.",
        "Confirmation the consent was taken by the treating doctor or a doctor member of the team.",
    ],
    "PRE.2.h": [
        "Rights-display record naming the right to complain.",
        "Admission-counselling record confirming the complaint method was explained.",
        "Cross-reference to the PRE.7 complaint mechanism.",
    ],
    "PRE.2.i": [
        "Cost-information record given during rights counselling.",
        "Cross-reference to the PRE.6 tariff and cost-estimate process.",
        "Confirmation cost information was part of counselling, not only available in accounts.",
    ],
    "PRE.2.j": [
        "Written clinical-record access-request record.",
        "Turnaround-time record against the organisation-defined period.",
        "Cross-reference to the medical-records procedure.",
    ],
    "PRE.2.k": [
        "Admission record naming the treating doctor, care plan and progress information given.",
        "Consultant-name display record — board or wristband process.",
        "Walk-round record confirming patients can name their treating doctor.",
    ],
    "PRE.2.l": [
        "Patient's documented choice on information-sharing — self/family, named family member, or do-not-share instruction.",
        "Minor's-guardian information record, where applicable.",
        "Confirmation the choice was respected in practice.",
    ],
    "PRE.3.a": [
        "Documented and signed explanation of proposed care — risks, benefits, alternatives, expected results, complications.",
        "Record of the explanation being repeated at periodic intervals.",
        "Confirmation this discussion is distinct from the signed consent form.",
    ],
    "PRE.3.b": [
        "Care-plan document showing patient or family consultation.",
        "Record of concerns or requests incorporated, or the reason noted where not possible.",
        "Religious, cultural or spiritual consideration record.",
    ],
    "PRE.3.c": [
        "Record of diagnostic-result explanation to the patient or family.",
        "Same-day explanation record for an abnormal result changing the plan.",
        "Confirmation results were not left as an unexplained printout in the file.",
    ],
    "PRE.3.d": [
        "Timely condition-change explanation record.",
        "On-call doctor communication record for night or emergency deterioration.",
        "Withholding-of-resuscitation discussion record within ethical and legal limits, where applicable.",
    ],
    "PRE.3.e": [
        "Multi-disciplinary counselling session record — attendees, topic, date.",
        "Situation-identification record (critically ill family, organ donor, long-stay patient, etc.).",
        "Cross-reference to COP.1.e for uniform-care counselling overlap.",
    ],
    "PRE.4.a": [
        "Written list of procedures requiring informed consent, cross-referencing applicable statutes (for example the MTP Act, PC-PNDT Act, Transplantation of Human Organs Act, HIV Act/NACO policy where in scope).",
        "Staff training record on the consent process.",
        "Escalation record for any listed procedure started without consent.",
    ],
    "PRE.4.b": [
        "Consent form showing at least one witness present for the full doctor-patient communication.",
        "Repeat-procedure consent-validity record (for example dialysis, six-month validity, endorsement at each repeat).",
        "Quarterly consent-form audit record by the Quality Coordinator.",
    ],
    "PRE.4.c": [
        "Consent form naming the performing doctor, and each principal surgeon where multiple specialties operate.",
        "Trainee-doctor and supervising-doctor naming record, where applicable.",
        "Bilingual form and interpreter record, where used.",
    ],
    "PRE.4.d": [
        "Written description of who can consent when the patient is incapable — the next-of-kin order.",
        "Consent record showing the correct order was followed for a sampled incapable-patient case.",
        "Same-shift dual-clinician life-threatening-decision record, where applicable.",
    ],
    "PRE.4.e": [
        "Consent record confirming the performing doctor, or a doctor member of that team, obtained it — not delegated to nursing.",
        "Quarterly record-audit sample by the Medical Superintendent.",
        "Cross-reference to procedure-, sedation-, anaesthesia- and surgery-specific consent policies (COP.7/12/13/14).",
    ],
    "PRE.5.a": [
        "Language and format screening record for patient or family understanding.",
        "Education material in the identified language — counselling, print, audio-visual.",
        "Confirmation education was delivered in a format the patient could understand.",
    ],
    "PRE.5.b": [
        "Current medication-education list — drugs needing extra safety or side-effect counselling.",
        "Nursing or pharmacy education record against that list.",
        "Confirmation this is separate from the MOM administration checks.",
    ],
    "PRE.5.c": [
        "Current food-drug-interaction list relevant to this hospital.",
        "Diet or nursing education record when a listed drug is prescribed.",
        "Medication-counselling or diet-note record.",
    ],
    "PRE.5.d": [
        "Therapeutic-diet education record for in-patients.",
        "Out-patient diet-education record when requested by the treating doctor.",
        "Confirmation education was patient-specific, not a generic poster.",
    ],
    "PRE.5.e": [
        "Immunisation-advice record, adult and paediatric as applicable.",
        "Vaccines-due record kept by the treating doctor or immunisation-clinic nurse.",
        "Universal Immunisation Programme reference for paediatric advice.",
    ],
    "PRE.5.f": [
        "Long-term pain-management education record, within the patient's personal, cultural or religious beliefs.",
        "Named record of who delivers long-term pain education.",
        "Record distinguishing this from acute post-operative pain teaching.",
    ],
    "PRE.5.g": [
        "Disease-specific education record — process, complications, prevention, lifestyle, diet, immunisation.",
        "Supporting material (booklet, video, leaflet) used.",
        "Treating-doctor assignment and nursing/health-educator delivery record.",
    ],
    "PRE.5.h": [
        "HAI-prevention education record on the admission checklist — hand hygiene, avoiding overcrowding.",
        "Cross-reference to the IPC chapter's infection-prevention programme.",
        "Confirmation person-to-person education occurred, not posters alone.",
    ],
    "PRE.5.i": [
        "Special-educational-need identification record in the patient's chart (for example ADHD, autism, physical disability, communication needs).",
        "Adapted counselling or material record addressing that need.",
        "Confirmation the identified need was actually met, not only flagged.",
    ],
    "PRE.5.j": [
        "Patient-engagement activity record — support group, safety-improvement involvement, incident-reporting encouragement.",
        "Patient advisory council or safety-champion record, where implemented.",
        "Quarterly engagement-activity log by the Quality Coordinator.",
    ],
    "PRE.6.a": [
        "Displayed pricing-policy components at the registration or admission desk for OP, emergency, ICU and IP settings.",
        "Current-version record kept by the Patient Accounts In-Charge.",
        "Confirmation the policy is visible at the desk, not only held in accounts.",
    ],
    "PRE.6.b": [
        "Current dated tariff list available to patients.",
        "Charge-versus-tariff reconciliation record.",
        "Confirmation no undisclosed additional charge was applied.",
    ],
    "PRE.6.c": [
        "Written treatment-cost estimate on file, prepared in consultation with the treating doctor.",
        "Record of limitations discussed (for example emergency admission).",
        "Estimate filed in the patient account or medical record.",
    ],
    "PRE.6.d": [
        "Revised-estimate record when the care plan changes cost materially (ICU shift, medical-to-surgical, expensive investigation).",
        "Timing record confirming the patient or family was informed before or as soon as practicable after the change.",
        "Confirmation no surprise discharge charge occurred for a known plan change.",
    ],
    "PRE.7.a": [
        "Feedback-tool record capturing patient satisfaction, with out-patient and in-patient data kept separate.",
        "Response-rate record against the defined sample target.",
        "Confirmation feedback is tabulated, not left as an untabulated visitor book.",
    ],
    "PRE.7.b": [
        "Patient-experience data record — doctor/nurse communication, pain management, environment, responsiveness, discharge information, medication communication, overall rating, PREM.",
        "Quarterly PREM/experience report to the Medical Superintendent.",
        "Confirmation this goes beyond satisfaction scores alone.",
    ],
    "PRE.7.c": [
        "Written complaint-redressal guidance — lodging method, compilation, analysis timeframe, responsible person, documentation of action.",
        "Complaint log held by Guest Relations/Patient Rights Officer, including anonymous complaints and those against healthcare workers.",
        "Redressal-outcome record for a sampled complaint.",
    ],
    "PRE.7.d": [
        "Displayed feedback/complaint-procedure record — rights display, admission pamphlet.",
        "Verification record confirming the displayed path matches the actual complaints desk, phone or form.",
        "Awareness spot-check record.",
    ],
    "PRE.7.e": [
        "Review or analysis record within the defined timeframe (for example complaints within 7 days, feedback tabulated monthly).",
        "Documented process record.",
        "Overdue-complaint list reported to the Medical Superintendent each month.",
    ],
    "PRE.7.f": [
        "CAPA record from feedback or complaint analysis, with owner, due date and closure.",
        "Cross-reference record with PRE.1.e rights-violation CAPA where subjects overlap.",
        "Confirmation analysis led to action, not analysis alone.",
    ],
    "PRE.8.a": [
        "Communication-training record at induction and annually.",
        "Barrier-identification and interpreter-arrangement record — language, hearing, literacy.",
        "Observed-practice record confirming effective communication, not training alone.",
    ],
    "PRE.8.b": [
        "Written list of special situations needing enhanced communication — breaking bad news, adverse events, aggressive patient or family, death, complicated-intervention counselling.",
        "Training-pack record covering the list.",
        "Staff-awareness record for emergency, ICU, OT and ward staff.",
    ],
    "PRE.8.c": [
        "Enhanced-communication model record (for example SPIKES) adopted for breaking bad news.",
        "Note confirming the enhanced-communication conversation happened for a sampled case.",
        "Treating-doctor-led, nursing-supported record.",
    ],
    "PRE.8.d": [
        "Conduct-incident record for any unacceptable communication — abuse, disrespect, cultural or religious insult.",
        "Action-taken record by the Medical Superintendent for a confirmed breach.",
        "Training-example record so staff can recognise the line.",
    ],
    "PRE.8.e": [
        "Quarterly observation or record-sample review by the Quality Coordinator.",
        "Findings record reported to the Medical Superintendent.",
        "Action-taken record when a communication failure was found.",
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
        records = PRE_RECORDS.get(oe["oe_code"])
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

    doc_no = D(f"HCO/PRE/POL/{n:02d}")
    prepared = D(PREPARED_BY[n])
    steps = build_steps(n, oes, bodies, interps)
    oe_codes = [o["oe_code"] for o in oes]
    letters = f"{oes[0]['letter']}–{oes[-1]['letter']}"

    purpose = f"""This policy says how {HOSPITAL} meets NABH Hospitals 6th Edition standard PRE.{n}: {std_title}

It covers objective elements PRE.{n}.{letters} ({len(oes)} elements).

Chapter intent (official Standards PDF): {CHAPTER_INTENT}

This policy owns PRE.{n}. Related AAC, COP, MOM, IPC/HIC and IMS duties stay with those policies — cross-reference only. Other PRE standards stay with their own policies.

Words marked {D('like this')} are defaults. A blank marked {BLANK} must be filled before issue."""

    scope = f"""This policy applies to staff who register, admit, treat, counsel, bill, take consent from, or communicate with patients and families at {HOSPITAL}, including the {prepared}, treating doctors, nursing, Guest Relations / Patient Rights, Patient Accounts and the Quality Coordinator.

It covers {len(oes)} objective elements ({', '.join(oe_codes)}).

{hco_boundaries_clause(["AAC", "COP", "MOM"])} Spell out abbreviations on first use in training materials. OE counts/levels/asterisks stay with the official portal Standards PDF. Method notes come from the Guidebook Interpretation paragraphs (scanned PDF md5 {GUIDEBOOK_MD5})."""

    lead = (std_title[0].lower() + std_title[1:]).rstrip(".") if std_title else "patient and family rights are protected"
    policy_statement = f"""{HOSPITAL} implements PRE.{n} so that {lead}.

Staff follow written guidance, keep the records listed in the OE table, and escalate when stop-work triggers fire (if this policy includes a stop-work section)."""

    responsibility = f"""Medical Superintendent
- Accountable that PRE.{n} is resourced and followed.
- Acts on rights violations, consent failures and communication breaches that reach top leadership.

{PREPARED_BY[n]}
- Owns day-to-day implementation and records for this standard.

Guest Relations / Patient Rights Officer
- Supports rights display, counselling, complaint access and family communication as this standard requires.

Quality Coordinator
- Audits this policy {D('quarterly')}; holds training acknowledgements."""

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

This policy is reviewed {D('annually')}, and sooner after a related rights incident, consent failure or complaint cluster."""

    training = f"""Staff covered by this policy are trained at induction and {D('once a year')} after that. Training covers the What-we-do steps, non-negotiables and stop-work (if present).

Staff acknowledgement

I have read this {title} policy of {HOSPITAL}. I will follow the processes described.

Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________

(One row per staff member. The Quality Coordinator holds signed acknowledgements with the induction record.)"""

    references = f"""- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Accreditation Standards for Hospitals, 6th Edition (January 2025) — Patient Rights and Education, standard PRE.{n}. Official portal PDF (OE text, counts, levels, asterisks).
- NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — PRE.{n} interpretations (source PDF md5 {GUIDEBOOK_MD5}; OCR policies/source/hco6_pre_guidebook_ocr.txt).
- Internal documents of {HOSPITAL}: Patient Rights display and pamphlet, informed-consent list and forms, tariff and estimate process, feedback and complaints guidance, and communication models named for PRE.{n}."""

    abbreviations = f"""CAPA — Corrective and Preventive Action
CORE — Core objective element (NABH)
HCO — Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)
IEC — Information, Education and Communication
IMS — Information Management System (NABH Hospitals chapter)
NABH — National Accreditation Board for Hospitals and Healthcare Providers
NACO — National AIDS Control Organisation
OE — Objective Element
PRE — Patient Rights and Education (NABH Hospitals chapter)
PREM — Patient-Reported Experience Measure
SPIKES — Setting, Perception, Invitation/information, Knowledge, Empathy, Summarize/strategize (breaking-bad-news model named in the Guidebook)"""

    ufg = f"""HCO PRE.{n} v2 (2026-08-21). Official Standards PDF OE count {len(oes)}; levels and asterisks from portal body text (matrix agrees on levels). Asterisked: {stars}. CORE: {cores}. Achievement: {ach}. Excellence: {exc}.
Stop-work: {"YES — proposed: " + STOP_WORK_PROPOSALS[n] if has_stop else "omitted (proposed default: no stop-work on this standard)"}.
draft_label={DRAFT_LABEL!r} via hco_document_control. chapter=HCO. doc_no HCO/PRE/POL/{n:02d}.
Official chapter is 8 standards / 52 OEs (confirmed against portal summary). Guidebook interpretations from scanned PDF md5 {GUIDEBOOK_MD5}. PRE.4 statute P2 proposed (guidebook names MTP, PC-PNDT, THOA, HIV/AIDS Act 2017).
Do not touch AAC, COP or MOM."""

    distribution = distribution_dedupe(
        [
            "Medical Superintendent",
            PREPARED_BY[n],
            "Nursing Superintendent",
            "Guest Relations / Patient Rights Officer",
            "Patient Accounts In-Charge",
            "Quality Coordinator",
            f"department clinical staff covered by PRE.{n}",
        ]
    )

    draft = {
        "standard_code": f"PRE.{n}",
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
                "description": f"HCO Full 6th Edition PRE.{n} v2 draft: portal PDF OE data + Guidebook interpretations (md5 {GUIDEBOOK_MD5}); draft_label={DRAFT_LABEL}.",
            }
        ],
        "status": "draft",
        "definitions": std_title,
        "exceptions": non_negotiables(n, oes),
        "monitoring_audit": monitoring,
        "training_competency": training,
        "resources_required": hco_document_control(doc_no=doc_no, prepared_by=prepared),
        "prepared_by": prepared,
        "template_test": "hco_pre_v2_adoptable_shape",
        "subtitle": f"{PROGRAMME} — PRE.{n}.",
        "doc_no": doc_no,
        "acknowledgement_note": "The Quality Coordinator holds signed acknowledgements with the induction record.",
        "stop_work": sw,
        "edition_label": HCO_EDITION_LABEL,
        "render_basename": f"HCO.PRE.{n}",
        "programme": PROGRAMME,
    }
    return draft, statute_clause, accreditation_only, oe_codes


def write_builder(n: int) -> None:
    path = BUILD / f"build_hco_pre{n}_v2.py"
    path.write_text(
        f'''# -*- coding: utf-8 -*-
"""HCO PRE.{n} v2 — {POLICY_TITLES[n]} (HCO Full, 6th Edition).

Generated builder. Regenerate with: python3 generate_hco_pre_v2.py
Explicit draft_label via hco_pre_v2_common.hco_document_control.
Does NOT overwrite SHCO PRE, HCO AAC, HCO COP or HCO MOM files.
"""
from __future__ import annotations

import sys
from generate_hco_pre_v2 import emit_standard

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
        f"hco_pre{n}_v2_draft.json",
        f"HCO.PRE.{n}_v2_preview.md",
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
    assert total == 52, total
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
        assert DRAFT_LABEL in draft["resources_required"]
        joined = "\n".join(draft["procedure_steps"])
        assert joined.count("Method note (from guidebook interpretation):") == len(oe_codes)
        assert "Prepared by (designation):" in draft["resources_required"]
        dist_parts = [x.strip() for x in re.split(r"[,;\n]", draft["distribution"]) if x.strip()]
        assert len(dist_parts) == len(set(p.casefold() for p in dist_parts)), dist_parts
        emit_pre_v2(
            draft,
            f"hco_pre{n}_v2_draft.json",
            f"HCO.PRE.{n}_v2_preview.md",
            oe_codes=oe_codes,
            statute_clause=statute_clause,
            accreditation_only=accreditation_only,
            edition_label=HCO_EDITION_LABEL,
            drafts_dir=HCO_DRAFTS,
            preview_dir=HCO_PREVIEW,
        )
        print(
            f"PRE.{n}: {len(oe_codes)} OEs; stop_work={'yes' if draft['stop_work'] else 'no'}; "
            f"prepared_by={PREPARED_BY[n]!r}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
