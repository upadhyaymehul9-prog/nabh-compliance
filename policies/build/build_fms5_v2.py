# -*- coding: utf-8 -*-
"""Template-test rebuild of FMS.5 as an adoptable hospital policy.

Does NOT overwrite policies/drafts/fms5_draft.json or build_fms5.py.
Writes policies/drafts/fms5_v2_draft.json only. No SQL. No Supabase insert.

This file is a FORMAT EXPERIMENT. It is not the pipeline master. It does not
use emit_and_verify (that helper requires OE-skeleton numbering, unset optional
sections, and [Hospital to define] inventory). Disclaimer P1/P3/P4 remain the
shared block; paragraph 2 still names NBC 2016 as locally applied.

Editable defaults are marked «like this». True blanks (no sensible default)
are marked «________».
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from policy_build_common import (
    DISCLAIMER_P1_MD5,
    DISCLAIMER_P3_MD5,
    DISCLAIMER_P4_MD5,
    HIC_BOILERPLATE_STATUTES,
    POLICIES,
    make_disclaimer,
)

STANDARD_CODE = "FMS.5"
CHAPTER = "FMS"
OE_CODES = ["FMS.5.a", "FMS.5.b", "FMS.5.c", "FMS.5.d", "FMS.5.e"]

POLICY_TITLE = "Fire and Non-Fire Emergencies"

VERSION = "2.1"
REVISION_HISTORY = [
    {
        "version": "2.0",
        "date": "18-08-2026",
        "description": "Template-test rebuild: adoptable hospital policy shape. Not an approved master.",
    },
    {
        "version": "2.1",
        "date": "18-08-2026",
        "description": "Renumber: 5.1–5.8 under What we do; stop-work as section 6. Disclaimer unchanged.",
    },
]

# Marks a default a small hospital can adopt; change the words inside the marks.
D = lambda s: f"«{s}»"
BLANK = "«________»"
# Regular string, not an f-string: two braces on each side. Insert as {HOSPITAL}
# inside f-strings so the draft still carries {{HOSPITAL_NAME}}.
HOSPITAL = "{{HOSPITAL_NAME}}"

PURPOSE = f"""This policy governs how {HOSPITAL} prevents, detects, contains and recovers from fire and from named non-fire emergencies inside its facilities, so that patients, families, staff and visitors can get out — or shelter — alive, and so that essential clinical services continue or pause under a named decision.

It sets the standards the hospital requires of every person on the premises. It is not a step-by-step drill script, a vendor maintenance manual, or a substitute for the fire NOC issued to this building. Floor-level actions (who takes which corridor, which extinguisher is used on which class of fire) are trained against this policy and recorded in the drill file.

Editable defaults in this document are marked {D('like this')}. A hospital that adopts the default keeps the wording. A hospital that needs a different owner, interval or arrangement replaces the marked text before issue. True blanks — {BLANK} — have no sensible default and must be completed before this document is signed."""

SAFETY_OBJECTIVE = """People leave a fire. Equipment is replaced. A blocked exit, a wedged fire door, or a silenced detector is never a convenience."""

SCOPE = f"""This policy applies to every occupied space of {HOSPITAL} and to every person on the premises: employees, visiting consultants, contract staff, students, vendors and visitors.

It covers fire, and the following named non-fire emergencies:

- earthquake;
- flood or water ingress, if this building has a basement, a history of ingress, or a roof tank whose failure would flood a clinical floor — otherwise the Medical Superintendent records flood as not applicable;
- bomb threat or a suspicious object;
- civil unrest or violence that closes a unit;
- lift entrapment, if this hospital has a lift — otherwise recorded as not applicable;
- medical-gas leak, manifold-room fire, or oxygen-enriched fire;
- major electrical failure after the hospital's electrical backup has failed or cannot carry essential circuits;
- any other event the Medical Superintendent adds in writing to the named list.

A photocopied chemical / biological / radiological / nuclear annex is not in force unless the Medical Superintendent has added that event to the named list because this occupancy actually faces it.

This policy does not govern routine testing of electrical and water backup (that is the utilities programme), biomedical preventive maintenance of clinical devices (that is the equipment programme), medical-gas procurement and cylinder handling (that is the medical-gases programme), laboratory chemical hygiene at the bench, or the incident-reporting form. Those programmes remain in force. A finding from a monthly facility round that a fire door is wedged or an extinguisher is missing is closed under this policy. A gas leak is handled as a named non-fire emergency here; how cylinders are stored remains the medical-gases programme.

Laboratory fire is handled under this hospital fire plan. Radiation and PC-PNDT notices are not the fire-exit display. Wayfinding signs are not the exit plan."""

POLICY_STATEMENT = f"""{HOSPITAL} will not occupy a clinical floor whose exits, detection, first-attack equipment or fire doors are known to be failed, unless a compensating provision is already in place and the Medical Superintendent has accepted the residual risk in writing until restoration.

Every occupied floor has a displayed exit plan that matches the as-built drawings, names the assembly point, and can be read by a first-time family and by the night nurse. The assembly point is {BLANK}.

Fire is detected by the provisions the local fire authority required for this occupancy under the National Building Code of India, 2016 — smoke or heat detectors, manual call points, and a panel that is audible at the Nursing Station and at the Security desk on every occupied shift. An alarm at 03:00 is treated as a fire until the Night Duty Officer has verified it is not.

First attack uses the portable extinguishers on that floor, maintained to IS 2190 practice. Hose reels, hydrants, pumps or sprinklers are used only if this occupancy's fire NOC required them and staff on duty have been trained to operate them. This hospital does not assume a sprinkler installation that the NOC did not require.

Containment means fire doors and shutters close and stay closed. A door closer that has been disconnected is a failed provision, not a summer ventilation arrangement.

Non-fire emergencies use the same command: the senior person on site (Medical Superintendent by day; Night Duty Officer by night) declares the event, decides evacuate or shelter-in-place, and decides whether named essential services continue, pause, move internally, or divert to the receiving hospital named below.

Dependent patients (neonates, restrained or non-ambulant adults, patients on oxygen or a ventilator) are moved with their oxygen and a named nurse; they are not left for a second wave that may not come. Clinical identification, matching of a neonate to a mother, and bedside observation of a vulnerable adult remain those care policies; this policy requires that the move actually happens.

Mock drills are held at least twice in every calendar year: one fire drill and one drill of a named non-fire event. Across any twelve-month period, at least one of those drills is run on a night or weekend shift. Every drill includes a dependent-patient move. A tabletop in the quality office is not a drill.

Fire-related equipment and infrastructure are maintained on the schedule in this policy. A fire NOC in a drawer, an annual-maintenance contract with no job card, or a commissioning certificate from the year the pipe was laid, is not maintenance.

If a ward, theatre or plant is lost, essential services continue, pause or divert under the continuity decisions in this policy. Diversion, if used, is to {BLANK} (a named hospital — not "a nearby hospital"). The person who telephones that hospital is the Medical Superintendent or the Night Duty Officer.

Staff do not operate fire pumps, zone isolation, medical-gas isolation, or the fire panel unless they have been trained and named for that task."""

NON_NEGOTIABLES = f"""The following are prohibited. There is no operational exception, no festival exception, and no "until the vendor comes" exception. Stop-work applies.

1. Blocking an exit, an exit corridor, a stair, or an assembly route with beds, stores, trolleys, construction material or a parked vehicle.
2. Wedging, tying, or latching open a fire door or fire shutter, or disconnecting its closer.
3. Covering, painting, silencing, isolating or removing a detector, sounder or manual call point except under a written isolation permit issued by the Maintenance In-Charge for a dated job, with a compensating watcher and restoration recorded the same shift.
4. Leaving in place an extinguisher that is missing, discharged, unsealed, or past its maintenance date. A failed extinguisher is replaced or the location is given a compensating extinguisher the same shift.
5. Locking an emergency exit while the floor is occupied.
6. Using an exit arrow, locked grill, or board-room frame as the exit plan. The displayed plan must match the route a person can actually walk.
7. Treating the fire NOC, an AMC invoice, or a commissioning certificate as proof that a pump, panel, door closer or extinguisher works today.
8. Allowing untrained staff to start a fire pump, isolate a fire zone, isolate a medical-gas zone, or silence the fire panel.
9. Smoking, naked flame, or sparking tools in an oxygen-enriched area or a manifold room.
10. Skipping, photographing, or paper-signing a mock drill. A drill that did not leave the quality office, that excluded theatre or the night shift for convenience, or that omitted a dependent-patient move, has not been held.
11. Storing full and empty medical-gas cylinders mixed, or using a cylinder as a doorstop, in a way that blocks egress or feeds a fire. Cylinder handling remains the medical-gases programme; blocking egress is this policy.
12. Diverting patients to an unnamed hospital, or declaring continuity without naming who cannot be moved without oxygen from the medical-gas reserve.

Anyone who sees a prohibited act stops it under the stop-work clause and reports it the same shift to the {D('Maintenance In-Charge')} or, at night, the Night Duty Officer."""

PROCEDURE_STEPS = [
f"""5.1 Detection and raising the alarm

The fire provisions installed in this building are those the local fire authority required for this occupancy under the National Building Code of India, 2016, given this building's height and built-up area. They include, as that NOC required: {D('smoke and/or heat detectors covering occupied corridors, stores, kitchen and plant rooms')}; manual call points on each occupied floor at the {D('Nursing Station and stair landing')}; a fire alarm panel at the {D('Security desk')}, with repeater or sounder coverage of the {D('Nursing Station')} so that a night nurse hears it.

Fire NOC number: {BLANK}. Issuing authority: {BLANK}. A copy of the current NOC is held by the Maintenance In-Charge with the as-built fire drawings.

Any person who sees smoke, flame, a detector alarm, or a smell of burning raises the alarm: operate the nearest manual call point, shout "fire" with the location, and telephone the switchboard / Security. The alarm is not investigated in silence. The Night Duty Officer may silence sounders only after the floor has been seen and only with a watcher left on that floor.

A laboratory fire uses this same alarm path. Bench chemical hygiene remains the laboratory safety programme.

Medical-gas leaks, earthquake, bomb threat and the other named non-fire events are raised by the person who first knows of them to the Night Duty Officer or Medical Superintendent. There is no requirement to wait for a detector: an earthquake is felt; a bomb threat is a call; a leak is a smell, a hiss, or a manifold alarm.""",

f"""5.2 First attack and containment

Staff trained in extinguisher use may make a first attack on an incipient fire with the extinguisher for that class, if their own exit is clear behind them. If the fire is larger than a waste-bin, if smoke is already in the corridor, or if the person has not been trained, they close the door, leave, and do not return for belongings.

Portable extinguishers are provided on every occupied floor so that a person does not pass a fire to reach one. They are maintained to IS 2190 practice: monthly visual inspection (gauge in the green, pin and seal intact, accessible, correct type for the location) by the {D('Maintenance In-Charge')}, and {D('annual')} servicing by a competent person. A kitchen, manifold room, generator room and electrical panel have the class of extinguisher those hazards require.

Hose reels, hydrants, sprinklers and fire pumps — if the NOC required them — are operated only by staff named on the trained-operator list. This policy does not invent a sprinkler, hydrant or pump that the occupancy does not have. If a class of provision is not installed, the Maintenance In-Charge records it as not installed (not as "N/A because we are small").

Containment: fire doors and shutters on the as-built drawings close automatically or are closed by the Floor Fire Warden as they leave. Stair doors are not hooked open. A compartment that still has a working door closer is how a ward that is not in the fire continues to hold patients until the Medical Superintendent decides otherwise.

Electrical isolation of the affected zone is ordered by the Medical Superintendent or Night Duty Officer and carried out by the {D('Maintenance In-Charge')} or the trained night technician. Medical-gas isolation of a zone on fire is ordered the same way and carried out only by a person trained under the medical-gases programme. Untrained isolation of oxygen on a floor that still has ventilator-dependent patients is prohibited.""",

f"""5.3 Evacuation, assembly and dependent patients

The default for fire is evacuate the affected compartment, then the floor, then the building, as the Medical Superintendent or Night Duty Officer directs. The default for earthquake is shelter-in-place away from glass until shaking stops, then evacuate if the structure is unsafe. The default for bomb threat is evacuate away from the named location. The default for medical-gas leak is isolate, ventilate, remove ignition sources, and evacuate the affected zone. The senior person on site may change the default; they say so out loud and it is recorded after the event.

Each occupied floor has a Floor Fire Warden: by day, the {D('senior staff nurse on that floor')}; by night, the {D('senior nurse on duty for that floor')}. The warden sweeps toilets, stores and side rooms on the way out, reports "floor clear" or "patients remaining" to the Night Duty Officer, and does not re-enter.

The assembly point is {BLANK}. It is marked, reachable without crossing the usual fire-appliance stand, and named on every displayed exit plan. Security (or, if Security is not on site, the Night Duty Officer) accounts for staff against the duty roster and for patients against the ward census. Visitors are directed to the assembly point and not back into the building.

Dependent patients move with a named nurse and with portable oxygen from the medical-gas reserve. Neonates move in their transport cot or in arms, matched to the mother or designated guardian under the neonatal care policy. A patient who cannot be moved without piped oxygen is the Medical Superintendent's named exception for that event and is sheltered with a nurse and a working portable supply — not left unattended because "the lift is for firemen."

Lifts are not used for fire evacuation unless the fire authority's occupancy conditions for this building say otherwise in writing. If this hospital has no lift, that sentence does not apply.""",

f"""5.4 Named non-fire emergencies

Earthquake. Staff protect patients from falling fixtures, shut off non-essential flame, and wait for shaking to stop before moving. Aftershock is expected. The Maintenance In-Charge inspects stairs, medical-gas manifold, diesel store and electrical panels before anyone is sent back in. National Disaster Management Authority Hospital Safety Guidelines (2016) are the framework for this decision; they are not pasted as a district booklet.

Flood or water ingress. Electricity to the wet zone is isolated before anyone wades. Patients are moved upward or out. A basement that this building does not have is recorded as not applicable.

Bomb threat or suspicious object. The person who takes the call writes the words used, the time, and any location named. The Medical Superintendent or Night Duty Officer evacuates away from that location and informs the police. Staff do not touch, open or carry the object.

Civil unrest or violence that closes a unit. External doors are controlled by Security. Essential in-patients stay; out-patient services pause. Transfer out is the Medical Superintendent's decision.

Lift entrapment (if a lift exists). Power is left on unless there is also a fire. Rescue is by the lift-maintenance contractor or the fire service; staff do not force the car doors. A hospital with no lift records this event as not applicable.

Medical-gas leak or oxygen-enriched fire. Ignition sources are removed. Zone isolation follows the medical-gases programme. Evacuation of the affected zone follows this policy. A leaking cylinder is not rolled through an exit route.

Major electrical failure after backup has failed. Continuity decisions in section 5.8 apply. This is not the routine generator test.

Violence, bomb threat and civil unrest that become a reportable incident are also entered in the incident system. This policy is the emergency action; the incident form is not a substitute for clearing the floor.""",

f"""5.5 Exit plan — documented and displayed

Every occupied floor displays, at the {D('Nursing Station and at each stair door')}, a floor plan that shows: the route a person on that floor actually walks to the stair or final exit; the location of extinguishers and manual call points; the assembly point; and "you are here." The plan is in {D('Gujarati and English')}. It matches the controlled as-built drawings. A framed plan in the board room, an arrow pointing at a locked grilled window, or a radiation / PC-PNDT notice is not this display.

When a fire door, a ward, or a stair is taken out of use, the Maintenance In-Charge updates the display the same day and dates the drawing. A faded, contradictory or obsolete display is a failed provision.

Staff on induction walk the route from their workplace to the assembly point once before they work a night shift.""",

f"""5.6 Maintenance of fire-related equipment and infrastructure

The Maintenance In-Charge owns the maintenance plan for every fire provision this occupancy actually has. Biomedical preventive maintenance of ventilators, monitors and sterilisers is not this plan.

Schedule (adopt as written; replace a marked interval only with a tighter one):

- Portable extinguishers — monthly visual inspection to IS 2190 practice; {D('annual')} servicing by a competent person. A failed unit is replaced or compensated the same shift.
- Fire alarm panel, detectors, sounders, manual call points — {D('quarterly')} functional test (a detector or call point on each floor is activated and the panel and sounders are confirmed); {D('annual')} service under AMC or by a competent person. A failed zone is isolated only under the written permit in the non-negotiable rules, with a watcher.
- Emergency lighting — {D('monthly')} functional test; {D('annual')} duration test.
- Fire doors and shutters, including closers and seals — monthly, on the facility inspection round, and repaired under this plan. A disconnected closer is restored within {D('24 hours')} or the door is put on a watcher.
- Hose reels / hydrants / sprinklers / fire pumps — only if installed: {D('weekly')} pump auto-start if a pump exists; {D('quarterly')} water-flow or valve inspection as the AMC specifies; {D('annual')} service. A pump that has never been started on test is a failed provision. A yearly vendor visit with no job card is not this schedule.
- Fire drawings and displayed exit plans — checked monthly against the floor.

The fire NOC is not a job card. The last inspection of each class is retrievable. A failed detector zone, discharged extinguisher, or fire pump that will not start is withdrawn from reliance and a compensating provision is put in place until restored.""",

f"""5.7 Mock drills

Mock drills are held at least twice a year. That floor is not optional.

In each calendar year {HOSPITAL} holds:

- one fire drill that starts with an alarm (not with a memo), on an occupied floor, and proceeds to assembly, including a dependent-patient move; and
- one drill of a named non-fire event (earthquake, bomb threat, gas leak, or electrical failure after backup — the Medical Superintendent chooses which, and rotates so that the same event is not the only one ever practised).

Across any twelve-month period, at least one of the two is run on a night or weekend shift. Theatre and labour, if running, take part or receive a dated written deferral from the Medical Superintendent with a replacement date inside thirty days that still meets the twice-a-year floor.

The {D('Quality Coordinator')} observes against a written objective list: alarm heard at the Nursing Station; wardens sweep; dependent patient moved with oxygen; assembly accounted; fire doors closed. A failed objective is recorded, a corrective action is assigned, and that objective is re-drilled within {D('thirty days')}.

A drill that harms someone is also an incident. Staff training records for fire and non-fire emergencies are held with the personnel file; this policy is what they are trained to.""",

f"""5.8 Service continuity

When a ward, theatre, labour room, laboratory, imaging room or plant is lost to fire or to a named non-fire event, the Medical Superintendent (day) or Night Duty Officer (night) declares one of: continue in place with restrictions; pause; move internally; or divert.

Essential services that this hospital actually runs — emergency receiving, labour if obstetric services are offered, oxygen-dependent in-patients, and any other service the Medical Superintendent has listed as essential — are not left without a named decision. A service the hospital does not offer is not given a continuity annex.

Continue in place uses electrical backup and medical-gas reserve as those programmes provide. This policy does not rewrite those tests; it uses them in the hour they were tested for.

Pause means no new elective work; in-patients already present are kept safe.

Move internally uses an uninvolved ward or hall that still has exits, power and oxygen.

Divert, if declared, is to {BLANK}. The Medical Superintendent or Night Duty Officer places the call, sends the census of who is moving, and sends oxygen-dependent patients with portable supply and a nurse. An unnamed "nearby hospital" is not a receiving arrangement.

Who cannot be moved without piped oxygen is listed on the continuity card held at the {D('Nursing Station')} and updated when a ventilator-dependent patient is admitted or discharged.""",

]

STOP_WORK = f"""Every person on the premises has the authority and the duty to stop an act that breaches a non-negotiable rule of this policy: a blocked exit, a wedged fire door, a silenced detector, an untrained person at the fire panel, a sparking tool in an oxygen area, a drill being paper-signed.

The person says "stop" to the act, makes the immediate safe condition (remove the wedge, unblock the door, restore the pin on the call point if they are competent to, or keep people away if they are not), and reports the same shift to the {D('Maintenance In-Charge')} or the Night Duty Officer.

There is no retaliation for a good-faith stop-work. A stop-work that was wrong in hindsight is still recorded; the act is not restarted until the Maintenance In-Charge says so.

A vendor or visiting consultant who refuses to stop is required to leave the area. The Medical Superintendent is informed the same shift."""


RESPONSIBILITY = f"""Roles below are titles, not vacancies. If one person holds two titles in a small hospital, both duties still apply.

Medical Superintendent (Head of the Institution)
- Accountable that this policy is issued, resourced and followed.
- Declares evacuate, shelter, continuity or divert by day.
- Accepts in writing any residual risk while a failed fire provision has a compensating arrangement.
- Names the receiving hospital before this policy is issued.
- Chooses and rotates the annual non-fire drill event.

Maintenance In-Charge (Fire Safety Officer for this policy)
- Owns detection, first-attack equipment, fire doors, emergency lighting, pumps if installed, drawings and displayed exit plans.
- Holds the fire NOC and the as-built fire drawings.
- Runs the maintenance schedule in section 5.6 and closes fire findings from monthly facility rounds.
- Issues and closes isolation permits for detectors and zones.
- Trains and names staff who may operate pumps, panels and zone isolation.

Nursing Superintendent
- Names Floor Fire Wardens for each occupied floor and for the night roster.
- Owns the dependent-patient move and the continuity card at the Nursing Station.
- Ensures displayed exit plans are not covered by notices.

Night Duty Officer (senior doctor or senior nurse on night duty, as rostered)
- Holds the Medical Superintendent's emergency authority between {D('20:00 and 08:00')}.
- Receives the alarm, declares the event, and orders evacuate or shelter.
- Does not silence the panel without a watcher on the floor.

Floor Fire Warden (senior staff nurse of that floor / senior nurse on night duty for that floor)
- Sweeps the floor, closes fire doors on the way out, reports floor clear or patients remaining.

Security Supervisor (or the person covering the Security desk)
- Hears the panel, calls the fire service on a confirmed or un-ruled-out fire: {D('101 / local fire-station number held at the desk')}.
- Controls the assembly-point count against the duty roster.
- Keeps vehicle access clear for fire appliances.

Quality Coordinator
- Observes drills, holds the drill file, tracks failed objectives to re-drill.
- Audits this policy {D('quarterly')} (see monitoring).
- Dual-enters a fire, a failed drill that caused harm, or a stop-work that became an incident, in the incident system.

Department in-charges (theatre, labour, laboratory, imaging, pharmacy, kitchen)
- Evacuate or shelter their unit on order; do not continue elective work through a fire alarm.
- Laboratory fire follows this plan.

All staff, vendors and visiting consultants
- Know the route from their workplace to the assembly point.
- Obey stop-work and the non-negotiable rules.
- Do not operate fire equipment they have not been trained to operate.

A RACI snapshot:

- Alarm raised: all staff (R); Night Duty Officer / Medical Superintendent (A)
- First attack: trained staff on that floor (R); Maintenance In-Charge (A for equipment)
- Evacuation sweep: Floor Fire Warden (R); Nursing Superintendent (A)
- Fire service called: Security Supervisor (R); Night Duty Officer (A)
- Isolation of power / gas: Maintenance In-Charge or trained night technician (R); Medical Superintendent / Night Duty Officer (A)
- Maintenance & NOC: Maintenance In-Charge (R/A)
- Drills: Quality Coordinator (R for observation); Medical Superintendent (A)
- Continuity / divert: Medical Superintendent or Night Duty Officer (R/A)
- Stop-work: all staff (R); Maintenance In-Charge (A for restart)"""

MONITORING_AUDIT = f"""The Quality Coordinator audits this policy {D('quarterly')}, and after every real activation or failed drill. The audit looks at the provisions and the records, not at a binder.

What is monitored each quarter:

- Extinguishers: monthly visual sheets for the quarter; any gauge in the red closed the same shift.
- Detectors and panel: last quarterly functional test; any isolated zone has a current permit and a watcher.
- Fire doors: monthly round findings closed; no door on a watcher older than {D('24 hours')} without Medical Superintendent sign-off.
- Exit displays: still match the drawings; assembly point still as issued.
- Drill calendar: two drills dated in the last twelve months, one fire and one named non-fire, one of them night or weekend; dependent-patient move recorded; failed objectives re-drilled inside thirty days.
- Continuity card: receiving hospital named; oxygen-dependent in-patients listed.
- Stop-work and incident dual-entry: every activation and every stop-work that met the incident definition is in the incident file.
- Fire NOC: still current.

Any non-conformity is a finding. The Maintenance In-Charge (equipment and fabric) or the Nursing Superintendent (wardens, displays, dependent-patient move) owns the corrective action. Root-cause analysis is required when: a drill objective fails twice; a real alarm is not heard at the Nursing Station; a fire door is found wedged on two successive rounds; an extinguisher is found discharged or missing; or a person operated a pump, panel or gas isolation without being on the trained list.

Corrective and preventive action is dated, has an owner, and is checked at the next quarterly audit. An open CAPA older than {D('thirty days')} is escalated to the Medical Superintendent.

This policy is reviewed {D('annually')}, and sooner after a real fire, a failed drill, a change to the fire NOC, a change of assembly point, or a change to the receiving hospital."""

TRAINING_ACKNOWLEDGEMENT = f"""Every staff member whose work is on an occupied floor is trained against this policy at induction, before a first night shift, and {D('once a year')} thereafter. Training covers: the alarm, the route to the assembly point, first-attack limits, dependent-patient move, stop-work, and the non-negotiable rules. Staff who may operate the fire panel, a pump, or medical-gas isolation are named on a trained-operator list held by the Maintenance In-Charge.

Vendors who work in plant rooms or on the fire system are briefed on stop-work and on the isolation-permit rule before they start.

Staff acknowledgement

I have read this Fire and Non-Fire Emergencies policy of {HOSPITAL}. I know the route from my workplace to the assembly point. I understand the non-negotiable rules and the stop-work duty. I will not operate fire pumps, the fire panel, or medical-gas isolation unless I am named on the trained-operator list.


Name: ___________________________    Designation: ___________________________

Department / floor: ____________________    Date: ____________

Signature: ___________________________


(One row per staff member. The Nursing Superintendent holds the signed acknowledgements with the induction record. A staff member who has not signed does not work a night shift on an occupied floor.)"""

DOCUMENT_CONTROL = f"""Document number: {D('FMS/POL/05')}
Issue number: {D('01')}
Version: 2.1 (template test — numbering fix; not an approved master)
Date created: {BLANK}
Date of implementation: {BLANK}
Review due: {D('one year from implementation')}
Number of pages: as printed

Prepared by (designation): {D('Maintenance In-Charge')}    Name: {BLANK}    Signature: {BLANK}
Reviewed by (designation): {D('Quality Coordinator')}    Name: {BLANK}    Signature: {BLANK}
Approved by (designation): {D('Medical Superintendent')}    Name: {BLANK}    Signature: {BLANK}

Fire NOC number: {BLANK}    Issuing authority: {BLANK}    Valid until: {BLANK}
Assembly point: {BLANK}
Receiving hospital for diversion: {BLANK}

Amendment sheet (add a line for each change after issue)

Sr | Section | Change | Reason | Prepared | Approved
1. |  |  |  |  | """

REFERENCES = """- National Building Code of India, 2016 (Bureau of Indian Standards), fire and life-safety provisions as the local fire authority has applied them to this occupancy.
- IS 2190 — selection, installation and maintenance of first-aid fire extinguishers (NBC-pointed practice for portable extinguishers).
- National Disaster Management Authority, National Disaster Management Guidelines — Hospital Safety (2016), framework for non-fire events and continuity of essential hospital functions.
- NABH Standards for Small Healthcare Organisations, 3rd Edition, Chapter 8 Facility Management and Safety, standard FMS.5 (this policy is written so that those requirements are met in operation; it is not a commentary on the standard).
- Internal: as-built fire drawings; utilities / electrical-backup programme; medical-gases programme; equipment programme; laboratory safety programme; incident system; monthly facility inspection rounds."""

DISTRIBUTION = f"""Controlled master: office of the Medical Superintendent, {HOSPITAL}, with a working copy held by the Maintenance In-Charge and the Quality Coordinator.

Issued to: Nursing Superintendent, Security Supervisor, every Floor Fire Warden, Night Duty Officer folder, theatre in-charge, laboratory in-charge.

Available to all staff at the {D('Nursing Station policy folder')} and, if the hospital keeps an intranet, at the {D('staff intranet / policies')}.

On revision, every displayed copy is withdrawn the same day. One dated superseded copy is retained by the Quality Coordinator."""

ABBREVIATIONS = """NBC — National Building Code of India, 2016
NDMA — National Disaster Management Authority
NOC — no-objection certificate issued by the local fire / building authority
AMC — annual maintenance contract
CAPA — corrective and preventive action
RCA — root-cause analysis
IS — Indian Standard

Floor Fire Warden — the senior nurse accountable for sweeping a named floor during an emergency
Night Duty Officer — the senior doctor or senior nurse holding emergency command overnight
Maintenance In-Charge — the person accountable for fire equipment and fabric under this policy (Fire Safety Officer)"""

STATUTE_CLAUSE = (
    "the National Building Code of India, 2016, insofar as the local fire and building "
    "authority has applied it to this facility for fire and life safety, occupancy and "
    "the provisions required by this hospital's fire NOC"
)
DISCLAIMER = make_disclaimer(STATUTE_CLAUSE)

# Traceability only — not the skeleton. "steps" is the where-addressed column.
OE_MAPPING = [
    {
        "oe_code": "FMS.5.a",
        "requirement": "The organisation has plans and provisions for early detection, abatement and containment of the fire, and non-fire emergencies.",
        "steps": "Safety objective; Section 3; 5.1 Detection and alarm; 5.2 First attack and containment; 5.4 Named non-fire emergencies; Section 4",
        "responsible": "Medical Superintendent (accountable); Maintenance In-Charge (provisions); Night Duty Officer (command at night)",
    },
    {
        "oe_code": "FMS.5.b",
        "requirement": "The organisation has a documented and displayed exit plan in case of fire and non-fire emergencies",
        "steps": "Section 3; 5.3 Evacuation, assembly and dependent patients; 5.5 Exit plan — documented and displayed",
        "responsible": "Maintenance In-Charge (drawings and display); Nursing Superintendent (notices not covering the plan)",
    },
    {
        "oe_code": "FMS.5.c",
        "requirement": "Mock drills are held at least twice a year.",
        "steps": "Section 3; 5.7 Mock drills; Section 8 Quality monitoring; Section 4 item 10",
        "responsible": "Medical Superintendent (accountable); Quality Coordinator (observe and file)",
    },
    {
        "oe_code": "FMS.5.d",
        "requirement": "There is a maintenance plan for fire-related equipment and infrastructure.",
        "steps": "5.2 First attack; 5.6 Maintenance of fire equipment and infrastructure; Section 8 Quality monitoring; Section 4 items 3, 4, 7",
        "responsible": "Maintenance In-Charge",
    },
    {
        "oe_code": "FMS.5.e",
        "requirement": "The organisation has a service continuity plan in case of fire and non-fire emergencies.",
        "steps": "Section 3; 5.8 Service continuity; Section 7 Governance",
        "responsible": "Medical Superintendent / Night Duty Officer",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """FORMAT EXPERIMENT (2026-08-18). This is FMS.5 v2, not the pipeline master.

Intent: an adoptable SHCO policy organised around what staff do in a fire or named
non-fire emergency. OE letters are a traceability table at the end, not headings.
Defaults are marked « ». True blanks are «________» (assembly point, fire NOC,
receiving hospital, signature names, implementation dates).

Numbering (v2.1): one sequence. 1 Purpose, 2 Scope, 3 Policy standards,
4 Non-negotiable rules (internal 1–12 list is prohibitions, not document
sections), 5 What we do with subsections 5.1–5.8, 6 Stop-work authority
(promoted: standing duty, not a fire-response step), 7 Governance,
8 Quality monitoring, 9 Training, 10 References, 11 Distribution,
12 Abbreviations, 13 Traceability. Shape is mandatory; word count is not.
Administrative standards keep this order with fewer 4.x rules and fewer
5.x subsections — length follows the subject.

Disclaimer P1/P3/P4 are the shared block. P2 names NBC 2016 as locally applied.
BMW/FSS/CPA/CEA 2010/MHCA are not in P2. P1 is unchanged in this rebuild.

Technical substance retained from v1: NBC 2016 as-applied (no invented sprinkler
mandate); IS 2190 monthly visual + periodic service; NDMA Hospital Safety 2016
for non-fire and continuity; loaded/functioning tests not paper changeovers;
dependent-patient move; night/weekend drill sample; fire NOC is not a job card;
lab fire uses this plan; gas leak is an emergency here and handling stays the
gas programme; COP matching/observation stay care policies.

Not used: [Hospital to define] in the body (disclaimer P1 still contains that
phrase because the shared block is unchanged). Assessor-facing "this OE" /
"an assessor will ask" / "common error" framing. SQL insert. Status remains draft.

OE coverage: a detection/abatement/containment + non-fire; b exit display;
c drills twice a year; d maintenance schedule; e continuity with a named hospital.
"""


def _verify_disclaimer(disclaimer: str, statute_clause: str) -> None:
    parts = disclaimer.split("\n\n")
    assert len(parts) == 4, f"disclaimer is not four paragraphs: {len(parts)}"
    assert hashlib.md5(parts[0].encode("utf-8")).hexdigest() == DISCLAIMER_P1_MD5
    assert hashlib.md5(parts[2].encode("utf-8")).hexdigest() == DISCLAIMER_P3_MD5
    assert hashlib.md5(parts[3].encode("utf-8")).hexdigest() == DISCLAIMER_P4_MD5
    assert statute_clause in parts[1]
    for banned in HIC_BOILERPLATE_STATUTES:
        assert banned not in parts[1]
    print("disclaimer P1/P3/P4 shared; P2 NBC 2016 statute-matched:", True)


def _verify_no_oe_headings(steps: list[str]) -> None:
    for s in steps:
        title = s.split("\n", 1)[0]
        assert not re.search(r"FMS\.5\.[a-e]\b", title), f"OE code in a section title: {title}"
    print("operational section titles are not OE codes:", True)


def _verify_mapping() -> None:
    assert [m["oe_code"] for m in OE_MAPPING] == OE_CODES
    for m in OE_MAPPING:
        assert m.get("steps") and m.get("responsible")
        assert "evidence" not in m, "v2 mapping is traceability only; no assessor evidence column"
    print("OE mapping is a traceability table covering all 5 OEs:", True)


def _verify_placeholders(draft: dict) -> None:
    blob = json.dumps(draft, ensure_ascii=False)
    # Body must not use the old deferral marker except the shared disclaimer P1.
    body = " ".join(
        [
            draft["purpose"],
            draft["scope"],
            draft["policy_statement"],
            draft["responsibility"],
            draft["references_text"],
            draft["distribution"],
            draft["abbreviations"],
            draft.get("definitions") or "",
            draft.get("training_competency") or "",
            draft.get("monitoring_audit") or "",
            draft.get("exceptions") or "",
            draft.get("resources_required") or "",
            draft.get("stop_work") or "",
        ]
        + draft["procedure_steps"]
        + [json.dumps(draft["oe_mapping"], ensure_ascii=False)]
    )
    assert "[Hospital to define" not in body, "v2 body still defers with [Hospital to define]"
    assert "«________»" in body, "true blanks missing"
    assert "«Maintenance In-Charge»" in body, "role default missing"
    assert "{{HOSPITAL_NAME}}" in body
    assert not re.search(r"(?<!\{)\{HOSPITAL_NAME\}(?!\})", body)
    print("defaults marked « »; true blanks present; no body [Hospital to define]:", True)
    print("disclaimer still contains shared [Hospital to define] in P1:", "[Hospital to define]" in draft["disclaimer"])
    _ = blob


def build_markdown(draft: dict) -> str:
    """Readable rendered policy for side-by-side comparison (not the Word pipeline)."""
    h = "{{HOSPITAL_NAME}}"
    lines = [
        f"# {draft['policy_title']}",
        f"**{h}**",
        "",
        "*Standards for fire and named non-fire emergencies. Not a drill script.*",
        "",
        "## Document control",
        "",
        draft["resources_required"],
        "",
        "## Safety objective",
        "",
        draft["definitions"],
        "",
        "## 1. Purpose",
        "",
        draft["purpose"],
        "",
        "## 2. Scope",
        "",
        draft["scope"],
        "",
        "## 3. Policy standards",
        "",
        draft["policy_statement"],
        "",
        "## 4. Non-negotiable rules",
        "",
        draft["exceptions"],
        "",
        "## 5. What we do",
        "",
    ]
    for step in draft["procedure_steps"]:
        num_title, _, body = step.partition("\n\n")
        lines.append(f"### {num_title}")
        lines.append("")
        lines.append(body)
        lines.append("")
    lines += [
        "## 6. Stop-work authority",
        "",
        draft["stop_work"],
        "",
        "## 7. Governance and responsibility",
        "",
        draft["responsibility"],
        "",
        "## 8. Quality monitoring (RCA → CAPA)",
        "",
        draft["monitoring_audit"],
        "",
        "## 9. Training and staff acknowledgement",
        "",
        draft["training_competency"],
        "",
        "## 10. References",
        "",
        draft["references_text"],
        "",
        "## 11. Distribution",
        "",
        draft["distribution"],
        "",
        "## 12. Abbreviations",
        "",
        draft["abbreviations"],
        "",
        "## 13. Traceability to NABH SHCO 3rd Edition FMS.5",
        "",
        "This table is an index. It is not how the policy is organised.",
        "",
        "| OE | Requirement | Where this policy addresses it | Responsible |",
        "| --- | --- | --- | --- |",
    ]
    for m in draft["oe_mapping"]:
        req = m["requirement"].replace("|", "/")
        lines.append(f"| {m['oe_code']} | {req} | {m['steps']} | {m['responsible']} |")
    lines += [
        "",
        "## Disclaimer",
        "",
        draft["disclaimer"],
        "",
    ]
    return "\n".join(lines).replace("{{HOSPITAL_NAME}}", "Preview Hospital")


def main() -> int:
    draft = {
        "standard_code": STANDARD_CODE,
        "chapter": CHAPTER,
        "oe_codes": OE_CODES,
        "policy_title": POLICY_TITLE,
        "purpose": PURPOSE,
        "scope": SCOPE,
        "policy_statement": POLICY_STATEMENT,
        "procedure_steps": PROCEDURE_STEPS,
        "stop_work": STOP_WORK,
        "responsibility": RESPONSIBILITY,
        "references_text": REFERENCES,
        "distribution": DISTRIBUTION,
        "abbreviations": ABBREVIATIONS,
        "disclaimer": DISCLAIMER,
        "oe_mapping": OE_MAPPING,
        "universal_facts_checklist": UNIVERSAL_FACTS_CHECKLIST,
        "version": VERSION,
        "revision_history": REVISION_HISTORY,
        "status": "draft",
        # Optional schema fields — used by the v2 renderer; forbidden on pipeline masters.
        "definitions": SAFETY_OBJECTIVE,
        "exceptions": NON_NEGOTIABLES,
        "monitoring_audit": MONITORING_AUDIT,
        "training_competency": TRAINING_ACKNOWLEDGEMENT,
        "resources_required": DOCUMENT_CONTROL,
        "template_test": "fms5_v2_adoptable_shape",
    }

    assert len(PROCEDURE_STEPS) == 8, f"expected 8 operational subsections, got {len(PROCEDURE_STEPS)}"
    for i, s in enumerate(PROCEDURE_STEPS, start=1):
        prefix = f"5.{i} "
        assert s.startswith(prefix), f"step {i} must start with {prefix!r}"
    assert "\r" not in json.dumps(draft)
    _verify_disclaimer(DISCLAIMER, STATUTE_CLAUSE)
    _verify_no_oe_headings(PROCEDURE_STEPS)
    _verify_mapping()
    _verify_placeholders(draft)
    assert draft["status"] == "draft"
    print("status is draft; no SQL written:", True)

    out_json = POLICIES / "drafts" / "fms5_v2_draft.json"
    out_md = POLICIES / "build" / "preview" / "FMS.5_v2_preview.md"
    out_md.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(draft, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = build_markdown(draft)
    expected_headings = [
        "## 1. Purpose",
        "## 2. Scope",
        "## 3. Policy standards",
        "## 4. Non-negotiable rules",
        "## 5. What we do",
        "### 5.1 Detection and raising the alarm",
        "### 5.2 First attack and containment",
        "### 5.3 Evacuation, assembly and dependent patients",
        "### 5.4 Named non-fire emergencies",
        "### 5.5 Exit plan — documented and displayed",
        "### 5.6 Maintenance of fire-related equipment and infrastructure",
        "### 5.7 Mock drills",
        "### 5.8 Service continuity",
        "## 6. Stop-work authority",
        "## 7. Governance and responsibility",
        "## 8. Quality monitoring (RCA → CAPA)",
        "## 9. Training and staff acknowledgement",
        "## 10. References",
        "## 11. Distribution",
        "## 12. Abbreviations",
        "## 13. Traceability to NABH SHCO 3rd Edition FMS.5",
    ]
    numbered = [ln for ln in md.splitlines() if re.match(r"^#{2,3} \d", ln)]
    assert numbered == expected_headings, (
        "heading sequence drifted:\n"
        + "\n".join(f"  got {g!r}" for g in numbered)
    )
    print("markdown heading sequence is 1–13 with 5.1–5.8:", True)
    out_md.write_text(md, encoding="utf-8")
    print(f"wrote {out_json}")
    print(f"wrote {out_md} ({len(md.splitlines())} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
