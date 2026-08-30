# -*- coding: utf-8 -*-
"""
generate_hco_cop_rewrites.py
Generates HCO COP chapter v2 rewrite-reference DOCX files.

Pipeline : python-docx, identical to generate_hco_psq_rewrites.py.
Output   : policies/build/rewrite_reference/HCO_COP_N_v2_REWRITE_DRAFT.docx
Source   : ChatGPT first-draft content (approved) + policies/build/cop_raw_dump_*.txt
"""
import os
from docx import Document

HN  = "«Hospital Name»"
OUT = "policies/build/rewrite_reference"
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
# COP.1 — Uniform Care Guided by Written Guidance   (no stop-work)
# Content: ChatGPT final draft (approved, COP 01.pdf).
# Structure: Document control table, Governance table, Section 12 bullet list.
# COREs: b | Stars: a*, f* | Excellence: d, e
# Exact quantities: "at least two identifiers" (3.2), "two clinical care pathways every year" (3.4)
# Telemedicine conditionality: COP.1.f — conditional on service being provided
# ══════════════════════════════════════════════════════════════════════════════
def gen_cop1():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Uniform Patient Care and Clinical Care Pathways")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/COP/POL/01", "Quality Coordinator")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"{HN} ensures that patients with the same clinical condition and care needs receive "
      "the same quality of health care throughout the organisation. Care is provided uniformly "
      "across settings and ward categories and does not depend on whether the patient is paying "
      "or non-paying or on the source of payment.")
    p(doc,
      "The organisation uses patient identification processes, clinical practice guidance, "
      "clinical care pathways and multidisciplinary care planning to support uniform patient care.")
    p(doc,
      "Where telemedicine services are provided, they are delivered safely and securely based "
      "on written guidance.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "The purpose of this policy is to establish requirements for uniform patient care, patient "
      "identification, clinical practice guidance, clinical care pathways, multidisciplinary and "
      "multi-speciality care, and telemedicine where provided.")
    p(doc, "Those requirements are covered in the hospital's other policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc, f"This policy applies to outpatient, day-care, inpatient and emergency care provided by {HN}.")
    p(doc,
      "It applies across different categories of wards and settings of care and to patients "
      "irrespective of whether they are paying or non-paying or supported by a governmental or "
      "private insurance scheme.")
    p(doc, "This section applies where the organisation provides telemedicine services.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 Uniform patient care")
    p(doc,
      "The organisation needs to implement mechanisms to ensure that care received in outpatient, "
      "day-care, inpatient and emergency settings is uniform.")
    p(doc, "The level of care provided to patients shall be the same throughout the organisation.")
    p(doc,
      "Patients with the same clinical condition and care needs shall receive the same quality "
      "of health care throughout the organisation, irrespective of the setting and category of "
      "ward and whether the patient is paying or non-paying or supported by a governmental or "
      "private insurance scheme or not.")
    p(doc,
      "Care is based on the clinical needs of the patient and not on the class or category of "
      "the patient.")
    p(doc,
      "Where the organisation has separate outpatient departments for different categories of "
      "patients, the methodology for care delivery shall be uniform in all outpatient departments.")

    h(doc, 2, "3.2 Patient identification")
    p(doc, "The mechanism for identification of patients shall be uniform across the organisation.")
    p(doc, "For any care-related aspect, at least two identifiers shall be used.")
    p(doc,
      "One of the identifiers shall be the unique identification number generated at the time "
      "of registration.")
    p(doc,
      "The patient identification process shall be used in imaging, diagnostic and therapeutic "
      "procedures, blood transfusion, day care and nutrition or diet.")

    h(doc, 2, "3.3 Evidence-based clinical practice guidelines and clinical protocols")
    p(doc,
      "The organisation implements evidence-based clinical practice guidelines and/or clinical "
      "protocols to guide uniform patient care.")
    p(doc,
      "Clinical practice guidelines brought out by national and international professional "
      "organisations may be used.")
    p(doc,
      "Standard treatment guidelines brought out by the Government of India are a good starting "
      "point.")
    p(doc,
      "In the absence of evidence-based clinical practice guidelines, or where adapting the "
      "clinical practice guidelines is not feasible, sound clinical practices shall guide the "
      "delivery of care.")
    p(doc,
      "For the definitions of evidence-based medicine and clinical practice guidelines, refer "
      "to the Glossary.")

    h(doc, 2, "3.4 Clinical care pathways")
    p(doc,
      "Clinical care pathways shall be multidisciplinary and based on evidence and/or best "
      "clinical practices.")
    p(doc, "They provide detailed guidance at various stages of care.")
    p(doc, "At a minimum, the organisation shall develop two clinical care pathways every year.")
    p(doc,
      "The clinical care pathways shall be followed consistently across all settings of care "
      "and shall be reviewed and updated annually.")

    h(doc, 2, "3.5 Multidisciplinary and multi-speciality care")
    p(doc,
      "Whenever the patient's clinical condition warrants care from multiple disciplines and/or "
      "multiple specialties, a multidisciplinary and multi-speciality care plan shall be charted "
      "out based on established best clinical practices or clinical practice guidelines for the "
      "specific clinical condition.")
    p(doc,
      "An integrated care plan, including medical professional, nursing, nutritional and supportive "
      "care professionals, shall be developed and implemented appropriately by representatives of "
      "the various disciplines and specialities.")
    p(doc,
      "Examples of situations where multidisciplinary care may be required include care of a "
      "cancer patient determined by a multi-disciplinary tumour board, care of transplant patients, "
      "diabetes patients cared for by multiple specialists to prevent and manage end-organ damage, "
      "palliative or end-of-life care for terminally ill patients, and long-stay patients.")

    h(doc, 2, "3.6 Telemedicine")
    p(doc, "This section applies where the organisation provides telemedicine services.")
    p(doc,
      "Whenever the telemedicine facility is provided, the organisation shall develop written "
      "guidance in consonance with prevailing laws and guidelines and implement the same.")
    p(doc,
      "The written guidance shall include protection of the patient's identity and confidentiality.")
    p(doc,
      "The limitations of information and communication technologies shall be explicitly addressed.")
    p(doc, "The organisation shall have a mechanism for appropriate data storage and retrieval.")
    p(doc, "The organisation shall have an MoU for its telemedicine services if outsourced.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not provide different levels of care to patients with the same clinical condition "
       "and care needs because of payment status, source of payment, ward category or care setting.")
    lb(doc,
       "Do not use different care-delivery methods in separate outpatient departments for "
       "different categories of patients.")
    lb(doc,
       "Do not identify a patient for a care-related aspect using fewer than at least two "
       "identifiers.")
    lb(doc,
       "Do not omit the unique identification number generated at registration from the required "
       "patient identifiers.")
    lb(doc,
       "Do not use a non-uniform patient-identification process across the organisation.")
    lb(doc,
       "Do not leave care without evidence-based clinical practice guidelines or feasible "
       "adaptation of such guidelines without using sound clinical practices to guide delivery "
       "of care.")
    lb(doc, "Do not develop fewer than two clinical care pathways every year.")
    lb(doc, "Do not leave clinical care pathways without annual review and update.")
    lb(doc,
       "Do not omit multidisciplinary and multi-speciality care planning when the patient's "
       "clinical condition warrants care from multiple disciplines or specialties.")
    lb(doc,
       "Where telemedicine services are provided, do not provide them without written guidance "
       "developed in accordance with prevailing laws and guidelines.")
    lb(doc,
       "Where telemedicine services are provided, do not operate without protection of patient "
       "identity and confidentiality, explicit consideration of information and communication "
       "technology limitations, and a mechanism for appropriate data storage and retrieval.")
    lb(doc,
       "Where telemedicine services are outsourced, do not provide the outsourced telemedicine "
       "services without an MoU.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Provide uniform care")
    p(doc,
      "Care is provided uniformly across outpatient, day-care, inpatient and emergency settings.")
    p(doc,
      "Patients with the same clinical condition and care needs receive the same quality of "
      "health care throughout the organisation.")
    p(doc,
      "Care is based on clinical need and is not influenced by payment status, source of payment, "
      "ward category or care setting.")

    h(doc, 2, "5.2 Identify patients consistently")
    p(doc, "The same patient-identification mechanism is used throughout the organisation.")
    p(doc,
      "At least two identifiers are used for any care-related aspect, with the registration-"
      "generated unique identification number as one identifier.")
    p(doc,
      "The process is used for imaging, diagnostic and therapeutic procedures, blood transfusion, "
      "day care and nutrition or diet.")

    h(doc, 2, "5.3 Use clinical practice guidance")
    p(doc,
      "Evidence-based clinical practice guidelines and/or clinical protocols guide uniform "
      "patient care.")
    p(doc, "National and international professional organisation guidelines may be used.")
    p(doc, "Government of India standard treatment guidelines are a good starting point.")
    p(doc,
      "Where evidence-based guidelines are absent or cannot feasibly be adapted, sound clinical "
      "practices guide care.")
    p(doc,
      "The Glossary is used for the definitions of evidence-based medicine and clinical practice "
      "guidelines.")

    h(doc, 2, "5.4 Develop and maintain clinical care pathways")
    p(doc,
      "Clinical care pathways are multidisciplinary and based on evidence and/or best clinical "
      "practices.")
    p(doc, "At least two clinical care pathways are developed every year.")
    p(doc,
      "Clinical care pathways are followed consistently across all settings of care and reviewed "
      "and updated annually.")

    h(doc, 2, "5.5 Plan multidisciplinary and multi-speciality care")
    p(doc,
      "When the patient's clinical condition warrants care from multiple disciplines or "
      "specialties, a multidisciplinary and multi-speciality care plan is prepared based on "
      "established best clinical practices or clinical practice guidelines.")
    p(doc,
      "An integrated plan covering medical, nursing, nutritional and supportive care is "
      "developed and implemented appropriately by representatives of the relevant disciplines "
      "and specialities.")

    h(doc, 2, "5.6 Provide telemedicine safely where applicable")
    p(doc,
      "Where the organisation provides telemedicine services, written guidance is developed "
      "and implemented in accordance with prevailing laws and guidelines.")
    p(doc, "Patient identity and confidentiality are protected.")
    p(doc, "Limitations of information and communication technologies are addressed.")
    p(doc, "Appropriate data storage and retrieval are provided.")
    p(doc, "Where telemedicine services are outsourced, an MoU is maintained.")

    # 6. Governance and responsibility — proper table
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        ("Management",
         "Management ensures mechanisms for uniform patient care and supports implementation "
         "of the requirements in this policy."),
        ("Clinical leadership",
         "Clinical leadership supports consistent care delivery, use of clinical practice "
         "guidance, development of clinical care pathways and multidisciplinary and "
         "multi-speciality care where clinically warranted."),
        ("Clinical and nursing personnel",
         "Clinical and nursing personnel follow the applicable patient identification "
         "processes, clinical guidance, clinical care pathways and multidisciplinary care plans."),
        ("Telemedicine responsibility",
         "Where telemedicine is provided, responsible personnel implement the written guidance "
         "and requirements for patient identity, confidentiality, technology limitations, data "
         "storage and retrieval and outsourced services."),
    ])

    # 7. Quality monitoring — table
    h(doc, 1, "7. Quality monitoring")
    mon_tbl(doc, [
        ("Uniform patient care",
         "Same quality of care for patients with the same clinical condition and care needs "
         "across settings and ward categories"),
        ("Patient identification",
         "Uniform process and use of at least two identifiers, including the registration-"
         "generated unique identification number"),
        ("Clinical guidance",
         "Use of evidence-based clinical practice guidelines and/or clinical protocols, or "
         "sound clinical practices where stated"),
        ("Clinical care pathways",
         "Development of two clinical care pathways every year and annual review and update"),
        ("Multidisciplinary care",
         "Care plans when the patient's clinical condition warrants multiple disciplines or "
         "specialties"),
        ("Telemedicine",
         "Written guidance and required safeguards where telemedicine services are provided"),
    ])

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "Staff involved in patient care shall be familiar with the requirements for uniform care, "
      "patient identification, clinical practice guidance, clinical care pathways and "
      "multidisciplinary care applicable to their work.")
    p(doc,
      "Personnel providing telemedicine services, where applicable, shall be familiar with the "
      "written telemedicine guidance.")
    p(doc,
      f"I have read the Policy on Uniform Patient Care and Clinical Care Pathways of {HN}. "
      "I will follow the processes described.")
    sig_tbl(doc)

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "This policy shall be available to personnel involved in patient care and the "
      "implementation of the processes described in this policy.")
    p(doc,
      "Where telemedicine services are provided, the applicable written telemedicine guidance "
      "shall be available to the personnel responsible for those services.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("MoU",   "Memorandum of Understanding"),
        ("ICMR",  "Indian Council of Medical Research"),
        ("MoHFW", "Ministry of Health and Family Welfare"),
    ])

    # 11. Traceability table
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the Level "
      "column means documentation of the process is required.")
    tr = tbl(doc, 7, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("COP.1.a", "Commitment*",
         "Sections 3.1 and 5.1 address uniform care irrespective of setting, ward category, "
         "payment status or source of payment."),
        ("COP.1.b", "CORE",
         "Sections 3.2 and 5.2 address the uniform identification process, at least two "
         "identifiers and the registration-generated unique identification number."),
        ("COP.1.c", "Commitment",
         "Sections 3.3 and 5.3 address clinical practice guidelines, clinical protocols, sound "
         "clinical practices where required and reference to the Glossary."),
        ("COP.1.d", "Excellence",
         "Sections 3.4 and 5.4 address multidisciplinary clinical care pathways, two clinical "
         "care pathways every year, consistent use and annual review and update."),
        ("COP.1.e", "Excellence",
         "Sections 3.5 and 5.5 address clinically triggered multidisciplinary and multi-"
         "speciality care planning and integrated care."),
        ("COP.1.f", "Commitment*",
         "Sections 3.6 and 5.6 address telemedicine requirements conditionally where "
         "telemedicine services are provided."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist — bulleted list
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Uniform patient care")
    lb(doc,
       "Written guidance or mechanisms showing uniform care across outpatient, day-care, "
       "inpatient and emergency settings.")
    lb(doc,
       "Care-delivery processes showing the same quality of health care for patients with "
       "the same clinical condition and care needs.")
    lb(doc,
       "Processes showing that care is not influenced by payment status, source of payment "
       "or ward category.")
    lb(doc,
       "Uniform care-delivery methodology used across separate outpatient departments where "
       "different categories of patients are served.")

    h(doc, 2, "Patient identification")
    lb(doc, "Uniform patient-identification process used across the organisation.")
    lb(doc,
       "Patient identification records showing use of at least two identifiers for care-"
       "related aspects.")
    lb(doc,
       "Patient identification process showing use of the unique identification number "
       "generated at registration as one identifier.")
    lb(doc,
       "Patient identification process applied to imaging, diagnostic and therapeutic "
       "procedures, blood transfusion, day care and nutrition or diet.")

    h(doc, 2, "Clinical practice guidance")
    lb(doc,
       "Evidence-based clinical practice guidelines and/or clinical protocols used to guide "
       "uniform patient care.")
    lb(doc,
       "National or international professional organisation guidelines where the organisation "
       "has chosen to use them.")
    lb(doc,
       "Government of India standard treatment guidelines where used as a starting point.")
    lb(doc,
       "Clinical practices used to guide care where evidence-based clinical practice guidelines "
       "are absent or cannot feasibly be adapted.")
    lb(doc,
       "Access to the Glossary for the definitions of evidence-based medicine and clinical "
       "practice guidelines.")

    h(doc, 2, "Clinical care pathways")
    lb(doc, "At least two clinical care pathways developed every year.")
    lb(doc,
       "Clinical care pathways showing multidisciplinary development and basis in evidence "
       "and/or best clinical practices.")
    lb(doc, "Clinical care pathways showing detailed guidance at various stages of care.")
    lb(doc, "Records showing clinical care pathways are followed across all settings of care.")
    lb(doc, "Records showing clinical care pathways are reviewed and updated annually.")

    h(doc, 2, "Multidisciplinary and multi-speciality care")
    lb(doc,
       "Multidisciplinary and multi-speciality care plans for patients whose clinical condition "
       "warrants care from multiple disciplines or specialties.")
    lb(doc,
       "Integrated care plans covering medical, nursing, nutritional and supportive care where "
       "appropriate.")
    lb(doc,
       "Documentation showing participation by representatives of relevant disciplines and "
       "specialities.")
    lb(doc,
       "Care plans based on established best clinical practices or clinical practice guidelines "
       "for the specific clinical condition.")

    h(doc, 2, "Telemedicine")
    lb(doc,
       "Written telemedicine guidance where the organisation provides telemedicine services.")
    lb(doc, "Telemedicine guidance aligned with prevailing laws and guidelines.")
    lb(doc, "Safeguards protecting patient identity and confidentiality.")
    lb(doc,
       "Written consideration of limitations of information and communication technologies.")
    lb(doc, "Mechanism for appropriate telemedicine data storage and retrieval.")
    lb(doc, "MoU for outsourced telemedicine services where applicable.")

    # 13. References
    h(doc, 1, "13. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH Accreditation "
       "Standards for Hospitals, 6th Edition. COP.1.")
    ln(doc, "Guidebook interpretation supplied for COP.1.a through COP.1.f.")
    ln(doc,
       "NABH Glossary for the definitions of evidence-based medicine and clinical practice "
       "guidelines.")
    ln(doc, "Telemedicine Practice Guidelines, ICMR, 2020, MoHFW.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied COP.1 objective-element wording and Guidebook "
      "interpretation into plain-language policy format. The modal strength of the source has "
      "been preserved. Optional examples and mechanisms have not been converted into mandatory "
      "requirements. The exact requirements of at least two identifiers, two clinical care "
      "pathways every year, and annual review and update have been retained. Telemedicine "
      "requirements are conditional and apply where the organisation provides telemedicine "
      "services.")

    save_and_verify(doc, "HCO_COP_1_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# COP.2 — Emergency Services   (HAS stop-work: Section 6)
# Content: ChatGPT final draft (approved, COP 02.pdf).
# Structure: Document control table, Stop-work Section 6, Governance table,
#            Section 13 bullet checklist, Section 14 References.
# COREs: c | Stars: c*, d*, h*, i* | Stop-work trigger: identified area + triage competence + overcrowding
# Death management: 5 BID elements + 4 post-resus elements = 9 total (all mandatory)
# ══════════════════════════════════════════════════════════════════════════════
def gen_cop2():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Emergency Care Services")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/COP/POL/02", "Emergency In-Charge")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"{HN} provides emergency patients with accessible emergency care, appropriate resources, "
      "written emergency guidance, qualified triage, reassessment, documented disposition, "
      "discharge or transfer information, quality assurance, and defined processes for patients "
      "found dead on arrival or who die within a few minutes of arrival.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "The purpose of this policy is to establish requirements for receiving and managing "
      "emergency patients, triage, reassessment, disposition, transfer, emergency quality "
      "assurance, and management of patients found dead on arrival or who die within a few "
      "minutes of arrival.")
    p(doc, "Those requirements are covered in the hospital's other policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to the emergency department and personnel involved in emergency "
      f"patient care at {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 Emergency area and resources")
    p(doc,
      "The identified area to treat emergency patients shall be easily accessible for initiation "
      "of care.")
    p(doc, "There shall be understandable signage and directions leading to the emergency area.")
    p(doc,
      "Emergency services preferably have designated triage, resuscitation treatment and patient "
      "holding areas.")
    p(doc,
      "The organisation shall specify the minimum number of beds based on its scope of services.")
    p(doc,
      "At a minimum, adequate and appropriate human resources, basic resuscitation equipment, "
      "equipment for monitoring vital parameters, appropriate consumables, and life-saving and "
      "emergency care drugs shall be available.")
    p(doc,
      "Personnel operating the emergency area shall be privileged to work in this area and have "
      "access to ongoing training.")

    h(doc, 2, "3.2 Overcrowding and crowd management")
    p(doc,
      "Prevention of patient overcrowding includes monitoring footfall trends and developing "
      "strategies to manage overcrowding and violence.")
    p(doc,
      "High footfall times are expected to be anticipated, with adequate human resources assigned "
      "and strategies to manage overcrowding put in place.")
    p(doc,
      "Crowd management shall include an appropriate policy for patient relatives, attendants "
      "and visitors.")

    h(doc, 2, "3.3 Emergency care and medico-legal cases")
    p(doc,
      "Written guidance shall include guidelines, SOPs or protocols for general emergency care "
      "and management of specific conditions, for example poisoning, road traffic accidents, "
      "acute stroke and coronary disease.")
    p(doc, "It shall address both adult and paediatric patients.")
    p(doc,
      "The procedure shall incorporate at a minimum identification, assessment and provision "
      "of care.")
    p(doc,
      "Where emergency services are outside the scope of the organisation, or facilities for "
      "appropriate emergency care of a given clinical condition are unavailable, at a minimum "
      "the patient shall be provided first aid before transfer to another organisation.")
    p(doc, "Processes shall be in place to ensure patient safety.")
    p(doc, "The organisation shall define what constitutes a medico-legal case (MLC).")
    p(doc,
      "Care provided, especially documentation and intimation to appropriate authorities, shall "
      "be in accordance with statutory requirements.")
    p(doc,
      "The organisation shall have a policy on management of suspected sexual assault and "
      "guidance on storage of samples of MLC patients.")

    h(doc, 2, "3.4 Triage")
    p(doc, "Triage shall be done only by qualified/trained personnel.")
    p(doc,
      "Written guidance based on evidence or sound clinical practices shall guide triage.")
    p(doc,
      "Triage shall be part of routine day-to-day functioning of the emergency department and "
      "not only disaster management.")
    p(doc,
      "Criteria could be separate for trauma and non-trauma patients and adults and children, "
      "for example PAT or POPS.")
    p(doc,
      "If several clients are waiting to be triaged, a visual triage assessment may be "
      "conducted.")

    h(doc, 2, "3.5 Reassessment")
    p(doc,
      "Patients waiting in the emergency are reassessed as appropriate for a change in status.")
    p(doc,
      "The findings of reassessment shall be documented in the patient's medical record.")

    h(doc, 2, "3.6 Admission, discharge and transfer")
    p(doc,
      "The organisation shall maintain documentation indicating whether an emergency patient "
      "was sent home after initial care, admitted for further care, admitted in an emergency "
      "for a short stay and then discharged, or transferred to another organisation.")
    p(doc,
      "Staff shall have a clear understanding of the scope of the organisation's activities "
      "and the procedure for referral and transfer to another appropriate centre for patients "
      "who cannot be cared for in-house, after due first-aid or emergency care.")

    h(doc, 2, "3.7 Discharge and transfer note")
    p(doc,
      "In case of discharge to home or transfer to another organisation, a discharge or "
      "transfer note shall be given to the patient.")
    p(doc,
      "The note shall contain salient clinical findings, investigations done, treatment given "
      "and condition at discharge or transfer.")
    p(doc, "The reasons for discharge or transfer shall be documented.")

    h(doc, 2, "3.8 Quality assurance")
    p(doc, "The organisation shall implement a quality assurance programme.")
    p(doc,
      "Written quality assurance guidance may be developed individually or could be part of "
      "the organisation's overall quality-improvement programme.")
    p(doc,
      "The quality assurance programme shall involve all aspects of the functioning of the "
      "Emergency department.")
    p(doc,
      "The Emergency department shall collect data on key performance indicators, including "
      "care outcomes, as part of its quality improvement programme.")
    p(doc,
      "An example of a care outcome measure is return to the emergency department for the "
      "same complaint.")
    p(doc,
      "Collected data shall be collated, analysed and used for further improvements.")
    p(doc, "Improvements shall be monitored for sustenance.")

    h(doc, 2, "3.9 Patients found dead on arrival")
    p(doc,
      "There shall be written guidance for managing a patient found dead on arrival, conforming "
      "to relevant local laws.")
    p(doc,
      "The guidance shall address maintaining a logbook of patients found dead on arrival; "
      "the decision on whether to perform a post-mortem; the decision regarding issue of a "
      "medical certificate of cause of death; temporary storage of the body in appropriate "
      "conditions; and what to do in case of unclaimed or unaccompanied bodies.")

    h(doc, 2, "3.10 Patients who die within a few minutes of arrival")
    p(doc,
      "There shall be written guidance for managing a patient who dies within a few minutes "
      "of arrival after a failed attempt at resuscitation, conforming to relevant local laws.")
    p(doc,
      "The guidance shall address registration of such patients and recording the entire "
      "resuscitation events; the decision on whether to perform a post-mortem; temporary "
      "storage of the body in appropriate conditions; issue of a medical certificate of cause "
      "of death; and handing over of the body.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not receive and treat an emergency patient in an area that is not the identified "
       "emergency area, or when triage-competent personnel and basic resuscitation equipment "
       "are not available.")
    lb(doc,
       "Do not leave overcrowding unmanaged when it blocks triage, resuscitation or safe "
       "holding.")
    lb(doc,
       "Do not provide emergency care without written guidance incorporating at minimum "
       "identification, assessment and provision of care.")
    lb(doc,
       "Do not transfer a patient without first providing first aid when appropriate emergency "
       "care is outside the organisation's scope or unavailable for the given clinical condition.")
    lb(doc,
       "Do not perform triage through personnel who are not qualified/trained.")
    lb(doc,
       "Do not treat triage as only a disaster-management activity; it shall be part of "
       "routine day-to-day emergency functioning.")
    lb(doc,
       "Do not omit documentation of reassessment findings in the patient's medical record.")
    lb(doc,
       "Do not discharge a patient home or transfer a patient without giving the patient the "
       "required discharge or transfer note.")
    lb(doc,
       "Do not omit any of the required contents of the discharge or transfer note or the "
       "reasons for discharge or transfer.")
    lb(doc,
       "Do not omit the required management processes for either a patient found dead on "
       "arrival or a patient who dies within a few minutes after arrival following failed "
       "resuscitation.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Emergency intake and resources")
    p(doc,
      "Maintain an accessible identified emergency area with understandable signage and "
      "directions.")
    p(doc, "Specify the minimum number of beds based on scope of services.")
    p(doc,
      "Maintain adequate and appropriate human resources, basic resuscitation equipment, "
      "vital-parameter monitoring equipment, consumables and life-saving/emergency care drugs.")
    p(doc,
      "Ensure emergency personnel are privileged to work in the area and have access to "
      "ongoing training.")

    h(doc, 2, "5.2 Crowd management")
    p(doc,
      "Monitor footfall trends and develop strategies for overcrowding and violence.")
    p(doc,
      "Anticipate high footfall times, assign adequate human resources and put strategies "
      "in place.")
    p(doc,
      "Maintain an appropriate policy for patient relatives, attendants and visitors.")

    h(doc, 2, "5.3 Emergency care")
    p(doc,
      "Use written guidelines, SOPs or protocols for general emergency care and specific "
      "conditions.")
    p(doc, "Cover adult and paediatric patients.")
    p(doc,
      "Use identification, assessment and provision of care as the minimum procedure elements.")
    p(doc,
      "Provide first aid before transfer when appropriate emergency care is outside scope or "
      "unavailable.")

    h(doc, 2, "5.4 Triage")
    p(doc, "Ensure triage is performed only by qualified/trained personnel.")
    p(doc, "Use written guidance based on evidence or sound clinical practices.")
    p(doc, "Keep triage as part of routine day-to-day emergency functioning.")
    p(doc,
      "Separate criteria or visual triage assessment may be used as described in the Guidebook.")

    h(doc, 2, "5.5 Reassessment")
    p(doc,
      "Reassess patients waiting in emergency as appropriate for a change in status.")
    p(doc, "Document reassessment findings in the patient's medical record.")

    h(doc, 2, "5.6 Disposition and transfer")
    p(doc,
      "Document whether patients are sent home, admitted, kept for a short emergency stay "
      "and discharged, or transferred.")
    p(doc,
      "Ensure staff understand the scope of activities and referral and transfer procedures.")

    h(doc, 2, "5.7 Discharge and transfer note")
    p(doc,
      "Give the patient a discharge or transfer note when discharged home or transferred.")
    p(doc,
      "Include salient clinical findings, investigations done, treatment given, condition at "
      "discharge or transfer, and reasons for discharge or transfer.")

    h(doc, 2, "5.8 Quality assurance")
    p(doc,
      "Implement a quality assurance programme covering all aspects of Emergency department "
      "functioning.")
    p(doc,
      "Collect, collate and analyse key performance indicator data, including care outcomes.")
    p(doc,
      "Use collected data for further improvements and monitor improvements for sustenance.")
    p(doc,
      "The quality assurance programme may be standalone or could be part of the overall "
      "quality-improvement programme.")

    h(doc, 2, "5.9 Patients found dead on arrival")
    p(doc, "Use written guidance conforming to relevant local laws.")
    p(doc,
      "Address the logbook, post-mortem decision, medical certificate of cause of death "
      "decision, temporary body storage and unclaimed/unaccompanied bodies.")

    h(doc, 2, "5.10 Patients who die within a few minutes of arrival")
    p(doc, "Use written guidance conforming to relevant local laws.")
    p(doc,
      "Address registration and complete recording of resuscitation events, post-mortem "
      "decision, temporary body storage, medical certificate of cause of death and handing "
      "over of the body.")

    # 6. Stop-work authority
    h(doc, 1, "6. Stop-work authority")
    p(doc,
      "Do not receive and treat an emergency patient in an area that is not the identified "
      "emergency area, or when triage-competent personnel and basic resuscitation equipment "
      "are not available. Do not leave overcrowding unmanaged when it blocks triage, "
      "resuscitation or safe holding. Stop-work applies to unsafe emergency intake, not to "
      "immediate life-saving measures already under way — those continue while escalation "
      "happens. The person who stops tells the Emergency In-Charge and the Medical "
      "Superintendent the same shift. Refusing unsafe emergency intake is not a disciplinary "
      "matter.")

    # 7. Governance and responsibility — proper table
    h(doc, 1, "7. Governance and responsibility")
    gov_tbl(doc, [
        ("Management",
         "Management ensures the identified emergency area, required resources, written "
         "guidance and quality assurance arrangements."),
        ("Emergency In-Charge",
         "The Emergency In-Charge oversees emergency operations and escalation of unsafe "
         "emergency intake."),
        ("Qualified/trained personnel",
         "Qualified/trained personnel perform triage."),
        ("Emergency personnel",
         "Emergency personnel follow applicable emergency, reassessment, referral, transfer "
         "and documentation processes."),
        ("Quality personnel",
         "Quality personnel support quality assurance data collection, collation, analysis "
         "and improvement monitoring."),
    ])

    # 8. Quality monitoring — proper table
    h(doc, 1, "8. Quality monitoring")
    mon_tbl(doc, [
        ("Emergency footfall and overcrowding",
         "Emergency department footfall and overcrowding trends"),
        ("Emergency care KPIs",
         "Emergency care key performance indicators, including care outcomes"),
        ("Quality data",
         "Quality data collation and analysis"),
        ("Improvements",
         "Further improvements and monitoring for sustenance"),
        ("Reassessment and disposition",
         "Reassessment documentation and patient disposition documentation"),
        ("Discharge and transfer note",
         "Discharge and transfer note requirements"),
    ])

    # 9. Training and staff acknowledgement
    h(doc, 1, "9. Training and staff acknowledgement")
    p(doc,
      "Personnel operating the emergency area shall have access to ongoing training. Triage "
      "shall be performed only by qualified/trained personnel.")
    p(doc,
      "Staff shall have a clear understanding of the scope of the organisation's activities "
      "and applicable referral and transfer procedures.")
    p(doc,
      f"I have read the Policy on Emergency Care Services of {HN}. I will follow the "
      "processes described.")
    sig_tbl(doc)

    # 10. Distribution
    h(doc, 1, "10. Distribution")
    p(doc,
      "This policy shall be available to personnel involved in emergency care and emergency "
      "department operations.")

    # 11. Abbreviations
    h(doc, 1, "11. Abbreviations")
    abbrev_tbl(doc, [
        ("MLC",  "Medico-legal case"),
        ("SOP",  "Standard Operating Procedure"),
        ("PAT",  "Paediatric Assessment Triangle"),
        ("POPS", "Paediatric Observation Priority Score"),
    ])

    # 12. Traceability table
    h(doc, 1, "12. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the Level "
      "column means documentation of the process is required.")
    tr = tbl(doc, 10, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("COP.2.a", "Commitment",
         "Sections 3.1 and 5.1 address the identified accessible emergency area, signage and "
         "directions, minimum beds, resources, privileged personnel and ongoing training."),
        ("COP.2.b", "Achievement",
         "Sections 3.2 and 5.2 address prevention of overcrowding and crowd management, "
         "including the required policy for patient relatives, attendants and visitors."),
        ("COP.2.c", "CORE*",
         "Sections 3.3 and 5.3 address emergency care in accordance with statutory requirements "
         "and written guidance, including minimum identification, assessment and provision of care, "
         "MLC definition, statutory documentation, sexual assault policy and MLC sample storage."),
        ("COP.2.d", "Commitment*",
         "Sections 3.4 and 5.4 address triage by qualified/trained personnel using written "
         "guidance as routine emergency functioning."),
        ("COP.2.e", "Commitment",
         "Sections 3.5 and 5.5 address appropriate reassessment for change in status and "
         "documentation of findings."),
        ("COP.2.f", "Commitment",
         "Sections 3.6 and 5.6 address documentation of admission, discharge and transfer and "
         "the clear referral/transfer process."),
        ("COP.2.g", "Commitment",
         "Sections 3.7 and 5.7 address the discharge/transfer note with salient clinical "
         "findings, investigations done, treatment given, condition at discharge/transfer and "
         "reasons."),
        ("COP.2.h", "Achievement*",
         "Sections 3.8 and 5.8 address the quality assurance programme, Emergency department "
         "coverage, KPI data, analysis, improvement and sustenance monitoring."),
        ("COP.2.i", "Commitment*",
         "Sections 3.9, 3.10, 5.9 and 5.10 address systems for management of patients found "
         "dead on arrival (five mandatory elements) and patients who die within a few minutes "
         "of arrival after failed resuscitation (four mandatory elements)."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 13. Required Records/Evidence Checklist — bulleted list
    h(doc, 1, "13. Required Records/Evidence Checklist")

    h(doc, 2, "Emergency area and resources")
    lb(doc, "Identified emergency area with signage and understandable directions.")
    lb(doc, "Minimum number of beds specified based on scope of services.")
    lb(doc,
       "Human resources, basic resuscitation equipment, vital-parameter monitoring equipment, "
       "consumables and life-saving/emergency drugs available.")
    lb(doc, "Emergency personnel privileging and ongoing training arrangements.")

    h(doc, 2, "Crowd management")
    lb(doc, "Footfall trend information and overcrowding/violence management strategies.")
    lb(doc, "Planning for high-footfall times and allocation of adequate human resources.")
    lb(doc, "Policy for patient relatives, attendants and visitors.")

    h(doc, 2, "Emergency care and MLC")
    lb(doc,
       "Written emergency guidelines, SOPs or protocols for general care and specific "
       "conditions.")
    lb(doc, "Adult and paediatric emergency guidance.")
    lb(doc, "Emergency procedure covering identification, assessment and provision of care.")
    lb(doc,
       "First-aid and transfer arrangements where appropriate emergency care is outside "
       "scope or unavailable.")
    lb(doc, "Patient-safety processes.")
    lb(doc, "Definition of MLC and statutory documentation/intimation process.")
    lb(doc,
       "Policy for suspected sexual assault management and guidance for storage of MLC "
       "samples.")

    h(doc, 2, "Triage and reassessment")
    lb(doc, "Qualification/training arrangements for personnel performing triage.")
    lb(doc, "Written triage guidance based on evidence or sound clinical practices.")
    lb(doc, "Routine day-to-day triage process.")
    lb(doc, "Medical records containing documented reassessment findings.")

    h(doc, 2, "Disposition and transfer")
    lb(doc,
       "Emergency records showing whether patients were sent home, admitted, kept for short "
       "emergency stay and discharged, or transferred.")
    lb(doc,
       "Referral and transfer procedure for patients who cannot be cared for in-house after "
       "due first-aid/emergency care.")
    lb(doc,
       "Discharge/transfer notes containing salient clinical findings, investigations done, "
       "treatment given, condition at discharge/transfer and reasons for discharge/transfer.")

    h(doc, 2, "Quality assurance")
    lb(doc,
       "Written quality assurance guidance, standalone or part of the overall "
       "quality-improvement programme.")
    lb(doc, "Emergency department quality assurance covering all aspects of functioning.")
    lb(doc,
       "Key performance indicator and care-outcome data with collation and analysis.")
    lb(doc, "Improvement actions and monitoring for sustenance.")

    h(doc, 2, "Found dead on arrival")
    lb(doc, "Written guidance conforming to relevant local laws.")
    lb(doc, "Logbook for patients found dead on arrival.")
    lb(doc,
       "Post-mortem decision and medical certificate of cause of death decision processes.")
    lb(doc, "Temporary body storage arrangements.")
    lb(doc, "Process for unclaimed or unaccompanied bodies.")

    h(doc, 2, "Death within a few minutes of arrival")
    lb(doc, "Written guidance conforming to relevant local laws.")
    lb(doc, "Registration process and complete recording of resuscitation events.")
    lb(doc, "Post-mortem decision process.")
    lb(doc, "Temporary body storage arrangements.")
    lb(doc, "Medical certificate of cause of death process and body-handover process.")

    # 14. References
    h(doc, 1, "14. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH Accreditation "
       "Standards for Hospitals, 6th Edition. COP.2.")
    ln(doc, "Guidebook interpretation supplied for COP.2.a through COP.2.i.")
    ln(doc,
       "Relevant local laws for management of patients found dead on arrival or who die within "
       "a few minutes of arrival.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy is a plain-language reorganisation of the supplied COP.2 objective elements "
      "and Guidebook interpretation. Mandatory requirements, stated examples, preferable measures "
      "and optional mechanisms have been kept at their stated level of strength.")

    save_and_verify(doc, "HCO_COP_2_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# COP.3 — Ambulance Services and Safe Transportation   (HAS stop-work: Section 6)
# Content: ChatGPT final draft (approved, COP%2003.pdf).
# Structure: Document control table, Stop-work Section 6, Governance table,
#            Section 13 bullet checklist, Section 14 References.
# COREs: none | Stars: f* | Stop-work: dispatch triggers only (NOT overcrowding)
# FIX: The sentence "Do not leave overcrowding unmanaged when it blocks triage,
#      resuscitation or safe holding." belongs to COP.2 and is excluded here.
# ══════════════════════════════════════════════════════════════════════════════
def gen_cop3():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Ambulance Services")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/COP/POL/03", "Ambulance/Transport In-Charge")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"{HN} shall have access to ambulance services commensurate with its scope of services. "
      "Ambulance services shall support safe patient transport with appropriate care, adequate "
      "access and space, appropriate equipment and trained personnel, reliable communication, "
      "and safe transfer of clinical information.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "The purpose of this policy is to establish requirements for ambulance access, space, "
      "statutory fitness, equipment, personnel, daily and post-trip checks, communication and "
      "support for patients while in transit.")
    p(doc, "Those requirements are covered in the hospital's other policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to ambulance services used by {HN}, whether provided in-house or "
      "through an outsourced service.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 Ambulance access and level")
    p(doc,
      "The organisation may provide an in-house or outsourced ambulance service for safe "
      "patient transport with appropriate care.")
    p(doc,
      "The organisation shall decide the appropriate level of ambulance based on the National "
      "Ambulance Code AIS-125.")

    h(doc, 2, "3.2 Ambulance space and access")
    p(doc,
      "The organisation shall demarcate a proper space for ambulances, keeping easy "
      "accessibility for receiving patients and enabling ambulances to exit quickly.")
    p(doc,
      "Adequate and prominent signage shall guide ambulance drivers to the ambulance entry "
      "and route to the emergency department.")
    p(doc, "It is preferable that the organisation has an ambulance parking bay.")

    h(doc, 2, "3.3 Fitness and equipment")
    p(doc,
      "The vehicle used as an ambulance shall adhere to applicable statutory requirements. "
      "Examples include registration as an ambulance under the Motor Vehicle Act, a valid "
      "fitness certificate, pollution control certificate and insurance. These are examples "
      "and not an exhaustive list of statutory requirements.")
    p(doc,
      "An ambulance shall have at least basic life support equipment for both adult and "
      "paediatric patients.")
    p(doc,
      "Based on the organisation's scope, additional equipment, for example monitoring and "
      "resuscitative equipment, shall be available in the ambulance.")
    p(doc, "Reference: National Ambulance Code AIS-125.")

    h(doc, 2, "3.4 Personnel")
    p(doc, "The ambulance shall be operated by a driver with a valid driving licence.")
    p(doc,
      "Personnel in the ambulance shall have training in basic life support and basic "
      "cardiopulmonary resuscitation.")
    p(doc,
      "A technician, nurse and/or doctor may be present depending on the situation and "
      "scope of the ambulance.")

    h(doc, 2, "3.5 Daily and post-trip checks")
    p(doc,
      "The daily check shall indicate the functioning status of ambulance systems like "
      "lights, siren, beacon lights, fuel and tyres.")
    p(doc, "Medical equipment shall be checked using a documented checklist.")
    p(doc,
      "Emergency medications shall be available in the ambulance during patient transport.")
    p(doc,
      "A daily check shall ensure availability and expiry dates of emergency medications "
      "and shall be documented.")
    p(doc,
      "After every trip, medications used shall be topped up if used and the same verified "
      "and documented.")
    p(doc,
      "Medications shall be stored in a safe environment as per organisational policy.")
    p(doc,
      "If the organisation follows a system of sealing the emergency medication kit, the "
      "check shall be carried out after each use of the kit.")

    h(doc, 2, "3.6 Communication")
    p(doc,
      "The ambulance shall be connected with the organisation/control room by "
      "wireless/mobile phones.")
    p(doc,
      "The communication system shall encompass the whole process of patient transport.")
    p(doc,
      "There shall be written guidance on how a call for patient transport is received, "
      "who is expected to respond and who organises the transport.")
    p(doc,
      "Communication shall ensure that the ambulance leaves the hospital within a "
      "predefined timeframe based upon the patient's needs.")

    h(doc, 2, "3.7 Care while in transit")
    p(doc,
      "From first communication with the patient or attendant, a file is created to record "
      "appropriate information.")
    p(doc,
      "Attempts are made to gather important clinical information such as age, weight, "
      "provisional diagnosis and ongoing treatment at the referring organisation.")
    p(doc,
      "This information is used by ambulance personnel of the receiving organisation to be "
      "better prepared to assess, initiate emergency care/interventions during transit and "
      "transport the patient safely.")
    p(doc,
      "During transit, when required, there is an exchange of information between ambulance "
      "personnel and the medical professional at the receiving organisation.")
    p(doc,
      "When the patient is shifted by an external agency, wherever possible, the doctor of "
      "the receiving organisation attempts to communicate with the ambulance personnel of the "
      "external agency to ascertain the clinical situation and make appropriate suggestions.")
    p(doc,
      "The medical professional in the ambulance is responsible for decision-making regarding "
      "care/interventions during transit.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not dispatch or continue an ambulance transfer when the vehicle fails its readiness "
       "check, required equipment is non-functional, the driver is not licensed for the vehicle "
       "class, or the organisation/control-room communication link is down.")
    lb(doc,
       "Do not operate an ambulance without at least basic life support equipment for both "
       "adult and paediatric patients.")
    lb(doc,
       "Do not operate an ambulance without a driver with a valid driving licence.")
    lb(doc,
       "Do not allow ambulance personnel to provide service without basic life support and "
       "basic cardiopulmonary resuscitation training.")
    lb(doc,
       "Do not omit the daily check of vehicle systems, medical equipment and emergency "
       "medication availability and expiry, or the required documentation.")
    lb(doc,
       "Do not omit the post-trip top-up of medications used, verification and documentation.")
    lb(doc,
       "Where a sealed emergency medication kit is used, do not omit the check after each use.")
    lb(doc,
       "Do not operate the ambulance without the required organisation/control-room "
       "communication link, whole-process communication coverage and written call-receipt/"
       "response guidance.")
    lb(doc,
       "Do not dispatch an ambulance outside the predefined timeframe based on the patient's "
       "needs.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Access and ambulance level")
    p(doc,
      "Provide in-house or outsourced ambulance service as decided by the organisation.")
    p(doc,
      "Select the appropriate ambulance level based on National Ambulance Code AIS-125.")

    h(doc, 2, "5.2 Space and access")
    p(doc, "Demarcate ambulance space for easy patient receipt and quick exit.")
    p(doc,
      "Maintain prominent signage to the ambulance entry and emergency department route.")
    p(doc, "An ambulance parking bay may be provided.")

    h(doc, 2, "5.3 Vehicle fitness and equipment")
    p(doc, "Maintain statutory compliance applicable to the ambulance.")
    p(doc, "Provide at least basic life support equipment for adult and paediatric patients.")
    p(doc, "Provide additional monitoring and resuscitative equipment based on scope.")

    h(doc, 2, "5.4 Personnel")
    p(doc, "Use a driver with a valid driving licence.")
    p(doc,
      "Ensure ambulance personnel have basic life support and basic cardiopulmonary "
      "resuscitation training.")
    p(doc,
      "A technician, nurse and/or doctor may be included depending on situation and scope.")

    h(doc, 2, "5.5 Checks and medication")
    p(doc,
      "Perform and document the daily vehicle, medical equipment and medication checks.")
    p(doc, "After every trip, top up medications used, verify and document this.")
    p(doc, "Where a sealed kit system is used, check the kit after each use.")
    p(doc, "Store medications safely according to organisational policy.")

    h(doc, 2, "5.6 Communication")
    p(doc,
      "Maintain connection with the organisation/control room by wireless or mobile phones.")
    p(doc, "Ensure communication covers the whole transport process.")
    p(doc, "Follow written call-receipt and response guidance.")
    p(doc,
      "Ensure ambulance departure within the predefined timeframe based on patient needs.")

    h(doc, 2, "5.7 In-transit care")
    p(doc,
      "Create a file from first communication and gather appropriate clinical information.")
    p(doc,
      "Use available information to prepare for assessment, emergency care/interventions "
      "and safe transport.")
    p(doc,
      "Exchange information with the receiving medical professional when required.")
    p(doc,
      "Where an external agency transports the patient, wherever possible, the receiving "
      "doctor attempts communication with its ambulance personnel.")
    p(doc,
      "The medical professional in the ambulance makes decisions regarding "
      "care/interventions during transit.")

    # 6. Stop-work authority
    # NOTE: "Do not leave overcrowding unmanaged when it blocks triage, resuscitation or
    # safe holding." is a COP.2 sentence that leaked into earlier drafts — it is excluded here.
    h(doc, 1, "6. Stop-work authority")
    p(doc,
      "Do not dispatch or continue an ambulance transfer when the vehicle fails its readiness "
      "check, required equipment is non-functional, the driver is not licensed for the vehicle "
      "class, or the organisation/control-room communication link is down. Stop-work applies "
      "to the transfer dispatch, not to on-scene life-saving measures. The person who stops "
      "tells the Ambulance / Transport In-Charge and the Medical Superintendent the same shift. "
      "Refusing an unsafe ambulance dispatch is not a disciplinary matter.")

    # 7. Governance and responsibility — proper table
    h(doc, 1, "7. Governance and responsibility")
    gov_tbl(doc, [
        ("Ambulance/Transport In-Charge",
         "Ambulance/Transport In-Charge oversees ambulance readiness, dispatch, communication "
         "and transport processes."),
        ("Management",
         "Management determines the appropriate ambulance level and whether services are "
         "provided in-house or outsourced."),
        ("Ambulance personnel",
         "Ambulance personnel maintain required checks, equipment, medications and "
         "communication."),
        ("Medical professional in ambulance",
         "The medical professional in the ambulance is responsible for decision-making "
         "regarding care/interventions during transit."),
    ])

    # 8. Quality monitoring — proper table
    h(doc, 1, "8. Quality monitoring")
    mon_tbl(doc, [
        ("Daily readiness checks",
         "Daily ambulance readiness checks and documented findings"),
        ("Post-trip checks",
         "Post-trip medication top-up, verification and documentation"),
        ("Equipment and medication",
         "Equipment functionality and medication availability/expiry"),
        ("Communication",
         "Communication-system availability and predefined response timeframe"),
        ("Access and space",
         "Ambulance access, space and signage"),
        ("Statutory compliance",
         "Compliance with applicable statutory requirements"),
    ])

    # 9. Training and staff acknowledgement
    h(doc, 1, "9. Training and staff acknowledgement")
    p(doc,
      "Ambulance personnel shall have basic life support and basic cardiopulmonary "
      "resuscitation training. The ambulance driver shall have a valid driving licence.")
    p(doc,
      f"I have read the Policy on Ambulance Services of {HN}. I will follow the processes "
      "described.")
    sig_tbl(doc)

    # 10. Distribution
    h(doc, 1, "10. Distribution")
    p(doc,
      "This policy shall be available to ambulance/transport personnel and personnel "
      "responsible for emergency patient transport.")

    # 11. Abbreviations
    h(doc, 1, "11. Abbreviations")
    abbrev_tbl(doc, [
        ("AIS", "Automotive Industry Standard"),
        ("CPR", "Cardiopulmonary Resuscitation"),
    ])

    # 12. Traceability table
    h(doc, 1, "12. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the Level "
      "column means documentation of the process is required.")
    tr = tbl(doc, 8, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("COP.3.a", "Commitment",
         "Sections 3.1 and 5.1 address access to ambulance services commensurate with scope "
         "and ambulance level selection based on National Ambulance Code AIS-125."),
        ("COP.3.b", "Commitment",
         "Sections 3.2 and 5.2 address adequate ambulance access and space, quick exit and "
         "prominent signage."),
        ("COP.3.c", "Commitment",
         "Sections 3.3 and 5.3 address statutory compliance, at least basic life support "
         "equipment for adult and paediatric patients, and scope-based additional equipment."),
        ("COP.3.d", "Commitment",
         "Sections 3.4 and 5.4 address valid driving licence and basic life support/CPR "
         "training; additional crew may be present depending on situation and scope."),
        ("COP.3.e", "Commitment",
         "Sections 3.5 and 5.5 address daily vehicle/equipment/medication checks, post-trip "
         "medication top-up, verification and documentation, and sealed-kit checks where "
         "applicable."),
        ("COP.3.f", "Commitment*",
         "Sections 3.6 and 5.6 address the proper communication system covering the whole "
         "patient-transport process, written call/response guidance and predefined timeframe "
         "based on patient needs."),
        ("COP.3.g", "Achievement",
         "Sections 3.7 and 5.7 address early treatment opportunities while in transit, "
         "clinical information exchange and responsibility of the medical professional in "
         "the ambulance for transit care decisions."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 13. Required Records/Evidence Checklist — bulleted list
    h(doc, 1, "13. Required Records/Evidence Checklist")

    h(doc, 2, "Ambulance access and statutory compliance")
    lb(doc,
       "Demarcated ambulance space with accessible patient-receiving area and quick exit.")
    lb(doc, "Prominent signage to ambulance entry and emergency department route.")
    lb(doc,
       "Applicable ambulance statutory documents, such as registration, fitness certificate, "
       "pollution control certificate and insurance.")
    lb(doc,
       "Documentation showing the ambulance level selected with reference to National "
       "Ambulance Code AIS-125.")

    h(doc, 2, "Equipment and personnel")
    lb(doc, "Basic life support equipment for both adult and paediatric patients.")
    lb(doc, "Scope-based additional monitoring and resuscitative equipment.")
    lb(doc, "Valid driving licence for the ambulance driver.")
    lb(doc, "Basic life support and CPR training records for ambulance personnel.")

    h(doc, 2, "Daily and post-trip checks")
    lb(doc,
       "Documented daily vehicle-system checks covering lights, siren, beacon lights, fuel "
       "and tyres.")
    lb(doc, "Documented medical-equipment checks.")
    lb(doc, "Daily emergency-medication availability and expiry checks.")
    lb(doc, "Post-trip medication top-up, verification and documentation.")
    lb(doc,
       "Sealed emergency medication-kit checks after each use where that system is used.")
    lb(doc, "Medication storage arrangements according to organisational policy.")

    h(doc, 2, "Communication and transport")
    lb(doc,
       "Connection between ambulance and organisation/control room by wireless or mobile "
       "phones.")
    lb(doc, "Written call-receipt, response and transport-organisation guidance.")
    lb(doc, "Communication coverage for the whole patient-transport process.")
    lb(doc, "Predefined timeframe for ambulance departure based on patient needs.")

    h(doc, 2, "In-transit care")
    lb(doc, "File created from first communication with the patient or attendant.")
    lb(doc,
       "Available clinical information such as age, weight, provisional diagnosis and "
       "ongoing treatment at the referring organisation.")
    lb(doc,
       "Information exchange between ambulance personnel and receiving medical professional "
       "when required.")
    lb(doc,
       "Attempts, wherever possible, by the receiving doctor to communicate with an external "
       "ambulance agency when applicable.")
    lb(doc,
       "Documentation identifying the medical professional in the ambulance responsible for "
       "care/intervention decisions during transit.")

    # 14. References
    h(doc, 1, "14. References")
    ln(doc, "National Ambulance Code AIS-125.")
    ln(doc,
       "Motor Vehicle Act and applicable statutory requirements for ambulance vehicles.")
    ln(doc, "Guidebook interpretation supplied for COP.3.a through COP.3.g.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied COP.3 objective elements and Guidebook "
      "interpretation into plain language. Mandatory requirements and their stated modal "
      "strength have been retained. Optional, preferable, illustrative and scope-dependent "
      "provisions have not been converted into mandatory requirements.")

    save_and_verify(doc, "HCO_COP_3_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# COP.4 — Community Emergencies, Epidemics and Other Disasters  (NO stop-work)
# Content: ChatGPT final draft (approved, COP%2004.pdf).
# Structure: Document control table, NO Stop-work, Governance Section 6 (table),
#            Quality monitoring Section 7 (table), Checklist Section 12, Refs Section 13.
# OEs: a★, b★, c, d (all Commitment). Prepared by: Medical Superintendent.
# 14 plan elements: 7 "must" + 7 "shall" in Section 3.2 (all List Bullet).
# Frequencies: "at least twice a year" + "at least one mock drill once in 12 months".
# ══════════════════════════════════════════════════════════════════════════════
def gen_cop4():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Community Emergencies, Epidemics and Other Disasters")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/COP/POL/04", "Medical Superintendent")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      "The organisation shall identify potential community emergencies, epidemics and other "
      "disasters and manage them through a documented plan. Resources shall be available "
      "according to threat perception and expected workload. The plan shall be tested at "
      "least twice a year, with at least one mock drill once in 12 months.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "This policy establishes how the organisation identifies and manages community "
      "emergencies, epidemics and other disasters that may cause a sudden rush of victims.")
    p(doc, "Those requirements are covered in the hospital's other policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      "This policy applies to the organisation's planning and preparedness for community "
      "emergencies, epidemics and other disasters relevant to its geographical location and "
      "the community served.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 Identification of potential emergencies")
    p(doc,
      "The organisation shall identify potential community emergencies, epidemics and other "
      "disasters likely to cause a sudden rush of victims.")
    p(doc,
      "The potential emergencies shall be identified based on geographical location and the "
      "community served by the organisation.")
    p(doc,
      "Examples include earthquake, floods, train accident, civil unrest outside the "
      "organisation's premises, major fire and outbreak of disease/epidemics. These are "
      "examples, not a fixed list.")
    p(doc,
      "For example, an organisation in an industrial town shall identify the industrial "
      "hazards that may occur in its vicinity.")

    h(doc, 2, "3.2 Documented disaster, community emergency and epidemic plan")
    p(doc, "The disaster, community emergency and epidemic plan must incorporate:")
    lb(doc, "alert code")
    lb(doc, "information and communication")
    lb(doc, "action cards for each of the staff")
    lb(doc,
       "availability and earmarking of resources including adequacy of medical supplies, "
       "equipment, materials and trained personnel")
    lb(doc, "establishment of command nucleus")
    lb(doc, "training and mock drills")
    lb(doc, "managing clinical activities during the event")
    p(doc, "The plan shall also include:")
    lb(doc, "activating and deactivating the plan")
    lb(doc, "receiving, identifying and triaging casualties")
    lb(doc, "defined areas for reception and treatment for casualties")
    lb(doc, "transportation aids")
    lb(doc, "communication aids")
    lb(doc, "managing visitors and controlling the movement of individuals and vehicles")
    lb(doc, "relocating/discharging admitted patients wherever needed")
    p(doc,
      "The plans shall conform to the relevant local laws and national plans on disaster "
      "management.")
    p(doc,
      "The emergency room could follow triage policy according to the National Disaster "
      "Management Authority (NDMA) guidelines. A good reference is NDMA guidelines.")

    h(doc, 2, "3.3 Medical supplies, equipment and materials")
    p(doc, "Resource availability shall be according to threat perception.")
    p(doc,
      "The number of resources, including medical consumables and equipment, shall be "
      "commensurate with the expected workload.")

    h(doc, 2, "3.4 Testing of the plan")
    p(doc,
      "Testing twice a year is only the minimum frequency, and this may be increased.")
    p(doc,
      "In case the organisation has different plans for different disasters, each of the "
      "plans shall be tested at least twice a year.")
    p(doc, "The plan can be tested using a table-top exercise, or a mock drill.")
    p(doc,
      "At a minimum, at least one mock drill shall be held once in 12 months.")
    p(doc,
      "This shall test all the components of the plan and not just awareness.")
    p(doc,
      "In the case of a mock drill, simulated patients, not real patients, shall be used.")
    p(doc,
      "After every table-top exercise/mock drill, the variations are identified, the reason "
      "for the same is analysed, debriefing conducted and where appropriate the necessary "
      "corrective and/or preventive actions are taken.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not leave potential community emergencies, epidemics or other disasters "
       "unidentified when they are relevant to the organisation's geographical location and "
       "the community served.")
    lb(doc,
       "Do not manage a community emergency, epidemic or other disaster without the "
       "documented plan incorporating the required alert code, information and communication, "
       "action cards, resources, command nucleus, training and mock drills, and management "
       "of clinical activities during the event.")
    lb(doc,
       "Do not use a documented disaster, community emergency and epidemic plan that omits "
       "activation and deactivation, casualty reception/identification/triage, defined "
       "reception and treatment areas, transportation aids, communication aids, visitor and "
       "movement management, and relocation/discharge of admitted patients wherever needed.")
    lb(doc,
       "Do not use the plan without conformity to relevant local laws and national plans on "
       "disaster management.")
    lb(doc,
       "Do not provide medical supplies, equipment and materials at levels that are not "
       "according to threat perception and commensurate with expected workload.")
    lb(doc, "Do not treat twice-yearly plan testing as optional.")
    lb(doc,
       "Where different plans exist for different disasters, do not leave any of those plans "
       "untested at least twice a year.")
    lb(doc,
       "Do not count testing that covers only awareness as sufficient; testing shall cover "
       "all components of the plan.")
    lb(doc,
       "Do not use real patients in a mock drill; simulated patients shall be used.")
    lb(doc,
       "Do not close a table-top exercise or mock drill without identifying variations, "
       "analysing the reason for the variations, conducting debriefing and, where "
       "appropriate, taking the necessary corrective and/or preventive actions.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Identify relevant emergencies")
    p(doc,
      "Identify potential community emergencies, epidemics and other disasters likely to "
      "cause a sudden rush of victims.")
    p(doc, "Base identification on geographical location and the community served.")
    p(doc,
      "Identify industrial hazards that may occur in the vicinity when relevant to an "
      "organisation in an industrial town.")

    h(doc, 2, "5.2 Maintain the documented plan")
    p(doc,
      "Maintain the alert code, information and communication arrangements, action cards "
      "for each staff member, resource availability and earmarking, command nucleus, "
      "training and mock drills, and arrangements for managing clinical activities during "
      "the event.")
    p(doc,
      "Include activation and deactivation, casualty reception/identification/triage, "
      "defined casualty reception and treatment areas, transportation aids, communication "
      "aids, visitor and movement management, and relocation/discharge of admitted patients "
      "wherever needed.")
    p(doc,
      "Ensure conformity with relevant local laws and national plans on disaster management.")
    p(doc,
      "The emergency room could follow triage policy according to NDMA guidelines.")

    h(doc, 2, "5.3 Maintain resources")
    p(doc, "Make resources available according to threat perception.")
    p(doc,
      "Ensure the number of medical consumables, equipment and other resources is "
      "commensurate with expected workload.")

    h(doc, 2, "5.4 Test and improve the plan")
    p(doc, "Test the plan at least twice a year.")
    p(doc,
      "Where different plans exist for different disasters, test each plan at least twice "
      "a year.")
    p(doc, "A table-top exercise or mock drill can be used for testing.")
    p(doc, "Hold at least one mock drill once in 12 months.")
    p(doc, "Test all components of the plan and not just awareness.")
    p(doc, "Use simulated patients, not real patients, for mock drills.")
    p(doc,
      "After every table-top exercise/mock drill, identify variations, analyse the reason, "
      "conduct debriefing and, where appropriate, take corrective and/or preventive actions.")

    # 6. Governance and responsibility — proper table (NO stop-work section above)
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        ("Organisation",
         "The organisation is responsible for identifying relevant community emergencies, "
         "epidemics and other disasters, maintaining the documented plan, making required "
         "resources available and ensuring the plan is tested."),
        ("All staff",
         "The plan includes an established command nucleus and action cards for each staff "
         "member, defining individual responsibilities during the event."),
        ("Emergency Room",
         "The emergency room could follow triage policy according to NDMA guidelines where "
         "the organisation chooses to adopt it."),
    ])

    # 7. Quality monitoring — proper table
    h(doc, 1, "7. Quality monitoring")
    mon_tbl(doc, [
        ("Plan testing frequency",
         "Completion of plan testing at least twice a year"),
        ("Disaster-specific plan testing",
         "Testing of each disaster-specific plan at least twice a year where different "
         "plans exist"),
        ("Mock drill frequency",
         "Completion of at least one mock drill once in 12 months"),
        ("Testing coverage",
         "Coverage of all plan components during testing"),
        ("Mock-drill patients",
         "Use of simulated patients rather than real patients in mock drills"),
        ("Post-exercise actions",
         "Identification of variations, analysis of reasons, debriefing and "
         "corrective/preventive action where appropriate after every exercise"),
    ])

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "Training and mock drills are incorporated into the documented disaster, community "
      "emergency and epidemic plan.")
    p(doc,
      f"I have read the Policy on Community Emergencies, Epidemics and Other Disasters of "
      f"{HN}. I will follow the processes described.")
    sig_tbl(doc)

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "The documented disaster, community emergency and epidemic plan, including action "
      "cards for each staff member, shall be available to the personnel involved in "
      "managing the event.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("NDMA", "National Disaster Management Authority"),
    ])

    # 11. Traceability table
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the "
      "Level column means documentation of the process is required.")
    tr = tbl(doc, 5, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("COP.4.a", "Commitment*",
         "Sections 3.1 and 5.1 address identification of potential community emergencies, "
         "epidemics and other disasters based on geographical location and the community "
         "served."),
        ("COP.4.b", "Commitment*",
         "Sections 3.2 and 5.2 address the documented disaster, community emergency and "
         "epidemic plan with all 14 required plan elements and conformity to relevant laws "
         "and national plans."),
        ("COP.4.c", "Commitment",
         "Sections 3.3 and 5.3 address availability of medical supplies, equipment and "
         "materials according to threat perception and commensurate with expected workload."),
        ("COP.4.d", "Commitment",
         "Sections 3.4 and 5.4 address testing at least twice a year, at least one mock "
         "drill once in 12 months, all-component coverage, simulated patients and four "
         "mandatory post-exercise steps."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist — bulleted list
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Emergency identification")
    lb(doc,
       "Documented list of potential community emergencies, epidemics and other disasters "
       "identified for the organisation's geographical location and community.")
    lb(doc,
       "Identification of relevant hazards in the vicinity, including industrial hazards "
       "where relevant.")

    h(doc, 2, "Documented disaster, community emergency and epidemic plan")
    lb(doc,
       "Current documented plan containing the alert code; information and communication; "
       "action cards for each staff member; availability and earmarking of medical supplies, "
       "equipment, materials and trained personnel; command nucleus; training and mock drills; "
       "and management of clinical activities during the event.")
    lb(doc,
       "Plan covering activation and deactivation; casualty reception, identification and "
       "triage; defined casualty reception and treatment areas; transportation aids; "
       "communication aids; visitor management and control of individual and vehicle movement; "
       "and relocation/discharge of admitted patients wherever needed.")
    lb(doc,
       "Plan showing conformity with relevant local laws and national plans on disaster "
       "management.")
    lb(doc,
       "NDMA guidelines retained as a reference; any emergency-room triage policy based on "
       "NDMA guidelines where the organisation chooses to follow it.")

    h(doc, 2, "Resources")
    lb(doc,
       "Arrangements showing availability and earmarking of medical supplies, equipment, "
       "materials and trained personnel according to threat perception and expected workload.")

    h(doc, 2, "Testing and exercises")
    lb(doc,
       "Testing records showing the plan was tested at least twice a year.")
    lb(doc,
       "Where different disaster plans exist, testing records for each plan showing testing "
       "at least twice a year.")
    lb(doc,
       "Record of at least one mock drill once in 12 months.")
    lb(doc,
       "Exercise records showing all components of the plan were tested, not just awareness.")
    lb(doc,
       "Mock-drill records showing simulated patients, not real patients, were used.")
    lb(doc,
       "After-exercise records showing variations identified, reasons analysed, debriefing "
       "conducted and corrective and/or preventive actions taken where appropriate.")

    # 13. References
    h(doc, 1, "13. References")
    ln(doc, "National Disaster Management Authority (NDMA) guidelines.")
    ln(doc, "Relevant local laws and national plans on disaster management.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied COP.4 objective elements and Guidebook "
      "interpretation into plain language. Mandatory requirements and their stated modal "
      "strength have been retained. Illustrative examples, optional approaches and references "
      "have not been converted into mandatory requirements.")

    save_and_verify(doc, "HCO_COP_4_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# COP.5 — Cardio-pulmonary Resuscitation Services   (STOP-WORK YES)
# Content: ChatGPT final draft (approved, COP%2005.pdf).
# Structure: Stop-work Section 6, Governance Section 7, Quality monitoring Section 8.
# All OEs: Commitment | No stars | No COREs
# Exact frequency: "at least once a quarter" (3.5/5.5)
# 9 coverage areas (3.3/5.3) | 5 record items (3.4/5.4) | 5 analysis foci (3.5/5.5)
# 4 committee roles (3.5/5.5)
# ══════════════════════════════════════════════════════════════════════════════
def gen_cop5():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Cardio-pulmonary Resuscitation Services")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/COP/POL/05", "Medical Superintendent")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      "Cardio-pulmonary resuscitation services shall be available and provided to patients "
      f"at all times. {HN} shall maintain a documented CPR procedure, appropriate equipment "
      "and medications, trained team roles, event recording, post-event analysis and corrective "
      "and preventive measures.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "This policy establishes requirements for providing cardio-pulmonary resuscitation "
      "services, maintaining CPR readiness, recording CPR events and mock drills, analysing "
      "outcomes, and implementing corrective and preventive measures. Those requirements are "
      "covered in the hospital's other policies.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies across all areas of {HN} where cardio-pulmonary resuscitation "
      "may be required, including the patient care areas identified in this policy.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 CPR procedure and immediate response")
    p(doc,
      "The organisation shall document the procedure for cardio-pulmonary resuscitation (CPR) "
      "for adults across all areas in the organisation. This shall be in consonance with "
      "accepted practices.")
    p(doc,
      "Where appropriate, it shall also address obstetric, paediatric and neonatal patients.")
    p(doc,
      "The organisation shall ensure that medical equipment for resuscitation and medications "
      "for basic and advanced life support are provided in standardised manner.")
    p(doc,
      "Basic life support shall be initiated as soon as a condition requiring CPR is identified. "
      "This shall be implemented in all areas of the organisation.")
    p(doc,
      "The protocols could be displayed prominently in all critical areas such as emergency, "
      "ICU, OT and all crash carts.")

    h(doc, 2, "3.2 CPR team roles and responsibilities")
    p(doc,
      "CPR team members shall have a clear understanding of their roles and responsibilities "
      "during resuscitation and shall comply with their assigned roles and responsibilities "
      "to effectively function as a team.")

    h(doc, 2, "3.3 Equipment and medications")
    p(doc,
      "At a minimum, emergency medications and equipment for intubation based on the needs "
      "of the patients served shall be available in patient care areas including the blood "
      "centre, radiology, day care, dialysis, chemo ward, OPD, rehabilitation services areas, "
      "endoscopy, and in areas where any invasive procedure is performed.")
    p(doc,
      "Other equipment like defibrillator shall be easily accessible to ensure that there is "
      "no delay in cardio-pulmonary resuscitation.")
    p(doc,
      "It is preferable that the minimum emergency medication is standardised across the "
      "organisation.")

    h(doc, 2, "3.4 Recording CPR events and mock drills")
    p(doc,
      "In the actual event of cardio-pulmonary resuscitation, or a mock drill of the same, "
      "all the activities along with the personnel attended shall be recorded.")
    p(doc,
      "At the minimum, it will include timeliness of response, availability of human resources, "
      "equipment, drugs, and barriers if any.")
    p(doc,
      "The recording could be done using the pre-defined procedural checklist and by monitoring "
      "whether the prescribed activity has been performed properly and in the right sequence.")
    p(doc,
      "It is a good practice to debrief team members regarding the necessary immediate "
      "corrective and preventive action.")

    h(doc, 2, "3.5 Post-event analysis")
    p(doc,
      "The frequency of the committee meeting shall be at least once a quarter.")
    p(doc,
      "The analysis shall focus on the initiation of CPR, time of arrival of the team, "
      "availability of required resources, recording of the sequence of events during CPR "
      "(including technique) and the overall coordination.")
    p(doc,
      "The organisation shall monitor outcome of CPR and identify areas for improvement.")
    p(doc,
      "The multidisciplinary committee shall be independent and include at least one "
      "physician/cardiologist, one anaesthesiologist, one member from the code blue team "
      "and one nurse.")
    p(doc,
      "The analysis shall be completed within a defined time frame.")

    h(doc, 2, "3.6 Corrective and preventive measures")
    p(doc,
      "Corrective and preventive measures shall be completed within a defined time frame.")
    p(doc,
      "The findings of the post-event analysis shall be communicated to the personnel who "
      "participated in the CPR.")
    p(doc,
      "Any lapses shall be discussed, with the view to improve the outcomes in future.")
    p(doc,
      "During subsequent resuscitations, it is preferable that implementation of these actions "
      "is noted and training be modified, if necessary.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not start CPR without initiating basic life support as soon as a condition "
       "requiring CPR is identified.")
    lb(doc,
       "Do not start a planned resuscitation response without a named CPR team with clear "
       "roles and without the minimum emergency medications and equipment available at the "
       "location.")
    lb(doc,
       "Do not use a CPR process without the documented CPR procedure and standardised "
       "resuscitation equipment and medications required by this policy.")
    lb(doc,
       "Do not omit emergency medications and intubation equipment from the specified "
       "patient care areas.")
    lb(doc,
       "Do not conduct CPR where the defibrillator cannot be accessed without delay.")
    lb(doc,
       "Do not omit recording of an actual CPR event or mock drill, including timeliness "
       "of response, availability of human resources, equipment, drugs, and barriers if any.")
    lb(doc,
       "Do not complete a post-event analysis without the multidisciplinary committee meeting "
       "at least once a quarter and analysing the specified CPR performance areas.")
    lb(doc,
       "Do not omit the independent multidisciplinary committee composition specified in "
       "this policy.")
    lb(doc,
       "Do not leave corrective and preventive measures incomplete beyond the defined time "
       "frame.")
    lb(doc,
       "Do not withhold post-event analysis findings from personnel who participated in "
       "the CPR.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 CPR procedure and readiness")
    lb(doc,
       "Maintain a documented adult CPR procedure across all areas in consonance with "
       "accepted practices.")
    lb(doc, "Where appropriate, address obstetric, paediatric and neonatal patients.")
    lb(doc,
       "Provide resuscitation equipment and basic and advanced life-support medications in "
       "a standardised manner.")
    lb(doc,
       "Initiate basic life support as soon as a condition requiring CPR is identified in "
       "all areas.")
    lb(doc,
       "Protocols could be displayed prominently in critical areas such as emergency, ICU, "
       "OT and crash carts.")

    h(doc, 2, "5.2 CPR team")
    lb(doc,
       "Ensure CPR team members understand and comply with their assigned roles and "
       "responsibilities.")

    h(doc, 2, "5.3 Equipment and medication coverage")
    lb(doc,
       "Keep at least the required emergency medications and intubation equipment based on "
       "patient needs in the blood centre, radiology, day care, dialysis, chemo ward, OPD, "
       "rehabilitation services areas, endoscopy, and areas where an invasive procedure is "
       "performed.")
    lb(doc, "Keep the defibrillator easily accessible so there is no delay in CPR.")
    lb(doc, "Standardisation of the minimum emergency medication is preferable.")

    h(doc, 2, "5.4 Event recording")
    lb(doc, "Record all activities and personnel involved in actual CPR events and mock drills.")
    lb(doc,
       "Record timeliness of response, availability of human resources, equipment, drugs, "
       "and barriers if any.")
    lb(doc, "A predefined procedural checklist could be used.")
    lb(doc,
       "Debriefing team members regarding immediate corrective and preventive action is "
       "good practice.")

    h(doc, 2, "5.5 Post-event analysis")
    lb(doc, "Have the multidisciplinary committee meet at least once a quarter.")
    lb(doc,
       "Analyse initiation of CPR, time of arrival of the team, availability of required "
       "resources, recording of the sequence of events during CPR including technique, and "
       "overall coordination.")
    lb(doc, "Monitor CPR outcomes and identify areas for improvement.")
    lb(doc,
       "Maintain an independent multidisciplinary committee with at least one "
       "physician/cardiologist, one anaesthesiologist, one member from the code blue team "
       "and one nurse.")
    lb(doc, "Complete the analysis within a defined time frame.")

    h(doc, 2, "5.6 Corrective and preventive measures")
    lb(doc, "Complete corrective and preventive measures within a defined time frame.")
    lb(doc,
       "Communicate post-event analysis findings to personnel who participated in the CPR.")
    lb(doc, "Discuss lapses to improve outcomes in future.")
    lb(doc,
       "Preferably note implementation of actions during subsequent resuscitations and "
       "modify training if necessary.")

    # 6. Stop-work authority
    h(doc, 1, "6. Stop-work authority")
    p(doc,
      "Do not start a planned resuscitation response (or mock drill counted as CPR "
      "competence evidence) without a named CPR team with clear roles and without the "
      "minimum emergency medications and equipment available at the location. Stop-work "
      "does not block an unexpected cardiac arrest already in progress — start CPR "
      "with available staff and escalate for equipment/team immediately. The person "
      "responsible tells the CPR Committee chair or Emergency In-Charge the same shift. "
      "Refusing to run a hollow CPR response is not a disciplinary matter.")
    p(doc,
      "The post-event analysis committee is a separate governance and quality loop, not "
      "part of the stop-work trigger. Stop-work concerns CPR readiness at the moment of "
      "need, not analysis-timeline compliance.")

    # 7. Governance and responsibility — proper table
    h(doc, 1, "7. Governance and responsibility")
    gov_tbl(doc, [
        ("CPR team members",
         "CPR team members are responsible for understanding and complying with their "
         "assigned roles and responsibilities during resuscitation."),
        ("Multidisciplinary CPR committee",
         "Responsible for post-event analysis, CPR outcome monitoring and identification "
         "of areas for improvement. The committee shall be independent and include at least "
         "one physician/cardiologist, one anaesthesiologist, one member from the code blue "
         "team and one nurse."),
    ])

    # 8. Quality monitoring — proper table
    h(doc, 1, "8. Quality monitoring")
    mon_tbl(doc, [
        ("CPR event recording",
         "CPR events and mock drills, including the required minimum record content"),
        ("Committee meetings",
         "Committee meetings at least once a quarter"),
        ("Analysis coverage",
         "Analysis of initiation of CPR, time of arrival of the team, availability of "
         "required resources, recording of the sequence of events during CPR including "
         "technique, and overall coordination"),
        ("CPR outcomes",
         "CPR outcomes and areas for improvement"),
        ("CAPA completion",
         "Completion of corrective and preventive measures within the defined time frame"),
        ("Post-event communication",
         "Communication of post-event findings to CPR participants"),
    ])

    # 9. Training and staff acknowledgement
    h(doc, 1, "9. Training and staff acknowledgement")
    p(doc,
      "Training and mock drills form part of the documented CPR arrangements. CPR team "
      "members shall understand their assigned roles and responsibilities.")
    p(doc,
      f"I have read the Policy on Cardio-pulmonary Resuscitation Services of {HN}. "
      "I will follow the processes described.")
    sig_tbl(doc)

    # 10. Distribution
    h(doc, 1, "10. Distribution")
    p(doc,
      "The policy shall be available to personnel involved in CPR services, including CPR "
      "team members and personnel working in patient care areas.")

    # 11. Abbreviations
    h(doc, 1, "11. Abbreviations")
    abbrev_tbl(doc, [
        ("BLS",  "Basic Life Support"),
        ("ALS",  "Advanced Life Support"),
        ("CPR",  "Cardio-pulmonary Resuscitation"),
        ("CAPA", "Corrective and Preventive Action"),
        ("ICU",  "Intensive Care Unit"),
        ("OT",   "Operation Theatre"),
        ("OPD",  "Outpatient Department"),
    ])

    # 12. Traceability table
    h(doc, 1, "12. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the "
      "Level column means documentation of the process is required.")
    tr = tbl(doc, 7, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("COP.5.a", "Commitment",
         "Sections 3.1 and 5.1 address the documented CPR procedure for adults across all "
         "areas, standardised resuscitation equipment and medications, and immediate BLS "
         "initiation."),
        ("COP.5.b", "Commitment",
         "Sections 3.2 and 5.2 address CPR team compliance with assigned roles and "
         "responsibilities."),
        ("COP.5.c", "Commitment",
         "Sections 3.3 and 5.3 address emergency medications and intubation equipment in "
         "the nine specified areas and areas where invasive procedures are performed, and "
         "defibrillator accessibility."),
        ("COP.5.d", "Commitment",
         "Sections 3.4 and 5.4 address recording of actual CPR events and mock drills, "
         "including the five minimum content items."),
        ("COP.5.e", "Commitment",
         "Sections 3.5 and 5.5 address post-event analysis: quarterly committee meetings, "
         "five analysis areas, CPR outcome monitoring, independent committee with minimum "
         "composition and analysis within a defined time frame."),
        ("COP.5.f", "Commitment",
         "Sections 3.6 and 5.6 address CAPA within a defined time frame, findings "
         "communicated to CPR participants, and lapses discussed for future improvement."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 13. Required Records/Evidence Checklist
    h(doc, 1, "13. Required Records/Evidence Checklist")

    h(doc, 2, "CPR procedure and readiness")
    lb(doc,
       "Documented adult CPR procedure across all areas in consonance with accepted practices.")
    lb(doc,
       "Written provisions, where appropriate, for obstetric, paediatric and neonatal CPR.")
    lb(doc,
       "Standardised resuscitation equipment and BLS/ALS medications across the organisation.")
    lb(doc,
       "Evidence that BLS is initiated immediately on identification of a CPR-requiring "
       "condition in all areas.")

    h(doc, 2, "Equipment and medication coverage")
    lb(doc,
       "Emergency medications and intubation equipment available in the blood centre, "
       "radiology, day care, dialysis, chemo ward, OPD, rehabilitation services areas, "
       "endoscopy, and all areas where invasive procedures are performed.")
    lb(doc, "Defibrillator accessible without delay in CPR locations.")

    h(doc, 2, "CPR event and mock drill recording")
    lb(doc, "Records of actual CPR events and mock drills including personnel attended.")
    lb(doc,
       "Minimum record content: timeliness of response, availability of human resources, "
       "equipment, drugs, and barriers if any.")

    h(doc, 2, "Post-event analysis")
    lb(doc,
       "Evidence that the multidisciplinary committee meets at least once a quarter.")
    lb(doc,
       "Analysis records covering: initiation of CPR, time of arrival of the team, "
       "availability of required resources, recording of event sequence including technique, "
       "and overall coordination.")
    lb(doc, "CPR outcome records and identified areas for improvement.")
    lb(doc,
       "Evidence of independent multidisciplinary committee with at least one "
       "physician/cardiologist, one anaesthesiologist, one member from the code blue team "
       "and one nurse.")
    lb(doc, "Evidence of analysis completed within the defined time frame.")

    h(doc, 2, "CAPA and communication")
    lb(doc, "CAPA records showing measures completed within the defined time frame.")
    lb(doc,
       "Evidence that post-event analysis findings were communicated to CPR participants.")
    lb(doc, "Records of lapses discussed and actions taken for future improvement.")

    # 14. References
    h(doc, 1, "14. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. COP.5.")
    ln(doc, "Guidebook interpretation supplied for COP.5.a through COP.5.f.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied COP.5 objective elements and Guidebook "
      "interpretation into plain language. Mandatory requirements and their stated modal "
      "strength have been retained. Illustrative examples, optional approaches and references "
      "have not been converted into mandatory requirements.")

    save_and_verify(doc, "HCO_COP_5_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
# COP.6 — Nursing Care   (NO stop-work)
# Content: raw source dump cop_raw_dump_5-8.txt (no ChatGPT PDF — rebuilt from source)
# Structure: Governance Section 6, Quality monitoring Section 7 (no stop-work shift)
# Stars: a★, d★ | Achievement: c | All other OEs: Commitment
# Exact frequency: "reviewed annually at the minimum" (3.1/5.1)
# Five nursing care plan components (3.4/5.4): assessment, plan of care,
#   implementation of care, evaluation, modification of plan of care as may be required
# ══════════════════════════════════════════════════════════════════════════════
def gen_cop6():
    doc = Document()

    # Title
    h(doc, 0, "Policy on Nursing Care")
    p(doc, HN)

    # Document control
    h(doc, 1, "Document control")
    doc_ctrl(doc, "HCO/COP/POL/06", "Nursing Superintendent")
    p(doc, "A blank marked ________ must be completed before issue.")

    # Statement of intent
    h(doc, 1, "Statement of intent")
    p(doc,
      f"{HN} ensures that nursing care is provided to patients in consonance with clinical "
      "protocols. Nursing care follows written guidance, is assigned based on clinical need and "
      "competence, is documented in an individualised nursing care plan, and is supported by "
      "appropriate equipment. Nurses are empowered to make patient care decisions within their "
      "defined scope of practice.")

    # 1. Purpose
    h(doc, 1, "1. Purpose")
    p(doc,
      "This policy establishes requirements for providing nursing care through written guidance "
      "and clinical practice guidelines, assigning patient care based on clinical requirements "
      "and nursing competence, implementing acuity-based staffing, maintaining individualised "
      "nursing care plans, providing appropriate nursing equipment, and defining the scope of "
      "nursing practice decisions.")

    # 2. Scope
    h(doc, 1, "2. Scope")
    p(doc,
      f"This policy applies to all nursing staff providing patient care across all wards, "
      f"departments and care settings of {HN}.")

    # 3. Policy standards
    h(doc, 1, "3. Policy standards")

    h(doc, 2, "3.1 Written guidance and clinical practice guidelines")
    p(doc,
      "Nursing care is provided in accordance with written guidance. The written guidance could "
      "be in the form of a nursing manual or standard operating procedures incorporating various "
      "basic nursing practices and procedures.")
    p(doc,
      "Care of patients in specific clinical situations shall be guided by nursing clinical "
      "practice guidelines based on best clinical practices.")
    p(doc,
      "Nursing clinical care guidelines and pathways shall be reviewed annually at the minimum, "
      "and revised as appropriate.")
    p(doc,
      "Examples of nursing clinical practice guidelines include prevention of fall, prevention "
      "of development of pressure ulcers in an in-patient, and deep venous thrombosis risk "
      "assessment and prevention. These examples are illustrative; the organisation selects "
      "guidelines appropriate to its clinical scope.")

    h(doc, 2, "3.2 Assignment of patient care")
    p(doc,
      "Assignment of patient care shall be based on the patient's clinical requirements and "
      "the competence of the nursing staff, and shall align with the guidelines laid down by "
      "regulatory and professional bodies.")

    h(doc, 2, "3.3 Acuity-based staffing")
    p(doc,
      "The organisation implements acuity-based staffing — matching both the number and "
      "competence of nursing personnel to patient acuity — to improve patient outcomes.")
    p(doc,
      "Patient outcomes linked to acuity-based staffing may include incidence of pressure "
      "sores, falls, medication administration errors, and ventilator-associated pneumonia. "
      "The organisation selects relevant outcome indicators for its own scope of services.")

    h(doc, 2, "3.4 Nursing care plan")
    p(doc,
      "Care shall be provided as per the nursing care plan, which shall be individualised as "
      "per the clinical needs of each patient. Where a patient care plan has been developed, "
      "the nursing care plan shall be aligned with it. Uniformity and continuity of care shall "
      "be practised.")
    p(doc,
      "Components of the nursing care plan include: Assessment; Plan of care; Implementation "
      "of care; Evaluation; and Modification of plan of care as may be required.")
    p(doc,
      "Documentation includes all nursing-related care and not just monitoring of vitals and "
      "documentation of medication administration. Nursing progress shall be documented in a "
      "timely manner for each patient.")

    h(doc, 2, "3.5 Nursing equipment")
    p(doc,
      "There shall be an adequate number of basic nursing equipment and gadgets necessary for "
      "functioning in each designated area. Examples include nebuliser machines, glucometers, "
      "sphygmomanometers, thermometers and weighing scales — the organisation determines the "
      "appropriate equipment for its scope and patient population.")
    p(doc,
      "The equipment shall be appropriate for the area. For example, BP cuffs in a paediatric "
      "area shall be of appropriate size for the patient population served.")

    h(doc, 2, "3.6 Scope of nursing practice decisions")
    p(doc,
      "The organisation shall define the patient care decisions that come under the scope of "
      "nursing practice.")
    p(doc,
      "Nurses shall be aware of their defined scope and shall be able to make appropriate "
      "nursing-related decisions in a timely manner.")

    # 4. Non-negotiable rules
    h(doc, 1, "4. Non-negotiable rules")
    lb(doc,
       "Do not provide nursing care for specific clinical situations without nursing clinical "
       "practice guidelines based on best clinical practices.")
    lb(doc,
       "Do not let nursing clinical care guidelines and pathways go more than one year without "
       "review.")
    lb(doc,
       "Do not assign patient care without considering the patient's clinical requirements and "
       "the competence of the nursing staff.")
    lb(doc,
       "Do not omit the nursing care plan for any patient where one is required; the plan shall "
       "be individualised as per the patient's clinical needs.")
    lb(doc,
       "Do not omit any of the five nursing care plan components: Assessment; Plan of care; "
       "Implementation of care; Evaluation; and Modification of plan of care as may be required.")
    lb(doc,
       "Do not leave a ward or department without an adequate number of nursing equipment "
       "appropriate for the area and patient population.")
    lb(doc,
       "Do not leave the scope of nursing practice decisions undefined or leave nurses unaware "
       "of their defined scope.")

    # 5. What we do
    h(doc, 1, "5. What we do")

    h(doc, 2, "5.1 Written guidance and clinical practice guidelines")
    lb(doc,
       "Provide written guidance for nursing care — this could be a nursing manual or SOPs "
       "covering basic nursing practices and procedures.")
    lb(doc,
       "Guide care of patients in specific clinical situations through nursing clinical practice "
       "guidelines based on best clinical practices.")
    lb(doc,
       "Review nursing clinical care guidelines and pathways annually at the minimum and revise "
       "as appropriate.")
    lb(doc,
       "Examples of applicable guidelines include fall prevention, pressure ulcer prevention "
       "and DVT risk assessment — the organisation selects relevant guidelines for its scope.")

    h(doc, 2, "5.2 Assignment of patient care")
    lb(doc,
       "Assign patient care based on the patient's clinical requirements and the competence of "
       "the nursing staff, aligned with regulatory and professional body guidelines.")

    h(doc, 2, "5.3 Acuity-based staffing")
    lb(doc,
       "Implement acuity-based staffing — match the number and competence of nursing personnel "
       "to patient acuity — to improve patient outcomes.")
    lb(doc,
       "Monitor patient outcomes linked to acuity-based staffing and use results for "
       "improvement.")

    h(doc, 2, "5.4 Nursing care plan")
    lb(doc,
       "Provide nursing care as per an individualised nursing care plan based on each patient's "
       "clinical needs; where a patient care plan exists, align the nursing care plan with it.")
    lb(doc, "Practise uniformity and continuity of care.")
    lb(doc,
       "Ensure every nursing care plan covers all five components: Assessment; Plan of care; "
       "Implementation of care; Evaluation; and Modification of plan of care as may be required.")
    lb(doc,
       "Document all nursing-related care — not just monitoring of vitals and medication "
       "administration — in a timely manner for each patient.")

    h(doc, 2, "5.5 Nursing equipment")
    lb(doc,
       "Maintain an adequate number of basic nursing equipment appropriate for each ward and "
       "department and the patient population it serves.")
    lb(doc,
       "Ensure equipment is appropriate for the area — e.g., appropriate-size BP cuffs in "
       "paediatric areas.")

    h(doc, 2, "5.6 Scope of nursing practice decisions")
    lb(doc,
       "Define the patient care decisions that come under the scope of nursing practice and "
       "ensure all nurses are aware of their defined scope.")
    lb(doc,
       "Ensure nurses are able to make appropriate nursing-related decisions in a timely manner.")

    # 6. Governance and responsibility — proper table (no stop-work, so Section 6)
    h(doc, 1, "6. Governance and responsibility")
    gov_tbl(doc, [
        ("Nursing Superintendent",
         "Owns day-to-day implementation of nursing care processes; ensures nursing clinical "
         "practice guidelines are reviewed annually at the minimum; oversees individualised "
         "nursing care plan documentation and compliance."),
        ("Medical Superintendent",
         "Accountable that this policy is followed and appropriately resourced."),
        ("Quality Coordinator",
         "Supports audit of nursing care documentation, CPG review records and nursing "
         "equipment adequacy."),
    ])

    # 7. Quality monitoring — proper table
    h(doc, 1, "7. Quality monitoring")
    mon_tbl(doc, [
        ("Written guidance and CPG review",
         "Nursing written guidance in place; nursing CPGs/pathways reviewed annually at the "
         "minimum and revised as appropriate"),
        ("Nursing care plans",
         "Individualised nursing care plans present and documented, covering all five "
         "components: assessment, plan of care, implementation of care, evaluation, and "
         "modification of plan of care as may be required"),
        ("Nursing progress documentation",
         "Nursing progress documented in a timely manner for each patient, covering all "
         "nursing-related care and not only vitals and medication administration"),
        ("Care assignment",
         "Patient care assignment based on clinical requirements and nursing staff competence, "
         "aligned with regulatory and professional body guidelines"),
        ("Nursing equipment",
         "Adequate and area-appropriate nursing equipment present in all wards and departments"),
        ("Scope of practice",
         "Defined scope of nursing practice decisions; nurses aware and making timely decisions"),
    ])

    # 8. Training and staff acknowledgement
    h(doc, 1, "8. Training and staff acknowledgement")
    p(doc,
      "Nursing staff shall have access to ongoing training on nursing care processes, clinical "
      "practice guidelines and care plan documentation.")
    p(doc,
      f"I have read the Policy on Nursing Care of {HN}. I will follow the processes described.")
    sig_tbl(doc)

    # 9. Distribution
    h(doc, 1, "9. Distribution")
    p(doc,
      "This policy shall be available to all nursing staff, the Nursing Superintendent, "
      "ward in-charges and the Quality Coordinator.")

    # 10. Abbreviations
    h(doc, 1, "10. Abbreviations")
    abbrev_tbl(doc, [
        ("CPG",  "Clinical Practice Guideline"),
        ("DVT",  "Deep Venous Thrombosis"),
        ("SOP",  "Standard Operating Procedure"),
        ("VAP",  "Ventilator-Associated Pneumonia"),
    ])

    # 11. Traceability table
    h(doc, 1, "11. Traceability table")
    p(doc,
      "This table is an index. It is not how the policy is organised. An asterisk in the "
      "Level column means documentation of the process is required.")
    tr = tbl(doc, 7, 3)
    for ci, hdr in enumerate(("Objective Element", "Level", "Traceability to this policy")):
        tr.cell(0, ci).text = hdr
    trace_rows = [
        ("COP.6.a", "Commitment*",
         "Sections 3.1 and 5.1 address nursing care in accordance with written guidance, "
         "nursing CPGs based on best clinical practices for specific clinical situations, and "
         "annual review of nursing CPGs/pathways at the minimum."),
        ("COP.6.b", "Commitment",
         "Sections 3.2 and 5.2 address assignment of patient care based on clinical "
         "requirements and nursing staff competence, aligned with regulatory and professional "
         "body guidelines."),
        ("COP.6.c", "Achievement",
         "Sections 3.3 and 5.3 address implementation of acuity-based staffing — matching "
         "numbers and competence to patient acuity — to improve patient outcomes."),
        ("COP.6.d", "Commitment*",
         "Sections 3.4 and 5.4 address the individualised nursing care plan aligned with the "
         "overall patient care plan where one exists; uniformity and continuity of care; all "
         "five nursing care plan components; and timely documentation of all nursing-related "
         "care."),
        ("COP.6.e", "Commitment",
         "Sections 3.5 and 5.5 address adequate nursing equipment in adequate numbers, "
         "appropriate for each area and patient population."),
        ("COP.6.f", "Commitment",
         "Sections 3.6 and 5.6 address the defined scope of nursing practice decisions and "
         "nurses' ability to make timely nursing decisions within that scope."),
    ]
    for ri, (oe, lvl, txt) in enumerate(trace_rows, 1):
        tr.cell(ri, 0).text = oe
        tr.cell(ri, 1).text = lvl
        tr.cell(ri, 2).text = txt

    # 12. Required Records/Evidence Checklist
    h(doc, 1, "12. Required Records/Evidence Checklist")

    h(doc, 2, "Written guidance and CPG review")
    lb(doc,
       "Nursing written guidance (nursing manual, SOPs, or clinical practice guidelines) "
       "covering basic nursing practices and procedures.")
    lb(doc,
       "Nursing clinical practice guidelines for specific clinical situations, based on best "
       "clinical practices.")
    lb(doc,
       "Evidence of annual review and revision of nursing CPGs and pathways at the minimum.")

    h(doc, 2, "Nursing care plan and documentation")
    lb(doc,
       "Individualised nursing care plans covering all five components: assessment, plan of "
       "care, implementation of care, evaluation, and modification of plan of care as may be "
       "required.")
    lb(doc,
       "Evidence that the nursing care plan is aligned with the overall patient care plan "
       "where one exists.")
    lb(doc,
       "Nursing progress records documenting all nursing-related care in a timely manner, "
       "not limited to vitals and medication administration.")

    h(doc, 2, "Care assignment and staffing")
    lb(doc,
       "Evidence that patient care assignment is based on clinical requirements and nursing "
       "staff competence, aligned with regulatory and professional body guidelines.")
    lb(doc,
       "Acuity-based staffing arrangements — numbers and competence matched to patient acuity "
       "— and patient outcome monitoring.")

    h(doc, 2, "Nursing equipment")
    lb(doc,
       "Adequate number of basic nursing equipment present in each ward and department, "
       "appropriate for the area and patient population served.")

    h(doc, 2, "Scope of nursing practice")
    lb(doc,
       "Written definition of patient care decisions within the scope of nursing practice.")
    lb(doc,
       "Evidence that nurses are aware of their defined scope and make timely nursing decisions.")

    # 13. References
    h(doc, 1, "13. References")
    ln(doc,
       "National Accreditation Board for Hospitals and Healthcare Providers. NABH "
       "Accreditation Standards for Hospitals, 6th Edition. COP.6.")
    ln(doc, "Guidebook interpretation supplied for COP.6.a through COP.6.f.")

    # Disclaimer
    h(doc, 1, "Disclaimer")
    p(doc,
      "This policy reorganises the supplied COP.6 objective elements and Guidebook "
      "interpretation into plain language. Mandatory requirements and their stated modal "
      "strength have been retained. Illustrative examples, optional approaches and references "
      "have not been converted into mandatory requirements.")

    save_and_verify(doc, "HCO_COP_6_v2_REWRITE_DRAFT.docx")


# ══════════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    gen_cop1()
    print("\nCOP.1 draft generated.")
    gen_cop2()
    print("\nCOP.2 draft generated.")
    gen_cop3()
    print("\nCOP.3 draft generated.")
    gen_cop4()
    print("\nCOP.4 draft generated.")
    gen_cop5()
    print("\nCOP.5 draft generated.")
    gen_cop6()
    print("\nCOP.6 draft generated.")
