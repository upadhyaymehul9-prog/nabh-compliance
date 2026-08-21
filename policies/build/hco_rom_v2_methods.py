# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO ROM.1–ROM.6.

HCO 6th Edition chapter name is Responsibilities of Management (ROM).
Method notes from the Guidebook are attached separately by the generator.
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    ms = D("Medical Superintendent")
    qc = D("Quality Coordinator")
    gov = D("those responsible for governance")
    yearly = D("annually")
    quarterly = D("quarterly")

    return {
        "ROM.1.a": f"""{HOSPITAL} identifies {gov} by name and role (owner, partners, trustees, board, or the responsible ministry for a public hospital) and documents their roles and responsibilities.

The current list and role document sit with the {ms}. A letterhead name without written roles is not this CORE asterisked element.""",

        "ROM.1.b": f"""{gov} lay down the organisation's vision, mission and values in writing. They are made public (display, website, induction pack as the organisation defines).

The {ms} holds the current approved text. A poster without a dated approval is not this asterisked element.""",

        "ROM.1.c": f"""{gov} approve the documented strategic plan, operational plan and annual budget before the year starts (or at the defined cycle). Approval is minuted.

The {ms} files the approved plans and budget. An unapproved spreadsheet is not this asterisked element.""",

        "ROM.1.d": f"""{gov} monitor and measure organisational performance against the stated mission at a defined interval (default {quarterly} dashboard plus {yearly} review).

Minutes record what was reviewed and any decision. The {qc} prepares the pack.""",

        "ROM.1.e": f"""{gov} appoint the senior leaders (including the person heading the organisation). Appointment letters, dates and reporting lines are on file with the {ms}.

A person acting as head without a governance appointment is escalated the same week.""",

        "ROM.1.f": f"""{gov} support safety initiatives, the clinical-governance framework and quality-improvement plans: they receive those reports, resource them, and minute decisions.

Support is visible in minutes and budget lines, not only in a statement of intent. This is an asterisked element.""",

        "ROM.1.g": f"""{gov} develop a clinical-governance framework covering clinical audit, clinical pathways, education and research as they apply to this hospital's scope.

The framework is written, dated and owned by the {ms} with the {qc}. ROM.1.f is support of that framework; this element is that the framework exists.""",

        "ROM.1.h": f"""{gov} support the ethical-management framework (ROM.2): they receive ethics issues that reach governance, resource the framework, and minute decisions.

This Achievement element is evidenced by that support, not by the existence of the framework alone.""",

        "ROM.1.i": f"""{gov} inform the public of the quality and performance of services (for example selected indicators, accreditation status, and how to give feedback — the hospital names the set and channel).

The {qc} keeps samples and dates of what was published.""",

        "ROM.2.a": f"""Leaders establish a written ethical-management framework: principles, who decides, how issues are raised, and how decisions are recorded.

The {ms} keeps the current framework. Minutes-only notes are not this CORE asterisked element.""",

        "ROM.2.b": f"""The framework includes processes for managing issues with ethical implications, dilemmas and concerns (clinical and organisational examples the organisation names).

A named path, timeline and record exist. An informal corridor discussion is not this asterisked element.""",

        "ROM.2.c": f"""The organisation discloses its ownership in a defined public place (reception display, website, statutory board as applicable).

The {ms} holds the current disclosure text and checks it {yearly}.""",

        "ROM.2.d": f"""The organisation honestly portrays its affiliations and accreditations: only current, in-scope programmes are displayed; expired or applied-for status is not shown as awarded.

The {qc} reviews public materials {quarterly}.""",

        "ROM.3.a": f"""{gov} address the organisation's sustainability programme in Environment, Social and Governance (ESG) terms: a written programme, named owner and a review at least {yearly}.

The {ms} tables the programme at a governance meeting. A slogan without a programme is not this element.""",

        "ROM.3.b": f"""The organisation takes documented initiatives toward an energy-efficient and environmentally friendly hospital (energy, water, waste-to-environment as FMS owns the engineering controls).

Actions, dates and results sit in the ESG / engineering file. This is an asterisked element. FMS remains the home of facility safety; this element is the sustainability initiative.""",

        "ROM.3.c": f"""{gov} address the organisation's social responsibility (community access, charity care, local health initiatives as the hospital defines).

The programme and any annual report of activity are minuted. Intent wording "organisations social responsibility" is kept as printed in the Standards PDF.""",

        "ROM.3.d": f"""Staff well-being is promoted: defined work-hour monitoring, healthy-lifestyle support, scheduled breaks and a way to raise workload concern — as the organisation writes.

HR and the {ms} hold the current measures. A poster without a working arrangement is not this element.""",

        "ROM.3.e": f"""The organisation follows sustainable procurement practices (environmental and social criteria in selected tenders, as the purchase policy names).

Purchase files show those criteria were applied. This Excellence element is evidenced by completed procurements, not by a policy sentence alone.""",

        "ROM.3.f": f"""The hospital encourages employees to use common / public transport to reduce commuting impact (information, any incentive the organisation defines, and a record that it was offered).

HR keeps the current offer. This Achievement element is encouragement, not a mandate that every staff member commute that way.""",

        "ROM.3.g": f"""The organisation ensures financial sustainability by balancing the financial aspects of healthcare delivery: budget vs actual, cash and credit discipline, and a {yearly} view that services can continue.

The {ms} and accounts table this to {gov}. A budget without a review is incomplete under this Achievement element.""",

        "ROM.4.a": f"""The person heading the organisation has requisite and appropriate administrative qualifications and experience: qualification in hospital management / administration, and administrative experience in a hospital, as {gov} define for this hospital's legal form and size.

Certificates and a CV are on file. {gov} check this at appointment and if the role-holder changes. The default title is {ms}.""",

        "ROM.4.b": f"""The leader is responsible for and complies with laid-down and applicable legislations, regulations and notifications. A current register of what applies to this hospital (legal form and services actually run) is maintained; India Code is the lookup, not a paste of every central Act.

The {ms} owns the register and evidence of compliance. This CORE element does not import a named Act as a checklist for the whole standard; statutory duties that already live in other documents of {HOSPITAL} remain those documents.""",

        "ROM.4.c": f"""The leader appoints or participates in recruiting department leaders who assist day-to-day functioning. Appointment files show the leader's role in the decision.

A department running without an identified leader is escalated to the {ms} the same week.""",

        "ROM.4.d": f"""The leader ensures each organisational programme, service, site or department has effective leadership: a named person, time allocation and a reporting line.

The {ms} keeps the current leadership map. This Achievement element is evidenced by that map plus how vacancies are covered.""",

        "ROM.4.e": f"""The performance of the organisation's leader is reviewed for effectiveness at least {yearly} by {gov} (or the appointing authority).

The review is dated and filed. A year without a review is a gap under this Achievement element.""",

        "ROM.5.a": f"""The organisation has strategic and operational plans, including long-term and short-term goals commensurate with vision, mission and values, developed in consultation with stakeholders.

Plans name owners and timeframes. The {qc} holds the current set with the {ms}.""",

        "ROM.5.b": f"""The organisation coordinates functioning with departments and external agencies and monitors progress against defined goals and objectives.

Coordination minutes and a progress view sit with the {qc}. This is an asterisked element.""",

        "ROM.5.c": f"""The organisation plans and budgets for its activities {yearly}. The operational plan is linked to the strategic plan. The {ms} tables the annual plan and budget for governance approval (ROM.1.c).""",

        "ROM.5.d": f"""The functioning of committees is reviewed for effectiveness at a defined interval (default {yearly}): whether they met, decided, and closed actions.

The {qc} prepares the review. A list of committees without an effectiveness review is not this Achievement element.""",

        "ROM.5.e": f"""The organisation documents measurable service standards and monitors them (what good looks like for selected services, the measure, and the review interval).

The {qc} keeps the standard set and results. This is an asterisked element.""",

        "ROM.5.f": f"""Systems and processes are in place for change management: written guidance for operational, clinical or structural change, including who approves, how staff are told, and how service continuity is kept.

A change started with no record on that path is incomplete under this Excellence asterisked element.""",

        "ROM.6.a": f"""Leadership ensures proactive risk management across the organisation: a risk-management system, identification of clinical and organisational risks (examples the Guidebook names include falls, infections, vulnerable-patient risks such as DVT, and clinical alarms), assessment, action and review.

The {ms} owns the system with the {qc}. A register that is not used on the floor is not this CORE asterisked element.""",

        "ROM.6.b": f"""Leadership provides resources for proactive risk-assessment and risk-reduction: time, tools, training and a contingency for preventive actions the leaders require.

The {ms} signs the resource line. A risk system with no time or budget to act is not this element.""",

        "ROM.6.c": f"""Leadership ensures integration between quality improvement, risk management and strategic planning: risk and quality findings feed the plan; the plan names risk and quality work.

The {qc} shows the join in the {D('Quality Improvement Committee')} and governance packs.""",

        "ROM.6.d": f"""Leadership ensures systems for internal and external reporting of system and process failures (what is reported, to whom inside, and to which external agency when required, with timelines). The Guidebook example: MRI breakdown is reported internally to the head and to patients; a radiation-source event is reported to AERB; fire needs strong internal and external reporting.

A documented service-continuity plan covers fire and non-fire emergencies for critical operations and is tested at defined intervals. Skipping a required report is a stop-work trigger (section 6). This is an asterisked Achievement element.""",

        "ROM.6.e": f"""Leadership ensures a documented agreement for every outsourced service, including service parameters (quality, numbers, reports, timelines) and how disputes are resolved. An affiliate or group firm still has an agreement.

Starting or continuing outsourced work without that agreement is a stop-work trigger (section 6).""",

        "ROM.6.f": f"""Leadership monitors the quality of outsourced services against the agreement at least {yearly} (more often if the service is critical to patient care) and makes improvements with the vendor as required.

Where outsourcing is done solely under prescribed statutory norms or regulations, the Guidebook says monitoring the quality of that outsourced service is not mandatory. The {ms} holds review notes. An agreement without monitoring (when monitoring is required) is incomplete under this Achievement element.""",
    }
