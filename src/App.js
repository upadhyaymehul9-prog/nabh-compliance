import { useState, useEffect, useCallback } from "react";
import { createClient } from "@supabase/supabase-js";
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, Tooltip, ReferenceLine, ResponsiveContainer, CartesianGrid } from "recharts";
import jsPDF from 'jspdf';

const supabase = createClient(
  "https://tbptllgcjtiiqspxqcde.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRicHRsbGdjanRpaXFzcHhxY2RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY2NjkzNjAsImV4cCI6MjA5MjI0NTM2MH0.4CPgNp6ytVNRmTU0FJbu2io94QJmsAow5im-vGtoRAU",
  { auth: { flowType: "implicit" } }
);

// ── SHCO ELC Static Data ─────────────────────────────────────────────────
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

const SHCO_FEE_SLABS = [
  {label:"Up to 5 beds",beds:[1,5],fee:21000,discounted:null,discountTill:null},
  {label:"6–20 beds",beds:[6,20],fee:40000,discounted:30000,discountTill:"30 Sep 2026"},
  {label:"21–50 beds",beds:[21,50],fee:80000,discounted:48000,discountTill:"30 Sep 2026"},
];

const SHCO_ELC_PROCESS = [
  {step:1,name:"Register on HOPE Portal",url:"nabh.qcin.org",desc:"Go to nabh.qcin.org → Register → Fill hospital details",output:"Login credentials + application ID"},
  {step:2,name:"Fill 7-Part Questionnaire",url:"nabh.qcin.org",desc:"Complete all 7 parts of the HOPE questionnaire online — General Info, Physical Infrastructure, Statutory, Clinical, Staffing, Quality, Documentation",output:"Completed questionnaire submission"},
  {step:3,name:"Upload Documents",url:"nabh.qcin.org",desc:"Upload portal documents via web portal + mobile app documents via HOPE mobile app",output:"Document submission complete"},
  {step:4,name:"Pay Fee",url:"nabh.qcin.org",desc:"Pay applicable certification fee based on bed strength (+ 18% GST). Discount valid till 30 Sep 2026.",output:"Payment receipt + application confirmed"},
  {step:5,name:"Desktop Assessment (DA)",url:"",desc:"NABH desk team reviews all submitted documents. NCs raised online. You get ONE chance to respond — no second round.",output:"NC closure letter"},
  {step:6,name:"Onsite Assessment",url:"",desc:"Date allotted after successful DA NC closure. Assessor visits physically. NCs raised on-site.",output:"Onsite assessment report"},
  {step:7,name:"Certification Committee",url:"",desc:"Final report submitted to Certification Committee. Committee approves or rejects.",output:"Approval / Rejection letter"},
  {step:8,name:"Digital Certificate",url:"",desc:"Printable digital certificate issued. Valid for 2 years. Apply for renewal 6 months before expiry.",output:"NABH ELC Certificate"},
];

// ── HCO ELC Static Data ─────────────────────────────────────────────────
const HCO_ELC_DOCS = [
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
  {id:"076",part:"III",section:"Statutory Compliances",text:"Which statutory compliances does the organisation have? (Yes/No for each)",upload:"Mobile",type:"field"},
  {id:"077",part:"III",section:"Statutory Compliances",text:"License Number (for each applicable license)",upload:"Mobile",type:"field"},
  {id:"078",part:"III",section:"Statutory Compliances",text:"License Status (Valid/Expired)",upload:"Mobile",type:"field"},
  {id:"079",part:"III",section:"Statutory Compliances",text:"Issuing Authority",upload:"Mobile",type:"field"},
  {id:"080",part:"III",section:"Statutory Compliances",text:"Expiry Date",upload:"Mobile",type:"field"},
  {id:"081",part:"III",section:"MoU of Outsourced Services",text:"MoU with other Hospital for all outsourced services (upload via Portal)",upload:"Portal",type:"field"},
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

const HCO_ELC_PROCESS = [
  {step:1,name:"Register on HOPE Portal",url:"hope.qcin.org",desc:"Go to www.hope.qcin.org → Click Register → Fill Hospital User Registration Form (Hospital name, SPOC details, State, total sanctioned beds)",output:"Login credentials sent to registered email"},
  {step:2,name:"Fill 7-Part Questionnaire",url:"hope.qcin.org",desc:"Complete all 7 parts on the web portal: General Info, Physical Infrastructure, Statutory Compliances, Clinical Services, Hospital Staffing, Quality Improvement Process, Documentation. Save progress at each step.",output:"Completed questionnaire submission (cannot edit after Final Submit)"},
  {step:3,name:"Upload Documents",url:"hope.qcin.org",desc:"Portal documents → upload via web portal (Upload any file icon). Mobile documents → upload via HOPE Android app (View Uploaded File icon). Save on portal first. Cannot use both simultaneously.",output:"Document submission complete"},
  {step:4,name:"Pay Fee",url:"hope.qcin.org",desc:"Pay HCO ELC fee of ₹52,000 + 18% GST = ₹61,360 total. Fee is non-refundable and non-transferable. Once paid, application moves to DA team.",output:"Payment receipt + Permanent Application Number"},
  {step:5,name:"Desktop Assessment (DA)",url:"",desc:"NABH DA team reviews all submitted documents online. NCs raised with remarks. HCO submits NC reply + supporting document upload. Two rounds of NC closure cycle available at DA stage.",output:"DA NC closure → Date allotment for onsite assessment"},
  {step:6,name:"Onsite Assessment",url:"",desc:"Physical visit by NABH assessor. Assessment activities: document review, patient care area visit, functional interviews, facility tours. Assessor uploads report within 7 days. HCO gets two NC closure cycles.",output:"Onsite assessment report + NC closure"},
  {step:7,name:"Certification Committee",url:"",desc:"After all NCs closed, case placed before Certification Committee. Committee recommendations are final. If rejected, HCO can appeal to Chairman NABH after paying appeal fee.",output:"Approval letter / Rejection letter"},
  {step:8,name:"Digital Certificate",url:"",desc:"Printable digital certificate issued with unique certificate number, hospital name, effective date, expiry date. Valid for 2 years. No surveillance assessment under certification programmes. Apply for renewal 6 months before expiry.",output:"NABH HCO ELC Certificate (2-year validity)"},
];

const HCO_FEE = {
  base: 52000,
  gstRate: 0.18,
  label: "HCO Entry Level Certification (>50 sanctioned beds)",
  note: "Fee is non-refundable and non-transferable. Source: NABH Guidebook on ELC for HCOs/SHCOs.",
};

// ── NABH 6th Edition official chapter order ─────────────────────────────
const CHAPTER_ORDER = {
  "AAC": 1,  // Access, Assessment and Continuity of Care
  "COP": 2,  // Care of Patients
  "MOM": 3,  // Management of Medication
  "PRE": 4,  // Patient Rights and Education
  "IPC": 5,  // Infection Prevention and Control
  "PSQ": 6,  // Patient Safety and Quality Improvement
  "ROM": 7,  // Responsibility of Management
  "FMS": 8,  // Facility Management and Safety
  "HRM": 9,  // Human Resource Management
  "IMS": 10, // Information Management System
};

// ── Chapter-level achieve guidance (fallback when per-OE DB tips absent) ──
const OE_TIPS = {
  HRM: [
    "Nurse-patient ratio standards: ICU ventilated 1:1, ICU non-ventilated 1:2, general ward 1:6 — document and monitor daily on duty roster",
    "Maintain valid nursing registration certificates for all nursing staff — set expiry reminders 3 months in advance",
    "Annual competency assessment is mandatory for all clinical staff — document assessment tool, assessor signature, and outcome",
    "Training records required for: BLS/CPR, Fire Safety, BMW handling, IPC practices, LASA medications, Code Blue response, Patient Rights, Needle Stick Injury, Disaster Management",
    "Duty roster must explicitly show skill mix and competency-based deployment — assessors verify that competent staff are allocated to high-risk areas",
    "Staff orientation records must cover hospital policies, patient safety goals, emergency procedures, and departmental SOPs",
    "Maintain a Training Calendar with planned vs completed sessions — track attendance ≥80% compliance per staff per year",
  ],
  MOM: [
    "Implement FIFO (First In First Out) and FEFO (First Expired First Out) for all medications — label shelves and train pharmacy staff",
    "Temperature monitoring: narcotics and controlled substances at 15–30°C ambient; refrigerated medications at 2–8°C cold chain with twice-daily log",
    "Narcotic register: record receipt, issue, balance, patient name, date, and prescriber name in ink — no erasures, corrections must be countersigned",
    "LASA (Look-Alike Sound-Alike) medications must be physically segregated with tall-man lettering labels on bins and shelves",
    "High-alert medications (insulin, heparin, concentrated electrolytes, chemotherapy) require double-check policy with two-nurse verification before administration",
    "Medical supplies and consumables: organized storage with expiry date tracking, stock-out prevention through par-level reorder triggers",
    "Adverse Drug Reaction (ADR) and medication error reporting: maintain register, conduct RCA for every significant event, submit monthly data to pharmacy committee",
    "Emergency medications list must be standardized, reviewed annually by P&T committee, and available in all clinical areas including OT and ICU",
  ],
  IPC: [
    "Hand hygiene monitoring: observe and record WHO 5 Moments compliance monthly per department — target ≥80%, display results publicly",
    "PPE protocol: gloves + mask for all patient contact, add gown and goggles for aerosol-generating procedures and isolation patients — risk-tiered approach",
    "BMW segregation: Yellow bag — infectious/anatomical waste; Red bag — recyclable contaminated; Blue/White translucent — glass/sharps; Black bag — general waste",
    "Sterilization validation: biological indicator (Geobacillus stearothermophilus) run weekly for autoclaves; chemical indicator (Type 5 or 6) every cycle",
    "HAI surveillance: microbiological cultures from OT, ICU, NICU, Labour Room every 3 months — document results, trend, and corrective action",
    "Bundle care protocols: VAP (Ventilator-Associated Pneumonia) bundle, CLABSI (Central Line) bundle, CAUTI (Catheter UTI) bundle — compliance monitored daily",
    "AMR surveillance: flag CRE (Carbapenem-Resistant Enterobacteriaceae), MRSA, VRE — isolate immediately, notify infection control team, document outbreak response",
    "Pre-exposure prophylaxis: hepatitis B vaccination for all healthcare workers — maintain records with dose dates and titre levels",
  ],
  FMS: [
    "MRI safety zone system: Zone 1 — public area unrestricted; Zone 2 — supervised by MRI staff; Zone 3 — restricted, controlled access, no ferromagnetic objects; Zone 4 — magnet room, highest risk, screened personnel only",
    "OT machine daily checklist: anesthesia machine leak test + O2/N2O pressure check; defibrillator battery status + pad expiry date; suction pre-surgery function check; cautery grounding plate placement verification",
    "Fire safety: monthly mock drills with attendance record and debriefing; exit route maps posted at every 20 metres; all staff trained on RACE (Rescue-Alarm-Contain-Evacuate) and PASS (Pull-Aim-Squeeze-Sweep)",
    "Emergency crash cart: daily checklist with seal intact verification; drug and consumable expiry checked monthly; AED pads and battery status weekly; designated nurse responsible per shift",
    "Medical gas management: pipeline pressure gauges monitored daily; cylinder stock maintained above minimum; no flammable materials near O2 outlets",
    "Facility inspection rounds: documented monthly rounds covering patient areas, OT, ICU, pharmacy, kitchen, and laundry — findings with CAPA and closure dates",
    "Equipment maintenance: preventive maintenance schedule for all clinical equipment; maintenance log, calibration certificate, and next-service date displayed on equipment",
  ],
  COP: [
    "MLC documentation: assign unique MLC number to every case; police intimation in writing within 24 hours per local rules; injury diagram mandatory for trauma; maintain chain of custody for specimens; handover memo to police with receiving officer signature",
    "WHO Surgical Safety Checklist: Sign In (before anesthesia induction) — patient identity + site + consent + allergies; Time Out (before incision) — entire team pauses + confirms; Sign Out (before patient leaves OT) — instrument/swab/specimen count confirmed",
    "Patient identification: use two identifiers (name + date of birth or UHID) at every care transition — medication administration, blood transfusion, specimen collection, surgical procedures",
    "Fall risk assessment: Morse Fall Scale on admission, post-fall, and every 24 hours for high-risk patients — documented with interventions (bed rails, call bell, non-slip footwear, signage)",
    "Pressure injury prevention: Braden Scale assessment on admission and daily for high-risk patients — document score, intervention (turning schedule, pressure-relieving mattress), and outcome",
    "Informed consent: separate consent for surgery, anesthesia, blood transfusion, and high-risk procedures — patient-readable language, witness signature, and physician explanation documented",
    "Discharge summary: completed within 24 hours of discharge with diagnosis, procedures, medications, follow-up instructions, and emergency contact — copy given to patient",
    "Critical value reporting: lab notifies clinical team immediately for defined critical values — document time of result, time notified, and action taken in medical record",
  ],
  PSQ: [
    "Internal audits: minimum 6 types annually — clinical audit, medication audit, nursing care audit, hand hygiene compliance audit, documentation completeness audit, crash cart audit",
    "CAPA process: root cause analysis (5-Why or fishbone) for every significant audit finding; action assigned to named responsible person with target date; effectiveness review documented at next audit cycle",
    "KPI monitoring: monthly data collection for all defined indicators; trend analysis (run chart or control chart); results presented at departmental review meetings; staff awareness session based on findings",
    "Sentinel event reporting: define sentinel events (wrong-site surgery, patient fall with injury, medication error causing harm) — mandatory reporting within 24 hours, RCA within 30 days",
    "Patient safety goals: track compliance monthly for each of the 6 NABH patient safety goals — correct identification, effective communication, medication safety, surgical safety, infection prevention, fall prevention",
    "Quality committee: meets at least monthly; reviews audit results, KPI data, incident reports, and CAPA status — minutes documented and circulated to department heads",
    "Patient satisfaction survey: collect and analyze minimum quarterly; calculate satisfaction score; display results; take CAPA for scores below threshold",
  ],
};

const DARK_THEME = {
  bg:"#050e1a", panel:"#081525", panel2:"#0c1e35", border:"#0f2640",
  gold:"#c9a84c", goldL:"#f0d070", goldD:"rgba(201,168,76,0.10)",
  red:"#e05a5a", redD:"rgba(224,90,90,0.10)",
  orange:"#f4a441", orangeD:"rgba(244,164,65,0.10)",
  green:"#4caf7d", greenD:"rgba(76,175,125,0.10)",
  blue:"#4fc3f7", blueD:"rgba(79,195,247,0.08)",
  muted:"#3a5870", text:"#c8dcea", white:"#eef4f9",
};

const LIGHT_THEME = {
  bg:"#e8f2fb", panel:"#ddeef8", panel2:"#c8e2f5", border:"#a8cce0",
  gold:"#1565c0", goldL:"#1565c0", goldD:"rgba(21,101,192,0.10)",
  red:"#d32f2f", redD:"rgba(211,47,47,0.10)",
  orange:"#e65100", orangeD:"rgba(230,81,0,0.10)",
  green:"#2e7d32", greenD:"rgba(46,125,50,0.10)",
  blue:"#1976d2", blueD:"rgba(25,118,210,0.10)",
  muted:"#4a6f8a", text:"#0d1f33", white:"#0a1828",
  panelShadow:"0 2px 8px rgba(0,0,0,0.08)",
  headerBg:"#c8e2f5",
};

// Mutable reference — App() reassigns this before each render so all
// component functions that close over T see the correct theme values.
let T = DARK_THEME;

const lvColor = l => l==="CORE"?"#e05a5a":l==="Commitment"?"#4fc3f7":l==="Achievement"?"#4caf7d":"#c9a84c";
const chColor = {AAC:"#4fc3f7",COP:"#f4a441",MOM:"#e05a5a",PRE:"#4caf7d",IPC:"#c084e8",PSQ:"#ff8a65",ROM:"#80cbc4",FMS:"#a5d6a7",HRM:"#f0d070",IMS:"#90caf9"};
const sevColor = s => s==="CRITICAL"?T.red:s==="HIGH"?T.orange:s==="MEDIUM"?T.gold:T.green;

const MONTHS_SHORT = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

function Ring({ pct=0, size=110, stroke=9, color=T.green, label }) {
  const r=(size-stroke)/2,circ=2*Math.PI*r,dash=(pct/100)*circ;
  return (
    <div style={{position:"relative",width:size,height:size,flexShrink:0}}>
      <svg width={size} height={size} style={{transform:"rotate(-90deg)"}}>
        <circle cx={size/2} cy={size/2} r={r} fill="none" stroke={`${color}20`} strokeWidth={stroke}/>
        <circle cx={size/2} cy={size/2} r={r} fill="none" stroke={color} strokeWidth={stroke}
          strokeDasharray={`${dash} ${circ}`} strokeLinecap="round"
          style={{transition:"stroke-dasharray 0.8s cubic-bezier(0.4,0,0.2,1)"}}/>
      </svg>
      <div style={{position:"absolute",inset:0,display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center"}}>
        <div style={{fontSize:size>90?20:14,fontWeight:800,color,fontFamily:"Georgia,serif",lineHeight:1}}>{pct}%</div>
        {label&&<div style={{fontSize:8,color:T.muted,letterSpacing:1,marginTop:2}}>{label}</div>}
      </div>
    </div>
  );
}

function KpiTrendChart({ history, target, unit }) {
  if (!history || history.length === 0) return (
    <div style={{background:T.panel2,borderRadius:8,padding:"20px",textAlign:"center",border:`1px solid ${T.border}`,marginBottom:12}}>
      <div style={{fontSize:28,marginBottom:8}}>📈</div>
      <div style={{fontSize:13,color:T.muted}}>No data yet. Enter monthly values above to see your trend chart.</div>
    </div>
  );
  const chartData=[...history].sort((a,b)=>a.year!==b.year?a.year-b.year:a.month-b.month).slice(-12).map(d=>({name:`${MONTHS_SHORT[d.month-1]} ${String(d.year).slice(2)}`,value:d.value,capa:d.capa_required}));
  const vals=chartData.map(d=>d.value);const minVal=Math.min(...vals);const maxVal=Math.max(...vals);const pad=Math.max((maxVal-minVal)*0.2,1);
  const yMin=Math.max(0,Math.floor((minVal-pad)*10)/10);const yMax=Math.ceil((Math.max(maxVal,parseFloat(target)||0)+pad)*10)/10;
  const CustomDot=(props)=>{const{cx,cy,payload}=props;if(!payload.capa)return <circle cx={cx} cy={cy} r={3} fill={T.gold}/>;return <circle cx={cx} cy={cy} r={5} fill={T.orange} stroke={T.bg} strokeWidth={1.5}/>;};
  const TT=({active,payload,label})=>{if(!active||!payload||!payload.length)return null;const d=payload[0].payload;return(<div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:8,padding:"8px 12px",fontSize:12}}><div style={{color:T.gold,fontWeight:700,marginBottom:4}}>{label}</div><div style={{color:T.white}}>Value: <strong style={{color:T.goldL}}>{d.value} {unit}</strong></div>{target&&<div style={{color:T.green,marginTop:2}}>Target: {target}</div>}{d.capa&&<div style={{color:T.orange,marginTop:2}}>CAPA raised</div>}</div>);};
  return(<div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:8,padding:"12px 8px 8px 0",marginBottom:12}}><div style={{fontSize:11,color:T.gold,letterSpacing:1,marginBottom:8,paddingLeft:12,display:"flex",gap:12}}><span>TREND — last {chartData.length} months</span>{target&&<span style={{color:T.green}}>Target: {target} {unit}</span>}</div><ResponsiveContainer width="100%" height={160}><LineChart data={chartData} margin={{top:4,right:16,left:0,bottom:0}}><CartesianGrid strokeDasharray="2 4" stroke={T.border} vertical={false}/><XAxis dataKey="name" tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false}/><YAxis domain={[yMin,yMax]} tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false} width={36}/><Tooltip content={<TT/>}/>{target&&<ReferenceLine y={parseFloat(target)} stroke={T.green} strokeDasharray="4 3" strokeWidth={1.5}/>}<Line type="monotone" dataKey="value" stroke={T.gold} strokeWidth={2.5} dot={<CustomDot/>} activeDot={{r:5,fill:T.goldL}}/></LineChart></ResponsiveContainer><div style={{display:"flex",gap:14,paddingLeft:12,marginTop:6,fontSize:8,color:T.muted}}><span style={{color:T.gold}}>Value</span>{target&&<span style={{color:T.green}}>-- Target</span>}<span style={{color:T.orange}}>o CAPA</span></div></div>);
}

function AuditComplianceChart({ records }) {
  if (!records || records.length === 0) return (
    <div style={{background:T.panel2,borderRadius:8,padding:"20px",textAlign:"center",border:`1px solid ${T.border}`,marginBottom:12}}>
      <div style={{fontSize:28,marginBottom:8}}>📊</div>
      <div style={{fontSize:13,color:T.muted}}>No records yet. Record an audit to see compliance trends.</div>
    </div>
  );
  const getBarColor=(pct)=>pct>=80?T.green:pct>=60?T.orange:T.red;
  const chartData=[...records].filter(r=>r.sample_size>0&&r.compliant_count!==null).sort((a,b)=>new Date(a.audit_date)-new Date(b.audit_date)).slice(-12).map(r=>({name:new Date(r.audit_date).toLocaleDateString("en-IN",{day:"2-digit",month:"short"}),pct:Math.round((r.compliant_count/r.sample_size)*100),capa:r.capa_raised}));
  if(chartData.length===0)return(<div style={{background:T.panel2,borderRadius:8,padding:"12px",textAlign:"center",border:`1px solid ${T.border}`,fontSize:12,color:T.muted,marginBottom:12}}>Enter sample size and compliant count when recording audits to see charts.</div>);
  const TT=({active,payload,label})=>{if(!active||!payload||!payload.length)return null;const d=payload[0].payload;return(<div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:8,padding:"8px 12px",fontSize:12}}><div style={{color:T.gold,fontWeight:700,marginBottom:4}}>{label}</div><div style={{color:getBarColor(d.pct),fontWeight:700,fontSize:15}}>{d.pct}%</div>{d.capa&&<div style={{color:T.orange,marginTop:3}}>CAPA raised</div>}</div>);};
  return(<div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:8,padding:"12px 8px 8px 0",marginBottom:12}}><div style={{fontSize:11,color:T.gold,letterSpacing:1,marginBottom:8,paddingLeft:12,display:"flex",gap:12}}><span>COMPLIANCE TREND — last {chartData.length} audits</span><span style={{color:T.green}}>Target: 80%</span></div><ResponsiveContainer width="100%" height={150}><BarChart data={chartData} margin={{top:4,right:16,left:0,bottom:0}}><CartesianGrid strokeDasharray="2 4" stroke={T.border} vertical={false}/><XAxis dataKey="name" tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false}/><YAxis domain={[0,100]} tick={{fontSize:8,fill:T.muted}} axisLine={false} tickLine={false} width={30} tickFormatter={v=>`${v}%`}/><Tooltip content={<TT/>}/><ReferenceLine y={80} stroke={T.green} strokeDasharray="4 3" strokeWidth={1.5}/><Bar dataKey="pct" radius={[3,3,0,0]} shape={(props)=>{const{x,y,width,height,value}=props;return <rect x={x} y={y} width={Math.max(width,4)} height={Math.max(height,1)} rx={3} fill={getBarColor(value)} fillOpacity={0.85}/>;}} /></BarChart></ResponsiveContainer><div style={{display:"flex",gap:14,paddingLeft:12,marginTop:6,fontSize:8,color:T.muted}}><span style={{color:T.green}}>Good (80%+)</span><span style={{color:T.orange}}>Fair (60-79%)</span><span style={{color:T.red}}>Critical</span></div></div>);
}

function LoginScreen({ onLogin, initialError }) {
  const [email,setEmail]=useState(""); const [pass,setPass]=useState("");
  const [mode,setMode]=useState("login"); const [error,setError]=useState(initialError||"");
  const [loading,setLoading]=useState(false); const [msg,setMsg]=useState("");
  useEffect(()=>{
    if(initialError)setError(initialError);
  },[initialError]);
  const handle=async()=>{
    setError("");setMsg("");setLoading(true);
    try{
      if(mode==="login"){const{data,error:err}=await supabase.auth.signInWithPassword({email,password:pass});if(err)throw err;onLogin(data.user);}
      else if(mode==="signup"){const{data,error:err}=await supabase.auth.signUp({email,password:pass});if(err)throw err;
        if(data.session)onLogin(data.user);else{setMsg("Account created. You can now sign in.");setMode("login");}}
      else if(mode==="reset"){if(!email.trim())throw new Error("Enter your email address first.");const{error:err}=await supabase.auth.resetPasswordForEmail(email,{redirectTo:"https://upadhyaymehul9-prog.github.io/nabh-compliance/"});if(err)throw err;setMsg("Password reset email sent! Check your inbox.");setMode("login");}
    }catch(e){setError(e.message);}
    setLoading(false);
  };
  const signInWithGoogle=async()=>{
    setError("");setLoading(true);
    const{error:err}=await supabase.auth.signInWithOAuth({
      provider:"google",
      options:{redirectTo:"https://upadhyaymehul9-prog.github.io/nabh-compliance/"}
    });
    if(err){setError(err.message);setLoading(false);}
  };
  if(mode==='terms') return <TermsScreen onBack={()=>setMode('login')}/>;
  if(mode==='privacy') return <PrivacyScreen onBack={()=>setMode('login')}/>;
  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:16,padding:"40px 36px",width:360}}>
        <div style={{textAlign:"center",marginBottom:28}}>
          <div style={{width:48,height:48,borderRadius:12,background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:24,margin:"0 auto 12px"}}>⚕</div>
          <div style={{fontSize:8,letterSpacing:3,color:T.gold,marginBottom:4}}>NABH 6TH EDITION</div>
          <div style={{fontSize:18,fontWeight:700,color:T.white}}>Compliance Engine</div>
          <div style={{fontSize:13,color:T.muted,marginTop:4}}>Hospital Accreditation Platform</div>
        </div>
        {error&&<div style={{background:T.redD,border:`1px solid ${T.red}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:13,color:T.red}}>{error}</div>}
        {msg&&<div style={{background:T.greenD,border:`1px solid ${T.green}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:13,color:T.green}}>{msg}</div>}
        <div style={{textAlign:'center',padding:'0 0 20px 0',marginBottom:20,borderBottom:'1px solid #0f2640'}}>
          <div style={{fontFamily:'Georgia,serif',fontSize:15,fontStyle:'italic',color:'#c8dcea',lineHeight:1.8}}>"An investment in knowledge pays the best interest."</div>
          <div style={{fontSize:12,color:'#3a5870',marginTop:6,letterSpacing:2}}>— BENJAMIN FRANKLIN</div>
        </div>
        <div style={{marginBottom:14}}>
          <div style={{fontSize:12,color:T.muted,marginBottom:6}}>EMAIL</div>
          <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="admin@hospital.com" type="email"
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,boxSizing:"border-box"}}/>
        </div>
        {mode!=="reset"&&<div style={{marginBottom:20}}>
          <div style={{fontSize:12,color:T.muted,marginBottom:6}}>PASSWORD</div>
          <input value={pass} onChange={e=>setPass(e.target.value)} placeholder="••••••••" type="password" onKeyDown={e=>e.key==="Enter"&&handle()}
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,boxSizing:"border-box"}}/>
        </div>}
        {mode==="reset"&&<div style={{marginBottom:20,fontSize:13,color:T.muted,lineHeight:1.6}}>Enter your email above and we'll send you a password reset link.</div>}
        <button onClick={handle} disabled={loading} style={{width:"100%",padding:"12px",borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:15,fontWeight:700,cursor:"pointer",opacity:loading?0.7:1}}>
          {loading?"Please wait…":mode==="login"?"Sign In →":mode==="signup"?"Create Account →":"Send Reset Email →"}
        </button>
        {mode==="login"&&(
          <>
            <div style={{display:"flex",alignItems:"center",gap:10,margin:"16px 0"}}>
              <div style={{flex:1,height:1,background:T.border}}/>
              <div style={{fontSize:12,color:T.muted,letterSpacing:1}}>OR</div>
              <div style={{flex:1,height:1,background:T.border}}/>
            </div>
            <button onClick={signInWithGoogle} disabled={loading}
              style={{width:"100%",padding:"11px",borderRadius:10,background:T.panel2,border:`1px solid ${T.border}`,color:T.text,fontSize:15,fontWeight:600,cursor:"pointer",display:"flex",alignItems:"center",justifyContent:"center",gap:10,opacity:loading?0.7:1}}>
              <svg width="16" height="16" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.08 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.18 1.48-4.97 2.31-8.16 2.31-6.26 0-11.57-3.58-13.46-8.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
              Continue with Google
            </button>
            <div style={{textAlign:"center",marginTop:12,fontSize:13,color:T.muted}}>
              <span onClick={()=>{setMode("reset");setError("");setMsg("");}} style={{color:T.blue,cursor:"pointer"}}>Forgot password?</span>
            </div>
            <div style={{display:'flex',gap:20,justifyContent:'center',marginTop:14,flexWrap:'wrap'}}>
              <a href="mailto:upadhyay.mehul9@gmail.com" style={{fontSize:12,color:'#3a5870',textDecoration:'none',letterSpacing:1,textTransform:'uppercase'}}>Contact Us</a>
              <span onClick={()=>setMode('terms')} style={{fontSize:12,color:'#3a5870',cursor:'pointer',letterSpacing:1,textTransform:'uppercase'}}>Terms & Conditions</span>
              <span onClick={()=>setMode('privacy')} style={{fontSize:12,color:'#3a5870',cursor:'pointer',letterSpacing:1,textTransform:'uppercase'}}>Privacy Policy</span>
            </div>
          </>
        )}
        <div style={{textAlign:"center",marginTop:10,fontSize:13,color:T.muted}}>
          {mode==="login"?"Don't have an account? ":mode==="signup"?"Already have an account? ":"Remember your password? "}
          <span onClick={()=>{setMode(mode==="login"?"signup":"login");setError("");setMsg("");}} style={{color:T.gold,cursor:"pointer",fontWeight:600}}>
            {mode==="login"?"Sign up":mode==="reset"?"Sign in":"Sign in"}
          </span>
        </div>
        <div style={{textAlign:"center",marginTop:10,fontSize:11,color:T.muted}}>Independent educational tool — Not affiliated with NABH/QCI</div>
        <div style={{textAlign:"center",marginTop:10,paddingBottom:4}}>
          <span style={{fontSize:12,color:T.muted}}>14-day free trial · No credit card · </span>
          <a href="https://upadhyaymehul9-prog.github.io/nabh-compliance/#pricing" onClick={e=>{e.preventDefault();window.open("https://wa.me/918511180957","_blank");}} style={{fontSize:12,color:T.gold,cursor:"pointer",textDecoration:"none",fontWeight:600}}>💎 View Pricing Plans →</a>
        </div>
      </div>
    </div>
  );
}
function TermsScreen({onBack}){return(
    <div style={{minHeight:'100vh',background:'#050e1a',color:'#c8dcea',fontFamily:'Segoe UI,sans-serif',padding:'40px 24px',maxWidth:720,margin:'0 auto'}}>
      <button onClick={onBack} style={{background:'transparent',border:'1px solid #0f2640',color:'#3a5870',padding:'6px 16px',borderRadius:6,cursor:'pointer',fontSize:13,marginBottom:32}}>← Back to Login</button>
      <div style={{color:'#c9a84c',fontSize:12,letterSpacing:3,marginBottom:8,textTransform:'uppercase'}}>AccredReady</div>
      <h1 style={{fontFamily:'Georgia,serif',fontSize:28,fontWeight:300,color:'#eef4f9',marginBottom:6}}>Terms & Conditions</h1>
      <div style={{fontSize:12,color:'#3a5870',letterSpacing:1,marginBottom:32}}>Effective Date: 19 May 2026</div>
      {[
        ['1. Acceptance','By using AccredReady at accredready.in, you agree to these terms. If you disagree, do not use the platform.'],
        ['2. What AccredReady Is','AccredReady is an independent educational preparation tool for healthcare accreditation. It is not affiliated with, endorsed by, or officially connected to any accreditation body including any government authority.'],
        ['3. Your Account','You are responsible for keeping your login credentials secure. You agree to provide accurate information. We may suspend accounts that violate these terms.'],
        ['4. Subscription & Payment','Plans: ₹499/month (Starter), ₹999/month (Professional), ₹2,999/month (Consultant). 14-day free trial for new users — no payment required. Payment via UPI or bank transfer. Cancel anytime by emailing upadhyay.mehul9@gmail.com. No refunds for partial months used.'],
        ['5. Acceptable Use','You agree not to share your account, attempt to access other users data, copy or reproduce platform content, or use the platform for any unlawful purpose.'],
        ['6. Intellectual Property','All content, design, and code is owned by AccredReady / Dr. Mehul Upadhyay. No reproduction without written permission.'],
        ['7. Disclaimer','AccredReady does not guarantee accreditation outcomes. All accreditation decisions rest with the relevant accreditation body. Always verify content against official published standards.'],
        ['8. Limitation of Liability','AccredReady is not liable for any indirect, incidental, or consequential damages arising from use of the platform.'],
        ['9. Governing Law','These terms are governed by Indian law. Disputes are subject to courts in Gujarat, India.'],
        ['10. Changes','We may update these terms. Continued use after changes means acceptance.'],
        ['11. Contact','Email: upadhyay.mehul9@gmail.com'],
      ].map(([title,body])=>(
        <div key={title} style={{marginBottom:20}}>
          <div style={{fontSize:13,fontWeight:700,color:'#c9a84c',letterSpacing:1,textTransform:'uppercase',marginBottom:6}}>{title}</div>
          <div style={{fontSize:15,color:'#c8dcea',lineHeight:1.8}}>{body}</div>
        </div>
      ))}
    </div>
  );}
function PrivacyScreen({onBack}){return(
    <div style={{minHeight:'100vh',background:'#050e1a',color:'#c8dcea',fontFamily:'Segoe UI,sans-serif',padding:'40px 24px',maxWidth:720,margin:'0 auto'}}>
      <button onClick={onBack} style={{background:'transparent',border:'1px solid #0f2640',color:'#3a5870',padding:'6px 16px',borderRadius:6,cursor:'pointer',fontSize:13,marginBottom:32}}>← Back to Login</button>
      <div style={{color:'#c9a84c',fontSize:12,letterSpacing:3,marginBottom:8,textTransform:'uppercase'}}>AccredReady</div>
      <h1 style={{fontFamily:'Georgia,serif',fontSize:28,fontWeight:300,color:'#eef4f9',marginBottom:6}}>Privacy Policy</h1>
      <div style={{fontSize:12,color:'#3a5870',letterSpacing:1,marginBottom:32}}>Effective Date: 19 May 2026</div>
      {[
        ['1. What We Collect','Name and email address from Google or email signup. Hospital or facility name and data you enter including scores, KPIs, committees, and audit records. Basic usage logs for platform improvement.'],
        ['2. How We Use It','To operate and maintain your account. To provide platform features. To send service emails only — not marketing.'],
        ['3. Data Storage','Your data is stored on Supabase (PostgreSQL on AWS) with industry-standard encryption. We do not store data outside secured cloud infrastructure.'],
        ['4. Data Sharing','We do not sell or share your data. The only exceptions are Supabase for infrastructure and Google for authentication — both necessary to operate the platform.'],
        ['5. Your Rights','Access your data anytime from your account. Request correction of inaccurate data. Request full deletion — we remove all data within 30 days. Email upadhyay.mehul9@gmail.com to exercise any right.'],
        ['6. Cookies','We use session cookies for authentication only. No tracking or advertising cookies are used.'],
        ['7. Children','AccredReady is for healthcare professionals only. We do not knowingly collect data from anyone under 18 years of age.'],
        ['8. Changes','We may update this policy. Registered users will be notified of significant changes by email.'],
        ['9. Contact','Email: upadhyay.mehul9@gmail.com'],
      ].map(([title,body])=>(
        <div key={title} style={{marginBottom:20}}>
          <div style={{fontSize:13,fontWeight:700,color:'#c9a84c',letterSpacing:1,textTransform:'uppercase',marginBottom:6}}>{title}</div>
          <div style={{fontSize:15,color:'#c8dcea',lineHeight:1.8}}>{body}</div>
        </div>
      ))}
    </div>
  );}

// ── ONBOARDING WIZARD (first-time users only, 1 step) ────────────────────
function OnboardingScreen({ hospitalName, onDone }) {
  const [nabh_status, setNabhStatus] = useState("");

  const NABH_STATUSES = [
    { id: "exploring",   icon: "🔍", label: "Just Exploring",       desc: "Want to understand NABH requirements" },
    { id: "preparing",   icon: "📋", label: "Preparing to Apply",   desc: "Planning to apply within 6–12 months" },
    { id: "applied",     icon: "📨", label: "Application Submitted", desc: "Already submitted NABH application" },
    { id: "assessment",  icon: "🏥", label: "Assessment Scheduled",  desc: "Assessors visiting soon" },
    { id: "consultant",  icon: "🤝", label: "NABH Consultant",       desc: "Managing multiple hospitals" },
  ];

  return (
    <div style={{ minHeight: "100vh", background: T.bg, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Segoe UI,system-ui,sans-serif", padding: 16 }}>
      <div style={{ background: T.panel, border: `1px solid ${T.border}`, borderRadius: 16, padding: "36px", width: 460, maxWidth: "100%" }}>
        <div style={{ marginBottom: 24 }}>
          <div style={{ fontSize: 8, letterSpacing: 3, color: T.gold, marginBottom: 8 }}>ACCREDREADY · SETUP</div>
          <div style={{ fontSize: 20, fontWeight: 700, color: T.white, marginBottom: 4 }}>Welcome, {hospitalName}! 🎉</div>
          <div style={{ fontSize: 11, color: T.muted, lineHeight: 1.6 }}>One quick question to personalise your experience.</div>
        </div>

        <div style={{ fontSize: 13, fontWeight: 700, color: T.white, marginBottom: 4 }}>Where are you in your NABH journey?</div>
        <div style={{ fontSize: 10, color: T.muted, marginBottom: 16 }}>We'll tailor your dashboard based on your stage.</div>
        <div style={{ display: "grid", gap: 8 }}>
          {NABH_STATUSES.map(s => (
            <div key={s.id} onClick={() => setNabhStatus(s.id)}
              style={{ padding: "12px 16px", borderRadius: 10, border: `1px solid ${nabh_status === s.id ? T.gold : T.border}`, background: nabh_status === s.id ? T.goldD : T.panel2, cursor: "pointer", display: "flex", alignItems: "center", gap: 12, transition: "all 0.15s" }}>
              <div style={{ fontSize: 20, flexShrink: 0 }}>{s.icon}</div>
              <div>
                <div style={{ fontSize: 12, fontWeight: 700, color: nabh_status === s.id ? T.goldL : T.white }}>{s.label}</div>
                <div style={{ fontSize: 10, color: T.muted, marginTop: 2 }}>{s.desc}</div>
              </div>
              {nabh_status === s.id && <div style={{ marginLeft: "auto", color: T.gold, fontSize: 16 }}>✓</div>}
            </div>
          ))}
        </div>

        <div style={{ display: "flex", justifyContent: "flex-end", marginTop: 24 }}>
          <button onClick={() => onDone({ nabh_status })} disabled={!nabh_status}
            style={{ padding: "10px 24px", borderRadius: 9, background: nabh_status ? `linear-gradient(135deg,${T.gold},#f0d070)` : T.border, border: "none", color: nabh_status ? T.bg : T.muted, fontSize: 12, fontWeight: 700, cursor: nabh_status ? "pointer" : "default", transition: "all 0.2s" }}>
            Continue →
          </button>
        </div>

        <div style={{ textAlign: "center", marginTop: 14 }}>
          <button onClick={() => onDone({ nabh_status: "preparing" })}
            style={{ background: "transparent", border: "none", color: T.muted, fontSize: 10, cursor: "pointer", textDecoration: "underline" }}>
            Skip →
          </button>
        </div>
      </div>
    </div>
  );
}

// ── PROGRAMME SELECTOR ────────────────────────────────────────────────────
function ProgrammeSelector({ user, ctx, onSelect }) {
  const [comingSoonModal, setComingSoonModal] = useState(null);
  const [notifyDone, setNotifyDone] = useState({});
  const [notifyLoading, setNotifyLoading] = useState(false);

  const programmes = [
    {
      key: "hco_full",
      title: "NABH Hospital Accreditation",
      subtitle: "HCO Full Accreditation",
      badge: "6th Edition",
      tags: ["51+ beds", "639 OEs"],
      desc: "Full NABH accreditation for hospitals with 51 or more beds. The gold standard in Indian hospital accreditation.",
      available: true,
      icon: "🏥",
      color: T.gold,
    },
    {
      key: "hco_elc",
      title: "Entry Level Certification",
      subtitle: "Hospital Entry Level",
      badge: "Available",
      tags: ["51+ beds", "Docs & Licenses"],
      desc: "Entry-level certification for hospitals with 51+ beds. Document and license based — structured first step toward full HCO accreditation.",
      available: true,
      icon: "🎯",
      color: T.blue,
    },
    {
      key: "shco_full",
      title: "SHCO Full Accreditation",
      subtitle: "Small Hospital Full",
      badge: "3rd Edition · Coming Soon",
      tags: ["≤50 beds", "408 OEs"],
      desc: "Full NABH accreditation for small hospitals with up to 50 beds. Comprehensive quality programme.",
      available: false,
      icon: "🏨",
      color: T.orange,
    },
    {
      key: "shco_elc",
      title: "SHCO Entry Level Certification",
      subtitle: "Small Hospital ELC",
      badge: "Available",
      tags: ["≤50 beds", "Docs & Licenses"],
      desc: "Entry-level certification for hospitals with up to 50 beds. Document and license based — no OE scoring required.",
      available: true,
      icon: "📋",
      color: T.green,
    },
  ];

  const handleNotify = async (programme) => {
    setNotifyLoading(true);
    const { error } = await supabase.from("programme_interest")
      .upsert({ user_id: user.id, programme }, { onConflict: "user_id,programme", ignoreDuplicates: true });
    setNotifyLoading(false);
    if (!error) setNotifyDone(prev => ({ ...prev, [programme]: true }));
  };

  return (
    <div style={{ minHeight: "100vh", background: T.bg, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Segoe UI,system-ui,sans-serif", padding: 24 }}>
      <div style={{ width: "100%", maxWidth: 860 }}>
        <div style={{ textAlign: "center", marginBottom: 36 }}>
          <div style={{ width: 52, height: 52, borderRadius: 14, background: `linear-gradient(135deg,${T.gold},#f0d070)`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 26, margin: "0 auto 16px" }}>⚕</div>
          <div style={{ fontSize: 9, letterSpacing: 3, color: T.gold, marginBottom: 8 }}>ACCREDREADY</div>
          <div style={{ fontSize: 26, fontWeight: 700, color: T.white, fontFamily: "Georgia,serif", marginBottom: 8 }}>Select Your Programme</div>
          <div style={{ fontSize: 12, color: T.muted }}>Choose the accreditation programme you are working towards. You can switch anytime.</div>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(2,1fr)", gap: 16 }}>
          {programmes.map(p => (
            <div key={p.key}
              onClick={() => p.available ? onSelect(p.key, ctx) : setComingSoonModal(p)}
              style={{ background: T.panel, border: `1.5px solid ${T.border}`, borderRadius: 14, padding: "24px", cursor: "pointer", position: "relative", transition: "border-color 0.18s, background 0.18s" }}
              onMouseEnter={e => { e.currentTarget.style.borderColor = p.color; e.currentTarget.style.background = T.panel2; }}
              onMouseLeave={e => { e.currentTarget.style.borderColor = T.border; e.currentTarget.style.background = T.panel; }}
            >
              <div style={{ position: "absolute", top: 14, right: 14, fontSize: 8, fontWeight: 700, letterSpacing: 1, padding: "3px 9px", borderRadius: 20, background: p.available ? `${p.color}20` : `${T.muted}18`, color: p.available ? p.color : T.muted, border: `1px solid ${p.available ? p.color : T.muted}40` }}>{p.badge}</div>
              <div style={{ fontSize: 30, marginBottom: 12 }}>{p.icon}</div>
              <div style={{ fontSize: 15, fontWeight: 800, color: T.white, marginBottom: 3 }}>{p.title}</div>
              <div style={{ fontSize: 10, color: p.color, fontWeight: 600, marginBottom: 10 }}>{p.subtitle}</div>
              <div style={{ display: "flex", gap: 6, marginBottom: 14, flexWrap: "wrap" }}>
                {p.tags.map(tag => (
                  <span key={tag} style={{ fontSize: 9, padding: "2px 8px", borderRadius: 8, background: T.panel2, border: `1px solid ${T.border}`, color: T.muted }}>{tag}</span>
                ))}
              </div>
              <div style={{ fontSize: 11, color: T.text, lineHeight: 1.7, marginBottom: 16 }}>{p.desc}</div>
              {p.available ? (
                <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: 11, fontWeight: 700, color: p.color }}>Open Dashboard <span>→</span></div>
              ) : (
                <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: 11, color: T.muted }}><span>🔔</span> Notify me when available</div>
              )}
            </div>
          ))}
        </div>
      </div>

      {comingSoonModal && (
        <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.72)", display: "flex", alignItems: "center", justifyContent: "center", zIndex: 1000, padding: 20 }}
          onClick={() => { setComingSoonModal(null); }}>
          <div style={{ background: T.panel, border: `1px solid ${T.border}`, borderRadius: 16, padding: "36px", width: 380, maxWidth: "100%" }} onClick={e => e.stopPropagation()}>
            <div style={{ textAlign: "center", marginBottom: 20 }}>
              <div style={{ fontSize: 40, marginBottom: 12 }}>🚧</div>
              <div style={{ fontSize: 18, fontWeight: 700, color: T.white, marginBottom: 8 }}>{comingSoonModal.title}</div>
              <div style={{ fontSize: 11, color: T.muted, lineHeight: 1.7 }}>This programme is coming soon. We're actively building it — register your interest and we'll notify you when it launches.</div>
            </div>
            {notifyDone[comingSoonModal.key] ? (
              <div style={{ textAlign: "center", padding: "14px", background: T.greenD, border: `1px solid ${T.green}40`, borderRadius: 10, color: T.green, fontSize: 12, fontWeight: 700 }}>
                ✓ You're on the list! We'll notify you when it launches.
              </div>
            ) : (
              <button onClick={() => handleNotify(comingSoonModal.key)} disabled={notifyLoading}
                style={{ width: "100%", padding: "12px", borderRadius: 10, background: `linear-gradient(135deg,${T.gold},#f0d070)`, border: "none", color: T.bg, fontSize: 13, fontWeight: 700, cursor: "pointer", opacity: notifyLoading ? 0.7 : 1 }}>
                {notifyLoading ? "Saving…" : "🔔 Notify me when available"}
              </button>
            )}
            <button onClick={() => { setComingSoonModal(null); }}
              style={{ width: "100%", marginTop: 10, padding: "10px", borderRadius: 10, background: "transparent", border: `1px solid ${T.border}`, color: T.muted, fontSize: 12, cursor: "pointer" }}>
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

function SetupScreen({ user, onReady }) {
  const [hospital,setHospital]=useState(null);
  const [assessments,setAssessments]=useState([]);
  const [selAss,setSelAss]=useState("");
  const [newHosp,setNewHosp]=useState("");
  const [newAss,setNewAss]=useState("");
  const [loading,setLoading]=useState(true);
  const [error,setError]=useState("");
  const [showOnboarding,setShowOnboarding]=useState(false);

  useEffect(()=>{init();},[]);

  const init=async()=>{
    setLoading(true);
    const{data:hosp}=await supabase.from("hospitals").select("*").limit(1).single();
    if(hosp){
      setHospital(hosp);
      const{data:ass}=await supabase.from("assessments").select("*").eq("hospital_id",hosp.id).order("created_at",{ascending:false});
      const assData=ass||[];
      setAssessments(assData);
      if(assData.length===1){
        onReady({hospitalId:hosp.id,assessmentId:assData[0].id,hospitalName:hosp.name,assessmentName:assData[0].name,userEmail:user.email,userId:user.id});
        return;
      }
      if(assData.length>0)setSelAss(assData[0].id);
    }
    setLoading(false);
  };

  const createHospital=async()=>{
    if(!newHosp.trim())return;
    setLoading(true);setError("");
    const{data,error:err}=await supabase.from("hospitals").insert({name:newHosp.trim(),nabh_status:"preparing"}).select().single();
    if(err){setError(err.message);setLoading(false);return;}
    await supabase.from("profiles").upsert({id:user.id,hospital_id:data.id,role:"admin",name:user.email});
    setHospital(data);setAssessments([]);setNewHosp("");setLoading(false);
    setShowOnboarding(true);
  };

  const handleOnboardingDone=async({nabh_status})=>{
    setShowOnboarding(false);
    setLoading(true);
    if(hospital){
      await supabase.from("hospitals").update({nabh_status:nabh_status||"preparing"}).eq("id",hospital.id);
    }
    const assName=`NABH Assessment ${new Date().getFullYear()}`;
    const{data:ass,error:assErr}=await supabase.from("assessments").insert({
      hospital_id:hospital.id,name:assName,created_by:user.id,status:"in_progress"
    }).select().single();
    if(assErr){setError(assErr.message);setLoading(false);return;}
    // Fire welcome email – non-blocking; won't break onboarding if the function is absent
    supabase.functions.invoke("send-welcome-email",{body:{
      email:user.email,
      hospitalName:hospital.name,
      nabh_status:nabh_status||"preparing"
    }}).catch(()=>{});
    setLoading(false);
    onReady({hospitalId:hospital.id,assessmentId:ass.id,hospitalName:hospital.name,assessmentName:assName,userEmail:user.email,userId:user.id});
  };

  const createAssessment=async()=>{
    if(!newAss.trim()||!hospital)return;
    setLoading(true);setError("");
    const{data,error:err}=await supabase.from("assessments").insert({hospital_id:hospital.id,name:newAss.trim(),created_by:user.id,status:"in_progress"}).select().single();
    if(err){setError(err.message);setLoading(false);return;}
    setAssessments(p=>[data,...p]);setSelAss(data.id);setNewAss("");setLoading(false);
  };

  const proceed=()=>{
    if(!hospital||!selAss)return;
    const ass=assessments.find(a=>a.id===selAss);
    onReady({hospitalId:hospital.id,assessmentId:selAss,hospitalName:hospital.name,assessmentName:ass?.name,userEmail:user.email,userId:user.id});
  };

  if(loading) return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",color:T.gold,fontFamily:"Segoe UI,sans-serif",fontSize:16}}>
      Setting up your workspace…
    </div>
  );

  if(showOnboarding&&hospital) return (
    <OnboardingScreen hospitalName={hospital.name} onDone={handleOnboardingDone}/>
  );

  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:16,padding:"36px",width:420}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:4}}>
          <div style={{fontSize:8,letterSpacing:3,color:T.gold}}>ACCREDREADY</div>
          <button onClick={()=>supabase.auth.signOut()} style={{fontSize:12,color:T.muted,background:"transparent",border:`1px solid ${T.border}`,borderRadius:6,padding:"3px 10px",cursor:"pointer"}}>Sign out</button>
        </div>

        {error&&<div style={{background:T.redD,border:`1px solid ${T.red}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:13,color:T.red,marginTop:12}}>{error}</div>}

        {!hospital&&(
          <>
            <div style={{fontSize:18,fontWeight:700,color:T.white,margin:"16px 0 8px"}}>Welcome! Set up your hospital</div>
            <div style={{fontSize:13,color:T.muted,marginBottom:20,lineHeight:1.6}}>Each account is linked to one hospital. Enter your hospital name to get started.</div>
            <div style={{fontSize:12,color:T.muted,marginBottom:8,letterSpacing:1}}>HOSPITAL NAME</div>
            <div style={{display:"flex",gap:8}}>
              <input value={newHosp} onChange={e=>setNewHosp(e.target.value)} placeholder="e.g. HMP Foundation Hospital" onKeyDown={e=>e.key==="Enter"&&createHospital()}
                style={{flex:1,padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,boxSizing:"border-box"}}/>
              <button onClick={createHospital} disabled={!newHosp.trim()} style={{padding:"10px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:14,fontWeight:700,cursor:newHosp.trim()?"pointer":"default",opacity:newHosp.trim()?1:0.5}}>Create</button>
            </div>
          </>
        )}

        {hospital&&(
          <>
            <div style={{fontSize:18,fontWeight:700,color:T.white,margin:"16px 0 4px"}}>{hospital.name}</div>
            <div style={{fontSize:12,color:T.green,marginBottom:20}}>✓ Hospital registered</div>

            <div style={{fontSize:12,color:T.muted,marginBottom:8,letterSpacing:1}}>ASSESSMENT</div>
            {assessments.length>0&&(
              <select value={selAss} onChange={e=>setSelAss(e.target.value)}
                style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,marginBottom:10,boxSizing:"border-box"}}>
                {assessments.map(a=><option key={a.id} value={a.id}>{a.name}</option>)}
              </select>
            )}
            <div style={{display:"flex",gap:8,marginBottom:16}}>
              <input value={newAss} onChange={e=>setNewAss(e.target.value)} placeholder="Or create new assessment…" onKeyDown={e=>e.key==="Enter"&&createAssessment()}
                style={{flex:1,padding:"9px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:"border-box"}}/>
              <button onClick={createAssessment} disabled={!newAss.trim()} style={{padding:"9px 16px",borderRadius:8,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:14,cursor:"pointer"}}>Add</button>
            </div>
            <button onClick={proceed} disabled={!selAss} style={{width:"100%",padding:"12px",borderRadius:10,background:selAss?`linear-gradient(135deg,${T.gold},#f0d070)`:T.border,border:"none",color:selAss?T.bg:T.muted,fontSize:15,fontWeight:700,cursor:selAss?"pointer":"default"}}>
              Open Assessment →
            </button>
          </>
        )}
      </div>
    </div>
  );
}

function VerdictBanner({ decision }) {
  const rd=decision.readiness||"NOT READY";
  const rdColor=rd==="NOT READY"?T.red:rd==="RISKY"?T.orange:T.green;
  const rdBg=rd==="NOT READY"?T.redD:rd==="RISKY"?T.orangeD:T.greenD;
  const vColor=decision.verdict==="FAIL"?T.red:decision.verdict==="PASS"?T.green:decision.verdict==="PARTIAL"?T.orange:T.blue;
  const failReasons=decision.fail_reasons||[];
  return (
    <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:14,overflow:"hidden",marginBottom:14}}>
      <div style={{height:4,background:`linear-gradient(90deg,${vColor},${rdColor})`}}/>
      <div style={{padding:"18px 22px"}}>
        <div style={{display:"flex",gap:20,alignItems:"center",flexWrap:"wrap"}}>
          <div style={{textAlign:"center",minWidth:100}}>
            <div style={{fontSize:11,letterSpacing:3,color:T.muted,marginBottom:4}}>VERDICT</div>
            <div style={{fontSize:34,fontWeight:900,color:vColor,fontFamily:"Georgia,serif",letterSpacing:2,lineHeight:1}}>{decision.verdict||"—"}</div>
          </div>
          <div style={{width:1,height:60,background:T.border}}/>
          <div style={{background:rdBg,border:`1px solid ${rdColor}30`,borderRadius:10,padding:"10px 18px",textAlign:"center"}}>
            <div style={{fontSize:8,letterSpacing:2,color:T.muted,marginBottom:4}}>READINESS</div>
            <div style={{fontSize:15,fontWeight:800,color:rdColor,letterSpacing:1}}>{rd}</div>
          </div>
          <div style={{width:1,height:60,background:T.border}}/>
          <Ring pct={decision.overall_pct||0} color={(decision.overall_pct||0)>=80?T.green:T.red} label="OVERALL"/>
          <Ring pct={decision.total_core>0?Math.round(((decision.total_core-(decision.core_failures||0))/decision.total_core)*100):0} color={decision.core_pass?T.green:T.red} label="CORE" size={90} stroke={7}/>
          <Ring pct={Math.round(((decision.scored_count||0)/639)*100)} color={T.blue} label="SCORED" size={90} stroke={7}/>
          <div style={{flex:1,minWidth:160}}>
            <div style={{fontSize:13,color:T.text,lineHeight:1.7}}>{decision.scored_count>0?`Scored ${decision.scored_count} of ${decision.total_oes||639} OEs. Overall ${decision.overall_pct||0}% compliance.`:decision.summary||"No data yet. Start scoring OEs."}</div>
            <div style={{display:"flex",gap:6,marginTop:8,flexWrap:"wrap"}}>
              {[["Rule 1: CORE",decision.rule1_core],["Rule 2: Overall ≥80%",decision.rule2_overall],["Rule 3: Chapters",decision.rule3_chapters],["Rule 4: Standards",decision.rule4_standards]].map(([label,pass])=>(
                <span key={label} style={{fontSize:11,padding:"2px 8px",borderRadius:8,background:pass?T.greenD:T.redD,color:pass?T.green:T.red,border:`1px solid ${pass?T.green:T.red}30`}}>{pass?"✓":"✗"} {label}</span>
              ))}
            </div>
          </div>
        </div>
        {failReasons.length>0&&(
          <div style={{marginTop:14,display:"grid",gap:6}}>
            {failReasons.map((r,i)=>(
              <div key={i} style={{display:"flex",gap:10,alignItems:"flex-start",background:r.severity==="CRITICAL"?T.redD:r.severity==="HIGH"?T.orangeD:T.goldD,border:`1px solid ${sevColor(r.severity)}25`,borderRadius:8,padding:"9px 14px"}}>
                <span style={{fontSize:16,flexShrink:0}}>{r.severity==="CRITICAL"?"🚨":r.severity==="HIGH"?"⚠️":"📌"}</span>
                <div>
                  <span style={{fontSize:11,padding:"1px 7px",borderRadius:5,background:`${sevColor(r.severity)}20`,color:sevColor(r.severity),marginRight:8,fontWeight:700}}>{r.severity}</span>
                  <span style={{fontSize:13,color:T.text,lineHeight:1.6}}>{r.message}</span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

function ChapterHeatmap({ breakdown }) {
  if(!breakdown||Object.keys(breakdown).length===0) return (
    <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 18px"}}>
      <div style={{fontSize:11,letterSpacing:2,color:T.muted,marginBottom:12}}>CHAPTER HEATMAP</div>
      <div style={{fontSize:13,color:T.muted,textAlign:"center",padding:"20px 0"}}>No scores yet. Start scoring OEs to see chapter breakdown.</div>
    </div>
  );
  return (
    <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 18px"}}>
      <div style={{fontSize:11,letterSpacing:2,color:T.muted,marginBottom:12}}>CHAPTER HEATMAP</div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(5,1fr)",gap:8}}>
        {Object.entries(breakdown).sort(([a],[b])=>(CHAPTER_ORDER[a]||99)-(CHAPTER_ORDER[b]||99)).map(([ch,data])=>{
          const pct=typeof data==="number"?data:(data?.pct||0);
          const pass=pct>=80;
          const col=chColor[ch]||T.gold;
          const bg=pct>=80?`${T.green}18`:pct>=70?`${T.orange}15`:`${T.red}15`;
          const brd=pct>=80?T.green:pct>=70?T.orange:T.red;
          return (
            <div key={ch} style={{background:bg,border:`1px solid ${brd}25`,borderRadius:8,padding:"10px 8px",textAlign:"center"}}>
              <div style={{fontSize:15,fontWeight:800,color:col,marginBottom:3}}>{ch}</div>
              <div style={{height:3,background:`${brd}20`,borderRadius:2,marginBottom:5}}><div style={{width:`${pct}%`,height:"100%",background:brd,borderRadius:2}}/></div>
              <div style={{fontSize:15,fontWeight:700,color:brd}}>{pct}%</div>
              <div style={{fontSize:8,color:T.muted,marginTop:1}}>{pass?"✓ Pass":"✗ Fail"}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

function Dashboard({ decision, gaps, onNav }) {
  const top5=[...(gaps||[])].sort((a,b)=>b.priority_score-a.priority_score).slice(0,5);

  // Build pillar status from decision object
  const oePct = decision.overall_pct||0;
  const oeStatus = decision.rule1_core&&decision.rule2_overall&&decision.rule3_chapters&&decision.rule4_standards ? "READY" : oePct>0 ? "IN_PROGRESS" : "NOT_STARTED";
  const kpiPct = decision.kpi_pct||0;
  const kpiStatus = decision.kpi_ready ? "READY" : kpiPct>0 ? "IN_PROGRESS" : "NOT_STARTED";
  const commPct = Math.round(((decision.comm_active||0)/26)*100);
  const commStatus = decision.comm_ready ? "READY" : (decision.comm_active||0)>0 ? "IN_PROGRESS" : "NOT_STARTED";
  const auditTotal = decision.audit_total||35;
  const auditPct = Math.round(((decision.audit_done||0)/auditTotal)*100);
  const auditStatus = decision.audit_ready ? "READY" : (decision.audit_done||0)>0 ? "IN_PROGRESS" : "NOT_STARTED";

  const pillars=[
    {key:"oe",   label:"OE Scoring",     icon:"📋", pct:oePct,    status:oeStatus,    nav:"scoring",    detail:`${decision.scored_count||0}/639 OEs`},
    {key:"kpi",  label:"KPI Tracking",   icon:"📈", pct:kpiPct,   status:kpiStatus,   nav:"kpis",       detail:`${decision.kpi_tracked||0}/${decision.kpi_total||50} KPIs ≥3mo`},
    {key:"comm", label:"Committees",     icon:"🏛️", pct:commPct,  status:commStatus,  nav:"committees", detail:`${decision.comm_active||0}/26 active`},
    {key:"audit",label:"Clinical Audits",icon:"🔍", pct:auditPct, status:auditStatus, nav:"audits",     detail:`${decision.audit_done||0}/${auditTotal} completed`},
  ];
  const statusColor=s=>s==="READY"?T.green:s==="IN_PROGRESS"?T.orange:T.red;
  const statusLabel=s=>s==="READY"?"✅ Ready":s==="IN_PROGRESS"?"⚠️ In Progress":"❌ Not Started";
  const allReady=pillars.every(p=>p.status==="READY");

  // ── Next Actions ───────────────────────────────────────────────
  const nextActions=(()=>{
    const items=[];
    const coreIssues=(decision.core_unscored||0)+(decision.core_scored_failures||0);
    if(decision.rule1_core===false&&coreIssues>0)
      items.push({sev:3,color:T.red,text:`⚠️ ${coreIssues} CORE OE${coreIssues>1?"s":""} need attention — assessment will be rejected`,nav:"scoring"});
    const scored=decision.scored_count||0;
    if(scored<639)
      items.push({sev:2,color:T.orange,text:`📝 Score remaining OEs — ${scored} of 639 scored so far`,nav:"scoring"});
    if((gaps||[]).length>0)
      items.push({sev:2,color:T.orange,text:`🔧 ${gaps.length} gap${gaps.length>1?"s":""} need corrective action`,nav:"gaps"});
    if(!decision.kpi_ready){
      const kt=decision.kpi_tracked||0;
      items.push({sev:1,color:T.gold,text:kt===0?"📈 KPI tracking not started — assessors verify 3 months of data":`📈 KPI tracking incomplete — ${kt}/${decision.kpi_total||50} KPIs tracked`,nav:"kpis"});
    }
    if(!decision.comm_ready){
      const ca=decision.comm_active||0;
      items.push({sev:1,color:T.gold,text:ca===0?"🏛️ No committee meetings recorded":`🏛️ Committees not ready — ${ca}/26 active`,nav:"committees"});
    }
    items.push({sev:1,color:T.gold,text:"🚨 Mock drill records missing",nav:"drills"});
    items.sort((a,b)=>b.sev-a.sev);
    return items.slice(0,4);
  })();

  return (
    <div>
      <VerdictBanner decision={decision}/>
      {/* Next Actions */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"14px 16px",marginTop:14,marginBottom:14}}>
        <div style={{fontSize:11,letterSpacing:2,color:T.muted,marginBottom:10}}>WHAT TO DO NEXT</div>
        {nextActions.length===0
          ?<div style={{fontSize:13,color:T.green,textAlign:"center",padding:"8px 0"}}>✅ All key actions completed — you're on track!</div>
          :nextActions.map((item,i)=>(
            <div key={i} style={{display:"flex",alignItems:"center",gap:10,padding:"8px 10px",borderRadius:8,borderLeft:`3px solid ${item.color}`,background:`${item.color}10`,marginBottom:i<nextActions.length-1?6:0}}>
              <div style={{flex:1,fontSize:13,color:T.text,lineHeight:1.4}}>{item.text}</div>
              <button onClick={()=>onNav(item.nav)} style={{padding:"3px 9px",borderRadius:6,border:`1px solid ${item.color}40`,background:"transparent",color:item.color,fontSize:13,cursor:"pointer",flexShrink:0}}>→</button>
            </div>
          ))
        }
      </div>
      {/* 4-Pillar Readiness */}
      <div style={{background:T.panel,border:`1px solid ${allReady?T.green:T.border}`,borderRadius:12,padding:"14px 16px",marginTop:14,marginBottom:14}}>
        <div style={{fontSize:11,letterSpacing:2,color:T.muted,marginBottom:10}}>ASSESSMENT READINESS — 4 PILLARS</div>
        <div style={{display:"grid",gridTemplateColumns:"repeat(4,1fr)",gap:10}}>
          {pillars.map(p=>(
            <div key={p.key} onClick={()=>onNav(p.nav)} style={{background:T.panel2,border:`1px solid ${statusColor(p.status)}30`,borderRadius:10,padding:"12px 10px",cursor:"pointer",textAlign:"center"}}>
              <div style={{fontSize:20,marginBottom:4}}>{p.icon}</div>
              <div style={{fontSize:12,fontWeight:700,color:T.white,marginBottom:4}}>{p.label}</div>
              <div style={{fontSize:18,fontWeight:800,color:statusColor(p.status),marginBottom:2}}>{Math.round(p.pct)}%</div>
              <div style={{fontSize:8,color:T.muted,marginBottom:4}}>{p.detail}</div>
              <div style={{fontSize:8,color:statusColor(p.status)}}>{statusLabel(p.status)}</div>
              <div style={{height:3,background:T.border,borderRadius:2,marginTop:8}}>
                <div style={{height:"100%",borderRadius:2,background:statusColor(p.status),width:`${Math.min(100,p.pct)}%`}}/>
              </div>
            </div>
          ))}
        </div>
        {!allReady&&<div style={{marginTop:10,padding:"8px 12px",background:T.redD,borderRadius:8,fontSize:12,color:T.red}}>⚠️ NABH assessors verify all 4 pillars — OE scores, KPI data (≥3 months), committee meeting minutes, and clinical audit records. App shows PASS only when all 4 pillars are ready.</div>}
      </div>
      <ChapterHeatmap breakdown={decision.chapter_breakdown}/>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 18px",marginTop:14}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:12}}>
          <div style={{fontSize:11,letterSpacing:2,color:T.muted}}>TOP 5 GAPS BY PRIORITY</div>
          <button onClick={()=>onNav("gaps")} style={{fontSize:12,color:T.gold,background:"transparent",border:`1px solid ${T.gold}30`,borderRadius:10,padding:"3px 10px",cursor:"pointer"}}>View all →</button>
        </div>
        {top5.length===0&&<div style={{fontSize:13,color:T.muted,textAlign:"center",padding:"16px 0"}}>No gaps yet. Score some OEs first.</div>}
        {top5.map((g,i)=>(
          <div key={g.oe_id} style={{display:"flex",gap:10,alignItems:"center",padding:"8px 0",borderBottom:i<4?`1px solid ${T.border}`:"none"}}>
            <div style={{width:22,height:22,borderRadius:6,background:g.level==="CORE"?T.redD:T.orangeD,border:`1px solid ${g.level==="CORE"?T.red:T.orange}40`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,fontWeight:800,color:g.level==="CORE"?T.red:T.orange,flexShrink:0}}>{i+1}</div>
            <div style={{flex:1}}>
              <div style={{display:"flex",gap:6,alignItems:"center",marginBottom:2}}>
                <span style={{fontSize:12,fontWeight:700,color:lvColor(g.level),fontFamily:"monospace"}}>{g.oe_id}</span>
                {g.level==="CORE"&&<span style={{fontSize:8,padding:"1px 5px",borderRadius:4,background:T.redD,color:T.red}}>CORE</span>}
              </div>
              <div style={{fontSize:12,color:T.muted,lineHeight:1.3}}>{(g.oe_text||"").slice(0,70)}…</div>
            </div>
            <div style={{textAlign:"center",flexShrink:0}}>
              <div style={{fontSize:16,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
              <div style={{fontSize:7,color:T.muted}}>/ 5</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function ScoringScreen({ assessmentId, oes, standards, onRefresh }) {
  const [filter,setFilter]=useState("ALL"); const [chFilter,setChFilter]=useState("ALL");
  const [search,setSearch]=useState("");
  const [toast,setToast]=useState(null); const [saving,setSaving]=useState({});
  const [localScores,setLocalScores]=useState({}); const [showTip,setShowTip]=useState({});
  const [localLinks,setLocalLinks]=useState({}); const [linkInputOpen,setLinkInputOpen]=useState({});
  const [linkUrl,setLinkUrl]=useState({}); const [linkLabel,setLinkLabel]=useState({}); const [linkBusy,setLinkBusy]=useState({});
  useEffect(()=>{const s={};const l={};oes.forEach(oe=>{s[oe.id]=oe.score||null;l[oe.id]=oe.evidenceLinks||[];});setLocalScores(s);setLocalLinks(l);},[oes]);
  const chapters=["ALL","AAC","COP","MOM","PRE","IPC","PSQ","ROM","FMS","HRM","IMS"];
  const levels=["ALL","CORE","Commitment","Achievement","Excellence"];
  const filtered=oes.filter(oe=>{const lm=filter==="ALL"||oe.level===filter;const cm=chFilter==="ALL"||oe.chapter===chFilter;const sm=!search||oe.id.toLowerCase().includes(search.toLowerCase())||(oe.text||"").toLowerCase().includes(search.toLowerCase());return lm&&cm&&sm;});
  const scored=Object.values(localScores).filter(s=>s!==null).length;
  const handleScore=async(oeId,oeLevel,oeDoc,newScore)=>{
    const isUnset=localScores[oeId]===newScore;
    if(isUnset){
      setLocalScores(p=>({...p,[oeId]:null}));setSaving(p=>({...p,[oeId]:true}));
      const{error}=await supabase.from("scores").delete().match({assessment_id:assessmentId,oe_id:oeId});
      setSaving(p=>({...p,[oeId]:false}));
      if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});return;}
      setToast({type:"SCORE CLEARED",sev:"SUCCESS",msg:"Score removed. Click again to re-score."});
      setTimeout(()=>setToast(null),3000);
      onRefresh();
      return;
    }
    setLocalScores(p=>({...p,[oeId]:newScore}));setSaving(p=>({...p,[oeId]:true}));
    const{error}=await supabase.from("scores").upsert({assessment_id:assessmentId,oe_id:oeId,score:newScore,updated_at:new Date().toISOString()},{onConflict:"assessment_id,oe_id"});
    setSaving(p=>({...p,[oeId]:false}));
    if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});return;}
    const{data}=await supabase.rpc("get_score_impact",{param_assessment:assessmentId,param_oe:oeId,param_score:newScore});
    if(data?.alerts?.length>0){
      const a=data.alerts[0];
      const isDocAlert=(a.type||"").toUpperCase().includes("DOC")||(a.message||"").toLowerCase().includes("documentation");
      const hasLinks=(localLinks[oeId]||[]).length>0;
      if(!(isDocAlert&&hasLinks)){
        setToast({type:a.type,sev:a.severity,msg:a.message});setTimeout(()=>setToast(null),4000);
      }
    }
    onRefresh();
  };
  const scoreBtn=(oeId,oeLevel,oeDoc,score,label,color)=>(
    <button key={score} onClick={()=>handleScore(oeId,oeLevel,oeDoc,score)} style={{padding:"5px 10px",borderRadius:7,fontSize:13,fontWeight:700,cursor:"pointer",background:localScores[oeId]===score?`${color}30`:T.panel2,border:`1px solid ${localScores[oeId]===score?color:`${color}40`}`,color:localScores[oeId]===score?color:T.muted,transition:"all 0.15s"}}>{label}</button>
  );

  const validUrl=(s)=>{try{const u=new URL(s);return u.protocol==="http:"||u.protocol==="https:";}catch{return false;}};
  const domainOf=(s)=>{try{return new URL(s).hostname.replace(/^www\./,"");}catch{return s;}};

  const saveLink=async(oeId)=>{
    const url=(linkUrl[oeId]||"").trim();
    const label=(linkLabel[oeId]||"").trim();
    if(!url){setToast({type:"ERROR",sev:"CRITICAL",msg:"Paste a URL first."});setTimeout(()=>setToast(null),3000);return;}
    if(!validUrl(url)){setToast({type:"ERROR",sev:"CRITICAL",msg:"Invalid URL. Must start with http:// or https://"});setTimeout(()=>setToast(null),3000);return;}
    const existing=localLinks[oeId]||[];
    if(existing.length>=10){setToast({type:"LIMIT",sev:"HIGH",msg:"Max 10 links per OE."});setTimeout(()=>setToast(null),3000);return;}
    const newEntry={url,label:label||domainOf(url),added_at:new Date().toISOString()};
    const updated=[...existing,newEntry];
    setLinkBusy(p=>({...p,[oeId]:true}));
    const{error}=await supabase.from("scores").upsert({assessment_id:assessmentId,oe_id:oeId,score:localScores[oeId]||null,evidence_links:updated,updated_at:new Date().toISOString()},{onConflict:"assessment_id,oe_id"});
    setLinkBusy(p=>({...p,[oeId]:false}));
    if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});setTimeout(()=>setToast(null),4000);return;}
    setLocalLinks(p=>({...p,[oeId]:updated}));
    setLinkUrl(p=>({...p,[oeId]:""}));setLinkLabel(p=>({...p,[oeId]:""}));
    setToast({type:"EVIDENCE ADDED",sev:"SUCCESS",msg:"Evidence link saved."});setTimeout(()=>setToast(null),2500);
    onRefresh();
  };

  const removeLink=async(oeId,index)=>{
    const existing=localLinks[oeId]||[];
    const updated=existing.filter((_,i)=>i!==index);
    setLinkBusy(p=>({...p,[oeId]:true}));
    const{error}=await supabase.from("scores").upsert({assessment_id:assessmentId,oe_id:oeId,score:localScores[oeId]||null,evidence_links:updated,updated_at:new Date().toISOString()},{onConflict:"assessment_id,oe_id"});
    setLinkBusy(p=>({...p,[oeId]:false}));
    if(error){setToast({type:"ERROR",sev:"CRITICAL",msg:error.message});setTimeout(()=>setToast(null),4000);return;}
    setLocalLinks(p=>({...p,[oeId]:updated}));
    onRefresh();
  };
  return (
    <div>
      {toast&&<div style={{position:"fixed",top:80,right:16,zIndex:999,maxWidth:360,background:toast.sev==="CRITICAL"?T.redD:toast.sev==="SUCCESS"?T.greenD:toast.sev==="HIGH"?T.orangeD:T.goldD,border:`1px solid ${toast.sev==="CRITICAL"?T.red:toast.sev==="SUCCESS"?T.green:toast.sev==="HIGH"?T.orange:T.gold}50`,borderRadius:10,padding:"12px 16px",boxShadow:"0 8px 32px rgba(0,0,0,0.5)"}}>
        <div style={{fontSize:12,fontWeight:700,marginBottom:4,color:toast.sev==="CRITICAL"?T.red:toast.sev==="SUCCESS"?T.green:toast.sev==="HIGH"?T.orange:T.gold}}>{toast.sev==="CRITICAL"?"🚨":toast.sev==="SUCCESS"?"✅":toast.sev==="HIGH"?"⚠️":"📄"} {toast.type?.replace(/_/g," ")}</div>
        <div style={{fontSize:13,color:T.text,lineHeight:1.5}}>{toast.msg}</div>
      </div>}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:12}}>
        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:8}}>
          <div style={{fontSize:13,color:T.text}}>Scored: <strong style={{color:T.gold}}>{scored}</strong> / {oes.length} OEs</div>
          <div style={{fontSize:12,color:T.muted}}>{Math.round(scored/Math.max(oes.length,1)*100)}% complete</div>
        </div>
        <div style={{height:4,background:T.border,borderRadius:2}}>
          <div style={{width:`${Math.round(scored/Math.max(oes.length,1)*100)}%`,height:"100%",background:`linear-gradient(90deg,${T.gold},${T.green})`,borderRadius:2,transition:"width 0.5s"}}/>
        </div>
      </div>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 14px",marginBottom:14}}>
        <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search OEs by ID or text (e.g. 'hand hygiene', 'COP.1.a', 'fall risk')..." style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${search?T.gold:T.border}`,background:T.panel2,color:T.text,fontSize:14,marginBottom:10,boxSizing:"border-box"}}/>
        <div style={{display:"flex",gap:8,flexWrap:"wrap",alignItems:"center"}}>
          <div style={{display:"flex",gap:4,flexWrap:"wrap"}}>{levels.map(l=><button key={l} onClick={()=>setFilter(l)} style={{padding:"5px 12px",borderRadius:8,fontSize:12,cursor:"pointer",background:filter===l?T.goldD:T.panel2,border:`1px solid ${filter===l?T.gold:T.border}`,color:filter===l?T.goldL:T.muted}}>{l}</button>)}</div>
          <select value={chFilter} onChange={e=>setChFilter(e.target.value)} style={{padding:"5px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:12}}>{chapters.map(c=><option key={c} value={c}>{c}</option>)}</select>
          {(search||filter!=="ALL"||chFilter!=="ALL")&&(<button onClick={()=>{setSearch("");setFilter("ALL");setChFilter("ALL");}} style={{padding:"4px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.redD,border:`1px solid ${T.red}30`,color:T.red}}>X Clear</button>)}
          <span style={{fontSize:11,color:T.muted,marginLeft:"auto"}}>{filtered.length} OEs shown</span>
        </div>
      </div>
      <div style={{display:"grid",gap:8}}>
        {(() => {
          // Build standard lookup: id → title
          const stdMap = {};
          (standards||[]).forEach(s => { stdMap[s.id] = s.title; });
          // Group filtered OEs by standard_id, preserving order
          const groups = [];
          const seen = {};
          filtered.forEach(oe => {
            const sid = oe.standard || "_unknown";
            if (!seen[sid]) { seen[sid] = []; groups.push({ id: sid, items: seen[sid] }); }
            seen[sid].push(oe);
          });
          return groups.map(g => (
            <div key={g.id}>
              {g.id !== "_unknown" && (
                <div style={{
                  background: T.headerBg||T.panel2,
                  border: T.headerBg?`1px solid ${T.gold}30`:`1px solid ${T.gold}40`,
                  borderLeft: T.headerBg?`4px solid ${T.gold}`:`3px solid ${T.gold}`,
                  borderRadius: 8,
                  padding: "10px 14px",
                  marginTop: 14,
                  marginBottom: 6
                }}>
                  <div style={{ fontSize: 9, letterSpacing: 2, color: T.gold, marginBottom: 4 }}>
                    STANDARD {g.id.replace(/\.$/,"")}
                  </div>
                  <div style={{ fontSize: 11, color: T.white, lineHeight: 1.5, fontWeight: 600 }}>
                    {stdMap[g.id] || "Standard title not available"}
                  </div>
                </div>
              )}
              <div style={{display:"grid",gap:8}}>
              {g.items.map(oe=>{
                const currentScore=localScores[oe.id]; const isSaving=saving[oe.id];
                const scoreColor=!currentScore?T.muted:currentScore<=2?T.red:currentScore===3?T.orange:T.green;
                return (
                  <div key={oe.id} style={{background:T.panel,border:`1px solid ${oe.level==="CORE"?`${T.red}30`:T.border}`,borderRadius:10,padding:"14px 16px",opacity:isSaving?0.7:1,boxShadow:T.panelShadow||""}}>
                    <div style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:10}}>
                      <div style={{flexShrink:0}}>
                        <span style={{fontFamily:"monospace",fontSize:13,fontWeight:700,color:lvColor(oe.level)}}>{oe.id}</span>{" "}
                        <span style={{fontSize:11,padding:"2px 7px",borderRadius:5,background:`${lvColor(oe.level)}22`,color:lvColor(oe.level)}}>{oe.level}</span>
                        {oe.doc&&<span style={{fontSize:11,padding:"2px 6px",borderRadius:5,background:T.goldD,color:T.gold,marginLeft:4}}>DOC*</span>}
                      </div>
                      <div style={{fontSize:12,color:T.text,lineHeight:1.5,flex:1}}>{oe.text}</div>
                      <div style={{fontSize:22,fontWeight:800,color:scoreColor,flexShrink:0,minWidth:30,textAlign:"center"}}>{isSaving?"…":currentScore||"—"}</div>
                    </div>
                    <div style={{display:"flex",gap:6,flexWrap:"wrap",alignItems:"center"}}>
                      {scoreBtn(oe.id,oe.level,oe.doc,1,"1 – None",T.red)}
                      {scoreBtn(oe.id,oe.level,oe.doc,2,"2 – Partial",T.orange)}
                      {scoreBtn(oe.id,oe.level,oe.doc,3,"3 – Mostly",T.gold)}
                      {scoreBtn(oe.id,oe.level,oe.doc,4,"4 – Full",T.green)}
                      {scoreBtn(oe.id,oe.level,oe.doc,5,"5 – Excellent",T.blue)}
                      <button onClick={()=>setShowTip(p=>({...p,[oe.id]:!p[oe.id]}))}
                        style={{marginLeft:"auto",padding:"4px 10px",borderRadius:7,fontSize:12,cursor:"pointer",
                          background:showTip[oe.id]?T.blueD:"transparent",
                          border:`1px solid ${showTip[oe.id]?T.blue:T.muted}`,
                          color:showTip[oe.id]?T.blue:T.muted}}>
                        {showTip[oe.id]?"▲ Hide":"? How to achieve"}
                      </button>
                    </div>
                    {oe.doc&&(()=>{
                      const links=localLinks[oe.id]||[];
                      const isOpen=linkInputOpen[oe.id];
                      const busy=linkBusy[oe.id];
                      return (
                        <div style={{marginTop:10,background:links.length>0?T.greenD:T.orangeD,border:`1px solid ${links.length>0?T.green:T.orange}30`,borderRadius:8,padding:"10px 12px"}}>
                          <div style={{display:"flex",gap:8,alignItems:"center",flexWrap:"wrap",marginBottom:links.length>0||isOpen?8:0}}>
                            <span style={{fontSize:12,fontWeight:700,color:links.length>0?T.green:T.orange,letterSpacing:1}}>
                              {links.length>0?`📎 EVIDENCE (${links.length})`:"⚠️ DOCUMENTATION REQUIRED"}
                            </span>
                            {links.length===0&&<span style={{fontSize:12,color:T.muted}}>This OE requires evidence — paste a Drive/OneDrive/Dropbox link.</span>}
                            <button onClick={()=>setLinkInputOpen(p=>({...p,[oe.id]:!p[oe.id]}))} style={{marginLeft:"auto",padding:"3px 10px",borderRadius:6,fontSize:12,cursor:"pointer",background:isOpen?T.panel2:`${T.gold}20`,border:`1px solid ${T.gold}40`,color:T.gold,fontWeight:700}}>
                              {isOpen?"✕ Cancel":"+ Add link"}
                            </button>
                          </div>
                          {links.length>0&&(
                            <div style={{display:"flex",gap:5,flexWrap:"wrap",marginBottom:isOpen?8:0}}>
                              {links.map((l,i)=>(
                                <div key={i} style={{display:"flex",alignItems:"center",gap:5,padding:"4px 4px 4px 10px",borderRadius:6,background:T.panel2,border:`1px solid ${T.green}30`,fontSize:12}}>
                                  <a href={l.url} target="_blank" rel="noopener noreferrer" style={{color:T.text,textDecoration:"none",maxWidth:200,overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}>📄 {l.label||domainOf(l.url)}</a>
                                  <span style={{fontSize:11,color:T.muted}}>· {domainOf(l.url)}</span>
                                  <button onClick={()=>removeLink(oe.id,i)} disabled={busy} style={{padding:"2px 7px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:11,cursor:"pointer"}}>✕</button>
                                </div>
                              ))}
                            </div>
                          )}
                          {isOpen&&(
                            <div style={{display:"grid",gap:6,paddingTop:6,borderTop:`1px dashed ${T.border}`}}>
                              <input value={linkUrl[oe.id]||""} onChange={e=>setLinkUrl(p=>({...p,[oe.id]:e.target.value}))} placeholder="https://drive.google.com/..." style={{padding:"7px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13}}/>
                              <div style={{display:"flex",gap:6}}>
                                <input value={linkLabel[oe.id]||""} onChange={e=>setLinkLabel(p=>({...p,[oe.id]:e.target.value}))} placeholder="Optional label (e.g., 'IPC Policy v3')" style={{flex:1,padding:"7px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13}}/>
                                <button onClick={()=>saveLink(oe.id)} disabled={busy} style={{padding:"6px 14px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:13,fontWeight:700,cursor:busy?"not-allowed":"pointer",opacity:busy?0.5:1}}>{busy?"Saving…":"Save link"}</button>
                              </div>
                              <div style={{fontSize:11,color:T.muted}}>Paste any URL — Google Drive, OneDrive, Dropbox, internal HIS, etc. Files stay in your storage; only the link is saved here.</div>
                            </div>
                          )}
                        </div>
                      );
                    })()}
                    {showTip[oe.id]&&(()=>{
                      const tips=oe.achieveTips;
                      const chapterTips=OE_TIPS[oe.chapter]||null;
                      const lvlTips = oe.level==="CORE"
                        ? ["CORE element — assessed at EVERY NABH visit, not just final","Score <4 on any CORE = automatic FAIL regardless of overall score","Prioritise this OE above all others in your improvement plan","Assessors will examine records, observe practice, and interview staff"]
                        : oe.level==="Achievement"
                        ? ["Achievement level — assessed at Final Assessment only","Must show measurable outcomes, not just process compliance","Collect before/after data to demonstrate improvement","Quality committee validates achievement data"]
                        : oe.level==="Excellence"
                        ? ["Excellence level — assessed at Re-accreditation only","Demonstrate innovation and leadership beyond basic compliance","Benchmark against national/international best practices","Document formal recognition or external validation"]
                        : ["Commitment level — assessed at Final Assessment","Document the policy/SOP and evidence of implementation","Staff must be able to demonstrate knowledge when interviewed","Audit trail: records should show consistent compliance"];
                      const displayTips = tips || chapterTips || lvlTips;
                      const tipLabel = tips?"HOW TO ACHIEVE THIS OE":chapterTips?"CHAPTER GUIDANCE — "+oe.chapter:"GENERAL GUIDANCE — "+oe.level.toUpperCase();
                      return (
                        <div style={{marginTop:10,background:T.blueD,border:`1px solid ${T.blue}20`,borderRadius:8,padding:"12px 14px"}}>
                          <div style={{fontSize:11,letterSpacing:2,color:T.blue,marginBottom:8}}>
                            {tipLabel}
                          </div>
                          {displayTips.map((tip,i)=>(
                            <div key={i} style={{display:"flex",gap:8,marginBottom:6,alignItems:"flex-start"}}>
                              <div style={{width:18,height:18,borderRadius:"50%",background:`${T.blue}20`,border:`1px solid ${T.blue}40`,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,fontSize:11,color:T.blue,fontWeight:700}}>{i+1}</div>
                              <div style={{fontSize:13,color:T.text,lineHeight:1.6,paddingTop:1}}>{tip}</div>
                            </div>
                          ))}
                          {!tips&&!chapterTips&&<div style={{fontSize:11,color:T.muted,marginTop:6,fontStyle:"italic"}}>Specific achieve tips not available for this OE — general {oe.level} guidance shown.</div>}
                        </div>
                      );
                    })()}
                  </div>
                );
              })}
              </div>
            </div>
          ));
        })()}
        {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"30px",fontSize:14}}>{search?"No OEs match your search. Try different keywords or clear filters.":"No OEs match this filter."}</div>}
      </div>
    </div>
  );
}

function GapFixScreen({ assessmentId, gaps, onRefresh }) {
  const [sevFilter,setSevFilter]=useState("ALL"); const [capas,setCapas]=useState({}); const [saving,setSaving]=useState({});
  const [search, setSearch] = useState('');
  const filteredGaps = (gaps||[]).filter(g => {
    const matchesSev = sevFilter === 'ALL' || g.severity === sevFilter;
    const matchesSearch = !search ||
      g.oe_id?.toLowerCase().includes(search.toLowerCase()) ||
      g.text?.toLowerCase().includes(search.toLowerCase());
    return matchesSev && matchesSearch;
  });
  const submitCapa=async(oeId)=>{
    const c=capas[oeId];if(!c?.finding||!c?.action)return;setSaving(p=>({...p,[oeId]:true}));
    await supabase.from("capa").upsert({assessment_id:assessmentId,oe_id:oeId,finding:c.finding,root_cause:c.root_cause||"",action_planned:c.action,action_type:c.action_type||"Process",responsible_person:c.person||"",target_date:c.date||null,status:"open"},{onConflict:"assessment_id,oe_id"});
    setSaving(p=>({...p,[oeId]:false}));setCapas(p=>({...p,[oeId]:{...p[oeId],saved:true}}));onRefresh();
  };
  return (
    <div>
      <input
        value={search}
        onChange={e=>setSearch(e.target.value)}
        placeholder="Search gaps by OE ID or text (e.g. 'AAC.1.a', 'hand hygiene')..."
        style={{width:'100%',padding:'10px 14px',borderRadius:8,border:'1px solid #0f2640',background:'#081525',color:'#eef4f9',fontSize:14,marginBottom:10,boxSizing:'border-box'}}
      />
      <div style={{display:"flex",gap:8,marginBottom:14}}>
        {["ALL","CRITICAL","HIGH","MEDIUM","LOW"].map(s=><button key={s} onClick={()=>setSevFilter(s)} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:sevFilter===s?`${sevColor(s)}20`:"transparent",border:`1px solid ${sevFilter===s?sevColor(s):T.border}`,color:sevFilter===s?sevColor(s):T.muted}}>{s}</button>)}
        <div style={{marginLeft:"auto",fontSize:13,color:T.muted,alignSelf:"center"}}>{filteredGaps.length} gaps</div>
      </div>
      {filteredGaps.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"40px",fontSize:14}}>{(gaps||[]).length===0?"No gaps found. Score OEs first.":"No gaps at this severity level."}</div>}
      <div style={{display:"grid",gap:10}}>
        {filteredGaps.map(g=>{
          const c=capas[g.oe_id]||{}; const expanded=c.expanded;
          return (
            <div key={g.oe_id} style={{background:T.panel,border:`1px solid ${sevColor(g.severity)}25`,borderRadius:12,overflow:"hidden"}}>
              <div style={{height:3,background:sevColor(g.severity)}}/>
              <div style={{padding:"14px 16px"}}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:8}}>
                  <div style={{flex:1}}>
                    <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:4,flexWrap:"wrap"}}>
                      <span style={{fontFamily:"monospace",fontSize:13,fontWeight:700,color:lvColor(g.level)}}>{g.oe_id}</span>
                      <span style={{fontSize:11,padding:"2px 7px",borderRadius:5,background:`${sevColor(g.severity)}15`,color:sevColor(g.severity)}}>{g.severity}</span>
                      {g.level==="CORE"&&<span style={{fontSize:11,padding:"2px 6px",borderRadius:5,background:T.redD,color:T.red}}>CORE</span>}
                      {g.gap_closed&&<span style={{fontSize:11,padding:"2px 6px",borderRadius:5,background:T.greenD,color:T.green}}>✓ CLOSED</span>}
                    </div>
                    <div style={{fontSize:12,color:T.text,lineHeight:1.5,marginBottom:6}}>{g.oe_text}</div>
                    <div style={{fontSize:12,color:T.muted,fontStyle:"italic"}}>{g.message}</div>
                  </div>
                  <div style={{textAlign:"center",flexShrink:0}}>
                    <div style={{fontSize:22,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
                    <div style={{fontSize:7,color:T.muted}}>/ 5</div>
                  </div>
                </div>
                <button onClick={()=>setCapas(p=>({...p,[g.oe_id]:{...c,expanded:!expanded}}))} style={{fontSize:12,color:T.gold,background:"transparent",border:`1px solid ${T.gold}30`,borderRadius:8,padding:"4px 14px",cursor:"pointer"}}>{expanded?"▲ Hide CAPA":"▼ Add CAPA"}</button>
                {expanded&&(
                  <div style={{marginTop:12,display:"grid",gap:8}}>
                    {c.saved&&<div style={{fontSize:12,color:T.green,padding:"6px 10px",background:T.greenD,borderRadius:6}}>✓ CAPA saved</div>}
                    <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>FINDING *</div><textarea value={c.finding||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,finding:e.target.value}}))} rows={2} placeholder="Describe the non-compliance finding…" style={{width:"100%",padding:"8px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:"vertical",boxSizing:"border-box"}}/></div>
                    <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>ACTION PLANNED *</div><textarea value={c.action||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,action:e.target.value}}))} rows={2} placeholder="Corrective action to be taken…" style={{width:"100%",padding:"8px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:"vertical",boxSizing:"border-box"}}/></div>
                    <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                      <div style={{flex:1,minWidth:140}}><div style={{fontSize:11,color:T.muted,marginBottom:4}}>RESPONSIBLE PERSON</div><input value={c.person||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,person:e.target.value}}))} placeholder="Name / Designation" style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:"border-box"}}/></div>
                      <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>TARGET DATE</div><input type="date" value={c.date||""} onChange={e=>setCapas(p=>({...p,[g.oe_id]:{...c,date:e.target.value}}))} style={{padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/></div>
                      <button onClick={()=>submitCapa(g.oe_id)} disabled={saving[g.oe_id]||!c.finding||!c.action} style={{marginTop:14,padding:"7px 20px",borderRadius:10,background:`linear-gradient(135deg,${T.green},#3d9e6e)`,border:"none",color:T.bg,fontSize:14,fontWeight:700,cursor:c.finding&&c.action?"pointer":"default",opacity:c.finding&&c.action?1:0.5}}>{saving[g.oe_id]?"Saving…":"Save CAPA →"}</button>
                    </div>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}


// ── COMMITTEES — with full MOM ─────────────────────────────
function CommitteesScreen({ hospitalId }) {
  const [committees,setCommittees]=useState([]);
  const [meetings,setMeetings]=useState([]);
  const [loading,setLoading]=useState(true);
  const [search,setSearch]=useState("");
  const [filter,setFilter]=useState("ALL");
  const [expanded,setExpanded]=useState(null);
  const [guideOpen,setGuideOpen]=useState(null);
  const [view,setView]=useState("reference"); // reference | mom
  const [showMOMForm,setShowMOMForm]=useState(null); // committee_id
  const [saving,setSaving]=useState(false);
  const [momSuccess,setMomSuccess]=useState(false);

  // MOM form state
  const emptyMOM = () => ({
    meeting_date:"", meeting_no:"", venue:"", chairperson:"",
    members_present:"", members_total:"", quorum_met:true,
    agenda_items:[{item:"",discussion:"",decision:"",action_owner:"",target_date:""}],
    minutes_text:"", previous_capa_reviewed:false,
    next_meeting_date:"", next_meeting_agenda:"",
    minutes_approved_by:"", minutes_approved_date:"",
    evidence_url:""
  });
  const [momForm,setMOMForm]=useState(emptyMOM());

  useEffect(()=>{
    supabase.from("committees").select("*").order("id").then(({data})=>setCommittees(data||[]));
    if(hospitalId){
      supabase.from("committee_meetings").select("*").eq("hospital_id",hospitalId)
        .order("meeting_date",{ascending:false})
        .then(({data})=>{setMeetings(data||[]);setLoading(false);});
    } else { setLoading(false); }
  },[hospitalId]);

  const filtered=committees.filter(c=>{
    const ms=!search||c.name.toLowerCase().includes(search.toLowerCase())||c.chapter_ref?.toLowerCase().includes(search.toLowerCase());
    const mf=filter==="ALL"||(filter==="NEW"&&c.is_new_in_6th)||(filter==="JCI"&&c.is_jci);
    return ms&&mf;
  });

  // committee meeting counts
  const meetingCount=(cid)=>meetings.filter(m=>m.committee_id===cid).length;
  const lastMeeting=(cid)=>{
    const m=meetings.filter(m=>m.committee_id===cid).sort((a,b)=>new Date(b.meeting_date)-new Date(a.meeting_date))[0];
    return m?m.meeting_date:null;
  };

  const addAgendaItem=()=>setMOMForm(f=>({...f,agenda_items:[...f.agenda_items,{item:"",discussion:"",decision:"",action_owner:"",target_date:""}]}));
  const updateAgenda=(i,k,v)=>setMOMForm(f=>{const a=[...f.agenda_items];a[i]={...a[i],[k]:v};return{...f,agenda_items:a};});
  const removeAgenda=(i)=>setMOMForm(f=>({...f,agenda_items:f.agenda_items.filter((_,idx)=>idx!==i)}));

  const saveMOM=async(committeeId)=>{
    if(!momForm.meeting_date||!momForm.chairperson){alert("Meeting date and chairperson are required.");return;}
    setSaving(true);
    const {error}=await supabase.from("committee_meetings").insert({
      hospital_id:hospitalId,
      committee_id:committeeId,
      meeting_date:momForm.meeting_date,
      meeting_no:momForm.meeting_no||null,
      venue:momForm.venue||null,
      chairperson:momForm.chairperson,
      quorum_met:momForm.quorum_met,
      members_present:momForm.members_present?parseInt(momForm.members_present):null,
      members_total:momForm.members_total?parseInt(momForm.members_total):null,
      agenda_items:momForm.agenda_items.filter(a=>a.item.trim()),
      minutes_text:momForm.minutes_text||null,
      previous_capa_reviewed:momForm.previous_capa_reviewed,
      next_meeting_date:momForm.next_meeting_date||null,
      next_meeting_agenda:momForm.next_meeting_agenda||null,
      minutes_approved_by:momForm.minutes_approved_by||null,
      minutes_approved_date:momForm.minutes_approved_date||null,
      evidence_url:momForm.evidence_url||null,
    });
    if(!error){
      const{data}=await supabase.from("committee_meetings").select("*").eq("hospital_id",hospitalId).order("meeting_date",{ascending:false});
      setMeetings(data||[]);
      setShowMOMForm(null);
      setMOMForm(emptyMOM());
      setMomSuccess(true);
      setTimeout(()=>setMomSuccess(false),3000);
    } else { alert("Error saving MOM: "+error.message); }
    setSaving(false);
  };

  const deleteMeeting=async(id)=>{
    if(!window.confirm("Delete this meeting record?"))return;
    await supabase.from("committee_meetings").delete().eq("id",id);
    setMeetings(m=>m.filter(x=>x.id!==id));
  };

  const inp={width:"100%",padding:"7px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13,boxSizing:"border-box"};
  const lbl={fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1};

  const totalActive=new Set(meetings.filter(m=>{
    const d=new Date(m.meeting_date); const now=new Date();
    return (now-d)/(1000*60*60*24*365)<=1;
  }).map(m=>m.committee_id)).size;

  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading…</div>;

  return (
    <div>
      {/* 4-pillar summary bar */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14,display:"flex",gap:16,alignItems:"center",flexWrap:"wrap"}}>
        <div style={{flex:1}}>
          <div style={{fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1}}>COMMITTEE FUNCTIONING</div>
          <div style={{fontSize:14,color:totalActive>=20?T.green:totalActive>0?T.orange:T.red,fontWeight:700}}>
            {totalActive}/26 committees active <span style={{fontSize:11,color:T.muted}}>(met in last 12 months)</span>
          </div>
          <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
            <div style={{height:"100%",borderRadius:2,background:totalActive>=20?T.green:totalActive>0?T.orange:T.red,width:`${Math.min(100,(totalActive/26)*100)}%`,transition:"width 0.5s"}}/>
          </div>
        </div>
        <div style={{display:"flex",gap:8}}>
          <button onClick={()=>setView("reference")} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:view==="reference"?T.goldD:"transparent",border:`1px solid ${view==="reference"?T.gold:T.border}`,color:view==="reference"?T.goldL:T.muted}}>📋 Reference</button>
          <button onClick={()=>setView("mom")} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:view==="mom"?T.goldD:"transparent",border:`1px solid ${view==="mom"?T.gold:T.border}`,color:view==="mom"?T.goldL:T.muted}}>📝 Meeting Records {meetings.length>0&&<span style={{marginLeft:4,background:T.gold,color:T.bg,borderRadius:4,padding:"0 5px",fontSize:8}}>{meetings.length}</span>}</button>
        </div>
      </div>

      {momSuccess&&<div style={{background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,padding:"10px 14px",marginBottom:12,fontSize:13,color:T.green}}>✅ Meeting minutes saved successfully.</div>}

      {/* REFERENCE VIEW */}
      {view==="reference"&&(
        <div>
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
            <div style={{display:"flex",gap:10,alignItems:"center",flexWrap:"wrap"}}>
              <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search committees…" style={{flex:1,minWidth:180,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
              {["ALL","NEW","JCI"].map(f=><button key={f} onClick={()=>setFilter(f)} style={{padding:"5px 12px",borderRadius:8,fontSize:12,cursor:"pointer",background:filter===f?T.goldD:"transparent",border:`1px solid ${filter===f?T.gold:T.border}`,color:filter===f?T.goldL:T.muted}}>{f==="NEW"?"🆕 New 6th":f==="JCI"?"🌐 JCI":"All"}</button>)}
              <div style={{fontSize:13,color:T.muted}}>{filtered.length}/{committees.length}</div>
            </div>
          </div>
          <div style={{display:"grid",gap:8}}>
            {filtered.map(c=>{
              const isOpen=expanded===c.id;
              const docs=Array.isArray(c.required_docs)?c.required_docs:(c.required_docs?JSON.parse(c.required_docs):[]);
              const mCount=meetingCount(c.id); const last=lastMeeting(c.id);
              return (
                <div key={c.id} style={{background:T.panel,border:`1px solid ${c.is_new_in_6th?`${T.gold}30`:T.border}`,borderRadius:10,overflow:"hidden"}}>
                  <div style={{padding:"14px 16px",cursor:"pointer"}} onClick={()=>setExpanded(isOpen?null:c.id)}>
                    <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                      <div style={{flex:1}}>
                        <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:5,flexWrap:"wrap"}}>
                          <span style={{fontSize:15,fontWeight:700,color:T.white}}>{c.name}</span>
                          {c.is_new_in_6th&&<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:`${T.gold}20`,color:T.gold,fontWeight:700}}>NEW 6TH</span>}
                          {c.is_jci&&<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:T.blueD,color:T.blue}}>JCI</span>}
                          {mCount>0?<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:T.greenD,color:T.green}}>✓ {mCount} meeting{mCount>1?"s":""} recorded</span>
                            :<span style={{fontSize:8,padding:"2px 7px",borderRadius:5,background:T.redD,color:T.red}}>No meetings recorded</span>}
                        </div>
                        <div style={{display:"flex",gap:12,flexWrap:"wrap"}}>
                          <span style={{fontSize:12,color:T.muted}}>📋 {c.chapter_ref}</span>
                          <span style={{fontSize:12,color:T.muted}}>🔄 {c.frequency}</span>
                          <span style={{fontSize:12,color:T.muted}}>👤 {c.chair}</span>
                          {last&&<span style={{fontSize:12,color:T.green}}>Last: {last}</span>}
                        </div>
                      </div>
                      <button onClick={e=>{e.stopPropagation();setShowMOMForm(c.id);setMOMForm(emptyMOM());setView("reference");}} style={{padding:"4px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,flexShrink:0}}>+ Add MOM</button>
                      <span style={{fontSize:16,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                    </div>
                  </div>
                  {/* MOM Form inline */}
                  {showMOMForm===c.id&&(
                    <div style={{borderTop:`1px solid ${T.gold}40`,padding:"16px",background:T.panel2}}>
                      <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:12,letterSpacing:1}}>📝 ADD MEETING MINUTES — {c.name}</div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                        {[["Meeting Date *","date","meeting_date"],["Meeting No.","text","meeting_no"],["Venue","text","venue"],["Chairperson *","text","chairperson"]].map(([l,t,k])=>(
                          <div key={k}><div style={lbl}>{l}</div><input type={t} value={momForm[k]} onChange={e=>setMOMForm(f=>({...f,[k]:e.target.value}))} style={inp}/></div>
                        ))}
                        <div><div style={lbl}>Members Present</div><input type="number" value={momForm.members_present} onChange={e=>setMOMForm(f=>({...f,members_present:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Total Members</div><input type="number" value={momForm.members_total} onChange={e=>setMOMForm(f=>({...f,members_total:e.target.value}))} style={inp}/></div>
                      </div>
                      <div style={{display:"flex",gap:16,marginBottom:12}}>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer"}}>
                          <input type="checkbox" checked={momForm.quorum_met} onChange={e=>setMOMForm(f=>({...f,quorum_met:e.target.checked}))}/> Quorum Met
                        </label>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer"}}>
                          <input type="checkbox" checked={momForm.previous_capa_reviewed} onChange={e=>setMOMForm(f=>({...f,previous_capa_reviewed:e.target.checked}))}/> Previous CAPA Reviewed
                        </label>
                      </div>
                      {/* Agenda items */}
                      <div style={{marginBottom:12}}>
                        <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:8}}>
                          <div style={{fontSize:12,fontWeight:700,color:T.gold,letterSpacing:1}}>AGENDA ITEMS</div>
                          <button onClick={addAgendaItem} style={{padding:"3px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold}}>+ Add Item</button>
                        </div>
                        {momForm.agenda_items.map((ag,i)=>(
                          <div key={i} style={{background:T.panel,borderRadius:8,padding:"10px",marginBottom:8,border:`1px solid ${T.border}`}}>
                            <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:6}}>
                              <div style={{fontSize:11,color:T.gold,fontWeight:700}}>ITEM {i+1}</div>
                              {momForm.agenda_items.length>1&&<button onClick={()=>removeAgenda(i)} style={{fontSize:11,color:T.red,background:"transparent",border:"none",cursor:"pointer"}}>✕ Remove</button>}
                            </div>
                            <div style={{display:"grid",gap:6}}>
                              {[["Agenda Item","item"],["Discussion","discussion"],["Decision","decision"]].map(([l,k])=>(
                                <div key={k}><div style={lbl}>{l}</div><input value={ag[k]} onChange={e=>updateAgenda(i,k,e.target.value)} style={inp}/></div>
                              ))}
                              <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8}}>
                                <div><div style={lbl}>Action Owner</div><input value={ag.action_owner} onChange={e=>updateAgenda(i,"action_owner",e.target.value)} style={inp}/></div>
                                <div><div style={lbl}>Target Date</div><input type="date" value={ag.target_date} onChange={e=>updateAgenda(i,"target_date",e.target.value)} style={inp}/></div>
                              </div>
                            </div>
                          </div>
                        ))}
                      </div>
                      {/* Minutes & next meeting */}
                      <div style={{marginBottom:10}}><div style={lbl}>MINUTES / SUMMARY</div><textarea value={momForm.minutes_text} onChange={e=>setMOMForm(f=>({...f,minutes_text:e.target.value}))} rows={3} style={{...inp,resize:"vertical"}}/></div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:12}}>
                        <div><div style={lbl}>Next Meeting Date</div><input type="date" value={momForm.next_meeting_date} onChange={e=>setMOMForm(f=>({...f,next_meeting_date:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Next Meeting Agenda</div><input value={momForm.next_meeting_agenda} onChange={e=>setMOMForm(f=>({...f,next_meeting_agenda:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Minutes Approved By</div><input value={momForm.minutes_approved_by} onChange={e=>setMOMForm(f=>({...f,minutes_approved_by:e.target.value}))} style={inp}/></div>
                        <div><div style={lbl}>Approval Date</div><input type="date" value={momForm.minutes_approved_date} onChange={e=>setMOMForm(f=>({...f,minutes_approved_date:e.target.value}))} style={inp}/></div>
                      </div>
                      <div style={{marginBottom:12}}>
                        <div style={lbl}>EVIDENCE LINK — Meeting Minutes (Google Drive / OneDrive URL)</div>
                        <input style={inp} placeholder="https://drive.google.com/…" value={momForm.evidence_url} onChange={e=>setMOMForm(f=>({...f,evidence_url:e.target.value}))}/>
                      </div>
                      <div style={{display:"flex",gap:8}}>
                        <button onClick={()=>saveMOM(c.id)} disabled={saving} style={{padding:"8px 20px",borderRadius:8,background:T.green,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>{saving?"Saving…":"💾 Save Meeting Minutes"}</button>
                        <button onClick={()=>{setShowMOMForm(null);setMOMForm(emptyMOM());}} style={{padding:"8px 16px",borderRadius:8,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:13,cursor:"pointer"}}>Cancel</button>
                      </div>
                    </div>
                  )}
                  {isOpen&&(
                    <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px",display:"grid",gap:12}}>
                      <div><div style={{fontSize:11,color:T.muted,marginBottom:5,letterSpacing:1}}>SCOPE</div><div style={{fontSize:13,color:T.text,lineHeight:1.6}}>{c.scope}</div></div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
                        <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>COORDINATOR</div><div style={{fontSize:13,color:T.text}}>{c.coordinator}</div></div>
                        <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>MEMBERS</div><div style={{fontSize:13,color:T.text,lineHeight:1.5}}>{c.members}</div></div>
                      </div>
                      {docs.length>0&&<div><div style={{fontSize:11,color:T.muted,marginBottom:7,letterSpacing:1}}>REQUIRED DOCUMENTS</div><div style={{display:"flex",gap:5,flexWrap:"wrap"}}>{docs.map((d,i)=><span key={i} style={{fontSize:12,padding:"3px 10px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}30`,color:T.gold}}>📄 {d}</span>)}</div></div>}
                      {c.linked_oes?.length>0&&<div><div style={{fontSize:11,color:T.muted,marginBottom:5}}>LINKED OEs</div><div style={{display:"flex",gap:4,flexWrap:"wrap"}}>{c.linked_oes.map(oe=><span key={oe} style={{fontSize:11,padding:"2px 7px",borderRadius:5,background:T.blueD,color:T.blue,fontFamily:"monospace"}}>{oe}</span>)}</div></div>}
                      {c.formation_guide&&(()=>{
                        const fg=typeof c.formation_guide==="string"?JSON.parse(c.formation_guide):c.formation_guide;
                        const isGuideOpen=guideOpen===c.id;
                        return (
                          <div style={{borderTop:`1px dashed ${T.border}`,paddingTop:10,marginTop:2}}>
                            <div onClick={()=>setGuideOpen(isGuideOpen?null:c.id)} style={{cursor:"pointer",display:"flex",alignItems:"center",gap:6,fontSize:12,color:T.gold,letterSpacing:1,fontWeight:700}}>
                              <span>{isGuideOpen?"▲":"▼"}</span><span>📖 FORMATION GUIDE — HOW TO CONSTITUTE & RUN</span>
                            </div>
                            {isGuideOpen&&(
                              <div style={{display:"grid",gap:12,marginTop:11,padding:"12px 14px",background:T.panel2,borderRadius:8,border:`1px solid ${T.gold}20`}}>
                                <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
                                  <div><div style={{fontSize:11,color:T.gold,marginBottom:4,letterSpacing:1,fontWeight:700}}>QUORUM</div><div style={{fontSize:13,color:T.text,lineHeight:1.5}}>{fg.quorum}</div></div>
                                  <div><div style={{fontSize:11,color:T.gold,marginBottom:4,letterSpacing:1,fontWeight:700}}>TERM</div><div style={{fontSize:13,color:T.text,lineHeight:1.5}}>{fg.term}</div></div>
                                </div>
                                {Array.isArray(fg.agenda_template)&&fg.agenda_template.length>0&&(
                                  <div>
                                    <div style={{fontSize:11,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>AGENDA TEMPLATE ({fg.agenda_template.length} ITEMS)</div>
                                    <div style={{display:"grid",gap:4}}>
                                      {fg.agenda_template.map((item,i)=>(
                                        <div key={i} style={{display:"flex",gap:8,alignItems:"flex-start",padding:"6px 9px",background:T.panel,borderRadius:5,border:`1px solid ${T.border}`}}>
                                          <span style={{fontSize:11,color:T.gold,fontWeight:700,minWidth:14}}>{i+1}.</span>
                                          <span style={{fontSize:12,color:T.text,lineHeight:1.5}}>{item}</span>
                                        </div>
                                      ))}
                                    </div>
                                  </div>
                                )}
                                {Array.isArray(fg.induction_first_90_days)&&fg.induction_first_90_days.length>0&&(
                                  <div>
                                    <div style={{fontSize:11,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>FIRST 90 DAYS — INDUCTION ROADMAP</div>
                                    <div style={{display:"grid",gap:5}}>
                                      {fg.induction_first_90_days.map((step,i)=>(
                                        <div key={i} style={{padding:"7px 10px",background:T.panel,borderRadius:5,borderLeft:`3px solid ${T.gold}`,fontSize:12,color:T.text,lineHeight:1.55}}>{step}</div>
                                      ))}
                                    </div>
                                  </div>
                                )}
                                {fg.escalation_path&&(
                                  <div style={{padding:"10px 12px",background:T.redD,borderRadius:6,border:`1px solid ${T.red}30`}}>
                                    <div style={{fontSize:11,color:T.red,marginBottom:5,letterSpacing:1,fontWeight:700}}>⚠️ ESCALATION PATH</div>
                                    <div style={{fontSize:12,color:T.text,lineHeight:1.55}}>{fg.escalation_path}</div>
                                  </div>
                                )}
                              </div>
                            )}
                          </div>
                        );
                      })()}
                      {/* Past meetings for this committee */}
                      {meetings.filter(m=>m.committee_id===c.id).length>0&&(
                        <div style={{borderTop:`1px dashed ${T.border}`,paddingTop:10}}>
                          <div style={{fontSize:11,color:T.muted,marginBottom:8,letterSpacing:1}}>MEETING HISTORY ({meetings.filter(m=>m.committee_id===c.id).length})</div>
                          {meetings.filter(m=>m.committee_id===c.id).map(m=>(
                            <div key={m.id} style={{background:T.panel2,borderRadius:8,padding:"10px 12px",marginBottom:6,border:`1px solid ${T.green}20`}}>
                              <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start"}}>
                                <div>
                                  <div style={{fontSize:13,fontWeight:700,color:T.white}}>{m.meeting_date} {m.meeting_no&&<span style={{color:T.muted,fontSize:11}}>— {m.meeting_no}</span>}</div>
                                  <div style={{fontSize:12,color:T.muted,marginTop:2}}>Chair: {m.chairperson} | {m.members_present}/{m.members_total} members | Quorum: {m.quorum_met?"✅":"❌"}</div>
                                  {m.agenda_items?.length>0&&<div style={{fontSize:11,color:T.muted,marginTop:3}}>{m.agenda_items.length} agenda items · {m.previous_capa_reviewed?"CAPA reviewed":"CAPA not reviewed"}</div>}
                                </div>
                                <div style={{display:"flex",gap:6,alignItems:"center"}}>
                                  {m.evidence_url&&<a href={m.evidence_url} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Minutes</a>}
                                  <button onClick={()=>deleteMeeting(m.id)} style={{fontSize:11,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                                </div>
                              </div>
                            </div>
                          ))}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* MOM RECORDS VIEW */}
      {view==="mom"&&(
        <div>
          {meetings.length===0?(
            <div style={{textAlign:"center",padding:40,color:T.muted}}>
              <div style={{fontSize:32,marginBottom:12}}>📝</div>
              <div style={{fontSize:15,marginBottom:6}}>No meeting minutes recorded yet.</div>
              <div style={{fontSize:13}}>Switch to Reference view and click "+ Add MOM" on any committee.</div>
            </div>
          ):(
            <div style={{display:"grid",gap:8}}>
              {meetings.map(m=>{
                const comm=committees.find(c=>c.id===m.committee_id);
                return (
                  <div key={m.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"14px 16px"}}>
                    <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start",marginBottom:8}}>
                      <div>
                        <div style={{fontSize:14,fontWeight:700,color:T.white}}>{comm?.name||m.committee_id}</div>
                        <div style={{fontSize:12,color:T.muted,marginTop:2}}>{m.meeting_date} {m.meeting_no&&`— ${m.meeting_no}`} | {m.venue||"Venue not specified"}</div>
                      </div>
                      <div style={{display:"flex",gap:6,alignItems:"center"}}>
                        <span style={{fontSize:11,padding:"2px 8px",borderRadius:4,background:m.quorum_met?T.greenD:T.redD,color:m.quorum_met?T.green:T.red}}>Quorum {m.quorum_met?"Met":"Not Met"}</span>
                        {m.evidence_url&&<a href={m.evidence_url} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Minutes</a>}
                        <button onClick={()=>deleteMeeting(m.id)} style={{fontSize:11,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                      </div>
                    </div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr 1fr",gap:8,marginBottom:8}}>
                      <div style={{background:T.panel2,borderRadius:6,padding:"7px 10px"}}><div style={{fontSize:8,color:T.muted}}>CHAIRPERSON</div><div style={{fontSize:12,color:T.text}}>{m.chairperson}</div></div>
                      <div style={{background:T.panel2,borderRadius:6,padding:"7px 10px"}}><div style={{fontSize:8,color:T.muted}}>ATTENDANCE</div><div style={{fontSize:12,color:T.text}}>{m.members_present||"—"}/{m.members_total||"—"} members</div></div>
                      <div style={{background:T.panel2,borderRadius:6,padding:"7px 10px"}}><div style={{fontSize:8,color:T.muted}}>NEXT MEETING</div><div style={{fontSize:12,color:T.text}}>{m.next_meeting_date||"Not set"}</div></div>
                    </div>
                    {m.agenda_items?.length>0&&(
                      <div>
                        <div style={{fontSize:11,color:T.muted,marginBottom:5,letterSpacing:1}}>AGENDA & DECISIONS ({m.agenda_items.length} items)</div>
                        {m.agenda_items.map((ag,i)=>(
                          <div key={i} style={{background:T.panel2,borderRadius:6,padding:"7px 10px",marginBottom:4,borderLeft:`2px solid ${T.gold}`}}>
                            <div style={{fontSize:12,fontWeight:700,color:T.text}}>{i+1}. {ag.item}</div>
                            {ag.decision&&<div style={{fontSize:11,color:T.green,marginTop:2}}>Decision: {ag.decision}</div>}
                            {ag.action_owner&&<div style={{fontSize:11,color:T.blue,marginTop:1}}>Action: {ag.action_owner} by {ag.target_date||"—"}</div>}
                          </div>
                        ))}
                      </div>
                    )}
                    {m.minutes_approved_by&&<div style={{fontSize:11,color:T.muted,marginTop:6}}>Minutes approved by: {m.minutes_approved_by} on {m.minutes_approved_date||"—"}</div>}
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

// ── KPIs — with monthly data entry ───────────────────────────
function KPIsScreen({ hospitalId, user }) {
  const [kpis,setKpis]=useState([]);
  const [kpiData,setKpiData]=useState([]); // existing monthly data
  const [loading,setLoading]=useState(true);
  const [tab,setTab]=useState("hospital");
  const [search,setSearch]=useState("");
  const [expanded,setExpanded]=useState(null);
  const [dataForm,setDataForm]=useState({}); // {kpiId: {month,year,value,trend,capa_required,capa_notes}}
  const [saving,setSaving]=useState(null);
  const [saveSuccess,setSaveSuccess]=useState(null);
  const [calcResult,setCalcResult]=useState({});
  const [customTargets,setCustomTargets]=useState({});
  const [editingTarget,setEditingTarget]=useState(null);
  const [customTargetInput,setCustomTargetInput]=useState('');

  const now=new Date(); const curMonth=now.getMonth()+1; const curYear=now.getFullYear();
  const MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

  useEffect(()=>{
    supabase.from("kpis").select("*, source, source_doc").order("kpi_no").then(({data})=>setKpis(data||[]));
    if(hospitalId){
      const loadData=async()=>{
        const[{data:kdData},{data:ctData}]=await Promise.all([
          supabase.from("kpi_data").select("*").eq("hospital_id",hospitalId).order("year",{ascending:false}).order("month",{ascending:false}),
          user?.id?supabase.from("kpi_custom_targets").select("*").eq("user_id",user.id).eq("hospital_id",hospitalId):Promise.resolve({data:null})
        ]);
        setKpiData(kdData||[]);
        if(ctData){const ctMap={};ctData.forEach(ct=>{ctMap[ct.kpi_id]=ct.custom_target;});setCustomTargets(ctMap);}
        setLoading(false);
      };
      loadData();
    } else { setLoading(false); }
  },[hospitalId,user]);

  const filtered=kpis.filter(k=>k.category===tab&&(!search||k.name.toLowerCase().includes(search.toLowerCase())||(k.dept||"").toLowerCase().includes(search.toLowerCase())));
  const depts=[...new Set(kpis.filter(k=>k.category==="dept_specific").map(k=>k.dept))].sort();

  const getKpiHistory=(kpiId)=>kpiData.filter(d=>String(d.kpi_id)===String(kpiId)).sort((a,b)=>b.year-a.year||b.month-a.month);
  const getLatest=(kpiId)=>getKpiHistory(kpiId)[0];
  const monthsTracked=(kpiId)=>new Set(kpiData.filter(d=>String(d.kpi_id)===String(kpiId)).map(d=>`${d.year}-${d.month}`)).size;

  const trackingStatus=(kpiId)=>{
    const n=monthsTracked(kpiId);
    if(n===0) return {label:"Not started",color:T.red};
    if(n<3) return {label:`${n} month${n>1?"s":""}`,color:T.orange};
    return {label:`${n} months`,color:T.green};
  };

  const initForm=(kpi)=>{
    if(!dataForm[kpi.id]){
      setDataForm(f=>({...f,[kpi.id]:{month:curMonth,year:curYear,value:"",trend:"stable",capa_required:false,capa_notes:"",evidence_url:"",calc_num:"",calc_den:""}}));
    }
  };

  const saveCustomTarget=async(kpi)=>{
    await supabase.from("kpi_custom_targets").upsert({
      user_id:user.id,hospital_id:hospitalId,kpi_id:kpi.id,
      custom_target:customTargetInput,updated_at:new Date().toISOString()
    },{onConflict:"user_id,hospital_id,kpi_id"});
    setCustomTargets(prev=>({...prev,[kpi.id]:customTargetInput}));
    setEditingTarget(null);
    setCustomTargetInput('');
  };

  const isWithinTarget=(value,kpi)=>{
    const bv=parseFloat(kpi.benchmark_value);
    if(isNaN(bv))return true;
    const target=kpi.target||"";
    if(target.startsWith("≥")||target.startsWith(">=")||target.startsWith(">"))return value>=bv;
    if(target.startsWith("≤")||target.startsWith("<=")||target.startsWith("<"))return value<=bv;
    return Math.abs(value-bv)<0.001;
  };

  const getResultColor=(result,target)=>{
    if(!target)return '#c9a84c';
    const t=target.trim();
    if(t.includes('Decreasing')||t.includes('benchmark')||t.includes(';')||t.includes('1:')||t.includes('varies')||t.includes('trend'))return '#c9a84c';
    const ltMatch=t.match(/^<\s*([\d.]+)/);
    if(ltMatch)return result<parseFloat(ltMatch[1])?'#4caf7d':'#e05a5a';
    const gtMatch=t.match(/^>\s*([\d.]+)/);
    if(gtMatch)return result>parseFloat(gtMatch[1])?'#4caf7d':'#e05a5a';
    return '#c9a84c';
  };

  const getResultLabel=(result,target)=>{
    const color=getResultColor(result,target);
    if(color==='#4caf7d')return '✅ Within target';
    if(color==='#e05a5a')return '❌ Outside target';
    return '📊 Compare with baseline';
  };

  const calcAndSave=async(kpi)=>{
    const f=dataForm[kpi.id];
    if(!f||f.calc_num===""||f.calc_den===""){alert("Enter numerator and denominator.");return;}
    const num=parseFloat(f.calc_num);
    const den=parseFloat(f.calc_den);
    if(isNaN(num)||isNaN(den)||den===0){alert("Enter valid non-zero denominator.");return;}
    const isPercent=(kpi.unit||"").toLowerCase().includes("%");
    const result=isPercent?(num/den)*100:num/den;
    setCalcResult(r=>({...r,[kpi.id]:result}));
    setSaving(kpi.id);
    const{error}=await supabase.from("kpi_data").upsert({
      hospital_id:hospitalId,kpi_id:kpi.id,
      numerator:num,denominator:den,
      value:parseFloat(result.toFixed(4)),
      benchmark:kpi.benchmark_value||null,
      month:curMonth,year:curYear,
      trend:"stable",capa_required:false
    },{onConflict:"hospital_id,kpi_id,month,year"});
    if(!error){
      const{data}=await supabase.from("kpi_data").select("*").eq("hospital_id",hospitalId).order("year",{ascending:false}).order("month",{ascending:false});
      setKpiData(data||[]);
      setSaveSuccess(kpi.id);
      setTimeout(()=>setSaveSuccess(null),2000);
    } else { alert("Error: "+error.message); }
    setSaving(null);
  };

  const saveKpiData=async(kpi)=>{
    const f=dataForm[kpi.id];
    if(!f||f.value===""){alert("Enter a value to save.");return;}
    setSaving(kpi.id);
    // check if entry for this month/year exists
    const existing=kpiData.find(d=>String(d.kpi_id)===String(kpi.id)&&d.month===parseInt(f.month)&&d.year===parseInt(f.year));
    let error;
    if(existing){
      ({error}=await supabase.from("kpi_data").update({
        value:parseFloat(f.value),trend:f.trend,capa_required:f.capa_required,capa_notes:f.capa_notes||null,evidence_url:f.evidence_url||null,
        numerator:f.calc_num!==""?parseFloat(f.calc_num):null,denominator:f.calc_den!==""?parseFloat(f.calc_den):null
      }).eq("id",existing.id));
    } else {
      ({error}=await supabase.from("kpi_data").insert({
        hospital_id:hospitalId,kpi_id:kpi.id,
        month:parseInt(f.month),year:parseInt(f.year),
        value:parseFloat(f.value),benchmark:kpi.benchmark_value||null,
        trend:f.trend,capa_required:f.capa_required,capa_notes:f.capa_notes||null,evidence_url:f.evidence_url||null,
        numerator:f.calc_num!==""?parseFloat(f.calc_num):null,denominator:f.calc_den!==""?parseFloat(f.calc_den):null
      }));
    }
    if(!error){
      const{data}=await supabase.from("kpi_data").select("*").eq("hospital_id",hospitalId).order("year",{ascending:false}).order("month",{ascending:false});
      setKpiData(data||[]);
      setSaveSuccess(kpi.id);
      setTimeout(()=>setSaveSuccess(null),2000);
    } else { alert("Error: "+error.message); }
    setSaving(null);
  };

  const deleteKpiEntry=async(entryId)=>{
    if(!window.confirm("Delete this entry?"))return;
    const{error}=await supabase.from("kpi_data").delete().eq("id",entryId);
    if(!error){setKpiData(p=>p.filter(d=>d.id!==entryId));}
    else{alert("Error: "+error.message);}
  };

  // Overall KPI tracking summary
  const tracked=kpis.filter(k=>monthsTracked(k.id)>=3).length;
  const total=kpis.length;

  const inp={padding:"6px 9px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13};

  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading KPIs…</div>;

  return (
    <div>
      {/* Summary bar */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
        <div style={{display:"flex",gap:16,alignItems:"center",flexWrap:"wrap"}}>
          <div style={{flex:1}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1}}>KPI TRACKING STATUS</div>
            <div style={{fontSize:14,color:tracked>=total*0.8?T.green:tracked>0?T.orange:T.red,fontWeight:700}}>
              {tracked}/{total} KPIs with ≥3 months data
              <span style={{fontSize:11,color:T.muted,marginLeft:6}}>(minimum required for NABH assessment)</span>
            </div>
            <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
              <div style={{height:"100%",borderRadius:2,background:tracked>=total*0.8?T.green:tracked>0?T.orange:T.red,width:`${Math.min(100,(tracked/total)*100)}%`,transition:"width 0.5s"}}/>
            </div>
          </div>
          <div style={{textAlign:"right"}}>
            <div style={{fontSize:20,fontWeight:700,color:T.gold}}>{Math.round((tracked/total)*100)}%</div>
            <div style={{fontSize:11,color:T.muted}}>KPI readiness</div>
          </div>
        </div>
      </div>

      {/* Tabs & Search */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
        <div style={{display:"flex",gap:8,marginBottom:10}}>
          {[["hospital","🏥 Hospital-wide (32)"],["dept_specific","🏬 Dept-specific (18)"]].map(([k,l])=>(
            <button key={k} onClick={()=>{setTab(k);setSearch("");}} style={{padding:"6px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:tab===k?T.goldD:"transparent",border:`1px solid ${tab===k?T.gold:T.border}`,color:tab===k?T.goldL:T.muted}}>{l}</button>
          ))}
        </div>
        <input value={search} onChange={e=>setSearch(e.target.value)} placeholder="Search KPIs…" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:"border-box"}}/>
      </div>
      {tab==="dept_specific"&&!search&&<div style={{display:"flex",gap:5,flexWrap:"wrap",marginBottom:10}}>{depts.map(d=><button key={d} onClick={()=>setSearch(d)} style={{padding:"3px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.blueD,border:`1px solid ${T.blue}30`,color:T.blue}}>{d}</button>)}</div>}

      <div style={{display:"grid",gap:8}}>
        {filtered.map(k=>{
          const isOpen=expanded===k.id;
          const history=getKpiHistory(k.id);
          const latest=getLatest(k.id);
          const status=trackingStatus(k.id);
          const f=dataForm[k.id]||{month:curMonth,year:curYear,value:"",trend:"stable",capa_required:false,capa_notes:"",evidence_url:"",calc_num:"",calc_den:""};

          return (
            <div key={k.id} style={{background:T.panel,border:`1px solid ${k.is_mandatory?`${T.gold}25`:T.border}`,borderRadius:10,overflow:"hidden"}}>
              <div style={{padding:"12px 16px",cursor:"pointer"}} onClick={()=>{setExpanded(isOpen?null:k.id);if(!isOpen)initForm(k);}}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                  <div style={{width:28,height:28,borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}30`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:12,fontWeight:800,color:T.gold,flexShrink:0}}>{k.kpi_no}</div>
                  <div style={{flex:1}}>
                    <div style={{display:"flex",gap:7,alignItems:"center",marginBottom:3,flexWrap:"wrap"}}>
                      <span style={{fontSize:14,fontWeight:700,color:T.white}}>{k.name}</span>
                      {k.is_mandatory&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${T.red}20`,color:T.red}}>MANDATORY</span>}
                      {k.dept&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.blueD,color:T.blue}}>{k.dept}</span>}
                      <span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${status.color}20`,color:status.color}}>📊 {status.label}</span>
                    </div>
                    <div style={{display:"flex",gap:10,flexWrap:"wrap"}}>
                      <span style={{fontSize:12,color:T.muted}}>📋 {k.standard_ref}</span>
                      <span style={{fontSize:12,color:T.green,fontWeight:600}}>🎯 {k.target}</span>
                      {customTargets[k.id]?(
                        <span style={{fontSize:12,color:'#4caf7d',marginLeft:6}}>
                          🎯 Custom: {customTargets[k.id]}
                          <span onClick={e=>{e.stopPropagation();setEditingTarget(k.id);setCustomTargetInput(customTargets[k.id]);}} style={{cursor:'pointer',marginLeft:4,color:'#c9a84c'}}>✏️</span>
                        </span>
                      ):(
                        <span onClick={e=>{e.stopPropagation();setEditingTarget(k.id);setCustomTargetInput('');}} style={{fontSize:12,color:'#3a5870',cursor:'pointer',marginLeft:6}}>+ Set custom target</span>
                      )}
                      <span style={{fontSize:12,color:T.muted}}>📅 {k.frequency}</span>
                      {latest&&<span style={{fontSize:12,color:T.blue}}>Latest: {latest.value} ({MONTHS[latest.month-1]} {latest.year})</span>}
                    </div>
                    {editingTarget===k.id&&(
                      <div style={{display:'flex',gap:6,marginTop:6,alignItems:'center'}} onClick={e=>e.stopPropagation()}>
                        <input value={customTargetInput} onChange={e=>setCustomTargetInput(e.target.value)} placeholder="e.g. <3% or >85%" style={{flex:1,padding:'4px 8px',borderRadius:6,border:'1px solid #0f2640',background:'#081525',color:'#eef4f9',fontSize:13}}/>
                        <button onClick={()=>saveCustomTarget(k)} style={{padding:'4px 10px',borderRadius:6,background:'#c9a84c',border:'none',color:'#050e1a',fontSize:13,fontWeight:700,cursor:'pointer'}}>Save</button>
                        <button onClick={()=>setEditingTarget(null)} style={{padding:'4px 8px',borderRadius:6,background:'transparent',border:'1px solid #3a5870',color:'#3a5870',fontSize:13,cursor:'pointer'}}>Cancel</button>
                      </div>
                    )}
                  </div>
                  <span style={{fontSize:16,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                </div>
              </div>

              {(k.source||k.source_doc)&&<div style={{fontSize:12,color:'#3a5870',marginTop:6,fontStyle:'italic',padding:"0 16px 10px"}}>📚 Source: {k.source} — {k.source_doc}</div>}

              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px",display:"grid",gap:12}}>
                  {/* KPI definition */}
                  <div style={{fontSize:13,color:T.text,lineHeight:1.6}}>{k.definition}</div>
                  <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
                    <div style={{background:T.panel2,borderRadius:8,padding:"10px 12px"}}><div style={{fontSize:11,color:T.muted,marginBottom:4}}>NUMERATOR</div><div style={{fontSize:13,color:T.text}}>{k.numerator}</div></div>
                    <div style={{background:T.panel2,borderRadius:8,padding:"10px 12px"}}><div style={{fontSize:11,color:T.muted,marginBottom:4}}>DENOMINATOR</div><div style={{fontSize:13,color:T.text}}>{k.denominator}</div></div>
                  </div>
                  <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                    <div style={{background:T.goldD,border:`1px solid ${T.gold}30`,borderRadius:8,padding:"8px 12px",flex:1}}><div style={{fontSize:11,color:T.muted,marginBottom:3}}>FORMULA</div><div style={{fontSize:13,color:T.gold,fontWeight:700}}>{k.formula} → {k.unit}</div></div>
                    <div style={{background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,padding:"8px 12px",flex:1}}><div style={{fontSize:11,color:T.muted,marginBottom:3}}>TARGET</div><div style={{fontSize:13,color:T.green,fontWeight:700}}>{k.target}</div></div>
                  </div>
                  {k.remarks&&<div style={{fontSize:12,color:T.muted,fontStyle:"italic",lineHeight:1.5}}>💡 {k.remarks}</div>}

                  {/* CALCULATOR */}
                  <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                    <div style={{fontSize:12,fontWeight:700,color:T.blue,marginBottom:10,letterSpacing:1}}>🧮 CALCULATOR</div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>NUMERATOR — {k.numerator}</div>
                        <input type="number" step="0.01" value={f.calc_num||""} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,calc_num:e.target.value}}))} placeholder="Enter value" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>DENOMINATOR — {k.denominator}</div>
                        <input type="number" step="0.01" value={f.calc_den||""} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,calc_den:e.target.value}}))} placeholder="Enter value" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                      </div>
                    </div>
                    <button onClick={()=>calcAndSave(k)} disabled={saving===k.id} style={{padding:"7px 18px",borderRadius:7,background:T.blueD,border:`1px solid ${T.blue}`,color:T.blue,fontSize:13,fontWeight:700,cursor:"pointer"}}>
                      {saving===k.id?"Saving…":"🧮 Calculate & Save"}
                    </button>
                    {calcResult[k.id]!==undefined&&(()=>{const effectiveTarget=customTargets[k.id]||k.target;return(
                      <div style={{marginTop:8}}>
                        <div style={{fontSize:15,fontWeight:700,color:getResultColor(calcResult[k.id],effectiveTarget)}}>
                          Result: {calcResult[k.id].toFixed(2)} {k.unit}
                        </div>
                        <div style={{fontSize:12,color:getResultColor(calcResult[k.id],effectiveTarget),marginTop:2}}>
                          {getResultLabel(calcResult[k.id],effectiveTarget)}
                        </div>
                      </div>
                    );})()}
                  </div>

                  {/* DATA ENTRY */}
                  <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                    <div style={{fontSize:12,fontWeight:700,color:T.gold,marginBottom:10,letterSpacing:1}}>📥 ENTER MONTHLY DATA</div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr 1fr",gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>MONTH</div>
                        <select value={f.month} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,month:parseInt(e.target.value)}}))} style={{...inp,width:"100%"}}>
                          {MONTHS.map((m,i)=><option key={i} value={i+1}>{m}</option>)}
                        </select>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>YEAR</div>
                        <select value={f.year} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,year:parseInt(e.target.value)}}))} style={{...inp,width:"100%"}}>
                          {[curYear-1,curYear,curYear+1].map(y=><option key={y} value={y}>{y}</option>)}
                        </select>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>VALUE ({k.unit})</div>
                        <input type="number" step="0.01" value={f.value} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,value:e.target.value}}))} placeholder="Enter value" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                      </div>
                    </div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>TREND</div>
                        <select value={f.trend} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,trend:e.target.value}}))} style={{...inp,width:"100%"}}>
                          <option value="improving">📈 Improving</option>
                          <option value="stable">➡️ Stable</option>
                          <option value="worsening">📉 Worsening</option>
                        </select>
                      </div>
                      <div style={{display:"flex",alignItems:"flex-end"}}>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer",paddingBottom:2}}>
                          <input type="checkbox" checked={f.capa_required} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,capa_required:e.target.checked}}))}/> CAPA Required
                        </label>
                      </div>
                    </div>
                    {f.capa_required&&(
                      <div style={{marginBottom:8}}>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>CAPA NOTES</div>
                        <textarea value={f.capa_notes} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,capa_notes:e.target.value}}))} rows={2} placeholder="Describe corrective action planned…" style={{...inp,width:"100%",resize:"vertical",boxSizing:"border-box"}}/>
                      </div>
                    )}
                    <div style={{marginBottom:8}}>
                      <div style={{fontSize:8,color:T.muted,marginBottom:3}}>EVIDENCE LINK — Data Sheet (Google Drive / OneDrive URL)</div>
                      <input value={f.evidence_url||""} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,evidence_url:e.target.value}}))} placeholder="https://drive.google.com/…" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                    </div>
                    <button onClick={()=>saveKpiData(k)} disabled={saving===k.id} style={{padding:"7px 18px",borderRadius:7,background:saveSuccess===k.id?T.green:T.goldD,border:`1px solid ${saveSuccess===k.id?T.green:T.gold}`,color:saveSuccess===k.id?T.bg:T.gold,fontSize:13,fontWeight:700,cursor:"pointer"}}>
                      {saving===k.id?"Saving…":saveSuccess===k.id?"✅ Saved!":"💾 Save Entry"}
                    </button>
                  </div>

                  {/* History */}
                  {history.length>0&&(
                    <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                      <KpiTrendChart history={history} target={k.benchmark_value||k.target} unit={k.unit}/>
                      <div style={{fontSize:11,color:T.muted,marginBottom:8,letterSpacing:1,marginTop:12}}>TRACKING HISTORY ({history.length} entries)</div>
                      <div style={{display:"grid",gap:4}}>
                        {history.slice(0,6).map(d=>(
                          <div key={d.id} style={{display:"flex",gap:10,alignItems:"center",padding:"6px 10px",background:T.panel2,borderRadius:6,border:`1px solid ${d.capa_required?`${T.orange}30`:T.border}`}}>
                            <span style={{fontSize:12,color:T.muted,minWidth:60}}>{MONTHS[d.month-1]} {d.year}</span>
                            <span style={{fontSize:14,fontWeight:700,color:T.white}}>{d.value} {k.unit}</span>
                            <span style={{fontSize:11,color:d.trend==="improving"?T.green:d.trend==="worsening"?T.red:T.muted}}>{d.trend==="improving"?"📈":d.trend==="worsening"?"📉":"➡️"} {d.trend}</span>
                            {d.capa_required&&<span style={{fontSize:11,color:T.orange}}>⚠️ CAPA</span>}
                            <button onClick={()=>deleteKpiEntry(d.id,k.id)} style={{marginLeft:"auto",padding:"2px 8px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:11,cursor:"pointer"}}>Delete</button>
                          </div>
                        ))}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
        {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:30,fontSize:14}}>No KPIs match.</div>}
      </div>
    </div>
  );
}

// ── AUDITS — 3 tabs: NABH Audits | My Audits | What is Audit ─────────────────────────────────────
function AuditsScreen({ hospitalId }) {
  const [mainTab,setMainTab]=useState("nabh"); // nabh | mine | learn

  // ── NABH AUDITS state ──
  const [audits,setAudits]=useState([]);
  const [auditRecords,setAuditRecords]=useState([]);
  const [loading,setLoading]=useState(true);
  const [filter,setFilter]=useState("ALL");
  const [catFilter,setCatFilter]=useState("ALL");
  const [expanded,setExpanded]=useState(null);
  const [checked,setChecked]=useState({});
  const [guideOpen,setGuideOpen]=useState(null);
  const [showRecordForm,setShowRecordForm]=useState(null);
  const [saving,setSaving]=useState(false);
  const [recordSuccess,setRecordSuccess]=useState(null);

  // ── MY AUDITS state ──
  const [customAudits,setCustomAudits]=useState([]);
  const [customRecords,setCustomRecords]=useState([]);
  const [showCreateForm,setShowCreateForm]=useState(false);
  const [createForm,setCreateForm]=useState({name:"",audit_category:"clinical",is_core:false,parameters:[]});
  const [newParam,setNewParam]=useState("");
  const [savingCreate,setSavingCreate]=useState(false);
  const [customExpanded,setCustomExpanded]=useState(null);
  const [showCustomRecord,setShowCustomRecord]=useState(null);
  const [customRecordForm,setCustomRecordForm]=useState({});
  const [savingCustomRecord,setSavingCustomRecord]=useState(false);
  const [customRecordSuccess,setCustomRecordSuccess]=useState(null);
  const [deleteConfirm,setDeleteConfirm]=useState(null);

  const emptyRecord=()=>({audit_date:"",auditor_name:"",department:"",sample_size:"",compliant_count:"",findings:"",capa_raised:false,capa_notes:"",capa_target_date:"",reaudit_date:"",status:"completed",evidence_url:""});
  const [recordForm,setRecordForm]=useState(emptyRecord());

  const loadData=async()=>{
    supabase.from("audit_checklists").select("*").order("audit_code").then(({data})=>setAudits(data||[]));
    if(hospitalId){
      const[{data:ar},{data:ca},{data:cr}]=await Promise.all([
        supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).is("custom_audit_id",null).order("audit_date",{ascending:false}),
        supabase.from("custom_audits").select("*").eq("hospital_id",hospitalId).order("created_at",{ascending:false}),
        supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).not("custom_audit_id","is",null).order("audit_date",{ascending:false}),
      ]);
      setAuditRecords(ar||[]);
      setCustomAudits(ca||[]);
      setCustomRecords(cr||[]);
    }
    setLoading(false);
  };

  useEffect(()=>{loadData();},[hospitalId]); // eslint-disable-line

  const filtered=audits.filter(a=>{
    const coreMatch=filter==="ALL"||(filter==="CORE"&&a.is_core)||(filter==="NON_CORE"&&!a.is_core);
    const catMatch=catFilter==="ALL"||(a.audit_category||"clinical")===catFilter;
    return coreMatch&&catMatch;
  });
  const getRecords=(auditId)=>auditRecords.filter(r=>String(r.audit_id)===String(auditId));
  const getCustomRecords=(customAuditId)=>customRecords.filter(r=>String(r.custom_audit_id)===String(customAuditId));
  const totalAudits=audits.length;
  const completedAudits=new Set(auditRecords.filter(r=>r.status==="completed"&&new Date(r.audit_date)>new Date(Date.now()-365*24*60*60*1000)).map(r=>r.audit_id)).size;

  const saveRecord=async(auditId)=>{
    if(!recordForm.audit_date){alert("Audit date is required.");return;}
    setSaving(true);
    const {error}=await supabase.from("audit_records").insert({
      hospital_id:hospitalId,audit_id:auditId,
      audit_date:recordForm.audit_date,
      auditor_name:recordForm.auditor_name||null,
      department:recordForm.department||null,
      sample_size:recordForm.sample_size?parseInt(recordForm.sample_size):null,
      compliant_count:recordForm.compliant_count?parseInt(recordForm.compliant_count):null,
      findings:recordForm.findings||null,
      capa_raised:recordForm.capa_raised,
      capa_notes:recordForm.capa_notes||null,
      capa_target_date:recordForm.capa_target_date||null,
      reaudit_date:recordForm.reaudit_date||null,
      status:recordForm.status,
      evidence_url:recordForm.evidence_url||null,
    });
    if(!error){
      const{data}=await supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).is("custom_audit_id",null).order("audit_date",{ascending:false});
      setAuditRecords(data||[]);
      setShowRecordForm(null);
      setRecordForm(emptyRecord());
      setRecordSuccess(auditId);
      setTimeout(()=>setRecordSuccess(null),3000);
    } else { alert("Error: "+error.message); }
    setSaving(false);
  };

  const deleteRecord=async(id)=>{
    if(!window.confirm("Delete this audit record?"))return;
    await supabase.from("audit_records").delete().eq("id",id);
    setAuditRecords(r=>r.filter(x=>x.id!==id));
  };

  // ── CUSTOM AUDIT functions ──
  const createCustomAudit=async()=>{
    if(!createForm.name.trim()){alert("Audit name is required.");return;}
    setSavingCreate(true);
    const{data,error}=await supabase.from("custom_audits").insert({
      hospital_id:hospitalId,
      name:createForm.name.trim(),
      audit_category:createForm.audit_category,
      is_core:createForm.is_core,
      parameters:createForm.parameters,
    }).select().single();
    if(!error){
      setCustomAudits(p=>[data,...p]);
      setCreateForm({name:"",audit_category:"clinical",is_core:false,parameters:[]});
      setShowCreateForm(false);
    } else { alert("Error: "+error.message); }
    setSavingCreate(false);
  };

  const deleteCustomAudit=async(id)=>{
    await supabase.from("audit_records").delete().eq("custom_audit_id",id);
    await supabase.from("custom_audits").delete().eq("id",id);
    setCustomAudits(p=>p.filter(a=>a.id!==id));
    setCustomRecords(p=>p.filter(r=>r.custom_audit_id!==id));
    setDeleteConfirm(null);
  };

  const saveCustomRecord=async(audit)=>{
    if(!customRecordForm.audit_date){alert("Audit date is required.");return;}
    setSavingCustomRecord(true);
    const params=Array.isArray(audit.parameters)?audit.parameters:JSON.parse(audit.parameters||"[]");
    const checkedParams=params.filter((_,i)=>customRecordForm[`param_${i}`]);
    const compliantCount=checkedParams.length;
    const sampleSize=params.length||parseInt(customRecordForm.sample_size)||0;
    const{error}=await supabase.from("audit_records").insert({
      hospital_id:hospitalId,
      custom_audit_id:audit.id,
      audit_date:customRecordForm.audit_date,
      auditor_name:customRecordForm.auditor_name||null,
      department:customRecordForm.department||null,
      sample_size:sampleSize||null,
      compliant_count:params.length>0?compliantCount:(customRecordForm.compliant_count?parseInt(customRecordForm.compliant_count):null),
      findings:customRecordForm.findings||null,
      capa_raised:customRecordForm.capa_raised||false,
      capa_notes:customRecordForm.capa_notes||null,
      capa_target_date:customRecordForm.capa_target_date||null,
      reaudit_date:customRecordForm.reaudit_date||null,
      status:customRecordForm.status||"completed",
      evidence_url:customRecordForm.evidence_url||null,
    });
    if(!error){
      const{data}=await supabase.from("audit_records").select("*").eq("hospital_id",hospitalId).not("custom_audit_id","is",null).order("audit_date",{ascending:false});
      setCustomRecords(data||[]);
      setShowCustomRecord(null);
      setCustomRecordForm({});
      setCustomRecordSuccess(audit.id);
      setTimeout(()=>setCustomRecordSuccess(null),3000);
    } else { alert("Error: "+error.message); }
    setSavingCustomRecord(false);
  };

  const deleteCustomRecord=async(id)=>{
    if(!window.confirm("Delete this record?"))return;
    await supabase.from("audit_records").delete().eq("id",id);
    setCustomRecords(r=>r.filter(x=>x.id!==id));
  };

  const AUDIT_CATEGORIES=[
    {value:"clinical",label:"🏥 Clinical Audit"},
    {value:"nursing",label:"💉 Nursing Audit"},
    {value:"qip",label:"🎯 Quality Improvement Project"},
    {value:"financial",label:"💰 Financial Audit"},
    {value:"structural",label:"🏗️ Structural Audit"},
    {value:"process",label:"⚙️ Process Audit"},
    {value:"outcome",label:"📊 Outcome Audit"},
    {value:"pharmacy",label:"💊 Pharmacy Audit"},
    {value:"dietary",label:"🍽️ Dietary Audit"},
    {value:"other",label:"📋 Other"},
  ];

  const inp={padding:"6px 9px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13};
  const lbl={fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1};

  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading audits…</div>;

  // ── WHAT IS AUDIT tab ──
  const LearnTab=()=>(
    <div style={{display:"grid",gap:12}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:8}}>WHAT IS AN AUDIT?</div>
        <div style={{fontSize:15,fontWeight:700,color:T.white,marginBottom:10,lineHeight:1.5}}>
          An audit is a systematic process of measuring current practice against a defined standard, identifying gaps, taking corrective action, and re-measuring to confirm improvement.
        </div>
        <div style={{fontSize:13,color:T.text,lineHeight:1.8}}>
          Audit is not just data collection. The improvement action and re-audit are mandatory parts of the cycle. A single data collection without follow-up action is <span style={{color:T.orange}}>not a complete audit</span>.
        </div>
      </div>

      {/* Audit Cycle */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:14}}>THE AUDIT CYCLE — 5 STEPS</div>
        <div style={{display:"grid",gap:8}}>
          {[
            {step:1,color:T.blue,icon:"🎯",title:"Choose Topic & Set Standard",desc:"Identify what you want to measure. Define the standard — e.g. 'Hand hygiene compliance should be ≥85%'. Standard can come from NABH, hospital policy, or evidence-based guidelines."},
            {step:2,color:T.gold,icon:"📋",title:"Collect Data — Measure Current Practice",desc:"Observe, record, or review patient care against the standard. Define your sample size. This is your baseline measurement."},
            {step:3,color:T.orange,icon:"🔍",title:"Compare Data Against Standard",desc:"Calculate your compliance %. If below the standard, identify the root cause — is it a knowledge gap, process failure, resource issue, or behavioural problem?"},
            {step:4,color:T.red,icon:"🔧",title:"Implement Change",desc:"Take corrective action based on root cause. Could be re-training, SOP revision, infrastructure change, or process redesign. Document what change was made and when."},
            {step:5,color:T.green,icon:"✅",title:"Re-audit — Confirm Improvement",desc:"After allowing time for the change to embed (usually 3–6 months), repeat the audit. Compare new compliance % with baseline. This is the proof of improvement NABH assessors look for."},
          ].map(s=>(
            <div key={s.step} style={{display:"flex",gap:12,alignItems:"flex-start",padding:"12px 14px",background:T.panel2,borderRadius:8,border:`1px solid ${s.color}20`}}>
              <div style={{width:32,height:32,borderRadius:"50%",background:`${s.color}20`,border:`2px solid ${s.color}40`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:16,flexShrink:0}}>{s.icon}</div>
              <div>
                <div style={{fontSize:13,fontWeight:700,color:s.color,marginBottom:4}}>Step {s.step}: {s.title}</div>
                <div style={{fontSize:12,color:T.text,lineHeight:1.6}}>{s.desc}</div>
              </div>
            </div>
          ))}
        </div>
        <div style={{marginTop:12,padding:"10px 14px",background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,fontSize:12,color:T.text,lineHeight:1.6}}>
          <span style={{fontWeight:700,color:T.green}}>Key message for NABH: </span>
          Assessors want to see the full cycle — not just records of audits done, but evidence that findings led to action and action led to improvement. Two complete cycles on the same topic is stronger than ten single-cycle audits.
        </div>
      </div>

      {/* Types */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:12}}>TYPES OF AUDIT — NO FIXED NUMBER</div>
        <div style={{fontSize:13,color:T.text,lineHeight:1.7,marginBottom:12}}>
          NABH does not mandate a fixed number of audits. Audit can cover any area that is beneficial to patients and the hospital. What matters is: <span style={{color:T.gold,fontWeight:700}}>quality of the cycle, not quantity of audits.</span>
        </div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8}}>
          {[
            {cat:"Clinical Audit",icon:"🏥",desc:"Measures clinical care — hand hygiene, medication errors, consent, fall rates, surgical site infections"},
            {cat:"Nursing Audit",icon:"💉",desc:"Nursing-specific — IV care, catheter care, pressure ulcer prevention, nursing documentation"},
            {cat:"Quality Improvement Project",icon:"🎯",desc:"Structured project following improvement methodology. NABH mandates minimum 2 QIPs per year"},
            {cat:"Process Audit",icon:"⚙️",desc:"Measures whether processes are followed — discharge process, admission process, referral process"},
            {cat:"Structural Audit",icon:"🏗️",desc:"Physical infrastructure, equipment availability, facility compliance — biomedical, fire safety"},
            {cat:"Outcome Audit",icon:"📊",desc:"Patient outcomes — mortality rate, readmission rate, complication rates, patient satisfaction"},
            {cat:"Financial Audit",icon:"💰",desc:"Billing accuracy, cost per procedure, insurance claim compliance, revenue leakage"},
            {cat:"Pharmacy Audit",icon:"💊",desc:"Prescription accuracy, drug storage, expiry management, HIGH alert medication compliance"},
          ].map(t=>(
            <div key={t.cat} style={{padding:"10px 12px",background:T.panel2,borderRadius:8,border:`1px solid ${T.border}`}}>
              <div style={{fontSize:13,fontWeight:700,color:T.white,marginBottom:3}}>{t.icon} {t.cat}</div>
              <div style={{fontSize:12,color:T.muted,lineHeight:1.5}}>{t.desc}</div>
            </div>
          ))}
        </div>
      </div>

      {/* Common mistakes */}
      <div style={{background:T.panel,border:`1px solid ${T.red}30`,borderRadius:12,padding:"18px 20px"}}>
        <div style={{fontSize:11,letterSpacing:3,color:T.red,marginBottom:12}}>COMMON AUDIT MISTAKES TO AVOID</div>
        <div style={{display:"grid",gap:6}}>
          {[
            "Doing the audit but taking no corrective action — assessors will reject this",
            "Not defining the standard before collecting data — data becomes meaningless",
            "Sample size too small — 5 observations out of 500 is not valid",
            "Re-audit done too soon — changes need 3–6 months to embed before re-measurement",
            "Recording 100% compliance on every audit — assessors will question authenticity",
            "Audit done only once before assessment — shows no improvement trend",
            "Avoid applying the same methodology (e.g. PDCA) to every audit — use the approach that best fits the problem",
          ].map((m,i)=>(
            <div key={i} style={{display:"flex",gap:8,alignItems:"flex-start",padding:"7px 10px",background:T.redD,borderRadius:6}}>
              <span style={{color:T.red,fontSize:14,flexShrink:0}}>✗</span>
              <span style={{fontSize:12,color:T.text,lineHeight:1.5}}>{m}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  // ── MY AUDITS tab ──
  const MyAuditsTab=()=>(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:12,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:15,fontWeight:700,color:T.white}}>My Hospital Audits</div>
          <div style={{fontSize:12,color:T.muted,marginTop:2}}>{customAudits.length} custom audit{customAudits.length!==1?"s":""} · Any type, any number · Your hospital's own audit programme</div>
        </div>
        <button onClick={()=>setShowCreateForm(p=>!p)} style={{padding:"7px 16px",borderRadius:8,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:13,fontWeight:700,cursor:"pointer"}}>
          {showCreateForm?"✕ Cancel":"+ Create New Audit"}
        </button>
      </div>

      {/* Create form */}
      {showCreateForm&&(
        <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:"18px 20px",marginBottom:14}}>
          <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:14,letterSpacing:1}}>📋 NEW AUDIT</div>
          <div style={{display:"grid",gap:10}}>
            <div>
              <div style={lbl}>AUDIT NAME *</div>
              <input value={createForm.name} onChange={e=>setCreateForm(f=>({...f,name:e.target.value}))} placeholder="e.g. Hand Hygiene Compliance Audit, OT Checklist Audit…" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
            </div>
            <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
              <div>
                <div style={lbl}>CATEGORY</div>
                <select value={createForm.audit_category} onChange={e=>setCreateForm(f=>({...f,audit_category:e.target.value}))} style={{...inp,width:"100%"}}>
                  {AUDIT_CATEGORIES.map(c=><option key={c.value} value={c.value}>{c.label}</option>)}
                </select>
              </div>
              <div style={{display:"flex",alignItems:"flex-end",paddingBottom:4}}>
                <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer"}}>
                  <input type="checkbox" checked={createForm.is_core} onChange={e=>setCreateForm(f=>({...f,is_core:e.target.checked}))}/> Mark as CORE (critical audit)
                </label>
              </div>
            </div>

            {/* Parameters */}
            <div>
              <div style={lbl}>CHECKLIST PARAMETERS (optional — add items to check during audit)</div>
              {createForm.parameters.map((p,i)=>(
                <div key={i} style={{display:"flex",gap:6,marginBottom:5,alignItems:"center"}}>
                  <input value={p} onChange={e=>{const ps=[...createForm.parameters];ps[i]=e.target.value;setCreateForm(f=>({...f,parameters:ps}));}} style={{...inp,flex:1}} placeholder={`Parameter ${i+1}`}/>
                  <button onClick={()=>setCreateForm(f=>({...f,parameters:f.parameters.filter((_,j)=>j!==i)}))} style={{padding:"4px 9px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:13,cursor:"pointer"}}>✕</button>
                </div>
              ))}
              <div style={{display:"flex",gap:6,marginTop:4}}>
                <input value={newParam} onChange={e=>setNewParam(e.target.value)} onKeyDown={e=>{if(e.key==="Enter"&&newParam.trim()){setCreateForm(f=>({...f,parameters:[...f.parameters,newParam.trim()]}));setNewParam("");}}} placeholder="Type parameter and press Enter…" style={{...inp,flex:1}}/>
                <button onClick={()=>{if(newParam.trim()){setCreateForm(f=>({...f,parameters:[...f.parameters,newParam.trim()]}));setNewParam("");}}} style={{padding:"4px 12px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:12,cursor:"pointer"}}>+ Add</button>
              </div>
              <div style={{fontSize:11,color:T.muted,marginTop:4}}>Parameters become checkboxes during audit recording. Leave empty if you prefer free-text findings only.</div>
            </div>

            <button onClick={createCustomAudit} disabled={savingCreate||!createForm.name.trim()} style={{padding:"9px 20px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:14,fontWeight:700,cursor:"pointer",opacity:savingCreate||!createForm.name.trim()?0.5:1,marginTop:4}}>
              {savingCreate?"Creating…":"✓ Create Audit"}
            </button>
          </div>
        </div>
      )}

      {customAudits.length===0&&!showCreateForm&&(
        <div style={{textAlign:"center",padding:"40px 20px",color:T.muted}}>
          <div style={{fontSize:32,marginBottom:12}}>📋</div>
          <div style={{fontSize:15,color:T.text,marginBottom:6}}>No custom audits yet</div>
          <div style={{fontSize:13,lineHeight:1.6}}>Create your hospital's own audit programme. You can add clinical, nursing, financial, structural — any type of audit relevant to your hospital.</div>
        </div>
      )}

      <div style={{display:"grid",gap:8}}>
        {customAudits.map(a=>{
          const isOpen=customExpanded===a.id;
          const params=Array.isArray(a.parameters)?a.parameters:JSON.parse(a.parameters||"[]");
          const records=getCustomRecords(a.id);
          const hasRecentRecord=records.some(r=>new Date(r.audit_date)>new Date(Date.now()-365*24*60*60*1000));
          const catLabel=AUDIT_CATEGORIES.find(c=>c.value===a.audit_category)?.label||a.audit_category;
          const avgCompliance=records.length>0?Math.round(records.filter(r=>r.sample_size>0).reduce((sum,r)=>sum+(r.compliant_count/r.sample_size)*100,0)/Math.max(1,records.filter(r=>r.sample_size>0).length)):null;

          return (
            <div key={a.id} style={{background:T.panel,border:`1px solid ${a.is_core?`${T.red}30`:T.border}`,borderRadius:10,overflow:"hidden"}}>
              {deleteConfirm===a.id&&(
                <div style={{background:T.redD,padding:"10px 16px",display:"flex",gap:10,alignItems:"center",justifyContent:"space-between"}}>
                  <span style={{fontSize:13,color:T.red}}>Delete "{a.name}" and all its records?</span>
                  <div style={{display:"flex",gap:6}}>
                    <button onClick={()=>deleteCustomAudit(a.id)} style={{padding:"4px 12px",borderRadius:6,background:T.red,border:"none",color:"#fff",fontSize:13,cursor:"pointer"}}>Delete</button>
                    <button onClick={()=>setDeleteConfirm(null)} style={{padding:"4px 12px",borderRadius:6,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:13,cursor:"pointer"}}>Cancel</button>
                  </div>
                </div>
              )}
              <div style={{padding:"12px 16px",cursor:"pointer"}} onClick={()=>setCustomExpanded(isOpen?null:a.id)}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                  <div style={{width:44,height:44,borderRadius:8,background:a.is_core?T.redD:T.goldD,border:`1px solid ${a.is_core?T.red:T.gold}30`,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,fontSize:20}}>
                    {AUDIT_CATEGORIES.find(c=>c.value===a.audit_category)?.label.split(" ")[0]||"📋"}
                  </div>
                  <div style={{flex:1}}>
                    <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:4,flexWrap:"wrap"}}>
                      <span style={{fontSize:14,fontWeight:700,color:T.white}}>{a.name}</span>
                      {a.is_core&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${T.red}20`,color:T.red}}>CORE</span>}
                      {hasRecentRecord?<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✓ {records.length} record{records.length!==1?"s":""}</span>
                        :<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.redD,color:T.red}}>No records</span>}
                      {customRecordSuccess===a.id&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✅ Saved!</span>}
                    </div>
                    <div style={{display:"flex",gap:10,flexWrap:"wrap"}}>
                      <span style={{fontSize:12,color:T.muted}}>{catLabel}</span>
                      {params.length>0&&<span style={{fontSize:12,color:T.muted}}>📝 {params.length} parameters</span>}
                      {avgCompliance!==null&&<span style={{fontSize:12,color:avgCompliance>=80?T.green:avgCompliance>=60?T.orange:T.red,fontWeight:700}}>Avg: {avgCompliance}%</span>}
                    </div>
                  </div>
                  <div style={{display:"flex",gap:5,alignItems:"center"}}>
                    <button onClick={e=>{e.stopPropagation();setShowCustomRecord(a.id);setCustomRecordForm({status:"completed"});}} style={{padding:"4px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold}}>+ Record</button>
                    <button onClick={e=>{e.stopPropagation();setDeleteConfirm(a.id);}} style={{padding:"4px 8px",borderRadius:6,fontSize:11,cursor:"pointer",background:"transparent",border:`1px solid ${T.red}30`,color:T.red}}>🗑</button>
                    <span style={{fontSize:16,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                  </div>
                </div>
              </div>

              {/* Record form */}
              {showCustomRecord===a.id&&(
                <div style={{borderTop:`1px solid ${T.gold}40`,padding:"16px",background:T.panel2}}>
                  <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:12,letterSpacing:1}}>📋 RECORD AUDIT — {a.name}</div>
                  <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                    {[["Audit Date *","date","audit_date"],["Auditor Name","text","auditor_name"],["Department","text","department"]].map(([l,t,k])=>(
                      <div key={k}><div style={lbl}>{l}</div><input type={t} value={customRecordForm[k]||""} onChange={e=>setCustomRecordForm(f=>({...f,[k]:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                    ))}
                    <div>
                      <div style={lbl}>STATUS</div>
                      <select value={customRecordForm.status||"completed"} onChange={e=>setCustomRecordForm(f=>({...f,status:e.target.value}))} style={{...inp,width:"100%"}}>
                        <option value="completed">Completed</option>
                        <option value="planned">Planned</option>
                        <option value="missed">Missed</option>
                      </select>
                    </div>
                  </div>

                  {/* Checklist parameters */}
                  {params.length>0&&(
                    <div style={{marginBottom:12}}>
                      <div style={{fontSize:12,fontWeight:700,color:T.gold,marginBottom:8,letterSpacing:1}}>CHECKLIST — TICK COMPLIANT ITEMS</div>
                      <div style={{display:"grid",gap:5}}>
                        {params.map((p,i)=>{
                          const isDone=customRecordForm[`param_${i}`];
                          return(
                            <div key={i} onClick={()=>setCustomRecordForm(f=>({...f,[`param_${i}`]:!f[`param_${i}`]}))}
                              style={{display:"flex",gap:10,alignItems:"center",padding:"8px 12px",background:isDone?T.greenD:T.panel,border:`1px solid ${isDone?T.green:T.border}30`,borderRadius:7,cursor:"pointer"}}>
                              <div style={{width:16,height:16,borderRadius:3,border:`2px solid ${isDone?T.green:T.muted}`,background:isDone?T.green:"transparent",display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,color:T.bg,flexShrink:0}}>{isDone?"✓":""}</div>
                              <span style={{fontSize:13,color:isDone?T.green:T.text}}>{p}</span>
                            </div>
                          );
                        })}
                      </div>
                      <div style={{fontSize:12,color:T.muted,marginTop:6}}>
                        Compliant: {params.filter((_,i)=>customRecordForm[`param_${i}`]).length}/{params.length}
                        {params.length>0&&<span style={{marginLeft:8,fontWeight:700,color:Math.round(params.filter((_,i)=>customRecordForm[`param_${i}`]).length/params.length*100)>=80?T.green:T.orange}}>
                          ({Math.round(params.filter((_,i)=>customRecordForm[`param_${i}`]).length/params.length*100)}%)
                        </span>}
                      </div>
                    </div>
                  )}

                  {params.length===0&&(
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                      <div><div style={lbl}>SAMPLE SIZE</div><input type="number" value={customRecordForm.sample_size||""} onChange={e=>setCustomRecordForm(f=>({...f,sample_size:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                      <div><div style={lbl}>COMPLIANT COUNT</div><input type="number" value={customRecordForm.compliant_count||""} onChange={e=>setCustomRecordForm(f=>({...f,compliant_count:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                    </div>
                  )}

                  <div style={{marginBottom:10}}><div style={lbl}>FINDINGS</div><textarea value={customRecordForm.findings||""} onChange={e=>setCustomRecordForm(f=>({...f,findings:e.target.value}))} rows={2} placeholder="Key findings from this audit…" style={{...inp,width:"100%",resize:"vertical",boxSizing:"border-box"}}/></div>

                  <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:10}}>
                    <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer"}}>
                      <input type="checkbox" checked={customRecordForm.capa_raised||false} onChange={e=>setCustomRecordForm(f=>({...f,capa_raised:e.target.checked}))}/> CAPA Required
                    </label>
                  </div>

                  {customRecordForm.capa_raised&&(
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                      <div><div style={lbl}>CAPA NOTES</div><input value={customRecordForm.capa_notes||""} onChange={e=>setCustomRecordForm(f=>({...f,capa_notes:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                      <div><div style={lbl}>TARGET DATE</div><input type="date" value={customRecordForm.capa_target_date||""} onChange={e=>setCustomRecordForm(f=>({...f,capa_target_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                      <div><div style={lbl}>RE-AUDIT DATE</div><input type="date" value={customRecordForm.reaudit_date||""} onChange={e=>setCustomRecordForm(f=>({...f,reaudit_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                    </div>
                  )}

                  <div style={{marginBottom:10}}>
                    <div style={lbl}>EVIDENCE LINK — Audit Report (Google Drive / OneDrive URL)</div>
                    <input value={customRecordForm.evidence_url||""} onChange={e=>setCustomRecordForm(f=>({...f,evidence_url:e.target.value}))} placeholder="https://drive.google.com/…" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                  </div>

                  <div style={{display:"flex",gap:8}}>
                    <button onClick={()=>saveCustomRecord(a)} disabled={savingCustomRecord} style={{padding:"8px 20px",borderRadius:8,background:T.green,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>{savingCustomRecord?"Saving…":"💾 Save Record"}</button>
                    <button onClick={()=>{setShowCustomRecord(null);setCustomRecordForm({});}} style={{padding:"8px 16px",borderRadius:8,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:13,cursor:"pointer"}}>Cancel</button>
                  </div>
                </div>
              )}

              {/* Expanded detail */}
              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px"}}>
                  {params.length>0&&(
                    <div style={{marginBottom:12}}>
                      <div style={{fontSize:11,color:T.muted,marginBottom:6,letterSpacing:1}}>CHECKLIST PARAMETERS ({params.length})</div>
                      <div style={{display:"flex",gap:5,flexWrap:"wrap"}}>
                        {params.map((p,i)=><span key={i} style={{fontSize:12,padding:"3px 9px",borderRadius:6,background:T.panel2,border:`1px solid ${T.border}`,color:T.text}}>📌 {p}</span>)}
                      </div>
                    </div>
                  )}
                  {records.length>0&&(
                    <div>
                      <div style={{fontSize:11,color:T.muted,marginBottom:6,letterSpacing:1}}>AUDIT RECORDS ({records.length})</div>
                      {records.map(r=>{
                        const compPct=r.sample_size>0?Math.round((r.compliant_count/r.sample_size)*100):null;
                        return(
                          <div key={r.id} style={{background:T.panel2,borderRadius:8,padding:"10px 12px",marginBottom:6,border:`1px solid ${compPct!==null?(compPct>=80?`${T.green}20`:`${T.orange}20`):T.border}`}}>
                            <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start"}}>
                              <div>
                                <div style={{fontSize:13,fontWeight:700,color:T.white}}>{r.audit_date}</div>
                                <div style={{fontSize:12,color:T.muted,marginTop:2}}>{r.auditor_name&&`Auditor: ${r.auditor_name}`}{r.department&&` · ${r.department}`}</div>
                                {compPct!==null&&<div style={{fontSize:13,fontWeight:700,color:compPct>=80?T.green:T.orange,marginTop:3}}>Compliance: {compPct}% ({r.compliant_count}/{r.sample_size})</div>}
                                {r.findings&&<div style={{fontSize:11,color:T.text,marginTop:3,lineHeight:1.4}}>{r.findings}</div>}
                                {r.capa_raised&&<div style={{fontSize:11,color:T.orange,marginTop:2}}>⚠️ CAPA: {r.capa_notes} — Due: {r.capa_target_date||"—"}</div>}
                              </div>
                              <div style={{display:"flex",gap:6,alignItems:"flex-start"}}>
                                {r.evidence_url&&<a href={r.evidence_url} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Report</a>}
                                <button onClick={()=>deleteCustomRecord(r.id)} style={{fontSize:11,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                              </div>
                            </div>
                          </div>
                        );
                      })}
                    </div>
                  )}
                  {records.length===0&&<div style={{fontSize:13,color:T.muted,textAlign:"center",padding:"16px 0"}}>No records yet. Click "+ Record" to log your first audit.</div>}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );

  return (
    <div>
      {/* Main tab bar */}
      <div style={{display:"flex",gap:6,marginBottom:14,borderBottom:`1px solid ${T.border}`,paddingBottom:10}}>
        {[
          {id:"nabh",label:"📋 NABH Audits",count:audits.length},
          {id:"mine",label:"➕ My Audits",count:customAudits.length},
          {id:"learn",label:"📖 What is Audit?"},
        ].map(t=>(
          <button key={t.id} onClick={()=>setMainTab(t.id)}
            style={{padding:"7px 16px",borderRadius:8,fontSize:13,fontWeight:600,cursor:"pointer",
              background:mainTab===t.id?T.goldD:"transparent",
              border:`1px solid ${mainTab===t.id?T.gold:T.border}`,
              color:mainTab===t.id?T.goldL:T.muted}}>
            {t.label}{t.count!==undefined&&<span style={{marginLeft:5,fontSize:11,opacity:0.7}}>({t.count})</span>}
          </button>
        ))}
      </div>

      {mainTab==="learn"&&<LearnTab/>}
      {mainTab==="mine"&&<MyAuditsTab/>}

      {mainTab==="nabh"&&(
        <div>
          {/* Summary — fixed framing */}
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",marginBottom:14}}>
            <div style={{display:"flex",gap:16,alignItems:"center",flexWrap:"wrap"}}>
              <div style={{flex:1}}>
                <div style={{fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1}}>NABH AUDIT PROGRAMME — LAST 12 MONTHS</div>
                <div style={{fontSize:14,color:completedAudits>0?T.green:T.orange,fontWeight:700}}>
                  {completedAudits} of {totalAudits} NABH audits have records in last 12 months
                </div>
                <div style={{fontSize:12,color:T.muted,marginTop:3}}>NABH has no fixed minimum number — focus on completing the full audit cycle for each audit conducted.</div>
                <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
                  <div style={{height:"100%",borderRadius:2,background:completedAudits>0?T.green:T.orange,width:`${Math.min(100,(completedAudits/Math.max(totalAudits,1))*100)}%`,transition:"width 0.5s"}}/>
                </div>
              </div>
              <div style={{textAlign:"right"}}>
                <div style={{fontSize:20,fontWeight:700,color:T.gold}}>{completedAudits}/{totalAudits}</div>
                <div style={{fontSize:11,color:T.muted}}>With records</div>
              </div>
            </div>
          </div>

          {/* Category tabs */}
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"10px 14px",marginBottom:6,display:"flex",gap:8,flexWrap:"wrap"}}>
            {[["ALL","📋 All Categories"],["clinical","🏥 Clinical Audit"],["nursing","💉 Nursing Audit"],["qip","🎯 Quality Improvement Project"]].map(([f,l])=>(
              <button key={f} onClick={()=>setCatFilter(f)} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:catFilter===f?T.goldD:"transparent",border:`1px solid ${catFilter===f?T.gold:T.border}`,color:catFilter===f?T.goldL:T.muted}}>{l}
                {f!=="ALL"&&<span style={{marginLeft:4,fontSize:11,color:catFilter===f?T.gold:T.muted}}>({audits.filter(a=>(a.audit_category||"clinical")===f).length})</span>}
              </button>
            ))}
          </div>
          {catFilter==="qip"&&(
            <div style={{background:T.goldD,border:`1px solid ${T.gold}40`,borderRadius:8,padding:"8px 14px",marginBottom:8,fontSize:12,color:T.goldL}}>
              ⭐ <b>NABH Mandatory:</b> Minimum 2 Quality Improvement Projects per year. Each QIP must be presented to the Quality Management Committee.
            </div>
          )}
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"10px 14px",marginBottom:14,display:"flex",gap:8}}>
            {[["ALL",`All (${filtered.length})`],["CORE",`🔴 CORE (${filtered.filter(a=>a.is_core).length})`],["NON_CORE",`🟡 Non-CORE (${filtered.filter(a=>!a.is_core).length})`]].map(([f,l])=>(
              <button key={f} onClick={()=>setFilter(f)} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:filter===f?T.goldD:"transparent",border:`1px solid ${filter===f?T.gold:T.border}`,color:filter===f?T.goldL:T.muted}}>{l}</button>
            ))}
          </div>

          <div style={{display:"grid",gap:8}}>
            {filtered.map(a=>{
              const isOpen=expanded===a.id;
              const params=Array.isArray(a.parameters)?a.parameters:JSON.parse(a.parameters||"[]");
              const doneCount=params.filter((_,i)=>checked[`${a.id}-${i}`]).length;
              const records=getRecords(a.id);
              const hasRecentRecord=records.some(r=>new Date(r.audit_date)>new Date(Date.now()-365*24*60*60*1000));
              const compPctAvg=records.length>0?Math.round(records.filter(r=>r.sample_size>0).reduce((sum,r)=>sum+(r.compliant_count/r.sample_size)*100,0)/Math.max(1,records.filter(r=>r.sample_size>0).length)):null;
              return (
                <div key={a.id} style={{background:T.panel,border:`1px solid ${a.is_core?`${T.red}30`:T.border}`,borderRadius:10,overflow:"hidden"}}>
                  <div style={{padding:"12px 16px",cursor:"pointer"}} onClick={()=>setExpanded(isOpen?null:a.id)}>
                    <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                      <div style={{width:44,height:44,borderRadius:8,background:a.is_core?T.redD:T.goldD,border:`1px solid ${a.is_core?T.red:T.gold}30`,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0,flexDirection:"column"}}>
                        <span style={{fontSize:11,fontWeight:800,color:a.is_core?T.red:T.gold}}>{a.audit_code}</span>
                        {a.is_core&&<span style={{fontSize:7,color:T.red}}>CORE</span>}
                      </div>
                      <div style={{flex:1}}>
                        <div style={{display:"flex",gap:8,alignItems:"center",marginBottom:4,flexWrap:"wrap"}}>
                          <span style={{fontSize:14,fontWeight:700,color:T.white}}>{a.name}</span>
                          {a.is_core&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:`${T.red}20`,color:T.red}}>CORE</span>}
                          {hasRecentRecord?<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✓ {records.length} record{records.length>1?"s":""}</span>
                            :<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.redD,color:T.red}}>No records</span>}
                          {recordSuccess===a.id&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:T.greenD,color:T.green}}>✅ Saved!</span>}
                          {compPctAvg!==null&&<span style={{fontSize:8,padding:"2px 6px",borderRadius:4,background:compPctAvg>=80?T.greenD:T.orangeD,color:compPctAvg>=80?T.green:T.orange,fontWeight:700}}>Avg {compPctAvg}%</span>}
                        </div>
                        <div style={{display:"flex",gap:10,flexWrap:"wrap"}}>
                          <span style={{fontSize:12,color:T.muted}}>📋 {a.nabh_ref}</span>
                          <span style={{fontSize:12,color:T.muted}}>📅 {a.frequency}</span>
                          <span style={{fontSize:12,color:T.muted}}>👤 {a.who_does_it}</span>
                        </div>
                      </div>
                      {doneCount>0&&<span style={{fontSize:12,color:T.green,flexShrink:0}}>{doneCount}/{params.length} ✓</span>}
                      <button onClick={e=>{e.stopPropagation();setShowRecordForm(a.id);setRecordForm(emptyRecord());}} style={{padding:"4px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,flexShrink:0}}>+ Record Audit</button>
                      <span style={{fontSize:16,color:T.muted}}>{isOpen?"▲":"▼"}</span>
                    </div>
                  </div>

                  {showRecordForm===a.id&&(
                    <div style={{borderTop:`1px solid ${T.gold}40`,padding:"16px",background:T.panel2}}>
                      <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:12,letterSpacing:1}}>📋 RECORD AUDIT — {a.name}</div>
                      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                        {[["Audit Date *","date","audit_date"],["Auditor Name","text","auditor_name"],["Department","text","department"],["Status","select","status"]].map(([l,t,k])=>(
                          <div key={k}><div style={lbl}>{l}</div>
                            {t==="select"?<select value={recordForm[k]} onChange={e=>setRecordForm(f=>({...f,[k]:e.target.value}))} style={{...inp,width:"100%"}}>
                              <option value="completed">Completed</option><option value="planned">Planned</option><option value="missed">Missed</option>
                            </select>:<input type={t} value={recordForm[k]} onChange={e=>setRecordForm(f=>({...f,[k]:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/>}
                          </div>
                        ))}
                        <div><div style={lbl}>SAMPLE SIZE</div><input type="number" value={recordForm.sample_size} onChange={e=>setRecordForm(f=>({...f,sample_size:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                        <div><div style={lbl}>COMPLIANT COUNT</div><input type="number" value={recordForm.compliant_count} onChange={e=>setRecordForm(f=>({...f,compliant_count:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                      </div>
                      <div style={{marginBottom:10}}><div style={lbl}>FINDINGS</div><textarea value={recordForm.findings} onChange={e=>setRecordForm(f=>({...f,findings:e.target.value}))} rows={2} style={{...inp,width:"100%",resize:"vertical",boxSizing:"border-box"}}/></div>
                      <div style={{display:"flex",alignItems:"center",gap:8,marginBottom:10}}>
                        <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer"}}>
                          <input type="checkbox" checked={recordForm.capa_raised} onChange={e=>setRecordForm(f=>({...f,capa_raised:e.target.checked}))}/> CAPA Required
                        </label>
                      </div>
                      {recordForm.capa_raised&&(
                        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
                          <div><div style={lbl}>CAPA NOTES</div><input value={recordForm.capa_notes} onChange={e=>setRecordForm(f=>({...f,capa_notes:e.target.value}))} style={{...inp,width:"100%",boxSizing:"border-box"}}/></div>
                          <div><div style={lbl}>TARGET DATE</div><input type="date" value={recordForm.capa_target_date} onChange={e=>setRecordForm(f=>({...f,capa_target_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                          <div><div style={lbl}>RE-AUDIT DATE</div><input type="date" value={recordForm.reaudit_date} onChange={e=>setRecordForm(f=>({...f,reaudit_date:e.target.value}))} style={{...inp,width:"100%"}}/></div>
                        </div>
                      )}
                      <div style={{marginBottom:10}}>
                        <div style={lbl}>EVIDENCE LINK — Audit Report (Google Drive / OneDrive URL)</div>
                        <input value={recordForm.evidence_url} onChange={e=>setRecordForm(f=>({...f,evidence_url:e.target.value}))} placeholder="https://drive.google.com/…" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                      </div>
                      <div style={{display:"flex",gap:8}}>
                        <button onClick={()=>saveRecord(a.id)} disabled={saving} style={{padding:"8px 20px",borderRadius:8,background:T.green,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>{saving?"Saving…":"💾 Save Record"}</button>
                        <button onClick={()=>{setShowRecordForm(null);setRecordForm(emptyRecord());}} style={{padding:"8px 16px",borderRadius:8,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:13,cursor:"pointer"}}>Cancel</button>
                      </div>
                    </div>
                  )}

                  {isOpen&&(
                    <div style={{borderTop:`1px solid ${T.border}`,padding:"14px 16px",display:"grid",gap:12}}>
                      {records.length>0&&(
                        <div>
                          <AuditComplianceChart records={records}/>
                          <div style={{fontSize:11,color:T.muted,marginBottom:6,letterSpacing:1,marginTop:12}}>AUDIT RECORDS ({records.length})</div>
                          {records.map(r=>{
                            const rPct=r.sample_size>0?Math.round((r.compliant_count/r.sample_size)*100):null;
                            return(
                              <div key={r.id} style={{background:T.panel2,borderRadius:8,padding:"10px 12px",marginBottom:6,border:`1px solid ${rPct!==null?(rPct>=80?`${T.green}20`:`${T.orange}20`):T.border}`}}>
                                <div style={{display:"flex",justifyContent:"space-between",alignItems:"flex-start"}}>
                                  <div>
                                    <div style={{fontSize:13,fontWeight:700,color:T.white}}>{r.audit_date}</div>
                                    <div style={{fontSize:12,color:T.muted,marginTop:2}}>{r.auditor_name&&`Auditor: ${r.auditor_name}`}{r.department&&` · ${r.department}`}</div>
                                    {rPct!==null&&<div style={{fontSize:13,fontWeight:700,color:rPct>=80?T.green:T.orange,marginTop:3}}>Compliance: {rPct}% ({r.compliant_count}/{r.sample_size})</div>}
                                    {r.findings&&<div style={{fontSize:11,color:T.text,marginTop:3,lineHeight:1.4}}>{r.findings}</div>}
                                    {r.capa_raised&&<div style={{fontSize:11,color:T.orange,marginTop:2}}>⚠️ CAPA: {r.capa_notes} — Due: {r.capa_target_date||"—"}</div>}
                                  </div>
                                  <div style={{display:"flex",gap:6,alignItems:"flex-start"}}>
                                    {r.evidence_url&&<a href={r.evidence_url} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Report</a>}
                                    <button onClick={()=>deleteRecord(r.id)} style={{fontSize:11,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                                  </div>
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      )}
                      {a.conduct_guide&&(()=>{
                        const cg=typeof a.conduct_guide==="string"?JSON.parse(a.conduct_guide):a.conduct_guide;
                        const isGuideOpen=guideOpen===a.id;
                        return (
                          <div style={{borderTop:`1px dashed ${T.border}`,paddingTop:10,marginTop:2}}>
                            <div onClick={()=>setGuideOpen(isGuideOpen?null:a.id)} style={{cursor:"pointer",display:"flex",alignItems:"center",gap:6,fontSize:12,color:T.gold,letterSpacing:1,fontWeight:700}}>
                              <span>{isGuideOpen?"▲":"▼"}</span><span>📖 HOW TO CONDUCT THIS AUDIT</span>
                            </div>
                            {isGuideOpen&&(
                              <div style={{display:"grid",gap:10,marginTop:10,padding:"12px 14px",background:T.panel2,borderRadius:8,border:`1px solid ${T.gold}20`}}>
                                {Array.isArray(cg.preparation)&&cg.preparation.length>0&&(
                                  <div><div style={{fontSize:11,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>PREPARATION</div>
                                    <div style={{display:"grid",gap:4}}>{cg.preparation.map((step,i)=>(
                                      <div key={i} style={{display:"flex",gap:8,padding:"6px 9px",background:T.panel,borderRadius:5,border:`1px solid ${T.border}`}}>
                                        <span style={{fontSize:11,color:T.gold,fontWeight:700,minWidth:14}}>{i+1}.</span>
                                        <span style={{fontSize:12,color:T.text,lineHeight:1.5}}>{step}</span>
                                      </div>
                                    ))}</div>
                                  </div>
                                )}
                                {Array.isArray(cg.execution_steps)&&cg.execution_steps.length>0&&(
                                  <div><div style={{fontSize:11,color:T.gold,marginBottom:6,letterSpacing:1,fontWeight:700}}>EXECUTION</div>
                                    <div style={{display:"grid",gap:5}}>{cg.execution_steps.map((step,i)=>(
                                      <div key={i} style={{padding:"7px 10px",background:T.panel,borderRadius:5,borderLeft:`3px solid ${T.gold}`,fontSize:12,color:T.text,lineHeight:1.55}}>{step}</div>
                                    ))}</div>
                                  </div>
                                )}
                                {cg.sample_size_calculation&&<div style={{padding:"10px 12px",background:T.blueD,borderRadius:6}}><div style={{fontSize:11,color:T.blue,marginBottom:4,fontWeight:700}}>📊 SAMPLE SIZE</div><div style={{fontSize:12,color:T.text}}>{cg.sample_size_calculation}</div></div>}
                                {cg.reporting_template&&<div style={{padding:"10px 12px",background:T.greenD,borderRadius:6}}><div style={{fontSize:11,color:T.green,marginBottom:4,fontWeight:700}}>📄 REPORTING</div><div style={{fontSize:12,color:T.text}}>{cg.reporting_template}</div></div>}
                                {cg.re_audit_timeline&&<div style={{padding:"10px 12px",background:T.orangeD,borderRadius:6}}><div style={{fontSize:11,color:T.orange,marginBottom:4,fontWeight:700}}>🔁 RE-AUDIT</div><div style={{fontSize:12,color:T.text}}>{cg.re_audit_timeline}</div></div>}
                              </div>
                            )}
                          </div>
                        );
                      })()}
                    </div>
                  )}
                </div>
              );
            })}
            {filtered.length===0&&<div style={{textAlign:"center",color:T.muted,padding:30,fontSize:14}}>No audits match this filter.</div>}
          </div>
        </div>
      )}
    </div>
  );
}

// ── CHECKLISTS ────────────────────────────────────────
function ChecklistsScreen({ hospitalId }) {
  const [checklists,setChecklists]=useState([]); const [loading,setLoading]=useState(true);
  const [selected,setSelected]=useState(null); const [checked,setChecked]=useState({});
  const [links,setLinks]=useState({}); // {checklistId: evidence_url}
  const [savingLink,setSavingLink]=useState(null);

  useEffect(()=>{
    const load=async()=>{
      const{data:cl}=await supabase.from("department_checklists").select("*").order("dept");
      setChecklists(cl||[]);
      if(cl&&cl.length>0)setSelected(cl[0]);
      if(hospitalId){
        const{data:ll}=await supabase.from("checklist_links").select("*").eq("hospital_id",hospitalId);
        const lmap={};(ll||[]).forEach(l=>{lmap[l.checklist_id]=l.evidence_url||"";});
        setLinks(lmap);
      }
      setLoading(false);
    };
    load();
  },[hospitalId]);

  const saveLink=async(checklistId,url)=>{
    if(!hospitalId)return;
    setSavingLink(checklistId);
    await supabase.from("checklist_links").upsert({
      hospital_id:hospitalId,checklist_id:checklistId,evidence_url:url||null,updated_at:new Date().toISOString()
    },{onConflict:"hospital_id,checklist_id"});
    setSavingLink(null);
  };

  const items=selected?(Array.isArray(selected.items)?selected.items:JSON.parse(selected.items||"[]")):[];
  const doneCount=items.filter((_,i)=>checked[`${selected?.id}-${i}`]).length;
  const pct=items.length>0?Math.round(doneCount/items.length*100):0;
  if(loading) return <div style={{textAlign:"center",color:T.muted,padding:40}}>Loading checklists…</div>;
  return (
    <div style={{display:"grid",gridTemplateColumns:"210px 1fr",gap:12,alignItems:"start"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:8}}>
        <div style={{fontSize:11,letterSpacing:2,color:T.muted,padding:"5px 8px",marginBottom:4}}>DEPARTMENTS</div>
        {checklists.map(c=>(
          <button key={c.id} onClick={()=>setSelected(c)} style={{width:"100%",textAlign:"left",padding:"7px 10px",borderRadius:7,marginBottom:3,cursor:"pointer",background:selected?.id===c.id?T.goldD:"transparent",border:`1px solid ${selected?.id===c.id?T.gold:T.border}`,color:selected?.id===c.id?T.goldL:T.text,fontSize:13,display:"flex",gap:6,alignItems:"center"}}>
            <span>{c.icon||"📋"}</span><span style={{flex:1}}>{c.dept}</span>
            {links[c.id]&&<span style={{fontSize:8,color:T.green}}>📎</span>}
          </button>
        ))}
      </div>
      {selected&&(
        <div>
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"14px 16px",marginBottom:10}}>
            <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:8}}>
              <div>
                <div style={{fontSize:16,fontWeight:700,color:T.white}}>{selected.icon} {selected.dept}</div>
                <div style={{fontSize:12,color:T.muted,marginTop:2}}>NABH: {selected.nabh_chapter} · {items.length} items</div>
              </div>
              <div style={{textAlign:"center"}}>
                <div style={{fontSize:22,fontWeight:800,color:pct===100?T.green:pct>50?T.gold:T.red}}>{pct}%</div>
                <div style={{fontSize:8,color:T.muted}}>{doneCount}/{items.length}</div>
              </div>
            </div>
            <div style={{height:4,background:T.border,borderRadius:2,marginBottom:12}}><div style={{width:`${pct}%`,height:"100%",background:pct===100?T.green:pct>50?T.gold:T.red,borderRadius:2,transition:"width 0.3s"}}/></div>
            {/* Evidence link */}
            <div>
              <div style={{fontSize:11,color:T.muted,marginBottom:4,letterSpacing:1}}>EVIDENCE LINK — Completed Checklist (Google Drive / OneDrive URL)</div>
              <div style={{display:"flex",gap:8,alignItems:"center"}}>
                <input
                  value={links[selected.id]||""}
                  onChange={e=>setLinks(l=>({...l,[selected.id]:e.target.value}))}
                  onBlur={e=>saveLink(selected.id,e.target.value)}
                  placeholder="https://drive.google.com/… (auto-saves on exit)"
                  style={{flex:1,padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}
                />
                {savingLink===selected.id&&<span style={{fontSize:11,color:T.muted}}>Saving…</span>}
                {links[selected.id]&&savingLink!==selected.id&&(
                  <a href={links[selected.id]} target="_blank" rel="noopener noreferrer"
                    style={{padding:"6px 12px",borderRadius:7,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:12,textDecoration:"none",fontWeight:600,whiteSpace:"nowrap"}}>📎 View</a>
                )}
              </div>
            </div>
          </div>
          <div style={{display:"grid",gap:5}}>
            {items.map((item,i)=>{
              const key=`${selected.id}-${i}`; const done=checked[key];
              return (
                <div key={i} onClick={()=>setChecked(p=>({...p,[key]:!done}))}
                  style={{background:T.panel,border:`1px solid ${done?`${T.green}40`:T.border}`,borderRadius:8,padding:"9px 13px",cursor:"pointer",display:"flex",gap:10,alignItems:"flex-start",opacity:done?0.7:1}}>
                  <div style={{width:17,height:17,borderRadius:4,border:`2px solid ${done?T.green:T.muted}`,background:done?T.green:"transparent",flexShrink:0,display:"flex",alignItems:"center",justifyContent:"center",fontSize:12,color:T.bg,marginTop:1}}>{done?"✓":""}</div>
                  <div style={{flex:1}}>
                    <div style={{fontSize:13,color:done?T.muted:T.text,textDecoration:done?"line-through":"none",lineHeight:1.5}}>{item.t}</div>
                    <div style={{fontSize:11,color:T.muted,marginTop:2}}>Ref: {item.ref}</div>
                  </div>
                </div>
              );
            })}
          </div>
          {pct===100&&<div style={{background:T.greenD,border:`1px solid ${T.green}40`,borderRadius:10,padding:"12px 16px",marginTop:10,textAlign:"center"}}><div style={{fontSize:15,color:T.green,fontWeight:700}}>✅ All items verified for {selected.dept}</div></div>}
        </div>
      )}
    </div>
  );
}

// ── PRICING ──────────────────────────────────────────
function PricingScreen() {
  const plans=[
    {name:"Starter",price:"₹499",period:"/month",color:T.blue,icon:"🏥",users:"1 hospital · 3 users",features:["639 OEs with scoring & tips","26 Committee tracking + MOM","50 KPI monitoring with trends","35 Clinical & nursing audits","Mock drill management","Statutory license tracker","Evidence document links","Patient tracer tool"]},
    {name:"Professional",price:"₹999",period:"/month",color:T.gold,icon:"⭐",users:"1 hospital · Unlimited users",popular:true,features:["Everything in Starter","Unlimited team members","Priority support","Advanced gap analysis","Full audit trend charts","Complete audit history","KPI trend analytics","Early access to new features"]},
    {name:"Consultant",price:"₹2,999",period:"/month",color:T.green,icon:"🏆",users:"Up to 5 hospitals",features:["Everything in Professional","Manage 5 hospitals","Single login dashboard","Ideal for NABH consultants","Bulk hospital onboarding","Client progress tracking","5× saving vs individual plans","Dedicated support channel"]},
  ];
  return (
    <div style={{maxWidth:"100%",overflowX:"hidden"}}>
      {/* Header */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"20px 24px",marginBottom:20,textAlign:"center"}}>
        <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:6}}>PRICING</div>
        <div style={{fontSize:20,fontWeight:800,color:T.white,marginBottom:6}}>Simple, transparent pricing</div>
        <div style={{fontSize:13,color:T.muted}}>14-day free trial on all plans · No credit card required · Pay via UPI</div>
      </div>

      {/* Trial banner */}
      <div style={{background:`linear-gradient(135deg,${T.goldD},rgba(201,168,76,0.05))`,border:`1px solid ${T.gold}40`,borderRadius:12,padding:"14px 20px",marginBottom:20,display:"flex",alignItems:"center",gap:14}}>
        <div style={{fontSize:28}}>🎁</div>
        <div>
          <div style={{fontSize:15,fontWeight:700,color:T.goldL}}>You're on a 14-day free trial</div>
          <div style={{fontSize:13,color:T.muted,marginTop:3}}>Full access to all features during trial. No payment needed until trial ends. To upgrade, contact us on WhatsApp.</div>
        </div>
      </div>

      {/* Plan cards */}
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(260px,1fr))",gap:14,marginBottom:20}}>
        {plans.map(plan=>(
          <div key={plan.name} style={{background:plan.popular?`linear-gradient(145deg,${T.panel},#0f2235)`:T.panel,border:`1px solid ${plan.popular?T.gold:T.border}`,borderRadius:14,padding:"22px 18px",position:"relative"}}>
            {plan.popular&&<div style={{position:"absolute",top:-11,left:"50%",transform:"translateX(-50%)",background:T.gold,color:T.bg,fontSize:8,fontWeight:800,padding:"3px 14px",borderRadius:20,letterSpacing:1,whiteSpace:"nowrap"}}>MOST POPULAR</div>}
            <div style={{textAlign:"center",marginBottom:16}}>
              <div style={{fontSize:26,marginBottom:8}}>{plan.icon}</div>
              <div style={{fontSize:16,fontWeight:800,color:T.white,marginBottom:4}}>{plan.name}</div>
              <div style={{fontSize:11,color:T.muted,marginBottom:12}}>{plan.users}</div>
              <div style={{display:"flex",alignItems:"baseline",justifyContent:"center",gap:2}}>
                <span style={{fontSize:28,fontWeight:800,color:plan.color}}>{plan.price}</span>
                <span style={{fontSize:12,color:T.muted}}>{plan.period}</span>
              </div>
            </div>
            <div style={{borderTop:`1px solid ${T.border}`,paddingTop:14,marginBottom:16}}>
              {plan.features.map((f,i)=>(
                <div key={i} style={{display:"flex",gap:8,alignItems:"flex-start",marginBottom:8}}>
                  <span style={{fontSize:12,color:plan.color,flexShrink:0,marginTop:1}}>✓</span>
                  <span style={{fontSize:12,color:T.text,lineHeight:1.4}}>{f}</span>
                </div>
              ))}
            </div>
            <a href="https://wa.me/918511180957" target="_blank" rel="noopener noreferrer"
              style={{display:"block",textAlign:"center",padding:"10px",borderRadius:8,background:plan.popular?`linear-gradient(135deg,${T.gold},#f0d070)`:T.panel2,border:`1px solid ${plan.popular?T.gold:T.border}`,color:plan.popular?T.bg:T.muted,fontSize:13,fontWeight:plan.popular?700:400,textDecoration:"none",cursor:"pointer"}}>
              {plan.popular?"💬 Upgrade Now":"💬 Contact to Upgrade"}
            </a>
          </div>
        ))}
      </div>

      {/* Contact box */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"18px 24px"}}>
        <div style={{fontSize:13,fontWeight:700,color:T.white,marginBottom:12}}>How to upgrade</div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:12}}>
          <div style={{background:T.panel2,borderRadius:8,padding:"12px 14px"}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:4,letterSpacing:1}}>STEP 1</div>
            <div style={{fontSize:13,color:T.text}}>WhatsApp us your plan choice at <span style={{color:T.green,fontWeight:700}}>+91 85111 80957</span></div>
          </div>
          <div style={{background:T.panel2,borderRadius:8,padding:"12px 14px"}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:4,letterSpacing:1}}>STEP 2</div>
            <div style={{fontSize:13,color:T.text}}>Pay via UPI — we'll send the UPI ID on WhatsApp</div>
          </div>
          <div style={{background:T.panel2,borderRadius:8,padding:"12px 14px"}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:4,letterSpacing:1}}>STEP 3</div>
            <div style={{fontSize:13,color:T.text}}>Your account is activated within 2 hours of payment</div>
          </div>
          <div style={{background:T.panel2,borderRadius:8,padding:"12px 14px"}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:4,letterSpacing:1}}>INVOICE</div>
            <div style={{fontSize:13,color:T.text}}>Invoice provided for all payments. GST invoice available on request.</div>
          </div>
        </div>
        <div style={{marginTop:14,padding:"10px 14px",background:T.goldD,borderRadius:8,border:`1px solid ${T.gold}30`,textAlign:"center"}}>
          <div style={{fontSize:12,color:T.muted}}>Questions? We respond within 2 hours on WhatsApp</div>
          <a href="https://wa.me/918511180957" target="_blank" rel="noopener noreferrer" style={{fontSize:14,color:T.gold,fontWeight:700,textDecoration:"none"}}>💬 +91 85111 80957</a>
        </div>
      </div>
    </div>
  );
}

// ── PROFILE ──────────────────────────────────────────
function ProfileScreen({ user, context, onContextUpdate }) {
  const [hospitalName,setHospitalName]=useState(context?.hospitalName||"");
  const [displayName,setDisplayName]=useState("");
  const [profile,setProfile]=useState(null);
  const [savingHospital,setSavingHospital]=useState(false);
  const [savingProfile,setSavingProfile]=useState(false);
  const [pwCurrent,setPwCurrent]=useState("");
  const [pwNew,setPwNew]=useState("");
  const [pwConfirm,setPwConfirm]=useState("");
  const [pwBusy,setPwBusy]=useState(false);
  const [toast,setToast]=useState(null);

  useEffect(()=>{
    if(!user)return;
    supabase.from("profiles").select("*").eq("id",user.id).single().then(({data})=>{
      if(data){setProfile(data);setDisplayName(data.name||"");}
    });
  },[user]);

  const showToast=(type,msg,sev="SUCCESS")=>{setToast({type,msg,sev});setTimeout(()=>setToast(null),3500);};

  const saveHospital=async()=>{
    if(!hospitalName.trim()){showToast("ERROR","Hospital name cannot be empty","CRITICAL");return;}
    if(!context?.hospitalId){showToast("ERROR","No hospital linked to this account","CRITICAL");return;}
    setSavingHospital(true);
    const{error}=await supabase.from("hospitals").update({name:hospitalName.trim()}).eq("id",context.hospitalId);
    setSavingHospital(false);
    if(error){showToast("ERROR",error.message,"CRITICAL");return;}
    if(onContextUpdate)onContextUpdate({...context,hospitalName:hospitalName.trim()});
    showToast("SAVED","Hospital name updated. Refresh to see it in the header.");
  };

  const saveProfile=async()=>{
    if(!user)return;
    setSavingProfile(true);
    const{error}=await supabase.from("profiles").upsert({id:user.id,name:displayName.trim()||null,hospital_id:context?.hospitalId,role:profile?.role||"admin"});
    setSavingProfile(false);
    if(error){showToast("ERROR",error.message,"CRITICAL");return;}
    showToast("SAVED","Display name updated.");
  };

  const changePassword=async()=>{
    if(!pwCurrent||!pwNew||!pwConfirm){showToast("ERROR","Fill all three password fields","CRITICAL");return;}
    if(pwNew.length<6){showToast("ERROR","New password must be at least 6 characters","CRITICAL");return;}
    if(pwNew!==pwConfirm){showToast("ERROR","New password and confirmation do not match","CRITICAL");return;}
    if(pwNew===pwCurrent){showToast("ERROR","New password must differ from current","CRITICAL");return;}
    setPwBusy(true);
    const{error}=await supabase.auth.updateUser({password:pwNew});
    setPwBusy(false);
    if(error){showToast("ERROR",error.message,"CRITICAL");return;}
    setPwCurrent("");setPwNew("");setPwConfirm("");
    showToast("SAVED","Password changed successfully. Use the new password next time you sign in.");
  };

  const memberSince=user?.created_at?new Date(user.created_at).toLocaleDateString("en-IN",{year:"numeric",month:"long",day:"numeric"}):"—";

  return (
    <div>
      {toast&&<div style={{position:"fixed",top:80,right:16,zIndex:999,maxWidth:360,background:toast.sev==="CRITICAL"?T.redD:T.greenD,border:`1px solid ${toast.sev==="CRITICAL"?T.red:T.green}50`,borderRadius:10,padding:"12px 16px",boxShadow:"0 8px 32px rgba(0,0,0,0.5)"}}>
        <div style={{fontSize:12,fontWeight:700,marginBottom:4,color:toast.sev==="CRITICAL"?T.red:T.green}}>{toast.sev==="CRITICAL"?"🚨":"✅"} {toast.type}</div>
        <div style={{fontSize:13,color:T.text,lineHeight:1.5}}>{toast.msg}</div>
      </div>}

      <div style={{display:"grid",gap:14}}>
        {/* Account info */}
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{display:"flex",gap:14,alignItems:"center",marginBottom:14}}>
            <div style={{width:48,height:48,borderRadius:"50%",background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:22,flexShrink:0}}>👤</div>
            <div style={{flex:1}}>
              <div style={{fontSize:11,letterSpacing:2,color:T.gold,marginBottom:2}}>ACCOUNT</div>
              <div style={{fontSize:16,fontWeight:700,color:T.white}}>{user?.email}</div>
            </div>
          </div>
          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:14,fontSize:13}}>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:3}}>MEMBER SINCE</div><div style={{color:T.text}}>{memberSince}</div></div>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:3}}>ROLE</div><div style={{color:T.text}}>{profile?.role||"admin"}</div></div>
          </div>
        </div>

        {/* Hospital + Display name */}
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{fontSize:11,letterSpacing:2,color:T.gold,marginBottom:12}}>YOUR HOSPITAL & DISPLAY NAME</div>
          <div style={{display:"grid",gap:12}}>
            <div>
              <div style={{fontSize:11,color:T.muted,marginBottom:5}}>HOSPITAL NAME — shown in app header and reports</div>
              <div style={{display:"flex",gap:8}}>
                <input value={hospitalName} onChange={e=>setHospitalName(e.target.value)} placeholder="e.g., HMP Foundation, Ankleshwar" style={{flex:1,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
                <button onClick={saveHospital} disabled={savingHospital||hospitalName===context?.hospitalName} style={{padding:"7px 16px",borderRadius:8,border:`1px solid ${T.gold}40`,background:T.goldD,color:T.gold,fontSize:13,fontWeight:700,cursor:savingHospital||hospitalName===context?.hospitalName?"not-allowed":"pointer",opacity:savingHospital||hospitalName===context?.hospitalName?0.5:1}}>{savingHospital?"Saving…":"Save"}</button>
              </div>
            </div>
            <div>
              <div style={{fontSize:11,color:T.muted,marginBottom:5}}>YOUR DISPLAY NAME — optional, used in audit logs</div>
              <div style={{display:"flex",gap:8}}>
                <input value={displayName} onChange={e=>setDisplayName(e.target.value)} placeholder="e.g., Dr. Mehul Upadhyay" style={{flex:1,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
                <button onClick={saveProfile} disabled={savingProfile} style={{padding:"7px 16px",borderRadius:8,border:`1px solid ${T.gold}40`,background:T.goldD,color:T.gold,fontSize:13,fontWeight:700,cursor:savingProfile?"not-allowed":"pointer",opacity:savingProfile?0.5:1}}>{savingProfile?"Saving…":"Save"}</button>
              </div>
            </div>
          </div>
        </div>

        {/* Change password */}
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{fontSize:11,letterSpacing:2,color:T.gold,marginBottom:12}}>🔒 CHANGE PASSWORD</div>
          <div style={{display:"grid",gap:10}}>
            <div>
              <div style={{fontSize:11,color:T.muted,marginBottom:4}}>CURRENT PASSWORD</div>
              <input type="password" value={pwCurrent} onChange={e=>setPwCurrent(e.target.value)} autoComplete="current-password" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
            </div>
            <div>
              <div style={{fontSize:11,color:T.muted,marginBottom:4}}>NEW PASSWORD (min 6 characters)</div>
              <input type="password" value={pwNew} onChange={e=>setPwNew(e.target.value)} autoComplete="new-password" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
            </div>
            <div>
              <div style={{fontSize:11,color:T.muted,marginBottom:4}}>CONFIRM NEW PASSWORD</div>
              <input type="password" value={pwConfirm} onChange={e=>setPwConfirm(e.target.value)} autoComplete="new-password" style={{width:"100%",padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
            </div>
            <button onClick={changePassword} disabled={pwBusy} style={{padding:"9px 16px",borderRadius:8,border:`1px solid ${T.gold}40`,background:T.goldD,color:T.gold,fontSize:13,fontWeight:700,cursor:pwBusy?"not-allowed":"pointer",opacity:pwBusy?0.5:1,marginTop:4}}>{pwBusy?"Updating…":"Update Password"}</button>
            <div style={{fontSize:11,color:T.muted,lineHeight:1.5,marginTop:2}}>You will stay signed in after change. Use the new password next time you sign in on any device.</div>
          </div>
        </div>

        {/* Sign out */}
        <div style={{background:T.panel,border:`1px solid ${T.red}30`,borderRadius:10,padding:"14px 18px",display:"flex",justifyContent:"space-between",alignItems:"center",gap:12,flexWrap:"wrap"}}>
          <div>
            <div style={{fontSize:13,fontWeight:700,color:T.red,marginBottom:3}}>Sign out</div>
            <div style={{fontSize:12,color:T.muted}}>End your current session on this device.</div>
          </div>
          <button onClick={()=>supabase.auth.signOut()} style={{padding:"7px 18px",borderRadius:8,border:`1px solid ${T.red}50`,background:T.redD,color:T.red,fontSize:13,fontWeight:700,cursor:"pointer"}}>Sign out</button>
        </div>
      </div>
    </div>
  );
}

// ── PASSWORD RECOVERY ──────────────────────────────────
function RecoveryScreen({ user, onDone }) {
  const [pwNew,setPwNew]=useState("");
  const [pwConfirm,setPwConfirm]=useState("");
  const [busy,setBusy]=useState(false);
  const [err,setErr]=useState("");
  const [done,setDone]=useState(false);

  const submit=async()=>{
    setErr("");
    if(!pwNew||!pwConfirm){setErr("Fill both password fields.");return;}
    if(pwNew.length<6){setErr("Password must be at least 6 characters.");return;}
    if(pwNew!==pwConfirm){setErr("Passwords do not match.");return;}
    setBusy(true);
    const{error}=await supabase.auth.updateUser({password:pwNew});
    setBusy(false);
    if(error){setErr(error.message);return;}
    setDone(true);
  };

  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif",padding:"20px"}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:14,padding:"28px 32px",maxWidth:420,width:"100%"}}>
        <div style={{display:"flex",gap:12,alignItems:"center",marginBottom:18}}>
          <div style={{width:42,height:42,borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:20}}>🔐</div>
          <div>
            <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:2}}>NABH 6TH EDITION</div>
            <div style={{fontSize:15,fontWeight:700,color:T.white}}>Set New Password</div>
          </div>
        </div>

        {!done ? (
          <>
            <div style={{fontSize:13,color:T.text,lineHeight:1.6,marginBottom:18,padding:"10px 12px",background:T.panel2,borderRadius:8,border:`1px solid ${T.border}`}}>
              You arrived here via a password reset link for <strong style={{color:T.gold}}>{user?.email||"your account"}</strong>. Set your new password below.
            </div>

            <div style={{display:"grid",gap:12}}>
              <div>
                <div style={{fontSize:11,color:T.muted,marginBottom:5,letterSpacing:1}}>NEW PASSWORD (min 6 characters)</div>
                <input type="password" value={pwNew} onChange={e=>setPwNew(e.target.value)} autoFocus autoComplete="new-password" style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15}}/>
              </div>
              <div>
                <div style={{fontSize:11,color:T.muted,marginBottom:5,letterSpacing:1}}>CONFIRM NEW PASSWORD</div>
                <input type="password" value={pwConfirm} onChange={e=>setPwConfirm(e.target.value)} onKeyDown={e=>{if(e.key==="Enter")submit();}} autoComplete="new-password" style={{width:"100%",padding:"9px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15}}/>
              </div>

              {err&&<div style={{padding:"8px 12px",background:T.redD,border:`1px solid ${T.red}40`,borderRadius:7,color:T.red,fontSize:13}}>⚠️ {err}</div>}

              <button onClick={submit} disabled={busy} style={{padding:"11px 16px",borderRadius:8,border:`1px solid ${T.gold}`,background:`linear-gradient(135deg,${T.gold},#f0d070)`,color:T.bg,fontSize:14,fontWeight:800,cursor:busy?"not-allowed":"pointer",opacity:busy?0.6:1,marginTop:4}}>{busy?"Updating…":"Set Password & Continue"}</button>
            </div>

            <div style={{marginTop:18,paddingTop:14,borderTop:`1px solid ${T.border}`,fontSize:12,color:T.muted,textAlign:"center"}}>
              Didn't request this? <button onClick={async()=>{await supabase.auth.signOut();window.location.reload();}} style={{background:"transparent",border:"none",color:T.blue,fontSize:12,cursor:"pointer",textDecoration:"underline",padding:0}}>Cancel and sign out</button>
            </div>
          </>
        ) : (
          <div style={{textAlign:"center",padding:"20px 0"}}>
            <div style={{fontSize:36,marginBottom:10}}>✅</div>
            <div style={{fontSize:16,color:T.green,fontWeight:700,marginBottom:6}}>Password Updated</div>
            <div style={{fontSize:13,color:T.text,lineHeight:1.6,marginBottom:18}}>Your password has been set. Sign in with your new password to continue.</div>
            <button onClick={async()=>{await supabase.auth.signOut();if(onDone)onDone();}} style={{padding:"10px 28px",borderRadius:8,border:`1px solid ${T.gold}`,background:T.goldD,color:T.gold,fontSize:14,fontWeight:700,cursor:"pointer"}}>Continue to Sign In</button>
          </div>
        )}
      </div>
    </div>
  );
}

// ── ROOT APP ──────────────────────────────────────────
export default function App() {
  const [authState,setAuthState]=useState("loading");
  const [user,setUser]=useState(null);
  const [context,setContext]=useState(null);
  const [screen,setScreen]=useState("dashboard");
  const [decision,setDecision]=useState({});
  const [gaps,setGaps]=useState([]);
  const [oes,setOes]=useState([]);
  const [standards,setStandards]=useState([]);
  const [loading,setLoading]=useState(false);
  const [selectedProgramme, setSelectedProgramme] = useState("hco");
  const [shcoMode, setShcoMode] = useState('elc');
  const [shcoElcTab, setShcoElcTab] = useState('overview');
  const [shcoElcProgress, setShcoElcProgress] = useState({});
  const [shcoLicProgress, setShcoLicProgress] = useState({});
  const [shcoBeds, setShcoBeds] = useState('');
  const [shcoDocFilter, setShcoDocFilter] = useState('all');
  const [shcoDocPart, setShcoDocPart] = useState('all');
  const [hcoMode, setHcoMode] = useState('elc');
  const [hcoElcTab, setHcoElcTab] = useState('overview');
  const [hcoElcProgress, setHcoElcProgress] = useState({});
  const [hcoLicProgress, setHcoLicProgress] = useState({});
  const [hcoDocFilter, setHcoDocFilter] = useState('all');
  const [hcoDocPart, setHcoDocPart] = useState('all');
  const [pdfLoading, setPdfLoading] = useState(false);
  const [showMoreMenu, setShowMoreMenu] = useState(false);
  const [theme, setTheme] = useState('dark');

  // Reassign module-level T so all component closures see the correct theme
  T = theme === 'light' ? LIGHT_THEME : DARK_THEME;

  const toggleTheme = async () => {
    const next = theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    if (user?.id) {
      await supabase.from("profiles").upsert({ id: user.id, theme_preference: next }, { onConflict: "id" });
    }
  };

  const generatePDF = async () => {
    setPdfLoading(true);
    try {
      const doc = new jsPDF({ unit:'pt', format:'a4' });
      const W = doc.internal.pageSize.getWidth();
      const H = doc.internal.pageSize.getHeight();
      const today = new Date();
      const dateStr = today.toLocaleDateString('en-IN',{day:'2-digit',month:'long',year:'numeric'});
      const fileDateStr = String(today.getDate()).padStart(2,'0')+String(today.getMonth()+1).padStart(2,'0')+today.getFullYear();
      const cleanHospital=(context?.hospitalName||'Hospital').replace(/\s+(New|Trial|Active|Expired)$/i,'').trim();
      const assessmentName=context?.assessmentName||'';

      // ── PAGE 1: COVER ───────────────────────────────────────────────────
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor('#c9a84c'); doc.rect(0,0,W,6,'F');

      doc.setFontSize(9); doc.setTextColor('#c9a84c');
      doc.text('ACCREDREADY - NABH 6TH EDITION',W/2,60,{align:'center'});
      doc.setFontSize(28); doc.setTextColor('#eef4f9');
      doc.text('NABH Compliance Gap Report',W/2,110,{align:'center'});
      doc.setDrawColor('#c9a84c'); doc.setLineWidth(0.5);
      doc.line(60,128,W-60,128);

      doc.setFontSize(22); doc.setTextColor('#c9a84c');
      doc.text(cleanHospital,W/2,165,{align:'center'});
      doc.setFontSize(11); doc.setTextColor('#c8dcea');
      doc.text(assessmentName,W/2,188,{align:'center'});
      doc.setFontSize(9); doc.setTextColor('#3a5870');
      doc.text(`Generated on ${dateStr}`,W/2,208,{align:'center'});

      const oePct=decision.overall_pct||0;
      const verdict=decision.verdict||'-';
      const readiness=decision.readiness||'NOT READY';
      const scoreCol=oePct>=80?'#4caf7d':oePct>=60?'#f4a441':'#e05a5a';
      const verdictCol=verdict==='PASS'?'#4caf7d':verdict==='FAIL'?'#e05a5a':verdict==='PARTIAL'?'#f4a441':'#4fc3f7';
      const rdCol=readiness==='READY'?'#4caf7d':readiness==='RISKY'?'#f4a441':'#e05a5a';

      doc.setFontSize(72); doc.setTextColor(scoreCol);
      doc.text(`${oePct}%`,W/2,306,{align:'center'});
      doc.setFontSize(11); doc.setTextColor('#c8dcea');
      doc.text('OVERALL COMPLIANCE',W/2,328,{align:'center'});
      doc.setFontSize(20); doc.setTextColor(verdictCol);
      doc.text(`VERDICT: ${verdict}`,W/2,366,{align:'center'});
      doc.setFontSize(14); doc.setTextColor(rdCol);
      doc.text(`READINESS: ${readiness}`,W/2,390,{align:'center'});
      doc.setFontSize(9); doc.setTextColor('#c8dcea');
      doc.text(`Scored OEs: ${decision.scored_count||0} / ${decision.total_oes||639}`,W/2-110,424,{align:'center'});
      doc.text(`Active Gaps: ${(gaps||[]).length}`,W/2,424,{align:'center'});
      doc.text(`Core Pass: ${decision.rule1_core?'YES':'NO'}`,W/2+110,424,{align:'center'});
      doc.setFontSize(7); doc.setTextColor('#3a5870');
      doc.text('Generated by accredready.in - Independent educational tool - Not affiliated with NABH/QCI',W/2,H-30,{align:'center'});

      // ── PAGE 2: COMPLIANCE STATUS ───────────────────────────────────────
      doc.addPage();
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');

      let y=50;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Compliance Status',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.setLineWidth(0.5);
      doc.line(60,y,W-60,y); y+=26;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text('ACCREDITATION RULES',60,y); y+=18;

      [
        ['Rule 1 - CORE OEs','All CORE objective elements must score >= 4',decision.rule1_core],
        ['Rule 2 - Overall >= 80%','Overall OE compliance must be 80% or above',decision.rule2_overall],
        ['Rule 3 - Chapter averages','Every chapter must average 80% or above',decision.rule3_chapters],
        ['Rule 4 - No OE <= 2','No individual OE may score 2 or below',decision.rule4_standards],
      ].forEach(([name,desc,pass])=>{
        doc.setFillColor(pass?'#081f10':'#1f0808');
        doc.roundedRect(60,y-14,W-120,30,3,3,'F');
        doc.setFontSize(10); doc.setTextColor('#eef4f9');
        doc.text(name,76,y-2);
        doc.setFontSize(8); doc.setTextColor('#c8dcea');
        doc.text(desc,76,y+10);
        doc.setFillColor(pass?'#4caf7d':'#e05a5a');
        doc.roundedRect(W-102,y-7,38,15,3,3,'F');
        doc.setFontSize(8); doc.setTextColor('#050e1a');
        doc.text(pass?'PASS':'FAIL',W-83,y+3,{align:'center'});
        y+=38;
      });

      y+=12;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text('CHAPTER-WISE SCORES',60,y); y+=18;

      const chapterNames={
        AAC:'Access, Assessment & Continuity of Care',COP:'Care of Patients',
        MOM:'Management of Medications',PRE:'Pre-Operative Management',
        IPC:'Infection Prevention & Control',PSQ:'Patient Safety & Quality Improvement',
        ROM:'Responsibilities of Management',FMS:'Facility Management & Safety',
        HRM:'Human Resource Management',IMS:'Information Management System',
      };
      const breakdown=decision.chapter_breakdown||{};

      doc.setFillColor('#081525'); doc.rect(60,y-13,W-120,19,'F');
      doc.setFontSize(8); doc.setTextColor('#c9a84c');
      doc.text('CH',74,y-2); doc.text('CHAPTER NAME',116,y-2);
      doc.text('SCORE',W-138,y-2); doc.text('STATUS',W-86,y-2);
      y+=12;

      Object.entries(breakdown)
        .sort(([a],[b])=>(CHAPTER_ORDER[a]||99)-(CHAPTER_ORDER[b]||99))
        .forEach(([ch,data])=>{
          const pct=typeof data==='number'?data:(data?.pct||0);
          const pass=pct>=80;
          const rowCol=pass?'#081f10':pct>=60?'#151208':'#1f0808';
          const scoreC=pass?'#4caf7d':pct>=60?'#f4a441':'#e05a5a';
          doc.setFillColor(rowCol); doc.rect(60,y-12,W-120,20,'F');
          doc.setFontSize(9); doc.setTextColor(chColor[ch]||'#c9a84c');
          doc.text(ch,74,y-1);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text((chapterNames[ch]||ch).slice(0,42),116,y-1);
          doc.setFontSize(10); doc.setTextColor(scoreC);
          doc.text(`${pct}%`,W-138,y-1);
          doc.setFontSize(8); doc.setTextColor(scoreC);
          doc.text(pass?'PASS':'FAIL',W-86,y-1);
          y+=22;
        });

      // ── PAGE 3: GAP ANALYSIS ────────────────────────────────────────────
      doc.addPage();
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');

      y=50;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Gap Analysis',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=20;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text('ACTIVE GAPS REQUIRING ATTENTION',60,y); y+=20;

      const drawGapHeader=(atY)=>{
        doc.setFillColor('#081525'); doc.rect(60,atY-13,W-120,19,'F');
        doc.setFontSize(8); doc.setTextColor('#c9a84c');
        doc.text('OE CODE',74,atY-2); doc.text('STANDARD',148,atY-2);
        doc.text('DESCRIPTION',218,atY-2); doc.text('SEV',W-116,atY-2); doc.text('SC',W-76,atY-2);
        return atY+12;
      };

      const gapsToShow=(gaps||[]).slice(0,50);
      if(gapsToShow.length===0){
        doc.setFontSize(11); doc.setTextColor('#3a5870');
        doc.text('No active gaps recorded.',W/2,y+40,{align:'center'});
      } else {
        y=drawGapHeader(y);
        gapsToShow.forEach(g=>{
          if(y>H-70){
            doc.addPage();
            doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
            doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');
            y=40; y=drawGapHeader(y);
          }
          const sevC=g.severity==='CRITICAL'?'#e05a5a':g.severity==='HIGH'?'#f4a441':g.severity==='MEDIUM'?'#c9a84c':'#3a5870';
          const rowBg=g.severity==='CRITICAL'?'#1a0808':g.severity==='HIGH'?'#1a0f00':'#081525';
          doc.setFillColor(rowBg); doc.rect(60,y-11,W-120,19,'F');
          doc.setFontSize(8); doc.setTextColor('#4fc3f7');
          doc.text((g.oe_id||'').slice(0,14),74,y-1);
          doc.setTextColor('#c8dcea');
          doc.text((g.standard_id||'').slice(0,10),148,y-1);
          doc.text((g.oe_text||'').slice(0,42),218,y-1);
          doc.setTextColor(sevC);
          doc.text((g.severity||'').slice(0,8),W-116,y-1);
          const sc=g.score<=2?'#e05a5a':g.score===3?'#f4a441':'#4caf7d';
          doc.setFontSize(9); doc.setTextColor(sc);
          doc.text(String(g.score||'-'),W-68,y-1,{align:'right'});
          y+=21;
        });
      }

      // ── PAGE 4: SUMMARY ─────────────────────────────────────────────────
      doc.addPage();
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');

      y=60;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Report Summary',60,y); y+=36;

      const gl=gaps||[];
      [
        ['Total Active Gaps',  String(gl.length),                                    '#c9a84c'],
        ['Critical',           String(gl.filter(g=>g.severity==='CRITICAL').length),  '#e05a5a'],
        ['High',               String(gl.filter(g=>g.severity==='HIGH').length),      '#f4a441'],
        ['Medium',             String(gl.filter(g=>g.severity==='MEDIUM').length),    '#c9a84c'],
        ['Low',                String(gl.filter(g=>g.severity==='LOW').length),       '#3a5870'],
      ].forEach(([label,val,col])=>{
        doc.setFillColor('#081525'); doc.roundedRect(60,y-15,W-120,30,4,4,'F');
        doc.setFontSize(11); doc.setTextColor('#c8dcea');
        doc.text(label,80,y);
        doc.setFontSize(18); doc.setTextColor(col);
        doc.text(val,W-80,y,{align:'right'});
        y+=38;
      });

      y+=16;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=24;
      doc.setFontSize(9); doc.setTextColor('#3a5870');
      doc.text(`Report generated on ${dateStr} via accredready.in`,W/2,y,{align:'center'}); y+=18;
      doc.text('This report is based on self-assessment scores entered by the hospital team.',W/2,y,{align:'center'}); y+=14;
      doc.text('It is not an official NABH assessment and should not be used as a substitute for formal evaluation.',W/2,y,{align:'center'});

      // Page numbers on all pages
      const nPages=doc.internal.getNumberOfPages();
      for(let i=1;i<=nPages;i++){
        doc.setPage(i);
        doc.setFontSize(7); doc.setTextColor('#3a5870');
        doc.text(`Page ${i} of ${nPages}`,W-60,H-18,{align:'right'});
        if(i>1) doc.text('NABH Compliance Engine - accredready.in',60,H-18);
      }

      const cleanName=cleanHospital.replace(/[^a-zA-Z0-9]/g,'_');
      doc.save(`${cleanName}_NABH_Gap_Report_${fileDateStr}.pdf`);
    } catch(e){ console.error('PDF generation failed:',e); }
    setPdfLoading(false);
  };

  const [authErrorMsg,setAuthErrorMsg]=useState("");

  useEffect(()=>{
    // Detect auth error fragment in URL (e.g., expired/invalid recovery link)
    // This MUST run before any session check — an expired link with an active session
    // would otherwise silently land on dashboard, hiding the error from the user.
    const hash=window.location.hash;
    if(hash&&hash.includes("error=")){
      const params=new URLSearchParams(hash.slice(1));
      const code=params.get("error_code");
      const desc=params.get("error_description")||"";
      let msg="";
      if(code==="otp_expired"||desc.toLowerCase().includes("expired")){
        msg="⏱️ Your password reset link has expired. Click 'Forgot password?' below to request a new one — and use it within 1 hour of receiving the email.";
      }else if(code==="access_denied"){
        msg="⚠️ This link is invalid or already used. Click 'Forgot password?' below to request a fresh reset email.";
      }else if(desc){
        msg=decodeURIComponent(desc.replace(/\+/g," "));
      }
      if(msg){
        setAuthErrorMsg(msg);
        window.history.replaceState(null,"",window.location.pathname);
        // Force sign-out so the LoginScreen actually renders with our banner
        supabase.auth.signOut().then(()=>{setUser(null);setAuthState("login");setContext(null);});
        return; // Skip the normal session check
      }
    }
    // Check for token_hash + type=recovery in query params (Supabase email template sends SiteURL?token_hash=...&type=recovery)
    const urlParams=new URLSearchParams(window.location.search);
    const tokenHash=urlParams.get("token_hash");
    const urlType=urlParams.get("type");
    const isRecoveryLink=tokenHash&&urlType==="recovery";
    if(isRecoveryLink){
      window.history.replaceState(null,"",window.location.pathname);
      supabase.auth.verifyOtp({token_hash:tokenHash,type:"recovery"}).then(({data,error})=>{
        if(error){setAuthErrorMsg("⚠️ Password reset link is invalid or expired. Request a new one.");setAuthState("login");}
        else{if(data?.user)setUser(data.user);setAuthState("recovery");}
      });
      return;
    }
    supabase.auth.getSession().then(({data:{session}})=>{
      if(session?.user){setUser(session.user);setAuthState("setup");}
      else setAuthState("login");
    });
    const{data:{subscription}}=supabase.auth.onAuthStateChange((event,session)=>{
      if(event==="PASSWORD_RECOVERY"){
        if(session?.user)setUser(session.user);
        setAuthState("recovery");
        return;
      }
      if(session?.user){setUser(session.user);setAuthState(s=>s==="recovery"?s:s==="loading"?"setup":s);}
      else{setUser(null);setAuthState("login");setContext(null);}
    });
    return()=>subscription.unsubscribe();
  },[]);

  // Load theme preference when user logs in
  useEffect(()=>{
    if(!user?.id)return;
    supabase.from("profiles").select("theme_preference").eq("id",user.id).maybeSingle()
      .then(({data})=>{if(data?.theme_preference)setTheme(data.theme_preference);});
  },[user?.id]);

  // Load SHCO ELC progress from DB when entering that programme
  useEffect(()=>{
    if(selectedProgramme!=="shco-elc"||!context?.assessmentId)return;
    supabase.from("shco_elc_progress")
      .select("doc_progress,lic_progress")
      .eq("assessment_id",context.assessmentId)
      .maybeSingle()
      .then(({data})=>{
        if(data?.doc_progress)setShcoElcProgress(data.doc_progress);
        if(data?.lic_progress)setShcoLicProgress(data.lic_progress);
      });
  },[selectedProgramme,context?.assessmentId]);

  // Persist doc progress whenever it changes
  useEffect(()=>{
    if(selectedProgramme!=="shco-elc"||!context?.assessmentId||Object.keys(shcoElcProgress).length===0)return;
    supabase.from("shco_elc_progress")
      .upsert({assessment_id:context.assessmentId,doc_progress:shcoElcProgress},{onConflict:"assessment_id"});
  },[shcoElcProgress]);// eslint-disable-line react-hooks/exhaustive-deps

  // Persist lic progress whenever it changes
  useEffect(()=>{
    if(selectedProgramme!=="shco-elc"||!context?.assessmentId||Object.keys(shcoLicProgress).length===0)return;
    supabase.from("shco_elc_progress")
      .upsert({assessment_id:context.assessmentId,lic_progress:shcoLicProgress},{onConflict:"assessment_id"});
  },[shcoLicProgress]);// eslint-disable-line react-hooks/exhaustive-deps

  // Load HCO ELC progress from DB when entering that programme
  useEffect(()=>{
    if(selectedProgramme!=="hco-elc"||!context?.assessmentId)return;
    supabase.from("hco_elc_progress")
      .select("doc_progress,lic_progress")
      .eq("assessment_id",context.assessmentId)
      .maybeSingle()
      .then(({data})=>{
        if(data?.doc_progress)setHcoElcProgress(data.doc_progress);
        if(data?.lic_progress)setHcoLicProgress(data.lic_progress);
      });
  },[selectedProgramme,context?.assessmentId]);

  // Persist HCO doc progress whenever it changes
  useEffect(()=>{
    if(selectedProgramme!=="hco-elc"||!context?.assessmentId||Object.keys(hcoElcProgress).length===0)return;
    supabase.from("hco_elc_progress")
      .upsert({assessment_id:context.assessmentId,doc_progress:hcoElcProgress},{onConflict:"assessment_id"});
  },[hcoElcProgress]);// eslint-disable-line react-hooks/exhaustive-deps

  // Persist HCO lic progress whenever it changes
  useEffect(()=>{
    if(selectedProgramme!=="hco-elc"||!context?.assessmentId||Object.keys(hcoLicProgress).length===0)return;
    supabase.from("hco_elc_progress")
      .upsert({assessment_id:context.assessmentId,lic_progress:hcoLicProgress},{onConflict:"assessment_id"});
  },[hcoLicProgress]);// eslint-disable-line react-hooks/exhaustive-deps

  // Close ••• dropdown on outside click
  useEffect(()=>{
    if(!showMoreMenu)return;
    const handler=()=>setShowMoreMenu(false);
    document.addEventListener("click",handler);
    return()=>document.removeEventListener("click",handler);
  },[showMoreMenu]);

  const loadData=useCallback(async(ctx)=>{
    if(!ctx?.assessmentId)return;
    setLoading(true);const aid=ctx.assessmentId;
    const{data:dec}=await supabase.rpc("get_final_decision",{param_id:aid});if(dec)setDecision(dec);
    const{data:gapsData}=await supabase.rpc("get_active_gaps",{param_id:aid});setGaps(gapsData||[]);
    const{data:stdsData}=await supabase.from("standards").select("id, chapter_id, title").order("id");
    if(stdsData)setStandards(stdsData);
    const{data:oesData}=await supabase.from("objective_elements").select("id, chapter_id, level, text, doc_required, standard_id, achieve_tips").order("chapter_id");
    if(oesData){
      const{data:scoresData}=await supabase.from("scores").select("oe_id, score, evidence_links").eq("assessment_id",aid);
      const scoreMap={};const linksMap={};(scoresData||[]).forEach(s=>{scoreMap[s.oe_id]=s.score;linksMap[s.oe_id]=s.evidence_links||[];});
      const sorted=oesData.sort((a,b)=>{
        if(a.chapter_id!==b.chapter_id){
          const orderA=CHAPTER_ORDER[a.chapter_id]||999;
          const orderB=CHAPTER_ORDER[b.chapter_id]||999;
          return orderA-orderB;
        }
        return a.id.localeCompare(b.id,undefined,{numeric:true,sensitivity:"base"});
      });
      setOes(sorted.map(oe=>({id:oe.id,chapter:oe.chapter_id,level:oe.level,text:oe.text,doc:oe.doc_required,standard:oe.standard_id,achieveTips:oe.achieve_tips||null,score:scoreMap[oe.id]||null,evidenceLinks:linksMap[oe.id]||[]})));
    }
    setLoading(false);
  },[]);

  const handleReady=(ctx)=>{setContext(ctx);setAuthState("programme");};
  const handleSignOut=async()=>{await supabase.auth.signOut();};
  const handleProgrammeSelect=(key,ctx)=>{
    const resolvedCtx=ctx||context;
    if(key==="hco_full"){setSelectedProgramme("hco");setScreen("dashboard");setAuthState("app");loadData(resolvedCtx);}
    else if(key==="shco_elc"){setSelectedProgramme("shco-elc");setScreen("shco");setAuthState("app");}
    else if(key==="hco_elc"){setSelectedProgramme("hco-elc");setScreen("hco-elc");setAuthState("app");}
  };

  if(authState==="loading") return <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",color:T.gold,fontFamily:"Segoe UI,sans-serif",fontSize:16}}>Loading…</div>;
  if(authState==="recovery") return <RecoveryScreen user={user} onDone={()=>{setUser(null);setAuthState("login");setContext(null);}}/>;
  if(authState==="login") return <LoginScreen onLogin={u=>{setUser(u);setAuthState("setup");}} initialError={authErrorMsg}/>;
  if(authState==="setup") return <SetupScreen user={user} onReady={handleReady}/>;
  if(authState==="programme") return <ProgrammeSelector user={user} ctx={context} onSelect={handleProgrammeSelect}/>;

  const readinessColor=decision.readiness==="NOT READY"?T.red:decision.readiness==="RISKY"?T.orange:T.green;
  const verdictColor=decision.verdict==="FAIL"?T.red:decision.verdict==="PASS"?T.green:decision.verdict==="PARTIAL"?T.orange:T.blue;

  const renderSHCOTab = () => {

  // ── Fee Calculator Logic ──
  const calcFee = (beds) => {
    const n = parseInt(beds);
    if (!n || n < 1 || n > 50) return null;
    const slab = SHCO_FEE_SLABS.find(s => n >= s.beds[0] && n <= s.beds[1]);
    if (!slab) return null;
    const base = slab.discounted || slab.fee;
    const gst = Math.round(base * 0.18);
    const total = base + gst;
    const savingVsOriginal = slab.discounted ? (slab.fee - slab.discounted) : 0;
    return { slab, base, gst, total, savingVsOriginal };
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
      <span style={{fontSize:12,padding:'2px 6px',borderRadius:10,background:color+'22',color,border:`1px solid ${color}44`,whiteSpace:'nowrap'}}>
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
        <div style={{color:T.text,fontSize:15,lineHeight:1.6}}>
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
              <div style={{color:T.muted,fontSize:13}}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>

      {/* ELC 2nd Edition OE Summary */}
      <div style={{color:T.blue,fontWeight:600,fontSize:15,marginBottom:10}}>ELC 2nd Edition — 189 OEs (Entry Level reference)</div>
      <div style={{display:'grid',gap:6,marginBottom:20}}>
        {SHCO_ELC_OE_SUMMARY.map(c => (
          <div key={c.ch} style={{background:T.panel,borderRadius:8,padding:'8px 12px',border:`1px solid ${T.border}`}}>
            <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:4}}>
              <div>
                <span style={{color:T.gold,fontWeight:700,fontSize:13,marginRight:6}}>{c.ch}</span>
                <span style={{color:T.text,fontSize:13}}>{c.name}</span>
              </div>
              <span style={{color:T.blue,fontSize:13,fontWeight:600}}>{c.oes} OEs</span>
            </div>
            <div style={{display:'flex',gap:6,flexWrap:'wrap'}}>
              <span style={{fontSize:12,padding:'1px 6px',borderRadius:8,background:T.green+'22',color:T.green}}>Core: {c.core}</span>
              <span style={{fontSize:12,padding:'1px 6px',borderRadius:8,background:T.orange+'22',color:T.orange}}>Commitment: {c.commitment}</span>
              <span style={{fontSize:12,padding:'1px 6px',borderRadius:8,background:T.gold+'22',color:T.gold}}>Excellence: {c.excellence}</span>
            </div>
          </div>
        ))}
        <div style={{color:T.muted,fontSize:13,textAlign:'center',marginTop:4}}>Source: NABH ELC Standards — 2nd Edition (Jan 2026)</div>
      </div>

      {/* Chapter breakdown */}
      <div style={{color:T.gold,fontWeight:600,fontSize:15,marginBottom:10}}>Chapter Breakdown — 3rd Edition</div>
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
              <span style={{color:T.gold,fontWeight:700,fontSize:14,marginRight:8}}>{c.ch}</span>
              <span style={{color:T.text,fontSize:14}}>{c.name}</span>
            </div>
            <div style={{display:'flex',gap:12,fontSize:13}}>
              <span style={{color:T.muted}}>{c.stds} Stds</span>
              <span style={{color:T.blue,fontWeight:600}}>{c.oes} OEs</span>
            </div>
          </div>
        ))}
      </div>

      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.orange}44`}}>
        <div style={{color:T.orange,fontWeight:600,fontSize:15,marginBottom:6}}>⚠️ OE Scoring — Coming Soon</div>
        <div style={{color:T.text,fontSize:14,lineHeight:1.6}}>
          The 408 OEs from the 3rd Edition SHCO standards are ready in the database. OE-level scoring for Full Accreditation will be enabled in the next update.
          <br/><br/>
          To prepare: Score each OE on 1–5 scale. NABH requires all 10 chapters ≥ 80%, no OE ≤ 2, and no chapter below threshold.
        </div>
      </div>
    </div>
  );

  // ── OVERVIEW sub-tab ──
  const renderOverview = () => {
    const feeResult = calcFee(shcoBeds);
    return (
      <div style={{padding:16,display:'flex',flexDirection:'column',gap:16}}>

        {/* 2nd Edition notice */}
        <div style={{background:'#1a0a00',border:`1px solid ${T.orange}`,borderRadius:10,padding:14}}>
          <div style={{color:T.orange,fontWeight:700,fontSize:15,marginBottom:4}}>📋 2nd Edition Active — March 2026</div>
          <div style={{color:T.text,fontSize:14,lineHeight:1.6}}>
            ELC now uses the unified 2nd Edition standards (Jan 2026). New applicants from March 2026 must apply via <strong style={{color:T.gold}}>nabh.qcin.org</strong>.
            1st Edition (149 OEs) is no longer valid for new applications.
          </div>
        </div>

        {/* Readiness Summary */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:14}}>📊 ELC Readiness</div>
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
                  <div style={{position:'absolute',top:'50%',left:'50%',transform:'translate(-50%,-50%)',color:s.color,fontWeight:700,fontSize:16}}>{s.pct}%</div>
                </div>
                <div style={{color:T.text,fontSize:14,fontWeight:600}}>{s.label}</div>
                {s.done !== null && <div style={{color:T.muted,fontSize:12}}>{s.done}/{s.total}</div>}
              </div>
            ))}
          </div>
        </div>

        {/* Fee Calculator */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>💰 Certification Fee Calculator</div>
          <div style={{display:'flex',gap:10,alignItems:'center',marginBottom:12}}>
            <input
              type="number" min="1" max="50" placeholder="Enter bed count (1–50)"
              value={shcoBeds} onChange={e => setShcoBeds(e.target.value)}
              style={{flex:1,padding:'8px 12px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.white,fontSize:15}}
            />
          </div>
          {feeResult ? (
            <div style={{background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
              <div style={{color:T.muted,fontSize:13,marginBottom:8}}>{feeResult.slab.label}</div>
              <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginBottom:10}}>
                <div>
                  <div style={{color:T.muted,fontSize:12}}>Certification Fee</div>
                  <div style={{color:T.gold,fontWeight:700,fontSize:16}}>₹{feeResult.base.toLocaleString('en-IN')}</div>
                  {feeResult.savingVsOriginal > 0 && (
                    <div style={{color:T.green,fontSize:12}}>Saving ₹{feeResult.savingVsOriginal.toLocaleString('en-IN')} (till {feeResult.slab.discountTill})</div>
                  )}
                </div>
                <div>
                  <div style={{color:T.muted,fontSize:12}}>GST (18%)</div>
                  <div style={{color:T.text,fontWeight:600,fontSize:16}}>₹{feeResult.gst.toLocaleString('en-IN')}</div>
                </div>
              </div>
              <div style={{borderTop:`1px solid ${T.border}`,paddingTop:10,display:'flex',justifyContent:'space-between',alignItems:'center'}}>
                <span style={{color:T.white,fontWeight:700,fontSize:15}}>Total Payable</span>
                <span style={{color:T.green,fontWeight:700,fontSize:18}}>₹{feeResult.total.toLocaleString('en-IN')}</span>
              </div>
              <div style={{marginTop:8,fontSize:13,color:T.muted}}>
                Focus assessment: ₹15,000 + GST | Re-issue of certificate: ₹6,000 + GST
              </div>
            </div>
          ) : shcoBeds ? (
            <div style={{color:T.red,fontSize:14}}>ELC is only for SHCOs with 1–50 beds.</div>
          ) : null}
        </div>

        {/* Assessment Matrix */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>📐 What Gets Assessed — By Cycle</div>
          <div style={{display:'grid',gap:8}}>
            {[
              {cycle:'New Applicant — Cycle 1',beds:'1–50 beds',assessed:'Core only (124 OEs)',color:T.green},
              {cycle:'First Renewal — Cycle 2',beds:'1–50 beds',assessed:'Core + Commitment (160 OEs)',color:T.orange},
              {cycle:'Second Renewal+ — Cycle 3',beds:'1–50 beds',assessed:'Core + Commitment + Excellence (189 OEs)',color:T.gold},
              {cycle:'New Applicant — Cycle 1',beds:'51+ beds',assessed:'Core + Commitment (160 OEs)',color:T.blue},
            ].map((r,i) => (
              <div key={i} style={{background:T.panel2,borderRadius:8,padding:'10px 14px',border:`1px solid ${r.color}33`,display:'flex',justifyContent:'space-between',alignItems:'center',flexWrap:'wrap',gap:6}}>
                <div>
                  <div style={{color:r.color,fontWeight:600,fontSize:14}}>{r.cycle}</div>
                  <div style={{color:T.muted,fontSize:13}}>{r.beds}</div>
                </div>
                <div style={{color:T.text,fontSize:14,fontWeight:500}}>{r.assessed}</div>
              </div>
            ))}
          </div>
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
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:13,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>

        {/* Filters */}
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          <select value={shcoDocPart} onChange={e => setShcoDocPart(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}>
            <option value="all">All Parts</option>
            {parts.map(p => <option key={p} value={p}>Part {p}</option>)}
          </select>
          <select value={shcoDocFilter} onChange={e => setShcoDocFilter(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}>
            <option value="all">All Status</option>
            <option value="pending">Pending</option>
            <option value="ready">Ready</option>
            <option value="na">N/A</option>
          </select>
          <div style={{marginLeft:'auto',color:T.muted,fontSize:13,display:'flex',alignItems:'center'}}>{filteredDocs.length} items</div>
        </div>

        {/* Document list grouped by section */}
        {sections.map(sec => {
          const secDocs = filteredDocs.filter(d => d.section === sec);
          if (!secDocs.length) return null;
          return (
            <div key={sec} style={{marginBottom:16}}>
              <div style={{color:T.gold,fontWeight:600,fontSize:14,marginBottom:8,display:'flex',alignItems:'center',gap:8}}>
                <span>Part {secDocs[0].part} — {sec}</span>
                <span style={{color:T.muted,fontWeight:400,fontSize:13}}>({secDocs.length})</span>
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
                        <div style={{color:T.text,fontSize:14,lineHeight:1.5,flex:1}}>
                          <span style={{color:T.muted,fontSize:12,marginRight:6}}>#{doc.id}</span>
                          {doc.text}
                        </div>
                        <div style={{flexShrink:0}}>{uploadBadge(doc.upload)}</div>
                      </div>
                      <div style={{display:'flex',gap:6}}>
                        {['pending','ready','na'].map(status => (
                          <button key={status} onClick={() => setDocStatus(doc.id, status)}
                            style={{
                              padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:13,fontWeight:600,
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
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:13,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>

        {/* Mandatory licenses */}
        <div style={{color:T.red,fontWeight:700,fontSize:15,marginBottom:10}}>🔴 Mandatory Licenses ({mandatory.length})</div>
        <div style={{display:'flex',flexDirection:'column',gap:6,marginBottom:20}}>
          {mandatory.map(lic => {
            const s = licStatus(lic.id);
            return (
              <div key={lic.id} style={{
                background:T.panel,borderRadius:8,padding:'10px 12px',
                border:`1px solid ${s==='obtained'?T.green:T.border}`,
                opacity: s==='na' ? 0.6 : 1
              }}>
                <div style={{color:T.text,fontSize:14,marginBottom:6}}>{lic.name}</div>
                <div style={{display:'flex',gap:6}}>
                  {['pending','obtained','na'].map(status => (
                    <button key={status} onClick={() => setLicStatus(lic.id, status)}
                      style={{
                        padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:13,fontWeight:600,
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
        <div style={{color:T.orange,fontWeight:700,fontSize:15,marginBottom:6}}>⚡ AERB Licenses ({aerb.length}) — Mark N/A if service not available</div>
        <div style={{color:T.muted,fontSize:13,marginBottom:10}}>These are applicable only if your SHCO provides the specific imaging/radiation service.</div>
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
                  <div style={{color:T.text,fontSize:14,flex:1}}>{lic.name}</div>
                  <div style={{color:T.muted,fontSize:12,flexShrink:0,textAlign:'right',maxWidth:120}}>{lic.appl}</div>
                </div>
                <div style={{display:'flex',gap:6}}>
                  {['pending','obtained','na'].map(status => (
                    <button key={status} onClick={() => setLicStatus(lic.id, status)}
                      style={{
                        padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:13,fontWeight:600,
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
        <div style={{color:T.green,fontWeight:600,fontSize:14,marginBottom:4}}>⚠️ Key Change — 2nd Edition</div>
        <div style={{color:T.text,fontSize:14}}>Desktop Assessment now has a <strong>single NC closure cycle only</strong>. There is no second chance to respond. Submit complete NC responses the first time.</div>
      </div>

      <div style={{display:'flex',flexDirection:'column',gap:0}}>
        {SHCO_ELC_PROCESS.map((step, idx) => (
          <div key={step.step} style={{display:'flex',gap:12}}>
            {/* Timeline line */}
            <div style={{display:'flex',flexDirection:'column',alignItems:'center',width:32,flexShrink:0}}>
              <div style={{width:32,height:32,borderRadius:'50%',background:T.gold,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700,fontSize:15,color:T.bg,flexShrink:0}}>
                {step.step}
              </div>
              {idx < SHCO_ELC_PROCESS.length - 1 && (
                <div style={{width:2,flex:1,background:T.border,minHeight:20,margin:'4px 0'}}/>
              )}
            </div>
            {/* Step content */}
            <div style={{background:T.panel,borderRadius:10,padding:'12px 14px',marginBottom:10,flex:1,border:`1px solid ${T.border}`}}>
              <div style={{color:T.white,fontWeight:700,fontSize:15,marginBottom:4}}>{step.name}</div>
              {step.url && (
                <div style={{color:T.blue,fontSize:13,marginBottom:6}}>🔗 {step.url}</div>
              )}
              <div style={{color:T.text,fontSize:14,lineHeight:1.6,marginBottom:6}}>{step.desc}</div>
              <div style={{color:T.muted,fontSize:13}}>📄 Output: <span style={{color:T.gold}}>{step.output}</span></div>
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
        <div style={{color:T.text,fontSize:14,lineHeight:1.7}}>
          Entry Level Certification is the first step. After 2 years, SHCOs can upgrade to Full SHCO Accreditation (3rd Edition) — a significantly more rigorous programme that opens doors to premium empanelments, higher CGHS reimbursements, and community trust.
        </div>
      </div>

      {/* Comparison table */}
      <div style={{color:T.gold,fontWeight:600,fontSize:15,marginBottom:10}}>ELC vs Full Accreditation — Key Differences</div>
      <div style={{overflowX:'auto',marginBottom:16}}>
        <table style={{width:'100%',borderCollapse:'collapse',fontSize:14}}>
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
              ['Fee (6–20 beds)','₹30,000 + GST*','₹40,000 + GST'],
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
        <div style={{color:T.muted,fontSize:12,marginTop:4}}>* Discounted fee till 30 Sep 2026</div>
      </div>

      {/* Upgrade timeline */}
      <div style={{color:T.gold,fontWeight:600,fontSize:15,marginBottom:10}}>Recommended Timeline</div>
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
          <div style={{minWidth:90,color:p.color,fontWeight:600,fontSize:13,paddingTop:2}}>{p.phase}</div>
          <div style={{flex:1,background:T.panel,borderRadius:8,padding:'8px 12px',border:`1px solid ${p.color}33`,color:T.text,fontSize:14}}>{p.action}</div>
        </div>
      ))}

      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:15,marginBottom:6}}>💼 For Consultants (Rajesh Model)</div>
        <div style={{color:T.text,fontSize:14,lineHeight:1.7}}>
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
          {key:'elc', label:'📋 ELC Certification', sub:'Entry Level Certification for SHCO'},
          {key:'full', label:'🏆 Full Accreditation', sub:'Full Accreditation for SHCO'},
        ].map(m => (
          <button key={m.key} onClick={() => setShcoMode(m.key)}
            style={{
              flex:1, padding:'10px 8px', borderRadius:10, border:'none', cursor:'pointer',
              background: shcoMode === m.key ? T.gold+'22' : T.panel,
              outline: shcoMode === m.key ? `2px solid ${T.gold}` : `1px solid ${T.border}`,
              textAlign:'center'
            }}>
            <div style={{color: shcoMode === m.key ? T.gold : T.text, fontWeight:700, fontSize:14}}>{m.label}</div>
            <div style={{color:T.muted, fontSize:12, marginTop:2}}>{m.sub}</div>
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
                  background:'transparent', fontSize:14, fontWeight:600,
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

  // ── HCO ELC TAB ──────────────────────────────────────────────────────────
  const renderHCOTab = () => {

  const gst = Math.round(HCO_FEE.base * HCO_FEE.gstRate);
  const totalFee = HCO_FEE.base + gst;

  const docStatus = (id) => hcoElcProgress[id] || 'pending';
  const licStatus = (id) => hcoLicProgress[id] || 'pending';
  const setDocStatus = (id, status) => setHcoElcProgress(prev => ({ ...prev, [id]: status }));
  const setLicStatus = (id, status) => setHcoLicProgress(prev => ({ ...prev, [id]: status }));

  const docsDone = HCO_ELC_DOCS.filter(d => docStatus(d.id) === 'ready').length;
  const docsNA = HCO_ELC_DOCS.filter(d => docStatus(d.id) === 'na').length;
  const docsApplicable = HCO_ELC_DOCS.length - docsNA;
  const docsPct = docsApplicable > 0 ? Math.round((docsDone / docsApplicable) * 100) : 0;

  const licDone = HCO_ELC_LICENSES.filter(l => licStatus(l.id) === 'obtained').length;
  const licNA = HCO_ELC_LICENSES.filter(l => licStatus(l.id) === 'na').length;
  const licApplicable = HCO_ELC_LICENSES.length - licNA;
  const licPct = licApplicable > 0 ? Math.round((licDone / licApplicable) * 100) : 0;

  const overallPct = Math.round((docsPct + licPct) / 2);

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
      <span style={{fontSize:12,padding:'2px 6px',borderRadius:10,background:color+'22',color,border:`1px solid ${color}44`,whiteSpace:'nowrap'}}>
        {label}
      </span>
    );
  };

  const renderFullAccredTab = () => (
    <div style={{padding:16}}>
      <div style={{background:T.panel,border:`1px solid ${T.gold}44`,borderRadius:12,padding:20,marginBottom:16}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:16,marginBottom:8}}>🏆 NABH Full Hospital Accreditation — 6th Edition</div>
        <div style={{color:T.text,fontSize:15,lineHeight:1.6}}>
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
              <div style={{color:T.muted,fontSize:13}}>{s.label}</div>
            </div>
          ))}
        </div>
      </div>
      <div style={{color:T.gold,fontWeight:600,fontSize:15,marginBottom:10}}>Chapter Breakdown — 6th Edition</div>
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
              <span style={{color:T.gold,fontWeight:700,fontSize:14,marginRight:8}}>{c.ch}</span>
              <span style={{color:T.text,fontSize:14}}>{c.name}</span>
            </div>
            <span style={{color:T.blue,fontWeight:600,fontSize:14}}>{c.oes} OEs</span>
          </div>
        ))}
      </div>
      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.orange}44`}}>
        <div style={{color:T.orange,fontWeight:600,fontSize:15,marginBottom:6}}>⚠️ Key Differences vs ELC</div>
        <div style={{color:T.text,fontSize:14,lineHeight:1.7}}>
          Full accreditation requires implementation of all 639 OEs vs simplified ELC standards. Requires pre-assessment, final assessment + surveillance at 24 months. Validity is 4 years (vs 2 years for ELC).
          Apply via <strong style={{color:T.gold}}>portal.nabh.co</strong> (not HOPE portal). Assessment team is 2–3 assessors vs 1–2 for ELC.
        </div>
      </div>
    </div>
  );

  const renderOverview = () => (
    <div style={{padding:16,display:'flex',flexDirection:'column',gap:16}}>
      <div style={{background:'#0a0a1a',border:`1px solid ${T.blue}`,borderRadius:10,padding:14}}>
        <div style={{color:T.blue,fontWeight:700,fontSize:15,marginBottom:6}}>✅ HCO ELC Eligibility Criteria</div>
        <div style={{display:'flex',flexDirection:'column',gap:6}}>
          {[
            {icon:'🏥',text:'More than 50 sanctioned beds (hospitals with ≤50 beds must apply as SHCO)'},
            {icon:'📅',text:'Organisation must be operational for at least 6 months before applying'},
            {icon:'📊',text:'Average bed occupancy ≥ 30% (calculated over last 6 months)'},
            {icon:'🔄',text:'Must apply for ALL services from the specific location — no partial accreditation'},
            {icon:'📋',text:'Must comply with all applicable NABH standards and laws of the land'},
          ].map((e,i) => (
            <div key={i} style={{display:'flex',gap:8,alignItems:'flex-start'}}>
              <span style={{fontSize:16}}>{e.icon}</span>
              <span style={{color:T.text,fontSize:14,lineHeight:1.5}}>{e.text}</span>
            </div>
          ))}
        </div>
      </div>

      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:14}}>📊 ELC Readiness</div>
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
                <div style={{position:'absolute',top:'50%',left:'50%',transform:'translate(-50%,-50%)',color:s.color,fontWeight:700,fontSize:16}}>{s.pct}%</div>
              </div>
              <div style={{color:T.text,fontSize:14,fontWeight:600}}>{s.label}</div>
              {s.done !== null && <div style={{color:T.muted,fontSize:12}}>{s.done}/{s.total}</div>}
            </div>
          ))}
        </div>
      </div>

      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>💰 HCO ELC Certification Fee</div>
        <div style={{background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
          <div style={{color:T.muted,fontSize:13,marginBottom:10}}>{HCO_FEE.label}</div>
          <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginBottom:10}}>
            <div>
              <div style={{color:T.muted,fontSize:12}}>Certification Fee</div>
              <div style={{color:T.gold,fontWeight:700,fontSize:20}}>₹{HCO_FEE.base.toLocaleString('en-IN')}</div>
            </div>
            <div>
              <div style={{color:T.muted,fontSize:12}}>GST (18%)</div>
              <div style={{color:T.text,fontWeight:600,fontSize:16}}>₹{gst.toLocaleString('en-IN')}</div>
            </div>
          </div>
          <div style={{borderTop:`1px solid ${T.border}`,paddingTop:10,display:'flex',justifyContent:'space-between',alignItems:'center'}}>
            <span style={{color:T.white,fontWeight:700,fontSize:15}}>Total Payable</span>
            <span style={{color:T.green,fontWeight:700,fontSize:20}}>₹{totalFee.toLocaleString('en-IN')}</span>
          </div>
          <div style={{marginTop:8,fontSize:13,color:T.muted}}>
            {HCO_FEE.note}<br/>
            Focus assessment: ₹15,000 + GST | Re-issue of certificate: ₹6,000 + GST | Fee is non-refundable.
          </div>
        </div>
      </div>

      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>🏥 HCO vs SHCO — Which applies to you?</div>
        <div style={{overflowX:'auto'}}>
          <table style={{width:'100%',borderCollapse:'collapse',fontSize:14}}>
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
                ['ELC Fee','₹52,000 + GST','₹21,000 + GST'],
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

      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>📖 HCO ELC — 10 Assessment Chapters</div>
        <div style={{display:'grid',gap:6}}>
          {HCO_ELC_CHAPTER_SUMMARY.map(c => (
            <div key={c.ch} style={{background:T.panel2,borderRadius:8,padding:'10px 12px',border:`1px solid ${T.border}`}}>
              <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:3}}>
                <span style={{color:T.gold,fontWeight:700,fontSize:14,minWidth:36}}>{c.ch}</span>
                <span style={{color:T.text,fontSize:14,fontWeight:600}}>{c.name}</span>
              </div>
              <div style={{color:T.muted,fontSize:13,lineHeight:1.4,paddingLeft:44}}>{c.desc}</div>
            </div>
          ))}
        </div>
        <div style={{marginTop:10,color:T.muted,fontSize:13,textAlign:'center'}}>Source: NABH Guidebook on Entry-Level Certification for HCOs/SHCOs (Section 4.1)</div>
      </div>
    </div>
  );

  const renderDocTracker = () => {
    const sections = [...new Set(filteredDocs.map(d => d.section))];
    return (
      <div style={{padding:16}}>
        <div style={{display:'flex',gap:8,marginBottom:12,flexWrap:'wrap'}}>
          {[
            {label:`✅ Ready: ${docsDone}`,color:T.green},
            {label:`⏳ Pending: ${HCO_ELC_DOCS.length - docsDone - docsNA}`,color:T.orange},
            {label:`➖ N/A: ${docsNA}`,color:T.muted},
            {label:`Total: ${HCO_ELC_DOCS.length}`,color:T.blue},
          ].map(s => (
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:13,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          <select value={hcoDocPart} onChange={e => setHcoDocPart(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}>
            <option value="all">All Parts</option>
            {parts.map(p => <option key={p} value={p}>Part {p}</option>)}
          </select>
          <select value={hcoDocFilter} onChange={e => setHcoDocFilter(e.target.value)}
            style={{padding:'6px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}>
            <option value="all">All Status</option>
            <option value="pending">Pending</option>
            <option value="ready">Ready</option>
            <option value="na">N/A</option>
          </select>
          <div style={{marginLeft:'auto',color:T.muted,fontSize:13,display:'flex',alignItems:'center'}}>{filteredDocs.length} items</div>
        </div>
        {sections.map(sec => {
          const secDocs = filteredDocs.filter(d => d.section === sec);
          if (!secDocs.length) return null;
          return (
            <div key={sec} style={{marginBottom:16}}>
              <div style={{color:T.gold,fontWeight:600,fontSize:14,marginBottom:8,display:'flex',alignItems:'center',gap:8}}>
                <span>Part {secDocs[0].part} — {sec}</span>
                <span style={{color:T.muted,fontWeight:400,fontSize:13}}>({secDocs.length})</span>
              </div>
              <div style={{display:'flex',flexDirection:'column',gap:6}}>
                {secDocs.map(doc => {
                  const s = docStatus(doc.id);
                  return (
                    <div key={doc.id} style={{background:T.panel,borderRadius:8,padding:'10px 12px',border:`1px solid ${s==='ready'?T.green:T.border}`,opacity:s==='na'?0.6:1}}>
                      <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:8,marginBottom:6}}>
                        <div style={{color:T.text,fontSize:14,lineHeight:1.5,flex:1}}>
                          <span style={{color:T.muted,fontSize:12,marginRight:6}}>#{doc.id}</span>
                          {doc.text}
                        </div>
                        <div style={{flexShrink:0}}>{uploadBadge(doc.upload)}</div>
                      </div>
                      <div style={{display:'flex',gap:6}}>
                        {['pending','ready','na'].map(status => (
                          <button key={status} onClick={() => setDocStatus(doc.id, status)}
                            style={{
                              padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:13,fontWeight:600,
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

  const renderLicenseTracker = () => {
    const mandatory = HCO_ELC_LICENSES.filter(l => l.cat === 'Mandatory');
    const aerb = HCO_ELC_LICENSES.filter(l => l.cat === 'AERB');
    return (
      <div style={{padding:16}}>
        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap'}}>
          {[
            {label:`✅ Obtained: ${licDone}`,color:T.green},
            {label:`⏳ Pending: ${HCO_ELC_LICENSES.length - licDone - licNA}`,color:T.orange},
            {label:`➖ N/A: ${licNA}`,color:T.muted},
          ].map(s => (
            <div key={s.label} style={{padding:'4px 10px',borderRadius:20,background:s.color+'22',color:s.color,fontSize:13,border:`1px solid ${s.color}44`}}>{s.label}</div>
          ))}
        </div>
        <div style={{background:'#0a0d00',border:`1px solid ${T.green}44`,borderRadius:8,padding:10,marginBottom:14}}>
          <div style={{color:T.green,fontSize:14,fontWeight:600,marginBottom:2}}>⚠️ HCO-Specific: PCB License Required</div>
          <div style={{color:T.text,fontSize:13}}>Unlike SHCOs, HCOs ({'>'} 50 beds) must have the Pollution Control Board License for water and Air Pollution. Mark as N/A only if NABH formally exempts your facility.</div>
        </div>
        <div style={{color:T.red,fontWeight:700,fontSize:15,marginBottom:10}}>🔴 Mandatory Licenses ({mandatory.length})</div>
        <div style={{display:'flex',flexDirection:'column',gap:6,marginBottom:20}}>
          {mandatory.map(lic => {
            const s = licStatus(lic.id);
            return (
              <div key={lic.id} style={{background:T.panel,borderRadius:8,padding:'10px 12px',border:`1px solid ${s==='obtained'?T.green:T.border}`,opacity:s==='na'?0.6:1}}>
                <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:8,marginBottom:6}}>
                  <div style={{color:T.text,fontSize:14,flex:1}}>{lic.name}</div>
                  <div style={{color:T.muted,fontSize:12,flexShrink:0}}>{lic.appl}</div>
                </div>
                <div style={{display:'flex',gap:6}}>
                  {['pending','obtained','na'].map(status => (
                    <button key={status} onClick={() => setLicStatus(lic.id, status)}
                      style={{
                        padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:13,fontWeight:600,
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
        <div style={{color:T.orange,fontWeight:700,fontSize:15,marginBottom:6}}>⚡ AERB Licenses ({aerb.length}) — Mark N/A if service not available</div>
        <div style={{color:T.muted,fontSize:13,marginBottom:10}}>Applicable only if your HCO provides the specific imaging/radiation service. If expired, document of renewal application must also be uploaded via portal.</div>
        <div style={{display:'flex',flexDirection:'column',gap:6}}>
          {aerb.map(lic => {
            const s = licStatus(lic.id);
            return (
              <div key={lic.id} style={{background:T.panel,borderRadius:8,padding:'10px 12px',border:`1px solid ${s==='obtained'?T.green:T.border}`,opacity:s==='na'?0.5:1}}>
                <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:8,marginBottom:6}}>
                  <div style={{color:T.text,fontSize:14,flex:1}}>{lic.name}</div>
                  <div style={{color:T.muted,fontSize:12,flexShrink:0,textAlign:'right',maxWidth:120}}>{lic.appl}</div>
                </div>
                <div style={{display:'flex',gap:6}}>
                  {['pending','obtained','na'].map(status => (
                    <button key={status} onClick={() => setLicStatus(lic.id, status)}
                      style={{
                        padding:'3px 10px',borderRadius:6,border:'none',cursor:'pointer',fontSize:13,fontWeight:600,
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

  const renderProcess = () => (
    <div style={{padding:16}}>
      <div style={{background:'#0a0a1a',border:`1px solid ${T.blue}44`,borderRadius:10,padding:12,marginBottom:16}}>
        <div style={{color:T.blue,fontWeight:600,fontSize:14,marginBottom:4}}>💡 Key Points for HCO Applicants</div>
        <div style={{color:T.text,fontSize:14,lineHeight:1.6}}>
          • Two rounds of NC closure at both DA and Onsite stages (unlike SHCO 2nd Edition which gives only one).<br/>
          • Registration details on HOPE portal cannot be edited after submission — fill accurately.<br/>
          • Cannot use both web portal and mobile app simultaneously — save on portal first.<br/>
          • Travel/boarding expenses for onsite assessor are borne by the applicant HCO.<br/>
          • Accreditation certificate uses the hospital name as registered on the HOPE portal.
        </div>
      </div>
      <div style={{display:'flex',flexDirection:'column',gap:0}}>
        {HCO_ELC_PROCESS.map((step, idx) => (
          <div key={step.step} style={{display:'flex',gap:12}}>
            <div style={{display:'flex',flexDirection:'column',alignItems:'center',width:32,flexShrink:0}}>
              <div style={{width:32,height:32,borderRadius:'50%',background:T.gold,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700,fontSize:15,color:T.bg,flexShrink:0}}>
                {step.step}
              </div>
              {idx < HCO_ELC_PROCESS.length - 1 && (
                <div style={{width:2,flex:1,background:T.border,minHeight:20,margin:'4px 0'}}/>
              )}
            </div>
            <div style={{flex:1,paddingBottom:20}}>
              <div style={{color:T.white,fontWeight:700,fontSize:15,marginBottom:4}}>{step.name}</div>
              <div style={{color:T.text,fontSize:14,lineHeight:1.6,marginBottom:6}}>{step.desc}</div>
              <div style={{color:T.green,fontSize:13}}>→ {step.output}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );

  const renderUpgrade = () => (
    <div style={{padding:16}}>
      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.gold}44`,marginBottom:16}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:15,marginBottom:8}}>🚀 The Journey: HCO ELC → Full NABH Accreditation</div>
        <div style={{color:T.text,fontSize:14,lineHeight:1.7}}>
          Entry Level Certification is the first step. After ELC, HCOs can upgrade to Full NABH Hospital Accreditation (6th Edition) — 639 OEs, 4-year validity, and the gold standard in Indian hospital accreditation. Apply via portal.nabh.co at least 6 months before ELC expiry.
        </div>
      </div>
      <div style={{color:T.gold,fontWeight:600,fontSize:15,marginBottom:10}}>Recommended Timeline</div>
      {[
        {phase:'Now – Month 2',action:'Gap analysis: compare current practices against HCO ELC standards. Identify missing documents and expired licenses.',color:T.blue},
        {phase:'Month 2–4',action:'Collect all 223 documents and 26 licenses. Train SPOC on HOPE portal and mobile app.',color:T.blue},
        {phase:'Month 4–5',action:'Register on hope.qcin.org. Fill all 7 parts. Upload portal + mobile app documents. Pay ₹61,360.',color:T.orange},
        {phase:'Month 5–6',action:'Desktop Assessment — respond to NC rounds (two cycles available). Submit complete evidence first time.',color:T.orange},
        {phase:'Month 6–8',action:'Onsite Assessment by NABH assessor. Close onsite NCs (two cycles). Submit feedback.',color:T.orange},
        {phase:'Month 8–9',action:'Certification Committee decision. Receive HCO ELC Certificate (2-year validity).',color:T.green},
        {phase:'Month 9–24',action:'Implement NABH 6th Edition standards (639 OEs). Use portal.nabh.co for full accreditation application.',color:T.gold},
        {phase:'Month 18',action:'Apply for Full NABH Hospital Accreditation via portal.nabh.co — 6 months before ELC expiry.',color:T.gold},
      ].map((p,i) => (
        <div key={i} style={{display:'flex',gap:12,marginBottom:8,alignItems:'flex-start'}}>
          <div style={{minWidth:90,color:p.color,fontWeight:600,fontSize:13,paddingTop:2}}>{p.phase}</div>
          <div style={{flex:1,background:T.panel,borderRadius:8,padding:'8px 12px',border:`1px solid ${p.color}33`,color:T.text,fontSize:14}}>{p.action}</div>
        </div>
      ))}
      <div style={{marginTop:16,background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
        <div style={{color:T.gold,fontWeight:700,fontSize:15,marginBottom:6}}>💼 Post-Accreditation Obligations</div>
        <div style={{color:T.text,fontSize:14,lineHeight:1.7}}>
          After ELC certificate: No surveillance visits (certification programme). Apply for renewal at least 6 months before expiry.
          If renewal not applied 3 months before expiry, NABH presumes disinterest and certificate expires — HCO must re-apply fresh.
          Accredited HCO must use NABH mark only as per guidelines and maintain all standards continuously.
        </div>
      </div>
    </div>
  );

  const HCO_ELC_TABS = [
    {key:'overview', label:'📊 Overview'},
    {key:'docs', label:'📂 Documents'},
    {key:'licenses', label:'📋 Licenses'},
    {key:'process', label:'🗺️ Process'},
    {key:'upgrade', label:'⬆️ Upgrade Path'},
  ];

  const renderHCOELCTab = () => {
    switch(hcoElcTab) {
      case 'overview': return renderOverview();
      case 'docs': return renderDocTracker();
      case 'licenses': return renderLicenseTracker();
      case 'process': return renderProcess();
      case 'upgrade': return renderUpgrade();
      default: return renderOverview();
    }
  };

  return (
    <div style={{background:T.bg,minHeight:'100vh',color:T.text}}>
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
            <div style={{color: hcoMode === m.key ? T.gold : T.text, fontWeight:700, fontSize:14}}>{m.label}</div>
            <div style={{color:T.muted, fontSize:12, marginTop:2}}>{m.sub}</div>
          </button>
        ))}
      </div>

      {hcoMode === 'full' ? (
        renderFullAccredTab()
      ) : (
        <>
          <div style={{display:'flex',overflowX:'auto',gap:0,padding:'12px 16px 0',borderBottom:`1px solid ${T.border}`}}>
            {HCO_ELC_TABS.map(tab => (
              <button key={tab.key} onClick={() => setHcoElcTab(tab.key)}
                style={{
                  padding:'8px 14px', border:'none', cursor:'pointer', whiteSpace:'nowrap',
                  background:'transparent', fontSize:14, fontWeight:600,
                  color: hcoElcTab === tab.key ? T.gold : T.muted,
                  borderBottom: hcoElcTab === tab.key ? `2px solid ${T.gold}` : '2px solid transparent',
                }}>
                {tab.label}
              </button>
            ))}
          </div>
          {renderHCOELCTab()}
        </>
      )}
    </div>
  );
  };

  const ALL_NAV=[
    {id:"dashboard",label:"Dashboard",icon:"📊",programmes:["hco"],primary:true},
    {id:"scoring",label:"Score OEs",icon:"✏️",programmes:["hco"],primary:true},
    {id:"gaps",label:"Fix Gaps",icon:"🔧",programmes:["hco"],primary:true},
    {id:"audits",label:"Audits",icon:"🔍",programmes:["hco"],primary:true},
    {id:"drills",label:"Drills",icon:"🚨",programmes:["hco"],primary:true},
    {id:"committees",label:"Committees",icon:"🏛️",programmes:["hco"],primary:false},
    {id:"kpis",label:"KPIs",icon:"📈",programmes:["hco"],primary:false},
    {id:"checklists",label:"Checklists",icon:"✅",programmes:["hco"],primary:false},
    {id:"committee-calendar",label:"Cal",icon:"📅",programmes:["hco"],primary:false},
    {id:"licenses",label:"Licenses",icon:"📋",programmes:["hco"],primary:false},
    {id:"tracer",label:"Tracer",icon:"🩺",programmes:["hco"],primary:false},
    {id:"pricing",label:"Pricing",icon:"💎",programmes:["hco","shco-elc","hco-elc"],primary:false},
    {id:"profile",label:"Profile",icon:"👤",programmes:["hco","shco-elc","hco-elc"],primary:false},
    {id:"shco",label:"SHCO",icon:"🏥",programmes:["shco-elc"]},
    {id:"hco-elc",label:"HCO ELC",icon:"🎯",programmes:["hco-elc"]},
  ];
  const NAV=ALL_NAV.filter(n=>n.programmes.includes(selectedProgramme));
  const PRIMARY_NAV=NAV.filter(n=>n.primary);
  const SECONDARY_NAV=NAV.filter(n=>!n.primary);
  const secondaryActive=SECONDARY_NAV.some(n=>n.id===screen);

  return (
    <div data-theme={theme} style={{fontFamily:"Segoe UI,system-ui,sans-serif",background:T.bg,minHeight:"100vh",color:T.text}}>
      <style>{`
        *{box-sizing:border-box}
        ::-webkit-scrollbar{width:4px}
        ::-webkit-scrollbar-track{background:${T.bg}}
        ::-webkit-scrollbar-thumb{background:${T.border};border-radius:2px}
        button,select,textarea,input{font-family:inherit}
        ${theme==='light'?`
          [data-theme="light"] body{background:#e8f2fb}
        `:''}
      `}</style>
      <div style={{background:theme==='light'?"#1565c0":"linear-gradient(90deg,#040d1a,#08192e)",borderBottom:`1px solid ${theme==='light'?"#0d47a1":T.border}`,padding:"10px 20px",position:"sticky",top:0,zIndex:200,boxShadow:theme==='light'?"0 2px 12px rgba(21,101,192,0.4)":"0 2px 20px rgba(0,0,0,0.6)"}}>
        <div style={{maxWidth:1200,margin:"0 auto",display:"flex",alignItems:"center",gap:10,flexWrap:"wrap"}}>
          <div style={{width:32,height:32,borderRadius:8,background:theme==='light'?"rgba(255,255,255,0.15)":`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:17,flexShrink:0,border:theme==='light'?"1px solid rgba(255,255,255,0.3)":"none",color:"#ffffff"}}>⚕</div>
          <div style={{flex:1,minWidth:100}}>
            <div style={{fontSize:7,letterSpacing:3,color:theme==='light'?"rgba(255,255,255,0.7)":T.gold}}>NABH 6TH EDITION</div>
            <div style={{fontSize:14,fontWeight:700,color:"#ffffff"}}>{context?.hospitalName||"Compliance Engine"}{context?.assessmentName&&<span style={{fontSize:11,color:theme==='light'?"rgba(255,255,255,0.7)":T.muted,marginLeft:6}}>{context.assessmentName}</span>}</div>
          </div>
          {loading&&<div style={{fontSize:11,color:theme==='light'?"rgba(255,255,255,0.7)":T.muted}}>Refreshing…</div>}
          {selectedProgramme==="hco"&&<div style={{padding:"3px 10px",borderRadius:20,background:`${readinessColor}25`,border:`1px solid ${readinessColor}60`,fontSize:11,fontWeight:700,color:theme==='light'?"#ffffff":readinessColor}}>{decision.readiness==="NOT READY"?"❌":decision.readiness==="RISKY"?"⚠️":"✅"} {decision.readiness||"—"}</div>}
          {selectedProgramme==="hco"&&<div style={{padding:"3px 10px",borderRadius:20,background:`${verdictColor}25`,border:`1px solid ${verdictColor}60`,fontSize:12,fontWeight:800,color:theme==='light'?"#ffffff":verdictColor}}>{decision.verdict==="PARTIAL"?"⚠️":""}{decision.verdict||"—"}</div>}
          <div style={{display:"flex",gap:3,flexWrap:"wrap",position:"relative"}}>
            {PRIMARY_NAV.map(n=>(
              <button key={n.id} onClick={()=>setScreen(n.id)} style={{
                padding:"4px 9px",borderRadius:7,fontSize:11,cursor:"pointer",
                background:screen===n.id?(theme==='light'?"rgba(255,255,255,0.25)":T.goldD):"transparent",
                border:`1px solid ${screen===n.id?(theme==='light'?"rgba(255,255,255,0.6)":T.gold):(theme==='light'?"rgba(255,255,255,0.3)":T.border)}`,
                color:"#ffffff",
                fontWeight:screen===n.id?700:400,
              }}>{n.icon} {n.label}</button>
            ))}
            {SECONDARY_NAV.length>0&&(
              <div style={{position:"relative"}}>
                <button
                  onClick={e=>{e.stopPropagation();setShowMoreMenu(v=>!v);}}
                  style={{padding:"4px 9px",borderRadius:7,fontSize:11,cursor:"pointer",letterSpacing:2,
                    background:(secondaryActive||showMoreMenu)?(theme==='light'?"rgba(255,255,255,0.25)":T.goldD):"transparent",
                    border:`1px solid ${(secondaryActive||showMoreMenu)?(theme==='light'?"rgba(255,255,255,0.6)":T.gold):(theme==='light'?"rgba(255,255,255,0.3)":T.border)}`,
                    color:"#ffffff",
                  }}
                >•••</button>
                {showMoreMenu&&(
                  <div
                    onClick={e=>e.stopPropagation()}
                    style={{position:"absolute",top:"calc(100% + 6px)",right:0,background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:10,display:"grid",gridTemplateColumns:"repeat(3,1fr)",gap:6,zIndex:300,minWidth:220,boxShadow:"0 8px 30px rgba(0,0,0,0.15)"}}>
                    {SECONDARY_NAV.map(n=>(
                      <button key={n.id} onClick={()=>{setScreen(n.id);setShowMoreMenu(false);}}
                        style={{padding:"7px 4px",borderRadius:7,border:`1px solid ${screen===n.id?T.gold:T.border}`,background:screen===n.id?T.goldD:T.panel2,color:screen===n.id?T.gold:T.text,fontSize:11,cursor:"pointer",display:"flex",flexDirection:"column",alignItems:"center",gap:3,fontWeight:screen===n.id?700:400}}>
                        <span style={{fontSize:16}}>{n.icon}</span>
                        <span>{n.label}</span>
                      </button>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
          <button onClick={()=>setAuthState("programme")} style={{padding:"4px 9px",borderRadius:7,background:"transparent",border:`1px solid ${theme==='light'?"rgba(255,255,255,0.3)":T.border}`,color:"#ffffff",fontSize:11,cursor:"pointer"}}>Switch</button>
          <a href="https://drive.google.com/drive/folders/1DOfGmHg_dO5blXw_3Mz07dtre6IKYYlI" target="_blank" rel="noopener noreferrer" style={{padding:"4px 9px",borderRadius:7,background:theme==='light'?"rgba(255,255,255,0.15)":T.goldD,border:`1px solid ${theme==='light'?"rgba(255,255,255,0.4)":T.gold}`,color:"#ffffff",fontSize:11,fontWeight:700,textDecoration:"none",whiteSpace:"nowrap"}}>📁 Docs</a>
          <button onClick={toggleTheme} title={theme==='dark'?'Switch to light mode':'Switch to dark mode'} style={{padding:"4px 9px",borderRadius:7,background:theme==='light'?"rgba(255,255,255,0.2)":"transparent",border:`1px solid ${theme==='light'?"rgba(255,255,255,0.4)":T.border}`,color:"#ffffff",fontSize:15,cursor:"pointer",lineHeight:1}}>{theme==='dark'?'☀️':'🌙'}</button>
          <button onClick={handleSignOut} style={{padding:"4px 9px",borderRadius:7,background:"transparent",border:`1px solid ${theme==='light'?"rgba(255,255,255,0.3)":T.border}`,color:"#ffffff",fontSize:11,cursor:"pointer"}}>Sign out</button>
        </div>
      </div>

      {selectedProgramme==="hco"&&(!decision.core_pass&&(decision.core_failures||0)>0)&&(
        <div style={{background:T.redD,padding:"8px 20px",display:"flex",gap:10,alignItems:"center"}}>
          <span style={{fontSize:16}}>🚨</span>
          <span style={{fontSize:13,fontWeight:700,color:T.red}}>
            CORE FAILURE: {decision.core_failures} element{decision.core_failures>1?"s":""} at risk
            {decision.core_unscored>0&&` (${decision.core_unscored} unscored, ${decision.core_scored_failures||0} scored below 4)`}
            {" "}— assessment will be rejected.
          </span>
        </div>
      )}

      <div style={{maxWidth:1200,margin:"0 auto",padding:"16px"}}>
        {screen==="dashboard"&&<Dashboard decision={decision} gaps={gaps} onNav={setScreen}/>}
        {screen==="dashboard"&&<button onClick={generatePDF} disabled={pdfLoading}
          style={{position:'fixed',bottom:20,right:20,zIndex:9999,padding:'8px 16px',borderRadius:9,border:`1px solid ${T.gold}`,background:T.bg,color:T.gold,fontSize:12,fontWeight:700,cursor:pdfLoading?'default':'pointer',opacity:pdfLoading?0.6:1,boxShadow:'0 2px 12px rgba(0,0,0,0.5)'}}>
          {pdfLoading?'⏳ Generating…':'⬇ Export PDF'}
        </button>}
        {screen==="scoring"&&<ScoringScreen assessmentId={context?.assessmentId} oes={oes} standards={standards} onRefresh={()=>loadData(context)}/>}
        {screen==="gaps"&&<GapFixScreen assessmentId={context?.assessmentId} gaps={gaps} onRefresh={()=>loadData(context)}/>}
        {screen==="committees"&&<CommitteesScreen hospitalId={context?.hospitalId}/>}
        {screen==="committee-calendar"&&<CommitteeCalendarScreen hospitalId={context?.hospitalId}/>}
        {screen==="kpis"&&<KPIsScreen hospitalId={context?.hospitalId} user={user}/>}
        {screen==="checklists"&&<ChecklistsScreen hospitalId={context?.hospitalId}/>}
        {screen==="audits"&&<AuditsScreen hospitalId={context?.hospitalId}/>}
        {screen==="drills"&&<MockDrillsScreen hospitalId={context?.hospitalId}/>}
        {screen==="licenses"&&<StatutoryLicensesScreen hospitalId={context?.hospitalId}/>}
        {screen==="tracer"&&<PatientTracerScreen hospitalId={context?.hospitalId}/>}
        {screen==="pricing"&&<PricingScreen/>}
        {screen==="profile"&&<ProfileScreen user={user} context={context} onContextUpdate={setContext}/>}
        {screen==="shco"&&renderSHCOTab()}
        {screen==="hco-elc"&&renderHCOTab()}
      </div>

      <div style={{textAlign:"center",padding:"14px",color:T.muted,fontSize:11,borderTop:`1px solid ${T.border}`,marginTop:20}}>
        NABH Compliance Engine — Independent educational tool — Not affiliated with NABH/QCI | Dr. Mehul Upadhyay
      </div>
    </div>
  );
}

// ── MOCK DRILLS ───────────────────────────────────────────────
function MockDrillsScreen({ hospitalId }) {
  const [drills,setDrills]=useState([]);
  const [records,setRecords]=useState([]);
  const [view,setView]=useState("tracker"); // tracker | calendar | record
  const [selectedDrill,setSelectedDrill]=useState(null);
  const [form,setForm]=useState({drill_date:"",drill_time:"",location:"",conducted_by:"",supervised_by:"",participants_category:"",total_participants:"",pre_briefing:"Done",scenario_desc:"",drill_description:"",observations:["","",""],debriefing:"Done",corrective_actions:"",preventive_actions:"",additional_points:"",status:"completed",evidence_url:""});
  const [saving,setSaving]=useState(false);
  const [expanded,setExpanded]=useState(null);
  const [loading,setLoading]=useState(true);

  const deleteRecord=async(id)=>{
    await supabase.from("mock_drill_records").delete().eq("id",id);
    setRecords(prev=>prev.filter(r=>r.id!==id));
  };

  useEffect(()=>{
    Promise.all([
      supabase.from("mock_drills").select("*").order("frequency_per_year",{ascending:false}),
      supabase.from("mock_drill_records").select("*").eq("hospital_id",hospitalId).order("drill_date",{ascending:false})
    ]).then(([{data:d,error:e1},{data:r,error:e2}])=>{
      if(e1)console.error("mock_drills error:",e1);
      if(e2)console.error("mock_drill_records error:",e2);
      setDrills(d||[]);setRecords(r||[]);setLoading(false);
    });
  },[hospitalId]);

  const drillRecords=(id)=>records.filter(r=>r.drill_id===id);
  const lastDrill=(id)=>drillRecords(id)[0];
  const daysSince=(d)=>d?Math.floor((Date.now()-new Date(d).getTime())/86400000):999;
  const freqDays=(d)=>d==="monthly"?31:d==="quarterly"?92:120;
  const drillStatus=(drill)=>{
    const last=lastDrill(drill.id);
    if(!last)return"NOT_STARTED";
    const days=daysSince(last.drill_date);
    const max=freqDays(drill.frequency);
    if(days<=max)return"ON_TRACK";
    return"OVERDUE";
  };
  const statusColor=(s)=>s==="ON_TRACK"?T.green:s==="NOT_STARTED"?T.red:T.orange;
  const statusLabel=(s)=>s==="ON_TRACK"?"✅ On Track":s==="NOT_STARTED"?"❌ Not Started":"⚠️ Overdue";

  const totalDrills=drills.length;
  const onTrack=drills.filter(d=>drillStatus(d)==="ON_TRACK").length;
  const pct=totalDrills>0?Math.round((onTrack/totalDrills)*100):0;

  const saveRecord=async()=>{
    if(!form.drill_date||!selectedDrill)return;
    setSaving(true);
    const obs=form.observations.filter(o=>o.trim());
    await supabase.from("mock_drill_records").insert({
      hospital_id:hospitalId,drill_id:selectedDrill.id,
      drill_date:form.drill_date,drill_time:form.drill_time,
      location:form.location,conducted_by:form.conducted_by,
      supervised_by:form.supervised_by,
      participants_category:form.participants_category,
      total_participants:form.total_participants?parseInt(form.total_participants):null,
      pre_briefing:form.pre_briefing,scenario_desc:form.scenario_desc,
      drill_description:form.drill_description,
      observations:obs,debriefing:form.debriefing,
      corrective_actions:form.corrective_actions,
      preventive_actions:form.preventive_actions,
      additional_points:form.additional_points,status:form.status,
      evidence_url:form.evidence_url||null
    });
    const {data:r}=await supabase.from("mock_drill_records").select("*").eq("hospital_id",hospitalId).order("drill_date",{ascending:false});
    setRecords(r||[]);setSaving(false);setView("tracker");setSelectedDrill(null);
  };

  if(loading)return <div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  // RECORD FORM
  if(view==="record"&&selectedDrill)return(
    <div>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:14}}>
        <button onClick={()=>{setView("tracker");setSelectedDrill(null);}} style={{padding:"5px 12px",borderRadius:7,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:13,cursor:"pointer"}}>← Back</button>
        <div style={{fontSize:16,fontWeight:700,color:T.gold}}>Record Drill: {selectedDrill.name}</div>
      </div>
      <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10,marginBottom:10}}>
        {[["Drill Date *","date","drill_date"],["Drill Time","time","drill_time"],["Location","text","location"],["Conducted By","text","conducted_by"],["Supervised By","text","supervised_by"],["Participants Category","text","participants_category"],["Total Participants","number","total_participants"]].map(([l,t,k])=>(
          <div key={k}>
            <div style={{fontSize:11,color:T.muted,marginBottom:3}}>{l}</div>
            <input type={t} value={form[k]} onChange={e=>setForm(p=>({...p,[k]:e.target.value}))}
              style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
          </div>
        ))}
        {[["Pre-Briefing","pre_briefing"],["Status","status"],["Debriefing","debriefing"]].map(([l,k])=>(
          <div key={k}>
            <div style={{fontSize:11,color:T.muted,marginBottom:3}}>{l}</div>
            <select value={form[k]} onChange={e=>setForm(p=>({...p,[k]:e.target.value}))}
              style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}>
              {k==="status"?<><option value="completed">Completed</option><option value="planned">Planned</option><option value="missed">Missed</option></>
              :<><option value="Done">Done</option><option value="Not Done">Not Done</option><option value="Not Required">Not Required</option></>}
            </select>
          </div>
        ))}
      </div>
      {[["Scenario Description","scenario_desc"],["Drill Description & Response","drill_description"],["Corrective Actions","corrective_actions"],["Preventive Actions","preventive_actions"],["Additional Points","additional_points"]].map(([l,k])=>(
        <div key={k} style={{marginBottom:8}}>
          <div style={{fontSize:11,color:T.muted,marginBottom:3}}>{l}</div>
          <textarea value={form[k]} onChange={e=>setForm(p=>({...p,[k]:e.target.value}))} rows={2}
            style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:"vertical"}}/>
        </div>
      ))}
      <div style={{marginBottom:10}}>
        <div style={{fontSize:11,color:T.muted,marginBottom:5}}>Deviations / Observations (one per line)</div>
        {form.observations.map((o,i)=>(
          <input key={i} value={o} onChange={e=>{const obs=[...form.observations];obs[i]=e.target.value;setForm(p=>({...p,observations:obs}));}}
            placeholder={`Observation ${i+1}`}
            style={{width:"100%",padding:"6px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,marginBottom:4}}/>
        ))}
        <button onClick={()=>setForm(p=>({...p,observations:[...p.observations,""]}))}
          style={{fontSize:12,color:T.gold,background:"transparent",border:"none",cursor:"pointer"}}>+ Add observation</button>
      </div>
      <div style={{marginBottom:12}}>
        <div style={{fontSize:11,color:T.muted,marginBottom:4}}>EVIDENCE LINK — Drill Record/Photo (Google Drive / OneDrive URL)</div>
        <input value={form.evidence_url||""} onChange={e=>setForm(p=>({...p,evidence_url:e.target.value}))} placeholder="https://drive.google.com/…"
          style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
      </div>
      <button onClick={saveRecord} disabled={saving||!form.drill_date}
        style={{padding:"10px 24px",borderRadius:9,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:14,fontWeight:700,cursor:"pointer"}}>
        {saving?"Saving…":"💾 Save Drill Record"}
      </button>
    </div>
  );

  // TRACKER VIEW
  return(
    <div>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"14px 18px",marginBottom:14,display:"flex",gap:20,alignItems:"center",flexWrap:"wrap"}}>
        <div>
          <div style={{fontSize:11,letterSpacing:2,color:T.muted,marginBottom:2}}>MOCK DRILL READINESS</div>
          <div style={{fontSize:28,fontWeight:800,color:pct===100?T.green:pct>50?T.gold:T.red}}>{pct}%</div>
          <div style={{fontSize:12,color:T.muted}}>{onTrack}/{totalDrills} drills on track</div>
        </div>
        <div style={{flex:1,minWidth:200}}>
          <div style={{height:8,background:T.border,borderRadius:4,marginBottom:8}}>
            <div style={{width:`${pct}%`,height:"100%",background:pct===100?T.green:pct>50?T.gold:T.red,borderRadius:4,transition:"width 0.5s"}}/>
          </div>
          <div style={{display:"flex",gap:16,fontSize:11,color:T.muted}}>
            <span>🔴 {drills.filter(d=>drillStatus(d)==="NOT_STARTED").length} Not Started</span>
            <span>⚠️ {drills.filter(d=>drillStatus(d)==="OVERDUE").length} Overdue</span>
            <span>✅ {onTrack} On Track</span>
          </div>
        </div>
      </div>

      <div style={{display:"grid",gap:8}}>
        {drills.map(drill=>{
          const st=drillStatus(drill);
          const last=lastDrill(drill.id);
          const recs=drillRecords(drill.id);
          const isOpen=expanded===drill.id;
          return(
            <div key={drill.id} style={{background:T.panel,border:`1px solid ${isOpen?T.gold:T.border}`,borderRadius:10,overflow:"hidden"}}>
              <div style={{padding:"10px 14px",display:"flex",alignItems:"center",gap:10,cursor:"pointer"}} onClick={()=>setExpanded(isOpen?null:drill.id)}>
                <div style={{width:44,height:44,borderRadius:8,background:drill.color||T.goldD,display:"flex",alignItems:"center",justifyContent:"center",flexShrink:0}}>
                  <div style={{fontSize:7,fontWeight:800,color:"#ffffff",textAlign:"center",lineHeight:1.2}}>{drill.code||"DRILL"}</div>
                </div>
                <div style={{flex:1}}>
                  <div style={{fontSize:14,fontWeight:700,color:T.white}}>{drill.name}</div>
                  <div style={{fontSize:11,color:T.muted,marginTop:2}}>
                    🔁 {drill.frequency} &nbsp;|&nbsp; 📋 NABH: {drill.nabh_ref}
                    {last&&<span style={{marginLeft:8}}>Last: {last.drill_date}</span>}
                    {!last&&<span style={{marginLeft:8,color:T.red}}>Never conducted</span>}
                  </div>
                </div>
                <div style={{fontSize:11,fontWeight:700,color:statusColor(st),padding:"3px 10px",borderRadius:20,background:`${statusColor(st)}15`,border:`1px solid ${statusColor(st)}40`,whiteSpace:"nowrap"}}>{statusLabel(st)}</div>
                <button onClick={e=>{e.stopPropagation();setSelectedDrill(drill);setForm({drill_date:"",drill_time:"",location:"",conducted_by:"",supervised_by:"",participants_category:"",total_participants:"",pre_briefing:"Done",scenario_desc:"",drill_description:"",observations:["","",""],debriefing:"Done",corrective_actions:"",preventive_actions:"",additional_points:"",status:"completed",evidence_url:""});setView("record");}}
                  style={{padding:"5px 12px",borderRadius:7,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:12,fontWeight:700,cursor:"pointer",whiteSpace:"nowrap"}}>+ Record</button>
                <div style={{color:T.muted,fontSize:13}}>{isOpen?"▲":"▼"}</div>
              </div>
              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"12px 14px"}}>
                  <div style={{fontSize:12,color:T.muted,marginBottom:8,lineHeight:1.6}}>{drill.description}</div>
                  {recs.length>0&&(
                    <div>
                      <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:6}}>DRILL HISTORY</div>
                      {recs.slice(0,5).map(r=>(
                        <div key={r.id} style={{background:T.panel2,borderRadius:7,padding:"8px 12px",marginBottom:5,fontSize:11,color:T.muted,display:"flex",gap:10,alignItems:"center"}}>
                          <div style={{fontWeight:700,color:T.text,minWidth:80}}>{r.drill_date}</div>
                          <div style={{flex:1}}>{r.location&&`📍 ${r.location} · `}{r.total_participants&&`👥 ${r.total_participants} participants · `}{r.conducted_by&&`👤 ${r.conducted_by}`}</div>
                          {r.corrective_actions&&<div style={{color:T.orange}}>⚡ CAPA raised</div>}
                          <button onClick={()=>deleteRecord(r.id)} style={{padding:"2px 8px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:11,cursor:"pointer",flexShrink:0}}>Delete</button>
                        </div>
                      ))}
                    </div>
                  )}
                  {recs.length===0&&<div style={{fontSize:12,color:T.red,padding:"8px 0"}}>No drills recorded yet — click "+ Record" to add the first drill.</div>}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

// ── COMMITTEE CALENDAR ────────────────────────────────────────
function CommitteeCalendarScreen({ hospitalId }) {
  const [committees,setCommittees]=useState([]);
  const [calendarPlan,setCalendarPlan]=useState([]); // calendar_plan table (planning only)
  const [year,setYear]=useState(new Date().getFullYear());
  const [loading,setLoading]=useState(true);
  const [viewMode,setViewMode]=useState("committee");
  const [popup,setPopup]=useState(null); // {committeeId, monthNum, dateVal, saving, isDrill}

  const MONTHS=["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"];
  const MONTH_NUMS=[4,5,6,7,8,9,10,11,12,1,2,3];

  const DRILLS=[
    {id:"code-blue",name:"Code Blue",color:"#1A4A7A",freq:"M",months:[4,5,6,7,8,9,10,11,12,1,2,3]},
    {id:"code-red",name:"Code Red",color:"#8B1A1A",freq:"M",months:[4,5,6,7,8,9,10,11,12,1,2,3]},
    {id:"code-pink",name:"Code Pink",color:"#8B1A6B",freq:"Q",months:[4,7,10,1]},
    {id:"code-grey",name:"Code Grey",color:"#4A4A4A",freq:"H",months:[4,10]},
    {id:"code-orange",name:"Code Orange",color:"#8B5A1A",freq:"H",months:[5,11]},
    {id:"code-yellow",name:"Code Yellow",color:"#8B8B1A",freq:"H",months:[6,12]},
    {id:"code-purple",name:"Code Purple",color:"#4A1A6B",freq:"H",months:[7,1]},
    {id:"chemical-spill",name:"Chemical Spill",color:"#2D6B2D",freq:"H",months:[8,2]},
    {id:"bomb-threat",name:"Bomb Threat",color:"#5A1A1A",freq:"H",months:[9,3]},
    {id:"infection-outbreak",name:"Infection Outbreak",color:"#1A5A2D",freq:"H",months:[4,10]},
    {id:"missing-patient",name:"Missing Patient",color:"#1A4A6B",freq:"H",months:[5,11]},
    {id:"it-failure",name:"IT Failure",color:"#1A1A5A",freq:"H",months:[6,12]},
    {id:"mci-community",name:"MCI Community",color:"#6B1A1A",freq:"H",months:[7,1]},
  ];

  useEffect(()=>{
    Promise.all([
      supabase.from("committees").select("id,name,frequency,chapter_ref").order("name"),
      supabase.from("calendar_plan").select("id,item_type,item_id,planned_date").eq("hospital_id",hospitalId)
    ]).then(([{data:c,error:e1},{data:cp}])=>{
      if(e1)console.error("committees error:",e1);
      setCommittees(c||[]);setCalendarPlan(cp||[]);setLoading(false);
    });
  },[hospitalId]);

  const matchesYearMonth=(dateStr,monthNum)=>{
    const d=new Date(dateStr);const mYear=d.getFullYear();const mMonth=d.getMonth()+1;
    if(monthNum>=4)return mYear===year&&mMonth===monthNum;
    return mYear===year+1&&mMonth===monthNum;
  };

  const getPlanRecord=(itemId,monthNum,itemType)=>
    calendarPlan.find(p=>p.item_id===itemId&&p.item_type===itemType&&matchesYearMonth(p.planned_date,monthNum))||null;

  const hasScheduled=(committeeId,monthNum)=>!!getPlanRecord(committeeId,monthNum,"committee");

  const getMeetingDay=(id,monthNum,isDrill)=>{
    const rec=getPlanRecord(id,monthNum,isDrill?"drill":"committee");
    return rec?new Date(rec.planned_date).getDate():null;
  };

  const freqMonths=(freq)=>{
    if(!freq)return[4,7,10,1];
    const f=freq.toLowerCase();
    if(f.includes("month"))return[4,5,6,7,8,9,10,11,12,1,2,3];
    if(f.includes("bi"))return[4,6,8,10,12,2];
    if(f.includes("quarter"))return[4,7,10,1];
    if(f.includes("six")||f.includes("half"))return[4,10];
    if(f.includes("annual"))return[10];
    return[4,7,10,1];
  };

  const now=new Date();
  const isPast=(monthNum)=>{const mYear=monthNum>=4?year:year+1;return new Date(mYear,monthNum,1)<now;};

  const openPopup=(itemId,monthNum,isDrill=false)=>{
    const itemType=isDrill?"drill":"committee";
    const rec=getPlanRecord(itemId,monthNum,itemType);
    const targetYear=monthNum>=4?year:year+1;
    const defaultDate=rec?new Date(rec.planned_date).toISOString().split("T")[0]:`${targetYear}-${String(monthNum).padStart(2,"0")}-01`;
    setPopup({committeeId:itemId,monthNum,dateVal:defaultDate,saving:false,isDrill});
  };

  const saveDate=async()=>{
    if(!popup||popup.saving)return;
    setPopup(p=>({...p,saving:true}));
    const{committeeId:itemId,monthNum,dateVal,isDrill}=popup;
    const itemType=isDrill?"drill":"committee";
    const existing=getPlanRecord(itemId,monthNum,itemType);
    // delete existing plan entry for this item+month
    if(existing?.id){
      await supabase.from("calendar_plan").delete().eq("id",existing.id);
    }
    if(dateVal){
      const d=new Date(dateVal);
      const planYear=d.getFullYear();const planMonth=d.getMonth()+1;
      const{error:insErr}=await supabase.from("calendar_plan").insert({
        hospital_id:hospitalId,item_type:itemType,item_id:itemId,
        planned_date:dateVal,year:planYear,month:planMonth
      });
      if(insErr){setPopup(p=>({...p,saving:false,error:insErr.message}));return;}
    }
    // optimistic local update
    setCalendarPlan(prev=>{
      const filtered=prev.filter(p=>!(p.item_id===itemId&&p.item_type===itemType&&matchesYearMonth(p.planned_date,monthNum)));
      return dateVal?[...filtered,{item_id:itemId,item_type:itemType,planned_date:dateVal}]:filtered;
    });
    setPopup(null);
  };

  const totalExpected=committees.reduce((sum,c)=>sum+freqMonths(c.frequency).length,0);
  const totalDone=committees.reduce((sum,c)=>sum+MONTH_NUMS.filter(m=>hasScheduled(c.id,m)).length,0);
  const pct=totalExpected>0?Math.round((totalDone/totalExpected)*100):0;

  if(loading)return <div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  const tableHdr=(
    <thead><tr>
      <th style={{padding:"6px 8px",textAlign:"left",fontSize:11,color:T.gold,background:T.panel,border:`1px solid ${T.border}`,minWidth:150,position:"sticky",left:0,zIndex:1}}>Name</th>
      <th style={{padding:"6px 2px",textAlign:"center",fontSize:7,color:T.muted,background:T.panel,border:`1px solid ${T.border}`,minWidth:22}}>Freq</th>
      {MONTHS.map(m=><th key={m} style={{padding:"5px 2px",textAlign:"center",fontSize:7.5,color:T.gold,background:T.panel,border:`1px solid ${T.border}`,minWidth:32}}>{m}</th>)}
      <th style={{padding:"6px 2px",textAlign:"center",fontSize:7,color:T.muted,background:T.panel,border:`1px solid ${T.border}`,minWidth:34}}>Done</th>
    </tr></thead>
  );

  return(
    <div>
      {popup&&(
        <div style={{position:"fixed",inset:0,zIndex:1000,display:"flex",alignItems:"center",justifyContent:"center",background:"rgba(0,0,0,0.55)"}} onClick={()=>setPopup(null)}>
          <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"22px 26px",minWidth:270,boxShadow:"0 8px 40px #000c"}} onClick={e=>e.stopPropagation()}>
            <div style={{fontSize:15,fontWeight:700,color:T.gold,marginBottom:4}}>Set Meeting Date</div>
            <div style={{fontSize:12,color:T.muted,marginBottom:14}}>{MONTHS[MONTH_NUMS.indexOf(popup.monthNum)]} {popup.monthNum>=4?year:year+1}</div>
            <input type="date" value={popup.dateVal} onChange={e=>setPopup(p=>({...p,dateVal:e.target.value,error:null}))}
              style={{width:"100%",padding:"9px 11px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,marginBottom:14,boxSizing:"border-box"}}/>
            {popup.error&&<div style={{fontSize:12,color:T.red,marginBottom:10}}>{popup.error}</div>}
            <div style={{display:"flex",gap:8}}>
              <button onClick={saveDate} disabled={popup.saving} style={{flex:1,padding:"9px",borderRadius:7,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontWeight:700,fontSize:15,cursor:"pointer",opacity:popup.saving?0.6:1}}>{popup.saving?"Saving…":"Save"}</button>
              <button onClick={()=>setPopup(null)} style={{padding:"9px 16px",borderRadius:7,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:15,cursor:"pointer"}}>Cancel</button>
            </div>
          </div>
        </div>
      )}
      <div style={{display:"grid",gridTemplateColumns:"1fr auto 1fr",alignItems:"center",marginBottom:10,gap:8}}>
        <div>
          <div style={{fontSize:15,fontWeight:700,color:T.gold}}>{viewMode==="committee"?"Committee Calendar":"Mock Drill Calendar"}</div>
          <div style={{fontSize:12,color:T.muted}}>FY {year}–{year+1}{viewMode==="committee"?` · ${totalDone}/${totalExpected} done · ${pct}%`:""}</div>
        </div>
        <div style={{display:"flex",borderRadius:8,border:`1px solid ${T.border}`,overflow:"hidden"}}>
          <button onClick={()=>setViewMode("committee")} style={{padding:"7px 18px",fontSize:16,fontWeight:700,cursor:"pointer",background:viewMode==="committee"?T.goldD:"transparent",border:"none",color:viewMode==="committee"?T.goldL:T.muted,letterSpacing:0.2}}>🏛️ Committees</button>
          <div style={{width:1,background:T.border}}/>
          <button onClick={()=>setViewMode("drill")} style={{padding:"7px 18px",fontSize:16,fontWeight:700,cursor:"pointer",background:viewMode==="drill"?T.goldD:"transparent",border:"none",color:viewMode==="drill"?T.goldL:T.muted,letterSpacing:0.2}}>🚨 Drills</button>
        </div>
        <div style={{display:"flex",gap:6,alignItems:"center",justifyContent:"flex-end"}}>
          <button onClick={()=>setYear(y=>y-1)} style={{padding:"3px 8px",borderRadius:5,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:12,cursor:"pointer"}}>◀</button>
          <div style={{fontSize:12,fontWeight:700,color:T.gold,padding:"3px 10px",borderRadius:5,border:`1px solid ${T.gold}`,background:T.goldD}}>FY {year}–{year+1}</div>
          <button onClick={()=>setYear(y=>y+1)} style={{padding:"3px 8px",borderRadius:5,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:12,cursor:"pointer"}}>▶</button>
        </div>
      </div>

      <div style={{display:"flex",gap:10,marginBottom:8,fontSize:8,flexWrap:"wrap"}}>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:T.green,display:"inline-block"}}/>Done</span>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:"#1A3A5A",border:`1px dashed ${T.gold}`,display:"inline-block"}}/>Planned</span>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:T.red,display:"inline-block"}}/>Missed</span>
        <span style={{display:"flex",alignItems:"center",gap:3}}><span style={{width:12,height:12,borderRadius:2,background:T.border,display:"inline-block"}}/>Not Expected</span>
      </div>

      <div style={{overflowX:"auto"}}>
        {viewMode==="committee"&&(
          <table style={{borderCollapse:"collapse",width:"100%",minWidth:860}}>
            {tableHdr}
            <tbody>
              {committees.length===0&&<tr><td colSpan={16} style={{textAlign:"center",padding:30,color:T.muted,fontSize:13}}>No committees loading — check connection.</td></tr>}
              {committees.map((c,ci)=>{
                const done=MONTH_NUMS.filter(m=>hasScheduled(c.id,m)).length;
                const exp=freqMonths(c.frequency).length;
                return(
                  <tr key={c.id} style={{background:ci%2===0?T.panel:T.panel2}}>
                    <td style={{padding:"4px 8px",fontSize:8.5,border:`1px solid ${T.border}`,position:"sticky",left:0,background:ci%2===0?T.panel:T.panel2,zIndex:1}}>
                      <div style={{fontWeight:600,color:T.white,whiteSpace:"nowrap",overflow:"hidden",textOverflow:"ellipsis",maxWidth:145}}>{c.name}</div>
                      <div style={{fontSize:6.5,color:T.muted}}>{c.chapter_ref}</div>
                    </td>
                    <td style={{padding:"3px",textAlign:"center",fontSize:7,color:T.muted,border:`1px solid ${T.border}`}}>{c.frequency?.charAt(0).toUpperCase()||"Q"}</td>
                    {MONTH_NUMS.map((mn,mi)=>{
                      const dayNum=getMeetingDay(c.id,mn);
                      const isDone=!!dayNum||hasScheduled(c.id,mn);
                      const isExp=freqMonths(c.frequency).includes(mn);
                      const past=isPast(mn);
                      let bg="transparent",txt="",brd="none";
                      if(isDone){bg=T.green;txt=dayNum||"✓";}
                      else if(isExp&&!past){bg="#1A3A5A";txt="·";brd=`1px dashed ${T.gold}`;}
                      else if(isExp&&past){bg=T.red;txt="✗";}
                      return(
                        <td key={mi} onClick={()=>openPopup(c.id,mn)} style={{padding:"2px",textAlign:"center",border:`1px solid ${T.border}`,cursor:"pointer"}}>
                          <div style={{width:24,height:24,borderRadius:3,background:bg,margin:"0 auto",display:"flex",alignItems:"center",justifyContent:"center",fontSize:8,color:"#fff",fontWeight:700,border:brd}}>{txt}</div>
                        </td>
                      );
                    })}
                    <td style={{padding:"3px",textAlign:"center",fontSize:8,fontWeight:700,color:done>=exp?T.green:done>0?T.orange:T.red,border:`1px solid ${T.border}`}}>{done}/{exp}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        )}
        {viewMode==="drill"&&(
          <table style={{borderCollapse:"collapse",width:"100%",minWidth:860}}>
            {tableHdr}
            <tbody>
              {DRILLS.map((d,ci)=>(
                <tr key={d.id} style={{background:ci%2===0?T.panel:T.panel2}}>
                  <td style={{padding:"4px 8px",fontSize:8.5,border:`1px solid ${T.border}`,position:"sticky",left:0,background:ci%2===0?T.panel:T.panel2,zIndex:1}}>
                    <div style={{display:"flex",alignItems:"center",gap:5}}>
                      <div style={{width:8,height:8,borderRadius:2,background:d.color,flexShrink:0}}/>
                      <div style={{fontWeight:600,color:T.white}}>{d.name}</div>
                    </div>
                  </td>
                  <td style={{padding:"3px",textAlign:"center",fontSize:7,color:T.muted,border:`1px solid ${T.border}`}}>{d.freq}</td>
                  {MONTH_NUMS.map((mn,mi)=>{
                    const isPlanned=d.months.includes(mn);
                    const past=isPast(mn);
                    const dayNum=getMeetingDay(d.id,mn,true);
                    const isDone=!!dayNum;
                    let bg="transparent",txt="",brd="none";
                    if(isDone){bg=d.color;txt=dayNum;brd=`1px solid ${d.color}`;}
                    else if(isPlanned&&!past){bg="#1A2A1A";txt="·";brd=`1px dashed ${d.color}`;}
                    else if(isPlanned&&past){bg="#2A2A3A";txt="?";}
                    return(
                      <td key={mi} onClick={()=>openPopup(d.id,mn,true)} style={{padding:"2px",textAlign:"center",border:`1px solid ${T.border}`,cursor:"pointer"}}>
                        <div style={{width:24,height:24,borderRadius:3,background:bg,margin:"0 auto",display:"flex",alignItems:"center",justifyContent:"center",fontSize:7,color:"#fff",fontWeight:700,border:brd}}>{txt}</div>
                      </td>
                    );
                  })}
                  {(()=>{const actualDone=MONTH_NUMS.filter(m=>!!getMeetingDay(d.id,m,true)).length;const exp=d.months.length;return(<td style={{padding:"3px",textAlign:"center",fontSize:8,fontWeight:700,color:actualDone>=exp?T.green:actualDone>0?T.orange:T.red,border:`1px solid ${T.border}`}}>{actualDone>0?`${actualDone}/${exp}`:"—"}</td>);})()}
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}


// ── STATUTORY LICENSE TRACKER ─────────────────────────────────
const LICENSE_TEMPLATES = [
  {name:"Fire NOC",authority:"Fire Department / Municipality",type:"Safety"},
  {name:"BMW Authorization",authority:"State Pollution Control Board",type:"Waste"},
  {name:"PCB Consent to Operate",authority:"State Pollution Control Board",type:"Environmental"},
  {name:"CGWA Water Withdrawal",authority:"Central Ground Water Authority",type:"Environmental"},
  {name:"Lift License",authority:"State Electrical Inspectorate",type:"Infrastructure"},
  {name:"Clinical Establishment Registration",authority:"State Health Department",type:"Regulatory"},
  {name:"Blood Bank License",authority:"CDSCO / State Drugs Controller",type:"Clinical"},
  {name:"Pharmacy License",authority:"State Drugs Controller",type:"Clinical"},
  {name:"AERB Radiation Safety",authority:"Atomic Energy Regulatory Board",type:"Radiation"},
  {name:"NABH Accreditation Certificate",authority:"NABH / QCI",type:"Accreditation"},
  {name:"NABL Accreditation (Lab)",authority:"NABL",type:"Accreditation"},
  {name:"Narcotics License",authority:"State Drugs Controller / NCB",type:"Clinical"},
  {name:"Trade License",authority:"Municipality / Local Body",type:"Regulatory"},
  {name:"Biomedical Equipment Calibration",authority:"Internal / NABL Lab",type:"Quality"},
  {name:"Building Completion Certificate",authority:"Municipality",type:"Infrastructure"},
  {name:"Water Potability Certificate",authority:"Municipality / Accredited Lab",type:"Safety"},
  {name:"Sewage Treatment Plant Certificate",authority:"State PCB",type:"Environmental"},
  {name:"Medical Gas Pipeline Certificate",authority:"State Electrical Inspectorate",type:"Safety"},
  {name:"Boiler Certificate",authority:"State Boiler Inspectorate",type:"Infrastructure"},
  {name:"Diesel Generator Clearance",authority:"State PCB / Municipality",type:"Environmental"},
];

function StatutoryLicensesScreen({ hospitalId }) {
  const [licenses,setLicenses]=useState([]);
  const [loading,setLoading]=useState(true);
  const [saving,setSaving]=useState(false);
  const [editId,setEditId]=useState(null);
  const [showAdd,setShowAdd]=useState(false);
  const [form,setForm]=useState({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""});
  const [filter,setFilter]=useState("all");

  useEffect(()=>{load();},[hospitalId]);

  const load=async()=>{
    setLoading(true);
    const{data}=await supabase.from("statutory_licenses").select("*").eq("hospital_id",hospitalId).order("expiry_date",{ascending:true});
    setLicenses(data||[]);setLoading(false);
  };

  const getStatus=(expiry)=>{
    if(!expiry)return{label:"No Expiry Set",color:T.muted,bg:"transparent"};
    const d=new Date(expiry),now=new Date(),diff=Math.ceil((d-now)/(1000*60*60*24));
    if(diff<0)return{label:"EXPIRED",color:T.red,bg:T.redD};
    if(diff<=30)return{label:`Expires in ${diff}d`,color:T.orange,bg:T.orangeD};
    if(diff<=90)return{label:`Expires in ${diff}d`,color:T.gold,bg:T.goldD};
    return{label:"Valid",color:T.green,bg:T.greenD};
  };

  const save=async()=>{
    if(!form.license_name.trim())return;
    setSaving(true);
    if(editId){
      await supabase.from("statutory_licenses").update({...form,updated_at:new Date().toISOString()}).eq("id",editId);
    } else {
      await supabase.from("statutory_licenses").insert({...form,hospital_id:hospitalId});
    }
    setSaving(false);setEditId(null);setShowAdd(false);
    setForm({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""});
    load();
  };

  const del=async(id)=>{
    if(!window.confirm("Delete this license record?"))return;
    await supabase.from("statutory_licenses").delete().eq("id",id);
    load();
  };

  const startEdit=(l)=>{
    setEditId(l.id);
    setForm({license_name:l.license_name||"",issuing_authority:l.issuing_authority||"",license_type:l.license_type||"",license_number:l.license_number||"",issue_date:l.issue_date||"",expiry_date:l.expiry_date||"",evidence_url:l.evidence_url||"",notes:l.notes||""});
    setShowAdd(true);
  };

  const addTemplate=(t)=>{
    setForm(f=>({...f,license_name:t.name,issuing_authority:t.authority,license_type:t.type}));
  };

  const expired=licenses.filter(l=>getStatus(l.expiry_date).label==="EXPIRED").length;
  const expiring=licenses.filter(l=>getStatus(l.expiry_date).color===T.orange).length;
  const valid=licenses.filter(l=>getStatus(l.expiry_date).color===T.green).length;

  const filtered=filter==="all"?licenses:filter==="expired"?licenses.filter(l=>getStatus(l.expiry_date).label==="EXPIRED"):filter==="expiring"?licenses.filter(l=>getStatus(l.expiry_date).color===T.orange):licenses.filter(l=>getStatus(l.expiry_date).color===T.green);

  const inp={width:"100%",padding:"8px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:"border-box"};

  if(loading)return<div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  return(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:16,fontWeight:700,color:T.gold}}>📋 Statutory License Tracker</div>
          <div style={{fontSize:12,color:T.muted}}>Track all mandatory licenses — get alerted before expiry</div>
        </div>
        <button onClick={()=>{setShowAdd(true);setEditId(null);setForm({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""}); }} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>+ Add License</button>
      </div>

      {/* Summary cards */}
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(120px,1fr))",gap:10,marginBottom:16}}>
        {[["Total",licenses.length,T.blue],["Valid",valid,T.green],["Expiring Soon",expiring,T.orange],["Expired",expired,T.red]].map(([label,count,color])=>(
          <div key={label} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",textAlign:"center"}}>
            <div style={{fontSize:22,fontWeight:800,color}}>{count}</div>
            <div style={{fontSize:11,color:T.muted,marginTop:2}}>{label}</div>
          </div>
        ))}
      </div>

      {/* Filter */}
      <div style={{display:"flex",gap:6,marginBottom:12}}>
        {[["all","All"],["valid","Valid"],["expiring","Expiring"],["expired","Expired"]].map(([val,label])=>(
          <button key={val} onClick={()=>setFilter(val)} style={{padding:"4px 12px",borderRadius:6,border:`1px solid ${filter===val?T.gold:T.border}`,background:filter===val?T.goldD:"transparent",color:filter===val?T.goldL:T.muted,fontSize:11,cursor:"pointer"}}>{label}</button>
        ))}
      </div>

      {/* Add/Edit form */}
      {showAdd&&(
        <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:18,marginBottom:16}}>
          <div style={{fontSize:14,fontWeight:700,color:T.gold,marginBottom:12}}>{editId?"Edit License":"Add New License"}</div>

          {/* Quick templates */}
          {!editId&&(
            <div style={{marginBottom:14}}>
              <div style={{fontSize:11,color:T.muted,marginBottom:6,letterSpacing:1}}>QUICK ADD FROM TEMPLATE</div>
              <div style={{display:"flex",flexWrap:"wrap",gap:5}}>
                {LICENSE_TEMPLATES.map(t=>(
                  <button key={t.name} onClick={()=>addTemplate(t)} style={{padding:"3px 8px",borderRadius:5,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:11,cursor:"pointer"}}>{t.name}</button>
                ))}
              </div>
            </div>
          )}

          <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>LICENSE NAME *</div><input style={inp} value={form.license_name} onChange={e=>setForm(f=>({...f,license_name:e.target.value}))}/></div>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>ISSUING AUTHORITY</div><input style={inp} value={form.issuing_authority} onChange={e=>setForm(f=>({...f,issuing_authority:e.target.value}))}/></div>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>LICENSE NUMBER</div><input style={inp} value={form.license_number} onChange={e=>setForm(f=>({...f,license_number:e.target.value}))}/></div>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>TYPE</div>
              <select style={inp} value={form.license_type} onChange={e=>setForm(f=>({...f,license_type:e.target.value}))}>
                <option value="">Select type…</option>
                {["Safety","Waste","Environmental","Clinical","Regulatory","Infrastructure","Radiation","Accreditation","Quality"].map(t=><option key={t} value={t}>{t}</option>)}
              </select>
            </div>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>ISSUE DATE</div><input style={inp} type="date" value={form.issue_date} onChange={e=>setForm(f=>({...f,issue_date:e.target.value}))}/></div>
            <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>EXPIRY DATE</div><input style={inp} type="date" value={form.expiry_date} onChange={e=>setForm(f=>({...f,expiry_date:e.target.value}))}/></div>
            <div style={{gridColumn:"span 2"}}><div style={{fontSize:11,color:T.muted,marginBottom:4}}>EVIDENCE LINK (Google Drive / OneDrive URL)</div><input style={inp} placeholder="https://drive.google.com/…" value={form.evidence_url} onChange={e=>setForm(f=>({...f,evidence_url:e.target.value}))}/></div>
            <div style={{gridColumn:"span 2"}}><div style={{fontSize:11,color:T.muted,marginBottom:4}}>NOTES</div><input style={inp} placeholder="Renewal in progress, contact person, etc." value={form.notes} onChange={e=>setForm(f=>({...f,notes:e.target.value}))}/></div>
          </div>
          <div style={{display:"flex",gap:8,marginTop:12}}>
            <button onClick={save} disabled={saving||!form.license_name.trim()} style={{padding:"8px 20px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer",opacity:saving?0.6:1}}>{saving?"Saving…":"Save License"}</button>
            <button onClick={()=>{setShowAdd(false);setEditId(null);}} style={{padding:"8px 16px",borderRadius:8,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:13,cursor:"pointer"}}>Cancel</button>
          </div>
        </div>
      )}

      {/* License list */}
      {filtered.length===0?(
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"30px",textAlign:"center",color:T.muted,fontSize:13}}>
          {licenses.length===0?"No licenses added yet. Click '+ Add License' to start tracking.":"No licenses in this filter."}
        </div>
      ):(
        <div style={{display:"grid",gap:8}}>
          {filtered.map(l=>{
            const st=getStatus(l.expiry_date);
            return(
              <div key={l.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",display:"flex",gap:12,alignItems:"center",flexWrap:"wrap"}}>
                <div style={{flex:1,minWidth:180}}>
                  <div style={{fontSize:14,fontWeight:700,color:T.white}}>{l.license_name}</div>
                  <div style={{fontSize:12,color:T.muted,marginTop:2}}>{l.issuing_authority||"—"}{l.license_number&&<span style={{marginLeft:8,color:T.blue}}>#{l.license_number}</span>}</div>
                  {l.notes&&<div style={{fontSize:11,color:T.muted,marginTop:3}}>{l.notes}</div>}
                </div>
                <div style={{textAlign:"center",minWidth:80}}>
                  <div style={{fontSize:11,color:T.muted}}>EXPIRY</div>
                  <div style={{fontSize:13,color:T.text,marginTop:2}}>{l.expiry_date?new Date(l.expiry_date).toLocaleDateString("en-IN",{day:"2-digit",month:"short",year:"numeric"}):"Not set"}</div>
                </div>
                <div style={{padding:"4px 10px",borderRadius:8,background:st.bg,border:`1px solid ${st.color}30`,fontSize:11,fontWeight:700,color:st.color,minWidth:90,textAlign:"center"}}>{st.label}</div>
                {l.license_type&&<div style={{padding:"3px 8px",borderRadius:6,background:T.blueD,border:`1px solid ${T.blue}30`,fontSize:8,color:T.blue}}>{l.license_type}</div>}
                <div style={{display:"flex",gap:6,alignItems:"center"}}>
                  {l.evidence_url&&<a href={l.evidence_url} target="_blank" rel="noopener noreferrer" style={{padding:"4px 10px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 View</a>}
                  <button onClick={()=>startEdit(l)} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:11,cursor:"pointer"}}>Edit</button>
                  <button onClick={()=>del(l.id)} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.red}30`,background:"transparent",color:T.red,fontSize:11,cursor:"pointer"}}>Delete</button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}

// ── PATIENT TRACER ─────────────────────────────────────────────
const TRACER_TYPES = {
  "General IPD": {
    icon:"🛏️",
    color:"#4fc3f7",
    desc:"General inpatient admission tracer",
    questions:[
      {id:"t1",q:"Was the patient triaged and initial assessment completed within 30 minutes of admission?",oe:"AAC.1"},
      {id:"t2",q:"Is a complete nursing assessment documented within 8 hours of admission?",oe:"AAC.2"},
      {id:"t3",q:"Has a medical history and physical examination been completed and documented by a doctor?",oe:"AAC.3"},
      {id:"t4",q:"Is the care plan documented with goals, interventions, and responsible staff?",oe:"COP.1"},
      {id:"t5",q:"Is informed consent obtained and documented before any invasive procedure?",oe:"PRE.4"},
      {id:"t6",q:"Are the patient's rights and responsibilities communicated and acknowledged?",oe:"PRE.1"},
      {id:"t7",q:"Is medication reconciliation done and documented at admission?",oe:"MOM.1"},
      {id:"t8",q:"Are all medications prescribed with generic name, dose, route, frequency?",oe:"MOM.3"},
      {id:"t9",q:"Is the patient's pain assessed and documented using a validated scale?",oe:"COP.2"},
      {id:"t10",q:"Is fall risk assessment done and prevention measures documented?",oe:"PSQ.1"},
      {id:"t11",q:"Is pressure sore risk assessed (Braden/Waterlow scale)?",oe:"COP.3"},
      {id:"t12",q:"Are hand hygiene observations documented for this patient's care team?",oe:"IPC.1"},
      {id:"t13",q:"Is the discharge plan initiated within 24 hours of admission?",oe:"AAC.5"},
      {id:"t14",q:"Is patient/family education documented with language and literacy noted?",oe:"PRE.5"},
      {id:"t15",q:"Are all investigations ordered with clinical indication documented?",oe:"AAC.4"},
    ]
  },
  "Surgical Tracer": {
    icon:"🔪",
    color:"#e05a5a",
    desc:"Pre-op, intra-op, and post-op documentation audit",
    questions:[
      {id:"s1",q:"Is pre-operative assessment completed and documented?",oe:"COP.8"},
      {id:"s2",q:"Is anaesthesia pre-assessment done and signed by anaesthetist?",oe:"COP.9"},
      {id:"s3",q:"Is surgical consent obtained by the operating surgeon (not delegated)?",oe:"PRE.4"},
      {id:"s4",q:"Is anaesthesia consent separately obtained by the anaesthetist?",oe:"PRE.4"},
      {id:"s5",q:"Is the WHO Surgical Safety Checklist completed (Sign-In, Time-Out, Sign-Out)?",oe:"COP.10"},
      {id:"s6",q:"Is the operative note completed within 24 hours of surgery?",oe:"COP.11"},
      {id:"s7",q:"Is post-operative monitoring documented (vitals, pain, drainage)?",oe:"COP.12"},
      {id:"s8",q:"Are prophylactic antibiotics given as per protocol (1 hour pre-incision)?",oe:"IPC.4"},
      {id:"s9",q:"Is the site marking documented pre-operatively for laterality?",oe:"PSQ.3"},
      {id:"s10",q:"Is blood availability confirmed pre-operatively for major surgeries?",oe:"COP.8"},
      {id:"s11",q:"Is VTE prophylaxis assessed and documented?",oe:"COP.3"},
      {id:"s12",q:"Is implant register updated if any implant was used?",oe:"COP.11"},
      {id:"s13",q:"Is the specimen sent to histopathology with proper labeling?",oe:"AAC.4"},
      {id:"s14",q:"Is immediate post-op note written in OT itself?",oe:"COP.11"},
      {id:"s15",q:"Is patient transferred to recovery room with documented handover?",oe:"COP.12"},
    ]
  },
  "ICU Tracer": {
    icon:"🫀",
    color:"#f4a441",
    desc:"Critical care bundle compliance and documentation",
    questions:[
      {id:"i1",q:"Is ICU admission note with APACHE II score documented?",oe:"COP.5"},
      {id:"i2",q:"Are daily ICU rounds documented with goals of care?",oe:"COP.5"},
      {id:"i3",q:"Is VAP bundle compliance documented (HOB elevation, oral care, cuff pressure)?",oe:"IPC.5"},
      {id:"i4",q:"Is CLABSI bundle documented for all central lines (insertion + daily care)?",oe:"IPC.6"},
      {id:"i5",q:"Is CAUTI prevention bundle documented for all urinary catheters?",oe:"IPC.7"},
      {id:"i6",q:"Are ventilator settings and changes documented with rationale?",oe:"COP.5"},
      {id:"i7",q:"Is sedation/analgesia scale used and documented (RASS/VAS)?",oe:"COP.2"},
      {id:"i8",q:"Is daily spontaneous breathing trial documented for ventilated patients?",oe:"COP.5"},
      {id:"i9",q:"Is family communication documented at least once in 24 hours?",oe:"PRE.3"},
      {id:"i10",q:"Is fluid balance charted every 6 hours?",oe:"COP.5"},
      {id:"i11",q:"Are blood glucose monitoring results documented per protocol?",oe:"COP.6"},
      {id:"i12",q:"Is DVT prophylaxis assessed and documented?",oe:"COP.3"},
      {id:"i13",q:"Is restraint use (if any) documented with consent and hourly monitoring?",oe:"COP.7"},
      {id:"i14",q:"Is end-of-life care plan documented for terminal patients?",oe:"COP.4"},
      {id:"i15",q:"Is ICU transfer note written when patient is shifted to ward?",oe:"AAC.5"},
    ]
  },
  "Emergency Tracer": {
    icon:"🚨",
    color:"#e05a5a",
    desc:"Emergency department triage and documentation",
    questions:[
      {id:"e1",q:"Is triage done within 5 minutes of arrival using validated triage scale?",oe:"AAC.1"},
      {id:"e2",q:"Is triage category documented and consistent with patient condition?",oe:"AAC.1"},
      {id:"e3",q:"Are vitals documented at arrival and at regular intervals?",oe:"AAC.2"},
      {id:"e4",q:"Is MLC (Medico-Legal Case) identification and reporting documented?",oe:"ROM.6"},
      {id:"e5",q:"Is police intimation documented for MLC cases?",oe:"ROM.6"},
      {id:"e6",q:"Is time of doctor assessment from arrival documented?",oe:"AAC.1"},
      {id:"e7",q:"Is ABCDE assessment documented for critical patients?",oe:"COP.1"},
      {id:"e8",q:"Is informed consent obtained before any procedure?",oe:"PRE.4"},
      {id:"e9",q:"Is drug allergy checked before administering medications?",oe:"MOM.5"},
      {id:"e10",q:"Is reason for admission or discharge documented?",oe:"AAC.3"},
      {id:"e11",q:"Is social history (domestic violence, child abuse) screened if applicable?",oe:"PRE.1"},
      {id:"e12",q:"Is LAMA (Leave Against Medical Advice) documented with informed refusal?",oe:"PRE.1"},
      {id:"e13",q:"Is disaster/mass casualty procedure documentation available?",oe:"FMS.7"},
      {id:"e14",q:"Is crash cart checked and documented as per protocol?",oe:"FMS.3"},
      {id:"e15",q:"Is referral documentation complete if patient transferred to another facility?",oe:"AAC.6"},
    ]
  },
  "Maternity Tracer": {
    icon:"🤱",
    color:"#c084e8",
    desc:"Labour room and maternity care documentation",
    questions:[
      {id:"m1",q:"Is antenatal history documented completely on admission?",oe:"COP.13"},
      {id:"m2",q:"Is partograph initiated and maintained from active labour?",oe:"COP.13"},
      {id:"m3",q:"Is fetal heart rate monitoring documented every 30 minutes in active labour?",oe:"COP.13"},
      {id:"m4",q:"Is consent for delivery (normal/caesarean) documented?",oe:"PRE.4"},
      {id:"m5",q:"Is oxytocin administration documented with dose, rate, and monitoring?",oe:"MOM.3"},
      {id:"m6",q:"Is birth register updated with all mandatory fields?",oe:"IMS.2"},
      {id:"m7",q:"Is APGAR score documented at 1 and 5 minutes?",oe:"COP.14"},
      {id:"m8",q:"Is vitamin K prophylaxis given and documented for newborn?",oe:"COP.14"},
      {id:"m9",q:"Is breast feeding initiation documented within 1 hour of birth?",oe:"COP.14"},
      {id:"m10",q:"Is blood loss quantified and documented in delivery note?",oe:"COP.13"},
      {id:"m11",q:"Is PPH prevention protocol (oxytocin) documented?",oe:"COP.13"},
      {id:"m12",q:"Is newborn screening documented as per national programme?",oe:"COP.14"},
      {id:"m13",q:"Is placental disposal documented per BMW rules?",oe:"IPC.9"},
      {id:"m14",q:"Is maternal death reporting (if any) done as per protocol?",oe:"PSQ.6"},
      {id:"m15",q:"Is discharge summary for mother and baby both documented?",oe:"AAC.5"},
    ]
  },
  "Medication Tracer": {
    icon:"💊",
    color:"#4caf7d",
    desc:"Medication management and high-alert drug compliance",
    questions:[
      {id:"med1",q:"Are LASA (Look-Alike Sound-Alike) drugs identified and separately stored?",oe:"MOM.2"},
      {id:"med2",q:"Are high-alert medications labeled and stored with double-check protocol?",oe:"MOM.2"},
      {id:"med3",q:"Are narcotics/controlled substances in a locked cabinet with dual custody?",oe:"MOM.6"},
      {id:"med4",q:"Is narcotics register maintained with all mandatory columns?",oe:"MOM.6"},
      {id:"med5",q:"Is medication administration documented with time, dose, route, and nurse signature?",oe:"MOM.5"},
      {id:"med6",q:"Are medication errors reported through incident reporting system?",oe:"MOM.7"},
      {id:"med7",q:"Are near-miss medication events also captured in incident reports?",oe:"PSQ.4"},
      {id:"med8",q:"Is expiry date checked before dispensing — no expired drugs in wards?",oe:"MOM.3"},
      {id:"med9",q:"Is medication reconciliation done at discharge?",oe:"MOM.1"},
      {id:"med10",q:"Are PRN (as needed) medications administered with documented indication?",oe:"MOM.5"},
      {id:"med11",q:"Is IV fluid administration documented with rate and total volume?",oe:"MOM.5"},
      {id:"med12",q:"Are adverse drug reactions documented and reported to pharmacovigilance?",oe:"MOM.7"},
      {id:"med13",q:"Is patient counselling on medications documented at discharge?",oe:"PRE.5"},
      {id:"med14",q:"Are antibiotic prescriptions following hospital antibiotic policy?",oe:"IPC.4"},
      {id:"med15",q:"Is chemotherapy (if any) prescribed and administered per double-check protocol?",oe:"MOM.4"},
    ]
  },
  "Blood Transfusion": {
    icon:"🩸",
    color:"#e05a5a",
    desc:"Blood bank and transfusion safety compliance",
    questions:[
      {id:"b1",q:"Is consent for blood transfusion obtained separately?",oe:"PRE.4"},
      {id:"b2",q:"Is blood request form complete with clinical indication?",oe:"COP.15"},
      {id:"b3",q:"Is pre-transfusion blood grouping and cross-matching documented?",oe:"COP.15"},
      {id:"b4",q:"Is bedside verification (2-person check) documented before starting transfusion?",oe:"PSQ.3"},
      {id:"b5",q:"Are vital signs documented before, during (15 min), and after transfusion?",oe:"COP.15"},
      {id:"b6",q:"Is transfusion reaction protocol available and followed?",oe:"COP.15"},
      {id:"b7",q:"Are transfusion reactions reported through haemovigilance system?",oe:"PSQ.4"},
      {id:"b8",q:"Is blood issue time and transfusion completion time documented?",oe:"COP.15"},
      {id:"b9",q:"Is blood returned to blood bank if not transfused within 30 min?",oe:"COP.15"},
      {id:"b10",q:"Is blood bag discarded as per BMW rules after transfusion?",oe:"IPC.9"},
    ]
  },
  "Document Tracer": {
    icon:"📄",
    color:"#90caf9",
    desc:"Medical record completeness and documentation standards",
    questions:[
      {id:"d1",q:"Is the admission note completed within 24 hours with all mandatory fields?",oe:"IMS.1"},
      {id:"d2",q:"Are all entries dated, timed, and signed with designation?",oe:"IMS.3"},
      {id:"d3",q:"Are corrections made by crossing out (not erasing) with date/sign?",oe:"IMS.3"},
      {id:"d4",q:"Is the discharge summary completed within 24 hours of discharge?",oe:"AAC.5"},
      {id:"d5",q:"Does the discharge summary contain all 10 mandatory elements?",oe:"AAC.5"},
      {id:"d6",q:"Are medical records stored securely with access control?",oe:"IMS.5"},
      {id:"d7",q:"Are medical records available within 30 minutes for emergency access?",oe:"IMS.5"},
      {id:"d8",q:"Is patient identity verified using at least 2 identifiers on all documents?",oe:"PSQ.2"},
      {id:"d9",q:"Are all diagnostic reports signed by the reporting doctor?",oe:"IMS.2"},
      {id:"d10",q:"Is the medical record complete before filing (deficiency tracking)?",oe:"IMS.4"},
    ]
  }
};

function PatientTracerScreen({ hospitalId }) {
  const [view,setView]=useState("list"); // list | new | conduct | history
  const [tracerType,setTracerType]=useState("General IPD");
  const [tracers,setTracers]=useState([]);
  const [loading,setLoading]=useState(true);
  const [activeTracer,setActiveTracer]=useState(null);
  const [responses,setResponses]=useState({});
  const [meta,setMeta]=useState({patient_ref:"",conducted_by:"",conducted_date:new Date().toISOString().split("T")[0],notes:""});
  const [saving,setSaving]=useState(false);

  useEffect(()=>{loadTracers();},[hospitalId]);

  const loadTracers=async()=>{
    setLoading(true);
    const{data}=await supabase.from("patient_tracers").select("*").eq("hospital_id",hospitalId).order("created_at",{ascending:false});
    setTracers(data||[]);setLoading(false);
  };

  const startNew=()=>{
    setResponses({});
    setMeta({patient_ref:"",conducted_by:"",conducted_date:new Date().toISOString().split("T")[0],notes:""});
    setActiveTracer(null);
    setView("new");
  };

  const startConduct=()=>{
    setView("conduct");
  };

  const setResp=(qid,val)=>setResponses(r=>({...r,[qid]:val}));

  const calcScore=()=>{
    const qs=TRACER_TYPES[tracerType].questions;
    const answered=qs.filter(q=>responses[q.id]==="yes"||responses[q.id]==="partial"||responses[q.id]==="no");
    if(answered.length===0)return 0;
    const score=qs.reduce((sum,q)=>sum+(responses[q.id]==="yes"?1:responses[q.id]==="partial"?0.5:0),0);
    return Math.round((score/qs.length)*100);
  };

  const saveTracer=async()=>{
    setSaving(true);
    const pct=calcScore();
    await supabase.from("patient_tracers").insert({
      hospital_id:hospitalId,
      tracer_type:tracerType,
      patient_ref:meta.patient_ref,
      conducted_date:meta.conducted_date,
      conducted_by:meta.conducted_by,
      responses,
      score_pct:pct,
      notes:meta.notes
    });
    setSaving(false);
    loadTracers();
    setView("list");
  };

  const scoreColor=(pct)=>pct>=80?T.green:pct>=60?T.orange:T.red;

  const inp={width:"100%",padding:"8px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:"border-box"};

  if(loading)return<div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  // LIST VIEW
  if(view==="list")return(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:16,fontWeight:700,color:T.gold}}>🩺 Patient Tracer</div>
          <div style={{fontSize:12,color:T.muted}}>Simulate assessor patient file review — identify gaps before they do</div>
        </div>
        <button onClick={startNew} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>+ New Tracer</button>
      </div>

      {/* Tracer type cards */}
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(160px,1fr))",gap:10,marginBottom:20}}>
        {Object.entries(TRACER_TYPES).map(([type,data])=>{
          const done=tracers.filter(t=>t.tracer_type===type);
          const avg=done.length>0?Math.round(done.reduce((s,t)=>s+t.score_pct,0)/done.length):null;
          return(
            <div key={type} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px",cursor:"pointer"}} onClick={()=>{setTracerType(type);startNew();}}>
              <div style={{fontSize:20,marginBottom:6}}>{data.icon}</div>
              <div style={{fontSize:13,fontWeight:700,color:T.white,marginBottom:3}}>{type}</div>
              <div style={{fontSize:11,color:T.muted,marginBottom:8,lineHeight:1.4}}>{data.questions.length} questions</div>
              {avg!==null?(
                <div style={{fontSize:12,fontWeight:700,color:scoreColor(avg)}}>{avg}% avg ({done.length} done)</div>
              ):(
                <div style={{fontSize:11,color:T.muted}}>Not conducted yet</div>
              )}
            </div>
          );
        })}
      </div>

      {/* History */}
      {tracers.length>0&&(
        <>
          <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:10}}>Recent Tracers</div>
          <div style={{display:"grid",gap:8}}>
            {tracers.slice(0,10).map(t=>(
              <div key={t.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px 16px",display:"flex",gap:12,alignItems:"center",flexWrap:"wrap"}}>
                <div style={{fontSize:18}}>{TRACER_TYPES[t.tracer_type]?.icon||"🩺"}</div>
                <div style={{flex:1,minWidth:150}}>
                  <div style={{fontSize:13,fontWeight:700,color:T.white}}>{t.tracer_type}</div>
                  <div style={{fontSize:11,color:T.muted}}>{t.patient_ref&&`Patient: ${t.patient_ref} · `}{t.conducted_by&&`By: ${t.conducted_by} · `}{new Date(t.conducted_date).toLocaleDateString("en-IN")}</div>
                </div>
                <div style={{textAlign:"center"}}>
                  <div style={{fontSize:18,fontWeight:800,color:scoreColor(t.score_pct)}}>{t.score_pct}%</div>
                  <div style={{fontSize:8,color:T.muted}}>Score</div>
                </div>
                <div style={{padding:"3px 10px",borderRadius:7,background:t.score_pct>=80?T.greenD:t.score_pct>=60?T.orangeD:T.redD,color:scoreColor(t.score_pct),fontSize:11,fontWeight:700}}>
                  {t.score_pct>=80?"READY":t.score_pct>=60?"PARTIAL":"NOT READY"}
                </div>
              </div>
            ))}
          </div>
        </>
      )}

      {tracers.length===0&&(
        <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"30px",textAlign:"center",color:T.muted,fontSize:13}}>
          No tracers conducted yet. Click a tracer type above or '+ New Tracer' to start.
        </div>
      )}
    </div>
  );

  // NEW TRACER — select type + meta
  if(view==="new")return(
    <div>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:16}}>
        <button onClick={()=>setView("list")} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:12,cursor:"pointer"}}>← Back</button>
        <div style={{fontSize:15,fontWeight:700,color:T.gold}}>New Patient Tracer</div>
      </div>

      {/* Select tracer type */}
      <div style={{fontSize:11,color:T.muted,marginBottom:8,letterSpacing:1}}>SELECT TRACER TYPE</div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(140px,1fr))",gap:8,marginBottom:18}}>
        {Object.entries(TRACER_TYPES).map(([type,data])=>(
          <div key={type} onClick={()=>setTracerType(type)} style={{background:tracerType===type?`${data.color}15`:T.panel,border:`1px solid ${tracerType===type?data.color:T.border}`,borderRadius:9,padding:"10px",cursor:"pointer",textAlign:"center"}}>
            <div style={{fontSize:18,marginBottom:4}}>{data.icon}</div>
            <div style={{fontSize:12,fontWeight:700,color:tracerType===type?data.color:T.text}}>{type}</div>
            <div style={{fontSize:8,color:T.muted,marginTop:2}}>{data.questions.length}Q</div>
          </div>
        ))}
      </div>

      {/* Meta info */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:16,marginBottom:14}}>
        <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:12}}>Tracer Details (Optional)</div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
          <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>PATIENT REF / FILE NO.</div><input style={inp} placeholder="e.g. IPD/2026/1234" value={meta.patient_ref} onChange={e=>setMeta(m=>({...m,patient_ref:e.target.value}))}/></div>
          <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>CONDUCTED BY</div><input style={inp} placeholder="Name / Designation" value={meta.conducted_by} onChange={e=>setMeta(m=>({...m,conducted_by:e.target.value}))}/></div>
          <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>DATE</div><input style={inp} type="date" value={meta.conducted_date} onChange={e=>setMeta(m=>({...m,conducted_date:e.target.value}))}/></div>
          <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>NOTES</div><input style={inp} placeholder="Any observations…" value={meta.notes} onChange={e=>setMeta(m=>({...m,notes:e.target.value}))}/></div>
        </div>
      </div>

      <button onClick={startConduct} style={{width:"100%",padding:"12px",borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:15,fontWeight:700,cursor:"pointer"}}>
        Start {tracerType} Tracer ({TRACER_TYPES[tracerType].questions.length} questions) →
      </button>
    </div>
  );

  // CONDUCT TRACER — answer questions
  if(view==="conduct"){
    const tdata=TRACER_TYPES[tracerType];
    const answered=tdata.questions.filter(q=>responses[q.id]).length;
    const pct=calcScore();

    return(
      <div>
        <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:12,flexWrap:"wrap"}}>
          <button onClick={()=>setView("new")} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:12,cursor:"pointer"}}>← Back</button>
          <div style={{flex:1}}>
            <div style={{fontSize:15,fontWeight:700,color:tdata.color}}>{tdata.icon} {tracerType}</div>
            <div style={{fontSize:11,color:T.muted}}>{answered}/{tdata.questions.length} answered · Score: {pct}%</div>
          </div>
          <button onClick={saveTracer} disabled={saving} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer",opacity:saving?0.6:1}}>{saving?"Saving…":"Save & Finish"}</button>
        </div>

        {/* Progress bar */}
        <div style={{background:T.border,borderRadius:4,height:6,marginBottom:16}}>
          <div style={{height:6,borderRadius:4,background:`linear-gradient(90deg,${tdata.color},${T.gold})`,width:`${(answered/tdata.questions.length)*100}%`,transition:"width 0.3s"}}/>
        </div>

        <div style={{display:"grid",gap:8}}>
          {tdata.questions.map((q,idx)=>{
            const resp=responses[q.id];
            return(
              <div key={q.id} style={{background:T.panel,border:`1px solid ${resp?"#0f2640":T.border}`,borderRadius:10,padding:"12px 16px"}}>
                <div style={{display:"flex",gap:10,alignItems:"flex-start"}}>
                  <div style={{width:22,height:22,borderRadius:11,background:resp==="yes"?T.greenD:resp==="partial"?T.orangeD:resp==="no"?T.redD:T.panel2,border:`1px solid ${resp==="yes"?T.green:resp==="partial"?T.orange:resp==="no"?T.red:T.border}`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:11,fontWeight:700,color:resp==="yes"?T.green:resp==="partial"?T.orange:resp==="no"?T.red:T.muted,flexShrink:0,marginTop:1}}>{idx+1}</div>
                  <div style={{flex:1}}>
                    <div style={{fontSize:13,color:T.white,lineHeight:1.5,marginBottom:8}}>{q.q}</div>
                    <div style={{fontSize:8,color:T.muted,marginBottom:8}}>OE: {q.oe}</div>
                    <div style={{display:"flex",gap:8}}>
                      {[["yes","✓ Yes",T.green],["partial","~ Partial",T.orange],["no","✗ No",T.red]].map(([val,label,color])=>(
                        <button key={val} onClick={()=>setResp(q.id,resp===val?null:val)}
                          style={{padding:"5px 14px",borderRadius:7,border:`1px solid ${resp===val?color:T.border}`,background:resp===val?`${color}20`:"transparent",color:resp===val?color:T.muted,fontSize:12,fontWeight:resp===val?700:400,cursor:"pointer"}}>
                          {label}
                        </button>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        <div style={{marginTop:16,background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"14px 18px",display:"flex",justifyContent:"space-between",alignItems:"center"}}>
          <div>
            <div style={{fontSize:13,color:T.text}}>{answered} of {tdata.questions.length} questions answered</div>
            <div style={{fontSize:11,color:T.muted,marginTop:2}}>Score: <span style={{color:scoreColor(pct),fontWeight:700}}>{pct}%</span> — {pct>=80?"Ready for assessment":pct>=60?"Needs improvement":"Critical gaps found"}</div>
          </div>
          <button onClick={saveTracer} disabled={saving} style={{padding:"9px 22px",borderRadius:9,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:14,fontWeight:700,cursor:"pointer",opacity:saving?0.6:1}}>{saving?"Saving…":"Save & Finish"}</button>
        </div>
      </div>
    );
  }

  return null;
}
