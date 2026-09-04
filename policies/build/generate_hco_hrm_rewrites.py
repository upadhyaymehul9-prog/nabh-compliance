# -*- coding: utf-8 -*-
"""
generate_hco_hrm_rewrites.py
Generates HCO HRM.1-5 v2 rewrite-reference DOCX files.

Pipeline : python-docx, identical to generate_hco_fms_rewrites.py.
Output   : policies/build/rewrite_reference/HCO_HRM_N_v2_REWRITE_DRAFT.docx
Source   : hrm1_content.txt … hrm5_content.txt (Downloads) — content
           embedded directly as string literals below.
"""
import os
from docx import Document

HN  = "«Hospital Name»"
OUT = "policies/build/rewrite_reference"
os.makedirs(OUT, exist_ok=True)


# ── Helpers (identical to generate_hco_fms_rewrites.py) ───────────────────────

def h(doc, lv, txt):
    return doc.add_paragraph(txt, style={0: "Title", 1: "Heading 1", 2: "Heading 2"}[lv])

def p(doc, txt=""):
    return doc.add_paragraph(txt, style="Normal")

def ln(doc, txt):
    return doc.add_paragraph(txt, style="List Number")

def lb(doc, txt):
    return doc.add_paragraph(txt, style="List Bullet")

def tbl(doc, rows, cols):
    t = doc.add_table(rows=rows, cols=cols)
    try:
        t.style = "Table Grid"
    except KeyError:
        pass
    return t

def doc_ctrl(doc, no, prep, appr="Medical Superintendent"):
    dc = tbl(doc, 6, 4)
    for ri, (a, b, c, d) in enumerate([
        ("Document No.", no,        "Version",                "1.0"),
        ("Issue No.",    "01",       "Review due",             "One year from implementation"),
        ("Date created", "________", "Date of implementation", "________"),
    ]):
        dc.cell(ri, 0).text = a; dc.cell(ri, 1).text = b
        dc.cell(ri, 2).text = c; dc.cell(ri, 3).text = d
    for ri, (lbl, txt) in enumerate([
        ("Prepared by", f"{prep}  Name: ________  Signature: ________"),
        ("Reviewed by", "Quality Coordinator  Name: ________  Signature: ________"),
        ("Approved by", f"{appr}  Name: ________  Signature: ________"),
    ], start=3):
        dc.cell(ri, 0).text = lbl
        c1 = dc.cell(ri, 1); c1.text = txt; c1.merge(dc.cell(ri, 3))

def gov_tbl(doc, rows):
    t = tbl(doc, len(rows) + 1, 2)
    t.cell(0, 0).text = "Role"; t.cell(0, 1).text = "Responsibility"
    for ri, (role, resp) in enumerate(rows, 1):
        t.cell(ri, 0).text = role; t.cell(ri, 1).text = resp

def abbrev_tbl(doc, rows):
    t = tbl(doc, len(rows) + 1, 2)
    t.cell(0, 0).text = "Abbreviation"; t.cell(0, 1).text = "Meaning"
    for ri, (a, m) in enumerate(rows, 1):
        t.cell(ri, 0).text = a; t.cell(ri, 1).text = m

def trace_tbl(doc, rows):
    t = tbl(doc, len(rows) + 1, 4)
    for ci, hdr in enumerate(("OE", "Level", "Where addressed", "Responsible")):
        t.cell(0, ci).text = hdr
    for ri, row in enumerate(rows, 1):
        for ci, v in enumerate(row):
            t.cell(ri, ci).text = v

def sig_tbl(doc):
    t = tbl(doc, 4, 4)
    for ci, hdr in enumerate(("Staff name", "Designation", "Signature", "Date")):
        t.cell(0, ci).text = hdr
    for ri in range(1, 4):
        for ci in range(4):
            t.cell(ri, ci).text = "________"

def hrm_disclaimer(doc):
    p(doc,
      f"This document is a template prepared for the guidance of {HN} and must be reviewed, "
      f"adapted and formally approved by {HN} before use. Every entry marked ________ "
      f"must be completed before the document is issued.")
    p(doc,
      f"The requirements in this document are accreditation requirements of the NABH Full "
      f"Accreditation Standards for Hospitals, 6th Edition, not duties under a named Act of "
      f"Parliament. Statutory duties that arise under other documents of {HN} remain those "
      f"documents. {HN} is responsible for verifying any statutory duty that applies to it; "
      f"this document does not constitute legal advice.")
    p(doc,
      f"The clinical and technical content reflects recognised national and international guidance "
      f"current at the date of preparation. {HN} remains responsible for verifying that it is "
      f"current and consistent with the edition of the accreditation standard against which it "
      f"is being assessed.")
    p(doc,
      "This document is not issued by, endorsed by, or affiliated with NABH or any other body "
      "named in it. Wording is original; no text has been reproduced from the standards, rules "
      "or guidelines referenced.")

def save_and_verify(doc, fname):
    import sys
    out = sys.stdout
    def pr(s):
        try:
            out.write(s + "\n")
        except UnicodeEncodeError:
            out.write(s.encode("ascii", "replace").decode() + "\n")
    pr(f"\n=== {fname} ===")
    pr(f"  Total paras: {len(doc.paragraphs)}")
    path = os.path.join(OUT, fname)
    doc.save(path)
    pr(f"  Saved: {path}")

# Shared constants
_HR  = "HR In-Charge / Personnel Officer"
_MS  = "Medical Superintendent"
_QC  = "Quality Coordinator"

HRM_ABBREVS_BASE = [
    ("HCO",  "Hospital (Full Accreditation programme under NABH Hospitals 6th Edition)"),
    ("HR",   "Human Resources"),
    ("HRM",  "Human Resource Management (NABH Hospitals 6th Edition chapter)"),
    ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
    ("OE",   "Objective Element"),
]


# ══════════════════════════════════════════════════════════════════════════════
# HRM.1 — Human Resource Planning and Governance   (no stop-work)
# ══════════════════════════════════════════════════════════════════════════════
def gen_hrm1():
    doc = Document()
    h(doc, 0, "Policy on Human Resource Planning and Governance")
    p(doc, HN)
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/HRM/POL/01", _HR)
    p(doc, "A blank marked ________ must be completed before issue.")
    h(doc, 1, "Statement of intent")
    p(doc, f"{HN} plans its workforce so that the right number and mix of skilled staff is "
           "available now and in the future, not just when a crisis makes the gap obvious.")
    h(doc, 1, "1. Purpose")
    p(doc, f"This policy explains how {HN} plans staffing to meet patient care needs, defines "
           "jobs and reporting lines, checks new staff before they start, and learns from staff who leave.")
    p(doc, "This policy does not cover recruitment steps, induction training, or staff appraisal "
           "— those are covered in other hospital policies.")
    h(doc, 1, "2. Scope")
    p(doc, f"This policy applies to the HR In-Charge / Personnel Officer, department heads, and "
           f"the Medical Superintendent, for every category of staff — full-time, part-time, "
           f"employed, honorary, voluntary and temporary.")
    h(doc, 1, "3. Policy standards")
    p(doc, f"{HN} prepares an annual workforce plan against patient volume, services and technology "
           "in use; keeps enough staff, in the right mix, to meet patient needs; has a tested "
           "contingency plan for staff shortages; defines a job description for every staff category; "
           "background-checks new staff; documents reporting lines for every category of staff; and "
           "uses exit interviews to improve HR practice.")
    h(doc, 1, "4. Non-negotiable rules")
    ln(doc, "Do not let the workforce plan go a year without being compared against actual patient "
            "volume, services and staffing.")
    ln(doc, "Do not leave a staffing shortfall unaddressed — trigger the contingency plan.")
    ln(doc, "Do not let any staff category go without a defined job description and specification.")
    ln(doc, "Do not skip the background check on a new staff member, or delay it beyond one month of joining.")
    ln(doc, "Do not leave a staff role without a documented reporting line.")
    ln(doc, "Do not let exit-interview findings sit unread — they must feed back into HR practice.")
    ln(doc, f"Staff who see any of these rules broken report it the same shift to the "
            f"HR In-Charge / Personnel Officer or the Medical Superintendent.")
    h(doc, 1, "5. What we do")
    h(doc, 2, "5.1 Plan the workforce every year")
    p(doc, f"The HR In-Charge / Personnel Officer prepares a workforce plan every year, comparing "
           "current staff numbers and skill mix against the hospital's mission, patient volume and mix, "
           "services offered, and medical technology in use, with input from department heads. Recognised "
           "staffing methods are used to set levels against the strategic and operational plan. Where the "
           "year's actual staffing varies from the plan, the corrective action taken is recorded and "
           "carried into the next year's plan.")
    h(doc, 2, "5.2 Keep enough staff, in the right mix")
    p(doc, f"{HN} keeps a number and mix of staff commensurate with workload and clinical need. "
           "Nursing staffing follows a published guideline (for example, WHO's Workload Indicators of "
           "Staffing Need method, or another recognised nursing staffing guideline). The "
           "HR In-Charge / Personnel Officer compares sanctioned against actual strength by department "
           "on a regular schedule and escalates an unresolved shortfall to the Medical Superintendent. "
           "Any shortfall triggers the contingency plan in 5.3.")
    h(doc, 2, "5.3 Plan for staff shortages before they happen")
    p(doc, f"The hospital keeps a written contingency plan for shift-by-shift, short-term and "
           "long-term workforce shortages, including unplanned ones. The plan may include reprioritising "
           "tasks, reallocating tasks across available staff, and drawing on a pool of filler staff "
           "such as previous employees or agency-sourced casual staff. Every shortage event is logged "
           "with its cause, the measure used, and the outcome. The plan itself is tested at a regular "
           "interval to confirm it still works.")
    h(doc, 2, "5.4 Define every job")
    p(doc, f"Every staff category at {HN} — full-time, part-time, employed, honorary, voluntary or "
           "temporary — has a job description and specification laying down the job's content and the "
           "qualifications, skills and experience needed. A role requiring the skills of a doctor or "
           "nurse carries a minimum qualification of MBBS or GNM respectively, unless a government or "
           "statutory body has granted an exemption. The HR In-Charge / Personnel Officer holds the "
           "current set of job descriptions; a new hire signs to confirm they have received and "
           "understood theirs.")
    h(doc, 2, "5.5 Check new staff before they start")
    p(doc, f"{HN} performs a background check on every new staff member, using a defined method, "
           "either before the person joins or within one month of joining. The "
           "HR In-Charge / Personnel Officer keeps a register recording the method used, the date "
           "completed, and the outcome for each new hire. A staff member with no background check on "
           "file is escalated to the Medical Superintendent — this is not left for later.")
    h(doc, 2, "5.6 Document who reports to whom")
    p(doc, "Reporting relationships are defined for every category of staff, documented as an "
           "organisation chart showing hierarchy, line of control and functions at each level. The "
           "chart is disseminated to all stakeholders, and reporting relationships are also defined "
           "at department or service level. The HR In-Charge / Personnel Officer holds the current chart.")
    h(doc, 2, "5.7 Learn from staff who leave")
    p(doc, f"{HN} conducts exit interviews and uses them to improve HR practice. A personal interview "
           "is the default method; taking part is voluntary for the departing staff member. The "
           "HR In-Charge / Personnel Officer compiles findings at a regular interval into a trend "
           "report for the Medical Superintendent and, where the hospital has one, the governing body, "
           "with proposed HR improvements tracked to closure.")
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        (_HR,
         "Owns the workforce plan, staffing comparison, contingency plan, job descriptions, "
         "background checks, organisation chart, and exit-interview trend reports."),
        ("Department heads",
         "Provide input to the workforce plan; confirm reporting lines and job content for their department."),
        (_MS,
         "Accountable that this policy is followed; receives escalations on unresolved staffing "
         "shortfalls and exit-interview trend reports."),
    ])
    h(doc, 1, "7. Quality monitoring")
    p(doc, "The HR In-Charge / Personnel Officer reviews a sample of records under this policy "
           "periodically against the steps in Section 5, confirming the workforce plan, contingency-plan "
           "tests, job descriptions, background checks, the organisation chart, and exit-interview trend "
           "reports are current. This policy itself is reviewed every year, and sooner if there is a "
           "major change in hospital services or staffing structure.")
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc, f"Staff covered by this policy — the HR In-Charge / Personnel Officer and department heads "
           "— are trained on this policy when they take up the role, and again every year after that. "
           "Training covers what's in Section 5 and the non-negotiable rules.")
    p(doc, f"I have read the Policy on Human Resource Planning and Governance of {HN}. I will follow the processes described.")
    sig_tbl(doc)
    h(doc, 1, "9. Distribution")
    p(doc, "HR In-Charge / Personnel Officer; department heads; Medical Superintendent; governing body, "
           "where applicable.")
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("GNM",  "General Nursing and Midwifery"),
    ] + HRM_ABBREVS_BASE + [
        ("MBBS", "Bachelor of Medicine, Bachelor of Surgery"),
        ("WISN", "Workload Indicators of Staffing Need (WHO method)"),
    ])
    h(doc, 1, "11. Traceability to NABH HCO Full Accreditation 6th Edition HRM.1")
    p(doc, "This table is an index. It is not how the policy is organised. An asterisk in the "
           "Level column means documentation of the process is required.")
    trace_tbl(doc, [
        ("HRM.1.a", "Commitment",
         "Section 3; 5.1", _HR),
        ("HRM.1.b", "CORE*",
         "Section 3; 5.2", _HR),
        ("HRM.1.c", "Achievement",
         "Section 3; 5.3", _HR),
        ("HRM.1.d", "Commitment",
         "Section 3; 5.4", _HR),
        ("HRM.1.e", "Commitment",
         "Section 3; 5.5", _HR),
        ("HRM.1.f", "Commitment*",
         "Section 3; 5.6", _HR),
        ("HRM.1.g", "Achievement",
         "Section 3; 5.7", _HR),
    ])
    h(doc, 1, "12. Required Records / Evidence Checklist")
    h(doc, 2, "HRM.1.a — Human resource planning supports current and future patient needs.")
    lb(doc, "Annual workforce plan comparing current and projected staffing against services and patient volume.")
    lb(doc, "Department-head input record into the plan.")
    lb(doc, "Corrective-action record for a variance found during the year.")
    h(doc, 2, "HRM.1.b — Adequate number and mix of staff maintained.")
    lb(doc, "Sanctioned-versus-actual staffing comparison record by department.")
    lb(doc, "Staffing-norm reference used for nursing.")
    lb(doc, "Escalation record for an unresolved shortfall.")
    h(doc, 2, "HRM.1.c — Contingency plans for workforce shortages.")
    lb(doc, "Written contingency plan for long- and short-term workforce shortages, including unplanned shortages.")
    lb(doc, "Shortage-event log with cause, measure used and outcome.")
    lb(doc, "Test record of the contingency plan.")
    h(doc, 2, "HRM.1.d — Job specification and job description defined.")
    lb(doc, "Job description on file for each staff category, including qualification, skill and experience requirements.")
    lb(doc, "Signed acknowledgement record from a new hire receiving their job description.")
    lb(doc, "Minimum-qualification exemption record, where applicable.")
    h(doc, 2, "HRM.1.e — Background check of new staff.")
    lb(doc, "Background-check register recording method, date and outcome per new hire.")
    lb(doc, "Completion record before or within one month of joining.")
    lb(doc, "Escalation record for any staff member with no background check on file.")
    h(doc, 2, "HRM.1.f — Reporting relationships defined.")
    lb(doc, "Current organisation structure or chart showing hierarchy and reporting lines.")
    lb(doc, "Department- or service-level reporting-relationship record.")
    lb(doc, "Dissemination record to stakeholders.")
    h(doc, 2, "HRM.1.g — Exit interviews conducted and used.")
    lb(doc, "Completed exit-interview record for a departing staff member.")
    lb(doc, "Trend report compiled from exit interviews.")
    lb(doc, "HR-improvement action record from exit-interview findings.")
    h(doc, 1, "13. References")
    lb(doc, "NABH Accreditation Standards for Hospitals, 6th Edition — standard HRM.1.")
    lb(doc, "NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.1 interpretations.")
    h(doc, 1, "Disclaimer")
    hrm_disclaimer(doc)
    save_and_verify(doc, "HCO_HRM_1_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# HRM.2 — Staff Recruitment   (no stop-work)
# ══════════════════════════════════════════════════════════════════════════════
def gen_hrm2():
    doc = Document()
    h(doc, 0, "Policy on Staff Recruitment")
    p(doc, HN)
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/HRM/POL/02", _HR)
    p(doc, "A blank marked ________ must be completed before issue.")
    h(doc, 1, "Statement of intent")
    p(doc, f"{HN} recruits staff through a transparent, documented process that checks fitness, "
           "character and conduct before someone starts patient-facing work.")
    h(doc, 1, "1. Purpose")
    p(doc, f"This policy explains how {HN} recruits staff, checks their fitness to work, sets "
           "standards of conduct, and documents its administrative procedures.")
    p(doc, "This policy does not cover induction training, job descriptions, or staff appraisal "
           "— those are covered in other hospital policies.")
    h(doc, 1, "2. Scope")
    p(doc, f"This policy applies to the HR In-Charge / Personnel Officer and every category of "
           f"staff being recruited at {HN}.")
    h(doc, 1, "3. Policy standards")
    p(doc, f"{HN} recruits against written, transparent guidance; conducts a lawful, consent-based "
           "pre-employment medical examination; defines and implements a code of conduct that protects "
           "patient confidentiality; and documents its administrative HR procedures.")
    h(doc, 1, "4. Non-negotiable rules")
    ln(doc, "Do not recruit any staff category without written, documented guidance covering that category.")
    ln(doc, "Do not perform any pre-employment test without the candidate's consent and without it being lawful.")
    ln(doc, "Do not let a staff member start work without having signed the code of conduct.")
    ln(doc, "Do not leave administrative procedures — attendance, leave, conduct, replacement — undocumented.")
    ln(doc, f"Staff who see any of these rules broken report it the same shift to the "
            f"HR In-Charge / Personnel Officer or the Medical Superintendent.")
    h(doc, 1, "5. What we do")
    h(doc, 2, "5.1 Recruit against written, transparent guidance")
    p(doc, f"Written guidance governs recruitment at {HN}, based on defined criteria for each staff "
           "category, ensuring an adequate number and skill mix to provide the hospital's services. "
           "The procedure confirms a candidate has the necessary registration, qualifications, skills "
           "and experience before appointment, and follows statutory requirements where they apply. "
           "The process is documented and carried out transparently. The HR In-Charge / Personnel "
           "Officer maintains a recruitment register logging the vacancy, candidates considered, "
           "selection rationale and fill date.")
    h(doc, 2, "5.2 Confirm fitness to work, lawfully")
    p(doc, "A pre-employment medical examination is conducted to confirm a candidate is fit to provide "
           "safe care. The scope of testing is guided by the nature of the role, but any test performed "
           "follows the law of the land — for example, pre-employment HIV testing without the candidate's "
           "consent is illegal and is not this hospital's practice. The HR In-Charge / Personnel Officer "
           "holds the examination record with the personnel file.")
    h(doc, 2, "5.3 Set and sign a code of conduct")
    p(doc, f"{HN} defines and implements a code of conduct outlining the do's and don'ts of workplace "
           "behaviour, aligned with the hospital's values and ethics framework and including protection "
           "of patient confidentiality. Staff sign the code at the time of joining; it may form part "
           "of the hospital's service rules. The HR In-Charge / Personnel Officer holds signed "
           "acknowledgements with the personnel file.")
    h(doc, 2, "5.4 Document HR administrative procedures")
    p(doc, "Administrative procedures for human resource management are documented — at minimum "
           "attendance, leave, conduct and replacement. The HR In-Charge / Personnel Officer maintains "
           "the current procedure set and covers it during induction.")
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        (_HR,
         "Owns the recruitment register, medical examination records, code-of-conduct "
         "acknowledgements, and administrative procedure documentation."),
        (_MS, "Accountable that this policy is followed."),
    ])
    h(doc, 1, "7. Quality monitoring")
    p(doc, "The HR In-Charge / Personnel Officer reviews a sample of recruitment files periodically "
           "against the steps in Section 5, confirming registration/qualification checks, medical "
           "examination and consent records, and signed codes of conduct are on file. This policy "
           "itself is reviewed every year.")
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc, "Staff covered by this policy are trained on it when they take up the role, and again "
           "every year after that.")
    p(doc, f"I have read the Policy on Staff Recruitment of {HN}. I will follow the processes described.")
    sig_tbl(doc)
    h(doc, 1, "9. Distribution")
    p(doc, "HR In-Charge / Personnel Officer; Medical Superintendent; department heads.")
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, HRM_ABBREVS_BASE)
    h(doc, 1, "11. Traceability to NABH HCO Full Accreditation 6th Edition HRM.2")
    p(doc, "This table is an index. It is not how the policy is organised. An asterisk in the "
           "Level column means documentation of the process is required.")
    trace_tbl(doc, [
        ("HRM.2.a", "CORE*",   "Section 3; 5.1", _HR),
        ("HRM.2.b", "Commitment", "Section 3; 5.2", _HR),
        ("HRM.2.c", "CORE",    "Section 3; 5.3", _HR),
        ("HRM.2.d", "Commitment*", "Section 3; 5.4", _HR),
    ])
    h(doc, 1, "12. Required Records / Evidence Checklist")
    h(doc, 2, "HRM.2.a — Written guidance governs recruitment.")
    lb(doc, "Written recruitment guidance document.")
    lb(doc, "Recruitment register — vacancy, candidates, selection rationale, fill date.")
    lb(doc, "Statutory-requirement compliance record where applicable.")
    h(doc, 2, "HRM.2.b — Pre-employment medical examination.")
    lb(doc, "Pre-employment medical examination record on file.")
    lb(doc, "Consent record for any testing performed, confirming no non-consensual testing.")
    lb(doc, "Fitness-to-work determination record.")
    h(doc, 2, "HRM.2.c — Code of conduct defined and implemented.")
    lb(doc, "Written code of conduct document.")
    lb(doc, "Signed staff acknowledgement at joining.")
    lb(doc, "Confidentiality-protection clause record within the code.")
    h(doc, 2, "HRM.2.d — Administrative HR procedures documented.")
    lb(doc, "Documented administrative procedures — attendance, leave, conduct, replacement.")
    lb(doc, "Current-version record held by HR.")
    lb(doc, "Induction coverage record for these procedures.")
    h(doc, 1, "13. References")
    lb(doc, "NABH Accreditation Standards for Hospitals, 6th Edition — standard HRM.2.")
    lb(doc, "NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.2 interpretations.")
    h(doc, 1, "Disclaimer")
    hrm_disclaimer(doc)
    save_and_verify(doc, "HCO_HRM_2_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# HRM.3 — Staff Induction Training   (no stop-work)
# ══════════════════════════════════════════════════════════════════════════════
def gen_hrm3():
    doc = Document()
    h(doc, 0, "Policy on Staff Induction Training")
    p(doc, HN)
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/HRM/POL/03", _HR)
    p(doc, "A blank marked ________ must be completed before issue.")
    h(doc, 1, "Statement of intent")
    p(doc, f"{HN} orients every new person — staff, volunteer, student or trainee — to the hospital "
           "and to their specific role before they are left to work unsupervised.")
    h(doc, 1, "1. Purpose")
    p(doc, f"This policy explains what induction training covers at {HN} and when it is completed.")
    p(doc, "This policy does not cover ongoing professional training, job-specific clinical training, "
           "or performance appraisal — those are covered in other hospital policies.")
    h(doc, 1, "2. Scope")
    p(doc, f"This policy applies to the HR In-Charge / Personnel Officer, department heads, and "
           f"every staff member, consultant, outsourced worker, volunteer, student and trainee "
           f"joining {HN}.")
    h(doc, 1, "3. Policy standards")
    p(doc, f"{HN} provides induction training within one month of joining, covering the hospital's "
           "vision and values, staff and patient rights, safety, CPR, infection control, service "
           "standards, administrative procedures, department-level policies, and information-systems use.")
    h(doc, 1, "4. Non-negotiable rules")
    ln(doc, "Do not let a new staff member, consultant, outsourced worker, volunteer, student or "
            "trainee go without induction training within one month of joining.")
    ln(doc, "Do not skip any of the required induction topics: vision/mission/values, staff and patient "
            "rights, safety, CPR, infection control, service standards, administrative procedures, "
            "department-level orientation, and information-systems training.")
    ln(doc, "Do not let department-level orientation be skipped in favour of organisation-level "
            "induction alone.")
    ln(doc, f"Staff who see any of these rules broken report it the same shift to the "
            f"HR In-Charge / Personnel Officer or the Medical Superintendent.")
    h(doc, 1, "5. What we do")
    h(doc, 2, "5.1 Provide induction within one month")
    p(doc, f"{HN} provides induction training to its staff, including doctors, consultants "
           "(including visiting), outsourced staff, volunteers, students and trainees, oriented to "
           "the hospital and to their specific assignment. Induction is completed within one month "
           "of joining and covers every topic in 5.2 through 5.9. Contents may be issued as a "
           "booklet; separate induction may run at organisational and departmental level. The "
           "HR In-Charge / Personnel Officer keeps the training record.")
    h(doc, 2, "5.2 Orient to vision, mission and values")
    p(doc, "Induction includes orientation to the hospital's vision, mission and values, so that "
           "staff — including outsourced staff — are aware of and can correctly interpret them.")
    h(doc, 2, "5.3 Cover staff and patient rights")
    p(doc, "Induction includes awareness of staff rights and responsibilities and of patient rights "
           "and responsibilities, so that staff can comprehend the implications of both and can "
           "identify and report a violation of patient rights when it occurs.")
    h(doc, 2, "5.4 Train on safety")
    p(doc, "Induction includes training on safety — patient, visitor and staff safety, including "
           "the hospital's emergency codes.")
    h(doc, 2, "5.5 Train on CPR")
    p(doc, "Induction includes training on cardio-pulmonary resuscitation. At minimum, doctors, "
           "nursing staff, technologists and rehabilitation staff are trained to at least basic life "
           "support; doctors and nurses in intensive care or high-dependency units undergo appropriate "
           "advanced training (for example ACLS, PALS or NRP, or an equivalent). A staff member with "
           "a valid existing training certificate does not need to repeat it.")
    h(doc, 2, "5.6 Train on infection prevention and control")
    p(doc, "Induction includes training in hospital infection prevention and control — the policies, "
           "procedures and practices of the infection prevention and control programme.")
    h(doc, 2, "5.7 Orient to service standards")
    p(doc, "Induction includes orientation to the hospital's service standards, so that staff are "
           "trained to implement them.")
    h(doc, 2, "5.8 Orient to administrative and department-level procedures")
    p(doc, "Induction includes an orientation on administrative procedures — attendance, leave, "
           "conduct and similar matters — and awareness of organisation-wide policies. It also "
           "includes an orientation on the policies and procedures of the specific department, unit, "
           "service or programme the staff member will work in, delivered at that level.")
    h(doc, 2, "5.9 Train on information systems")
    p(doc, "Staff are trained on information systems, information security, information use and "
           "management, according to their job responsibility, job description and data and "
           "information needs. Where the hospital uses electronic health records, staff who access, "
           "review or document in the EMR are trained to ensure it is used correctly.")
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        (_HR,
         "Owns the induction schedule, content and training records at organisational level."),
        ("Department heads",
         "Deliver department/unit/service-level induction content."),
        (_MS, "Accountable that this policy is followed."),
    ])
    h(doc, 1, "7. Quality monitoring")
    p(doc, "The HR In-Charge / Personnel Officer reviews a sample of induction records periodically "
           "against the steps in Section 5, confirming every required topic was covered within one "
           "month of joining. This policy itself is reviewed every year.")
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc, "Staff covered by this policy are trained on it when they take up the role, and again "
           "every year after that.")
    p(doc, f"I have read the Policy on Staff Induction Training of {HN}. I will follow the processes described.")
    sig_tbl(doc)
    h(doc, 1, "9. Distribution")
    p(doc, "HR In-Charge / Personnel Officer; department heads; Medical Superintendent.")
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("ACLS", "Advanced Cardiac Life Support"),
        ("CPR",  "Cardio-Pulmonary Resuscitation"),
        ("EMR",  "Electronic Medical Record"),
    ] + HRM_ABBREVS_BASE + [
        ("NRP",  "Neonatal Resuscitation Program"),
        ("PALS", "Paediatric Advanced Life Support"),
    ])
    h(doc, 1, "11. Traceability to NABH HCO Full Accreditation 6th Edition HRM.3")
    p(doc, "This table is an index. It is not how the policy is organised. An asterisk in the "
           "Level column means documentation of the process is required.")
    trace_tbl(doc, [
        ("HRM.3.a", "CORE",       "Section 3; 5.1", _HR),
        ("HRM.3.b", "Commitment", "Section 3; 5.2", _HR),
        ("HRM.3.c", "Commitment", "Section 3; 5.3", _HR),
        ("HRM.3.d", "Commitment", "Section 3; 5.4", _HR),
        ("HRM.3.e", "Commitment", "Section 3; 5.5", _HR),
        ("HRM.3.f", "Commitment", "Section 3; 5.6", _HR),
        ("HRM.3.g", "Commitment", "Section 3; 5.7", _HR),
        ("HRM.3.h", "Commitment", "Section 3; 5.8", _HR),
        ("HRM.3.i", "Commitment", "Section 3; 5.8", "Department heads"),
        ("HRM.3.j", "Commitment", "Section 3; 5.9", _HR),
    ])
    h(doc, 1, "12. Required Records / Evidence Checklist")
    h(doc, 2, "HRM.3.a — Induction training provided.")
    lb(doc, "Induction-training record within one month of joining.")
    lb(doc, "Attendance record covering doctors, consultants, outsourced staff, volunteers, students and trainees.")
    lb(doc, "Induction-content record covering HRM.3.b–j.")
    h(doc, 2, "HRM.3.b — Vision, mission and values orientation.")
    lb(doc, "Vision, mission and values orientation record within induction.")
    lb(doc, "Staff-awareness confirmation record.")
    h(doc, 2, "HRM.3.c — Staff and patient rights and responsibilities.")
    lb(doc, "Staff-rights and patient-rights training record.")
    lb(doc, "Violation-identification-and-reporting awareness confirmation.")
    h(doc, 2, "HRM.3.d — Safety training.")
    lb(doc, "Safety training record — patient, visitor, staff safety, emergency codes.")
    lb(doc, "Emergency-code awareness confirmation.")
    h(doc, 2, "HRM.3.e — CPR training.")
    lb(doc, "CPR training record at the appropriate level (BLS minimum; advanced for ICU/HDU staff).")
    lb(doc, "Valid-certificate exemption record, where applicable.")
    h(doc, 2, "HRM.3.f — Infection prevention and control training.")
    lb(doc, "Hospital infection prevention and control training record within induction.")
    h(doc, 2, "HRM.3.g — Service standards orientation.")
    lb(doc, "Service-standards orientation record within induction.")
    h(doc, 2, "HRM.3.h — Administrative procedures orientation.")
    lb(doc, "Administrative-procedures orientation record — attendance, leave, conduct.")
    lb(doc, "Organisation-wide policy-awareness record.")
    h(doc, 2, "HRM.3.i — Department/unit-level orientation.")
    lb(doc, "Department, unit, service or programme-level policy-and-procedure orientation record.")
    lb(doc, "Delivery-location record confirming it was given at that level.")
    h(doc, 2, "HRM.3.j — Information systems training.")
    lb(doc, "Information-systems, security and data-use training record.")
    lb(doc, "EMR-access training record, where the hospital uses electronic health records.")
    h(doc, 1, "13. References")
    lb(doc, "NABH Accreditation Standards for Hospitals, 6th Edition — standard HRM.3.")
    lb(doc, "NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.3 interpretations.")
    h(doc, 1, "Disclaimer")
    hrm_disclaimer(doc)
    save_and_verify(doc, "HCO_HRM_3_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# HRM.4 — Professional Training and Development   (no stop-work)
# ══════════════════════════════════════════════════════════════════════════════
def gen_hrm4():
    doc = Document()
    h(doc, 0, "Policy on Professional Training and Development")
    p(doc, HN)
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/HRM/POL/04", _HR)
    p(doc, "A blank marked ________ must be completed before issue.")
    h(doc, 1, "Statement of intent")
    p(doc, f"{HN} keeps its staff's skills current through an ongoing, documented training programme, "
           "and checks that training actually changes what happens at the workplace.")
    h(doc, 1, "1. Purpose")
    p(doc, f"This policy explains how {HN} plans, records, and evaluates staff professional training "
           "and development, and how it supports continuing learning.")
    p(doc, "This policy does not cover induction training or job-specific clinical training — those "
           "are covered in other hospital policies.")
    h(doc, 1, "2. Scope")
    p(doc, f"This policy applies to the HR In-Charge / Personnel Officer, department heads, and "
           f"every category of staff, including doctors and outsourced staff where applicable.")
    h(doc, 1, "3. Policy standards")
    p(doc, f"{HN} runs training and development against written guidance; keeps a training record "
           "for every session; retrains staff when responsibilities or equipment change; collects "
           "feedback to improve the programme; evaluates whether training actually worked; and "
           "supports staff in continuing professional development.")
    h(doc, 1, "4. Non-negotiable rules")
    ln(doc, "Do not run training and development without written guidance covering training-needs "
            "identification, methodology, documentation, assessment and a training calendar.")
    ln(doc, "Do not leave a training session unrecorded — title, trainer, date, duration and "
            "trainee list with signatures are mandatory.")
    ln(doc, "Do not skip training when a staff member's job responsibilities change or new "
            "equipment is introduced.")
    ln(doc, "Do not run the training programme without a feedback mechanism covering course "
            "material, facilities and trainer capability.")
    ln(doc, "Do not treat training as complete without evaluating whether it worked, both "
            "immediately and after time has passed.")
    ln(doc, f"Staff who see any of these rules broken report it the same shift to the "
            f"HR In-Charge / Personnel Officer or the Medical Superintendent.")
    h(doc, 1, "5. What we do")
    h(doc, 2, "5.1 Run training against written guidance")
    p(doc, f"Written guidance governs training and development at {HN}: a training manual covering "
           "identification of training needs, methodology, documentation, assessment, impact "
           "evaluation and a training calendar. At minimum, staff are trained on occupational safety "
           "and soft skills, and educated on patient-centred care — respecting patient preferences, "
           "shared decision-making and integrated care. Training covers all staff categories, "
           "including doctors and outsourced staff where applicable.")
    h(doc, 2, "5.2 Keep the training record")
    p(doc, "The HR In-Charge / Personnel Officer maintains the training record for every session: "
           "at minimum the title, trainer(s), date, duration and list of trainees with signatures. "
           "Contents are captured where possible; records may be kept digitally.")
    h(doc, 2, "5.3 Retrain when the job or the equipment changes")
    p(doc, "Training also occurs when job responsibilities change or new equipment is introduced, "
           "focused on the revised responsibilities or the newly introduced equipment and technology. "
           "For new equipment, operating staff are trained on both operational use and daily "
           "maintenance before working with it independently.")
    h(doc, 2, "5.4 Collect feedback to improve the programme")
    p(doc, "Feedback mechanisms are in place for improving the training and development programme, "
           "covering both internal and external training — appropriateness of course material, "
           "training facilities and trainer capability.")
    h(doc, 2, "5.5 Evaluate whether training worked")
    p(doc, f"{HN} evaluates training effectiveness immediately after training (for example a pre- "
           "and post-test) and again after a defined period has lapsed, to confirm the training "
           "improved workplace competency. Incident reports and assessment non-conformities are "
           "useful inputs for the later check. The evaluation covers knowledge, skills and attitude; "
           "retraining is provided where the evaluation shows it is needed.")
    h(doc, 2, "5.6 Support continuing professional development")
    p(doc, f"{HN} supports continuing professional development and learning, so staff can keep up "
           "with advancements in their field — encouraging and resourcing attendance at courses or "
           "conferences, and providing access to distance learning or e-learning. The hospital "
           "specifies minimum mandatory training hours every staff member attends each year.")
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        (_HR,
         "Owns the training manual, training records, feedback mechanism, effectiveness "
         "evaluations, and CPD support arrangements."),
        ("Department heads",
         "Identify training needs arising from job or equipment changes in their department."),
        (_MS,
         "Accountable that this policy is followed; sets minimum mandatory annual training hours."),
    ])
    h(doc, 1, "7. Quality monitoring")
    p(doc, "The HR In-Charge / Personnel Officer reviews a sample of training records periodically "
           "against the steps in Section 5, confirming sessions are documented, feedback is "
           "collected, and effectiveness evaluations and any resulting retraining are on file. "
           "This policy itself is reviewed every year.")
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc, "Staff covered by this policy are trained on it when they take up the role, and again "
           "every year after that.")
    p(doc, f"I have read the Policy on Professional Training and Development of {HN}. I will follow the processes described.")
    sig_tbl(doc)
    h(doc, 1, "9. Distribution")
    p(doc, "HR In-Charge / Personnel Officer; department heads; Medical Superintendent.")
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("CPD", "Continuing Professional Development"),
    ] + HRM_ABBREVS_BASE)
    h(doc, 1, "11. Traceability to NABH HCO Full Accreditation 6th Edition HRM.4")
    p(doc, "This table is an index. It is not how the policy is organised. An asterisk in the "
           "Level column means documentation of the process is required.")
    trace_tbl(doc, [
        ("HRM.4.a", "CORE*",       "Section 3; 5.1", _HR),
        ("HRM.4.b", "Commitment",  "Section 3; 5.2", _HR),
        ("HRM.4.c", "Commitment",  "Section 3; 5.3", _HR),
        ("HRM.4.d", "Commitment",  "Section 3; 5.4", _HR),
        ("HRM.4.e", "Achievement", "Section 3; 5.5", _HR),
        ("HRM.4.f", "Achievement", "Section 3; 5.6", _HR),
    ])
    h(doc, 1, "12. Required Records / Evidence Checklist")
    h(doc, 2, "HRM.4.a — Written guidance for training and development.")
    lb(doc, "Written training and development policy or manual.")
    lb(doc, "Training-needs-identification, methodology, assessment and calendar record.")
    lb(doc, "Coverage record for all staff categories, including doctors and outsourced staff.")
    h(doc, 2, "HRM.4.b — Training record maintained.")
    lb(doc, "Training record with title, trainer, date, duration and trainee list with signatures.")
    lb(doc, "Content-capture record where possible.")
    h(doc, 2, "HRM.4.c — Training on job/equipment change.")
    lb(doc, "Training record triggered by a job-responsibility change or new-equipment introduction.")
    lb(doc, "Operational-and-maintenance training record for new equipment.")
    lb(doc, "Training-completion confirmation before independent use.")
    h(doc, 2, "HRM.4.d — Feedback mechanism.")
    lb(doc, "Feedback-mechanism record for training-programme improvement.")
    lb(doc, "Feedback data on course material, facilities and trainer capability.")
    h(doc, 2, "HRM.4.e — Evaluation of training effectiveness.")
    lb(doc, "Immediate post-training evaluation record — pre/post-test.")
    lb(doc, "Later workplace-effectiveness evaluation record.")
    lb(doc, "Retraining record where the evaluation showed a need.")
    h(doc, 2, "HRM.4.f — Continuing professional development.")
    lb(doc, "CPD support record — courses, conferences, e-learning access.")
    lb(doc, "Minimum mandatory annual training-hours specification record.")
    lb(doc, "Staff-participation record against the mandatory hours.")
    h(doc, 1, "13. References")
    lb(doc, "NABH Accreditation Standards for Hospitals, 6th Edition — standard HRM.4.")
    lb(doc, "NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.4 interpretations.")
    h(doc, 1, "Disclaimer")
    hrm_disclaimer(doc)
    save_and_verify(doc, "HCO_HRM_4_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# HRM.5 — Job-Specific Staff Training   (no stop-work)
# ══════════════════════════════════════════════════════════════════════════════
def gen_hrm5():
    doc = Document()
    h(doc, 0, "Policy on Job-Specific Staff Training")
    p(doc, HN)
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/HRM/POL/05", _HR)
    p(doc, "A blank marked ________ must be completed before issue.")
    h(doc, 1, "Statement of intent")
    p(doc, f"{HN} trains staff on the specific skills their job requires — blood handling, "
           "vulnerable-patient care, restraint, communication, resuscitation and infection control "
           "— not just general induction.")
    h(doc, 1, "1. Purpose")
    p(doc, f"This policy explains the job-specific training {HN} provides beyond induction, based "
           "on what a staff member's role actually requires.")
    p(doc, "This policy does not cover the clinical procedures themselves for blood transfusion, "
           "vulnerable-patient care, control and restraint, or patient communication — those are "
           "covered in other hospital policies. This policy is the staff training layer for those procedures.")
    h(doc, 1, "2. Scope")
    p(doc, f"This policy applies to the HR In-Charge / Personnel Officer, department heads, and "
           "every staff member whose role requires blood-handling, vulnerable-patient care, restraint, "
           "communication, CPR, or infection-control skills.")
    h(doc, 1, "3. Policy standards")
    p(doc, f"{HN} trains relevant staff in blood and blood product handling, vulnerable-patient care, "
           "control and restraint techniques, healthcare communication, periodic CPR for "
           "direct-patient-care staff, and infection prevention and control.")
    h(doc, 1, "4. Non-negotiable rules")
    ln(doc, "Do not let staff handling blood or blood products work without training in safe "
            "transport, consent, documentation and transfusion-reaction handling.")
    ln(doc, "Do not let staff caring for vulnerable patients work without training in identifying "
            "and caring for them.")
    ln(doc, "Do not let staff use control and restraint techniques without training in their "
            "appropriate use.")
    ln(doc, "Do not let CPR training lapse beyond two years for direct-patient-care staff, or "
            "beyond the interval required after a protocol change.")
    ln(doc, "Do not let infection-prevention-and-control training lapse beyond a year for any "
            "staff member.")
    ln(doc, f"Staff who see any of these rules broken report it the same shift to the "
            f"HR In-Charge / Personnel Officer or the Medical Superintendent.")
    h(doc, 1, "5. What we do")
    h(doc, 2, "5.1 Train staff on blood and blood product handling")
    p(doc, "Staff involved in blood transfusion services — doctors, nurses, technicians and staff "
           "transporting blood from the blood bank or storage unit — are trained in handling blood "
           "and blood products: safe transport, obtaining informed consent, required documentation, "
           "identifying and handling transfusion reactions, and educating the patient and family on "
           "donation. Blood transfusion service practice itself is covered in other hospital "
           "policies; this element is the staff training layer.")
    h(doc, 2, "5.2 Train staff on vulnerable-patient care")
    p(doc, "Relevant staff are trained in identifying and rendering care to vulnerable patients, "
           "per the hospital's written guidance. The vulnerable-patient care process itself is "
           "covered in other hospital policies; this element is the staff training layer.")
    h(doc, 2, "5.3 Train staff on control and restraint")
    p(doc, "Relevant staff are trained in the appropriate use of control and restraint techniques, "
           "per the hospital's written guidance. The control-and-restraint process itself is covered "
           "in other hospital policies; this element is the staff training layer.")
    h(doc, 2, "5.4 Train staff on healthcare communication")
    p(doc, "Staff are trained in healthcare communication techniques, including handling challenging "
           "situations and good communication practice. Training needs may be identified from patient "
           "complaints, incident reports, appraisals and employee feedback. Patient-facing "
           "communication practice itself is covered in other hospital policies; this element is "
           "the staff training layer.")
    h(doc, 2, "5.5 Train staff on CPR periodically")
    p(doc, "Staff involved in direct patient care are trained on cardio-pulmonary resuscitation "
           "periodically, at the level appropriate to their role. Doctors, nurses and rehabilitation "
           "staff refresh at least once in two years, or sooner if protocol changes; staff in "
           "emergency, intensive care or high-dependency units undergo appropriate advanced training "
           "(for example ACLS, ATLS, PALS or NRP, or an equivalent).")
    h(doc, 2, "5.6 Train staff on infection prevention and control")
    p(doc, f"{HN} provides staff training on infection prevention and control through in-service "
           "sessions at least once a year, including antimicrobial policy and antimicrobial "
           "stewardship content for medical professionals, infection-prevention-and-control nurses, "
           "the clinical pharmacist and support staff.")
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        (_HR,
         "Owns training records for all job-specific training under this policy."),
        ("Department heads",
         "Identify which staff in their department are \"relevant staff\" for each training requirement."),
        (_MS, "Accountable that this policy is followed."),
    ])
    h(doc, 1, "7. Quality monitoring")
    p(doc, "The HR In-Charge / Personnel Officer reviews a sample of training records periodically "
           "against the steps in Section 5, confirming CPR refreshers are current and "
           "infection-control training has not lapsed beyond a year. This policy itself is "
           "reviewed every year.")
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc, "Staff covered by this policy are trained on it when they take up the role, and again "
           "every year after that.")
    p(doc, f"I have read the Policy on Job-Specific Staff Training of {HN}. I will follow the processes described.")
    sig_tbl(doc)
    h(doc, 1, "9. Distribution")
    p(doc, "HR In-Charge / Personnel Officer; department heads; Medical Superintendent.")
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("ACLS", "Advanced Cardiac Life Support"),
        ("ATLS", "Advanced Trauma Life Support"),
        ("CPR",  "Cardio-Pulmonary Resuscitation"),
    ] + HRM_ABBREVS_BASE + [
        ("NRP",  "Neonatal Resuscitation Program"),
        ("PALS", "Paediatric Advanced Life Support"),
    ])
    h(doc, 1, "11. Traceability to NABH HCO Full Accreditation 6th Edition HRM.5")
    p(doc, "This table is an index. It is not how the policy is organised. An asterisk in the "
           "Level column means documentation of the process is required.")
    trace_tbl(doc, [
        ("HRM.5.a", "Commitment", "Section 3; 5.1", _HR),
        ("HRM.5.b", "Commitment", "Section 3; 5.2", _HR),
        ("HRM.5.c", "Commitment", "Section 3; 5.3", _HR),
        ("HRM.5.d", "Commitment", "Section 3; 5.4", _HR),
        ("HRM.5.e", "CORE",       "Section 3; 5.5", _HR),
        ("HRM.5.f", "Commitment", "Section 3; 5.6", _HR),
    ])
    h(doc, 1, "12. Required Records / Evidence Checklist")
    h(doc, 2, "HRM.5.a — Blood and blood product handling training.")
    lb(doc, "Blood-and-blood-product handling training record for relevant staff (doctors, nurses, technicians, transport staff).")
    lb(doc, "Training-content record — safe transport, informed consent, documentation, transfusion-reaction handling.")
    h(doc, 2, "HRM.5.b — Vulnerable-patient training.")
    lb(doc, "Vulnerable-patient identification-and-care training record.")
    lb(doc, "Relevant-staff coverage record.")
    h(doc, 2, "HRM.5.c — Control and restraint training.")
    lb(doc, "Control-and-restraint-technique training record.")
    lb(doc, "Relevant-staff coverage record.")
    h(doc, 2, "HRM.5.d — Healthcare communication training.")
    lb(doc, "Healthcare-communication-technique training record.")
    lb(doc, "Training-needs source record — complaints, incident reports, appraisals, feedback.")
    h(doc, 2, "HRM.5.e — Periodic CPR training.")
    lb(doc, "Periodic CPR-training record for direct-patient-care staff, at least once in two years or sooner after protocol change.")
    lb(doc, "Advanced-training record for emergency, ICU or high-dependency staff.")
    lb(doc, "Refresher-schedule tracking record.")
    h(doc, 2, "HRM.5.f — Infection prevention and control training.")
    lb(doc, "Infection-prevention-and-control training record at least annually.")
    lb(doc, "Antimicrobial-stewardship-content record for medical professionals, IPC nurses, clinical pharmacist and support staff.")
    h(doc, 1, "13. References")
    lb(doc, "NABH Accreditation Standards for Hospitals, 6th Edition — standard HRM.5.")
    lb(doc, "NABH Guidebook to Accreditation Standards for Hospitals, 6th Edition — HRM.5 interpretations.")
    h(doc, 1, "Disclaimer")
    hrm_disclaimer(doc)
    save_and_verify(doc, "HCO_HRM_5_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    gen_hrm1()
    gen_hrm2()
    gen_hrm3()
    gen_hrm4()
    gen_hrm5()
    print("\nAll 5 HRM rewrite drafts generated.")
