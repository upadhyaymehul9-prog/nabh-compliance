# -*- coding: utf-8 -*-
"""Shared builder for SHCO SOP + Record master .docx files.

Introduced with the FMS chapter (Oct 2026). The AAC/COP/HRM/ROM chapters
were each hand-built with one-off python-docx scripts -- no reusable module
existed. This factors out the structure every one of those files already
shared (verified against SOP_COP.13.*.docx and its Records/*.docx on
2026-10-10: same heading set, same "Table Grid" style, same yellow
FFF2CC worked-example-row shading, same page/margin defaults), so every
later chapter (PSQ, MOM, IPC, PRE, HRM additions, etc.) builds from one
place instead of re-deriving the template by eye each time.

Nothing here invents new structure. It only encodes what the already-
approved files already do, so this module is itself verifiable against
them -- see policies/build/verify_sop_record_template.py.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml.ns import qn
from docx.oxml.shared import OxmlElement
from docx.shared import Pt

WORKED_EXAMPLE_FILL = "FFF2CC"

# Source strings may embed a real, verified URL as a Markdown-style link:
#   "...(2016). [National Building Code of India, 2016](https://example.gov.in/...)."
# _render_source_text() below turns the bracketed span into an actual
# clickable w:hyperlink run (same OOXML AAC/COP/ROM/HRM already use) and
# leaves the rest of the string as plain text. A source with no [..](..)
# renders as plain text, same as before -- this is additive, not a format
# change to every existing call site.
_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^\s)]+)\)")


def add_hyperlink(paragraph, text: str, url: str):
    """Append a real, clickable external hyperlink run to `paragraph`.

    Mirrors the w:hyperlink + externally-related r:id structure already
    present in every AAC/COP/ROM/HRM source citation (verified by
    inspecting their word/_rels/document.xml.rels) -- this is not a new
    format, just the first time this shared module does it.
    """
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)

    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)

    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0563C1")
    rPr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rPr.append(u)
    new_run.append(rPr)

    t = OxmlElement("w:t")
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)

    paragraph._p.append(hyperlink)
    return hyperlink


def _render_source_text(paragraph, raw_text: str) -> None:
    """Write raw_text into paragraph, converting any [label](url) span into
    a real clickable hyperlink run and everything else into plain text."""
    pos = 0
    for m in _LINK_RE.finditer(raw_text):
        before = raw_text[pos:m.start()]
        if before:
            paragraph.add_run(before)
        add_hyperlink(paragraph, m.group(1), m.group(2))
        pos = m.end()
    tail = raw_text[pos:]
    if tail or pos == 0:
        paragraph.add_run(tail)


def _shade_row(row, fill: str = WORKED_EXAMPLE_FILL) -> None:
    for cell in row.cells:
        tcPr = cell._tc.get_or_add_tcPr()
        shd = tcPr.makeelement(qn("w:shd"), {
            qn("w:val"): "clear",
            qn("w:color"): "auto",
            qn("w:fill"): fill,
        })
        tcPr.append(shd)


def _add_single_cell_table(doc: Document, text: str) -> None:
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    t.rows[0].cells[0].text = text
    doc.add_paragraph("")


# ---------------------------------------------------------------- SOP -----

@dataclass
class ProcedureBlock:
    heading: str          # e.g. "4.1 Patients in pain are effectively managed (COP.13.a)"
    why_it_matters: str
    steps: list[str]      # already-numbered strings, "1. ...", "2. ..."
    technical_sources: list[str] | None = None  # bare APA-style lines, bulleted


@dataclass
class SOPSpec:
    sop_no: str                 # "SOP-FMS.1"
    title: str                  # "Planned Facilities, Utilities and Environment-Friendly Measures"
    standard_code_range: str    # "FMS.1.a-f"
    what_is_this_for: str
    worked_example: str
    why_nabh_asks: str
    purpose: str
    scope: str
    responsibilities: list[tuple[str, str]]   # (role, text)
    blocks: list[ProcedureBlock]
    records_note: str
    related_documents: list[str]
    verified_sources: list[str]
    review_text: str
    effective_date_placeholder: str = "«________»"
    version: str = "1.0"


def build_sop(spec: SOPSpec, out_path: Path) -> None:
    doc = Document()

    doc.add_paragraph("Standard Operating Procedure")
    doc.add_paragraph(spec.title)
    doc.add_paragraph(f"«Hospital Name» — Supports {spec.standard_code_range}")
    doc.add_paragraph("")
    doc.add_paragraph("")
    doc.add_paragraph("")

    _add_single_cell_table(doc, spec.what_is_this_for)
    _add_single_cell_table(doc, spec.worked_example)
    _add_single_cell_table(doc, spec.why_nabh_asks)

    ctrl = doc.add_table(rows=2, cols=4)
    ctrl.style = "Table Grid"
    ctrl.rows[0].cells[0].text = "SOP No."
    ctrl.rows[0].cells[1].text = spec.sop_no
    ctrl.rows[0].cells[2].text = "Version"
    ctrl.rows[0].cells[3].text = spec.version
    ctrl.rows[1].cells[0].text = "Effective Date"
    ctrl.rows[1].cells[1].text = spec.effective_date_placeholder
    ctrl.rows[1].cells[2].text = "Review Frequency"
    ctrl.rows[1].cells[3].text = "Annual, or on change"
    doc.add_paragraph("")

    doc.add_heading("1. Purpose", level=1)
    doc.add_paragraph(spec.purpose)

    doc.add_heading("2. Scope", level=1)
    doc.add_paragraph(spec.scope)

    doc.add_heading("3. Responsibility", level=1)
    for role, text in spec.responsibilities:
        doc.add_paragraph(f"{role}: {text}")

    doc.add_heading("4. Procedure", level=1)
    for i, block in enumerate(spec.blocks, start=1):
        doc.add_heading(block.heading, level=2)
        doc.add_paragraph(f"Why this step matters: {block.why_it_matters}")
        for step in block.steps:
            doc.add_paragraph(step)
        if block.technical_sources:
            doc.add_paragraph("Technical source(s) for these steps: ")
            for src in block.technical_sources:
                p = doc.add_paragraph(style="List Paragraph")
                p.add_run("• ")
                _render_source_text(p, src)

    doc.add_heading("5. Records", level=1)
    doc.add_paragraph(spec.records_note)

    doc.add_heading("6. Related Documents", level=1)
    for rd in spec.related_documents:
        doc.add_paragraph(rd, style="List Paragraph")

    doc.add_heading("7. Where This SOP's Requirements Come From (Verified Sources)", level=1)
    for src in spec.verified_sources:
        p = doc.add_paragraph(style="List Paragraph")
        p.add_run("• ")
        _render_source_text(p, src)

    doc.add_heading("8. Review", level=1)
    doc.add_paragraph(spec.review_text)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


# ------------------------------------------------------- SOP, v2 format -----
# Added Oct 2026 per Mk's explicit sign-off (sample iterated FMS.2_Combined_
# SOP_SAMPLE v1-v4, approved): one controlled document, two parts.
#   - Body: plain language, no NABH standard codes, no "NABH requires"
#     framing. Each section gets one short "Why:" line, patient/family/
#     staff-safety framed, never compliance-framed -- the only exception is
#     the Purpose section, which keeps the original three boxes (plain
#     summary / real trigger scenario / why-it-matters) because that's what
#     Mk reviewed and approved as the document's front matter.
#   - Appendix (after a page break): OE codes, boundary/disambiguation
#     against neighbouring standards, and verified hyperlinked citations,
#     ending in one consolidated reference list. For the Quality Coordinator
#     and NABH assessment use -- staff never need to read past "7. Review".
#
# This is intentionally a separate dataclass/function pair from SOPSpec/
# build_sop above, not a parameter bolted onto it: every other built chapter
# (AAC/COP/ROM/HRM, and FMS.1/.3/.4/.5 until each is separately approved in
# this new format) keeps using build_sop() unchanged. Nothing here is wired
# into that path.

def _box(doc: Document, text: str) -> None:
    _add_single_cell_table(doc, text)


def _three_boxes(doc: Document, plain: str, trigger: str, why: str) -> None:
    _box(doc, plain)
    _box(doc, trigger)
    _box(doc, why)


@dataclass
class PlainItem:
    heading: str                 # plain, no code, e.g. "Keeping patient-safety devices working"
    why: str                     # one line, patient/family/staff-safety framed, no NABH/codes
    body: list[str]              # plain-language paragraphs, codes/jargon stripped
    oe_code: str                 # appendix only, e.g. "FMS.2.a" or "FMS.2.f (Commitment, ASTERISKED)"
    boundary: list[str] = field(default_factory=list)   # appendix only
    technical_sources: list[str] | None = None          # appendix only


@dataclass
class SOPSpecV2:
    sop_no: str
    title: str
    purpose_plain: str                 # box 1 under Purpose
    purpose_trigger: str                # box 2
    purpose_why: str                    # box 3 -- patient-safety framed, not "NABH requires"
    purpose_text: str                   # the actual Purpose paragraph
    scope_why: str
    scope_text: str
    responsibility_why: str
    responsibilities: list[tuple[str, str]]
    items: list[PlainItem]
    records_note: str
    related_documents: list[str]
    review_text: str
    full_reference_list: list[str]
    effective_date_placeholder: str = "«________»"
    version: str = "1.0"


def build_sop_v2(spec: SOPSpecV2, out_path: Path) -> None:
    doc = Document()

    doc.add_paragraph("Standard Operating Procedure")
    doc.add_paragraph(spec.title)
    doc.add_paragraph(f"«Hospital Name» — {spec.sop_no} — Version {spec.version}")
    doc.add_paragraph("")

    ctrl = doc.add_table(rows=2, cols=4)
    ctrl.style = "Table Grid"
    ctrl.rows[0].cells[0].text = "SOP No."
    ctrl.rows[0].cells[1].text = spec.sop_no
    ctrl.rows[0].cells[2].text = "Version"
    ctrl.rows[0].cells[3].text = spec.version
    ctrl.rows[1].cells[0].text = "Effective Date"
    ctrl.rows[1].cells[1].text = spec.effective_date_placeholder
    ctrl.rows[1].cells[2].text = "Review Frequency"
    ctrl.rows[1].cells[3].text = "Annual, or on change"
    doc.add_paragraph("")

    # ---- Body ----
    doc.add_heading("1. Purpose", level=1)
    _three_boxes(doc, spec.purpose_plain, spec.purpose_trigger, spec.purpose_why)
    doc.add_paragraph(spec.purpose_text)

    doc.add_heading("2. Scope", level=1)
    doc.add_paragraph(spec.scope_why)
    doc.add_paragraph(spec.scope_text)

    doc.add_heading("3. Responsibility", level=1)
    doc.add_paragraph(spec.responsibility_why)
    for role, text in spec.responsibilities:
        rp = doc.add_paragraph()
        rp.add_run(f"{role}: ").bold = True
        rp.add_run(text)

    doc.add_heading("4. What to do", level=1)
    for item in spec.items:
        doc.add_heading(item.heading, level=2)
        doc.add_paragraph(item.why)
        for para in item.body:
            doc.add_paragraph(para)

    doc.add_heading("5. Records", level=1)
    doc.add_paragraph(spec.records_note)

    doc.add_heading("6. Related SOPs", level=1)
    for rd in spec.related_documents:
        doc.add_paragraph(rd, style="List Paragraph")

    doc.add_heading("7. Review", level=1)
    doc.add_paragraph(spec.review_text)

    # ---- Appendix ----
    doc.add_page_break()
    doc.add_heading("Appendix — NABH Standard Cross-Reference and Evidence Basis", level=1)
    doc.add_paragraph(
        "For the Quality Coordinator and NABH assessment use only. The reasoning "
        "and real-world triggers for each requirement are already in the body "
        "above -- this appendix adds only what the body deliberately leaves out: "
        "the exact objective-element code, how this SOP's scope is kept separate "
        "from neighbouring standards, and the verified technical source for "
        "anything cited."
    )
    for item in spec.items:
        doc.add_heading(f"{item.heading} — {item.oe_code}", level=2)
        if item.boundary:
            bp = doc.add_paragraph()
            bp.add_run("Boundary with other standards:").italic = True
            for b in item.boundary:
                doc.add_paragraph(f"• {b}", style="List Paragraph")
        if item.technical_sources:
            sp = doc.add_paragraph()
            sp.add_run("Verified source(s):").italic = True
            for src in item.technical_sources:
                dp = doc.add_paragraph(style="List Paragraph")
                dp.add_run("• ")
                _render_source_text(dp, src)

    doc.add_heading("Full reference list", level=2)
    for src in spec.full_reference_list:
        dp = doc.add_paragraph(style="List Paragraph")
        dp.add_run("• ")
        _render_source_text(dp, src)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))


# -------------------------------------------------------------- Record -----

@dataclass
class RecordSpec:
    oe_code: str
    oe_requirement: str
    record_title: str           # "FMS.1 Record 1 -- Space-to-service-directory alignment record"
    what_is_this: str
    real_example: str
    why_nabh_asks: str
    how_to_fill: list[tuple[str, str]]   # (column_name, instruction)
    verified_sources: list[str]
    column_headers: list[str]
    worked_example_row: list[str]
    extra_blank_rows: int = 7


def build_record(spec: RecordSpec, out_path: Path) -> None:
    doc = Document()

    doc.add_paragraph(f"{spec.oe_code} — {spec.oe_requirement}")
    doc.add_paragraph(spec.record_title)
    doc.add_paragraph("")
    doc.add_paragraph("")
    doc.add_paragraph("")

    _add_single_cell_table(doc, f"What is this record, in plain terms?\n{spec.what_is_this}")
    _add_single_cell_table(doc, f"A real example of when you'd use this\n{spec.real_example}")
    _add_single_cell_table(doc, f"Why does NABH ask for this?\n{spec.why_nabh_asks}")

    doc.add_paragraph("How to fill this in — column by column")
    for col, instr in spec.how_to_fill:
        doc.add_paragraph(f"{col}: {instr}")
    doc.add_paragraph(
        "The first data row below (shaded yellow, and marked WORKED EXAMPLE "
        "in the row itself) is a worked example already filled in correctly. "
        "Delete it or overwrite it once you start using this record for real "
        "— don't leave the example row mixed in with real entries. Add "
        "more blank rows as needed; don't create a second copy of this file."
    )
    doc.add_paragraph("")

    doc.add_paragraph("Where this requirement comes from (verified, clickable sources)")
    for src in spec.verified_sources:
        p = doc.add_paragraph(style="List Paragraph")
        p.add_run("• ")
        _render_source_text(p, src)
    doc.add_paragraph("")
    doc.add_paragraph("")
    doc.add_paragraph("")

    n_cols = len(spec.column_headers)
    total_rows = 1 + 1 + 1 + spec.extra_blank_rows  # header + spacer + example + blanks
    t = doc.add_table(rows=total_rows, cols=n_cols)
    t.style = "Table Grid"
    for j, h in enumerate(spec.column_headers):
        t.rows[0].cells[j].text = h
    _shade_row(t.rows[1])
    for j in range(n_cols):
        t.rows[1].cells[j].text = ""
    _shade_row(t.rows[2])
    for j, v in enumerate(spec.worked_example_row):
        t.rows[2].cells[j].text = v

    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(out_path))
