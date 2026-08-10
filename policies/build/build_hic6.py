# -*- coding: utf-8 -*-
"""Builds the HIC.6 master policy draft: JSON for review + SQL for the Supabase SQL Editor.

Column types confirmed against the live schema (2026-08-10):
  oe_codes        text[]
  procedure_steps text[]
  oe_mapping      jsonb

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition (August 2022),
Chapter 5 Hospital Infection Control, standard HIC.6 and OEs HIC.6.a-e, read from the standards
PDF at printed page 96 (PDF page index 102) in the local copy at
"C:/Users/SERVER/Desktop/NABH/SHCO-Standards-3rd-Edition.pdf".

Levels, verified against the PDF and against shco_full_oes: a Commitment, b Core, c Commitment,
d Commitment, e Commitment. FOUR OF THE FIVE OEs CARRY THE ASTERISK -- b, c, d and e. This
standard has no single documented-evidence anchor, and the draft therefore builds evidence depth
into four separate blocks rather than concentrating it in one as HIC.5 did on outbreaks.

The HIC.6.e asterisk was missing from shco_full_oes until the ten-chapter audit of 2026-08-10
corrected it; see scripts/master-policy-todos.md. Both sources now agree.

The five optional sections (definitions, training_competency, resources_required,
monitoring_audit, exceptions) are deliberately left unset, matching HIC.1-5.
"""
import json
import re

from pathlib import Path

# Output locations, resolved from this file rather than the working directory,
# so the build produces the same result regardless of where it is run from.
_HERE = Path(__file__).resolve().parent          # policies/build
_POLICIES = _HERE.parent                         # policies
DRAFTS = _POLICIES / "drafts"
SQL_OUT = _POLICIES / "sql"

STANDARD_CODE = "HIC.6"
CHAPTER = "HIC"
OE_CODES = ["HIC.6.a", "HIC.6.b", "HIC.6.c", "HIC.6.d", "HIC.6.e"]

POLICY_TITLE = "Sterilisation and Disinfection of Instruments, Equipment and Devices"

PURPOSE = """This document sets out how {{HOSPITAL_NAME}} makes a used instrument safe to use on the next patient. It governs the whole of that journey — the treatment an item receives at the moment it is put down, its transport, its cleaning, its inspection, its packaging, the process that disinfects or sterilises it, the conditions it is stored in, the check made before it is used again, and what happens when any of that fails.

A sterile instrument is the one infection control measure a patient cannot observe, cannot question, and has no way to verify. Every other protection in this hospital is visible to someone: hand hygiene can be watched, a catheter dressing can be inspected, an isolation sign can be read. Sterility is invisible, is destroyed silently, and is discovered to have failed only after the harm is done. That is why this document is built on records rather than assurances, and why it treats an unverifiable claim of sterility as equivalent to a claim of non-sterility.

This document also sets out what {{HOSPITAL_NAME}} does when the sterilisation system is found to have broken down after items have already been issued — how far back the failure reaches, how those items are retrieved, how patients already exposed are assessed, and who decides.

The other infection control policies of {{HOSPITAL_NAME}} rely on this one. Three of them state in terms that instrument reprocessing is governed here. This document is where that promise is met."""

SCOPE = """This policy applies to every reusable instrument, item of equipment and device used on a patient of {{HOSPITAL_NAME}}, wherever it is processed — in a central sterile supply department, in an operating theatre sub-sterile area, in a ward or clinic treatment room, in the labour room, in dialysis, in the dental or endoscopy suite, or by an external provider under contract.

It binds every person who handles a device between one patient and the next: processing technicians, nurses, theatre staff, clinicians who perform point-of-use treatment, porters who transport containers, and the staff of any outsourced processing service.

It applies to items owned by {{HOSPITAL_NAME}} and equally to loaner, consignment, trial and clinician-owned instrument sets brought into the hospital.

What this policy owns, and no other policy of {{HOSPITAL_NAME}} does:

- the classification of every reusable item as critical, semi-critical or non-critical, and the level of processing each classification requires;
- the internal zoning of the processing area and the direction of flow within it;
- every stage of the reprocessing cycle from point-of-use treatment to issue;
- the selection of disinfectants and sterilants for instruments and devices, as distinct from those used on the environment;
- the monitoring and validation of sterilisation, and the qualification of the equipment that performs it;
- the position of {{HOSPITAL_NAME}} on the reprocessing of devices labelled single-use;
- the recall of processed items when the sterilisation system is found to have failed.

Four boundaries need stating explicitly, because in each case another policy of {{HOSPITAL_NAME}} governs something adjacent and a reader can reasonably arrive at either document.

Building flows against unit zoning. The infection prevention and control in support services policy owns the separation of clean and contaminated flows across the hospital as a whole — the routes used to move waste, soiled linen and used instruments, the provision of dirty utility rooms, and the rule that sterile supplies are never stored in a sluice or waste holding area. This policy owns the zoning inside the processing area itself: the three zones, the barrier between them, the requirement that an item never moves backwards through them, and the ventilation and pressure relationship that supports it. The building's flows deliver items to this policy's door; what happens inside that door is governed here.

Environmental disinfection against device disinfection. The support services policy owns the disinfectants used on floors, surfaces and fittings, their working concentrations and contact times. This policy owns the disinfectants and sterilants applied to instruments and devices, including the choice of high-level disinfectant. The two sets of agents are not interchangeable, and the support services policy says so and points here. Neither document restates the other.

Clinical practice against reprocessing method. The prevention of healthcare associated infections policy owns what is done to the patient — aseptic technique, the sterile field, surgical hand preparation, the confirmation that an item is sterile before it is used, and the care of devices while they are in the patient. This policy owns how the item became sterile and how it is proved to have been. Where that policy requires ventilator accessories, humidifiers, heat and moisture exchangers, nebuliser chambers and resuscitation bags to be reprocessed between patients, this policy supplies the method and the record.

Outbreak quarantine against sterilisation recall. The surveillance policy quarantines a suspect product, device or batch during an outbreak investigation, on suspicion that it is a source. This policy recalls processed items when the sterilisation system itself is found to have failed. The trigger is different — an epidemiological signal in one case, a process failure in the other — although the physical act of retrieval is the same. Each route hands to the other where the evidence points that way, and neither restates the other's procedure.

What this policy does not cover: the governance, staffing, budget and consumable stock of the infection control programme, including the procurement and expiry checking of sterilisation supplies and indicators; the practices set out in the clinical areas policy; environmental cleaning, laundry, kitchen, water systems and biomedical waste; the counting of infections and the investigation of outbreaks; and occupational health, immunisation and post-exposure management for staff injured during reprocessing. Each has its own policy."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} holds that an item is sterile only where the hospital can show how it was made so. Sterility is not a property that can be inspected, and a pack that looks correct proves nothing about the process that produced it. The record is the only evidence there is, and an item whose processing cannot be evidenced is treated as non-sterile.

{{HOSPITAL_NAME}} commits to cleaning before anything else. No sterilisation or disinfection process can be relied on where soil, blood or biofilm remains, because organic matter shields organisms from the agent that is meant to kill them and neutralises many agents outright. A dirty instrument that has been through a sterilisation cycle is a dirty instrument. Cleaning is therefore treated as the critical stage of the whole cycle rather than as preparation for it.

{{HOSPITAL_NAME}} commits to processing every device according to the instructions of the organisation that made it. A device manufacturer's validated reprocessing instructions are specific to that device's materials, lumens, joints and coatings, and are not interchangeable between devices that look similar. Where the instructions for use cannot be obtained, or specify a process {{HOSPITAL_NAME}} cannot perform, the device is not reprocessed and not used, and the position is recorded rather than worked around.

{{HOSPITAL_NAME}} commits to releasing a load on evidence and not on appearance. A load is released by a named person against complete physical, chemical and, where required, biological results. Where any result is missing, unreadable or out of specification, the load is not released, whatever the operational pressure. {{HOSPITAL_NAME}} states plainly that pressure to release an unverified load is a patient safety hazard in its own right, and that no member of staff will be criticised for refusing to do so.

{{HOSPITAL_NAME}} does not reprocess devices labelled for single use except under a written protocol expressly approved for that device category. The default is that such a device is used once and discarded. Reprocessing a device that was never designed to survive it risks material degradation, retained contamination in lumens that cannot be cleaned, and a loss of function that is not visible before use, and the fact that a device appears undamaged is not evidence that it is safe.

{{HOSPITAL_NAME}} treats a sterilisation failure as a recall event and not as a paperwork exception. When the system is found to have broken down, the affected items are quarantined immediately, the recall reaches back to the last load with a satisfactory result, and where items have already been used the patients concerned are assessed rather than the matter being closed on the ground that nothing appears to have happened.

{{HOSPITAL_NAME}} states that reporting a processing error, a failed indicator or a doubt about a load is expected conduct. The person who raises it has prevented harm. Discipline is directed at concealment, never at disclosure, because a processing department that fears reporting will produce the one thing this policy exists to prevent — an unrecorded failure."""

PROCEDURE_STEPS = [
"""1. The decontamination life cycle at {{HOSPITAL_NAME}}

Every reusable item at {{HOSPITAL_NAME}} passes through the same sequence, in the same order, without exception:

point-of-use treatment; transport in containment; receipt and sorting; cleaning; rinsing; inspection and functional check; assembly; packaging; disinfection or sterilisation; cooling and post-cycle check; storage; issue; check before use.

The sequence is a cycle rather than a list, because an item leaving the patient re-enters it at the first stage. It has three properties that govern the whole of this policy.

It is unidirectional. An item moves forward through the stages and never backwards. An item that has entered the clean side and is then found soiled, dropped, or of doubtful status does not rejoin the flow where it left; it returns to the beginning and is processed again in full.

It is sequential in effect, not merely in order. Each stage depends on the one before it having been done properly, and no later stage can compensate for an earlier failure. Packaging cannot correct poor cleaning. A sterilisation cycle cannot correct poor packaging. This is why cleaning, which involves no antimicrobial claim at all, is the stage on which everything else rests.

It is recorded at every stage. The record is what allows an item in a patient's body to be traced back to the load that processed it, and the load to be traced forward to every item it contained. Without that link in both directions the recall required at steps 31 to 37 cannot be performed, and the hospital's only remaining option on a failure is to recall nothing or to recall everything.

Responsibility for the cycle sits with the person in charge of the processing area of {{HOSPITAL_NAME}}, whose title and reporting line are [Hospital to define]. Individual stages are performed by trained staff who sign for the stage they performed.""",

"""2. Classifying devices — critical, semi-critical, non-critical

{{HOSPITAL_NAME}} classifies every reusable item by the risk its use presents, and the classification determines the minimum level of processing. The classification is the one in general use in infection control and turns on what tissue the item contacts:

- Critical. Items that enter sterile tissue, the vascular system, or a normally sterile body cavity. Surgical instruments, implants, needles, cardiac and urinary catheters, and the inner components of instruments used in such procedures. These items must be sterile at the point of use, because any organism present is delivered directly to tissue that has no defence against it. They are sterilised, preferably by moist heat, and where the material cannot tolerate heat, by a validated low-temperature process. Sterilisation is the requirement; high-level disinfection is not an acceptable substitute for a critical item.
- Semi-critical. Items that contact intact mucous membranes or non-intact skin but do not penetrate sterile tissue. Flexible endoscopes, laryngoscope blades, respiratory therapy and anaesthesia equipment, vaginal and rectal probes, and reusable oral instruments. These require at minimum high-level disinfection, which destroys all microorganisms other than large numbers of bacterial spores. Where the item tolerates it, {{HOSPITAL_NAME}} sterilises in preference to disinfecting, because sterilisation carries a margin the mucosal route does not always forgive.
- Non-critical. Items that contact intact skin only. Blood pressure cuffs, stethoscopes, pulse oximeter probes, bedpans, patient furniture and the external surfaces of equipment. Intact skin is an effective barrier, so these require cleaning followed by low- or intermediate-level disinfection.

{{HOSPITAL_NAME}} maintains a written classification register listing every reusable item in use, its class, the processing method required, the manufacturer's instructions relied on, and the department that holds it. The register is approved by the Infection Prevention and Control Committee, is reviewed at least annually, and is updated whenever a new device is introduced. A device that is not on the register is not in service.

Three rules of application:

- classification follows intended use, not the department. The same instrument is critical in theatre and critical in a treatment room; the risk belongs to the tissue contacted, not the location;
- where an item's classification is genuinely uncertain, it is assigned to the higher class until the Infection Control Officer determines otherwise in writing;
- an item that will be used on a patient in a procedure of higher risk than its class assumes is processed to the higher standard for that use, and the register records the circumstance.

The choice of high-level disinfectant, and the selection of agents for instruments generally, is made under this policy at steps 15 and 16. The support services policy governs disinfectants used on the environment and expressly points here for devices; the two sets of agents are not interchangeable.""",

"""3. The processing area — space and zoning

{{HOSPITAL_NAME}} provides a defined area for reprocessing, physically separated from patient care and from clean storage, and laid out in three zones through which work moves in one direction only.

Zone 1, decontamination — the dirty zone. Receipt, sorting, disassembly, manual cleaning, ultrasonic cleaning and mechanical washing. Everything in this zone is treated as contaminated. It contains the sinks, the washer-disinfector loading side, the compressed air and water lines for lumen flushing, a hand-wash basin, and an eyewash facility. Staff wear the protective equipment required for the zone, which the occupational policy of {{HOSPITAL_NAME}} specifies and this policy does not restate.

Zone 2, clean assembly and packing. Inspection, functional testing, assembly of sets, packaging and loading. Items arrive here only through the barrier from zone 1, having been cleaned and dried. Nothing contaminated enters this zone at any time.

Zone 3, sterile storage. Cooled, processed items held until issue. Access is restricted to staff of the processing area, and the zone is not a thoroughfare.

The zones are separated by a physical barrier — a wall with a pass-through hatch, a double-door washer-disinfector, or at minimum a full-height partition with a controlled doorway. Where the existing building of {{HOSPITAL_NAME}} cannot provide a physical barrier, separation is achieved by a documented combination of distance, dedicated benching, defined direction of work and separation in time, the compensating measures are written down, and the limitation is entered in the infection control risk register and reviewed by the Committee. It is not left as an informal practice.

The layout of {{HOSPITAL_NAME}} is recorded on a marked drawing showing the three zones, the barrier, the transfer points and the direction of flow, and the drawing is held with this policy — [Hospital to define — attach or reference the marked layout drawing of the processing area].

The rule that governs all of it: an item never moves from a later zone to an earlier one and is never carried back through a barrier. An item on the clean side whose status becomes doubtful for any reason returns to zone 1 by the external route and is processed again from the beginning.

The separation of clean and contaminated flows in the rest of the hospital — the corridors, lifts, trolleys and storage that bring items here and take them away — is governed by the support services policy of {{HOSPITAL_NAME}} and is not restated here.""",

"""4. The processing area — ventilation, environment and utilities

The conditions in the processing area are engineering controls, and {{HOSPITAL_NAME}} treats them as such: specified in writing, monitored, and recorded.

Air. Air flows from clean to dirty and never the reverse. The clean assembly and sterile storage zones are maintained at a positive pressure relative to the decontamination zone, which is itself maintained negative to the corridor so that aerosols generated during cleaning are not carried outward. The air change rate for each zone, the pressure differentials, and the filtration provided are specified by the engineering service of {{HOSPITAL_NAME}} against the standard in force and the design of the plant — [Hospital to define — state the air change rate and pressure differential specified for each zone, and the standard relied on]. Pressure relationships are verified at a stated frequency and the verification recorded, because a pressure gradient is invisible and fails silently.

Temperature and humidity. The clean assembly and sterile storage zones are held within a defined range, monitored and recorded. Humidity matters in both directions: too high and packaging absorbs moisture and loses its barrier property, too low and static and particle generation increase. The ranges adopted at {{HOSPITAL_NAME}} are [Hospital to define — state the temperature and relative humidity ranges for the clean and storage zones, against the standard in force], with the excursion response and the record of monitoring.

Water. Water quality affects both cleaning and sterilisation. Potable water is used for initial cleaning; the final rinse of items destined for sterilisation uses treated water of a quality that does not leave mineral deposits or endotoxin on the instrument, and steam is generated from water treated to the specification the steriliser manufacturer requires. Deposits and staining on instruments are usually a water problem and are investigated as one. The water treatment in use, its specification and its testing regime are [Hospital to define — state the water treatment provided for final rinse and for steam generation, its specification, and the testing frequency].

Utilities and drainage. The area has drainage able to take the discharge of the machines installed, power provision including any requirement for uninterrupted supply, and compressed air where lumened devices are processed. Loss of any utility mid-cycle is treated as a cycle failure at step 30.

Environmental cleaning of the processing area itself is performed to the support services policy, at a frequency reflecting the zone, and the record is held by the processing area.""",

"""5. Processing outside the central area

Where {{HOSPITAL_NAME}} processes any item outside the central processing area — in a theatre sub-sterile room, a dental or endoscopy suite, a labour room, a dialysis unit, a clinic treatment room, or a ward — the arrangement is written down and approved rather than assumed.

{{HOSPITAL_NAME}} centralises processing so far as its size and layout allow, because a single controlled area with trained staff, monitored equipment and complete records is more reliable than several partial ones. Decentralised processing tends to fail in the same four ways: no separation of clean from dirty, no trained dedicated operator, monitoring that is performed but never reviewed, and records that cannot be linked to a patient.

For each location where processing occurs outside the central area, the following is recorded — [Hospital to define — list every location where reprocessing occurs outside the central area, and for each, the items processed, the method, the operator, the monitoring applied and the records kept]:

- the items processed there and their classification;
- why they are processed there rather than centrally;
- the method used and the manufacturer's instructions relied on;
- how clean and contaminated items and work surfaces are kept apart in that space, given that the three-zone layout of step 3 will not be reproducible;
- who performs the processing, their training and their competency assessment;
- the monitoring applied, which is the same monitoring required at steps 24 to 30 and is not reduced because the location is small;
- where the records are held, and how an item processed there can be traced to the patient it was used on, which is what makes the recall at steps 31 to 37 possible in that location.

Bench-top sterilisers used outside the central area are subject to this policy in full — qualification, routine monitoring, load records, release by a named person, and recall. A small steriliser is not a lesser one, and the commonest reason a recall cannot be executed is a bench-top unit whose loads were never linked to patients.

Any location that cannot meet these requirements ceases processing and sends its items to the central area. The Infection Control Officer decides this, and the decision is recorded.""",

"""6. Point-of-use treatment and transport

Reprocessing begins at the point of use, in the seconds after an item is put down, and not at the door of the processing area.

Soil that is allowed to dry on an instrument becomes substantially harder to remove, and dried blood, saline and tissue protect organisms from every subsequent process. Salt-containing solutions left in contact with instruments also cause pitting and corrosion that shortens their life and creates surfaces that cannot be cleaned. The user of the item, not the processing staff, is responsible for preventing this.

Immediately after use, the clinical team at {{HOSPITAL_NAME}}:

- removes gross soil at the point of use by wiping with a moistened sponge or cloth, and flushes lumens where the device has them;
- keeps instruments moist until they reach cleaning, by covering with a moistened towel, by using a product intended to keep soil from drying, or by immersion where the device permits it. Instruments are not left to soak in saline;
- separates sharps and delicate items so that neither injures staff nor is damaged by heavier instruments;
- disassembles items so far as the manufacturer's instructions require, opens hinged instruments, and retracts or dismantles multi-part devices;
- keeps sets together and complete, so that missing instruments are identified now rather than at assembly.

Transport is in a closed, leak-proof, puncture-resistant container or trolley, labelled to identify the contents as contaminated, and moved by the route the support services policy defines for used instruments. Items are never transported uncovered, in an open tray, or in the hands.

Where an item cannot reach the processing area promptly, the delay and the method used to keep it moist are recorded, and the maximum delay permitted at {{HOSPITAL_NAME}} before an item must be treated as requiring extended cleaning is [Hospital to define].

An item received in the processing area with dried soil is returned to the clinical area's attention through the record at step 7, not simply cleaned harder. The failure is at the point of use and is corrected there.""",

"""7. Receipt and sorting in the decontamination zone

Items arrive in the decontamination zone in their transport containers and are received by a named member of the processing staff, who records the arrival: the sending department, the date and time, the set or item identity, and the condition on arrival.

Receipt is a check, not merely an entry. The receiving staff member confirms the set against its checklist, notes items missing or additional, and records any of the following as a deviation requiring feedback to the sending area: dried soil, items not disassembled, sharps loose in the tray, instruments damaged, or a container that leaked in transit. These deviations are trended and reported to the Infection Prevention and Control Committee, because they are a measure of whether step 6 is actually happening and are the earliest available warning that it is not.

Sorting separates items by the processing they require — by material, by whether they can be machine-washed, by whether they have lumens, by whether they are heat-tolerant, and by the manufacturer's instructions applying to each. Items requiring manual cleaning only are separated from those going to the washer-disinfector, and delicate and microsurgical instruments are kept apart from general instruments throughout.

Single-use items are removed at this stage and discarded as biomedical waste under the support services policy. They do not enter the cleaning process, and the presence of single-use items in the reusable stream is recorded as a deviation and addressed under step 21.

Staff working in this zone wear the protective equipment specified for it and follow the exposure and injury procedures of the occupational health policy of {{HOSPITAL_NAME}}; a sharps injury sustained during sorting is managed under that policy and is not dealt with here.

Nothing leaves this zone in the direction of the clean side until it has completed cleaning and drying and passed the inspection at step 10.""",

"""8. Cleaning — manual

Manual cleaning is used for items the manufacturer's instructions require to be cleaned by hand, for delicate items, for items with lumens or channels needing brushing, and where a washer-disinfector is not available.

The method at {{HOSPITAL_NAME}}:

- the item is fully disassembled to the extent the instructions require, and hinged instruments are opened;
- cleaning is performed under the surface of the water, not above it, so that splashing and aerosol generation are minimised;
- an enzymatic or neutral pH detergent intended for medical instruments is used, prepared at the dilution and temperature the product specifies, and changed at the frequency stated or whenever visibly soiled. Household detergents, abrasive agents and steel wool are not used, and neither is any agent that will damage the instrument's finish;
- brushes are of the size and material specified for the lumen or surface, are themselves cleaned and disinfected or discarded at the end of each session, and are not shared between the dirty and clean sides;
- lumens are brushed through their full length in one direction, then flushed until the effluent runs clear;
- the item is rinsed thoroughly, with the final rinse in water of the quality step 4 specifies for items going to sterilisation, and is then dried, because residual moisture interferes with sterilisation, promotes corrosion, and supports microbial growth in storage.

The detergent in use at {{HOSPITAL_NAME}}, its dilution, its temperature and its contact time are [Hospital to define — state against the product instructions and the device manufacturer's instructions for use], and the same information is displayed at the sink.

Two rules that are commonly breached and matter:

- water temperature for the wash is kept below the point at which protein coagulates, since hot water fixes blood to the instrument rather than removing it. The temperature range is taken from the detergent's instructions;
- an instrument that cannot be cleaned — because a lumen cannot be reached, a joint cannot be opened, or a coating has degraded — is removed from service under step 10 and is not sent forward in the hope that the sterilisation cycle will compensate.""",

"""9. Cleaning — mechanical, and verification that cleaning worked

Where the device permits it, {{HOSPITAL_NAME}} cleans by machine in preference to by hand, because a machine performs the same cycle every time, records what it did, exposes staff to less risk, and does not tire.

Ultrasonic cleaners are used for fine, hinged and serrated instruments where the manufacturer permits, after gross soil has been removed, since ultrasonic energy does not remove heavy soil and cavitation is impeded by it. The solution is degassed after filling, is changed at the stated frequency and whenever visibly soiled, and instruments of dissimilar metals are not mixed in the same basket. Items are rinsed after the ultrasonic stage; the bath is not a rinse.

Washer-disinfectors are used for heat-tolerant items the manufacturer permits to be machine-processed. Loading follows the machine's instructions: items open and disassembled, lumened devices connected to the irrigation manifold, nothing shadowing anything else, baskets not overfilled. The cycle, its stages and its thermal disinfection parameters are those the machine and the device instructions specify, and the printout or data log is retained with the load record.

Machine performance is checked and recorded, not assumed:

- a daily check of the machine before the first load — spray arms turning freely, jets unblocked, filters and strainers clear, detergent and rinse aid present;
- routine verification of the wash process at the frequency the machine's instructions and the standard in force require, using a soil or process test device where one is specified;
- verification of the thermal disinfection stage against the machine's own recorded parameters;
- periodic qualification and requalification of the machine as required by step 29.

Cleaning verification. Because visual inspection alone will not detect residual protein inside a lumen or a box joint, {{HOSPITAL_NAME}} uses a cleaning verification method at the frequency stated in the schedule at step 24 — [Hospital to define — state the cleaning verification method used, the items and frequency to which it is applied, and the acceptance criterion, against the standard in force]. A failed verification is treated as a process failure under step 30: the affected items are recleaned, the cause is investigated, and the result is recorded.

Where a machine's cycle aborts or its parameters fall outside specification, the entire load is treated as uncleaned, is returned to the beginning, and the event is recorded.""",

"""10. Inspection, functional check and assembly

No item crosses to the clean side until it has been inspected, and inspection is the last opportunity to detect a fault before the item reaches a patient.

Each item is examined under good lighting, with magnification where the item is fine, for:

- residual soil, particularly at box joints, serrations, hinges, lumen openings and the junction of handle and shaft. Any soil found returns the item to cleaning in full, not to a local wipe;
- moisture, since an item packed damp will not sterilise reliably and may emerge wet;
- damage — cracks, pitting, corrosion, chipped plating, bent shafts, worn insulation on electrosurgical instruments, blunt or misaligned cutting edges;
- completeness, against the set checklist.

Function is tested, not merely appearance: scissors cut cleanly through the test material, forceps and clamps align and hold at each ratchet, hinged instruments move freely without excessive play, retractors lock, insulated instruments are checked for insulation integrity, and any instrument with a working channel is confirmed patent.

An item failing inspection is removed from the set, tagged, recorded and sent for repair or disposal. It is not returned to circulation "for now", and the set is not issued incomplete unless the checklist is amended and the amendment recorded. Instrument repair and replacement is requisitioned through the process the programme policy of {{HOSPITAL_NAME}} establishes for infection control consumables and equipment.

Assembly follows the set checklist, which lists every item, its quantity and its position. The checklist is the document a theatre nurse will count against, and it is what makes a missing instrument visible before rather than after a procedure. Instruments are assembled open or unlocked so that the sterilant reaches every surface; a closed ratchet or a clamped hinge is a surface the process will not reach.

The person performing inspection and assembly records having done so against the set, by name or identifier. Where an item is found damaged repeatedly, or a set repeatedly incomplete, the pattern is reported to the Committee.""",

"""11. Packaging

The purpose of packaging is to allow the sterilant in, and then to keep everything else out until the pack is opened at the point of use. A pack that fails at either does not deliver a sterile item.

{{HOSPITAL_NAME}} uses packaging validated for the sterilisation method it will undergo, compatible with the item, and used within the limits the packaging manufacturer states. The systems in use are [Hospital to define — state the packaging systems used for each sterilisation method, and the maximum pack size and mass permitted, against the manufacturer's instructions].

Requirements common to every packaging system:

- the material permits penetration of the sterilant and its removal at the end of the cycle, resists tearing and puncture in handling, and provides an effective microbial barrier while it remains intact and dry;
- packs are assembled so that air can be removed and the sterilant can reach every surface — instruments open, heavy items not resting on lighter ones, absorbent material where condensate will form, and nothing packed so tightly that it forms a barrier;
- pack size and mass stay within the limits validated for the cycle, since a pack that is too large or too dense will not achieve the conditions at its centre however long the cycle runs;
- an internal chemical indicator is placed inside every pack in the position most difficult for the sterilant to reach, and an external indicator is applied to the outside — the two have different purposes and step 26 sets out what each does and does not prove;
- the pack is sealed by the method the material requires, and seals are checked. Pins, staples and paper clips are never used to close a pack, because they perforate the barrier.

Rigid containers are inspected before each use for gasket integrity, latch function and filter condition, and the filter or valve is changed at the interval the manufacturer states. A container with a damaged gasket does not maintain a barrier and is removed from service.

Labelling. Every pack is labelled before it enters the steriliser with: the contents or set identity; the steriliser identity; the cycle or load number; the date of processing; the expiry or review date determined under step 18; and the identity of the person who assembled and packed it. The label is what makes recall possible and is written so that it survives the process legibly. A pack whose label is unreadable after processing is not issued.""",

"""12. Choosing the sterilisation method, and loading

The method is chosen by the device manufacturer's instructions, not by convenience or by what is free. Where the instructions permit more than one method, {{HOSPITAL_NAME}} selects moist heat, because it is the most reliable, the fastest to verify, the least toxic and the least costly, and reserves low-temperature methods for items that cannot tolerate it.

{{HOSPITAL_NAME}} does not sterilise an item by a method the manufacturer has not validated for it. Doing so risks a process that does not sterilise, a device that is damaged in a way not visible from outside, or a residue that is itself harmful.

The sterilisers in service at {{HOSPITAL_NAME}}, with their method, capacity, cycle types and location, are [Hospital to define — list each steriliser with its identifier, method, cycles available and location].

Loading rules, which apply to every method:

- the load is composed as the cycle was validated — a mixed load of textiles and instruments behaves differently from either alone, and the cycle used is the one validated for the load type;
- items are placed so that the sterilant circulates freely: packs not touching the chamber wall, not stacked in a way that traps air, spaced to allow flow between them, and within the shelf loading pattern the steriliser manufacturer specifies;
- containers and bowls are placed on edge or inverted so that condensate drains rather than pooling;
- peel pouches are placed on edge, paper to plastic, and are not stacked flat one on another;
- the chamber is not overloaded, and the load's total mass stays within the validated limit;
- a process challenge device is included where the schedule at step 24 requires one, in the location the standard specifies.

Immediate-use steam sterilisation — the short, unwrapped cycle sometimes used for an instrument needed urgently — is not routine practice at {{HOSPITAL_NAME}} and is not used to compensate for insufficient instrument stock, which is the reason it is most often used. Where it is used, it is only for an item that cannot be processed in time by the normal cycle, never for an implant, and it is recorded with the reason, the item, the patient, the cycle parameters and the indicator result, and the record is reviewed by the Infection Control Officer. Repeated use for the same reason is treated as an inventory problem and referred to management. Whether {{HOSPITAL_NAME}} permits it at all, and under what limits, is [Hospital to define].""",

"""13. Moist heat sterilisation

Moist heat is the primary sterilisation method at {{HOSPITAL_NAME}}. Saturated steam under pressure destroys microorganisms by denaturing protein, and it does so reliably because the conditions required can be measured directly and continuously.

Three conditions must be met together, and the failure of any one invalidates the cycle:

- air must be removed from the chamber and from within the load. Air is the enemy of steam sterilisation: a residual air pocket is a cold spot, and steam will not reach the surfaces inside it whatever the chamber gauge reads. This is why air-removal performance is tested separately at step 28;
- steam must be saturated and of the correct quality — neither wet, which soaks packaging and causes wet packs, nor superheated, which behaves as hot air and sterilises far less effectively at the same indicated temperature;
- the temperature must be held at every point in the load for the full exposure time. Time and temperature are related but not interchangeable, and a cycle that reaches temperature briefly has not sterilised.

The cycle parameters — temperature, exposure time and drying time for each cycle type — are those specified by the steriliser manufacturer for the load concerned and by the instructions for use of the devices in the load, taken together, and are recorded in the written guidance of {{HOSPITAL_NAME}}: [Hospital to define — state each cycle type in use with its temperature, exposure time and drying time, taken from the steriliser manufacturer's specification and the device instructions for use]. This policy deliberately does not state figures, because they are specific to the machine, the cycle and the load, and a number transcribed from elsewhere is a patient safety hazard rather than a documentation convenience.

Drying is part of the cycle and not an optional extension of it. A pack removed wet has lost its barrier: moisture wicks organisms from the outside surface through to the contents. Wet packs are treated as unsterile at step 17 and are investigated, since the cause is usually loading, load composition, steam quality or a drying stage cut short.

Every cycle is recorded — steriliser identity, cycle number, date, time, load contents, cycle type, the parameters achieved as shown by the machine's own record, the indicator results, and the operator. Release of the load is governed by step 17 and by the monitoring at steps 24 to 30.""",

"""14. Low-temperature sterilisation

Items that cannot tolerate moist heat are sterilised by a low-temperature method validated by the device manufacturer for that item. Where {{HOSPITAL_NAME}} holds such items and does not have the corresponding capability, they are sent to an external provider under step 38 or replaced with heat-tolerant alternatives; they are not processed by an unvalidated substitute.

The methods available in practice differ in what they can penetrate, what they are compatible with, and what they leave behind, and the differences decide which items each can process:

- ethylene oxide penetrates well, including long narrow lumens, and is compatible with a wide range of materials, but the cycle is long, the gas is toxic, flammable and a recognised carcinogen, and every load requires an aeration stage to remove residue before the item may be used. Where {{HOSPITAL_NAME}} uses it, the installation, ventilation, exposure monitoring for staff, and the aeration time are controlled under the occupational and facility requirements applying to it, and the aeration stage is never shortened;
- hydrogen peroxide based processes operate at low temperature, leave no toxic residue, and have short cycles, but are absorbed by cellulose so paper, linen and cotton cannot be processed, and penetration of long or narrow lumens is limited to what the process is validated for. The lumen limits stated by the equipment manufacturer are observed exactly;
- liquid chemical sterilant immersion is used only where no alternative exists. It is difficult to control and to verify, the item cannot be packaged and so is sterile only at the moment it leaves the solution and is subject to recontamination in the rinse and transfer, and it produces no pack that can be stored. It is not used for any item that can be processed by another method.

For each low-temperature process in use at {{HOSPITAL_NAME}}, the following is recorded: the method, the equipment, the cycle parameters from the manufacturer, the items validated for it, the packaging validated for it, the monitoring applied under steps 24 to 30, and the aeration or rinse requirement — [Hospital to define — state each low-temperature method in use with its cycle parameters, permitted items and packaging, from the manufacturer's specification].

Every low-temperature cycle is recorded and released on the same basis as a steam cycle, with the biological indicator appropriate to the process.""",

"""15. High-level disinfection of semi-critical devices

Semi-critical items that cannot be sterilised undergo high-level disinfection, which destroys all microorganisms except large numbers of bacterial spores. The commonest examples at {{HOSPITAL_NAME}} are flexible endoscopes, laryngoscope blades and handles where the manufacturer classifies them so, respiratory and anaesthesia equipment, and reusable probes used against mucous membranes.

This is the step that the prevention of healthcare associated infections policy of {{HOSPITAL_NAME}} relies on when it requires humidifiers, heat and moisture exchangers, nebuliser chambers, resuscitation bags and ventilator accessories to be reprocessed between patients. The method is here; that policy does not restate it, and the reprocessing record required there is the record produced here.

Cleaning first, without exception. High-level disinfection applied to an item that has not been thoroughly cleaned does not work. For lumened and channelled devices this means brushing every channel over its full length and flushing until clear, at step 8, before the item goes anywhere near the disinfectant.

The agent. The high-level disinfectant used for each device is the one the device manufacturer's instructions permit, at the concentration and contact time those instructions and the product's own instructions state. Agents in recognised use for this purpose include glutaraldehyde, ortho-phthalaldehyde, peracetic acid and hydrogen peroxide formulations; each has different material compatibility, contact time, toxicity and disposal requirements, and they are not interchangeable. The agents used at {{HOSPITAL_NAME}}, the devices each is used for, the concentration, the temperature and the contact time are [Hospital to define — state each high-level disinfectant in use, the devices it is used for, and its concentration, temperature and contact time from the product and device instructions for use].

Controls that make the process reliable:

- the item is fully immersed, with every channel filled and all air displaced, for the whole of the contact time. A partially immersed item is not disinfected;
- the concentration of the active ingredient is verified before each use or at the frequency the product states, using the test strips supplied for that product, and the result is recorded. A solution within its stated reuse life is not assumed to be at concentration — reuse life and concentration are different things, and dilution by carry-over is what defeats it;
- the solution is discarded at the end of its reuse life or when it fails the concentration test, whichever comes first, and the container is labelled with the date the solution was activated or opened and the date it expires;
- after disinfection the item is rinsed thoroughly with water of a quality that will not recontaminate it, and for devices contacting sterile or near-sterile sites the rinse water quality required is stated in the device instructions;
- the item is dried, including alcohol flushing and forced-air drying of channels where the instructions require, because residual moisture allows waterborne organisms to multiply and is the mechanism behind several published endoscope-related outbreaks;
- the item is stored so that it does not recontaminate — hung vertically, uncoiled, channels open and dry, in a cabinet designated for the purpose, not returned to a case or drawer.

Every cycle is recorded: the device identity, the patient or procedure it was last used on, the operator, the agent, the concentration test result, the contact time, the rinse and the drying, and the storage. For endoscopes this record is what links a device to a patient in both directions and is the record a look-back investigation depends on.

Staff performing high-level disinfection work with ventilation adequate to the agent and with the protective equipment the product requires; exposure and health surveillance are governed by the occupational health policy.

FLEXIBLE AND SEMI-RIGID ENDOSCOPES — ADDITIONAL MANDATORY REQUIREMENTS

The requirements in this subsection apply to flexible and semi-rigid endoscopes and to no other device. They do not apply to laryngoscope blades, respiratory and anaesthesia equipment, reusable probes, or any other semi-critical item, all of which remain governed by the generic process set out above in this step. Where a requirement here is stricter than the generic one, the requirement here prevails for endoscopes.

Why these devices are treated separately. An endoscope is the hardest reusable device in a hospital to reprocess and the one with the worst documented record. It has long, narrow, tortuous channels that cannot be seen into; internal surfaces that cannot be inspected once assembled; moving parts such as elevator mechanisms with recesses that resist brushing; and it is used in body sites with a heavy microbial load. Transmission of multidrug-resistant organisms, including carbapenem-resistant Enterobacterales, has been repeatedly documented in patients exposed to duodenoscopes that had been reprocessed in accordance with the manufacturer's instructions in force at the time, and has prompted regulatory safety communications and changes to device design. The generic high-level disinfection process above is necessary for these devices and is not sufficient.

Where {{HOSPITAL_NAME}} does not perform endoscopy. This subsection is not deleted. The head of the institution records a signed and dated declaration that flexible and semi-rigid endoscopy is not performed, with the reason and the referral arrangement for patients who need it, tabled at the Infection Prevention and Control Committee and reviewed each year and on any change to the services provided — [Hospital to define — state whether flexible or semi-rigid endoscopy is performed; if it is not, record the declaration, its reason and its review date]. This is the record that distinguishes a service the hospital does not offer from a reprocessing requirement it has failed to meet, and it is the same treatment given to invasive ventilation in the surveillance policy.

1. Leak testing, before cleaning, after every use. The endoscope is leak tested after every patient use and before it is immersed in any fluid, by the method and with the equipment the manufacturer specifies, and the result is recorded against the device and the procedure. Leak testing precedes cleaning because its purpose is to detect a breach before fluid enters it: a perforation of the outer sheath or an internal channel admits fluid into the interior of the instrument, damages it, and creates a contaminated space that no reprocessing method can reach. An endoscope that fails a leak test is not reprocessed and not used. It is quarantined, removed from service, recorded, and sent for repair, and it re-enters service only after repair and a passed leak test. Where the failure means a patient has been exposed to an endoscope with a breached channel, the recall route at steps 31 to 37 is entered.

2. Cleaning verification, mandatory and not schedule-dependent. For flexible and semi-rigid endoscopes, cleaning verification is performed after cleaning and before high-level disinfection, on every reprocessing cycle. This is a deliberate departure from the general position at step 9, where the verification method and its frequency are set by the monitoring schedule: for endoscopes the verification is not sampled and is not omitted because the schedule does not call for it that day. The test used measures residual organic soil — adenosine triphosphate bioluminescence, protein, carbohydrate or haemoglobin residue — applied to the channels and to the distal end, against the acceptance criterion the test manufacturer states. An endoscope failing verification is recleaned and re-tested and does not proceed to disinfection; a repeated failure on the same device is investigated as a channel or elevator-mechanism problem, not as an operator problem. Results are recorded per device per cycle.

3. Borescope inspection of internal channels. Visual inspection of an endoscope's exterior says nothing about the inside of a channel, and residual soil, retained fluid, scratches, adhesive failure, discoloration and channel damage are routinely found in devices that passed every external check. {{HOSPITAL_NAME}} therefore inspects the internal channels and the distal end of each endoscope with a borescope at a stated frequency, and records what was seen — [Hospital to define — state the borescope inspection frequency per endoscope and who performs it]. A device found with retained soil, retained fluid, scratching, channel damage or adhesive degradation is taken out of service and referred for repair or replacement; the finding is recorded and trended, and a pattern across devices is reported to the Committee as a reprocessing failure rather than a maintenance matter.

4. Active drying, with defined equipment. Drying is a control measure for these devices and not a finishing step. A residually wet channel allows waterborne organisms to multiply between uses, and this is the mechanism behind a substantial part of the published endoscope-associated outbreak literature. {{HOSPITAL_NAME}} therefore dries every endoscope actively, using a drying cabinet or a forced-air drying system that delivers filtered air through every channel for the period the equipment and the device manufacturer specify — [Hospital to define — state the drying equipment used, the drying time and the storage arrangement]. Passive drip-drying, wiping, and simply hanging a wet endoscope in a cupboard are not accepted for these devices. After drying, the endoscope is stored hanging vertically, uncoiled, with valves detached and channels open, in a cabinet designated for endoscope storage. Where a drying cabinet with validated storage conditions is used, the storage interval before reprocessing is required again is the one that cabinet is validated for; where it is not, the interval is [Hospital to define].

5. Water quality for endoscope reprocessing. The general water provisions at step 4 apply, and in addition the water used for the final rinse of endoscopes meets the quality specified for critical reprocessing water in the recognised standard for water for the processing of medical devices, which addresses microbial and endotoxin limits as well as chemical purity. Rinse water of ordinary potable quality will recontaminate a device that has just been high-level disinfected, which defeats the whole process. The specification adopted, the treatment that achieves it, and the testing frequency and action limits are [Hospital to define — state the endoscope rinse water specification, treatment, testing frequency and action limits, against the standard in force].

6. Personnel — certification and competency. Endoscope reprocessing is performed only by personnel assessed as competent for it specifically; competence in general instrument reprocessing does not transfer. {{HOSPITAL_NAME}} requires that a person assigned to endoscope reprocessing obtains a recognised endoscope reprocessing certification within two years of starting in the role, and that competency is verified by direct observation against the device manufacturer's instructions before the person reprocesses an endoscope unsupervised. Competency is reassessed at a stated interval, on any change of device or process, and after any reprocessing failure involving that person's work. The certification scheme accepted, the interval and the assessor are [Hospital to define — state the endoscope reprocessing certification accepted, the competency reassessment interval and who assesses]. Records are held for every person, including agency and contract staff, and a person without current verified competency is not assigned to reprocess an endoscope alone.

7. Records specific to endoscopes. In addition to the cycle record above: the leak test result per use; the cleaning verification result per cycle; borescope inspection findings with dates and images where the instrument captures them; the drying method, equipment and duration; the storage location and the date and time placed into storage; the water quality results; the repair and service history of each device; and the certification and competency record of each person who reprocessed it. Every endoscope carries a unique identifier and every use is linked to the patient, in both directions, because a look-back after a device is found defective depends on it.""",

"""16. Non-critical items and lower-level disinfection

Non-critical items contact intact skin only, and intact skin is an effective barrier. They are cleaned, and then disinfected at a low or intermediate level according to what they are and what they have been exposed to.

The items concerned at {{HOSPITAL_NAME}} include blood pressure cuffs, stethoscopes, pulse oximeter probes, thermometers used against intact skin or in the axilla, patient transfer equipment, bedpans and urinals, weighing scales, and the external surfaces of monitors, infusion pumps and ventilators.

The requirements:

- the agent is one the equipment manufacturer permits, since alcohol and chlorine damage many plastics, screens and cuff fabrics, and a cracked or crazed surface can no longer be cleaned. Where a manufacturer specifies particular wipes or agents, those are used;
- the whole surface is wiped, and the contact time stated for the agent is observed. A surface wiped and immediately dry has not been disinfected — the agent must remain wet for its stated time, which usually means wiping again rather than waiting;
- items are processed between patients, and any item visibly soiled with blood or body fluid is cleaned first and then disinfected at an intermediate level;
- items used on a patient under transmission-based precautions are dedicated to that patient where possible; where they cannot be, they are disinfected before leaving the room, and the practices policy of {{HOSPITAL_NAME}} governs the precaution itself;
- equipment shared between patients carries a visible indication of its status where {{HOSPITAL_NAME}} operates such a system, so that a nurse can tell a processed item from an unprocessed one — [Hospital to define — state whether a clean-status labelling system is used and how it works].

Responsibility for these items usually sits with the clinical area rather than the processing department, and that is where it most often falls down: an item that belongs to no one is processed by no one. The written guidance of {{HOSPITAL_NAME}} names, for each category of non-critical equipment, the person responsible for processing it and the frequency — [Hospital to define — assign each category of shared non-critical equipment to a responsible role and state the frequency].

Agents used on the patient environment itself — floors, walls, furniture and fittings — are governed by the support services policy and not by this one.""",

"""17. Unloading, cooling and release of the load

The load is not released because the cycle ended. It is released because a named person has checked the evidence and found it complete.

On completion of the cycle:

- the machine's own record — printout, data log or chart — is examined against the specified parameters for that cycle, and is signed by the operator. A cycle whose record is missing, incomplete or unreadable is a failed cycle;
- the external chemical indicator on each pack is checked for the expected change;
- packs are examined for integrity: intact seals, no tears or punctures, no wet or stained packaging;
- the biological or process challenge result is obtained where the schedule at step 24 requires one for that load, and for implant loads the load is quarantined until that result is available, as step 27 requires.

Wet packs. A pack that is wet on removal, or damp within the cooling period, is treated as unsterile. It is not dried and issued. The contents are returned to the beginning of the cycle and the cause is investigated — overloading, load composition, drainage, steam quality, drying time, or chamber loading pattern — and the finding recorded. Repeated wet packs are a machine or steam problem and are referred to biomedical engineering.

Cooling. Packs are left undisturbed on the trolley or rack until they reach room temperature, away from cold surfaces and out of any air stream. They are not handled, not stacked, and not moved to storage while warm. Two reasons, both of which produce contamination that nothing later will detect: a warm pack draws air in as it cools, and any organism at the surface is drawn through with it; and condensate forming where a warm pack meets a cold surface wets the packaging and destroys the barrier. The cooling period observed at {{HOSPITAL_NAME}} is [Hospital to define].

Release. A named person releases the load, recording their identity, the date and time, and the results relied on. Release is refused where any element is missing. The person releasing the load is authorised to refuse and is supported in doing so; a refused load is escalated to the Infection Control Officer and never overridden by the requesting department.

A load not released is quarantined in a designated area, physically separated and clearly marked, pending the decision at step 30.""",

"""18. Sterile storage and shelf life

Storage protects the barrier. Most loss of sterility in a hospital happens after processing, in storage and handling, rather than in the steriliser.

Conditions. Sterile items at {{HOSPITAL_NAME}} are stored in a designated area or cupboard used for no other purpose, off the floor, away from sinks, drains, windows and any source of moisture, clear of ventilation outlets that would blow dust over them, and away from heat. Shelving is smooth and cleanable. Storage is not in a corridor, not in a room that doubles as a thoroughfare, and not in the same cupboard as unprocessed items or general stores. Temperature and humidity are those specified at step 4, monitored and recorded.

Handling. Handling is the main cause of loss of sterility, so packs are handled as little as possible: stock is arranged so that a pack can be taken without disturbing others, staff perform hand hygiene before handling sterile stock, packs are not compressed, crushed, or held against clothing, and rubber bands or clips are never applied to a pack.

Shelf life. {{HOSPITAL_NAME}} operates an event-related or a time-related shelf life system, and states which — [Hospital to define — state whether shelf life is event-related or time-related, and if time-related, the period assigned to each packaging system].

- Under an event-related system a pack remains sterile until an event compromises it: a tear, a puncture, a broken seal, moisture, a dropped pack, or a pack that has been handled excessively. The date on the pack is then the processing date and the label carries the statement that the contents are sterile unless the package is opened or damaged.
- Under a time-related system each packaging system is assigned an expiry period and the pack carries an expiry date. The period is taken from the packaging manufacturer's data and not chosen by the hospital.

Whichever system is used, every pack is examined before issue and before use, and any pack that is torn, punctured, wet, stained, has a broken seal, has lost its label, or whose external indicator has not changed is treated as unsterile and reprocessed.

Stock rotation is by first-in, first-out, with the processing or expiry date visible without handling the pack. Stock levels are set so that rotation is achievable; a set held in excessive quantity will age on the shelf, and one held in insufficient quantity generates pressure for the immediate-use cycle at step 12.

Storage areas are cleaned to the schedule in the support services policy and are checked at a stated frequency for expired, damaged or unlabelled packs, with the check recorded — [Hospital to define].""",

"""19. Issue, transport to the point of use, and the check before use

Issue is recorded. The issue record identifies the item or set, its load number, the date, the department or theatre receiving it, and the person issuing it. Where the item is used on an identified patient, the record links load to patient, which is the link on which the recall at steps 31 to 37 depends. Where {{HOSPITAL_NAME}} operates a set tracking system, the record is generated by it; where the record is manual, it is kept in a form that can be searched by load number as well as by date — [Hospital to define — state the tracking system or manual record used and where it is held].

Transport of sterile items is in a closed or covered trolley or container that protects the pack from moisture, dust and handling damage, by a route that does not pass through a contaminated area, and never uncovered or in the hands. Sterile items are never transported in the same trolley or container as used items, in either direction.

The check before use. Immediately before a pack is opened for a patient, the person opening it confirms:

- the pack is the item required, and the set checklist matches;
- the packaging is intact — no tear, puncture, broken seal, damp patch or stain;
- the external chemical indicator has changed as expected;
- the pack is within its expiry, or under an event-related system that no event has compromised it;
- the internal chemical indicator, once the pack is opened, has changed as expected. This is checked at the point of use by the person setting up, not only in the processing department.

A pack failing any of these checks is not used. It is set aside, labelled, returned to the processing area with the reason recorded, and reprocessed. The failure is recorded and reviewed, because a pack failing at the point of use may indicate a load problem affecting other packs and is a trigger for step 31.

This check is the one the prevention of healthcare associated infections policy of {{HOSPITAL_NAME}} refers to when it requires that instruments, implants and supplies are sterile and that their sterility is confirmed at the point of use by checking the indicator and pack integrity. The requirement is stated there; the method and the record are here.

Responsibility for the check sits with the person opening the pack, and it is not delegated to the processing department, which cannot see the pack at the moment it matters.""",

"""20. The records that evidence the cycle

The cycle is evidenced by records, and this step collects in one place what {{HOSPITAL_NAME}} retains so that the requirement is not scattered.

For each load: the steriliser or disinfector identity; the load or cycle number; the date and time; the cycle type; the contents itemised sufficiently to identify every pack; the physical parameters achieved as recorded by the machine; the chemical indicator results, internal and external; the biological or process challenge result where required; the operator; the person releasing the load; and the release decision with its date and time.

For each item or set: its identity; the load that processed it; the date of processing; its expiry or review status; the department it was issued to; and, where it was used on an identified patient, that patient. Sets that are tracked individually carry an identifier that persists through processing.

For each machine: qualification and requalification records; calibration certificates for gauges, sensors and recorders; the daily and periodic performance test results; the maintenance record including every repair and what was done; and the record of any cycle failure and its resolution.

For the process as a whole: the classification register at step 2; the written reprocessing guidance and the manufacturer's instructions for use for every device and every machine; the set checklists; the training and competency records of every person who processes items; deviation records from step 7; cleaning verification results from step 9; and the recall records from steps 31 to 37.

Two properties these records must have, and which are what an assessor actually tests:

- they must permit tracing in both directions. From a patient to the load, and from a load to every patient and location its contents reached. A record that supports only one direction cannot support a recall;
- they must be legible, contemporaneous and attributable. A record completed at the end of a shift from memory is not a record of what happened.

Retention periods follow the records retention policy of {{HOSPITAL_NAME}}, and for implantable devices are at least the period the law and the device's expected life require — [Hospital to define — state the retention period for processing records, and for implant traceability records]. Records are stored so that they remain retrievable for the whole of that period, including where the tracking system is replaced.""",

"""21. Devices labelled single-use — the default position

A device labelled for single use by its manufacturer is used once at {{HOSPITAL_NAME}} and is then discarded. This is the default, it applies unless a written protocol approved under step 22 says otherwise for a named device category, and it is not displaced by cost, by scarcity, or by the fact that the device appears undamaged after use.

The reasoning is recorded here so that the rule is understood rather than merely obeyed. A single-use device has not been designed to be cleaned, and frequently cannot be: it may have lumens that no available brush reaches, sealed joints that trap fluid, adhesive bonds that fail on immersion, or surfaces that degrade on contact with disinfectant. It has not been validated for any reprocessing method, so no cycle can be shown to sterilise it. Its materials may not survive the process in ways not visible from outside — plastics craze, coatings lift, insulation thins, cutting edges dull, and the failure appears during use. And the manufacturer's liability for its performance does not extend past the first use, so the hospital that reprocesses it assumes that responsibility in full.

Identifying such devices. Single-use status is shown by the manufacturer's symbol or wording on the device or its packaging. Staff of {{HOSPITAL_NAME}} are trained to recognise it, and the symbol is displayed at the sorting bench in the decontamination zone and in every clinical area that generates used items.

Single-use items are removed from the reusable stream at step 7 and discarded as biomedical waste under the support services policy. The presence of a single-use item in the reusable stream is recorded as a deviation, fed back to the sending area, and trended to the Committee.

An unused single-use device whose packaging has been opened but which has not contacted a patient is still not resterilised for reuse unless a protocol under step 22 covers it; it is discarded. This is the situation in which the rule is most often broken, because the device looks untouched.

Where the true cost of the default is unsustainable for a particular device — which is a legitimate concern and not one this policy dismisses — the route is a protocol under step 22 or a change of procurement to a reusable equivalent, decided in the open. It is not an informal local practice.""",

"""22. If a single-use device is reprocessed — what the written guidance must contain

{{HOSPITAL_NAME}} reprocesses a device labelled single-use only where the Infection Prevention and Control Committee has approved a written protocol for that specific device category, on the recommendation of the Infection Control Officer, and the decision and its basis are recorded in the Committee's minutes.

No such protocol exists by default. The categories for which {{HOSPITAL_NAME}} has approved one, if any, are [Hospital to define — list every single-use device category approved for reprocessing, or record that none is approved].

A protocol is approved only where it states all of the following, and a protocol missing any of them is not approved:

- the device, by manufacturer, model and catalogue reference. A protocol is never written for a class of device in general;
- the regulatory position relied on, and confirmation that reprocessing this device is permitted under the law applying to {{HOSPITAL_NAME}} and under any condition attached to its own licences. Where reprocessing is performed by a licensed external reprocessor rather than by the hospital, that provider is named and its authorisation held on file;
- the validated cleaning method, in full, including how each lumen and joint is reached, and how cleaning is verified for a device not designed to be inspected internally;
- the validated sterilisation or disinfection method, with the evidence that it achieves sterility for this device and does not degrade it;
- the maximum number of reprocessing cycles the device may undergo, with the basis for that number;
- the method of counting cycles for an individual device, which must be reliable at the level of the single item and not merely at batch level;
- the acceptance criteria applied before each reuse — function, integrity, appearance — and who applies them;
- the devices, procedures or patients for which the reprocessed device may not be used;
- the record kept for each device and each cycle, and how it links to the patient;
- the review date, and the trigger for withdrawing the protocol.

The Infection Control Officer confirms in writing, before approval, that a reprocessed device of this category presents no greater risk to a patient than a new one. Where that confirmation cannot honestly be given, the protocol is not approved.

Patients are not exposed to a reprocessed single-use device without the hospital having made this determination. Whether patient consent is separately sought is a decision for {{HOSPITAL_NAME}} on the advice of the Committee, and the position adopted is [Hospital to define].""",

"""23. Devices never reprocessed

Certain items are not reprocessed at {{HOSPITAL_NAME}} under any circumstance, and no protocol under step 22 may cover them:

- any implant labelled single-use;
- any device that has contacted tissue of the central nervous system, or the posterior eye, in a patient known or suspected to have a transmissible spongiform encephalopathy. Conventional sterilisation does not reliably inactivate the agent involved. Such instruments are handled under the specific precautions the practices policy of {{HOSPITAL_NAME}} sets out, and are destroyed rather than returned to service;
- any device whose manufacturer's instructions for use cannot be obtained, or which cannot be identified with certainty;
- any device with a lumen or channel that cannot be cleaned by an available method and verified;
- any device visibly degraded, discoloured, cracked, or with damaged insulation or coating;
- any device that has been contaminated by an event outside its intended use — dropped into a contaminated area, exposed to a chemical spill, or involved in a fire or flood — unless the manufacturer confirms it may be returned to service;
- any device recalled by its manufacturer or a regulator, which is quarantined and dealt with under the manufacturer's or regulator's instruction and not reprocessed;
- any device beyond the cycle count set for it in an approved protocol.

An item falling into any of these categories is removed from service immediately, marked so that it cannot be returned to use in error, recorded, and disposed of under the biomedical waste route in the support services policy or returned to the manufacturer as that instruction requires.

The decision to withdraw an item under this step is made by any member of the processing staff or any clinician, and does not require prior authorisation. It is reported to the Infection Control Officer, who records it. A decision to withdraw is never reversed by a person other than the Infection Control Officer, and never on operational grounds alone.""",

"""24. The monitoring and validation schedule

{{HOSPITAL_NAME}} distinguishes two things that are commonly confused, because the difference decides what a result actually proves.

Validation establishes, once and on repeat occasions, that a process is capable of sterilising — that this machine, running this cycle, with this type of load, achieves the required conditions throughout. It is performed on installation, after relocation or major repair, and at defined intervals thereafter, and it is the subject of step 29.

Routine monitoring establishes, for each cycle, that the process behaved as validated. It cannot establish that an unvalidated process works, and it cannot rescue a machine that has never been qualified.

Both are required. A hospital with excellent daily monitoring on a machine that was never qualified has evidence that an unknown process ran consistently.

Routine monitoring at {{HOSPITAL_NAME}} operates at four levels, each answering a different question:

- physical or mechanical monitoring — did the machine reach and hold the specified conditions? (step 25);
- chemical indicators — was a given point in the load exposed to the conditions? (step 26);
- biological indicators — were organisms of known resistance actually killed? (step 27);
- air removal and leak testing — can steam reach the load at all? (step 28).

No single level is sufficient. A physical record shows the chamber's conditions but not the inside of a pack. A chemical indicator shows exposure but not lethality. A biological indicator shows lethality for the challenge it presents, at the point it was placed, on the cycle it ran.

The written schedule of {{HOSPITAL_NAME}} states, for each machine and each cycle type: what is tested, at what frequency, by whom, where in the chamber or load the test is placed, the acceptance criterion, who reads and records the result, and what happens on a failure. The schedule is approved by the Infection Prevention and Control Committee and is reviewed annually and whenever a machine or a standard changes — [Hospital to define — state the monitoring schedule for each machine and cycle, against the standard in force and the manufacturer's specification].

Results are not merely filed. They are reviewed by the person in charge of processing at a stated frequency, trended, and reported to the Committee with the failures, the actions taken and the outcomes.""",

"""25. Physical and mechanical monitoring

Every cycle produces a record from the machine itself, showing what the chamber did: time, temperature, and pressure through each phase, and for low-temperature processes the parameters specific to that method.

The record is examined and signed by the operator at the end of every cycle, before the load is released, and is checked against the specified parameters for that cycle. Signing is a check, not a formality — a signature on an unexamined printout is worse than no signature, because it creates evidence that a check occurred.

What the operator confirms:

- the cycle ran to completion without an abort or an alarm;
- the temperature reached the specified value and was held for the full exposure time, and did not exceed the upper limit;
- pressure corresponded to temperature throughout, since a divergence between the two indicates air in the chamber or a steam quality problem even where the temperature alone looks correct;
- the phases occurred in the right order and each lasted its specified time, including the drying phase;
- the trace shows no interruption, dropout or irregularity.

A cycle whose record is missing, incomplete, unreadable, or shows any deviation is a failed cycle. The load is quarantined and dealt with under step 30. It is not released on the basis that the chemical indicators changed, because an indicator confirms exposure at a point and cannot confirm that the chamber held its conditions throughout.

The instruments producing this record — temperature sensors, pressure gauges, timers and the recorder itself — are calibrated at the interval the manufacturer and the standard in force require, by a competent person, against traceable references, and the certificates are retained. An uncalibrated sensor produces a record that is confident and wrong, and this is the failure mode that routine monitoring is least able to detect on its own. Calibration frequency and provider are [Hospital to define].

Where a machine has an independent recorder in addition to its control system, both are checked, and any divergence between them is investigated rather than averaged.

Machine records are retained with the load record under step 20 for the period stated there.""",

"""26. Chemical indicators

Chemical indicators change appearance on exposure to one or more of the conditions of the process. They give an immediate, visible result, which is their value, and they are widely misread, which is their risk.

What they prove and what they do not. A chemical indicator shows that the point at which it was placed was exposed to the conditions it responds to. It does not show that the item is sterile. The most basic indicators respond to a single condition, most commonly temperature, and will change on brief exposure that would not sterilise anything. Treating a changed indicator as proof of sterility is the single commonest error in this field, and {{HOSPITAL_NAME}} states expressly that a changed indicator is a necessary condition for release and never a sufficient one.

Indicators are classified by what they respond to and how closely they track the process, from simple process indicators that merely distinguish a processed pack from an unprocessed one, through indicators responding to a single variable, to integrating indicators designed to react to all the critical variables of the cycle and to correlate with the performance of a biological indicator. The class of indicator used at each point at {{HOSPITAL_NAME}} is specified in the schedule at step 24 against the standard in force — [Hospital to define — state the class of chemical indicator used externally, internally, and within any process challenge device, against the standard in force].

Where they are used:

- externally on every pack, so that a processed pack is distinguishable from an unprocessed one at a glance. This is its only purpose; it says nothing about the inside of the pack;
- internally in every pack, placed in the position the sterilant will reach last, which is generally the geometric centre of the pack or the most difficult lumen. The person opening the pack at the point of use reads it, under step 19;
- within a process challenge device where the schedule requires one, presenting a defined resistance to the process and placed in the coldest or most difficult location in the chamber.

Reading. Indicators are read against the manufacturer's reference, in adequate light, immediately on removal or on opening. An indicator whose change is partial, patchy, ambiguous, or different from the reference is a failure, not a marginal pass. Where a reader is unsure, the load is quarantined and the Infection Control Officer decides.

Indicators are stored as their manufacturer requires, are used within their expiry, and the lot number in use is recorded so that an indicator fault can itself be traced.

An internal indicator failure discovered at the point of use is reported immediately to the processing area, because it may affect the whole load, and it is a trigger for step 31.""",

"""27. Biological indicators

A biological indicator carries a defined population of bacterial spores selected for their resistance to the process concerned, and it is the only routine monitor that demonstrates lethality rather than exposure. Killing the spores demonstrates that the process was capable of killing what it was meant to kill, at the point where the indicator sat.

The organism is the one appropriate to the process — for moist heat and for hydrogen peroxide based processes, spores of a species selected for resistance to those conditions; for ethylene oxide, a different species selected for resistance to it. The indicator is supplied for the specific process and is never substituted between processes. The indicators in use at {{HOSPITAL_NAME}}, with the process each is used for and the incubation time and temperature specified by their manufacturer, are [Hospital to define — state the biological indicator used for each process, its organism, and the incubation conditions specified by its manufacturer].

Placement and use:

- the indicator is placed within a process challenge device, in the location in the chamber that is most difficult for the sterilant to reach, which is determined at qualification and stated in the schedule;
- a control indicator from the same lot, not processed, is incubated alongside every test indicator. Without a positive control a negative result is uninterpretable, because it cannot be distinguished from a lot in which the organisms were never viable;
- results are read at the time the manufacturer specifies, by a person trained to read them, and are recorded with the lot number, the load, the reader and the time.

Frequency. Biological monitoring is performed at the frequency stated in the schedule at step 24, and at minimum on each day the steriliser is used for the cycles the schedule names, on installation and after any repair or requalification, and whenever the cycle or load type changes materially.

Implants. Every load containing an implant is monitored with a biological indicator and a process challenge device, and the load is quarantined and not released until the result is available and satisfactory. An implant is released before the result only where the clinical need is genuinely immediate, and then only on the authority of the Infection Control Officer or the operating surgeon jointly, with the reason, the patient and the authorising person recorded, and the result followed up and recorded when it becomes available. {{HOSPITAL_NAME}} tracks how often this occurs, because a pattern of early release indicates an inventory or scheduling problem rather than a series of emergencies.

A positive biological indicator, with a valid negative control, is a sterilisation failure and triggers step 30 and the recall at steps 31 to 37 immediately. It is not repeated first in the hope of a different answer; a repeat test may be run in parallel with the recall, never in place of starting it.""",

"""28. Air removal and leak testing

Steam cannot sterilise what it cannot reach, and the most common reason it cannot reach a load is air. Air is heavier than steam, does not mix with it, and collects in the coolest and most enclosed parts of the chamber and the pack — which are precisely the parts that most need to be reached. A chamber gauge showing the correct temperature says nothing about a pocket of trapped air inside a pack.

Sterilisers that remove air dynamically, by drawing a vacuum before admitting steam, are therefore tested for air removal separately from any other monitoring:

- an air removal test is performed each day the steriliser is used, in an empty chamber, as the first cycle of the day, using the test pack or device the standard in force and the manufacturer specify. The result is read against the reference and recorded;
- a leak rate test is performed at the frequency the schedule states, to establish that the chamber holds vacuum. A chamber that leaks draws air in during the vacuum phase, and the leak will not appear on the temperature trace;
- a failed air removal or leak test takes the steriliser out of service immediately. It is not used for patient items until the fault is found, corrected, and the test repeated and passed, and the repair is recorded under step 29.

The test in use at {{HOSPITAL_NAME}}, the acceptance criterion, and the leak test frequency are [Hospital to define — state the air removal test and leak test used, their frequency and acceptance criteria, against the standard in force and the steriliser manufacturer's specification].

Where a steriliser removes air by gravity displacement rather than dynamically, this test does not apply, but the limitation does: such a machine removes air less effectively, and the load types and packaging it may be used for are correspondingly restricted to those its qualification covered. {{HOSPITAL_NAME}} records which of its machines are of which type and what each may process.

Loading practice at step 12 is part of air removal and not separate from it. A chamber loaded so that air cannot escape will fail a load even where the machine passed its test that morning, which is why a failed indicator in a correctly functioning machine is investigated as a loading problem before it is investigated as a machine fault.""",

"""29. Qualification, requalification and maintenance of equipment

Every steriliser, washer-disinfector and automated disinfection machine at {{HOSPITAL_NAME}} is qualified before it is used on patient items, and requalified thereafter.

Qualification has three parts, and all three are recorded:

- installation qualification establishes that the machine was delivered and installed as specified, in a suitable location, correctly connected to the services it requires — water of the specified quality, steam of the specified quality, drainage, power, ventilation — and that it operates within its own specification;
- operational qualification establishes that the machine achieves its stated parameters throughout the chamber when empty, including that the temperature is uniform and that no location falls outside the band;
- performance qualification establishes that the machine achieves the required conditions in the actual loads {{HOSPITAL_NAME}} will process, using thermometric measurement and biological challenge in the loads concerned. This is the part most often omitted, and it is the part that identifies the coldest location in a real load — which is where the process challenge device at step 27 must then be placed.

Performance qualification is repeated for each distinct load type the machine will process. A machine qualified for instrument trays has not been qualified for textile packs.

Requalification is performed: at the interval the standard in force and the manufacturer specify; after relocation; after any major repair or replacement of a component affecting the process, including a door seal, a vacuum pump, a control system or a sensor; after a change in the utilities supplying it; and after any unexplained failure. A repair is not complete until requalification has passed and been recorded.

Maintenance follows the manufacturer's schedule, is performed by a competent person, and is recorded with the date, the work done, the parts replaced and the person performing it. Planned maintenance is not deferred on operational grounds without the Infection Control Officer recording the decision and the compensating measure.

Where qualification or maintenance is performed by an external provider, that provider's competence and the traceability of its test instruments are established before appointment, its reports are retained by {{HOSPITAL_NAME}}, and the reports are reviewed rather than filed. The provider and the qualification interval are [Hospital to define].

A machine that is due requalification and has not had it is taken out of service for patient items. Continuing to use it is a decision only the head of the institution may take, on the Infection Control Officer's written advice, with the compensating measures and the review date recorded.""",

"""30. When a test fails — the immediate decision

This step governs what happens between the discovery of a failure and the recall that may follow. Its purpose is to prevent the two errors that occur at this moment: releasing the load anyway, and repeating the test until it passes.

On any failed physical record, failed chemical indicator, failed biological indicator, failed air removal or leak test, wet pack, or aborted cycle:

1. The load is quarantined immediately. It is physically separated, clearly marked as not released, and secured so that it cannot be issued in error. Where any part of the load has already left the processing area, step 31 is entered at once and without waiting for the investigation.
2. The machine is taken out of service for patient items pending investigation, unless the cause is established immediately and unambiguously as a loading or operator error confined to that load.
3. The failure is recorded — machine, cycle, date and time, the test that failed, the result, the person who found it, and the action taken.
4. The Infection Control Officer is informed, on the same day, and for a positive biological indicator or a failed air removal test, immediately.

The investigation establishes the cause before the machine returns to service. The usual causes, in the order they are checked: operator or loading error; packaging or pack density; steam supply quality, pressure or wetness; water quality; a fault in the machine, its door seal, its vacuum system or its sensors; and an indicator lot fault, which is confirmed only after the others have been excluded and never assumed first.

Repeating a test is permitted only as part of the investigation, alongside the actions above and never instead of them. A repeat test that passes does not explain the failure, does not release the quarantined load, and does not return the machine to service on its own. Where a biological indicator has failed, the recall at step 31 begins immediately and runs in parallel with any repeat testing.

Return to service requires: the cause identified, the correction made, requalification where step 29 requires it, and a satisfactory test result. The Infection Control Officer authorises return to service and records the authority.

Quarantined items are reprocessed in full from the beginning of the cycle once the machine is fit, or are discarded where reprocessing is not appropriate. They are never released on the basis that the failure was probably not real.""",

"""31. What counts as a breakdown in the sterilisation system

The recall procedure of {{HOSPITAL_NAME}} is entered whenever the sterilisation system is found to have failed and items processed by it have already been issued or used. The trigger is the discovery of the failure, not proof that harm resulted.

The following are breakdowns requiring entry into the recall route:

- a positive biological indicator with a valid negative control;
- a failed internal chemical indicator discovered at the point of use, or a failed indicator discovered in any pack after issue;
- a physical or mechanical record showing that a cycle did not achieve or hold its specified parameters, discovered after the load was released;
- a failed air removal or leak test where loads have been processed since the last passed test;
- discovery that a machine was operating outside specification, was uncalibrated, or was overdue requalification, over a period during which loads were released;
- discovery of a systematic process deviation — the wrong cycle used for a load type, packaging outside its validated limits, a cleaning stage omitted, a disinfectant below concentration, or an aeration stage shortened;
- wet packs discovered after issue;
- a cluster of infections referred from the surveillance policy of {{HOSPITAL_NAME}} in which a processed item or a processing failure is among the hypotheses;
- a manufacturer's or regulator's recall of a device, a packaging material, an indicator lot or a sterilant used by {{HOSPITAL_NAME}}.

Any member of staff who identifies any of these reports it immediately to the person in charge of processing and to the Infection Control Officer, directly and without going through a line manager. The report is made on suspicion. A member of staff who reports a suspected breakdown that proves unfounded has done the right thing and is told so; concealment or delay is the conduct this policy treats as serious.

The report is logged with the date, the time, the reporter, what was observed and the action taken, including reports that prove unfounded, because the log is the evidence that the route is live and used.

The Infection Control Officer, or the named deputy where the Officer is unavailable, decides within the time stated in this policy whether the recall route is entered, and records the decision either way with reasons. The Officer and deputy, with contact details available at all hours, are [Hospital to define — name the Infection Control Officer and the deputy and state 24-hour contact details].""",

"""32. Immediate response — quarantine and stop

On entering the recall route, the following are done immediately and are not deferred pending investigation, a meeting, or an approval.

Stop the source. The machine or process concerned is taken out of service for patient items at once and secured so that it cannot be used inadvertently. Where the failure lies in a process rather than a machine — a disinfectant below concentration, a packaging fault, an indicator lot — the process is suspended across every location it is used in, including locations outside the central processing area under step 5.

Quarantine what is still held. All items processed by the affected machine or process, since the last point at which the system is known to have been working, are located and quarantined wherever they are: sterile storage, theatre, wards, clinics, procedure rooms, trolleys and emergency sets. Quarantined items are physically separated, clearly marked as not for use, and secured. Marking alone is not sufficient where an item remains accessible.

Stop further issue. Issue from the affected stock ceases immediately, and the departments concerned are told directly rather than by circular, so that a set is not opened while the message is in transit.

Establish the clinical position. The person in charge of processing and the Infection Control Officer establish, from the records at step 20, which items have already been used and on which patients, and which are still retrievable. This is where the traceability required at steps 11, 19 and 20 either works or does not, and where its absence becomes a patient safety problem rather than a documentation one.

Protect continuity of care. The Infection Control Officer, with the departments affected, establishes what capacity remains — an unaffected machine, an alternative processing route, an external provider under step 38, or single-use alternatives — and whether any procedure must be postponed. A procedure is not performed with an item of unverified sterility because no alternative is available; the procedure is postponed and the decision recorded.

Record the timing. The time the failure was identified, the time each of the above was completed, and the interval between them are recorded. The interval from identification to containment is the number that says whether this procedure works, and it is reported with the outbreak or incident report at step 36.""",

"""33. Determining the scope of the recall

The scope is decided by evidence of when the system was last known to be working, not by an estimate of when it probably failed.

The rule at {{HOSPITAL_NAME}}: the recall extends back to and includes every load processed since the last load for which a satisfactory result of the type that has now failed is on record.

Applied in practice:

- where a biological indicator has failed, the recall reaches back to the last load with a satisfactory biological indicator result. Where biological monitoring is daily, that may be a full day's loads or more;
- where an air removal test has failed, the recall reaches back to the last passed air removal test, which is generally the previous day's test, and includes every load processed in between;
- where a calibration or qualification lapse is discovered, the recall reaches back to the last point at which the machine was demonstrably within specification;
- where the fault is a process rather than a machine, the recall covers every item processed by that process across every location, over the whole period the deviation persisted.

Where the last satisfactory result cannot be established, the scope extends to the earliest point at which the records support a positive statement that the system was working. Where no such point can be established, the Infection Control Officer sets the scope conservatively and records the reasoning, and the inability to establish it is itself recorded as a finding requiring corrective action, because it means the monitoring regime is not producing the evidence it exists to produce.

The scope is recorded in writing before retrieval begins, listing the machine, the period, the load numbers and the item categories included, and is authorised by the Infection Control Officer. It is widened without hesitation if the investigation shows the failure began earlier; it is narrowed only on evidence, never on inconvenience, and any narrowing is recorded with its basis and the Officer's authority.

Where the scope includes implants, the scope is treated as extending to every patient who received one, regardless of how long ago, and the assessment at step 34 applies to each.""",

"""34. Executing the recall and assessing exposed patients

Retrieval. Every item within the scope is located and retrieved. The retrieval list is worked through by location and signed off location by location, so that the position at any moment is known. Each item is recorded as retrieved, already used, or not accounted for. An item not accounted for is pursued until it is; an unresolved item is treated as used and is escalated to the Infection Control Officer.

Retrieved items are returned to the processing area, kept separate from all other stock, and dealt with under step 35.

Patients already exposed. For every item already used, {{HOSPITAL_NAME}} identifies the patient, the procedure, the date and the clinician, and the Infection Control Officer performs a documented risk assessment covering:

- the nature of the failure and what it means for the likelihood that the item was in fact non-sterile — a failed external indicator on an otherwise correct cycle is a different proposition from a positive biological indicator or an omitted cleaning stage;
- the item's classification under step 2 and the tissue it contacted;
- whether an implant was involved;
- the patient's susceptibility;
- the organisms plausibly involved, including bloodborne viruses where the failure involved inadequate cleaning of an item used on a previous patient;
- the clinical course since the procedure, obtained from the treating team.

The assessment is recorded for every exposed patient individually, whether or not any action follows. A group conclusion recorded once does not meet this requirement.

Clinical action. Where the assessment indicates it, the treating clinician is informed and the patient is placed under enhanced clinical follow-up, with the parameters and duration recorded. Where testing or prophylaxis is indicated, it is arranged and provided at the cost of {{HOSPITAL_NAME}}. Any infection that follows is reported to surveillance under the surveillance policy and is counted there.

Informing patients. The decision whether to inform an exposed patient is taken by the head of the institution on the written advice of the Infection Control Officer, is taken promptly, and is recorded with its reasoning whichever way it goes. {{HOSPITAL_NAME}} starts from the position that a patient who has been exposed to a material risk is told, and that the burden lies on any argument for not telling them. Where patients are informed, the communication is made by a named clinician, in person where practicable, with the factual position, what is known and not known, what is being offered, and who to contact. All external communication about the event is authorised by the head of the institution.

Statutory or regulatory reporting, and reporting to a manufacturer where a device, indicator or sterilant is implicated, is made where required, and the report and its date are recorded.""",

"""35. Reprocessing recalled items and return to service

Recalled items. Every retrieved item is reprocessed in full from the first stage of the cycle — not from the stage at which the failure occurred. An item whose cleaning stage is in doubt is recleaned; an item whose sterilisation is in doubt is unpacked, inspected, repacked and resterilised. Packaging is discarded and replaced, since a pack cannot be resterilised in its existing wrapping and its barrier status is unknown.

Items that cannot be reprocessed satisfactorily, and any item whose integrity is in doubt after the event, are withdrawn under step 23 and disposed of.

Reprocessed items are released only on the full evidence required by step 17, on a machine that has been returned to service under this step, and the release record is annotated to show that the item was part of a recall.

The machine or process. Return to service requires all of the following, recorded:

- the cause identified by the investigation at step 36, or where no cause is established, the explicit finding that none was established together with the measures taken in consequence;
- the correction made, whether repair, replacement, recalibration, a change to the process, or retraining;
- requalification under step 29 where the fault or the repair requires it, with satisfactory installation, operational and performance qualification results for the load types the machine will process;
- satisfactory results from the full monitoring set — physical, chemical, biological and, where applicable, air removal — on test cycles run before any patient item is processed;
- the written authority of the Infection Control Officer, with the date and time.

Where a machine has failed for the same cause more than once, it is not returned to service on a repeat repair alone; the Infection Control Officer refers it to the head of the institution with a recommendation on replacement, and the recommendation and the decision are recorded, including where replacement is declined and the reason.

Enhanced monitoring. For a period following return to service, stated by the Infection Control Officer and recorded, monitoring is increased above the routine schedule — typically more frequent biological monitoring and closer review of physical records — and the results are reviewed by the Officer rather than only by the processing area. The period and the enhanced regime are recorded, and the return to routine monitoring is a decision that is also recorded.""",

"""36. The recall report, investigation and corrective action

Every recall produces a written report, authored by the Infection Control Officer, tabled at the Infection Prevention and Control Committee, and copied to the head of the institution. The report is produced within the period this policy states — [Hospital to define — state the period within which the recall report is produced].

The report states:

- how the failure was identified, by whom, and when — including whether it was found by the monitoring system as designed, or by chance, or at the point of use, which is itself a finding about the monitoring system;
- the interval from identification to containment;
- the scope of the recall and how it was determined;
- what was retrieved, what had been used, and anything not accounted for;
- the patients exposed, the assessments made, the clinical actions taken, and the decisions on informing patients with their reasoning;
- the investigation and its conclusion as to cause;
- the corrective and preventive actions, each with a single named owner and a due date;
- what this event says about the system rather than about the individuals involved.

The investigation establishes cause, using a formal root cause analysis where the event is serious or the cause is not immediately clear. It examines the technical cause and the system that allowed it: whether the monitoring would have caught it and how quickly, whether staffing or workload pressure contributed, whether training or competency assessment was adequate, whether an inventory shortage created pressure to release early or to use the immediate-use cycle, and whether a previous similar event was closed without effective action.

Where no cause is established, the report says so plainly. A significant proportion of process failure investigations close without a proven cause, and a report that manufactures one is worse than a report that admits none, because it produces a corrective action aimed at the wrong thing and closes the matter.

Corrective actions are entered in the register the surveillance policy of {{HOSPITAL_NAME}} maintains, are tracked by the Committee to closure, and are verified by re-measurement rather than closed on assertion. Where an action proves ineffective, that is recorded as plainly as a success and a further action is taken.

The lessons are carried into the written guidance, the training programme and the monitoring schedule. A recall that changes no document and no practice has not been learned from.""",

"""37. Mock recalls

A recall procedure that has never been exercised is a document, not a capability. The failure it is written for arrives without notice, usually at an inconvenient hour, and the thing that breaks is almost always traceability rather than willingness.

{{HOSPITAL_NAME}} therefore performs a mock recall at a stated interval — [Hospital to define — state the interval at which a mock recall is performed] — and at least annually.

The exercise selects a load processed at a point in the past and requires the processing area to establish, within a defined time and from the records alone:

- every item that load contained;
- where each item is now — in storage, issued to a department, used on a patient, or disposed of;
- for every item used, the patient, the procedure, the date and the clinician;
- the monitoring results for that load;
- the point back to which a recall would have to extend if that load had failed.

The exercise is timed, and the time taken is recorded, because in a real recall the interval to containment is the measure that matters.

The findings are recorded whether or not they are comfortable, and the traceability gaps the exercise exposes — a load whose contents were not itemised, an issue record that cannot be searched by load number, a bench-top steriliser outside the central area whose loads were never linked to patients, a set that was broken up and redistributed, an item used but not recorded against a patient — are entered as corrective actions with owners and due dates and are closed by re-testing rather than by assertion.

The mock recall is tabled at the Infection Prevention and Control Committee with its findings and its actions. An exercise that finds nothing is examined for whether it was demanding enough; a load selected because it is easy to trace does not test anything.

The exercise also tests the human elements: whether the out-of-hours contact route reaches someone, whether the person in charge of processing knows their standing authority to quarantine without waiting for approval, and whether departments know how to respond to a stop-issue instruction.""",

"""38. Outsourced processing

Where {{HOSPITAL_NAME}} sends any item to an external provider for cleaning, disinfection or sterilisation, the provider performs a function this policy governs, and the obligations of this policy do not weaken because the work is performed elsewhere.

Before appointment, {{HOSPITAL_NAME}} establishes and records:

- the provider's legal authorisation to perform the service, and any licence or registration it relies on;
- the methods it operates, and that each is validated for the items {{HOSPITAL_NAME}} will send;
- its qualification, monitoring and calibration regime, and that it meets the requirements of steps 24 to 30;
- its traceability system, and specifically that it can link a load to the items in it and support a recall reaching back to {{HOSPITAL_NAME}};
- its transport arrangements for contaminated and for processed items, including containment, separation and temperature where relevant;
- its recall procedure and its obligation to notify {{HOSPITAL_NAME}} of any failure affecting items it has processed.

The contract states these as obligations, and states expressly: that the provider supplies the load record, the monitoring results and the release evidence for every consignment; that it notifies {{HOSPITAL_NAME}} of any process failure within a stated time; that it permits audit by {{HOSPITAL_NAME}} or its representative; and that it retains records for the period the records retention policy of {{HOSPITAL_NAME}} requires. The provider and the contract review date are [Hospital to define].

{{HOSPITAL_NAME}} audits the provider at a stated frequency, on site, against these obligations, and records the audit and its findings. The audit is performed by {{HOSPITAL_NAME}} rather than accepted from the provider's own assurance, and the findings are carried into contract review and renewal.

Items received back from the provider are checked on receipt as any other processed item is checked at step 19 — packaging integrity, indicator change, labelling, and the accompanying release evidence. A consignment arriving without its release evidence is not put into stock; it is quarantined and the evidence obtained.

Where the provider notifies a failure, {{HOSPITAL_NAME}} enters its own recall route at step 31 for the items concerned. The provider's investigation does not substitute for the hospital's assessment of its own patients under step 34.

The contract manager of {{HOSPITAL_NAME}} is responsible for these obligations being in the contract and being enforced; the Infection Control Officer is responsible for the technical adequacy of the arrangement.""",

"""39. Loaner, consignment and trial instrument sets

Instrument sets brought into {{HOSPITAL_NAME}} for a particular case — loaner sets from a supplier, consignment implant sets, trial instruments, and instruments brought in by a visiting clinician — are the commonest route by which an unprocessed or inadequately processed item reaches a patient. They arrive late, they arrive without documentation, and they arrive under time pressure before a scheduled case, which is exactly the combination this policy exists to resist.

{{HOSPITAL_NAME}} therefore applies the following, without exception:

- a loaner set is booked in advance, and the booking states the case, the date, the set contents and the supplier. The lead time required before the case is [Hospital to define — state the minimum lead time for receipt of a loaner set before the scheduled case], set so that the set can be processed in a normal cycle rather than an immediate-use one;
- the set arrives with its inventory list and the manufacturer's instructions for use for every item in it, including the reprocessing method, cycle parameters and any restriction. A set arriving without its instructions for use is not processed and not used;
- the set is treated as contaminated on arrival regardless of what the supplier states, and is processed in full through the cycle at steps 6 to 20 before use. A set arriving in a sterile pack from the supplier is inspected and, unless the supplier is an authorised processor whose release evidence accompanies it, is reprocessed;
- the set is checked against its inventory on receipt and again before return, and both checks are recorded;
- the set is processed to the instructions for use held for it, and where those instructions specify a cycle {{HOSPITAL_NAME}} cannot perform, the set is not used and the surgeon and supplier are told;
- after use the set is decontaminated before it leaves {{HOSPITAL_NAME}}, and the return is recorded;
- the set's processing records are retained by {{HOSPITAL_NAME}} in the same way as for its own items, and are linked to the patient, so that the set falls within any subsequent recall.

A set that arrives too late to be processed in a normal cycle does not create an exception. The case is postponed, or an alternative set is used. The decision is made by the operating surgeon with the Infection Control Officer, and is recorded, including where a case proceeds and on what basis.

The pattern of late arrivals is trended and reported to the Committee, because it is a supplier and scheduling problem that presents as an infection control one.""",

"""40. Records retained under this policy

{{HOSPITAL_NAME}} retains the following as evidence that this policy operates, available for inspection and retrievable for the whole of the retention period:

Governance and guidance. This policy and its revision history; the written reprocessing guidance; the device classification register at step 2; the manufacturer's instructions for use for every reusable device and every processing machine; the set checklists; the monitoring and validation schedule at step 24; the single-use position and any protocol approved under step 22, with the Committee minutes approving them; the layout drawing of the processing area.

Facility. Ventilation, pressure differential, temperature and humidity monitoring records; water treatment specification and testing results; the risk register entry for any accepted limitation of zoning or separation; the record of every location processing items outside the central area under step 5.

Cycle records. Per load: machine, cycle number, date and time, cycle type, contents, physical parameters, chemical indicator results, biological or process challenge results where required, operator, and the named release decision. Per item or set: identity, processing load, issue destination, and the patient where identified. Point-of-use deviation records from step 7; cleaning verification results from step 9; inspection and rejection records from step 10; high-level disinfection records from step 15 including concentration test results; wet pack and quarantine records from step 17; storage checks from step 18.

Equipment. Installation, operational and performance qualification and every requalification; calibration certificates; daily and periodic performance tests including air removal and leak tests; the maintenance and repair record; the record of every failure, its investigation and its resolution.

Failure and recall. The suspicion and report log from step 31 including reports that proved unfounded; the recall scope authorisation from step 33; retrieval records; the individual patient exposure assessments from step 34; the clinical actions and patient communications; return-to-service authorisations from step 35; the recall report and its corrective actions from step 36; mock recall records and findings from step 37.

People and providers. Training and competency assessment records for every person who processes items, including agency and contract staff; the outsourced provider's authorisation, contract, consignment release evidence and audit reports; loaner set receipt, processing and return records.

Retention periods follow the records retention policy of {{HOSPITAL_NAME}}, subject to the requirement that implant traceability records are kept for at least the period the law and the device's expected life require — [Hospital to define — state the retention period for each class of record under this policy].

This policy is reviewed at the interval {{HOSPITAL_NAME}} sets, and in any event after any recall, any change of steriliser or process, any change to the standard in force, and any change in the services provided — [Hospital to define — state the review interval]."""
,
]

RESPONSIBILITY = """The Infection Prevention and Control Committee owns this policy. It approves the written reprocessing guidance, the device classification register, the monitoring and validation schedule, any single-use reprocessing protocol and the position on single-use devices generally, receives the monitoring trend and every recall report, tracks corrective and preventive actions to closure, reviews the mock recall findings, and escalates unresolved failures and unfunded requirements to management.

The Infection Control Officer is accountable for the technical integrity of reprocessing at {{HOSPITAL_NAME}}. This person approves the classification of any device whose class is uncertain, confirms in writing that any reprocessed single-use device presents no greater risk than a new one, decides on every failed test whether the recall route is entered, authorises the scope of a recall, performs and records the exposure assessment for every affected patient, advises the head of the institution on informing patients, authorises the return of any machine or process to service, sets the enhanced monitoring period that follows, authors the recall report, and decides whether a location processing items outside the central area may continue to do so. A named deputy holds the same authority at all hours.

The person in charge of the processing area of {{HOSPITAL_NAME}} operates the system day to day. This person is accountable for the whole cycle at steps 6 to 20, for zone discipline and the direction of flow, for load release against complete evidence and for refusing release where it is incomplete, for routine monitoring being performed, read and recorded, for taking a machine out of service on a failed test, for quarantining immediately on discovering a breakdown without waiting for approval, for the traceability records that make recall possible, and for the competency of the staff performing each stage.

Processing technicians and any other staff who reprocess items are responsible for performing each stage to the written guidance and the manufacturer's instructions, for signing for the stage they performed, for withdrawing any item that fails inspection, and for reporting immediately any failure, doubt or deviation. Every one of them holds the authority to refuse to release a load.

Biomedical engineering is responsible for installation, operational and performance qualification, for requalification after repair, relocation or unexplained failure, for calibration of gauges, sensors and recorders against traceable references, for planned maintenance to the manufacturer's schedule, and for the technical investigation of an equipment failure.

The engineering service of {{HOSPITAL_NAME}} is responsible for the ventilation, pressure relationships, temperature, humidity, water treatment, steam quality, drainage and power on which the processing area depends, for verifying them at the stated frequency, and for recording the verification.

Heads of clinical departments are responsible for point-of-use treatment being performed in their areas, for the pre-use check at step 19 being made before every pack is opened, for shared non-critical equipment in their area being processed by the person named for it, for responding to a stop-issue instruction without delay, and for the corrective actions assigned to their areas.

The operating surgeon is responsible, jointly with the Infection Control Officer, for any decision to release an implant load before its biological indicator result is available, and for the decision to proceed with or postpone a case where a loaner set has arrived too late to be processed normally.

The contract manager at {{HOSPITAL_NAME}} is responsible for the obligations of this policy being written into the contract of any outsourced processing provider, for obtaining that provider's release evidence and records, for arranging the on-site audit, and for carrying the findings into contract review and renewal.

The purchase function is responsible for procuring devices whose reprocessing instructions {{HOSPITAL_NAME}} can actually perform, for obtaining and passing on the instructions for use for every device acquired, and for procuring consistently with the single-use position at step 21.

The head of the institution is accountable for providing the space, equipment, staffing and utilities this policy assumes, for authorising any continued use of a machine overdue requalification, for authorising the decision to inform exposed patients and all external communication about a recall, for deciding on the replacement of a repeatedly failing machine, and for the undertaking that no member of staff is penalised for refusing to release an unverified load or for reporting a suspected failure.

All staff are responsible for treating an item of unverified sterility as non-sterile, and for reporting immediately any suspicion that the sterilisation system has failed — a duty that belongs to every member of staff of every grade and is exercised directly."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Hospital Infection Control chapter, standard HIC.6.
- Centers for Disease Control and Prevention and the Healthcare Infection Control Practices Advisory Committee, Guideline for Disinfection and Sterilization in Healthcare Facilities — the device classification on which step 2 is based, the cleaning-before-disinfection principle, high-level disinfection practice, and sterilisation monitoring.
- World Health Organization and Pan American Health Organization, Decontamination and Reprocessing of Medical Devices for Health-care Facilities — the decontamination life cycle, processing area zoning and workflow, and reprocessing practice in resource-limited settings.
- World Health Organization, Guidelines on Core Components of Infection Prevention and Control Programmes at the National and Acute Health Care Facility Level.
- International Organization for Standardization, ISO 17665 — sterilisation of health care products, moist heat: requirements for the development, validation and routine control of a sterilisation process.
- International Organization for Standardization, ISO 11135 — sterilisation of health care products, ethylene oxide.
- International Organization for Standardization, ISO 11138 series — sterilisation of health care products, biological indicators.
- International Organization for Standardization, ISO 11140 series — sterilisation of health care products, chemical indicators and their classification.
- International Organization for Standardization, ISO 15883 series — washer-disinfectors: requirements, testing and performance.
- International Organization for Standardization, ISO 11607 series — packaging for terminally sterilised medical devices.
- Association for the Advancement of Medical Instrumentation, ANSI/AAMI ST79, Comprehensive guide to steam sterilization and sterility assurance in health care facilities — load release, process challenge devices, air removal testing, qualification and requalification.
- Association for the Advancement of Medical Instrumentation, ANSI/AAMI ST91:2021, Flexible and semi-rigid endoscope processing in health care facilities — the endoscope-specific requirements in step 15: leak testing before cleaning on every use, mandatory cleaning verification, borescope inspection of internal channels, active drying with defined equipment, storage, and the certification and competency of endoscope reprocessing personnel.
- Association for the Advancement of Medical Instrumentation, ANSI/AAMI ST108:2023, Water for the processing of medical devices — the water quality categories, including the critical water specification applied to the final rinse of endoscopes at step 15, and the microbial, endotoxin and chemical limits, testing frequency and action limits that go with it.
- United States Food and Drug Administration, safety communications on duodenoscope reprocessing and on transmission of multidrug-resistant organisms by reprocessed endoscopes — the documented outbreak history that is the reason step 15 treats these devices separately.
- Indian Council of Medical Research, Hospital Infection Control Guidelines, and the ICMR treatment guidelines for antimicrobial use insofar as they bear on device-related infection.
- National Centre for Disease Control, Ministry of Health and Family Welfare, Government of India, National Guidelines for Infection Prevention and Control in Healthcare Facilities.
- Drugs and Cosmetics Act, 1940 and the Medical Devices Rules, 2017, and the requirements of the Central Drugs Standard Control Organisation applying to medical devices and to any reprocessing of them.
- Bio-Medical Waste Management Rules, 2016, and subsequent amendments, in respect of the disposal of single-use items, withdrawn devices and processing waste.
- Internal documents of {{HOSPITAL_NAME}}: infection prevention and control programme policy, infection prevention and control practices policy, infection prevention and control in support services policy, prevention of healthcare associated infections and staff occupational health policy, infection prevention and control surveillance policy, occupational health policy, records retention policy, and the procurement and contract management procedures."""

DISTRIBUTION = """Controlled master copy: Infection Control Team, {{HOSPITAL_NAME}}.

Copies issued to: the office of the head of the institution; the Infection Prevention and Control Committee (all members); the Infection Control Officer and the Infection Control Nurse; the central sterile supply department and every location processing items outside it; operating theatres, recovery and the theatre sub-sterile area; the labour room; every inpatient ward and critical care and high-dependency area; emergency, outpatient, day-care and dialysis; the endoscopy and dental suites where provided; nursing administration; biomedical engineering and engineering services; pharmacy and stores; purchase and the contracts function, for onward issue to any outsourced processing provider and to loaner set suppliers; housekeeping; occupational health; medical records; and the quality or accreditation coordinator.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. Extracts relevant to a specific process are displayed as job aids at the point of work, in the languages staff read: the device classification register, at the sorting bench and in every clinical area holding reusable items; the detergent and disinfectant dilution, temperature and contact time, at each sink and each disinfection station; the loading pattern and pack size limits, at each steriliser; the single-use symbol and the rule against reprocessing, at the sorting bench and in every clinical area; the pre-use check at step 19, at every point where a sterile pack is opened; and the breakdown reporting contact and number, in the processing area, theatre, and every clinical area. The 24-hour contact for the Infection Control Officer and deputy, and the standing authority of processing staff to quarantine and to refuse release, are included in the induction pack issued to every worker in the processing area, including contracted and agency staff.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the Infection Control Team."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1, HIC.2, HIC.3, HIC.4 and HIC.5 master policies are not repeated here. A reader using this document on its own should refer to those policies for the full infection control glossary, including CSSD, OT, ICU, PPE, IPC, IPCC, ICC, ICN, ICO, ICT, HAI, MDRO, MRSA, VRE, CRE, ESBL, MDR, XDR, PDR, CAUTI, CLABSI, SSI, VAE, VAP, IVAC, PVAP, HAP, LCBI, SUTI, UTI, CVC, PICC, ABHR, BMW, HEPA, AIIR, ACH, AHU, HVAC, SOP, IEC, IDSP, IHIP, IPCAF, AMR, ASP, AST, ATP, CAPA, CFU, CLSI, DDD, AWaRe, HBV, HCV, HIV, PEP, NSI, PoA, RCA, RLU, SIR, ICMR, NABH, NCDC, NHSN, WHO, CDC, SHEA, NACO, SHCO and OE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.5:

AAMI — Association for the Advancement of Medical Instrumentation
BI — Biological Indicator
CDSCO — Central Drugs Standard Control Organisation
CI — Chemical Indicator
EO — Ethylene Oxide
HLD — High-Level Disinfection, or High-Level Disinfectant
IFU — Instructions For Use (the device or equipment manufacturer's)
IQ — Installation Qualification
ISO — International Organization for Standardization
IUSS — Immediate-Use Steam Sterilisation
OPA — Ortho-Phthalaldehyde
OQ — Operational Qualification
PCD — Process Challenge Device
PQ — Performance Qualification
RO — Reverse Osmosis
SAL — Sterility Assurance Level
SUD — Single-Use Device
TSE — Transmissible Spongiform Encephalopathy
WD — Washer-Disinfector

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

# Verbatim from the approved HIC.3 / HIC.4 / HIC.5 master policies -- do not edit. The master
# template boilerplate is shared across the HIC set, so any change belongs in a deliberate pass
# over all of them, not in this file. Verified below against the live HIC.5 row by hash.
DISCLAIMER = """This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Bio-Medical Waste Management Rules, 2016 and the Food Safety and Standards Act, 2006. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced."""

# md5 of the live HIC.5 disclaimer with CR stripped, read from shco_policy_masters on
# 2026-08-10. HIC.3, HIC.4 and HIC.5 all carry this identical value; HIC.6 makes four.
HIC5_DISCLAIMER_MD5_LF = "ae331bb0cb2ca6428d4d1e0800e51e60"

OE_MAPPING = [
    {
        "oe_code": "HIC.6.a",
        "requirement": "Adequate space and appropriate zoning are provided for sterilisation activities",
        "steps": "Steps 1-5",
        "evidence": "Marked layout drawing of the processing area showing the three zones — decontamination, clean assembly and packing, sterile storage — with the physical barrier and the transfer points; documented unidirectional workflow and the rule that an item never moves backwards through a zone; ventilation records showing air change rates and the pressure gradient from clean to dirty with the design basis and the standard relied on, verified at a stated frequency; temperature and humidity monitoring records for the clean and storage zones with the excursion response; water treatment specification and testing results for final rinse and steam generation; hand-wash and eyewash provision in the decontamination zone; drainage, power and compressed air provision; the written statement of which items are processed centrally and which outside, with the location list required by step 5 stating items, method, operator, monitoring and record location for each; where the building cannot achieve full separation, the written compensating measures and the corresponding entry in the infection control risk register with evidence of Committee review",
        "responsible": "Head of the institution for space, capital and utilities provision; person in charge of the processing area for zone discipline and direction of flow; engineering for ventilation, pressure, temperature, humidity, water and steam quality with verification records; Infection Control Officer for approving compensating measures and for deciding whether a decentralised location may continue processing; IPCC for accepting any recorded limitation",
    },
    {
        "oe_code": "HIC.6.b",
        "requirement": "Cleaning, packing, disinfection and/or sterilisation, storing and the issue of items is done as per the written guidance",
        "steps": "Steps 2, 6-20, 38-40",
        "evidence": "The written reprocessing guidance itself, approved, version-controlled and covering every stage of the cycle; the device classification register assigning every reusable item to critical, semi-critical or non-critical with the processing level required, approved by the IPCC and reviewed annually; manufacturer's instructions for use held for every reusable device and every processing machine, with evidence they are followed; point-of-use treatment and transport records, and the receipt deviation log with its trend to the IPCC; manual cleaning records with detergent, dilution, temperature and contact time, and the same displayed at the sink; ultrasonic and washer-disinfector cycle printouts, daily machine checks and cleaning verification results with the acceptance criterion; inspection and functional check records with the rejection and repair route; set checklists and assembly sign-off by named person; packing records identifying packaging system, pack size and mass limits, internal and external indicator placement, and the label carrying contents, steriliser, load number, date, expiry or review status and packer; per-load sterilisation records showing cycle type, parameters achieved, indicator results, operator and the named release decision; high-level disinfection records for semi-critical devices with agent, concentration test result, contact time, rinse, drying and storage — including the ventilator accessories, humidifiers, heat and moisture exchangers, nebuliser chambers and resuscitation bags that the HIC.4 policy requires to be reprocessed between patients; for flexible and semi-rigid endoscopes additionally, per device and per use, the leak test result recorded before cleaning, the mandatory cleaning verification result for every cycle with its acceptance criterion, borescope inspection findings of internal channels and distal end at the stated frequency with the action taken on any device found with retained soil, retained fluid or channel damage, the active drying method, equipment and duration with the storage arrangement and validated storage interval, the endoscope rinse water specification with its testing frequency and action limits, the unique device identifier linking every use to the patient in both directions, the repair and service history per device, and the certification and competency records of every person who reprocesses endoscopes including agency and contract staff; where endoscopy is not performed, the signed and dated declaration to that effect with its reason, referral arrangement and annual review; unloading, wet pack and cooling records; sterile storage conditions, the shelf life system adopted and its basis, stock rotation and the periodic check for expired, damaged or unlabelled packs; issue register linking load to department and, where identified, to patient; the point-of-use check of indicator and pack integrity before opening, and the record of any pack rejected at that check; outsourced provider contract, consignment release evidence and on-site audit reports; loaner set booking, inventory, instructions for use, processing and return records; training and competency records for every person performing each stage",
        "responsible": "Person in charge of the processing area accountable for the whole cycle and for load release, and authorised to refuse release; trained processing technicians for each stage with named sign-off; heads of clinical departments for point-of-use treatment and for the pre-use check; Infection Control Nurse for audit of adherence; contract manager for outsourced processing and loaner suppliers; purchase for obtaining instructions for use at procurement; IPCC for approving the written guidance and the classification register",
    },
    {
        "oe_code": "HIC.6.c",
        "requirement": "Reprocessing of single-use instruments, equipment and devices is done as per written guidance",
        "steps": "Steps 21-23",
        "evidence": "The written position of {{HOSPITAL_NAME}} on devices labelled single-use, approved by the IPCC with the approval minuted, stating the default that such a device is used once and discarded; the list of any device categories for which reprocessing is nevertheless approved, or the explicit record that none is; for each approved category, a protocol naming the device by manufacturer, model and catalogue reference and stating the regulatory basis relied on, the validated cleaning method including how each lumen is reached and how cleaning is verified, the validated sterilisation or disinfection method with the evidence it achieves sterility without degrading the device, the maximum number of cycles with its basis, the method of counting cycles at the level of the individual item, the acceptance criteria applied before each reuse and who applies them, the uses for which the device may not be used, the record kept per device and per cycle with its link to the patient, and the review date and withdrawal trigger; the Infection Control Officer's written confirmation that a reprocessed device of the category presents no greater risk than a new one; the recorded position on whether patient consent is separately sought; the never-reprocess list at step 23 and the withdrawal, marking and disposal records for items removed under it; training records on recognising single-use marking; the deviation log of single-use items found in the reusable stream, with feedback to the sending area and the trend reported to the IPCC",
        "responsible": "IPCC approves the position and every protocol and minutes the decision; Infection Control Officer accountable for the clinical risk judgement and for the written confirmation, and is the only person who may reverse a withdrawal under step 23; person in charge of the processing area for protocol execution and cycle counting; purchase for procuring consistently with the position; heads of clinical departments for compliance at the point of use; any staff member or clinician may withdraw an item under step 23 without prior authorisation",
    },
    {
        "oe_code": "HIC.6.d",
        "requirement": "Regular validation tests for sterilisation are carried out and documented",
        "steps": "Steps 24-30, 38",
        "evidence": "The written monitoring and validation schedule, approved by the IPCC and reviewed annually and on any change of machine or standard, stating for each machine and cycle what is tested, at what frequency, by whom, where in the chamber or load, the acceptance criterion and the failure response; physical and mechanical monitoring — the machine's own printout or data log for every cycle, examined and signed by the operator before release, with the temperature, pressure and phase durations checked against specification; calibration certificates for gauges, sensors, timers and recorders against traceable references, with the frequency and provider stated; chemical indicator records with the class used externally, internally and within any process challenge device stated against the standard in force, the lot number in use, and the reading against the manufacturer's reference; biological indicator records with organism, lot, placement in a process challenge device at the location determined at qualification, the incubated negative control from the same lot, incubation conditions, result, reader and time; the rule and its records that every implant load is biologically monitored and quarantined pending result, with any early release recorded by patient, reason and authorising person and its frequency tracked; daily air removal test and periodic leak test records with acceptance criteria for dynamic-air-removal sterilisers, and the record of which machines are gravity displacement and what each may process; installation, operational and performance qualification records for every steriliser, washer-disinfector and automated disinfection machine, with performance qualification repeated for each distinct load type; requalification after relocation, major repair, utility change or unexplained failure; the planned maintenance and repair record; the failure record at step 30 with quarantine, machine withdrawal, investigation, cause, correction and the Infection Control Officer's written return-to-service authority; the enhanced monitoring period following return to service; trend review of monitoring results tabled at the IPCC; equivalent qualification, monitoring and calibration evidence obtained from any outsourced processing provider and verified by on-site audit",
        "responsible": "Person in charge of the processing area performs and records routine monitoring and releases loads only on complete results; processing technicians read and record indicators and may refuse release; biomedical engineering for qualification, requalification, calibration and planned maintenance; external qualification provider under contract with traceable instruments; Infection Control Officer reviews every failure and is the only person who authorises return to service and sets the enhanced monitoring period; head of the institution for any decision to continue using a machine overdue requalification, and for replacement of a repeatedly failing machine; IPCC for the schedule and the trend",
    },
    {
        "oe_code": "HIC.6.e",
        "requirement": "The established recall procedure is implemented when a breakdown in the sterilisation system is identified",
        "steps": "Steps 31-37, 40",
        "evidence": "The written recall procedure, approved and rehearsed, defining what constitutes a breakdown and listing the triggers at step 31 — positive biological indicator, failed chemical indicator including one found at the point of use, out-of-specification physical record discovered after release, failed air removal or leak test, calibration or requalification lapse, systematic process deviation, wet packs after issue, a surveillance-referred infection cluster implicating a processed item, and a manufacturer's or regulator's recall; the named Infection Control Officer and deputy with 24-hour contact details, and the standing authority of processing staff to quarantine and stop issue immediately without waiting for approval or a meeting; the suspicion and report log with date, time, reporter, observation and action, including reports that proved unfounded and their acknowledgement; the record of the decision whether to enter the recall route, with reasons, taken either way; containment records showing the time of identification, the time each immediate measure was completed and the interval between them; the written recall scope authorised by the Infection Control Officer before retrieval begins, stating the machine, period, load numbers and item categories, with the reasoning for reaching back to the last satisfactory result of the type that failed, and the record of any widening or narrowing with its basis; retrieval records worked and signed off by location, recording each item as retrieved, already used or not accounted for, and the escalation of anything unresolved; the individual documented exposure assessment for every patient on whom an affected item was used, covering the nature of the failure, the device class and tissue contacted, implant involvement, patient susceptibility, organisms plausibly involved and the clinical course; the clinical actions taken including enhanced follow-up parameters, and testing or prophylaxis provided at the hospital's cost; the decision on informing patients with its reasoning either way, the head of the institution's authority for it, and the record of communications made; statutory, regulatory and manufacturer reports with dates; reprocessing of recalled items from the first stage with packaging discarded, and release records annotated as recall items; return-to-service evidence — cause identified or explicitly not established, correction made, requalification, satisfactory full monitoring set on test cycles, and the Officer's written authority with date and time; the enhanced monitoring period and the recorded decision to return to routine; the written recall report within the stated period, tabled at the IPCC and copied to the head of the institution, stating how the failure was found, the interval to containment, scope, retrieval outcome, patients exposed and assessed, investigation and cause including where none was established, and CAPA with single named owners and due dates; evidence the CAPA register was tracked to closure and verified by re-measurement, including actions recorded as ineffective; evidence the lessons reached the written guidance, the training programme and the monitoring schedule; mock recall records at the stated interval and at least annually, timed, with the traceability gaps exposed and the corrective actions closed by re-testing",
        "responsible": "Any member of staff of any grade identifies and reports a suspected breakdown directly and without going through a line manager; person in charge of the processing area quarantines and stops issue immediately on discovery, without waiting for approval; Infection Control Officer decides on entry to the recall route, authorises the scope, performs the patient exposure assessments, advises on patient notification, authorises return to service and authors the report, with a named deputy holding the same authority at all hours; head of the institution authorises the decision to inform exposed patients and all external communication, and decides on machine replacement; treating clinicians for the clinical assessment and follow-up of exposed patients; biomedical engineering for the equipment root cause; Infection Control Nurse cross-references any resulting infection to surveillance under the HIC.5 policy; IPCC receives the report and the mock recall findings and tracks CAPA to closure",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. HIC.6 standard text and all five OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF held locally at "C:/Users/SERVER/Desktop/NABH/SHCO-Standards-3rd-Edition.pdf", Chapter 5, printed page 96 (PDF page index 102). Levels: HIC.6.a Commitment, HIC.6.b Core, HIC.6.c Commitment, HIC.6.d Commitment, HIC.6.e Commitment. Cross-checked against the live shco_full_oes table; both agree.
   FOUR OF THE FIVE OEs CARRY THE ASTERISK -- b, c, d AND e. This standard has NO single documented-evidence anchor, which is why the draft builds four separate deep evidence blocks (steps 6-20 for b, 21-23 for c, 24-30 for d, 31-37 for e) rather than concentrating depth in one as HIC.5 did on outbreaks. HIC.6.a is the only unasterisked OE and is correspondingly the shortest block.
   THE HIC.6.e ASTERISK WAS MISSING FROM THE DATABASE UNTIL 2026-08-10. It was found on 2026-08-07 while verifying HIC.5, logged in scripts/master-policy-todos.md, and corrected on 2026-08-10 as part of a ten-chapter audit that found 14 such errors in total, all in the same direction. Had HIC.6 been drafted from the database before that audit, the recall procedure -- the OE an assessor is most likely to ask a document for -- would have been built as an ordinary Commitment element. Reviewer to note: this draft is built against the PDF and against the corrected table, which now agree.
   ONE SOURCE ARTEFACT, COSMETIC ONLY: the PDF's text layer drops the "fi" ligature, so HIC.6.e extracts as "identied" for "identified", the same artefact seen in HIC.5.d. Does not affect meaning.
   The SHCO 3rd Edition standards PDF contains no per-standard interpretation text for any HIC standard -- only intent, standards, OEs and a chapter reference list. Nothing was omitted for want of access.

DEVICE CLASSIFICATION AND PROCESSING LEVEL (step 2)
1. The critical / semi-critical / non-critical classification, and the processing level each requires -- sterilisation for critical, at minimum high-level disinfection for semi-critical, cleaning plus low- or intermediate-level disinfection for non-critical. This is the Spaulding scheme, verified against the CDC/HICPAC Guideline for Disinfection and Sterilization in Healthcare Facilities. Step 2.
2. High-level disinfection destroys all microorganisms except large numbers of bacterial spores. Standard definition, same source. Steps 2, 15.
3. Classification follows intended use and the tissue contacted, not the department holding the item. Standard application of the scheme. Step 2.

CLEANING (steps 6, 8, 9)
4. Cleaning must precede disinfection and sterilisation, and organic matter shields organisms and neutralises many agents. Foundational and uncontested. Policy statement, steps 1, 8, 15.
5. Dried soil is substantially harder to remove and saline causes pitting and corrosion; point-of-use treatment and keeping instruments moist are the standard countermeasures. Step 6.
6. Water above the protein coagulation point fixes blood to the instrument. Standard practice teaching; THE DRAFT DOES NOT STATE A TEMPERATURE, pointing instead at the detergent's instructions, since the figure varies by product. Step 8.
7. Ultrasonic cleaning does not remove gross soil and requires degassing; instruments of dissimilar metals are not mixed. Standard. Step 9.
8. Visual inspection will not detect residual protein in lumens and box joints, which is why a cleaning verification method is required. Verified against the disinfection and sterilization guideline and the washer-disinfector standard. Step 9. THE METHOD AND ACCEPTANCE CRITERION ARE LEFT AS [Hospital to define] against the standard in force.

PACKAGING, STERILISATION AND STORAGE (steps 11-14, 17, 18)
9. Packaging must permit sterilant penetration and removal and then maintain a microbial barrier while intact and dry; pins, staples and clips perforate the barrier. Verified against ISO 11607 and AAMI ST79. Step 11.
10. Moist heat requires air removal, saturated steam of correct quality, and time at temperature throughout the load, and the failure of any one invalidates the cycle. Superheated steam behaves as hot air. Verified against ISO 17665 and ST79. Step 13.
11. NO CYCLE PARAMETERS ARE STATED ANYWHERE IN THIS DRAFT -- no temperatures, no exposure times, no drying times, no HLD concentrations or contact times, no shelf-life periods, no air change rates, no biological indicator frequencies. This was CONFIRMED AS THE DEFAULT BY THE OWNER on 2026-08-10: these are machine-, cycle-, load- and device-specific, and a figure transcribed from a general source into a hospital's controlled document is a patient-safety hazard rather than a documentation convenience. Every one is left as [Hospital to define] against the manufacturer's instructions for use and the standard in force. This is the same treatment HIC.5 gave to SSI surveillance windows and the CLSI minimum isolate count, and it is deliberate throughout. Reviewer to note this is a decision, not an omission.
12. Ethylene oxide penetrates well including lumens but is toxic, flammable and carcinogenic and requires aeration; hydrogen peroxide processes are absorbed by cellulose so paper, linen and cotton cannot be processed and lumen penetration is limited to what is validated; liquid chemical sterilant immersion produces no storable pack and the item is subject to recontamination at rinse and transfer. Verified against the CDC disinfection and sterilization guideline. Step 14.
13. Wet packs are unsterile because moisture wicks organisms through the barrier; a warm pack draws air in as it cools and condensate forms where a warm pack meets a cold surface. Standard, and the basis for the cooling rule. Step 17.
14. Event-related and time-related shelf life are both recognised systems; under an event-related system the date on the pack is the processing date and sterility is maintained unless an event compromises the package. Verified against ST79. Step 18. WHICH SYSTEM IS USED IS LEFT TO THE HOSPITAL.
15. Immediate-use steam sterilisation is not for routine use, is never used for implants, and its commonest real cause is insufficient instrument inventory. Verified against ST79 and the CDC guideline. Step 12. The draft permits it only on a recorded exception basis and refers repeated use to management as an inventory problem.

SINGLE-USE DEVICES (steps 21-23)
15a. FLEXIBLE AND SEMI-RIGID ENDOSCOPES -- ADDED 2026-08-10 ON INSTRUCTION, as a distinct subsection of step 15. Basis: ANSI/AAMI ST91:2021, Flexible and semi-rigid endoscope processing in health care facilities, with ANSI/AAMI ST108:2023 for reprocessing water quality. Added because the original draft listed flexible endoscopes as one example among laryngoscope blades, respiratory equipment and probes, and gave them no distinct treatment despite their being the hardest reusable device to reprocess and the one with the worst documented transmission record.
   SCOPE DELIBERATELY NARROW: the subsection states in its first paragraph that it applies to flexible and semi-rigid endoscopes and to no other device, and that laryngoscope blades, respiratory and anaesthesia equipment and reusable probes remain under the generic process. This was an explicit instruction and should not be widened without a decision.
   PLACED AS A SUBSECTION OF STEP 15 RATHER THAN A NEW STEP 16. Inserting a new step would have renumbered steps 16-40 and required rewriting 107 numeric cross-references across the procedure, the responsibility section, the OE mapping and this checklist. The risk of a silently wrong cross-reference in a controlled clinical document was judged to outweigh the benefit of a separate step number. Reviewer to note this was a deliberate structural choice, not an oversight.
   The specific facts, each verified against ST91:2021 unless noted:
   - Leak testing after every use and BEFORE immersion, by the manufacturer's method, because its purpose is to detect a breach before fluid enters it; a failed leak test means the device is not reprocessed and not used, and is quarantined for repair.
   - Cleaning verification for endoscopes is MANDATORY EVERY CYCLE, deliberately departing from the schedule-driven position at step 9 that governs other devices. The draft says so explicitly so the departure is visible rather than looking like an inconsistency. Tests named are the recognised residual-soil markers (ATP bioluminescence, protein, carbohydrate, haemoglobin); NO ACCEPTANCE THRESHOLD IS STATED -- left to the test manufacturer's criterion, consistent with the no-numbers rule at item 11.
   - Borescope inspection of internal channels and distal end, because external visual inspection cannot see into a channel and published inspection studies routinely find retained soil, retained fluid, scratches and adhesive failure in devices that passed every external check. FREQUENCY LEFT AS [Hospital to define] -- ST91 requires inspection but the interval is a local decision.
   - Active drying with a drying cabinet or forced-air system delivering filtered air through every channel, with passive drip-drying, wiping and hanging a wet endoscope expressly not accepted. Residual moisture permitting waterborne organism growth is the mechanism behind a substantial part of the endoscope outbreak literature. Drying time and storage interval left as [Hospital to define], with the note that a validated drying cabinet's own storage interval governs where one is used.
   - Reprocessing water quality per ST108:2023 critical water for the final rinse, IN ADDITION TO the general water provisions at step 4, since potable-quality rinse water recontaminates a device that has just been disinfected. Specification, treatment, testing frequency and action limits left as [Hospital to define].
   - Personnel certification within two years of starting in the role, and competency verified by direct observation before unsupervised reprocessing, with reassessment at a stated interval and after any reprocessing failure. THE TWO-YEAR FIGURE IS THE ONE NUMBER STATED IN THIS SUBSECTION and it comes directly from the instruction and from ST91's certification provision; the certification scheme itself is left as [Hospital to define] because accepted schemes differ by country.
   - The outbreak history referred to in the draft -- transmission of multidrug-resistant organisms including carbapenem-resistant Enterobacterales by duodenoscopes reprocessed according to the manufacturer's instructions then in force, and the resulting regulatory safety communications and device design changes -- is stated in general terms with NO SPECIFIC OUTBREAK, HOSPITAL, DATE OR CASE COUNT NAMED, deliberately. The FDA safety communications are cited in the reference list as the place to look.
   - NOT-APPLICABLE HANDLING: a hospital not performing endoscopy records a signed, dated declaration with reason, referral arrangement and annual review rather than deleting the subsection, mirroring the invasive-ventilation applicability declaration in the approved HIC.5 draft. This is required because these masters are multi-tenant templates; HMP Foundation's own position is a [Hospital to define] entry, not a reason to omit the content.

16. The reasons a single-use device is not reprocessed by default -- not designed to be cleaned, lumens that cannot be reached or verified, no validated reprocessing method, material degradation not visible externally, and the manufacturer's liability not extending past first use. Standard position, consistent with the CDC guideline and with regulatory positions internationally. Steps 21, 22.
17. Reprocessing of single-use devices is regulated, and in some jurisdictions is permitted only by a licensed reprocessor. THE DRAFT DOES NOT ASSERT WHAT INDIAN LAW PERMITS. It requires the protocol to state the regulatory basis relied on and to confirm that reprocessing is permitted under the law applying to the hospital and under its own licence conditions, and it names the Drugs and Cosmetics Act, the Medical Devices Rules 2017 and CDSCO in the reference list as the place to look. THIS IS DELIBERATE -- the regulatory position is exactly the kind of fact that changes and that varies by device class, and stating it would be worse than pointing at it. CONFIRMED CORRECT AS DRAFTED BY THE OWNER on 2026-08-10: do not assert a legal position. Consider whether legal advice should be obtained before any protocol is approved.
18. Devices contacting central nervous system or posterior eye tissue in a patient with suspected transmissible spongiform encephalopathy are not reliably decontaminated by conventional sterilisation and are destroyed. Verified against the CDC guideline's prion section. Step 23. The draft points at the practices policy for the handling precautions rather than restating them.

MONITORING AND VALIDATION (steps 24-30)
19. Validation and routine monitoring are different things and both are required; monitoring cannot rescue an unqualified machine. Verified against ISO 17665 and ST79. Step 24.
20. The four monitoring levels and what each does and does not prove -- physical shows chamber conditions but not the inside of a pack; chemical shows exposure at a point but not lethality; biological shows lethality for the challenge presented at the point placed; air removal shows steam can reach the load at all. Verified against ST79. Steps 24-28.
21. A CHANGED CHEMICAL INDICATOR IS NOT PROOF OF STERILITY, and treating it as such is the commonest error in this field. Explicit in the CDC guideline and in ST79. The draft states this in terms at step 26 because it is the single most consequential misunderstanding a reviewer could leave in place.
22. Chemical indicators are classified by what they respond to, from simple process indicators through single-variable to integrating indicators correlating with biological performance. Verified against ISO 11140. THE DRAFT DOES NOT NUMBER THE CLASSES, because the numbering is standard-specific and has been revised; it describes them and leaves the class used at each point as [Hospital to define] against the standard in force. Step 26.
23. A biological indicator requires an incubated unprocessed control from the same lot, without which a negative result is uninterpretable. Verified against ISO 11138 and ST79. Step 27.
24. Every implant load is biologically monitored and quarantined pending the result; early release is an exception requiring recorded authority and follow-up. Verified against ST79 and the CDC guideline. Step 27. The draft additionally requires the hospital to track how often early release occurs, on the reasoning that a pattern indicates an inventory or scheduling problem -- that inference is an editorial position, not a cited requirement. CONFIRMED KEPT AS DRAFTED BY THE OWNER on 2026-08-10.
25. Air is the principal obstacle to steam sterilisation, collects in the coolest and most enclosed locations, and a correct chamber temperature says nothing about a trapped air pocket; hence a separate daily air removal test for dynamic-air-removal sterilisers and a periodic leak test. Verified against ST79 and ISO 17665. Step 28. THE TEST NAME AND ACCEPTANCE CRITERION ARE LEFT AS [Hospital to define] -- the widely known eponymous test is one method among several and its acceptance criteria are standard-specific.
26. Gravity displacement sterilisers remove air less effectively and are correspondingly restricted in load types and packaging. Standard. Step 28.
27. Installation, operational and performance qualification, with performance qualification repeated per load type and requalification after relocation, major repair, utility change or unexplained failure. Verified against ISO 17665 and ST79. Step 29. The point that performance qualification identifies the coldest location in a real load, which then determines where the process challenge device is placed, is the practically important one and is stated explicitly.
28. A POSITIVE BIOLOGICAL INDICATOR WITH A VALID CONTROL IS A FAILURE AND TRIGGERS RECALL IMMEDIATELY; repeating the test in the hope of a different result, in place of acting, is the classic error. The draft permits a repeat only in parallel with the recall, never instead of it. Verified against ST79 and the CDC guideline. Steps 27, 30.

RECALL (steps 31-37)
29. The recall scope rule -- back to the last load with a satisfactory result of the type that has now failed. Verified against ST79. Step 33. The draft extends the same logic to calibration and qualification lapses and to process deviations, which is a reasoned application rather than a quoted rule; reviewer to note.
30. Traceability must work in both directions -- patient to load and load to every patient and location -- or a recall cannot be executed. Standard, and the practical basis for steps 11, 19, 20 and 37. THE DRAFT TREATS INABILITY TO ESTABLISH THE LAST SATISFACTORY RESULT AS ITSELF A FINDING requiring corrective action, which is an editorial position and is stated as such at step 33. CONFIRMED KEPT AS DRAFTED BY THE OWNER on 2026-08-10.
31. Mock recalls as the means of testing traceability before it is needed. Established practice in sterile services and borrowed from recall practice generally. Step 37. The requirement to time the exercise, and the point that a load chosen because it is easy to trace tests nothing, are editorial. Reviewer to confirm the interval and that an annual minimum is wanted.
32. A significant proportion of process failure investigations close without an established cause; the draft expressly permits an honest "cause not established" conclusion rather than discouraging it, mirroring the position taken in the approved HIC.5 draft on outbreaks. Step 36. Editorial position carried across for consistency.
33. PATIENT NOTIFICATION AFTER EXPOSURE -- THE DRAFT TAKES A POSITION AND THE REVIEWER SHOULD SEE IT. Step 34 states that {{HOSPITAL_NAME}} starts from the position that a patient exposed to a material risk is told, and that the burden lies on any argument for not telling them, with the decision reserved to the head of the institution on the Infection Control Officer's written advice and recorded either way. This is a policy and ethical position rather than a cited technical requirement. It is consistent with the disclosure posture of the approved HIC.1 and HIC.5 documents, and with the non-punitive reporting position taken throughout the set. CONFIRMED KEPT BY THE OWNER on 2026-08-10 as consistent with the set's disclosure posture. The hospital should still satisfy itself that it does not conflict with any legal advice it has taken.
34. TESTING OR PROPHYLAXIS AT THE HOSPITAL'S COST, step 34. Same class of decision as the "on full pay" line confirmed for HIC.5 step 34 on 2026-08-07, and kept for the same two reasons: it is consistent with the approved HIC.4 position that no cost under that policy is passed to a worker, and cost is the obvious barrier to a patient completing follow-up the hospital's own failure made necessary. CONFIRMED KEPT BY THE OWNER on 2026-08-10. Reviewer to note it is an editorial position with a financial consequence.

FORWARD REFERENCES FROM THE APPROVED DOCUMENTS -- HONOURED, AND VERIFIED
This standard is the reverse of the HIC.2/HIC.4/HIC.5 overlap pattern. Rather than duplicating approved content, HIC.3, HIC.4 and HIC.5 have all DEFERRED TO a "sterilisation and disinfection policy" that did not exist -- seven references in total. Three of those are substantive promises, and this draft was checked against each of them:
  - HIC.3 SCOPE promises this policy covers "the reprocessing, disinfection and sterilisation of instruments, equipment and devices, including the Spaulding classification of devices as critical, semi-critical or non-critical, central sterile supply processes, sterilisation indicators and sterile storage". DELIVERED: Spaulding at step 2, CSSD processes at steps 3-20, indicators at steps 26-28, sterile storage at step 18.
  - HIC.3 STEP 15 promises this policy governs "selection and reprocessing of disinfectants for instruments and devices, including the classification of devices as critical, semi-critical or non-critical and the choice of high-level disinfectant". DELIVERED: step 2 and step 15, with step 15 naming the agent classes in recognised use and leaving the selection to the device instructions for use.
  - HIC.4 STEP 10 requires humidifiers, heat and moisture exchangers, nebuliser chambers, resuscitation bags and ventilator accessories to be "reprocessed between patients according to the sterilisation and disinfection policy, and the reprocessing is recorded". DELIVERED: step 15 names those items explicitly and supplies both the method and the record.
  - HIC.4 STEP 20 requires that "instruments, implants and supplies are sterile, and their sterility is confirmed at the point of use by checking the indicator and the pack integrity, in accordance with the sterilisation and disinfection policy". DELIVERED: step 19 sets out that check and the record of any pack rejected at it, and states in terms that it is the check HIC.4 refers to.
  The policy TITLE was chosen to match the name those documents already use for it, so their references resolve. NO RECONCILIATION PASS IS CREATED BY THIS DRAFT on any of the four. The build script asserts all six markers at build time, so a later edit that drops one will break the build rather than silently orphan an approved document's cross-reference.

BOUNDARY WITH HIC.3 -- STATED, NOT SILENTLY DRAFTED AROUND
  HIC.3 step 7 ("Physical separation of clean and contaminated flows") already covers hospital-wide clean/dirty separation, including defined routes for used instruments and the rule that sterile supplies are never stored in a sluice or waste holding area. HIC.6.a is the zoning INSIDE the processing unit. The two are adjacent and a reader can arrive at either. The Scope section of this draft states the division explicitly -- the support services policy owns the building's flows, this policy owns the processing area's internal zoning -- and step 3 closes with a sentence pointing back. HIC.3 was NOT reopened and no divergence was created; this is a boundary statement, not a conflict. Consistent with the treatment HIC.5 gave its three overlaps.

BOUNDARY WITH HIC.5 -- PRE-AGREED, CROSS-LINKED BOTH WAYS
  HIC.5 step 32 quarantines a suspect product, device or batch during an OUTBREAK investigation. This policy recalls processed items on a STERILISATION SYSTEM failure. Different triggers, same physical act. The HIC.5 checklist already recorded the boundary ("Instrument reprocessing, sterility assurance and recall -- HIC.6, not yet drafted. Step 32 quarantines a suspect device and does not address reprocessing"). This draft states the division in Scope, and step 31 accepts a surveillance-referred infection cluster as a trigger into this route while step 34 refers any resulting infection back to surveillance. Neither document restates the other's procedure.

DELIBERATELY NOT INCLUDED -- checked and judged to belong to other standards:
- Programme governance, the infection control committee and team, the annual programme, the infection control budget, and the stock register and expiry checking of sterilisation supplies and indicators -- HIC.1, approved. This policy specifies which indicators are required; HIC.1 procures and stocks them.
- Standard and transmission-based precautions, PPE selection and doffing, aseptic technique, safe injection practice, the sterile field, surgical hand preparation, and the prion handling precautions -- HIC.2, approved. Step 23 refers to the precautions and does not restate them.
- Environmental cleaning agents and their concentrations, water systems, laundry, kitchen, biomedical waste, and the hospital's clean/dirty building flows -- HIC.3, approved. Step 15 governs device disinfectants only, and says so; HIC.3 already points here for those.
- Care bundles, device insertion and maintenance practice, the operating room disciplines, and the confirmation of sterility at the point of use as a clinical requirement -- HIC.4, approved. Step 19 supplies the method and record for that confirmation.
- Surveillance case definitions, infection rates, outbreak investigation and the outbreak quarantine route -- HIC.5, approved.
- Occupational health, staff immunisation, sharps injury and exposure management for staff injured during reprocessing -- HIC.4 and the occupational health policy. Steps 7 and 15 point there and do not restate.
- The five optional sections (definitions, training_competency, resources_required, monitoring_audit, exceptions) are deliberately left unset, matching HIC.1-5. NOTE: this means the substantial training and competency content implied by steps 5, 21 and 40 lives inside the procedure and the evidence columns rather than in a training_competency section. Consistent with the rest of the set; flagged so the reviewer knows it was a choice.

DISCLAIMER BLOCK -- VERBATIM FROM HIC.5, AND WHAT THAT MEANS
The disclaimer is the approved HIC.5 block reproduced word for word. It is asserted against the live HIC.5 row by md5 at build time, so it cannot drift unnoticed. The comparison strips CR before hashing, since the stored rows use CRLF paragraph breaks and this file uses LF throughout per the newline="\\n" rule in build_hic1.py. The same value is live on HIC.3 and HIC.4; HIC.6 makes four.
The two consequences recorded against HIC.4 and HIC.5 apply here and are, for this standard, mixed:
- Paragraph 2 cites the Bio-Medical Waste Management Rules, 2016 and the Food Safety and Standards Act, 2006. The waste rules ARE relevant here for the first time since HIC.3 -- single-use items, withdrawn devices and processing waste are disposed of under them, and they appear in this document's own reference list. The Food Safety and Standards Act is not relevant to HIC.6 at all.
- Paragraph 4 names the FSSAI and Pollution Control Boards, which this document does not cite, and does not name the CDC, ISO, AAMI or CDSCO, which it does.
If the boilerplate is ever revised, both points should be picked up in a pass across all of HIC.1 to HIC.6 rather than in this file alone. HIC.1 (three paragraphs) and HIC.2 (five, different opening) remain unaligned with the HIC.3/HIC.4/HIC.5/HIC.6 block; aligning them is a separate decision and has not been made here. WITH HIC.6 DRAFTED, ALL SIX HIC STANDARDS NOW EXIST, so that pass is now possible for the first time.

AUTHOR BYLINE -- NOT IMPLEMENTED, AND WHY
Unchanged from HIC.5. shco_policy_masters still has no byline, author or prepared_by column; policy-doc-template.ts still has no byline parameter and still hardcodes "Prepared By" as a blank signature line; and no master policy carries the byline in any field. Verified again on 2026-08-10: the renderer file is unchanged since 2026-08-06 and no migration has run. Storing it in an unrendered field would repeat the dormant-column error already logged against `version`. The work remains merged into the version/revision-history infrastructure TODO in scripts/master-policy-todos.md, with its six build steps. NOT silently skipped.

STATE OF THE HIC SET AS AT THIS DRAFT
With HIC.6 drafted, all six HIC standards exist. The reconciliation pass recorded in scripts/master-policy-todos.md -- which was explicitly gated on "not before all 6 HIC standards are drafted" -- is now unblocked. Its open items are: the HIC.2/HIC.4 PEP and antiseptic-wording divergences; the HIC.5 versus HIC.2 hand hygiene session length; the HIC.3 environmental surface swab contradiction with HIC.5 step 28; reducing HIC.1 step 26 to a pointer at HIC.5; the HIC.3 placeholder count correction from 38 to 40 and the HIC.1 check at 25; and the HIC.2.c asterisk, which is asterisked in the PDF but deliberately left false in shco_full_oes because flipping it requires a documented-evidence anchor HIC.2 does not currently contain. NOTHING IN THIS DRAFT ADDS TO THAT LIST.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 46 fillable blanks in the rendered document: 12 in the exact form "[Hospital to define]" and 34 in the guidance-bearing form "[Hospital to define - what to state]". A search for the exact string finds 12 of 46; a search for "Hospital to define" without brackets finds all 46, and that is the search a hospital should be told to run. The figure rose from 40 to 46 on 2026-08-10 when the endoscope subsection was added to step 15; the six new entries are the endoscopy applicability declaration, the borescope inspection frequency, the drying equipment and time, the endoscope storage interval, the endoscope rinse water specification, and the endoscope reprocessing certification scheme and reassessment interval. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, and was used from the first build of this file. The build also asserts that no nested placeholder exists.

The values the hospital must supply: the title and reporting line of the person in charge of processing; the marked layout drawing of the processing area; air change rates and pressure differentials per zone with the standard relied on; temperature and humidity ranges for the clean and storage zones; the water treatment for final rinse and steam generation, its specification and testing frequency; every location processing items outside the central area, with its items, method, operator, monitoring and records; the maximum delay before an item requires extended cleaning; the detergent, dilution, temperature and contact time for manual cleaning; the cleaning verification method, items, frequency and acceptance criterion; the packaging systems per method with pack size and mass limits; the list of sterilisers with identifier, method, cycles and location; whether immediate-use steam sterilisation is permitted at all and under what limits; the moist heat cycle parameters per cycle type; each low-temperature method with its parameters, permitted items and packaging; each high-level disinfectant with its devices, concentration, temperature and contact time; whether flexible or semi-rigid endoscopy is performed at all, and if not the signed declaration with its reason, referral arrangement and review date; the borescope inspection frequency per endoscope and who performs it; the endoscope drying equipment, drying time and storage arrangement, and the storage interval where the drying cabinet does not supply a validated one; the endoscope rinse water specification, treatment, testing frequency and action limits; the endoscope reprocessing certification accepted, the competency reassessment interval and who assesses; whether a clean-status labelling system is used for shared equipment; the responsible role and frequency for each category of shared non-critical equipment; the cooling period; the shelf life system and, if time-related, the period per packaging system; the storage check frequency; the tracking system or manual record and where it is held; the retention period for processing records and for implant traceability; the single-use device categories approved for reprocessing, if any, or the record that none is; the position on separate patient consent for a reprocessed single-use device; the monitoring schedule per machine and cycle; the calibration frequency and provider; the chemical indicator class used at each point; the biological indicator per process with its incubation conditions; the air removal and leak test, frequency and acceptance criteria; the external qualification provider and requalification interval; the Infection Control Officer and deputy with 24-hour contact details; the period within which the recall report is produced; the mock recall interval; the outsourced processing provider and contract review date; the minimum lead time for a loaner set; the record retention period per class; the policy review interval; the intranet or folder location; and any additional local abbreviation."""

draft = {
    "standard_code": STANDARD_CODE,
    "chapter": CHAPTER,
    "oe_codes": OE_CODES,
    "policy_title": POLICY_TITLE,
    "purpose": PURPOSE,
    "scope": SCOPE,
    "policy_statement": POLICY_STATEMENT,
    "procedure_steps": PROCEDURE_STEPS,
    "responsibility": RESPONSIBILITY,
    "references_text": REFERENCES,
    "distribution": DISTRIBUTION,
    "abbreviations": ABBREVIATIONS,
    "disclaimer": DISCLAIMER,
    "oe_mapping": OE_MAPPING,
    "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
    "status": "draft",
}

# The five optional sections (definitions, training_competency, resources_required,
# monitoring_audit, exceptions) are intentionally absent -- they stay NULL so the
# renderer does not emit those headings, matching HIC.1-5.

# newline="\n" is REQUIRED -- see build_hic1.py. Windows CRLF inside the policy text
# breaks the renderer's step regex and silently flattens every step.
with open(DRAFTS / "hic6_draft.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(draft, f, ensure_ascii=False, indent=2)


def dollar(s, tag="q"):
    assert f"${tag}$" not in s, f"delimiter collision in: {s[:60]}"
    return f"${tag}${s}${tag}$"


def pg_array(items):
    return "array[" + ", ".join("'" + i.replace("'", "''") + "'" for i in items) + "]"


def steps_array(steps):
    return "array[\n    " + ",\n    ".join(dollar(s, "s") for s in steps) + "\n  ]"


sql = f"""-- HIC.6 master policy -- DRAFT for review. Do NOT set status = 'approved' here;
-- approval is a separate manual step after fact-checking.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 5, printed page 96.
-- Levels: a Commitment, b Core, c Commitment, d Commitment, e Commitment.
-- FOUR OF FIVE OEs CARRY THE ASTERISK -- b, c, d and e. No single evidence anchor;
-- depth is built into four separate blocks.
--
-- The five optional sections are deliberately not populated, matching HIC.1-5.

insert into public.shco_policy_masters (
  standard_code,
  chapter,
  oe_codes,
  policy_title,
  purpose,
  scope,
  policy_statement,
  procedure_steps,
  responsibility,
  references_text,
  distribution,
  abbreviations,
  disclaimer,
  oe_mapping,
  universal_facts_checklist,
  status
) values (
  '{STANDARD_CODE}',
  '{CHAPTER}',
  {pg_array(OE_CODES)},
  {dollar(POLICY_TITLE)},
  {dollar(PURPOSE)},
  {dollar(SCOPE)},
  {dollar(POLICY_STATEMENT)},
  {steps_array(PROCEDURE_STEPS)},
  {dollar(RESPONSIBILITY)},
  {dollar(REFERENCES)},
  {dollar(DISTRIBUTION)},
  {dollar(ABBREVIATIONS)},
  {dollar(DISCLAIMER)},
  {dollar(json.dumps(OE_MAPPING, ensure_ascii=False))}::jsonb,
  {dollar(UNIVERSAL_FACTS_CHECKLIST)},
  'draft'
);
"""

with open(SQL_OUT / "hic6_insert.sql", "w", encoding="utf-8", newline="\n") as f:
    f.write(sql)


# ---------------------------------------------------------------- verification

print("steps:", len(PROCEDURE_STEPS))

# Every step must open with its own number, in order -- the renderer keys off this.
bad = []
for i, s in enumerate(PROCEDURE_STEPS, start=1):
    m = re.match(r"^(\d+)\.\s", s)
    if not m or int(m.group(1)) != i:
        bad.append((i, s[:50]))
print("step numbering contiguous from 1:", not bad, bad or "")

# No stray CR anywhere -- CRLF flattens every step in the renderer.
print("no CR in any field:", not any(
    "\r" in v for v in [PURPOSE, SCOPE, POLICY_STATEMENT, RESPONSIBILITY, REFERENCES,
                        DISTRIBUTION, ABBREVIATIONS, DISCLAIMER, UNIVERSAL_FACTS_CHECKLIST]
    + PROCEDURE_STEPS))

print("mapping covers all 5 OEs:", sorted(m["oe_code"] for m in OE_MAPPING) == sorted(OE_CODES))
print("every mapping row has evidence + responsible:",
      all(m.get("evidence") and m.get("responsible") for m in OE_MAPPING))

# Each mapped step range must point at steps that exist.
referenced = set()
for m in OE_MAPPING:
    for a, b in re.findall(r"(\d+)-(\d+)", m["steps"]):
        referenced.update(range(int(a), int(b) + 1))
    for n in re.findall(r"(?<![\d-])(\d+)(?![\d-])", m["steps"]):
        referenced.add(int(n))
print("mapped step numbers all exist:", max(referenced) <= len(PROCEDURE_STEPS))
print("steps not mapped to any OE:", sorted(set(range(1, len(PROCEDURE_STEPS) + 1)) - referenced))

# The optional five must not have leaked into the payload.
optional = ["definitions", "training_competency", "resources_required", "monitoring_audit", "exceptions"]
print("optional sections left unset:", not any(k in draft for k in optional))

print("status is draft:", draft["status"] == "draft")

# The disclaimer must stay byte-identical to the approved HIC.5 block, ignoring line endings.
import hashlib
_d = hashlib.md5(DISCLAIMER.replace("\r", "").encode("utf-8")).hexdigest()
assert _d == HIC5_DISCLAIMER_MD5_LF, f"disclaimer drifted from HIC.5: {_d}"
print("disclaimer verbatim identical to HIC.5 (LF-normalised md5):", _d)

# The four forward promises made by the approved HIC.3 and HIC.4 documents must be met.
_all = " ".join([PURPOSE, SCOPE, POLICY_STATEMENT, RESPONSIBILITY, DISTRIBUTION,
                 ABBREVIATIONS] + PROCEDURE_STEPS + [json.dumps(OE_MAPPING)])
_promises = {
    "Spaulding classification (HIC.3 scope, HIC.3 step 15)": "semi-critical",
    "sterile storage (HIC.3 scope)": "shelf life",
    "sterilisation indicators (HIC.3 scope)": "biological indicator",
    "choice of high-level disinfectant (HIC.3 step 15)": "high-level disinfectant",
    "ventilator accessory reprocessing (HIC.4 step 10)": "heat and moisture exchangers",
    "point-of-use sterility check (HIC.4 step 20)": "pack integrity",
}
_missing = [k for k, v in _promises.items() if v not in _all]
assert not _missing, f"forward promise from an approved policy not honoured: {_missing}"
print("all forward promises from HIC.3/HIC.4 honoured:", len(_promises))

# The ST91 endoscope subsection carries six requirements that were added on
# instruction. Assert each survives future edits rather than silently regressing.
_endoscope = {
    "leak testing before cleaning": "leak tested after every patient use",
    "mandatory cleaning verification": "on every reprocessing cycle",
    "borescope inspection": "borescope",
    "active drying with defined equipment": "forced-air drying system",
    "endoscope water quality (ST108)": "endoscope rinse water specification",
    "personnel certification within two years": "within two years of starting in the role",
    "not-applicable declaration": "endoscopy is not performed",
}
_ep_missing = [k for k, v in _endoscope.items() if v not in _all]
assert not _ep_missing, f"endoscope requirement missing from step 15: {_ep_missing}"
# Scope guard: the subsection must keep excluding the other semi-critical items.
assert "and to no other device" in _all, "endoscope subsection lost its scope limitation"
print("endoscope (ST91) requirements present:", len(_endoscope), "+ scope guard")

from policy_placeholder_audit import audit
_exact, _variant, _total, _problems = audit(draft)
assert not _problems, _problems
print("wrote hic6_draft.json and hic6_insert.sql")
