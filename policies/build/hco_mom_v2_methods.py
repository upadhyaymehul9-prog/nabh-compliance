# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO MOM.1–MOM.11.

Written from official Standards PDF OE wording + chapter intent (not Guidebook
Interpretation paragraphs — those are not available in this environment).
Do not restate the OE line as the whole method.
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    mso = D("Medication Safety Officer")
    pharm = D("Pharmacy In-Charge")
    dtc = D("Drug and Therapeutics Committee")
    ns = D("Nursing Superintendent")
    qc = D("Quality Coordinator")
    ms = D("Medical Superintendent")
    yearly = D("annually")
    quarterly = D("quarterly")

    return {
        "MOM.1.a": f"""{HOSPITAL} runs pharmacy services and the rest of medication management from written guidance. The {mso} and the {pharm} keep that guidance current. It covers procurement, storage, prescription, transcription, dispensing, administration, monitoring after administration, and reporting of near misses, medication errors and adverse drug reactions.

The guidance names who does each step, which records are kept, and how after-hours and stock-out supply works (section 5.4). The {dtc} (the organisation's multi-disciplinary pharmacy committee) approves the guidance. The {qc} holds the current version.

Staff who prescribe, dispense or administer medications are trained on this guidance at induction and {yearly}. A current copy is available in pharmacy, emergency, ICU, OT, wards and at {D('staff intranet / policies')}.""",

        "MOM.1.b": f"""The {ms} constitutes the {dtc} with at least pharmacy, medical, nursing and {D("one clinical specialty representative matching the hospital's scope")}. The committee's written terms of reference cover formulary, high-risk and emergency medication lists, storage and floor-stock oversight, verbal-order and reconciliation rules, and medication-error review.

The committee meets {D('at least quarterly')}. Minutes name decisions, owners and due dates. The {mso} is a standing member and brings incident and audit findings. Pharmacy services and medication-management guidance are not issued or changed without this committee's review.""",

        "MOM.1.c": f"""The {dtc} reviews medication-management processes at least {yearly} and sooner after a related serious incident, recall, formulary change or audit finding.

An update is a written change to a process (who does what, where, with which record), not only a restatement of the same rule. The {mso} tracks open actions from the last meeting until they close. Staff who must change practice are informed under section 5.5 before the new process is counted as implemented.""",

        "MOM.1.d": f"""When the main pharmacy is closed, or when a required item is out of stock, staff obtain medications through a named after-hours / stock-out procedure.

The procedure names: who is authorised to access the after-hours store or night cupboard; how a second person (or recorded override) is used for high-risk items; how the issue is entered so pharmacy can reconcile the next working day; and how an out-of-stock item is sourced from {D("an approved supplier, another organisation, or the treating doctor's documented alternative")} without leaving the patient without treatment.

Emergency medications in crash carts and emergency trolleys stay under MOM.3; this procedure is for items that are not on those trolleys. The {pharm} tests the after-hours path {quarterly}.""",

        "MOM.1.e": f"""When the {dtc} changes a medication-management process, a formulary item, a high-risk or emergency list, or a recall action, the {mso} informs the staff who prescribe, dispense or administer before the change takes effect.

The mechanism is {D('a dated circular plus a briefing at the next departmental huddle, with the current list posted in pharmacy and on the intranet')}. The {qc} keeps the distribution list and acknowledgements. A change that is only filed in committee minutes is not counted as communicated.""",

        "MOM.2.a": f"""The {dtc} develops the hospital formulary: the list of medications appropriate for the patients {HOSPITAL} actually treats, matched to the defined clinical scope (AAC.1). The list is built collaboratively — pharmacy proposes; clinicians from the services that use the drugs agree; nursing flags administration constraints.

The formulary records generic name, strength(s), dosage form, and whether the item is high-risk. It is not a wholesale catalogue. Items outside scope (for example a chemotherapy agent when the hospital has no oncology service) are not listed as routine stock. The {ms} approves the first issue of the list.""",

        "MOM.2.b": f"""The {dtc} reviews the formulary at least {yearly} and whenever a service is added or withdrawn. Additions, deletions and restrictions are minuted with a clinical reason.

Between annual reviews, urgent additions (a new essential item, a shortage substitution) go through the same committee or a documented emergency sub-process and are ratified at the next meeting. The {pharm} dates the current list on the cover.""",

        "MOM.2.c": f"""The current formulary is available where clinicians prescribe: {D('OPD consulting rooms, wards, ICU, emergency, OT and the hospital information system / intranet')}. An outdated printed copy is removed when a new version is issued.

Pharmacy keeps the master. The {qc} checks availability of the current version at a sample of prescribing locations {quarterly}.""",

        "MOM.2.d": f"""Clinicians prescribe from the current formulary. A non-formulary item is obtained only through the MOM.2.f procedure, not by informal purchase.

Pharmacy flags non-formulary prescribing to the {mso}. Repeated non-adherence by a department is tabled at the {dtc}. This Achievement element is evidenced by prescription-versus-formulary audit, not by a poster.""",

        "MOM.2.e": f"""Formulary medications are acquired through the organisation's written procurement procedure: approved supplier, quality checks on receipt, batch and expiry recorded, and storage handed to pharmacy.

The {pharm} does not accept a delivery that fails identity, integrity or cold-chain checks. Purchase of a formulary item off-procedure (cash from a nearby shop without record) is not acquisition under this policy except as documented in the stock-out procedure (MOM.1.d) and then entered the next working day.""",

        "MOM.2.f": f"""A medication not on the formulary is obtained only through a written non-formulary request: clinical justification, approval by {D('the treating consultant and the Pharmacy In-Charge or DTC chair')}, and a record of source, batch and indication.

The request does not by itself add the item to the formulary. If the item will be needed routinely, the {dtc} considers a formulary amendment. Emergency life-saving non-formulary use is documented retrospectively the same shift.""",

        "MOM.3.a": f"""Pharmacy and every floor-stock location store medications in a clean, safe and secure area. Manufacturer recommendations for temperature, light, humidity and reconstitution are followed. Refrigerated items go in a dedicated medicines refrigerator with a recorded temperature {D('twice daily')}; excursions are reported to pharmacy the same shift.

Access to the main pharmacy and to controlled-drug cupboards is limited to authorised staff. Floor-stock cupboards are locked when the area is unmanned. Food, specimens and staff belongings are not stored with medicines.

Pharmacy has oversight of medications stocked outside the pharmacy, as the chapter intent requires.""",

        "MOM.3.b": f"""Inventory control at {HOSPITAL} uses {D('FEFO (first expiry, first out), defined maximum–minimum levels, and a documented indent cycle')}. Pharmacy reviews expiry and slow-moving stock {D('monthly')}. Floor-stock lists are authorised by the {dtc}; unofficial hoarding in clinical areas is removed.

The {pharm} can account for stock movement from receipt to issue. A location that cannot show its current list and last expiry check is not a compliant storage site.""",

        "MOM.3.c": f"""The {dtc} defines the hospital's high-risk medication list and updates it at least {yearly} and after a related incident. The list includes, at minimum, look-alike / sound-alike items used here, concentrated electrolytes, anticoagulants, insulin, opioids, chemotherapeutic agents, and any other item the committee names for this hospital's scope.

The current list is posted in pharmacy and at every location that stores those items. Staff who prescribe, dispense or administer are trained on it. A list that exists only in a committee file is not implemented.""",

        "MOM.3.d": f"""High-risk medications are stored only where they are clinically necessary — for example concentrated electrolytes in ICU/OT as the committee defines, not in every ward cupboard.

The {dtc} names those locations. Pharmacy does not issue high-risk floor stock to an unlisted area. This Achievement element is evidenced by the location list matching actual storage on walk-round.""",

        "MOM.3.e": f"""Look-alike and sound-alike medications, and different concentrations of the same medication, are stored physically apart — separate bins or shelves, with tall-man lettering or equivalent differentiation where the organisation uses it.

They are never stored alphabetically adjacent when that would put LASA pairs together. The {pharm} checks physical separation on the monthly storage round. Finding two concentrations of the same drug in one bin is a stop-work trigger (section 6).""",

        "MOM.3.f": f"""The {dtc} defines the emergency-medication list. The same list, in the same layout, is used in crash carts / emergency trolleys across {HOSPITAL} so staff moving between areas find drugs in the same place.

Each trolley has a sealed or checklist-controlled inventory. The {ns} and the {pharm} agree the layout. Local 'extra' emergency drugs that are not on the defined list are not stored on the trolley unless the committee amends the list.""",

        "MOM.3.g": f"""Emergency medications are present 24 hours a day at every defined location. After use, the item is replenished {D('immediately from pharmacy, and in any case before the trolley is returned to service')}.

Nursing checks the trolley {D('each shift')} against the list and records the check. A missing or expired emergency drug is a stop-work trigger for that trolley until it is corrected. Pharmacy keeps a replenishment log.""",

        "MOM.4.a": f"""Prescribers follow the organisation's written good-practice / rational-prescribing guidance: indication, dose appropriate to age/weight/organ function, duration, and avoidance of unnecessary polypharmacy and restricted antimicrobials except per the hospital antimicrobial policy.

The {dtc} names the reference guidance ({D('WHO / national essential-medicines principles and the hospital antimicrobial policy')}). Prescription audit under MOM.4.g samples against this guidance.""",

        "MOM.4.b": f"""Every prescription at {HOSPITAL} meets the determined minimum requirements, which include: patient name and unique identification number; generic or approved name of the medicine; route; strength; frequency / time; date and time of the order; and the prescriber's signature (or authenticated electronic equivalent) and identifier.

The {dtc} publishes this minimum list. Pharmacy and nursing do not act on an order that fails the minimum, except through the documented emergency-prescription path, which is completed as soon as the patient is stable.""",

        "MOM.4.c": f"""Before prescribing, the clinician ascertains known drug allergies and previous adverse drug reactions from the patient / family and from the medical record, and records the result (including 'none known').

A red-alert allergy band or equivalent is used when an allergy is recorded. Prescribing without this check is a stop-work trigger. Admission and transfer notes carry the allergy status forward (MOM.4.e).""",

        "MOM.4.d": f"""{HOSPITAL} assists clinicians to prescribe the appropriate medication through {D('formulary access at the point of prescribing, dose-range information for high-risk drugs, and pharmacy clarification of unclear orders before dispensing')}.

Where the hospital uses e-prescribing or clinical decision support, that is the mechanism; where it uses paper, the mechanism is the current formulary plus pharmacy review of orders. This Excellence element is evidenced by a working assistance mechanism, not by a poster.""",

        "MOM.4.e": f"""Medication reconciliation is done at transition points: admission, transfer between units (including ICU to ward), and discharge.

The {D('treating doctor or designated nurse')} compares the patient's current medication list (home + in-hospital) with the new orders, resolves discrepancies with the prescriber, and records the reconciled list in the medical record. Pharmacy supports high-risk and polypharmacy reconciliations. A transfer without a reconciled list is incomplete.""",

        "MOM.4.f": f"""Verbal (including telephone) medication orders are used only when the prescriber cannot write or enter the order in time for safe care. The receiver writes the order, reads it back (drug, dose, route, frequency, patient), and the prescriber confirms.

The prescriber countersigns {D('within 24 hours, and before the next dose where practicable')}. Verbal orders are not used for {D('chemotherapy')} except under a documented emergency rule. Acting on a verbal order without read-back is a stop-work trigger.""",

        "MOM.4.g": f"""The {mso} (or Quality with pharmacy) audits medication orders / prescriptions {quarterly} for safe and rational prescribing: minimum requirements, allergy documentation, formulary adherence, and high-risk dose checks.

The sample size is {D('at least 20 prescriptions per quarter, including emergency and inpatient')}. Results go to the {dtc}.""",

        "MOM.4.h": f"""When the prescription audit finds a gap, the {dtc} assigns corrective and / or preventive action with an owner and a due date. The {mso} tracks closure.

Actions may include feedback to a prescriber, a formulary or guidance change, or training. An audit without follow-up is not Achievement for this element.""",

        "MOM.5.a": f"""Only personnel authorised by {HOSPITAL} write medication orders. The authorised list is held by the {ms} and includes doctors with prescribing privileges for their scope. Interns / residents write under the rules the organisation sets and a named supervisor.

Nursing and pharmacy do not write prescribing orders except where law and hospital privilege expressly allow (for example a documented nurse-prescribing protocol, if any). An order from a person not on the list is not acted on.""",

        "MOM.5.b": f"""Medication orders are written in one uniform location in the medical record — {D('the medication chart / order sheet')} — which already shows the patient's name and unique identification number on that sheet.

Orders are not scattered across progress notes as the only copy. Stickers or loose slips are transcribed onto the uniform chart the same shift. The {ns} checks location uniformity on record audit.""",

        "MOM.5.c": f"""Every medication order is legible, dated, timed and signed (or authenticated in the electronic record). Illegible orders are not guessed — the prescriber is contacted and the order rewritten.

Late entries follow the medical-record rules (timed, marked as late). Pharmacy and nursing have the authority to hold an unsigned or untimed order.""",

        "MOM.5.d": f"""Each order states the name of the medicine, the route, the strength to be administered, and the frequency or time of administration. 'Continue same' or 'as usual' is not an order unless it points to a current, complete charted regimen.

PRN orders include the indication and the maximum frequency. The missing-element check is part of MOM.4.b minimum requirements and of pharmacy verification.""",

        "MOM.6.a": f"""Pharmacy dispenses against a valid order, confirming the right patient, drug, dose, route and frequency, and inspecting the product (integrity, expiry, storage condition) before it leaves the pharmacy or after-hours store.

High-risk items follow MOM.6.e. Floor-stock issue to wards is still a dispense under this policy and is recorded. Dispensing is done in a workspace that limits interruption for high-risk work.""",

        "MOM.6.b": f"""When a recall notice reaches {HOSPITAL} (manufacturer, regulator, or internal quality failure), the {pharm} quarantines affected batch(es) in pharmacy and at floor-stock locations the same shift, identifies patients who received the batch where records allow, and informs the {mso} and treating teams.

Recalled stock is not reissued. The recall file holds the notice, locations checked, quantities recovered, and patient-notification decisions. A recall that sits in an inbox overnight while stock remains on a trolley is not effective handling.""",

        "MOM.6.c": f"""Near-expiry medications are identified by the FEFO system and a {D('monthly')} expiry round. Items that will expire before likely use are withdrawn from clinical areas to pharmacy for disposal or return per supplier rules.

Pharmacy does not issue a medication that cannot be used within its expiry for the intended course. Short-dated items used in emergency trolleys are replaced before expiry, not after.""",

        "MOM.6.d": f"""Every dispensed medication is labelled before it leaves pharmacy (or the after-hours store). The label includes patient identity where the item is patient-specific, name of the medicine, strength, route, frequency / directions, and expiry where relevant.

Ward floor-stock multi-dose containers show drug name, strength, expiry and date of opening where applicable. An unlabelled syringe, cup or strip is not issued. This is a CORE element.""",

        "MOM.6.e": f"""Before a high-risk medication is dispensed, an appropriate person (a second pharmacist, or a pharmacist plus a trained second checker where only one pharmacist is on duty) verifies dose, frequency and route against the order and the patient's record (weight, renal function, allergy as applicable).

The verification is recorded. This is the chapter-intent requirement that every high-risk order is verified. Dispensing a high-risk item on a single unchecked reading is a stop-work trigger.""",

        "MOM.6.f": f"""Unused or discontinued medications returned to pharmacy follow a written return procedure: identity and integrity check, decision to restock or destroy, and a record of the return.

Controlled drugs, reconstituted items, and items that left temperature control are not restocked onto usable shelves. Patient's own medicines follow MOM.7.k, not this return path, unless pharmacy has accepted them into hospital stock under that policy.""",

        "MOM.7.a": f"""Only persons permitted by law and by {HOSPITAL}'s authorised list administer medications. The {ns} and the {ms} hold the list (registered nurses, doctors, and other cadres the organisation names for defined routes).

Students administer only under documented supervision. A person who is not on the list does not give the drug, including 'just this once'. This element names the law; statutory duties remain those of the applicable professional and drugs legislation — this policy is not legal advice.""",

        "MOM.7.b": f"""When a medication is prepared (drawn up, reconstituted, mixed), it is labelled before a second drug is prepared. The label names the drug, strength, patient (if patient-specific), route and time prepared.

Two unlabelled syringes on the same tray are a stop-work condition. This applies in OT, ICU, emergency and wards.""",

        "MOM.7.c": f"""The person administering identifies the patient immediately before administration using the organisation's identifiers (at least two: {D('name and unique identification number')}), matching the order and the labelled product.

Asking only the attendant, or matching the bed number alone, is not identification. If identity cannot be confirmed, administration stops.""",

        "MOM.7.d": f"""Before administration the person checks the labelled product against the medication order (right drug) and physically inspects it (clarity, integrity, expiry, correct formulation). A mismatch or defect stops administration.

This CORE check is separate from strength, route and timing (5.5–5.7) and is recorded by the administration entry.""",

        "MOM.7.e": f"""Strength / dose is verified from the order before administration, including any calculation for weight-based or infusion doses. A second check is used for high-risk medications per the high-risk list.

If the strength on the product does not match the order, do not convert at the bedside unless the conversion is a documented pharmacy-prepared change.""",

        "MOM.7.f": f"""Route is verified from the order before administration. Oral products are not given intravenously; epidural and intravenous lines are distinguished (see 5.8). If the route on the product or device does not match the order, administration stops.""",

        "MOM.7.g": f"""Timing is verified from the order before administration: scheduled time, interval since the last dose, and any 'before food / with food / hold if …' instruction. Early or late doses outside the organisation's allowed window are not given without prescriber review, except documented emergency use.""",

        "MOM.7.h": f"""Before injecting or infusing into a catheter or tubing, staff trace the line from the patient to the source, confirm the intended lumen, and label lines where more than one lumen or device is in use.

Oral syringes are used for oral liquids so they cannot connect to IV ports. This CORE asterisked element is trained at induction for ICU, OT, emergency and ward staff who give IV / epidural / feeding-tube medicines. Untreated mis-connection risk is a stop-work trigger.""",

        "MOM.7.i": f"""Every administration is documented on the medication chart at the time of giving (or immediately after a crash dose): drug, dose, route, time, and the administrator's identifier. Omitted or held doses are documented with the reason.

Documentation is not left to the end of the shift. The portal PDF prints this objective-element letter as 'I.'; {HOSPITAL} treats it as MOM.7.i.""",

        "MOM.7.j": f"""Patients self-administer medications only under written measures: the {dtc} / treating team decides when self-administration is allowed, which drugs, how they are stored at the bedside, and how nursing still records that the dose was taken.

Uncontrolled bedside hoarding of hospital stock is not self-administration. If self-administration is not used at {HOSPITAL}, that decision is written and staff do not permit it informally.""",

        "MOM.7.k": f"""Medications brought from outside are declared at admission, identified by pharmacy or the treating doctor, and either taken into a documented patient's-own-medicines process (labelled, stored securely, ordered on the chart) or sent home / stored away from the bedside.

Staff do not give an unidentified home tablet from a loose strip. The measures are written; this is an asterisked element.""",

        "MOM.8.a": f"""After administration, the patient is monitored for the intended effect and for adverse effects, with intensity matching the drug and the clinical setting (for example post-IV opioid sedation and respiration; post-chemotherapy as the protocol states; routine oral doses as the chart and NEWS/EWS require).

The written guidance names what to watch and when to escalate. Monitoring is recorded. This asterisked element is not satisfied by 'observe generally'.""",

        "MOM.8.b": f"""When monitoring shows the drug is ineffective, poorly tolerated, or causing harm, the treating doctor is informed and the medication is changed, held or the dose adjusted as clinically indicated, with the order rewritten under MOM.5.

Nursing does not silently continue a drug that is causing a clear adverse reaction while waiting for a convenient round.""",

        "MOM.8.c": f"""{HOSPITAL} captures near misses, medication errors and adverse drug reactions in a defined reporting system (incident form / electronic equivalent, plus pharmacovigilance reporting where applicable).

Capture includes events that did not reach the patient (near miss) and reactions that did. The {mso} owns the capture system. Failure to have a working capture route is a CORE gap.""",

        "MOM.8.d": f"""Near misses, medication errors and adverse drug reactions are reported within a specified time frame: {D('unsafe ongoing situations immediately; all other medication incidents the same shift; ADRs as soon as recognised and in any case within 24 hours')}.

The {dtc} may tighten these times. Late discovery is reported when found, marked as delayed, not hidden.""",

        "MOM.8.e": f"""The {mso} collects reports and the {dtc} analyses them {quarterly} (and sooner for a serious event): type, stage (prescribing / dispensing / administration), high-risk drug involvement, and harm.

Analysis looks for system causes, not only individual blame. A pile of unanalysed forms is not compliance.""",

        "MOM.8.f": f"""Corrective and / or preventive actions from the analysis are assigned, timed and closed. Examples: storage separation after a LASA mix-up, a second-check rule after a dose error, a formulary restriction.

The {qc} includes open medication CAPA in the quarterly audit. Repeat events of the same type trigger a deeper review.""",

        "MOM.9.a": f"""Narcotic drugs and psychotropic substances, chemotherapeutic agents and radio-pharmaceuticals are used only under the written safety measures in this policy: authorised prescriber, secure storage, qualified preparation and administration, and complete records (9.b–9.e).

The {pharm} and the {mso} own the combined programme. Services that {HOSPITAL} does not provide (for example radio-pharmaceuticals or chemotherapy) are written as out of scope; those items are then not stocked. Where they are in scope, the full chain applies. This asterisked element is the umbrella.""",

        "MOM.9.b": f"""These agents are prescribed only by caregivers authorised for that class: {D('consultants / privileged doctors for narcotics and psychotropics; oncology-privileged prescribers for chemotherapy; radiation-medicine / nuclear-medicine privileged prescribers for radio-pharmaceuticals')}.

A verbal chemotherapy order is not used except under the documented emergency rule in MOM.4.f. Pharmacy does not dispense these classes against an unauthorised signature.""",

        "MOM.9.c": f"""Narcotics and psychotropics are stored in a locked, access-controlled cupboard or safe, with a register. Chemotherapeutic agents and radio-pharmaceuticals are stored as their licences and manufacturer instructions require, separate from general stock, with access limited to authorised staff.

Keys / access rights are named. Unsecured opioids in a ward drawer are a stop-work trigger. The extra word 'drugs' in the official OE line ('radio-pharmaceuticals drugs') is kept as printed; practice is secure storage of all three classes.""",

        "MOM.9.d": f"""Chemotherapy and radio-pharmaceuticals are prepared in the required facility (for example a cytotoxic cabinet / designated hot lab) by personnel qualified and trained for that preparation, and administered by personnel qualified for that administration.

PPE, spill kits and waste streams are in place before preparation starts. Preparation by an unqualified person, or on an open ward bench, is a stop-work trigger. If {HOSPITAL} does not prepare these on site, preparation is contracted to a named qualified provider and receipt checks still apply.""",

        "MOM.9.e": f"""Usage, administration and disposal of these three classes are recorded: narcotic / psychotropic register (receipt, issue, administration, wastage, balance); chemotherapy administration record (protocol, dose, batch, given-by); radio-pharmaceutical log as the radiation programme requires.

Disposal follows biomedical-waste and, where applicable, AERB / radiation rules. A missing register line is investigated the same shift.""",

        "MOM.10.a": f"""Implantable prostheses and medical devices used at {HOSPITAL} are selected against scientific criteria and national / international recognised guidelines or approvals for that item (for example CDSCO / Medical Devices Rules approvals, BIS where named, and specialty-society indications).

The OT / cath-lab / relevant clinical head and Biomedical keep an approved-item list. An implant without recognised approval is not used except under a documented trial / compassionate pathway approved by the {ms}.""",

        "MOM.10.b": f"""The organisation implements a written mechanism for using these items: request and approval, sterile-supply chain, intra-operative timeout confirming the implant, and recording of identifiers (section 5.4).

The {D('OT In-Charge')} owns the mechanism for surgical implants; the relevant lab / cath-lab in-charge owns it for devices used there. This asterisked element is the procedure, not only the criteria in 5.1.""",

        "MOM.10.c": f"""The patient and family are counselled before implantation on what will be implanted, expected benefit, material risks, alternatives, and precautions after implant (MRI compatibility, anticoagulation, infection signs, follow-up).

Counselling is recorded in the medical record (consent process may sit with PRE; this policy owns the implant-specific content). Emergency life-saving implants are counselled as soon as practicable.""",

        "MOM.10.d": f"""Batch and serial number (or equivalent unique identifier) of the implantable prosthesis or medical device are recorded in three places: the patient's medical record, the master implant logbook, and the discharge summary.

A sticker from the implant pack is the usual source; if it is lost, pharmacy / stores trace the batch before the patient leaves. Missing identifiers are a reportable gap.""",

        "MOM.10.e": f"""When an implant or device is recalled, the {D('OT In-Charge / Biomedical')} traces every affected batch from the master logbook, contacts the treating team and, where required, the patient, and follows the supplier / regulator instruction (explant, extra surveillance, or information only).

The recall file holds the notice, patients identified, actions taken and closure. This asterisked Achievement element is evidenced by a drill or a real recall file, not by a sentence in this policy.""",

        "MOM.11.a": f"""Medical supplies and consumables are acquired through a defined process: approved vendors, specifications, receipt check (identity, quantity, integrity, expiry where applicable), and entry into stores.

The {D('Stores In-Charge')} owns acquisition. Informal local purchase is allowed only through the documented emergency-purchase path and is entered the next working day. This asterisked element is the written acquisition process in use, not a poster.""",

        "MOM.11.b": f"""Supplies and consumables are used as intended: sterile items stay sterile until use; single-use items are not reused; opening-date is written on multi-use bottles where the manufacturer requires.

User departments do not improvise a device against its labelled use. Incidents of unsafe use are reported under the incident system.""",

        "MOM.11.c": f"""Stores and user locations keep supplies in a clean, safe and secure environment and follow manufacturer recommendations (temperature, humidity, light, upright storage, first-expiry). Sterile stores are physically separate from dirty utility.

Food and medications are not mixed into the general consumable racks except where pharmacy owns the item under MOM.3.""",

        "MOM.11.d": f"""Inventory control uses defined stock levels, FEFO, and a documented indent cycle. Expiry and damaged stock are removed on the {D('monthly')} stores round. Floor hoarding of sterile packs past a usable dating is returned to stores.

The {D('Stores In-Charge')} can show movement from receipt to issue for sampled items.""",

        "MOM.11.e": f"""Before issue and at defined intervals, staff verify the condition of supplies and consumables: package integrity, sterility indicators where present, expiry, and any cold-chain logger for items that need it.

Failed items are quarantined, not used. User departments may refuse a pack that fails condition check at the point of use and return it with a note.""",
    }


__all__ = ["method_bodies"]
