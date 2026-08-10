# -*- coding: utf-8 -*-
"""Builds the HIC.4 master policy draft: JSON for review + SQL for the Supabase SQL Editor.

Column types confirmed against the live schema (2026-08-06):
  oe_codes        text[]
  procedure_steps text[]
  oe_mapping      jsonb

Official source: NABH Standards for Small Healthcare Organisations, 3rd Edition (August 2022),
Chapter 5 Hospital Infection Control, standard HIC.4 and OEs HIC.4.a-f, read from the standards
PDF at printed pages 94-95. All six OEs are Commitment level; HIC.4.f alone carries the asterisk
(doc_required = true in shco_full_oes).

The five optional sections (definitions, training_competency, resources_required,
monitoring_audit, exceptions) are deliberately left unset, matching HIC.1-3.
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

STANDARD_CODE = "HIC.4"
CHAPTER = "HIC"
OE_CODES = ["HIC.4.a", "HIC.4.b", "HIC.4.c", "HIC.4.d", "HIC.4.e", "HIC.4.f"]

POLICY_TITLE = "Prevention of Healthcare Associated Infections and Staff Occupational Health"

PURPOSE = """This document sets out the actions {{HOSPITAL_NAME}} takes to prevent the four healthcare associated infections that arise from the things a hospital does to a patient — urinary catheterisation, mechanical ventilation, intravascular access and surgery — and the actions it takes to protect the health of the people who deliver that care.

The four infections are grouped together because they share a cause. None of them is transmitted to the patient by chance; each follows a device or an incision that the hospital chose to place, and each is reduced by the same method — a small number of interventions performed together, every time, on every patient, and verified rather than assumed.

The second half of this document concerns staff. A healthcare worker is both a route by which infection reaches a patient and a person who can be harmed by the patient's infection. This policy states what {{HOSPITAL_NAME}} does to keep its workers well enough and protected enough not to become the former, and what it does for them when, despite that, an exposure occurs."""

SCOPE = """This policy applies to every area of {{HOSPITAL_NAME}} in which a urinary catheter is placed, a patient is mechanically ventilated, an intravascular device is inserted or maintained, or a surgical or invasive procedure is performed — inpatient wards, critical care and high-dependency areas, operation theatres and procedure rooms, the labour room, emergency, day-care, dialysis, and any outpatient area where these are done.

The occupational health and post-exposure provisions apply more widely still. They bind every person engaged by {{HOSPITAL_NAME}} who may come into contact with blood, body fluids, contaminated sharps, biomedical waste, soiled linen or an infectious patient. That includes employed clinical and non-clinical staff, visiting and consultant practitioners, nurses, technicians, therapists, students and trainees on clinical attachment, housekeeping, laundry, kitchen, security, mortuary and biomedical engineering personnel, and outsourced or contract staff of every description. Where a person is engaged through a contractor, {{HOSPITAL_NAME}} remains responsible for ensuring these provisions reach them, and says so in the contract.

The division of responsibility between this policy and the infection prevention and control practices policy is deliberate and should be read carefully. That policy governs the practices which prevent an exposure from happening — standard precautions, hand hygiene, transmission-based precautions, safe injection and infusion practice, sharps handling and personal protective equipment. This policy governs the health of the worker and everything that happens after an exposure has occurred: fitness for placement, immunisation, work restriction, first aid at the point of exposure, risk assessment, testing, post-exposure prophylaxis and follow-up. Where the two documents touch, they are intended to agree; where a reader finds they do not, the discrepancy is reported to the Infection Control Team for resolution at the next revision of both.

What this policy does not cover: the method of surveillance by which infection is counted. Standard case definitions, numerator and denominator collection, device-day counting, rate calculation, benchmarking and validation belong to the surveillance policy. This policy measures whether the preventive actions were performed — a process measure it owns — and hands the resulting infection data to surveillance to be counted. It also does not restate the governance of the infection control programme, the practices set out in the clinical areas policy, the support services requirements, or instrument reprocessing and sterilisation, each of which has its own policy."""

POLICY_STATEMENT = """{{HOSPITAL_NAME}} holds that a healthcare associated infection is, in the great majority of cases, a preventable outcome and not an unavoidable cost of treatment. A device-associated infection begins with a decision to place a device, and every day that device stays in is a decision to leave it there.

{{HOSPITAL_NAME}} therefore adopts the bundle as its method. A bundle is a short list of interventions, each independently supported by evidence, which are performed together and scored together: performing four elements out of five is recorded as a failure of the bundle, not as eighty per cent success. This is not pedantry. The value of a bundle lies in its reliability, and a bundle applied inconsistently returns little of the benefit its individual elements promise.

{{HOSPITAL_NAME}} commits to the daily question. For every indwelling urinary catheter, every central line and every ventilated patient, the care team asks each day whether the device is still needed, records the answer, and removes what is no longer needed the same day. Most device-associated infection is prevented by devices that were never placed or were taken out sooner.

{{HOSPITAL_NAME}} does not regard a low reported infection rate as evidence that its practice is sound. A rate depends on how hard the hospital looks. Compliance with the preventive actions is measured directly, by observation, and is reported alongside the rate so that the two can be read against each other.

On staff, {{HOSPITAL_NAME}} states plainly that the health of its workers is a condition of patient safety and not a separate welfare matter. It undertakes to assess fitness at placement, to offer the immunisation the work requires, to restrict from patient contact any worker whose own infection puts patients at risk, and to bear the cost of all of this itself. No charge for immunisation, assessment, post-exposure prophylaxis or follow-up is passed to a worker of {{HOSPITAL_NAME}}, whether employed or contracted.

{{HOSPITAL_NAME}} further undertakes that reporting an exposure carries no penalty of any kind. Under-reporting of needlestick and mucosal exposure is the single largest obstacle to managing it, and it is driven by fear — of blame, of the result, of being seen as careless. A worker who reports an exposure at {{HOSPITAL_NAME}} is treated as having done the right thing, and is told so."""

PROCEDURE_STEPS = [
"""1. What "taking action to prevent" means at {{HOSPITAL_NAME}}

Steps 2 to 22 set out the preventive actions for the four healthcare associated infections named in this standard. They are written to a common method, and the method matters as much as the content.

For each of the four, {{HOSPITAL_NAME}} maintains a written care bundle: a defined, short set of interventions applied to every eligible patient, every time. The bundle is not a summary of good practice; it is a checklist against which compliance is scored all-or-none. A bundle is recorded as complied with only where every applicable element was performed. Where an element was deliberately omitted for a clinical reason, the reason is recorded against that patient and the bundle is scored as a justified variance rather than as compliance.

Each bundle is separated into insertion elements, performed once, and maintenance elements, performed continuously for as long as the device or wound remains. Both are audited; maintenance is the part more often lost, because the person who inserted the device is rarely the person caring for it a week later.

The clinical content of each bundle is reviewed by the Infection Prevention and Control Committee against current national and international guidance at an interval of [Hospital to define], and whenever a significant change in that guidance is published. Where guidance is genuinely contested — and several elements in these bundles are — {{HOSPITAL_NAME}} records the position it has adopted, the source it followed, and the date, so that a later reader can see that a choice was made rather than an oversight committed.

Bundle compliance is measured as set out in step 23. Infection rates arising from these bundles are counted under the surveillance policy, not here.""",

"""2. Catheter-associated urinary tract infection — deciding whether to catheterise at all

The most effective action against catheter-associated urinary tract infection is not to place the catheter. {{HOSPITAL_NAME}} therefore treats urinary catheterisation as a clinical decision requiring an indication, not as a routine element of admission, of surgery, or of nursing an incontinent patient.

An indwelling urinary catheter is placed at {{HOSPITAL_NAME}} only for a recorded indication. Recognised indications are: acute urinary retention or bladder outlet obstruction; a need for accurate measurement of urine output in a critically ill patient where that measurement will change management; selected surgical procedures and defined peri-operative periods; to assist healing of an open sacral or perineal wound in an incontinent patient; a requirement for prolonged immobilisation, for example an unstable spine or multiple traumatic injuries; and comfort at the end of life.

The following are not indications and a catheter is not placed for them at {{HOSPITAL_NAME}}: as a substitute for nursing care of a patient who is incontinent; to obtain urine for culture or other tests from a patient who can void voluntarily; for the convenience of staff or of the patient's attendants; or continued after surgery beyond the period the procedure itself justified.

The indication is entered in the case record at the time of insertion, together with the date and time and the name of the person who inserted. A catheter for which no indication is recorded is treated on the next daily review as a catheter without an indication, and removed.

Before catheterising, the treating team considers the alternatives set out in step 5. Where a bladder scanner is available, it is used to establish whether retention is actually present rather than inferring it.""",

"""3. Catheter-associated urinary tract infection — insertion

Insertion is performed only by a person trained and assessed as competent in the procedure. {{HOSPITAL_NAME}} maintains a list of staff so assessed; a member of staff not on that list does not catheterise unsupervised, and trainees insert under direct supervision until assessed.

The insertion bundle at {{HOSPITAL_NAME}} is:

- hand hygiene immediately before the procedure and again immediately after, in addition to glove use and not in place of it;
- aseptic technique throughout, with sterile equipment: sterile gloves, a sterile drape, sterile sponges or swabs, an antiseptic or sterile solution for periurethral cleaning, and a single-use sachet of sterile lubricant;
- cleaning of the periurethral area before insertion;
- selection of the smallest bore catheter that will drain adequately and, where the catheter is to remain, that minimises trauma at the urethra and bladder neck;
- connection to a sterile closed drainage system at the moment of insertion, with the system not broken thereafter;
- securement of the catheter after insertion so that movement and traction on the urethra are prevented.

Insertion is documented at the time. The record states the indication, the date and time, the catheter type and size, whether insertion was achieved at the first attempt, and the inserter's name. Repeated failed attempts are recorded and the procedure handed to a more experienced operator rather than persisted with; each failed attempt traumatises the urethra and raises the infection risk of the catheter finally placed.""",

"""4. Catheter-associated urinary tract infection — maintaining the closed system

Once a closed system is established, the whole of the remaining risk turns on keeping it closed and keeping it draining. The maintenance bundle at {{HOSPITAL_NAME}} is performed and recorded on every shift:

- the drainage system remains closed; it is not disconnected for any reason. Where disconnection has occurred, or where aseptic technique was broken, or where the system leaks, the catheter and the collecting system are both replaced aseptically, as a set — reconnecting a system that has been opened does not restore it;
- urine flow is unobstructed at all times: the catheter and tubing are kept free of kinks, dependent loops and compression, and the patient is not lain on the tubing;
- the drainage bag is kept below the level of the bladder at all times, including during transfer, transport, ambulation and imaging, and is never rested on the floor;
- the bag is emptied regularly and before it is full, using a separate clean collecting container for each patient, with the drainage spigot not touching the container or any other surface;
- hand hygiene is performed and clean gloves worn before handling the catheter or the drainage system, and hand hygiene repeated afterwards;
- routine meatal hygiene is performed as part of daily bathing, with soap and water. Antiseptics are not applied to the meatus as a routine measure, and antiseptic or antimicrobial instillation into the bladder or the drainage bag is not performed;
- catheters and drainage bags are not changed at fixed routine intervals. They are changed for clinical indication — obstruction, leakage, breach of the system, contamination, or a manufacturer-stated maximum dwell time for the catheter material.

Systemic antimicrobials are not given as prophylaxis to prevent catheter-associated urinary tract infection in a patient with a catheter in situ.""",

"""5. Catheter-associated urinary tract infection — daily review, removal and alternatives

Every indwelling urinary catheter at {{HOSPITAL_NAME}} is reviewed once every day. The review asks one question — is the recorded indication still present — and produces one of two recorded answers: the indication continues, and why; or it does not, and the catheter is removed today.

The review is documented in the nursing record and countersigned or endorsed by the treating team. {{HOSPITAL_NAME}} implements a reminder mechanism so that the review cannot simply be forgotten: [Hospital to define — for example a daily catheter round, a prompt on the nursing handover sheet, a ward catheter register, or a nurse-initiated removal protocol under which nursing staff may remove a catheter without a fresh medical order once no listed indication applies].

Where a catheter can be avoided altogether, it is. The alternatives considered at {{HOSPITAL_NAME}} are:

- intermittent catheterisation, in place of an indwelling catheter, where bladder emptying rather than continuous drainage is what is needed;
- external collection devices for a cooperative male patient without retention or outlet obstruction;
- continence care, timed voiding and absorbent products for the incontinent patient who has no other indication;
- bladder scanning to confirm or exclude retention before catheterising, and to guide intermittent catheterisation.

Catheter days are the denominator against which this hospital's performance in this area is ultimately judged. Reducing them is the intervention with the largest effect, and it is a matter of daily discipline rather than of technique.""",

"""6. Catheter-associated urinary tract infection — specimens, and what is not done

Urine specimens from a catheterised patient are collected aseptically. A small volume for culture is taken from the sampling port after disinfecting it, using a sterile syringe; where a larger volume is genuinely required, it is taken aseptically from the drainage bag. Specimens are not taken by disconnecting the system, and are not taken from the bag for culture where a port is available.

Urine is cultured when there is a clinical question to answer. {{HOSPITAL_NAME}} does not culture urine as a screening test in catheterised patients, and does not treat a positive culture in the absence of signs or symptoms. Asymptomatic bacteriuria in a catheterised patient is common, is not an infection, and treating it produces resistance without producing benefit. The circumstances in which asymptomatic bacteriuria is nonetheless treated — pregnancy, and before an invasive urological procedure with anticipated mucosal bleeding — are set out in the antimicrobial usage policy and are not extended beyond it.

This distinction is stated here because it is the point at which prevention and reporting most often go wrong together: a hospital that cultures every catheterised patient will find bacteriuria, will treat it, will record the treatment as an infection, and will conclude that its bundle is failing when the fault lies in its testing.

Where infection is genuinely suspected, the catheter is reassessed for removal or replacement as part of the clinical response, and the case is notified to the Infection Control Team for surveillance under the surveillance policy.""",

"""7. Ventilator-associated pneumonia and infection-related ventilator-associated complication — applicability

{{HOSPITAL_NAME}} records here whether it provides invasive mechanical ventilation: [Hospital to define — state whether invasive mechanical ventilation is provided, in which areas, and with how many ventilators].

Where invasive mechanical ventilation is not provided at {{HOSPITAL_NAME}}, this is recorded as a not-applicable position with the reason — [Hospital to define — for example that the hospital operates no intensive care beds and transfers any patient requiring intubation under a documented referral arrangement to a named receiving hospital]. That declaration is dated, signed by the head of the institution, tabled at the Infection Prevention and Control Committee, and reviewed at each revision of this policy. It is not sufficient to leave steps 8 to 11 silently unused; a section that is not applicable is declared not applicable, with a reason, in writing.

Where any form of ventilation is provided — including non-invasive ventilation, and including short-term ventilation of a post-operative or transferring patient — the relevant parts of steps 8 to 11 apply for as long as the patient is ventilated, however briefly.

A note on what this objective element names. The standard refers to infection-related ventilator-associated complication as well as to ventilator-associated pneumonia, and the two are not synonyms. Contemporary surveillance describes a tiered set of ventilator-associated events: a sustained deterioration in oxygenation after a period of stability; that deterioration accompanied by evidence of infection and the start of an antimicrobial; and, within that, cases with microbiological evidence pointing to pneumonia. {{HOSPITAL_NAME}} prevents all of these with a single set of actions, set out below. Which tier a given case falls into is a surveillance question, settled under the surveillance policy against published case definitions, and is not decided here.""",

"""8. Ventilator-associated pneumonia — avoiding and shortening invasive ventilation

As with the urinary catheter, the largest single reduction comes from the device that was not placed, or was removed a day earlier.

{{HOSPITAL_NAME}} therefore requires that:

- non-invasive ventilation or high-flow nasal oxygen is considered, and the consideration recorded, before intubating a patient in whom either could reasonably succeed;
- sedation is minimised. Sedation is targeted to a defined level of consciousness using a validated sedation scale rather than titrated to stillness, the target is recorded, and the patient is assessed against it at defined intervals;
- sedation is interrupted daily, unless a recorded contraindication applies, and the patient is assessed for readiness to breathe spontaneously. Where the interruption is tolerated, a spontaneous breathing trial follows the same day, and the two are performed as a paired procedure rather than independently;
- readiness to extubate is assessed daily and the assessment recorded, whether or not extubation follows;
- early mobilisation and rehabilitation are provided from the earliest point at which the patient's condition permits, because deconditioning prolongs ventilation and prolonged ventilation is the exposure that matters;
- the ventilator weaning and extubation protocol of {{HOSPITAL_NAME}} is written, is available at the bedside, and is [Hospital to define].

Where a contraindication to daily sedation interruption or to a spontaneous breathing trial exists, it is recorded against the patient for that day. A blank is treated on audit as an omission, not as a contraindication.""",

"""9. Ventilator-associated pneumonia — position, the mouth and the airway

The ventilated patient at {{HOSPITAL_NAME}} is nursed with the head of the bed elevated to between 30 and 45 degrees, unless a specific contraindication is recorded. The elevation is checked and recorded at each nursing shift and after every procedure, transfer or bed change, because it is routinely lost during them and rarely restored unprompted.

Oral care is provided at a defined frequency of [Hospital to define] and comprises two elements, both of which are required:

- mechanical cleaning of the teeth, gums, tongue and oral cavity, by brushing;
- chlorhexidine gluconate oral antiseptic, applied at the same frequency. The concentration used at {{HOSPITAL_NAME}} is [Hospital to define], the preparations in common use being in the range of 0.12 to 0.2 per cent. An oral, non-alcoholic preparation is used; skin or surgical chlorhexidine preparations are not used in the mouth.

Oral care is recorded on the ventilator care chart each time it is given. Both elements are scored, and giving one without the other is recorded as the bundle element not performed.

Chlorhexidine is mandated here rather than left to local choice. {{HOSPITAL_NAME}} notes that guidance on routine chlorhexidine oral care in ventilated patients has been revised in recent years and is not uniform between authorities, while mechanical cleaning is not in dispute. The position adopted by {{HOSPITAL_NAME}} is recorded under step 1 together with the source relied on and the date, and is re-examined at each review of this policy under step 38.

The airway itself is managed as follows:

- for a patient expected to require ventilation beyond the first two to three days, an endotracheal tube with a subglottic secretion drainage port is used where available, and the drainage is actually applied and recorded rather than the port left unused;
- cuff pressure is measured with a manometer at a defined frequency of [Hospital to define] and maintained within the range specified by {{HOSPITAL_NAME}}, conventionally around 20 to 30 centimetres of water. Pressure is not judged by palpation of the pilot balloon;
- suctioning is performed only when clinically indicated, using aseptic technique, with hand hygiene before and after and clean or sterile gloves as the technique requires;
- where a closed in-line suction system is used, it is changed for clinical indication and not on a fixed routine schedule;
- the airway is not disconnected unnecessarily, and where disconnection is unavoidable the circuit is protected.""",

"""10. Ventilator-associated pneumonia — circuit, condensate and equipment

The ventilator circuit at {{HOSPITAL_NAME}} is changed when it is visibly soiled or is malfunctioning, and between patients. It is not changed at fixed routine intervals; routine circuit changes increase manipulation without reducing pneumonia.

Condensate collects in the tubing and is contaminated. It is drained away from the patient, at a defined frequency and before any repositioning of the patient or the circuit, and is never allowed to run back towards the airway. Hand hygiene is performed after handling condensate, and the fluid is disposed of as biomedical waste.

Humidifiers, heat and moisture exchangers, nebuliser chambers, resuscitation bags and ventilator accessories are single-patient items. They are reprocessed between patients according to the sterilisation and disinfection policy, and the reprocessing is recorded; this policy does not restate the method. Sterile water only is used to fill humidifier reservoirs and nebulisers, and reservoirs are not topped up — they are emptied, dried and refilled.

Medication for nebulisation is prepared aseptically, drawn immediately before use, and not left standing in the nebuliser chamber between doses.

Ventilators, monitors, bed rails, infusion pumps and the surfaces around a ventilated patient are cleaned and disinfected at the frequency and with the agents set out in the support services policy. High-touch surfaces around a ventilated bed space are the route by which organisms reach the circuit; they are treated as part of ventilator care and not as housekeeping.""",

"""11. Ventilator-associated pneumonia — supporting elements and the daily review

The following are performed for every ventilated patient at {{HOSPITAL_NAME}} unless a contraindication is recorded:

- enteral nutrition is started early in preference to parenteral nutrition, and gastric overdistension is avoided, with feed volume, residual assessment and tube position managed to the written feeding protocol of {{HOSPITAL_NAME}};
- prophylaxis against venous thromboembolism is prescribed or its omission justified;
- stress ulcer prophylaxis is prescribed on assessed risk rather than as a routine for every ventilated patient, and is reviewed for discontinuation as risk falls;
- oral rather than nasal intubation is preferred where the clinical situation permits, and the route is recorded;
- the patient is repositioned and the airway suctioned before any planned cuff deflation or tube movement.

A ventilator care review is conducted once daily for each ventilated patient and recorded on the ventilator care chart. It confirms, item by item, that the head of the bed was elevated, that sedation was assessed against target and interrupted or a contraindication recorded, that a spontaneous breathing trial was performed or a contraindication recorded, that oral care was given at the required frequency, that cuff pressure was checked, and that the patient's readiness for extubation was assessed. The chart is the audit record for step 23; a bundle element left blank is scored as not performed.

Any ventilated patient who develops new or worsening oxygenation requirements is assessed clinically, and the case is notified to the Infection Control Team for classification and counting under the surveillance policy.""",

"""12. Catheter-linked bloodstream infection — applicability and what is covered

{{HOSPITAL_NAME}} records here whether central venous access is established on its premises: [Hospital to define — state whether central venous catheters, peripherally inserted central catheters, haemodialysis catheters, tunnelled lines or implanted ports are inserted or maintained, in which areas, and by whom].

Where central venous access is neither inserted nor maintained at {{HOSPITAL_NAME}}, this is recorded as a not-applicable position with the reason — [Hospital to define] — dated, signed by the head of the institution, tabled at the Infection Prevention and Control Committee, and reviewed at each revision of this policy, on the same basis as step 7. The peripheral cannula provisions at step 16 apply in every case, because every hospital places peripheral cannulae.

What this objective element covers is bloodstream infection linked to an intravascular device. At {{HOSPITAL_NAME}} that means: non-tunnelled and tunnelled central venous catheters; peripherally inserted central catheters; haemodialysis catheters and arteriovenous access; implanted ports; arterial catheters used for monitoring; umbilical catheters where neonatal care is provided; and peripheral intravenous cannulae. Each is covered by the provisions below to the extent that they apply to it.

Insertion of a central line is performed only by an operator trained and assessed as competent, or by a trainee under the direct supervision of such an operator. {{HOSPITAL_NAME}} maintains the list of assessed operators and the date of each assessment.""",

"""13. Catheter-linked bloodstream infection — the decision, the site and the insertion

A central venous catheter is placed at {{HOSPITAL_NAME}} only where there is a recorded indication that peripheral access cannot meet, and the indication is entered in the case record at insertion.

Site selection weighs infection risk against mechanical risk, and the choice is recorded. For a non-tunnelled central catheter in an adult, the femoral site carries the highest infection risk and is avoided where an alternative is feasible; the subclavian site carries the lowest infection risk but the higher risk of mechanical complication, and the balance is a clinical judgement for the operator on the individual patient. In a patient with advanced kidney disease, vein preservation for future access takes precedence and the site is selected in consultation with the treating nephrologist.

The insertion bundle at {{HOSPITAL_NAME}} is performed as a single sequence and recorded on a central line insertion checklist:

- hand hygiene immediately before the procedure;
- maximal sterile barrier precautions for the operator and assistants — cap, mask, sterile gown and sterile gloves — and a sterile full-body drape over the patient, not a fenestrated towel;
- skin antisepsis with an alcohol-based chlorhexidine gluconate preparation, applied and then allowed to dry completely before puncture. Where chlorhexidine is contraindicated or the patient is very young, an alternative agent is used and the substitution recorded;
- ultrasound guidance where available, to reduce the number of punctures;
- a catheter with the minimum number of lumens required for the intended therapy;
- securement and application of a sterile dressing at the end of the procedure.

A checklist is completed for every insertion by a trained observer who is not the operator, and that observer is explicitly authorised — in writing, by the head of the institution — to halt a non-emergency procedure if asepsis is breached. This authority is stated here because it does not work unless it is stated: an observer who must challenge a senior operator without written backing will not do so.

In a genuine emergency where full asepsis could not be observed, that fact is recorded and the catheter is replaced at the earliest safe opportunity, and in any event within [Hospital to define].""",

"""14. Catheter-linked bloodstream infection — the dressing and the access hub

After insertion, the two remaining routes into the bloodstream are the skin at the exit site and the hub through which the line is accessed. Both are governed here.

The exit site:

- is covered with a sterile transparent semipermeable dressing, or with sterile gauze where the site is bleeding or oozing or the patient is diaphoretic;
- is inspected at every dressing change and, through an intact transparent dressing, at least once each shift, with the site condition recorded;
- has its transparent dressing changed at an interval not exceeding seven days, and its gauze dressing at an interval not exceeding two days, and either changed immediately whenever it becomes damp, soiled, loosened or no longer intact;
- is cleaned at each dressing change with an alcohol-based chlorhexidine preparation, allowed to dry;
- may, where the infection rate at {{HOSPITAL_NAME}} does not fall despite full compliance with this bundle, be dressed with a chlorhexidine-impregnated dressing, subject to the escalation decision at step 16.

The hub, and every port, connector and stopcock:

- is disinfected before every single access, by scrubbing the surface with an appropriate antiseptic for a defined time and allowing it to dry. The agent and the scrub time adopted by {{HOSPITAL_NAME}} are [Hospital to define], and are displayed at the bedside. "Wiping" is not scrubbing, and a hub accessed while still wet has not been disinfected;
- is covered by a sterile cap when not in use, and a cap once removed is discarded and not replaced;
- is accessed only with sterile devices, following hand hygiene, and never with a syringe that has already been used on any patient.

Dressing changes and hub care are recorded. The record is the maintenance audit trail for step 23.""",

"""15. Catheter-linked bloodstream infection — infusates, administration sets and line necessity

Administration sets at {{HOSPITAL_NAME}} are replaced on the following basis:

- sets used for continuous infusion of fluids that do not contain blood, blood products or lipid, at an interval defined by {{HOSPITAL_NAME}} of [Hospital to define], which is not more frequent than every 96 hours and not less frequent than every 7 days;
- sets used to administer blood, blood products or lipid-containing emulsions, within 24 hours of starting the infusion;
- sets used for propofol, at the interval stated by the manufacturer;
- any set immediately, where its integrity is in doubt or it has been contaminated.

Parenteral fluids and admixtures are prepared aseptically, in the pharmacy where {{HOSPITAL_NAME}} provides that service; where preparation occurs in a clinical area, it is done in a designated clean space, immediately before use, and never in a dirty utility, at a sluice or on an open trolley in a corridor. Infusion bags and bottles are inspected for turbidity, particulate matter, leakage and expiry before use, and a container once entered is not stored for later use.

Line necessity is reviewed every day for every intravascular device, and the review is recorded alongside the ventilator and catheter reviews. A central line remaining solely because it is convenient, because peripheral access is difficult, or because no one has considered removing it, is removed.

Central catheters are not replaced at routine intervals in order to prevent infection, and a guidewire exchange is not used to prevent infection — it is used only to replace a malfunctioning catheter where the site is not suspected of infection. Systemic antimicrobial prophylaxis is not given to prevent catheter-related bloodstream infection.

Where catheter-related bloodstream infection is suspected, blood cultures are taken before antimicrobials are started, from a peripheral vein and from the catheter, and the case is notified to the Infection Control Team.""",

"""16. Catheter-linked bloodstream infection — peripheral cannulae, and escalation when the rate does not fall

Peripheral intravenous cannulae are the most numerous intravascular devices at {{HOSPITAL_NAME}} and receive the least attention. They are governed as follows:

- inserted only for a recorded indication, using aseptic non-touch technique, after hand hygiene and skin antisepsis allowed to dry;
- upper limb sites preferred to lower limb in adults; a site over a joint avoided where possible;
- secured and covered with a sterile transparent dressing that permits inspection;
- inspected at least once each shift for pain, tenderness, erythema, swelling, induration and discharge, with the finding recorded against a phlebitis scale adopted by {{HOSPITAL_NAME}} of [Hospital to define];
- removed immediately on any sign of phlebitis or infection, on suspected contamination, or when no longer needed; and in any event reviewed daily for continued need;
- where a cannula was inserted in an emergency without full asepsis, replaced as soon as practicable and in any event within [Hospital to define].

Asymptomatic peripheral cannulae in adults are replaced at a routine fixed interval, which at {{HOSPITAL_NAME}} is [Hospital to define] hours, set within the band of 72 to 96 hours. The interval is not shortened below 72 hours, since more frequent replacement subjects the patient to additional cannulations without reducing infection. It is not extended beyond 96 hours for an asymptomatic cannula under this policy.

This applies to the routine replacement of a cannula that remains clinically needed and shows no sign of phlebitis or infection. It does not displace the obligations above: a cannula showing any sign of phlebitis or infection is removed immediately whatever its age, a cannula no longer needed is removed at the daily review whatever its age, and a cannula inserted without full asepsis is replaced under the emergency provision rather than left to the routine interval.

In children, routine replacement of an asymptomatic, functioning peripheral cannula is not performed; the cannula is left until therapy is complete or a clinical indication for removal arises.

The date and time of insertion is recorded on the cannula dressing and in the nursing record so that the interval can be applied and audited. A cannula whose insertion time cannot be established is treated as due for replacement.

Escalation. Where the catheter-related bloodstream infection rate at {{HOSPITAL_NAME}} does not fall despite audited compliance with the bundles above, the Infection Prevention and Control Committee considers the additional measures — chlorhexidine-impregnated dressings, antimicrobial-impregnated catheters, antimicrobial lock solutions, or chlorhexidine bathing of patients in critical care. These are second-line measures. They are considered only after compliance has been measured and found adequate, because adopting them in place of basic compliance spends money to conceal a practice problem.""",

"""17. Surgical site infection — the pre-operative period

Surgical site infection is prevented across three periods — before, during and after the operation — and the pre-operative period carries more of the burden than is generally credited.

Before elective surgery at {{HOSPITAL_NAME}}:

- the patient is assessed for modifiable risk, and the assessment recorded: glycaemic control, nutritional state, obesity, smoking, concurrent infection elsewhere, immunosuppressive therapy, and anaemia;
- an active infection remote from the operative site is identified and treated, and elective surgery deferred until it is resolved, unless deferral itself carries the greater risk and that judgement is recorded;
- blood glucose is optimised before admission in a diabetic patient, and the target adopted by {{HOSPITAL_NAME}} is [Hospital to define];
- the patient who smokes is advised to stop and is offered support, at the earliest point in the pathway rather than on the morning of surgery;
- a patient who is undernourished and is to undergo major surgery is considered for nutritional supplementation before operation;
- the pre-operative stay is kept as short as the clinical situation allows, because the length of pre-operative hospitalisation correlates with colonisation by hospital organisms.

Mechanical bowel preparation is not used alone as an infection-prevention measure. In elective colorectal surgery, where {{HOSPITAL_NAME}} uses it, it is combined with oral antimicrobials in accordance with the protocol of {{HOSPITAL_NAME}}, which is [Hospital to define].

The surgical safety checklist of {{HOSPITAL_NAME}} is completed for every operation, and its sign-in, time-out and sign-out points include confirmation of antimicrobial prophylaxis and of sterility indicators. The checklist itself is governed by the patient safety policy; what this policy fixes is that the infection-prevention items on it are actually asked aloud and answered, not ticked in advance.""",

"""18. Surgical site infection — bathing, hair removal and decolonisation

Bathing. The patient bathes or showers before surgery, using plain soap or an antimicrobial soap, at a time defined by {{HOSPITAL_NAME}} of [Hospital to define]. The purpose is to reduce the microbial load on the skin; the choice between plain and antimicrobial soap is a matter on which the evidence does not strongly separate the two, and either is acceptable provided the bath actually happens and is recorded.

Hair removal. Hair is not removed unless it will physically interfere with the operation. Where removal is necessary:

- it is done with clippers with a single-use head, or with a depilatory agent where appropriate;
- it is never done with a razor. Razors produce micro-abrasions that are colonised by the time of incision, and shaving the night before is worse than shaving immediately before, which is itself worse than not shaving at all;
- it is done as close to the time of surgery as practicable, and outside the operating room;
- razors are not stocked in pre-operative areas or wards of {{HOSPITAL_NAME}} for this purpose, because a policy against shaving that leaves razors within reach is not a policy.

Decolonisation. For a patient known to be a nasal carrier of Staphylococcus aureus undergoing cardiothoracic or orthopaedic surgery, {{HOSPITAL_NAME}} provides nasal mupirocin, with or without a chlorhexidine body wash, in accordance with its written decolonisation protocol. Whether {{HOSPITAL_NAME}} screens for carriage before such surgery, and in which patient groups, is [Hospital to define]; mupirocin is not used indiscriminately, because unrestricted use produces mupirocin resistance and removes the option.

Antiseptic-impregnated adhesive incise drapes are not used as an infection-prevention measure. Where {{HOSPITAL_NAME}} uses incise drapes for another reason, that reason is recorded and they are not credited as prevention.""",

"""19. Surgical site infection — surgical antimicrobial prophylaxis

Surgical antimicrobial prophylaxis is the element most often got wrong, and it is got wrong in a characteristic way: the right drug given at the wrong time, and then continued for days.

At {{HOSPITAL_NAME}}:

- the procedures for which prophylaxis is indicated, and the agent and dose for each, are set out in the surgical prophylaxis schedule of {{HOSPITAL_NAME}}, which forms part of the antimicrobial usage policy and is [Hospital to define]. Prophylaxis is not prescribed by individual preference outside that schedule;
- the dose is given so that an effective tissue concentration is present at the moment of incision. It is administered within 120 minutes before incision, and for most agents in ordinary use the appropriate window is narrower than that — the timing is set by the half-life and infusion time of the agent chosen and is stated in the schedule. Administration after incision is recorded as a missed dose, not as a late dose;
- the dose is weight-adjusted where the schedule requires;
- an intra-operative repeat dose is given where the operation exceeds two half-lives of the agent, or where blood loss is substantial, and the schedule states the interval for each agent;
- prophylaxis is stopped at the end of the operation. It is not continued into the post-operative period, and it is not continued because a drain is in place. Where a surgeon judges that continuation is clinically necessary in an individual case, the reason is recorded in the case record and the case is reviewed by the antimicrobial stewardship arrangement of {{HOSPITAL_NAME}};
- prophylaxis is distinguished in the prescription from treatment of an established infection, so that the two are not conflated on audit.

Timing, agent and duration are recorded for every operation and are audited. Compliance with the prophylaxis element is reported to both the Infection Prevention and Control Committee and the antimicrobial stewardship arrangement, since it is simultaneously an infection prevention measure and the largest single item of antimicrobial use in most surgical hospitals.""",

"""20. Surgical site infection — the operating room

Within the operating room at {{HOSPITAL_NAME}}:

- surgical hand preparation is performed by every member of the scrubbed team before the first procedure of the list and before each subsequent procedure, using either an appropriate antimicrobial soap and running water or an alcohol-based surgical handrub, following the technique and for the duration specified by the product;
- nails are kept short, and artificial nails, nail extensions, nail polish, rings, wrist watches and bracelets are not worn by scrubbed staff;
- the surgical site is prepared with an alcohol-based antiseptic solution, chlorhexidine gluconate based where not contraindicated, applied and allowed to dry fully before draping and before the use of any ignition source such as diathermy;
- sterile gowns and gloves are worn by the scrubbed team; double gloving is used where the risk of perforation is high, and gloves are changed when perforated, contaminated, or at defined points in an implant procedure;
- instruments, implants and supplies are sterile, and their sterility is confirmed at the point of use by checking the indicator and the pack integrity, in accordance with the sterilisation and disinfection policy;
- traffic through the theatre is kept to the minimum necessary, doors are kept closed, and the number of people present is limited to those required, because both the pressure regime and the airborne particle count depend on it;
- theatre ventilation, air quality, temperature, humidity and pressure differentials are maintained and validated under the support services policy, and are not restated here. That policy requires unidirectional downward airflow over the operating table, and nothing in this policy qualifies, weakens or displaces that engineering requirement. What this policy adds is narrower: {{HOSPITAL_NAME}} does not claim ultra-clean or laminar flow ventilation as a surgical site infection prevention measure, and does not rely on it in place of the bundle elements set out above. The engineering requirement stands and is met; the infection-prevention claim is not made, because the guidance on laminar flow as an intervention against surgical site infection — particularly in joint replacement — is not settled;
- wound irrigation before closure, and the use of any antimicrobial agent for it, is [Hospital to define]; antimicrobial sealants are not used;
- the use of triclosan-coated sutures is [Hospital to define].

Where an operation is contaminated or dirty, the procedure is scheduled and the theatre is cleaned in accordance with the support services policy; the practice of listing such cases last is a matter of theatre management and is not by itself an infection control measure.""",

"""21. Surgical site infection — physiological control during surgery

Three physiological variables during surgery affect whether the wound becomes infected, and all three are the anaesthetist's responsibility at {{HOSPITAL_NAME}} in conjunction with the surgical team:

- Temperature. Normothermia is maintained throughout the peri-operative period. The patient is warmed actively where the duration or nature of the operation makes hypothermia likely, warmed intravenous fluids are used where indicated, and core temperature is monitored and recorded. Hypothermia causes vasoconstriction, reduces tissue oxygen delivery to the wound and impairs immune function, and it is both common and easily missed.
- Glycaemia. Blood glucose is monitored and controlled during and immediately after surgery in both diabetic and non-diabetic patients undergoing major procedures. The target range and the protocol adopted by {{HOSPITAL_NAME}} are [Hospital to define], set so as to avoid hypoglycaemia, which carries its own serious risk.
- Perfusion and oxygenation. Adequate circulating volume and tissue perfusion are maintained; goal-directed fluid therapy is used where the patient and procedure warrant it. The inspired oxygen concentration maintained during general anaesthesia with a secured airway, and in the immediate recovery period, is [Hospital to define]; the guidance on raised inspired oxygen as a surgical site infection measure has been revised since it was first issued and {{HOSPITAL_NAME}} records the position it has adopted and the source relied on, in accordance with step 1.

Each of the three is recorded on the anaesthetic record, and the records form part of the surgical site infection bundle audit at step 23.""",

"""22. Surgical site infection — after the operation

The wound is covered at the end of the operation with a sterile dressing, which remains undisturbed for the period specified by the surgeon, conventionally the first 24 to 48 hours for a wound closed primarily, unless it becomes soaked, soiled or displaced.

Thereafter:

- dressings are changed using aseptic non-touch technique, with hand hygiene before and after and appropriate personal protective equipment;
- where a patient has more than one wound, or where several patients are dressed in sequence, the order runs from clean to contaminated and hand hygiene is performed between each;
- the wound is assessed at each dressing change against a defined description — erythema, swelling, tenderness, warmth, discharge and its character, and wound edge separation — and the assessment is recorded rather than summarised as "dressing done";
- advanced or antimicrobial dressings are not used routinely in place of a standard sterile dressing on a primarily closed wound;
- drains are placed only where indicated, are managed as closed systems, and are removed as soon as the indication ends; a drain is not left in as a reason to continue antimicrobials;
- the patient and, where appropriate, the family are instructed before discharge in wound care, in what an infected wound looks like, and in exactly whom to contact and how — and the instruction is given in a language they read and is recorded as given.

Post-discharge follow-up. Most surgical site infections present after the patient has left. {{HOSPITAL_NAME}} therefore follows up operated patients for the period defined in the surveillance policy — conventionally 30 days from the procedure, and longer where an implant was placed — through a defined mechanism of [Hospital to define — for example a follow-up outpatient appointment, a structured telephone call, or a review of readmissions and outpatient wound attendances]. Any infection identified is notified to the Infection Control Team. Without post-discharge follow-up a hospital's surgical site infection rate is not low; it is merely unobserved, and this policy does not permit that to be reported as success.""",

"""23. Measuring whether the preventive actions are actually being performed

Steps 2 to 22 are worth nothing unless they happen. {{HOSPITAL_NAME}} therefore measures compliance directly rather than inferring it from infection rates, and treats compliance measurement as the process indicator this policy owns.

Compliance is measured by:

- direct observation of insertion procedures against the insertion checklist, by a trained observer;
- audit of the daily maintenance records — the catheter review, the ventilator care chart, the line necessity review, the dressing record, the anaesthetic record and the prophylaxis record — against the bundle elements;
- observation of practice at the bedside by the Infection Control Nurse, independent of the department being audited.

Scoring is all-or-none, as set out in step 1. The compliance rate for a bundle is the number of patient-days or procedures on which every applicable element was performed, divided by the number observed, expressed as a percentage. Element-level rates are also calculated, because they identify which element is failing; the all-or-none rate is what is reported as the bundle result.

The audit interval and sample size for each bundle are [Hospital to define], set so that the sample is large enough to be meaningful in a hospital of this size rather than copied from a larger institution's protocol.

Results are fed back to the department concerned within [Hospital to define] of the audit, at the level of the team rather than the individual, except where an individual practice problem requires it to be addressed with that person by their head of department. Results are tabled at the Infection Prevention and Control Committee alongside the infection rates produced under the surveillance policy, so that compliance and outcome can be read together.

Where compliance falls below the threshold set by {{HOSPITAL_NAME}} of [Hospital to define], a recorded corrective action with a named owner and a date follows, and a re-audit confirms the correction. A compliance figure reported without a corrective action attached to it is an observation, not a quality process.""",

"""24. Occupational health — the arrangement and the staff health record

{{HOSPITAL_NAME}} maintains an occupational health arrangement for its workers. In a hospital of this size that is unlikely to be a department, and it is not required to be: it is a named person with defined responsibility, defined time, and access to the clinical services needed to discharge it. The occupational health responsibility at {{HOSPITAL_NAME}} rests with [Hospital to define], who reports to [Hospital to define] and who has direct access to the head of the institution on matters of worker health.

A staff health record is maintained for every worker within the scope of this policy. It contains the pre-placement assessment, immunisation status and dates, results of any periodic assessment, records of occupational exposure and its management, records of work restriction, and any relevant fitness determination.

The staff health record is confidential clinical information. It is held separately from the personnel and disciplinary file, is accessible only to the occupational health responsible person and to those they authorise for a specific clinical purpose, and is not shared with a worker's line manager. What a manager receives is a fitness determination — fit, fit with restriction and what the restriction is, or not currently fit for a stated period — and never the underlying clinical detail or diagnosis.

This separation is stated in strong terms because the occupational health function fails immediately if workers believe it reports to their supervisor. A worker who conceals a diagnosis, an exposure or a symptom because they fear it will reach their manager is a risk to patients that no amount of policy elsewhere will offset.

Records are retained for the period defined by {{HOSPITAL_NAME}} of [Hospital to define], having regard to the long latency of some occupational infections, and are disposed of securely.""",

"""25. Occupational health — assessment at placement and thereafter

Every worker within the scope of this policy undergoes a health assessment before, or at the point of, first placement in a role involving patient contact or exposure to blood, body fluids, biomedical waste, soiled linen or food. This applies equally to contracted and outsourced personnel; where a contractor performs the assessment, {{HOSPITAL_NAME}} obtains and retains confirmation that it was done and that the worker is fit for the role.

The pre-placement assessment establishes:

- the worker's immunisation history and current immune status for the vaccine-preventable diseases relevant to the role;
- any existing condition relevant to fitness for the role or requiring accommodation;
- for staff who will work in areas of higher exposure, a baseline assessment against which any later occupational illness can be compared;
- for food handlers, fitness under the arrangements in the support services policy.

Periodic reassessment is carried out at an interval of [Hospital to define], and additionally on return from a prolonged illness, after a significant occupational exposure, on transfer to a role with materially different exposure, and where a worker or their manager raises a concern about fitness.

Assessment is conducted by [Hospital to define] and its cost is borne entirely by {{HOSPITAL_NAME}}. A worker is not asked to arrange or pay for a pre-placement or periodic assessment required by this policy.

The outcome recorded and communicated is a fitness determination as described in step 24. Where a restriction is determined, it states what the worker may not do and for how long, and it is reviewed at the stated date rather than left standing indefinitely.""",

"""26. Occupational health — immunisation of staff

{{HOSPITAL_NAME}} offers immunisation to its workers according to the exposure their work involves. Immunisation is offered, recorded, and provided free of charge. It is not made a condition of employment except where {{HOSPITAL_NAME}} has determined and recorded that it must be for a specific role, and a worker who declines is asked to record the declination in writing so that the offer and the response are both documented.

Hepatitis B is the immunisation that matters most in a hospital, and it is handled as follows:

- offered to every worker with any reasonably foreseeable exposure to blood or body fluids, including housekeeping, laundry, waste handling, mortuary and biomedical engineering staff, and to students and trainees before clinical attachment begins;
- given as a three-dose intramuscular course into the deltoid at zero, one and six months;
- followed by testing for antibody to hepatitis B surface antigen one to two months after the final dose, with a result of 10 milli-international units per millilitre or above taken as protective;
- where the response is inadequate, a repeat course is given and the worker retested. A worker who does not respond after a second complete course is recorded as a non-responder and is managed as susceptible, which means they will require hepatitis B immunoglobulin after a significant exposure regardless of vaccination history. The worker is told this, in terms, because it changes what they must do if exposed;
- the vaccination dates and the antibody result are entered in the staff health record, and the worker is given their own copy.

Other immunisations offered by {{HOSPITAL_NAME}}, in line with national policy and the role concerned, are [Hospital to define], and typically include influenza; tetanus and diphtheria containing vaccine, particularly for staff handling biomedical waste and sharps; and evidence of immunity to measles, mumps, rubella and varicella for staff in contact with patients. Typhoid immunisation for food handlers is provided under the support services policy.

Immunisation status is reviewed at the periodic assessment and when a worker changes role.""",

"""27. Occupational health — the worker who is infected: reporting and work restriction

A worker at {{HOSPITAL_NAME}} who has, or believes they may have, an infection transmissible to patients or colleagues reports it — to the occupational health responsible person, or to their head of department, on the day it arises and before starting work.

{{HOSPITAL_NAME}} accepts that this only happens if the consequence of reporting is manageable. It therefore undertakes that a worker who reports an infection and is restricted or excluded from work as a result does not lose pay for the period of that restriction, and that the restriction is not recorded as a disciplinary or attendance matter. Where a contractor's staff are affected, {{HOSPITAL_NAME}} requires the same treatment through the contract. A hospital that docks the pay of a worker who reports diarrhoea has, in practice, instructed its workers not to report diarrhoea.

Work restriction is determined by the occupational health responsible person against the written schedule of {{HOSPITAL_NAME}}, which is [Hospital to define] and which is based on recognised guidance on work restrictions for healthcare personnel with communicable conditions. The schedule states, for each condition, whether the worker is excluded from work altogether, restricted from patient contact, restricted from contact with particular patient groups such as the immunocompromised or the newborn, or restricted from food handling — and for how long, measured from a defined point such as the onset of symptoms or the resolution of fever.

The conditions the schedule covers include at minimum: acute gastroenteritis and any diarrhoeal illness; acute respiratory infection with fever; conjunctivitis; herpetic lesions on the hands; draining or infected skin lesions; group A streptococcal infection; the exanthematous illnesses to which staff may be susceptible; active pulmonary tuberculosis; and infestation with scabies or head lice.

A worker restricted from patient contact is assigned to suitable alternative work where such work exists and the restriction permits it, rather than simply sent home, provided this does not defeat the purpose of the restriction.""",

"""28. Occupational health — protecting the worker at the point of work

The practices that prevent an exposure — hand hygiene, standard and transmission-based precautions, personal protective equipment, safe injection and infusion practice and sharps handling — are set out in the infection prevention and control practices policy. What this policy adds is the employer-side obligation to make them possible.

{{HOSPITAL_NAME}} accordingly:

- provides personal protective equipment appropriate to the exposure, in the sizes its workers actually need, at the point of work and in sufficient quantity that no worker is placed in the position of proceeding without it or delaying care to find it;
- provides sharps containers that are puncture-proof, leak-proof and closable, at the point of use, and replaces them before they are overfilled;
- adopts safety-engineered sharps devices where they are available and suitable, and records the assessment where it decides not to;
- provides respiratory protection for staff working with patients on airborne precautions, together with a respiratory protection programme covering the selection of the respirator, fit-testing at an interval of [Hospital to define] and on any change of make or facial change, and instruction in the user seal check performed before every use;
- provides adequate hand hygiene facilities and skin care products, and manages occupational dermatitis, since damaged skin both harbours organisms and deters hand hygiene;
- identifies and manages latex sensitivity, providing alternatives to workers affected;
- ensures that staffing levels and workload permit the precautions to be performed. Where the Infection Control Team judges that workload is defeating compliance in a particular area, it reports that to the Infection Prevention and Control Committee and to management as an infection control finding, not as a human resources matter.

Training in all of the above is delivered under step 30 and recorded.""",

"""29. Occupational health — workers at particular risk

Some workers carry a risk different from that of their colleagues, and {{HOSPITAL_NAME}} accounts for it rather than applying a single rule to everyone.

A worker who is pregnant, is immunocompromised, is receiving immunosuppressive therapy, or is susceptible to a specific infection may request an assessment of their work assignment, and {{HOSPITAL_NAME}} may also initiate one. The assessment is confidential, is made by the occupational health responsible person, and results in a fitness determination as described in step 24, with any resulting reassignment made without loss of pay or standing.

In particular:

- a worker without evidence of immunity to measles or varicella is not assigned to the care of a patient with, or suspected of, those infections where an immune worker is available;
- a worker who is pregnant is counselled on the specific risks relevant to their assignment and on the precautions that address them, and reassignment is considered where the risk cannot be adequately controlled;
- a worker who is immunocompromised is counselled on their own risk from patients with transmissible infection and their assignment adjusted where indicated.

The disclosure of pregnancy, immune status or any condition for the purpose of such an assessment is confidential to occupational health under step 24, and no worker is required to disclose to their manager in order to obtain the assessment.

A worker who is themselves infected with a bloodborne virus is not excluded from work at {{HOSPITAL_NAME}} on that ground. Their fitness for exposure-prone procedures, if any form part of their role, is assessed individually and confidentially against national guidance, and the outcome is a fitness determination and nothing more. No worker's bloodborne virus status is disclosed to colleagues, to managers, or to patients.""",

"""30. Occupational health — training, competence and cost

Every worker within the scope of this policy is trained at induction, before first unsupervised exposure, in: the standard precautions relevant to their role; the personal protective equipment they must use and how to use it; safe handling and disposal of sharps and biomedical waste; the immunisation available to them; what constitutes an occupational exposure; and exactly what to do in the first minutes after one — which they should be able to state without reference to a document.

Training is repeated at an interval of [Hospital to define] and additionally on any change of role or of procedure, and after any exposure incident in the area concerned.

Training is delivered in a language the worker reads and understands. For housekeeping, laundry, waste handling, kitchen, mortuary and security staff — who carry substantial exposure and frequently the least formal education — training is delivered practically and in the vernacular, and its effectiveness is checked by asking the worker to demonstrate rather than by collecting a signature on an attendance sheet.

Attendance and the competence assessment are recorded. Contracted and outsourced staff are trained on the same basis; where a contractor delivers the training, {{HOSPITAL_NAME}} specifies the content, verifies delivery, and retains the record.

The exposure reporting route — who to call, at what number, at any hour — is displayed at every clinical area, treatment room, laboratory, sluice, waste holding area and laundry of {{HOSPITAL_NAME}}, and is included on the identity card or in the induction pack given to each worker.

All costs arising under steps 24 to 36 — assessment, immunisation, testing, prophylaxis, treatment and follow-up — are borne by {{HOSPITAL_NAME}}. No part of the cost is recovered from a worker, whether employed, contracted or a student on attachment.""",

"""31. Occupational exposure — first aid in the first minutes

An occupational exposure means a percutaneous injury from a needle or other sharp, contact of blood or other potentially infectious material with a mucous membrane, or contact with non-intact skin. Saliva, sweat, tears, urine, faeces and vomit are not treated as infectious for bloodborne virus purposes unless visibly bloodstained.

Immediately on exposure, the worker stops what they are doing — the task is handed over, not completed first — and:

- for a percutaneous injury, washes the site with soap and running water. The wound is not squeezed, not scrubbed, and not sucked, and no caustic agent, bleach, antiseptic or disinfectant is applied to it. Squeezing and caustics damage tissue and have no benefit;
- for a mucous membrane exposure, irrigates the eye, mouth or nose with copious clean water or normal saline for several minutes. The eye is irrigated with the eyelids held open; contact lenses are removed after irrigation begins, not before, and are then cleaned or discarded;
- for exposure of non-intact skin, washes with soap and running water without scrubbing.

Eye irrigation facilities or sterile saline are available at [Hospital to define], and their availability is checked at an interval of [Hospital to define].

The worker then reports immediately as set out in step 32. First aid is the first action and reporting the second, but the interval between them is minutes, not hours: for some prophylaxis the value falls measurably with every hour of delay, and a worker who completes their shift before reporting may have lost the opportunity.""",

"""32. Occupational exposure — reporting and risk assessment

Reporting is available at every hour of every day. {{HOSPITAL_NAME}} designates a person to receive exposure reports and a deputy, and the arrangement for nights, weekends and holidays is [Hospital to define]. Reporting does not wait for the next working day.

The designated person records the exposure on the occupational exposure form of {{HOSPITAL_NAME}} and conducts a risk assessment covering:

- the date, time and place of the exposure and the activity in progress;
- the type of exposure — percutaneous, mucous membrane, or non-intact skin — and, for a percutaneous injury, the device involved, whether it was hollow-bore, its gauge, the depth of injury, whether blood was visible on the device, and whether the device had been in the source patient's artery or vein;
- the material involved and its volume, and the duration of contact for a mucosal exposure;
- the exposed worker's hepatitis B immunisation status and, if known, their antibody status;
- the identity and, where known, the infection status of the source patient;
- the immediate first aid actually performed;
- the circumstances that produced the exposure — including whether a safety device was available, whether it was activated, whether a sharps container was within reach and not overfilled, whether recapping was involved, and whether workload or staffing contributed.

The last of these is the item most often omitted and the only one that prevents the next exposure. It is recorded even where the answer is unflattering to the hospital.

The assessment is completed at the time of report and drives the decisions at steps 33 to 36. A decision on human immunodeficiency virus prophylaxis is not deferred pending completion of the paperwork; the clinical decision is taken first and documented immediately after.""",

"""33. Occupational exposure — testing the source and the exposed worker

Source patient. Where the source is known, the source patient is approached for testing for human immunodeficiency virus, hepatitis B surface antigen and hepatitis C antibody. Testing is performed only with the source patient's informed consent, given after pre-test information, and the result is confidential to them. It is disclosed to the exposed worker only to the extent necessary to manage the exposure, and the source patient's identity is not recorded on any document that travels with the worker's own results.

The source patient is not tested without consent, is not pressured, and is not treated differently in any respect if they decline. Where consent is refused or the source is unknown, the exposure is managed on the assessed risk as though the source were positive, if the assessment so indicates. The decision on prophylaxis is not held up waiting for a source result, and never held up beyond the window in which prophylaxis is effective.

Exposed worker. The exposed worker is offered baseline testing for human immunodeficiency virus, hepatitis B surface antigen and antibody, and hepatitis C antibody, with their informed consent and with pre- and post-test counselling. Baseline testing establishes the worker's status at the time of exposure, which matters both clinically and, should the question later arise, for the worker's own protection.

Confidentiality. Testing for human immunodeficiency virus in India is governed by statute, and informed consent, pre- and post-test counselling and confidentiality are legal requirements rather than good practice. {{HOSPITAL_NAME}} complies with the applicable law and with the national programme's requirements, and the identity of any person tested under this policy is not disclosed to their manager, their colleagues, or any other person without their written consent.

Testing is performed at the cost of {{HOSPITAL_NAME}} and at [Hospital to define — the laboratory or integrated counselling and testing centre used, and the arrangement out of hours].""",

"""34. Post-exposure prophylaxis — human immunodeficiency virus

Where the risk assessment at step 32 indicates it, post-exposure prophylaxis against human immunodeficiency virus is started as soon as possible after the exposure. Time is the governing consideration:

- the first dose is given as soon as possible, ideally within hours of the exposure, and preferably within two;
- prophylaxis is not started beyond 72 hours after the exposure, after which it is not considered effective;
- the first dose is not delayed to await the source patient's test result, expert advice, or counselling. Where indicated, the first dose is given and the regimen is reviewed once the result and advice are available, including discontinuation if the source proves negative.

To make this possible, {{HOSPITAL_NAME}} keeps a starter supply of the prophylaxis regimen physically available on the premises at all hours, at [Hospital to define], with the stock and its expiry checked at an interval of [Hospital to define]. A regimen that must be fetched from a pharmacy that is closed is not available.

The regimen used is that specified by the national programme, is prescribed by [Hospital to define], and is taken for 28 days. The worker is counselled on the regimen, its adverse effects, the importance of completing the course, and the interactions to avoid, and is reviewed for tolerance and adherence during the course.

Where expert advice is required — in pregnancy, in the presence of comorbidity or interacting medication, where the source is known or suspected to carry resistant virus, or where the exposure is unusual — {{HOSPITAL_NAME}} obtains it from [Hospital to define], and does so in parallel with starting the first dose rather than instead of it.

A worker may decline prophylaxis after counselling. The declination and the counselling given are recorded, the worker is told they may change their mind within the 72-hour window, and follow-up under step 36 continues regardless.""",

"""35. Post-exposure prophylaxis — hepatitis B, and the management of hepatitis C

Hepatitis B. Prophylaxis is determined by the exposed worker's vaccination and antibody status together with the source's hepatitis B surface antigen status, and is directed by the schedule adopted by {{HOSPITAL_NAME}}, which follows recognised national guidance and is [Hospital to define]. The principles applied are:

- prophylaxis is started as soon as possible and ideally within 24 hours. Its effectiveness after a percutaneous exposure is not established beyond about seven days, so a delayed report is managed urgently rather than treated as too late to act;
- a worker known to have responded to vaccination requires no prophylaxis;
- an unvaccinated or incompletely vaccinated worker is started on, or completes, the vaccine course, and receives hepatitis B immunoglobulin where the source is positive or of unknown status with risk factors;
- a documented non-responder — see step 26 — is managed as susceptible and receives immunoglobulin, and a second dose where indicated, irrespective of having completed a vaccine course;
- where hepatitis B immunoglobulin and vaccine are both given, they are administered at separate anatomical sites.

Hepatitis C. There is no vaccine against hepatitis C and no post-exposure prophylaxis for it. Antivirals are not given prophylactically and immunoglobulin has no role. Management is therefore baseline testing, structured follow-up testing under step 36 to detect seroconversion early, and prompt referral for assessment and treatment if it occurs — treatment which is now highly effective, which is the reason follow-up matters rather than being a formality.

The worker is told plainly at the outset which of the three viruses can be prevented after exposure and which cannot, because a worker who believes hepatitis C is being prevented by the tablets they are taking will not attend for the follow-up test that actually protects them.""",

"""36. Occupational exposure — other exposures, follow-up and counselling

Other exposures. This policy also governs exposures that are not bloodborne:

- exposure to a patient later found to have infectious pulmonary tuberculosis — contact staff are identified, assessed and managed under the arrangement of {{HOSPITAL_NAME}}, which is [Hospital to define];
- exposure to meningococcal disease, pertussis and other conditions for which chemoprophylaxis of close contacts is indicated — managed against the schedule at [Hospital to define];
- an animal bite or scratch sustained on the premises — managed under the rabies prophylaxis arrangement of {{HOSPITAL_NAME}}, which is [Hospital to define];
- tetanus prophylaxis is considered for any contaminated or penetrating wound, against the worker's immunisation record.

Follow-up. The exposed worker is followed up on a defined schedule of clinical review, counselling and serological testing, running to the end point set by {{HOSPITAL_NAME}} of [Hospital to define], which is set against current national guidance for each virus and takes account of the testing technology in use. Follow-up appointments are arranged for the worker rather than left to them to remember, and non-attendance is followed up actively.

Interim advice. Until follow-up is complete, the worker is counselled on precautions during the follow-up period, covering the avoidance of blood, plasma, organ, tissue and semen donation; barrier precautions in sexual contact; and, where relevant, advice on breastfeeding and on pregnancy. Advice is given in a manner that does not disclose the worker's situation to anyone else.

Support. Occupational exposure is frightening, and the anxiety is frequently out of proportion to the measured risk but is not thereby unreasonable. {{HOSPITAL_NAME}} provides counselling and, where needed, referral to appropriate support, for the duration of the follow-up period and beyond it where required.

Confidentiality. Everything recorded under steps 31 to 36 is confidential clinical information held under step 24. The fact of a worker's exposure, the source's identity and status, and any test result are not disclosed to colleagues or managers.""",

"""37. Records, indicators and reporting to the Committee

The records generated under this policy are:

- catheter insertion and daily review records; ventilator care charts; central line insertion checklists, dressing and hub care records and line necessity reviews; surgical safety checklists, prophylaxis timing and duration records, anaesthetic temperature and glycaemia records, and wound assessment records;
- bundle compliance audit reports and the corrective actions arising from them;
- staff health records, immunisation registers and fitness determinations;
- work restriction records;
- occupational exposure reports, risk assessments, prophylaxis given or declined, and follow-up completion;
- training attendance and competence assessment records.

Retention is for the period defined by {{HOSPITAL_NAME}} of [Hospital to define], subject to any longer period required by law, and having regard to the long follow-up horizon of occupational bloodborne virus exposure. Staff health and exposure records are held under the confidentiality terms of step 24 and are not merged into personnel files.

Reporting to the Infection Prevention and Control Committee is at an interval of [Hospital to define] and covers, at minimum:

- bundle compliance rates for each of the four infections, all-or-none and by element;
- corrective actions outstanding from previous audits;
- the number of occupational exposures, by area, by staff category and by mechanism, together with the proportion reported within one hour and within 24 hours;
- the proportion of exposures in which prophylaxis was indicated and was started within the required window;
- follow-up completion rates;
- staff immunisation coverage, particularly hepatitis B coverage and documented response;
- training coverage.

A rise in reported exposures is not read by the Committee as deterioration without further evidence; it is at least as likely to indicate improved reporting, which this policy actively seeks. What the Committee examines is the mechanism data at step 32 — whether the same device, the same task, the same area or the same hour of the shift recurs — because that is what identifies a correctable cause.

Infection rates themselves are produced and reported under the surveillance policy and are read alongside these process measures.""",

"""38. Review of this policy

This policy is reviewed by the Infection Prevention and Control Committee at least once every [Hospital to define], and sooner where national or international guidance on any of the four bundles is materially revised, where the national guidance on post-exposure prophylaxis or on staff immunisation changes, where a statutory requirement affecting testing or confidentiality changes, where a cluster or a serious exposure incident exposes a gap, or where {{HOSPITAL_NAME}} begins or ceases to provide a service covered by this policy.

The review specifically checks:

- that the applicability declarations at steps 7 and 12 still reflect the services {{HOSPITAL_NAME}} actually provides, and that any not-applicable position recorded there remains correct and is still signed and dated;
- that the bundle content still matches current guidance, and that each position recorded under step 1 on a contested element has been re-examined against its source;
- that the named responsibilities in this policy still correspond to posts that exist and are filled;
- that this policy and the infection prevention and control practices policy still agree with each other on immunisation and post-exposure management, and that any divergence identified since the last review has been resolved rather than carried forward.

Revisions are approved by the Committee, endorsed by management, and issued with the superseded version withdrawn from every point of use."""
]

RESPONSIBILITY = """The Infection Prevention and Control Committee owns this policy, approves the content of the four care bundles, reviews compliance and exposure data, and escalates unresolved failures and unfunded requirements to management.

The Infection Control Officer approves the clinical content of the bundles against current guidance, records the position adopted where guidance is contested, advises on individual exposure risk assessments, and leads the investigation of any cluster.

The Infection Control Nurse audits bundle compliance independently of the department being audited, observes practice at the bedside, delivers and records training, and is a first point of contact for staff on exposure and prevention questions.

The occupational health responsible person of {{HOSPITAL_NAME}} maintains the staff health records, conducts or arranges pre-placement and periodic assessment, manages the immunisation programme, determines work restrictions and fitness, receives and manages occupational exposure reports, and directs post-exposure prophylaxis and follow-up. This person holds the staff health record confidentially and reports only fitness determinations to managers.

Heads of clinical departments are responsible for their staff performing the bundles, for the daily device reviews being done and recorded in their areas, for releasing staff for training, and for acting on audit findings and corrective actions in their departments.

Nursing in-charges of each area are responsible for the daily catheter, line and ventilator reviews, for the maintenance elements of every bundle, and for ensuring exposure reporting information is displayed and known.

The surgical team — operating surgeon and anaesthetist jointly — is responsible for the surgical site infection bundle, with the surgeon accountable for hair removal, skin preparation, asepsis, wound care and post-discharge follow-up, and the anaesthetist accountable for prophylaxis timing and re-dosing, normothermia, glycaemic control and perfusion.

The intensive care or ward in-charge, where ventilation is provided, is responsible for the ventilator care chart being completed for every patient every day.

The pharmacy of {{HOSPITAL_NAME}} is responsible for maintaining availability of the surgical prophylaxis agents, the post-exposure prophylaxis starter supply and hepatitis B immunoglobulin, and for alerting the occupational health responsible person before any of these expires or falls below its reorder level.

The head of the institution signs the applicability declarations at steps 7 and 12, authorises the insertion observer at step 13 to halt a procedure, and is accountable for the undertaking that no cost under this policy is passed to a worker.

Where a service is outsourced, the contract manager at {{HOSPITAL_NAME}} is responsible for enforcing the occupational health and exposure provisions through the contract, and for obtaining the contractor's records of assessment, immunisation and training.

All staff are responsible for performing the bundle elements applicable to their role, for recording what they have done, for reporting their own transmissible infection, and for reporting every occupational exposure immediately — their own and any they witness."""

REFERENCES = """- National Accreditation Board for Hospitals and Healthcare Providers (NABH), Standards for Small Healthcare Organisations, 3rd Edition — Hospital Infection Control chapter, standard HIC.4.
- Centers for Disease Control and Prevention and the Healthcare Infection Control Practices Advisory Committee, Guideline for Prevention of Catheter-Associated Urinary Tract Infections.
- Centers for Disease Control and Prevention and the Healthcare Infection Control Practices Advisory Committee, Guidelines for the Prevention of Intravascular Catheter-Related Infections.
- Centers for Disease Control and Prevention, National Healthcare Safety Network — ventilator-associated event surveillance definitions, used in this policy only to explain the terms the standard uses; the definitions themselves are applied under the surveillance policy.
- Society for Healthcare Epidemiology of America and Infectious Diseases Society of America, Compendium of Strategies to Prevent Healthcare-Associated Infections in Acute Care Hospitals — the practice recommendations for ventilator-associated pneumonia and ventilator-associated events, catheter-associated urinary tract infection, central line-associated bloodstream infection and surgical site infection.
- World Health Organization, Global Guidelines for the Prevention of Surgical Site Infection, and its subsequent update.
- Centers for Disease Control and Prevention, Guideline for the Prevention of Surgical Site Infection.
- National Centre for Disease Control, Ministry of Health and Family Welfare, Government of India, National Guidelines for Infection Prevention and Control in Healthcare Facilities.
- National AIDS Control Organisation, Ministry of Health and Family Welfare, Government of India, National Technical Guidelines on Anti Retroviral Treatment — post-exposure prophylaxis provisions.
- The Human Immunodeficiency Virus and Acquired Immune Deficiency Syndrome (Prevention and Control) Act, 2017, Government of India — informed consent, confidentiality and non-discrimination in testing.
- Centers for Disease Control and Prevention, guidance on immunisation of healthcare personnel, on post-exposure management of occupational exposure to hepatitis B, hepatitis C and human immunodeficiency virus, and on infection control in healthcare personnel.
- World Health Organization, Guidelines on Core Components of Infection Prevention and Control Programmes — core component on multimodal strategies and on monitoring, audit and feedback.
- Association of Occupational Health Professionals in Healthcare, recommended work restrictions for healthcare workers with communicable diseases.
- Internal documents of {{HOSPITAL_NAME}}: infection prevention and control programme policy, infection prevention and control practices policy, infection prevention and control in support services policy, surveillance policy, sterilisation and disinfection policy, antimicrobial usage policy, surgical prophylaxis schedule, patient safety policy and surgical safety checklist, and the occupational health and post-exposure procedure."""

DISTRIBUTION = """Controlled master copy: Infection Control Team, {{HOSPITAL_NAME}}.

Copies issued to: the office of the head of the institution; the Infection Prevention and Control Committee (all members); the occupational health responsible person; nursing administration; every inpatient ward and critical care and high-dependency area; operating theatre, recovery and procedure rooms; the labour room; emergency and outpatient departments; dialysis and day-care; laboratory; pharmacy; central sterile supply; radiology and interventional areas; housekeeping, laundry, kitchen, waste handling and mortuary supervisors; engineering and biomedical engineering; human resources, for the provisions on cost, pay during work restriction and confidentiality of health records; the contracts or purchase function for onward issue to each outsourced service provider; and the quality or accreditation coordinator.

The current version is available to all staff at [Hospital to define — intranet location or nursing station folder]. Extracts relevant to a specific process — the four bundle checklists, the daily device review prompt, the immediate first aid steps after an exposure, and the exposure reporting contact and number — are displayed as job aids at the point of work, in the languages staff read. The exposure reporting contact is displayed in every clinical area, treatment room, laboratory, sluice, waste holding area and laundry, and is included in the induction pack issued to every worker including contracted staff and students.

Superseded versions are withdrawn from all points of use on issue of a revision, and one dated copy of each is retained by the Infection Control Team."""

ABBREVIATIONS = """Abbreviations already defined in the HIC.1, HIC.2 and HIC.3 master policies are not repeated here. A reader using this document on its own should refer to those policies for the full infection control glossary, including CAUTI, CLABSI, SSI, VAE, VAP, HAI, PEP, PPE, HBIG, anti-HBs, HBV, HCV, HIV, IPC, IPCC, ICN, ICO, ICT, NSI, MDRO, HEPA, AIIR, ICU, OT, SOP, NABH, NCDC, WHO, CDC, NHSN, SHCO and OE.

The following abbreviations are used in this document and are not defined in HIC.1 to HIC.3:

ART — Antiretroviral Therapy
CHG — Chlorhexidine Gluconate
CVC — Central Venous Catheter
FiO2 — Fraction of Inspired Oxygen
HBsAg — Hepatitis B surface Antigen
HFNC — High-Flow Nasal Cannula
IVAC — Infection-related Ventilator-Associated Complication
MBP — Mechanical Bowel Preparation
MRSA — Methicillin-Resistant Staphylococcus aureus
NACO — National AIDS Control Organisation
NIV — Non-Invasive Ventilation
PICC — Peripherally Inserted Central Catheter
PVAP — Possible Ventilator-Associated Pneumonia
SAP — Surgical Antimicrobial Prophylaxis
SAT — Spontaneous Awakening Trial
SBT — Spontaneous Breathing Trial
SHEA — Society for Healthcare Epidemiology of America
VAC — Ventilator-Associated Condition

Any additional abbreviation used locally within {{HOSPITAL_NAME}} is [Hospital to define] and is added to this list at the next revision."""

# Verbatim from the approved HIC.3 master policy -- do not edit. The master template
# boilerplate is shared across the HIC set, so any change belongs in a deliberate pass
# over all of them, not in this file. Verified below against the live HIC.3 row by hash.
DISCLAIMER = """This document is a template prepared for the guidance of {{HOSPITAL_NAME}} and must be reviewed, adapted and formally approved by {{HOSPITAL_NAME}} before use. Every entry marked [Hospital to define] must be replaced with the hospital's own decision; a document issued with those markers left in place is not an approved policy.

Several requirements in this document are statutory rather than advisory — in particular those arising under the Bio-Medical Waste Management Rules, 2016 and the Food Safety and Standards Act, 2006. Statutory requirements change, and State authorities impose additional or stricter conditions. {{HOSPITAL_NAME}} is responsible for verifying the current text of any rule cited here and the conditions attached to its own authorisations and licences; this document does not constitute legal advice.

The clinical and technical content reflects recognised national and international guidance current at the date of preparation. {{HOSPITAL_NAME}} remains responsible for verifying that it is current and consistent with the edition of the accreditation standard against which it is being assessed.

This document is not issued by, endorsed by, or affiliated with NABH, the World Health Organization, the National Centre for Disease Control, the Food Safety and Standards Authority of India, any Pollution Control Board, or any other body named in it. Wording is original; no text has been reproduced from the standards, rules or guidelines referenced."""

# md5 of the live HIC.3 disclaimer with CR stripped, read from shco_policy_masters on
# 2026-08-06. HIC.3 is stored with CRLF paragraph breaks; this file uses LF throughout,
# per the newline="\n" rule in build_hic1.py, so the comparison is line-ending agnostic.
HIC3_DISCLAIMER_MD5_LF = "ae331bb0cb2ca6428d4d1e0800e51e60"

OE_MAPPING = [
    {
        "oe_code": "HIC.4.a",
        "requirement": "Action is taken to prevent urinary tract infection associated with indwelling urinary catheters",
        "steps": "Steps 1-6, 23",
        "evidence": "Written CAUTI insertion and maintenance bundle; recorded indication at insertion in every case record; catheter insertion register with inserter name and competency list; daily catheter review record showing continued indication or removal; nurse-initiated removal protocol where adopted; shift-wise maintenance checklist covering closed system, bag position and meatal hygiene; bundle compliance audit reports (all-or-none and by element) with corrective actions; catheter-day counts handed to surveillance",
        "responsible": "Nursing in-charge of each area for the daily review and maintenance elements, with the treating team accountable for the indication, audited independently by the Infection Control Nurse",
    },
    {
        "oe_code": "HIC.4.b",
        "requirement": "Action is taken to prevent infection-related ventilator-associated complications and ventilator-associated pneumonia",
        "steps": "Steps 1, 7-11, 23",
        "evidence": "Signed and dated applicability declaration recording whether invasive ventilation is provided, or the not-applicable position and its reason, tabled at the IPCC; written VAP bundle; ventilator care chart per patient per day covering head-of-bed elevation, sedation assessment against target, daily sedation interruption and spontaneous breathing trial or recorded contraindication, oral care, cuff pressure measurement and extubation readiness; circuit and condensate management records; humidifier and accessory reprocessing records; weaning protocol; bundle compliance audit reports with corrective actions",
        "responsible": "Intensive care or ward in-charge where ventilation is provided, with the treating intensivist or physician accountable for sedation and weaning decisions; head of the institution signs the applicability declaration",
    },
    {
        "oe_code": "HIC.4.c",
        "requirement": "Action is taken to prevent bloodstream infection linked to intravascular catheters",
        "steps": "Steps 1, 12-16, 23",
        "evidence": "Signed and dated applicability declaration recording whether central venous access is inserted or maintained, or the not-applicable position and its reason; list of operators assessed as competent, with assessment dates; completed central line insertion checklist for every insertion, signed by an observer who is not the operator; written authorisation of the observer to halt a non-emergency procedure; site selection recorded; dressing change and hub care records; administration set change records; daily line necessity review; peripheral cannula inspection and phlebitis scoring records; IPCC minutes recording any escalation decision on second-line measures; bundle compliance audit reports",
        "responsible": "The inserting operator for the insertion bundle and the nursing in-charge of the area for the maintenance bundle, with the Infection Control Officer advising on escalation; head of the institution signs the applicability declaration and the observer authorisation",
    },
    {
        "oe_code": "HIC.4.d",
        "requirement": "Action is taken to prevent infection of the surgical site",
        "steps": "Steps 1, 17-22, 23",
        "evidence": "Written SSI bundle; pre-operative risk assessment in the case record; pre-operative bathing record; hair removal record showing method used, with clippers stocked and razors absent from pre-operative areas; decolonisation protocol and its application records; surgical prophylaxis schedule; per-operation record of prophylaxis agent, dose, administration time relative to incision, intra-operative re-dosing and stop time; completed surgical safety checklist; anaesthetic record showing core temperature and blood glucose; wound assessment records at each dressing change; discharge wound-care instruction record; post-discharge follow-up mechanism and its records to the defined follow-up horizon; bundle compliance audit reports, with prophylaxis compliance also reported to the antimicrobial stewardship arrangement",
        "responsible": "Operating surgeon and anaesthetist jointly, with the surgeon accountable for asepsis, hair removal, wound care and post-discharge follow-up and the anaesthetist accountable for prophylaxis timing, normothermia and glycaemic control",
    },
    {
        "oe_code": "HIC.4.e",
        "requirement": "Occupational health and safety practices are implemented to reduce transmission of microorganisms among healthcare providers",
        "steps": "Steps 24-30, 37",
        "evidence": "Named occupational health responsible person with defined reporting line; confidential staff health records held separately from personnel files; pre-placement assessment records for employed, contracted and student staff; periodic reassessment records; immunisation register with hepatitis B course dates, anti-HBs results and non-responder determinations, and declination records where immunisation was refused; written work restriction schedule and records of restrictions applied, with confirmation that pay was not withheld; respiratory protection programme with fit-test records; PPE and sharps container provision and replenishment records; safety-engineered device assessment; induction and periodic training attendance with competence assessment, including contractor staff; exposure reporting contact displayed at every point of work; evidence that no cost was passed to any worker",
        "responsible": "The occupational health responsible person of {{HOSPITAL_NAME}}, with heads of department accountable for releasing staff and acting on findings, and the contract manager for outsourced personnel",
    },
    {
        "oe_code": "HIC.4.f",
        "requirement": "Appropriate post-exposure prophylaxis is provided to every staff member concerned",
        "steps": "Steps 31-36, 37",
        "evidence": "Written post-exposure procedure with a named designated person and deputy and a documented 24x7 arrangement; occupational exposure report form completed for every exposure, including the risk assessment and the circumstances that produced it; source and exposed-person consent, counselling and testing records held confidentially; HIV PEP starter stock physically on the premises with location, stock and expiry check records; record of time of exposure against time of first dose; 28-day course completion or documented declination after counselling; hepatitis B PEP schedule with vaccine and immunoglobulin administration records showing separate sites; hepatitis C baseline and follow-up testing records; tetanus, rabies and other chemoprophylaxis records; follow-up schedule completion and counselling records; aggregate exposure and PEP indicators reported to the IPCC",
        "responsible": "The occupational health responsible person of {{HOSPITAL_NAME}} and the designated exposure contact (and deputy) available at all hours, with the pharmacy accountable for the availability of the starter supply and immunoglobulin",
    },
]

UNIVERSAL_FACTS_CHECKLIST = """Universal (non-NABH) facts included in this draft, and where each was verified. Check these first.

SOURCE OF THE OE TEXT
0. HIC.4 standard text and all six OEs were read directly from the official NABH SHCO Standards 3rd Edition PDF (nabh-portal-live S3 copy), Chapter 5, printed pages 94-95. All six OEs are Commitment level; none is Core. HIC.4.f alone carries the asterisk, matching doc_required = true in shco_full_oes.
   NOTE ON A DISCREPANCY INSIDE THE PDF: the Summary of Standards (printed p.92) renders the standard as "takes actions to prevent healthcare associated Infections (HAI)", while the Standards and Objective Elements page (printed p.94) renders it "takes actions to prevent OR REDUCE healthcare associated infections (HAI)". The p.94 wording is the operative one and matches shco_full_oes. Reviewer to note.
   The SHCO 3rd Edition standards PDF contains no per-standard interpretation text for any HIC standard — only intent, standards, OEs and a chapter reference list. Nothing was omitted for want of access.

CATHETER-ASSOCIATED URINARY TRACT INFECTION (steps 2-6)
1. Appropriate indications for an indwelling urinary catheter — acute retention or bladder outlet obstruction; accurate output measurement in the critically ill; selected peri-operative use; to assist healing of an open sacral or perineal wound in an incontinent patient; prolonged immobilisation; end-of-life comfort. And the inappropriate uses — as a substitute for nursing care of an incontinent patient, to obtain urine from a patient who can void, and continuation after surgery without indication. Verified against CDC/HICPAC Guideline for Prevention of Catheter-Associated Urinary Tract Infections.
2. Insertion — aseptic technique, sterile equipment, sterile gloves, drape, sponges, antiseptic periurethral cleaning, single-use lubricant sachet; smallest bore that drains adequately; sterile closed drainage established at insertion; catheter secured after insertion. Same source.
3. Maintenance — closed system not broken; catheter AND collecting system replaced as a set aseptically after any disconnection, aseptic breach or leak; unobstructed flow, no kinks; bag below bladder level at all times and never on the floor; emptied regularly with a separate clean container per patient and the spigot not contacting the container; routine meatal hygiene as part of daily bathing; antiseptics NOT applied to the meatus and no antiseptic instillation into bladder or bag; catheters and bags NOT changed at fixed routine intervals; no systemic antimicrobial prophylaxis. Same source.
4. Alternatives and removal — external collection devices for cooperative males without retention or obstruction; intermittent catheterisation; bladder scanning to assess volume and avoid unnecessary catheterisation; reminder systems and nurse-initiated removal protocols. Same source.
5. Specimens and asymptomatic bacteriuria — small volumes aseptically from the sampling port after disinfection using a sterile syringe, larger volumes from the bag; do not screen for or treat asymptomatic bacteriuria (the recognised exceptions, pregnancy and pre-urological-procedure, are pointed to the antimicrobial usage policy rather than restated). Same source.

VENTILATOR-ASSOCIATED PNEUMONIA / IVAC (steps 7-11)
6. The tiered ventilator-associated event framework — a ventilator-associated condition (sustained oxygenation deterioration after stability), an infection-related ventilator-associated complication (that deterioration plus evidence of infection and a new antimicrobial), and possible ventilator-associated pneumonia within it. Described in step 7 in general terms ONLY, to explain what the OE's phrase "infection-related ventilator associated complication" refers to; the actual case definitions are explicitly deferred to the surveillance policy. Verified via CDC NHSN ventilator-associated event surveillance definitions.
7. Prevention elements — prefer non-invasive ventilation or high-flow nasal oxygen where feasible; minimise sedation and target it to a scale; paired daily sedation interruption and spontaneous breathing trial; daily extubation readiness assessment; early mobilisation; head of bed elevated 30-45 degrees; oral care with mechanical cleaning; subglottic secretion drainage tubes for patients expected to need more than 48-72 hours of ventilation; cuff pressure maintained around 20-30 cm H2O measured by manometer; ventilator circuit changed only when soiled or malfunctioning and NOT routinely; condensate drained away from the patient; early enteral nutrition; stress ulcer prophylaxis on assessed risk rather than routinely. Verified via the SHEA/IDSA Compendium of Strategies to Prevent Healthcare-Associated Infections in Acute Care Hospitals (VAP/VAE practice recommendations) and CDC guidance.
   >> DECISION TAKEN 2026-08-06 — CHLORHEXIDINE ORAL CARE IS MANDATED. Guidance here is not uniform. Older bundles specified chlorhexidine mouthwash as standard; the more recent SHEA compendium update stepped back from routine chlorhexidine following evidence of possible harm, while retaining mechanical oral cleaning (toothbrushing) as the element that carries the benefit. Indian practice and most local ICU protocols still specify chlorhexidine.
   On instruction, step 9 now REQUIRES BOTH mechanical cleaning and chlorhexidine gluconate, scored together, with one without the other recorded as the bundle element not performed. The antiseptic agent is no longer a local choice. Only the concentration is left as [Hospital to define], the preparations in common use falling in the 0.12 to 0.2 per cent range; the step also requires an oral non-alcoholic preparation and excludes skin/surgical chlorhexidine from oral use. The divergence between authorities is stated in the step itself, and the hospital records its adopted position and source under the step 1 mechanism, with re-examination at each review under step 38.
   REVIEWER: this is a deliberate departure from the most recent SHEA position. It is defensible and is what most Indian ICUs do, but it should be a conscious choice at approval, not a default.

CATHETER-LINKED BLOODSTREAM INFECTION (steps 12-16)
8. Insertion — hand hygiene; maximal sterile barrier precautions (cap, mask, sterile gown, sterile gloves and a sterile FULL-BODY drape, not a fenestrated towel); skin antisepsis with alcohol-based chlorhexidine gluconate allowed to dry before puncture; ultrasound guidance to reduce attempts; minimum number of lumens; a checklist completed by an observer other than the operator, with authority to halt a non-emergency procedure; catheters placed without full asepsis in an emergency replaced at the earliest safe opportunity. Verified via CDC/HICPAC Guidelines for the Prevention of Intravascular Catheter-Related Infections and the SHEA/IDSA compendium CLABSI recommendations.
9. Site selection — femoral site carries the highest infection risk and is avoided where feasible; subclavian carries the lowest infection risk but higher mechanical risk; vein preservation takes precedence in advanced kidney disease. The draft presents this as a recorded clinical judgement rather than a fixed rule, because the CDC subclavian preference and the mechanical-risk counterargument are both live. Same sources.
10. Dressings — sterile transparent semipermeable dressing, or gauze where bleeding, oozing or diaphoretic; transparent dressings changed at not more than 7 days, gauze at not more than 2 days, either immediately when damp, soiled or loosened; chlorhexidine-impregnated dressings as an escalation measure. Same sources.
11. Hub disinfection — scrub the access port/hub with an appropriate antiseptic and allow to dry before EVERY access. The draft deliberately leaves the agent and the scrub time as [Hospital to define] because published scrub times vary between sources; what it fixes is that scrubbing (not wiping) occurs and that the hub is dry before access. Same sources.
12. Administration sets — continuously used sets containing neither blood, blood products nor lipid replaced no more frequently than every 96 hours and at least every 7 days; blood, blood product and lipid-containing sets within 24 hours; propofol per manufacturer. Verified via CDC intravascular catheter guidelines.
13. Central catheters NOT replaced at routine intervals to prevent infection; guidewire exchange not used for infection prevention, only to replace a malfunctioning catheter at a site not suspected of infection; no routine systemic antimicrobial prophylaxis; antimicrobial-impregnated catheters and lock solutions as second-line escalation only after compliance is measured. Same sources.
   >> DECISION TAKEN 2026-08-06 — ROUTINE PERIPHERAL CANNULA REPLACEMENT AT 72-96 HOURS. CDC's 2011 guideline supports replacing peripheral cannulae in adults no more frequently than every 72-96 hours; more recent trial evidence supports clinically-indicated replacement instead. On instruction, step 16 now sets routine fixed-interval replacement in adults as the policy, with only the exact number of hours left as [Hospital to define] inside the 72-96 band. The band is bounded in both directions: not shortened below 72 hours (which adds cannulations without reducing infection) and not extended beyond 96 hours for an asymptomatic cannula.
   Three points written into the step so the interval is not misread as the whole rule: it governs only a cannula that is still needed and shows no sign of phlebitis or infection; removal on clinical sign, removal at daily review when no longer needed, and replacement of an emergency-inserted cannula all continue to apply regardless of age; and insertion date and time must be recorded on the dressing and in the nursing record, with an undatable cannula treated as due for replacement.
   PAEDIATRIC EXCEPTION RETAINED: routine replacement of an asymptomatic functioning cannula is NOT performed in children, consistent with CDC. Reviewer to confirm this exception is wanted if {{HOSPITAL_NAME}} treats children.

SURGICAL SITE INFECTION (steps 17-22)
14. Pre-operative — pre-operative bathing or showering with plain or antimicrobial soap; hair NOT removed unless it interferes with the operation and then with clippers or depilatory, NEVER a razor, as close to surgery as practicable; nasal mupirocin with or without chlorhexidine body wash for known S. aureus nasal carriers undergoing cardiothoracic and orthopaedic surgery; nutritional support for underweight patients undergoing major surgery; smoking cessation; mechanical bowel preparation NOT used alone, and combined with oral antimicrobials in elective colorectal surgery; shortest feasible pre-operative stay. Verified via WHO Global Guidelines for the Prevention of Surgical Site Infection and CDC's Guideline for the Prevention of Surgical Site Infection.
15. Surgical antimicrobial prophylaxis — administered within 120 minutes before incision with the precise timing governed by the agent's half-life and infusion time; weight adjustment; intra-operative re-dosing where the procedure exceeds two half-lives of the agent or blood loss is substantial; and — stated strongly in both sources — prophylaxis NOT continued after the operation ends, including where a drain is in place. Same sources. The draft deliberately does not name agents or doses; those belong to the hospital's own prophylaxis schedule under the antimicrobial usage policy.
16. Intra-operative — alcohol-based chlorhexidine gluconate skin preparation allowed to dry fully before draping and before any ignition source; surgical hand preparation with antimicrobial soap and water or alcohol-based surgical handrub; no artificial nails, polish or hand jewellery; double gloving where perforation risk is high; normothermia maintained; peri-operative glycaemic control in diabetic AND non-diabetic patients undergoing major surgery, with the target left to the hospital to avoid mandating a range that risks hypoglycaemia; goal-directed fluid therapy; plastic adhesive incise drapes NOT used as a prevention measure; antimicrobial sealants not used; triclosan-coated sutures left as [Hospital to define] (WHO conditional in favour, evidence not strong enough to mandate); wound irrigation left as [Hospital to define] (WHO makes no recommendation for or against saline irrigation and only a conditional statement on povidone-iodine). Same sources.
   >> REVIEWER FLAG — RAISED INSPIRED OXYGEN. WHO originally issued a strong recommendation for 80% FiO2 intra-operatively in intubated adults under general anaesthesia, and subsequently DOWNGRADED it to conditional in its update following re-appraisal of the evidence. The draft therefore leaves the FiO2 as [Hospital to define] and requires the hospital to record the position and source relied on, rather than mandating 80%. Confirm you want it left open.
   >> REVIEWER FLAG — LAMINAR FLOW. WHO issued a CONDITIONAL RECOMMENDATION AGAINST using laminar airflow ventilation to reduce SSI risk in total joint arthroplasty. This runs against widespread belief and against how ultra-clean theatres are often marketed in India. CHECKED AGAINST HIC.3 ON 2026-08-06, AND STEP 20 WAS AMENDED AS A RESULT. HIC.3 step 2 ("Ventilation of operating theatres") positively REQUIRES "unidirectional downward airflow over the operating table from a non-aspirating laminar flow diffuser or ceiling array, at a face velocity of 25 to 35 feet per minute", for both Type A and Type B theatres, per the NABH OT air-conditioning guidelines. The earlier wording of HIC.4 step 20 — "Ultra-clean or laminar flow ventilation is not adopted at {{HOSPITAL_NAME}} on the basis that it prevents surgical site infection" — was strictly correct on a careful parse ("not adopted FOR THAT REASON") but read at a glance as "not adopted", which flatly contradicts HIC.3 and would be read that way by an assessor comparing the two documents.
   Step 20 now states explicitly that HIC.3's engineering requirement stands, is met, and is not qualified or displaced by this policy, and that the only thing HIC.4 declines to do is CLAIM laminar flow as an SSI prevention measure or rely on it in place of the bundle. The two documents no longer collide on any reading. No change was made to HIC.3.
17. Post-operative — sterile dressing on a primarily closed wound left undisturbed for the first 24-48 hours; aseptic non-touch technique at dressing changes; advanced or antimicrobial dressings not used routinely in place of a standard sterile dressing; drains managed as closed systems and removed when the indication ends, and never a reason to continue antimicrobials; post-discharge surveillance to 30 days, extended where an implant was placed. Verified via WHO and CDC SSI guidelines; the follow-up horizon is stated as the surveillance policy's, not fixed here.

OCCUPATIONAL HEALTH (steps 24-30)
18. Hepatitis B immunisation of healthcare personnel — three-dose intramuscular course into the deltoid at 0, 1 and 6 months; anti-HBs tested 1-2 months after the final dose; 10 mIU/mL or above taken as protective; non-response managed by a repeat course and retest, and a documented non-responder managed as susceptible and requiring HBIG after a significant exposure regardless of vaccination history. Verified via CDC hepatitis B vaccine administration and healthcare personnel immunisation guidance. CONSISTENT WITH the HIC.2 approved draft (its checklist items 21-23) — this is the accepted duplication.
19. Work restrictions for healthcare personnel with communicable conditions — exclusion or restriction by condition and for a defined period measured from a defined point. The draft names the conditions to be covered (gastroenteritis, febrile respiratory infection, conjunctivitis, herpetic hand lesions, draining skin lesions, group A streptococcal infection, exanthematous illness, active pulmonary tuberculosis, scabies and head lice) but leaves the schedule itself as [Hospital to define] rather than reproducing a table. Verified via the AOHP recommended work restrictions document and CDC infection control in healthcare personnel guidance.
20. Respiratory protection — fit-testing of the respirator, repeated on change of make or facial change, plus a user seal check before every use. Verified via CDC and OSHA respiratory protection guidance; CONSISTENT WITH the HIC.2 draft's checklist item 14.
21. Non-immune staff not assigned to measles or varicella patients where an immune worker is available. Verified via CDC transmission-based precautions guidance; CONSISTENT WITH HIC.2 checklist item 15.

POST-EXPOSURE MANAGEMENT (steps 31-36)
22. First aid — wash the percutaneous site with soap and running water; do NOT squeeze, scrub or suck the wound; do NOT apply bleach, caustic agents or antiseptic to it; irrigate mucous membranes with copious water or saline; begin eye irrigation before removing contact lenses. Consistent with WHO/CDC occupational exposure management, and consistent with what HIC.2 step 24 already says.
   >> OPEN, AND LOGGED FOR THE RECONCILIATION PASS 2026-08-06 (was HIC.2 checklist flag 27). On review, there is a real if minor substantive point, and it is the SAME in both documents: each groups *antiseptic* with caustic agents and prohibits it outright. CDC's position is narrower and three-part — caustic agents (bleach) are not applied; antiseptic or disinfectant is not INJECTED INTO the wound; and antiseptics generally have no evidence of reducing transmission, which is "not proven useful" rather than "prohibited". No clinical harm either way, since washing is the element that matters, but as written both documents may contradict local practice, povidone-iodine after washing being common in Indian protocols.
   NO FIX DRAFTED, DELIBERATELY. The correction is roughly one sentence in each document and must be worded identically in both; HIC.2 is approved and is not reopened for it now. Recorded in scripts/master-policy-todos.md under the HIC.2/HIC.4 reconciliation pass, to be done after all six HIC standards are drafted. Also logged there: the HIV PEP window differs in emphasis between the two documents (HIC.2 "a few hours / certainly within 24 hours" vs HIC.4 "ideally within hours / preferably within two"), both respecting the 72-hour ceiling.
23. HIV post-exposure prophylaxis — first dose as soon as possible, ideally within hours and preferably within two; not started beyond 72 hours; 28-day course; first dose not delayed for the source result, expert advice or counselling, with the regimen reviewed and stopped if the source proves negative. Verified via CDC/National Clinician Consultation Center PEP guidance and consistent with NACO's national ART guidelines. The specific drug regimen is deliberately NOT named — it is left to the national programme's current specification and to [Hospital to define] — because the national first-line regimen has changed within recent years and naming it would date the document.
24. Hepatitis B post-exposure prophylaxis — started as soon as possible and ideally within 24 hours; effectiveness after percutaneous exposure not established beyond about 7 days; management determined by the exposed worker's vaccination and antibody status against the source's HBsAg status; a documented non-responder receives HBIG regardless of vaccination history; where HBIG and vaccine are given together they go at separate anatomical sites. Verified via CDC occupational HBV post-exposure guidance; CONSISTENT WITH HIC.2 checklist item 25.
25. Hepatitis C — no vaccine and no post-exposure prophylaxis; antivirals not given prophylactically; immunoglobulin has no role; management is baseline plus follow-up testing to detect seroconversion early, with prompt referral for treatment, which is now highly effective. CDC position.
   >> FLAG CLOSED 2026-08-06. HIC.2's checklist item 26 had flagged this as not separately verified and asked the reviewer to confirm. Reviewed against both documents and closed: HIC.2 step 24 and HIC.4 step 35 already agree and both are correct. The flag existed because the point had not been searched in its own right, not because anything looked doubtful. No text change required in either document, and it is NOT part of the HIC.2/HIC.4 reconciliation pass.
   Optional refinement recorded but deliberately not made: HIC.2 says "baseline and follow-up testing" without naming the test, whereas current practice leans on HCV RNA at around 3-6 weeks rather than waiting on antibody, because early detection enables curative treatment. HIC.4 routes this through step 36 with the schedule left as [Hospital to define]. HIC.2 is vaguer, not wrong.
26. HIV testing in India requires informed consent, pre- and post-test counselling and confidentiality as a matter of statute (the HIV and AIDS (Prevention and Control) Act, 2017), not merely as good practice. The draft states the obligation and cites the Act in references but does NOT paraphrase specific sections. Reviewer to confirm the Act's short title and that it remains in force as cited before approval.
27. Follow-up testing schedule after exposure — the draft deliberately does NOT state week counts. Follow-up endpoints differ between HIV, HBV and HCV and depend on the generation of assay in use, and published schedules have shortened as fourth-generation assays became standard. Left as [Hospital to define] against current national guidance. This is a deliberate omission of a number, not an oversight.
28. Interim advice during follow-up — avoid blood, plasma, organ, tissue and semen donation; barrier precautions in sexual contact; advice on breastfeeding and pregnancy. Standard occupational exposure counselling content, consistent with WHO/CDC guidance. Not separately verified in a dedicated search — reviewer to confirm.

DELIBERATELY NOT INCLUDED — checked and judged to belong to other standards:
- HAI surveillance methodology: standard case definitions, numerator and denominator collection, device-day counting, rate calculation, benchmarking and validation. These belong to HIC.5 under SHCO 3rd Edition. This draft covers bundle-compliance measurement only (step 23), which is a process measure HIC.4 owns, and hands infection data to surveillance. The deferred-content tracker has been corrected accordingly: it previously assigned this to CQI.
- Standard precautions, hand hygiene technique, transmission-based precautions, PPE donning and doffing sequence, safe injection and infusion practice, sharps handling technique and blood/body fluid spill management — HIC.2, already drafted and approved. This policy states the employer-side obligation to make those practices possible (step 28) and does not restate the practices.
- Operating theatre ventilation parameters, air changes, pressure differentials, HEPA specification, temperature and humidity, environmental cleaning, terminal cleaning, laundry and biomedical waste — HIC.3, already drafted and approved. Step 20 points to it and does not restate it.
- Instrument reprocessing, sterility assurance, Spaulding classification, indicators and recall — HIC.6, not yet drafted. Steps 10 and 20 point to it.
- Antimicrobial agent selection, the antibiogram, stewardship structure and the surgical prophylaxis schedule's drug content — HIC.2 and the antimicrobial usage policy. Step 19 fixes the timing, duration and audit obligations only.
- Typhoid immunisation of food handlers — HIC.3 support services policy, where it already sits. Step 26 points to it rather than duplicating it.

ACCEPTED DUPLICATION WITH HIC.2 — CONFIRMED BY THE USER 2026-08-06
HIC.4.e and HIC.4.f are the OEs that own staff immunisation and post-exposure prophylaxis, and HIC.4.f is the asterisked OE in the chapter. The approved HIC.2 draft already carries hepatitis B immunisation, anti-HBs testing, HIV and HBV PEP timing, HCV management and exposure first aid as a spillover from HIC.2.d (safe injection). On instruction, HIC.4 carries the FULL occupational health and PEP programme and the approved HIC.2 document has NOT been reopened. The scope section states the division explicitly: HIC.2 governs the practices that prevent an exposure, HIC.4 governs worker health and everything after an exposure occurs. A reconciliation pass across HIC.2 and HIC.4 is recorded in scripts/master-policy-todos.md, to be done after all six HIC standards are drafted.

ABBREVIATIONS HANDLING — DEVIATION FROM HIC.3, ON INSTRUCTION
HIC.3 repeated abbreviations already defined in HIC.1 and HIC.2 (ACH, AIIR, CSSD, HAI, HEPA, HIC, IPC, IPCC, NABH, NCDC, OE, PPE, SHCO, WHO and others). On instruction, HIC.4 lists ONLY abbreviations not already defined in HIC.1-3, with a lead-in line directing a standalone reader to those documents for the rest. Eighteen new abbreviations are added. Reviewer to note that this makes HIC.4 the first of the set not to be self-contained on abbreviations.

DISCLAIMER BLOCK — VERBATIM FROM HIC.3, AND WHAT THAT MEANS
The disclaimer is the approved HIC.3 block reproduced word for word, on instruction (2026-08-06). It is asserted against the live HIC.3 row by md5 at build time, so it cannot drift unnoticed. The only difference from the stored HIC.3 value is line endings: HIC.3 is stored with CRLF paragraph breaks, this file uses LF throughout per the newline="\\n" rule in build_hic1.py, and the hash check strips CR before comparing. Wording is byte-identical.

Two consequences the reviewer should be aware of, neither of which is an error in the draft:
- Paragraph 2 cites the Bio-Medical Waste Management Rules, 2016 and the Food Safety and Standards Act, 2006. Neither bears on HIC.4. The statute that does bear on HIC.4 — the consent, counselling and confidentiality requirements governing HIV testing in India — is therefore NOT named in the disclaimer. It is named in the references list and its obligations are stated in step 33, so the requirement itself is not lost; only the disclaimer's legal-caveat pointer to it is.
- Paragraph 4 names the FSSAI and Pollution Control Boards, which this document does not cite, and does not name the CDC, NACO or SHEA, which it does. The non-affiliation statement is therefore over-inclusive in one direction and under-inclusive in the other.

An earlier revision of this draft adapted both paragraphs to HIC.4's subject matter. That adaptation was reverted on instruction in favour of an identical shared block across the HIC set. If the boilerplate is ever revised, both points above should be picked up in that pass across all six standards rather than in this file alone.

There is no single identical disclaimer across HIC.1-3 as things stand: HIC.1 has three paragraphs, HIC.2 five with a different opening, HIC.3 four. HIC.4 now matches HIC.3. Aligning HIC.1 and HIC.2 to the same block is a separate decision and has not been made here.

HOSPITAL-SPECIFIC VALUES LEFT AS [Hospital to define] — 57 fillable blanks in the rendered document: 50 in the exact form "[Hospital to define]" and 7 in the guidance-bearing form "[Hospital to define — what to state]". A search for the exact string finds 50 of 57; a search for "Hospital to define" without brackets finds all 57, and that is the search a hospital should be told to run. The 7 guidance-bearing ones are deliberate and are retained because the guidance is part of the instruction and is replaced wholesale along with the bracket: the ventilation and central-access applicability declarations (steps 7 and 12), the not-applicable example (step 7), the catheter review reminder mechanism (step 5), the post-discharge follow-up mechanism (step 22), the testing laboratory and its out-of-hours arrangement (step 33), and the intranet location in Distribution.
   Corrected 2026-08-06: an earlier build reported 48. That figure was wrong twice over and the two errors cancelled — it omitted rendered fields (the disclaimer's placeholder was never counted) and it matched only the exact form, so every guidance-bearing placeholder was invisible, including the Distribution one, which was reported as zero. The counter now audits every rendered field in both forms; see policy_placeholder_audit.py.
   Also corrected in the same pass: step 7 previously contained a NESTED placeholder ("...referral arrangement to [Hospital to define]]"), which cannot be replaced as a single unit and leaves a stray closing bracket. The inner one is now plain descriptive text, since it was an example inside guidance that gets replaced wholesale rather than a separate blank. Two placeholders whose guidance merely restated their own sentence — the eye irrigation locations (step 31) and the PEP starter stock location (step 34) — were normalised to the exact form. The build now asserts that no nested placeholder is reintroduced.

The full list of values the hospital must supply: bundle review interval; catheter review reminder mechanism; ventilation applicability declaration and its not-applicable reason and referral destination; oral care frequency; oral chlorhexidine concentration (agent itself is mandated, not optional); cuff pressure check frequency; weaning and extubation protocol; central access applicability declaration and its not-applicable reason; emergency catheter replacement window; hub disinfection agent and scrub time; administration set change interval; phlebitis scale; emergency peripheral cannula replacement window; routine peripheral cannula replacement interval, bounded to the 72-96 hour band; pre-operative glycaemic target; bowel preparation protocol; pre-operative bathing timing; S. aureus screening policy; surgical prophylaxis schedule; wound irrigation policy; triclosan-coated suture policy; intra-operative glycaemic target and protocol; intra-operative FiO2 position; post-discharge follow-up mechanism; bundle audit interval and sample size; feedback turnaround; compliance threshold triggering corrective action; occupational health responsible person and reporting line; staff health record retention; periodic reassessment interval; assessing practitioner; other immunisations offered; work restriction schedule; respirator fit-test interval; eye irrigation facility locations and check interval; out-of-hours exposure reporting arrangement; testing laboratory or ICTC and its out-of-hours arrangement; PEP starter stock location and check interval; PEP prescriber; expert advice source; hepatitis B PEP schedule; tuberculosis contact management arrangement; chemoprophylaxis schedule; rabies prophylaxis arrangement; follow-up endpoint; training interval; record retention period; IPCC reporting interval; intranet location."""

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
# renderer does not emit those headings, matching HIC.1-3.

# newline="\n" is REQUIRED -- see build_hic1.py. Windows CRLF inside the policy text
# breaks the renderer's step regex and silently flattens every step.
with open(DRAFTS / "hic4_draft.json", "w", encoding="utf-8", newline="\n") as f:
    json.dump(draft, f, ensure_ascii=False, indent=2)


def dollar(s, tag="q"):
    assert f"${tag}$" not in s, f"delimiter collision in: {s[:60]}"
    return f"${tag}${s}${tag}$"


def pg_array(items):
    return "array[" + ", ".join("'" + i.replace("'", "''") + "'" for i in items) + "]"


def steps_array(steps):
    return "array[\n    " + ",\n    ".join(dollar(s, "s") for s in steps) + "\n  ]"


sql = f"""-- HIC.4 master policy -- DRAFT for review. Do NOT set status = 'approved' here;
-- approval is a separate manual step after fact-checking.
--
-- Source: NABH SHCO Standards 3rd Edition (August 2022), Chapter 5, printed pages 94-95.
-- All six OEs are Commitment level. HIC.4.f alone carries the asterisk (doc_required = true).
--
-- The five optional sections are deliberately not populated, matching HIC.1-3.

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

with open(SQL_OUT / "hic4_insert.sql", "w", encoding="utf-8", newline="\n") as f:
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

print("mapping covers all 6 OEs:", sorted(m["oe_code"] for m in OE_MAPPING) == sorted(OE_CODES))
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

# The disclaimer must stay byte-identical to the approved HIC.3 block, ignoring line endings.
import hashlib
_d = hashlib.md5(DISCLAIMER.replace("\r", "").encode("utf-8")).hexdigest()
assert _d == HIC3_DISCLAIMER_MD5_LF, f"disclaimer drifted from HIC.3: {_d}"
print("disclaimer verbatim identical to HIC.3 (LF-normalised md5):", _d)
from policy_placeholder_audit import audit
_exact, _variant, _total, _problems = audit(draft)
assert not _problems, _problems
print("wrote hic4_draft.json and hic4_insert.sql")
