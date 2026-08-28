# -*- coding: utf-8 -*-
"""
generate_hco_psq_rewrites.py
Generates HCO PSQ.1-7 v2 rewrite-reference DOCX files.

Pipeline : python-docx, identical to generate_hco_fms_rewrites.py.
Output   : policies/build/rewrite_reference/HCO_PSQ_N_v2_REWRITE_DRAFT.docx
Source   : ChatGPT first-draft content (approved) + policies/drafts_hco/hco_psqN_v2_draft.json
"""
import os
from docx import Document

HN  = "«Hospital Name»"
OUT = "policies/build/rewrite_reference"
os.makedirs(OUT, exist_ok=True)


# ── Helpers (identical to generate_hco_fms_rewrites.py) ──────────────────────

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
        ("Document No.", no,         "Version",              "2.0"),
        ("Issue No.",    "01",        "Review due",           "One year from implementation"),
        ("Date created", "________",  "Date of implementation", "________"),
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

def save_and_verify(doc, fname):
    import sys
    out = sys.stdout
    def pr(s):
        try:
            out.write(s + "\n")
        except UnicodeEncodeError:
            out.write(s.encode("ascii", "replace").decode() + "\n")
    pr(f"\n=== {fname} ===")
    for i, para in enumerate(doc.paragraphs[:60]):
        sn = para.style.name if para.style else "(None)"
        pr(f"{i:3d}  {sn!r:30s}  {para.text[:60]!r}")
    pr(f"  Total paras: {len(doc.paragraphs)}")
    path = os.path.join(OUT, fname)
    doc.save(path)
    print(f"  Saved: {path}")


# ══════════════════════════════════════════════════════════════════════════════
# PSQ.1 — Patient Safety Programme   (no stop-work)
# Content: ChatGPT first draft (approved). Two mechanical fixes applied:
#   1. Section numbers renumbered: Traceability=11, Records=12, References=13
#   2. Literal <b> / </b> stripped from staff acknowledgement sentence
# ══════════════════════════════════════════════════════════════════════════════
def gen_psq1():
    doc = Document()

    # Title + hospital name
    h(doc, 0, "Policy on Patient Safety Programme")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/PSQ/POL/01", "Patient Safety Officer")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc, f"{HN} implements a structured patient safety programme.")
    p(doc,
      "The patient safety programme is developed, implemented and maintained by a multi-disciplinary "
      "safety committee. The programme covers the major elements related to patient safety and incidents "
      "ranging from “no harm” to “sentinel events”. Designated patient safety officer(s) "
      "coordinate implementation of the patient safety programme. The organisation performs proactive "
      "analysis of patient safety risks and makes improvements accordingly. The programme is reviewed "
      "and updated at least once a year and the organisation adapts and implements national and "
      "international patient-safety goals, solutions or frameworks.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "The purpose of this policy is to establish and maintain a structured approach to patient safety "
      "and quality improvement through defined goals, resources, quality indicators, data analysis, "
      "improvement actions and communication of patient safety and quality information.")
    p(doc, "This policy does not cover matters outside the patient safety programme.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies across {HN} to the patient safety programme and the activities supporting "
      "patient safety and quality improvement.")
    p(doc,
      "It applies to the multi-disciplinary safety committee, designated patient safety officer(s), "
      "leadership, relevant staff, departments and, where applicable, the governing body.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 Patient safety and quality goals")
    p(doc, "The organisation identifies patient safety and quality goals for a minimum period of one year.")
    p(doc, "The goals are based on findings from:")
    lb(doc, "Surveillance.")
    lb(doc, "Audit.")
    lb(doc, "Incident reports.")
    lb(doc, "Patient feedback.")
    lb(doc, "Risk assessments.")
    p(doc, "The goals should be measurable and address high-risk, high-volume or problem-prone areas.")

    h(doc, 2, "3.2 Resources for patient safety and quality goals")
    p(doc,
      "Leadership provides adequate human and financial resources to implement and sustain the "
      "identified quality and patient safety goals.")
    p(doc, "Resources include:")
    lb(doc, "Budget.")
    lb(doc, "Staff time.")
    lb(doc, "Training.")
    p(doc,
      "Resource allocation should be visible in planning documents and should not be only stated "
      "as intent.")

    h(doc, 2, "3.3 Quality indicators")
    p(doc,
      "The organisation identifies and monitors quality indicators relevant to clinical and "
      "managerial processes.")
    p(doc, "The indicators are aligned with the identified patient safety and quality goals.")
    p(doc, "Each indicator shall have:")
    lb(doc, "A defined numerator.")
    lb(doc, "A defined denominator.")
    lb(doc, "A defined data-collection frequency.")

    h(doc, 2, "3.4 Quality-data analysis")
    p(doc,
      "The organisation defines a mechanism for aggregating, analysing and using quality-indicator "
      "data on a periodic basis.")
    p(doc, "The mechanism is used to identify:")
    lb(doc, "Trends.")
    lb(doc, "Variances.")
    lb(doc, "Improvement opportunities.")
    p(doc, "Analysis could use run charts, control charts or comparative benchmarking.")

    h(doc, 2, "3.5 Use of quality data for improvement")
    p(doc,
      "The organisation shall document evidence that quality data is used to drive actual "
      "improvement actions.")
    p(doc,
      "Data collection alone, without a documented improvement response, does not meet this "
      "requirement.")

    h(doc, 2, "3.6 Communication of quality and patient safety information")
    p(doc,
      "Quality and patient safety information shall be regularly communicated to relevant staff "
      "and departments.")
    p(doc,
      "Where applicable, the information shall also be communicated to the governing body.")
    p(doc, "Communication could be through:")
    lb(doc, "Dashboards.")
    lb(doc, "Meetings.")
    lb(doc, "Reports.")

    h(doc, 2, "3.7 Quality-improvement tools")
    p(doc,
      "The organisation could use quality-improvement tools to structure improvement projects.")
    p(doc, "Examples include:")
    lb(doc, "PDSA.")
    lb(doc, "Six Sigma.")
    lb(doc, "Lean methodologies.")
    p(doc, "The choice of tool or methodology is not mandated.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    ln(doc,
       "Do not treat quality indicators as complete without defined numerators, denominators and "
       "data-collection frequency.")
    ln(doc,
       "Do not treat quality-data collection alone as sufficient without documented evidence of "
       "the improvement action driven by the data.")
    ln(doc,
       "Do not withhold regular quality and patient safety information from relevant staff and "
       "departments.")
    ln(doc,
       "Do not omit communication of quality and patient safety information to the governing body "
       "where applicable.")
    ln(doc,
       "Do not replace the required quality-data analysis mechanism with a specific analytical tool "
       "as though that tool were mandatory; the use of run charts, control charts or comparative "
       "benchmarking could be selected.")
    ln(doc,
       "Do not make PDSA, Six Sigma or Lean a mandatory methodology for quality-improvement "
       "projects; the choice of tool or methodology is not mandated.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Identify patient safety and quality goals")
    p(doc,
      "The organisation identifies patient safety and quality goals for a minimum period of one year.")
    p(doc,
      "The goals are informed by surveillance, audit, incident reports, patient feedback and "
      "risk assessments.")
    p(doc,
      "Goals should be measurable and should address high-risk, high-volume or problem-prone areas.")

    h(doc, 2, "5.2 Provide resources")
    p(doc,
      "Leadership provides adequate human and financial resources for implementation and "
      "sustainability of the identified goals.")
    p(doc, "The resources include budget, staff time and training.")
    p(doc, "Resource allocation should be visible in planning documents.")

    h(doc, 2, "5.3 Define and monitor indicators")
    p(doc,
      "The organisation identifies quality indicators relevant to clinical and managerial processes.")
    p(doc, "Indicators are aligned with identified goals.")
    p(doc,
      "Each indicator shall have a defined numerator, denominator and data-collection frequency.")

    h(doc, 2, "5.4 Aggregate and analyse data")
    p(doc,
      "Quality-indicator data is aggregated, analysed and used through a defined mechanism.")
    p(doc,
      "The analysis is performed on a periodic basis to identify trends, variances and improvement "
      "opportunities.")
    p(doc,
      "Run charts, control charts or comparative benchmarking could be used for analysis.")

    h(doc, 2, "5.5 Act on quality data")
    p(doc, "The organisation uses quality data to drive actual improvement actions.")
    p(doc,
      "The organisation shall document evidence of the improvement actions arising from quality data.")

    h(doc, 2, "5.6 Communicate information")
    p(doc,
      "Quality and patient safety information shall be regularly communicated to relevant staff "
      "and departments.")
    p(doc, "Where applicable, the governing body receives the information.")
    p(doc, "Dashboards, meetings or reports could be used for communication.")

    h(doc, 2, "5.7 Use improvement tools where appropriate")
    p(doc,
      "The organisation could use PDSA, Six Sigma or Lean methodologies to structure improvement "
      "projects.")
    p(doc, "The choice of quality-improvement tool or methodology is not mandated.")

    # 6. Governance and responsibility
    h(doc, 1, "6. Governance and responsibility")

    h(doc, 2, "6.1 Leadership")
    p(doc,
      "Leadership provides adequate human and financial resources to implement and sustain "
      "identified quality and patient safety goals.")
    p(doc, "Leadership supports resource allocation for budget, staff time and training.")

    h(doc, 2, "6.2 Multi-disciplinary safety committee")
    p(doc,
      "The multi-disciplinary safety committee develops, implements and maintains the patient "
      "safety programme.")
    p(doc,
      "The committee supports the identification of patient safety and quality goals and the "
      "implementation of the programme.")

    h(doc, 2, "6.3 Patient safety officer(s)")
    p(doc,
      "Designated patient safety officer(s) coordinate implementation of the patient safety "
      "programme.")

    h(doc, 2, "6.4 Relevant staff and departments")
    p(doc,
      "Relevant staff and departments participate in the implementation of identified patient "
      "safety and quality goals.")
    p(doc,
      "They receive quality and patient safety information through the defined communication "
      "mechanism.")

    h(doc, 2, "6.5 Governing body")
    p(doc,
      "Where applicable, the governing body receives quality and patient safety information "
      "through the established communication mechanism.")

    # 7. Quality monitoring
    h(doc, 1, "7. Quality monitoring")
    mon_rows = [
        ("Patient safety goals",   "Identified patient safety and quality goals"),
        ("Goal period",            "Goals identified for a minimum period of one year"),
        ("Goal basis",             "Surveillance, audit, incident reports, patient feedback and risk assessments"),
        ("Resources",              "Human and financial resources, budget, staff time and training"),
        ("Quality indicators",     "Clinical and managerial quality indicators"),
        ("Indicator definition",   "Numerator, denominator and data-collection frequency"),
        ("Data management",        "Aggregation, analysis and use of quality-indicator data"),
        ("Data analysis",          "Trends, variances and improvement opportunities"),
        ("Improvement response",   "Documented evidence that quality data drives actual improvement actions"),
        ("Communication",          "Regular communication of quality and patient safety information"),
        ("Recipients",             "Relevant staff, departments and, where applicable, governing body"),
        ("Improvement tools",      "Use of quality-improvement tools where the organisation chooses to use them"),
    ]
    mon = tbl(doc, len(mon_rows) + 1, 2)
    mon.cell(0, 0).text = "Monitoring area"
    mon.cell(0, 1).text = "What is monitored"
    for ri, (area, what) in enumerate(mon_rows, 1):
        mon.cell(ri, 0).text = area
        mon.cell(ri, 1).text = what
    p(doc,
      "Quality monitoring shall distinguish between data collection and documented improvement "
      "response. Data collection without a documented improvement response does not meet the "
      "stated requirement.")

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "Leadership provides training as part of the resources required to implement and sustain "
      "identified quality and patient safety goals.")
    p(doc,
      "Relevant staff participate in activities related to the patient safety programme according "
      "to their responsibilities.")
    p(doc, "Staff acknowledgement:")
    # Fix 2: <b> / </b> stripped — sentence as plain text
    p(doc,
      f"I have read the Policy on Patient Safety Programme of {HN}. I will follow the processes "
      "described.")
    # Sign-off table: 4 columns, 4 rows (header + 3 data)
    sig = tbl(doc, 4, 4)
    for ci, hdr in enumerate(("Staff name", "Designation", "Signature", "Date")):
        sig.cell(0, ci).text = hdr
    for ri in range(1, 4):
        for ci in range(4):
            sig.cell(ri, ci).text = "________"

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "This policy shall be available to relevant staff and departments involved in the patient "
      "safety programme.")
    p(doc,
      "Quality and patient safety information shall be regularly communicated to relevant staff "
      "and departments and, where applicable, the governing body.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("NABH", "National Accreditation Board for Hospitals and Healthcare Providers"),
        ("PDSA", "Plan-Do-Study-Act"),
        ("PSQ",  "Patient Safety and Quality Improvement"),
    ])

    # 11. Traceability table  [fix 1: was 12 in source]
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the Level "
      "column means documentation of the process is required.")
    tr = tbl(doc, 8, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("PSQ.1.a", "CORE*",
         "Sections 3.1, 5.1 and 6.2 address patient safety and quality goals and the development, "
         "implementation and maintenance of the patient safety programme by the multi-disciplinary "
         "safety committee."),
        ("PSQ.1.b", "Commitment",
         "Sections 3.2 and 6.1 address adequate human and financial resources, including budget, "
         "staff time and training, and the visibility of resource allocation in planning documents."),
        ("PSQ.1.c", "Commitment",
         "Sections 3.3 and 5.3 address identification and monitoring of quality indicators and "
         "defined numerators, denominators and data-collection frequency."),
        ("PSQ.1.d", "Commitment",
         "Sections 3.4 and 5.4 address the defined mechanism for aggregating, analysing and using "
         "quality-indicator data on a periodic basis to identify trends, variances and improvement "
         "opportunities."),
        ("PSQ.1.e", "Commitment",
         "Sections 3.5 and 5.5 address documented evidence that quality data is used to drive "
         "actual improvement actions."),
        ("PSQ.1.f", "Commitment",
         "Sections 3.6 and 5.6 address regular communication of quality and patient safety "
         "information to relevant staff, departments and, where applicable, the governing body."),
        ("PSQ.1.g", "CORE",
         "Sections 3.7 and 5.7 address the possible use of quality-improvement tools while "
         "preserving the source position that the choice of tool or methodology is not mandated."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist  [fix 1: was 13 in source]
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Patient safety and quality goals")
    lb(doc, "Current patient safety and quality goals covering a minimum period of one year.")
    lb(doc,
       "Documents showing the goals were based on surveillance findings, audit findings, incident "
       "reports, patient feedback and risk assessments.")
    lb(doc,
       "Goals that are measurable and address high-risk, high-volume or problem-prone areas.")

    h(doc, 2, "Resources and planning")
    lb(doc,
       "Planning documents showing the human and financial resources allocated to patient safety "
       "and quality goals.")
    lb(doc, "Budget allocation for the identified goals.")
    lb(doc, "Staff-time allocation for the identified goals.")
    lb(doc, "Training resources allocated for the identified goals.")

    h(doc, 2, "Quality indicators")
    lb(doc, "List of quality indicators for relevant clinical and managerial processes.")
    lb(doc, "Document showing how each indicator is aligned with the identified goals.")
    lb(doc, "Defined numerator and denominator for each indicator.")
    lb(doc, "Defined data-collection frequency for each indicator.")

    h(doc, 2, "Quality data management and analysis")
    lb(doc, "Defined mechanism for aggregating quality-indicator data.")
    lb(doc, "Defined mechanism for analysing quality-indicator data.")
    lb(doc,
       "Defined mechanism for using quality-indicator data to identify trends, variances and "
       "improvement opportunities.")
    lb(doc,
       "Periodic quality-data analysis showing identified trends, variances and improvement "
       "opportunities, where applicable.")
    lb(doc,
       "Analysis may include run charts, control charts or comparative benchmarking where these "
       "methods are used.")

    h(doc, 2, "Improvement actions")
    lb(doc, "Documents showing quality data led to actual improvement actions.")
    lb(doc,
       "Documentation of the improvement response taken after quality-data analysis.")

    h(doc, 2, "Communication")
    lb(doc,
       "Dashboards, meeting records or reports showing regular communication of quality and patient "
       "safety information to relevant staff and departments.")
    lb(doc, "Where applicable, information shared with the governing body.")
    lb(doc,
       "Records showing the communication method used, such as dashboards, meetings or reports.")

    h(doc, 2, "Quality-improvement methods")
    lb(doc,
       "Where used, project documents showing the quality-improvement tool or methodology selected, "
       "such as PDSA, Six Sigma or Lean.")
    lb(doc,
       "There is no requirement to use a particular quality-improvement tool or methodology.")

    # 13. References  [fix 1: was 14 in source]
    h(doc, 1, "13. References")
    lb(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH Accreditation "
       "Standards for Hospitals, 6th Edition. PSQ.1, “The organisation implements a structured "
       "patient safety programme.”")
    lb(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH Accreditation "
       "Standards for Hospitals, 6th Edition. Guidance on reading standards and objective elements, "
       "including the interpretation of asterisked objective elements as requiring documentation.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied PSQ.1 objective-element wording and Guidebook "
      "interpretation into plain-language policy format. The modal strength of the Guidebook has "
      "been preserved: shall requirements are treated as mandatory, while should, could and examples "
      "have not been converted into mandatory requirements. No additional frequency, deadline, "
      "threshold or prescribed methodology has been added beyond what is stated in the supplied source.")

    save_and_verify(doc, "HCO_PSQ_1_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    gen_psq1()
    print("\nPSQ.1 draft generated.")
