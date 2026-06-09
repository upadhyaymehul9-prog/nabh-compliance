// ============================================================
// SHCO TAB — Add to App.js (accredready.in)
// Two modes: ELC Prep + Full Accreditation Prep
// Author: Dr. Mehul Upadhyay | May 2026
// ============================================================
// USAGE: Paste this entire file's content into App.js
// 1. Add SHCO_ELC_DOCS, SHCO_ELC_LICENSES constants (static data section)
// 2. Add shcoElcProgress, shcoLicProgress state variables
// 3. Add '🏥 SHCO' to tabs array
// 4. Add renderSHCOTab() call in tab render switch
// ============================================================

// ── STEP 1: STATIC DATA (paste near other constants like OE_TIPS) ─────────

const SHCO_ELC_DOCS = [
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
  {id:"036",part:"II",section:"Utilities & Infrastructure",text:"Electrical supply availability",upload:"Both",type:"field"},
  {id:"037",part:"II",section:"Utilities & Infrastructure",text:"Water supplier details",upload:"Both",type:"field"},
  {id:"038",part:"II",section:"Utilities & Infrastructure",text:"Elevators present? (Certificate of Lift License/Safety via Portal)",upload:"Both",type:"field"},
  {id:"039",part:"II",section:"Utilities & Infrastructure",text:"Water portability certificate (IS 10500:2012 via Mobile App)",upload:"Both",type:"field"},
  {id:"040",part:"II",section:"Utilities & Infrastructure",text:"Type of trolleys present at the hospital",upload:"Both",type:"field"},
  {id:"041",part:"II",section:"Utilities & Infrastructure",text:"Ambulance Accessibility",upload:"Both",type:"field"},
  {id:"042",part:"II",section:"Utilities & Infrastructure",text:"Uniform signage system in the Facility",upload:"Both",type:"field"},
  {id:"043",part:"II",section:"Ambulance (if applicable)",text:"List of drugs present in the ambulance",upload:"Mobile",type:"doc"},
  {id:"044",part:"II",section:"Ambulance (if applicable)",text:"Training records and driving license of drivers",upload:"Mobile",type:"doc"},
  {id:"045",part:"II",section:"Ambulance (if applicable)",text:"Training records of doctors deputed in ambulances",upload:"Mobile",type:"doc"},
  {id:"046",part:"II",section:"Ambulance (if applicable)",text:"Training records of nurses deputed in ambulances",upload:"Mobile",type:"doc"},
  {id:"047",part:"II",section:"Ambulance (if applicable)",text:"Training records of technicians deputed in ambulances",upload:"Mobile",type:"doc"},
  {id:"048",part:"II",section:"Land/Building",text:"Land/Rent Agreement or Occupancy Certificate",upload:"Portal",type:"doc"},
  {id:"049",part:"III",section:"Statutory Compliances",text:"Which statutory compliances does the organisation have? (Yes/No for each)",upload:"Mobile",type:"field"},
  {id:"050",part:"III",section:"Statutory Compliances",text:"License Number (for each applicable license)",upload:"Mobile",type:"field"},
  {id:"051",part:"III",section:"Statutory Compliances",text:"License Status (Valid/Expired)",upload:"Mobile",type:"field"},
  {id:"052",part:"III",section:"Statutory Compliances",text:"Issuing Authority",upload:"Mobile",type:"field"},
  {id:"053",part:"III",section:"Statutory Compliances",text:"Expiry Date",upload:"Mobile",type:"field"},
  {id:"054",part:"III",section:"MoU of Outsourced Services",text:"MoU with other Hospital for all outsourced services (upload via Portal)",upload:"Mobile",type:"field"},
  {id:"055",part:"IV",section:"OPD & IPD Data",text:"Number of OPD patients for the past 12 months",upload:"Both",type:"field"},
  {id:"056",part:"IV",section:"OPD & IPD Data",text:"Number of IPD admissions in the past 12 months",upload:"Both",type:"field"},
  {id:"057",part:"IV",section:"OPD & IPD Data",text:"Number of inpatient days in a month (average)",upload:"Both",type:"field"},
  {id:"058",part:"IV",section:"OPD & IPD Data",text:"Number of available bed days",upload:"Both",type:"field"},
  {id:"059",part:"IV",section:"OPD & IPD Data",text:"Average Occupancy Rate",upload:"Both",type:"field"},
  {id:"060",part:"IV",section:"OPD & IPD Data",text:"Number of ICU inpatient days",upload:"Both",type:"field"},
  {id:"061",part:"IV",section:"OPD & IPD Data",text:"Number of available ICU bed days",upload:"Both",type:"field"},
  {id:"062",part:"IV",section:"OPD & IPD Data",text:"Data of past 3 months for monthly average",upload:"Both",type:"field"},
  {id:"063",part:"IV",section:"Scope of Services",text:"Name of service offered",upload:"Both",type:"field"},
  {id:"064",part:"IV",section:"Scope of Services",text:"Full time / Part time / Visiting (type of consultant)",upload:"Both",type:"field"},
  {id:"065",part:"IV",section:"Scope of Services",text:"Doctor Name",upload:"Both",type:"field"},
  {id:"066",part:"IV",section:"Scope of Services",text:"Graduation",upload:"Both",type:"field"},
  {id:"067",part:"IV",section:"Scope of Services",text:"Post-Graduation",upload:"Both",type:"field"},
  {id:"068",part:"IV",section:"Additional Clinical Info",text:"Ten most frequent clinical services where admissions take place",upload:"Both",type:"field"},
  {id:"069",part:"IV",section:"Additional Clinical Info",text:"Ten most frequent diagnoses for in-patients",upload:"Both",type:"field"},
  {id:"070",part:"IV",section:"Additional Clinical Info",text:"Ten most frequent surgical procedures at your hospital",upload:"Both",type:"field"},
  {id:"071",part:"IV",section:"Additional Clinical Info",text:"Type of sterilization modes used in the hospital",upload:"Both",type:"field"},
  {id:"072",part:"IV",section:"OPD & IPD Documents",text:"UHID of 5 patients treated in past 6 months under each clinical service offered",upload:"Mobile",type:"doc"},
  {id:"073",part:"V",section:"Medical Officers",text:"Name",upload:"Portal",type:"field"},
  {id:"074",part:"V",section:"Medical Officers",text:"Designation",upload:"Portal",type:"field"},
  {id:"075",part:"V",section:"Medical Officers",text:"Qualification",upload:"Portal",type:"field"},
  {id:"076",part:"V",section:"Medical Officers",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"077",part:"V",section:"Medical Officers",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"078",part:"V",section:"Medical Officers",text:"Working Department",upload:"Portal",type:"field"},
  {id:"079",part:"V",section:"Nurses",text:"Name",upload:"Portal",type:"field"},
  {id:"080",part:"V",section:"Nurses",text:"Designation",upload:"Portal",type:"field"},
  {id:"081",part:"V",section:"Nurses",text:"Qualification",upload:"Portal",type:"field"},
  {id:"082",part:"V",section:"Nurses",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"083",part:"V",section:"Nurses",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"084",part:"V",section:"Nurses",text:"Working Department",upload:"Portal",type:"field"},
  {id:"085",part:"V",section:"Paramedical Staff",text:"Name",upload:"Portal",type:"field"},
  {id:"086",part:"V",section:"Paramedical Staff",text:"Designation",upload:"Portal",type:"field"},
  {id:"087",part:"V",section:"Paramedical Staff",text:"Qualification",upload:"Portal",type:"field"},
  {id:"088",part:"V",section:"Paramedical Staff",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"089",part:"V",section:"Paramedical Staff",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"090",part:"V",section:"Paramedical Staff",text:"Working Department",upload:"Portal",type:"field"},
  {id:"091",part:"V",section:"Admin & Support Staff",text:"Name",upload:"Portal",type:"field"},
  {id:"092",part:"V",section:"Admin & Support Staff",text:"Designation",upload:"Portal",type:"field"},
  {id:"093",part:"V",section:"Admin & Support Staff",text:"Qualification",upload:"Portal",type:"field"},
  {id:"094",part:"V",section:"Admin & Support Staff",text:"Type of Degree",upload:"Portal",type:"field"},
  {id:"095",part:"V",section:"Admin & Support Staff",text:"Registration Number",upload:"Portal",type:"field"},
  {id:"096",part:"V",section:"Admin & Support Staff",text:"Working Department",upload:"Portal",type:"field"},
  {id:"097",part:"VI",section:"Committee / Coordinator",text:"Documents for any two changes in hospital related to quality & patient safety (certified by Top Management)",upload:"Mobile",type:"doc"},
  {id:"098",part:"VI",section:"Committee / Coordinator",text:"Documents for any five indicators data signed by Top Management",upload:"Mobile",type:"doc"},
  {id:"099",part:"VI",section:"Registration & Billing",text:"Scanned copy of OPD registration/admission form",upload:"Portal",type:"doc"},
  {id:"100",part:"VI",section:"Registration & Billing",text:"Scanned copy of IPD registration/admission form",upload:"Portal",type:"doc"},
  {id:"101",part:"VI",section:"Registration & Billing",text:"Scanned copy of Emergency registration/admission form",upload:"Portal",type:"doc"},
  {id:"102",part:"VI",section:"Registration & Billing",text:"Copy of Basic Tariff List (bed, OT, ICU charges, packages)",upload:"Mobile",type:"doc"},
  {id:"103",part:"VI",section:"Patient & Family Education",text:"Blood and Blood Product Transfusion Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"104",part:"VI",section:"Patient & Family Education",text:"Blood Donation Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"105",part:"VI",section:"Patient & Family Education",text:"Anaesthesia Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"106",part:"VI",section:"Patient & Family Education",text:"Surgery Consent of 3 patients",upload:"Mobile",type:"doc"},
  {id:"107",part:"VI",section:"Patient & Family Education",text:"Training material on safe parenting, nutrition and immunization",upload:"Portal",type:"doc"},
  {id:"108",part:"VI",section:"Patient Related Processes",text:"UHID of any one patient + filled Initial Assessment form (OPD by doctor, IPD by doctor, IPD by nurse, Emergency)",upload:"Mobile",type:"doc"},
  {id:"109",part:"VI",section:"Patient Related Processes",text:"Any 1 MLC or Police intimation form or MLC register scanned copy",upload:"Mobile",type:"doc"},
  {id:"110",part:"VI",section:"Patient Related Processes",text:"Copy of scope of Obstetric Services + UHID with ante natal, maternal nutrition, post-natal care",upload:"Mobile",type:"doc"},
  {id:"111",part:"VI",section:"Patient Related Processes",text:"UHID of any 1 patient + filled assessment sheet (nutritional, growth, immunization)",upload:"Mobile",type:"doc"},
  {id:"112",part:"VI",section:"Patient Related Processes",text:"Copy of Pediatrics service documentation",upload:"Mobile",type:"doc"},
  {id:"113",part:"VI",section:"Patient Related Processes",text:"Register of patients referred/transferred from Inpatient area",upload:"Mobile",type:"doc"},
  {id:"114",part:"VI",section:"Patient Related Processes",text:"Filled patient case sheet of any 1 patient from ICU",upload:"Mobile",type:"doc"},
  {id:"115",part:"VI",section:"Patient Related Processes",text:"Filled patient case sheet of any 1 patient from any 1 ward",upload:"Mobile",type:"doc"},
  {id:"116",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with Pre-anaesthesia assessment format",upload:"Mobile",type:"doc"},
  {id:"117",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with anaesthesia monitoring format",upload:"Mobile",type:"doc"},
  {id:"118",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with post-anaesthesia status monitoring format",upload:"Mobile",type:"doc"},
  {id:"119",part:"VI",section:"Patient Related Processes",text:"Copy of adverse anaesthesia events records in past 3 months (if applicable)",upload:"Mobile",type:"doc"},
  {id:"120",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with preoperative assessment and provisional diagnosis",upload:"Mobile",type:"doc"},
  {id:"121",part:"VI",section:"Patient Related Processes",text:"Copy of any 1 patient case sheet with operative notes and post-operative plan of care",upload:"Mobile",type:"doc"},
  {id:"122",part:"VI",section:"Patient Related Processes",text:"Filled ward discharge summary (all pages) of any one patient",upload:"Mobile",type:"doc"},
  {id:"123",part:"VI",section:"Patient Related Processes",text:"Filled discharge summary (all pages) of any one LAMA patient",upload:"Mobile",type:"doc"},
  {id:"124",part:"VI",section:"Nursing Care",text:"1 copy of nursing documentation (Medication Administration Record)",upload:"Mobile",type:"doc"},
  {id:"125",part:"VI",section:"Nursing Care",text:"Copy of nursing monitoring charts",upload:"Mobile",type:"doc"},
  {id:"126",part:"VI",section:"Nursing Care",text:"Copy of nurses notes",upload:"Mobile",type:"doc"},
  {id:"127",part:"VI",section:"Medication Management",text:"Copies of fridge temperature records of last three months",upload:"Mobile",type:"doc"},
  {id:"128",part:"VI",section:"Medication Management",text:"Scanned list of emergency and high risk medications",upload:"Mobile",type:"doc"},
  {id:"129",part:"VI",section:"Medication Management",text:"Photo of stock of emergency medications",upload:"Mobile",type:"doc"},
  {id:"130",part:"VI",section:"Medication Management",text:"Copies of prescriptions of any 3 patients",upload:"Mobile",type:"doc"},
  {id:"131",part:"VI",section:"Medication Management",text:"Copy of medication order from ICU, Wards, Emergency, Obs & Gyn, Pediatric",upload:"Mobile",type:"doc"},
  {id:"132",part:"VI",section:"Infection Control",text:"Copy of housekeeping checklist for any 3 locations",upload:"Mobile",type:"doc"},
  {id:"133",part:"VI",section:"Infection Control",text:"Photo of autoclaving records indicators",upload:"Mobile",type:"doc"},
  {id:"134",part:"VI",section:"Infection Control",text:"Microbiological surveillance culture report (OT, Labour Room, ICU, NICU - past 3 months)",upload:"Mobile",type:"doc"},
  {id:"135",part:"VI",section:"Infection Control",text:"Records of pre and post exposure prophylaxis provided to staff",upload:"Mobile",type:"doc"},
  {id:"136",part:"VI",section:"Infection Control",text:"Bio Medical Waste (BMW) authorization from Pollution Control Board",upload:"Portal",type:"doc"},
  {id:"137",part:"VI",section:"Infection Control",text:"MoU with outsourced bio medical waste agency",upload:"Portal",type:"doc"},
  {id:"138",part:"VI",section:"Infection Control",text:"Photo of display of work instructions for segregation and handling of BMW",upload:"Mobile",type:"doc"},
  {id:"139",part:"VI",section:"Infection Control",text:"Record of fee, documents & report submitted to authorities for BMW on stipulated dates",upload:"Mobile",type:"doc"},
  {id:"140",part:"VI",section:"Management Process",text:"Scanned copy of documented hospital mission",upload:"Portal",type:"doc"},
  {id:"141",part:"VI",section:"Management Process",text:"Organisation's organogram",upload:"Portal",type:"doc"},
  {id:"142",part:"VI",section:"Management Process",text:"Handling record of patient grievances/complaints",upload:"Mobile",type:"doc"},
  {id:"143",part:"VI",section:"Management Process",text:"Documents of composition of all committees (Quality & Safety, IPC, P&T, Blood Transfusion, Medical Records etc.)",upload:"Portal",type:"doc"},
  {id:"144",part:"VI",section:"Management Process",text:"Copy of terms of reference of all the committees",upload:"Portal",type:"doc"},
  {id:"145",part:"VI",section:"Management Process",text:"Copy of minutes of meeting of all committees for last 3 months",upload:"Mobile",type:"doc"},
  {id:"146",part:"VI",section:"Management Process",text:"Scanned data of Medication Error and Adverse Drug Reaction of last 3 months",upload:"Mobile",type:"doc"},
  {id:"147",part:"VI",section:"Management Process",text:"Scanned Root Cause Analysis (RCA) and CAPA of Medication Error and ADR of last 3 months",upload:"Mobile",type:"doc"},
  {id:"148",part:"VI",section:"Management Process",text:"Scope of services (Laboratory and Imaging)",upload:"Mobile",type:"doc"},
  {id:"149",part:"VI",section:"Management Process",text:"Defined turnaround time for tests (Laboratory and Imaging)",upload:"Mobile",type:"doc"},
  {id:"150",part:"VI",section:"Management Process",text:"Critical result reporting register (test ready time, communicated time, name of individual conveyed to)",upload:"Mobile",type:"doc"},
  {id:"151",part:"VI",section:"Management Process",text:"Blood transfusion records (orders, pre-transfusion medications, cross matching, blood product label, monitoring - at least 3)",upload:"Mobile",type:"doc"},
  {id:"152",part:"VI",section:"Management Process",text:"Scanned filled Blood transfusion reaction form in past 3 months",upload:"Mobile",type:"doc"},
  {id:"153",part:"VI",section:"Management Process",text:"Scanned copy of Blood transfusion committee's minutes with discussed reaction and CAPA",upload:"Portal",type:"doc"},
  {id:"154",part:"VI",section:"Safety Management",text:"Filled WHO Surgical Safety Checklist used for every surgery (any 3)",upload:"Mobile",type:"doc"},
  {id:"155",part:"VI",section:"Safety Management",text:"Scanned copy of facility inspection rounds",upload:"Mobile",type:"doc"},
  {id:"156",part:"VI",section:"Safety Management",text:"Copy of document of maintenance plan of medical gases and vacuum systems",upload:"Mobile",type:"doc"},
  {id:"157",part:"VI",section:"Safety Management",text:"Copy of floor plans with exit routes",upload:"Mobile",type:"doc"},
  {id:"158",part:"VI",section:"Record Management",text:"Checklist for completeness for medical records",upload:"Mobile",type:"doc"},
  {id:"159",part:"VI",section:"Record Management",text:"Filled case sheet with doctors name, signature, date & time (1 from each: ICU, Operative Patient, Ward, Emergency, Obs & Gyn)",upload:"Mobile",type:"doc"},
  {id:"160",part:"VII",section:"SOPs & Procedures",text:"Procedure guide for collection, identification, handling, transportation, processing and disposal of specimens",upload:"Portal",type:"doc"},
  {id:"161",part:"VII",section:"SOPs & Procedures",text:"Process addressing discharge of all patients including MLC cases and patients leaving against medical advice (LAMA)",upload:"Portal",type:"doc"},
  {id:"162",part:"VII",section:"SOPs & Procedures",text:"Documented procedure addressing care of patients in emergency including medico-legal cases",upload:"Portal",type:"doc"},
  {id:"163",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures for rational use of blood and blood products",upload:"Portal",type:"doc"},
  {id:"164",part:"VII",section:"SOPs & Procedures",text:"Documented procedures governing transfusion of blood and blood products",upload:"Portal",type:"doc"},
  {id:"165",part:"VII",section:"SOPs & Procedures",text:"Documented procedure for administration of anaesthesia",upload:"Portal",type:"doc"},
  {id:"166",part:"VII",section:"SOPs & Procedures",text:"Defined criterion to transfer the patient from the recovery area",upload:"Portal",type:"doc"},
  {id:"167",part:"VII",section:"SOPs & Procedures",text:"Documented procedure addressing prevention of adverse events (wrong site, wrong patient, wrong surgery)",upload:"Portal",type:"doc"},
  {id:"168",part:"VII",section:"SOPs & Procedures",text:"Documented procedure incorporating purchase, storage, prescription and dispensation of medications",upload:"Portal",type:"doc"},
  {id:"169",part:"VII",section:"SOPs & Procedures",text:"Documented procedures addressing procurement and usage of implantable prostheses",upload:"Portal",type:"doc"},
  {id:"170",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures for storage of medications",upload:"Portal",type:"doc"},
  {id:"171",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures governing usage of radioactive drugs",upload:"Portal",type:"doc"},
  {id:"172",part:"VII",section:"SOPs & Procedures",text:"Policies and procedures for safe storage, preparation, handling, distribution and disposal of radioactive drugs",upload:"Portal",type:"doc"},
  {id:"173",part:"VII",section:"SOPs & Procedures",text:"Infection control manual, periodically updated, with surveillance activities",upload:"Portal",type:"doc"},
  {id:"174",part:"VII",section:"SOPs & Procedures",text:"Documented operational and maintenance plan for clinical and support service equipment",upload:"Portal",type:"doc"},
  {id:"175",part:"VII",section:"SOPs & Procedures",text:"Documented safe exit plan in case of fire and non-fire emergencies",upload:"Portal",type:"doc"},
  {id:"176",part:"VII",section:"SOPs & Procedures",text:"Well-defined staff recruitment process",upload:"Portal",type:"doc"},
  {id:"177",part:"VII",section:"SOPs & Procedures",text:"Documented disciplinary and grievance handling procedure",upload:"Portal",type:"doc"},
  {id:"178",part:"VII",section:"SOPs & Procedures",text:"Documented policies and procedures for maintaining confidentiality, integrity and security of records",upload:"Portal",type:"doc"},
  {id:"179",part:"VII",section:"SOPs & Procedures",text:"Documented procedures for retention time of medical records, data and information",upload:"Portal",type:"doc"},
  {id:"180",part:"VII",section:"SOPs & Procedures",text:"Defined process to whom the patient record can be released",upload:"Portal",type:"doc"},
  {id:"181",part:"VII",section:"SOPs & Procedures",text:"Procedure on destruction of medical records",upload:"Portal",type:"doc"},
];

const SHCO_ELC_LICENSES = [
  {id:"LIC001",cat:"Mandatory",name:"Legal status - Shops and Commercial Establishments Act",appl:"All"},
  {id:"LIC002",cat:"Mandatory",name:"State Pollution Control Board (SPCB) Consent",appl:"All"},
  {id:"LIC003",cat:"Mandatory",name:"MoU with BMW collecting Agency",appl:"All"},
  {id:"LIC004",cat:"Mandatory",name:"Pollution Control Board License",appl:"All"},
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

// ELC 2nd Edition — OE summary (for display only, no scoring)
const SHCO_ELC_OE_SUMMARY = [
  {ch:"AAC",name:"Access, Assessment & Continuity",standards:7,oes:29,core:20,commitment:2,excellence:7},
  {ch:"COP",name:"Care of Patients",standards:10,oes:44,core:24,commitment:9,excellence:11},
  {ch:"MOM",name:"Management of Medication",standards:7,oes:28,core:20,commitment:5,excellence:3},
  {ch:"PRE",name:"Patient Rights & Education",standards:2,oes:17,core:14,commitment:1,excellence:2},
  {ch:"IPC",name:"Infection Prevention & Control",standards:2,oes:12,core:7,commitment:3,excellence:2},
  {ch:"PSQ",name:"Patient Safety & Quality Improvement",standards:2,oes:8,core:4,commitment:2,excellence:2},
  {ch:"ROM",name:"Responsibilities of Management",standards:4,oes:12,core:4,commitment:4,excellence:4},
  {ch:"FMS",name:"Facility Management & Safety",standards:4,oes:13,core:12,commitment:1,excellence:0},
  {ch:"HRM",name:"Human Resource Management",standards:5,oes:15,core:9,commitment:6,excellence:0},
  {ch:"IMS",name:"Information Management System",standards:3,oes:11,core:8,commitment:2,excellence:1},
];

// ELC Process steps
const SHCO_ELC_PROCESS = [
  {step:1,name:"Register on HOPE Portal",url:"nabh.qcin.org",desc:"Go to nabh.qcin.org → Register → Fill hospital details",output:"Login credentials + application ID"},
  {step:2,name:"Fill 7-Part Questionnaire",url:"nabh.qcin.org",desc:"Complete all 7 parts of the HOPE questionnaire online — General Info, Physical Infrastructure, Statutory, Clinical, Staffing, Quality, Documentation",output:"Completed questionnaire submission"},
  {step:3,name:"Upload Documents",url:"nabh.qcin.org",desc:"Upload portal documents via web portal + mobile app documents via HOPE mobile app",output:"Document submission complete"},
  {step:4,name:"Pay Fee",url:"nabh.qcin.org",desc:"Pay applicable certification fee based on bed strength (+ 18% GST). See nabh.co for current fee structure.",output:"Payment receipt + application confirmed"},
  {step:5,name:"Desktop Assessment (DA)",url:"",desc:"NABH desk team reviews all submitted documents. NCs raised online. You get ONE chance to respond — no second round.",output:"NC closure letter"},
  {step:6,name:"Onsite Assessment",url:"",desc:"Date allotted after successful DA NC closure. Assessor visits physically. NCs raised on-site.",output:"Onsite assessment report"},
  {step:7,name:"Certification Committee",url:"",desc:"Final report submitted to Certification Committee. Committee approves or rejects.",output:"Approval / Rejection letter"},
  {step:8,name:"Digital Certificate",url:"",desc:"Printable digital certificate issued. Valid for 2 years. Apply for renewal 6 months before expiry.",output:"NABH ELC Certificate"},
];


// ── STEP 2: STATE VARIABLES (paste inside App function with other useState) ──
// const [shcoMode, setShcoMode] = useState('elc'); // 'elc' | 'full'
// const [shcoElcTab, setShcoElcTab] = useState('overview'); // 'overview'|'docs'|'licenses'|'questionnaire'|'process'|'upgrade'
// const [shcoElcProgress, setShcoElcProgress] = useState({}); // {docId: 'pending'|'ready'|'na'}
// const [shcoLicProgress, setShcoLicProgress] = useState({}); // {licId: 'pending'|'obtained'|'na'}
// const [shcoBeds, setShcoBeds] = useState('');
// const [shcoDocFilter, setShcoDocFilter] = useState('all'); // 'all'|'pending'|'ready'
// const [shcoDocPart, setShcoDocPart] = useState('all');


// ── STEP 3: RENDER FUNCTION (paste inside App component) ─────────────────

const renderSHCOTab = () => {
  const T = {
    bg:"#050e1a", panel:"#081525", panel2:"#0c1e35", border:"#0f2640",
    gold:"#c9a84c", red:"#e05a5a", orange:"#f4a441", green:"#4caf7d",
    blue:"#4fc3f7", muted:"#3a5870", text:"#c8dcea", white:"#eef4f9"
  };

// ── ELC Doc Progress ──
  const docStatus = (id) => shcoElcProgress[id] || 'pending';
  const licStatus = (id) => shcoLicProgress[id] || 'pending';

  const setDocStatus = (id, status) => {
    setShcoElcProgress(prev => ({ ...prev, [id]: status }));
  };
  const setLicStatus = (id, status) => {
    setShcoLicProgress(prev => ({ ...prev, [id]: status }));
  };

  // Stats
  const docsDone = SHCO_ELC_DOCS.filter(d => docStatus(d.id) === 'ready').length;
  const docsNA = SHCO_ELC_DOCS.filter(d => docStatus(d.id) === 'na').length;
  const docsApplicable = SHCO_ELC_DOCS.length - docsNA;
  const docsPct = docsApplicable > 0 ? Math.round((docsDone / docsApplicable) * 100) : 0;

  const licDone = SHCO_ELC_LICENSES.filter(l => licStatus(l.id) === 'obtained').length;
  const licNA = SHCO_ELC_LICENSES.filter(l => licStatus(l.id) === 'na').length;
  const licApplicable = SHCO_ELC_LICENSES.length - licNA;
  const licPct = licApplicable > 0 ? Math.round((licDone / licApplicable) * 100) : 0;

  const overallPct = Math.round((docsPct + licPct) / 2);

  // Filtered docs
  const filteredDocs = SHCO_ELC_DOCS.filter(d => {
    const partMatch = shcoDocPart === 'all' || d.part === shcoDocPart;
    const statusMatch = shcoDocFilter === 'all' || docStatus(d.id) === shcoDocFilter;
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

  const statusColor = (s) => s === 'ready' || s === 'obtained' ? T.green : s === 'na' ? T.muted : T.orange;
  const statusLabel = (s, type='doc') => {
    if (type === 'lic') return s === 'obtained' ? '✅ Obtained' : s === 'na' ? '➖ N/A' : '⏳ Pending';
    return s === 'ready' ? '✅ Ready' : s === 'na' ? '➖ N/A' : '⏳ Pending';
  };

  // ── SHCO Full Accreditation summary (uses shco_scores table)
  const renderFullAccredTab = () => (
    <div style={{padding:16}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}44`,borderRadius:12,padding:20,marginBottom:16}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:16,marginBottom:8}}>🏆 SHCO Full Accreditation — 3rd Edition (August 2022)</div>
        <div style={{color:T.text,fontSize:13,lineHeight:1.6}}>
          Full accreditation for Small Healthcare Organisations. Assessed against 408 Objective Elements across 71 standards in 10 chapters.
        </div>
        <div style={{display:'flex',gap:12,flexWrap:'wrap',marginTop:16}}>
          {[
            {label:'Standards',val:'71'},
            {label:'Total OEs',val:'408'},
            {label:'Chapters',val:'10'},
            {label:'Validity',val:'4 Years'},
          ].map(s => (
            <div key={s.label} style={{background:T.panel2,borderRadius:8,padding:'10px 16px',textAlign:'center',border:`1px solid ${T.border}`}}>
              <div style={{color:T.gold,fontWeight:700,fontSize:20}}>{s.val}</div>
              <div style={{color:T.muted,fontSize:11}}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Chapter breakdown */}
      <div style={{color:T.gold,fontWeight:600,fontSize:13,marginBottom:10}}>Chapter Breakdown — 3rd Edition</div>
      <div style={{display:'grid',gap:6}}>
        {[
          {ch:'AAC',name:'Access, Assessment & Continuity',stds:8,oes:48},
          {ch:'COP',name:'Care of Patients',stds:13,oes:82},
          {ch:'MOM',name:'Management of Medication',stds:9,oes:52},
          {ch:'PRE',name:'Patient Rights & Education',stds:6,oes:39},
          {ch:'HIC',name:'Hospital Infection Control',stds:6,oes:36},
          {ch:'PSQ',name:'Patient Safety & Quality',stds:5,oes:28},
          {ch:'ROM',name:'Responsibilities of Management',stds:4,oes:19},
          {ch:'FMS',name:'Facility Management & Safety',stds:5,oes:29},
          {ch:'HRM',name:'Human Resource Management',stds:9,oes:45},
          {ch:'IMS',name:'Information Management System',stds:6,oes:30},
        ].map(c => (
          <div key={c.ch} style={{background:T.panel,borderRadius:8,padding:'10px 14px',display:'flex',justifyContent:'space-between',alignItems:'center',border:`1px solid ${T.border}`}}>
            <div>
              <span style={{color:T.gold,fontWeight:700,fontSize:12,marginRight:8}}>{c.ch}</span>
              <span style={{color:T.text,fontSize:12}}>{c.name}</span>
            </div>
            <div style={{display:'flex',gap:12,fontSize:11}}>
              <span style={{color:T.muted}}>{c.stds} Stds</span>
              <span style={{color:T.blue,fontWeight:600}}>{c.oes} OEs</span>
            </div>
          </div>
        ))}
      </div>

      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.orange}44`}}>
        <div style={{color:T.orange,fontWeight:600,fontSize:13,marginBottom:6}}>⚠️ OE Scoring — Coming Soon</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.6}}>
          The 408 OEs from the 3rd Edition SHCO standards are ready in the database. OE-level scoring for Full Accreditation will be enabled in the next update.
          <br/><br/>
          To prepare: Score each OE on 1–5 scale. NABH requires all 10 chapters ≥ 80%, no OE ≤ 2, and no chapter below threshold.
        </div>
      </div>
    </div>
  );

  // ── OVERVIEW sub-tab ──
  const renderOverview = () => {
    return (
      <div style={{padding:16,display:'flex',flexDirection:'column',gap:16}}>

        {/* 2nd Edition notice */}
        <div style={{background:'#1a0a00',border:`1px solid ${T.orange}`,borderRadius:10,padding:14}}>
          <div style={{color:T.orange,fontWeight:700,fontSize:13,marginBottom:4}}>📋 2nd Edition Active — March 2026</div>
          <div style={{color:T.text,fontSize:12,lineHeight:1.6}}>
            ELC now uses the unified 2nd Edition standards (Jan 2026). New applicants from March 2026 must apply via <strong style={{color:T.gold}}>nabh.qcin.org</strong>.
            1st Edition (149 OEs) is no longer valid for new applications.
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

        {/* Fee Reference */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:12}}>💰 Certification Fee</div>
          <div style={{background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
            <div style={{color:T.muted,fontSize:13,marginBottom:10}}>Fees vary by bed strength and are updated periodically by NABH.</div>
            <a href="https://nabh.co/accreditations-certifications-and-empanelments/" target="_blank" rel="noopener noreferrer" style={{color:T.blue,fontWeight:600,fontSize:13,textDecoration:'underline'}}>
              View current fee structure on the official NABH website →
            </a>
            <div style={{fontSize:11,color:T.muted,marginTop:10}}>
              18% GST applicable. Fee is non-refundable and non-transferable. Focus assessment and re-issue charges apply separately.
            </div>
          </div>
        </div>

        {/* Assessment Matrix */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:12}}>📐 What Gets Assessed — By Cycle</div>
          <div style={{display:'grid',gap:8}}>
            {[
              {cycle:'New Applicant — Cycle 1',beds:'1–50 beds',assessed:'Core only (124 OEs)',color:T.green},
              {cycle:'First Renewal — Cycle 2',beds:'1–50 beds',assessed:'Core + Commitment (160 OEs)',color:T.orange},
              {cycle:'Second Renewal+ — Cycle 3',beds:'1–50 beds',assessed:'Core + Commitment + Excellence (189 OEs)',color:T.gold},
              {cycle:'New Applicant — Cycle 1',beds:'51+ beds',assessed:'Core + Commitment (160 OEs)',color:T.blue},
            ].map((r,i) => (
              <div key={i} style={{background:T.panel2,borderRadius:8,padding:'10px 14px',border:`1px solid ${r.color}33`,display:'flex',justifyContent:'space-between',alignItems:'center',flexWrap:'wrap',gap:6}}>
                <div>
                  <div style={{color:r.color,fontWeight:600,fontSize:12}}>{r.cycle}</div>
                  <div style={{color:T.muted,fontSize:11}}>{r.beds}</div>
                </div>
                <div style={{color:T.text,fontSize:12,fontWeight:500}}>{r.assessed}</div>
              </div>
            ))}
          </div>
        </div>

        {/* ELC OE Summary */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:14,marginBottom:12}}>📖 2nd Edition — 189 OEs Across 10 Chapters</div>
          <div style={{display:'grid',gap:6}}>
            {SHCO_ELC_OE_SUMMARY.map(c => (
              <div key={c.ch} style={{background:T.panel2,borderRadius:8,padding:'8px 12px',border:`1px solid ${T.border}`}}>
                <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:4}}>
                  <div>
                    <span style={{color:T.gold,fontWeight:700,fontSize:11,marginRight:6}}>{c.ch}</span>
                    <span style={{color:T.text,fontSize:11}}>{c.name}</span>
                  </div>
                  <span style={{color:T.blue,fontSize:11,fontWeight:600}}>{c.oes} OEs</span>
                </div>
                <div style={{display:'flex',gap:6,flexWrap:'wrap'}}>
                  <span style={{fontSize:10,padding:'1px 6px',borderRadius:8,background:T.green+'22',color:T.green}}>Core: {c.core}</span>
                  <span style={{fontSize:10,padding:'1px 6px',borderRadius:8,background:T.orange+'22',color:T.orange}}>Commitment: {c.commitment}</span>
                  <span style={{fontSize:10,padding:'1px 6px',borderRadius:8,background:T.gold+'22',color:T.gold}}>Excellence: {c.excellence}</span>
                </div>
              </div>
            ))}
          </div>
          <div style={{marginTop:10,color:T.muted,fontSize:11,textAlign:'center'}}>Source: NABH Certification Standards for Entry Level Hospital — 2nd Edition (Jan 2026)</div>
        </div>
      </div>
    );
  };

  // ── DOCUMENT TRACKER sub-tab ──
  const renderDocTracker = () => {
    const sections = [...new Set(filteredDocs.map(d => d.section))];
    return (
      <div style={{padding:16}}>
        {/* Stats bar */}
        <div style={{display:'flex',gap:8,marginBottom:12,flexWrap:'wrap'}}>
          {[
            {label:`✅ Ready: ${docsDone}`,color:T.green},
            {label:`⏳ Pending: ${SHCO_ELC_DOCS.length - docsDone - docsNA}`,color:T.orange},
            {label:`➖ N/A: ${docsNA}`,color:T.muted},
          ].map(s => (
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:11,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>

        {/* Filters */}
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          <select value={shcoDocPart} onChange={e => setShcoDocPart(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}>
            <option value="all">All Parts</option>
            {parts.map(p => <option key={p} value={p}>Part {p}</option>)}
          </select>
          <select value={shcoDocFilter} onChange={e => setShcoDocFilter(e.target.value)}
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
                      border:`1px solid ${s==='ready'?T.green:s==='na'?T.border:T.border}`,
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
    const mandatory = SHCO_ELC_LICENSES.filter(l => l.cat === 'Mandatory');
    const aerb = SHCO_ELC_LICENSES.filter(l => l.cat === 'AERB');
    return (
      <div style={{padding:16}}>
        {/* Stats */}
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          {[
            {label:`✅ Obtained: ${licDone}`,color:T.green},
            {label:`⏳ Pending: ${SHCO_ELC_LICENSES.length - licDone - licNA}`,color:T.orange},
            {label:`➖ N/A: ${licNA}`,color:T.muted},
          ].map(s => (
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:11,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
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
                <div style={{color:T.text,fontSize:12,marginBottom:6}}>{lic.name}</div>
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
        <div style={{color:T.muted,fontSize:11,marginBottom:10}}>These are applicable only if your SHCO provides the specific imaging/radiation service.</div>
        <div style={{display:'flex',flexDirection:'column',gap:6}}>
          {aerb.map(lic => {
            const s = licStatus(lic.id);
            return (
              <div key={lic.id} style={{
                background:T.panel,borderRadius:8,padding:'10px 12px',
                border:`1px solid ${s==='obtained'?T.green:s==='na'?T.border:T.border}`,
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
      <div style={{background:'#0a1200',border:`1px solid ${T.green}44`,borderRadius:10,padding:12,marginBottom:16}}>
        <div style={{color:T.green,fontWeight:600,fontSize:12,marginBottom:4}}>⚠️ Key Change — 2nd Edition</div>
        <div style={{color:T.text,fontSize:12}}>Desktop Assessment now has a <strong>single NC closure cycle only</strong>. There is no second chance to respond. Submit complete NC responses the first time.</div>
      </div>

      <div style={{display:'flex',flexDirection:'column',gap:0}}>
        {SHCO_ELC_PROCESS.map((step, idx) => (
          <div key={step.step} style={{display:'flex',gap:12}}>
            {/* Timeline line */}
            <div style={{display:'flex',flexDirection:'column',alignItems:'center',width:32,flexShrink:0}}>
              <div style={{width:32,height:32,borderRadius:'50%',background:T.gold,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700,fontSize:13,color:T.bg,flexShrink:0}}>
                {step.step}
              </div>
              {idx < SHCO_ELC_PROCESS.length - 1 && (
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
        <div style={{color:T.gold,fontWeight:700,fontSize:15,marginBottom:8}}>🚀 The Journey: ELC → Full SHCO Accreditation</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.7}}>
          Entry Level Certification is the first step. After 2 years, SHCOs can upgrade to Full SHCO Accreditation (3rd Edition) — a significantly more rigorous programme that opens doors to premium empanelments, higher CGHS reimbursements, and community trust.
        </div>
      </div>

      {/* Comparison table */}
      <div style={{color:T.gold,fontWeight:600,fontSize:13,marginBottom:10}}>ELC vs Full Accreditation — Key Differences</div>
      <div style={{overflowX:'auto',marginBottom:16}}>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:12}}>
          <thead>
            <tr>
              {['Parameter','ELC (2nd Ed.)','Full Accreditation (3rd Ed.)'].map(h => (
                <th key={h} style={{padding:'8px 12px',background:T.panel,color:T.gold,fontWeight:600,textAlign:'left',border:`1px solid ${T.border}`}}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {[
              ['Standards',46,71],
              ['Objective Elements',189,408],
              ['Validity','2 years','4 years'],
              ['Process','Desktop + Onsite','Desktop + Onsite + Surveillance'],
              ['Fee','See nabh.co','See nabh.co'],
              ['Portal','nabh.qcin.org','portal.nabh.co'],
              ['Assessors','1–2','2–3'],
            ].map((row, i) => (
              <tr key={i} style={{background: i%2===0 ? T.panel : T.panel2}}>
                <td style={{padding:'8px 12px',color:T.muted,border:`1px solid ${T.border}`,fontWeight:600}}>{row[0]}</td>
                <td style={{padding:'8px 12px',color:T.text,border:`1px solid ${T.border}`}}>{row[1]}</td>
                <td style={{padding:'8px 12px',color:T.gold,border:`1px solid ${T.border}`}}>{row[2]}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Upgrade timeline */}
      <div style={{color:T.gold,fontWeight:600,fontSize:13,marginBottom:10}}>Recommended Timeline</div>
      {[
        {phase:'Month 1–3',action:'Start ELC preparation — documents, licenses, questionnaire',color:T.blue},
        {phase:'Month 4',action:'Submit ELC application on nabh.qcin.org',color:T.blue},
        {phase:'Month 5–6',action:'Desktop Assessment + NC closure (one chance only)',color:T.orange},
        {phase:'Month 6–7',action:'Onsite Assessment',color:T.orange},
        {phase:'Month 8',action:'Certification Committee — ELC Certificate received',color:T.green},
        {phase:'Month 8–18',action:'Implement SHCO 3rd Edition standards (408 OEs) for full accreditation',color:T.gold},
        {phase:'Month 19–24',action:'Apply for Full SHCO Accreditation via portal.nabh.co',color:T.gold},
      ].map((p,i) => (
        <div key={i} style={{display:'flex',gap:12,marginBottom:8,alignItems:'flex-start'}}>
          <div style={{minWidth:90,color:p.color,fontWeight:600,fontSize:11,paddingTop:2}}>{p.phase}</div>
          <div style={{flex:1,background:T.panel,borderRadius:8,padding:'8px 12px',border:`1px solid ${p.color}33`,color:T.text,fontSize:12}}>{p.action}</div>
        </div>
      ))}

      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:13,marginBottom:6}}>💼 For Consultants (Rajesh Model)</div>
        <div style={{color:T.text,fontSize:12,lineHeight:1.7}}>
          Managing 10+ SHCOs? Track each SHCO independently. Use the Document Tracker and License Tracker per facility. 
          The goal: get all SHCOs ELC-certified within 8 months, then upsell to Full Accreditation. 
          At ₹2,999/month, 10 SHCOs = ₹29,990/month recurring — fully justified by the preparation support you're providing.
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
    switch(shcoElcTab) {
      case 'overview': return renderOverview();
      case 'docs': return renderDocTracker();
      case 'licenses': return renderLicenseTracker();
      case 'process': return renderProcess();
      case 'upgrade': return renderUpgrade();
      default: return renderOverview();
    }
  };

  // ── MAIN SHCO TAB RENDER ──
  return (
    <div style={{background:T.bg,minHeight:'100vh',color:T.text}}>
      {/* Mode selector */}
      <div style={{padding:'16px 16px 0',display:'flex',gap:8}}>
        {[
          {key:'elc', label:'📋 ELC Prep', sub:'Entry Level Certification'},
          {key:'full', label:'🏆 Full Accreditation', sub:'3rd Edition — 408 OEs'},
        ].map(m => (
          <button key={m.key} onClick={() => setShcoMode(m.key)}
            style={{
              flex:1, padding:'10px 8px', borderRadius:10, border:'none', cursor:'pointer',
              background: shcoMode === m.key ? T.gold+'22' : T.panel,
              outline: shcoMode === m.key ? `2px solid ${T.gold}` : `1px solid ${T.border}`,
              textAlign:'center'
            }}>
            <div style={{color: shcoMode === m.key ? T.gold : T.text, fontWeight:700, fontSize:12}}>{m.label}</div>
            <div style={{color:T.muted, fontSize:10, marginTop:2}}>{m.sub}</div>
          </button>
        ))}
      </div>

      {shcoMode === 'full' ? (
        renderFullAccredTab()
      ) : (
        <>
          {/* ELC sub-tabs */}
          <div style={{display:'flex',overflowX:'auto',gap:0,padding:'12px 16px 0',borderBottom:`1px solid ${T.border}`}}>
            {ELC_TABS.map(tab => (
              <button key={tab.key} onClick={() => setShcoElcTab(tab.key)}
                style={{
                  padding:'8px 14px', border:'none', cursor:'pointer', whiteSpace:'nowrap',
                  background:'transparent', fontSize:12, fontWeight:600,
                  color: shcoElcTab === tab.key ? T.gold : T.muted,
                  borderBottom: shcoElcTab === tab.key ? `2px solid ${T.gold}` : '2px solid transparent',
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
// In your tabs array, add: { key: 'shco', label: '🏥 SHCO' }

// ── STEP 5: ADD TO TAB RENDER SWITCH ─────────────────────────────────────
// case 'shco': return renderSHCOTab();

// ── STEP 6: ADD STATE VARIABLES ──────────────────────────────────────────
// Add these to your App() component alongside existing useState declarations:
//
// const [shcoMode, setShcoMode] = useState('elc');
// const [shcoElcTab, setShcoElcTab] = useState('overview');
// const [shcoElcProgress, setShcoElcProgress] = useState({});
// const [shcoLicProgress, setShcoLicProgress] = useState({});
// const [shcoBeds, setShcoBeds] = useState('');
// const [shcoDocFilter, setShcoDocFilter] = useState('all');
// const [shcoDocPart, setShcoDocPart] = useState('all');
