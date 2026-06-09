// ============================================================
// HCO ELC TAB — Add to App.js (accredready.in)
// For Healthcare Organisations with MORE than 50 Sanctioned Beds
// Two modes: ELC Prep + Full Accreditation Prep
// Author: Dr. Mehul Upadhyay | May 2026
// Source: NABH Guidebook on Entry-Level Certification for HCOs/SHCOs
//         + NABH-PROC_ASSESSMENT Issue 5 (Aug 2025)
// ============================================================
// USAGE: Paste this entire file's content into App.js
// 1. Add HCO_ELC_DOCS, HCO_ELC_LICENSES constants (static data section)
// 2. Add hcoElcProgress, hcoLicProgress state variables
// 3. Add '🏨 HCO ELC' to tabs array
// 4. Add renderHCOTab() call in tab render switch
// ============================================================

// ── STEP 1: STATIC DATA (paste near other constants like OE_TIPS) ─────────

const HCO_ELC_DOCS = [
  // ── Part I — General Information ──────────────────────────────────────────
  {id:"001",part:"I",section:"Contact Details",text:"Name of the Hospital",upload:"Portal",type:"field"},
  {id:"002",part:"I",section:"Contact Details",text:"Address",upload:"Portal",type:"field"},
  {id:"003",part:"I",section:"Contact Details",text:"City",upload:"Portal",type:"field"},
  {id:"004",part:"I",section:"Contact Details",text:"State",upload:"Portal",type:"field"},
  {id:"005",part:"I",section:"Contact Details",text:"Name of SPOC (quality coordinator)",upload:"Portal",type:"field"},
  {id:"006",part:"I",section:"Contact Details",text:"SPOC Designation",upload:"Portal",type:"field"},
  {id:"007",part:"I",section:"Contact Details",text:"Contact Number",upload:"Portal",type:"field"},
  {id:"008",part:"I",section:"Contact Details",text:"Email ID",upload:"Portal",type:"field"},
  {id:"009",part:"I",section:"Hospital Information",text:"Certificate validating registered name of the Hospital",upload:"Portal",type:"doc"},
  {id:"010",part:"I",section:"Hospital Information",text:"Registration Certificate (State/Local Statutory Body OR Clinical Establishment Act OR Shop & Establishment Act)",upload:"Portal",type:"doc"},
  {id:"011",part:"I",section:"Hospital Information",text:"Registration Certificate for type of ownership/partnership",upload:"Portal",type:"doc"},
  {id:"012",part:"I",section:"Hospital Information",text:"Certificate under government empanelment scheme (ECHS, CGHS, etc.) if applicable",upload:"Mobile",type:"doc"},
  {id:"013",part:"I",section:"Hospital Information",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"014",part:"I",section:"Hospital Information",text:"Registration Date",upload:"Portal",type:"field"},
  {id:"015",part:"I",section:"Hospital Information",text:"Type of Ownership (Private Corporate / Proprietary / Cooperative etc.)",upload:"Portal",type:"field"},
  {id:"016",part:"I",section:"Hospital Information",text:"Do Patients stay overnight? (Yes/No)",upload:"Portal",type:"field"},
  {id:"017",part:"I",section:"Hospital Information",text:"Upload Registration Certificate (portal)",upload:"Portal",type:"field"},
  // ── Part II — Physical Infrastructure ────────────────────────────────────
  {id:"018",part:"II",section:"Bed Strength",text:"Number of operational beds - Emergency Ward",upload:"Both",type:"field"},
  {id:"019",part:"II",section:"Bed Strength",text:"Number of operational beds - ICU",upload:"Both",type:"field"},
  {id:"020",part:"II",section:"Bed Strength",text:"Number of operational beds - HDU",upload:"Both",type:"field"},
  {id:"021",part:"II",section:"Bed Strength",text:"Number of operational beds - General Ward",upload:"Both",type:"field"},
  {id:"022",part:"II",section:"Bed Strength",text:"Number of operational beds - Private Ward",upload:"Both",type:"field"},
  {id:"023",part:"II",section:"Bed Strength",text:"Number of operational beds - Semi-Private Ward",upload:"Both",type:"field"},
  {id:"024",part:"II",section:"Services Offered",text:"Anesthesia (location)",upload:"Both",type:"field"},
  {id:"025",part:"II",section:"Services Offered",text:"Blood Bank (location)",upload:"Both",type:"field"},
  {id:"026",part:"II",section:"Services Offered",text:"Cardiac OT (location)",upload:"Both",type:"field"},
  {id:"027",part:"II",section:"Services Offered",text:"Cath Lab (location)",upload:"Both",type:"field"},
  {id:"028",part:"II",section:"Services Offered",text:"CCU (location)",upload:"Both",type:"field"},
  {id:"029",part:"II",section:"Services Offered",text:"ICU (location)",upload:"Both",type:"field"},
  {id:"030",part:"II",section:"Services Offered",text:"Labour Room (location)",upload:"Both",type:"field"},
  {id:"031",part:"II",section:"Services Offered",text:"Medical Ward (location)",upload:"Both",type:"field"},
  {id:"032",part:"II",section:"Services Offered",text:"NICU (location)",upload:"Both",type:"field"},
  {id:"033",part:"II",section:"Services Offered",text:"Nuclear Medicine (location)",upload:"Both",type:"field"},
  {id:"034",part:"II",section:"Services Offered",text:"OT (location)",upload:"Both",type:"field"},
  {id:"035",part:"II",section:"Services Offered",text:"Ortho Ward (location)",upload:"Both",type:"field"},
  {id:"036",part:"II",section:"Laboratory Services",text:"Clinical Bio-chemistry Lab — location or MoU (if outsourced)",upload:"Both",type:"field"},
  {id:"037",part:"II",section:"Laboratory Services",text:"Clinical Microbiology & Serology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"038",part:"II",section:"Laboratory Services",text:"Clinical Pathology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"039",part:"II",section:"Laboratory Services",text:"Cytopathology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"040",part:"II",section:"Laboratory Services",text:"Genetics Lab — location or MoU",upload:"Both",type:"field"},
  {id:"041",part:"II",section:"Laboratory Services",text:"Haematology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"042",part:"II",section:"Laboratory Services",text:"Histopathology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"043",part:"II",section:"Laboratory Services",text:"Toxicology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"044",part:"II",section:"Laboratory Services",text:"Molecular Biology Lab — location or MoU",upload:"Both",type:"field"},
  {id:"045",part:"II",section:"Diagnostic Imaging",text:"Bone Densitometry — location or MoU",upload:"Both",type:"field"},
  {id:"046",part:"II",section:"Diagnostic Imaging",text:"CT Scanning — location or MoU",upload:"Both",type:"field"},
  {id:"047",part:"II",section:"Diagnostic Imaging",text:"DSA Lab — location or MoU",upload:"Both",type:"field"},
  {id:"048",part:"II",section:"Diagnostic Imaging",text:"Gamma Camera — location or MoU",upload:"Both",type:"field"},
  {id:"049",part:"II",section:"Diagnostic Imaging",text:"Mammography — location or MoU",upload:"Both",type:"field"},
  {id:"050",part:"II",section:"Diagnostic Imaging",text:"MRI — location or MoU",upload:"Both",type:"field"},
  {id:"051",part:"II",section:"Diagnostic Imaging",text:"Nuclear Medicine — location or MoU",upload:"Both",type:"field"},
  {id:"052",part:"II",section:"Diagnostic Imaging",text:"PET — location or MoU",upload:"Both",type:"field"},
  {id:"053",part:"II",section:"Diagnostic Imaging",text:"Ultrasound — location or MoU",upload:"Both",type:"field"},
  {id:"054",part:"II",section:"Diagnostic Imaging",text:"Urodynamic Studies — location or MoU",upload:"Both",type:"field"},
  {id:"055",part:"II",section:"Diagnostic Imaging",text:"X-Ray — location or MoU",upload:"Both",type:"field"},
  {id:"056",part:"II",section:"Other Services",text:"2D Echo — location or MoU",upload:"Both",type:"field"},
  {id:"057",part:"II",section:"Other Services",text:"Audiometry — location or MoU",upload:"Both",type:"field"},
  {id:"058",part:"II",section:"Other Services",text:"EEG — location or MoU",upload:"Both",type:"field"},
  {id:"059",part:"II",section:"Other Services",text:"EMG/EP — location or MoU",upload:"Both",type:"field"},
  {id:"060",part:"II",section:"Other Services",text:"Holter Monitoring — location or MoU",upload:"Both",type:"field"},
  {id:"061",part:"II",section:"Other Services",text:"Spirometry-PFT — location or MoU",upload:"Both",type:"field"},
  {id:"062",part:"II",section:"Other Services",text:"Tread Mill Testing — location or MoU",upload:"Both",type:"field"},
  {id:"063",part:"II",section:"Utilities & Infrastructure",text:"Electrical supply availability",upload:"Both",type:"field"},
  {id:"064",part:"II",section:"Utilities & Infrastructure",text:"Water supplier details",upload:"Both",type:"field"},
  {id:"065",part:"II",section:"Utilities & Infrastructure",text:"Elevators present? (Certificate of Lift License/Safety via Portal)",upload:"Both",type:"field"},
  {id:"066",part:"II",section:"Utilities & Infrastructure",text:"Water portability certificate (IS 10500:2012 via Mobile App)",upload:"Mobile",type:"doc"},
  {id:"067",part:"II",section:"Utilities & Infrastructure",text:"Type of trolleys present at the hospital",upload:"Both",type:"field"},
  {id:"068",part:"II",section:"Utilities & Infrastructure",text:"Ambulance Accessibility",upload:"Both",type:"field"},
  {id:"069",part:"II",section:"Utilities & Infrastructure",text:"Uniform signage system in the Facility",upload:"Both",type:"field"},
  {id:"070",part:"II",section:"Ambulance (if applicable)",text:"List of drugs present in the ambulance",upload:"Mobile",type:"doc"},
  {id:"071",part:"II",section:"Ambulance (if applicable)",text:"Training records and driving license of drivers",upload:"Mobile",type:"doc"},
  {id:"072",part:"II",section:"Ambulance (if applicable)",text:"Training records of doctors deputed in ambulances",upload:"Mobile",type:"doc"},
  {id:"073",part:"II",section:"Ambulance (if applicable)",text:"Training records of nurses deputed in ambulances",upload:"Mobile",type:"doc"},
  {id:"074",part:"II",section:"Ambulance (if applicable)",text:"Training records of technicians deputed in ambulances",upload:"Mobile",type:"doc"},
  {id:"075",part:"II",section:"Land/Building",text:"Land/Rent Agreement or Occupancy Certificate",upload:"Portal",type:"doc"},
  // ── Part III — Statutory Compliances ─────────────────────────────────────
  {id:"076",part:"III",section:"Statutory Compliances",text:"Which statutory compliances does the organisation have? (Yes/No for each)",upload:"Mobile",type:"field"},
  {id:"077",part:"III",section:"Statutory Compliances",text:"License Number (for each applicable license)",upload:"Mobile",type:"field"},
  {id:"078",part:"III",section:"Statutory Compliances",text:"License Status (Valid/Expired)",upload:"Mobile",type:"field"},
  {id:"079",part:"III",section:"Statutory Compliances",text:"Issuing Authority",upload:"Mobile",type:"field"},
  {id:"080",part:"III",section:"Statutory Compliances",text:"Expiry Date",upload:"Mobile",type:"field"},
  {id:"081",part:"III",section:"MoU of Outsourced Services",text:"MoU with other Hospital for all outsourced services (upload via Portal)",upload:"Portal",type:"field"},
  // ── Part IV — Clinical Services Details ──────────────────────────────────
  {id:"082",part:"IV",section:"OPD & IPD Data",text:"Number of OPD patients for the past 12 months",upload:"Both",type:"field"},
  {id:"083",part:"IV",section:"OPD & IPD Data",text:"Number of IPD admissions in the past 12 months",upload:"Both",type:"field"},
  {id:"084",part:"IV",section:"OPD & IPD Data",text:"Number of inpatient days in a month (average)",upload:"Both",type:"field"},
  {id:"085",part:"IV",section:"OPD & IPD Data",text:"Number of available bed days",upload:"Both",type:"field"},
  {id:"086",part:"IV",section:"OPD & IPD Data",text:"Average Occupancy Rate (must be ≥30% for last 6 months)",upload:"Both",type:"field"},
  {id:"087",part:"IV",section:"OPD & IPD Data",text:"Number of ICU inpatient days",upload:"Both",type:"field"},
  {id:"088",part:"IV",section:"OPD & IPD Data",text:"Number of available ICU bed days",upload:"Both",type:"field"},
  {id:"089",part:"IV",section:"OPD & IPD Data",text:"Data of past 3 months for monthly average",upload:"Both",type:"field"},
  {id:"090",part:"IV",section:"Scope of Services",text:"Name of service offered",upload:"Both",type:"field"},
  {id:"091",part:"IV",section:"Scope of Services",text:"Full time / Part time / Visiting (type of consultant)",upload:"Both",type:"field"},
  {id:"092",part:"IV",section:"Scope of Services",text:"Doctor Name",upload:"Both",type:"field"},
  {id:"093",part:"IV",section:"Scope of Services",text:"Graduation",upload:"Both",type:"field"},
  {id:"094",part:"IV",section:"Scope of Services",text:"Post-Graduation",upload:"Both",type:"field"},
  {id:"095",part:"IV",section:"Additional Clinical Info",text:"Ten most frequent clinical services where admissions take place",upload:"Both",type:"field"},
  {id:"096",part:"IV",section:"Additional Clinical Info",text:"Ten most frequent diagnoses for in-patients",upload:"Both",type:"field"},
  {id:"097",part:"IV",section:"Additional Clinical Info",text:"Ten most frequent surgical procedures at your hospital",upload:"Both",type:"field"},
  {id:"098",part:"IV",section:"Additional Clinical Info",text:"Type of sterilization modes used in the hospital",upload:"Both",type:"field"},
  {id:"099",part:"IV",section:"OPD & IPD Documents",text:"UHID of 5 patients treated in past 6 months under each clinical service offered",upload:"Mobile",type:"doc"},
  // ── Part V — Hospital Staffing (No Documents Required — fields only) ─────
  {id:"100",part:"V",section:"Medical Officers",text:"Name",upload:"Portal",type:"field"},
  {id:"101",part:"V",section:"Medical Officers",text:"Designation",upload:"Portal",type:"field"},
  {id:"102",part:"V",section:"Medical Officers",text:"Qualification",upload:"Portal",type:"field"},
  {id:"103",part:"V",section:"Medical Officers",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"104",part:"V",section:"Medical Officers",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"105",part:"V",section:"Medical Officers",text:"Working Department",upload:"Portal",type:"field"},
  {id:"106",part:"V",section:"Nurses",text:"Name",upload:"Portal",type:"field"},
  {id:"107",part:"V",section:"Nurses",text:"Designation",upload:"Portal",type:"field"},
  {id:"108",part:"V",section:"Nurses",text:"Qualification",upload:"Portal",type:"field"},
  {id:"109",part:"V",section:"Nurses",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"110",part:"V",section:"Nurses",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"111",part:"V",section:"Nurses",text:"Working Department",upload:"Portal",type:"field"},
  {id:"112",part:"V",section:"Nurses",text:"Nurse-patient ratio: Ward, ICU (ventilated), ICU (non-ventilated)",upload:"Portal",type:"field"},
  {id:"113",part:"V",section:"Paramedical Staff",text:"Name",upload:"Portal",type:"field"},
  {id:"114",part:"V",section:"Paramedical Staff",text:"Designation",upload:"Portal",type:"field"},
  {id:"115",part:"V",section:"Paramedical Staff",text:"Qualification",upload:"Portal",type:"field"},
  {id:"116",part:"V",section:"Paramedical Staff",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"117",part:"V",section:"Paramedical Staff",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"118",part:"V",section:"Paramedical Staff",text:"Working Department",upload:"Portal",type:"field"},
  {id:"119",part:"V",section:"Admin & Support Staff",text:"Name",upload:"Portal",type:"field"},
  {id:"120",part:"V",section:"Admin & Support Staff",text:"Designation",upload:"Portal",type:"field"},
  {id:"121",part:"V",section:"Admin & Support Staff",text:"Qualification",upload:"Portal",type:"field"},
  {id:"122",part:"V",section:"Admin & Support Staff",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"123",part:"V",section:"Admin & Support Staff",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"124",part:"V",section:"Admin & Support Staff",text:"Working Department",upload:"Portal",type:"field"},
  // ── Part VI — Quality Improvement Process ────────────────────────────────
  {id:"125",part:"VI",section:"Committee / Coordinator",text:"Documents for any two changes in hospital related to quality & patient safety (certified by Top Management)",upload:"Mobile",type:"doc"},
  {id:"126",part:"VI",section:"Committee / Coordinator",text:"Documents for any five indicators data signed by Top Management",upload:"Mobile",type:"doc"},
  {id:"127",part:"VI",section:"Registration & Billing",text:"Scanned copy of OPD registration/admission form",upload:"Portal",type:"doc"},
  {id:"128",part:"VI",section:"Registration & Billing",text:"Scanned copy of IPD registration/admission form",upload:"Portal",type:"doc"},
  {id:"129",part:"VI",section:"Registration & Billing",text:"Scanned copy of Emergency registration/admission form",upload:"Portal",type:"doc"},
  {id:"130",part:"VI",section:"Registration & Billing",text:"Copy of Basic Tariff List (bed, OT, ICU charges, packages)",upload:"Mobile",type:"doc"},
  {id:"131",part:"VI",section:"Patient & Family Education",text:"Blood and Blood Product Transfusion Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"132",part:"VI",section:"Patient & Family Education",text:"Blood Donation Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"133",part:"VI",section:"Patient & Family Education",text:"Anaesthesia Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"134",part:"VI",section:"Patient & Family Education",text:"Surgery Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"135",part:"VI",section:"Patient & Family Education",text:"Training material on safe parenting, nutrition and immunization",upload:"Portal",type:"doc"},
  {id:"136",part:"VI",section:"Patient Related Processes",text:"UHID of any one patient + filled Initial Assessment form (OPD by doctor, IPD by doctor, IPD by nurse, Emergency)",upload:"Mobile",type:"doc"},
  {id:"137",part:"VI",section:"Patient Related Processes",text:"Any 1 MLC or Police intimation form or MLC register scanned copy",upload:"Mobile",type:"doc"},
  {id:"138",part:"VI",section:"Patient Related Processes",text:"Copy of scope of Obstetric Services + UHID with ante natal, maternal nutrition, post-natal care",upload:"Mobile",type:"doc"},
  {id:"139",part:"VI",section:"Patient Related Processes",text:"UHID of any 1 patient + filled assessment sheet (nutritional, growth, immunization)",upload:"Mobile",type:"doc"},
  {id:"140",part:"VI",section:"Patient Related Processes",text:"Copy of Pediatrics service documentation",upload:"Mobile",type:"doc"},
  {id:"141",part:"VI",section:"Patient Related Processes",text:"Register of patients referred/transferred from Inpatient area",upload:"Mobile",type:"doc"},
  {id:"142",part:"VI",section:"Patient Related Processes",text:"Filled patient case sheet of any 1 patient from ICU",upload:"Mobile",type:"doc"},
  {id:"143",part:"VI",section:"Patient Related Processes",text:"Filled patient case sheet of any 1 patient from any 1 ward",upload:"Mobile",type:"doc"},
  {id:"144",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with Pre-anaesthesia assessment format",upload:"Mobile",type:"doc"},
  {id:"145",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with anaesthesia monitoring format",upload:"Mobile",type:"doc"},
  {id:"146",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with post-anaesthesia status monitoring format",upload:"Mobile",type:"doc"},
  {id:"147",part:"VI",section:"Patient Related Processes",text:"Copy of adverse anaesthesia events records in past 3 months (if applicable)",upload:"Mobile",type:"doc"},
  {id:"148",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with preoperative assessment and provisional diagnosis",upload:"Mobile",type:"doc"},
  {id:"149",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with operative notes and post-operative plan of care",upload:"Mobile",type:"doc"},
  {id:"150",part:"VI",section:"Patient Related Processes",text:"Filled ward discharge summary (all pages) of any one patient",upload:"Mobile",type:"doc"},
  {id:"151",part:"VI",section:"Patient Related Processes",text:"Filled discharge summary (all pages) of any one LAMA patient",upload:"Mobile",type:"doc"},
  {id:"152",part:"VI",section:"Nursing Care",text:"1 copy of nursing documentation (Medication Administration Record)",upload:"Mobile",type:"doc"},
  {id:"153",part:"VI",section:"Nursing Care",text:"Copy of nursing monitoring charts",upload:"Mobile",type:"doc"},
  {id:"154",part:"VI",section:"Nursing Care",text:"Copy of nurses notes",upload:"Mobile",type:"doc"},
  {id:"155",part:"VI",section:"Medication Management",text:"Copies of fridge temperature records of last three months",upload:"Mobile",type:"doc"},
  {id:"156",part:"VI",section:"Medication Management",text:"Scanned list of emergency and high risk medications",upload:"Mobile",type:"doc"},
  {id:"157",part:"VI",section:"Medication Management",text:"Photo of stock of emergency medications",upload:"Mobile",type:"doc"},
  {id:"158",part:"VI",section:"Medication Management",text:"Copies of prescriptions of any 3 patients",upload:"Mobile",type:"doc"},
  {id:"159",part:"VI",section:"Medication Management",text:"Copy of medication order from ICU, Wards, Emergency, Obs & Gyn, Pediatric",upload:"Mobile",type:"doc"},
  {id:"160",part:"VI",section:"HR Training Records",text:"Training record — Scope of services",upload:"Mobile",type:"doc"},
  {id:"161",part:"VI",section:"HR Training Records",text:"Training record — Care of emergency patients",upload:"Mobile",type:"doc"},
  {id:"162",part:"VI",section:"HR Training Records",text:"Training record — Infection Control Practices",upload:"Mobile",type:"doc"},
  {id:"163",part:"VI",section:"HR Training Records",text:"Training record — Safety Education programme",upload:"Mobile",type:"doc"},
  {id:"164",part:"VI",section:"HR Training Records",text:"Training record — Medication Error",upload:"Mobile",type:"doc"},
  {id:"165",part:"VI",section:"HR Training Records",text:"Training record — Grievance Handling procedures",upload:"Mobile",type:"doc"},
  {id:"166",part:"VI",section:"HR Training Records",text:"Training record — Safe Practices in Laboratory",upload:"Mobile",type:"doc"},
  {id:"167",part:"VI",section:"HR Training Records",text:"Training record — Safe Practices in Imaging",upload:"Mobile",type:"doc"},
  {id:"168",part:"VI",section:"HR Training Records",text:"Training record — Child Abduction Prevention",upload:"Mobile",type:"doc"},
  {id:"169",part:"VI",section:"HR Training Records",text:"Training record video — Fire mock drills",upload:"Mobile",type:"doc"},
  {id:"170",part:"VI",section:"HR Training Records",text:"Training record — Spill Management",upload:"Mobile",type:"doc"},
  {id:"171",part:"VI",section:"HR Training Records",text:"Training record — Needle stick injury",upload:"Mobile",type:"doc"},
  {id:"172",part:"VI",section:"HR Training Records",text:"Training record — Disciplinary Procedures",upload:"Mobile",type:"doc"},
  {id:"173",part:"VI",section:"HR Training Records",text:"Training record — Preparation and Administration of Chemotherapeutic Drugs",upload:"Mobile",type:"doc"},
  {id:"174",part:"VI",section:"Infection Control",text:"Copy of housekeeping checklist for any 3 locations",upload:"Mobile",type:"doc"},
  {id:"175",part:"VI",section:"Infection Control",text:"Photo of autoclaving records indicators",upload:"Mobile",type:"doc"},
  {id:"176",part:"VI",section:"Infection Control",text:"Microbiological surveillance culture report (OT, Labour Room, ICU, NICU - past 3 months)",upload:"Mobile",type:"doc"},
  {id:"177",part:"VI",section:"Infection Control",text:"Records of pre and post exposure prophylaxis provided to staff",upload:"Mobile",type:"doc"},
  {id:"178",part:"VI",section:"Infection Control",text:"Bio Medical Waste (BMW) authorization from Pollution Control Board",upload:"Portal",type:"doc"},
  {id:"179",part:"VI",section:"Infection Control",text:"MoU with outsourced bio medical waste agency",upload:"Portal",type:"doc"},
  {id:"180",part:"VI",section:"Infection Control",text:"Photo of display of work instructions for segregation and handling of BMW",upload:"Mobile",type:"doc"},
  {id:"181",part:"VI",section:"Infection Control",text:"Record of fee, documents & report submitted to authorities for BMW on stipulated dates",upload:"Mobile",type:"doc"},
  {id:"182",part:"VI",section:"Management Process",text:"Scanned copy of documented hospital mission",upload:"Portal",type:"doc"},
  {id:"183",part:"VI",section:"Management Process",text:"Organisation's organogram",upload:"Portal",type:"doc"},
  {id:"184",part:"VI",section:"Management Process",text:"Handling record of patient grievances/complaints",upload:"Mobile",type:"doc"},
  {id:"185",part:"VI",section:"Management Process",text:"Documents of composition of all committees (Quality & Safety, IPC, P&T, Blood Transfusion, Medical Records etc.)",upload:"Portal",type:"doc"},
  {id:"186",part:"VI",section:"Management Process",text:"Copy of terms of reference of all the committees",upload:"Portal",type:"doc"},
  {id:"187",part:"VI",section:"Management Process",text:"Copy of minutes of meeting of all committees for last 3 months",upload:"Mobile",type:"doc"},
  {id:"188",part:"VI",section:"Management Process",text:"Scanned data of Medication Error and Adverse Drug Reaction of last 3 months",upload:"Mobile",type:"doc"},
  {id:"189",part:"VI",section:"Management Process",text:"Scanned Root Cause Analysis (RCA) and CAPA of Medication Error and ADR of last 3 months",upload:"Mobile",type:"doc"},
  {id:"190",part:"VI",section:"Management Process",text:"Scope of services (Laboratory and Imaging)",upload:"Mobile",type:"doc"},
  {id:"191",part:"VI",section:"Management Process",text:"Defined turnaround time for tests (Laboratory and Imaging)",upload:"Mobile",type:"doc"},
  {id:"192",part:"VI",section:"Management Process",text:"Critical result reporting register (test ready time, communicated time, name of individual conveyed to)",upload:"Mobile",type:"doc"},
  {id:"193",part:"VI",section:"Management Process",text:"Blood transfusion records (orders, pre-transfusion medications, cross matching, blood product label, monitoring - at least 3)",upload:"Mobile",type:"doc"},
  {id:"194",part:"VI",section:"Management Process",text:"Scanned filled Blood transfusion reaction form in past 3 months",upload:"Mobile",type:"doc"},
  {id:"195",part:"VI",section:"Management Process",text:"Scanned copy of Blood transfusion committee's minutes with discussed reaction and CAPA",upload:"Portal",type:"doc"},
  {id:"196",part:"VI",section:"Safety Management",text:"Filled WHO Surgical Safety Checklist used for every surgery (any 3)",upload:"Mobile",type:"doc"},
  {id:"197",part:"VI",section:"Safety Management",text:"Scanned copy of facility inspection rounds",upload:"Mobile",type:"doc"},
  {id:"198",part:"VI",section:"Safety Management",text:"Copy of document of maintenance plan of medical gases and vacuum systems",upload:"Mobile",type:"doc"},
  {id:"199",part:"VI",section:"Safety Management",text:"Copy of floor plans with exit routes",upload:"Mobile",type:"doc"},
  {id:"200",part:"VI",section:"Record Management",text:"Checklist for completeness for medical records",upload:"Mobile",type:"doc"},
  {id:"201",part:"VI",section:"Record Management",text:"Filled case sheet with doctors name, signature, date & time (1 from each: ICU, Operative Patient, Ward, Emergency, Obs & Gyn)",upload:"Mobile",type:"doc"},
  // ── Part VII — Documentation Requirements (all via Portal) ───────────────
  {id:"202",part:"VII",section:"SOPs & Procedures",text:"Procedure guide for collection, identification, handling, transportation, processing and disposal of specimens",upload:"Portal",type:"doc"},
  {id:"203",part:"VII",section:"SOPs & Procedures",text:"Process addressing discharge of all patients including MLC cases and patients leaving against medical advice (LAMA)",upload:"Portal",type:"doc"},
  {id:"204",part:"VII",section:"SOPs & Procedures",text:"Documented procedure addressing care of patients in emergency including medico-legal cases",upload:"Portal",type:"doc"},
  {id:"205",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures for rational use of blood and blood products",upload:"Portal",type:"doc"},
  {id:"206",part:"VII",section:"SOPs & Procedures",text:"Documented procedures governing transfusion of blood and blood products",upload:"Portal",type:"doc"},
  {id:"207",part:"VII",section:"SOPs & Procedures",text:"Documented procedure for administration of anaesthesia",upload:"Portal",type:"doc"},
  {id:"208",part:"VII",section:"SOPs & Procedures",text:"Defined criterion to transfer the patient from the recovery area",upload:"Portal",type:"doc"},
  {id:"209",part:"VII",section:"SOPs & Procedures",text:"Documented procedure addressing prevention of adverse events (wrong site, wrong patient, wrong surgery)",upload:"Portal",type:"doc"},
  {id:"210",part:"VII",section:"SOPs & Procedures",text:"Documented procedure incorporating purchase, storage, prescription and dispensation of medications",upload:"Portal",type:"doc"},
  {id:"211",part:"VII",section:"SOPs & Procedures",text:"Documented procedures addressing procurement and usage of implantable prostheses",upload:"Portal",type:"doc"},
  {id:"212",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures for storage of medications",upload:"Portal",type:"doc"},
  {id:"213",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures governing usage of radioactive drugs",upload:"Portal",type:"doc"},
  {id:"214",part:"VII",section:"SOPs & Procedures",text:"Policies and procedures for safe storage, preparation, handling, distribution and disposal of radioactive drugs",upload:"Portal",type:"doc"},
  {id:"215",part:"VII",section:"SOPs & Procedures",text:"Infection control manual, periodically updated, with surveillance activities",upload:"Portal",type:"doc"},
  {id:"216",part:"VII",section:"SOPs & Procedures",text:"Documented operational and maintenance plan for clinical and support service equipment",upload:"Portal",type:"doc"},
  {id:"217",part:"VII",section:"SOPs & Procedures",text:"Documented safe exit plan in case of fire and non-fire emergencies",upload:"Portal",type:"doc"},
  {id:"218",part:"VII",section:"SOPs & Procedures",text:"Well-defined staff recruitment process",upload:"Portal",type:"doc"},
  {id:"219",part:"VII",section:"SOPs & Procedures",text:"Documented disciplinary and grievance handling procedure",upload:"Portal",type:"doc"},
  {id:"220",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures for maintaining confidentiality, integrity and security of records",upload:"Portal",type:"doc"},
  {id:"221",part:"VII",section:"SOPs & Procedures",text:"Documented procedures for retention time of medical records, data and information",upload:"Portal",type:"doc"},
  {id:"222",part:"VII",section:"SOPs & Procedures",text:"Defined process to whom the patient record can be released",upload:"Portal",type:"doc"},
  {id:"223",part:"VII",section:"SOPs & Procedures",text:"Procedure on destruction of medical records",upload:"Portal",type:"doc"},
];

const HCO_ELC_LICENSES = [
  {id:"LIC001",cat:"Mandatory",name:"Legal status — Shops and Commercial Establishments Act (Registration & place of business)",appl:"All"},
  {id:"LIC002",cat:"Mandatory",name:"State Pollution Control Board (SPCB) Consent to generate Bio-Medical Waste (BMW)",appl:"All"},
  {id:"LIC003",cat:"Mandatory",name:"MoU with BMW collecting Agency",appl:"All"},
  {id:"LIC004",cat:"Mandatory",name:"Pollution Control Board License for water and Air Pollution",appl:">50 beds"},
  {id:"LIC005",cat:"Mandatory",name:"PC-PNDT Act Registration",appl:"All"},
  {id:"LIC006",cat:"Mandatory",name:"MTP Act Registration",appl:"All"},
  {id:"LIC007",cat:"Mandatory",name:"Narcotics License",appl:"All"},
  {id:"LIC008",cat:"Mandatory",name:"Retail Pharmacy License",appl:"All"},
  {id:"LIC009",cat:"AERB",name:"AERB License for X-Ray",appl:"If X-Ray available"},
  {id:"LIC010",cat:"AERB",name:"AERB License for Mobile X-Ray(s)",appl:"If Mobile X-Ray available"},
  {id:"LIC011",cat:"AERB",name:"AERB License for Dental X-Rays",appl:"If Dental X-Ray available"},
  {id:"LIC012",cat:"AERB",name:"AERB License for OPG",appl:"If OPG available"},
  {id:"LIC013",cat:"AERB",name:"AERB License for CT Scan",appl:"If CT Scan available"},
  {id:"LIC014",cat:"AERB",name:"AERB License for Mammography",appl:"If Mammography available"},
  {id:"LIC015",cat:"AERB",name:"AERB License for BMD services",appl:"If BMD available"},
  {id:"LIC016",cat:"AERB",name:"AERB License for C-Arm",appl:"If C-Arm available"},
  {id:"LIC017",cat:"AERB",name:"AERB License for Cath Lab",appl:"If Cath Lab available"},
  {id:"LIC018",cat:"AERB",name:"RSO Level I, II, III License",appl:"If radiation services available"},
  {id:"LIC019",cat:"AERB",name:"Nuclear Medicine Compliance License",appl:"If Nuclear Medicine available"},
  {id:"LIC020",cat:"AERB",name:"PET Scan Compliance License",appl:"If PET Scan available"},
  {id:"LIC021",cat:"AERB",name:"SPET/CT Compliance License",appl:"If SPET/CT available"},
  {id:"LIC022",cat:"AERB",name:"Radiotherapy Compliance License",appl:"If Radiotherapy available"},
  {id:"LIC023",cat:"AERB",name:"IMRT Compliance License",appl:"If IMRT available"},
  {id:"LIC024",cat:"AERB",name:"Cobalt Compliance License",appl:"If Cobalt therapy available"},
  {id:"LIC025",cat:"AERB",name:"Linear Accelerator (LINAC) Compliance License",appl:"If LINAC available"},
  {id:"LIC026",cat:"AERB",name:"Brachytherapy Compliance License",appl:"If Brachytherapy available"},
];

// HCO ELC — 10 Chapter Framework (NABH Guidebook, Section 4.1)
// Chapters: AAI, COP, HIC, MOM, PRE, CQI, ROM, FMS, HRM, IMS
// Note: OE counts not published in brochure — shown as per standard category
const HCO_ELC_CHAPTER_SUMMARY = [
  {ch:"AAI",name:"Access, Assessment & Information",desc:"Key safety and process elements in continuum of patient care within hospital till discharge"},
  {ch:"COP",name:"Care of Patients",desc:"Emergency care, ambulance services, clinical care in consonance with clinical requirements"},
  {ch:"HIC",name:"Hospital Infection Control",desc:"Effective infection control programme to reduce/eliminate infection risks to patients, visitors and staff"},
  {ch:"MOM",name:"Management of Medication",desc:"Emergency medications standardized and available; monitoring post-administration; adverse drug event reporting"},
  {ch:"PRE",name:"Patient Rights & Education",desc:"Defined patient/family rights and responsibilities; staff trained to protect patient rights"},
  {ch:"CQI",name:"Continuous Quality Improvement",desc:"Continual quality improvement and patient safety programme involving all areas and staff"},
  {ch:"ROM",name:"Responsibilities of Management",desc:"Governance of organisation in professional and ethical manner; defined management responsibilities"},
  {ch:"FMS",name:"Facility Management & Safety",desc:"Safe and secure environment for patients, families, staff and visitors; regular facility inspection rounds"},
  {ch:"HRM",name:"Human Resource Management",desc:"Acquire, provide, retain and maintain competent people in right numbers to meet patient needs"},
  {ch:"IMS",name:"Information Management System",desc:"Medical record requirements; continuity of care and communication between care providers"},
];

// ELC Process steps
const HCO_ELC_PROCESS = [
  {step:1,name:"Register on HOPE Portal",url:"hope.qcin.org",desc:"Go to www.hope.qcin.org → Click Register → Fill Hospital User Registration Form (Hospital name, SPOC details, State, total sanctioned beds)",output:"Login credentials sent to registered email"},
  {step:2,name:"Fill 7-Part Questionnaire",url:"hope.qcin.org",desc:"Complete all 7 parts on the web portal: General Info, Physical Infrastructure, Statutory Compliances, Clinical Services, Hospital Staffing, Quality Improvement Process, Documentation. Save progress at each step.",output:"Completed questionnaire submission (cannot edit after Final Submit)"},
  {step:3,name:"Upload Documents",url:"hope.qcin.org",desc:"Portal documents → upload via web portal (Upload any file icon). Mobile documents → upload via HOPE Android app (View Uploaded File icon). Save on portal before using mobile app. Cannot use both simultaneously.",output:"Document submission complete"},
  {step:4,name:"Pay Fee",url:"hope.qcin.org",desc:"Pay HCO ELC fee based on bed strength (w.e.f. June 2025): 51–100 beds ₹96,000 | 101–300 beds ₹1,20,000 — plus 18% GST. Fee is non-refundable and non-transferable. Once paid, application moves to DA team.",output:"Payment receipt + Permanent Application Number"},
  {step:5,name:"Desktop Assessment (DA)",url:"",desc:"NABH DA team reviews all submitted documents online. NCs raised with remarks. HCO submits NC reply + supporting document upload. Two rounds of NC closure cycle available at DA stage.",output:"DA NC closure → Date allotment for onsite assessment"},
  {step:6,name:"Onsite Assessment",url:"",desc:"Physical visit by NABH assessor. Assessment activities: document review, patient care area visit, functional interviews, facility tours. Assessor uploads report within 7 days. HCO gets two NC closure cycles.",output:"Onsite assessment report + NC closure"},
  {step:7,name:"Certification Committee",url:"",desc:"After all NCs closed, case placed before Certification Committee. Committee recommendations are final. If rejected, HCO can appeal to Chairman NABH after paying appeal fee.",output:"Approval letter / Rejection letter"},
  {step:8,name:"Digital Certificate",url:"",desc:"Printable digital certificate issued with unique certificate number, hospital name, effective date, expiry date. Valid for 2 years. No surveillance assessment under certification programmes. Apply for renewal 6 months before expiry.",output:"NABH HCO ELC Certificate (2-year validity)"},
];

// HCO Fee — slab-based by bed strength (w.e.f. June 2025)
const HCO_FEE = {
  gstRate: 0.18,
  label: "HCO Entry Level Certification (>50 sanctioned beds)",
  note: "Fee is non-refundable and non-transferable. w.e.f. June 2025. Source: NABH HOPE ELC fee schedule.",
  slabs: [
    { beds: "51–100 beds",  base: 96000 },
    { beds: "101–300 beds", base: 120000 },
  ],
};

// ── STEP 2: STATE VARIABLES (paste inside App function with other useState) ──
// const [hcoMode, setHcoMode] = useState('elc'); // 'elc' | 'full'
// const [hcoElcTab, setHcoElcTab] = useState('overview'); // 'overview'|'docs'|'licenses'|'chapters'|'process'|'upgrade'
// const [hcoElcProgress, setHcoElcProgress] = useState({}); // {docId: 'pending'|'ready'|'na'}
// const [hcoLicProgress, setHcoLicProgress] = useState({}); // {licId: 'pending'|'obtained'|'na'}
// const [hcoDocFilter, setHcoDocFilter] = useState('all'); // 'all'|'pending'|'ready'
// const [hcoDocPart, setHcoDocPart] = useState('all');


// ── STEP 3: RENDER FUNCTION (paste inside App component) ─────────────────

const renderHCOTab = () => {
  const T = {
    bg:"#050e1a", panel:"#081525", panel2:"#0c1e35", border:"#0f2640",
    gold:"#c9a84c", red:"#e05a5a", orange:"#f4a441", green:"#4caf7d",
    blue:"#4fc3f7", muted:"#3a5870", text:"#c8dcea", white:"#eef4f9"
  };

  // ── Fee Calculation (slab-based) ──
  const feeSlab = HCO_FEE.slabs[0]; // default display slab (51–100 beds)
  const gst = Math.round(feeSlab.base * HCO_FEE.gstRate);
  const totalFee = feeSlab.base + gst;

  // ── Progress Helpers ──
  const docStatus = (id) => hcoElcProgress[id] || 'pending';
  const licStatus = (id) => hcoLicProgress[id] || 'pending';

  const setDocStatus = (id, status) => {
    setHcoElcProgress(prev => ({ ...prev, [id]: status }));
  };
  const setLicStatus = (id, status) => {
    setHcoLicProgress(prev => ({ ...prev, [id]: status }));
  };

  // Stats
  const docsDone = HCO_ELC_DOCS.filter(d => docStatus(d.id) === 'ready').length;
  const docsNA = HCO_ELC_DOCS.filter(d => docStatus(d.id) === 'na').length;
  const docsApplicable = HCO_ELC_DOCS.length - docsNA;
  const docsPct = docsApplicable > 0 ? Math.round((docsDone / docsApplicable) * 100) : 0;

  const licDone = HCO_ELC_LICENSES.filter(l => licStatus(l.id) === 'obtained').length;
  const licNA = HCO_ELC_LICENSES.filter(l => licStatus(l.id) === 'na').length;
  const licApplicable = HCO_ELC_LICENSES.length - licNA;
  const licPct = licApplicable > 0 ? Math.round((licDone / licApplicable) * 100) : 0;

  const overallPct = Math.round((docsPct + licPct) / 2);

  // Filtered docs
  const filteredDocs = HCO_ELC_DOCS.filter(d => {
    const partMatch = hcoDocPart === 'all' || d.part === hcoDocPart;
    const statusMatch = hcoDocFilter === 'all' || docStatus(d.id) === hcoDocFilter;
    return partMatch && statusMatch;
  });

  const parts = ['I','II','III','IV','V','VI','VII'];

  const uploadBadge = (upload) => {
    const color = upload === 'Portal' ? T.blue : upload === 'Mobile' ? T.orange : T.gold;
    const label = upload === 'Portal' ? '🌐 Portal' : upload === 'Mobile' ? '📱 Mobile' : '🔄 Both';
    return (
      <span style={{fontSize:10,padding:'2px 6px',borderRadius:10,background:color+'22',color,border:`1px solid ${color}44`,whiteSpace:'nowrap'}}>
        {label}
      </span>
    );
  };

  // ── Full Accreditation summary (NABH 6th Edition Hospital Standards)
  const renderFullAccredTab = () => (
    <div style={{padding:16}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}44`,borderRadius:12,padding:20,marginBottom:16}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:16,marginBottom:8}}>🏆 NABH Full Hospital Accreditation — 6th Edition</div>
        <div style={{color:T.text,fontSize:13,lineHeight:1.6}}>
          Full accreditation for Healthcare Organisations (HCOs). Assessed against 639 Objective Elements across 10 chapters under the 6th Edition NABH Hospital Standards.
        </div>
        <div style={{display:'flex',gap:12,flexWrap:'wrap',marginTop:16}}>
          {[
            {label:'Chapters',val:'10'},
            {label:'Total OEs',val:'639'},
            {label:'Validity',val:'4 Years'},
            {label:'Surveillance',val:'24 Months'},
          ].map(s => (
            <div key={s.label} style={{background:T.panel2,borderRadius:8,padding:'10px 16px',textAlign:'center',border:`1px solid ${T.border}`}}>
              <div style={{color:T.gold,fontWeight:700,fontSize:20}}>{s.val}</div>
              <div style={{color:T.muted,fontSize:11}}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>

      <div style={{color:T.gold,fontWeight:600,fontSize:13,marginBottom:10}}>Chapter Breakdown — 6th Edition</div>
      <div style={{display:'grid',gap:6}}>
        {[
          {ch:'AAC',name:'Access, Assessment & Continuity of Care',oes:72},
          {ch:'COP',name:'Care of Patients',oes:117},
          {ch:'MOM',name:'Management of Medication',oes:67},
          {ch:'PRE',name:'Patient Rights & Education',oes:47},
          {ch:'HIC',name:'Hospital Infection Control',oes:48},
          {ch:'PSQ',name:'Patient Safety & Quality Improvement',oes:34},
          {ch:'ROM',name:'Responsibilities of Management',oes:51},
          {ch:'FMS',name:'Facility Management & Safety',oes:61},
          {ch:'HRM',name:'Human Resource Management',oes:62},
          {ch:'IMS',name:'Information Management System',oes:40},
        ].map(c => (
          <div key={c.ch} style={{background:T.panel,borderRadius:8,padding:'10px 14px',display:'flex',justifyContent:'space-between',alignItems:'center',border:`1px solid ${T.border}`}}>
            <div>
              <span style={{color:T.gold,fontWeight:700,fontSize:12,marginRight:8}}>{c.ch}</span>
              <span style={{color:T.text,fontSize:12}}>{c.name}</span>
            </div>
            <span style={{color:T.blue,fontWeight:600,fontSize:12}}>{c.oes} OEs</span>
          </div>
        ))}
      </div>

      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.orange}44`}}>
        <div style={{color:T.orange,fontWeight:600,fontSize:13,marginBottom:6}}>⚠️ Key Differences vs ELC</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.7}}>
          Full accreditation requires implementation of all 639 OEs vs simplified ELC standards. Requires pre-assessment, final assessment + surveillance at 24 months. Validity is 4 years (vs 2 years for ELC).
          Apply via <strong style={{color:T.gold}}>portal.nabh.co</strong> (not HOPE portal). Assessment team is 2–3 assessors vs 1–2 for ELC.
        </div>
      </div>
    </div>
  );

  // ── OVERVIEW sub-tab ──
  const renderOverview = () => (
    <div style={{padding:16,display:'flex',flexDirection:'column',gap:16}}>

      {/* Eligibility criteria */}
      <div style={{background:'#0a0a1a',border:`1px solid ${T.blue}`,borderRadius:10,padding:14}}>
        <div style={{color:T.blue,fontWeight:700,fontSize:13,marginBottom:6}}>✅ HCO ELC Eligibility Criteria</div>
        <div style={{display:'flex',flexDirection:'column',gap:6}}>
          {[
            {icon:'🏥',text:'More than 50 sanctioned beds (hospitals with ≤50 beds must apply as SHCO)'},
            {icon:'📅',text:'Organisation must be operational for at least 6 months before applying'},
            {icon:'📊',text:'Average bed occupancy ≥ 30% (calculated over last 6 months)'},
            {icon:'🔄',text:'Must apply for ALL services from the specific location — no partial accreditation'},
            {icon:'📋',text:'Must comply with all applicable NABH standards and laws of the land'},
          ].map((e,i) => (
            <div key={i} style={{display:'flex',gap:8,alignItems:'flex-start'}}>
              <span style={{fontSize:14}}>{e.icon}</span>
              <span style={{color:T.text,fontSize:12,lineHeight:1.5}}>{e.text}</span>
            </div>
          ))}
        </div>
      </div>

      {/* Readiness Summary */}
      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:14}}>📊 ELC Readiness</div>
        <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:12}}>
          {[
            {label:'Documents',pct:docsPct,done:docsDone,total:docsApplicable,color:docsPct>=80?T.green:docsPct>=50?T.orange:T.red},
            {label:'Licenses',pct:licPct,done:licDone,total:licApplicable,color:licPct>=80?T.green:licPct>=50?T.orange:T.red},
            {label:'Overall',pct:overallPct,done:null,total:null,color:overallPct>=80?T.green:overallPct>=50?T.orange:T.red},
          ].map(s => (
            <div key={s.label} style={{background:T.panel2,borderRadius:10,padding:12,textAlign:'center',border:`1px solid ${T.border}`}}>
              <div style={{position:'relative',width:64,height:64,margin:'0 auto 8px'}}>
                <svg viewBox="0 0 36 36" style={{width:64,height:64,transform:'rotate(-90deg)'}}>
                  <circle cx="18" cy="18" r="15.9" fill="none" stroke={T.border} strokeWidth="3"/>
                  <circle cx="18" cy="18" r="15.9" fill="none" stroke={s.color} strokeWidth="3"
                    strokeDasharray={`${s.pct} ${100-s.pct}`} strokeDashoffset="0" strokeLinecap="round"/>
                </svg>
                <div style={{position:'absolute',top:'50%',left:'50%',transform:'translate(-50%,-50%)',color:s.color,fontWeight:700,fontSize:14}}>{s.pct}%</div>
              </div>
              <div style={{color:T.text,fontSize:12,fontWeight:600}}>{s.label}</div>
              {s.done !== null && <div style={{color:T.muted,fontSize:10}}>{s.done}/{s.total}</div>}
            </div>
          ))}
        </div>
      </div>

      {/* Fee Display */}
      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:12}}>💰 HCO ELC Certification Fee</div>
        <div style={{background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
          <div style={{color:T.muted,fontSize:11,marginBottom:10}}>{HCO_FEE.label} — fee by bed strength (w.e.f. June 2025)</div>
          <table style={{width:'100%',borderCollapse:'collapse',fontSize:12,marginBottom:10}}>
            <thead>
              <tr>
                {['Bed Strength','Fee (excl. GST)','GST @ 18%','Total Payable'].map(h => (
                  <th key={h} style={{padding:'6px 8px',background:T.panel,color:T.gold,fontWeight:600,textAlign:'left',border:`1px solid ${T.border}`,fontSize:11}}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {HCO_FEE.slabs.map((s,i) => {
                const g = Math.round(s.base * HCO_FEE.gstRate);
                return (
                  <tr key={i} style={{background: i%2===0 ? T.panel : T.panel2}}>
                    <td style={{padding:'6px 8px',color:T.muted,border:`1px solid ${T.border}`}}>{s.beds}</td>
                    <td style={{padding:'6px 8px',color:T.gold,fontWeight:700,border:`1px solid ${T.border}`}}>₹{s.base.toLocaleString('en-IN')}</td>
                    <td style={{padding:'6px 8px',color:T.text,border:`1px solid ${T.border}`}}>₹{g.toLocaleString('en-IN')}</td>
                    <td style={{padding:'6px 8px',color:T.green,fontWeight:700,border:`1px solid ${T.border}`}}>₹{(s.base+g).toLocaleString('en-IN')}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          <div style={{fontSize:11,color:T.muted}}>
            {HCO_FEE.note}<br/>
            Focus assessment: ₹15,000 + GST | Re-issue of certificate: ₹6,000 + GST | Fee is non-refundable.
          </div>
        </div>
      </div>

      {/* HCO vs SHCO at a glance */}
      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:12}}>🏥 HCO vs SHCO — Which applies to you?</div>
        <div style={{overflowX:'auto'}}>
          <table style={{width:'100%',borderCollapse:'collapse',fontSize:12}}>
            <thead>
              <tr>
                {['Parameter','HCO ELC','SHCO ELC'].map(h => (
                  <th key={h} style={{padding:'8px 12px',background:T.panel2,color:T.gold,fontWeight:600,textAlign:'left',border:`1px solid ${T.border}`}}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {[
                ['Sanctioned Beds','>50 beds','≤50 beds'],
                ['ELC Fee','₹96k–₹1.2L + GST (by beds)','₹21,000–₹48,000 + GST'],
                ['Certification Validity','2 Years','2 Years'],
                ['Portal','hope.qcin.org','hope.qcin.org'],
                ['Upgrade Path','NABH 6th Ed. (639 OEs)','NABH Hospital (639 OEs)'],
                ['PCB License','Required (>50 beds)','Not required'],
                ['Surveillance','None under ELC','None under ELC'],
              ].map((row,i) => (
                <tr key={i} style={{background: i%2===0 ? T.panel : T.panel2}}>
                  <td style={{padding:'8px 12px',color:T.muted,border:`1px solid ${T.border}`,fontWeight:600}}>{row[0]}</td>
                  <td style={{padding:'8px 12px',color:T.blue,border:`1px solid ${T.border}`}}>{row[1]}</td>
                  <td style={{padding:'8px 12px',color:T.text,border:`1px solid ${T.border}`}}>{row[2]}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* 10 Chapter Summary */}
      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:12}}>📖 HCO ELC — 10 Assessment Chapters</div>
        <div style={{display:'grid',gap:6}}>
          {HCO_ELC_CHAPTER_SUMMARY.map(c => (
            <div key={c.ch} style={{background:T.panel2,borderRadius:8,padding:'10px 12px',border:`1px solid ${T.border}`}}>
              <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:3}}>
                <span style={{color:T.gold,fontWeight:700,fontSize:12,minWidth:36}}>{c.ch}</span>
                <span style={{color:T.text,fontSize:12,fontWeight:600}}>{c.name}</span>
              </div>
              <div style={{color:T.muted,fontSize:11,lineHeight:1.4,paddingLeft:44}}>{c.desc}</div>
            </div>
          ))}
        </div>
        <div style={{marginTop:10,color:T.muted,fontSize:11,textAlign:'center'}}>Source: NABH Guidebook on Entry-Level Certification for HCOs/SHCOs (Section 4.1)</div>
      </div>
    </div>
  );

  // ── DOCUMENT TRACKER sub-tab ──
  const renderDocTracker = () => {
    const sections = [...new Set(filteredDocs.map(d => d.section))];
    return (
      <div style={{padding:16}}>
        {/* Stats bar */}
        <div style={{display:'flex',gap:8,marginBottom:12,flexWrap:'wrap'}}>
          {[
            {label:`✅ Ready: ${docsDone}`,color:T.green},
            {label:`⏳ Pending: ${HCO_ELC_DOCS.length - docsDone - docsNA}`,color:T.orange},
            {label:`➖ N/A: ${docsNA}`,color:T.muted},
            {label:`Total: ${HCO_ELC_DOCS.length}`,color:T.blue},
          ].map(s => (
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:11,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>

        {/* Filters */}
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          <select value={hcoDocPart} onChange={e => setHcoDocPart(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}>
            <option value="all">All Parts</option>
            {parts.map(p => <option key={p} value={p}>Part {p}</option>)}
          </select>
          <select value={hcoDocFilter} onChange={e => setHcoDocFilter(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}>
            <option value="all">All Status</option>
            <option value="pending">Pending</option>
            <option value="ready">Ready</option>
            <option value="na">N/A</option>
          </select>
          <div style={{marginLeft:'auto',color:T.muted,fontSize:11,display:'flex',alignItems:'center'}}>{filteredDocs.length} items</div>
        </div>

        {/* Document list grouped by section */}
        {sections.map(sec => {
          const secDocs = filteredDocs.filter(d => d.section === sec);
          if (!secDocs.length) return null;
          return (
            <div key={sec} style={{marginBottom:16}}>
              <div style={{color:T.gold,fontWeight:600,fontSize:12,marginBottom:8,display:'flex',alignItems:'center',gap:8}}>
                <span>Part {secDocs[0].part} — {sec}</span>
                <span style={{color:T.muted,fontWeight:400,fontSize:11}}>({secDocs.length})</span>
              </div>
              <div style={{display:'flex',flexDirection:'column',gap:6}}>
                {secDocs.map(doc => {
                  const s = docStatus(doc.id);
                  return (
                    <div key={doc.id} style={{
                      background:T.panel,borderRadius:8,padding:'10px 12px',
                      border:`1px solid ${s==='ready'?T.green:T.border}`,
                      opacity: s==='na' ? 0.6 : 1
                    }}>
                      <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:8,marginBottom:6}}>
                        <div style={{color:T.text,fontSize:12,lineHeight:1.5,flex:1}}>
                          <span style={{color:T.muted,fontSize:10,marginRight:6}}>#{doc.id}</span>
                          {doc.text}
                        </div>
                        <div style={{flexShrink:0}}>{uploadBadge(doc.upload)}</div>
                      </div>
                      <div style={{display:'flex',gap:6}}>
                        {['pending','ready','na'].map(status => (
                          <button key={status} onClick={() => setDocStatus(doc.id, status)}
                            style={{
                              padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:11,fontWeight:600,
                              background: s===status ? (status==='ready'?T.green:status==='na'?T.muted:T.orange)+'33' : T.panel2,
                              color: s===status ? (status==='ready'?T.green:status==='na'?T.muted:T.orange) : T.muted,
                              outline: s===status ? `1px solid ${status==='ready'?T.green:status==='na'?T.muted:T.orange}` : 'none',
                            }}>
                            {status==='ready'?'✅ Ready':status==='na'?'➖ N/A':'⏳ Pending'}
                          </button>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          );
        })}
      </div>
    );
  };

  // ── LICENSE TRACKER sub-tab ──
  const renderLicenseTracker = () => {
    const mandatory = HCO_ELC_LICENSES.filter(l => l.cat === 'Mandatory');
    const aerb = HCO_ELC_LICENSES.filter(l => l.cat === 'AERB');
    return (
      <div style={{padding:16}}>
        {/* Stats */}
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          {[
            {label:`✅ Obtained: ${licDone}`,color:T.green},
            {label:`⏳ Pending: ${HCO_ELC_LICENSES.length - licDone - licNA}`,color:T.orange},
            {label:`➖ N/A: ${licNA}`,color:T.muted},
          ].map(s => (
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:11,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>

        {/* HCO-specific note */}
        <div style={{background:'#0a0d00',border:`1px solid ${T.green}44`,borderRadius:8,padding:10,marginBottom:14}}>
          <div style={{color:T.green,fontSize:12,fontWeight:600,marginBottom:2}}>⚠️ HCO-Specific: PCB License Required</div>
          <div style={{color:T.text,fontSize:11}}>Unlike SHCOs, HCOs (>50 beds) must have the Pollution Control Board License for water and Air Pollution. Mark as N/A only if NABH formally exempts your facility.</div>
        </div>

        {/* Mandatory licenses */}
        <div style={{color:T.red,fontWeight:700,fontSize:13,marginBottom:10}}>🔴 Mandatory Licenses ({mandatory.length})</div>
        <div style={{display:'flex',flexDirection:'column',gap:6,marginBottom:20}}>
          {mandatory.map(lic => {
            const s = licStatus(lic.id);
            return (
              <div key={lic.id} style={{
                background:T.panel,borderRadius:8,padding:'10px 12px',
                border:`1px solid ${s==='obtained'?T.green:T.border}`,
                opacity: s==='na' ? 0.6 : 1
              }}>
                <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:8,marginBottom:6}}>
                  <div style={{color:T.text,fontSize:12,flex:1}}>{lic.name}</div>
                  <div style={{color:T.muted,fontSize:10,flexShrink:0}}>{lic.appl}</div>
                </div>
                <div style={{display:'flex',gap:6}}>
                  {['pending','obtained','na'].map(status => (
                    <button key={status} onClick={() => setLicStatus(lic.id, status)}
                      style={{
                        padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:11,fontWeight:600,
                        background: s===status ? (status==='obtained'?T.green:status==='na'?T.muted:T.orange)+'33' : T.panel2,
                        color: s===status ? (status==='obtained'?T.green:status==='na'?T.muted:T.orange) : T.muted,
                        outline: s===status ? `1px solid ${status==='obtained'?T.green:status==='na'?T.muted:T.orange}` : 'none',
                      }}>
                      {status==='obtained'?'✅ Obtained':status==='na'?'➖ N/A':'⏳ Pending'}
                    </button>
                  ))}
                </div>
              </div>
            );
          })}
        </div>

        {/* AERB licenses */}
        <div style={{color:T.orange,fontWeight:700,fontSize:13,marginBottom:6}}>⚡ AERB Licenses ({aerb.length}) — Mark N/A if service not available</div>
        <div style={{color:T.muted,fontSize:11,marginBottom:10}}>Applicable only if your HCO provides the specific imaging/radiation service. If expired, document of renewal application must also be uploaded via portal.</div>
        <div style={{display:'flex',flexDirection:'column',gap:6}}>
          {aerb.map(lic => {
            const s = licStatus(lic.id);
            return (
              <div key={lic.id} style={{
                background:T.panel,borderRadius:8,padding:'10px 12px',
                border:`1px solid ${s==='obtained'?T.green:T.border}`,
                opacity: s==='na' ? 0.5 : 1
              }}>
                <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:8,marginBottom:6}}>
                  <div style={{color:T.text,fontSize:12,flex:1}}>{lic.name}</div>
                  <div style={{color:T.muted,fontSize:10,flexShrink:0,textAlign:'right',maxWidth:120}}>{lic.appl}</div>
                </div>
                <div style={{display:'flex',gap:6}}>
                  {['pending','obtained','na'].map(status => (
                    <button key={status} onClick={() => setLicStatus(lic.id, status)}
                      style={{
                        padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:11,fontWeight:600,
                        background: s===status ? (status==='obtained'?T.green:status==='na'?T.muted:T.orange)+'33' : T.panel2,
                        color: s===status ? (status==='obtained'?T.green:status==='na'?T.muted:T.orange) : T.muted,
                        outline: s===status ? `1px solid ${status==='obtained'?T.green:status==='na'?T.muted:T.orange}` : 'none',
                      }}>
                      {status==='obtained'?'✅ Obtained':status==='na'?'➖ N/A':'⏳ Pending'}
                    </button>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    );
  };

  // ── PROCESS TIMELINE sub-tab ──
  const renderProcess = () => (
    <div style={{padding:16}}>
      <div style={{background:'#0a0a1a',border:`1px solid ${T.blue}44`,borderRadius:10,padding:12,marginBottom:16}}>
        <div style={{color:T.blue,fontWeight:600,fontSize:12,marginBottom:4}}>💡 Key Points for HCO Applicants</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.6}}>
          • Two rounds of NC closure at both DA and Onsite stages (unlike SHCO 2nd Edition which gives only one).<br/>
          • Registration details on HOPE portal cannot be edited after submission — fill accurately.<br/>
          • Cannot use both web portal and mobile app simultaneously — save on portal first.<br/>
          • Travel, boarding and lodging for onsite assessors is borne by the HCO.
        </div>
      </div>

      <div style={{display:'flex',flexDirection:'column',gap:0}}>
        {HCO_ELC_PROCESS.map((step, idx) => (
          <div key={step.step} style={{display:'flex',gap:12}}>
            {/* Timeline connector */}
            <div style={{display:'flex',flexDirection:'column',alignItems:'center',width:32,flexShrink:0}}>
              <div style={{width:32,height:32,borderRadius:'50%',background:T.gold,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700,fontSize:13,color:T.bg,flexShrink:0}}>
                {step.step}
              </div>
              {idx < HCO_ELC_PROCESS.length - 1 && (
                <div style={{width:2,flex:1,background:T.border,minHeight:20,margin:'4px 0'}}/>
              )}
            </div>
            {/* Step content */}
            <div style={{background:T.panel,borderRadius:10,padding:'12px 14px',marginBottom:10,flex:1,border:`1px solid ${T.border}`}}>
              <div style={{color:T.white,fontWeight:700,fontSize:13,marginBottom:4}}>{step.name}</div>
              {step.url && (
                <div style={{color:T.blue,fontSize:11,marginBottom:6}}>🔗 {step.url}</div>
              )}
              <div style={{color:T.text,fontSize:12,lineHeight:1.6,marginBottom:6}}>{step.desc}</div>
              <div style={{color:T.muted,fontSize:11}}>📄 Output: <span style={{color:T.gold}}>{step.output}</span></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  // ── UPGRADE PATH sub-tab ──
  const renderUpgrade = () => (
    <div style={{padding:16}}>
      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.gold}44`,marginBottom:16}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:15,marginBottom:8}}>🚀 The Journey: HCO ELC → Full NABH Hospital Accreditation</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.7}}>
          HCO Entry Level Certification is the stepping stone. After 2 years, HCOs can upgrade to Full NABH Hospital Accreditation (6th Edition) —
          assessed against 639 OEs. Full accreditation unlocks premium CGHS/ECHS empanelment, medical tourism eligibility,
          higher insurance reimbursements, and national recognition.
        </div>
      </div>

      {/* ELC vs Full Accreditation comparison */}
      <div style={{color:T.gold,fontWeight:600,fontSize:13,marginBottom:10}}>HCO ELC vs Full NABH Accreditation</div>
      <div style={{overflowX:'auto',marginBottom:16}}>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:12}}>
          <thead>
            <tr>
              {['Parameter','HCO ELC','Full Accreditation (6th Ed.)'].map(h => (
                <th key={h} style={{padding:'8px 12px',background:T.panel,color:T.gold,fontWeight:600,textAlign:'left',border:`1px solid ${T.border}`}}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {[
              ['Standards','Simplified (10 chapters)','Full 6th Edition (10 chapters)'],
              ['Objective Elements','Simplified subset','639 OEs'],
              ['Validity','2 years','4 years'],
              ['Process','DA + Onsite','Pre-Assessment + DA + Onsite + Surveillance'],
              ['Surveillance','None','At 24 months'],
              ['Fee','₹96k–₹1.2L + GST (bed-based, Jun 2025)','Per NABH fee schedule (bed-based)'],
              ['Portal','hope.qcin.org','portal.nabh.co'],
              ['Assessors','1–2','2–3'],
              ['Pre-assessment','Optional','Yes (or skip on request)'],
            ].map((row,i) => (
              <tr key={i} style={{background: i%2===0 ? T.panel : T.panel2}}>
                <td style={{padding:'8px 12px',color:T.muted,border:`1px solid ${T.border}`,fontWeight:600}}>{row[0]}</td>
                <td style={{padding:'8px 12px',color:T.text,border:`1px solid ${T.border}`}}>{row[1]}</td>
                <td style={{padding:'8px 12px',color:T.gold,border:`1px solid ${T.border}`}}>{row[2]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Recommended timeline */}
      <div style={{color:T.gold,fontWeight:600,fontSize:13,marginBottom:10}}>Recommended Timeline</div>
      {[
        {phase:'Month 1–2',action:'Confirm eligibility: >50 beds, ≥6 months operational, ≥30% occupancy. Start document and license gap analysis.',color:T.blue},
        {phase:'Month 2–4',action:'Collect all 223 documents and 26 licenses. Train SPOC on HOPE portal and mobile app.',color:T.blue},
        {phase:'Month 4–5',action:'Register on hope.qcin.org. Fill all 7 parts. Upload portal + mobile app documents. Pay ₹61,360.',color:T.orange},
        {phase:'Month 5–6',action:'Desktop Assessment — respond to NC rounds (two cycles available). Submit complete evidence first time.',color:T.orange},
        {phase:'Month 6–8',action:'Onsite Assessment by NABH assessor. Close onsite NCs (two cycles). Submit feedback.',color:T.orange},
        {phase:'Month 8–9',action:'Certification Committee decision. Receive HCO ELC Certificate (2-year validity).',color:T.green},
        {phase:'Month 9–24',action:'Implement NABH 6th Edition standards (639 OEs). Use portal.nabh.co for full accreditation application.',color:T.gold},
        {phase:'Month 18',action:'Apply for Full NABH Hospital Accreditation via portal.nabh.co — 6 months before ELC expiry.',color:T.gold},
      ].map((p,i) => (
        <div key={i} style={{display:'flex',gap:12,marginBottom:8,alignItems:'flex-start'}}>
          <div style={{minWidth:90,color:p.color,fontWeight:600,fontSize:11,paddingTop:2}}>{p.phase}</div>
          <div style={{flex:1,background:T.panel,borderRadius:8,padding:'8px 12px',border:`1px solid ${p.color}33`,color:T.text,fontSize:12}}>{p.action}</div>
        </div>
      ))}

      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:13,marginBottom:6}}>💼 Post-Accreditation Obligations</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.7}}>
          After ELC certificate: No surveillance visits (certification programme). Apply for renewal at least 6 months before expiry.
          If renewal not applied 3 months before expiry, NABH presumes disinterest and certificate expires — HCO must re-apply fresh.
          Accredited HCO must use NABH mark only as per guidelines and maintain all standards continuously.
        </div>
      </div>
    </div>
  );

  // ── ELC sub-tab router ──
  const ELC_TABS = [
    {key:'overview', label:'📊 Overview'},
    {key:'docs', label:'📂 Documents'},
    {key:'licenses', label:'📋 Licenses'},
    {key:'process', label:'🗺️ Process'},
    {key:'upgrade', label:'⬆️ Upgrade Path'},
  ];

  const renderELCTab = () => {
    switch(hcoElcTab) {
      case 'overview': return renderOverview();
      case 'docs': return renderDocTracker();
      case 'licenses': return renderLicenseTracker();
      case 'process': return renderProcess();
      case 'upgrade': return renderUpgrade();
      default: return renderOverview();
    }
  };

  // ── MAIN HCO TAB RENDER ──
  return (
    <div style={{background:T.bg,minHeight:'100vh',color:T.text}}>
      {/* Mode selector */}
      <div style={{padding:'16px 16px 0',display:'flex',gap:8}}>
        {[
          {key:'elc', label:'📋 ELC Prep', sub:'Entry Level Certification (>50 beds)'},
          {key:'full', label:'🏆 Full Accreditation', sub:'6th Edition — 639 OEs'},
        ].map(m => (
          <button key={m.key} onClick={() => setHcoMode(m.key)}
            style={{
              flex:1, padding:'10px 8px', borderRadius:10, border:'none', cursor:'pointer',
              background: hcoMode === m.key ? T.gold+'22' : T.panel,
              outline: hcoMode === m.key ? `2px solid ${T.gold}` : `1px solid ${T.border}`,
              textAlign:'center'
            }}>
            <div style={{color: hcoMode === m.key ? T.gold : T.text, fontWeight:700, fontSize:12}}>{m.label}</div>
            <div style={{color:T.muted, fontSize:10, marginTop:2}}>{m.sub}</div>
          </button>
        ))}
      </div>

      {hcoMode === 'full' ? (
        renderFullAccredTab()
      ) : (
        <>
          {/* ELC sub-tabs */}
          <div style={{display:'flex',overflowX:'auto',gap:0,padding:'12px 16px 0',borderBottom:`1px solid ${T.border}`}}>
            {ELC_TABS.map(tab => (
              <button key={tab.key} onClick={() => setHcoElcTab(tab.key)}
                style={{
                  padding:'8px 14px', border:'none', cursor:'pointer', whiteSpace:'nowrap',
                  background:'transparent', fontSize:12, fontWeight:600,
                  color: hcoElcTab === tab.key ? T.gold : T.muted,
                  borderBottom: hcoElcTab === tab.key ? `2px solid ${T.gold}` : '2px solid transparent',
                }}>
                {tab.label}
              </button>
            ))}
          </div>

          {/* ELC content */}
          {renderELCTab()}
        </>
      )}
    </div>
  );
};

// ── STEP 4: ADD TO TABS ARRAY ─────────────────────────────────────────────
// In your tabs array, add: { key: 'hco', label: '🏨 HCO ELC' }

// ── STEP 5: ADD TO TAB RENDER SWITCH ─────────────────────────────────────
// case 'hco': return renderHCOTab();

// ── STEP 6: ADD STATE VARIABLES ──────────────────────────────────────────
// Add these to your App() component alongside existing useState declarations:
//
// const [hcoMode, setHcoMode] = useState('elc');
// const [hcoElcTab, setHcoElcTab] = useState('overview');
// const [hcoElcProgress, setHcoElcProgress] = useState({});
// const [hcoLicProgress, setHcoLicProgress] = useState({});
// const [hcoDocFilter, setHcoDocFilter] = useState('all');
// const [hcoDocPart, setHcoDocPart] = useState('all');
