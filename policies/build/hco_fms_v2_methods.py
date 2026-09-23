# -*- coding: utf-8 -*-
"""Hospital-facing What-we-do methods for HCO FMS.1–FMS.7.

HCO 6th Edition chapter name is Facility Management and Safety (FMS).
"""
from __future__ import annotations


def method_bodies(*, D, HOSPITAL, BLANK) -> dict[str, str]:
    """Return method body text keyed by oe_code (without the 5.N title)."""
    eng = D("Engineering In-Charge")
    ms = D("Medical Superintendent")
    qc = D("Quality Coordinator")
    monthly = D("monthly")
    yearly = D("annually")
    quarterly = D("quarterly")

    return {
        "FMS.1.a": f"""Patient-safety devices and infrastructure (grab bars, bed rails, stretcher and wheelchair belts, call bells, alarms, radiation or biohazard warning signs, fire-safety devices as listed for each area) are installed across {HOSPITAL} and inspected at a defined interval (default {monthly}).

The {eng} holds the current list and last inspection. A missing device in a care area that is in use is escalated the same shift.""",

        "FMS.1.b": f"""{HOSPITAL} has facilities for the differently-abled (at a minimum a wheelchair-accessible entrance and an adapted toilet, as regulatory requirement and this hospital's building allow).

The {eng} keeps the current access list. A step-only entrance with no documented alternative does not satisfy this element.""",

        "FMS.1.c": f"""Facility inspection rounds to ensure safety are conducted at least once a month using a checklist. Potential safety and security-risk / restricted areas are identified and monitored.

The {eng} owns the round calendar. A month without a completed round is a gap.""",

        "FMS.1.d": f"""Inspection reports of facility rounds are documented. Corrective and preventive measures are undertaken. The safety committee reviews the reports monthly. Pre- and post-correction evidence is kept for at least one accreditation cycle.

The {qc} files the reviewed reports with the {eng}.""",

        "FMS.1.e": f"""Before construction, renovation or expansion of the existing hospital, a risk-assessment is carried out covering noise, vibration and infection prevention and control. IPC.4 remains the home of construction-infection controls; this element is that the assessment happens before work starts.

The {eng} holds the dated assessment. Work started with no assessment does not satisfy this element.""",

        "FMS.2.a": f"""Facilities and space provisions match the scope of services this hospital actually offers, using national or international guidance (including Atomic Energy Regulatory Board guidance where radiation services are in scope).

The {eng} and {ms} keep the current space-vs-services map. A service listed without a matching space is escalated.""",

        "FMS.2.b": f"""As-built and updated drawings are maintained as required by the applicable registering authority for this site: site layout, floor plans, floor-wise fire-evacuation plans, and separate civil, electrical, extra-low-voltage, plumbing, heating-ventilation-air-conditioning, piped medical-gas and information-technology drawings.

A named person under the {eng} holds the current set. This element does not import a named Act as a checklist for the whole standard.""",

        "FMS.2.c": f"""Internal and external sign posting is in a manner patients, families and the community understand (language and/or pictorial; bilingual where this hospital defines). Signs meet applicable statutory posting rules for this site.

The {eng} walks the signs {quarterly}.""",

        "FMS.2.d": f"""Potable water and electricity are available round the clock. Potable-water quality is tested at the tap: biochemical at least once in three months and microbiological at least once a month, against the current IS 10500. Dialysis reverse-osmosis inlet water is tested for endotoxin every month where dialysis is in scope.

A care area without water or power is a stop-work trigger (section 6).""",

        "FMS.2.e": f"""Alternate sources for electricity and water are provided as backup for any failure or shortage (diesel generator, solar, uninterruptible power supply; bore or tanker or extra tanks as this hospital names). Electric load matches demand. National Building Code is a reference for water quantity, not a paste of every clause.

The {eng} owns the backup list. Critical areas have a named continuity action when supply fails.""",

        "FMS.2.f": f"""The organisation tests these alternate sources at a predefined frequency (default {monthly} for the diesel generator and a documented water-acceptance test when an emergency source is used). Results are recorded. Refer to FMS.2.d for water quality.

A backup that is never tested does not satisfy this element.""",

        "FMS.3.a": f"""Operational planning identifies extra-security areas and describes access for staff, patients and visitors (at a minimum operating theatre, intensive-care units including neonatal if in scope, labour room and emergency). Vulnerable spots (dark areas, long corridors, critical-area doors) have a defined control such as closed-circuit television.

Written security guidance exists.""",

        "FMS.3.b": f"""When this hospital plans, designs or constructs a new building, or re-plans or retrofits an existing one, patient-safety structural aspects of critical areas are considered. Indian Seismic Code IS 1893 (Part 1), latest version, is the minimum structural reference named in the Guidebook.

The {eng} files what was applied. This element is evidenced on actual building work, not by a policy sentence alone.""",

        "FMS.3.c": f"""The organisation conducts electrical safety audits of the facility at least once a year to reduce risk to people and property and to prevent fire from short-circuiting. National Electrical Code of India 2023 is a reference. Thermal imaging may be used.

The {eng} holds the last audit and actions.""",

        "FMS.3.d": f"""There is a written procedure for identifying and disposing of material not in use (non-functioning items, excess stock, general scrap). Condemnation records sit with the {eng}.""",

        "FMS.3.e": f"""Hazardous materials used here are identified and used safely: sorting, storage, handling, transport and disposal, using Material Safety Data Sheets. Common examples the Guidebook names include chemicals, blood and cultures, mercury, nuclear isotopes, medical gases, liquefied petroleum gas, steam and ethylene oxide.

Using an unidentified hazardous material is a stop-work trigger (section 6).""",

        "FMS.3.f": f"""The spill plan for hazardous materials is implemented: a summarised Material Safety Data Sheet the floor can read, a hazardous-materials kit where those materials are stored, and trained handlers.

A kit in a locked office the floor cannot reach does not satisfy this element.""",

        "FMS.4.a": f"""The organisation plans utility and engineering equipment to match services and the strategic plan, including future needs (diesel generator, chiller). Plans are implemented and reviewed at a defined interval. Selection, rental, update or upgrade is collaborative (end-user, management, finance, engineering).

The {eng} holds the current plan.""",

        "FMS.4.b": f"""Equipment is inventoried and logs are maintained. Each item has a unique identifier. Quality-conformance certificates, factory test certificates and installation reports are kept where they apply.

A plant item with no identity number does not satisfy this element.""",

        "FMS.4.c": f"""The documented operational and maintenance (preventive and breakdown) plan is implemented for utility and engineering equipment, electrical systems, water, heating-ventilation-air-conditioning, facility and furniture — including transformers, low-tension and high-tension panels, lifts, tanks, reverse-osmosis and sewage-treatment if present, chillers, air-handling units and filters.

Running critical utility equipment with no implemented plan is a stop-work trigger (section 6).""",

        "FMS.4.d": f"""Utility equipment is periodically inspected and calibrated where applicable (for example steam-steriliser pressure gauges, medication-refrigerator temperature gauges), in-house or outsourced, with traceability to prescribed standards.

The {eng} holds the calibration schedule.""",

        "FMS.4.e": f"""Competent personnel (qualification, experience or training) operate, inspect, test and maintain equipment and utility systems. Enough supervisors and tradespeople, including fire-safety and electrical-safety trained staff, plus tools and personal protective equipment, are available.

A plant running with no competent person named for that shift is escalated to the {eng}.""",

        "FMS.4.f": f"""Maintenance staff are contactable round the clock for emergency repairs. An escalation matrix (who to call if the person on duty cannot complete the job) is at the nursing station and departments.

A night call with no answer path does not satisfy this element.""",

        "FMS.4.g": f"""Downtime for critical engineering and utility equipment breakdowns is monitored from reporting to inspection and corrective action. At a minimum the critical list includes diesel generator, lifts, uninterruptible power supply, fire-related equipment, dialysis reverse-osmosis and water pumps. A complaint register records receipt, job allotment and user-ratified completion.

Start of downtime is complaint time; end is user-ratified completion.""",

        "FMS.4.h": f"""Written guidance supports equipment replacement, identification of unwanted material and disposal. Unusable utility and engineering equipment is condemned in a systematic way. Records are kept.""",

        "FMS.5.a": f"""The organisation plans medical equipment to match services and the strategic plan, including future needs. Indian Public Health Standards are a reference for a minimum set. Selection, rental, update or upgrade is collaborative (end-user, management, finance, engineering, biomedical).

The {eng} holds the current medical-equipment plan with the {ms}.""",

        "FMS.5.b": f"""Medical equipment is inventoried and logs are maintained. Items are classified by medical-device risk. Each has a unique identifier, including rental and demonstration items. Factory test and conformance certificates are kept.

An in-use device with no identity does not satisfy this element.""",

        "FMS.5.c": f"""The documented operational and maintenance (preventive and breakdown) plan for medical equipment is implemented: operator training, daily operating checks, preventive-maintenance tracker, and breakdown response including nights and weekends.

Using equipment with no implemented plan is a stop-work trigger (section 6).""",

        "FMS.5.d": f"""Medical equipment that measures is inspected and calibrated on a weekly, monthly or annual schedule as the manufacturer and this hospital define, in-house or outsourced, with traceability. Conformance is checked before commissioning and again after repair.

A measuring device past its calibration due date is a stop-work trigger (section 6).""",

        "FMS.5.e": f"""Qualified and trained personnel operate and maintain medical equipment. Operators are trained for the devices they use (for example blood-gas analyser, electrocardiograph, syringe pump). Maintenance is by a biomedical engineer or technologist, or an instrumentation engineer or technologist, with relevant training and experience.""",

        "FMS.5.f": f"""Written guidance supports medical equipment replacement and disposal. Condemnation is systematic and recorded.""",

        "FMS.5.g": f"""Medical equipment and devices are monitored for adverse events. Hazard notices and recalls from the manufacturer or regulator are acted on at once; the device is not returned to clinical use until the issue is closed. The Guidebook names Gazette of India GSR 78(E) 2023 / Medical Devices Rules 2023 and participation in the Materiovigilance Programme of India. MOM.10 remains the home of medication-supply recall; this element is equipment and devices.

An open recall left in use is a stop-work trigger (section 6).""",

        "FMS.5.h": f"""Downtime for critical medical-equipment breakdown is monitored from reporting to inspection and corrective action. At a minimum the critical list includes ventilators, X-ray, magnetic resonance imaging, catheterisation laboratory, computed tomography, anaesthesia machines, monitors, laboratory and ultrasound — especially where there is no alternative. A complaint register records receipt, job allotment and user-ratified completion.

Start of downtime is complaint time; end is user-ratified completion.""",

        "FMS.6.a": f"""Written guidance governs procurement, handling, storage, distribution, usage and replenishment of all medical gases used here, including colour coding and full/empty signage. HTM 02-01 or the National Fire Protection Association medical-gas handbook is a reference.

The Guidebook names the Explosives Act, Gas Cylinder Rules and Static and Mobile Pressure Vessels (Unfired) Rules. Those duties stay with the named statute; this policy does not paste the Act.""",

        "FMS.6.b": f"""Medical gases are handled, stored, distributed and used safely: colour-coded cylinders and pipelines; alarms and valve boxes; twenty-four-hour monitoring of plant alarms; pin-indexed outlets; automatic change-over to the alternate source.

A live leak or a silenced required alarm is a stop-work trigger (section 6).""",

        "FMS.6.c": f"""There is an operational, inspection, testing and maintenance plan for piped medical gas, compressed air and vacuum, following the manufacturer. Compressed-air purity is checked at a terminal outlet at least once a year, at least one terminal in the operating theatre and one in intensive care if those areas exist.""",

        "FMS.6.d": f"""Alternate sources for medical gases, vacuum and compressed air are provided for failure (stand-by compressor and vacuum pump; stand-by manifold or bulk cylinders).

No required alternate source is a stop-work trigger (section 6).""",

        "FMS.6.e": f"""The organisation tests these alternate sources at a defined frequency (default {monthly}). Results are documented.""",

        "FMS.7.a": f"""{HOSPITAL} has plans and provisions for early detection, abatement, containment of fire and evacuation: a fire plan (inflammable items, explosion, short-circuit, negligence or incompetence), qualified personnel, current NABH minimum fire-safety measures, smoke control, training, mock-drill schedules including table-top, drill records, displayed exits, evacuation of patients, staff and visitors, and emergency illumination.

Occupying a patient-care floor without required detection, abatement or evacuation provision is a stop-work trigger (section 6).""",

        "FMS.7.b": f"""The organisation has plans and provisions for identification and management of non-fire emergencies (examples the Guidebook names include earthquake, flood, toxic leak, structural collapse, utility failure, boiler burst, violence, stray animals). National Disaster Management Authority / State / District guidelines are referred to. Liaison with civil, police and fire authorities is as required by law.

Portal wording "identification, and management" is kept as printed.""",

        "FMS.7.c": f"""A documented exit plan is displayed on each floor, especially near lifts and inside enclosed rooms and laboratories. Exit doors remain open or have push bars. Fire signage follows the fire service and/or National Building Code. Refuge areas are signed and maintained where they apply.

A patient-care floor with no displayed exit plan is a stop-work trigger (section 6).""",

        "FMS.7.d": f"""Mock drills are held at least twice a year (minimum; more often if this hospital defines). This covers fire and the important non-fire events this hospital names. A table-top exercise or a mock drill may be used; at a minimum one mock drill every six months tests the whole plan, not only awareness. Simulated patients, not real patients, are used. Variations are debriefed and corrected.

A year with fewer than two drills is a gap under this element.""",

        "FMS.7.e": f"""There is a maintenance plan for fire-related equipment and infrastructure: inspection, testing, preventive and breakdown maintenance, following the manufacturer and applicable statutory recommendations.

The {eng} holds the plan and last service evidence.""",
    }
