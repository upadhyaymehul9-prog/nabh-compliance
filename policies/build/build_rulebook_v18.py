# -*- coding: utf-8 -*-
"""
build_rulebook_v18.py
Builds HCO v2 Master Rulebook v1.8 from full preserved v1.7 content.

Change from v1.7: Extends Check 5.8 with a mandatory explicit pattern
match for the 'Guidebook interpretation supplied for...' generator
artefact, confirmed across all 20 COP documents and previously found
in AAC.9-13.

Run from policies/build/:
    python build_rulebook_v18.py
Output: HCO_v2_Master_Rulebook_and_Verification_Checklist.pdf
Archive: HCO_v2_Master_Rulebook_v1.7_ARCHIVE.pdf (renamed from current)
"""
import os
import shutil
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BUILD_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_PATH = os.path.join(BUILD_DIR, "HCO_v2_Master_Rulebook_v1.7_ARCHIVE.pdf")
CURRENT_PDF = os.path.join(BUILD_DIR, "HCO_v2_Master_Rulebook_and_Verification_Checklist.pdf")
OUT_DOCX = os.path.join(BUILD_DIR, "HCO_v2_Master_Rulebook_and_Verification_Checklist.docx")
OUT_PDF = CURRENT_PDF


def h1(doc, text):
    p = doc.add_paragraph(text, style="Heading 1")
    return p


def h2(doc, text):
    p = doc.add_paragraph(text, style="Heading 2")
    return p


def body(doc, text):
    p = doc.add_paragraph(text, style="Normal")
    return p


def bullet(doc, text):
    p = doc.add_paragraph(text, style="List Bullet")
    return p


def bullets(doc, items):
    for item in items:
        bullet(doc, item)


def build():
    # Step 1: Archive current v1.7 PDF
    if os.path.exists(CURRENT_PDF):
        if os.path.exists(ARCHIVE_PATH):
            print(f"Archive already exists: {ARCHIVE_PATH}")
        else:
            shutil.copy2(CURRENT_PDF, ARCHIVE_PATH)
            print(f"Archived v1.7 PDF to: {ARCHIVE_PATH}")
    else:
        print("WARNING: Current PDF not found — skipping archive step")

    doc = Document()

    # ── Page margins ──────────────────────────────────────────────────
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)

    # ── Version banner ────────────────────────────────────────────────
    banner = doc.add_paragraph(style="Normal")
    banner.add_run(
        "Version 1.8 – September 2026. Adds explicit mandatory pattern check to Check 5.8 "
        "(References / Rule 2.8 audit): Check 5.8 must now specifically search every References "
        "section for the ‘Guidebook interpretation supplied for…’ artefact string, "
        "confirmed as a recurring generator artefact found across all 20 COP documents and previously "
        "in AAC.9-13. All prior content preserved unchanged."
    ).italic = True

    # ── Title ─────────────────────────────────────────────────────────
    title_p = doc.add_paragraph(style="Title")
    title_p.add_run(
        "HCO Full v2 Policy Rewrite – Master Rulebook and\nVerification Checklist"
    )

    subtitle = doc.add_paragraph(style="Normal")
    subtitle.add_run(
        "Consolidated edition – combines the original rulebook, the project handoff’s "
        "recurring-failure-pattern notes, and every defect actually found and fixed during the "
        "HRM / PRE / IMS / COP completion sessions. Generated for chapter-by-chapter "
        "cross-checking, starting fresh from AAC."
    ).italic = True

    # ── Table of Contents ─────────────────────────────────────────────
    h1(doc, "How to use this document")
    bullets(doc, [
        "Section 0 – Source Verification (check this first, every time)",
        "0.1 – Raw dumps are a starting point, not a source of truth",
        "Section 1 – The Core Principle",
        "Section 2 – Content Rules",
        "2.1 – Match the source’s exact strength of obligation",
        "2.2 – Never reuse another standard’s sentences or reasoning",
        "2.3 – CORE / asterisk status lives in exactly one place",
        "2.4 – Abbreviations tables are derived, not copied",
        "2.5 – Policies must be understandable without NABH knowledge",
        "2.5d – No undefined internal shorthand terms [NEW v1.6]",
        "2.5e – Deferred definitions must name where the definition lives [NEW v1.6]",
        "2.5f – No reference to a resource that isn’t provided or located [NEW v1.7]",
        "2.6 – Never invent a specific date, number, or deadline the source doesn’t give",
        "2.7 – No leftover template boilerplate",
        "2.8 – References lists external authority only",
        "2.9 – Filling NABH’s deliberate gaps with verified external practice [extended v1.4]",
        "2.10 – Every stated time value must have a verified source, cited in References [NEW v1.3]",
        "Section 3 – Structure and Formatting Rules",
        "3.1 – Title",
        "3.2 – Guillemets (« »)",
        "3.3 – Staff acknowledgement sentence",
        "3.4 – Section order",
        "3.5 – Word paragraph styles",
        "3.6 – Document control table",
        "Section 4 – Recurring Failure Patterns",
        "Pattern A – Modal-strength inflation",
        "Pattern B – Cross-standard content borrowing",
        "Pattern C – Inline CORE/asterisk narration",
        "Pattern D – Cross-reference codes leaking into prose",
        "Pattern E – Stop-work tags blanket-applied to every OE in a standard",
        "Pattern F – Auto-generated non-negotiables violate Rule 2.7 by construction",
        "Pattern G – Dump commentary treated as sourced fact",
        "Pattern H – Docx-level structural bugs invisible to text review",
        "Pattern I – Rule 2.8’s References bug recurring in already-committed chapters",
        "Section 5 – Verification Loop (run all of this, every standard)",
        "5.1 – Pull and verify the source",
        "5.2 – Cross-check against the real Guidebook pages",
        "5.3 – Draft",
        "5.4 – Overlap check",
        "5.5 – Build",
        "5.6 – Guillemet audit",
        "5.7 – Cross-reference leak audit (Pattern D)",
        "5.8 – References / Rule 2.8 audit (Pattern I) [extended v1.8]",
        "5.9 – CORE/asterisk inline-sentence audit (Pattern C)",
        "5.10 – Fabricated-frequency audit (Pattern G)",
        "5.11 – Stop-work tagging audit (Pattern E)",
        "5.12 – Template boilerplate audit (Pattern F, Rule 2.7)",
        "5.13 – Paragraph style / structure check",
        "5.14 – Visual render check",
        "5.15 – Open the real file in Word (Pattern H – not optional)",
        "5.16 – Confirm before committing",
        "5.17 – Verified-practice source audit [extended v1.5]",
        "5.18 – Undefined shorthand audit [NEW v1.6]",
        "5.19 – Deferred-definition audit [NEW v1.6]",
        "5.20 – Dead reference audit [NEW v1.7]",
        "Section 6 – Git Discipline",
        "Section 7 – Official Chapter and Standard Counts",
        "Disclaimer",
    ])

    # ── Body: How to use ──────────────────────────────────────────────
    body(doc,
         "This is the single reference to check any chapter’s raw source dump and any "
         "generated policy .docx against. It replaces the original 8-page rulebook – "
         "everything from that document is preserved here, with the failure patterns that were "
         "only theoretical there now marked with a confirmed real-world hit from this project.")
    body(doc, "For each chapter, in order:")
    bullets(doc, [
        "Get the real NABH HCO Full Accreditation 6th Edition source – the Standards PDF "
        "and the Guidebook – for that chapter specifically. See Section 0: Source "
        "Verification before touching anything else.",
        "Pull or receive the raw OE/Guidebook dump for the chapter.",
        "Cross-check the dump against the real Guidebook pages, not just against itself. "
        "This is what has caught every real error so far.",
        "Draft plain-language content following Sections 1–3.",
        "Build the .docx.",
        "Run every check in Section 5: The Verification Loop – all of it, not a subset "
        "– before treating anything as done.",
        "Open the actual file in Word. Not optional. See Section 5.15.",
        "Stage and commit per Section 6: Git Discipline.",
    ])

    # ── Section 0 ─────────────────────────────────────────────────────
    h1(doc, "Section 0 – Source Verification (check this first, every time)")
    body(doc,
         "This project has already shipped one near-miss: an attempt to build the IMS chapter "
         "from SHCO 3rd Edition build scripts that were sitting in the repo, when the actual "
         "target is HCO Full Accreditation 6th Edition – a different NABH programme with "
         "different OE text, different OE counts, and different chapter numbering. It was caught "
         "before anything got drafted, but only because it was checked.")
    body(doc, "Before drafting anything for a chapter:")
    bullets(doc, [
        "Confirm the source material is explicitly HCO Full Accreditation, 6th Edition. If a "
        "script, JSON file, or dump references SHCO, a different edition number, or doesn’t "
        "say which programme it’s from, stop and confirm before using it.",
        "Confirm the OE count for the chapter matches the official chapter table (Section 7 of "
        "this document) before drafting a single standard. A mismatch (like AAC being treated "
        "as 8 standards when it has 13) is a scoping error, not a content error, and it "
        "compounds silently.",
        "When extracting from a PDF, do not assume a printed page number equals the PDF’s "
        "internal page index. A 242-page PDF’s internal page 293 is not necessarily the "
        "page printed as ‘293’ in the document. If page-index extraction produces "
        "nonsense (wrong chapter, garbled text), stop and ask for the correct page range "
        "rather than guessing.",
        "The safest source is the person supplying the actual Guidebook PDF pages for the "
        "chapter, the same way PRE (pages 176–195) and IMS (pages 293–311) were "
        "supplied this session. A raw dump alone is not enough to trust – see Section 0.1.",
    ])

    h2(doc, "0.1 – Raw dumps are a starting point, not a source of truth")
    body(doc,
         "A raw dump can be well-organised and still contain two kinds of content that must be "
         "told apart before drafting:")
    bullets(doc, [
        "Sourced content: the verbatim OE text and the Guidebook’s own Interpretation "
        "paragraph. This is safe to draft from.",
        "Dump-author commentary: ‘Achievement status’ narratives, worked "
        "audit-guidance examples, or ‘Documentation’ notes that describe what an "
        "assessor might look for. This is often useful context, but it is not Guidebook text, "
        "and it has already been caught inventing specific numbers that don’t exist in the "
        "source (see Rule 2.6 and Pattern G below).",
    ])
    body(doc,
         "When a dump gives you a specific number – a frequency, a day count, a percentage "
         "– trace it back to the actual OE or Interpretation sentence it came from. If it "
         "only appears in a commentary/status section, leave it out.")

    # ── Section 1 ─────────────────────────────────────────────────────
    h1(doc, "Section 1 – The Core Principle")
    body(doc,
         "A policy rewrite has two separate jobs, and they must not be confused:")
    bullets(doc, [
        "Structure/formatting – title format, section order, table layout, bracket rules. "
        "This is mechanical and safe to copy from an approved reference document.",
        "Content – the actual rules, obligations, and explanations. This is not mechanical. "
        "It must be pulled fresh from each standard’s own source text (OE + Guidebook "
        "interpretation) and checked every single time, even though the pattern looks the same.",
    ])
    body(doc,
         "Never let confidence in the structure create false confidence in the content. A "
         "document can be perfectly formatted and still contain a wrong rule. A document can "
         "also be perfectly worded and still be structurally broken in a way plain-text review "
         "won’t catch – see Pattern H below, found in this project’s own IMS build.")

    # ── Section 2 ─────────────────────────────────────────────────────
    h1(doc, "Section 2 – Content Rules")

    h2(doc, "2.1 – Match the source’s exact strength of obligation")
    body(doc,
         "NABH source text uses different modal words on purpose: shall / must (mandatory), "
         "may / could (optional or an example), should (recommended). A rewritten rule must "
         "preserve that exact strength – never upgrade a ‘may’ into a "
         "‘must’.")
    body(doc,
         "Do: Pull the raw OE sentence and the Guidebook interpretation before writing any rule. "
         "Write out a modal-strength table (which words are shall/may/could) before drafting "
         "rules. When a source lists something as one possible example (‘could be in the "
         "form of a registration certificate’), phrase it as an example, not the only "
         "accepted method.")
    body(doc,
         "Don’t: Don’t turn ‘may require formal orientation’ into "
         "‘Do not skip formal orientation.’ (Real error, ROM.1 draft 1.) Don’t "
         "turn ‘selection may be based on qualifications…’ into a required "
         "criterion. (Real error, ROM.1 draft 1.) Don’t invent enumerated failure scenarios "
         "the source never lists.")

    h2(doc, "2.2 – Never reuse another standard’s sentences or reasoning")
    body(doc,
         "Each standard’s rules must trace only to its own OE text and interpretation "
         "– never copied or adapted from a sibling standard, even when the topics feel "
         "related.")
    body(doc,
         "Do: Run an explicit overlap check before presenting a draft: which sentences also "
         "appear in previously-approved documents, and is that overlap genuine shared boilerplate "
         "(training sentence, distribution line) or borrowed subject-matter content that belongs "
         "to the other standard? State the check’s result out loud, even if the answer is "
         "‘no reuse found.’")
    body(doc,
         "Don’t: Don’t reuse a chapter-specific exclusion list. (ROM.1’s "
         "exclusion list was copied wholesale into a ROM.6 draft – wrong duties entirely.) "
         "Don’t let two different standards’ Reference sections list the same internal "
         "artefacts unless those artefacts genuinely belong to both.")

    h2(doc, "2.3 – CORE / asterisk status lives in exactly one place")
    body(doc,
         "Objective elements are asterisked (documentation required) or marked CORE (zero "
         "tolerance) in the official standards data. This status must survive into the rewritten "
         "document – but only once.")
    body(doc,
         "Do: Put CORE/asterisk status only in a ‘Level’ column in the Traceability "
         "table, pulled from the actual inventory data – never transcribed by eye. Give the "
         "Quality Monitoring section a working cross-reference back to that Level column, with "
         "the right section number.")
    body(doc,
         "Don’t: Don’t write ‘This objective element is asterisked…’ "
         "or ‘This is a CORE objective element…’ as inline sentences inside the "
         "plain-language ‘What we do’ prose. It breaks the readable voice and "
         "duplicates the Traceability table. Don’t drop the CORE/asterisk marker entirely "
         "– the underlying obligation still needs a real referent somewhere in the document.")

    h2(doc, "2.4 – Abbreviations tables are derived, not copied")
    body(doc,
         "Do: List only abbreviations that actually appear in that specific document’s "
         "rendered text. Derive this mechanically – scan the rendered body (excluding the "
         "glossary itself) and keep only abbreviations with at least one real occurrence.")
    body(doc,
         "Don’t: Don’t copy a fixed abbreviations list from a previous chapter’s "
         "approved document. A governance policy listing AERB (a radiation authority) makes the "
         "document look template-assembled.")

    h2(doc, "2.5 – Policies must be understandable without NABH knowledge")
    body(doc,
         "Every policy document must be fully understandable to a reader with zero knowledge of "
         "NABH standards, chapter codes, or accreditation terminology. The document’s job "
         "is to tell hospital staff what to do – not to map onto an accreditation framework "
         "the reader may never have heard of.")
    body(doc, "This means:")
    bullets(doc, [
        "The Purpose section’s boundary statement must describe what topics this policy "
        "does NOT cover in plain language (e.g., ‘This policy does not cover patient "
        "registration or admission – those are covered in other hospital "
        "policies’), WITHOUT the trailing sentence ‘The other [Chapter] standards "
        "have their own policies too’ or any similar phrase that only makes sense to "
        "someone who already knows what a ‘standard’ or ‘chapter’ is in "
        "NABH’s system.",
        "No standard code (e.g., ‘AAC.1.a-d’, ‘COP.6’) may appear anywhere "
        "in the Purpose, Scope, or body prose sections – not even the document’s own "
        "standard number. Describe content by topic, not by code. (‘It covers defining "
        "services in line with community needs, diagnostic and treatment capability with "
        "qualified personnel, department scope, and permanent bi-lingual display’ – "
        "not ‘It covers AAC.1.a-d: …’).",
        "Sections 11 (Traceability table) and 12 (Required Records / Evidence Checklist) are "
        "explicitly EXEMPT from this rule – these are reference/audit sections where NABH "
        "codes are expected and useful, and require no change.",
    ])
    body(doc,
         "This rule applies retroactively to all previously-built documents, not just newly "
         "drafted ones – because the underlying framing (assuming NABH literacy) was baked "
         "into every chapter’s Purpose/Scope generation.")

    h2(doc, "2.5d – No undefined internal shorthand terms [NEW v1.6]")
    body(doc,
         "A policy document must not introduce a compound or shorthand label for a concept "
         "(e.g., ‘temporary-holding over-run,’ ‘priority-flag lapse’) and "
         "then use that label elsewhere in the document as if it were self-explanatory, unless "
         "the label is explicitly defined at first use.")
    body(doc,
         "This applies whether the underlying concept is explained earlier in the same document "
         "or not – a reader may encounter any single sentence in isolation (a training "
         "extract, an audit excerpt, a quoted passage) and must be able to understand it without "
         "needing to have read the rest of the document first.")
    body(doc,
         "Fix pattern: either (a) spell out the concept in plain language at the point of use "
         "instead of using a shorthand label, or (b) if a shorthand term is genuinely useful "
         "for a repeated concept, define it in full the first time it appears (e.g., ‘a "
         "patient remaining on a temporary bed beyond the defined limit – a "
         "temporary-holding over-run’) and only use the bare shorthand in later occurrences "
         "within the same document.")
    body(doc,
         "This rule was added after AAC.2’s ‘temporary-holding over-run’ was "
         "found used in a Quality Monitoring sentence without ever being defined anywhere in "
         "the document – a reader encountering that sentence alone would not know what it "
         "meant.")

    h2(doc, "2.5e – Deferred definitions must name where the definition lives [NEW v1.6]")
    body(doc,
         "When a policy defers a specific number, threshold, or procedure to ‘the "
         "organisation’s defined [X]’ (rather than stating the value directly), it "
         "must also state WHERE that definition actually lives – e.g., a named SOP, a "
         "specific role responsible for setting it (e.g. ‘as defined by the Quality "
         "Coordinator in the RCA procedure’), or a cross-reference to a real governance "
         "document.")
    body(doc,
         "A bare deferral with no named home for the definition (e.g., ‘the "
         "organisation’s defined recurrence threshold applies,’ with nothing else) "
         "is not acceptable – it reads as a promise pointing at nothing and gives hospital "
         "staff no way to actually find or act on the value. This is functionally as ungrounded "
         "as a fabricated number, just vaguer instead of false.")
    body(doc,
         "This rule was added after reviewing AAC.1-8’s root-cause-analysis "
         "recurrence-threshold fixes, which uniformly used ‘the organisation’s "
         "defined recurrence threshold applies’ without stating where that threshold is "
         "actually documented.")

    h2(doc, "2.5f – No reference to a resource that isn’t provided or located [NEW v1.7]")
    body(doc,
         "A policy document must not tell the reader to “refer to” or “see” "
         "another resource (a Glossary, an Appendix, another policy, a table) unless that "
         "resource either (a) actually exists within this same document, or (b) is named "
         "precisely enough to be found — a specific document title, section number, page "
         "reference, or URL.")
    body(doc,
         "A bare reference like “refer to the Glossary” with no glossary present "
         "anywhere in the document, and no indication of where such a glossary can be found, "
         "is a dead pointer and must be fixed by either:")
    bullets(doc, [
        "including the actual definition directly in the document at the point of use, or",
        "naming precisely where the resource lives (e.g., “see the NABH Guidebook to "
        "Accreditation Standards for Hospitals, 6th Edition, Glossary of Terms”).",
    ])
    body(doc,
         "This rule was added after COP.1 was found instructing readers to “refer to the "
         "Glossary” for two specific term definitions, in three separate places, when no "
         "glossary existed anywhere in the document or was named as a locatable external source.")

    h2(doc, "2.6 – Never invent a specific date, number, or deadline the source doesn’t give")
    body(doc,
         "Real error caught in a comparison test: a model asked to fill in a Document Control "
         "table invented ‘Effective Date: October 2026’ and ‘Next Review: October "
         "2027’ – plausible-looking, completely fabricated.")
    body(doc,
         "Confirmed hit this session: PRE.7 and PRE.8’s first build included "
         "‘quarterly PREM reporting,’ ‘complaints within 7 days,’ and "
         "‘feedback tabulated monthly’ – none of it stated anywhere in the actual "
         "OE or Guidebook interpretation. It had leaked in from the raw dump’s own "
         "illustrative ‘Achievement status’ commentary (see Section 0.1). It had to "
         "be stripped and rebuilt.")
    body(doc,
         "Do: Leave a real blank – ‘________’ – for any date, effective "
         "date, or review date not supplied as part of the source data. Only state a specific "
         "number (a frequency, a deadline, a threshold) when the OE or Guidebook text actually "
         "states that number. When a dump gives you a number, trace it to its literal source "
         "sentence before using it. If you can’t find it in the OE or Interpretation text "
         "itself, don’t use it.")
    body(doc,
         "Don’t: Don’t fill in a plausible-sounding date, version number, or interval "
         "just because the template has a field for it. Don’t carry a dump’s "
         "‘Achievement status’ or ‘Documentation’ narrative numbers into "
         "policy text as if they were sourced obligations.")

    h2(doc, "2.7 – No leftover template boilerplate")
    body(doc, "Don’t include, unless it appears in an already-approved reference document:")
    bullets(doc, [
        "‘This policy covers all N requirements under this standard, listed in detail "
        "below.’",
        "‘Do not skip: [restated OE sentence]’ as a non-negotiable rule – this "
        "is a label, not a rule. (See Pattern F.)",
        "‘Hospital Name implements X so that [restated OE sentence]’ or ‘This "
        "policy says how Hospital Name meets standard X:’",
        "Internal build artefacts: md5 hashes, OCR file paths, draft_label values, ‘Method "
        "note (from guidebook interpretation):’ – none of this belongs in a document "
        "a hospital or assessor reads.",
    ])

    h2(doc, "2.8 – References lists external authority only")
    body(doc, "(Added after the AAC.1-8 audit. Confirmed to recur in PRE.1-4 – see Pattern I.)")
    body(doc,
         "The References section exists to cite outside sources that justify what the policy "
         "says – the NABH Guidebook, ISO/NABL standards, named Acts. It is not a second "
         "copy of the hospital’s own records.")
    body(doc,
         "Do: Keep References limited to external authority: the NABH Guidebook citation for "
         "the standard, and any named external standard or law actually stated in the source "
         "(ISO 15189:2022, NABL 112, AERB, PC-PNDT Act, the Indian Nursing Council Act, the "
         "Code of Medical Ethics, etc.) – never invented ones. Let the Required Records / "
         "Evidence Checklist section be the only place the hospital’s own internal "
         "documents are listed.")
    body(doc,
         "Don’t: Don’t add a bullet like ‘Internal documents of "
         "«Hospital Name»: …’ to References. If the same list already "
         "appears in the Required Records section, repeating it in References is pure "
         "duplication. If a specific internal document genuinely needs to be pointed to from "
         "References (rare), it must carry its own document number and revision.")

    h2(doc, "2.9 – Filling NABH’s deliberate gaps with verified external practice [extended v1.4]")
    body(doc,
         "Where NABH’s source text deliberately leaves a number, frequency, or method "
         "undefined (using ‘may,’ ‘could,’ ‘at appropriate "
         "intervals,’ ‘within a defined time frame,’ or similar), the hospital "
         "may adopt a specific practice based on a verified, internationally recognised standard "
         "or professional body’s published guidance – provided:")
    bullets(doc, [
        "The source is real, current, and independently verifiable via a live, working link.",
        "Policy text is honest about authorship: phrased as ‘the organisation’s "
        "defined practice, based on [source]’ – never implied to be an NABH mandate.",
        "The source is listed in the standard’s References section as a named external "
        "authority – the same treatment NABH’s own Guidebook uses (e.g., AAC.7.a "
        "citing ISO 15189:2022 and NABL 112).",
        "This never overrides a number NABH does explicitly state – it only fills genuine, "
        "confirmed gaps.",
        "Every source must be actually searched, fetched, and confirmed live at drafting time "
        "– never invented or assumed by an AI drafting tool. A plausible-sounding but "
        "unverified citation is the same class of error as a fabricated number (see Pattern G) "
        "and is treated with equal severity.",
    ])
    body(doc,
         "When multiple credible external sources conflict on a value, the following priority "
         "order applies for source selection:")
    bullets(doc, [
        "NABH’s own text (always wins if it states a number – see Rule 2.1).",
        "WHO (World Health Organization) guidance, where applicable.",
        "The Joint Commission (TJC) or Joint Commission International (JCI) patient-safety "
        "standards – cite whichever body actually published the specific standard in "
        "question; never treat TJC and JCI as interchangeable, since they are related but "
        "distinct organizations with separate published standards.",
        "Other named professional/accrediting bodies (e.g., CAP, ACEP, ISO, NABL) – used "
        "when none of the above have published on the specific point.",
        "Peer-reviewed research findings – used only when no accrediting or professional "
        "body has published a direct standard.",
    ])
    body(doc,
         "Higher-priority sources override lower ones on conflict. The rationale for the source "
         "actually selected must be stated in the policy text (per Rule 2.9’s "
         "authorship-honesty requirement), and if two sources at the SAME priority level "
         "disagree, the discrepancy must be disclosed per Rule 2.10 rather than silently "
         "resolved.")

    h2(doc, "2.10 – Every stated time value must have a verified source, cited in References [NEW – v1.3]")
    body(doc,
         "Any time-based value stated as a firm rule in a policy document – an hour, a day "
         "count, a week, a month, a quarter, a year, or any other specific duration or frequency "
         "– must satisfy one of these two conditions, with no exception:")
    bullets(doc, [
        "The value is taken directly from NABH’s own OE or Interpretation text (e.g., "
        "AAC.4.c’s ‘24 hours,’ AAC.6.g’s ‘one hour’). No "
        "citation is needed beyond the existing NABH Guidebook reference already in this "
        "standard’s References section.",
        "The value is NOT stated by NABH (NABH leaves it undefined, uses ‘may,’ "
        "‘could,’ ‘at appropriate intervals,’ ‘within a defined time "
        "frame,’ or is simply silent). In this case, per Rule 2.9, the value must be "
        "based on a verified, real, independently-checkable external authority – and that "
        "source MUST be named in the References section of that same standard’s document, "
        "with enough detail (author/body, publication, and a working reference) that a reader "
        "can verify it themselves.",
    ])
    body(doc,
         "There is no third option. A time value that is neither NABH-sourced nor externally "
         "verified and cited is a Rule 2.6/Pattern G violation and must be fixed before the "
         "document is considered complete – either by sourcing it properly (per Rule 2.9) "
         "or by removing the specific number and using NABH’s own open-ended language "
         "instead (as done for AAC.5’s early-warning review, where no verified external "
         "source existed for that specific claim).")
    body(doc,
         "When two credible external sources disagree (e.g., two accreditation or professional "
         "bodies proposing different values for the same practice), the discrepancy must be "
         "disclosed rather than silently picking one – either by naming the source actually "
         "adopted and why, or by flagging the disagreement to the person for a decision, as was "
         "done for AAC.2’s temporary-bed holding time (Joint Commission’s 4 hours vs. "
         "CMS’s 6 hours).")
    body(doc,
         "This rule applies retroactively: every time value in all 100 already-built documents "
         "must be checked against this rule, not just newly drafted content.")

    # ── Section 3 ─────────────────────────────────────────────────────
    h1(doc, "Section 3 – Structure and Formatting Rules")

    h2(doc, "3.1 – Title")
    bullets(doc, [
        "Format: ‘Policy on [Subject]’ – e.g. ‘Policy on Those Responsible "
        "for Governance’.",
        "Uses the Word ‘Title’ paragraph style – not Heading 1, not plain bold "
        "text.",
        "No chapter/edition subtitle line underneath.",
    ])

    h2(doc, "3.2 – Guillemets (« »)")
    bullets(doc, [
        "Keep « » brackets only around ‘Hospital Name’ – this is the "
        "one placeholder the delivery system finds and replaces automatically.",
        "Every other placeholder (Medical Superintendent, department in-charge, quarterly, 90 "
        "days, role names, timeframes, frequencies, etc.) is written as plain text.",
    ])

    h2(doc, "3.3 – Staff acknowledgement sentence")
    bullets(doc, [
        "Format: ‘I have read the Policy on [Subject] of «Hospital Name». "
        "I will follow the processes described.’",
        "Check for the ‘Policy on X policy of Y’ stutter whenever the title changes.",
    ])

    h2(doc, "3.4 – Section order")
    body(doc, "In this exact sequence:")
    bullets(doc, [
        "Document control (table)",
        "Statement of intent",
        "Purpose",
        "Scope",
        "Policy standards",
        "Non-negotiable rules",
        "What we do (with 5.1, 5.2… subsections)",
        "Stop-work authority – only if the standard actually has stop-work data in its "
        "source (see Pattern E – this is the single most commonly mis-applied rule in the "
        "whole project)",
        "Governance and responsibility (table)",
        "Quality monitoring",
        "Training and staff acknowledgement (with signature table)",
        "Distribution",
        "Abbreviations (table)",
        "Traceability to NABH HCO Full Accreditation 6th Edition [Code] (table, with Level "
        "column)",
        "Required Records / Evidence Checklist",
        "References – LAST numbered section, immediately before Disclaimer",
        "Disclaimer (fixed paragraphs, not numbered)",
    ])
    body(doc,
         "When section numbers shift because a standard has no Stop-work section, check every "
         "internal ‘Section N’ cross-reference in the document – a Level-column "
         "reference or a Quality Monitoring reference can silently point at the wrong number.")

    h2(doc, "3.5 – Word paragraph styles")
    bullets(doc, [
        "Main title: Title",
        "Top-level sections: Heading 1",
        "Subsections (5.1, 5.2…): Heading 2",
        "Body text: Normal",
        "Non-negotiable rules: List Number (native Word numbering – see Pattern H)",
        "Bulleted lists (References, Evidence Checklist): List Bullet",
    ])
    body(doc,
         "Real error caught: a document generated by cloning another file’s raw XML had "
         "its title on Heading 1 instead of Title, and every top-level section demoted one "
         "level. Always verify the actual paragraph style objects, not just how the text looks "
         "when skimmed.")

    h2(doc, "3.6 – Document control table")
    body(doc,
         "6 rows – 4 columns: Document No./Version, Issue No./Review due, Date "
         "created/Date of implementation, then Prepared by / Reviewed by / Approved by – "
         "each spanning the remaining columns as one merged cell.")
    body(doc,
         "Prepared/Reviewed/Approved rows must be actual table rows with merged cells – "
         "not separate paragraphs sitting below the table.")

    # ── Section 4 ─────────────────────────────────────────────────────
    h1(doc, "Section 4 – Recurring Failure Patterns")
    body(doc,
         "Every pattern below has caused a real, confirmed error in this project. When auditing "
         "a new chapter, check for all of them – not just the ones that feel likely for "
         "that chapter’s subject matter.")

    h2(doc, "Pattern A – Modal-strength inflation")
    body(doc, "Turning ‘may’ or ‘could’ into ‘must’ or ‘shall.’ See Rule 2.1.")

    h2(doc, "Pattern B – Cross-standard content borrowing")
    body(doc,
         "Reusing a sibling standard’s specific reasoning or exclusion list instead of "
         "drafting from the standard’s own source. See Rule 2.2.")

    h2(doc, "Pattern C – Inline CORE/asterisk narration")
    body(doc,
         "Writing ‘this is a CORE element’ in the readable prose instead of only in "
         "the Traceability table. See Rule 2.3.")

    h2(doc, "Pattern D – Cross-reference codes leaking into prose")
    body(doc,
         "The rule against reproducing codes like ‘COP.1.e’ in policy prose gets "
         "violated pervasively – not just cross-chapter (AAC→PRE/COP/HRM/ROM, "
         "FMS→IPC/MOM) but same-chapter, standard-to-standard (AAC.1 citing AAC.6/8, "
         "AAC.6 citing AAC.7). A first audit pass on any chapter that only searches for "
         "cross-chapter codes will under-report the problem.")
    body(doc,
         "Confirmed hits: AAC.1-8 (same-chapter leaks missed by the first pass), HRM.6 "
         "(PSQ.1.a, IPC.8.a), HRM.9 (FMS.3.a). PRE.5-8 and IMS were checked and had none in "
         "source – but they still had to be checked.")
    body(doc,
         "When auditing any chapter, search for the chapter’s own code prefix as a "
         "cross-reference target too, not just other chapters’ prefixes.")
    body(doc,
         "Fix is always the same: replace the named code with ‘covered in other hospital "
         "policies’ (or, for same-standard self-references like ‘AAC.1.a-d’ or "
         "‘HRM.8.c-e’ pointing to a different OE within the same standard, rephrase "
         "as an internal section pointer like ‘Section 5.3’ – those are fine to "
         "keep as internal pointers, only pointers to a different standard are the problem).")

    h2(doc, "Pattern E – Stop-work tags blanket-applied to every OE in a standard")
    body(doc,
         "A confirmed, documented bug in generation tooling: a standard’s ‘Where "
         "addressed’ column tags every OE with ‘Section 6, Stop-work’ when the "
         "actual stop-work triggers apply to only one or two specific OEs.")
    body(doc,
         "Confirmed hits: ROM.6 (triggers only on .d and .e, not a/b/c/f – found by "
         "manual inspection after the automated fix missed it). The same bug’s source "
         "comments were found in the HRM.11/12/13 raw dump itself before any drafting began: "
         "oe_mapping() was documented as adding ‘; Section 6 Stop-work’ to all OEs, "
         "when the dump’s own OE-level flags confirmed real triggers exist on only 2 of "
         "6-7 OEs per standard (HRM.11.a/d, HRM.12.a/d, HRM.13.a/c).")
    body(doc,
         "This was headed off successfully in HRM.11-13 by flagging it explicitly in the "
         "drafted content before building, and confirmed correct in the rendered Traceability "
         "table afterward. That is the model to repeat: state which specific OEs trigger "
         "stop-work, in writing, before the build step – don’t wait to catch it "
         "after. Assume this bug is possible in any standard with stop-work data until checked, "
         "in every chapter.")

    h2(doc, "Pattern F – Auto-generated non-negotiables violate Rule 2.7 by construction")
    body(doc,
         "A generator’s default non-negotiable output can follow the pattern ‘Do not "
         "skip: {OE text restated}’ – which Rule 2.7 explicitly prohibits. This is a "
         "label, not a rule.")
    body(doc,
         "Every standard’s non-negotiables section must be hand-written as a real "
         "prohibition, phrased as an actual ‘do not do X’ instruction with its own "
         "logic – not a mechanical restatement of the OE sentence with ‘Do not "
         "skip’ bolted on front. Any chapter using auto-generation for this section should "
         "be checked for this pattern specifically.")

    h2(doc, "Pattern G – Dump commentary treated as sourced fact")
    body(doc, "(New this session – see Section 0.1 and Rule 2.6.)")
    body(doc,
         "A raw dump’s own ‘Achievement status’ or ‘Documentation’ "
         "narrative – which describes what an assessor might plausibly look for – "
         "can contain specific numbers (a frequency, a day count) that do not appear anywhere "
         "in the actual OE or Guidebook interpretation text.")
    body(doc,
         "Confirmed hit: PRE.7 and PRE.8’s build included ‘quarterly,’ ‘7 "
         "days,’ and ‘monthly’ language sourced from exactly this kind of "
         "commentary, not from the standard’s real source text. Caught by close reading "
         "against the literal Guidebook pages, not by trusting the dump.")
    body(doc,
         "Before using any specific number from a dump, find its literal sentence in the OE "
         "text or the Guidebook Interpretation paragraph. If it only exists in a "
         "status/commentary section, it does not go in the policy.")

    h2(doc, "Pattern H – Docx-level structural bugs invisible to text review")
    body(doc, "(New this session, found in the IMS chapter build.)")
    body(doc,
         "A document’s text content can be extracted, read, and confirmed correct – "
         "every word right, every section present – while the rendering is still broken. "
         "Found in this project: a non-negotiables list where the docx-generation code applied "
         "Word’s native auto-numbering and also hardcoded a literal ‘1.’, "
         "‘2.’ prefix into each list item’s own text, producing a doubled "
         "‘1. 1. Do not…’ / ‘2. 2. Do not…’ result that "
         "plain-text extraction (pandoc, raw XML text parsing) does not surface, because the "
         "extracted text technically reads fine linearly.")
    body(doc,
         "This is why opening the actual file in a real Word renderer is not optional "
         "(Section 5.15) – some defects only exist in how content is combined with "
         "structure, and a text-only check will pass a genuinely broken file.")
    body(doc,
         "Any time a build process combines native Word numbering/bullets with "
         "manually-written ordinal prefixes in the same list, check the rendered output "
         "specifically for doubled numbers.")

    h2(doc, "Pattern I – Rule 2.8’s References bug recurring in already-committed chapters")
    body(doc, "(New this session.)")
    body(doc,
         "The Rule 2.8 ‘internal documents in References’ bug was first found and "
         "fixed in AAC.1-8. It was assumed fixed project-wide afterward. It was not: the same "
         "generator-level bug was found independently in PRE.1-4 – files that had already "
         "been committed and treated as ‘done’ for the entire project’s duration "
         "up to this point.")
    body(doc,
         "‘Already committed’ and ‘already audited’ are not the same "
         "claim. A generator-level bug fixed in one chapter does not mean it was fixed "
         "everywhere that chapter’s generator (or a sibling generator built the same way) "
         "touched. Any chapter using a generator script that has ever shown this bug anywhere "
         "should be re-checked for it specifically, even if it was committed and ‘finished’ "
         "long ago.")

    # ── Section 5 ─────────────────────────────────────────────────────
    h1(doc, "Section 5 – Verification Loop (run all of this, every standard)")
    body(doc,
         "This is the process that catches the errors above. Skipping any step is how a wrong "
         "rule or a broken file reaches a finished document.")

    h2(doc, "5.1 – Pull and verify the source")
    body(doc,
         "Get the raw OE text and Guidebook interpretation for every objective element in the "
         "standard, verbatim, from the actual HCO 6th Edition source (see Section 0). Never "
         "draft from memory or by pattern-matching a previous chapter. Check for "
         "truncation/corruption before using it.")

    h2(doc, "5.2 – Cross-check against the real Guidebook pages")
    body(doc,
         "If the person can supply the actual Guidebook PDF pages for the chapter, cross-check "
         "the dump against them before drafting – this is what caught Pattern E in HRM "
         "before any content was written, and Pattern G in PRE after the fact. Don’t skip "
         "this step just because a dump ‘looks’ complete.")

    h2(doc, "5.3 – Draft")
    body(doc,
         "Follow Sections 1–3 above. Flag, in writing, any standard with stop-work data, "
         "naming exactly which OEs trigger it (Pattern E).")

    h2(doc, "5.4 – Overlap check")
    body(doc,
         "Explicitly compare the new draft’s sentences against every previously-approved "
         "document in the chapter. Report which sentences overlap and why (shared boilerplate "
         "vs. borrowed content) – even an answer of ‘no reuse found’ should be "
         "stated, not assumed.")

    h2(doc, "5.5 – Build")
    body(doc, "Generate the actual .docx file.")

    h2(doc, "5.6 – Guillemet audit")
    body(doc,
         "Search the rendered text for every «» occurrence. The only string that "
         "should ever appear inside guillemets is ‘Hospital Name’. Anything else "
         "– a role, a frequency, a timeframe – is a Rule 3.2 violation.")

    h2(doc, "5.7 – Cross-reference leak audit (Pattern D)")
    body(doc,
         "Search for every occurrence of a standard-code pattern (e.g. "
         "[A-Z]{2,4}\\.[0-9]+(\\.[a-z])?) in the rendered text. Every hit should belong to "
         "the standard’s own code. Any hit from a different chapter, or a different "
         "standard within the same chapter, is a leak – fix by rephrasing as "
         "‘covered in other hospital policies’ (different standard) or an internal "
         "section pointer (same standard).")
    body(doc,
         "5.7 now additionally requires: search Purpose and Scope sections specifically for "
         "the document’s OWN standard code (e.g., an AAC.1 document searched for "
         "‘AAC.1’), not just foreign-standard codes. A same-standard code reference "
         "in Purpose/Scope is now also a Rule 2.5 violation per the updated rule above, not an "
         "acceptable internal pointer – internal pointers belong only inside body prose as "
         "‘Section 5.3’-style references, never in Purpose or Scope.")

    # ── CHECK 5.8 — EXTENDED in v1.8 ──────────────────────────────────
    h2(doc, "5.8 – References / Rule 2.8 audit (Pattern I) [extended v1.8]")
    body(doc,
         "Search for ‘internal document’ (or similar) inside the References section "
         "specifically. It should never appear there. Confirm References contains only the NABH "
         "Guidebook citation and any genuinely named external law/standard.")
    body(doc,
         "Additionally — mandatory explicit pattern search [NEW v1.8]: Search every "
         "References section for the exact string “Guidebook interpretation supplied "
         "for” (and close variants such as “supplied for [CODE].a through "
         "[CODE].[letter]” or “…supplied for [CODE].[letter]-[letter]”). "
         "This is a confirmed recurring generator artefact — an internal build note "
         "describing what source material was given to the drafting tool, not a real external "
         "citation. It has no value as a reference entry and must never be retained in a "
         "document a hospital or assessor reads.")
    body(doc,
         "Confirmed history of this artefact: first found and removed from AAC.9-13; "
         "independently found again across all 20 COP documents (COP.1-20), confirming it is "
         "not chapter-specific and not fixed by cleaning one chapter. Any document found with "
         "this pattern must have the line deleted from References. Do not assume it is absent "
         "in a chapter simply because a previous chapter was cleaned — each chapter’s "
         "References section must be searched independently on every audit pass.")

    h2(doc, "5.9 – CORE/asterisk inline-sentence audit (Pattern C)")
    body(doc,
         "Search for phrases like ‘is a CORE element,’ ‘is an asterisked "
         "element,’ ‘core objective element’ inside the body prose (not the "
         "Traceability table). None should appear.")

    h2(doc, "5.10 – Fabricated-frequency audit (Pattern G)")
    body(doc,
         "Search for frequency/interval words (annually, quarterly, monthly, every year, X "
         "days, X hours) anywhere in the document. For each hit, confirm it traces to an actual "
         "number stated in the OE or Guidebook Interpretation text – not a dump’s "
         "illustrative commentary, and not something invented to fill a template field. The one "
         "universal exception is the fixed disclaimer’s own ‘reviewed at least once "
         "every year’ boilerplate line, which is administrative housekeeping applied "
         "identically to every document, not a sourced NABH requirement.")
    body(doc,
         "5.10 now additionally requires: for every time value that passes the existing "
         "fabrication check (i.e., it IS a real, intentional number, not an obvious "
         "fabrication), confirm a citation for that exact value exists in the standard’s "
         "References section – either the existing NABH Guidebook citation (if NABH states "
         "the number) or a named external source (if adopted per Rule 2.9/2.10). A time value "
         "with no traceable citation anywhere in the document, even if not fabricated-looking, "
         "is a Rule 2.10 violation and must be flagged.")

    h2(doc, "5.11 – Stop-work tagging audit (Pattern E)")
    body(doc,
         "For any standard with a Stop-work section, check the Traceability table’s "
         "‘Where addressed’ column OE by OE. Only the specific OEs confirmed to "
         "trigger stop-work in the source should carry the stop-work reference. Every other OE "
         "in that standard should show only its normal Section 5 subsection reference.")

    h2(doc, "5.12 – Template boilerplate audit (Pattern F, Rule 2.7)")
    body(doc,
         "Search for ‘Do not skip:’ followed by what looks like a restated OE "
         "sentence, and for ‘Method note’ or similar internal-build-artefact labels. "
         "None should appear.")

    h2(doc, "5.13 – Paragraph style / structure check")
    body(doc,
         "Open the docx’s underlying XML (or use a script) and confirm: the title uses "
         "the Title style (not Heading 1 or bold Normal text), top-level sections use Heading "
         "1, subsections use Heading 2. Don’t trust how it looks rendered – verify "
         "the actual style object.")

    h2(doc, "5.14 – Visual render check")
    body(doc,
         "Convert the docx to PDF/images and look at it. Specifically check: the Document "
         "Control table, the Traceability table (does the Level column show the right "
         "CORE/Commitment/Achievement/Excellence/asterisk value per OE?), the staff sign-off "
         "table (does it render as a real multi-row table, not a single-person block?), and "
         "the Disclaimer.")

    h2(doc, "5.15 – Open the real file in Word (Pattern H – not optional)")
    body(doc,
         "A text-extraction pass and even a rendered-PDF check can both pass a file that is "
         "still broken – the IMS non-negotiables double-numbering bug did exactly this. "
         "Before treating any batch of files as final, open at least one or two of them in "
         "actual Microsoft Word and read them like a human would. Look specifically at "
         "numbered/bulleted lists for doubling, and confirm there are no compatibility warnings "
         "on open.")

    h2(doc, "5.16 – Confirm before committing")
    body(doc,
         "Only after every check above passes should a file move toward being staged and "
         "committed. If any check fails, fix and re-run all of the checks – not just the "
         "one that failed – since a fix can introduce a new problem elsewhere (as happened "
         "when the first ‘Internal documents’ fix attempt in one chapter left a "
         "different chapter’s version of the same bug unfixed).")

    h2(doc, "5.17 – Verified-practice source audit [extended v1.5]")
    body(doc, "For any standard where a number/frequency was filled per Rule 2.9, confirm:")
    bullets(doc, [
        "The external source is named in-line in the policy text (not just in References).",
        "The link in References is live and actually supports the stated number – fetch "
        "and check it, don’t assume.",
        "The phrasing doesn’t claim or imply NABH mandates it.",
        "The source is a real, checkable, professional/international body’s guidance "
        "– not a blog, forum, or unverifiable page.",
    ])
    body(doc,
         "5.17 now additionally requires, for every external Reference URL in every document: "
         "actually fetch the URL’s live content – Claude Code has confirmed "
         "web-fetch capability in this environment; use it, and do not defer to ‘needs "
         "manual verification.’ Extract the fetched page’s real title, publisher, "
         "and what it actually says. Compare that against what the document’s citation "
         "claims it supports. A mismatch – wrong body, wrong topic, a withdrawn or "
         "cancelled study, a dead link, or content that does not address the specific number "
         "or practice being cited – is a confirmed Rule 2.9/2.10 violation to report and "
         "fix, not a flag to defer.")

    h2(doc, "5.18 – Undefined shorthand audit [NEW v1.6]")
    body(doc,
         "For every compound or shorthand term used in the document as if self-explanatory "
         "(e.g., a hyphenated noun phrase like ‘temporary-holding over-run’ or "
         "‘priority-flag lapse’), confirm that the term was defined in plain language "
         "at its first occurrence in the same document. A shorthand term used before its "
         "definition, or never defined at all, is a Rule 2.5d violation. Flag it and either "
         "replace the bare label with the full concept at each point of use, or insert the "
         "definition at first occurrence.")

    h2(doc, "5.19 – Deferred-definition audit [NEW v1.6]")
    body(doc,
         "For every ‘the organisation’s defined [X]’ or similar deferral phrase "
         "found in the document, confirm the sentence also names where that definition lives "
         "– a specific SOP, a named role responsible for maintaining it, or a "
         "cross-reference to a real governance document. A deferral with no named home is a "
         "Rule 2.5e violation. Fix it by adding the home (e.g., ‘as defined by the "
         "Quality Coordinator in the Incident Management SOP’), or – if no "
         "governance document for it currently exists – flag it as a gap for the "
         "organisation to fill before the policy is finalised.")

    h2(doc, "5.20 – Dead reference audit [NEW v1.7]")
    body(doc,
         "For every “refer to,” “see,” or similar pointer phrase in the "
         "document, confirm the referenced resource is either:")
    bullets(doc, [
        "present in this same document (an actual Glossary section, an Appendix, a named "
        "table that exists in the rendered file), or",
        "named precisely enough for the reader to locate it independently — a specific "
        "document title, section number, page reference, or URL.",
    ])
    body(doc,
         "A pointer that satisfies neither condition — e.g., “refer to the "
         "Glossary” when no glossary exists in the document and no glossary is named as "
         "a findable external source — is a dead pointer (Rule 2.5f violation). Fix by "
         "either including the referenced content at the point of use or replacing the bare "
         "reference with a precise locator (e.g., “see the NABH Guidebook to "
         "Accreditation Standards for Hospitals, 6th Edition, Glossary of Terms”).")
    body(doc,
         "This check applies to every document regardless of chapter. Pointer phrases to "
         "search for include: “refer to the Glossary,” “see Appendix,” "
         "“refer to the policy on,” “as defined in the attached table,” "
         "“see the list below” (where no list follows), “see Section” "
         "(where the named section does not exist), and similar constructions.")

    # ── Section 6 ─────────────────────────────────────────────────────
    h1(doc, "Section 6 – Git Discipline")
    bullets(doc, [
        "Every session, first thing, in a new cmd/PowerShell window (not the Claude Code "
        "bash-hook terminal, which has a known non-blocking rtk: command not found error that "
        "makes its own git output untrustworthy to read past): git fetch then "
        "git log -1 --oneline .",
        "Git commands run one at a time, never chained with &&, when typed directly into cmd "
        "by a person.",
        "Never git add . – Stage explicit file lists only.",
        "After staging, always run git status --short (full output, not a collapsed pane) and "
        "confirm the staged file list exactly matches intent before committing. This has caught "
        "real discrepancies more than once – a tool’s own narrated summary of "
        "‘what’s staged’ is not verification; check the actual git status output.",
        "When a file already exists on master and a fix touches it, do not assume M in git "
        "status means real content changed. Diff the actual document.xml (or equivalent) "
        "between the committed version and the working copy. If the diff is empty, it’s "
        "container noise (a real, repeated finding in this project – COP.1-6, PSQ.1, and "
        "HRM.1-5 all showed this at different points) and should not be re-staged. If the diff "
        "is non-empty, it’s a real change and belongs in the commit.",
        "A plain local git commit is a low-stakes, reversible action. Verify the staged file "
        "list once or twice, then commit – don’t loop indefinitely re-checking a "
        "reversible step.",
        "Instructions meant for an agentic coding tool (plain-English task descriptions) should "
        "never be handed to a person to type directly into a raw cmd window – they fail as "
        "unrecognized commands. Give literal, paste-ready shell commands for direct typing; "
        "plain-English task descriptions only when relayed through the coding tool itself.",
    ])

    # ── Section 7 ─────────────────────────────────────────────────────
    h1(doc, "Section 7 – Official Chapter and Standard Counts")
    body(doc,
         "Per the NABH 6th Edition Guidebook’s own ‘Summary of Chapters, Standards "
         "and Objective Elements’ table. Verify against a chapter’s actual Guidebook "
         "page before drafting – this project has miscounted before.")
    bullets(doc, [
        "AAC: 13 standards",
        "COP: 20 standards",
        "MOM: 11 standards",
        "PRE: 8 standards",
        "IPC: 8 standards",
        "PSQ: 7 standards",
        "ROM: 6 standards",
        "FMS: 7 standards",
        "HRM: 13 standards",
        "IMS: 7 standards",
        "Total: 100 standards",
    ])
    body(doc,
         "A chapter’s docx file existing on disk is not the same as that chapter being "
         "verified. Track three separate states per chapter: built (a docx exists), "
         "mechanically fixed (got a References-line or similar automated pass), and audited "
         "(went through the full Verification Loop in Section 5 against real source pages). "
         "Only the third state should be reported as ‘done’ without a caveat.")

    # ── Disclaimer ────────────────────────────────────────────────────
    h1(doc, "Disclaimer")
    body(doc,
         "This document is an internal working reference compiled for the AccredReady / HCO "
         "Full v2 policy rewrite project. It consolidates the project’s original rulebook "
         "with defects and patterns found and fixed during actual drafting work. It is not "
         "itself an NABH publication and creates no accreditation obligation on its own – "
         "the authoritative source for any standard’s content remains the real NABH HCO "
         "Full Accreditation 6th Edition Standards and Guidebook.")

    # ── Save DOCX ─────────────────────────────────────────────────────
    doc.save(OUT_DOCX)
    print(f"DOCX saved: {OUT_DOCX}")

    # ── Convert to PDF ────────────────────────────────────────────────
    try:
        from docx2pdf import convert
        convert(OUT_DOCX, OUT_PDF)
        print(f"PDF saved: {OUT_PDF}")
    except Exception as e:
        print(f"PDF conversion error: {e}")
        print("Manual step: open the DOCX in Word and export as PDF.")

    # ── Verify paragraph count ─────────────────────────────────────────
    verify_doc = Document(OUT_DOCX)
    print(f"\nVerification: {len(verify_doc.paragraphs)} paragraphs in DOCX")
    print("Checking Check 5.8 extended text is present...")
    found_58 = False
    found_artefact = False
    for p in verify_doc.paragraphs:
        if "5.8" in p.text and "extended v1.8" in p.text:
            found_58 = True
        if "Guidebook interpretation supplied for" in p.text:
            found_artefact = True
    print(f"  Check 5.8 heading with '[extended v1.8]': {'FOUND' if found_58 else 'MISSING'}")
    print(f"  'Guidebook interpretation supplied for' pattern text: {'FOUND' if found_artefact else 'MISSING'}")
    print("\nDone.")


if __name__ == "__main__":
    build()
