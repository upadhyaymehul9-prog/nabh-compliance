# -*- coding: utf-8 -*-
"""
generate_hco_mom_rewrites.py
Generates HCO MOM chapter v2 rewrite-reference DOCX files.

Pipeline : python-docx, identical to generate_hco_cop_rewrites.py.
Output   : policies/build/rewrite_reference/HCO_MOM_N_v2_REWRITE_DRAFT.docx
Source   : Approved plain-language content (mom1_content.txt, mom2_content.txt)
           + policies/build/mom_raw_dump_1-6.txt
"""
import os
from docx import Document

HN  = "«Hospital Name»"
# Resolve relative to this file so the script can be run from any CWD
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rewrite_reference")
os.makedirs(OUT, exist_ok=True)


# ── Helpers ───────────────────────────────────────────────────────────────────

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
        ("Document No.", no,          "Version",                "2.0"),
        ("Issue No.",    "01",         "Review due",             "One year from implementation"),
        ("Date created", "________",   "Date of implementation", "________"),
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

def abbrev_tbl(doc, rows):
    t = tbl(doc, len(rows) + 1, 2)
    t.cell(0, 0).text = "Abbreviation"; t.cell(0, 1).text = "Meaning"
    for ri, (a, m) in enumerate(rows, 1):
        t.cell(ri, 0).text = a; t.cell(ri, 1).text = m

def gov_tbl(doc, rows):
    t = tbl(doc, len(rows) + 1, 2)
    t.cell(0, 0).text = "Role"; t.cell(0, 1).text = "Responsibility"
    for ri, (role, resp) in enumerate(rows, 1):
        t.cell(ri, 0).text = role; t.cell(ri, 1).text = resp

def mon_tbl(doc, rows):
    t = tbl(doc, len(rows) + 1, 2)
    t.cell(0, 0).text = "Monitoring area"; t.cell(0, 1).text = "What is monitored"
    for ri, (area, what) in enumerate(rows, 1):
        t.cell(ri, 0).text = area; t.cell(ri, 1).text = what

def sig_tbl(doc):
    sig = tbl(doc, 4, 4)
    for ci, hdr in enumerate(("Staff name", "Designation", "Signature", "Date")):
        sig.cell(0, ci).text = hdr
    for ri in range(1, 4):
        for ci in range(4):
            sig.cell(ri, ci).text = "________"

def save_and_verify(doc, fname):
    import sys
    out = sys.stdout

    def pr(s):
        try:
            out.write(s + "\n")
        except UnicodeEncodeError:
            out.write(s.encode("ascii", "replace").decode() + "\n")

    pr(f"\n=== {fname} ===")
    for i, para in enumerate(doc.paragraphs[:80]):
        sn = para.style.name if para.style else "(None)"
        pr(f"{i:3d}  {sn!r:30s}  {para.text[:60]!r}")
    counts = {}
    for para in doc.paragraphs:
        sn = para.style.name if para.style else "(None)"
        counts[sn] = counts.get(sn, 0) + 1
    pr("  Style inventory:")
    for sn, n in sorted(counts.items()):
        pr(f"    {sn}: {n}")
    pr(f"  Total paras: {len(doc.paragraphs)}")
    path = os.path.join(OUT, fname)
    doc.save(path)
    pr(f"  Saved: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# MOM.1 — Safe Pharmacy Services and Medication Management   (NO stop-work)
# Content: mom1_content.txt (approved).
# Structure: Document control table, Governance table, Section 12 bullet list.
# COREs: none | Stars: a*, d* | Achievement: c | Excellence: none
# Exact items verified:
#   5.1: "Medication Management Manual" named as the single document
#   5.2: "at least once every three months" — exact frequency
#   5.3: "at least once a year" — annual system review exact
#   5.5: "within 24 hours" — drug recall notification timeframe exact
# ══════════════════════════════════════════════════════════════════════════════
def gen_mom1():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Safe Pharmacy Services and Medication Management")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/MOM/POL/01", "Medication Safety Officer")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"Pharmacy services and medication management at {HN} are governed by written "
      "guidance, overseen by a multi-disciplinary committee, and stay reliable even "
      "when the pharmacy is closed or stock runs out.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      f"This policy explains how {HN} runs its pharmacy services and medication "
      "management under written guidance, uses a multi-disciplinary committee to guide "
      "and update that guidance, keeps medications available when the pharmacy is closed "
      "or out of stock, and keeps staff informed of key changes.")
    p(doc,
      "This policy does not cover the hospital formulary, medication storage, "
      "prescription, dispensing, or reconciliation in detail — those are covered in "
      "other hospital policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to all pharmacy staff and clinical staff involved in "
      f"medication management at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")
    p(doc,
      f"{HN} runs pharmacy services and medication management under a Medication "
      "Management Manual, guided by a multi-disciplinary committee that meets at least "
      "once every three months and reviews the whole system at least once a year. "
      "There is a standard procedure to obtain medications when the pharmacy is closed "
      "or out of stock, and a process to keep relevant staff informed of shortages, "
      "recalls, and safety incidents.")
    p(doc, "Staff follow the written guidance below and keep the records it requires.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not manage medications without written guidance covering the formulary, "
       "procurement, storage, prescription, dispensing, administration, and monitoring "
       "— documented as a single Medication Management Manual, and supervised by a "
       "qualified individual across every patient care area.")
    lb(doc,
       "Do not run the medication management committee without its defined roles, its "
       "required composition, or its terms of reference, and do not let it meet less "
       "often than once every three months, without documenting the minutes.")
    lb(doc,
       "Do not skip the committee's review of the whole medication management system "
       "at least once a year.")
    lb(doc,
       "Do not leave the hospital without a standard procedure to obtain medications "
       "when the pharmacy is closed or stock runs out.")
    lb(doc,
       "Do not delay informing relevant staff of medication shortages, and do not take "
       "more than 24 hours to inform them of a drug recall.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Manage medications under written guidance")
    p(doc,
      "Written guidance — documented as a single Medication Management Manual — covers "
      "the formulary, procurement, storage, prescription, dispensing, administration, "
      "and monitoring of medications. A qualified individual supervises all pharmacy "
      "service activities, and this guidance applies across every patient care area in "
      "the organisation.")

    h(doc, 2, "5.2 Guide medication management through a multi-disciplinary committee")
    p(doc,
      "A multi-disciplinary committee has defined roles and responsibilities for managing "
      "medications, in line with applicable legislation and regulations where relevant. "
      "Its responsibilities include, among other things, developing medication management "
      "processes, developing and revising the formulary, and evaluating medication use "
      "and safety incidents. The committee includes representatives from major clinical "
      "departments, administration, a pharmacist or clinical pharmacologist, the "
      "medication safety officer, nursing, and the Quality department. Its terms of "
      "reference — composition, meeting frequency, and quorum — are defined, and it "
      "meets at least once every three months, with minutes documented.")

    h(doc, 2, "5.3 Review and update the medication management system")
    p(doc,
      "The committee reviews the whole medication management system at least once a year, "
      "covering rational use, medication errors, medication management processes, adverse "
      "drug reactions, patient safety, and high-risk medications.")
    p(doc,
      f"{HN} designates a medication safety officer — this responsibility could be held "
      "by the patient safety officer. Related requirements are covered in the hospital's "
      "other policies.")

    h(doc, 2, "5.4 Keep medications available when the pharmacy is closed or out of stock")
    p(doc,
      "A standard operating procedure sets out how to procure medications when the "
      "pharmacy is closed, or during a stock-out. It is preferable for "
      f"{HN} to run a 24-hour pharmacy.")

    h(doc, 2, "5.5 Keep staff informed of key changes")
    p(doc,
      "A process is in place to communicate medication shortages and stock-outs to "
      "clinicians and nurses. Staff are informed of a drug recall within 24 hours, and "
      "of any serious adverse events or patient safety incidents connected to medication "
      "use. The Pharmacy In-Charge, or a designated authority, is responsible for this "
      "communication, and it is documented. Related requirements are covered in the "
      "hospital's other policies.")

    # 6. Governance and responsibility
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        ("Medical Superintendent",
         "Accountable for ensuring pharmacy services and medication management are "
         "resourced and implemented as required by this policy."),
        ("Medication Safety Officer",
         "Owns day-to-day implementation of this policy; coordinates medication-safety "
         "processes; brings incidents and audit findings to the multi-disciplinary "
         "committee."),
        ("Multi-disciplinary committee",
         "Guides the formulation and implementation of pharmacy services and medication "
         "management; reviews the whole system at least once a year; meets at least "
         "once every three months and documents minutes."),
        ("Pharmacy In-Charge / designated authority",
         "Responsible for communicating medication shortages, recalls, and safety "
         "incidents to relevant staff; ensures the after-hours and stock-out procedure "
         "is operational."),
        ("Quality Coordinator",
         "Audits this policy; holds training records and staff acknowledgements."),
    ])

    # 7. Quality monitoring
    h(doc, 1, "7. Quality monitoring")
    mon_tbl(doc, [
        ("Medication Management Manual",
         "Current, complete, and supervised by a qualified individual across all patient "
         "care areas."),
        ("Multi-disciplinary committee",
         "Constitution, terms of reference, required composition, meeting frequency "
         "of at least once every three months, and documented minutes."),
        ("Annual system review",
         "Conducted by the committee at least once a year and covering all required "
         "topics (rational use, medication errors, ADRs, patient safety, high-risk "
         "medications)."),
        ("After-hours / stock-out procedure",
         "Standard operating procedure in place, tested, and used when required."),
        ("Staff communication",
         "Drug recalls communicated within 24 hours; shortages and serious adverse "
         "events communicated and documented."),
    ])

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "Pharmacy staff and clinical staff involved in medication management shall be "
      "familiar with the Medication Management Manual, the committee's role, the "
      "after-hours and stock-out procedure, and the staff communication process.")
    p(doc,
      f"I have read the Policy on Safe Pharmacy Services and Medication Management of "
      f"{HN}. I will follow the processes described.")
    sig_tbl(doc)

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "This policy shall be available to pharmacy staff, the multi-disciplinary "
      "committee, clinical staff involved in medication management, the Medication "
      "Safety Officer, the Pharmacy In-Charge, and the Quality Coordinator.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("ADR",  "Adverse drug reaction"),
        ("DTC",  "Drug and Therapeutics Committee (the organisation's multi-disciplinary "
                  "medication management committee)"),
        ("MSO",  "Medication Safety Officer"),
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("MOM",  "Management of Medication (NABH Hospitals chapter)"),
        ("SOP",  "Standard operating procedure"),
    ])

    # 11. Traceability table
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in "
      "the Level column means documentation of the process is required.")
    tr = tbl(doc, 6, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("MOM.1.a", "Commitment*",
         "Sections 3 and 5.1 address written guidance documented as a single Medication "
         "Management Manual, qualified supervision, and coverage of all patient care areas."),
        ("MOM.1.b", "Commitment",
         "Sections 3 and 5.2 address the committee's defined roles, required composition, "
         "terms of reference, meeting frequency of at least once every three months, and "
         "documented minutes."),
        ("MOM.1.c", "Achievement",
         "Sections 3 and 5.3 address the committee's annual review of the whole medication "
         "management system covering all required topics."),
        ("MOM.1.d", "Commitment*",
         "Sections 3 and 5.4 address the standard operating procedure to obtain medications "
         "when the pharmacy is closed or during a stock-out."),
        ("MOM.1.e", "Commitment",
         "Sections 3 and 5.5 address the staff communication process for shortages, "
         "drug recalls (within 24 hours), and serious adverse events, with documented "
         "communication by the Pharmacy In-Charge or designated authority."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Medication Management Manual (MOM.1.a)")
    lb(doc,
       "A single documented Medication Management Manual covering the formulary, "
       "procurement, storage, prescription, dispensing, administration, and monitoring.")
    lb(doc,
       "Evidence that a qualified individual supervises all pharmacy service activities.")
    lb(doc,
       "Evidence that the Manual applies across every patient care area in the "
       "organisation.")

    h(doc, 2, "Multi-disciplinary committee (MOM.1.b)")
    lb(doc,
       "Committee constitution record naming the required representatives: major "
       "clinical departments, administration, pharmacist or clinical pharmacologist, "
       "medication safety officer, nursing, and Quality department.")
    lb(doc,
       "Written terms of reference defining composition, meeting frequency, and quorum.")
    lb(doc,
       "Documented minutes of meetings held at least once every three months, naming "
       "decisions, owners, and due dates.")

    h(doc, 2, "Annual system review (MOM.1.c)")
    lb(doc,
       "Record of the committee's annual review of the medication management system.")
    lb(doc,
       "Evidence the review covered rational use, medication errors, medication "
       "management processes, adverse drug reactions, patient safety, and high-risk "
       "medications.")
    lb(doc,
       "Open-action tracking from the last review until closure.")

    h(doc, 2, "After-hours and stock-out procedure (MOM.1.d)")
    lb(doc,
       "Documented standard operating procedure to procure medications when the pharmacy "
       "is closed or during a stock-out.")
    lb(doc,
       "Evidence the procedure has been tested and is operational.")

    h(doc, 2, "Staff communication (MOM.1.e)")
    lb(doc,
       "Records of communication of medication shortages and stock-outs to clinicians "
       "and nurses.")
    lb(doc,
       "Records showing drug recalls communicated within 24 hours of notification.")
    lb(doc,
       "Records of communication of serious adverse events and patient safety incidents "
       "connected to medication use.")
    lb(doc,
       "Documentation identifying the Pharmacy In-Charge or designated authority as "
       "responsible for communication.")

    # 13. References
    h(doc, 1, "13. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. MOM.1.")
    ln(doc, "Guidebook interpretation supplied for MOM.1.a through MOM.1.e.")
    ln(doc,
       f"Internal documents of {HN}: Medication Management Manual; Drug and "
       "Therapeutics Committee terms of reference; committee minutes; after-hours and "
       "stock-out SOP; staff communication records.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied MOM.1 objective-element wording and "
      "Guidebook interpretation into plain-language policy format. The modal strength "
      "of the source has been preserved. Optional examples and mechanisms have not been "
      "converted into mandatory requirements. The exact requirements of the Medication "
      "Management Manual as a single named document, the committee meeting frequency "
      "of at least once every three months, the annual system review, and the 24-hour "
      "drug recall notification timeframe have been retained verbatim. MOM.1 has no "
      "stop-work section.")

    save_and_verify(doc, "HCO_MOM_1_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# MOM.2 — Hospital Formulary   (NO stop-work)
# Content: mom2_content.txt (approved).
# Structure: Document control table, Governance table, Section 12 bullet list.
# COREs: a | Stars: e*, f* | Achievement: d | Excellence: none
# Exact items verified:
#   5.1: molecule / formulation / strength — minimum three fields preserved
#   5.1: "Implants and devices are treated as drugs and included in the formulary"
#   5.2: "at least once a year" — annual review exact
#   5.5: all six acquisition-procedure elements preserved
#   5.6: three-step non-formulary process — evaluation / authorisation / ratification
#   MOM.2.a CORE designation does NOT create a stop-work section (none in this policy)
# ══════════════════════════════════════════════════════════════════════════════
def gen_mom2():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Hospital Formulary")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/MOM/POL/02", "Drug and Therapeutics Committee Chair")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"The hospital formulary at {HN} is developed collaboratively, kept current, "
      "made available to every clinician, and followed — with clear procedures for "
      "acquiring both formulary and non-formulary medications.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      f"This policy explains how {HN} develops and updates its formulary, makes it "
      "available to clinicians, monitors adherence to it, and follows defined "
      "procedures for acquiring formulary and non-formulary medications.")
    p(doc,
      "This policy does not cover medication storage, prescription, or dispensing in "
      "detail — those are covered in other hospital policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to the multi-disciplinary medication management committee, "
      f"pharmacy staff, and all treating doctors at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")
    p(doc,
      f"{HN}'s multi-disciplinary committee develops the formulary to match the "
      "organisation's mission, patient needs, and scope of services, reviews and "
      "updates it at least once a year, and makes the current version available to "
      "every treating doctor. Clinicians' adherence to the formulary is monitored, "
      "and defined procedures govern how formulary and non-formulary medications are "
      "acquired.")
    p(doc, "Staff follow the written guidance below and keep the records it requires.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not use a formulary that was not collaboratively prepared by the "
       "multi-disciplinary committee, or that omits the molecule name, formulation, "
       "and strength for each entry, or that leaves out implants and devices.")
    lb(doc,
       "Do not let the formulary go more than a year without a collaborative review "
       "and update.")
    lb(doc,
       "Do not leave the current formulary unavailable to any treating doctor.")
    lb(doc,
       "Do not acquire formulary medications without a documented procedure covering "
       "vendor selection, vendor evaluation, reorder levels, the indenting process, "
       "purchase order generation, receipt of goods, and managing stock-outs.")
    lb(doc,
       "Do not use a non-formulary medication through a local purchase without "
       "following an evaluation, authorisation, and ratification process, including "
       "a decision on whether it should be added to the formulary.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Develop the formulary collaboratively")
    p(doc,
      "The multi-disciplinary committee prepares the formulary to include medications "
      "necessary for the organisation's mission, patient needs, and scope of services. "
      "The National List of Essential Medicines or the WHO Model List of Essential "
      "Medicines could inform this, along with factors like harm potential, drug "
      "interactions, and likelihood of patient safety incidents. The committee could "
      "also consider a system-wise or speciality-wise formulary.")
    p(doc,
      "At minimum, every formulary entry names the molecule, its formulation, and its "
      f"strength. {HN} works to limit the number of concentrations of any one drug in "
      "the formulary. Implants and devices are treated as drugs and included in the "
      "formulary.")

    h(doc, 2, "5.2 Review and update the formulary")
    p(doc,
      "The committee reviews and updates the formulary collaboratively at least once a "
      "year — this could cover all medications or focus on certain categories, and could "
      "be done speciality by speciality. Non-formulary drugs regularly procured the "
      "previous year could be added during this review. Patient safety factors — adverse "
      "drug reactions, changing disease or resistance patterns, and cost — could inform "
      "the review.")

    h(doc, 2, "5.3 Make the current formulary available")
    p(doc,
      f"The current formulary is available to every treating doctor at {HN}, in "
      "physical or electronic form.")

    h(doc, 2, "5.4 Monitor adherence to the formulary")
    p(doc,
      f"{HN} makes sure prescriptions follow the formulary, and monitors how often "
      "prescriptions are rejected or a local purchase is needed because a non-formulary "
      "drug was prescribed.")

    h(doc, 2, "5.5 Follow the procedure for acquiring formulary medications")
    p(doc,
      "A documented procedure governs vendor selection, vendor evaluation, reorder "
      "levels, the indenting process, generating purchase orders, and receiving goods, "
      "and also addresses how stock-outs are managed.")

    h(doc, 2, "5.6 Follow the procedure for non-formulary medications")
    p(doc,
      "Where a medication is not in the formulary — for example through a local "
      "purchase or a hotline arrangement for urgent need — "
      f"{HN} follows a process of evaluation, authorisation, and ratification, and "
      "makes a decision on whether that medication should be added to the formulary.")

    # 6. Governance and responsibility
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        ("Medical Superintendent",
         "Accountable for ensuring the formulary is in place and that acquisition "
         "and non-formulary procedures are followed."),
        ("Drug and Therapeutics Committee Chair",
         "Owns formulary development and annual review; chairs the committee that "
         "governs all formulary decisions."),
        ("Multi-disciplinary committee (DTC)",
         "Develops, reviews and updates the formulary collaboratively; approves "
         "non-formulary requests; monitors adherence."),
        ("Pharmacy In-Charge",
         "Implements the acquisition procedure; manages non-formulary procurement "
         "records; ensures the current formulary is available at all prescribing "
         "locations."),
        ("Treating doctors / clinicians",
         "Prescribe from the current formulary; follow the non-formulary request "
         "process where a non-formulary drug is required."),
        ("Quality Coordinator",
         "Monitors formulary adherence; audits this policy; holds training records "
         "and staff acknowledgements."),
    ])

    # 7. Quality monitoring
    h(doc, 1, "7. Quality monitoring")
    mon_tbl(doc, [
        ("Formulary development",
         "Collaboratively prepared by the committee; every entry names molecule, "
         "formulation, and strength; implants and devices included as drugs."),
        ("Annual review",
         "Conducted and documented by the committee at least once a year; additions, "
         "deletions, and restrictions minuted with clinical reason."),
        ("Formulary availability",
         "Current version available to every treating doctor in physical or "
         "electronic form; outdated versions removed."),
        ("Adherence monitoring",
         "Frequency of non-formulary prescriptions, rejections, and local purchases "
         "tracked and reported to the committee."),
        ("Acquisition procedure",
         "All six procedure elements present and in use: vendor selection, vendor "
         "evaluation, reorder levels, indenting, purchase order generation, and "
         "receipt of goods; stock-out management addressed."),
        ("Non-formulary process",
         "Evaluation, authorisation, and ratification documented for every local "
         "purchase of a non-formulary medication; formulary-addition decision "
         "recorded."),
    ])

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "The multi-disciplinary committee, pharmacy staff, and all treating doctors "
      "shall be familiar with the formulary, the formulary acquisition procedure, "
      "and the non-formulary medication process.")
    p(doc,
      f"I have read the Policy on Hospital Formulary of {HN}. "
      "I will follow the processes described.")
    sig_tbl(doc)

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "This policy shall be available to the multi-disciplinary committee, pharmacy "
      "staff, all treating doctors, the Medication Safety Officer, and the Quality "
      "Coordinator.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("DTC",  "Drug and Therapeutics Committee (the organisation's multi-disciplinary "
                  "medication management committee)"),
        ("MSO",  "Medication Safety Officer"),
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("NLEM", "National List of Essential Medicines"),
        ("MOM",  "Management of Medication (NABH Hospitals chapter)"),
        ("WHO",  "World Health Organization"),
    ])

    # 11. Traceability table
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in "
      "the Level column means documentation of the process is required.")
    tr = tbl(doc, 7, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("MOM.2.a", "CORE",
         "Sections 3 and 5.1 address collaborative formulary preparation by the "
         "committee, minimum content (molecule, formulation, strength for every entry), "
         "and the inclusion of implants and devices as drugs."),
        ("MOM.2.b", "Commitment",
         "Sections 3 and 5.2 address the collaborative annual review and update of the "
         "formulary, including the review of all or certain medication categories."),
        ("MOM.2.c", "Commitment",
         "Sections 3 and 5.3 address making the current formulary available to every "
         "treating doctor in physical or electronic form."),
        ("MOM.2.d", "Achievement",
         "Section 5.4 addresses monitoring of prescription adherence to the formulary "
         "and tracking of rejections and local purchases."),
        ("MOM.2.e", "Commitment*",
         "Sections 3 and 5.5 address the documented acquisition procedure covering all "
         "six elements: vendor selection, vendor evaluation, reorder levels, indenting "
         "process, purchase order generation, receipt of goods, and stock-out "
         "management."),
        ("MOM.2.f", "Commitment*",
         "Sections 3 and 5.6 address the non-formulary medication process — evaluation, "
         "authorisation, and ratification — and the decision on formulary inclusion."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Formulary development — MOM.2.a (CORE)")
    lb(doc,
       "Formulary prepared collaboratively by the multi-disciplinary committee.")
    lb(doc,
       "Every formulary entry naming the molecule, formulation, and strength.")
    lb(doc,
       "Formulary including implants and devices as drugs.")
    lb(doc,
       "Record showing the committee limited the number of concentrations of any one "
       "drug where possible.")

    h(doc, 2, "Annual review — MOM.2.b")
    lb(doc,
       "Record of the committee's collaborative annual review and update of the "
       "formulary.")
    lb(doc,
       "Additions, deletions, and restrictions minuted with clinical reasons.")
    lb(doc,
       "Dated current-formulary cover showing the version in use.")

    h(doc, 2, "Formulary availability — MOM.2.c")
    lb(doc,
       "Current formulary available at prescribing locations — OPD consulting rooms, "
       "wards, ICU, emergency, OT, and the hospital information system or intranet.")
    lb(doc,
       "Record showing outdated copies removed when a new version is issued.")

    h(doc, 2, "Adherence monitoring — MOM.2.d")
    lb(doc,
       "Prescription-versus-formulary audit records.")
    lb(doc,
       "Tracking records for prescriptions rejected or resulting in local purchase "
       "because a non-formulary drug was prescribed.")
    lb(doc,
       "DTC records of any department's repeated non-adherence tabled for review.")

    h(doc, 2, "Acquisition procedure — MOM.2.e")
    lb(doc,
       "Documented acquisition procedure covering vendor selection, vendor evaluation, "
       "reorder levels, indenting process, purchase order generation, and receipt of "
       "goods.")
    lb(doc,
       "Record showing how stock-outs are managed under the procedure.")
    lb(doc,
       "Procurement records showing approved supplier, receipt quality checks, and "
       "batch and expiry logged.")

    h(doc, 2, "Non-formulary process — MOM.2.f")
    lb(doc,
       "Written non-formulary request record for every local purchase — including "
       "clinical justification (evaluation), approval (authorisation), and committee "
       "ratification.")
    lb(doc,
       "Record of the decision on whether the non-formulary item should be added to "
       "the formulary.")
    lb(doc,
       "Same-shift retrospective documentation record for any emergency non-formulary "
       "use.")

    # 13. References
    h(doc, 1, "13. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. MOM.2.")
    ln(doc, "Guidebook interpretation supplied for MOM.2.a through MOM.2.f.")
    ln(doc,
       "National List of Essential Medicines, Ministry of Health and Family Welfare, "
       "Government of India.")
    ln(doc,
       "WHO Model List of Essential Medicines, World Health Organization.")
    ln(doc,
       f"Internal documents of {HN}: hospital formulary; DTC meeting minutes; "
       "acquisition procedure; non-formulary request records.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied MOM.2 objective-element wording and "
      "Guidebook interpretation into plain-language policy format. The modal strength "
      "of the source has been preserved. Optional examples and mechanisms have not been "
      "converted into mandatory requirements. The exact requirements of minimum "
      "formulary entry fields (molecule, formulation, strength), inclusion of implants "
      "and devices as drugs, the annual review frequency, all six acquisition-procedure "
      "elements, and the three-step non-formulary process (evaluation, authorisation, "
      "ratification) have been retained verbatim. MOM.2.a carries CORE status; this "
      "policy does not contain a stop-work section, which is correct — MOM.2 is not "
      "in the MOM stop-work proposals.")

    save_and_verify(doc, "HCO_MOM_2_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# MOM.3 — Storage and Availability of Medications   (HAS stop-work: Section 6)
# Content: mom3_content.txt (approved).
# Structure: Document control, Sec 3 standards, Sec 4 non-negotiables,
#            Sec 5 (7 subsections), Sec 6 Stop-work, Sec 7 Governance,
#            Sec 8 Monitoring, Sec 9 Training, Sec 10 Distribution,
#            Sec 11 Abbreviations, Sec 12 Traceability, Sec 13 Records,
#            Sec 14 References, Disclaimer.
# COREs: a, c, e, g | Stars: c*, e*, f* | Achievement: d | Excellence: none
# Exact items verified:
#   5.1: manufacturer requirements apply to every area INCLUDING clinical areas
#   5.1: cold-storage temperature "at least once a day — or on every working day,
#        for areas not open daily" — both frequencies distinct
#   5.3: high-risk list CORE* — posted in pharmacy AND every clinical area storing it
#   5.5 + Sec 6: LASA/different-concentration separation is an absolute stop-work trigger
#   5.7: daily check distinct from sealed-cart "after each use or once a month"
# ══════════════════════════════════════════════════════════════════════════════
def gen_mom3():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Storage and Availability of Medications")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/MOM/POL/03", "Pharmacy In-Charge")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"Medications at {HN} are stored safely and to manufacturer requirements "
      "everywhere in the hospital, including clinical areas. High-risk and "
      "look-alike/sound-alike drugs are kept physically apart, and emergency "
      "medications are always available and replenished immediately after use.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      f"This policy explains how {HN} stores medications safely, controls inventory, "
      "identifies and separates high-risk and look-alike/sound-alike medications, "
      "and keeps emergency medications available and replenished at all times.")
    p(doc,
      "This policy does not cover prescription, dispensing, or administration of "
      "medications in detail — those are covered in other hospital policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to pharmacy staff and clinical staff involved in the "
      f"storage of medications at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")
    p(doc,
      f"{HN} stores medications in a clean, safe, and secure environment that follows "
      "manufacturer recommendations everywhere in the hospital, including clinical "
      "areas, and applies sound inventory control. A high-risk medication list is "
      "defined, kept current, and posted wherever high-risk medications are stored, "
      "and look-alike, sound-alike medications and different concentrations of the "
      "same drug are kept physically apart. A defined, uniformly stored emergency "
      "medication list is kept available at all times and replenished immediately "
      "after use.")
    p(doc, "Staff follow the written guidance below and keep the records it requires.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not store any medication outside its manufacturer's storage requirements, "
       "in any area of the hospital including clinical areas, and do not leave "
       "medications unprotected from loss or theft.")
    lb(doc,
       "Do not check cold-storage temperature less often than once a day — or on "
       "every working day, for areas not open daily — and do not store expired "
       "medications alongside those intended for patient use.")
    lb(doc,
       "Do not operate without a current, defined high-risk medication list posted "
       "in the pharmacy and every clinical area where high-risk medications are "
       "stored.")
    lb(doc,
       "Do not store high-risk medications outside their predetermined, clinically "
       "justified locations, or without safeguards against inadvertent administration.")
    lb(doc,
       "Do not store look-alike, sound-alike medications, or different concentrations "
       "of the same medication, physically together.")
    lb(doc,
       "Do not leave an emergency medication location without the defined list, or "
       "leave a used emergency medication unreplenished.")
    lb(doc,
       "Do not issue or use a medication that has been stored outside the "
       "manufacturer's temperature, light, or security recommendations until pharmacy "
       "has assessed it.")
    lb(doc,
       "Do not store any other drug alongside emergency medications, or check "
       "emergency medication stock less often than daily — or, for sealed carts, "
       "less often than after each use or once a month.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Store medications safely")
    p(doc,
      "Medication storage spaces are clean, safe, and secure, following the "
      "manufacturer's storage requirements — where none exist, "
      f"{HN} develops and applies its own. This applies to every area where "
      "medications are stored, including clinical areas. Medications are protected "
      "from loss or theft — for example by limiting access to authorised staff, "
      "locking medication carts and never leaving them unattended, or keeping them "
      "in a continuously staffed area. It is preferable for the storage area to be "
      "well organised, and overall cleanliness is maintained. Vaccines are kept at "
      "the manufacturer's required temperature, with temperature monitoring of the "
      "room or refrigerator done at least once a day — or on every working day, for "
      "areas not open daily. Medications past their expiry date are stored separately "
      "from those intended for patient use, pending disposal.")

    h(doc, 2, "5.2 Apply sound inventory control")
    p(doc,
      f"{HN} follows recognised inventory control practices — for example ABC, VED, "
      "FSN, or First-Expiry-First-Out analysis, alone or combined. Medicines could "
      "be stored alphabetically by generic name, and stock verification audits could "
      f"run at intervals {HN} defines, to detect loss or theft. There is also a "
      "mechanism for handling medications outside the regular inventory — for example, "
      "physicians' samples not for sale.")

    h(doc, 2, "5.3 Define and maintain the high-risk medication list")
    p(doc,
      f"{HN} defines and periodically updates its list of high-risk medications — "
      "those carrying a heightened risk of serious harm if an error occurs, such as "
      "drugs with a low therapeutic window, controlled substances, psychotherapeutic "
      "medications, look-alike/sound-alike medications, and concentrated electrolytes. "
      "The list is available in the pharmacy and every clinical area where high-risk "
      "medications are stored.")

    h(doc, 2, "5.4 Store high-risk medications where clinically necessary")
    p(doc,
      "High-risk medications are kept in predetermined areas — for example certain "
      "wards, the OT, or the ICU — based on clinical need. Where regulations apply, "
      "such as for narcotics, storage follows them. Safeguards are in place in every "
      "such area to prevent inadvertent administration.")

    h(doc, 2, "5.5 Keep look-alike, sound-alike, and different-concentration medications apart")
    p(doc,
      "Look-alike and sound-alike medications, and different concentrations of the "
      "same drug, are identified periodically, drawn from the hospital formulary, "
      "and listed. This list is made available in every unit where drugs are stored, "
      "not just the pharmacy, and revised whenever the formulary or drug packaging "
      "changes. It is good practice to store these medications as far apart as "
      "possible — but at minimum, they are kept physically apart, in the pharmacy "
      "and in patient care areas alike.")

    h(doc, 2, "5.6 Define and uniformly store emergency medications")
    p(doc,
      "The list of emergency medications is prepared in line with sound clinical "
      "practice and documented — it could vary by department, for example ICU, "
      "physiotherapy, emergency, or the cath lab. A crash cart with defined rows "
      "and drawers is a useful way to store these consistently. No other drug is "
      "kept with emergency medications.")

    h(doc, 2, "5.7 Keep emergency medications available and replenished")
    p(doc,
      "Adequate quantities of emergency medications are stocked at all times, "
      "checked at least daily. Where "
      f"{HN} uses a sealed emergency cart, the check happens after each use of "
      "the cart, or once a month, whichever comes first.")

    # 6. Stop-work authority
    h(doc, 1, "6. Stop-work authority")
    p(doc,
      "Do not store look-alike, sound-alike medications, or different concentrations "
      "of the same medication, physically together.")
    p(doc,
      "Do not leave an emergency medication location without the defined list, or "
      "leave a used emergency medication unreplenished.")
    p(doc,
      "Do not issue or use a medication that has been stored outside the "
      "manufacturer's temperature, light, or security recommendations until pharmacy "
      "has assessed it.")
    p(doc,
      "Stop-work applies to the storage location and to issue from that location. "
      "Immediate life-saving use of the only available dose continues while "
      "escalation happens, and is documented.")
    p(doc,
      "The person who stops tells the Pharmacy In-Charge and the Medication Safety "
      "Officer the same shift. Refusing unsafe storage or issue is not a "
      "disciplinary matter.")

    # 7. Governance and responsibility
    h(doc, 1, "7. Governance and responsibility")
    gov_tbl(doc, [
        ("Medical Superintendent",
         "Accountable for ensuring medication storage requirements are resourced "
         "and implemented across the organisation."),
        ("Pharmacy In-Charge",
         "Owns day-to-day implementation of this policy; maintains the high-risk "
         "and LASA lists; manages emergency medication replenishment; receives "
         "stop-work escalations the same shift."),
        ("Medication Safety Officer",
         "Coordinates stop-work escalations; brings storage incidents and audit "
         "findings to the Drug and Therapeutics Committee."),
        ("Nursing Superintendent",
         "Ensures clinical areas comply with manufacturer storage requirements, "
         "high-risk storage rules, and emergency medication check schedules."),
        ("Quality Coordinator",
         "Audits this policy; holds training records and staff acknowledgements."),
    ])

    # 8. Quality monitoring
    h(doc, 1, "8. Quality monitoring")
    mon_tbl(doc, [
        ("Medication storage conditions",
         "Manufacturer requirements followed in all areas including clinical areas; "
         "cold-storage temperature logged at least once a day or every working day; "
         "expired medications stored separately."),
        ("Inventory control",
         "Recognised inventory control practices in use throughout the organisation."),
        ("High-risk medication list",
         "Current, defined list updated periodically; posted in pharmacy and every "
         "clinical area that stores high-risk medications; staff trained."),
        ("High-risk storage locations",
         "Predetermined locations documented; walk-round confirms high-risk "
         "medications stored only in authorised areas with safeguards."),
        ("LASA and different-concentration separation",
         "List available in every unit where drugs are stored; physical separation "
         "confirmed in pharmacy and all patient care areas."),
        ("Emergency medication list and storage",
         "Defined list documented; uniform storage layout; no other drugs stored "
         "alongside emergency medications."),
        ("Emergency medication availability",
         "Daily inventory check at every location; sealed-cart check after each use "
         "or once a month; replenishment logged immediately after use."),
        ("Stop-work events",
         "Stop-work events logged with trigger, action taken, and outcome."),
    ])

    # 9. Training and staff acknowledgement
    h(doc, 1, "9. Training and staff acknowledgement")
    p(doc,
      "Pharmacy staff and clinical staff involved in the storage of medications "
      "shall be familiar with the storage requirements, high-risk and LASA lists, "
      "emergency medication procedures, and the stop-work authority in this policy.")
    p(doc,
      f"I have read the Policy on Storage and Availability of Medications of {HN}. "
      "I will follow the processes described.")
    sig_tbl(doc)

    # 10. Distribution
    h(doc, 1, "10. Distribution")
    p(doc,
      "This policy shall be available to pharmacy staff, nursing staff, clinical "
      "staff involved in medication storage, the Pharmacy In-Charge, the Medication "
      "Safety Officer, and the Quality Coordinator.")

    # 11. Abbreviations
    h(doc, 1, "11. Abbreviations")
    abbrev_tbl(doc, [
        ("ADR",  "Adverse drug reaction"),
        ("DTC",  "Drug and Therapeutics Committee"),
        ("FEFO", "First expiry, first out"),
        ("ICU",  "Intensive Care Unit"),
        ("LASA", "Look-alike, sound-alike"),
        ("MOM",  "Management of Medication (NABH Hospitals chapter)"),
        ("MSO",  "Medication Safety Officer"),
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("OT",   "Operation Theatre"),
    ])

    # 12. Traceability table
    h(doc, 1, "12. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk "
      "in the Level column means documentation of the process is required.")
    tr = tbl(doc, 8, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("MOM.3.a", "CORE",
         "Sections 3 and 5.1 address clean, safe, secure storage following "
         "manufacturer requirements in all areas including clinical areas, protection "
         "from loss or theft, temperature monitoring at least once a day or every "
         "working day, and separation of expired medications."),
        ("MOM.3.b", "Commitment",
         "Section 5.2 addresses recognised inventory control practices throughout "
         "the organisation and a mechanism for non-regular-inventory medications."),
        ("MOM.3.c", "CORE*",
         "Sections 3 and 5.3 address the defined, periodically updated high-risk "
         "medication list posted in the pharmacy and every clinical area where "
         "high-risk medications are stored."),
        ("MOM.3.d", "Achievement",
         "Section 5.4 addresses storage of high-risk medications in predetermined, "
         "clinically justified locations with safeguards against inadvertent "
         "administration."),
        ("MOM.3.e", "CORE*",
         "Sections 3 and 5.5 address the identification, listing, and physical "
         "separation of LASA medications and different concentrations in the pharmacy "
         "and all patient care areas. Physical separation is also a stop-work trigger "
         "in Section 6."),
        ("MOM.3.f", "Commitment*",
         "Section 5.6 addresses the defined emergency-medication list prepared in "
         "line with sound clinical practice, documented, uniformly stored, and kept "
         "free of other drugs."),
        ("MOM.3.g", "CORE",
         "Section 5.7 addresses adequate emergency medication stock checked at least "
         "daily — or, for sealed carts, after each use or once a month — and "
         "replenished immediately after use."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 13. Required Records/Evidence Checklist
    h(doc, 1, "13. Required Records/Evidence Checklist")

    h(doc, 2, "Medication storage conditions — MOM.3.a (CORE)")
    lb(doc,
       "Storage-condition records showing manufacturer requirements followed in all "
       "areas of the hospital, including clinical areas.")
    lb(doc,
       "Cold-storage and refrigerator temperature log with entries at least once a "
       "day — or on every working day for areas not open daily — and excursion-"
       "reporting records.")
    lb(doc,
       "Access-control records for the main pharmacy and controlled-drug cupboards.")
    lb(doc,
       "Records showing expired medications stored separately from those intended "
       "for patient use, pending disposal.")

    h(doc, 2, "Inventory control — MOM.3.b")
    lb(doc,
       "Documented inventory-control method (for example FEFO, ABC, VED, or FSN) "
       "in use throughout the organisation.")
    lb(doc,
       "Stock-movement traceability records from receipt to issue for sampled items.")

    h(doc, 2, "High-risk medication list — MOM.3.c (CORE*)")
    lb(doc,
       "Current, DTC-approved high-risk medication list, updated periodically and "
       "after any related incident.")
    lb(doc,
       "Posted-list records showing the current list available in the pharmacy and "
       "every clinical area where high-risk medications are stored.")
    lb(doc,
       "Staff training records on the high-risk list.")

    h(doc, 2, "High-risk storage locations — MOM.3.d")
    lb(doc,
       "DTC record naming the predetermined locations where each high-risk "
       "medication is clinically necessary.")
    lb(doc,
       "Walk-round record confirming high-risk medications stored only in "
       "authorised areas.")
    lb(doc,
       "Safeguard documentation in each designated high-risk storage area.")

    h(doc, 2, "LASA and different-concentration separation — MOM.3.e (CORE*)")
    lb(doc,
       "LASA and different-concentration medication list developed from the "
       "hospital formulary, available in every unit where drugs are stored.")
    lb(doc,
       "Physical-separation records showing LASA medications and different "
       "concentrations stored apart — in separate bins or on separate shelves — "
       "in the pharmacy and all patient care areas.")
    lb(doc,
       "List-revision records following formulary changes or drug packaging changes.")

    h(doc, 2, "Emergency medication list and storage — MOM.3.f (Commitment*)")
    lb(doc,
       "Defined, documented emergency-medication list prepared in line with sound "
       "clinical practice.")
    lb(doc,
       "Uniform-storage layout record across crash carts and emergency trolleys.")
    lb(doc,
       "Confirmation that no other drug is stored alongside emergency medications.")

    h(doc, 2, "Emergency medication availability and replenishment — MOM.3.g (CORE)")
    lb(doc,
       "Daily inventory-check records at every emergency-medication location "
       "(unsealed cart).")
    lb(doc,
       "Sealed-cart check records: after each use of the cart, or once a month, "
       "whichever comes first.")
    lb(doc,
       "Immediate-replenishment log after any use of an emergency medication, "
       "before the cart is returned to service.")

    # 14. References
    h(doc, 1, "14. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. MOM.3.")
    ln(doc, "Guidebook interpretation supplied for MOM.3.a through MOM.3.g.")
    ln(doc,
       f"Internal documents of {HN}: high-risk medication list; LASA list; "
       "emergency-medication list; temperature logs; inventory-control records.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied MOM.3 objective-element wording and "
      "Guidebook interpretation into plain-language policy format. The modal strength "
      "of the source has been preserved. Optional examples and mechanisms have not "
      "been converted into mandatory requirements. The exact requirements of "
      "manufacturer storage rules applying universally including clinical areas, "
      "the cold-storage temperature check at least once a day or on every working "
      "day for areas not open daily, the CORE high-risk list posted in all clinical "
      "areas storing high-risk medications, LASA and different-concentration "
      "physical separation as an absolute stop-work trigger, and the distinct "
      "emergency-medication check frequencies (daily for unsealed carts; after each "
      "use or once a month for sealed carts) have been retained verbatim.")

    save_and_verify(doc, "HCO_MOM_3_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# MOM.4 — Safe and Rational Prescription of Medications   (HAS stop-work: Sec 6)
# Content: mom4_content.txt (approved).
# Structure: Document control, Sec 3 standards, Sec 4 non-negotiables,
#            Sec 5 (8 subsections), Sec 6 Stop-work, Sec 7 Governance,
#            Sec 8 Monitoring, Sec 9 Training, Sec 10 Distribution,
#            Sec 11 Abbreviations, Sec 12 Traceability, Sec 13 Records,
#            Sec 14 References, Disclaimer.
# COREs: b, e, f | Stars: a*, b*, f* | Achievement: g, h | Excellence: d
# Exact items verified:
#   5.2: all SEVEN minimum prescription elements preserved verbatim
#   5.2: capital letters + no error-prone abbreviations stated explicitly
#   Sec 6: drug-allergy-check stop-work trigger first in the block
#   5.5: all THREE reconciliation transition points (admission, transfer, discharge)
#   5.6: countersignature "within 24 hours" exact
#   5.7: "at least once a month, using a representative sample" exact
# ══════════════════════════════════════════════════════════════════════════════
def gen_mom4():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Safe and Rational Prescription of Medications")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/MOM/POL/04", "Medical Superintendent")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"Medications at {HN} are prescribed rationally and meet defined minimum "
      "requirements every time, drug allergies are checked before every prescription, "
      "verbal orders follow a documented safe process, and medications are reconciled "
      "at every transition in a patient's care.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      f"This policy explains how {HN} ensures rational prescribing, applies minimum "
      "prescription requirements, checks drug allergies and adverse drug reactions "
      "before prescribing, reconciles medications at transitions of care, controls "
      "verbal orders, and audits prescriptions for safety.")
    p(doc,
      "This policy does not cover storage, dispensing, or administration of "
      "medications in detail — those are covered in other hospital policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to all doctors who prescribe medications, and to pharmacy "
      f"and nursing staff involved in checking, dispensing, and administering them, "
      f"at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")
    p(doc,
      f"{HN} prescribes medications in line with rational-prescribing good practice "
      "for both outpatients and inpatients, applies defined minimum requirements to "
      "every prescription, checks drug allergies and previous adverse reactions before "
      "prescribing, gives clinicians a mechanism to help avoid interactions and dosing "
      "errors, reconciles medications at every transition of care, controls verbal "
      "orders through a documented process, and audits prescriptions monthly for "
      "safety and rationality, acting on the findings where appropriate.")
    p(doc, "Staff follow the written guidance below and keep the records it requires.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not prescribe outside of good practice and guidelines for rational "
       "prescribing — this applies to both outpatient and inpatient care — and do "
       "not skip training clinicians on rational prescribing.")
    lb(doc,
       f"Do not accept, dispense, or administer a prescription that fails {HN}'s "
       "determined minimum requirements: patient name, unique hospital number, drug "
       "name (generic composition, except for vitamin or mineral combinations), "
       "strength, dosage instruction, duration and total quantity, and the prescribing "
       "doctor's name, signature, and registration number. Do not use error-prone "
       "abbreviations, and write every prescription in capital letters.")
    lb(doc,
       "Do not prescribe, or transcribe a prescription for action, without first "
       "ascertaining the patient's drug allergies and previous adverse drug reactions.")
    lb(doc,
       "Do not skip medication reconciliation at admission, at transfer between wards "
       "or departments, or at discharge, and do not leave it undocumented.")
    lb(doc,
       f"Do not act on a verbal medication order outside {HN}'s documented verbal-"
       "order process — including read-back, documentation at the time it is received, "
       "and countersignature by the ordering doctor within 24 hours.")
    lb(doc,
       "Do not skip the monthly medication order audit using a representative sample, "
       "and do not leave the corrective or preventive action decision undocumented "
       "where the audit calls for one.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Prescribe rationally")
    p(doc,
      "Prescribing follows good practice and guidelines for rational prescription of "
      "medications, across both outpatient and inpatient care. Clinicians are trained "
      "or sensitised on rational prescribing. The Code of Medical Ethics-2002, "
      "published by the Medical Council of India (now the National Medical "
      "Commission), is followed.")

    h(doc, 2, "5.2 Meet minimum prescription requirements")
    p(doc,
      "Every prescription — whether inpatient, outpatient, or emergency — follows "
      "applicable national and international guidelines. At minimum, it includes:")
    lb(doc, "the patient's name")
    lb(doc, "the patient's unique hospital number")
    lb(doc,
       "the drug name in generic composition, except for vitamin or mineral "
       "combinations")
    lb(doc, "strength")
    lb(doc, "dosage instructions")
    lb(doc, "duration and total quantity")
    lb(doc,
       "the prescribing doctor's name, signature, and registration number.")
    p(doc,
      "Error-prone abbreviations are not used, and prescriptions are written in "
      "capital letters. It is preferable to use a digital prescription system to "
      "reduce errors. Where a prescription has an error or is illegible, it is "
      "corrected with a single strikethrough, initialled, and rewritten.")

    h(doc, 2, "5.3 Check for drug allergies and prior reactions")
    p(doc,
      "Drug allergies and any previous adverse drug reactions are ascertained before "
      "prescribing — during the initial consultation, or at any point during the "
      "patient's care. It is good practice to record this prominently in the medical "
      "record for both outpatients and inpatients.")

    h(doc, 2, "5.4 Help clinicians avoid interactions and dosing errors")
    p(doc,
      f"{HN} provides clinicians with a mechanism — electronic or physical — to help "
      "identify drug interactions, food-drug interactions, alcohol-drug interactions, "
      "therapeutic duplication, and dose adjustments.")

    h(doc, 2, "5.5 Reconcile medications at transitions of care")
    p(doc,
      "Prescribed medications are checked for accuracy at three points:")
    lb(doc,
       "at admission — whether direct or after admission from the emergency "
       "department")
    lb(doc, "at transfer between wards or departments")
    lb(doc, "at discharge.")
    p(doc,
      "It is preferable to also reconcile after a cross-consultation. Reconciliation "
      "is documented, and there is a system to communicate it effectively during "
      "handover.")

    h(doc, 2, "5.6 Control verbal orders")
    p(doc,
      "Written guidance sets out who can give a verbal medication order, when it can "
      "be given, and how it is authenticated. Verbal orders are limited to urgent "
      "situations where immediate written or electronic communication is not "
      "practical, and their use is kept to a minimum. An approved list of formulary "
      "drugs that can be ordered verbally is maintained — defined either by what is "
      "included or what is excluded. The process includes read-back or repeat-back, "
      "and every verbal order is countersigned by the ordering doctor within 24 hours.")

    h(doc, 2, "5.7 Audit prescriptions")
    p(doc,
      "Medication order and prescription audits check legibility and use of capitals, "
      "the appropriateness of drug, dose, frequency, and route, therapeutic "
      "duplication, drug and food-drug interactions and how they are avoided, dosage "
      "adjustment for renal or hepatic impairment, IV incompatibility, inappropriate "
      "dilutions or infusion durations, and adherence to this policy's other "
      "requirements. This happens at least once a month, using a representative "
      "sample. It is preferably done by a clinical pharmacologist or clinical "
      "pharmacist — where none is available, a trained multidisciplinary team can "
      "do it instead. It is preferable to audit prescriptions live, before dispensing.")

    h(doc, 2, "5.8 Act on audit findings")
    p(doc,
      "Where appropriate, corrective or preventive action is taken based on the "
      "audit — ideally guided by root-cause analysis — and records of these actions "
      "are kept.")

    # 6. Stop-work authority
    h(doc, 1, "6. Stop-work authority")
    p(doc,
      "Do not prescribe (or transcribe a prescription for action) when drug allergies "
      "and previous adverse drug reactions have not been ascertained.")
    p(doc,
      "Do not act on a verbal medication order except through the organisation's "
      "documented verbal-order process (read-back, documentation, countersignature "
      "within the defined time).")
    p(doc,
      "Do not accept a prescription that fails the organisation's determined minimum "
      "requirements.")
    p(doc,
      "Stop-work applies to writing or acting on the unsafe order. Immediate "
      "life-saving medication in an emergency follows the documented emergency-"
      "prescription rules and is written up as soon as the patient is stable.")
    p(doc,
      "The person who stops tells the treating doctor and the Medication Safety "
      "Officer the same shift. Refusing an unsafe prescription is not a disciplinary "
      "matter.")

    # 7. Governance and responsibility
    h(doc, 1, "7. Governance and responsibility")
    gov_tbl(doc, [
        ("Medical Superintendent",
         "Accountable for rational prescribing implementation; maintains the "
         "authorised-prescriber list; receives stop-work escalations."),
        ("Medication Safety Officer",
         "Owns the prescription audit programme; brings audit findings and incidents "
         "to the Drug and Therapeutics Committee."),
        ("Treating doctors / prescribers",
         "Follow rational-prescribing guidance and the Code of Medical Ethics-2002; "
         "apply minimum prescription requirements; check drug allergies before "
         "prescribing; follow the verbal-order and reconciliation processes."),
        ("Pharmacy In-Charge",
         "Enforces minimum prescription requirements at the point of dispensing; "
         "holds the list of drugs orderable verbally; implements the verbal-order "
         "control process."),
        ("Nursing staff",
         "Check prescriptions before administration; complete medication "
         "reconciliation at transitions of care."),
        ("Quality Coordinator",
         "Audits this policy; holds training records and staff acknowledgements."),
    ])

    # 8. Quality monitoring
    h(doc, 1, "8. Quality monitoring")
    mon_tbl(doc, [
        ("Rational prescribing",
         "Clinicians trained; Code of Medical Ethics-2002 followed; prescribing "
         "in line with rational-prescribing guidelines for outpatients and "
         "inpatients."),
        ("Minimum prescription requirements",
         "All seven elements present (patient name, unique hospital number, generic "
         "drug name, strength, dosage instruction, duration and total quantity, "
         "prescriber name/signature/registration number); capital letters used; "
         "no error-prone abbreviations; non-compliant prescriptions held."),
        ("Drug-allergy check",
         "Drug allergies and previous ADRs ascertained and documented before "
         "prescribing for every patient."),
        ("Prescribing assistance mechanism",
         "Mechanism available and working — electronic or physical — for drug "
         "interactions, food-drug interactions, therapeutic duplication, and dose "
         "adjustments."),
        ("Medication reconciliation",
         "Documented at all three transition points: admission, transfer between "
         "wards or departments, and discharge."),
        ("Verbal orders",
         "Read-back performed and documented; countersignature by ordering doctor "
         "within 24 hours; verbal orders limited to urgent situations."),
        ("Prescription audit",
         "Conducted at least once a month with a representative sample; all scope "
         "parameters covered; findings documented; CAPA recorded where appropriate."),
        ("Stop-work events",
         "Stop-work events logged with trigger, action taken, and outcome."),
    ])

    # 9. Training and staff acknowledgement
    h(doc, 1, "9. Training and staff acknowledgement")
    p(doc,
      "All doctors who prescribe, and pharmacy and nursing staff involved in "
      "checking, dispensing, and administering medications, shall be familiar with "
      "the rational-prescribing guidance, minimum prescription requirements, "
      "allergy-check process, reconciliation requirements, verbal-order process, "
      "and stop-work authority in this policy.")
    p(doc,
      f"I have read the Policy on Safe and Rational Prescription of Medications "
      f"of {HN}. I will follow the processes described.")
    sig_tbl(doc)

    # 10. Distribution
    h(doc, 1, "10. Distribution")
    p(doc,
      "This policy shall be available to all treating doctors, pharmacy staff, "
      "nursing staff, the Medical Superintendent, the Medication Safety Officer, "
      "and the Quality Coordinator.")

    # 11. Abbreviations
    h(doc, 1, "11. Abbreviations")
    abbrev_tbl(doc, [
        ("ADR",  "Adverse drug reaction"),
        ("CAPA", "Corrective and Preventive Action"),
        ("DTC",  "Drug and Therapeutics Committee"),
        ("IV",   "Intravenous"),
        ("MCI",  "Medical Council of India"),
        ("MOM",  "Management of Medication (NABH Hospitals chapter)"),
        ("MSO",  "Medication Safety Officer"),
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("NMC",  "National Medical Commission"),
    ])

    # 12. Traceability table
    h(doc, 1, "12. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk "
      "in the Level column means documentation of the process is required.")
    tr = tbl(doc, 9, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("MOM.4.a", "Commitment*",
         "Sections 3 and 5.1 address rational prescribing for outpatients and "
         "inpatients, clinician training, and the Code of Medical Ethics-2002."),
        ("MOM.4.b", "CORE*",
         "Sections 3, 4, and 5.2 address all seven minimum prescription elements, "
         "capital letters, no error-prone abbreviations, and the process for holding "
         "non-compliant prescriptions. Physical-separation of requirements is "
         "presented as a bullet list for assessor legibility."),
        ("MOM.4.c", "Commitment",
         "Sections 3 and 5.3 address ascertainment of drug allergies and previous "
         "adverse drug reactions before prescribing. This is also the first stop-work "
         "trigger in Section 6."),
        ("MOM.4.d", "Excellence",
         "Section 5.4 addresses the clinician assistance mechanism — electronic or "
         "physical — for drug interactions, food-drug interactions, therapeutic "
         "duplication, and dose adjustments."),
        ("MOM.4.e", "CORE",
         "Sections 3 and 5.5 address medication reconciliation at all three mandatory "
         "transition points: admission, transfer between wards or departments, and "
         "discharge, with documentation and handover communication."),
        ("MOM.4.f", "CORE*",
         "Sections 3 and 5.6 address the verbal-order process: written guidance "
         "naming who, when, and how; read-back; countersignature within 24 hours; "
         "and a list of drugs orderable verbally. This is also a stop-work trigger "
         "in Section 6."),
        ("MOM.4.g", "Achievement",
         "Section 5.7 addresses the monthly prescription audit with a representative "
         "sample, covering all required scope parameters."),
        ("MOM.4.h", "Achievement",
         "Section 5.8 addresses corrective or preventive action taken where "
         "appropriate based on audit findings, with records kept."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 13. Required Records/Evidence Checklist
    h(doc, 1, "13. Required Records/Evidence Checklist")

    h(doc, 2, "Rational prescribing — MOM.4.a (Commitment*)")
    lb(doc,
       "DTC-named rational-prescribing reference (Code of Medical Ethics-2002; "
       "applicable rational-prescribing guidelines).")
    lb(doc,
       "Staff training records showing clinicians trained or sensitised on rational "
       "prescribing.")
    lb(doc,
       "Prescription-audit records sampled against rational-prescribing guidance.")

    h(doc, 2, "Minimum prescription requirements — MOM.4.b (CORE*)")
    lb(doc,
       "Published minimum-prescription-requirement list showing all seven mandatory "
       "elements.")
    lb(doc,
       "Sample prescriptions showing all elements present, written in capital "
       "letters, with no error-prone abbreviations.")
    lb(doc,
       "Hold or reject records for prescriptions failing minimum requirements, "
       "except through the documented emergency path.")

    h(doc, 2, "Drug-allergy check — MOM.4.c")
    lb(doc,
       "Drug-allergy and previous-ADR ascertainment records before prescribing, "
       "including entries stating 'none known'.")
    lb(doc,
       "Prominent allergy documentation in the medical record for outpatients and "
       "inpatients.")

    h(doc, 2, "Prescribing assistance mechanism — MOM.4.d")
    lb(doc,
       "Evidence of a working assistance mechanism — electronic or physical — for "
       "drug interactions, food-drug interactions, alcohol-drug interactions, "
       "therapeutic duplication, and dose adjustments.")
    lb(doc,
       "Records of orders clarified by pharmacy before dispensing where the "
       "mechanism identified a concern.")

    h(doc, 2, "Medication reconciliation — MOM.4.e (CORE)")
    lb(doc,
       "Reconciled-medication-list records at admission (direct or post-emergency), "
       "transfer between wards or departments, and at discharge.")
    lb(doc,
       "Discrepancy-resolution records between the reconciling clinician and the "
       "prescriber.")
    lb(doc,
       "Handover communication records showing reconciliation status transmitted "
       "at the transition point.")

    h(doc, 2, "Verbal orders — MOM.4.f (CORE*)")
    lb(doc,
       "Written verbal-order guidance naming who can give a verbal order, when, "
       "and how it is authenticated.")
    lb(doc,
       "Read-back records for each verbal order — drug, dose, route, frequency, "
       "patient — before administration.")
    lb(doc,
       "Countersignature records by the ordering doctor within 24 hours of the "
       "verbal order.")
    lb(doc,
       "Approved list of formulary drugs that can be ordered verbally.")

    h(doc, 2, "Prescription audit — MOM.4.g")
    lb(doc,
       "Monthly audit records with a representative sample, covering all required "
       "scope parameters.")
    lb(doc,
       "DTC or Medication Safety Officer presentation record of audit findings.")
    lb(doc,
       "Evidence the audit sample size was representative and the frequency was at "
       "least once a month.")

    h(doc, 2, "CAPA from audit — MOM.4.h")
    lb(doc,
       "CAPA records from audit findings, with owner and due date.")
    lb(doc,
       "Closure-tracking records for each open action.")
    lb(doc,
       "Decision records noting where CAPA was considered and judged not required, "
       "where that is the case.")

    # 14. References
    h(doc, 1, "14. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. MOM.4.")
    ln(doc, "Guidebook interpretation supplied for MOM.4.a through MOM.4.h.")
    ln(doc,
       "Code of Medical Ethics-2002, Medical Council of India (now National Medical "
       "Commission).")
    ln(doc,
       "Institute for Safe Medication Practices (ISMP) guidelines on error-prone "
       "abbreviations.")
    ln(doc,
       f"Internal documents of {HN}: rational-prescribing guidance; minimum-"
       "prescription-requirement list; verbal-order procedure; medication-"
       "reconciliation records; prescription audit reports.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied MOM.4 objective-element wording and "
      "Guidebook interpretation into plain-language policy format. The modal strength "
      "of the source has been preserved. Optional examples and mechanisms have not "
      "been converted into mandatory requirements. The exact requirements of all seven "
      "minimum prescription elements, the capital-letters and no-error-prone-"
      "abbreviations rules, the drug-allergy-check stop-work trigger, all three "
      "reconciliation transition points (admission, transfer, discharge), the verbal-"
      "order countersignature within 24 hours, and the monthly audit frequency with a "
      "representative sample have been retained verbatim.")

    save_and_verify(doc, "HCO_MOM_4_v2_REWRITE_DRAFT.docx")


def gen_mom5():
    """MOM.5 — Uniform Medication Orders (no stop-work; sections 1-13 + Disclaimer)"""
    doc = Document()

    # Title
    h(doc, 0, "Policy on Uniform Medication Orders")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/MOM/POL/05", "Medical Superintendent")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      "Medication orders are written only by authorised personnel, in one uniform "
      "place in the medical record, legibly, and complete with every required detail "
      "every time.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      f"This policy explains how {HN} ensures only authorised personnel write "
      "medication orders, keeps every order in one uniform location, keeps orders "
      "legible and traceable, and requires every order to include the medicine name, "
      "route, strength, and frequency.")
    p(doc,
      "This policy does not cover prescription content requirements or dispensing "
      "in detail — those are covered in other hospital policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to all doctors and authorised staff who write medication "
      f"orders at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")
    p(doc,
      f"{HN} ensures only doctors — or staff specifically authorised by legislation "
      "or government order — write medication orders. Every order is recorded in a "
      "single, uniform location in the medical record, including the patient's name "
      "and unique identification number, and only medications recorded there are "
      "administered. Orders are legible, dated, timed, signed, and traceable to the "
      "person who wrote them, and every order names the medicine, route of "
      "administration, strength, and frequency or time of administration.")
    p(doc, "Staff follow the written guidance below and keep the records it requires.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not let anyone other than a doctor — holding at least an MBBS qualification "
       "— write a medication order, unless another category of staff is specifically "
       "authorised by legislation or a government order.")
    lb(doc,
       "Do not administer a medication that isn't recorded in the uniform medication-"
       "order location of the medical record, and do not accept phrases like "
       "\"continue same treatment,\" \"repeat all,\" or similar shorthand in place of "
       "a written order.")
    lb(doc,
       "Do not modify an existing medication order by striking through or overwriting "
       "it — discontinue the original and write a fresh order instead.")
    lb(doc,
       "Do not use error-prone abbreviations in a medication order, and do not use "
       "any abbreviation outside the hospital's approved, standardised list.")
    lb(doc,
       "Do not write a multi-drug order without stating the strength of every "
       "individual drug, except where the combination is only of vitamins and/or "
       "minerals.")
    lb(doc,
       "Do not leave an incomplete medication order — missing the drug name, route, "
       "strength, or frequency — without a mechanism to catch and correct it.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Ensure only authorised personnel write orders")
    p(doc,
      "Medication orders are written by a doctor holding at minimum an MBBS "
      "qualification. Any other staff category authorised to write orders is backed "
      "by legislation or a government order, not an internal hospital decision alone. "
      "Even when transcribing a treating consultant's orders from an OP record or "
      "admission note, a doctor writes the inpatient medication order. Where the "
      "hospital uses an electronic medical record, the doctor enters the prescription "
      "directly using their own login; if an assistant enters it, the doctor verifies "
      "and authorises it.")

    h(doc, 2, "5.2 Keep every order in one uniform location")
    p(doc,
      "Every medication order is recorded in a single, uniform location in the "
      "medical record, which includes the patient's name and unique identification "
      "number. Only medications recorded there are administered — orders written "
      "anywhere else are moved to this location, and electronic orders follow the "
      "same principle. It's preferable for the prescription and administration record "
      "to sit on the same sheet — a drug \"Kardex,\" updated or authorised daily, is "
      "one useful format for this. Phrases like \"continue same treatment,\" "
      "\"repeat all,\" or \"repeat 1,4,5,8\" aren't accepted in place of a written "
      "order. Where a drug's dose changes — for example from four times a day to "
      "twice a day — the original order is discontinued and a fresh order written; a "
      "strike-through or overwrite of the old order isn't acceptable.")

    h(doc, 2, "5.3 Keep orders legible and traceable")
    p(doc,
      "Hand-written medication orders are written in capital letters. Where "
      "abbreviations are used, only the hospital's approved, standardised list "
      "applies, throughout the organisation — the Institute for Safe Medication "
      "Practices guidelines are a useful reference. Error-prone abbreviations aren't "
      "used. The identity of whoever wrote the order is traceable — for example by "
      "name against each order, a master signature list, or an employee code.")

    h(doc, 2, "5.4 Include every required detail")
    p(doc,
      "Where an order includes two or more drugs, the strength of each individual "
      "drug is stated — this may not apply to combinations of vitamins and/or "
      "minerals. Where the strength of a drug differs by time of administration, "
      "separate orders are recorded for each. There's a mechanism to catch and act "
      "on any order that's incomplete on drug name, route, strength, or frequency "
      "and time of administration. (Related requirements are covered in the "
      "hospital's other policies.)")

    # 6. Governance and responsibility
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        ("Medical Superintendent",
         "Accountable for implementing this policy; maintains the authorised-"
         "prescriber list."),
        ("Treating doctors / prescribers",
         "Write medication orders per this policy — MBBS minimum, uniform location, "
         "legible, complete — and do not delegate order-writing to non-authorised "
         "staff."),
        ("Nursing Superintendent / Nursing In-Charge",
         "Ensures only medications recorded in the uniform location are administered; "
         "checks orders for legibility and completeness before administration."),
        ("Quality Coordinator",
         "Audits adherence to this policy; holds training records."),
    ])

    # 7. Quality monitoring
    h(doc, 1, "7. Quality monitoring")
    mon_tbl(doc, [
        ("Authorised prescribers",
         "Only doctors holding MBBS minimum, or staff specifically authorised by "
         "legislation or government order, write medication orders."),
        ("Uniform order location",
         "All orders recorded in one location with patient name and unique ID; "
         "administration only from that location; no orders written elsewhere "
         "accepted without transfer."),
        ("Order legibility and traceability",
         "Orders written in capital letters; only approved abbreviations used; "
         "prescriber identity traceable on every order."),
        ("Order completeness",
         "Drug name, route, strength, and frequency present on every order; "
         "multi-drug orders state strength of each drug (vitamin/mineral exception "
         "applied correctly); mechanism in place for incomplete orders."),
        ("No shorthand or overwrite",
         "No CST, repeat-all, or similar shorthand; modifications written as fresh "
         "orders; no strike-through or overwrite accepted."),
    ])

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "All doctors and authorised staff who write medication orders, and nursing "
      "staff who administer them, shall be familiar with the authorised-prescriber "
      "requirements, uniform-location requirement, legibility, traceability, and "
      "order-completeness rules in this policy.")
    p(doc,
      f"I have read the Policy on Uniform Medication Orders of {HN}. "
      "I will follow the processes described.")
    sig_tbl(doc)

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "This policy shall be available to all treating doctors, nursing staff, the "
      "Medical Superintendent, the Medication Safety Officer, and the Quality "
      "Coordinator.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("EMR",  "Electronic Medical Record"),
        ("ISMP", "Institute for Safe Medication Practices"),
        ("MBBS", "Bachelor of Medicine, Bachelor of Surgery"),
        ("MOM",  "Management of Medication (NABH Hospitals chapter)"),
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("OE",   "Objective Element"),
        ("OP",   "Outpatient"),
    ])

    # 11. Traceability table
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk "
      "in the Level column means documentation of the process is required.")
    tr = tbl(doc, 5, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("MOM.5.a", "Commitment*",
         "Sections 3 and 5.1 address the MBBS-minimum qualification requirement, "
         "legislation or government-order basis for any other authorised category, "
         "the requirement for a doctor to write the inpatient order even when "
         "transcribing, and electronic-record direct-entry or doctor-verified "
         "assistant entry."),
        ("MOM.5.b", "Commitment",
         "Sections 3 and 5.2 address the single uniform location with patient name "
         "and unique ID, administration only from that location, transfer of orders "
         "written elsewhere, the ban on shorthand phrases (CST, repeat-all), and "
         "the fresh-order requirement for modifications — strike-through or overwrite "
         "of the old order is not acceptable."),
        ("MOM.5.c", "Commitment",
         "Section 5.3 addresses the capital-letter requirement for hand-written "
         "orders, the approved standardised abbreviation list applied throughout the "
         "organisation, the ban on error-prone abbreviations, and prescriber-identity "
         "traceability on every order."),
        ("MOM.5.d", "Commitment",
         "Section 5.4 addresses the multi-drug strength requirement — with the "
         "explicit exception for vitamin and/or mineral combinations only — separate "
         "orders for different strengths by time, and the mechanism for catching and "
         "acting on incomplete orders."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Authorised prescribers — MOM.5.a (Commitment*)")
    lb(doc, "Authorised-prescriber list showing MBBS minimum for doctors.")
    lb(doc,
       "Legislation or government order for any non-doctor category authorised "
       "to write medication orders.")
    lb(doc,
       "Electronic-record verification record where an assistant enters the "
       "prescription — showing doctor authorisation.")

    h(doc, 2, "Uniform order location — MOM.5.b")
    lb(doc,
       "Medication-order records showing uniform location containing patient name "
       "and unique identification number.")
    lb(doc,
       "Evidence that only medications from the uniform location are administered.")
    lb(doc,
       "Transfer records for orders originally written outside the uniform location.")
    lb(doc, "Absence of shorthand (CST, repeat-all) in current medication-order records.")
    lb(doc, "Fresh-order records for medication changes, with original discontinued.")

    h(doc, 2, "Legibility and traceability — MOM.5.c")
    lb(doc,
       "Sample medication orders written in capital letters with no error-prone "
       "abbreviations.")
    lb(doc, "Approved abbreviation list in use throughout the organisation.")
    lb(doc,
       "Prescriber-identity traceability on each order — name, master signature "
       "list, or employee code.")

    h(doc, 2, "Order completeness — MOM.5.d")
    lb(doc,
       "Sample orders showing drug name, route, strength, and frequency or time "
       "of administration present.")
    lb(doc,
       "Multi-drug orders with strength of each individual drug stated "
       "(vitamin/mineral exception documented where applied).")
    lb(doc, "Mechanism documentation for catching and acting on incomplete orders.")

    # 13. References
    h(doc, 1, "13. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. MOM.5.")
    ln(doc, "Guidebook interpretation supplied for MOM.5.a through MOM.5.d.")
    ln(doc,
       "Institute for Safe Medication Practices (ISMP) guidelines on error-prone "
       "abbreviations.")
    ln(doc,
       f"Internal documents of {HN}: authorised-prescriber list; approved "
       "abbreviation list; medication-order records.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied MOM.5 objective-element wording and "
      "Guidebook interpretation into plain-language policy format. The modal strength "
      "of the source has been preserved. Optional examples and mechanisms have not "
      "been converted into mandatory requirements. The MBBS-minimum qualification "
      "requirement, the single uniform location with patient name and unique "
      "identification number, the prohibition on strike-through or overwrite, and "
      "the multi-drug strength exception limited to vitamin and/or mineral "
      "combinations only have all been retained verbatim.")

    save_and_verify(doc, "HCO_MOM_5_v2_REWRITE_DRAFT.docx")


def gen_mom6():
    """MOM.6 — Safe Dispensing of Medications (stop-work Section 6; sections 1-14 + Disclaimer)"""
    doc = Document()

    # Title
    h(doc, 0, "Policy on Safe Dispensing of Medications")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/MOM/POL/06", "Pharmacy In-Charge")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      "Medications are dispensed only against a valid prescription, checked before "
      "dispensing, correctly labelled, verified before a high-risk order is dispensed, "
      "and recalled or expired medications never reach a patient.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      f"This policy explains how {HN} dispenses medications safely, handles recalls "
      "and near-expiry stock, labels dispensed medications, verifies high-risk orders "
      "before dispensing, and manages medication returns.")
    p(doc,
      "This policy does not cover storage or prescription of medications in detail "
      "— those are covered in other hospital policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to all pharmacy staff involved in dispensing medications "
      f"at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")
    p(doc,
      f"{HN} dispenses medications only against a valid prescription or order, "
      "checked for generic composition, formulation, expiry, and strength, across "
      "both bulk and retail pharmacy. Medication recalls and near-expiry stock are "
      "handled through defined systems, every dispensed medication is labelled, "
      "high-risk orders are verified before dispensing, and medication returns "
      "follow written guidance.")
    p(doc, "Staff follow the written guidance below and keep the records it requires.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not dispense a medication without a valid prescription or medication "
       "order, except for over-the-counter drugs, and do not dispense without "
       "checking generic composition, formulation, expiry date, and strength where "
       "applicable. Do not sell physicians' samples.")
    lb(doc,
       "Do not leave a recalled medication in usable stock, and do not skip "
       "reporting an internally identified recall to the appropriate regulatory "
       "authority.")
    lb(doc,
       "Do not let a beyond-expiry-date medication remain available in clinical "
       "stock.")
    lb(doc,
       "Do not dispense a medication that is unlabelled, recalled, expired, or a "
       "high-risk order that has not been verified for dose, frequency, and route.")
    lb(doc,
       "Do not accept a returned medication without written guidance on which "
       "medications are accepted and the minimum conditions they must meet.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Dispense medications safely")
    p(doc,
      "Written guidance governs the safe dispensing of medications. Medications are "
      "dispensed only against a valid prescription or medication order, except for "
      "over-the-counter drugs. Before dispensing, medications are checked for generic "
      "composition, formulation, expiry date, and — where applicable — strength. "
      "This applies to both bulk and retail pharmacy. Physicians' samples are never "
      "sold.")

    h(doc, 2, "5.2 Handle medication recalls")
    p(doc,
      f"{HN} has an established system for medication recalls, whether triggered by "
      "a regulatory authority, the manufacturer, or internal feedback — for example, "
      "noticing a visible contaminant in an IV fluid bottle. Where a recall arises "
      "from internal feedback, the appropriate regulatory authority is also informed. "
      "A record is kept whenever a recall occurs.")

    h(doc, 2, "5.3 Handle near-expiry medications")
    p(doc,
      f"{HN} defines what counts as \"near expiry\" — for example, three months "
      "before the expiry date — and has a mechanism to withdraw near-expiry stock "
      "before it goes past that date. No beyond-expiry-date medication is available "
      "in usable clinical stock.")

    h(doc, 2, "5.4 Label dispensed medications")
    p(doc,
      "At minimum, every label includes dosage instructions the patient can "
      "understand. Where medicines are dispensed as cut strips or from bulk "
      "containers, the label also includes the drug name, strength, and expiry date. "
      "This applies to both inpatients and outpatients, and to reconstituted drugs, "
      f"such as chemotherapy medications. {HN} could use technology like QR codes "
      "on individual medicines to strengthen this process.")

    h(doc, 2, "5.5 Verify high-risk orders before dispensing")
    p(doc,
      "High-risk medications are dispensed only against a written order, verified "
      "by staff before dispensing, and in line with applicable statutory "
      "requirements.")

    h(doc, 2, "5.6 Manage medication returns")
    p(doc,
      "Written guidance directs how medications are returned to the pharmacy, at "
      "minimum covering which medications are accepted for return — defined by "
      "inclusion or exclusion — and the minimum conditions for accepting a return, "
      "such as matching drug name, strength, batch number, and expiry date to the "
      "bill, and no visible damage. It's preferable not to accept a return of any "
      "medication with a specific temperature storage requirement once it has left "
      "the hospital's premises.")

    # 6. Stop-work authority
    h(doc, 1, "6. Stop-work authority")
    p(doc,
      "Do not dispense a medication that is unlabelled, recalled, expired, or a "
      "high-risk order that has not been verified for dose, frequency and route.")
    p(doc,
      "Stop-work applies to the dispense. Immediate life-saving issue from floor "
      "stock in an emergency follows the documented after-hours or emergency-dispense "
      "rules and is recorded.")
    p(doc,
      "The person who stops tells the Pharmacy In-Charge the same shift. Refusing "
      "an unsafe dispense is not a disciplinary matter.")

    # 7. Governance and responsibility
    h(doc, 1, "7. Governance and responsibility")
    gov_tbl(doc, [
        ("Medical Superintendent",
         "Accountable for safe dispensing implementation across the organisation."),
        ("Pharmacy In-Charge",
         "Owns day-to-day dispensing, recall handling, labelling compliance, "
         "high-risk order verification, and medication returns. Receives stop-work "
         "escalations the same shift."),
        ("Medication Safety Officer",
         "Coordinates notification of internally identified recalls to the "
         "appropriate regulatory authority; brings dispensing incidents to the DTC."),
        ("Quality Coordinator",
         "Audits adherence to this policy; holds training records."),
    ])

    # 8. Quality monitoring
    h(doc, 1, "8. Quality monitoring")
    mon_tbl(doc, [
        ("Safe dispensing",
         "Valid prescription or order checked before every dispense; generic "
         "composition, formulation, expiry, and strength checked; applies to bulk "
         "and retail pharmacy; no physicians' samples sold."),
        ("Medication recalls",
         "Established recall system in place; internally identified recalls reported "
         "to the appropriate regulatory authority the same shift; records kept on "
         "occurrence."),
        ("Near-expiry and beyond-expiry stock",
         "Near-expiry threshold defined; withdrawal mechanism in place before the "
         "defined date; no beyond-expiry-date medication available in clinical stock."),
        ("Labelling",
         "All dispensed medications labelled with dosage instructions; cut strips "
         "and bulk-container labels include drug name, strength, and expiry date; "
         "applies to inpatients and outpatients; reconstituted drugs (e.g. "
         "chemotherapy) labelled."),
        ("High-risk order verification",
         "Written order present for every high-risk dispense; staff verification "
         "completed before dispensing; statutory requirements met."),
        ("Medication returns",
         "Written returns guidance in place; inclusion/exclusion list defined; "
         "minimum conditions documented; return records kept."),
        ("Stop-work events",
         "Stop-work events logged with trigger, action taken, and outcome."),
    ])

    # 9. Training and staff acknowledgement
    h(doc, 1, "9. Training and staff acknowledgement")
    p(doc,
      "All pharmacy staff involved in dispensing medications shall be familiar with "
      "the safe-dispensing guidance, recall and near-expiry procedures, labelling "
      "requirements, high-risk order verification, medication-return guidance, and "
      "stop-work authority in this policy.")
    p(doc,
      f"I have read the Policy on Safe Dispensing of Medications of {HN}. "
      "I will follow the processes described.")
    sig_tbl(doc)

    # 10. Distribution
    h(doc, 1, "10. Distribution")
    p(doc,
      "This policy shall be available to all pharmacy staff, the Pharmacy In-Charge, "
      "the Medical Superintendent, the Medication Safety Officer, and the Quality "
      "Coordinator.")

    # 11. Abbreviations
    h(doc, 1, "11. Abbreviations")
    abbrev_tbl(doc, [
        ("DTC",  "Drug and Therapeutics Committee"),
        ("IV",   "Intravenous"),
        ("MOM",  "Management of Medication (NABH Hospitals chapter)"),
        ("MSO",  "Medication Safety Officer"),
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("OTC",  "Over-the-counter"),
        ("QR",   "Quick Response (code)"),
    ])

    # 12. Traceability table
    h(doc, 1, "12. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk "
      "in the Level column means documentation of the process is required.")
    tr = tbl(doc, 7, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("MOM.6.a", "Commitment*",
         "Sections 3 and 5.1 address the written safe-dispensing guidance, valid "
         "prescription or order requirement, pre-dispense checks (generic "
         "composition, formulation, expiry, strength), applicability to bulk and "
         "retail pharmacy, and the prohibition on selling physicians' samples."),
        ("MOM.6.b", "Commitment*",
         "Section 5.2 addresses the established recall system, the requirement to "
         "inform the appropriate regulatory authority when a recall is internally "
         "identified, and the record-keeping requirement on every recall occurrence."),
        ("MOM.6.c", "Commitment*",
         "Section 5.3 addresses the definition of 'near expiry,' the withdrawal "
         "mechanism for near-expiry stock, and the absolute requirement that no "
         "beyond-expiry-date medication is available in usable clinical stock — "
         "near-expiry and beyond-expiry are treated as distinct stages."),
        ("MOM.6.d", "CORE*",
         "Sections 3 and 5.4 address universal labelling scope — both inpatients "
         "and outpatients, and reconstituted drugs such as chemotherapy medications. "
         "Cut strips and bulk containers carry drug name, strength, and expiry date "
         "in addition to dosage instructions. This resolves the Guidebook internal "
         "inconsistency in favour of universal scope (not outpatient-only). This OE "
         "is also a stop-work trigger in Section 6."),
        ("MOM.6.e", "CORE",
         "Sections 3 and 5.5 address the written-order requirement for high-risk "
         "medications, staff verification before dispensing, and statutory "
         "requirements. This is also a stop-work trigger in Section 6."),
        ("MOM.6.f", "Commitment*",
         "Section 5.6 addresses the written medication-return guidance, the "
         "inclusion/exclusion definition of accepted medications, and the minimum "
         "conditions for accepting a return."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 13. Required Records/Evidence Checklist
    h(doc, 1, "13. Required Records/Evidence Checklist")

    h(doc, 2, "Safe dispensing — MOM.6.a (Commitment*)")
    lb(doc, "Written safe-dispensing guidance in place.")
    lb(doc,
       "Dispense records showing valid prescription or order checked before "
       "every dispense.")
    lb(doc,
       "Pre-dispense check records covering generic composition, formulation, "
       "expiry date, and strength.")
    lb(doc, "Evidence the process applies to both bulk and retail pharmacy.")
    lb(doc, "Confirmation physicians' samples are not sold.")

    h(doc, 2, "Medication recalls — MOM.6.b (Commitment*)")
    lb(doc, "Established recall system documentation.")
    lb(doc,
       "Recall file with trigger, batches affected, quarantine action, and "
       "recovery steps.")
    lb(doc,
       "Regulatory-authority notification records for any internally identified "
       "recalls.")
    lb(doc, "Records kept on every recall occurrence.")

    h(doc, 2, "Near-expiry and beyond-expiry — MOM.6.c (Commitment*)")
    lb(doc, "Organisation's defined 'near-expiry' threshold (e.g. three months).")
    lb(doc, "Withdrawal records for near-expiry stock.")
    lb(doc,
       "Evidence that no beyond-expiry-date medication is available in usable "
       "clinical stock.")

    h(doc, 2, "Labelling — MOM.6.d (CORE*)")
    lb(doc,
       "Sample labelled dispensed medications showing dosage instructions the "
       "patient can understand.")
    lb(doc,
       "Cut-strip and bulk-container labels showing drug name, strength, expiry "
       "date, and dosage instructions.")
    lb(doc, "Evidence that labelling applies to both inpatients and outpatients.")
    lb(doc,
       "Evidence that labelling applies to reconstituted drugs (e.g. chemotherapy "
       "medications).")

    h(doc, 2, "High-risk order verification — MOM.6.e (CORE)")
    lb(doc, "Written-order records for every high-risk medication dispense.")
    lb(doc,
       "Staff-verification records before dispensing (second-person check or "
       "equivalent).")
    lb(doc, "Statutory compliance records where applicable.")

    h(doc, 2, "Medication returns — MOM.6.f (Commitment*)")
    lb(doc, "Written medication-return guidance.")
    lb(doc, "Inclusion/exclusion list of medications accepted for return.")
    lb(doc,
       "Minimum-conditions record (drug name, strength, batch, expiry matching "
       "bill; no visible damage).")
    lb(doc, "Return records.")

    # 14. References
    h(doc, 1, "14. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. MOM.6.")
    ln(doc, "Guidebook interpretation supplied for MOM.6.a through MOM.6.f.")
    ln(doc,
       f"Internal documents of {HN}: safe-dispensing guidance; recall system "
       "records; near-expiry withdrawal records; medication-return guidance.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied MOM.6 objective-element wording and "
      "Guidebook interpretation into plain-language policy format. The modal strength "
      "of the source has been preserved. Optional examples and mechanisms have not "
      "been converted into mandatory requirements. The labelling scope has been "
      "resolved as universal — applying to both inpatients and outpatients and to "
      "reconstituted drugs — consistent with the operative statement in the Guidebook. "
      "The CORE stop-work trigger for unlabelled, recalled, expired, or unverified "
      "high-risk orders has been retained verbatim. The near-expiry versus "
      "beyond-expiry distinction, and the requirement to report internally identified "
      "recalls to the appropriate regulatory authority, have been retained verbatim.")

    save_and_verify(doc, "HCO_MOM_6_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    gen_mom1()
    print("\nMOM.1 draft generated.")
    gen_mom2()
    print("\nMOM.2 draft generated.")
    gen_mom3()
    print("\nMOM.3 draft generated.")
    gen_mom4()
    print("\nMOM.4 draft generated.")
    gen_mom5()
    print("\nMOM.5 draft generated.")
    gen_mom6()
    print("\nMOM.6 draft generated.")
