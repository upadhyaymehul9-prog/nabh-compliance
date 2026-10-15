# -*- coding: utf-8 -*-
"""Rebuilds the 6 existing ROM SOPs (ROM.1.a, ROM.1.b, ROM.1.e, ROM.3.d,
ROM.4.a, ROM.4.c) in the plain-body + audit-appendix format approved for
FMS.2 (2026-10-12), and now completed across the whole FMS chapter.

Unlike FMS, ROM has no build script -- each SOP was hand-built once and
only the .docx was committed (confirmed via git log, 2026-10-10 onward).
So this script does not transform a ProcedureBlock/SOPSpec the way
build_fms*_sop.py does: it is a fresh SOPSpecV2 per SOP, with every fact,
citation and URL read directly off the live committed .docx (dumped via
python-docx, including its hyperlink relationships) on 2026-10-12. No new
citation or number is introduced beyond what each live SOP already cites.

These are single-OE SOPs (not a-g ranges like FMS), so each one's "items"
are its own internal procedural steps (4.1-4.4), not separate objective
elements -- all four carry the same OE code in the appendix.

Writes over the existing committed paths in place; does not touch Records.

ROM.2 (added 2026-10-14) closes a real gap found by Mk live on the site:
the whole standard (OEs a-d -- administrative head qualifications,
experience, applicable-legislation compliance, and performance review)
had a master policy drafted back on 2026-08-17 but no SOP/Record pair was
ever built for it -- the only ROM standard left with nothing. Unlike
ROM.1, this is written as one combined SOP covering all four OEs (the
newer convention used by COP/HRM/MOM/PRE), since all four OEs concern the
same person and a single appointment-to-review cycle, not four
independent procedures. Three Records close it out: qualification/
experience verification at appointment, the applicable-legislation
register, and the leader performance-review record. This script now also
builds those records and rewrites manifest.json (merging, not replacing,
the existing ROM.1/3/4 entries already in it).
"""
from __future__ import annotations

import json
from pathlib import Path

from sop_record_common import PlainItem, RecordSpec, SOPSpecV2, build_record, build_sop_v2

OUT_ROOT = Path(__file__).parent / "sop_record_masters" / "ROM"
RECORDS_ROOT = OUT_ROOT / "Records"

NABH_ROM_CITE = (
    "National Accreditation Board for Hospitals and Healthcare Providers. (2022). "
    "Standards for Small Healthcare Organisations (3rd ed.). [NABH SHCO Accreditation "
    "Programme page](https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/). "
    "Responsibilities of Management chapter, standard {code}."
)

# --------------------------------------------------------------- ROM.1.a ---
ROM1A = SOPSpecV2(
    sop_no="SOP-ROM.1.a",
    title="Identification of Governance Roles and Responsibilities",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» identifies who is "
        "responsible for governance, documents each role holder's "
        "designation and responsibilities, and manages a vacancy without a "
        "gap in accountability -- so governance is written down, not "
        "assumed, at every point including a transition."
    ),
    purpose_trigger=(
        "A board member resigns with no notice. Without this SOP, nobody "
        "is sure who's accountable for governance decisions in the gap -- "
        "with it, the governing body designates an interim holder before "
        "the register even needs updating."
    ),
    purpose_why=(
        "We do this because governance that exists only as an informal "
        "understanding of who's in charge can't be checked, handed over, "
        "or held accountable when something goes wrong. Writing it down is "
        "what makes governance real instead of assumed."
    ),
    purpose_text=(
        "To define how «Hospital Name» identifies who is responsible for "
        "governance, documents each role holder's designation and "
        "responsibilities, and manages a governance-role vacancy without a "
        "gap in accountability."
    ),
    scope_why=(
        "so department and service heads actually know who they report to "
        "for governance decisions -- not just the governing body itself."
    ),
    scope_text=(
        "Applies to the governing body and the Medical Superintendent, and "
        "to department and service heads who need to understand the "
        "reporting lines it produces."
    ),
    responsibility_why=(
        "a governance register nobody actually maintains or checks drifts "
        "out of date within months -- naming who holds it and who audits "
        "it is what keeps it true."
    ),
    responsibilities=[
        ("Medical Superintendent",
         "Holds and keeps current the governance register, communicates "
         "the governance structure to department and service heads, and "
         "flags a vacancy to the governing body immediately."),
        ("Governing Body",
         "Confirms each role holder's designation and documented "
         "responsibilities, signs off any change, and designates an "
         "interim holder when a role becomes vacant."),
        ("Quality Coordinator", "Audits the register quarterly for currency."),
    ],
    items=[
        PlainItem(
            heading="Identify and register each governance role",
            why=(
                "Governance that exists only as an informal understanding "
                "of who's in charge can't be checked, handed over, or held "
                "accountable -- writing it down is what makes it real."
            ),
            body=[
                "The Medical Superintendent lists every person "
                "responsible for governance -- owners, board members, "
                "trustees or equivalent -- by name and designation.",
                "Each role holder's documented responsibilities are "
                "recorded against their entry in the governance register.",
                "The governing body confirms the register is accurate and "
                "complete.",
            ],
            oe_code="ROM.1.a",
        ),
        PlainItem(
            heading="Communicate the structure",
            why=(
                "A governance register nobody below the top knows about "
                "doesn't change how decisions actually get made day to "
                "day -- department heads have to know who is actually "
                "accountable for what."
            ),
            body=[
                "The Medical Superintendent communicates the governance "
                "structure and reporting lines to department and service "
                "heads.",
                "Department heads confirm they understand who is "
                "accountable for governance decisions that affect their "
                "area.",
            ],
            oe_code="ROM.1.a",
        ),
        PlainItem(
            heading="Manage a vacancy without a gap",
            why=(
                "A governance role left silently vacant -- after a "
                "resignation, incapacitation, or removal -- leaves a real "
                "accountability gap exactly where the register claims "
                "none exists."
            ),
            body=[
                "When a governance role becomes vacant, the Medical "
                "Superintendent notifies the governing body within "
                "«the hospital-defined notification period».",
                "The governing body designates an interim role holder, or "
                "reassigns the responsibilities on an interim basis, "
                "before the register is updated to show the role as "
                "filled.",
                "A permanent appointment, once made, is recorded in the "
                "register the same way as any other entry, closing out "
                "the interim period.",
            ],
            oe_code="ROM.1.a",
        ),
        PlainItem(
            heading="Review and update",
            why=(
                "A register that was accurate on the day it was written "
                "but never updated again is exactly how an accreditation "
                "assessor finds a governance role that no longer matches "
                "who is actually there."
            ),
            body=[
                "The governance register is reviewed at least annually, "
                "or immediately when a governance role changes.",
                "The Quality Coordinator confirms, during the quarterly "
                "audit, that the register is current.",
            ],
            oe_code="ROM.1.a",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the ROM.1 Records folder).",
    related_documents=[
        "Policy on Governance — Roles, Responsibilities and Ethical Management (ROM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if the "
        "quarterly audit finds the register out of date, or a vacancy is "
        "handled outside this SOP."
    ),
    full_reference_list=[NABH_ROM_CITE.format(code="ROM.1")],
)

# --------------------------------------------------------------- ROM.1.b ---
ROM1B = SOPSpecV2(
    sop_no="SOP-ROM.1.b",
    title="Vision, Mission, Values and Public Display",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» establishes its vision, "
        "mission and values, makes them public, confirms staff can "
        "actually relate them to their daily work, and corrects the gap "
        "when a refresher finds a staff member cannot -- not just that a "
        "poster exists."
    ),
    purpose_trigger=(
        "A new housekeeping staff member is asked at her annual refresher "
        "what the hospital's mission means for her work, and can't answer. "
        "This SOP is what gets her one-to-one coaching and a re-test -- "
        "not a quiet pass/fail note that changes nothing."
    ),
    purpose_why=(
        "We do this because a mission statement only matters if the "
        "people living it every day actually understand what it means for "
        "their own work. A poster on a wall doesn't change how someone "
        "treats a patient -- genuine understanding does."
    ),
    purpose_text=(
        "To define how «Hospital Name» establishes its vision, mission and "
        "values, makes them public, confirms staff can relate them to "
        "their daily work, and corrects the gap where a refresher finds a "
        "staff member cannot."
    ),
    scope_why=(
        "so every staff member -- not just clinical leadership -- is "
        "actually expected to know and explain the mission, since it's "
        "meant to shape everyone's daily work."
    ),
    scope_text=(
        "Applies to the governing body, the Medical Superintendent, and "
        "every staff member who is expected to know and explain the "
        "mission."
    ),
    responsibility_why=(
        "a vision statement nobody owns stays a draft, and a staff member "
        "who can't explain it gets no follow-up unless someone is named to "
        "arrange the coaching."
    ),
    responsibilities=[
        ("Governing Body", "Lays down and approves the vision, mission and values."),
        ("Medical Superintendent",
         "Confirms the current version is displayed, that staff can "
         "explain it at induction and annual refresher, and arranges "
         "remedial coaching where a staff member cannot."),
    ],
    items=[
        PlainItem(
            heading="Lay down and approve",
            why=(
                "A vision and mission nobody formally approved is just a "
                "draft -- governance ownership is what turns it into the "
                "organisation's actual stated purpose."
            ),
            body=[
                "The governing body drafts and approves the vision, "
                "mission and values statement, in writing.",
                "The approved statement is signed and dated.",
            ],
            oe_code="ROM.1.b",
            technical_sources=[
                "International Organization for Standardization. (2026). "
                "[ISO 9001:2026, Quality management systems — "
                "Requirements](https://www.iso.org/standard/88464.html), "
                "clause 5.2 (Quality Policy). External benchmark for top "
                "management establishing and communicating organisational "
                "direction; SHCO accreditation does not itself require "
                "ISO 9001 certification.",
            ],
        ),
        PlainItem(
            heading="Display it publicly",
            why=(
                "A vision, mission and values statement kept in a file "
                "nobody sees fails the point of having one -- it has to be "
                "visible where patients, families and staff actually "
                "encounter it."
            ),
            body=[
                "The current statement is displayed at «the main "
                "entrance, reception and each patient-care area», in "
                "«Hindi and English».",
                "The Medical Superintendent confirms the displayed "
                "version matches the currently approved one, and logs the "
                "confirmation.",
            ],
            oe_code="ROM.1.b",
        ),
        PlainItem(
            heading="Confirm staff can explain it",
            why=(
                "A staff member who can't explain the mission in their "
                "own words hasn't actually been told what it means for "
                "their work -- a poster they walk past isn't the same as "
                "understanding it."
            ),
            body=[
                "Induction covers the vision, mission and values, "
                "including what they mean for the specific role.",
                "An annual refresher confirms staff can still explain the "
                "mission in their own words.",
                "A poster alone, with no induction or refresher coverage, "
                "doesn't satisfy this.",
            ],
            oe_code="ROM.1.b",
        ),
        PlainItem(
            heading="Correct the gap when someone can't explain it",
            why=(
                "Finding that a staff member can't explain the mission "
                "and simply noting it as a pass/fail result, with no "
                "follow-up, leaves the actual gap unaddressed."
            ),
            body=[
                "Where the annual refresher finds a staff member cannot "
                "explain the mission in their own words, the Medical "
                "Superintendent arranges one-to-one coaching within a "
                "defined period.",
                "The staff member is re-tested after coaching, and the "
                "outcome is logged.",
            ],
            oe_code="ROM.1.b",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-3 (see the ROM.1 Records folder).",
    related_documents=[
        "Policy on Governance — Roles, Responsibilities and Ethical Management (ROM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if the "
        "vision, mission or values change, or a refresher repeatedly finds "
        "the same gap."
    ),
    full_reference_list=[
        NABH_ROM_CITE.format(code="ROM.1"),
        "International Organization for Standardization. (2026). [ISO 9001:2026, Quality management systems — Requirements](https://www.iso.org/standard/88464.html), clause 5.2.",
    ],
)

# --------------------------------------------------------------- ROM.1.e ---
ROM1E = SOPSpecV2(
    sop_no="SOP-ROM.1.e",
    title="Ethical Management Framework",
    purpose_plain=(
        "This SOP sets out how «Hospital Name»'s governance supports an "
        "ethical management framework that is actually operated and "
        "reviewed, including an option to report anonymously and a "
        "documented protection against retaliation -- a working reporting "
        "mechanism and a review cycle, not a display-only document."
    ),
    purpose_trigger=(
        "A junior staff member suspects a senior colleague of a conflict "
        "of interest but is afraid to put their name to it. This SOP is "
        "what lets them report anonymously, and what protects them if they "
        "chose to give their name and later face retaliation for it."
    ),
    purpose_why=(
        "We do this because an ethical concern that nobody feels safe "
        "reporting stays invisible until it causes real harm -- to a "
        "patient, to the organisation, or to the person who stayed quiet. "
        "A genuine, protected way to report is what keeps that from "
        "happening."
    ),
    purpose_text=(
        "To define how «Hospital Name»'s governance supports an ethical "
        "management framework that is actually operated and reviewed, "
        "including an anonymous reporting option and documented protection "
        "against retaliation."
    ),
    scope_why=(
        "so any staff member or governance member who has an ethical "
        "concern -- not just governance itself -- knows this is theirs to "
        "use."
    ),
    scope_text=(
        "Applies to the governing body, the Medical Superintendent, and "
        "any staff member who reports an ethical concern."
    ),
    responsibility_why=(
        "a conflict of interest that's never declared is invisible to the "
        "organisation until it causes a problem -- naming who owns the "
        "declaration register and who investigates retaliation is what "
        "catches it before then."
    ),
    responsibilities=[
        ("Governing Body",
         "Supports the framework, reviews ethical compliance at least "
         "annually and whenever a concern is reported, and investigates "
         "any allegation of retaliation against a reporter."),
        ("Medical Superintendent",
         "Is accountable for operating within the framework day to day "
         "and maintains the conflict-of-interest declaration register."),
    ],
    items=[
        PlainItem(
            heading="Establish the framework",
            why=(
                "A framework that is only a code of ethics on a wall, "
                "with no declaration process and no way to report a "
                "concern, is a display -- not a framework that manages "
                "anything."
            ),
            body=[
                "The framework has four required parts:",
                "1. A written code of ethics.",
                "2. A conflict-of-interest declaration process for every "
                "governance member.",
                "3. A mechanism for reporting ethical concerns, including "
                "an option to report anonymously.",
                "4. A review of ethical compliance, at least annually.",
                "The governing body approves the framework in writing.",
            ],
            oe_code="ROM.1.e",
            technical_sources=[
                "National Medical Commission (formerly Medical Council of "
                "India). (2002, amended 2016). [Indian Medical Council "
                "(Professional Conduct, Etiquette and Ethics) Regulations, "
                "2002](https://www.nmc.org.in/rules-regulations/code-of-medical-ethics-regulations-2002/1000/). Statutory backdrop a hospital's own ethical-management "
                "framework operates alongside; it does not itself require "
                "the governance-level framework this standard asks for.",
            ],
        ),
        PlainItem(
            heading="Collect and maintain conflict-of-interest declarations",
            why=(
                "A conflict of interest that is never declared cannot be "
                "managed -- it's invisible to the organisation until it "
                "causes a problem, which is exactly what the declaration "
                "process exists to prevent."
            ),
            body=[
                "Every governance member declares any conflict of "
                "interest in writing at appointment and refreshes the "
                "declaration at least annually.",
                "A declared conflict is reviewed by the governing body "
                "and a management action (recusal from the relevant "
                "decision, disclosure, etc.) is recorded.",
            ],
            oe_code="ROM.1.e",
        ),
        PlainItem(
            heading="Operate the reporting mechanism, including anonymous reports",
            why=(
                "A reporting mechanism nobody has ever used cannot be "
                "shown to actually work -- and a mechanism that requires "
                "a name discourages exactly the reports most worth "
                "having, from someone worried about retaliation."
            ),
            body=[
                "Any staff member or governance member can report an "
                "ethical concern through the documented mechanism, by "
                "name or anonymously.",
                "Each concern is logged with the date received, the "
                "nature of the concern, and the action taken, regardless "
                "of whether the reporter identified themselves.",
                "Any allegation that a reporter faced retaliation for "
                "raising a concern is investigated directly by the "
                "governing body, separately from the original concern.",
            ],
            oe_code="ROM.1.e",
        ),
        PlainItem(
            heading="Review annually",
            why=(
                "A framework that is approved once and never checked "
                "again drifts into being exactly the display-only "
                "document this requirement exists to rule out."
            ),
            body=[
                "The governing body reviews ethical compliance at least "
                "annually, and immediately whenever a concern is "
                "reported.",
                "Conflict-of-interest declarations are refreshed as part "
                "of the annual review.",
            ],
            oe_code="ROM.1.e",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-3 (see the ROM.1 Records folder).",
    related_documents=[
        "Policy on Governance — Roles, Responsibilities and Ethical Management (ROM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if an "
        "ethical concern -- or a retaliation allegation -- reveals a gap "
        "in the framework."
    ),
    full_reference_list=[
        NABH_ROM_CITE.format(code="ROM.1"),
        "National Medical Commission (formerly Medical Council of India). (2002, amended 2016). [Indian Medical Council (Professional Conduct, Etiquette and Ethics) Regulations, 2002](https://www.nmc.org.in/rules-regulations/code-of-medical-ethics-regulations-2002/1000/).",
    ],
)

# --------------------------------------------------------------- ROM.3.d ---
ROM3D = SOPSpecV2(
    sop_no="SOP-ROM.3.d",
    title="Measurable Service Standards",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» documents service standards "
        "that are genuinely measurable, monitors them, and escalates a "
        "standard that keeps missing its target instead of letting routine "
        "corrective action repeat itself indefinitely."
    ),
    purpose_trigger=(
        "A ward's patient-wait-time standard has been missed for three "
        "quarters running, with a fresh corrective action each time that "
        "never actually fixes it. This SOP is what escalates it to the "
        "governing body for a structural review instead of a fourth "
        "routine fix that won't work either."
    ),
    purpose_why=(
        "We do this because a standard that can't actually be measured, "
        "or that's measured but never acted on, gives patients and staff "
        "no real guarantee of anything -- it's just a sentence on a wall. "
        "A standard that's genuinely tracked, and genuinely fixed when it "
        "fails, is what makes 'good service' more than a slogan."
    ),
    purpose_text=(
        "To define how «Hospital Name» documents service standards that "
        "are genuinely measurable, monitors them, and escalates a standard "
        "that keeps missing its target instead of letting routine "
        "corrective action repeat itself indefinitely."
    ),
    scope_why=(
        "so every department that owns a service standard knows this is "
        "the process that applies to them, and knows exactly when a missed "
        "target stops being their problem alone to fix."
    ),
    scope_text=(
        "Applies to the Quality Coordinator, the Medical Superintendent, "
        "and every department or service head who owns a service "
        "standard."
    ),
    responsibility_why=(
        "a standard that nobody compiles data for, or that nobody escalates "
        "when it keeps failing, just repeats the same miss quarter after "
        "quarter with nothing actually changing."
    ),
    responsibilities=[
        ("Quality Coordinator",
         "Compiles service-standard data quarterly, presents it to the "
         "Medical Superintendent, and flags any standard missed for "
         "three consecutive cycles."),
        ("Department / Service Heads",
         "Define and monitor service standards within their own area."),
        ("Medical Superintendent",
         "Ensures standards that are not met trigger root-cause analysis "
         "and corrective action, and escalates a repeatedly-missed "
         "standard to the governing body."),
    ],
    items=[
        PlainItem(
            heading="Define a measurable standard",
            why=(
                "A standard that just says 'good patient care' can never "
                "be checked against anything -- it has to name an "
                "indicator, a target, where the data comes from, and how "
                "often it's checked before it counts as measurable."
            ),
            body=[
                "Each department or service defines its service standards. "
                "Each standard states four things:",
                "1. The indicator being measured.",
                "2. The target.",
                "3. The data source.",
                "4. How often it is monitored.",
                "A standard that cannot be measured is replaced with one "
                "that can, rather than kept on the books unmeasured.",
            ],
            oe_code="ROM.3.d",
        ),
        PlainItem(
            heading="Monitor and compile quarterly",
            why=(
                "A measurable standard that is never actually measured is "
                "functionally identical to one that was never defined -- "
                "monitoring is what makes the definition mean anything."
            ),
            body=[
                "The Quality Coordinator compiles service-standard data "
                "quarterly across all departments and services.",
                "The compiled data is presented to the Medical "
                "Superintendent.",
            ],
            oe_code="ROM.3.d",
            technical_sources=[
                "International Organization for Standardization. (2026). "
                "[ISO 9001:2026, Quality management systems — "
                "Requirements](https://www.iso.org/standard/88464.html), "
                "clause 9.1 (Monitoring, measurement, analysis and "
                "evaluation). External benchmark for how measured "
                "performance data should be compiled and reviewed; SHCO "
                "accreditation does not itself require ISO 9001 "
                "certification.",
            ],
        ),
        PlainItem(
            heading="Act on standards not met",
            why=(
                "A missed standard with no follow-up just repeats itself "
                "quarter after quarter -- root-cause analysis is what "
                "turns a missed number into an actual fix."
            ),
            body=[
                "A standard that is not met triggers root-cause analysis "
                "and a corrective action.",
                "Service standards are reviewed at least annually, or "
                "when a service changes.",
            ],
            oe_code="ROM.3.d",
        ),
        PlainItem(
            heading="Escalate a standard missed repeatedly",
            why=(
                "A standard that fails quarter after quarter, with a "
                "fresh root-cause analysis each time that never actually "
                "fixes it, isn't a monitoring problem any more -- it's a "
                "structural one that routine fixes at department level "
                "aren't equipped to solve."
            ),
            body=[
                "A service standard missed for three consecutive "
                "monitoring cycles is escalated by the Quality "
                "Coordinator to the Medical Superintendent and the "
                "governing body for structural review, rather than a "
                "fourth routine fix.",
                "The governing body's review considers whether the "
                "target itself, the resourcing behind it, or the process "
                "it measures needs to change.",
            ],
            oe_code="ROM.3.d",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-3 (see the ROM.3 Records folder).",
    related_documents=[
        "Policy on Strategic Plans, Operational Plans, Committees, Service Standards and Staff Rights (ROM.3)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if a "
        "service standard proves unmeasurable in practice, or is "
        "escalated under the repeated-miss step."
    ),
    full_reference_list=[
        NABH_ROM_CITE.format(code="ROM.3"),
        "International Organization for Standardization. (2026). [ISO 9001:2026, Quality management systems — Requirements](https://www.iso.org/standard/88464.html), clause 9.1.",
    ],
)

# --------------------------------------------------------------- ROM.4.a ---
ROM4A = SOPSpecV2(
    sop_no="SOP-ROM.4.a",
    title="Proactive Risk Management",
    purpose_plain=(
        "This SOP sets out how «Hospital Name»'s management maintains and "
        "reviews a risk register across clinical, operational, financial "
        "and compliance domains, including escalating a high-severity risk "
        "immediately rather than holding it for the next scheduled "
        "review, so risk is managed proactively as a management "
        "responsibility."
    ),
    purpose_trigger=(
        "A department head spots a structural defect that could cause "
        "real harm if it fails. This SOP is what gets it to the Medical "
        "Superintendent the same day, not logged for the next quarterly "
        "meeting three months away."
    ),
    purpose_why=(
        "We do this because a risk that's known about but sits unescalated "
        "until the next scheduled review is a risk that's had months to "
        "turn into actual harm. Acting the same a risk is identified, not "
        "when it's convenient to discuss it, is what keeps this "
        "proactive instead of reactive."
    ),
    purpose_text=(
        "To define how «Hospital Name»'s management maintains and reviews "
        "a risk register across clinical, operational, financial and "
        "compliance domains, including escalating a high-severity risk "
        "immediately rather than holding it for the next scheduled review."
    ),
    scope_why=(
        "so every department head who spots a risk -- not just the "
        "Medical Superintendent -- knows this is theirs to raise, and "
        "knows a serious one doesn't wait for a meeting."
    ),
    scope_text=(
        "Applies to the Medical Superintendent, the governing body, and "
        "every department or service head who identifies and escalates "
        "risks."
    ),
    responsibility_why=(
        "a risk that only gets mentioned once in a meeting and never "
        "written down isn't being managed at all -- naming who holds the "
        "register and who must act immediately on a severe one is what "
        "keeps a risk from being forgotten."
    ),
    responsibilities=[
        ("Medical Superintendent",
         "Maintains the risk register, reviews it quarterly, and acts "
         "immediately on any risk flagged as high-severity rather than "
         "waiting for the quarterly cycle."),
        ("Governing Body",
         "Reviews the risk-management programme half-yearly, and is "
         "notified immediately of any high-severity risk."),
        ("Department / Service Heads",
         "Identify and escalate risks within their area to the risk "
         "register, flagging a high-severity risk for immediate "
         "escalation rather than routine logging."),
    ],
    items=[
        PlainItem(
            heading="Identify and register risks",
            why=(
                "A risk that exists only as something a department head "
                "mentioned once in a meeting is not being managed -- it "
                "has to be written down, with a likelihood, an impact, "
                "and someone responsible for it."
            ),
            body=[
                "Department and service heads identify and escalate "
                "risks across clinical, operational, financial and "
                "compliance domains.",
                "Each risk entry records six things:",
                "1. The risk itself, in plain words.",
                "2. Its likelihood.",
                "3. Its impact.",
                "4. The mitigation action.",
                "5. The person responsible for it.",
                "6. The review date.",
            ],
            oe_code="ROM.4.a",
            technical_sources=[
                "International Organization for Standardization. (2018). "
                "[ISO 31000:2018, Risk management — "
                "Guidelines](https://www.iso.org/standard/65694.html). "
                "Internationally recognised framework for identifying, "
                "rating and treating risk that the register fields "
                "follow; SHCO accreditation does not itself require ISO "
                "31000 certification.",
            ],
        ),
        PlainItem(
            heading="Escalate a high-severity risk immediately",
            why=(
                "A newly identified risk with a high likelihood and a "
                "severe impact -- a structural defect, an equipment "
                "failure that could harm a patient -- cannot wait for the "
                "next quarterly meeting to be acted on; holding it for "
                "the scheduled cycle turns proactive risk management into "
                "reactive paperwork."
            ),
            body=[
                "A risk rated high likelihood and high (or severe) "
                "impact is escalated by the identifying department head "
                "to the Medical Superintendent the same day, not logged "
                "for the next quarterly review.",
                "The Medical Superintendent decides on immediate "
                "mitigating action and notifies the governing body "
                "without waiting for the half-yearly review.",
            ],
            oe_code="ROM.4.a",
        ),
        PlainItem(
            heading="Review quarterly and half-yearly",
            why=(
                "A risk register written once and never revisited stops "
                "reflecting the organisation's actual risk position "
                "within a quarter -- regular review is what keeps it "
                "proactive rather than historical."
            ),
            body=[
                "The Medical Superintendent reviews the risk register "
                "quarterly.",
                "The governing body reviews the risk-management "
                "programme half-yearly.",
            ],
            oe_code="ROM.4.a",
        ),
        PlainItem(
            heading="Connect it to the strategic plan",
            why=(
                "A risk register that never reaches the strategic plan "
                "means governance is approving plans without seeing the "
                "risks that could derail them."
            ),
            body=[
                "Risk-register items are made available to the Quality "
                "Coordinator for mapping against the strategic plan, "
                "where one has been drafted.",
            ],
            oe_code="ROM.4.a",
            boundary=[
                "Strategic-plan mapping traces to ROM.4.b, where "
                "drafted -- this step only owns that the risk data is "
                "made available to it.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the ROM.4 Records folder).",
    related_documents=[
        "Policy on Risk Management, System-Failure Reporting and Outsourced Services (ROM.4)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner after a "
        "significant risk event or a high-severity risk escalation."
    ),
    full_reference_list=[
        NABH_ROM_CITE.format(code="ROM.4"),
        "International Organization for Standardization. (2018). [ISO 31000:2018, Risk management — Guidelines](https://www.iso.org/standard/65694.html).",
    ],
)

# --------------------------------------------------------------- ROM.4.c ---
ROM4C = SOPSpecV2(
    sop_no="SOP-ROM.4.c",
    title="Internal and External Reporting of System and Process Failures",
    purpose_plain=(
        "This SOP sets out how «Hospital Name»'s management ensures "
        "systems exist, and are actually used, for reporting system and "
        "process failures internally -- including anonymously -- and, "
        "where legally required, externally to regulatory bodies, with "
        "trend analysis so a repeated failure triggers a systemic fix "
        "rather than being closed case by case indefinitely."
    ),
    purpose_trigger=(
        "The same type of medication near-miss happens for the third time "
        "this quarter, each one closed individually with no one asking why "
        "it keeps happening. This SOP is what turns that pattern into one "
        "systemic fix instead of a fourth isolated case."
    ),
    purpose_why=(
        "We do this because a failure that's mentioned informally and "
        "never logged can't be reviewed, trended, or fixed -- and closing "
        "the same type of failure over and over without asking why it "
        "keeps happening leaves the real problem in place to hurt the "
        "next patient or staff member."
    ),
    purpose_text=(
        "To define how «Hospital Name»'s management ensures systems exist, "
        "and are actually used, for reporting system and process failures "
        "internally -- including anonymously -- and, where legally "
        "required, externally to regulatory bodies, with trend analysis "
        "so a repeated failure triggers a systemic fix."
    ),
    scope_why=(
        "so any staff member who notices something going wrong -- not "
        "just the Quality Coordinator -- knows this is theirs to use, and "
        "knows they can use it without giving their name."
    ),
    scope_text=(
        "Applies to the Quality Coordinator, the Medical Superintendent, "
        "and every staff member who may need to report a system or "
        "process failure."
    ),
    responsibility_why=(
        "a report that's logged but never reviewed above the person who "
        "received it can't trigger the management attention a system "
        "failure actually needs."
    ),
    responsibilities=[
        ("Quality Coordinator",
         "Maintains the failure-reporting register, receives internal "
         "reports (including anonymous ones), and runs the periodic "
         "trend analysis."),
        ("Medical Superintendent",
         "Reviews the register monthly, presents a summary to the "
         "governing body quarterly, and opens a systemic fix when trend "
         "analysis finds a repeated failure type."),
        ("Department / Service Heads",
         "Report system and process failures through the internal "
         "reporting system."),
    ],
    items=[
        PlainItem(
            heading="Report internally, including anonymously",
            why=(
                "A failure that is mentioned informally and never logged "
                "cannot be reviewed, trended, or fixed -- and a reporting "
                "channel that requires a name discourages exactly the "
                "reports a staff member might hesitate to put their name "
                "to."
            ),
            body=[
                "Staff submit incident reports, near-miss reports and "
                "root-cause analyses to the Quality Coordinator, by name "
                "or anonymously.",
                "The Quality Coordinator logs every report in the "
                "failure-reporting register on the day it is received, "
                "regardless of whether the reporter identified "
                "themselves.",
            ],
            oe_code="ROM.4.c",
            technical_sources=[
                "World Health Organization. (2020, September 16). "
                "[Patient Safety Incident Reporting and Learning Systems: "
                "Technical Report and Guidance](https://iris.who.int/server/api/core/bitstreams/49947589-0a06-4708-8cc9-379bc8d2f9f2/content). "
                "WHO guidance on operating an incident reporting and "
                "learning system, including the value of anonymous and "
                "near-miss reporting; referenced as an external "
                "benchmark, not a mandate.",
            ],
        ),
        PlainItem(
            heading="Review monthly and report quarterly",
            why=(
                "A register that nobody above the Quality Coordinator "
                "ever looks at cannot trigger the management attention a "
                "system failure actually needs."
            ),
            body=[
                "The Medical Superintendent reviews the failure-"
                "reporting register monthly.",
                "A summary is presented to the governing body quarterly.",
            ],
            oe_code="ROM.4.c",
        ),
        PlainItem(
            heading="Report externally where required",
            why=(
                "A mandatory external notification that is missed is a "
                "statutory failure on top of the original system "
                "failure -- this has to be checked every time, not "
                "assumed not to apply."
            ),
            body=[
                "Every logged failure is checked against applicable "
                "external-reporting obligations -- for example adverse-"
                "event reporting or notifiable-disease reporting.",
                "Where an external report is required, it is submitted "
                "and the submission is recorded against the register "
                "entry.",
            ],
            oe_code="ROM.4.c",
        ),
        PlainItem(
            heading="Find the pattern, fix the system -- not just the case",
            why=(
                "Closing ten individual incidents of the same type, one "
                "at a time, without ever asking why the same failure "
                "keeps happening, leaves the actual system problem in "
                "place to produce an eleventh."
            ),
            body=[
                "The Quality Coordinator runs a trend analysis across the "
                "failure-reporting register at least quarterly, grouping "
                "reports by failure type.",
                "Where the same failure type recurs three or more times "
                "within a defined period, the Medical Superintendent "
                "opens a systemic fix addressing the underlying process, "
                "not just the individual cases.",
            ],
            oe_code="ROM.4.c",
        ),
    ],
    records_note="This SOP produces and maintains Records 1-2 (see the ROM.4 Records folder).",
    related_documents=[
        "Policy on Risk Management, System-Failure Reporting and Outsourced Services (ROM.4)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the Medical Superintendent, and sooner if a "
        "reporting gap is found or a trend analysis reveals a systemic "
        "issue."
    ),
    full_reference_list=[
        NABH_ROM_CITE.format(code="ROM.4"),
        "World Health Organization. (2020, September 16). [Patient Safety Incident Reporting and Learning Systems: Technical Report and Guidance](https://iris.who.int/server/api/core/bitstreams/49947589-0a06-4708-8cc9-379bc8d2f9f2/content).",
    ],
)

# --------------------------------------------------------------- ROM.2 -----
ROM2 = SOPSpecV2(
    sop_no="SOP-ROM.2",
    title="Administrative Head — Qualifications, Experience, Legal Compliance and Performance Review",
    purpose_plain=(
        "This SOP sets out how «Hospital Name» verifies, before "
        "appointment, that the person heading day-to-day operations has "
        "the requisite administrative qualifications and experience; "
        "keeps a current register of the legislations, regulations and "
        "notifications that leader is responsible for complying with; and "
        "reviews that leader's performance for effectiveness on a defined "
        "cycle -- so headship rests on verified fitness and ongoing "
        "accountability, not an unchecked appointment."
    ),
    purpose_trigger=(
        "A new administrative head takes charge, and six months later an "
        "assessor asks to see the qualification check that was done before "
        "appointment, the legislation register this head is accountable "
        "for, and the record of the first performance review. This SOP is "
        "what makes sure all three already exist, rather than being "
        "assembled the week before the visit."
    ),
    purpose_why=(
        "We do this because a hospital run day to day by someone whose "
        "qualifications were never checked, who doesn't know which laws "
        "apply to the services this hospital actually runs, or whose "
        "performance nobody ever reviews, is a hospital where day-to-day "
        "operating authority rests on an assumption instead of a verified "
        "fact."
    ),
    purpose_text=(
        "To define how «Hospital Name» verifies the administrative head's "
        "qualifications and experience before appointment, maintains a "
        "current applicable-legislation register for that role, and "
        "reviews the administrative head's performance for effectiveness "
        "on a defined cycle."
    ),
    scope_why=(
        "so this applies to whoever actually holds day-to-day operating "
        "authority -- by whatever title «Hospital Name» gives the role -- "
        "not only to a title that happens to say 'administrator.'"
    ),
    scope_text=(
        "Applies to the person heading «Hospital Name» on a day-to-day "
        "basis -- however that role is titled locally (Administrator, "
        "Medical Superintendent, CEO, or equivalent) -- and to the "
        "governing body that appoints, verifies and reviews that person."
    ),
    responsibility_why=(
        "qualifications nobody checked, a legislation list nobody keeps "
        "current, and a review nobody schedules are each a gap that only "
        "surfaces when something has already gone wrong under this "
        "person's authority."
    ),
    responsibilities=[
        ("Governing Body",
         "Verifies the administrative head's qualifications and "
         "experience before appointment, reviews that head's performance "
         "on the defined cycle, and signs off both."),
        ("Administrative Head",
         "Keeps the applicable-legislation register current against the "
         "hospital's actual services, and complies with every "
         "legislation, regulation and notification named in it."),
        ("Quality Coordinator",
         "Confirms, at the quarterly audit, that the legislation "
         "register is current and that the next performance review is "
         "scheduled, not overdue."),
    ],
    items=[
        PlainItem(
            heading="Verify qualifications and experience before appointment",
            why=(
                "An administrative head whose qualifications and "
                "experience were taken on trust, never checked against "
                "the role's own requirements, is running the hospital on "
                "an assumption the governing body never actually tested."
            ),
            body=[
                "Before appointment, the governing body checks the "
                "candidate's administrative qualifications and "
                "experience against the requirements this hospital has "
                "defined for the role.",
                "The verification is recorded, with the documents "
                "checked and the outcome, before the appointment is "
                "confirmed.",
                "Where the role changes hands, the same verification is "
                "repeated for the new appointee -- a transfer or "
                "promotion is never assumed to carry the check forward "
                "from a different role.",
                "The underlying qualification and registration documents "
                "themselves are filed in the administrative head's "
                "personal file under the hospital's human-resource "
                "credentialing process; this record is the governance-"
                "level verification that the check was done, not a "
                "second copy of the certificates.",
            ],
            oe_code="ROM.2.a",
            boundary=[
                "ROM.1.d covers the governing body's appointment of "
                "senior leaders generally; this step owns only the "
                "qualifications/experience check for the administrative "
                "head specifically.",
                "The personal file holding the actual certificates is "
                "HRM's credentialing process, not this SOP.",
            ],
        ),
        PlainItem(
            heading="Keep the applicable-legislation register current",
            why=(
                "An applicable-law list copied from another hospital, or "
                "one nobody updates when a service changes, tells the "
                "administrative head they are compliant with laws that "
                "may no longer be the ones that actually govern what this "
                "hospital does."
            ),
            body=[
                "The administrative head maintains a written register of "
                "the legislations, regulations and notifications this "
                "hospital is actually subject to, drawn from the "
                "hospital's defined service directory -- not a generic "
                "list of statutes the hospital's own services never "
                "trigger.",
                "When a service is added, suspended or withdrawn, the "
                "register is reviewed for that service and updated if "
                "needed.",
                "A statute already owned by another document -- "
                "biomedical waste rules under the infection-control "
                "policy, the Narcotic Drugs and Psychotropic Substances "
                "Act under medication management, PC-PNDT under imaging, "
                "for example -- stays in that owning document; this "
                "register records that the administrative head is "
                "responsible for the applicable set as a whole, not a "
                "duplicate copy of each one.",
                "The register is reviewed, and its currency confirmed, at "
                "least annually.",
            ],
            oe_code="ROM.2.c",
            boundary=[
                "A statute already owned by a specific chapter (HIC.3 "
                "biomedical waste, MOM.8 narcotics, AAC.5 PC-PNDT) stays "
                "there; this step owns the administrative head's overall "
                "accountability for the applicable set, not a second "
                "register of the same statutes.",
            ],
        ),
        PlainItem(
            heading="Review performance for effectiveness",
            why=(
                "An administrative head whose performance is never "
                "formally reviewed has, in practice, unaccountable "
                "day-to-day authority over the hospital -- a review that "
                "only happens informally, in conversation, leaves no "
                "record an assessor -- or the governing body itself -- can "
                "actually check."
            ),
            body=[
                "The governing body reviews the administrative head's "
                "performance for effectiveness at least annually, against "
                "criteria the governing body has defined for the role "
                "(such as achievement of operational plans, service "
                "standards and statutory compliance).",
                "The review is recorded, signed by the governing body, "
                "and shared with the administrative head.",
                "Where the review finds a performance gap, the governing "
                "body records the corrective step agreed and follows up "
                "at the next review.",
            ],
            oe_code="ROM.2.d",
            technical_sources=[
                "International Organization for Standardization. (2026). "
                "[ISO 9001:2026, Quality management systems — "
                "Requirements](https://www.iso.org/standard/88464.html), "
                "clause 5.3 (Organizational roles, responsibilities and "
                "authorities). External benchmark for defining and "
                "reviewing a leadership role's accountability; SHCO "
                "accreditation does not itself require ISO 9001 "
                "certification.",
            ],
            boundary=[
                "ROM.1.c (organisation's performance against its mission) "
                "and ROM.3.d (service-standard monitoring) are "
                "organisation-level measures this review may draw on; "
                "this step owns only the review of the person, not those "
                "underlying measures themselves.",
            ],
        ),
    ],
    records_note="This SOP produces and maintains Records 1-3 (see the ROM.2 Records folder).",
    related_documents=[
        "Policy on the Administrative Head of the Organisation (ROM.2)",
        "Policy on Governance — Roles, Responsibilities and Ethical Management (ROM.1)",
    ],
    review_text=(
        "This SOP is reviewed at least annually by the Quality Coordinator "
        "together with the governing body, and sooner if the role changes "
        "hands, the service directory changes in a way that alters the "
        "applicable-legislation register, or a performance review finds a "
        "gap this SOP did not anticipate."
    ),
    full_reference_list=[
        NABH_ROM_CITE.format(code="ROM.2"),
        "International Organization for Standardization. (2026). [ISO 9001:2026, Quality management systems — Requirements](https://www.iso.org/standard/88464.html), clause 5.3.",
    ],
)

SOPS = [
    ("SOP_ROM.1.a_governance_roles.docx", ROM1A),
    ("SOP_ROM.1.b_vision_mission_values.docx", ROM1B),
    ("SOP_ROM.1.e_ethical_management_framework.docx", ROM1E),
    ("SOP_ROM.3.d_measurable_service_standards.docx", ROM3D),
    ("SOP_ROM.4.a_risk_management.docx", ROM4A),
    ("SOP_ROM.4.c_failure_reporting.docx", ROM4C),
    ("SOP_ROM.2.a_to_d_administrative_head.docx", ROM2),
]

# --------------------------------------------------------- ROM.2 Records ---
ROM2_RECORDS: list[tuple[int, str, RecordSpec]] = [
    (1, "qualification_experience_verification", RecordSpec(
        oe_code="ROM.2.a / ROM.2.b",
        oe_requirement=(
            "The person heading the organisation has requisite and "
            "appropriate administrative qualifications and experience."
        ),
        record_title="ROM.2 Record 1 — Administrative head qualification and experience verification record",
        what_is_this=(
            "This record is the proof the governing body actually "
            "checked the administrative head's qualifications and "
            "experience against the role's own defined requirements "
            "before appointment -- not a copy of the certificates "
            "themselves, which stay in the personal file."
        ),
        real_example=(
            "Before confirming a new Administrator, the governing body "
            "checks the candidate's postgraduate hospital-administration "
            "qualification and nine years of administrative experience "
            "against the role's defined requirement of a postgraduate "
            "qualification and five years' experience, records the check "
            "as met, and signs off the appointment."
        ),
        why_nabh_asks=(
            "An administrative head whose qualifications were taken on "
            "trust, never checked against what the role actually "
            "requires, is running the hospital on an assumption the "
            "governing body never tested -- this record is the proof "
            "that assumption was replaced with a check."
        ),
        how_to_fill=[
            ("Appointee Name / Role", "Who is being verified, and the title this hospital uses for the role."),
            ("Qualification Required / Held", "The role's defined requirement, and what the candidate actually holds."),
            ("Experience Required / Held", "The role's defined requirement, and what the candidate actually has."),
            ("Documents Checked", "Degree certificate, registration, prior-employment proof, etc."),
            ("Outcome / Governing Body Sign-Off", "Met / Not Met, with the signing member and date."),
        ],
        verified_sources=[NABH_ROM_CITE.format(code="ROM.2")],
        column_headers=["Appointee Name / Role", "Qualification Required / Held", "Experience Required / Held", "Documents Checked", "Outcome / Governing Body Sign-Off"],
        worked_example_row=[
            "WORKED EXAMPLE — Dr. A. Rao / Administrator",
            "PG Diploma in Hospital Administration required / held",
            "5 years required / 9 years held",
            "Degree certificate, NMC registration, prior-employer letter",
            "Met — Chairperson, Governing Body / 03-Jan-2026",
        ],
    )),
    (2, "applicable_legislation_register", RecordSpec(
        oe_code="ROM.2.c (Core)",
        oe_requirement=(
            "The leader is responsible for and complies with the "
            "laid-down and applicable legislations, regulations and "
            "notifications."
        ),
        record_title="ROM.2 Record 2 — Administrative head applicable-legislation register",
        what_is_this=(
            "This record is the written list of which legislations, "
            "regulations and notifications actually apply to this "
            "hospital's services, kept current, with the administrative "
            "head's responsibility for each one on record."
        ),
        real_example=(
            "The register lists the Clinical Establishments Act "
            "registration, Biomedical Waste Management Rules, the "
            "Pre-Conception and Pre-Natal Diagnostic Techniques Act (this "
            "hospital runs an imaging service), each with its renewal or "
            "review date and the administrative head named as "
            "responsible."
        ),
        why_nabh_asks=(
            "A law list copied from another hospital, or one nobody "
            "updates when a service changes, tells the administrative "
            "head they are compliant with laws that may no longer be the "
            "ones that actually govern what this hospital does."
        ),
        how_to_fill=[
            ("Legislation / Regulation / Notification", "Name and year."),
            ("Why It Applies", "Which of this hospital's actual services triggers it."),
            ("Owning Document (If Any)", "Where the detailed compliance process already lives, e.g. HIC.3."),
            ("Renewal / Review Date", "When this entry is next checked."),
            ("Reviewed By / Date", "Administrative head sign-off."),
        ],
        verified_sources=[NABH_ROM_CITE.format(code="ROM.2")],
        column_headers=["Legislation / Regulation / Notification", "Why It Applies", "Owning Document (If Any)", "Renewal / Review Date", "Reviewed By / Date"],
        worked_example_row=[
            "WORKED EXAMPLE — Biomedical Waste Management Rules, 2016",
            "Hospital generates biomedical waste from clinical services",
            "HIC.3 Support-Services Infection-Control Policy",
            "Annual authorisation renewal — 15-Apr-2026",
            "Dr. A. Rao, Administrator / 10-Jan-2026",
        ],
    )),
    (3, "performance_review_record", RecordSpec(
        oe_code="ROM.2.d (Achievement)",
        oe_requirement=(
            "The performance of the organisation's leader is reviewed "
            "for effectiveness."
        ),
        record_title="ROM.2 Record 3 — Administrative head performance review record",
        what_is_this=(
            "This record is the proof the governing body actually held a "
            "formal performance review of the administrative head, "
            "against defined criteria, with a signed outcome -- not an "
            "informal conversation nobody wrote down."
        ),
        real_example=(
            "At the annual review, the governing body assesses the "
            "Administrator against the year's operational-plan targets, "
            "service-standard performance and statutory-compliance "
            "record, finds two targets missed, agrees a corrective step "
            "with a follow-up date, and signs the outcome."
        ),
        why_nabh_asks=(
            "An administrative head whose performance is never formally "
            "reviewed has, in practice, unaccountable day-to-day "
            "authority over the hospital -- this record is what makes "
            "that review checkable instead of assumed to have happened."
        ),
        how_to_fill=[
            ("Review Period", "The cycle being assessed, e.g. calendar or financial year."),
            ("Criteria Assessed", "What the governing body measured the head against."),
            ("Outcome", "Met / Partially Met / Not Met, in the governing body's own words."),
            ("Corrective Step Agreed (If Any)", "What changes, and by when."),
            ("Governing Body Sign-Off / Date", "Who conducted the review and signed it."),
        ],
        verified_sources=[
            NABH_ROM_CITE.format(code="ROM.2"),
            "International Organization for Standardization. (2026). [ISO 9001:2026, Quality management systems — Requirements](https://www.iso.org/standard/88464.html), clause 5.3.",
        ],
        column_headers=["Review Period", "Criteria Assessed", "Outcome", "Corrective Step Agreed (If Any)", "Governing Body Sign-Off / Date"],
        worked_example_row=[
            "WORKED EXAMPLE — Calendar Year 2026",
            "Operational-plan targets, service standards, statutory compliance",
            "Partially Met — 2 of 10 targets missed",
            "Monthly interim review of the 2 missed targets; Chairperson / next review 15-Jan-2027",
            "Chairperson, Governing Body / 10-Jan-2027",
        ],
    )),
]


def main() -> None:
    for fname, spec in SOPS:
        out_path = OUT_ROOT / fname
        build_sop_v2(spec, out_path)
        print(f"built {out_path} (v2: plain body + audit appendix)")

    for idx, slug, rspec in ROM2_RECORDS:
        rel_name = f"ROM.2_Record_{idx:02d}_{slug}.docx"
        out_path = RECORDS_ROOT / rel_name
        build_record(rspec, out_path)
        print(f"built {out_path}")

    manifest_path = OUT_ROOT / "manifest.json"
    manifest: list[dict] = json.loads(manifest_path.read_text(encoding="utf-8"))
    existing_files = {e["file"] for e in manifest}

    new_entries = [{
        "file": "SOP_ROM.2.a_to_d_administrative_head.docx",
        "document_type": "sop",
        "standard_code": "ROM.2",
        "title": "SOP — Administrative Head — Qualifications, Experience, Legal Compliance and Performance Review (ROM.2)",
    }]
    for idx, slug, rspec in ROM2_RECORDS:
        new_entries.append({
            "file": f"Records/ROM.2_Record_{idx:02d}_{slug}.docx",
            "document_type": "record",
            "standard_code": "ROM.2",
            "record_index": idx,
            "title": rspec.record_title.split("—", 1)[-1].strip(),
        })

    added = 0
    for entry in new_entries:
        if entry["file"] not in existing_files:
            manifest.append(entry)
            added += 1

    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {manifest_path} ({len(manifest)} entries, {added} new)")


if __name__ == "__main__":
    main()
