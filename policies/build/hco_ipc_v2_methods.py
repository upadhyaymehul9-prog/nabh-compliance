# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO IPC.1–IPC.8.

HCO 6th Edition chapter name is Infection Prevention and Control (IPC).
Method notes from the Guidebook are attached separately by the generator.
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    ipco = D("Infection Prevention and Control Officer")
    ipcn = D("Infection Prevention and Control Nurse")
    ipcc = D("Infection Prevention and Control Committee")
    ms = D("Medical Superintendent")
    qc = D("Quality Coordinator")
    ns = D("Nursing Superintendent")
    cssd = D("CSSD In-Charge")
    oh = D("Occupational Health Physician")
    yearly = D("annually")
    quarterly = D("quarterly")

    return {
        "IPC.1.a": f"""{HOSPITAL} documents its infection prevention and control programme. The written guidance covers clinical areas and support services and aims at preventing and reducing healthcare-associated infection in patients, visitors and staff.

The {ipco} keeps the current version in the {D('Infection Prevention and Control Manual')}. The {ipcc} approves it. A programme that exists only as meeting minutes is not documented under this CORE asterisked element.""",

        "IPC.1.b": f"""The {ipcc} identifies high-risk activities (for example OT, ICU, dialysis, CSSD, kitchen, laundry, BMW, construction) from scientific literature and this hospital's scope, and writes guidance to prevent and manage infection for each.

The current high-risk list is posted with the manual. Staff who work in those areas are trained on the matching guidance at induction and {yearly}.""",

        "IPC.1.c": f"""The {ipcc} reviews and updates the programme at least {yearly} and sooner after an outbreak, a new service, or a change in national guidance.

An update is a dated change to the manual or high-risk list, not only a restatement that the programme continues. The {qc} holds the review minute.""",

        "IPC.1.d": f"""The annual (or more frequent) review uses a validated infection-prevention assessment tool (for example WHO IPCAF or an equivalent the {ipcc} names). Gaps from the tool become actions with owners and due dates.

This Achievement element is evidenced by a completed tool plus follow-up, not by an informal walk-round note alone.""",

        "IPC.1.e": f"""The {ms} constitutes a multi-disciplinary {ipcc} that coordinates all IPC activities. Membership preferably includes administration, microbiology, a physician / IPC specialist, nursing, OT, CSSD, housekeeping and quality.

Terms of reference, quorum and meeting frequency ({D('at least monthly')}) are written. Minutes name decisions, owners and due dates.""",

        "IPC.1.f": f"""An infection prevention and control team runs day-to-day implementation: the {ipco}, {ipcn} (one or more) and named link staff. The team supports wards, investigates clusters, and brings findings to the {ipcc}.

The team's written terms sit in the manual. A committee without a working team is not this asterisked element.""",

        "IPC.1.g": f"""The {ms} designates an infection prevention and control officer — a doctor knowledgeable in infection prevention and control — as part of the team. The designation letter, time allocation and reporting line are on file.

The officer chairs or is a standing member of the {ipcc} and is reachable for outbreaks and exposure events.""",

        "IPC.1.h": f"""The {ms} designates infection prevention and control nurse(s): registered nurses with additional structured IPC training. Their responsibilities (surveillance, hand-hygiene audit, staff education, outbreak support) are in writing.

Coverage matches the hospital's size and risk. A nurse who has the title only on a circular is not designated under this element.""",

        "IPC.1.i": f"""{HOSPITAL} runs information, education and communication on IPC for the community it serves — at least hand hygiene, cough etiquette and when to seek care — with stakeholders as needed (posters, OPD talks, local messaging).

The {ipco} keeps samples and dates of community IEC. This is community-facing, not only staff induction.""",

        "IPC.1.j": f"""The organisation participates in managing community outbreaks: a written contact path to the public health / statutory agency, internal roles, and staff briefing when an outbreak is declared in the catchment.

The {ms} owns external communication. A drill or a real event in the last year is recorded.""",

        "IPC.2.a": f"""Management makes resources for the IPC programme available on a continual basis, including a line in the annual budget for PPE, hand-hygiene products, disinfectants, isolation capacity, laboratory support, training and the {ipco}/{ipcn} time.

The {ms} signs the budget line. Stock-outs of PPE or soap that last beyond the defined buffer are reported to the {ipcc}.""",

        "IPC.2.b": f"""Adequate and appropriate PPE, soaps and disinfectants are at the point of use, with an inventory so they do not run out. Staff are trained to use them correctly (donning/doffing, dilution of disinfectant as the manufacturer states).

The {ipcn} spot-checks availability and correct use {D('monthly')}. Starting a procedure without required PPE is a stop-work trigger under IPC.3.""",

        "IPC.2.c": f"""Every patient-care area has at least one easily accessible hand-hygiene point (washbasin with running water and/or alcohol-based handrub) for healthcare providers. Placement follows the organisation's hand-hygiene plan.

The {ipco} maps points and walks them {quarterly}. A sink that is present but blocked or without soap/rub is not accessible.""",

        "IPC.2.d": f"""The organisation defines when isolation is required and when barrier nursing or cohorting is used instead. Isolation rooms / barrier-nursing kits matching that definition are available.

The {ns} and the {ipco} agree the location list. A policy without a usable isolation or barrier arrangement is not this element.""",

        "IPC.3.a": f"""Staff apply standard precautions at all times, in every area: hand hygiene, PPE based on risk, respiratory hygiene, sharps safety, safe linen and environmental cleaning, and patient-care equipment handling.

The {ipcn} audits practice {D('monthly')}. Starting a procedure without standard precautions is a stop-work trigger (section 6).""",

        "IPC.3.b": f"""{HOSPITAL} adheres to national/international hand-hygiene guidelines (WHO 5 Moments is the default reference). Moments, technique and product are taught at induction and {yearly}.

Compliance is measured under IPC.6.d. Skipping a required moment before an invasive step is a stop-work trigger (section 6).""",

        "IPC.3.c": f"""Transmission-based precautions — contact, droplet, airborne — are applied when the organism or syndrome requires them. The PPE and room placement for each mode are in the manual.

The {D('treating doctor')} orders the precaution; nursing implements and signs the door/kardex alert. An airborne case without the defined placement/PPE is escalated the same shift.""",

        "IPC.3.d": f"""Safe injection and infusion practice follows one needle, one syringe, only one time (CDC / WHO). Multi-dose vials follow the organisation's written rule. Sharps go in a puncture-proof container at the point of use.

Reuse of a needle or syringe is a stop-work trigger (section 6). Pharmacy and nursing check infusion preparation areas {quarterly}.""",

        "IPC.3.e": f"""An antimicrobial usage policy is established and documented: which agents for which conditions, monotherapy vs combination, escalation/de-escalation, dose and duration, and a restricted list aligned with WHO AWaRe as the {ipcc} adopts it.

The policy is reviewed {yearly} with local susceptibility. The {D('Microbiologist and the Drug and Therapeutics Committee')} own the clinical content with the {ipco}.""",

        "IPC.3.f": f"""The antimicrobial stewardship programme is implemented: restricted agents are ordered through the defined path; deviations are fed back to the clinician; use is monitored (days of therapy / restricted-agent audit) and reported to the {ipcc}.

Starting a restricted agent off-path is a stop-work trigger (section 6) except documented emergency first doses, which are regularised within {D('24 hours')}.""",

        "IPC.4.a": f"""Engineering controls to prevent infection include layout of patient-care areas (including spacing between beds as the organisation defines, default one–two metres where the building allows), OT air-handling as designed, and water/plumbing that does not create infection risk.

The {D('Engineering In-Charge')} and the {ipco} review these controls {yearly} and after renovation.""",

        "IPC.4.b": f"""Before construction or renovation in or next to a patient-care area, an infection-control risk assessment (ICRA or equivalent validated tool) is completed and a written plan of barriers, traffic, dust and water controls is implemented.

Starting works without that plan is a stop-work trigger (section 6). The {ipco} signs the plan; engineering keeps the file.""",

        "IPC.4.c": f"""Housekeeping procedures are written and followed at every level: wards, OT, public areas including toilets, and support areas. Cleaning frequency, product, method and terminal clean after isolation are defined.

The {D('Housekeeping In-Charge')} trains staff. Effectiveness is monitored under IPC.6.f. This is a CORE asterisked element.""",

        "IPC.4.d": f"""Biomedical waste is segregated at source into the statutory colour-coded bags/containers, handled with PPE, stored as required, and handed to the authorised vendor. The {ipcc}/team monitors the programme as statute requires.

BMW without segregation or PPE is a stop-work trigger (section 6). This CORE element follows statutory provisions named in the Guidebook interpretation.""",

        "IPC.4.e": f"""Laundry and linen processes — in-house or outsourced — cover collection, transport, wash, and change-of-linen frequency. Used linen from isolation is bagged as the manual states.

The {D('Laundry In-Charge')} (or the outsourced supervisor named in the contract) keeps process records. The {ipcn} audits {quarterly}.""",

        "IPC.4.f": f"""Kitchen sanitation and food handling follow statutory requirements, including screening of food handlers, even when catering is outsourced: separate prep, off-floor storage, pest control, temperature of service, and no contact between cleaning chemicals and food.

The {D('Kitchen / Dietary In-Charge')} owns daily checks. The {ipco} includes kitchen in the IPC round.""",

        "IPC.5.a": f"""Actions to prevent catheter-associated urinary tract infection: insert only when indicated, aseptic insertion, closed system, daily review for removal, and standard plus transmission-based precautions as required.

Inserting a Foley without this bundle is a stop-work trigger (section 6). Nursing records indication and daily review.""",

        "IPC.5.b": f"""Actions to prevent ventilator-associated pneumonia: head-of-bed elevation as clinically allowed, oral care, sedation/weaning review, circuit handling as the bundle states, and standard plus transmission-based precautions.

Starting invasive ventilation without the VAP bundle in place (as soon as the airway is secure) is a stop-work trigger for continuation of non-essential steps (section 6).""",

        "IPC.5.c": f"""Actions to prevent central-line associated bloodstream infection: maximal barrier insertion, chlorhexidine skin prep (or the organisation's equivalent), daily line necessity review, and hub care.

Inserting a central line without the CLABSI bundle is a stop-work trigger (section 6).""",

        "IPC.5.d": f"""Actions to prevent surgical site infection: antimicrobial prophylaxis as the policy times it, skin prep, glycaemic and temperature control as the bundle states, and sterile technique.

Making an incision without the SSI bundle items that must be in place before knife-to-skin is a stop-work trigger (section 6). Cross-reference the surgical-safety policy.""",

        "IPC.6.a": f"""Surveillance mixes active and passive methods and tracks infection risks, rates and trends for the HAIs and processes the {ipcc} names (at least the HAIs in IPC.5 plus hand hygiene and BMW as applicable).

Denominator rules are written. The {ipcn} compiles monthly rates for the {ipcc}.""",

        "IPC.6.b": f"""The IPC team verifies surveillance data regularly — by reviewing each case or a defined sample — before rates are issued.

The {ipco} signs the monthly verification. Unverified counts are not used as official rates.""",

        "IPC.6.c": f"""Surveillance is directed at the high-risk activities identified in IPC.1.b. Evidence of periodic surveillance in those areas (OT, ICU, dialysis, CSSD, etc.) is on file.

A hospital-wide rate without high-risk-area breakout is not this element.""",

        "IPC.6.d": f"""Hand-hygiene compliance is monitored at least {D('monthly')} on an appropriate sample covering all staff categories who touch patients. Results go to the {ipcc} and to the units.

This CORE monitoring is how IPC.3.b is shown to be happening, not a substitute for it.""",

        "IPC.6.e": f"""Surveillance captures occurrence of multi-drug-resistant organisms (for example MRSA, VRE, carbapenem-resistant Enterobacterales as microbiology reports them). Infection vs colonisation is distinguished as the {ipcc} defines.

The {D('Microbiologist')} alerts the {ipcn} of new MDRO isolates the same working day. This Achievement element is evidenced by a working capture mechanism.""",

        "IPC.6.f": f"""Effectiveness of housekeeping is monitored on a defined schedule (visual plus, where used, fluorescent marker or ATP as the {ipcc} chooses) in high-risk and public areas.

Results go to housekeeping and the {ipcc}. Repeat fails trigger retraining or product/method change. This is CORE.""",

        "IPC.6.g": f"""Surveillance feedback — adherence rates, HAI rates, trends and opportunities — is given regularly to the healthcare providers who can act on it (unit in-charges, {ipcc}, treating doctors).

A rate that sits only in the IPC office is not feedback. The {ipcn} keeps the distribution list and dates.""",

        "IPC.6.h": f"""Outbreaks are defined using baseline rates. Written guidance names who declares an outbreak, isolation/cohorting, communication and when to call the statutory agency.

The {ipco} leads the response. Delay in declaring when the definition is met is escalated to the {ms}.""",

        "IPC.6.i": f"""The {ipcc} analyses surveillance data and assigns corrective and preventive action with owners and due dates. The {ipco} tracks closure.

Analysis without action is not this element.""",

        "IPC.7.a": f"""CSSD (or the sterilisation area the organisation uses) has adequate space and zoning: dirty, clean, sterile, with a one-way flow and a suitable location away from traffic that would contaminate packs.

The {cssd} and the {ipco} walk the zoning {quarterly}. Mixing dirty and sterile in one room without a defined barrier is a gap.""",

        "IPC.7.b": f"""Cleaning, packing, disinfection and/or sterilisation, storage and issue follow written guidance aligned with national/international references (CDC guideline for disinfection and sterilisation is a named Guidebook example).

Issue of an item not processed per that guidance is a stop-work trigger (section 6). This is CORE and asterisked.""",

        "IPC.7.c": f"""Instruments, equipment and devices suitable for re-use are identified. The number of re-uses (where limited) and the reprocessing method for each class are in written guidance.

Single-use items are not reprocessed unless a documented, accepted method and risk assessment exist. The {cssd} keeps the list.""",

        "IPC.7.d": f"""Validation tests for sterilisation are done and documented: physical/chemical indicators each load (at least daily physical/chemical as the Guidebook states) and biologic indicators on the defined schedule.

A load that fails validation is not issued. Documentation is the load record, not a monthly summary alone.""",

        "IPC.7.e": f"""When a sterilisation breakdown is identified, the recall procedure is implemented: stop issue, retrieve items from that load/machine (batch, date, machine number), notify users, and reprocess or discard.

A mock recall is run {D('at least annually')}. Issuing during an active recall is a stop-work trigger (section 6).""",

        "IPC.8.a": f"""Occupational health and safety practices to reduce transmission among healthcare providers are in written guidance: PPE, vaccination access, exposure reporting, and work restriction. Resources to implement it are available.

The {oh} and the {ipco} own the guidance. Staff are trained at induction and {yearly}.""",

        "IPC.8.b": f"""The staff immunisation policy matches available evidence. At a minimum, hepatitis B vaccination is provided to staff in direct patient care. Other vaccines follow risk and applicable statutory requirements.

The {oh} holds the register (dose, date, booster). An unvaccinated direct-care worker without a documented contraindication or refusal is a gap.""",

        "IPC.8.c": f"""Work restrictions for staff with transmissible infections (for example conjunctivitis, chickenpox, acute respiratory infection as the {oh} lists) limit role until cleared. Staff know how to report illness.

Working against a restriction is a stop-work trigger (section 6). This Achievement element is evidenced by restrictions that were actually applied.""",

        "IPC.8.d": f"""Blood and body-fluid exposure prevention: appropriate PPE, safe sharps, no recapping, splash protection for procedures that spray. Sharps containers are at the point of use and replaced before full.

The {ipcn} includes this in the monthly IPC round. A recapping culture on a unit is an incident.""",

        "IPC.8.e": f"""Post-exposure prophylaxis for hepatitis B and HIV is provided to concerned staff, aligned with national/international guidelines. First aid is immediate; the {oh} or emergency doctor starts the PEP path the same shift; the {ipcn} keeps the file.

Skipping PEP after a qualifying exposure is a stop-work trigger (section 6). Confidentiality of the file follows PRE.2.d.""",
    }
