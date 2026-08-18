-- FMS.5 master policy -- UNAPPROVED DRAFT for review.
-- Do NOT run this insert against Supabase until the owner has reviewed the draft
-- and explicitly confirmed the write. Do NOT set status = 'approved' here.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 8 FMS, printed page 118
-- (PDF page index 124). TWO OEs CARRY THE ASTERISK -- FMS.5.a, d.
-- UNAPPROVED DRAFT. Do not run this insert until the owner confirms the write.


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
  version,
  revision_history,
  status
) values (
  'FMS.5',
  'FMS',
  array['FMS.5.a', 'FMS.5.b', 'FMS.5.c', 'FMS.5.d', 'FMS.5.e'],
  $q$Fire and Non-Fire Emergencies$q$,
  $q$This document sets out how {{HOSPITAL_NAME}} plans for fire and non-fire emergencies within the facilities: plans and provisions for early detection, abatement and containment of fire and of non-fire emergencies; the documented and displayed exit plan; mock drills at least twice a year; the maintenance plan for fire-related equipment and infrastructure; and the service continuity plan in case of fire and non-fire emergencies.

The chapter intent is that the organisation plans for fire and non-fire emergencies. An extinguisher in a locked cupboard, a drill that only evacuates the quality office, or a fire NOC offered as the whole plan, is not that intent.

This document is fire and non-fire emergency planning inside the facilities. It is not FMS.1 utility backup testing (though a power failure may be a non-fire emergency). It is not FMS.2 monthly rounds (though a blocked exit found on a round is closed here). It is not FMS.4 gas-handling SOP (though a gas leak is a named non-fire emergency here). It is not HRM.3 staff training method (when drafted HRM will train to this plan). It is not the billing ledger.$q$,
  $q$This policy applies to fire and non-fire emergencies within the facilities of {{HOSPITAL_NAME}}, and to the people who detect, abate, contain, evacuate, drill, maintain fire equipment and continue services under those plans.

It covers: plans and provisions for early detection, abatement and containment of fire and of non-fire emergencies; documented and displayed exit plan; mock drills at least twice a year; maintenance of fire-related equipment and infrastructure; and service continuity in fire and non-fire emergencies.

Non-fire emergencies are the events this hospital has named from NDMA Hospital Safety Guidelines 2016 (chapter reference 9) and from its own risk picture: earthquake, flood or water ingress, bomb threat, civil unrest, VIP movement if used, lift entrapment if a lift exists, medical-gas leak (FMS.4), major electrical failure after FMS.1.e backup is exhausted or fails, violence that closes a unit, and others this occupancy actually faces. A copied metro-hospital CBRN annex for a ground-floor SHCO that does not face that risk is not this OE.

Boundaries with other policies of {{HOSPITAL_NAME}}:

- ROM.4.a is management's duty that proactive risk exists, including fire. THIS document writes the fire and non-fire plans. HANDOFF ACCEPTED from ROM.4's "FMS facility inspection rounds / fire plan" flag: rounds are FMS.2.d; fire plan is here.
- AAC.6 laboratory fire points at this hospital fire plan. Lab-bench chemical hygiene stays AAC.6; the building fire plan, detection and evacuation are here. HANDOFF ACCEPTED from the AAC FMS fire-plan forward-ref.
- AAC.6.e radiation/PC-PNDT signs are not the fire-exit display. FMS.1.c is wayfinding. THIS document's FMS.5.b is the emergency exit plan, documented and displayed, consistent with those signs.
- FMS.1.e is routine backup testing of electricity and water. A declared emergency after those backups fail, or a fire that kills the plant, is here (abatement and FMS.5.e continuity).
- FMS.2.d monthly rounds find blocked exits, missing extinguishers and wedged fire doors; closure of a fire finding is this maintenance and this plan. FMS.2.a patient-safety devices are not fire detection counted twice. FMS.2.e electrical audits are not this fire-equipment maintenance.
- FMS.3 equipment PPM is not fire-pump or detector maintenance. Fire-related equipment and infrastructure are this FMS.5.d.
- FMS.4 owns gas handling and MGPS tests. A leak, manifold-room fire or oxygen-enriched fire is named here as fire or non-fire as this hospital has classified it.
- COP.8.f / COP.12.b care-process security is not this evacuation of a nursery or a vulnerable patient. This plan must still say how a dependent patient is moved; COP.8/COP.12 remain the care method.
- HIC.2 / HIC.3 / MOM.8 spills are not this fire plan. A chemical fire or toxic release that becomes an emergency is here; the spill SOP stays with those owners.
- HRM.3 (undrafted) owns that staff are trained in the disaster management plan and in handling fire and non-fire emergencies. THIS document owns the plans they are trained to. Do not write the training file here.
- PSQ.5 owns incidents. A fire or a failed drill that harmed someone is dual-entered. PSQ.4 culture of safety is not this drill register.
- PRE.5 billing is not this document.
- NBC 2016 (chapter reference 4), including fire and life-safety provisions as the local fire authority applied them in this hospital's NOC / occupancy given this building's height and built-up area, is the Indian code hook. It is not a NABH sprinkler, hydrant, or occupancy-subdivision mandate for every SHCO. Hospital Safety Index (chapter reference 22) is an evaluator framework, not a mandated score. IPHS 2022 (chapter reference 18) is not this fire plan.$q$,
  $q${{HOSPITAL_NAME}} has plans and provisions for early detection, abatement and containment of fire and of non-fire emergencies.

{{HOSPITAL_NAME}} has a documented and displayed exit plan in case of fire and non-fire emergencies.

{{HOSPITAL_NAME}} holds mock drills at least twice a year.

{{HOSPITAL_NAME}} maintains fire-related equipment and infrastructure.

{{HOSPITAL_NAME}} has a service continuity plan in case of fire and non-fire emergencies.

{{HOSPITAL_NAME}} does not treat a fire NOC in a drawer, an extinguisher that was never inspected, or a drill that never left the quality office, as that duty.$q$,
  array[
    $s$1. Plans and provisions for early detection, abatement and containment

The organisation has plans and provisions for early detection, abatement and containment of the fire, and non-fire emergencies. This step is the documented-evidence anchor of a Core requirement the standard asterisks. An assessor will ask what detects a fire at 03:00, what abates it before the stair is lost, what contains it so a ward not in the compartment can continue, and what the equivalent is for the non-fire events this hospital has named. The answer must be plans and provisions that exist in the building, not a municipal fire NOC offered as the plan, not NBC 2016 copied in full, and not AAC.6's laboratory fire sentence offered as the hospital plan.

The reason detection, abatement and containment are three verbs is that an alarm without an extinguisher, or an extinguisher without a compartment door that closes, is not this OE. NBC 2016 (chapter reference 4) is the framework as the local fire authority applied it to this occupancy: detection (smoke/heat/manual call points as that NOC required), abatement (extinguishers to IS 2190 as NBC-pointed practice, hose reels/hydrant/sprinkler only if that occupancy required them — this document does not invent a sprinkler mandate for every SHCO), containment (fire doors, shutters, compartments as built and as the drawings at FMS.1.b show). NDMA Hospital Safety Guidelines 2016 (chapter reference 9) is the non-fire framework: what is detected (who notices an earthquake, a flood, a bomb threat, a gas leak from FMS.4), what abates it, what contains it so the rest of the hospital is not abandoned without a decision. The common error is a fire plan that is silent on non-fire, or a non-fire plan that is a photocopied district disaster booklet with no hospital roles.

The fire plan (detection, abatement, containment, who is fire warden, how a dependent patient is moved without rewriting COP.8/COP.12), the non-fire plans for events this occupancy actually faces, and the provisions installed, are [Hospital to define — plans and provisions for early detection, abatement and containment of fire and of the non-fire emergencies this hospital has named, using NBC 2016 as the local authority applied it and NDMA Hospital Safety 2016 as framework]. AAC.6 lab fire uses this plan. A service this hospital does not face (for example a basement flood in a single-storey building with no basement) is a recorded absence.$s$,
    $s$2. Documented and displayed exit plan

The organisation has a documented and displayed exit plan in case of fire and non-fire emergencies.

The plan is documented (how each occupied floor leaves, assembly point, who sweeps) and displayed where a first-time family and a night nurse can see it, consistent with FMS.1.c wayfinding and not confused with AAC.6.e radiation signs. A framed plan in the board room, or an exit arrow that points at a locked grilled window, is not this OE. NBC 2016 means of egress as the local authority applied them inform the display; this step does not invent a NABH travel-distance figure.

How the exit plan is documented, where it is displayed, and how a change in a fire door or a ward move updates the display, are [Hospital to define — the documented and displayed exit plan for fire and non-fire emergencies]. FMS.1.b drawings are the controlled set this display must match.$s$,
    $s$3. Mock drills at least twice a year

Mock drills are held at least twice a year. That interval is in the objective element and is not hospital-optional.

A drill tests detection-to-evacuation (or shelter-in-place if that is the plan for a named non-fire event) with the people who would actually be on duty, including a night or weekend sample over the year, and includes a dependent-patient move. The failure mode is two tabletop minutes in the quality office, or a fire-drill photograph of day-shift administration while OT continues unaware. Fire and non-fire need not be eight events; they need to cover, across the year, fire and at least one non-fire this hospital has named.

How drills are scheduled so the floor of twice a year is met, who observes, how a failed objective is recorded and re-drilled, and how HRM.3 (when drafted) uses these as the plans staff are trained to, are [Hospital to define — mock-drill method meeting at least twice a year, covering fire and named non-fire, including a dependent-patient move]. A drill that harmed someone is also a PSQ.5 incident.$s$,
    $s$4. Maintenance plan for fire-related equipment and infrastructure

There is a maintenance plan for fire-related equipment and infrastructure. This step is the documented-evidence anchor of a Commitment requirement the standard asterisks. An assessor will ask for the last inspection of detectors, alarms, extinguishers, hose reels, fire doors, emergency lighting and any pump or sprinkler this occupancy actually has. The answer must be a maintenance plan that was done, not a vendor contract with no job card, not FMS.3 biomedical PPM offered as detector maintenance, and not a fire NOC treated as proof that the pump still starts.

The reason this is a separate OE from 5.a is that a plan to contain fire fails when the door closer is disconnected and the extinguisher gauge is in the red. IS 2190 is the NBC-pointed framework for portable extinguishers (monthly visual and periodic maintenance as that standard's practice — the local interval is hospital-defined, not a NABH monthly-extinguisher mandate invented on top of FMS.2.d's monthly round). Detectors and panels follow the installer's and NBC-as-applied inspection. Fire doors, shutters and emergency lighting are infrastructure on this plan; FMS.2.d may find them failed, this plan repairs them. The common error is to inspect only the extinguishers in the corridor outside the director's office, or to leave a fire pump untested because "the AMC vendor comes yearly."

Which fire-related equipment and infrastructure this occupancy actually has, the maintenance task and interval for each class, who attends (in-house or AMC), and the rule that a failed detector zone or a discharged extinguisher is replaced or isolated with a compensating provision until restored, are [Hospital to define — the maintenance plan for fire-related equipment and infrastructure this occupancy actually has, using IS 2190 as NBC-pointed extinguisher practice and NBC 2016 as the local authority applied it]. An AMC that cannot show last month's extinguisher visual and last test of the alarm is not this OE.$s$,
    $s$5. Service continuity plan

The organisation has a service continuity plan in case of fire and non-fire emergencies.

Continuity is how defined AAC.1 services continue, pause, divert (AAC.2) or move internally (AAC.7) when a ward, OT or plant is lost to fire or to a named non-fire event. It is not FMS.1.e's DG test, though that test is a precondition. It is not ROM.4.e outsourced-quality monitoring. NDMA Hospital Safety 2016 (chapter reference 9) is the framework for keeping essential hospital functions. The failure mode is a continuity plan that says "patients will be shifted to a nearby hospital" with no named hospital, no who-calls, and no list of who cannot be moved without oxygen from FMS.4.c's reserve.

How each essential service continues or is paused, the named receiving arrangement if diversion is the plan, how medical-gas and electrical backups (FMS.4.c / FMS.1.e) are used in that hour, and who declares continuity versus full evacuation, are [Hospital to define — the service continuity plan in case of fire and non-fire emergencies]. AAC.1 unused services are not given a continuity annex.$s$,
    $s$6. Records, review and the order of operations

The fire and non-fire detection/abatement/containment plans and the record of provisions installed, the documented and displayed exit plan (and a photograph or inspection that it is still displayed and still matches FMS.1.b), drill records meeting at least twice a year, fire-equipment and infrastructure maintenance job cards, and the service continuity plan with any activation record, are retrievable.

The quality or accreditation coordinator audits a sample of these records at [Hospital to define — the audit interval for fire and non-fire emergency records] for: provisions that match the occupancy the fire authority actually required rather than a copied sprinkler mandate; non-fire events this building faces rather than a photocopied CBRN annex; exit display that matches drawings and is not AAC.6.e signs; drills twice a year that left the quality office; fire-equipment maintenance that is not FMS.3 PPM; continuity that names how AAC.1 services continue; AAC.6 lab fire pointing here; ROM.4.a left as management duty; HRM.3 left as training method; and PRE.5 billing left with PRE.5.

This policy is reviewed at [Hospital to define — the review interval for this policy], and sooner when a drill failed or a fire-door closer was found disconnected, or when FMS.1, FMS.2, FMS.4, AAC.6 or ROM.4 that this document hands work to are revised.$s$
  ],
  $q$The head of the institution is accountable that fire and non-fire emergency plans exist and are provisioned as this document requires.

A named fire or facilities lead holds the plans, exit display, drill records and fire-equipment maintenance as this hospital has defined those roles.

Fire wardens and night-duty leads execute the exit plan. Clinical heads execute continuity for the services they run.

FMS.1, FMS.2, FMS.3, FMS.4, AAC.1, AAC.6, COP.8, COP.12, ROM.4, PSQ.5 and HRM.3 (when drafted) remain the owning methods named in Scope.

The quality or accreditation coordinator audits the records at step 6.

All staff are expected to treat a blocked exit, a discharged extinguisher left in place, a fire door wedged open, and a year with fewer than two drills, as defects, and to report them.$q$,
  $q$- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Chapter 8 FMS, standard FMS.5.
- National Building Code of India, 2016. Bureau of Indian Standards — chapter reference 4; fire and life-safety framework as the local fire authority has applied it to this occupancy; not a universal sprinkler or occupancy-subdivision mandate. IS 2190 is NBC-pointed portable-extinguisher practice, not an extra paragraph-2 statute.
- National Disaster Management Guidelines. Hospital Safety. (2016). National Disaster Management Authority — chapter reference 9; non-fire and hospital-continuity framework, not an Act of Parliament.
- Hospital safety index: guide for evaluators – 2nd ed. World Health Organization (2015) — chapter reference 22; evaluator framework, not a mandated score.
- Indian Public Health Standards. (2022) — chapter reference 18; not this fire plan.
- Internal documents of {{HOSPITAL_NAME}}: fire plan; non-fire plans; exit display; drill file; fire-equipment maintenance; service continuity plan; FMS.1, FMS.2, FMS.4; AAC.6; ROM.4; drawings at FMS.1.b.$q$,
  $q$Controlled master copy: office of the head of the institution, {{HOSPITAL_NAME}}, with the named fire or facilities lead and the quality or accreditation coordinator.

Copies issued to: fire wardens; night-duty leads; department heads who execute continuity.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder].

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the quality or accreditation coordinator.$q$,
  $q$Abbreviations already defined in the HIC.1 to HIC.6 master policies are not repeated here. A reader using this document on its own should refer to those policies for the shared glossary, including NABH, SHCO, OE, WHO, SOP and PPE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.6:

FMS — Facility Management and Safety (SHCO 3rd Edition Chapter 8)
NBC — National Building Code of India, 2016
NDMA — National Disaster Management Authority
NOC — no-objection certificate (fire/occupancy as the local authority issued it)
AMC — annual maintenance contract
CBRN — chemical, biological, radiological, nuclear (named only as an example of a photocopied annex this occupancy may not need)

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision.$q$,
  $q$This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the National Building Code of India, 2016, insofar as the local fire and building authority has applied it to this facility for fire and life safety, occupancy and the provisions required by this hospital's fire NOC. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced.$q$,
  $q$[{"oe_code": "FMS.5.a", "requirement": "The organisation has plans and provisions for early detection, abatement and containment of the fire, and non-fire emergencies.", "steps": "Steps 1, 6", "evidence": "The fire plan covering detection, abatement and containment with provisions that match the occupancy the local fire authority actually required rather than a municipal NOC in a drawer or a copied sprinkler mandate for every SHCO; non-fire plans for events this building faces using NDMA Hospital Safety 2016 (chapter reference 9) as framework rather than a photocopied CBRN annex; the recorded use of NBC 2016 (chapter reference 4) as applied, not as a pasted code; the recorded splits that AAC.6 lab fire points at this plan, FMS.4 owns gas-handling SOP, COP.8/COP.12 remain care method for dependent patients, and ROM.4.a remains management risk duty; induction of fire wardens; the location of the plans; the audit sample at step 6 of a provision that exists in the building (detector, extinguisher, door closer) not only on paper", "responsible": "Named fire or facilities lead holds the plans and provisions; AAC.6/FMS.4/ROM.4 remain those documents; quality or accreditation coordinator audits"}, {"oe_code": "FMS.5.b", "requirement": "The organisation has a documented and displayed exit plan in case of fire and non-fire emergencies", "steps": "Steps 2, 6", "evidence": "The documented exit plan and inspection that it is displayed on occupied floors, matches FMS.1.b drawings, and is not AAC.6.e radiation signs or FMS.1.c wayfinding counted twice; the audit sample at step 6", "responsible": "Named fire lead; FMS.1.c and AAC.6.e remain those signs; quality or accreditation coordinator audits"}, {"oe_code": "FMS.5.c", "requirement": "Mock drills are held at least twice a year.", "steps": "Steps 3, 6", "evidence": "Drill records meeting at least twice a year covering fire and a named non-fire, including a dependent-patient move and a night or weekend sample across the year, rather than two tabletop minutes in the quality office; HRM.3 flagged as future training method; PSQ.5 dual entry if harm occurred; the audit sample at step 6", "responsible": "Named fire lead schedules drills; HRM.3 when drafted trains to this plan; quality or accreditation coordinator audits"}, {"oe_code": "FMS.5.d", "requirement": "There is a maintenance plan for fire-related equipment and infrastructure.", "steps": "Steps 4, 6", "evidence": "The maintenance plan and job cards for detectors, alarms, extinguishers, hose reels, fire doors, emergency lighting and any pump or sprinkler this occupancy actually has, showing last inspection and a failed item isolated with a compensating provision, rather than a vendor contract with no job card or a fire NOC treated as proof the pump still starts; the recorded use of IS 2190 as NBC-pointed extinguisher practice with hospital-defined local interval, not a NABH monthly-extinguisher mandate stacked on FMS.2.d; the recorded split that FMS.3 biomedical PPM is not detector maintenance and FMS.2.d may find a failure this plan must close; induction of the maintainer; the location of the plan; the audit sample at step 6 of an extinguisher gauge and a door closer that were actually inspected", "responsible": "Named fire or facilities lead holds fire-equipment maintenance; FMS.2.d and FMS.3 remain those programmes; quality or accreditation coordinator audits"}, {"oe_code": "FMS.5.e", "requirement": "The organisation has a service continuity plan in case of fire and non-fire emergencies.", "steps": "Steps 5, 6", "evidence": "The continuity plan showing how AAC.1 essential services continue, pause or divert with a named receiving arrangement and use of FMS.1.e/FMS.4.c backups, rather than an unnamed 'nearby hospital'; the audit sample at step 6", "responsible": "Named fire lead with clinical heads; AAC.1/AAC.2/AAC.7 remain those routes; quality or accreditation coordinator audits"}]$q$::jsonb,
  $q$Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. FMS.5 standard text and all five OEs were read from the official SHCO 3rd Edition PDF, Chapter 8, printed page 118 (PDF page index 124). OE-page header: "The organisation has plans for fire and non-fire emergencies within the facilities." Summary on printed page 115 uses "organization". FMS.5.b has no terminal period in the book — preserved in mapping. PDF md5 39e3bc86d73d651b9cfef283bbf018a9. Levels: a Core, b Commitment, c Commitment, d Commitment, e Achievement.
   TWO OEs CARRY THE ASTERISK -- FMS.5.a and FMS.5.d. b, c, e are unasterisked (Tier 2). FMS.5.a is Core and Tier 1 because it is asterisked. FMS.5.c's "at least twice a year" is in the OE and is stated.
   Asterisks verified 2026-08-18 against the page and scripts/shco_oe_asterisks.json.

TIERING UNDER THE STANDING RULE
1. TWO OF FIVE OEs ARE TIER 1. Tier 1: a, d -- steps 1 and 4 carry the reasoning. Tier 2: b, c, e, with named failure modes and NBC/NDMA frameworks. Shallower T1-style reasoning on b/c/e is a DECISION UNDER THE STANDING RULE.

CROSS-REFERENCE AND OVERLAP CHECK
2. Tier 1 cross-check (2026-08-18) of FMS.5.a/d against AAC.6, ROM.4, FMS.2, FMS.3, FMS.4.
   AAC.6 lab fire vs hospital fire plan -- HANDOFF ACCEPTED.
   ROM.4.a management risk vs this fire plan -- HANDOFF ACCEPTED.
   FMS.2.d round findings vs this maintenance -- finding there, repair here.
   FMS.3 PPM vs fire-equipment maintenance -- split.
   FMS.4 leak vs this emergency -- SOP there, emergency here.
3. FORWARD REFERENCES LANDED: ROM.4 fire plan -- this document. AAC fire plans vs lab fire -- this document / AAC.6 points here. PRE.5 billing -- not absorbed. HRM.3 training to this plan -- flagged.
4. T2 QUICK CHECK: FMS.5.b vs FMS.1.c wayfinding vs AAC.6.e signs -- flagged. FMS.5.c vs HRM.3 -- flagged. FMS.5.e vs FMS.1.e backups vs AAC.2 diversion -- flagged. COP.8/COP.12 dependent-patient move -- flagged.

STATUTORY AND EXTERNAL FACTS
5. P2 names NBC 2016 as applied by the local fire/building authority (NOC/occupancy). NDMA Hospital Safety 2016 is a framework, not an Act. BMW/FSS/CPA/CEA 2010/MHCA are not in P2. IS 2190 is NBC-pointed practice, not an extra P2 statute.
6. No invented NABH sprinkler, hydrant, travel-distance, bed-count or occupancy-subdivision mandate. Drill floor of twice a year is in the OE.

EDITORIAL POSITIONS TAKEN
7. Detection, abatement and containment are three provisions, not a NOC.
8. Non-fire is occupancy-specific; unused CBRN is a recorded absence.

DISCLAIMER BLOCK -- STATUTE-MATCHED UNDER THE 2026-08-17 STANDING RULE
9. P1/P3/P4 shared. P2 names NBC 2016 as applied via fire NOC/occupancy.

DELIBERATELY NOT INCLUDED
- HRM.3 training file. FMS.1 DG test method. FMS.3 biomedical PPM. FMS.4 gas SOP.
- Billing. BMW. A universal sprinkler mandate.
- The five optional sections are left unset.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] -- 10 fillable blanks in the rendered document: 2 in the exact form "[Hospital to define]" (one in Abbreviations, one inside the shared Disclaimer block) and 8 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 2 of 10; a search for "Hospital to define" without brackets finds all 10, and that is the search a hospital should be told to run. The figure is produced by policy_placeholder_audit.py across every rendered field in both forms, which also asserts that no nested placeholder exists.

The values the hospital must supply: fire and non-fire detection/abatement/containment plans and provisions; exit-plan documentation and display; mock-drill method meeting twice a year; fire-equipment maintenance plan; service continuity plan; the audit interval; the review interval; the intranet or folder location; and any additional local abbreviation.$q$,
  '1.0',
  $q$[{"version": "1.0", "date": "18-08-2026", "description": "Initial release."}]$q$::jsonb,
  'draft'
);
