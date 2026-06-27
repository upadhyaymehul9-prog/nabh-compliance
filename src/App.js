import { useState, useEffect, useCallback, useRef } from "react";
import { createClient } from "@supabase/supabase-js";
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, Tooltip, ReferenceLine, ResponsiveContainer, CartesianGrid } from "recharts";
import jsPDF from 'jspdf';
import AIAssistantWidget from "./components/AIAssistantWidget";
import HomepageScreen from "./components/HomepageScreen";

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


const SHCO_ELC_PROCESS = [
  {step:1,name:"Register on HOPE Portal",url:"hope.qcin.org",desc:"Go to hope.qcin.org → Register → Fill hospital details",output:"Login credentials + application ID"},
  {step:2,name:"Fill 7-Part Questionnaire",url:"hope.qcin.org",desc:"Complete all 7 parts of the HOPE questionnaire online — General Info, Physical Infrastructure, Statutory, Clinical, Staffing, Quality, Documentation",output:"Completed questionnaire submission"},
  {step:3,name:"Upload Documents",url:"hope.qcin.org",desc:"Upload portal documents via web portal + mobile app documents via HOPE mobile app",output:"Document submission complete"},
  {step:4,name:"Pay Fee",url:"hope.qcin.org",desc:"Pay the applicable certification fee based on your bed strength. For current fees, visit the official NABH website (nabh.co).",output:"Payment receipt + application confirmed"},
  {step:5,name:"Desktop Assessment (DA)",url:"",desc:"NABH desk team reviews all submitted documents. NCs raised online. Two rounds of NC closure available at DA stage.",output:"NC closure letter"},
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
  {id:"065",part:"II",section:"Utilities & Infrastructure",text:"Elevators present? (Certificate of Lift License/Safety via Portal)",upload:"Portal",type:"field"},
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
  {ch:"AAC",name:"Access, Assessment and Continuity of Care",oes:29,desc:"Defines scope of services, registration, initial assessment, laboratory/imaging services, discharge process"},
  {ch:"COP",name:"Care of Patients",oes:44,desc:"Uniform care delivery, emergency services, ICU, obstetric, paediatric, anaesthesia, surgical and rehabilitation care"},
  {ch:"MOM",name:"Management of Medication",oes:28,desc:"Safe pharmacy services, medication storage, prescription, dispensing, administration and high-risk medication management"},
  {ch:"PRE",name:"Patient Rights and Education",oes:17,desc:"Patient and family rights, informed consent, patient education and feedback mechanisms"},
  {ch:"IPC",name:"Infection Prevention and Control",oes:12,desc:"Infection prevention programme, hand hygiene, biomedical waste management, sterilization practices"},
  {ch:"PSQ",name:"Patient Safety and Quality Improvement",oes:8,desc:"Quality improvement programme, patient safety goals, key indicators monitoring and clinical audits"},
  {ch:"ROM",name:"Responsibilities of Management",oes:12,desc:"Governance, statutory compliance, ethical management, outsourced services and sustainability"},
  {ch:"FMS",name:"Facility Management and Safety",oes:13,desc:"Infrastructure safety, equipment maintenance, utility systems, fire and emergency preparedness"},
  {ch:"HRM",name:"Human Resource Management",oes:15,desc:"Staff mix, training, performance appraisal, occupational health and staff welfare"},
  {ch:"IMS",name:"Information Management System",oes:11,desc:"Medical record management, confidentiality, document control and digital health"},
];

const ELC_OE_TIPS = {
  'AAC1a': {
    tip_1: 'Define all healthcare services your facility provides in a formal written document approved by the medical director, covering OPD, IPD, emergency, diagnostics and support services.',
    tip_2: 'Maintain a Service Scope Register listing every specialty, procedure and ancillary service offered, updated whenever services are added or removed.',
    tip_3: 'Audit the service list quarterly against actual billing data and active departments to confirm no service is rendered outside the approved scope.',
    tip_4: 'Train department heads to review the defined service list at onboarding and whenever the scope changes, so all staff know exactly what services the hospital offers.'
  },
  'AAC1b': {
    tip_1: 'Display the complete list of healthcare services on notice boards at reception, OPD waiting area and main entrance in languages patients understand.',
    tip_2: 'Post laminated signage boards listing specialties, timings and consulting doctors at every patient-facing area and update them within 48 hours of any change.',
    tip_3: 'Check during monthly facility rounds that all service display boards are current, legible, undamaged and match the approved service scope register.',
    tip_4: 'Instruct housekeeping and front-desk staff to report damaged or outdated display boards immediately so corrections are made before the next patient visit.'
  },
  'AAC1c': {
    tip_1: 'Ensure every defined clinical service has at least one qualified medical officer covering OPD slots, IPD rounds and emergency call duty at all times.',
    tip_2: 'Maintain a coverage matrix document showing each service, the assigned qualified doctor, duty roster and on-call backup for OPD, IPD and emergency.',
    tip_3: 'Verify monthly that no service gap exists by cross-checking the duty roster against the service scope list and flagging any uncovered shifts to HR.',
    tip_4: 'Brief resident doctors and nursing staff at each shift handover about which specialist is on call for each service so emergency escalation is immediate.'
  },
  'AAC2a': {
    tip_1: 'Establish a written SOP covering the full registration and admission workflow for OPD, day-care, IPD and emergency patients, including steps, responsible staff and timelines.',
    tip_2: 'Keep the registration SOP accessible at the front desk and admission counter; include a patient flow chart on the wall showing each step visually.',
    tip_3: 'Audit patient registration records monthly to confirm all mandatory fields are captured and the process follows the written SOP without deviation.',
    tip_4: 'Train all reception and admission staff on the SOP during induction and refresh annually, with role-play exercises covering OPD, emergency and day-care scenarios.'
  },
  'AAC2b': {
    tip_1: 'Configure the hospital information system to auto-generate a unique patient identification number at the point of registration completion before any clinical activity begins.',
    tip_2: 'Print or display the unique ID on the wristband, prescription header, lab requisition and all patient documents so it links every record to one patient.',
    tip_3: 'Review registration logs weekly to detect any duplicate IDs or registrations completed without a unique number and fix the root cause immediately.',
    tip_4: 'Train front-desk staff that no patient may proceed to clinical areas until a unique ID has been generated and attached to all their documents.'
  },
  'AAC2c': {
    tip_1: 'Define a clear transfer and referral procedure covering internal transfers between units, outward referrals to higher centres and inward transfers from other facilities, including documentation and consent steps.',
    tip_2: 'Use a standardised transfer form capturing patient condition, reason for transfer, treatment given, receiving facility details and accompanying personnel.',
    tip_3: 'Review all transfer and referral records monthly to verify documentation completeness, patient stability at transfer and availability of referral acceptance confirmation.',
    tip_4: 'Train ward nurses and casualty staff on transfer SOP including how to stabilise the patient, fill the transfer form correctly and communicate with the receiving team.'
  },
  'AAC3a': {
    tip_1: 'Implement a standardised initial assessment form for OPD, day-care, IPD and emergency that captures chief complaint, history, vitals, physical exam and provisional diagnosis in a consistent format.',
    tip_2: 'Use printed or electronic structured assessment templates for each patient category so every clinician collects the same minimum data set at first contact.',
    tip_3: 'Audit 10 records per week across patient types to check that initial assessments are complete, signed and completed within defined timeframes.',
    tip_4: 'Orient all new doctors and nurses to the assessment templates during induction; hold quarterly case-based sessions to reinforce consistent documentation practice.'
  },
  'AAC3b': {
    tip_1: 'Require that every admitted patient has a documented care plan in the medical record within the time frame defined by hospital policy, covering diagnosis, planned investigations, treatment goals and expected discharge date.',
    tip_2: 'Use a dedicated care plan section in the case sheet that is signed by the treating doctor, specifying investigations, medications, procedures and review schedule.',
    tip_3: 'Conduct weekly medical record audits to confirm every in-patient file contains a completed and updated care plan with no gaps beyond the defined timeframe.',
    tip_4: 'Train junior doctors that writing a care plan is mandatory at admission, not optional, and include care plan documentation in their competency assessment checklist.'
  },
  'AAC4a': {
    tip_1: 'Assign a named primary treating doctor for every admitted patient at the time of admission and document that doctor\'\'s name prominently in the case sheet and on the bed-head ticket.',
    tip_2: 'Display the treating doctor\'\'s name on the patient\'\'s bedside card and record it in the admission register so all staff and family know who is responsible.',
    tip_3: 'Check during weekly medical record review that every in-patient record shows a named responsible doctor; escalate gaps to the medical superintendent immediately.',
    tip_4: 'Brief nursing staff at each shift that they must know the name of the responsible doctor for every patient in their ward to ensure correct escalation.'
  },
  'AAC4b': {
    tip_1: 'Establish a policy requiring documented reassessment of every in-patient at defined intervals, with findings, response to treatment and updated management plan noted in the case sheet.',
    tip_2: 'Use a structured reassessment note template that prompts recording of current vitals, symptom changes, investigation results and any plan modifications.',
    tip_3: 'Audit 10 case sheets per week to verify reassessment notes are present at the required intervals, are signed and contain clinical content not just routine entries.',
    tip_4: 'Train residents and nurses that timely reassessment documentation is a patient safety measure; include it in daily rounds checklists and handover briefings.'
  },
  'AAC4c': {
    tip_1: 'Implement an early warning score system such as NEWS2 or a locally adapted equivalent so any deteriorating patient triggers a defined escalation response.',
    tip_2: 'Document early warning scores on observation charts at every nursing round; ensure the escalation protocol with contact numbers is posted at each nursing station.',
    tip_3: 'Review all rapid-response or code blue activations monthly to assess whether early warning signs were identified and acted upon promptly.',
    tip_4: 'Train all ward nurses and resident doctors to calculate early warning scores, interpret the result and initiate escalation without waiting for senior approval.'
  },
  'AAC4d': {
    tip_1: 'Implement a structured handover tool such as SBAR for all shift changes and inter-unit transfers so critical patient information is communicated consistently.',
    tip_2: 'Record each handover in the nursing notes or handover register, capturing patient status, pending tasks, risk alerts and the name of the incoming staff member.',
    tip_3: 'Observe and score at least two handovers per week per ward using a checklist; share findings at the monthly nursing quality meeting.',
    tip_4: 'Train all nursing and resident medical staff on the SBAR handover format during induction and simulate a high-risk transfer scenario in quarterly drills.'
  },
  'AAC5a': {
    tip_1: 'Ensure the laboratory offers tests that match the clinical services provided by the hospital; any gap must be filled by an outsourced arrangement with a NABL-accredited lab.',
    tip_2: 'Maintain a laboratory services catalogue listing all available tests, turnaround times and reference ranges, updated whenever a new test is added or dropped.',
    tip_3: 'Review the test catalogue against clinical service scope annually and after any new department opens to confirm laboratory coverage is adequate.',
    tip_4: 'Inform doctors at departmental meetings about the current test menu, any new tests added and the process for ordering tests not available in-house.'
  },
  'AAC5b': {
    tip_1: 'Follow written procedures for every stage of specimen management: test requisition, collection technique, patient and sample labelling, safe transport, processing steps and final disposal.',
    tip_2: 'Use pre-printed specimen requisition forms with patient ID, test name, collection time and collector name; label all specimens at the bedside before transport.',
    tip_3: 'Conduct monthly observation audits in the lab and wards to verify staff follow the specimen SOP; record findings and correct deviations within 24 hours.',
    tip_4: 'Train phlebotomists and ward nurses on specimen collection, labelling and rejection criteria at induction; revalidate competency every year with a practical assessment.'
  },
  'AAC5c': {
    tip_1: 'Define turnaround times for all test categories, display them in the lab and ensure critical values are telephoned to the treating team immediately and documented.',
    tip_2: 'Record all critical value notifications in a dedicated register showing the test result, time called, staff who called, recipient name and time of acknowledgement.',
    tip_3: 'Audit critical value notification records monthly to confirm all results were communicated within the defined window and that acknowledgement was documented.',
    tip_4: 'Train lab staff on critical value thresholds for each test and the mandatory protocol for immediately calling the ward and documenting the communication.'
  },
  'AAC5d': {
    tip_1: 'Implement a laboratory safety programme covering chemical and biological hazard handling, PPE use, needle-stick injury protocol, spill management and waste segregation.',
    tip_2: 'Maintain a lab safety manual at the workstation along with a safety incident log, PPE inventory record and up-to-date MSDS sheets for all hazardous chemicals.',
    tip_3: 'Conduct monthly safety observation rounds in the lab and review all needle-stick or exposure incidents within 24 hours to implement corrective actions.',
    tip_4: 'Train all laboratory staff on safety protocols during induction; repeat annual refresher with a scenario-based exercise covering spill response and exposure reporting.'
  },
  'AAC5e': {
    tip_1: 'Run an internal quality assurance programme in the laboratory including daily internal quality controls, participation in external quality assessment schemes and periodic equipment calibration.',
    tip_2: 'Document all QC results, EQA reports, instrument calibration records and corrective actions in a QA register accessible to the lab in-charge.',
    tip_3: 'Review QC trends weekly and EQA results each cycle; escalate persistent failures to the quality committee with a root cause analysis and action plan.',
    tip_4: 'Train lab staff on the importance of running controls before patient samples, interpreting Levey-Jennings charts and reporting QC failures immediately.'
  },
  'AAC5f': {
    tip_1: 'Select outsourced labs based on documented evidence of quality assurance such as NABL accreditation or equivalent; review credentials before signing any service agreement.',
    tip_2: 'Maintain a file for each outsourced lab containing the MoU, quality certification, contact details and a record of periodic performance reviews.',
    tip_3: 'Review outsourced lab turnaround times and report quality quarterly; raise concerns formally if results are frequently delayed or discrepant.',
    tip_4: 'Inform clinical staff which tests are outsourced, the expected turnaround time and the process for urgent outsourced tests so patient care is not delayed.'
  },
  'AAC6a': {
    tip_1: 'Obtain and maintain all regulatory licences required for imaging services including AERB registration for X-ray and CT, and ensure renewals are tracked with a 90-day advance alert.',
    tip_2: 'Keep a compliance register in the radiology department listing each licence, issuing authority, issue date, expiry date and current status.',
    tip_3: 'Audit the licence register quarterly and cross-check with equipment inventory to confirm no imaging equipment is operated without a valid licence.',
    tip_4: 'Brief radiology in-charge and technicians that operating imaging equipment with an expired or absent licence is a legal violation that must be reported immediately.'
  },
  'AAC6b': {
    tip_1: 'Define the scope of imaging services to match the clinical specialties offered by the hospital; any imaging not available in-house must have an outsourcing arrangement in place.',
    tip_2: 'Publish an imaging services catalogue listing modalities available such as X-ray, ultrasound, CT, MRI, and display it in the radiology waiting area.',
    tip_3: 'Review the imaging scope annually against clinical service growth and confirm that new imaging services are added only with proper equipment, staff and licences.',
    tip_4: 'Educate clinicians at departmental meetings about available imaging modalities, turnaround times and the referral process for imaging not offered in-house.'
  },
  'AAC6c': {
    tip_1: 'Set defined turnaround times for each imaging type, display them in radiology and ensure critical imaging findings are communicated to the treating doctor immediately.',
    tip_2: 'Record all critical imaging findings in a communication log showing the finding, time reported, radiologist or technician name, recipient and time of acknowledgement.',
    tip_3: 'Review the imaging communication log monthly to confirm all critical findings were conveyed within the defined time window and that acknowledgement was recorded.',
    tip_4: 'Train radiologists, technicians and ward staff on which imaging findings are classified critical and the mandatory immediate verbal-then-written communication protocol.'
  },
  'AAC6d': {
    tip_1: 'Implement a radiation safety programme covering patient and staff dose monitoring, proper use of protective equipment, pregnancy screening before imaging and radiation incident reporting.',
    tip_2: 'Post radiation safety instructions and dose monitoring records in the imaging room; maintain a staff dosimetry register with monthly TLD badge readings.',
    tip_3: 'Review dosimetry reports monthly and investigate any reading above the reference level; conduct quarterly safety walk-throughs of all imaging areas.',
    tip_4: 'Train all radiology staff on radiation protection principles, correct use of lead aprons and shields, and the protocol for reporting any radiation incident or near-miss.'
  },
  'AAC6e': {
    tip_1: 'Establish a quality assurance programme for imaging covering equipment calibration, image quality testing, reject analysis and participation in external quality assessment.',
    tip_2: 'Maintain a QA register in radiology documenting calibration dates, phantom image results, reject analysis findings and corrective actions taken.',
    tip_3: 'Review imaging QA records monthly and flag any equipment showing drift in image quality or calibration failure to the biomedical team for immediate action.',
    tip_4: 'Train radiographers to perform daily equipment warm-up checks, document results and report any image quality concern to the radiology in-charge before patient use.'
  },
  'AAC6f': {
    tip_1: 'Establish formal agreements with quality-assured external imaging centres for any modality not available in-house; verify their quality credentials before finalising the arrangement.',
    tip_2: 'Keep a file for each outsourced imaging provider containing the agreement, quality certification, contact details and a log of referred cases and received reports.',
    tip_3: 'Review outsourced imaging report turnaround times and quality quarterly; escalate persistent delays or quality issues to management for contract review.',
    tip_4: 'Communicate to clinical staff which imaging investigations are outsourced, the expected report time and the escalation path if a report is critically delayed.'
  },
  'AAC7a': {
    tip_1: 'Establish a documented discharge process covering all patient categories including medical, surgical, day-care and medico-legal cases, with clear steps for documentation, billing and medication counselling.',
    tip_2: 'Use a discharge checklist in every case sheet that confirms summary completion, medication reconciliation, follow-up appointment and patient education are done before the patient leaves.',
    tip_3: 'Audit 10 discharge files weekly to verify the checklist was completed, the summary is present and signed, and medico-legal cases have police intimation documented.',
    tip_4: 'Train ward nurses and medical officers on the discharge SOP at induction; use a simulated discharge exercise in orientation to practise all documentation steps.'
  },
  'AAC7b': {
    tip_1: 'Ensure every discharge summary includes the patient\'\'s full name, unique hospital ID number, final diagnosis and a concise summary of significant clinical findings and investigations.',
    tip_2: 'Use a standardised discharge summary template with mandatory fields for name, UHID, diagnosis and findings; the system should not allow saving without these fields.',
    tip_3: 'Audit 10 discharge summaries weekly to verify all four mandatory elements are present and accurate; return incomplete summaries to the treating doctor within 24 hours.',
    tip_4: 'Train resident doctors that an unsigned or incomplete discharge summary must not be given to the patient; demonstrate the correct template format during clinical induction.'
  },
  'AAC7c': {
    tip_1: 'Include clear follow-up instructions, discharge medication list with dosing schedule and any dietary or activity restrictions in every discharge summary in plain, patient-friendly language.',
    tip_2: 'Print a separate patient instruction sheet accompanying the discharge summary that spells out medicines, follow-up date, diet instructions and warning symptoms to watch for.',
    tip_3: 'Randomly review 5 discharge summaries per week to confirm follow-up advice, medications and instructions are present, legible and written in understandable language.',
    tip_4: 'Train ward staff to explain discharge instructions verbally to patients or caregivers before they leave, confirm understanding and document that counselling was done.'
  },
  'AAC7d': {
    tip_1: 'Include specific guidance in every discharge summary about when symptoms warrant an urgent return visit and how the patient can access emergency care at your facility or elsewhere.',
    tip_2: 'Add a printed emergency contact section on the discharge summary listing the hospital emergency number and the specific warning signs that require immediate attention.',
    tip_3: 'Review 5 discharge summaries per week to confirm the urgent care section is completed and the emergency contact details are accurate and legible.',
    tip_4: 'Instruct discharge counsellors to verbally explain urgent-return criteria to every patient and caregiver and document that this counselling was provided before departure.'
  },
  'AAC7e': {
    tip_1: 'For every patient who dies in the hospital, complete a death summary that includes the primary cause of death, contributing conditions and a brief account of the clinical course.',
    tip_2: 'Use a separate death summary or a clearly marked section in the discharge summary template that requires entry of primary cause, contributing causes and clinical narrative.',
    tip_3: 'Review all death summaries within 72 hours of each death to verify cause of death is documented, the summary is signed and the record is complete before filing.',
    tip_4: 'Train medical officers on correct cause-of-death documentation using ICD coding principles and the hospital death summary format during clinical orientation.'
  },
  'COP1a': {
    tip_1: 'Verify that all clinical care activities comply with applicable statutes, Medical Council guidelines, clinical establishment regulations and any specialty-specific legal requirements before delivering care.',
    tip_2: 'Maintain a legal compliance register listing all applicable laws and regulations with their current compliance status, responsible owner and renewal dates.',
    tip_3: 'Conduct a half-yearly legal and regulatory compliance audit across all clinical departments; document findings and track corrective actions to closure.',
    tip_4: 'Brief department heads at quarterly medical staff meetings on any new laws or regulatory changes affecting clinical practice so care adjustments are made promptly.'
  },
  'COP1b': {
    tip_1: 'Ensure all clinical treatment follows approved written protocols, clinical pathways or treatment guidelines reviewed and signed off by the medical committee.',
    tip_2: 'File all approved clinical protocols in a central repository accessible to all treating doctors; post specialty-specific protocols at nursing stations and in clinical areas.',
    tip_3: 'Audit clinical records monthly to verify that care delivered matches the applicable protocol and that any deviation is documented with a clinical rationale.',
    tip_4: 'Orient new clinical staff to relevant treatment protocols during induction and conduct protocol-based case discussions at monthly department meetings to reinforce adherence.'
  },
  'COP1c': {
    tip_1: 'Develop condition-specific clinical pathways so that all patients with the same diagnosis receive the same standard sequence of assessment, investigations, treatment and monitoring.',
    tip_2: 'Post the clinical pathway flowchart in the relevant ward and include it in the patient case sheet so every team member follows the same plan.',
    tip_3: 'Compare outcomes data for the same diagnosis across different treating doctors monthly to detect care variability and discuss findings at the quality committee.',
    tip_4: 'Train clinicians that using clinical pathways is not optional; run quarterly case reviews comparing actual care to the pathway and highlight positive compliance examples.'
  },
  'COP1d': {
    tip_1: 'Implement nursing care protocols for all routine and specialty procedures so nurses follow the same evidence-based steps every time regardless of shift or unit.',
    tip_2: 'Maintain a nursing procedure manual at each nursing station with step-by-step protocols for all common care activities, updated when evidence or equipment changes.',
    tip_3: 'Conduct monthly nursing procedure observation audits where a senior nurse watches a procedure being performed and scores it against the written protocol.',
    tip_4: 'Train new nurses on procedure protocols during induction, require a supervised competency demonstration before independent practice and document the assessment result.'
  },
  'COP1e': {
    tip_1: 'Provide transfusion services only within the defined scope of the organisation; ensure blood bank or blood storage facilities are licensed and staffed appropriately.',
    tip_2: 'Maintain a blood bank services scope document listing product types available, storage capacity, licensed categories and emergency access procedures.',
    tip_3: 'Audit the blood bank licence, staffing and scope compliance every six months; verify that no products outside the approved scope are being issued.',
    tip_4: 'Brief clinical staff on the types of blood products available in-house, the ordering process and how to arrange products not available locally through the nearest blood bank.'
  },
  'COP1f': {
    tip_1: 'Follow a written transfusion guideline covering indications, pre-transfusion testing, cross-matching, issue, bedside verification, administration rate, monitoring and adverse reaction management.',
    tip_2: 'Use a pre-transfusion checklist attached to every blood product bag verifying patient identity, blood group, cross-match, product details and prescribing doctor\'\'s order.',
    tip_3: 'Review all transfusion records monthly for completeness of pre-checks, monitoring entries and any adverse reactions; present findings at the transfusion committee.',
    tip_4: 'Train nurses who administer blood products on the full transfusion protocol including bedside identity check, monitoring intervals, stopping criteria and reaction reporting.'
  },
  'COP1g': {
    tip_1: 'Obtain written informed consent from the patient or legal guardian before every blood or blood component transfusion, explaining the purpose, risks and alternatives.',
    tip_2: 'Use a dedicated transfusion consent form that describes the product, purpose, potential adverse effects and alternatives; file it in the case sheet before administration.',
    tip_3: 'Audit 10 transfusion records monthly to confirm a signed consent form is present in every file before the first unit was administered; flag gaps to the treating doctor.',
    tip_4: 'Train nursing and medical staff that starting a transfusion without a signed consent form is a patient rights violation; include it as a mandatory pre-transfusion checklist item.'
  },
  'COP2a': {
    tip_1: 'Ensure the emergency department is resourced with equipment, medications, trained staff and protocols matching the scope of emergency services the hospital has committed to provide.',
    tip_2: 'Maintain an emergency services capability document listing available equipment, drug trolleys, specialist on-call coverage and escalation pathways for each emergency type.',
    tip_3: 'Review emergency department readiness monthly by checking equipment functionality, crash cart contents, drug availability and on-call roster for adequacy.',
    tip_4: 'Train emergency staff on the specific emergency services the hospital is equipped to handle and the protocols for immediate referral when a case is beyond scope.'
  },
  'COP2b': {
    tip_1: 'Define a protocol for medico-legal cases that ensures emergency care is provided first without waiting for legal formalities, followed by mandatory police intimation and documentation.',
    tip_2: 'Use a medico-legal case register to record every MLC with patient details, nature of injury, time of arrival, treating doctor, police station informed and certificate issued.',
    tip_3: 'Review the MLC register weekly to confirm all cases are documented, police intimation was timely and case management followed the defined protocol consistently.',
    tip_4: 'Train emergency doctors, nurses and admissions staff on MLC identification, mandatory reporting obligations and the hospital MLC documentation procedure at induction.'
  },
  'COP2c': {
    tip_1: 'Implement a uniform CPR protocol throughout the organisation so any patient requiring resuscitation receives the same standard of care regardless of location in the hospital.',
    tip_2: 'Post the resuscitation protocol and crash cart inventory checklist at every nursing station and ensure crash carts are sealed, checked daily and restocked after each use.',
    tip_3: 'Conduct unannounced crash cart checks at least monthly; review all resuscitation events within 48 hours to assess adherence to the CPR protocol.',
    tip_4: 'Train all clinical staff including nurses and ward boys in basic life support; require annual BLS recertification as a condition of continued employment in clinical areas.'
  },
  'COP2d': {
    tip_1: 'Implement a triage system in the emergency department that categorises every incoming patient by clinical urgency and assigns care priority accordingly before any administrative processes.',
    tip_2: 'Display the triage criteria and colour-coded priority levels at the emergency reception; document triage category, time and assigned nurse for every patient on arrival.',
    tip_3: 'Review triage records monthly to assess time-to-triage compliance, category distribution and any triage under- or over-categorisation identified during clinical review.',
    tip_4: 'Train emergency nurses on the triage tool, triage categories and the decision rules for each level during induction; conduct quarterly scenario-based triage refresher sessions.'
  },
  'COP2e': {
    tip_1: 'Reassess all emergency patients at defined intervals based on their triage category and document vital signs, symptom changes and response to treatment in the emergency record.',
    tip_2: 'Use a structured emergency observation chart that prompts repeat vitals and clinical notes at triage-category-specific intervals during the patient\'\'s stay in the emergency area.',
    tip_3: 'Audit emergency records weekly to verify reassessments are documented at the required intervals and that any deterioration triggered an appropriate clinical response.',
    tip_4: 'Train emergency nurses that reassessment documentation is mandatory, not optional, and demonstrate how to complete the observation chart correctly during nursing orientation.'
  },
  'COP2f': {
    tip_1: 'Document the outcome of every emergency patient visit, whether the patient was admitted, discharged home or transferred to another facility, including the time and authorising clinician.',
    tip_2: 'Record admission or discharge or transfer decisions in the emergency register with patient ID, decision time, destination, transporting person and any referral documents issued.',
    tip_3: 'Review the emergency register weekly to confirm no patient was discharged or transferred without documented authorisation and a completed clinical record.',
    tip_4: 'Train emergency nursing and medical staff that every patient who leaves the emergency area must have their disposition formally recorded before departure.'
  },
  'COP2g': {
    tip_1: 'Establish a written protocol for patients found dead on arrival covering confirmation of death by a qualified doctor, documentation requirements, family notification and medico-legal obligations.',
    tip_2: 'Maintain a death on arrival register recording the date, time, patient details, certifying doctor, family informed time and police notification where legally required.',
    tip_3: 'Review all death-on-arrival records monthly to confirm the protocol was followed, documentation is complete and all mandatory notifications were made.',
    tip_4: 'Train emergency doctors and nurses on the dead-on-arrival protocol at induction, emphasising that proper documentation and legal obligations apply even when death precedes arrival.'
  },
  'COP2h': {
    tip_1: 'Ensure any ambulance operated by or affiliated with the hospital is staffed with trained personnel, equipped with required emergency medications and devices and checked for readiness before every shift.',
    tip_2: 'Maintain an ambulance readiness checklist completed at the start of every shift covering equipment inventory, drug expiry, oxygen level, vehicle fitness and driver licence validity.',
    tip_3: 'Review completed ambulance checklists weekly and arrange unannounced spot checks monthly to verify equipment is functional and staff are competent.',
    tip_4: 'Train ambulance staff on equipment use, emergency protocols, patient loading and communication procedures; document training and require annual competency reassessment.'
  },
  'COP2i': {
    tip_1: 'Develop and implement a hospital disaster management plan covering mass casualty events, epidemic surges and natural disasters, including surge capacity, staff roles and external coordination.',
    tip_2: 'Keep the disaster management plan document accessible to all department heads; display emergency contact trees and code activation procedures at nursing stations.',
    tip_3: 'Conduct at least two disaster or mass casualty mock drills per year and evaluate staff response against the plan, documenting gaps and corrective actions.',
    tip_4: 'Train all staff on their specific disaster role during induction and brief them on updated plans annually; appoint a disaster coordinator for each major department.'
  },
  'COP3a': {
    tip_1: 'Define the scope of ICU and HDU care in a written policy specifying admission and discharge criteria, monitoring standards, staffing ratios and available interventions.',
    tip_2: 'Post the ICU and HDU scope and admission criteria at the unit entrance and in the medical staff handbook so all clinicians apply consistent admission decisions.',
    tip_3: 'Review ICU and HDU admissions monthly to verify they meet the documented admission criteria and that scope boundaries were not exceeded without formal extension.',
    tip_4: 'Orient ICU and HDU staff on the defined scope, admission criteria and available interventions at induction; update them whenever the scope is formally revised.'
  },
  'COP3b': {
    tip_1: 'Implement a quality assurance programme for ICU and HDU that tracks key clinical indicators such as VAP rate, CAUTI rate, ventilator days and mortality benchmarked against standards.',
    tip_2: 'Maintain an ICU QA dashboard updated monthly showing indicator values, targets and trend charts; review at the quality committee meeting each month.',
    tip_3: 'Analyse ICU QA data monthly to identify adverse trends, conduct root cause analysis for significant deviations and implement targeted improvement actions.',
    tip_4: 'Engage ICU medical and nursing staff in reviewing their unit\'\'s quality data monthly; use the findings as teaching cases to reinforce best practice at the bedside.'
  },
  'COP3c': {
    tip_1: 'Establish a process for counselling patients and families in ICU and HDU at admission and at regular intervals to explain the treatment plan, prognosis and available options.',
    tip_2: 'Document all family counselling sessions in the case sheet noting date, time, topics discussed, who was present and the family\'\'s response or questions.',
    tip_3: 'Audit ICU records monthly to verify that counselling documentation is present for every admission within 24 hours and at weekly intervals thereafter.',
    tip_4: 'Train ICU doctors and nurses on effective counselling techniques for critical care families, emphasising clear language, empathy and confirming understanding.'
  },
  'COP3d': {
    tip_1: 'Provide end-of-life care that addresses physical comfort, pain control, emotional support and dignified surroundings for patients and their families at all times.',
    tip_2: 'Document the end-of-life care plan in the case sheet covering symptom management, family support measures, DNR decisions if applicable and chaplaincy or counselling services offered.',
    tip_3: 'Review end-of-life case records quarterly to assess quality of symptom management, family support and documentation completeness; discuss learnings at the ethics committee.',
    tip_4: 'Train clinical staff on palliative and end-of-life care principles, communication with grieving families and the hospital\'\'s policy on DNR and withholding of treatment.'
  },
  'COP4a': {
    tip_1: 'Provide obstetric care within a clearly defined scope that matches your hospital\'\'s staffing, infrastructure and emergency capability; document the scope and obtain regulatory approval.',
    tip_2: 'Display the obstetric services scope and emergency maternity contact numbers in the labour room and antenatal clinic; maintain relevant licences in a compliance file.',
    tip_3: 'Review obstetric service delivery annually against the defined scope and maternal and neonatal outcome indicators to ensure care standards are being met.',
    tip_4: 'Orient obstetricians, midwives and labour room nurses on the defined obstetric scope and the escalation protocol for cases that exceed the facility\'\'s capability.'
  },
  'COP4b': {
    tip_1: 'Provide comprehensive antenatal care including scheduled check-ups, maternal nutrition screening, immunisation with Td and other recommended vaccines and protocols for obstetric emergencies.',
    tip_2: 'Use a standard antenatal record card for each patient tracking all ANC visits, investigations done, immunisations given, nutrition status and risk flags.',
    tip_3: 'Audit antenatal records monthly to verify ANC visit frequency, immunisation coverage, nutrition assessment and emergency preparedness documentation for all enrolled patients.',
    tip_4: 'Train nursing staff in the ANC clinic on maternal nutrition counselling, vaccine schedules and early identification of high-risk pregnancies requiring specialist review.'
  },
  'COP4c': {
    tip_1: 'Ensure facilities managing obstetric cases can immediately stabilise and manage neonatal emergencies including resuscitation, hypothermia prevention and early transfer to a NICU if needed.',
    tip_2: 'Maintain a neonatal resuscitation kit and a functional radiant warmer in every delivery area; post the neonatal resuscitation protocol on the labour room wall.',
    tip_3: 'Check neonatal emergency equipment readiness at every shift handover; review all neonatal adverse events monthly to assess preparedness and response quality.',
    tip_4: 'Train all labour room staff in neonatal resuscitation and stabilisation annually; ensure at least one NRP-certified staff member is present at every delivery.'
  },
  'COP5a': {
    tip_1: 'Staff paediatric and neonatal units only with doctors and nurses who have demonstrated age-specific competencies in growth assessment, drug dosing, equipment use and clinical care.',
    tip_2: 'Maintain a competency record for each paediatric and neonatal staff member listing the skills assessed, assessment date, assessor name and review due date.',
    tip_3: 'Audit paediatric clinical records and directly observe staff practices quarterly to verify age-appropriate assessment and management techniques are being applied correctly.',
    tip_4: 'Provide age-specific competency training for all new paediatric and neonatal staff and schedule annual reassessment; link competency status to ward posting decisions.'
  },
  'COP5b': {
    tip_1: 'Include growth monitoring with weight-for-age and height-for-age charts, developmental milestone screening, nutritional status assessment and immunisation history in every paediatric assessment.',
    tip_2: 'Use a structured paediatric assessment form with dedicated sections for growth parameters, developmental milestones, nutritional status and vaccination history.',
    tip_3: 'Audit 10 paediatric records monthly to verify all four assessment domains are documented; flag incomplete records to the paediatric department head for correction.',
    tip_4: 'Train paediatric nurses and doctors on how to plot growth charts, assess developmental milestones and screen for malnutrition using standard tools at induction.'
  },
  'COP5c': {
    tip_1: 'Implement physical security measures to prevent child and neonate abduction including restricted access to maternity and paediatric wards, identity bands and staff recognition protocols.',
    tip_2: 'Attach matching identity bands to the neonate and mother at birth; document band numbers in the birth record and verify them at every handover and feeding.',
    tip_3: 'Test the access control system and abduction response protocol with a surprise drill once a year; review all security incidents in paediatric areas within 24 hours.',
    tip_4: 'Train all maternity and paediatric staff on abduction prevention protocols, how to respond to a suspicious person in the ward and who to alert immediately.'
  },
  'COP6a': {
    tip_1: 'Administer procedural sedation only under a written protocol that defines indications, pre-procedure assessment, monitoring requirements, recovery criteria and emergency response.',
    tip_2: 'Use a procedural sedation checklist documenting patient assessment, consent, drug name and dose, monitoring values and recovery room discharge criteria for every sedation event.',
    tip_3: 'Review all procedural sedation records monthly to verify protocol adherence, monitoring documentation and occurrence of any adverse sedation events.',
    tip_4: 'Train all staff who participate in procedural sedation on the protocol, drug interactions, airway management and emergency reversal agent availability before they are permitted to sedate independently.'
  },
  'COP6b': {
    tip_1: 'Assign procedural sedation only to competent and trained clinicians; obtain written informed consent from the patient before every sedation procedure and document it in the case sheet.',
    tip_2: 'Maintain a sedation competency register listing each certified provider, skills validated, certification date and renewal due date.',
    tip_3: 'Audit sedation records quarterly to confirm sedation was administered only by listed competent providers and that consent forms are present for every procedure.',
    tip_4: 'Train clinical staff that sedation can only be performed by those with documented competency and that no sedation should begin without a signed consent form in the file.'
  },
  'COP7a': {
    tip_1: 'Create a comprehensive anaesthesia management policy covering pre-operative assessment requirements, drug selection, monitoring standards, emergency protocols and post-anaesthesia recovery.',
    tip_2: 'File all anaesthesia protocols in the OT and recovery room with easy access for all anaesthetists; include a quick-reference card for common emergency scenarios.',
    tip_3: 'Review anaesthesia records monthly for documentation completeness and adherence to protocols; present findings including adverse events at the anaesthesia peer review meeting.',
    tip_4: 'Orient new anaesthetists and nurse anaesthetists to the anaesthesia policy during credentialling; include protocol-based case discussions in monthly departmental meetings.'
  },
  'COP7b': {
    tip_1: 'Complete a structured pre-anaesthesia assessment for every patient and document a written anaesthesia plan in the case sheet covering technique, drugs, monitoring and anticipated risks.',
    tip_2: 'Use a standardised pre-anaesthesia assessment form that captures ASA grade, airway assessment, allergy history, medication review and signed anaesthesia plan.',
    tip_3: 'Audit pre-anaesthesia documentation for all surgical cases weekly to verify the assessment and plan are present, complete and signed before the patient enters the OT.',
    tip_4: 'Train anaesthesia staff to complete the pre-anaesthesia form on the ward the evening before elective surgery and ensure emergency cases have at minimum a brief pre-assessment note.'
  },
  'COP7c': {
    tip_1: 'Monitor every anaesthetised patient continuously for SpO2, ECG, NIBP, EtCO2 where applicable and temperature, recording values at defined intervals throughout the procedure.',
    tip_2: 'Use an intraoperative anaesthesia monitoring chart that prompts recording of all vital parameters at 5-minute intervals with space for drug doses and event notes.',
    tip_3: 'Review anaesthesia charts monthly to verify continuous monitoring was maintained and documented throughout every case; investigate any gaps as potential safety events.',
    tip_4: 'Train OT nursing staff to assist anaesthetists with monitoring equipment setup and alert them immediately if any monitoring alarm sounds during a procedure.'
  },
  'COP7d': {
    tip_1: 'Record all post-anaesthesia observations in a recovery room chart and discharge patients from recovery only when they meet the defined Modified Aldrete or equivalent discharge score.',
    tip_2: 'Use a post-anaesthesia recovery chart with Aldrete or PAD score at defined intervals; only a qualified nurse or anaesthetist can authorise discharge from recovery.',
    tip_3: 'Audit recovery room records weekly to verify all patients met discharge criteria before leaving and that the authorising clinician\'\'s signature is present.',
    tip_4: 'Train recovery room nurses on the discharge scoring tool, how to calculate it correctly and the escalation protocol if a patient fails to meet discharge criteria.'
  },
  'COP7e': {
    tip_1: 'Record every intraoperative adverse anaesthesia event including unexpected desaturation, anaphylaxis, failed intubation or cardiac arrest in the anaesthesia record and the incident reporting system.',
    tip_2: 'Maintain an anaesthesia adverse event log separate from the routine record; document event type, time, immediate action taken and patient outcome.',
    tip_3: 'Review all anaesthesia adverse events at the monthly anaesthesia peer review meeting; conduct root cause analysis for serious events and track corrective actions to closure.',
    tip_4: 'Train anaesthesia staff to report all intraoperative adverse events without delay and treat them as learning opportunities rather than errors that invite blame.'
  },
  'COP8a': {
    tip_1: 'Perform all surgical and clinical procedures following written safety protocols including pre-procedure timeout, equipment checks, sterile field maintenance and post-procedure monitoring.',
    tip_2: 'Complete and file a surgical safety checklist for every OT case covering sign-in, timeout and sign-out phases, signed by the surgeon, anaesthetist and scrub nurse.',
    tip_3: 'Audit completed surgical safety checklists weekly to verify all three phases were completed for every case and that no procedure started before timeout was done.',
    tip_4: 'Train all OT staff on the surgical safety checklist process; conduct a quarterly simulation where the full timeout is practised as a team to reinforce compliance.'
  },
  'COP8b': {
    tip_1: 'Complete and document a pre-operative assessment for every surgical patient covering history, examination, investigations, risk stratification, allergies and pre-operative diagnosis before the case begins.',
    tip_2: 'Use a pre-operative assessment proforma in the surgical case sheet that must be completed and signed by the operating surgeon before the patient is taken to the OT.',
    tip_3: 'Audit surgical records weekly to verify every case has a completed pre-operative assessment with documented diagnosis before the OT record commences.',
    tip_4: 'Train surgical residents that a case should not be listed for operation until the pre-operative assessment form is complete, signed and available in the patient\'\'s file.'
  },
  'COP8c': {
    tip_1: 'Obtain written informed consent from the patient before every surgical procedure, explained by the operating surgeon in the patient\'\'s preferred language covering risks, benefits and alternatives.',
    tip_2: 'Use a procedure-specific consent form that describes the operation, anaesthesia type, significant risks and alternatives; it must be signed by patient or guardian and the surgeon.',
    tip_3: 'Audit surgical files weekly to confirm a properly completed and signed consent form is present for every case before the patient was taken to the OT.',
    tip_4: 'Train surgeons that consent must be obtained personally by the operating surgeon, not delegated to a junior doctor, and must be documented before the patient reaches the OT.'
  },
  'COP8d': {
    tip_1: 'Implement wrong-site, wrong-patient and wrong-procedure prevention measures including surgical site marking by the operating surgeon, pre-operative patient identity verification and OT timeout.',
    tip_2: 'Require the operating surgeon to mark the surgical site with an indelible pen in the pre-operative area before the patient is transferred to the OT.',
    tip_3: 'Verify site marking and patient identity using two identifiers at each handover point: ward to pre-op, pre-op to OT and at timeout; document each verification.',
    tip_4: 'Train all OT staff that they have the authority and responsibility to halt a procedure if site marking is absent or identity verification is incomplete until the issue is resolved.'
  },
  'COP8e': {
    tip_1: 'Document the operative note, post-procedure monitoring observations and post-operative care plan in the patient record immediately after every surgical or clinical procedure.',
    tip_2: 'Use an operation note template capturing pre-operative diagnosis, procedure performed, findings, specimen sent, complications and post-operative instructions, signed by the surgeon.',
    tip_3: 'Audit operation notes weekly to verify they are completed within the required timeframe, contain all mandatory elements and are signed by the operating surgeon.',
    tip_4: 'Train surgical residents to complete the operation note in the OT before moving to the next case; demonstrate the correct format using a completed example during orientation.'
  },
  'COP9a': {
    tip_1: 'Define categories of vulnerable patients such as elderly, disabled, children, victims of abuse and those with mental health needs; implement specific care and safeguarding protocols for each group.',
    tip_2: 'Flag vulnerable patients in the medical record with a designated indicator; document the vulnerability type, specific care modifications and any safeguarding actions taken.',
    tip_3: 'Audit records of identified vulnerable patients monthly to verify appropriate care modifications and safeguarding actions were implemented and documented.',
    tip_4: 'Train all clinical staff to identify vulnerable patient indicators, apply the correct care protocol and escalate any safeguarding concern to the designated responsible officer.'
  },
  'COP9b': {
    tip_1: 'Screen every admitted patient for fall risk, pressure ulcer risk and malnutrition risk using validated tools within 24 hours of admission and reassess at defined intervals.',
    tip_2: 'Document screening results in the case sheet and initiate a prevention plan for any patient scoring above the risk threshold, listing specific interventions and frequency.',
    tip_3: 'Audit 10 in-patient records weekly to verify risk screening was completed at admission, reassessed at intervals and prevention plans are documented for at-risk patients.',
    tip_4: 'Train nursing staff on the Morse fall scale, Braden pressure ulcer scale and a nutritional screening tool at induction; require supervised practice before independent use.'
  },
  'COP10a': {
    tip_1: 'Assess every patient for pain using a validated pain scale at admission, at regular intervals and after any pain-relieving intervention, adjusting the management plan based on scores.',
    tip_2: 'Document pain scores in the vital signs chart alongside BP and temperature; include analgesic doses, route, time and effect assessment in the medication administration record.',
    tip_3: 'Audit vital sign charts weekly to confirm pain scores are recorded at required intervals and that high pain scores triggered a documented clinical response.',
    tip_4: 'Train all nursing staff on validated pain assessment tools for different patient populations including children and non-verbal patients, and on the escalation pathway for uncontrolled pain.'
  },
  'COP10b': {
    tip_1: 'Ensure rehabilitation services are available at a scope commensurate with the clinical specialties offered, including physiotherapy, occupational therapy and speech therapy where needed.',
    tip_2: 'Maintain a rehabilitation services scope document listing available therapies, qualified therapists, referral process and available equipment.',
    tip_3: 'Review rehabilitation referral patterns and outcomes quarterly to confirm services meet patient needs and scope limitations do not result in unmet rehabilitation requirements.',
    tip_4: 'Train clinical teams to refer appropriate patients for rehabilitation early in the admission process and to document rehabilitation goals and progress in the case sheet.'
  },
  'COP10c': {
    tip_1: 'Screen every admitted patient for nutritional risk using a validated tool such as NRS-2002 or MNA within 24 hours of admission and document the result in the case sheet.',
    tip_2: 'Record the nutritional screening score in the case sheet; flag patients who screen positive for a dietician referral and document the referral in the notes.',
    tip_3: 'Audit 10 in-patient records weekly to verify nutritional screening was completed at admission and that at-risk patients received a dietician referral within 24 hours.',
    tip_4: 'Train nursing staff on how to use the chosen nutritional screening tool correctly; include a practical exercise in orientation so nurses are confident before independent use.'
  },
  'COP10d': {
    tip_1: 'Refer all patients identified as nutritionally at risk to a qualified dietician for a full nutritional assessment and individualised dietary prescription within a defined timeframe.',
    tip_2: 'Document the dietician\'\'s nutritional assessment, diagnosis, dietary prescription and monitoring plan in the case sheet; update it at each review visit.',
    tip_3: 'Audit dietician assessment records monthly to verify at-risk patients received timely assessment, a dietary plan was documented and follow-up reviews occurred.',
    tip_4: 'Train nursing staff and junior doctors to promptly refer at-risk patients to the dietician and to support dietary plan implementation during nursing rounds.'
  },
  'MOM1a': {
    tip_1: 'Establish a pharmacy services policy covering procurement, storage, dispensing, administration and disposal of medications, reviewed and updated annually by the pharmacy and therapeutics committee.',
    tip_2: 'Keep the pharmacy policy manual at the dispensing counter and in each clinical area; ensure current version date is visible and superseded copies are removed.',
    tip_3: 'Audit pharmacy practices monthly against the written policy, checking storage conditions, labelling, dispensing accuracy and documentation to identify gaps.',
    tip_4: 'Train all pharmacy staff on the medication management policy during induction; hold quarterly refresher sessions on any updated sections or newly identified risks.'
  },
  'MOM1b': {
    tip_1: 'Review the hospital formulary at least annually against current clinical services, evidence-based guidelines and any new regulatory approvals; update and circulate to all prescribers.',
    tip_2: 'Maintain the formulary as a controlled document with a version number, review date and sign-off by the pharmacy and therapeutics committee; make it available in print and digitally.',
    tip_3: 'Track non-formulary drug requests each quarter; analyse patterns and use data to update the formulary so it reflects actual prescribing needs and current evidence.',
    tip_4: 'Inform all prescribers at departmental meetings whenever the formulary is updated, highlighting additions, deletions and any therapeutic substitutions that affect their practice.'
  },
  'MOM2a': {
    tip_1: 'Store all medications in clean, secure, well-lit areas with appropriate temperature, humidity and lighting conditions; lock controlled substances and restrict access to authorised personnel.',
    tip_2: 'Maintain daily temperature monitoring logs for all medication storage areas including refrigerators; document any excursion and the corrective action taken.',
    tip_3: 'Conduct monthly medication storage audits across all wards, satellite pharmacies and emergency areas to verify storage conditions, security and orderly arrangement.',
    tip_4: 'Train all staff who store medications on correct storage requirements, temperature monitoring procedures and what to do if a storage excursion is detected.'
  },
  'MOM2b': {
    tip_1: 'Create a separate written protocol for high-alert medications and look-alike sound-alike drugs covering storage segregation, distinct labelling, double-checking requirements and restricted access.',
    tip_2: 'Label all high-alert medications with a distinctive sticker and store them in a separately designated section with a LASA warning; post the LASA drug list at dispensing areas.',
    tip_3: 'Audit high-alert medication storage areas monthly to verify segregation, labelling and access control are maintained; report any non-compliance to the pharmacy in-charge.',
    tip_4: 'Train pharmacy and nursing staff to recognise high-alert and LASA medications, apply the required additional checks before dispensing or administering and report any near-miss.'
  },
  'MOM2c': {
    tip_1: 'Check expiry dates of all medications in all storage areas at least monthly; remove and segregate any expired drug immediately and return or destroy it per the disposal SOP.',
    tip_2: 'Use a first-expiry first-out labelling system for all stock; maintain a monthly expiry check log signed by the pharmacist responsible for each storage area.',
    tip_3: 'Conduct surprise checks in satellite pharmacies and ward drug trolleys every quarter to detect expired drugs; document findings and corrective actions.',
    tip_4: 'Train ward nurses and pharmacy staff that using an expired medication is a medication error; show them how to check expiry dates and what to do when one is found.'
  },
  'MOM2d': {
    tip_1: 'Define a list of essential emergency medications for each clinical area, store them in a sealed and labelled emergency trolley and ensure they are available 24 hours a day.',
    tip_2: 'Attach a sealed drug inventory list to every emergency trolley listing each drug, dose, quantity and expiry date; re-seal and document after every use.',
    tip_3: 'Check all emergency drug trolleys at every shift handover for intact seal; perform a full inventory count after any use or broken seal and document the check.',
    tip_4: 'Train all clinical staff to know the location of the emergency drug trolley in their area, recognise the seal integrity check and report any broken seal immediately.'
  },
  'MOM3a': {
    tip_1: 'Establish a written policy specifying who is authorised to write prescriptions and medication orders in the hospital, linked to qualifications, registration and clinical privileges.',
    tip_2: 'Maintain a list of authorised prescribers with their specimen signatures on file in the pharmacy; update the list within 48 hours of any staff change.',
    tip_3: 'Audit a sample of prescriptions monthly to verify they were written only by authorised prescribers; flag any order written by an unregistered or unauthorised person.',
    tip_4: 'Inform all pharmacy and nursing staff of the current list of authorised prescribers and train them to reject any medication order that is not from an authorised source.'
  },
  'MOM3b': {
    tip_1: 'Define minimum requirements for a valid prescription: patient name, UHID, date, drug name in generic form, dose, route, frequency, duration and prescriber\'\'s name and signature.',
    tip_2: 'Post the valid prescription requirements at every prescribing workstation and pharmacy dispensing counter; use prescription pads or electronic templates that enforce these fields.',
    tip_3: 'Audit 20 prescriptions weekly to check all mandatory elements are present; return incomplete orders to the prescriber for correction before dispensing.',
    tip_4: 'Train all prescribers during medical staff orientation on the hospital\'\'s minimum prescription requirements and the consequences of dispensing against an incomplete order.'
  },
  'MOM3c': {
    tip_1: 'Check and document the patient\'\'s allergy status and history of adverse drug reactions in the medical record before writing any prescription, and prominently flag any known allergy.',
    tip_2: 'Use an allergy alert sticker or prominent box on the case sheet cover and prescription chart; record the specific drug, type of reaction and severity for each allergy.',
    tip_3: 'Audit 10 case sheets weekly to verify allergy documentation is present, legible and that no medication was prescribed to which the patient has a known adverse reaction.',
    tip_4: 'Train prescribers and nurses to ask every patient about allergies at admission, document the response even if there are no known allergies and alert the pharmacist for high-risk prescriptions.'
  },
  'MOM3d': {
    tip_1: 'Ensure every medication order is written clearly in block capitals or typed, includes the patient\'\'s name and UHID, is dated, timed and signed by the prescribing doctor.',
    tip_2: 'Use pre-printed prescription stationery or electronic order forms that include patient identification fields and require date, time and prescriber signature before submission.',
    tip_3: 'Audit 20 medication orders weekly for legibility, completeness, date, time and signature; return non-compliant orders to the prescriber for correction before dispensing.',
    tip_4: 'Train all prescribers that ambiguous handwriting on medication orders is a patient safety risk; demonstrate the required standard using examples of acceptable and unacceptable orders.'
  },
  'MOM3e': {
    tip_1: 'Reconcile all medications at every transition point including admission, transfer between units and discharge by comparing current medications with new orders and resolving discrepancies.',
    tip_2: 'Use a medication reconciliation form at each transition point listing pre-admission drugs, current hospital orders, changes made and the reason for each change.',
    tip_3: 'Audit medication reconciliation forms for all admissions and transfers weekly to verify reconciliation was performed, discrepancies were resolved and the form is in the case sheet.',
    tip_4: 'Train nursing and medical staff that medication reconciliation is a mandatory safety step at every transition point and must be completed before new orders are implemented.'
  },
  'MOM3f': {
    tip_1: 'Conduct regular audits of prescription and medication orders to assess safety, rationality, compliance with the formulary and adherence to prescribing guidelines.',
    tip_2: 'Document prescription audit findings in a monthly audit report including metrics such as polypharmacy rates, generic prescribing percentage and high-alert drug order compliance.',
    tip_3: 'Review prescription audit results at the pharmacy and therapeutics committee each month and implement targeted feedback to departments showing recurring prescribing issues.',
    tip_4: 'Share de-identified prescription audit findings with clinical departments as educational cases; recognise departments demonstrating consistent improvement in prescribing quality.'
  },
  'MOM4a': {
    tip_1: 'Define a hospital high-risk medication list covering anticoagulants, insulin, concentrated electrolytes and opioids, and document specific prescribing, dispensing and administration safety steps for each.',
    tip_2: 'Post the high-risk medication list with associated safety protocols in the pharmacy, every nursing station and any satellite supply point where these drugs are kept.',
    tip_3: 'Audit high-risk medication handling monthly checking that prescribed doses are verified, second nurse check is documented, and administration follows the safety protocol.',
    tip_4: 'Train pharmacy and nursing staff on the high-risk drug list, required double-check process before dispensing or administering and the protocol for reporting a high-risk medication error.'
  },
  'MOM4b': {
    tip_1: 'Label every dispensed medication with patient name, UHID, drug name, dose, route, frequency, start date and pharmacist\'\'s name before the medication leaves the pharmacy.',
    tip_2: 'Use pre-printed or computer-generated dispensing labels that include all required fields; never dispatch a medicine in an unlabelled or partially labelled container.',
    tip_3: 'Audit dispensed medication labels monthly for completeness, accuracy and legibility; record deficiencies and retrain the responsible pharmacist promptly.',
    tip_4: 'Train pharmacy staff that a medication without a complete and accurate label must not be dispensed; demonstrate label printing and verification during pharmacy induction.'
  },
  'MOM5a': {
    tip_1: 'Ensure medications are administered only by doctors, nurses or technicians who are legally authorised and have documented competency to administer the specific medication type and route.',
    tip_2: 'Maintain an authorised medication administrators list by staff category and route including IV, IM, oral, epidural; make it available at each nursing station.',
    tip_3: 'Audit medication administration records monthly to confirm each administration was performed by an authorised and competent staff member; flag any exceptions.',
    tip_4: 'Train nurses during induction on which medications and routes they are authorised to administer, the competency assessment process and the restriction on delegating to unqualified staff.'
  },
  'MOM5b': {
    tip_1: 'Verify five rights before every medication administration: right patient using two identifiers, right drug, right dose, right route and right time, documented in the medication administration record.',
    tip_2: 'Use a bedside medication administration record with pre-populated order details so the nurse can check and sign each administration against the original prescription.',
    tip_3: 'Observe nurses administering medications monthly to confirm five-rights verification is performed at the bedside each time; document observation findings.',
    tip_4: 'Train all nurses on the five-rights verification process at induction and reinforce through quarterly competency spot checks observed by the nursing supervisor.'
  },
  'MOM5c': {
    tip_1: 'Label any prepared medication with drug name, concentration, volume, patient name and preparation time before beginning the preparation of any second medication.',
    tip_2: 'Use pre-printed or handwritten labels applied to syringes and IV bags immediately after preparation; never prepare a second drug until the first is labelled.',
    tip_3: 'Observe medication preparation practices in clinical areas monthly to verify labelling is performed before preparing the next drug; document and act on any non-compliance.',
    tip_4: 'Train nurses and pharmacists that preparing two drugs simultaneously without labelling the first is a major medication safety risk; use a simulation exercise to demonstrate why during orientation.'
  },
  'MOM5d': {
    tip_1: 'Implement physical and system controls to prevent incorrect connections between IV lines, enteral tubes, urinary catheters and epidural catheters during medication administration.',
    tip_2: 'Use colour-coded connectors and route-specific labelling on all tubing; post a tubing connection safety guide at IV preparation areas and nursing stations.',
    tip_3: 'Conduct monthly audits of tubing setups in ICU and general wards to verify no mixed connections are present; report any near-miss or wrong connection as a safety incident.',
    tip_4: 'Train all nurses on catheter and tubing mis-connection risks at induction using real equipment; emphasise tracing all lines from patient to container before any infusion is started.'
  },
  'MOM5e': {
    tip_1: 'Document every medication administration in the patient\'\'s medication administration record immediately after giving the drug, including drug name, dose, route, time and administering nurse\'\'s signature.',
    tip_2: 'Use a pre-printed or electronic MAR with all prescribed drugs listed; sign each drug after administration and record the time; never pre-sign before giving the drug.',
    tip_3: 'Audit MARs weekly to check for unsigned entries, pre-signing, missed doses not explained and legibility; provide immediate feedback to the responsible nurse.',
    tip_4: 'Train nurses at induction that documentation of administration must happen at the bedside immediately after giving the drug, not from memory at the end of the shift.'
  },
  'MOM5f': {
    tip_1: 'Observe and document patient response after administering high-risk or new medications including vital signs, therapeutic effect, onset of side effects and allergic reactions.',
    tip_2: 'Record post-medication monitoring findings in the nursing notes or designated monitoring chart, noting the drug given, time of administration and observations at defined intervals.',
    tip_3: 'Audit nursing notes for patients on high-risk medications weekly to verify monitoring was performed and documented at the required intervals after each administration.',
    tip_4: 'Train nurses on the specific monitoring requirements for each high-risk medication class: what to observe, how soon, how often and when to escalate an abnormal finding.'
  },
  'MOM5g': {
    tip_1: 'Define near-miss events, medication errors and adverse drug events clearly; implement a reporting system that encourages staff to report without fear of blame for near-misses.',
    tip_2: 'Maintain a medication safety incident log recording every reported event with type, drug involved, contributing factors, patient harm level and actions taken.',
    tip_3: 'Analyse all medication incident reports monthly for patterns; conduct root cause analysis for serious events and track corrective action implementation to closure.',
    tip_4: 'Train all clinical staff on the definitions of near-miss, error and adverse event and how to complete an incident report; celebrate near-miss reporting as a safety culture indicator.'
  },
  'MOM6a': {
    tip_1: 'Store narcotic drugs and psychotropic substances in a double-locked cabinet with access restricted to authorised personnel as required by the Narcotic Drugs and Psychotropic Substances Act.',
    tip_2: 'Maintain a narcotic drug register with details of stock received, issued, administered and balance, signed after each transaction by an authorised nurse or pharmacist.',
    tip_3: 'Conduct weekly narcotic stock reconciliation by counting physical stock against the register; investigate any discrepancy immediately and report as per statutory requirements.',
    tip_4: 'Train all authorised nursing and pharmacy staff on NDPS Act storage requirements, register maintenance and the legal consequences of non-compliance at induction.'
  },
  'MOM6b': {
    tip_1: 'Prescribe, dispense and administer narcotic drugs and psychotropic substances only as per the NDPS Act requirements including authorised prescriber, controlled prescription format and witness for administration.',
    tip_2: 'Use NDPS-compliant prescription pads for narcotic orders; record each dispensed quantity in the narcotic register and require a second witness signature for every administration.',
    tip_3: 'Audit narcotic prescription and administration records monthly for statutory compliance; check that all dispensed quantities match administered amounts with no unexplained discrepancies.',
    tip_4: 'Train authorised prescribers and nurses on NDPS Act requirements for prescribing, dispensing and administration of narcotic substances, including witness and documentation obligations.'
  },
  'MOM6c': {
    tip_1: 'Prepare chemotherapy and radiopharmaceuticals in a designated controlled environment by trained pharmacists using appropriate protective equipment, following written preparation protocols.',
    tip_2: 'Maintain a chemotherapy preparation log recording drug name, dose calculated, patient UHID, preparer name, preparation time and pharmacist check before dispensing.',
    tip_3: 'Audit chemotherapy preparation records monthly to verify protocol adherence, double-check documentation and PPE compliance; review all preparation errors as safety incidents.',
    tip_4: 'Train chemotherapy pharmacy staff on safe preparation techniques, hazardous drug spill response and PPE use; require annual competency reassessment before independent preparation.'
  },
  'MOM6d': {
    tip_1: 'Keep a complete and contemporaneous record of every transaction involving narcotic and psychotropic drugs including receipt, dispensing, administration to patient and disposal of unused portions.',
    tip_2: 'Use a multi-column narcotic register capturing date, patient name, UHID, quantity issued, quantity administered, remaining balance, prescriber and administering nurse.',
    tip_3: 'Reconcile the narcotic register with physical stock count weekly; escalate any discrepancy to the pharmacy in-charge and medical superintendent for investigation within 24 hours.',
    tip_4: 'Train all staff authorised to handle narcotic and psychotropic substances on proper register maintenance procedures and the legal obligation to account for every dose.'
  },
  'MOM7a': {
    tip_1: 'Establish a written policy governing procurement, quality verification, storage, selection and usage of implantable prostheses and medical devices, including vendor qualification criteria.',
    tip_2: 'Maintain a device procurement register listing each implant type, vendor name, quality certification, batch number, device specifications and procurement date.',
    tip_3: 'Audit device procurement records quarterly to confirm only quality-verified devices from approved vendors are used; check for expired or recalled device batches.',
    tip_4: 'Train purchasing staff on device quality requirements, how to verify vendor credentials and the process for quarantining any device batch subject to a recall or safety alert.'
  },
  'MOM7b': {
    tip_1: 'Counsel patients and families about the type of implant or device proposed, its purpose, expected benefits, risks, alternatives and cost before obtaining consent for the procedure.',
    tip_2: 'Document implant counselling in the case sheet noting the topics discussed, who conducted the counselling, family member present and patient\'\'s confirmation of understanding.',
    tip_3: 'Audit implant procedure records monthly to verify counselling documentation is present before the procedure date and that consent was obtained after counselling.',
    tip_4: 'Train surgeons and nursing staff on what information must be provided to the patient about an implant or device; use a counselling checklist to ensure consistency.'
  },
  'MOM7c': {
    tip_1: 'Record the batch number, serial number, lot number and manufacturer details of every implant or medical device in the patient\'\'s case sheet at the time of implantation.',
    tip_2: 'Attach the device traceability sticker or label from the device packaging directly into the patient\'\'s case sheet or operative note so the information is permanently linked.',
    tip_3: 'Audit operative records monthly to confirm device traceability details are documented for every implant case; investigate missing entries and implement process corrections.',
    tip_4: 'Train OT nurses and surgeons to peel and affix the device traceability sticker from every implant packaging into the case sheet before the patient leaves the OT.'
  },
  'PRE1a': {
    tip_1: 'Display a comprehensive patient rights and responsibilities charter in all key patient-facing areas including entrance, OPD, wards and emergency, in languages patients understand.',
    tip_2: 'Provide a printed patient rights and responsibilities leaflet to every patient or caregiver at registration; document in the admission form that it was given and explained.',
    tip_3: 'Verify during monthly facility rounds that rights and responsibilities displays are current, undamaged, legible and present in all required locations.',
    tip_4: 'Train all front-desk, nursing and clinical staff to explain patient rights and responsibilities to patients at admission or first contact, using the hospital leaflet as a guide.'
  },
  'PRE1b': {
    tip_1: 'Implement care practices that respect each patient\'\'s personal beliefs, cultural practices and value systems, including dietary preferences, prayer requirements and modesty considerations.',
    tip_2: 'Include a beliefs and values section in the admission form where staff document any specific patient preferences or cultural requirements that should be respected during care.',
    tip_3: 'Review patient complaint records monthly for any grievances related to disrespect of beliefs or values; use findings to improve staff practices.',
    tip_4: 'Train all staff on cultural sensitivity and religious diversity at induction, using local examples to demonstrate how to accommodate common patient preferences respectfully.'
  },
  'PRE1c': {
    tip_1: 'Ensure patient dignity is maintained during all examinations and treatments by using curtains, screens or private rooms, and asking for patient consent before exposing any body part.',
    tip_2: 'Post a patient dignity and privacy notice in all clinical areas reminding staff and patients of the right to privacy; make screens available at every examination point.',
    tip_3: 'Include privacy and dignity observations in monthly facility inspection rounds; note any area where screens are broken, curtains missing or privacy practices are inadequate.',
    tip_4: 'Train all clinical staff that maintaining privacy is a patient right; include a practical session on correct curtain and screen use during nursing induction.'
  },
  'PRE1d': {
    tip_1: 'Establish a written policy prohibiting all forms of patient neglect, physical abuse, verbal abuse and discrimination; define the reporting and investigation process clearly.',
    tip_2: 'Display the anti-abuse policy and reporting mechanism in patient care areas; ensure patients know they can report concerns anonymously through the complaint box or helpline.',
    tip_3: 'Review all patient abuse or neglect complaints monthly; investigate every allegation, document findings and take corrective action including disciplinary steps when confirmed.',
    tip_4: 'Train all staff at induction that patient abuse or neglect is a serious violation; use scenario-based exercises to help staff recognise and respond to warning signs.'
  },
  'PRE1e': {
    tip_1: 'Treat all patient health information as strictly confidential; ensure records are accessible only to treating team members and authorised personnel as defined in the confidentiality policy.',
    tip_2: 'Place patient records in secure locations, use password-protected electronic systems and ensure paper records are not left open in public areas.',
    tip_3: 'Conduct quarterly information security audits to check that electronic records require login, paper files are secured and no patient information is visible in public areas.',
    tip_4: 'Train all staff including administrative staff that discussing or displaying patient information in public areas or to unauthorised persons is a breach of patient rights and may be legally actionable.'
  },
  'PRE1f': {
    tip_1: 'Inform every patient of their right to refuse any proposed treatment and their right to seek a second opinion from another doctor without fear of affecting the quality of their care.',
    tip_2: 'Document refusal of treatment in the case sheet using a standard refusal form signed by the patient or guardian, with the clinical team\'\'s response and alternative plan noted.',
    tip_3: 'Review cases of documented treatment refusal monthly to ensure the patient\'\'s decision was respected, alternatives were offered and no coercive practice occurred.',
    tip_4: 'Train clinical staff to handle treatment refusal professionally, counsel the patient on consequences without pressure and document the informed refusal and alternatives discussed.'
  },
  'PRE1g': {
    tip_1: 'Obtain a separate written informed consent from the patient or legal guardian specifically for blood and blood product transfusion before any transfusion is initiated.',
    tip_2: 'Use a dedicated blood transfusion consent form explaining the blood product, purpose, risks including transfusion reactions and alternatives; file it before the first unit is administered.',
    tip_3: 'Audit transfusion files monthly to verify a signed transfusion consent is present for every patient who received blood products during the audit period.',
    tip_4: 'Train nursing and medical staff that blood transfusion consent is a separate mandatory requirement from general surgical consent and must be obtained before the transfusion begins.'
  },
  'PRE1h': {
    tip_1: 'Establish a patient complaint mechanism including a suggestion and complaint box, dedicated helpline, online feedback form and a named grievance officer accessible to all patients.',
    tip_2: 'Display the complaint process prominently in all patient areas listing available channels, the grievance officer\'\'s name and the timeframe for acknowledgement and resolution.',
    tip_3: 'Track all complaints in a register, acknowledge every complaint within 24 hours and report resolution rates and recurring themes to management monthly.',
    tip_4: 'Train all staff to direct patients with complaints to the correct channel, never dismiss a complaint and ensure no patient faces negative consequences for raising a concern.'
  },
  'PRE1i': {
    tip_1: 'Provide patients with a written estimate of the expected cost of their treatment at admission including bed charges, investigations, surgical fees and medication costs where possible.',
    tip_2: 'Issue a cost estimate letter or billing summary at admission; update it proactively when the treatment plan changes significantly and before any major additional expenditure.',
    tip_3: 'Review patient billing complaints monthly; identify cases where actual bills exceeded estimates without prior notice and implement process changes to prevent recurrence.',
    tip_4: 'Train front-desk and billing staff to explain the cost estimate clearly to patients or families at admission and to proactively communicate when costs are expected to change.'
  },
  'PRE1j': {
    tip_1: 'Allow patients or their authorised representatives to access and obtain copies of their clinical records upon request, following the hospital\'\'s defined record access procedure.',
    tip_2: 'Post the procedure for requesting medical records in patient areas; maintain a log of all record requests with request date, requester identity, records provided and date of provision.',
    tip_3: 'Review record access request logs monthly to verify all requests were fulfilled within the defined timeframe and that no patient was denied their clinical records without a lawful reason.',
    tip_4: 'Train admissions and medical records staff on the patient\'\'s right to access clinical records, the steps to process a request and the documentation required for authorised release.'
  },
  'PRE1k': {
    tip_1: 'Inform every patient of the name of their treating doctor and the names of key team members caring for them at admission and whenever the team changes.',
    tip_2: 'Display the treating doctor\'\'s name and the names of responsible nurses on the patient\'\'s bedside card; update it immediately when the treating team changes.',
    tip_3: 'Check that bedside identification cards are current and accurate during monthly ward rounds; flag and correct any discrepancy with the actual treating team.',
    tip_4: 'Train nursing staff to introduce themselves by name at every shift start and to introduce the treating doctor by name to new patients and families on admission.'
  },
  'PRE2a': {
    tip_1: 'Explain the proposed care plan, its risks, potential complications and available alternatives to the patient or family in a language they understand before obtaining consent.',
    tip_2: 'Document in the case sheet that pre-consent explanation was provided, what was explained, who was present and whether the patient or family had any questions.',
    tip_3: 'Audit consent documentation monthly to verify that evidence of explanation before consent is recorded in every case where a consent form was obtained.',
    tip_4: 'Train all clinical staff that obtaining a signature without adequate explanation is not informed consent; use simulation exercises to practise patient-appropriate explanation techniques.'
  },
  'PRE2b': {
    tip_1: 'Obtain written informed consent from patients or legal guardians for all procedures and treatments listed in the hospital\'\'s defined consent policy before any procedure begins.',
    tip_2: 'Maintain a hospital-approved list of procedures requiring formal written consent; use procedure-specific consent forms that describe the intervention, risks and alternatives.',
    tip_3: 'Audit all case files for consent form completeness monthly; check that the form is signed, dated and present in the file before the documented procedure date.',
    tip_4: 'Train clinical staff on which procedures require formal consent, how to complete the consent form correctly and that consent must be obtained by the performing clinician.'
  },
  'PRE2c': {
    tip_1: 'Ensure the consent process follows all applicable statutory and regulatory requirements including age of consent, consent for minors and legally incapacitated patients and documentation standards.',
    tip_2: 'Review all high-risk procedure consent forms to confirm they meet legal requirements: patient identity, diagnosis, procedure details, risks explained, patient signature and witness signature.',
    tip_3: 'Audit consent practices quarterly against current legal requirements; seek legal and ethics input whenever there is doubt about whether a specific situation meets statutory norms.',
    tip_4: 'Train clinical staff on the legal requirements for valid informed consent, including capacity assessment, substitute decision-making for incapacitated patients and documentation standards.'
  },
  'PRE2d': {
    tip_1: 'Educate every patient and family on their diagnosis, the care plan, how to prevent complications, possible risks and what care will be needed after discharge before the patient goes home.',
    tip_2: 'Document patient and family education in the case sheet noting topics covered, format used such as verbal or leaflet, understanding confirmed and any questions answered.',
    tip_3: 'Audit patient education documentation monthly to verify it is present in every in-patient record before discharge and that home-care and preventive guidance is included.',
    tip_4: 'Train nurses and doctors on effective patient education techniques including teach-back method; use standard educational materials for common conditions to ensure consistency.'
  },
  'PRE2e': {
    tip_1: 'Communicate with patients and families using clear, simple language, professional interpreters when needed and written materials in the patient\'\'s language to ensure understanding.',
    tip_2: 'Document each significant communication with patients or families in the case sheet noting the content, medium used, interpreter if applicable and the patient\'\'s response.',
    tip_3: 'Review patient communication-related complaints monthly to identify language or clarity barriers and implement targeted improvements such as additional translated materials.',
    tip_4: 'Train clinical and administrative staff on effective patient communication including how to access interpreter services and how to confirm patient understanding using teach-back.'
  },
  'PRE2f': {
    tip_1: 'Implement a patient feedback mechanism using surveys, suggestion boxes, exit interviews and a formal complaint process with a designated grievance officer and defined resolution timelines.',
    tip_2: 'Collect and record patient feedback systematically; log all complaints with date, nature of complaint, action taken and resolution date in a grievance register.',
    tip_3: 'Analyse feedback and complaint data monthly; present recurring themes, resolution rates and patient satisfaction trends at the quality committee meeting.',
    tip_4: 'Train all patient-facing staff on how to encourage feedback, direct formal complaints to the grievance officer and ensure no patient or family member faces any negative consequence for complaining.'
  },
  'IPC1a': {
    tip_1: 'Develop a comprehensive infection prevention and control programme document covering surveillance, outbreak response, precaution types, training schedule and review frequency, updated at least annually.',
    tip_2: 'File the current IPC programme document in the infection control office and make it accessible to all department heads; mark the review date clearly on the cover.',
    tip_3: 'Review the IPC programme comprehensively once a year and after any significant outbreak or regulatory change; document the review meeting minutes and any programme amendments.',
    tip_4: 'Brief all clinical department heads on the IPC programme content at annual orientation and notify them of any updates via a written circular within two weeks of change.'
  },
  'IPC1b': {
    tip_1: 'Implement the five moments of hand hygiene using alcohol-based hand rub or soap and water, enforce standard precautions for all patients and apply transmission-based precautions for known infectious cases.',
    tip_2: 'Post WHO five-moment hand hygiene posters and precaution signage at every patient zone entry point, hand hygiene station and isolation room door.',
    tip_3: 'Conduct monthly hand hygiene observation audits in all clinical areas using the WHO observation tool; share compliance rates with department heads and the infection control committee.',
    tip_4: 'Train all clinical and support staff on hand hygiene five moments and precaution types at induction; repeat annual training and monitor compliance improvement over time.'
  },
  'IPC1c': {
    tip_1: 'Follow safe injection and infusion practices for every parenteral procedure including one needle one syringe policy, aseptic technique for IV preparation and single-use vials where mandated.',
    tip_2: 'Post safe injection practice guidelines at all injection preparation areas; maintain a needle-stick injury register and report all sharps injuries to infection control within 24 hours.',
    tip_3: 'Conduct monthly observation audits of injection preparation and administration practices; document any unsafe practice as an incident and follow up with retraining.',
    tip_4: 'Train all nursing staff on safe injection practices, aseptic non-touch technique and the consequences of reusing needles or multi-dose vials incorrectly during nursing induction.'
  },
  'IPC1d': {
    tip_1: 'Establish an antimicrobial stewardship programme with a written policy specifying antibiotic prescribing criteria, restricted antibiotic approval process and regular antibiogram review.',
    tip_2: 'Post the hospital antibiogram and antimicrobial prescribing guidelines in clinical areas and the pharmacy; circulate updates to all prescribers when the antibiogram is refreshed.',
    tip_3: 'Review antibiotic prescription patterns monthly with the infection control team and microbiologist; audit restricted antibiotic approvals and report findings to the antimicrobial stewardship committee.',
    tip_4: 'Train all prescribers on the antimicrobial policy, how to interpret the antibiogram and the process for requesting approval to use restricted antibiotics at clinical induction.'
  },
  'IPC1e': {
    tip_1: 'Provide pre-exposure prophylaxis for identified occupational exposures such as Hepatitis B vaccination for all clinical staff and post-exposure prophylaxis for needle-stick and mucosal exposures.',
    tip_2: 'Maintain a vaccination and exposure prophylaxis register for all staff listing vaccine given, date, next dose and any exposure incidents with prophylaxis provided.',
    tip_3: 'Audit staff vaccination records quarterly to confirm all new staff received mandatory pre-exposure vaccinations and that all reported exposures received timely post-exposure prophylaxis.',
    tip_4: 'Train all staff on the types of occupational exposures covered by the prophylaxis policy, how to report an exposure immediately and where to access post-exposure care at any time.'
  },
  'IPC1f': {
    tip_1: 'Conduct active surveillance to detect and monitor healthcare-associated infections including CAUTI, CLABSI, VAP and SSI rates, and implement corrective actions when rates exceed defined thresholds.',
    tip_2: 'Maintain an infection surveillance register updated weekly with HAI case counts per unit, calculate rates per device-day or patient-day and graph trends monthly.',
    tip_3: 'Present HAI surveillance data at the infection control committee every month; investigate any rate exceeding the defined benchmark and track improvement actions to closure.',
    tip_4: 'Train infection control link nurses in each department on how to identify and report suspected HAI cases; review surveillance methodology annually for accuracy and completeness.'
  },
  'IPC2a': {
    tip_1: 'Segregate biomedical waste at the point of generation into colour-coded bags and containers as per BMW Rules; ensure timely collection, storage in the common facility and authorised disposal.',
    tip_2: 'Display BMW segregation charts at every generation point; maintain a daily waste quantity log and BMW manifests for all handovers to the authorised collection agency.',
    tip_3: 'Conduct monthly BMW audits checking segregation compliance, container condition, storage area hygiene and manifests; report non-compliance to the infection control and environmental officer.',
    tip_4: 'Train all clinical and support staff on BMW segregation categories, colour coding, what goes into each container and the legal consequences of incorrect segregation at induction.'
  },
  'IPC2b': {
    tip_1: 'Install and maintain engineering controls such as negative pressure isolation rooms, appropriate ventilation in procedure areas, laminar airflow in OT and HEPA filtration where required.',
    tip_2: 'Maintain an engineering controls register listing each system, its location, design specification, maintenance schedule and most recent performance test result.',
    tip_3: 'Test ventilation and engineering control performance quarterly; review any failure findings with the infection control team and rectify deficiencies before resuming procedures in affected areas.',
    tip_4: 'Inform clinical staff which areas have special engineering controls, why they matter for infection prevention and what to do if a control system appears to malfunction.'
  },
  'IPC2c': {
    tip_1: 'Define cleaning and disinfection schedules and methods for all patient care areas specifying frequency, disinfectant type and concentration, contact time and responsible staff for each area type.',
    tip_2: 'Use cleaning checklists in every patient area with date, time, method and signature for each completed cleaning cycle; keep checklists visible for inspection.',
    tip_3: 'Audit cleaning practices and checklist completion weekly; conduct environmental surface cultures in high-risk areas quarterly and share results with housekeeping and infection control teams.',
    tip_4: 'Train housekeeping staff on correct dilution and use of approved disinfectants, cleaning sequence from clean to dirty areas and the increased frequency required in isolation rooms.'
  },
  'IPC2d': {
    tip_1: 'Follow validated decontamination processes for all reusable instruments and devices covering pre-cleaning, cleaning, packaging, sterilisation and sterility maintenance until use.',
    tip_2: 'Maintain a sterilisation log for every autoclave load recording cycle number, date, items, sterilisation parameters, indicator result and authorising technician.',
    tip_3: 'Test sterilisation effectiveness using biological indicators weekly and check chemical indicators with every load; quarantine and investigate any failed indicator immediately.',
    tip_4: 'Train CSSD staff on the full decontamination cycle, correct use of indicators, instrument inspection criteria and the protocol for releasing a failed steriliser load.'
  },
  'IPC2e': {
    tip_1: 'Collect, transport, launder, dry, fold and store linen using defined procedures that prevent cross-contamination between soiled and clean linen at every stage.',
    tip_2: 'Use colour-coded bags for soiled linen collection; maintain a linen processing log and keep laundry area segregated into soiled and clean zones with no flow reversal.',
    tip_3: 'Inspect laundry practices and facilities monthly for segregation compliance, washing temperature, chemical concentration and linen condition; document findings.',
    tip_4: 'Train laundry staff on safe linen handling procedures including protective equipment use when handling soiled linen, correct wash cycles and storage conditions at induction.'
  },
  'IPC2f': {
    tip_1: 'Follow kitchen sanitation standards covering food storage temperatures, preparation hygiene, equipment cleaning schedules, pest control and health checks for food handlers.',
    tip_2: 'Maintain kitchen sanitation logs for temperature monitoring, cleaning schedules, pest control visits and food handler health check records; file them in the dietary department.',
    tip_3: 'Conduct monthly kitchen hygiene audits using a structured checklist; test food samples for bacterial contamination quarterly and act on any out-of-specification result.',
    tip_4: 'Train kitchen and dietary staff on food safety principles, personal hygiene requirements, correct food storage temperatures and how to respond to a foodborne illness report.'
  },
  'PSQ1a': {
    tip_1: 'Establish a documented quality improvement and patient safety programme covering governance structure, annual objectives, improvement project methodology, indicator monitoring and reporting cycle.',
    tip_2: 'Maintain the quality programme document as a controlled file accessible to all department quality leads; display the programme summary and annual quality goals on the notice board.',
    tip_3: 'Review progress against quality programme objectives quarterly at the quality committee; report outcomes to hospital management and publish a summary to clinical staff.',
    tip_4: 'Orient all new staff to the quality and patient safety programme during induction; assign each department a quality focal point responsible for implementing local improvement actions.'
  },
  'PSQ1b': {
    tip_1: 'Implement all applicable NABH Patient Safety Goals including correct patient identification, effective communication, safe medication use, surgical safety and fall prevention with local adaptations.',
    tip_2: 'Post the adopted patient safety goals in all clinical areas and nursing stations; maintain a goals implementation register tracking status and evidence for each goal.',
    tip_3: 'Monitor compliance with each patient safety goal monthly using specific indicators; report non-compliant areas to the quality committee for corrective action.',
    tip_4: 'Train all clinical staff on each patient safety goal during induction and at annual refresher sessions; use patient safety incident data to illustrate why each goal matters.'
  },
  'PSQ1c': {
    tip_1: 'Establish a nursing quality improvement programme covering nursing-sensitive indicators such as medication errors, falls, pressure ulcers, needle-stick injuries and patient satisfaction with nursing care.',
    tip_2: 'Maintain a nursing quality dashboard updated monthly with indicator values, targets and trend analysis; review at the nursing leadership meeting.',
    tip_3: 'Analyse nursing quality indicator data monthly; identify wards with persistent compliance gaps, investigate root causes and implement targeted nursing improvement plans.',
    tip_4: 'Engage ward nursing staff in monthly quality data review; use their practical insights to design workable improvement actions and recognise wards that demonstrate improvement.'
  },
  'PSQ1d': {
    tip_1: 'Appoint a designated quality officer or head of quality department with defined responsibilities for overseeing the hospital-wide quality and patient safety programme.',
    tip_2: 'Document the quality officer\'\'s roles, responsibilities and authority in a formal job description or committee terms of reference; make the appointment visible to all staff.',
    tip_3: 'Verify at each accreditation readiness review that the designated quality officer is actively functioning, participating in meetings and maintaining programme documentation.',
    tip_4: 'Ensure the quality officer has protected time, management access and necessary resources; brief all department heads to cooperate with quality oversight activities.'
  },
  'PSQ2a': {
    tip_1: 'Identify and monitor key infection control indicators including CAUTI rate, CLABSI rate, VAP rate, SSI rate and hand hygiene compliance as part of the hospital quality programme.',
    tip_2: 'Update the infection control indicator dashboard monthly with calculated rates per device-day or patient-day; present data with trend analysis at the infection control committee.',
    tip_3: 'Investigate any indicator exceeding the defined threshold within one week; conduct a root cause analysis and implement corrective actions tracked to closure.',
    tip_4: 'Share infection control indicator results with all clinical department heads at monthly meetings; use the data to motivate hand hygiene and bundle compliance improvement.'
  },
  'PSQ2b': {
    tip_1: 'Define and track patient safety indicators including sentinel events, near-misses, wrong-site surgeries, falls with injury, medication errors and patient identification failures.',
    tip_2: 'Maintain a patient safety indicator log updated monthly; calculate rates, review trends and document all actions taken in response to adverse events or indicators above threshold.',
    tip_3: 'Review patient safety indicators at the quality committee monthly; conduct root cause analysis for all sentinel events and track corrective actions to verified closure.',
    tip_4: 'Train department heads to report patient safety events promptly, participate in root cause analysis and implement corrective actions; cultivate a no-blame reporting culture.'
  },
  'PSQ2c': {
    tip_1: 'Identify and monitor key clinical indicators such as mortality rate, re-admission rate, surgical complication rate and managerial indicators such as patient satisfaction scores and complaint resolution time.',
    tip_2: 'Maintain a combined clinical and managerial performance dashboard updated monthly; circulate reports to department heads and present at management review meetings.',
    tip_3: 'Analyse clinical and managerial indicator trends quarterly; benchmark against national or state data where available and present improvement proposals to the quality committee.',
    tip_4: 'Engage department heads in interpreting their unit\'\'s indicator data monthly; train them to distinguish between common cause and special cause variation to prioritise appropriate responses.'
  },
  'PSQ2d': {
    tip_1: 'Conduct structured clinical audits in each department involving clinicians in data collection, analysis and action planning to improve patient care quality.',
    tip_2: 'Maintain a clinical audit register listing each audit topic, audit lead, sample size, findings and corrective actions; track re-audit dates to verify improvement.',
    tip_3: 'Review clinical audit outputs at the quality committee quarterly; verify audits are completed on schedule, findings are shared with relevant clinicians and actions are implemented.',
    tip_4: 'Train department heads and clinical staff on how to design and conduct a clinical audit, analyse results and use findings to change practice; include clinical audit in annual training plans.'
  },
  'ROM1a': {
    tip_1: 'Identify the governing body or board of the organisation by name, define its composition, meeting frequency, quorum requirements, roles and responsibilities in a formal governance document.',
    tip_2: 'Maintain governance documents including bylaws, board resolutions and meeting minutes in a secure file accessible to quality and management as evidence of governance activity.',
    tip_3: 'Verify at each management review that the governing body has met at defined intervals, quorum was maintained and decisions are documented in formal minutes.',
    tip_4: 'Ensure all governing body members understand their roles and responsibilities; conduct an orientation for new members covering the organisation\'\'s mission, scope and governance obligations.'
  },
  'ROM1b': {
    tip_1: 'Register the organisation with all applicable regulatory bodies and maintain current compliance with all relevant laws covering clinical establishment, fire safety, labour, pharmacy and biomedical waste.',
    tip_2: 'Maintain a statutory compliance register listing every applicable licence with the issuing authority, issue date, expiry date and current status; flag renewals 90 days in advance.',
    tip_3: 'Audit the compliance register quarterly to confirm all licences are valid, renewals are in progress where needed and no area is operating without required approvals.',
    tip_4: 'Assign a compliance officer to track all regulatory requirements, file renewals in time and brief management on any new laws affecting the organisation\'\'s operations.'
  },
  'ROM2a': {
    tip_1: 'Publish the organisation\'\'s mission statement and core values prominently at the main entrance, reception area, patient waiting areas and on the hospital website.',
    tip_2: 'Display the mission statement on high-quality signage in reception and patient areas; include it in the staff handbook and patient information materials.',
    tip_3: 'Check during monthly facility rounds that mission statement displays are present, undamaged and accurately reflect the current approved version.',
    tip_4: 'Communicate the mission statement to all new staff during induction and explain how it guides daily work; conduct annual values alignment discussions at department meetings.'
  },
  'ROM2b': {
    tip_1: 'Develop and implement a code of ethics for the organisation covering conflict of interest, referral practices, billing transparency, patient rights and research ethics, reviewed and approved by the governing body.',
    tip_2: 'Circulate the code of ethics to all staff; maintain a signed acknowledgement register confirming each staff member has read and understood the ethical standards expected.',
    tip_3: 'Review ethics policy compliance annually; investigate any reported ethics violation promptly and document findings and actions in the ethics committee records.',
    tip_4: 'Train all staff on the code of ethics at induction; discuss specific ethical scenarios relevant to their role so they can apply the principles in everyday situations.'
  },
  'ROM2c': {
    tip_1: 'Ensure the billing process is based on actual services rendered using pre-disclosed rates; prevent unbundling, upcoding or charging for services not delivered.',
    tip_2: 'Display a publicly accessible rate card for common services, consultations and procedures at the billing counter and on the hospital website.',
    tip_3: 'Audit a sample of patient bills monthly to verify charges match the prescribed rate card and the services documented in the clinical record with no unjustified additions.',
    tip_4: 'Train billing staff on the ethical billing policy, the importance of charging only for services rendered and the process for handling a patient\'\'s query about their bill.'
  },
  'ROM3a': {
    tip_1: 'Establish functioning committees for infection control, quality improvement, pharmacy and therapeutics, and other key functions with defined terms of reference, membership and meeting schedules.',
    tip_2: 'Maintain committee records including terms of reference, membership lists, meeting minutes and action trackers for each committee; file them accessibly for review.',
    tip_3: 'Verify at each quality review that all designated committees have met at their required frequency, quorum was maintained and meeting actions are being tracked to completion.',
    tip_4: 'Orient new committee members on their committee\'\'s terms of reference, scope of authority and expected contribution; share past meeting minutes to provide continuity of context.'
  },
  'ROM3b': {
    tip_1: 'Ensure all outsourced services are covered by a written agreement specifying scope, quality standards, performance expectations, confidentiality obligations and review process.',
    tip_2: 'Maintain a register of all outsourced service agreements with service type, provider name, agreement start and end date, quality requirements and last review date.',
    tip_3: 'Review outsourced service performance against contractual quality standards annually; renew agreements only if quality standards have been met and document the review decision.',
    tip_4: 'Train the department heads who manage outsourced services on the contractual standards expected, how to raise a performance concern with the vendor and escalation to management.'
  },
  'ROM3c': {
    tip_1: 'Establish a formal mechanism for patients and staff to report violations of patient rights, with a confidential reporting pathway, named officer to receive reports and defined investigation and resolution process.',
    tip_2: 'Display the patient rights violation reporting mechanism prominently in all patient areas including how to contact the designated officer, email or phone number.',
    tip_3: 'Review all reported patient rights violations monthly; investigate each report within a defined timeframe, document findings and outcomes and report to the management committee.',
    tip_4: 'Train all staff that patient rights violations must be reported without delay and that no staff member should discourage a patient or colleague from making a rights complaint.'
  },
  'ROM4a': {
    tip_1: 'Develop a long-term strategic plan updated at least every three years addressing financial sustainability, infrastructure development, service expansion and human resource planning.',
    tip_2: 'Document the strategic plan with specific goals, timelines, resource requirements and measurable targets; present it to the governing body for formal approval and periodic review.',
    tip_3: 'Review strategic plan progress annually at the governing body meeting; measure achievement of targets and update the plan to reflect changing organisational priorities.',
    tip_4: 'Communicate key elements of the strategic plan to all department heads so they can align their departmental plans with the organisation\'\'s long-term sustainability goals.'
  },
  'ROM4b': {
    tip_1: 'Implement energy and environment efficiency initiatives including LED lighting, solar panels, water conservation, waste reduction and green procurement policies.',
    tip_2: 'Maintain records of energy consumption, water usage, waste quantities and environmental initiative progress; report metrics at the annual management review.',
    tip_3: 'Review environmental and energy performance indicators annually; set reduction targets and track progress quarter by quarter against the previous year\'\'s baseline.',
    tip_4: 'Create awareness among all staff about the organisation\'\'s environmental commitments; encourage staff to suggest practical energy-saving or waste-reduction measures in their work area.'
  },
  'ROM4c': {
    tip_1: 'Define corporate social responsibility activities such as free camps, community health education, support for underprivileged patients and environmental outreach as part of the organisation\'\'s annual plan.',
    tip_2: 'Document all social responsibility activities with dates, beneficiaries reached, resources used and outcomes achieved; compile an annual CSR report reviewed by the governing body.',
    tip_3: 'Review CSR activity progress quarterly against the annual plan; report outcomes to the governing body and use data to plan future community engagement activities.',
    tip_4: 'Engage staff in CSR activities by communicating the organisation\'\'s social responsibility goals and creating opportunities for staff to volunteer in community health programmes.'
  },
  'ROM4d': {
    tip_1: 'Implement staff well-being programmes addressing physical health, mental health, work-life balance, occupational hazard protection and recognition of staff contribution.',
    tip_2: 'Document well-being programme activities including health screenings, counselling services, staff recognition events and grievance resolution in an annual staff welfare report.',
    tip_3: 'Survey staff well-being and satisfaction annually; review results at the HR committee and implement targeted interventions for issues identified in the survey.',
    tip_4: 'Train managers to recognise signs of staff burnout or distress and refer staff to available support services; communicate well-being resources to all staff at induction.'
  },
  'FMS1a': {
    tip_1: 'Maintain all patient care areas in a clean, hygienic and structurally safe condition with adequate space, lighting, ventilation and functional equipment as required by patient safety standards.',
    tip_2: 'Use a facility condition register to record maintenance requests, completion dates and responsible staff; keep the register updated after every facility inspection round.',
    tip_3: 'Conduct monthly facility inspection rounds across all patient care areas and document findings, corrective actions and completion status in a structured inspection report.',
    tip_4: 'Train housekeeping and maintenance staff on the cleaning and maintenance standards required in patient care areas; brief them on any new area-specific requirements quarterly.'
  },
  'FMS1b': {
    tip_1: 'Conduct a structured facility safety inspection round at least once a month covering all patient care, utility and support areas to identify and address safety hazards.',
    tip_2: 'Use a standardised monthly inspection checklist that covers infrastructure, electrical safety, fire equipment, emergency exits, signage and housekeeping; file completed checklists.',
    tip_3: 'Review monthly facility inspection reports at the safety committee meeting; track all identified hazards to corrective action completion before the next inspection.',
    tip_4: 'Train the facility safety inspection team on what to look for during rounds, how to use the checklist and how to classify and escalate hazards by severity.'
  },
  'FMS1c': {
    tip_1: 'Identify areas requiring additional security such as labour room, neonatal unit, ICU, pharmacy, server room and cash office; implement access control appropriate to the risk level of each area.',
    tip_2: 'Maintain an access control register listing each restricted area, the security measure in place such as key card, lock or guard, and authorised personnel.',
    tip_3: 'Test access control measures for all high-security areas monthly; review any access breach incident within 24 hours and strengthen controls where gaps are identified.',
    tip_4: 'Brief all staff on which areas require restricted access, why it matters for patient and staff safety and the consequences of sharing access codes or keys with unauthorised persons.'
  },
  'FMS1d': {
    tip_1: 'Install clear, consistent internal and external signage in languages understood by the majority of patients and staff, covering directions, department locations, emergency exits and hazard warnings.',
    tip_2: 'Maintain a signage inventory listing all required signs, their location, language and condition; update the inventory whenever the facility layout or services change.',
    tip_3: 'Inspect all internal and external signage during monthly facility rounds for visibility, accuracy, damage and language appropriateness; replace non-compliant signs within two weeks.',
    tip_4: 'Survey patient and visitor feedback on signage clarity annually; use results to improve sign placement, language or design in areas where navigation difficulties are frequently reported.'
  },
  'FMS1e': {
    tip_1: 'Identify all hazardous materials used in the hospital including chemicals, gases, cytotoxics and disinfectants; store, handle and dispose of them following written safety procedures and legal requirements.',
    tip_2: 'Maintain a hazardous materials inventory with MSDS for each substance, approved storage location, required PPE and disposal method; keep MSDS accessible at point of use.',
    tip_3: 'Inspect hazardous material storage areas monthly to verify MSDS availability, correct storage conditions, PPE availability and absence of leaks or improper labelling.',
    tip_4: 'Train all staff who handle hazardous materials on correct use, storage requirements, PPE selection, spill response and disposal procedures; document training completion.'
  },
  'FMS2a': {
    tip_1: 'Implement written maintenance plans for all engineering support systems including HVAC, electrical panels, plumbing, lifts, medical gases and backup power; execute maintenance on schedule.',
    tip_2: 'Use a planned preventive maintenance register for all utility systems listing equipment, maintenance frequency, last service date, next due date and servicing technician.',
    tip_3: 'Verify maintenance completion records monthly; flag any overdue maintenance items and confirm they are addressed before the system is used for patient care.',
    tip_4: 'Train engineering and maintenance staff on the planned maintenance schedule, how to document completed work and the escalation protocol when a critical system fails unexpectedly.'
  },
  'FMS2b': {
    tip_1: 'Maintain, inspect and calibrate all medical equipment on a documented schedule; keep calibration certificates and maintenance records available for every device in use.',
    tip_2: 'Use a medical equipment maintenance register listing each device, serial number, maintenance schedule, last service date, calibration due date and certificate reference.',
    tip_3: 'Audit medical equipment records quarterly to confirm all devices are within calibration validity, maintenance is current and out-of-service equipment is tagged and removed from use.',
    tip_4: 'Train biomedical technicians to complete maintenance and calibration records accurately; train clinical staff to perform daily pre-use checks and report faulty equipment immediately.'
  },
  'FMS3a': {
    tip_1: 'Ensure potable water and uninterrupted electrical power are available 24 hours a day by maintaining backup systems including generators, UPS and stored water reserves.',
    tip_2: 'Log daily generator testing, fuel levels, UPS battery status and water reserve volumes in a utilities availability register signed by the maintenance in-charge.',
    tip_3: 'Test backup generator auto-changeover and UPS systems monthly; review the utilities register weekly for any gaps in availability and respond to supply interruptions immediately.',
    tip_4: 'Train maintenance staff on backup system operation, how to respond to power or water supply failure and the escalation protocol for prolonged outages affecting patient care.'
  },
  'FMS3b': {
    tip_1: 'Handle medical gases including oxygen, nitrous oxide and medical air and vacuum systems safely; ensure supply is continuous, cylinders are secured and manifold systems are inspected regularly.',
    tip_2: 'Maintain a medical gas inventory log recording cylinder stock, pressure levels, supplier delivery records and inspection dates for manifold and distribution systems.',
    tip_3: 'Inspect medical gas storage areas and distribution points monthly; check cylinder security, valve condition, area ventilation and leakage detection devices.',
    tip_4: 'Train all staff who handle medical gas cylinders on safe storage, correct connection, cylinder securing, leak detection and the emergency protocol for a gas supply failure.'
  },
  'FMS4a': {
    tip_1: 'Install and maintain fire detection systems including smoke detectors and alarm panels, suppression systems such as sprinklers or CO2 systems and fire extinguishers throughout the facility.',
    tip_2: 'Maintain a fire safety equipment register listing each device, type, location, installation date, last inspection date and next service due date.',
    tip_3: 'Test fire alarms and detection systems monthly; verify extinguisher pressure gauges and sprinkler head integrity quarterly; document all tests in the fire safety register.',
    tip_4: 'Train all staff on how to raise a fire alarm, use the correct extinguisher type and the location of the nearest fire point in their work area during induction.'
  },
  'FMS4b': {
    tip_1: 'Maintain all fire-related equipment and infrastructure including extinguishers, hose reels, hydrants, alarm panels, emergency lighting and fire doors on a documented preventive maintenance schedule.',
    tip_2: 'Use a fire equipment maintenance register with equipment ID, location, maintenance type, last service date, engineer name and next due date; retain service certificates.',
    tip_3: 'Audit the fire equipment maintenance register quarterly to confirm all items are serviced on schedule; escalate overdue maintenance items to the facility manager for immediate action.',
    tip_4: 'Train maintenance staff responsible for fire equipment on the manufacturer\'\'s maintenance requirements, how to identify faulty equipment and the reporting protocol for failed items.'
  },
  'FMS4c': {
    tip_1: 'Document and display a safe exit or evacuation plan for every floor and area of the hospital, showing the nearest emergency exits, assembly points and evacuation route.',
    tip_2: 'Post emergency exit floor plans at eye level near staircase entries and ward exits; mark evacuation routes on floors with non-slip reflective tape and ensure exits are never obstructed.',
    tip_3: 'Inspect evacuation route signage, exit door functionality and assembly point markings monthly during facility safety rounds; rectify any obstruction or damaged sign within 24 hours.',
    tip_4: 'Familiarise all staff with the evacuation plan for their specific work area at induction; include the nearest exit and assembly point location in the induction checklist for every department.'
  },
  'FMS4d': {
    tip_1: 'Conduct at least two fire safety mock drills per year across the entire facility; evaluate staff response, evacuation efficiency and equipment handling during each drill.',
    tip_2: 'Document each mock drill with date, area covered, scenario used, number of staff participating, observations and corrective actions identified.',
    tip_3: 'Review mock drill reports to identify recurring gaps in evacuation speed, staff response or equipment handling; track improvement between successive drills.',
    tip_4: 'Debrief all staff who participated in the drill immediately afterwards; explain what went well and what needs to improve so learning is immediate and applied in the next drill.'
  },
  'HRM1a': {
    tip_1: 'Plan and maintain a staffing complement that matches the volume of patients, range of services and operational hours across all departments, ensuring no critical care area is under-staffed.',
    tip_2: 'Maintain a staffing plan document specifying the required number and category of staff per unit per shift, updated annually or whenever service volume changes significantly.',
    tip_3: 'Review actual staffing against the approved staffing plan monthly; flag any persistent shortfall to HR and management for recruitment or redeployment action.',
    tip_4: 'Ensure department heads review their shift rosters daily and escalate to HR immediately whenever actual staffing falls below the minimum required for safe patient care.'
  },
  'HRM1b': {
    tip_1: 'Create written job descriptions and job specifications for every category of staff defining the purpose of the role, key responsibilities, required qualifications, experience and reporting relationship.',
    tip_2: 'File approved job descriptions in HR records and provide a copy to each staff member at appointment; update the job description whenever the role changes significantly.',
    tip_3: 'Audit HR files annually to verify every position has a current, signed job description; identify positions without job descriptions and create them within 30 days.',
    tip_4: 'Use job descriptions during staff induction to clarify expectations; revisit the job description at performance appraisal time to assess role delivery against documented responsibilities.'
  },
  'HRM1c': {
    tip_1: 'Develop a written code of conduct defining expected professional behaviour, dress standards, patient interaction norms, use of hospital resources and disciplinary consequences for violation.',
    tip_2: 'Provide every staff member with a copy of the code of conduct at joining; maintain a signed acknowledgement in each staff member\'\'s HR file.',
    tip_3: 'Review reported code of conduct violations monthly; investigate each case using the defined process, document the outcome and track repeat violations for pattern analysis.',
    tip_4: 'Train all new staff on the code of conduct during induction using specific examples of acceptable and unacceptable behaviour relevant to their role and department.'
  },
  'HRM2a': {
    tip_1: 'Define a training and development policy specifying mandatory training types, minimum training hours per year, eligible staff, approval process and record-keeping requirements.',
    tip_2: 'Maintain a training policy document approved by management as a controlled file; update it whenever training requirements change and circulate updates to department heads.',
    tip_3: 'Audit training programme delivery quarterly against the training policy to confirm training types, frequency and participation meet the defined requirements.',
    tip_4: 'Communicate the training policy to all department heads at the start of each year; include training completion as a metric in their annual performance evaluation.'
  },
  'HRM2b': {
    tip_1: 'Provide every new employee with a structured induction training programme before they begin independent work, covering hospital policies, safety rules, patient rights, infection control and their specific role.',
    tip_2: 'Use a standardised induction checklist for every new staff member documenting each topic covered, date, trainer name and new employee signature of completion.',
    tip_3: 'Audit induction records for all staff who joined in the past quarter to verify induction was completed before the staff member began independent clinical or operational duties.',
    tip_4: 'Assign a named induction mentor to every new staff member; the mentor guides the inductee through the checklist and confirms all required topics were understood.'
  },
  'HRM2c': {
    tip_1: 'Provide each clinical staff member with regular job-specific training covering new techniques, updated protocols, equipment use and clinical skill refreshers relevant to their role.',
    tip_2: 'Maintain individual training records for each staff member listing all training attended, training dates, competency assessments and outcomes.',
    tip_3: 'Audit training attendance records quarterly to confirm all clinical staff are meeting minimum training hour requirements; follow up with department heads where compliance is low.',
    tip_4: 'Schedule job-specific training sessions in advance and include them in the department calendar; report completion rates to HR and management at each monthly meeting.'
  },
  'HRM2d': {
    tip_1: 'Train all staff regularly on safety and quality topics including hand hygiene, fire safety, medication safety, patient identification, incident reporting and patient rights.',
    tip_2: 'Document all safety and quality training in a central training register showing staff name, designation, training topic, date and outcome of any associated competency test.',
    tip_3: 'Review safety and quality training completion rates quarterly and target departments with low compliance for prioritised follow-up training sessions.',
    tip_4: 'Use real incident or near-miss cases from the hospital as case studies in safety and quality training; anonymise cases before use to maximise learning impact.'
  },
  'HRM2e': {
    tip_1: 'Train all staff on disaster response, fire evacuation procedures and non-fire emergencies such as medical gas failure, power outage and bomb threat using scenario-based exercises.',
    tip_2: 'Maintain disaster and emergency training records for all staff with training date, scenario covered, competency assessment result and trainer name.',
    tip_3: 'Evaluate training effectiveness by conducting unannounced drills and assessing staff response accuracy; use the gap analysis to update training content for the next cycle.',
    tip_4: 'Include disaster and emergency response training in every new staff induction before deployment to any clinical or critical area; repeat the training at minimum annually.'
  },
  'HRM3a': {
    tip_1: 'Conduct performance appraisals for all staff at defined intervals, at minimum annually, using standardised appraisal forms that assess both technical performance and professional behaviour.',
    tip_2: 'File completed and signed appraisal forms in each staff member\'\'s HR file; document development plans, training needs and agreed performance targets for the next period.',
    tip_3: 'Audit HR files annually to confirm all staff have a completed appraisal on record within the defined period; follow up with department heads where appraisals are overdue.',
    tip_4: 'Train all managers on how to conduct a fair, structured performance appraisal including how to give constructive feedback and how to create a meaningful development plan.'
  },
  'HRM3b': {
    tip_1: 'Define and communicate a fair disciplinary process for misconduct and a separate grievance handling process for staff complaints, with clear steps, timelines and appeal rights.',
    tip_2: 'Document all disciplinary proceedings and grievance complaints with dates, parties involved, evidence considered, decision and any appeal in a confidential HR file.',
    tip_3: 'Review all open disciplinary or grievance cases monthly to ensure they are progressing within defined timeframes and that decisions are documented before the case is closed.',
    tip_4: 'Train HR staff and managers on how to conduct a fair disciplinary enquiry or grievance investigation, how to document findings and how to communicate decisions professionally.'
  },
  'HRM4a': {
    tip_1: 'Provide all staff with access to occupational health services including pre-employment health screening, immunisation, management of work-related injuries and periodic health monitoring.',
    tip_2: 'Maintain an occupational health register for all staff recording pre-employment screening results, vaccinations, injury incidents and health review dates.',
    tip_3: 'Review occupational health records for all staff annually; follow up on any health monitoring due dates, pending vaccinations or untreated work-related health issues.',
    tip_4: 'Inform all new staff at induction about available occupational health services, how to access them and the importance of reporting any work-related injury or illness promptly.'
  },
  'HRM4b': {
    tip_1: 'Establish a workplace violence prevention programme covering identification of violence risks, reporting mechanisms, security measures, support for affected staff and zero-tolerance policy.',
    tip_2: 'Maintain a workplace violence incident register logging each reported incident with date, nature of incident, perpetrator type, immediate response and follow-up action.',
    tip_3: 'Review all reported workplace violence incidents monthly; analyse patterns by location, shift or type and implement targeted preventive measures based on findings.',
    tip_4: 'Train all staff on recognising escalating aggression, de-escalation techniques, how to raise an alarm and the reporting process for any violent or threatening incident.'
  },
  'HRM5a': {
    tip_1: 'Create and maintain a personal file for every staff member from the date of appointment containing their application, appointment letter, credentials, training records and HR correspondence.',
    tip_2: 'Organise HR personal files with a standard structure so each file contains the same set of documents in the same order; keep files locked and accessible only to authorised HR staff.',
    tip_3: 'Audit a sample of HR personal files quarterly to confirm all required documents are present, current and correctly filed; report and rectify any gaps within 30 days.',
    tip_4: 'Assign an HR officer responsible for maintaining personal file completeness; train them on what documents each file must contain and how to obtain missing items from staff.'
  },
  'HRM5b': {
    tip_1: 'Ensure each staff member\'\'s HR file includes verified copies of educational credentials, registration certificates, training completion records, competency assessments and latest performance appraisal.',
    tip_2: 'Use a personal file checklist for each staff category listing every required document; sign off the checklist after verifying each item is present in the file.',
    tip_3: 'Audit HR files for clinical staff quarterly to confirm credentials are verified with original, registration is current and training records are complete to date.',
    tip_4: 'Train HR staff to collect and verify all credentials at the time of joining, request renewal certificates before expiry and update training records within two weeks of completion.'
  },
  'HRM5c': {
    tip_1: 'Grant clinical privileges to doctors and nurses based on documented assessment of their qualifications, training, relevant experience and current registration status, reviewed and approved by the credentials committee.',
    tip_2: 'Maintain a clinical privilege register for each medical and nursing professional listing the procedures and areas they are authorised to practise in, with review dates.',
    tip_3: 'Audit the privilege register annually to confirm privileges are current, supported by verified credentials and that no practitioner is performing procedures outside their granted scope.',
    tip_4: 'Train nursing managers and department heads to verify that any new practitioner has been granted appropriate privileges before allowing them to independently manage patients.'
  },
  'IMS1a': {
    tip_1: 'Identify the information needs of each staff category, establish communication channels for disseminating policies, clinical alerts and operational updates, and verify that information reaches all intended recipients.',
    tip_2: 'Maintain a communication log or newsletter register showing what information was shared, the channel used, target audience and date; confirm receipt by acknowledgement or read receipt.',
    tip_3: 'Survey staff annually on whether they receive accurate and timely information needed for their work; use results to improve information dissemination channels.',
    tip_4: 'Train department heads to cascade important information to all their staff within 48 hours of receipt; use a confirmation mechanism so the quality team can verify cascade completion.'
  },
  'IMS1b': {
    tip_1: 'If telemedicine services are provided, ensure they comply with applicable national telemedicine guidelines covering patient consent, doctor registration, prescription standards and record keeping.',
    tip_2: 'Maintain a telemedicine practice register recording each consultation with patient ID, consulting doctor, platform used, consent documented and prescription issued.',
    tip_3: 'Audit telemedicine records quarterly to verify compliance with applicable guidelines, including consent, documentation quality and prescription standards.',
    tip_4: 'Train doctors who provide telemedicine consultations on the applicable national guidelines, consent requirements and documentation standards before they begin providing the service.'
  },
  'IMS1c': {
    tip_1: 'Adopt digital health tools such as electronic medical records, clinical decision support, digital appointment systems and patient portals to improve care quality and efficiency.',
    tip_2: 'Document the digital health technology implementation plan listing each tool, implementation date, clinical area covered, training delivered and benefits measured.',
    tip_3: 'Review digital health technology performance annually including system uptime, user adoption rate and measurable quality improvements attributable to the technology.',
    tip_4: 'Train all staff who use digital health systems during implementation and provide refresher training after each system update; appoint a superuser in each department to support peers.'
  },
  'IMS2a': {
    tip_1: 'Assign a unique identifier to every patient medical record at registration and ensure this identifier is printed on every document in the file and used to link all records related to that patient.',
    tip_2: 'Configure the HIS to require a unique patient ID before any record can be created or retrieved; print the ID on wristbands, case sheets, lab and imaging requisitions.',
    tip_3: 'Audit a sample of medical records weekly to confirm every document in the file carries the correct unique patient identifier and that no record exists without one.',
    tip_4: 'Train front-desk and clinical staff that the unique patient identifier must appear on every piece of documentation and must be verified at every point of care delivery.'
  },
  'IMS2b': {
    tip_1: 'Maintain each patient\'\'s medical record as a complete, accurate and chronologically ordered account of all care received, with no missing dates, gaps in timeline or incomplete entries.',
    tip_2: 'Use a structured record format with date-ordered sections for history, examination, investigation results, treatment and progress notes so all records follow the same order.',
    tip_3: 'Conduct weekly medical record quality audits checking for completeness, chronological order, missing entries and unsigned notes; provide feedback to record authors.',
    tip_4: 'Train all clinical staff that incomplete or out-of-order records compromise care continuity and medico-legal protection; demonstrate the correct documentation standard during induction.'
  },
  'IMS2c': {
    tip_1: 'Require every entry in the medical record to be signed by the author with their printed name, designation, date and time of entry immediately after the entry is made.',
    tip_2: 'Use printed name stamps or a signature legend sheet in each case file listing all authorised entry makers with their specimen signatures for identification purposes.',
    tip_3: 'Audit 10 medical records weekly to check that all entries have a signature, printed name, date and time; flag unsigned or undated entries to the department head.',
    tip_4: 'Train all clinical staff that making an unsigned or undated entry in a medical record is a documentation violation that may affect the patient\'\'s legal protection and the clinician\'\'s accountability.'
  },
  'IMS2d': {
    tip_1: 'Review medical records periodically to assess completeness, accuracy, timeliness of documentation and compliance with record-keeping standards; use findings to drive improvement.',
    tip_2: 'Conduct structured medical record audits using a standardised tool at least monthly; document findings, scores and corrective actions in a records audit register.',
    tip_3: 'Report medical record audit findings to the medical records committee monthly; track improvement in documentation quality indicators over successive audit cycles.',
    tip_4: 'Share de-identified medical record audit results with clinical staff at department meetings; recognise departments with consistently high documentation quality scores.'
  },
  'IMS3a': {
    tip_1: 'Implement access controls, audit trails, secure storage and data backup systems to protect patient information from unauthorised access, modification, loss or breach.',
    tip_2: 'Maintain a data security register documenting access rights by user role, backup schedule, last backup date, audit trail review dates and any security incident reported.',
    tip_3: 'Review information security controls quarterly including access logs, backup completion records and any breach or attempted breach; escalate security incidents immediately.',
    tip_4: 'Train all staff on information security responsibilities including password management, not sharing login credentials, locking screens when away and reporting suspected breaches immediately.'
  },
  'IMS3b': {
    tip_1: 'Disclose patient health information only when authorised by the patient in writing or as required by applicable law such as court order, notifiable disease reporting or medico-legal obligations.',
    tip_2: 'Maintain a disclosure log recording every instance of health information released, the requester, the legal or consent basis, what was disclosed and the date.',
    tip_3: 'Audit the disclosure log quarterly to confirm all disclosures had documented authorisation or legal basis; investigate any disclosure without a documented justification.',
    tip_4: 'Train medical records and clinical staff on the legal basis for health information disclosure, how to handle a request from police, courts or external agencies and how to document each disclosure.'
  },
  'IMS3c': {
    tip_1: 'Implement a document control system that ensures all policies and procedures are uniquely numbered, version-controlled, reviewed on schedule, approved before use and archived when superseded.',
    tip_2: 'Maintain a document control register listing every controlled document with document number, title, current version, review date, approving authority and distribution list.',
    tip_3: 'Audit the document control register quarterly to confirm all documents are within review validity, obsolete versions are withdrawn and current versions are accessible to users.',
    tip_4: 'Train all document owners on the document control procedure including how to initiate a review, submit for approval, update the version number and withdraw the old version from circulation.'
  },
  'IMS3d': {
    tip_1: 'Define the retention period for each type of clinical record as required by applicable laws and hospital policy; store records securely for the full retention period before authorised destruction.',
    tip_2: 'Maintain a records retention schedule listing each record type, retention period, storage location and destruction method; obtain management approval before any records are destroyed.',
    tip_3: 'Audit the records retention schedule annually to verify records due for destruction are processed only per the approved schedule and that active records are not inadvertently destroyed.',
    tip_4: 'Train medical records staff on retention periods for each record type, secure storage requirements and the authorised destruction procedure including documentation required before and after destruction.'
  }
};


const HCO_ELC_OE_LIST = [
  {code:"AAC1a",chapter:"AAC",text:"The healthcare services being provided are defined."},
  {code:"AAC1b",chapter:"AAC",text:"The defined services are prominently displayed."},
  {code:"AAC1c",chapter:"AAC",text:"Each defined healthcare service should have outpatient, inpatient and emergency covered by qualified medical staff."},
  {code:"AAC2a",chapter:"AAC",text:"Written guidance governs the process that addresses registering and admitting out-patients, day care, in-patients and emergency patients."},
  {code:"AAC2b",chapter:"AAC",text:"A unique identification number is generated at the end of the registration."},
  {code:"AAC2c",chapter:"AAC",text:"There is an appropriate mechanism for transfer (in and out) or referral of patients."},
  {code:"AAC3a",chapter:"AAC",text:"The initial assessment of out-patients, day-care, in-patients and emergency patients is done in a standardised manner."},
  {code:"AAC3b",chapter:"AAC",text:"The initial assessment for in-patients results in a documented care plan."},
  {code:"AAC4a",chapter:"AAC",text:"During all phases of care, there is a qualified individual identified as responsible for the patient's care."},
  {code:"AAC4b",chapter:"AAC",text:"Patients are reassessed at appropriate intervals to determine their response to treatment and to plan further treatment or discharge."},
  {code:"AAC4c",chapter:"AAC",text:"The organisation lays down the guidelines and implements process to identify early warning signs of change or deterioration in clinical conditions."},
  {code:"AAC4d",chapter:"AAC",text:"The organisation implements standardized hand over communication during each staffing shift, between shifts and during transfers between units."},
  {code:"AAC5a",chapter:"AAC",text:"Scope of laboratory services is commensurate to the services provided by the organisation."},
  {code:"AAC5b",chapter:"AAC",text:"Requisition for tests, collection of specimens, identification, handling, safe transportation, processing and disposal is performed as per written guidance."},
  {code:"AAC5c",chapter:"AAC",text:"Laboratory reports are available in standardized manner within a defined time frame and critical results are intimated immediately."},
  {code:"AAC5d",chapter:"AAC",text:"There is an established laboratory safety program with laboratory personnel trained in safe practices."},
  {code:"AAC5e",chapter:"AAC",text:"There is an established laboratory quality assurance program."},
  {code:"AAC5f",chapter:"AAC",text:"Laboratory tests not available in the organisation are outsourced to an organisation based on its quality assurance system."},
  {code:"AAC6a",chapter:"AAC",text:"Imaging services comply with legal and other regulatory requirements."},
  {code:"AAC6b",chapter:"AAC",text:"Scope of imaging services is commensurate to the services provided by the organisation."},
  {code:"AAC6c",chapter:"AAC",text:"Imaging reports are available in standardised manner within a defined time frame and critical results are intimated immediately."},
  {code:"AAC6d",chapter:"AAC",text:"There is an established imaging safety program with imaging personnel trained in safe practices."},
  {code:"AAC6e",chapter:"AAC",text:"There is an established imaging services quality assurance program."},
  {code:"AAC6f",chapter:"AAC",text:"Services not available at the organisation are outsourced to an organisation based on its quality assurance system."},
  {code:"AAC7a",chapter:"AAC",text:"The organisation has a process for discharge of all patients including medico-legal cases."},
  {code:"AAC7b",chapter:"AAC",text:"The discharge summary contains the patient's name, unique identification number, diagnosis and significant findings."},
  {code:"AAC7c",chapter:"AAC",text:"Discharge summary contains follow up advice, medication and other instructions in an understandable manner."},
  {code:"AAC7d",chapter:"AAC",text:"Discharge summary incorporates instructions about when and how to obtain urgent care."},
  {code:"AAC7e",chapter:"AAC",text:"In case of death the summary of the case also includes the cause of death."},
  {code:"COP1a",chapter:"COP",text:"Care shall be provided in consonance with applicable laws and regulations."},
  {code:"COP1b",chapter:"COP",text:"The care and treatment is provided following written guidance."},
  {code:"COP1c",chapter:"COP",text:"Care delivery is uniform for a given clinical condition when similar case is encountered."},
  {code:"COP1d",chapter:"COP",text:"Nursing care and procedures are performed in consonance with the established protocols."},
  {code:"COP1e",chapter:"COP",text:"Transfusion services are provided as per the scope of services of the organisation."},
  {code:"COP1f",chapter:"COP",text:"Transfusion of blood and blood components is managed by written guidance."},
  {code:"COP1g",chapter:"COP",text:"Informed consent should be taken for transfusion of blood and blood products."},
  {code:"COP2a",chapter:"COP",text:"The organisation provides emergency services commensurate with its scope of services."},
  {code:"COP2b",chapter:"COP",text:"The organisation manages medico-legal cases and provides emergency care in a consistent manner."},
  {code:"COP2c",chapter:"COP",text:"Cardio-pulmonary resuscitation services are provided uniformly across the organisation."},
  {code:"COP2d",chapter:"COP",text:"Initiation of appropriate care is guided by a system of triage."},
  {code:"COP2e",chapter:"COP",text:"All patients in emergency are reassessed as appropriate for the change of status."},
  {code:"COP2f",chapter:"COP",text:"Admission or discharge to home/transfer to another organisation is documented for all emergency patients."},
  {code:"COP2g",chapter:"COP",text:"The organisation has a system in place for the management of patients found dead on arrival."},
  {code:"COP2h",chapter:"COP",text:"Appropriately manned and equipped ambulance is available and checked regularly."},
  {code:"COP2i",chapter:"COP",text:"The organisation plans and implements mechanisms for the care of patients during community emergencies, epidemics and other disasters."},
  {code:"COP3a",chapter:"COP",text:"The care of patient in intensive care units and high dependency units is in consonance with the defined scope."},
  {code:"COP3b",chapter:"COP",text:"The organisation shall implement a quality-assurance programme for its intensive care/high dependency units."},
  {code:"COP3c",chapter:"COP",text:"The organisation has a mechanism to counsel the patient and/or family members on the treatment plan."},
  {code:"COP3d",chapter:"COP",text:"End of life care is provided in a compassionate and considerate manner."},
  {code:"COP4a",chapter:"COP",text:"Organisation provides safe obstetric care as per defined scope of services."},
  {code:"COP4b",chapter:"COP",text:"Obstetric care includes ante-natal check ups, maternal nutrition assessment, immunisation and emergency obstetric care."},
  {code:"COP4c",chapter:"COP",text:"The organisation caring for obstetric cases has the facility to take care of neonatal emergencies."},
  {code:"COP5a",chapter:"COP",text:"Paediatric and neonatal services are organized and provided safely by doctors and nurses having age-specific competencies."},
  {code:"COP5b",chapter:"COP",text:"Paediatric assessment includes growth, developmental, nutritional and immunisation status."},
  {code:"COP5c",chapter:"COP",text:"The organisation has measures in place to prevent child/neonate abduction and abuse."},
  {code:"COP6a",chapter:"COP",text:"Procedural sedation is provided in a consistent manner and is administered as per defined written guidance."},
  {code:"COP6b",chapter:"COP",text:"Competent and trained persons perform and monitor sedation after informed consent."},
  {code:"COP7a",chapter:"COP",text:"There is written guidance for administration of anaesthesia."},
  {code:"COP7b",chapter:"COP",text:"The pre-anaesthesia assessment results in the formulation of an anaesthesia plan documented in the patient record."},
  {code:"COP7c",chapter:"COP",text:"Patients are monitored while under anaesthesia."},
  {code:"COP7d",chapter:"COP",text:"Post anaesthesia monitoring is documented and patients are discharged from recovery as per defined criteria."},
  {code:"COP7e",chapter:"COP",text:"Intraoperative adverse anaesthesia events are recorded and analyzed."},
  {code:"COP8a",chapter:"COP",text:"Clinical procedures as well as procedures done in operation theatres are done in a safe and consistent manner."},
  {code:"COP8b",chapter:"COP",text:"Surgical patients have a preoperative assessment and a documented pre-operative diagnosis."},
  {code:"COP8c",chapter:"COP",text:"An informed consent is obtained by a surgeon from the patient before surgery."},
  {code:"COP8d",chapter:"COP",text:"Care is taken to prevent adverse events like wrong site, wrong patient and wrong surgery."},
  {code:"COP8e",chapter:"COP",text:"Procedures/operation notes, post procedure monitoring and post-operative care are documented."},
  {code:"COP9a",chapter:"COP",text:"The organisation identifies and manages vulnerable patients."},
  {code:"COP9b",chapter:"COP",text:"The organisation identifies and manages patients who are at risk of fall, pressure ulcer and malnutrition."},
  {code:"COP10a",chapter:"COP",text:"Patients in pain are effectively managed."},
  {code:"COP10b",chapter:"COP",text:"Scope of rehabilitation services at a minimum is commensurate to the services provided."},
  {code:"COP10c",chapter:"COP",text:"Patients admitted to the organisation are screened for nutritional risk."},
  {code:"COP10d",chapter:"COP",text:"Nutritional assessment shall be done by a dietician for all patients found at risk."},
  {code:"MOM1a",chapter:"MOM",text:"Pharmacy services and safe medication usage are implemented following written guidance."},
  {code:"MOM1b",chapter:"MOM",text:"The organisation shall review and update the hospital formulary as per scope of services."},
  {code:"MOM2a",chapter:"MOM",text:"Medications are stored in a clean, safe and secure environment and storage conditions are monitored."},
  {code:"MOM2b",chapter:"MOM",text:"Written guidance exists for storage of high risk medications including look alike sound alike medications."},
  {code:"MOM2c",chapter:"MOM",text:"Beyond expiry date medications are not stored or used."},
  {code:"MOM2d",chapter:"MOM",text:"List of emergency medicines is defined, stored, and available all the time."},
  {code:"MOM3a",chapter:"MOM",text:"The organisation ensures that only authorized personnel can write prescriptions/medication orders."},
  {code:"MOM3b",chapter:"MOM",text:"The organisation adheres to the determined minimum requirements of a valid prescription/medication order."},
  {code:"MOM3c",chapter:"MOM",text:"Drug allergies and previous adverse drug reactions are ascertained before prescribing medication."},
  {code:"MOM3d",chapter:"MOM",text:"Medication orders are clear, legible, dated and signed and include name of the patient."},
  {code:"MOM3e",chapter:"MOM",text:"Reconciliation of medications occurs at transition points of patient care."},
  {code:"MOM3f",chapter:"MOM",text:"Audit of medication orders/prescription is carried out to check for safe and rational prescribing."},
  {code:"MOM4a",chapter:"MOM",text:"The organisation defines a list of high-risk medications and process to prescribe, dispense and administer them safely."},
  {code:"MOM4b",chapter:"MOM",text:"Dispensed medications are labelled."},
  {code:"MOM5a",chapter:"MOM",text:"Medications are administered by those who are permitted by law to do so."},
  {code:"MOM5b",chapter:"MOM",text:"Prior to administration, medication orders including patient, dosage, route and time are verified."},
  {code:"MOM5c",chapter:"MOM",text:"Prepared medication is labelled before preparation of a second drug."},
  {code:"MOM5d",chapter:"MOM",text:"Measures to avoid catheter and tubing mis-connections during medication administration are implemented."},
  {code:"MOM5e",chapter:"MOM",text:"Medication administration is documented."},
  {code:"MOM5f",chapter:"MOM",text:"Patients are monitored after medication administration."},
  {code:"MOM5g",chapter:"MOM",text:"Near miss, medication errors and adverse drug events are defined, documented and analyzed."},
  {code:"MOM6a",chapter:"MOM",text:"Narcotic drugs and psychotropic substances are stored safely as per statutory requirements."},
  {code:"MOM6b",chapter:"MOM",text:"Narcotic drugs and psychotropic substances are prescribed, dispensed and administered as per statutory requirements."},
  {code:"MOM6c",chapter:"MOM",text:"Chemotherapy and radio-pharmaceuticals are prepared properly and safely and administered with caution."},
  {code:"MOM6d",chapter:"MOM",text:"A proper record shall be kept of the usage, administration and disposal of narcotic and psychotropic substances."},
  {code:"MOM7a",chapter:"MOM",text:"Written guidance addresses procurement and usage of implantable prostheses and medical devices."},
  {code:"MOM7b",chapter:"MOM",text:"Patient and family are counselled for the usage of the implantable prosthesis or medical device."},
  {code:"MOM7c",chapter:"MOM",text:"The batch and serial number of the implantable prosthesis and medical device is recorded in the patient record."},
  {code:"PRE1a",chapter:"PRE",text:"Patient and family rights and responsibilities are displayed and they are made aware of the same."},
  {code:"PRE1b",chapter:"PRE",text:"Patient and family rights include respecting beliefs and values."},
  {code:"PRE1c",chapter:"PRE",text:"Patient and family rights include respect for personal dignity and privacy during examination and treatment."},
  {code:"PRE1d",chapter:"PRE",text:"Patient and family rights include protection from neglect or abuse."},
  {code:"PRE1e",chapter:"PRE",text:"Patient and family rights include treating patient information as confidential."},
  {code:"PRE1f",chapter:"PRE",text:"Patient and family rights include the refusal of treatment and right to seek second opinion."},
  {code:"PRE1g",chapter:"PRE",text:"Patient and family rights include informed consent before transfusion of blood and blood products."},
  {code:"PRE1h",chapter:"PRE",text:"Patient and family rights include a right to complain and information on how to do so."},
  {code:"PRE1i",chapter:"PRE",text:"Patient and family rights include information on the expected cost of the treatment."},
  {code:"PRE1j",chapter:"PRE",text:"Patient and family rights include access to their clinical records."},
  {code:"PRE1k",chapter:"PRE",text:"Patient and family rights include information on the name of the treating doctor and care team."},
  {code:"PRE2a",chapter:"PRE",text:"The patient and/or family members are explained about the proposed care, its risks and alternatives before consent."},
  {code:"PRE2b",chapter:"PRE",text:"The organisation obtains informed consent from the patient and/or family for the defined procedures and treatments."},
  {code:"PRE2c",chapter:"PRE",text:"Informed consent process adheres to statutory norms."},
  {code:"PRE2d",chapter:"PRE",text:"Patients and families are educated on plan of care, preventive aspects, possible complications and home care."},
  {code:"PRE2e",chapter:"PRE",text:"Communication with patients and/or family is done effectively."},
  {code:"PRE2f",chapter:"PRE",text:"The organisation has a mechanism to capture patient feedback and to redress grievances."},
  {code:"IPC1a",chapter:"IPC",text:"The infection prevention and control programme is documented and is periodically updated."},
  {code:"IPC1b",chapter:"IPC",text:"The organisation adheres to hand hygiene, standard precautions and transmission-based precautions."},
  {code:"IPC1c",chapter:"IPC",text:"The organisation adheres to safe injection and infusion practices."},
  {code:"IPC1d",chapter:"IPC",text:"The organisation establishes and implements the antimicrobial usage policy."},
  {code:"IPC1e",chapter:"IPC",text:"Appropriate pre and post exposure prophylaxis is provided to all concerned staff."},
  {code:"IPC1f",chapter:"IPC",text:"The organisation performs surveillance to capture and monitor infection rates and takes corrective action."},
  {code:"IPC2a",chapter:"IPC",text:"Biomedical waste (BMW) is handled appropriately and safely."},
  {code:"IPC2b",chapter:"IPC",text:"The organisation has appropriate engineering controls to prevent infections."},
  {code:"IPC2c",chapter:"IPC",text:"Cleaning and disinfection practices are defined and monitored as appropriate."},
  {code:"IPC2d",chapter:"IPC",text:"Instruments/devices cleaning, disinfection and sterilization practices are monitored."},
  {code:"IPC2e",chapter:"IPC",text:"The organisation adheres to laundry and linen management processes."},
  {code:"IPC2f",chapter:"IPC",text:"The organisation adheres to kitchen sanitation and food handling guidelines."},
  {code:"PSQ1a",chapter:"PSQ",text:"A comprehensive quality improvement and patient safety programme is established and implemented."},
  {code:"PSQ1b",chapter:"PSQ",text:"The organisation adapts and implements Patient Safety Goals."},
  {code:"PSQ1c",chapter:"PSQ",text:"There is an established process in the organisation to monitor and improve quality of nursing care."},
  {code:"PSQ1d",chapter:"PSQ",text:"The organisation has a designated individual to oversee the hospital-wide quality and patient safety programme."},
  {code:"PSQ2a",chapter:"PSQ",text:"The organisation identifies and monitors key indicators to oversee infection prevention and control."},
  {code:"PSQ2b",chapter:"PSQ",text:"The organisation identifies and monitors key indicators to oversee patient safety."},
  {code:"PSQ2c",chapter:"PSQ",text:"The organisation identifies and monitors key indicators to oversee clinical and managerial performance."},
  {code:"PSQ2d",chapter:"PSQ",text:"Clinical audits are performed to improve quality of patient care with the involvement of clinicians."},
  {code:"ROM1a",chapter:"ROM",text:"Those responsible for governance are identified and their roles and responsibilities are defined."},
  {code:"ROM1b",chapter:"ROM",text:"The organisation is registered with appropriate authorities and complies with the applicable laws and regulations."},
  {code:"ROM2a",chapter:"ROM",text:"The management makes public the mission statement of the organisation."},
  {code:"ROM2b",chapter:"ROM",text:"The leaders/management guide the organisation to function in an ethical manner."},
  {code:"ROM2c",chapter:"ROM",text:"The organisation billing process is accurate and ethical."},
  {code:"ROM3a",chapter:"ROM",text:"Designated committees oversee infection prevention and control, quality improvement and other key functions."},
  {code:"ROM3b",chapter:"ROM",text:"Management ensures that it has a documented agreement for all outsourced services."},
  {code:"ROM3c",chapter:"ROM",text:"The organisation has a mechanism to report a violation of patient and family rights."},
  {code:"ROM4a",chapter:"ROM",text:"Those responsible for governance address the organisation sustainability through long term planning."},
  {code:"ROM4b",chapter:"ROM",text:"The organisation takes initiatives towards an energy efficient and environment-friendly facility."},
  {code:"ROM4c",chapter:"ROM",text:"Those responsible for governance address the organisation social responsibility."},
  {code:"ROM4d",chapter:"ROM",text:"Staff well-being is promoted through defined programmes."},
  {code:"FMS1a",chapter:"FMS",text:"The organisation has appropriate infrastructure for patient safety and is maintained in a clean and hygienic condition."},
  {code:"FMS1b",chapter:"FMS",text:"Facility inspection rounds to ensure safety are conducted at least once a month."},
  {code:"FMS1c",chapter:"FMS",text:"Organisation identifies areas which need additional security and access control measures."},
  {code:"FMS1d",chapter:"FMS",text:"Internal and external signage shall be displayed in a language understood by the patients and staff."},
  {code:"FMS1e",chapter:"FMS",text:"Hazardous materials are identified and used safely within the organisation."},
  {code:"FMS2a",chapter:"FMS",text:"The operational and maintenance plan for engineering support services and utility systems are implemented as per written guidance."},
  {code:"FMS2b",chapter:"FMS",text:"Medical equipment is maintained, inspected and calibrated and there are documented records."},
  {code:"FMS3a",chapter:"FMS",text:"Potable water and electricity are available round the clock."},
  {code:"FMS3b",chapter:"FMS",text:"Medical gases and vacuum systems are handled safely and are available round the clock."},
  {code:"FMS4a",chapter:"FMS",text:"The organisation has plans and provisions for identification, early detection and suppression of fire."},
  {code:"FMS4b",chapter:"FMS",text:"There is a maintenance plan for fire related equipment and infrastructure."},
  {code:"FMS4c",chapter:"FMS",text:"The organisation has a documented and displayed safe exit plan in case of fire."},
  {code:"FMS4d",chapter:"FMS",text:"Mock drills are held at least twice in a year."},
  {code:"HRM1a",chapter:"HRM",text:"The mix of staff is commensurate with the volume and scope of services."},
  {code:"HRM1b",chapter:"HRM",text:"The job specification and job description are defined for each category of staff."},
  {code:"HRM1c",chapter:"HRM",text:"The organisation defines and implements a code of conduct for its staff."},
  {code:"HRM2a",chapter:"HRM",text:"Written guidance governs training and development policy for the staff."},
  {code:"HRM2b",chapter:"HRM",text:"Staff are provided with induction training."},
  {code:"HRM2c",chapter:"HRM",text:"Staff are regularly trained on patient care activities based on their specific job requirements."},
  {code:"HRM2d",chapter:"HRM",text:"Staff are regularly trained in safety and quality related aspects."},
  {code:"HRM2e",chapter:"HRM",text:"Staff are trained in handling disaster, fire and non-fire emergencies."},
  {code:"HRM3a",chapter:"HRM",text:"Performance appraisal is done for staff within the organisation at defined intervals."},
  {code:"HRM3b",chapter:"HRM",text:"Process for disciplinary and grievance handling is defined and implemented."},
  {code:"HRM4a",chapter:"HRM",text:"Health problems of the staff, including occupational health hazards, are taken care of by the organisation."},
  {code:"HRM4b",chapter:"HRM",text:"The organisation has measures in place for prevention and handling of workplace violence."},
  {code:"HRM5a",chapter:"HRM",text:"Personal files are maintained in respect of all staff."},
  {code:"HRM5b",chapter:"HRM",text:"Staff records include credentials, training, competency assessment and performance appraisal."},
  {code:"HRM5c",chapter:"HRM",text:"Medical and nursing professionals are granted privileges to admit and care for patients in consonance with their qualification, training, experience and registration."},
  {code:"IMS1a",chapter:"IMS",text:"The organisation identifies, captures and disseminates the information needs of all staff."},
  {code:"IMS1b",chapter:"IMS",text:"Use of telemedicine is as per applicable guidelines."},
  {code:"IMS1c",chapter:"IMS",text:"The organisation shall make efforts to use digital health technology to improve care."},
  {code:"IMS2a",chapter:"IMS",text:"Every medical record has a unique identifier."},
  {code:"IMS2b",chapter:"IMS",text:"The medical record provides a complete, up-to-date and chronological account of the patient's care."},
  {code:"IMS2c",chapter:"IMS",text:"Every medical record entry is signed, named, dated and timed by those authorized to make entries."},
  {code:"IMS2d",chapter:"IMS",text:"Medical records are reviewed periodically."},
  {code:"IMS3a",chapter:"IMS",text:"The organisation maintains confidentiality, integrity and security of information and records."},
  {code:"IMS3b",chapter:"IMS",text:"The organisation discloses privileged health information as authorized by the patient or as required by law."},
  {code:"IMS3c",chapter:"IMS",text:"Written guidance is available for document control."},
  {code:"IMS3d",chapter:"IMS",text:"Written guidance is available for retention and destruction of the patient's clinical records."},
];

const HCO_ELC_PROCESS = [
  {step:1,name:"Register on HOPE Portal",url:"hope.qcin.org",desc:"Go to www.hope.qcin.org → Click Register → Fill Hospital User Registration Form (Hospital name, SPOC details, State, total sanctioned beds)",output:"Login credentials sent to registered email"},
  {step:2,name:"Fill 7-Part Questionnaire",url:"hope.qcin.org",desc:"Complete all 7 parts on the web portal: General Info, Physical Infrastructure, Statutory Compliances, Clinical Services, Hospital Staffing, Quality Improvement Process, Documentation. Save progress at each step.",output:"Completed questionnaire submission (cannot edit after Final Submit)"},
  {step:3,name:"Upload Documents",url:"hope.qcin.org",desc:"Portal documents → upload via web portal (Upload any file icon). Mobile documents → upload via HOPE Android app (View Uploaded File icon). Save on portal first. Cannot use both simultaneously.",output:"Document submission complete"},
  {step:4,name:"Pay Fee",url:"hope.qcin.org",desc:"Pay the applicable certification fee based on your bed strength (18% GST extra). For current fees, visit the official NABH website (nabh.co). Fee is non-refundable and non-transferable. Once paid, application moves to DA team.",output:"Payment receipt + Permanent Application Number"},
  {step:5,name:"Desktop Assessment (DA)",url:"",desc:"NABH DA team reviews all submitted documents online. NCs raised with remarks. HCO submits NC reply + supporting document upload. Two rounds of NC closure cycle available at DA stage.",output:"DA NC closure → Date allotment for onsite assessment"},
  {step:6,name:"Onsite Assessment",url:"",desc:"Physical visit by NABH assessor. Assessment activities: document review, patient care area visit, functional interviews, facility tours. Assessor uploads report within 7 days. HCO gets two NC closure cycles.",output:"Onsite assessment report + NC closure"},
  {step:7,name:"Certification Committee",url:"",desc:"After all NCs closed, case placed before Certification Committee. Committee recommendations are final. If rejected, appeal facility is available after paying appeal fee.",output:"Approval letter / Rejection letter"},
  {step:8,name:"Digital Certificate",url:"",desc:"Printable digital certificate issued with unique certificate number, hospital name, effective date, expiry date. Valid for 2 years. No surveillance assessment under certification programmes. Apply for renewal 6 months before expiry.",output:"NABH HCO ELC Certificate (2-year validity)"},
];

const HCO_FEE = {
  label: "HCO Entry Level Certification (>50 sanctioned beds)",
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
  muted:"#1e3a52", text:"#0d1f33", white:"#0a1828",
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

function UpgradeWall({ daysUsed, onSignOut }) {
  const features=["Full NABH compliance tracking","Unlimited OE scoring","KPI tracking and audit management","Committee calendar and mock drills","PDF gap reports","No setup fee. Cancel anytime."];
  return (
    <div style={{minHeight:"100vh",background:"#050e1a",display:"flex",alignItems:"center",justifyContent:"center",padding:20,fontFamily:"Segoe UI,system-ui,sans-serif"}}>
      <div style={{maxWidth:440,width:"100%",textAlign:"center"}}>
        <div style={{fontSize:48,marginBottom:16}}>🔒</div>
        <div style={{fontSize:11,letterSpacing:3,color:"#c9a84c",marginBottom:8}}>ACCREDREADY</div>
        <div style={{fontSize:26,fontWeight:800,color:"#eef4f9",marginBottom:8}}>Your Free Trial Has Ended</div>
        <div style={{fontSize:14,color:"#3a5870",marginBottom:28}}>Your 14-day free trial expired. Upgrade to continue accessing your NABH compliance data.</div>
        <div style={{background:"#081525",border:"1px solid #c9a84c",borderRadius:14,padding:"24px 22px",marginBottom:20,textAlign:"center"}}>
          <div style={{fontSize:12,letterSpacing:2,color:"#c9a84c",fontWeight:700,marginBottom:8}}>ACCREDREADY</div>
          <div style={{display:"flex",alignItems:"baseline",justifyContent:"center",gap:4,marginBottom:4}}>
            <span style={{fontSize:38,fontWeight:800,color:"#eef4f9"}}>₹499</span>
            <span style={{fontSize:14,color:"#3a5870"}}>/month</span>
          </div>
          <div style={{fontSize:12,color:"#3a5870",marginBottom:20}}>Per hospital · All features included</div>
          <div style={{textAlign:"left",marginBottom:0}}>
            {features.map((f,i)=>(
              <div key={i} style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:9}}>
                <span style={{color:"#c9a84c",flexShrink:0,fontWeight:700}}>✓</span>
                <span style={{fontSize:13,color:"#c8dcea",lineHeight:1.5}}>{f}</span>
              </div>
            ))}
          </div>
        </div>
        <a href="https://wa.me/918511180957?text=Hi%20Dr.%20Mehul%2C%20I%20want%20to%20subscribe%20to%20AccredReady%20for%20Rs.%20499%2Fmonth" target="_blank" rel="noopener noreferrer"
          style={{display:"block",padding:"14px",borderRadius:12,background:"linear-gradient(135deg,#c9a84c,#f0d070)",color:"#050e1a",fontSize:16,fontWeight:800,textDecoration:"none",marginBottom:12,boxShadow:"0 4px 20px rgba(201,168,76,0.4)"}}>
          💬 Get Started — WhatsApp Us
        </a>
        <button onClick={onSignOut} style={{background:"transparent",border:"none",color:"#3a5870",fontSize:12,cursor:"pointer"}}>Sign out</button>
      </div>
    </div>
  );
}

function LoginScreen({ onLogin, initialError }) {
  const [email,setEmail]=useState(""); const [pass,setPass]=useState(""); const [whatsapp,setWhatsapp]=useState("");
  const [rememberMe,setRememberMe]=useState(false);
  const [mode,setMode]=useState("login"); const [error,setError]=useState(initialError||"");
  const [loading,setLoading]=useState(false); const [msg,setMsg]=useState("");
  const [showPricing,setShowPricing]=useState(false);
  const [showContact,setShowContact]=useState(false);
  useEffect(()=>{
    const saved=localStorage.getItem('savedEmail');
    if(saved){setEmail(saved);setRememberMe(true);}
  },[]);
  useEffect(()=>{
    if(initialError)setError(initialError);
  },[initialError]);
  const handle=async()=>{
    setError("");setMsg("");setLoading(true);
    try{
      if(mode==="login"){const{data,error:err}=await supabase.auth.signInWithPassword({email,password:pass});if(err)throw err;if(rememberMe){localStorage.setItem('savedEmail',email);}else{localStorage.removeItem('savedEmail');}onLogin(data.user);}
      else if(mode==="signup"){const{data,error:err}=await supabase.auth.signUp({email,password:pass});if(err)throw err;
        if(whatsapp.trim()&&data.user&&data.session){await supabase.from("profiles").upsert({id:data.user.id,whatsapp_number:whatsapp.trim()},{onConflict:"id"});}
        await fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({access_key:"2aaadfc3-c669-4b2b-92b8-6d6bee4faee1",subject:"New AccredReady Signup",name:"New User",email,message:`New signup:\nEmail: ${email}${whatsapp.trim()?`\nWhatsApp: ${whatsapp.trim()}`:""}`,})});
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
  return (
    <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"Segoe UI,system-ui,sans-serif"}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:16,padding:"40px 36px",width:360}}>
        <div style={{textAlign:"center",marginBottom:28}}>
          <div style={{width:48,height:48,borderRadius:12,background:`linear-gradient(135deg,${T.gold},#f0d070)`,display:"flex",alignItems:"center",justifyContent:"center",fontSize:24,margin:"0 auto 12px"}}>⚕</div>
          <div style={{fontSize:8,letterSpacing:3,color:T.gold,marginBottom:4}}>NABH ACCREDITATION</div>
          <div style={{fontSize:18,fontWeight:700,color:T.white}}>Compliance &amp; Preparation Platform</div>
          <div style={{fontSize:13,color:T.muted,marginTop:4}}>Hospital Accreditation Platform</div>
        </div>
        {error&&<div style={{background:T.redD,border:`1px solid ${T.red}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:13,color:T.red}}>{error}</div>}
        {msg&&<div style={{background:T.greenD,border:`1px solid ${T.green}40`,borderRadius:8,padding:"10px 14px",marginBottom:16,fontSize:13,color:T.green}}>{msg}</div>}
        <div style={{textAlign:'center',padding:'0 0 20px 0',marginBottom:20,borderBottom:'1px solid #0f2640'}}>
          <div style={{fontFamily:'Georgia,serif',fontSize:15,fontStyle:'italic',color:T.text,lineHeight:1.8}}>"Quality is not an act, it is a habit."</div>
          <div style={{fontSize:12,color:T.muted,marginTop:6,letterSpacing:2}}>— ARISTOTLE</div>
        </div>
        <div style={{marginBottom:14}}>
          <div style={{fontSize:12,color:T.muted,marginBottom:6}}>EMAIL</div>
          <input value={email} onChange={e=>setEmail(e.target.value)} placeholder="admin@hospital.com" type="email"
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,boxSizing:"border-box"}}/>
        </div>
        {mode==="signup"&&<div style={{marginBottom:14}}>
          <div style={{fontSize:12,color:T.muted,marginBottom:6}}>WHATSAPP NUMBER (OPTIONAL)</div>
          <input value={whatsapp} onChange={e=>setWhatsapp(e.target.value)} placeholder="+91 98765 43210" type="tel"
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,boxSizing:"border-box"}}/>
        </div>}
        {mode!=="reset"&&<div style={{marginBottom:20}}>
          <div style={{fontSize:12,color:T.muted,marginBottom:6}}>PASSWORD</div>
          <input value={pass} onChange={e=>setPass(e.target.value)} placeholder="••••••••" type="password" onKeyDown={e=>e.key==="Enter"&&handle()}
            style={{width:"100%",padding:"10px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:15,boxSizing:"border-box"}}/>
        </div>}
        {mode==="reset"&&<div style={{marginBottom:20,fontSize:13,color:T.muted,lineHeight:1.6}}>Enter your email above and we'll send you a password reset link.</div>}
        {mode==="login"&&<div style={{display:'flex',alignItems:'center',gap:8,margin:'8px 0 16px'}}>
          <input type="checkbox" id="rememberMe" checked={rememberMe} onChange={e=>setRememberMe(e.target.checked)} style={{width:16,height:16,accentColor:T.gold,cursor:'pointer'}}/>
          <label htmlFor="rememberMe" style={{color:T.muted,fontSize:13,cursor:'pointer'}}>Remember me</label>
        </div>}
        <button onClick={handle} disabled={loading} style={{width:"100%",padding:"12px",borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:15,fontWeight:700,cursor:"pointer",opacity:loading?0.7:1}}>
          {loading?"Please wait…":mode==="login"?"Sign In →":mode==="signup"?"Create Account →":"Send Reset Email →"}
        </button>
        <div style={{fontSize:11,color:T.muted,textAlign:"center",marginTop:8}}>🔒 Secured by Supabase · No spam, ever</div>
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
              <span onClick={()=>setShowContact(true)} style={{fontSize:12,color:'#3a5870',cursor:'pointer',letterSpacing:1,textTransform:'uppercase'}}>Contact Us</span>
              <span onClick={()=>setMode('terms')} style={{fontSize:12,color:'#3a5870',cursor:'pointer',letterSpacing:1,textTransform:'uppercase'}}>Terms & Conditions</span>
              <a href="/privacy.html" target="_blank" rel="noopener noreferrer" style={{fontSize:12,color:'#3a5870',letterSpacing:1,textTransform:'uppercase',textDecoration:'none'}}>Privacy Policy</a>
            </div>
          </>
        )}
        <div style={{textAlign:"center",marginTop:10,fontSize:13,color:T.muted}}>
          {mode==="login"?"Don't have an account? ":mode==="signup"?"Already have an account? ":"Remember your password? "}
          <span onClick={()=>{setMode(mode==="login"?"signup":"login");setError("");setMsg("");}} style={{color:T.gold,cursor:"pointer",fontWeight:600}}>
            {mode==="login"?"Sign up":mode==="reset"?"Sign in":"Sign in"}
          </span>
        </div>
        {/* Hidden inside the installed app (TWA/PWA) — those users already have it */}
        {!window.matchMedia("(display-mode: standalone)").matches&&(
          <div style={{textAlign:"center",marginTop:14}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:6}}>Or get the Android app</div>
            <a href="https://play.google.com/store/apps/details?id=com.mktech.nabhcompliance" target="_blank" rel="noopener noreferrer" style={{display:"inline-block"}}>
              <img src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" alt="Get it on Google Play" style={{height:44,width:"auto",display:"block"}}/>
            </a>
          </div>
        )}
        <div style={{textAlign:"center",marginTop:10,fontSize:11,color:T.muted}}>Independent educational tool — Not affiliated with NABH/QCI</div>
        <div style={{textAlign:"center",marginTop:10,paddingBottom:4}}>
          <span style={{fontSize:12,color:T.muted}}>14-day free trial · No credit card · </span>
          <button onClick={()=>setShowPricing(true)} style={{fontSize:12,color:T.gold,cursor:"pointer",fontWeight:600,background:"none",border:"none",padding:0,fontFamily:"inherit"}}>💎 View Pricing Plans →</button>
        </div>
      </div>
      {showPricing&&(
        <div onClick={()=>setShowPricing(false)} style={{position:"fixed",inset:0,zIndex:2000,background:"rgba(0,0,0,0.75)",display:"flex",alignItems:"center",justifyContent:"center",padding:20}}>
          <div onClick={e=>e.stopPropagation()} style={{background:"#081525",border:"1px solid #c9a84c",borderRadius:16,padding:"28px 24px",maxWidth:400,width:"100%",textAlign:"center",position:"relative"}}>
            <button onClick={()=>setShowPricing(false)} style={{position:"absolute",top:12,right:14,background:"none",border:"none",color:"#3a5870",fontSize:18,cursor:"pointer",lineHeight:1}}>✕</button>
            <div style={{fontSize:11,letterSpacing:3,color:"#c9a84c",marginBottom:8}}>ACCREDREADY</div>
            <div style={{display:"flex",alignItems:"baseline",justifyContent:"center",gap:4,marginBottom:4}}>
              <span style={{fontSize:38,fontWeight:800,color:"#eef4f9"}}>₹499</span>
              <span style={{fontSize:14,color:"#3a5870"}}>/month</span>
            </div>
            <div style={{fontSize:12,color:"#3a5870",marginBottom:20}}>Per hospital · All features included</div>
            <div style={{textAlign:"left",marginBottom:22}}>
              {["Full NABH compliance tracking","Unlimited OE scoring","KPI tracking and audit management","Committee calendar and mock drills","PDF gap reports","No setup fee. Cancel anytime."].map((f,i)=>(
                <div key={i} style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:9}}>
                  <span style={{color:"#c9a84c",flexShrink:0,fontWeight:700}}>✓</span>
                  <span style={{fontSize:13,color:"#c8dcea",lineHeight:1.5}}>{f}</span>
                </div>
              ))}
            </div>
            <a href="https://wa.me/918511180957?text=Hi%20Dr.%20Mehul%2C%20I%20want%20to%20subscribe%20to%20AccredReady%20for%20Rs.%20499%2Fmonth" target="_blank" rel="noopener noreferrer"
              style={{display:"block",padding:"13px",borderRadius:10,background:"linear-gradient(135deg,#c9a84c,#f0d070)",color:"#050e1a",fontSize:15,fontWeight:800,textDecoration:"none",boxShadow:"0 4px 20px rgba(201,168,76,0.4)"}}>
              💬 Get Started — WhatsApp Us
            </a>
            <div style={{fontSize:11,color:"#3a5870",marginTop:12}}>14-day free trial · Sign up to begin</div>
          </div>
        </div>
      )}
      {showContact&&<ContactModal onClose={()=>setShowContact(false)}/>}
    </div>
  );
}
function ContactModal({onClose}){
  const [name,setName]=useState("");const [email,setEmail]=useState("");const [phone,setPhone]=useState("");const [message,setMessage]=useState("");
  const [loading,setLoading]=useState(false);const [success,setSuccess]=useState(false);const [err,setErr]=useState(false);
  const submit=async(e)=>{
    e.preventDefault();setLoading(true);setSuccess(false);setErr(false);
    try{
      const res=await fetch("https://api.web3forms.com/submit",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({access_key:"2aaadfc3-c669-4b2b-92b8-6d6bee4faee1",name,email,phone,message})});
      const json=await res.json();
      if(res.ok&&json.success){setSuccess(true);setName("");setEmail("");setPhone("");setMessage("");}
      else setErr(true);
    }catch{setErr(true);}
    setLoading(false);
  };
  const inp={width:"100%",boxSizing:"border-box",padding:"10px 12px",background:"#0d2035",border:"1px solid #1e3a52",borderRadius:8,color:"#eef4f9",fontSize:15,outline:"none",fontFamily:"inherit"};
  const lbl={display:"block",color:"#7a9db8",fontSize:13,marginBottom:5};
  return(
    <div onClick={onClose} style={{position:"fixed",inset:0,zIndex:3000,background:"rgba(0,0,0,0.75)",display:"flex",alignItems:"center",justifyContent:"center",padding:20}}>
      <div onClick={e=>e.stopPropagation()} style={{background:"#081525",border:"1px solid #1e3a52",borderRadius:16,padding:"28px 24px",maxWidth:420,width:"100%",position:"relative",maxHeight:"90vh",overflowY:"auto"}}>
        <button onClick={onClose} style={{position:"absolute",top:12,right:14,background:"none",border:"none",color:"#7a9db8",fontSize:20,cursor:"pointer",lineHeight:1}}>✕</button>
        <div style={{fontSize:11,letterSpacing:3,color:"#c9a84c",marginBottom:8,textTransform:"uppercase"}}>AccredReady</div>
        <div style={{fontSize:20,fontWeight:700,color:"#eef4f9",marginBottom:18}}>Contact Us</div>
        {success&&<div style={{color:"#0E8A5F",fontSize:15,padding:14,background:"#EBF4F0",borderRadius:8,marginBottom:16}}>Thank you! We'll get back to you soon.</div>}
        {err&&<div style={{color:"#DC2626",fontSize:14,padding:12,background:"#fef2f2",borderRadius:8,marginBottom:16}}>Something went wrong, please try again.</div>}
        <form onSubmit={submit}>
          <div style={{marginBottom:14}}><label style={lbl}>Name *</label><input type="text" required value={name} onChange={e=>setName(e.target.value)} style={inp}/></div>
          <div style={{marginBottom:14}}><label style={lbl}>Email *</label><input type="email" required value={email} onChange={e=>setEmail(e.target.value)} style={inp}/></div>
          <div style={{marginBottom:14}}><label style={lbl}>Mobile *</label><input type="tel" required value={phone} onChange={e=>setPhone(e.target.value)} style={inp}/></div>
          <div style={{marginBottom:18}}><label style={lbl}>Message *</label><textarea required rows={4} value={message} onChange={e=>setMessage(e.target.value)} style={{...inp,resize:"vertical"}}/></div>
          <button type="submit" disabled={loading} style={{width:"100%",padding:12,background:"#0E8A5F",border:"none",borderRadius:10,color:"#fff",fontSize:15,fontWeight:600,cursor:"pointer",opacity:loading?0.7:1,fontFamily:"inherit"}}>{loading?"Sending…":"Send Message"}</button>
        </form>
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
        ['4. Subscription & Payment','Plan: ₹499/month per hospital, all features included. 14-day free trial for new users — no payment required. Payment via UPI or bank transfer. Cancel anytime by emailing upadhyay.mehul9@gmail.com. No refunds for partial months used.'],
        ['5. Acceptable Use','You agree not to share your account, attempt to access other users data, copy or reproduce platform content, or use the platform for any unlawful purpose.'],
        ['6. Intellectual Property','All content, design, and code is owned by AccredReady. No reproduction without written permission.'],
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
      badge: "3rd Edition",
      tags: ["≤50 beds", "408 OEs"],
      desc: "Full NABH accreditation for small hospitals with up to 50 beds. Comprehensive quality programme.",
      available: true,
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
    {
      key: "eco_full",
      title: "Eye Care Organisation (ECO)",
      subtitle: "Full Accreditation",
      badge: "302 OEs",
      tags: ["Eye Care", "Full Accreditation"],
      desc: "Full NABH accreditation for Eye Care Organisations. Comprehensive quality programme covering all eye care OEs.",
      available: true,
      icon: "👁️",
      color: "#06b6d4",
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

        {/* ── Coming Soon divider ── */}
        <div style={{ display: "flex", alignItems: "center", gap: 12, margin: "32px 0 20px" }}>
          <div style={{ flex: 1, height: 1, background: T.border }} />
          <div style={{ fontSize: 9, fontWeight: 700, letterSpacing: 3, color: T.muted, textTransform: "uppercase" }}>Coming Soon</div>
          <div style={{ flex: 1, height: 1, background: T.border }} />
        </div>

        {/* ── Coming Soon cards ── */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 16, opacity: 0.82 }}>
          {[
            {
              key: "ayush_hospital",
              icon: "🌿",
              title: "AYUSH Hospital",
              subtitle: "Ayurveda · Homeopathy · Unani",
              color: T.green,
              tags: ["Ayurveda", "Homeopathy", "Unani"],
              desc: "NABH accreditation for AYUSH hospitals including Ayurveda, Homeopathy, and Unani systems.",
            },
            {
              key: "dental_clinic",
              icon: "🦷",
              title: "Dental Clinic",
              subtitle: "Dental Accreditation",
              color: T.orange,
              tags: ["Dental", "Oral Health"],
              desc: "NABH accreditation standards for dental clinics and oral health care centres.",
            },
          ].map(cs => (
            <div key={cs.key} style={{ background: T.panel, border: `1.5px solid ${T.border}`, borderRadius: 14, padding: "24px", cursor: "default", position: "relative" }}>
              <div style={{ position: "absolute", top: 14, right: 14, fontSize: 8, fontWeight: 700, letterSpacing: 1, padding: "3px 9px", borderRadius: 20, background: `${T.muted}18`, color: T.muted, border: `1px solid ${T.muted}40` }}>Coming Soon</div>
              <div style={{ width: 44, height: 44, borderRadius: 12, background: T.panel2, border: `1px solid ${T.border}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 22, marginBottom: 12 }}>{cs.icon}</div>
              <div style={{ fontSize: 15, fontWeight: 800, color: T.white, marginBottom: 3 }}>{cs.title}</div>
              <div style={{ fontSize: 10, color: cs.color, fontWeight: 600, marginBottom: 10 }}>{cs.subtitle}</div>
              <div style={{ display: "flex", gap: 6, marginBottom: 14, flexWrap: "wrap" }}>
                {cs.tags.map(tag => (
                  <span key={tag} style={{ fontSize: 9, padding: "2px 8px", borderRadius: 8, background: T.panel2, border: `1px solid ${T.border}`, color: T.muted }}>{tag}</span>
                ))}
              </div>
              <div style={{ fontSize: 11, color: T.text, lineHeight: 1.7, marginBottom: 16 }}>{cs.desc}</div>
              <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: 11, color: T.muted }}><span>🔔</span> Notify me when available</div>
            </div>
          ))}
        </div>

        <div style={{ textAlign: "center", marginTop: 18, fontSize: 10, color: T.muted }}>
          All upcoming programmes will be included in your existing subscription at no extra cost.
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
    const{data:existingProf}=await supabase.from("profiles").select("id,hospital_id").eq("id",user.id).maybeSingle();
    if(!existingProf){await supabase.from("profiles").insert({id:user.id});}
    if(existingProf&&!existingProf.hospital_id){
      const{data:orphan}=await supabase.from("hospitals").select("id").eq("created_by",user.id).limit(1).maybeSingle();
      if(orphan){await supabase.from("profiles").update({hospital_id:orphan.id,role:"admin"}).eq("id",user.id);}
    }
    const{data:hosp}=await supabase.from("hospitals").select("*").limit(1).single();
    if(hosp){
      setHospital(hosp);
      const{data:ass}=await supabase.from("assessments").select("*").eq("hospital_id",hosp.id).order("created_at",{ascending:false});
      const assData=ass||[];
      setAssessments(assData);
      if(assData.length===1){
        onReady({hospitalId:hosp.id,assessmentId:assData[0].id,hospitalName:hosp.name,assessmentName:assData[0].name,userEmail:user.email,userId:user.id,plan:hosp.plan,access_until:hosp.access_until});
        return;
      }
      if(assData.length>0)setSelAss(assData[0].id);
    }
    setLoading(false);
  };

  const createHospital=async()=>{
    if(!newHosp.trim())return;
    setLoading(true);setError("");
    const{data:prof}=await supabase.from("profiles").select("whatsapp_number").eq("id",user.id).maybeSingle();
    const hospInsert={name:newHosp.trim(),nabh_status:"preparing",created_by:user.id};
    if(prof?.whatsapp_number)hospInsert.whatsapp=prof.whatsapp_number;
    const{data,error:err}=await supabase.from("hospitals").insert(hospInsert).select().single();
    if(err){setError(err.message);setLoading(false);return;}
    const{error:linkErr}=await supabase.from("profiles").update({hospital_id:data.id,role:"admin",name:user.email}).eq("id",user.id);
    if(linkErr){
      console.error("Hospital link failed:",linkErr);
      setError("Your hospital was created but could not be linked to your account. Please sign out and sign back in — it will be linked automatically on next login.");
      setLoading(false);
      return;
    }
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
    onReady({hospitalId:hospital.id,assessmentId:ass.id,hospitalName:hospital.name,assessmentName:assName,userEmail:user.email,userId:user.id,plan:hospital.plan,access_until:hospital.access_until});
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
    onReady({hospitalId:hospital.id,assessmentId:selAss,hospitalName:hospital.name,assessmentName:ass?.name,userEmail:user.email,userId:user.id,plan:hospital.plan,access_until:hospital.access_until});
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
  const safeHref=(s)=>(typeof s==="string"&&/^https?:\/\//i.test(s))?s:"#";

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
                                  <a href={safeHref(l.url)} target="_blank" rel="noopener noreferrer" style={{color:T.text,textDecoration:"none",maxWidth:200,overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"}}>📄 {l.label||domainOf(l.url)}</a>
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

function GapFixScreen({ assessmentId, gaps, onRefresh, onDownloadReport, pdfLoading }) {
  const [sevFilter,setSevFilter]=useState("ALL");
  const [search,setSearch]=useState('');
  const [saving,setSaving]=useState({});
  const [deleting,setDeleting]=useState({});
  const [capaDb,setCapaDb]=useState({});
  const [capaForm,setCapaForm]=useState({});

  const loadCapas=()=>{
    if(!assessmentId) return;
    supabase.from("capa").select("*").eq("assessment_id",assessmentId).then(({data})=>{
      if(!data) return;
      const m={};
      data.forEach(r=>{m[r.oe_id]=r;});
      setCapaDb(m);
    });
  };
  useEffect(()=>{loadCapas();},[assessmentId]); // eslint-disable-line

  const filteredGaps=(gaps||[]).filter(g=>{
    const matchesSev=sevFilter==='ALL'||g.severity===sevFilter;
    const matchesSearch=!search||
      g.oe_id?.toLowerCase().includes(search.toLowerCase())||
      g.text?.toLowerCase().includes(search.toLowerCase());
    return matchesSev&&matchesSearch;
  });

  const submitCapa=async(oeId)=>{
    const fc=capaForm[oeId];
    if(!fc?.finding||!fc?.action) return;
    setSaving(p=>({...p,[oeId]:true}));
    const {error}=await supabase.from("capa").upsert(
      {assessment_id:assessmentId,oe_id:oeId,finding:fc.finding,root_cause:fc.root_cause||"",action_planned:fc.action,action_type:fc.action_type||"Process",responsible_person:fc.person||"",target_date:fc.date||null,status:"open"},
      {onConflict:"assessment_id,oe_id"}
    );
    setSaving(p=>({...p,[oeId]:false}));
    if(error){alert("CAPA save failed: "+error.message);return;}
    const {data:fresh}=await supabase.from("capa").select("*").eq("assessment_id",assessmentId);
    if(fresh){const m={};fresh.forEach(r=>{m[r.oe_id]=r;});setCapaDb(m);}
    setCapaForm(p=>({...p,[oeId]:{...p[oeId],expanded:false}}));
    onRefresh();
  };

  const deleteCapa=async(oeId)=>{
    if(!window.confirm('Delete this CAPA entry?')) return;
    setDeleting(p=>({...p,[oeId]:true}));
    await supabase.from("capa").delete().match({assessment_id:assessmentId,oe_id:oeId});
    setCapaDb(p=>{const n={...p};delete n[oeId];return n;});
    setCapaForm(p=>{const n={...p};delete n[oeId];return n;});
    setDeleting(p=>({...p,[oeId]:false}));
    onRefresh();
  };

  return (
    <div>
      <input
        value={search}
        onChange={e=>setSearch(e.target.value)}
        placeholder="Search gaps by OE ID or text (e.g. 'AAC.1.a', 'hand hygiene')..."
        style={{width:'100%',padding:'10px 14px',borderRadius:8,border:'1px solid #0f2640',background:'#081525',color:'#eef4f9',fontSize:14,marginBottom:10,boxSizing:'border-box'}}
      />
      <div style={{display:"flex",gap:8,marginBottom:14,alignItems:"center"}}>
        {["ALL","CRITICAL","HIGH","MEDIUM","LOW"].map(s=><button key={s} onClick={()=>setSevFilter(s)} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:sevFilter===s?`${sevColor(s)}20`:"transparent",border:`1px solid ${sevFilter===s?sevColor(s):T.border}`,color:sevFilter===s?sevColor(s):T.muted}}>{s}</button>)}
        <div style={{fontSize:13,color:T.muted,alignSelf:"center"}}>{filteredGaps.length} gaps</div>
        {onDownloadReport&&<button onClick={onDownloadReport} disabled={pdfLoading}
          style={{marginLeft:'auto',padding:'6px 14px',borderRadius:7,border:`1px solid ${T.gold}`,
            background:'transparent',color:T.gold,fontSize:12,fontWeight:700,cursor:pdfLoading?'default':'pointer',
            opacity:pdfLoading?0.6:1,whiteSpace:'nowrap'}}>
          {pdfLoading?'⏳ Generating…':'⬇ Download Gap Report'}
        </button>}
      </div>
      {filteredGaps.length===0&&<div style={{textAlign:"center",color:T.muted,padding:"40px",fontSize:14}}>{(gaps||[]).length===0?"No gaps found. Score OEs first.":"No gaps at this severity level."}</div>}
      <div style={{display:"grid",gap:10}}>
        {filteredGaps.map(g=>{
          const fc=capaForm[g.oe_id]||{};
          const dbC=capaDb[g.oe_id];
          const hasSaved=!!dbC;
          const expanded=fc.expanded;
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
                      {hasSaved&&<span style={{fontSize:11,padding:"2px 6px",borderRadius:5,background:T.green+"22",color:T.green}}>✓ CAPA saved</span>}
                    </div>
                    <div style={{fontSize:12,color:T.text,lineHeight:1.5,marginBottom:6}}>{g.oe_text}</div>
                    <div style={{fontSize:12,color:T.muted,fontStyle:"italic"}}>{g.message}</div>
                  </div>
                  <div style={{textAlign:"center",flexShrink:0}}>
                    <div style={{fontSize:22,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
                    <div style={{fontSize:7,color:T.muted}}>/ 5</div>
                  </div>
                </div>

                <div style={{display:"flex",gap:8,flexWrap:"wrap",marginTop:4}}>
                  {!expanded&&hasSaved ? (
                    <>
                      <button onClick={()=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,expanded:true,finding:fc.finding!==undefined?fc.finding:(dbC?.finding||''),action:fc.action!==undefined?fc.action:(dbC?.action_planned||''),person:fc.person!==undefined?fc.person:(dbC?.responsible_person||''),date:fc.date!==undefined?fc.date:(dbC?.target_date||'')}}))} style={{fontSize:12,color:T.gold,background:"transparent",border:`1px solid ${T.gold}44`,borderRadius:8,padding:"4px 14px",cursor:"pointer"}}>✏️ Edit CAPA</button>
                      <button onClick={()=>deleteCapa(g.oe_id)} disabled={deleting[g.oe_id]||saving[g.oe_id]} style={{fontSize:12,color:T.red,background:"transparent",border:`1px solid ${T.red}44`,borderRadius:8,padding:"4px 14px",cursor:"pointer"}}>{deleting[g.oe_id]?"Deleting…":"🗑 Delete CAPA"}</button>
                    </>
                  ) : expanded ? (
                    <button onClick={()=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,expanded:false}}))} style={{fontSize:12,color:T.muted,background:"transparent",border:`1px solid ${T.border}`,borderRadius:8,padding:"4px 14px",cursor:"pointer"}}>▲ Hide CAPA</button>
                  ) : (
                    <button onClick={()=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,expanded:true}}))} style={{fontSize:12,color:T.gold,background:"transparent",border:`1px solid ${T.gold}44`,borderRadius:8,padding:"4px 14px",cursor:"pointer"}}>▼ Add CAPA</button>
                  )}
                </div>

                {/* ── EXPANDED: full form ── */}
                {expanded&&(
                  <div style={{marginTop:12,display:"grid",gap:8}}>
                    <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>FINDING *</div><textarea value={fc.finding||""} onChange={e=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,finding:e.target.value}}))} rows={2} placeholder="Describe the non-compliance finding…" style={{width:"100%",padding:"8px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:"vertical",boxSizing:"border-box"}}/></div>
                    <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>ACTION PLANNED *</div><textarea value={fc.action||""} onChange={e=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,action:e.target.value}}))} rows={2} placeholder="Corrective action to be taken…" style={{width:"100%",padding:"8px 10px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:"vertical",boxSizing:"border-box"}}/></div>
                    <div style={{display:"flex",gap:8,flexWrap:"wrap"}}>
                      <div style={{flex:1,minWidth:140}}><div style={{fontSize:11,color:T.muted,marginBottom:4}}>RESPONSIBLE PERSON</div><input value={fc.person||""} onChange={e=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,person:e.target.value}}))} placeholder="Name / Designation" style={{width:"100%",padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:"border-box"}}/></div>
                      <div><div style={{fontSize:11,color:T.muted,marginBottom:4}}>TARGET DATE</div><input type="date" value={fc.date||""} onChange={e=>setCapaForm(p=>({...p,[g.oe_id]:{...fc,date:e.target.value}}))} style={{padding:"7px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/></div>
                      <button onClick={()=>submitCapa(g.oe_id)} disabled={saving[g.oe_id]||deleting[g.oe_id]||!fc.finding||!fc.action} style={{marginTop:14,padding:"7px 20px",borderRadius:10,background:`linear-gradient(135deg,${T.green},#3d9e6e)`,border:"none",color:T.bg,fontSize:14,fontWeight:700,cursor:fc.finding&&fc.action?"pointer":"default",opacity:fc.finding&&fc.action?1:0.5}}>{saving[g.oe_id]?"Saving…":"Save CAPA →"}</button>
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
function CommitteesScreen({ hospitalId, committeesView, navigate }) {
  const [committees,setCommittees]=useState([]);
  const [meetings,setMeetings]=useState([]);
  const [loading,setLoading]=useState(true);
  const [search,setSearch]=useState("");
  const [filter,setFilter]=useState("ALL");
  const [expanded,setExpanded]=useState(null);
  const [guideOpen,setGuideOpen]=useState(null);
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
          <button onClick={()=>navigate({ committeesView: 'reference' })} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:committeesView==="reference"?T.goldD:"transparent",border:`1px solid ${committeesView==="reference"?T.gold:T.border}`,color:committeesView==="reference"?T.goldL:T.muted}}>📋 Reference</button>
          <button onClick={()=>navigate({ committeesView: 'mom' })} style={{padding:"5px 14px",borderRadius:8,fontSize:12,cursor:"pointer",background:committeesView==="mom"?T.goldD:"transparent",border:`1px solid ${committeesView==="mom"?T.gold:T.border}`,color:committeesView==="mom"?T.goldL:T.muted}}>📝 Meeting Records {meetings.length>0&&<span style={{marginLeft:4,background:T.gold,color:T.bg,borderRadius:4,padding:"0 5px",fontSize:8}}>{meetings.length}</span>}</button>
        </div>
      </div>

      {momSuccess&&<div style={{background:T.greenD,border:`1px solid ${T.green}30`,borderRadius:8,padding:"10px 14px",marginBottom:12,fontSize:13,color:T.green}}>✅ Meeting minutes saved successfully.</div>}

      {/* REFERENCE VIEW */}
      {committeesView==="reference"&&(
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
              const docs=Array.isArray(c.required_docs)?c.required_docs:(c.required_docs?((s)=>{try{return JSON.parse(s);}catch(e){return[];}})(c.required_docs):[]);
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
                      <button onClick={e=>{e.stopPropagation();setShowMOMForm(c.id);setMOMForm(emptyMOM());}} style={{padding:"4px 10px",borderRadius:6,fontSize:11,cursor:"pointer",background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,flexShrink:0}}>+ Add MOM</button>
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
                        const fg=typeof c.formation_guide==="string"?(()=>{try{return JSON.parse(c.formation_guide);}catch(e){return{};}})():c.formation_guide;
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
                                  {m.evidence_url&&<a href={/^https?:\/\//i.test(m.evidence_url)?m.evidence_url:"#"} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Minutes</a>}
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
      {committeesView==="mom"&&(
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
                        {m.evidence_url&&<a href={/^https?:\/\//i.test(m.evidence_url)?m.evidence_url:"#"} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Minutes</a>}
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

// Verified against official NABH 6th Edition (nabh_hco_kpi_correct.json). KPIs 1-32 only.
// KPIs 33-50 are not overridden — Supabase DB values pass through unchanged.
const HCO_KPI_OVERRIDE={
  1:{name:"Time for initial assessment of indoor patients",standard_ref:"PSQ.3a",numerator:"Sum of time taken for assessment (minutes)",denominator:"Total number of admissions",formula:"N/D",unit:"Minutes",target:"<60 min general wards, <30 min emergency"},
  2:{name:"Number of reporting errors per 1000 investigations",standard_ref:"PSQ.3a",numerator:"Number of reporting errors",denominator:"Number of tests performed",formula:"N/D x 1000",unit:"/1000 tests",target:"<1 per 1000 tests"},
  3:{name:"Percentage of adherence to safety precautions by staff in diagnostics",standard_ref:"PSQ.3a",numerator:"Number of staff adhering to safety precautions",denominator:"Number of staff audited",formula:"N/D x 100",unit:"Percentage",target:">95%"},
  4:{name:"Incidence of medication errors",standard_ref:"PSQ.3a",numerator:"Total number of medication errors",denominator:"Total number of opportunities",formula:"N/D x 100",unit:"Percentage",target:"<1%"},
  5:{name:"Percentage of in-patients developing adverse drug reactions",standard_ref:"PSQ.3a",numerator:"Number of adverse drug reactions",denominator:"Number of inpatients",formula:"N/D x 100",unit:"Percentage",target:"Monitor and improve"},
  6:{name:"Percentage of unplanned return to OT",standard_ref:"PSQ.3a",numerator:"Number of unplanned returns to OT",denominator:"Number of patients who underwent surgeries in OT",formula:"N/D x 100",unit:"Percentage",target:"<2%"},
  7:{name:"Percentage of surgeries where WHO safe surgery checklist was followed",standard_ref:"PSQ.3a",numerator:"Number of surgeries where WHO safe surgery checklist was followed",denominator:"Number of surgeries audited",formula:"N/D x 100",unit:"Percentage",target:">99%"},
  8:{name:"Percentage of transfusion reactions",standard_ref:"PSQ.3a",numerator:"Number of transfusion reactions",denominator:"Number of units transfused",formula:"N/D x 100",unit:"Percentage",target:"<1%"},
  9:{name:"Standardised Mortality Ratio for ICU",standard_ref:"PSQ.3a",numerator:"Actual deaths in ICU",denominator:"Predicted deaths in ICU",formula:"N/D",unit:"Ratio",target:"<1"},
  10:{name:"Return to ICU within 48 hours",standard_ref:"PSQ.3a",numerator:"Number of returns to ICU within 48 hours",denominator:"Number of discharges/transfers from ICU",formula:"N/D x 100",unit:"Percentage",target:"<5%"},
  11:{name:"Return to emergency within 72 hours with similar complaints",standard_ref:"PSQ.3a",numerator:"Number of returns to emergency within 72 hours with similar presenting complaints",denominator:"Number of patients who came to emergency",formula:"N/D x 100",unit:"Percentage",target:"<5%"},
  12:{name:"Incidence of hospital associated pressure ulcers after admission",standard_ref:"PSQ.3a",numerator:"Number of patients who develop new/worsening pressure ulcers after admission",denominator:"Total number of inpatient days",formula:"N/D x 1000",unit:"/1000 patient days",target:"<1 per 1000 patient days"},
  13:{name:"Catheter associated urinary tract infection rate",standard_ref:"PSQ.3b",numerator:"Number of urinary catheter associated UTIs in a month",denominator:"Number of urinary catheter days in that month",formula:"N/D x 1000",unit:"/1000 urinary catheter days",target:"<1 per 1000 catheter days"},
  14:{name:"Ventilator associated pneumonia rate",standard_ref:"PSQ.3b",numerator:"Number of VAP cases in a month",denominator:"Number of ventilator days in that month",formula:"N/D x 1000",unit:"/1000 ventilator days",target:"<2 per 1000 ventilator days"},
  15:{name:"Central line associated bloodstream infection rate",standard_ref:"PSQ.3b",numerator:"Number of central line associated bloodstream infections in a month",denominator:"Number of central line days in that month",formula:"N/D x 1000",unit:"/1000 central line days",target:"<1 per 1000 central line days"},
  16:{name:"Surgical site infection rate",standard_ref:"PSQ.3a",numerator:"Number of surgical site infections in a given month",denominator:"Number of surgeries performed in that month",formula:"N/D x 100",unit:"/100 procedures",target:"<2 per 100 procedures"},
  17:{name:"Compliance to hand hygiene practices",standard_ref:"PSQ.3b",numerator:"Total number of actions performed (hand hygiene compliant)",denominator:"Total number of hand hygiene opportunities",formula:"N/D x 100",unit:"Percentage",target:">80%"},
  18:{name:"Percentage of cases who receive appropriate prophylactic antibiotics",standard_ref:"PSQ.3b",numerator:"Number of patients who received appropriate prophylactic antibiotic",denominator:"Number of patients who underwent surgeries",formula:"N/D x 100",unit:"Percentage",target:">95%"},
  19:{name:"Percentage of rescheduling of surgeries",standard_ref:"PSQ.3c",numerator:"Number of cases rescheduled",denominator:"Number of surgeries planned",formula:"N/D x 100",unit:"Percentage",target:"<5%"},
  20:{name:"Turnaround time for issue of blood and blood components",standard_ref:"PSQ.3c",numerator:"Sum of time taken (in minutes)",denominator:"Total number of blood and blood components crossmatched/reserved",formula:"N/D",unit:"Minutes",target:"<30 minutes"},
  21:{name:"Nurse patient ratio for ICUs and wards",standard_ref:"PSQ.3c",numerator:"Number of nursing staff",denominator:"Number of occupied beds",formula:"N/D",unit:"Ratio",target:"ICU 1:1-2, Wards 1:6"},
  22:{name:"Waiting time for outpatient consultation",standard_ref:"PSQ.3c",numerator:"Sum total time for consultation (minutes)",denominator:"Total number of outpatients",formula:"N/D",unit:"Minutes",target:"<30 minutes"},
  23:{name:"Waiting time for diagnostics",standard_ref:"PSQ.3c",numerator:"Sum total time waiting for diagnostics (minutes)",denominator:"Number of outpatients reported in diagnostics",formula:"N/D",unit:"Minutes",target:"<30 minutes"},
  24:{name:"Time taken for discharge",standard_ref:"PSQ.3c",numerator:"Sum of time taken for discharge (minutes)",denominator:"Number of patients discharged",formula:"N/D",unit:"Minutes",target:"<60 minutes"},
  25:{name:"Percentage of medical records having incomplete and/or improper consent",standard_ref:"PSQ.3c",numerator:"Number of medical records having incomplete and/or improper consent",denominator:"Number of discharges and deaths",formula:"N/D x 100",unit:"Percentage",target:"<1%"},
  26:{name:"Number of stock-outs of emergency medications",standard_ref:"PSQ.3c",numerator:"Number of stock-outs of emergency drugs",denominator:"N/A - count only",formula:"Count",unit:"Number",target:"0"},
  27:{name:"Number of variations observed in mock drills",standard_ref:"PSQ.3d",numerator:"Total number of variations in a mock drill",denominator:"N/A - count only",formula:"Count",unit:"Number",target:"0"},
  28:{name:"Incidence of patient falls",standard_ref:"PSQ.3d",numerator:"Number of patient falls",denominator:"Total number of inpatient days",formula:"N/D x 1000",unit:"/1000 patient days",target:"<1 per 1000 patient days"},
  29:{name:"Percentage of near misses",standard_ref:"PSQ.3d",numerator:"Number of near misses reported",denominator:"Number of incidents reported",formula:"N/D x 100",unit:"Percentage",target:">30%"},
  30:{name:"Rate of needlestick injuries",standard_ref:"PSQ.3d",numerator:"Number of needlestick injuries",denominator:"Average occupied beds",formula:"N/D x 1000",unit:"Rate /1000 occupied beds (cumulative yearly)",target:"<5 per 1000 occupied beds per year"},
  31:{name:"Appropriate handovers during shift change",standard_ref:"PSQ.3d",numerator:"Total number of handovers done appropriately",denominator:"Total number of handover opportunities",formula:"N/D x 100",unit:"Percentage",target:">95%"},
  32:{name:"Percentage of safe and rational prescriptions",standard_ref:"PSQ.3d",numerator:"Total number of safe and rational prescriptions",denominator:"Total number of prescriptions audited",formula:"N/D x 100",unit:"Percentage",target:">90%"}
};

// Multipliers keyed by kpi_no — KPIs 1-32 from official NABH 6th Edition.
// 0 = count-only (KPI 26, 27). KPIs 33-50 fall through to text-based detection.
const KPI_MULTIPLIERS={
  1:1,   2:1000,3:100, 4:100, 5:100,
  6:100, 7:100, 8:100, 9:1,   10:100,
  11:100,12:1000,13:1000,14:1000,15:1000,
  16:100,17:100,18:100,19:100,20:1,
  21:1,  22:1,  23:1,  24:1,  25:100,
  26:0,  27:0,  28:1000,29:100,30:1000,
  31:100,32:100
};

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
    supabase.from("kpis").select("*, source, source_doc").order("kpi_no").then(({data})=>
      setKpis((data||[]).map(k=>({...k,...(HCO_KPI_OVERRIDE[k.kpi_no]||{})})))
    );
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
    const u=(kpi.unit||"").toLowerCase().replace(/,/g,"");
    const fml=(kpi.formula||"").toLowerCase().replace(/,/g,"");
    const nm=(kpi.name||"").toLowerCase();
    const multiplier=KPI_MULTIPLIERS[kpi.kpi_no]!==undefined?KPI_MULTIPLIERS[kpi.kpi_no]:
      (u.includes("1000")||fml.includes("1000")||nm.includes("1000"))?1000:
      (u.includes("%")||/\/100\b/.test(u)||fml.includes("%")||/[×x]\s*100\b/.test(fml))?100:
      1;
    const isCount=multiplier===0;
    if(!f||f.calc_num===""){alert(isCount?"Enter count.":"Enter numerator and denominator.");return;}
    if(!isCount&&f.calc_den===""){alert("Enter numerator and denominator.");return;}
    const num=parseFloat(f.calc_num);
    if(isNaN(num)){alert("Enter valid number.");return;}
    let result,den=null;
    if(isCount){
      result=num;
    } else {
      den=parseFloat(f.calc_den);
      if(isNaN(den)||den===0){alert("Enter valid non-zero denominator.");return;}
      result=(num/den)*multiplier;
    }
    setCalcResult(r=>({...r,[kpi.id]:result}));
    setSaving(kpi.id);
    const{error}=await supabase.from("kpi_data").upsert({
      hospital_id:hospitalId,kpi_id:kpi.id,
      numerator:num,denominator:den,
      value:parseFloat(result.toFixed(isCount?0:4)),
      benchmark:isCount?null:(kpi.benchmark_value||null),
      month:f.month||curMonth,year:f.year||curYear,
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

                  {/* DATA ENTRY */}
                  <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                    <div style={{fontSize:12,fontWeight:700,color:T.gold,marginBottom:10,letterSpacing:1}}>📥 ENTER DATA</div>
                    <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:8,marginBottom:8}}>
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
                    </div>
                    {KPI_MULTIPLIERS[k.kpi_no]===0?(
                      <div style={{marginBottom:8}}>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>COUNT — {k.numerator}</div>
                        <input type="number" step="1" value={f.calc_num||""} onChange={e=>setDataForm(df=>({...df,[k.id]:{...f,calc_num:e.target.value}}))} placeholder="Enter count" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
                      </div>
                    ):(
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
                    )}
                    <button onClick={()=>calcAndSave(k)} disabled={saving===k.id}
                      style={{padding:"7px 18px",borderRadius:7,background:saveSuccess===k.id?T.green:T.goldD,border:`1px solid ${saveSuccess===k.id?T.green:T.gold}`,color:saveSuccess===k.id?T.bg:T.gold,fontSize:13,fontWeight:700,cursor:"pointer"}}>
                      {saving===k.id?"Saving…":saveSuccess===k.id?"✅ Saved!":KPI_MULTIPLIERS[k.kpi_no]===0?"📋 Save Count":"🧮 Calculate & Save"}
                    </button>
                    {calcResult[k.id]!==undefined&&(()=>{const effectiveTarget=customTargets[k.id]||k.target;const isCount=KPI_MULTIPLIERS[k.kpi_no]===0;return(
                      <div style={{marginTop:8}}>
                        <div style={{fontSize:15,fontWeight:700,color:isCount?T.gold:getResultColor(calcResult[k.id],effectiveTarget)}}>
                          {isCount?`Count: ${calcResult[k.id].toFixed(0)} ${k.unit}`:`Result: ${calcResult[k.id].toFixed(2)} ${k.unit}`}
                        </div>
                        {!isCount&&<div style={{fontSize:12,color:getResultColor(calcResult[k.id],effectiveTarget),marginTop:2}}>
                          {getResultLabel(calcResult[k.id],effectiveTarget)}
                        </div>}
                      </div>
                    );})()}
                  </div>

                  {/* History */}
                  {history.length>0&&(
                    <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                      <KpiTrendChart history={history} target={k.benchmark_value||k.target} unit={k.unit}/>
                      <div style={{fontSize:11,color:T.muted,marginBottom:8,letterSpacing:1,marginTop:12}}>TRACKING HISTORY ({history.length} entries)</div>
                      <div style={{display:"grid",gap:4}}>
                        {history.map(d=>(
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

// ── ECO FULL — achieve tips box (module-level, no closure risk) ──────────────
function EcoTipBox(oe) {
  // Guard: achieve_tips must be an actual array of strings, otherwise fall back
  const rawTips = oe.achieve_tips;
  const tips = Array.isArray(rawTips) && rawTips.length > 0 ? rawTips : null;
  const lvlTips = oe.category === 'core'
    ? ['This is a Core OE — assessors will examine records, observe practice directly, and interview staff on every visit.',
       'Ensure 100% of patient files show evidence of compliance, with no exceptions — even one missing record is a finding.',
       'Conduct a monthly internal audit specifically for this OE and display the trend chart in the department.',
       'Prepare staff with a 2-minute verbal response explaining the process — assessors routinely ask directly.']
    : oe.category === 'achievement'
    ? ['Collect before/after data to demonstrate measurable improvement — a chart or table showing trend over 3 months is ideal.',
       'Ensure the quality committee has reviewed and minuted this indicator at least once in the last quarter.',
       'Show actual outcome numbers, not just that a system is in place.',
       'Achievement OEs are assessed at Surveillance — begin collecting data from Day 1 of accreditation.']
    : oe.category === 'excellence'
    ? ['Excellence OEs are assessed at Re-accreditation — document innovation and leadership beyond basic compliance.',
       'Benchmark against national or international standards and record the comparison formally.',
       'Seek external validation and document it.',
       'Excellence means demonstrated sustained improvement over multiple assessment cycles with supporting data.']
    : ['Create a dated, signed SOP for this process and place it in the relevant department folder — version-controlled.',
       'Train all concerned staff and maintain a signed attendance register as evidence of training.',
       'Maintain a monthly audit record showing consistent compliance.',
       'Ensure any relevant forms/registers are filled completely — incomplete records are scored as non-compliance.'];
  const displayTips = tips || lvlTips;
  const tipLabel = tips ? 'HOW TO ACHIEVE THIS OE' : `GENERAL GUIDANCE — ${(oe.category || '').toUpperCase()}`;
  return (
    <div style={{marginTop:6,marginBottom:8,background:T.blue+'14',border:`1px solid ${T.blue}22`,borderRadius:8,padding:'12px 14px'}}>
      <div style={{fontSize:10,letterSpacing:2,color:T.blue,marginBottom:8,fontWeight:700}}>{tipLabel}</div>
      {displayTips.map((tip, i) => (
        <div key={i} style={{display:'flex',gap:8,marginBottom:6,alignItems:'flex-start'}}>
          <div style={{width:18,height:18,borderRadius:'50%',background:T.blue+'22',border:`1px solid ${T.blue}44`,
            display:'flex',alignItems:'center',justifyContent:'center',flexShrink:0,fontSize:11,color:T.blue,fontWeight:700}}>{i+1}</div>
          <div style={{fontSize:12,color:T.text,lineHeight:1.6,paddingTop:1}}>{String(tip)}</div>
        </div>
      ))}
      {!tips && <div style={{fontSize:11,color:T.muted,marginTop:4,fontStyle:'italic'}}>OE-specific tips will appear once loaded — showing {oe.category} guidance for now.</div>}
    </div>
  );
}

// ── ECO FULL — KPI tab ────────────────────────────────────────────────────────
const ECO_KPIS=[
  {id:1,  name:"Time for initial assessment (OP / Emergency)",                  ref:"PSQ.3.b", formula:"Sum of assessment time / Total patients",                   unit:"minutes", numLabel:"Total assessment time (min)",                    denLabel:"Number of patients assessed",                multiplier:1,    source:"NABH ECO 2nd Ed (2026) Annexure 9 | IHI Institute for Healthcare Improvement",                                    sourceUrl:"https://www.ihi.org"},
  {id:2,  name:"Percentage of reporting errors / 100 investigations",           ref:"PSQ.3.c", formula:"Reporting errors / Tests performed × 100",                  unit:"%",       numLabel:"Number of reporting errors",                     denLabel:"Number of tests performed",                  multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | CAP College of American Pathologists — Laboratory Improvement",               sourceUrl:"https://www.cap.org/laboratory-improvement"},
  {id:3,  name:"Percentage of re-dos",                                          ref:"PSQ.3.c", formula:"Re-tests / Tests performed × 100",                          unit:"%",       numLabel:"Number of re-dos / re-tests",                    denLabel:"Number of tests performed",                  multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | CAP College of American Pathologists — Laboratory Improvement",               sourceUrl:"https://www.cap.org/laboratory-improvement"},
  {id:4,  name:"Incidence of medication errors",                                ref:"PSQ.3.d", formula:"Medication errors / Patient days × 1000",                   unit:"/1000",   numLabel:"Number of medication errors",                    denLabel:"Total patient days",                         multiplier:1000, source:"NABH ECO 2nd Ed (2026) Annexure 9 | ISMP Institute for Safe Medication Practices",                                sourceUrl:"https://www.ismp.org"},
  {id:5,  name:"Percentage of adverse drug reactions",                          ref:"PSQ.3.d", formula:"ADR admissions / Discharges & deaths × 100",                unit:"%",       numLabel:"Admissions with adverse drug reaction",          denLabel:"Total discharges and deaths",                multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | WHO Medication Without Harm Global Challenge",                                sourceUrl:"https://www.who.int/initiatives/medication-without-harm"},
  {id:6,  name:"Percentage of modification of anaesthesia plan",                ref:"PSQ.3.e", formula:"Modified plans / Total anaesthesias × 100",                 unit:"%",       numLabel:"Anaesthesia plans modified",                     denLabel:"Total patients who underwent anaesthesia",   multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | World Federation of Societies of Anaesthesiologists",                         sourceUrl:"https://www.wfsahq.org"},
  {id:7,  name:"Percentage of adverse anaesthesia events",                      ref:"PSQ.3.e", formula:"Adverse events / Total anaesthesias × 100",                 unit:"%",       numLabel:"Adverse anaesthesia events",                     denLabel:"Total patients who underwent anaesthesia",   multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | WHO Patient Safety — Safe Surgery Saves Lives",                               sourceUrl:"https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery"},
  {id:8,  name:"Percentage of adverse laser procedure events",                  ref:"PSQ.3.f", formula:"Adverse laser events / Laser procedures × 100",             unit:"%",       numLabel:"Adverse events related to laser procedures",     denLabel:"Total laser procedures performed",           multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | American Academy of Ophthalmology — Quality and Policy",                     sourceUrl:"https://www.aao.org/quality-and-policy"},
  {id:9,  name:"Percentage of unplanned return to OT",                          ref:"PSQ.3.g", formula:"Unplanned returns / Patients operated × 100",               unit:"%",       numLabel:"Unplanned returns to OT",                        denLabel:"Total patients operated",                    multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | ICHOM International Consortium for Health Outcomes Measurement",              sourceUrl:"https://www.ichom.org/standard-sets/"},
  {id:10, name:"Percentage of re-scheduling of surgeries",                      ref:"PSQ.3.g", formula:"Re-scheduled cases / Surgeries planned × 100",              unit:"%",       numLabel:"Cases re-scheduled (beyond 4 hrs)",              denLabel:"Total surgeries planned",                    multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | ICHOM International Consortium for Health Outcomes Measurement",              sourceUrl:"https://www.ichom.org/standard-sets/"},
  {id:11, name:"Adherence to wrong-site / wrong-patient / wrong-surgery check", ref:"PSQ.3.g", formula:"Protocol-followed cases / Surgeries performed × 100",       unit:"%",       numLabel:"Cases where prevention protocol was followed",   denLabel:"Total surgeries performed",                  multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | WHO Safe Surgery Saves Lives — Surgical Safety Checklist 2008",               sourceUrl:"https://www.who.int/teams/integrated-health-services/patient-safety/research/safe-surgery"},
  {id:12, name:"Percentage of surgery complications",                           ref:"PSQ.3.g", formula:"Surgery complications / Total surgeries × 100",              unit:"%",       numLabel:"Number of surgery complications",                denLabel:"Total surgeries performed",                  multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | ICHOM International Consortium for Health Outcomes Measurement",              sourceUrl:"https://www.ichom.org/standard-sets/"},
  {id:13, name:"Incidence of TASS / Endophthalmitis",                           ref:"PSQ.3.g", formula:"TASS or Endophthalmitis cases / Total surgeries × 100",     unit:"%",       numLabel:"TASS / Endophthalmitis cases",                   denLabel:"Total surgeries performed",                  multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | American Society of Cataract and Refractive Surgery (ASCRS)",                sourceUrl:"https://ascrs.org"},
  {id:14, name:"Critical equipment downtime",                                   ref:"PSQ.3.h", formula:"Sum of downtime hours for all critical equipment (monthly)", unit:"hours",   numLabel:"Total downtime hours (all critical equipment)",  denLabel:"Enter 1 (this is a sum indicator)",          multiplier:1,    source:"NABH ECO 2nd Ed (2026) Annexure 9 | NHS England Health Technical Memorandum (HTM)",                                sourceUrl:"https://www.england.nhs.uk/estates/health-technical-memoranda/"},
  {id:15, name:"Employee satisfaction index",                                   ref:"PSQ.3.j", formula:"Average score achieved / Maximum possible score × 100",      unit:"%",       numLabel:"Average score achieved",                         denLabel:"Maximum possible score",                     multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | Gallup Workplace Employee Engagement Research",                               sourceUrl:"https://www.gallup.com/workplace/285674/improve-employee-engagement-workplace.aspx"},
  {id:16, name:"Number of sentinel events reported and analysed",               ref:"PSQ.3.k", formula:"Events analysed & completed / Total reported × 100",         unit:"%",       numLabel:"Sentinel events analysed and completed",         denLabel:"Total sentinel events reported",             multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | The Joint Commission — Sentinel Events",                                      sourceUrl:"https://www.jointcommission.org/en-us/knowledge-library/sentinel-events"},
  {id:17, name:"Percentage of near misses",                                     ref:"PSQ.3.k", formula:"Near misses reported / Total incidents reported × 100",      unit:"%",       numLabel:"Near misses reported",                           denLabel:"Total incidents reported",                   multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | AHRQ PSNet — Adverse Events Near Misses and Errors",                         sourceUrl:"https://psnet.ahrq.gov/primer/adverse-events-near-misses-and-errors"},
  {id:18, name:"Percentage of medical records without discharge summary",        ref:"PSQ.3.i", formula:"Records without discharge summary / Discharges & deaths × 100", unit:"%",  numLabel:"Records without discharge summary",              denLabel:"Total discharges and deaths",                multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | National Medical Commission India",                                            sourceUrl:"https://www.nmc.org.in"},
  {id:19, name:"Percentage of records with incomplete / improper consent",      ref:"PSQ.3.i", formula:"Incomplete/improper consent records / Discharges & deaths × 100", unit:"%", numLabel:"Records with incomplete or improper consent",    denLabel:"Total discharges and deaths",                multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | National Medical Commission India",                                            sourceUrl:"https://www.nmc.org.in"},
  {id:20, name:"Staff adherence to hand hygiene protocols",                     ref:"PSQ.3.m", formula:"Compliant actions / Total opportunities × 100",              unit:"%",       numLabel:"Compliant hand hygiene actions observed",        denLabel:"Total hand hygiene opportunities observed",  multiplier:100,  source:"NABH ECO 2nd Ed (2026) Annexure 9 | WHO Guidelines on Hand Hygiene in Health Care 2009",                          sourceUrl:"https://www.who.int/publications/i/item/9789241597906"},
];

function EcoFullKpiTab({hospitalId}){
  const [kpiData,setKpiData]=useState([]);
  const [loading,setLoading]=useState(true);
  const [expanded,setExpanded]=useState(null);
  const [forms,setForms]=useState({});
  const [saving,setSaving]=useState(null);
  const [saveSuccess,setSaveSuccess]=useState(null);
  const [calcResults,setCalcResults]=useState({});

  const now=new Date(); const curMonth=now.getMonth()+1; const curYear=now.getFullYear();
  const MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

  useEffect(()=>{
    if(!hospitalId){setLoading(false);return;}
    supabase.from('eco_kpi_data').select('*').eq('hospital_id',hospitalId)
      .order('year',{ascending:false}).order('month',{ascending:false})
      .then(({data})=>{setKpiData(data||[]);setLoading(false);});
  },[hospitalId]);

  const getHistory=(id)=>kpiData.filter(d=>d.kpi_id===id).sort((a,b)=>b.year-a.year||b.month-a.month);
  const getLatest=(id)=>getHistory(id)[0];
  const monthsTracked=(id)=>new Set(kpiData.filter(d=>d.kpi_id===id).map(d=>`${d.year}-${d.month}`)).size;

  const calcValue=(kpi,num,den)=>(num/den)*kpi.multiplier;

  const calcAndSave=async(kpi)=>{
    const f=forms[kpi.id]||{};
    const num=parseFloat(f.num); const den=parseFloat(f.den);
    if(isNaN(num)||isNaN(den)||den===0){alert("Enter valid numerator and non-zero denominator.");return;}
    const value=calcValue(kpi,num,den);
    const month=f.month||curMonth; const year=f.year||curYear;
    setCalcResults(r=>({...r,[kpi.id]:value}));
    setSaving(kpi.id);
    const{error}=await supabase.from('eco_kpi_data').upsert({
      hospital_id:hospitalId,kpi_id:kpi.id,
      numerator:num,denominator:den,
      value:parseFloat(value.toFixed(4)),
      month,year
    },{onConflict:'hospital_id,kpi_id,month,year'});
    if(!error){
      const{data}=await supabase.from('eco_kpi_data').select('*').eq('hospital_id',hospitalId)
        .order('year',{ascending:false}).order('month',{ascending:false});
      setKpiData(data||[]);
      setSaveSuccess(kpi.id);
      setTimeout(()=>setSaveSuccess(null),2000);
    }else{alert("Error: "+error.message);}
    setSaving(null);
  };

  const deleteEntry=async(entryId)=>{
    if(!window.confirm("Delete this entry?"))return;
    const{error}=await supabase.from('eco_kpi_data').delete().eq('id',entryId);
    if(!error)setKpiData(p=>p.filter(d=>d.id!==entryId));
    else alert("Error: "+error.message);
  };

  const tracked=ECO_KPIS.filter(k=>monthsTracked(k.id)>=3).length;
  const inp={padding:'6px 9px',borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13};

  if(loading)return <div style={{textAlign:'center',color:T.muted,padding:40}}>Loading KPIs…</div>;

  return(
    <div style={{padding:'16px 16px 60px'}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:'12px 16px',marginBottom:14}}>
        <div style={{display:'flex',gap:16,alignItems:'center',flexWrap:'wrap'}}>
          <div style={{flex:1}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1}}>KPI TRACKING STATUS</div>
            <div style={{fontSize:14,color:tracked>=16?T.green:tracked>0?T.orange:T.red,fontWeight:700}}>
              {tracked}/20 KPIs with ≥3 months data
              <span style={{fontSize:11,color:T.muted,marginLeft:6}}>(required for NABH assessment)</span>
            </div>
            <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
              <div style={{height:'100%',borderRadius:2,background:tracked>=16?T.green:tracked>0?T.orange:T.red,width:`${Math.round((tracked/20)*100)}%`,transition:'width 0.5s'}}/>
            </div>
          </div>
          <div style={{textAlign:'right'}}>
            <div style={{fontSize:20,fontWeight:700,color:'#06b6d4'}}>{Math.round((tracked/20)*100)}%</div>
            <div style={{fontSize:11,color:T.muted}}>KPI readiness</div>
          </div>
        </div>
      </div>

      <div style={{display:'grid',gap:8}}>
        {ECO_KPIS.map(kpi=>{
          const isOpen=expanded===kpi.id;
          const history=getHistory(kpi.id);
          const latest=getLatest(kpi.id);
          const mt=monthsTracked(kpi.id);
          const statusColor=mt===0?T.red:mt<3?T.orange:T.green;
          const statusLabel=mt===0?'Not started':mt<3?`${mt} month${mt>1?'s':''}`:    `${mt} months`;
          const f=forms[kpi.id]||{};
          const month=f.month!=null?f.month:curMonth;
          const year=f.year!=null?f.year:curYear;
          const twoRecent=history.slice(0,2);
          const trendArrow=twoRecent.length<2?null:twoRecent[0].value>twoRecent[1].value?'↑':twoRecent[0].value<twoRecent[1].value?'↓':'→';

          return(
            <div key={kpi.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,overflow:'hidden'}}>
              <div style={{padding:'12px 16px',cursor:'pointer'}} onClick={()=>{
                setExpanded(isOpen?null:kpi.id);
                if(!isOpen&&!forms[kpi.id])setForms(sf=>({...sf,[kpi.id]:{month:curMonth,year:curYear,num:'',den:''}}));
              }}>
                <div style={{display:'flex',gap:10,alignItems:'flex-start'}}>
                  <div style={{width:28,height:28,borderRadius:6,background:'rgba(6,182,212,0.10)',border:'1px solid rgba(6,182,212,0.30)',display:'flex',alignItems:'center',justifyContent:'center',fontSize:12,fontWeight:800,color:'#06b6d4',flexShrink:0}}>{kpi.id}</div>
                  <div style={{flex:1}}>
                    <div style={{display:'flex',gap:7,alignItems:'center',marginBottom:3,flexWrap:'wrap'}}>
                      <span style={{fontSize:14,fontWeight:700,color:T.white}}>{kpi.name}</span>
                      <span style={{fontSize:8,padding:'2px 6px',borderRadius:4,background:`${statusColor}20`,color:statusColor}}>📊 {statusLabel}</span>
                    </div>
                    <div style={{display:'flex',gap:10,flexWrap:'wrap',alignItems:'center'}}>
                      <span style={{fontSize:12,color:T.muted}}>📋 {kpi.ref}</span>
                      <span style={{fontSize:12,color:T.muted}}>{kpi.formula} → <em>{kpi.unit}</em></span>
                      {latest&&(
                        <span style={{fontSize:12,color:T.blue}}>
                          Latest: {parseFloat(latest.value).toFixed(2)} {kpi.unit} ({MONTHS[latest.month-1]} {latest.year})
                          {trendArrow&&<span style={{marginLeft:4,fontWeight:700,color:trendArrow==='↑'?T.green:trendArrow==='↓'?T.red:T.muted}}>{trendArrow}</span>}
                        </span>
                      )}
                    </div>
                    {kpi.sourceUrl&&<div style={{fontSize:10,color:T.muted,marginTop:2}}>📚 <a href={kpi.sourceUrl} target="_blank" rel="noreferrer" style={{color:T.muted,textDecoration:'underline'}} onClick={e=>e.stopPropagation()}>{kpi.source}</a></div>}
                  </div>
                  <span style={{fontSize:16,color:T.muted}}>{isOpen?'▲':'▼'}</span>
                </div>
              </div>

              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:'14px 16px',display:'grid',gap:12}}>
                  <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                    <div style={{background:'rgba(6,182,212,0.08)',border:'1px solid rgba(6,182,212,0.20)',borderRadius:8,padding:'8px 12px',flex:1}}>
                      <div style={{fontSize:10,color:'#06b6d4',marginBottom:4,fontWeight:700}}>FORMULA</div>
                      <div style={{fontSize:12,color:T.text}}>{kpi.formula}</div>
                    </div>
                    <div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:8,padding:'8px 12px'}}>
                      <div style={{fontSize:10,color:T.muted,marginBottom:4}}>UNIT</div>
                      <div style={{fontSize:13,fontWeight:700,color:'#06b6d4'}}>{kpi.unit}</div>
                    </div>
                    {calcResults[kpi.id]!=null&&(
                      <div style={{background:T.greenD,border:`1px solid ${T.green}44`,borderRadius:8,padding:'8px 12px'}}>
                        <div style={{fontSize:10,color:T.green,marginBottom:4}}>RESULT</div>
                        <div style={{fontSize:13,fontWeight:700,color:T.green}}>{parseFloat(calcResults[kpi.id].toFixed(4))} {kpi.unit}</div>
                      </div>
                    )}
                  </div>

                  <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(180px,1fr))',gap:8}}>
                    <div>
                      <div style={{fontSize:11,color:T.muted,marginBottom:4}}>{kpi.numLabel}</div>
                      <input value={f.num||''} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,num:e.target.value}}))}
                        placeholder="Numerator" type="number" min="0" style={{...inp,width:'100%',boxSizing:'border-box'}}/>
                    </div>
                    <div>
                      <div style={{fontSize:11,color:T.muted,marginBottom:4}}>{kpi.denLabel}</div>
                      <input value={f.den||''} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,den:e.target.value}}))}
                        placeholder="Denominator" type="number" min="0" style={{...inp,width:'100%',boxSizing:'border-box'}}/>
                    </div>
                    <div>
                      <div style={{fontSize:11,color:T.muted,marginBottom:4}}>MONTH</div>
                      <select value={month} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,month:parseInt(e.target.value)}}))} style={{...inp,width:'100%',boxSizing:'border-box'}}>
                        {MONTHS.map((m,i)=><option key={m} value={i+1}>{m}</option>)}
                      </select>
                    </div>
                    <div>
                      <div style={{fontSize:11,color:T.muted,marginBottom:4}}>YEAR</div>
                      <input value={year||''} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,year:parseInt(e.target.value)}}))}
                        type="number" min="2020" style={{...inp,width:'100%',boxSizing:'border-box'}}/>
                    </div>
                  </div>

                  <div style={{display:'flex',gap:8,alignItems:'center',flexWrap:'wrap'}}>
                    <button onClick={()=>calcAndSave(kpi)} disabled={saving===kpi.id}
                      style={{padding:'8px 20px',borderRadius:8,background:'linear-gradient(135deg,#06b6d4,#0891b2)',border:'none',color:'#fff',fontSize:13,fontWeight:700,cursor:'pointer',opacity:saving===kpi.id?0.6:1}}>
                      {saving===kpi.id?'Saving…':'Calculate & Save'}
                    </button>
                    {saveSuccess===kpi.id&&<span style={{fontSize:13,color:T.green}}>✓ Saved</span>}
                  </div>

                  {history.length>0&&(
                    <div>
                      <div style={{fontSize:11,color:T.muted,marginBottom:6,letterSpacing:1}}>HISTORY</div>
                      <div style={{display:'grid',gap:4}}>
                        {history.slice(0,6).map(d=>(
                          <div key={d.id} style={{display:'flex',alignItems:'center',gap:10,padding:'6px 10px',borderRadius:7,background:T.panel2,border:`1px solid ${T.border}`}}>
                            <span style={{fontSize:12,color:T.muted,minWidth:70}}>{MONTHS[d.month-1]} {d.year}</span>
                            <span style={{fontSize:13,fontWeight:700,color:'#06b6d4'}}>{parseFloat(d.value).toFixed(2)} {kpi.unit}</span>
                            <span style={{fontSize:11,color:T.muted}}>{d.numerator} / {d.denominator}</span>
                            <button onClick={()=>deleteEntry(d.id)}
                              style={{marginLeft:'auto',fontSize:11,color:T.red,background:'transparent',border:`1px solid ${T.red}44`,borderRadius:6,padding:'2px 8px',cursor:'pointer'}}>
                              Delete
                            </button>
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
      </div>
    </div>
  );
}

// ── SHCO FULL — KPI tab ───────────────────────────────────────────────────────
const SHCO_KPIS=[
  {id:1, name:"Time for initial assessment of indoor patients",  ref:"PSQ.2a", formula:"Average time",                               unit:"minutes", numLabel:"Total assessment time (min)",    denLabel:"Number of patients",          multiplier:1},
  {id:2, name:"Incidence of medication errors",                  ref:"PSQ.2a", formula:"Errors / Opportunities × 100",              unit:"%",       numLabel:"Number of medication errors",     denLabel:"Number of opportunities",     multiplier:100},
  {id:3, name:"Percentage of transfusion reactions",             ref:"PSQ.2a", formula:"Reactions / Units transfused × 100",        unit:"%",       numLabel:"Number of transfusion reactions", denLabel:"Units transfused",            multiplier:100},
  {id:4, name:"Standardised Mortality Ratio ICU",                ref:"PSQ.2a", formula:"Actual deaths / Predicted deaths",          unit:"ratio",   numLabel:"Actual deaths",                   denLabel:"Predicted deaths",            multiplier:1},
  {id:5, name:"Incidence of pressure ulcers",                    ref:"PSQ.2a", formula:"Cases / 1000 patient days",                 unit:"/1000",   numLabel:"Number of pressure ulcer cases",  denLabel:"Total patient days",          multiplier:1000},
  {id:6, name:"Catheter associated UTI rate",                    ref:"PSQ.2b", formula:"UTIs / 1000 catheter days",                 unit:"/1000",   numLabel:"Number of catheter-associated UTIs",denLabel:"Total catheter days",       multiplier:1000},
  {id:7, name:"Ventilator associated pneumonia rate",            ref:"PSQ.2b", formula:"VAP / 1000 ventilator days",                unit:"/1000",   numLabel:"Number of VAP events",            denLabel:"Total ventilator days",       multiplier:1000},
  {id:8, name:"Central line bloodstream infection rate",         ref:"PSQ.2b", formula:"CLABSI / 1000 central line days",           unit:"/1000",   numLabel:"Number of CLABSI events",         denLabel:"Total central line days",     multiplier:1000},
  {id:9, name:"Surgical site infection rate",                    ref:"PSQ.2b", formula:"SSI / Surgeries × 100",                    unit:"%",       numLabel:"Number of SSIs",                  denLabel:"Number of surgeries",         multiplier:100},
  {id:10,name:"Hand hygiene compliance rate",                    ref:"PSQ.2b", formula:"Compliant observations / Opportunities × 100",unit:"%",     numLabel:"Compliant observations",          denLabel:"Total opportunities",         multiplier:100},
  {id:11,name:"Antibiotic prophylaxis compliance",               ref:"PSQ.2b", formula:"Compliant / Eligible × 100",               unit:"%",       numLabel:"Compliant patients",              denLabel:"Eligible patients",           multiplier:100},
  {id:12,name:"Waiting time for diagnostics",                    ref:"PSQ.2c", formula:"Average waiting time",                      unit:"minutes", numLabel:"Total waiting time (min)",        denLabel:"Number of patients",          multiplier:1},
  {id:13,name:"Time taken for discharge",                        ref:"PSQ.2c", formula:"Average discharge time",                    unit:"minutes", numLabel:"Total discharge time (min)",      denLabel:"Number of discharges",        multiplier:1},
  {id:14,name:"Incidence of patient falls",                      ref:"PSQ.2d", formula:"Falls / 1000 patient days",                 unit:"/1000",   numLabel:"Number of patient falls",         denLabel:"Total patient days",          multiplier:1000},
  {id:15,name:"Needlestick injuries",                            ref:"PSQ.2d", formula:"Injuries / 100 occupied beds",              unit:"/100",    numLabel:"Number of needlestick injuries",  denLabel:"Total occupied beds",         multiplier:100},
];

function ShcoFullKpiTab({hospitalId}){
  const [kpiData,setKpiData]=useState([]);
  const [loading,setLoading]=useState(true);
  const [expanded,setExpanded]=useState(null);
  const [forms,setForms]=useState({});
  const [saving,setSaving]=useState(null);
  const [saveSuccess,setSaveSuccess]=useState(null);
  const [calcResults,setCalcResults]=useState({});

  const now=new Date(); const curMonth=now.getMonth()+1; const curYear=now.getFullYear();
  const MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];

  useEffect(()=>{
    if(!hospitalId){setLoading(false);return;}
    supabase.from('shco_kpi_data').select('*').eq('hospital_id',hospitalId)
      .order('year',{ascending:false}).order('month',{ascending:false})
      .then(({data})=>{setKpiData(data||[]);setLoading(false);});
  },[hospitalId]);

  const getHistory=(id)=>kpiData.filter(d=>d.kpi_id===id).sort((a,b)=>b.year-a.year||b.month-a.month);
  const getLatest=(id)=>getHistory(id)[0];
  const monthsTracked=(id)=>new Set(kpiData.filter(d=>d.kpi_id===id).map(d=>`${d.year}-${d.month}`)).size;

  const calcValue=(kpi,num,den)=>(num/den)*kpi.multiplier;

  const calcAndSave=async(kpi)=>{
    const f=forms[kpi.id]||{};
    const num=parseFloat(f.num); const den=parseFloat(f.den);
    if(isNaN(num)||isNaN(den)||den===0){alert("Enter valid numerator and non-zero denominator.");return;}
    const value=calcValue(kpi,num,den);
    const month=f.month||curMonth; const year=f.year||curYear;
    setCalcResults(r=>({...r,[kpi.id]:value}));
    setSaving(kpi.id);
    const{error}=await supabase.from('shco_kpi_data').upsert({
      hospital_id:hospitalId,kpi_id:kpi.id,
      numerator:num,denominator:den,
      value:parseFloat(value.toFixed(4)),
      month,year
    },{onConflict:'hospital_id,kpi_id,month,year'});
    if(!error){
      const{data}=await supabase.from('shco_kpi_data').select('*').eq('hospital_id',hospitalId)
        .order('year',{ascending:false}).order('month',{ascending:false});
      setKpiData(data||[]);
      setSaveSuccess(kpi.id);
      setTimeout(()=>setSaveSuccess(null),2000);
    }else{alert("Error: "+error.message);}
    setSaving(null);
  };

  const deleteEntry=async(entryId)=>{
    if(!window.confirm("Delete this entry?"))return;
    const{error}=await supabase.from('shco_kpi_data').delete().eq('id',entryId);
    if(!error)setKpiData(p=>p.filter(d=>d.id!==entryId));
    else alert("Error: "+error.message);
  };

  const tracked=SHCO_KPIS.filter(k=>monthsTracked(k.id)>=3).length;
  const inp={padding:'6px 9px',borderRadius:6,border:`1px solid ${T.border}`,background:T.panel,color:T.text,fontSize:13};

  if(loading)return <div style={{textAlign:'center',color:T.muted,padding:40}}>Loading KPIs…</div>;

  return(
    <div style={{padding:'16px 16px 60px'}}>
      {/* Summary bar */}
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:'12px 16px',marginBottom:14}}>
        <div style={{display:'flex',gap:16,alignItems:'center',flexWrap:'wrap'}}>
          <div style={{flex:1}}>
            <div style={{fontSize:11,color:T.muted,marginBottom:3,letterSpacing:1}}>KPI TRACKING STATUS</div>
            <div style={{fontSize:14,color:tracked>=12?T.green:tracked>0?T.orange:T.red,fontWeight:700}}>
              {tracked}/15 KPIs with ≥3 months data
              <span style={{fontSize:11,color:T.muted,marginLeft:6}}>(required for NABH assessment)</span>
            </div>
            <div style={{height:4,background:T.border,borderRadius:2,marginTop:6}}>
              <div style={{height:'100%',borderRadius:2,background:tracked>=12?T.green:tracked>0?T.orange:T.red,width:`${Math.round((tracked/15)*100)}%`,transition:'width 0.5s'}}/>
            </div>
          </div>
          <div style={{textAlign:'right'}}>
            <div style={{fontSize:20,fontWeight:700,color:T.gold}}>{Math.round((tracked/15)*100)}%</div>
            <div style={{fontSize:11,color:T.muted}}>KPI readiness</div>
          </div>
        </div>
      </div>

      {/* KPI cards */}
      <div style={{display:'grid',gap:8}}>
        {SHCO_KPIS.map(kpi=>{
          const isOpen=expanded===kpi.id;
          const history=getHistory(kpi.id);
          const latest=getLatest(kpi.id);
          const mt=monthsTracked(kpi.id);
          const statusColor=mt===0?T.red:mt<3?T.orange:T.green;
          const statusLabel=mt===0?'Not started':mt<3?`${mt} month${mt>1?'s':''}`:    `${mt} months`;
          const f=forms[kpi.id]||{};
          const month=f.month!=null?f.month:curMonth;
          const year=f.year!=null?f.year:curYear;
          // trend: compare last two entries
          const twoRecent=history.slice(0,2);
          const trendArrow=twoRecent.length<2?null:twoRecent[0].value>twoRecent[1].value?'↑':twoRecent[0].value<twoRecent[1].value?'↓':'→';

          return(
            <div key={kpi.id} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,overflow:'hidden'}}>
              <div style={{padding:'12px 16px',cursor:'pointer'}} onClick={()=>{
                setExpanded(isOpen?null:kpi.id);
                if(!isOpen&&!forms[kpi.id])setForms(sf=>({...sf,[kpi.id]:{month:curMonth,year:curYear,num:'',den:''}}));
              }}>
                <div style={{display:'flex',gap:10,alignItems:'flex-start'}}>
                  <div style={{width:28,height:28,borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}30`,display:'flex',alignItems:'center',justifyContent:'center',fontSize:12,fontWeight:800,color:T.gold,flexShrink:0}}>{kpi.id}</div>
                  <div style={{flex:1}}>
                    <div style={{display:'flex',gap:7,alignItems:'center',marginBottom:3,flexWrap:'wrap'}}>
                      <span style={{fontSize:14,fontWeight:700,color:T.white}}>{kpi.name}</span>
                      <span style={{fontSize:8,padding:'2px 6px',borderRadius:4,background:`${statusColor}20`,color:statusColor}}>📊 {statusLabel}</span>
                    </div>
                    <div style={{display:'flex',gap:10,flexWrap:'wrap',alignItems:'center'}}>
                      <span style={{fontSize:12,color:T.muted}}>📋 {kpi.ref}</span>
                      <span style={{fontSize:12,color:T.muted}}>{kpi.formula} → <em>{kpi.unit}</em></span>
                      {latest&&(
                        <span style={{fontSize:12,color:T.blue}}>
                          Latest: {parseFloat(latest.value).toFixed(2)} {kpi.unit} ({MONTHS[latest.month-1]} {latest.year})
                          {trendArrow&&<span style={{marginLeft:4,fontWeight:700,color:trendArrow==='↑'?T.green:trendArrow==='↓'?T.red:T.muted}}>{trendArrow}</span>}
                        </span>
                      )}
                    </div>
                  </div>
                  <span style={{fontSize:16,color:T.muted}}>{isOpen?'▲':'▼'}</span>
                </div>
              </div>

              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:'14px 16px',display:'grid',gap:12}}>
                  {/* Formula strip */}
                  <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                    <div style={{background:T.goldD,border:`1px solid ${T.gold}30`,borderRadius:8,padding:'8px 12px',flex:1}}>
                      <div style={{fontSize:11,color:T.muted,marginBottom:3}}>FORMULA</div>
                      <div style={{fontSize:13,color:T.gold,fontWeight:700}}>{kpi.formula}</div>
                    </div>
                    <div style={{background:T.panel2,borderRadius:8,padding:'8px 12px',flex:1}}>
                      <div style={{fontSize:11,color:T.muted,marginBottom:3}}>UNIT</div>
                      <div style={{fontSize:13,color:T.text,fontWeight:700}}>{kpi.unit}</div>
                    </div>
                  </div>

                  {/* Calculator */}
                  <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                    <div style={{fontSize:12,fontWeight:700,color:T.blue,marginBottom:10,letterSpacing:1}}>🧮 CALCULATOR</div>
                    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>NUMERATOR — {kpi.numLabel}</div>
                        <input type="number" step="0.01" value={f.num||''} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,num:e.target.value}}))} placeholder="Enter value" style={{...inp,width:'100%',boxSizing:'border-box'}}/>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>DENOMINATOR — {kpi.denLabel}</div>
                        <input type="number" step="0.01" value={f.den||''} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,den:e.target.value}}))} placeholder="Enter value" style={{...inp,width:'100%',boxSizing:'border-box'}}/>
                      </div>
                    </div>
                    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginBottom:8}}>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>MONTH</div>
                        <select value={month} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,month:parseInt(e.target.value)}}))} style={{...inp,width:'100%'}}>
                          {MONTHS.map((m,i)=><option key={i} value={i+1}>{m}</option>)}
                        </select>
                      </div>
                      <div>
                        <div style={{fontSize:8,color:T.muted,marginBottom:3}}>YEAR</div>
                        <select value={year} onChange={e=>setForms(sf=>({...sf,[kpi.id]:{...f,year:parseInt(e.target.value)}}))} style={{...inp,width:'100%'}}>
                          {[curYear-1,curYear,curYear+1].map(y=><option key={y} value={y}>{y}</option>)}
                        </select>
                      </div>
                    </div>
                    <button onClick={()=>calcAndSave(kpi)} disabled={saving===kpi.id}
                      style={{padding:'7px 18px',borderRadius:7,background:saveSuccess===kpi.id?T.green:T.goldD,border:`1px solid ${saveSuccess===kpi.id?T.green:T.gold}`,color:saveSuccess===kpi.id?T.bg:T.gold,fontSize:13,fontWeight:700,cursor:'pointer'}}>
                      {saving===kpi.id?'Saving…':saveSuccess===kpi.id?'✅ Saved!':'🧮 Calculate & Save'}
                    </button>
                    {calcResults[kpi.id]!==undefined&&(
                      <div style={{marginTop:8,fontSize:15,fontWeight:700,color:T.gold}}>
                        Result: {calcResults[kpi.id].toFixed(2)} {kpi.unit}
                      </div>
                    )}
                  </div>

                  {/* History */}
                  {history.length>0&&(
                    <div style={{borderTop:`1px solid ${T.border}`,paddingTop:12}}>
                      <div style={{fontSize:11,color:T.muted,marginBottom:8,letterSpacing:1}}>TRACKING HISTORY ({history.length} entries)</div>
                      <div style={{display:'grid',gap:4}}>
                        {history.slice(0,6).map((d,i)=>{
                          const prev=history[i+1];
                          const diff=prev?parseFloat(d.value)-parseFloat(prev.value):null;
                          const arrow=diff===null?null:diff>0?'↑':diff<0?'↓':'→';
                          return(
                            <div key={d.id} style={{display:'flex',gap:10,alignItems:'center',padding:'6px 10px',background:T.panel2,borderRadius:6,border:`1px solid ${T.border}`}}>
                              <span style={{fontSize:12,color:T.muted,minWidth:60}}>{MONTHS[d.month-1]} {d.year}</span>
                              <span style={{fontSize:14,fontWeight:700,color:T.white}}>{parseFloat(d.value).toFixed(2)} {kpi.unit}</span>
                              {arrow&&<span style={{fontSize:13,fontWeight:700,color:arrow==='↑'?T.green:arrow==='↓'?T.red:T.muted}}>{arrow}</span>}
                              {diff!==null&&<span style={{fontSize:11,color:T.muted}}>{diff>0?'+':''}{diff.toFixed(2)} vs {MONTHS[prev.month-1]}</span>}
                              <button onClick={()=>deleteEntry(d.id)} style={{marginLeft:'auto',padding:'2px 8px',borderRadius:5,background:'transparent',border:`1px solid ${T.red}40`,color:T.red,fontSize:11,cursor:'pointer'}}>Delete</button>
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  )}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

// ── AUDITS — shared constants & styles ────────────────────────────────────────────────────────────

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

// Defined once at module level. Getter properties read the current T at spread/access time
// so theme changes are reflected correctly without recreating this object inside components.
const inp={
  get padding(){return"6px 9px"},
  get borderRadius(){return 6},
  get border(){return`1px solid ${T.border}`},
  get background(){return T.panel},
  get color(){return T.text},
  get fontSize(){return 13},
};
const lbl={
  get fontSize(){return 11},
  get color(){return T.muted},
  get marginBottom(){return 3},
  get letterSpacing(){return 1},
};

// ── CREATE AUDIT FORM — stable component so typing doesn't cause AuditsScreen to re-render ────────
function CreateAuditForm({ onSubmit, saving }) {
  const [name,setName]=useState("");
  const [audit_category,setAuditCategory]=useState("clinical");
  const [is_core,setIsCore]=useState(false);
  const [parameters,setParameters]=useState([]);
  const [newParam,setNewParam]=useState("");

  return (
    <div style={{background:T.panel,border:`1px solid ${T.gold}40`,borderRadius:12,padding:"18px 20px",marginBottom:14}}>
      <div style={{fontSize:13,fontWeight:700,color:T.gold,marginBottom:14,letterSpacing:1}}>📋 NEW AUDIT</div>
      <div style={{display:"grid",gap:10}}>
        <div>
          <div style={lbl}>AUDIT NAME *</div>
          <input value={name} onChange={e=>setName(e.target.value)} placeholder="e.g. Hand Hygiene Compliance Audit, OT Checklist Audit…" style={{...inp,width:"100%",boxSizing:"border-box"}}/>
        </div>
        <div style={{display:"grid",gridTemplateColumns:"1fr 1fr",gap:10}}>
          <div>
            <div style={lbl}>CATEGORY</div>
            <select value={audit_category} onChange={e=>setAuditCategory(e.target.value)} style={{...inp,width:"100%"}}>
              {AUDIT_CATEGORIES.map(c=><option key={c.value} value={c.value}>{c.label}</option>)}
            </select>
          </div>
          <div style={{display:"flex",alignItems:"flex-end",paddingBottom:4}}>
            <label style={{display:"flex",alignItems:"center",gap:6,fontSize:13,color:T.text,cursor:"pointer"}}>
              <input type="checkbox" checked={is_core} onChange={e=>setIsCore(e.target.checked)}/> Mark as CORE (critical audit)
            </label>
          </div>
        </div>
        <div>
          <div style={lbl}>CHECKLIST PARAMETERS (optional — add items to check during audit)</div>
          {parameters.map((p,i)=>(
            <div key={i} style={{display:"flex",gap:6,marginBottom:5,alignItems:"center"}}>
              <input value={p} onChange={e=>{const ps=[...parameters];ps[i]=e.target.value;setParameters(ps);}} style={{...inp,flex:1}} placeholder={`Parameter ${i+1}`}/>
              <button onClick={()=>setParameters(f=>f.filter((_,j)=>j!==i))} style={{padding:"4px 9px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:13,cursor:"pointer"}}>✕</button>
            </div>
          ))}
          <div style={{display:"flex",gap:6,marginTop:4}}>
            <input value={newParam} onChange={e=>setNewParam(e.target.value)} onKeyDown={e=>{if(e.key==="Enter"&&newParam.trim()){setParameters(f=>[...f,newParam.trim()]);setNewParam("");}}} placeholder="Type parameter and press Enter…" style={{...inp,flex:1}}/>
            <button onClick={()=>{if(newParam.trim()){setParameters(f=>[...f,newParam.trim()]);setNewParam("");}}} style={{padding:"4px 12px",borderRadius:6,background:T.goldD,border:`1px solid ${T.gold}40`,color:T.gold,fontSize:12,cursor:"pointer"}}>+ Add</button>
          </div>
          <div style={{fontSize:11,color:T.muted,marginTop:4}}>Parameters become checkboxes during audit recording. Leave empty if you prefer free-text findings only.</div>
        </div>
        <button onClick={()=>onSubmit({name,audit_category,is_core,parameters})} disabled={saving||!name.trim()} style={{padding:"9px 20px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:14,fontWeight:700,cursor:"pointer",opacity:saving||!name.trim()?0.5:1,marginTop:4}}>
          {saving?"Creating…":"✓ Create Audit"}
        </button>
      </div>
    </div>
  );
}

// ── AUDITS — 3 tabs: NABH Audits | My Audits | What is Audit ─────────────────────────────────────
function AuditsScreen({ hospitalId, auditMainTab, navigate }) {

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
  const createCustomAudit=async(formData)=>{
    setSavingCreate(true);
    const{data,error}=await supabase.from("custom_audits").insert({
      hospital_id:hospitalId,
      name:formData.name.trim(),
      audit_category:formData.audit_category,
      is_core:formData.is_core,
      parameters:formData.parameters,
    }).select().single();
    if(!error){
      setCustomAudits(p=>[data,...p]);
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
    const params=Array.isArray(audit.parameters)?audit.parameters:(()=>{try{return JSON.parse(audit.parameters||"[]");}catch(e){return[];}})();
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
      {showCreateForm&&<CreateAuditForm onSubmit={createCustomAudit} saving={savingCreate}/>}

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
          const params=Array.isArray(a.parameters)?a.parameters:(()=>{try{return JSON.parse(a.parameters||"[]");}catch(e){return[];}})();
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
                    <button onClick={e=>{e.stopPropagation();setDeleteConfirm(a.id);}} style={{padding:"4px 10px",borderRadius:6,fontSize:12,cursor:"pointer",background:"transparent",border:`1px solid ${T.red}50`,color:T.red,fontWeight:600}}>Delete</button>
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
                                {r.evidence_url&&<a href={/^https?:\/\//i.test(r.evidence_url)?r.evidence_url:"#"} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Report</a>}
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
          <button key={t.id} onClick={()=>navigate({ auditMainTab: t.id })}
            style={{padding:"7px 16px",borderRadius:8,fontSize:13,fontWeight:600,cursor:"pointer",
              background:auditMainTab===t.id?T.goldD:"transparent",
              border:`1px solid ${auditMainTab===t.id?T.gold:T.border}`,
              color:auditMainTab===t.id?T.goldL:T.muted}}>
            {t.label}{t.count!==undefined&&<span style={{marginLeft:5,fontSize:11,opacity:0.7}}>({t.count})</span>}
          </button>
        ))}
      </div>

      {auditMainTab==="learn"&&LearnTab()}
      {auditMainTab==="mine"&&MyAuditsTab()}

      {auditMainTab==="nabh"&&(
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
              const params=Array.isArray(a.parameters)?a.parameters:(()=>{try{return JSON.parse(a.parameters||"[]");}catch(e){return[];}})();
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
                                    {r.evidence_url&&<a href={/^https?:\/\//i.test(r.evidence_url)?r.evidence_url:"#"} target="_blank" rel="noopener noreferrer" style={{padding:"3px 9px",borderRadius:6,background:T.greenD,border:`1px solid ${T.green}40`,color:T.green,fontSize:11,textDecoration:"none",fontWeight:600}}>📎 Report</a>}
                                    <button onClick={()=>deleteRecord(r.id)} style={{fontSize:11,color:T.red,background:"transparent",border:`1px solid ${T.red}30`,borderRadius:4,padding:"2px 7px",cursor:"pointer"}}>Delete</button>
                                  </div>
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      )}
                      {a.conduct_guide&&(()=>{
                        const cg=typeof a.conduct_guide==="string"?(()=>{try{return JSON.parse(a.conduct_guide);}catch(e){return{};}})():a.conduct_guide;
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

  const items=selected?(Array.isArray(selected.items)?selected.items:(()=>{try{return JSON.parse(selected.items||"[]");}catch(e){return[];}})()):[];
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
  const features=["Full NABH compliance tracking","Unlimited OE scoring","KPI tracking and audit management","Committee calendar and mock drills","PDF gap reports","No setup fee. Cancel anytime."];
  return (
    <div style={{maxWidth:520,margin:"0 auto",padding:16}}>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"20px 24px",marginBottom:20,textAlign:"center"}}>
        <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:6}}>PRICING</div>
        <div style={{fontSize:20,fontWeight:800,color:T.white,marginBottom:6}}>Simple, transparent pricing</div>
        <div style={{fontSize:13,color:T.muted}}>14-day free trial · No credit card required · Pay via UPI</div>
      </div>
      <div style={{background:T.panel,border:`1px solid ${T.gold}`,borderRadius:14,padding:"28px 24px",marginBottom:20,textAlign:"center"}}>
        <div style={{fontSize:13,letterSpacing:2,color:T.gold,fontWeight:700,marginBottom:8}}>ACCREDREADY</div>
        <div style={{display:"flex",alignItems:"baseline",justifyContent:"center",gap:4,marginBottom:4}}>
          <span style={{fontSize:38,fontWeight:800,color:T.white}}>₹499</span>
          <span style={{fontSize:14,color:T.muted}}>/month</span>
        </div>
        <div style={{fontSize:12,color:T.muted,marginBottom:24}}>Per hospital · All features included</div>
        <div style={{textAlign:"left",marginBottom:24}}>
          {features.map((f,i)=>(
            <div key={i} style={{display:"flex",gap:10,alignItems:"flex-start",marginBottom:10}}>
              <span style={{color:T.gold,flexShrink:0,fontWeight:700}}>✓</span>
              <span style={{fontSize:13,color:T.text,lineHeight:1.5}}>{f}</span>
            </div>
          ))}
        </div>
        <a href="https://wa.me/918511180957?text=Hi%20Dr.%20Mehul%2C%20I%20want%20to%20subscribe%20to%20AccredReady%20for%20Rs.%20499%2Fmonth" target="_blank" rel="noopener noreferrer"
          style={{display:"block",padding:"14px",borderRadius:10,background:`linear-gradient(135deg,${T.gold},#f0d070)`,color:T.bg,fontSize:15,fontWeight:800,textDecoration:"none",boxShadow:`0 4px 20px ${T.gold}40`}}>
          💬 Get Started — WhatsApp Us
        </a>
      </div>
      <div style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:12,padding:"16px 20px",textAlign:"center"}}>
        <div style={{fontSize:12,color:T.muted,marginBottom:6}}>Questions? We respond within 2 hours on WhatsApp</div>
        <a href="https://wa.me/918511180957" target="_blank" rel="noopener noreferrer" style={{fontSize:14,color:T.gold,fontWeight:700,textDecoration:"none"}}>💬 +91 85111 80957</a>
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
  const [showDeleteModal,setShowDeleteModal]=useState(false);
  const [deleteLoading,setDeleteLoading]=useState(false);
  const [deleteError,setDeleteError]=useState(null);

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

  const handleDeleteAccount=async()=>{
    if(!context?.hospitalId||!user){setDeleteError("Missing account context. Please refresh and try again.");return;}
    setDeleteLoading(true);
    setDeleteError(null);
    try{
      const{data}=await supabase.auth.getSession();
      const accessToken=data?.session?.access_token;
      if(!accessToken)throw new Error("No active session — please sign in again.");

      // Fetch all assessment IDs for this hospital
      const{data:assessments}=await supabase.from("assessments").select("id").eq("hospital_id",context.hospitalId);
      const assessmentIds=(assessments||[]).map(a=>a.id);

      // Delete assessment-scoped tables
      if(assessmentIds.length>0){
        await supabase.from("scores").delete().in("assessment_id",assessmentIds);
        await supabase.from("capa").delete().in("assessment_id",assessmentIds);
      }

      // Delete hospital-scoped tables
      const hid=context.hospitalId;
      await supabase.from("kpi_data").delete().eq("hospital_id",hid);
      await supabase.from("audit_records").delete().eq("hospital_id",hid);
      await supabase.from("mock_drill_records").delete().eq("hospital_id",hid);
      await supabase.from("checklist_links").delete().eq("hospital_id",hid);
      await supabase.from("committee_meetings").delete().eq("hospital_id",hid);
      await supabase.from("calendar_plan").delete().eq("hospital_id",hid);
      await supabase.from("statutory_licenses").delete().eq("hospital_id",hid);
      await supabase.from("custom_audits").delete().eq("hospital_id",hid);
      await supabase.from("patient_tracers").delete().eq("hospital_id",hid);
      await supabase.from("kpi_custom_targets").delete().eq("hospital_id",hid);

      // Delete assessments, then hospital
      await supabase.from("assessments").delete().eq("hospital_id",hid);
      await supabase.from("hospitals").delete().eq("id",hid);

      // Delete the auth user account
      const { error: deleteAuthError } = await supabase.rpc("delete_user");
      if(deleteAuthError) throw new Error(deleteAuthError.message||"Auth deletion failed. Please contact support.");

      // Sign out — auth state listener returns to LoginScreen
      await supabase.auth.signOut();
    }catch(e){
      setDeleteError(e.message||"An unexpected error occurred. Please try again.");
    }finally{
      setDeleteLoading(false);
    }
  };

  const memberSince=user?.created_at?new Date(user.created_at).toLocaleDateString("en-IN",{year:"numeric",month:"long",day:"numeric"}):"—";

  return (
    <div>
      {toast&&<div style={{position:"fixed",top:80,right:16,zIndex:999,maxWidth:360,background:toast.sev==="CRITICAL"?T.redD:T.greenD,border:`1px solid ${toast.sev==="CRITICAL"?T.red:T.green}50`,borderRadius:10,padding:"12px 16px",boxShadow:"0 8px 32px rgba(0,0,0,0.5)"}}>
        <div style={{fontSize:12,fontWeight:700,marginBottom:4,color:toast.sev==="CRITICAL"?T.red:T.green}}>{toast.sev==="CRITICAL"?"🚨":"✅"} {toast.type}</div>
        <div style={{fontSize:13,color:T.text,lineHeight:1.5}}>{toast.msg}</div>
      </div>}

      {showDeleteModal&&(
        <div style={{position:"fixed",inset:0,zIndex:2000,background:"rgba(0,0,0,0.75)",display:"flex",alignItems:"center",justifyContent:"center",padding:16}}>
          <div style={{background:T.panel,border:`2px solid ${T.red}60`,borderRadius:14,padding:"28px 24px",maxWidth:420,width:"100%",boxShadow:"0 16px 64px rgba(0,0,0,0.7)"}}>
            <div style={{fontSize:22,marginBottom:8,textAlign:"center"}}>⚠️</div>
            <div style={{fontSize:17,fontWeight:800,color:T.red,marginBottom:10,textAlign:"center"}}>Delete Account</div>
            <div style={{fontSize:13,color:T.text,lineHeight:1.7,marginBottom:16,padding:"12px 14px",background:T.redD,borderRadius:8,border:`1px solid ${T.red}30`}}>
              This will permanently delete your <strong>hospital profile</strong>, all <strong>scores</strong>, <strong>CAPA records</strong>, <strong>KPI data</strong>, <strong>audit records</strong>, and your <strong>login</strong>. <br/><br/>
              <span style={{color:T.red,fontWeight:700}}>This cannot be undone.</span>
            </div>
            {deleteError&&<div style={{fontSize:12,color:T.red,background:T.redD,border:`1px solid ${T.red}30`,borderRadius:7,padding:"8px 12px",marginBottom:12}}>{deleteError}</div>}
            <div style={{display:"flex",gap:10,justifyContent:"flex-end"}}>
              <button onClick={()=>{setShowDeleteModal(false);setDeleteError(null);}} disabled={deleteLoading}
                style={{padding:"9px 20px",borderRadius:8,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:13,fontWeight:700,cursor:deleteLoading?"not-allowed":"pointer",opacity:deleteLoading?0.5:1}}>
                Cancel
              </button>
              <button onClick={handleDeleteAccount} disabled={deleteLoading}
                style={{padding:"9px 20px",borderRadius:8,border:`1px solid ${T.red}70`,background:T.redD,color:T.red,fontSize:13,fontWeight:800,cursor:deleteLoading?"not-allowed":"pointer",opacity:deleteLoading?0.7:1}}>
                {deleteLoading?"Deleting…":"Yes, delete everything"}
              </button>
            </div>
          </div>
        </div>
      )}

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
                <input value={displayName} onChange={e=>setDisplayName(e.target.value)} placeholder="e.g., Dr. Sharma" style={{flex:1,padding:"8px 12px",borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14}}/>
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

        {/* Delete Account */}
        <div style={{background:T.panel,border:`2px solid ${T.red}40`,borderRadius:10,padding:"16px 18px"}}>
          <div style={{fontSize:11,letterSpacing:2,color:T.red,marginBottom:10}}>⚠️ DANGER ZONE</div>
          <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",gap:12,flexWrap:"wrap"}}>
            <div>
              <div style={{fontSize:13,fontWeight:700,color:T.text,marginBottom:3}}>Delete Account</div>
              <div style={{fontSize:12,color:T.muted,maxWidth:320}}>Permanently removes your hospital, all scores, CAPAs, KPI data, audit records, and login. This cannot be undone.</div>
            </div>
            <button onClick={()=>{setShowDeleteModal(true);setDeleteError(null);}}
              style={{padding:"7px 18px",borderRadius:8,border:`1px solid ${T.red}60`,background:T.redD,color:T.red,fontSize:13,fontWeight:700,cursor:"pointer",flexShrink:0}}>
              Delete Account
            </button>
          </div>
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
            <div style={{fontSize:11,letterSpacing:3,color:T.gold,marginBottom:2}}>ACCREDREADY</div>
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
const TOUR_STEPS=[
  {title:"Welcome to AccredReady 🎉",body:"Your complete NABH accreditation toolkit. This 60-second tour shows you exactly where everything is.",targetId:null,tabToActivate:null},
  {title:"Your Readiness Verdict",body:"Dashboard shows your live PASS/FAIL verdict and compliance % across all 4 NABH rules.",targetId:"tour-target-dashboard",tabToActivate:"Dashboard"},
  {title:"Score Your OEs",body:"Go here to score each Objective Element — Met / Partial / Not Met. This drives your entire readiness verdict.",targetId:"tour-target-score",tabToActivate:"Score OEs"},
  {title:"Fix Gaps",body:"All your Not Met OEs appear here with corrective actions. Assign owner and target date.",targetId:"tour-target-fixgaps",tabToActivate:"Fix Gaps"},
  {title:"Audits & Drills",body:"Run mandatory clinical audits and mock drills before your survey. Checklists included.",targetId:"tour-target-audits",tabToActivate:"Audits"},
  {title:"KPIs & Committees",body:"Track KPIs and manage all mandatory committees with formation guides.",targetId:"tour-target-more",tabToActivate:null},
  {title:"You're ready to start! 🚀",body:"Begin with Score OEs → complete your first chapter. Your Gap Report PDF updates as you score.",targetId:null,tabToActivate:null},
];

const SHCO_FULL_TOUR_STEPS=[
  {title:"Welcome to SHCO Full Accreditation 🎉",body:"Your complete NABH SHCO Full Accreditation toolkit. This quick tour shows you where everything is.",targetId:null,shcoFullTab:'dashboard'},
  {title:"Step 1: Choose Assessment Mode",body:"Pick Final Assessment (first award), Surveillance (18-month check), or Re-accreditation (4-year renewal). This determines which OEs are evaluated.",targetId:"shco-tour-assess-mode",shcoFullTab:'dashboard'},
  {title:"Step 2: Readiness Dashboard",body:"See your live PASS/FAIL verdict across all NABH scoring rules — 80% overall compliance and every Core OE must score ≥4.",targetId:"shco-tour-rules",shcoFullTab:'dashboard'},
  {title:"Step 3: Score Your OEs",body:"Score each Objective Element 1–5 (No compliance to Full compliance). Filter by chapter or OE level to focus your effort.",targetId:"shco-tour-score",shcoFullTab:null},
  {title:"Step 4: Fix Gaps",body:"All weak OEs (score ≤3) appear here. Add corrective actions, assign an owner, and set target dates to track progress.",targetId:"shco-tour-fixgaps",shcoFullTab:'fixgaps'},
  {title:"Step 5: Download Gap Report",body:"Export a PDF Gap Report with your compliance % and all action items — share with your team or keep for assessor review.",targetId:"shco-tour-pdf",shcoFullTab:'dashboard'},
  {title:"You're ready to start! 🚀",body:"Begin with Score OEs → score your first chapter. The Dashboard updates in real time as you score.",targetId:null,shcoFullTab:null},
];

function WalktourOverlay({step,totalSteps,onNext,onSkip,steps}){
  const isLast=step===totalSteps-1;
  const s=steps[step];
  return(
    <div style={{position:'fixed',inset:0,zIndex:10000,display:'flex',alignItems:'center',justifyContent:'center'}}>
      <div style={{position:'fixed',inset:0,background:'rgba(0,0,0,0.82)'}}/>
      <div style={{position:'relative',width:'90%',maxWidth:420,background:T.panel,border:`1px solid ${T.border}`,borderRadius:16,padding:'24px 28px',zIndex:10001,boxShadow:'0 8px 40px rgba(0,0,0,0.6)'}}>
        <div style={{display:'flex',justifyContent:'center',gap:6,marginBottom:16}}>
          {steps.map((_,i)=>(
            <div key={i} style={{width:8,height:8,borderRadius:'50%',background:i===step?T.gold:T.muted,transition:'background 0.2s'}}/>
          ))}
        </div>
        <div style={{fontSize:19,fontWeight:700,color:T.gold,marginBottom:10,textAlign:'center'}}>{s.title}</div>
        <div style={{fontSize:14,color:T.text,lineHeight:1.65,textAlign:'center',marginBottom:24}}>{s.body}</div>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
          <button onClick={onSkip} style={{background:'none',border:'none',color:T.muted,cursor:'pointer',fontSize:13,padding:'8px 4px'}}>Skip Tour</button>
          <button onClick={onNext} style={{background:T.gold,color:'#000',border:'none',borderRadius:8,padding:'10px 22px',fontWeight:700,fontSize:14,cursor:'pointer'}}>
            {isLast?'Get Started':'Next →'}
          </button>
        </div>
      </div>
    </div>
  );
}

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
  const [shcoElcScores, setShcoElcScores] = useState({});
  const [shcoElcScoreSaving, setShcoElcScoreSaving] = useState({});
  const [shcoOeSearch, setShcoOeSearch] = useState('');
  const [shcoOeChapter, setShcoOeChapter] = useState('all');
  const [shcoOeExpanded, setShcoOeExpanded] = useState({});
  const [shcoOeTips, setShcoOeTips] = useState({});
  const [shcoOeTipsLoading, setShcoOeTipsLoading] = useState({});
  const [shcoDocFilter, setShcoDocFilter] = useState('all');
  const [shcoDocPart, setShcoDocPart] = useState('all');
  const [hcoMode, setHcoMode] = useState('elc');
  const [hcoElcTab, setHcoElcTab] = useState('overview');
  const [hcoElcProgress, setHcoElcProgress] = useState({});
  const [hcoLicProgress, setHcoLicProgress] = useState({});
  const [hcoDocFilter, setHcoDocFilter] = useState('all');
  const [hcoDocPart, setHcoDocPart] = useState('all');
  const [hcoOeSearch, setHcoOeSearch] = useState('');
  const [hcoOeChapter, setHcoOeChapter] = useState('all');
  const [hcoOeExpanded, setHcoOeExpanded] = useState({});
  const [hcoOeTips, setHcoOeTips] = useState({});
  const [hcoOeTipsLoading, setHcoOeTipsLoading] = useState({});
  const [hcoOeLevels, setHcoOeLevels] = useState({});
  const [elcScores, setElcScores] = useState({});
  const [elcScoreSaving, setElcScoreSaving] = useState({});
  const [hcoElcGapFilter, setHcoElcGapFilter] = useState('ALL');
  const [hcoElcGapSearch,  setHcoElcGapSearch]  = useState('');
  const [elcCapaDb,       setElcCapaDb]       = useState({});
  const [elcCapaForm,     setElcCapaForm]     = useState({});
  const [elcCapaSaving,   setElcCapaSaving]   = useState({});
  const [elcCapaDeleting, setElcCapaDeleting] = useState({});
  const [elcPdfLoading,   setElcPdfLoading]   = useState(false);
  const [pdfLoading, setPdfLoading] = useState(false);
  const [showMoreMenu, setShowMoreMenu] = useState(false);
  const [showUserMenu, setShowUserMenu] = useState(false);
  const [theme, setTheme] = useState('dark');
  const [navStack, setNavStack] = useState([]);
  const [drillsView, setDrillsView] = useState('tracker');
  const [selectedDrill, setSelectedDrill] = useState(null);
  const [tracerView, setTracerView] = useState('list');
  const [tracerType, setTracerType] = useState('General IPD');
  const [auditMainTab, setAuditMainTab] = useState('nabh');
  const [committeesView, setCommitteesView] = useState('reference');
  const [showLicenseAdd, setShowLicenseAdd] = useState(false);
  const [tourStep, setTourStep] = useState(null);
  const activeStepsRef = useRef(TOUR_STEPS);
  const [shcoFullOes, setShcoFullOes] = useState([]);
  const [shcoFullScores, setShcoFullScores] = useState({});
  const [shcoFullScoreSaving, setShcoFullScoreSaving] = useState({});
  const [shcoFullChapter, setShcoFullChapter] = useState('all');
  const [shcoFullLevel, setShcoFullLevel] = useState('all');
  const [shcoFullLoading, setShcoFullLoading] = useState(false);
  const [shcoFullAssessType, setShcoFullAssessType] = useState('final');
  const [shcoFullTab, setShcoFullTab] = useState('dashboard');
  const [shcoFullSearch, setShcoFullSearch] = useState('');
  const [shcoFullPdfLoading, setShcoFullPdfLoading] = useState(false);
  const [shcoFullShowTip, setShcoFullShowTip] = useState({});
  const [shcoFullGapFilter, setShcoFullGapFilter] = useState('ALL');
  const [shcoFullGapSearch, setShcoFullGapSearch] = useState('');
  const [aiWidgetOpen, setAiWidgetOpen] = useState(false);
  const [aiWidgetTrigger, setAiWidgetTrigger] = useState({ code: null, id: 0 });
  const [shcoFullCapaForm, setShcoFullCapaForm] = useState({});
  const [shcoFullCapaSaving, setShcoFullCapaSaving] = useState({});
  const [shcoFullCapaDb, setShcoFullCapaDb] = useState({});
  const [ecoFullOes, setEcoFullOes] = useState([]);
  const [ecoFullScores, setEcoFullScores] = useState({});
  const [ecoFullScoreSaving, setEcoFullScoreSaving] = useState({});
  const [ecoFullChapter, setEcoFullChapter] = useState('all');
  const [ecoFullLevel, setEcoFullLevel] = useState('all');
  const [ecoFullLoading, setEcoFullLoading] = useState(false);
  const [ecoFullAssessType, setEcoFullAssessType] = useState('final');
  const [ecoFullTab, setEcoFullTab] = useState('dashboard');
  const [ecoFullSearch, setEcoFullSearch] = useState('');
  const [ecoFullPdfLoading, setEcoFullPdfLoading] = useState(false);
  const [ecoFullShowTip, setEcoFullShowTip] = useState({});
  const [ecoFullGapFilter, setEcoFullGapFilter] = useState('ALL');
  const [ecoFullGapSearch, setEcoFullGapSearch] = useState('');
  const [ecoFullCapaForm, setEcoFullCapaForm] = useState({});
  const [ecoFullCapaSaving, setEcoFullCapaSaving] = useState({});
  const [ecoFullCapaDb, setEcoFullCapaDb] = useState({});

  // Reassign module-level T so all component closures see the correct theme
  T = theme === 'light' ? LIGHT_THEME : DARK_THEME;

  const toggleTheme = async () => {
    const next = theme === 'dark' ? 'light' : 'dark';
    setTheme(next);
    if (user?.id) {
      await supabase.from("profiles").upsert({ id: user.id, theme_preference: next }, { onConflict: "id" });
    }
  };

  const activeSteps = (selectedProgramme === 'shco-full' || selectedProgramme === 'eco-full') ? SHCO_FULL_TOUR_STEPS : TOUR_STEPS;
  activeStepsRef.current = activeSteps;

  const dismissTour = useCallback(async () => {
    setTourStep(null);
    console.log("[Tour] dismissTour called. context.hospitalId =", context?.hospitalId);
    if (context?.hospitalId) {
      console.log("[Tour] Running UPDATE hospitals SET walkthrough_dismissed=true WHERE id=", context.hospitalId);
      const { error } = await supabase.from("hospitals").update({walkthrough_dismissed:true}).eq("id",context.hospitalId);
      console.log("[Tour] UPDATE result — error:", error);
    } else {
      console.warn("[Tour] dismissTour: hospitalId is missing — skipping DB update");
    }
  },[context?.hospitalId]); // eslint-disable-line react-hooks/exhaustive-deps

  const nextTourStep = useCallback(() => {
    setTourStep(prev => {
      if (prev === null) return null;
      if (prev >= activeStepsRef.current.length - 1) { dismissTour(); return null; }
      return prev + 1;
    });
  }, [dismissTour]);

  const TAB_TO_SCREEN = {'Dashboard':'dashboard','Score OEs':'scoring','Fix Gaps':'gaps','Audits':'audits','KPIs':'kpis'};
  useEffect(() => {
    if (tourStep === null) return;
    const step = activeStepsRef.current[tourStep];
    if (step.shcoFullTab) { setShcoFullTab(step.shcoFullTab); }
    else if (step.tabToActivate) { setScreen(TAB_TO_SCREEN[step.tabToActivate] || screen); }
  }, [tourStep]); // eslint-disable-line react-hooks/exhaustive-deps

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
        MOM:'Management of Medications',PRE:'Patient Rights and Education',
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

      // ── PAGE: CORRECTIVE ACTIONS (CAPA) ─────────────────────────────────
      const {data:rawCapas}=await supabase.from("capa").select("*").eq("assessment_id",context?.assessmentId||'');
      const capaMap={};
      (rawCapas||[]).forEach(r=>{capaMap[r.oe_id]=r;});
      const capaEntries=(gaps||[]).filter(g=>capaMap[g.oe_id]?.finding);
      if(capaEntries.length>0){
        doc.addPage();
        doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
        doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');
        y=60;
        doc.setFontSize(16); doc.setTextColor('#eef4f9');
        doc.text('Corrective Actions (CAPA)',60,y); y+=10;
        doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=18;
        doc.setFontSize(8); doc.setTextColor('#3a5870');
        doc.text(`${capaEntries.length} CAPA(s) recorded for gap OEs`,60,y); y+=20;
        capaEntries.forEach(g=>{
          const capa=capaMap[g.oe_id];
          const scC=g.score<=2?'#e05a5a':g.score===3?'#f4a441':'#4caf7d';
          doc.setFontSize(8);
          const findLines=doc.splitTextToSize(capa.finding||'',W-180);
          const actionLines=doc.splitTextToSize(capa.action_planned||'',W-180);
          const estH=14+findLines.length*10+actionLines.length*10+28+16;
          if(y+estH>H-40){
            doc.addPage();
            doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
            doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');
            y=60;
          }
          doc.setFillColor('#0a1a2a');
          doc.roundedRect(60,y-4,W-120,estH,3,3,'F');
          doc.setDrawColor('#1a3550');
          doc.roundedRect(60,y-4,W-120,estH,3,3,'S');
          doc.setFontSize(9); doc.setTextColor('#c9a84c');
          doc.text(g.oe_id||'',68,y+8);
          doc.setFontSize(8); doc.setTextColor('#8aadcc');
          doc.text(g.level||'',130,y+8);
          doc.setFontSize(8); doc.setTextColor(scC);
          doc.text(`Score: ${g.score}/5`,W-64,y+8,{align:'right'});
          y+=18;
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('FINDING',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          findLines.forEach((line,i)=>doc.text(line,68,y+9+i*10));
          y+=9+findLines.length*10+4;
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('ACTION PLANNED',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          actionLines.forEach((line,i)=>doc.text(line,68,y+9+i*10));
          y+=9+actionLines.length*10+4;
          const person2=capa.responsible_person||'—';
          const dateStr2=capa.target_date?new Date(capa.target_date).toLocaleDateString('en-IN',{day:'2-digit',month:'short',year:'numeric'}):'—';
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('RESPONSIBLE: ',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text(person2,68+doc.getTextWidth('RESPONSIBLE: '),y);
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('TARGET DATE: ',W/2,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text(dateStr2,W/2+doc.getTextWidth('TARGET DATE: '),y);
          y+=18;
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
        if(i>1) doc.text('NABH Accreditation Platform - accredready.in',60,H-18);
      }

      const cleanName=cleanHospital.replace(/[^a-zA-Z0-9]/g,'_');
      doc.save(`${cleanName}_NABH_Gap_Report_${fileDateStr}.pdf`);
    } catch(e){ console.error('PDF generation failed:',e); }
    setPdfLoading(false);
  };

  // ── SHCO Full Gap Report PDF ─────────────────────────────────────────────
  const generateShcoFullPDF = async () => {
    setShcoFullPdfLoading(true);
    try {
      const doc = new jsPDF({ unit:'pt', format:'a4' });
      const W = doc.internal.pageSize.getWidth();
      const H = doc.internal.pageSize.getHeight();
      const today = new Date();
      const dateStr = today.toLocaleDateString('en-IN',{day:'2-digit',month:'long',year:'numeric'});
      const fileDateStr = String(today.getDate()).padStart(2,'0')+String(today.getMonth()+1).padStart(2,'0')+today.getFullYear();
      const cleanHospital = (context?.hospitalName||'Hospital').replace(/\s+(New|Trial|Active|Expired)$/i,'').trim();
      const assessTypeLabel = shcoFullAssessType==='final' ? 'Final Assessment'
                            : shcoFullAssessType==='surveillance' ? 'Surveillance Assessment'
                            : 'Re-accreditation Assessment';

      const SHCO_CHAPTERS = [
        {key:'AAC',name:'Access, Assessment and Continuity of Care'},
        {key:'COP',name:'Care of Patients'},
        {key:'MOM',name:'Management of Medication'},
        {key:'PRE',name:'Patient Rights and Education'},
        {key:'HIC',name:'Hospital Infection Prevention and Control'},
        {key:'PSQ',name:'Patient Safety and Quality Improvement'},
        {key:'ROM',name:'Responsibility of Management'},
        {key:'FMS',name:'Facility Management and Safety'},
        {key:'HRM',name:'Human Resource Management'},
        {key:'IMS',name:'Information Management System'},
      ];

      // OE subsets
      const coreCommOEs = shcoFullOes.filter(oe=>oe.level==='Core'||oe.level==='Commitment');
      const achieveOEs  = shcoFullOes.filter(oe=>oe.level==='Achievement');
      const excelOEs    = shcoFullOes.filter(oe=>oe.level==='Excellence');
      const coreOEs     = shcoFullOes.filter(oe=>oe.level==='Core');
      const relevantOEs = shcoFullAssessType==='final'        ? coreCommOEs
                        : shcoFullAssessType==='surveillance' ? shcoFullOes.filter(oe=>oe.level!=='Excellence')
                        : shcoFullOes;

      const compliance = arr => arr.length>0
        ? Math.round(arr.reduce((a,oe)=>a+(shcoFullScores[oe.oe_code]||0),0)/(arr.length*5)*100) : 0;

      const ccPct    = compliance(coreCommOEs);
      const achPct   = compliance(achieveOEs);
      const excelPct = compliance(excelOEs);

      // Chapter stats
      const chStats = SHCO_CHAPTERS.map(c=>{
        const chOes    = relevantOEs.filter(oe=>oe.chapter===c.key);
        const chScored = chOes.filter(oe=>shcoFullScores[oe.oe_code]);
        const chAvg    = chScored.length>0 ? chScored.reduce((a,oe)=>a+shcoFullScores[oe.oe_code],0)/chScored.length : null;
        const totalCount = shcoFullOes.filter(oe=>oe.chapter===c.key).length;
        const pct = chAvg!==null ? Math.round(chAvg/5*100) : null;
        return {...c, relevantCount:chOes.length, totalCount, scoredCount:chScored.length, avg:chAvg, pct };
      });

      // Rules
      const maxLowPerStd = shcoFullAssessType==='renewal' ? 0 : 1;
      const stdMap={};
      relevantOEs.forEach(oe=>{
        if(!stdMap[oe.standard_code])stdMap[oe.standard_code]={oes:[]};
        stdMap[oe.standard_code].oes.push(oe);
      });
      const stdChecks = Object.entries(stdMap).map(([code,{oes}])=>{
        const scored = oes.filter(oe=>shcoFullScores[oe.oe_code]);
        const avg    = scored.length>0 ? scored.reduce((a,oe)=>a+shcoFullScores[oe.oe_code],0)/scored.length : null;
        const atOrBelow2 = oes.filter(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]<=2).length;
        return {code,avg,atOrBelow2};
      });
      const chapAvgFails = chStats.filter(c=>c.avg!==null&&c.avg<4);
      const corePass  = coreOEs.every(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]>=4);
      const rule1Pass = corePass;
      const rule2Pass = ccPct>=80;
      const rule3Pass = stdChecks.every(s=>s.atOrBelow2<=maxLowPerStd);
      const rule4Pass = stdChecks.every(s=>s.avg===null||s.avg>=4);
      const rule5Pass = chapAvgFails.length===0;
      const allRulesPass = rule1Pass&&rule2Pass&&rule3Pass&&rule4Pass&&rule5Pass;

      const rules = [
        {label:'All Core OEs must score ≥4',            detail:`${coreOEs.length} Core OEs — every one must reach Good compliance`,       pass:rule1Pass},
        {label:`Core + Commitment overall ≥80% (${coreCommOEs.length} OEs)`, detail:`Current: ${ccPct}% — threshold: 80%`,                  pass:rule2Pass},
        {label:'No standard with >'+maxLowPerStd+' OE(s) scored ≤2', detail:`${stdChecks.filter(s=>s.atOrBelow2>maxLowPerStd).length} standard(s) failing this rule`, pass:rule3Pass},
        {label:'Average score per standard ≥4',         detail:`${stdChecks.filter(s=>s.avg!==null&&s.avg<4).length} standard(s) below 4 average`,                     pass:rule4Pass},
        {label:'Average score per chapter ≥4',          detail:`${chapAvgFails.length} chapter(s) below 4 average`,                         pass:rule5Pass},
      ];
      if(shcoFullAssessType==='surveillance'||shcoFullAssessType==='renewal'){
        rules.push({label:`Achievement overall ≥80% (${achieveOEs.length} OEs)`, detail:`Current: ${achPct}%`, pass:achPct>=80});
      }
      if(shcoFullAssessType==='renewal'){
        rules.push({label:`Excellence overall ≥80% (${excelOEs.length} OEs)`, detail:`Current: ${excelPct}%`, pass:excelPct>=80});
      }

      // Weak OEs (score ≤3, from relevantOEs)
      const weakOEs = relevantOEs.filter(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]<=3)
        .sort((a,b)=>shcoFullScores[a.oe_code]-shcoFullScores[b.oe_code]||a.oe_code.localeCompare(b.oe_code));
      const criticalOEs = coreOEs.filter(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]<4);
      const scoredCount = relevantOEs.filter(oe=>shcoFullScores[oe.oe_code]).length;

      const scoreLabel = ['','No compliance','Poor compliance','Partial compliance','Good compliance','Full compliance'];
      const scoreCol   = s => s===1||s===2 ? '#e05a5a' : s===3 ? '#f4a441' : s>=4 ? '#4caf7d' : '#3a5870';

      // ── Helper: new page background ──────────────────────────────────────
      const newPage = () => {
        doc.addPage();
        doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
        doc.setFillColor('#c9a84c'); doc.rect(0,0,W,4,'F');
      };

      // ── PAGE 1: COVER ───────────────────────────────────────────────────
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor('#c9a84c'); doc.rect(0,0,W,6,'F');

      doc.setFontSize(9); doc.setTextColor('#c9a84c');
      doc.text('ACCREDREADY · NABH SHCO 3RD EDITION',W/2,58,{align:'center'});
      doc.setFontSize(27); doc.setTextColor('#eef4f9');
      doc.text('NABH SHCO Gap Assessment Report',W/2,106,{align:'center'});
      doc.setDrawColor('#c9a84c'); doc.setLineWidth(0.5);
      doc.line(60,124,W-60,124);

      doc.setFontSize(22); doc.setTextColor('#c9a84c');
      const hospLines = doc.splitTextToSize(cleanHospital, W-160);
      doc.text(hospLines, W/2, 160, {align:'center'});
      const afterHosp = 160 + (hospLines.length-1)*28;
      doc.setFontSize(11); doc.setTextColor('#c8dcea');
      doc.text(assessTypeLabel, W/2, afterHosp+26, {align:'center'});
      doc.setFontSize(9); doc.setTextColor('#3a5870');
      doc.text(`Generated on ${dateStr}`, W/2, afterHosp+44, {align:'center'});

      const oePct = ccPct;
      const passCol  = oePct>=80 ? '#4caf7d' : oePct>=60 ? '#f4a441' : '#e05a5a';
      const verdictText = allRulesPass ? 'ACCREDITATION READY' : oePct>=80 ? 'RULES INCOMPLETE' : 'NOT READY';

      doc.setFontSize(72); doc.setTextColor(passCol);
      doc.text(`${oePct}%`,W/2, afterHosp+148,{align:'center'});
      doc.setFontSize(11); doc.setTextColor('#c8dcea');
      doc.text('CORE + COMMITMENT COMPLIANCE',W/2, afterHosp+172,{align:'center'});
      doc.setFontSize(20); doc.setTextColor(passCol);
      doc.text(`VERDICT: ${verdictText}`,W/2, afterHosp+208,{align:'center'});

      const statY = afterHosp+248;
      const stats3=[
        [`${scoredCount} / ${relevantOEs.length}`, 'Relevant OEs Scored'],
        [`${weakOEs.length}`,                       'Weak OEs (score ≤3)'],
        [`${criticalOEs.length}`,                   'Core OEs below 4'],
      ];
      const colW=(W-120)/3;
      stats3.forEach(([val,lbl],i)=>{
        const cx=60+colW*i+colW/2;
        doc.setFillColor('#081525'); doc.roundedRect(60+colW*i+4, statY-20, colW-8, 46, 4,4,'F');
        doc.setFontSize(22); doc.setTextColor('#c9a84c');
        doc.text(val, cx, statY+4, {align:'center'});
        doc.setFontSize(8); doc.setTextColor('#3a5870');
        doc.text(lbl, cx, statY+20, {align:'center'});
      });

      doc.setFontSize(7); doc.setTextColor('#3a5870');
      doc.text('Generated by accredready.in — Independent educational tool — Not affiliated with NABH/QCI',W/2,H-28,{align:'center'});

      // ── PAGE 2: ACCREDITATION RULES ─────────────────────────────────────
      newPage();
      let y=50;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Accreditation Rules',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.setLineWidth(0.5);
      doc.line(60,y,W-60,y); y+=24;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`ASSESSMENT TYPE: ${assessTypeLabel.toUpperCase()} · ${rules.filter(r=>r.pass).length} of ${rules.length} RULES PASSING`,60,y); y+=18;

      rules.forEach(r=>{
        if(y>H-60){ newPage(); y=50; }
        doc.setFillColor(r.pass?'#061810':'#180606');
        doc.roundedRect(60,y-14,W-120,32,3,3,'F');
        doc.setFillColor(r.pass?'#4caf7d':'#e05a5a');
        doc.roundedRect(W-106,y-7,40,16,3,3,'F');
        doc.setFontSize(8); doc.setTextColor('#050e1a');
        doc.text(r.pass?'PASS':'FAIL',W-86,y+3,{align:'center'});
        doc.setFontSize(10); doc.setTextColor('#eef4f9');
        doc.text(r.label,76,y-2);
        doc.setFontSize(8); doc.setTextColor('#8aadcc');
        doc.text(r.detail,76,y+11);
        y+=40;
      });

      // ── PAGE 2 continued: CHAPTER-WISE TABLE ────────────────────────────
      y+=16;
      if(y>H-220){ newPage(); y=50; }
      doc.setFontSize(14); doc.setTextColor('#eef4f9');
      doc.text('Chapter-wise Compliance',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=20;

      // Chapter table — fixed column x positions (content 60..535 = 475pt)
      // Ch:40 | Name:200 | Relevant:50 | Scored:50 | Compliance:60 | Status:75
      const chC1=64,chC2=108,chC3=312,chC4=368,chC5=424,chC6=530;

      // Header row
      doc.setFillColor('#081525'); doc.rect(60,y-13,W-120,20,'F');
      doc.setFontSize(8); doc.setTextColor('#c9a84c');
      doc.text('CH',chC1,y-2);
      doc.text('CHAPTER NAME',chC2,y-2);
      doc.text('RELEV.',chC3,y-2);
      doc.text('SCORED',chC4,y-2);
      doc.text('COMPLIANCE',chC5,y-2);
      doc.text('STATUS',chC6,y-2,{align:'right'});
      y+=14;

      chStats.forEach(c=>{
        if(y>H-40){ newPage(); y=50; }
        const pctVal = c.pct!==null ? c.pct : null;
        const pass   = pctVal!==null&&pctVal>=80;
        const rowBg  = pctVal===null ? '#0a1520' : pass ? '#061810' : pctVal>=60 ? '#14100a' : '#180606';
        const valCol = pctVal===null ? '#3a5870' : pass ? '#4caf7d' : pctVal>=60 ? '#f4a441' : '#e05a5a';
        // Pre-wrap chapter name to fit 200pt column at 8pt
        doc.setFontSize(8);
        const nameLines = doc.splitTextToSize(c.name, 200);
        const chRowH = Math.max(20, nameLines.length*10+6);
        doc.setFillColor(rowBg); doc.rect(60,y-12,W-120,chRowH,'F');
        doc.setFontSize(9); doc.setTextColor('#c9a84c');
        doc.text(c.key,chC1,y-1);
        doc.setFontSize(8); doc.setTextColor('#c8dcea');
        nameLines.forEach((line,i)=>doc.text(line,chC2,y-1+i*10));
        doc.setFontSize(8); doc.setTextColor('#8aadcc');
        doc.text(String(c.relevantCount),chC3,y-1);
        doc.text(String(c.scoredCount),chC4,y-1);
        doc.setTextColor(valCol);
        doc.text(pctVal!==null?`${pctVal}%`:'—',chC5,y-1);
        doc.setFontSize(7);
        doc.text(pctVal===null?'UNSCORED':pass?'PASS':'FAIL',chC6,y-1,{align:'right'});
        y+=chRowH+2;
      });

      // ── PAGE 3+: WEAK OEs GROUPED BY CHAPTER ───────────────────────────
      newPage(); y=50;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Gap Analysis — Weak OEs (Score ≤3)',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=18;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`${weakOEs.length} OE(s) scoring ≤3 require attention. Grouped by chapter.`,60,y); y+=20;

      if(weakOEs.length===0){
        doc.setFontSize(12); doc.setTextColor('#4caf7d');
        doc.text('✓ No weak OEs — all scored OEs are at 4 or 5.',W/2,y+40,{align:'center'});
      } else {
        // Column layout (content area = 60..535, width=475)
        // OE Code 12%=57, Level 10%=47, OE Text 58%=276, Score 20%=95
        const cX1=64, cX2=121, cX3=172, cX4=452; // left x of each col
        const textColW=276; // OE text column width for wrapping
        const rowPad=5;

        const drawGapColHeaders=()=>{
          doc.setFillColor('#081525'); doc.rect(60,y-11,W-120,16,'F');
          doc.setFontSize(7); doc.setTextColor('#c9a84c');
          doc.text('OE CODE',cX1,y-2);
          doc.text('LEVEL',cX2,y-2);
          doc.text('OE TEXT',cX3,y-2);
          doc.text('SCORE',W-64,y-2,{align:'right'});
          y+=14;
        };

        SHCO_CHAPTERS.forEach(ch=>{
          const chWeak = weakOEs.filter(oe=>oe.chapter===ch.key);
          if(chWeak.length===0) return;

          if(y>H-80){ newPage(); y=50; }
          // Chapter header band
          doc.setFillColor('#0c1e30');
          doc.rect(60,y-12,W-120,20,'F');
          doc.setFontSize(10); doc.setTextColor('#c9a84c');
          doc.text(`${ch.key} — ${ch.name}`,74,y-1);
          doc.setFontSize(8); doc.setTextColor('#3a5870');
          doc.text(`${chWeak.length} weak OE(s)`,W-64,y-1,{align:'right'});
          y+=22;

          drawGapColHeaders();

          chWeak.forEach(oe=>{
            const sc      = shcoFullScores[oe.oe_code]||0;
            const scC     = scoreCol(sc);
            const rowBg   = sc<=2 ? '#180606' : '#140e00';
            // Pre-compute wrapped text to know row height
            doc.setFontSize(7.5);
            const wrapped = doc.splitTextToSize(oe.text||'', textColW);
            const lineH   = 9;
            const rowH    = Math.max(18, wrapped.length * lineH + rowPad*2);

            if(y+rowH>H-40){
              newPage(); y=50;
              drawGapColHeaders();
            }

            doc.setFillColor(rowBg); doc.rect(60,y-rowPad,W-120,rowH,'F');

            // OE Code
            doc.setFontSize(8); doc.setTextColor('#4fc3f7');
            doc.text((oe.oe_code||''),cX1,y+2);
            // Level
            doc.setFontSize(7); doc.setTextColor('#8aadcc');
            doc.text((oe.level||'').slice(0,12),cX2,y+2);
            // OE Text — all wrapped lines, clipped to col width
            doc.setFontSize(7.5); doc.setTextColor('#c8dcea');
            wrapped.forEach((line,i)=>{ doc.text(line,cX3,y+2+i*lineH); });
            // Score — right-aligned in score col
            doc.setFontSize(8); doc.setTextColor(scC);
            doc.text(`${sc}/5`,W-64,y+2,{align:'right'});
            doc.setFontSize(7); doc.setTextColor(scC);
            doc.text((scoreLabel[sc]||'').slice(0,16),W-64,y+2+lineH,{align:'right'});

            y+=rowH+2;
          });
          y+=8;
        });
      }

      // ── PAGE: CORRECTIVE ACTIONS (CAPAs) ────────────────────────────────
      const capaEntries = weakOEs
        .map(oe=>({oe, capa:shcoFullCapaDb[oe.oe_code]}))
        .filter(({capa})=>capa&&capa.finding);

      if(capaEntries.length>0){
        newPage(); y=50;
        doc.setFontSize(16); doc.setTextColor('#eef4f9');
        doc.text('Corrective Actions (CAPA)',60,y); y+=10;
        doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=18;
        doc.setFontSize(8); doc.setTextColor('#3a5870');
        doc.text(`${capaEntries.length} CAPA(s) recorded for weak OEs`,60,y); y+=20;

        capaEntries.forEach(({oe,capa})=>{
          const sc  = shcoFullScores[oe.oe_code]||0;
          const scC = scoreCol(sc);

          // Estimate height needed
          doc.setFontSize(8);
          const findLines  = doc.splitTextToSize(capa.finding||'',W-180);
          const actionLines= doc.splitTextToSize(capa.action_planned||'',W-180);
          const estH = 14+findLines.length*10+actionLines.length*10+28+16;
          if(y+estH>H-40){ newPage(); y=50; }

          // Card background
          doc.setFillColor('#0a1a2a');
          doc.roundedRect(60,y-4,W-120,estH,3,3,'F');
          doc.setDrawColor('#1a3550');
          doc.roundedRect(60,y-4,W-120,estH,3,3,'S');

          // OE header
          doc.setFontSize(9); doc.setTextColor('#4fc3f7');
          doc.text(oe.oe_code,68,y+8);
          doc.setFontSize(8); doc.setTextColor('#8aadcc');
          doc.text(oe.level,130,y+8);
          doc.setFontSize(8); doc.setTextColor(scC);
          doc.text(`Score: ${sc}/5`,W-64,y+8,{align:'right'});
          y+=18;

          // Finding
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('FINDING',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          findLines.forEach((line,i)=>doc.text(line,68,y+9+i*10));
          y+=9+findLines.length*10+4;

          // Action
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('ACTION PLANNED',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          actionLines.forEach((line,i)=>doc.text(line,68,y+9+i*10));
          y+=9+actionLines.length*10+4;

          // Person + date
          const person = capa.responsible_person||'—';
          const dateStr2= capa.target_date ? new Date(capa.target_date).toLocaleDateString('en-IN',{day:'2-digit',month:'short',year:'numeric'}) : '—';
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text(`RESPONSIBLE: `,68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text(person,68+doc.getTextWidth('RESPONSIBLE: '),y);
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text(`TARGET DATE: `,W/2,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text(dateStr2,W/2+doc.getTextWidth('TARGET DATE: '),y);
          y+=18;
        });
      }

      // ── PAGE: SUMMARY ───────────────────────────────────────────────────
      newPage(); y=60;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Report Summary',60,y); y+=36;

      const summaryRows=[
        ['Assessment Type',    assessTypeLabel,                              '#c9a84c'],
        ['Total OEs in Scope', String(relevantOEs.length),                   '#eef4f9'],
        ['OEs Scored',         `${scoredCount} of ${relevantOEs.length}`,    '#4caf7d'],
        ['OEs Unscored',       String(relevantOEs.length-scoredCount),       scoredCount===relevantOEs.length?'#4caf7d':'#f4a441'],
        ['Weak OEs (≤3)',       String(weakOEs.length),                       weakOEs.length===0?'#4caf7d':'#f4a441'],
        ['Critical (Core <4)', String(criticalOEs.length),                   criticalOEs.length===0?'#4caf7d':'#e05a5a'],
        ['Core+Commit Compliance', `${ccPct}%`,                              ccPct>=80?'#4caf7d':'#e05a5a'],
        ['Overall Verdict',    verdictText,                                  allRulesPass?'#4caf7d':'#e05a5a'],
      ];

      summaryRows.forEach(([lbl,val,col])=>{
        if(y>H-60){ newPage(); y=60; }
        doc.setFillColor('#081525'); doc.roundedRect(60,y-15,W-120,28,3,3,'F');
        doc.setFontSize(10); doc.setTextColor('#c8dcea');
        doc.text(lbl,80,y-1);
        doc.setFontSize(11); doc.setTextColor(col);
        doc.text(val,W-80,y-1,{align:'right'});
        y+=36;
      });

      y+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=22;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`Report generated on ${dateStr} via accredready.in`,W/2,y,{align:'center'}); y+=16;
      doc.text('This report is based on self-assessment scores entered by the hospital team.',W/2,y,{align:'center'}); y+=13;
      doc.text('It is not an official NABH assessment and must not replace a formal NABH evaluation.',W/2,y,{align:'center'});

      // Page numbers
      const nPages = doc.internal.getNumberOfPages();
      for(let i=1;i<=nPages;i++){
        doc.setPage(i);
        doc.setFontSize(7); doc.setTextColor('#3a5870');
        doc.text(`Page ${i} of ${nPages}`,W-60,H-18,{align:'right'});
        if(i>1) doc.text('NABH SHCO Gap Report · accredready.in',60,H-18);
      }

      const cleanName = cleanHospital.replace(/[^a-zA-Z0-9]/g,'_');
      doc.save(`${cleanName}_SHCO_Gap_Report_${fileDateStr}.pdf`);
    } catch(e){ console.error('SHCO Full PDF generation failed:',e); }
    setShcoFullPdfLoading(false);
  };

  const generateEcoFullPDF = async () => {
    setEcoFullPdfLoading(true);
    try {
      let localOes = ecoFullOes;
      let localScores = ecoFullScores;
      let localCapa = ecoFullCapaDb;
      if(localOes.length===0){
        const [{data:oeD},{data:scD}]=await Promise.all([
          supabase.from("eco_full_oes").select("*").order("oe_code"),
          supabase.from("eco_full_scores").select("oe_code,score").eq("hospital_id",context.hospitalId),
        ]);
        if(oeD) localOes=oeD;
        if(scD){const m={};scD.forEach(s=>{m[s.oe_code]=s.score;});localScores=m;}
        const {data:capD}=await supabase.from("eco_full_capa").select("*").eq("hospital_id",context.hospitalId);
        if(capD){const m={};capD.forEach(c=>{m[c.oe_code]=c;});localCapa=m;}
      }
      const doc = new jsPDF({ unit:'pt', format:'a4' });
      const W = doc.internal.pageSize.getWidth();
      const H = doc.internal.pageSize.getHeight();
      const today = new Date();
      const dateStr = today.toLocaleDateString('en-IN',{day:'2-digit',month:'long',year:'numeric'});
      const fileDateStr = String(today.getDate()).padStart(2,'0')+String(today.getMonth()+1).padStart(2,'0')+today.getFullYear();
      const cleanHospital = (context?.hospitalName||'Organisation').replace(/\s+(New|Trial|Active|Expired)$/i,'').trim();
      const assessTypeLabel = ecoFullAssessType==='final' ? 'Final Assessment'
                            : ecoFullAssessType==='surveillance' ? 'Surveillance Assessment'
                            : 'Re-accreditation Assessment';

      // Derive chapters from loaded OE data
      const ecoChapterKeys = [...new Set(localOes.map(oe=>oe.chapter))].filter(Boolean).sort();
      const ECO_CHAPTERS = ecoChapterKeys.map(key=>{
        const chOe = localOes.find(oe=>oe.chapter===key);
        return {key, name: chOe?.chapter_name || key};
      });

      const coreCommOEs = localOes.filter(oe=>oe.category==='core'||oe.category==='commitment');
      const achieveOEs  = localOes.filter(oe=>oe.category==='achievement');
      const excelOEs    = localOes.filter(oe=>oe.category==='excellence');
      const coreOEs     = localOes.filter(oe=>oe.category==='core');
      const relevantOEs = ecoFullAssessType==='final'        ? coreCommOEs
                        : ecoFullAssessType==='surveillance' ? localOes.filter(oe=>oe.category!=='excellence')
                        : localOes;

      const compliance = arr => arr.length>0
        ? Math.round(arr.reduce((a,oe)=>a+(localScores[oe.oe_code]||0),0)/(arr.length*5)*100) : 0;

      const ccPct    = compliance(coreCommOEs);
      const achPct   = compliance(achieveOEs);
      const excelPct = compliance(excelOEs);

      const chStats = ECO_CHAPTERS.map(c=>{
        const chOes    = relevantOEs.filter(oe=>oe.chapter===c.key);
        const chScored = chOes.filter(oe=>localScores[oe.oe_code]);
        const chSum    = chScored.reduce((a,oe)=>a+localScores[oe.oe_code],0);
        const chAvg    = chScored.length>0 ? chSum/chScored.length : null;
        const totalCount = localOes.filter(oe=>oe.chapter===c.key).length;
        const pct = chScored.length>0 ? Math.round(chSum/(chOes.length*5)*100) : null;
        return {...c, relevantCount:chOes.length, totalCount, scoredCount:chScored.length, avg:chAvg, pct };
      });

      const maxLowPerStd = ecoFullAssessType==='renewal' ? 0 : 1;
      const stdMap={};
      relevantOEs.forEach(oe=>{
        const sk=oe.standard_code||(oe.oe_code?oe.oe_code.replace(/\.[^.]+$/,''):oe.chapter||'Other');
        if(!stdMap[sk])stdMap[sk]={oes:[]};
        stdMap[sk].oes.push(oe);
      });
      const stdChecks = Object.entries(stdMap).map(([code,{oes}])=>{
        const scored = oes.filter(oe=>localScores[oe.oe_code]);
        const avg    = scored.length>0 ? scored.reduce((a,oe)=>a+localScores[oe.oe_code],0)/scored.length : null;
        const atOrBelow2 = oes.filter(oe=>localScores[oe.oe_code]&&localScores[oe.oe_code]<=2).length;
        return {code,avg,atOrBelow2};
      });
      const chapAvgFails = chStats.filter(c=>c.avg!==null&&c.avg<4);
      const corePass  = coreOEs.every(oe=>localScores[oe.oe_code]&&localScores[oe.oe_code]>=4);
      const rule1Pass = corePass;
      const rule2Pass = ccPct>=80;
      const rule3Pass = stdChecks.every(s=>s.atOrBelow2<=maxLowPerStd);
      const rule4Pass = stdChecks.every(s=>s.avg===null||s.avg>=4);
      const rule5Pass = chapAvgFails.length===0;
      const allRulesPass = rule1Pass&&rule2Pass&&rule3Pass&&rule4Pass&&rule5Pass;

      const rules = [
        {label:'All Core OEs must score >=4',            detail:`${coreOEs.length} Core OEs — every one must reach Good compliance`,       pass:rule1Pass},
        {label:`Core + Commitment overall >=80% (${coreCommOEs.length} OEs)`, detail:`Current: ${ccPct}% — threshold: 80%`,                  pass:rule2Pass},
        {label:'No standard with >'+maxLowPerStd+' OE(s) scored <=2', detail:`${stdChecks.filter(s=>s.atOrBelow2>maxLowPerStd).length} standard(s) failing this rule`, pass:rule3Pass},
        {label:'Average score per standard >=4',         detail:`${stdChecks.filter(s=>s.avg!==null&&s.avg<4).length} standard(s) below 4 average`,                     pass:rule4Pass},
        {label:'Average score per chapter >=4',          detail:`${chapAvgFails.length} chapter(s) below 4 average`,                         pass:rule5Pass},
      ];
      if(ecoFullAssessType==='surveillance'||ecoFullAssessType==='renewal'){
        rules.push({label:`Achievement overall >=80% (${achieveOEs.length} OEs)`, detail:`Current: ${achPct}%`, pass:achPct>=80});
      }
      if(ecoFullAssessType==='renewal'){
        rules.push({label:`Excellence overall >=80% (${excelOEs.length} OEs)`, detail:`Current: ${excelPct}%`, pass:excelPct>=80});
      }

      const weakOEs = relevantOEs.filter(oe=>localScores[oe.oe_code]&&localScores[oe.oe_code]<=3)
        .sort((a,b)=>localScores[a.oe_code]-localScores[b.oe_code]||a.oe_code.localeCompare(b.oe_code));
      const criticalOEs = coreOEs.filter(oe=>localScores[oe.oe_code]&&localScores[oe.oe_code]<4);
      const scoredCount = relevantOEs.filter(oe=>localScores[oe.oe_code]).length;

      const scoreLabel = ['','No compliance','Poor compliance','Partial compliance','Good compliance','Full compliance'];
      const scoreCol   = s => s===1||s===2 ? '#e05a5a' : s===3 ? '#f4a441' : s>=4 ? '#4caf7d' : '#3a5870';

      const newPage = () => {
        doc.addPage();
        doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
        doc.setFillColor('#06b6d4'); doc.rect(0,0,W,4,'F');
      };

      // PAGE 1: COVER
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor('#06b6d4'); doc.rect(0,0,W,6,'F');

      doc.setFontSize(9); doc.setTextColor('#06b6d4');
      doc.text('ACCREDREADY · NABH ECO FULL ACCREDITATION',W/2,58,{align:'center'});
      doc.setFontSize(27); doc.setTextColor('#eef4f9');
      doc.text('NABH ECO Gap Assessment Report',W/2,106,{align:'center'});
      doc.setDrawColor('#06b6d4'); doc.setLineWidth(0.5);
      doc.line(60,124,W-60,124);

      doc.setFontSize(22); doc.setTextColor('#06b6d4');
      const hospLines = doc.splitTextToSize(cleanHospital, W-160);
      doc.text(hospLines, W/2, 160, {align:'center'});
      const afterHosp = 160 + (hospLines.length-1)*28;
      doc.setFontSize(11); doc.setTextColor('#c8dcea');
      doc.text(assessTypeLabel, W/2, afterHosp+26, {align:'center'});
      doc.setFontSize(9); doc.setTextColor('#3a5870');
      doc.text(`Generated on ${dateStr}`, W/2, afterHosp+44, {align:'center'});

      const oePct = ccPct;
      const passCol  = oePct>=80 ? '#4caf7d' : oePct>=60 ? '#f4a441' : '#e05a5a';
      const verdictText = allRulesPass ? 'ACCREDITATION READY' : oePct>=80 ? 'RULES INCOMPLETE' : 'NOT READY';

      doc.setFontSize(72); doc.setTextColor(passCol);
      doc.text(`${oePct}%`,W/2, afterHosp+148,{align:'center'});
      doc.setFontSize(11); doc.setTextColor('#c8dcea');
      doc.text('CORE + COMMITMENT COMPLIANCE',W/2, afterHosp+172,{align:'center'});
      doc.setFontSize(7.5); doc.setTextColor('#3a5870');
      doc.text('Based on all relevant OEs; unscored OEs count as 0.',W/2, afterHosp+186,{align:'center'});
      doc.setFontSize(20); doc.setTextColor(passCol);
      doc.text(`VERDICT: ${verdictText}`,W/2, afterHosp+208,{align:'center'});

      const statY = afterHosp+248;
      const stats3=[
        [`${scoredCount} / ${relevantOEs.length}`, 'Relevant OEs Scored'],
        [`${weakOEs.length}`,                       'Weak OEs (score <=3)'],
        [`${criticalOEs.length}`,                   'Core OEs below 4'],
      ];
      const colW=(W-120)/3;
      stats3.forEach(([val,lbl],i)=>{
        const cx=60+colW*i+colW/2;
        doc.setFillColor('#081525'); doc.roundedRect(60+colW*i+4, statY-20, colW-8, 46, 4,4,'F');
        doc.setFontSize(22); doc.setTextColor('#06b6d4');
        doc.text(val, cx, statY+4, {align:'center'});
        doc.setFontSize(8); doc.setTextColor('#3a5870');
        doc.text(lbl, cx, statY+20, {align:'center'});
      });

      doc.setFontSize(7); doc.setTextColor('#3a5870');
      doc.text('Generated by accredready.in — Independent educational tool — Not affiliated with NABH/QCI',W/2,H-28,{align:'center'});

      // PAGE 2: ACCREDITATION RULES
      newPage();
      let y=50;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Accreditation Rules',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.setLineWidth(0.5);
      doc.line(60,y,W-60,y); y+=24;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`ASSESSMENT TYPE: ${assessTypeLabel.toUpperCase()} · ${rules.filter(r=>r.pass).length} of ${rules.length} RULES PASSING`,60,y); y+=18;

      rules.forEach(r=>{
        if(y>H-60){ newPage(); y=50; }
        doc.setFillColor(r.pass?'#061810':'#180606');
        doc.roundedRect(60,y-14,W-120,32,3,3,'F');
        doc.setFillColor(r.pass?'#4caf7d':'#e05a5a');
        doc.roundedRect(W-106,y-7,40,16,3,3,'F');
        doc.setFontSize(8); doc.setTextColor('#050e1a');
        doc.text(r.pass?'PASS':'FAIL',W-86,y+3,{align:'center'});
        doc.setFontSize(10); doc.setTextColor('#eef4f9');
        doc.text(r.label,76,y-2);
        doc.setFontSize(8); doc.setTextColor('#8aadcc');
        doc.text(r.detail,76,y+11);
        y+=40;
      });

      // CHAPTER-WISE TABLE
      y+=16;
      if(y>H-220){ newPage(); y=50; }
      doc.setFontSize(14); doc.setTextColor('#eef4f9');
      doc.text('Chapter-wise Compliance',60,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=20;

      const chC1=64,chC2=108,chC3=312,chC4=368,chC5=424,chC6=530;
      doc.setFillColor('#081525'); doc.rect(60,y-13,W-120,20,'F');
      doc.setFontSize(8); doc.setTextColor('#06b6d4');
      doc.text('CH',chC1,y-2);
      doc.text('CHAPTER NAME',chC2,y-2);
      doc.text('RELEV.',chC3,y-2);
      doc.text('SCORED',chC4,y-2);
      doc.text('COMPLIANCE',chC5,y-2);
      doc.text('STATUS',chC6,y-2,{align:'right'});
      y+=14;

      chStats.forEach(c=>{
        if(y>H-40){ newPage(); y=50; }
        const pctVal = c.pct!==null ? c.pct : null;
        const pass   = pctVal!==null&&pctVal>=80;
        const rowBg  = pctVal===null ? '#0a1520' : pass ? '#061810' : pctVal>=60 ? '#14100a' : '#180606';
        const valCol = pctVal===null ? '#3a5870' : pass ? '#4caf7d' : pctVal>=60 ? '#f4a441' : '#e05a5a';
        doc.setFontSize(8);
        const nameLines = doc.splitTextToSize(c.name, 200);
        const chRowH = Math.max(20, nameLines.length*10+6);
        doc.setFillColor(rowBg); doc.rect(60,y-12,W-120,chRowH,'F');
        doc.setFontSize(9); doc.setTextColor('#06b6d4');
        doc.text(c.key,chC1,y-1);
        doc.setFontSize(8); doc.setTextColor('#c8dcea');
        nameLines.forEach((line,i)=>doc.text(line,chC2,y-1+i*10));
        doc.setFontSize(8); doc.setTextColor('#8aadcc');
        doc.text(String(c.relevantCount),chC3,y-1);
        doc.text(String(c.scoredCount),chC4,y-1);
        doc.setTextColor(valCol);
        doc.text(pctVal!==null?`${pctVal}%`:'—',chC5,y-1);
        doc.setFontSize(7);
        doc.text(pctVal===null?'UNSCORED':pass?'PASS':'FAIL',chC6,y-1,{align:'right'});
        y+=chRowH+2;
      });

      y+=14;
      if(y>H-60){ newPage(); y=50; }
      doc.setFont('helvetica','italic');
      doc.setFontSize(7); doc.setTextColor('#3a5870');
      const fnoteLines=doc.splitTextToSize('Compliance % = (sum of all OE scores in chapter) / (total relevant OEs in chapter x 5) x 100. Unscored OEs count as 0. A low % may simply mean most OEs are not yet scored.',W-120);
      fnoteLines.forEach((ln,i)=>doc.text(ln,60,y+i*9));
      y+=fnoteLines.length*9+6;
      doc.setFont('helvetica','normal');

      // PAGE 3+: WEAK OEs
      newPage(); y=50;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Gap Analysis — Weak OEs (Score <=3)',40,y); y+=10;
      doc.setDrawColor('#0f2640'); doc.line(40,y,W-40,y); y+=18;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`${weakOEs.length} OE(s) scoring <=3 require attention. Grouped by chapter.`,40,y); y+=20;

      if(weakOEs.length===0){
        doc.setFontSize(12); doc.setTextColor('#4caf7d');
        doc.text('✓ No weak OEs — all scored OEs are at 4 or 5.',W/2,y+40,{align:'center'});
      } else {
        const cX1=44, cX2=104, cX3=174;
        const textColW=220;
        const rowPad=5;

        const drawGapColHeaders=()=>{
          doc.setFillColor('#081525'); doc.rect(40,y-11,W-80,16,'F');
          doc.setFontSize(7); doc.setTextColor('#06b6d4');
          doc.text('OE CODE',cX1,y-2);
          doc.text('LEVEL',cX2,y-2);
          doc.text('OE TEXT',cX3,y-2);
          doc.text('SCORE',W-44,y-2,{align:'right'});
          y+=14;
        };

        ECO_CHAPTERS.forEach(ch=>{
          const chWeak = weakOEs.filter(oe=>oe.chapter===ch.key);
          if(chWeak.length===0) return;

          if(y>H-80){ newPage(); y=50; }
          doc.setFillColor('#0c1e30');
          doc.rect(40,y-12,W-80,20,'F');
          doc.setFontSize(10); doc.setTextColor('#06b6d4');
          doc.text(`${ch.key} — ${ch.name}`,54,y-1);
          doc.setFontSize(8); doc.setTextColor('#3a5870');
          doc.text(`${chWeak.length} weak OE(s)`,W-44,y-1,{align:'right'});
          y+=22;

          drawGapColHeaders();

          chWeak.forEach(oe=>{
            const sc      = localScores[oe.oe_code]||0;
            const scC     = scoreCol(sc);
            const rowBg   = sc<=2 ? '#180606' : '#140e00';
            doc.setFontSize(7.5);
            const oeText=(oe.oe_text||'').replace(/\uFB00/g,'ff').replace(/\uFB01/g,'fi').replace(/\uFB02/g,'fl').replace(/\uFB03/g,'ffi').replace(/\uFB04/g,'ffl').replace(/\uFB05/g,'st').replace(/\uFB06/g,'st').replace(/\u2018/g,"'").replace(/\u2019/g,"'").replace(/\u201C/g,'"').replace(/\u201D/g,'"').replace(/\u2013/g,'-').replace(/\u2014/g,'--').replace(/[^\x20-\x7E\xA0-\xFF]/g,'');
            const wrapped = doc.splitTextToSize(oeText, textColW);
            const lineH=9; const rowH=Math.max(20, wrapped.length*lineH+rowPad*2);

            if(y+rowH>H-40){ newPage(); y=50; drawGapColHeaders(); }

            doc.setFillColor(rowBg); doc.rect(40,y-rowPad,W-80,rowH,'F');
            doc.setFontSize(8); doc.setTextColor('#4fc3f7');
            doc.text((oe.oe_code||''),cX1,y+2);
            doc.setFontSize(7); doc.setTextColor('#8aadcc');
            doc.text((oe.category||'').slice(0,12),cX2,y+2);
            doc.setFontSize(7.5); doc.setTextColor('#c8dcea');
            doc.setCharSpace(0);
            wrapped.forEach((line,i)=>{ doc.text(line,cX3,y+2+i*lineH); });
            doc.setFontSize(8); doc.setTextColor(scC);
            doc.text(`${sc}/5`,W-44,y+2,{align:'right'});
            doc.setFontSize(7); doc.setTextColor(scC);
            doc.text((scoreLabel[sc]||'').slice(0,16),W-44,y+2+lineH,{align:'right'});
            y+=rowH+6;
          });
          y+=8;
        });
      }

      // CAPA PAGE
      const capaEntries = weakOEs
        .map(oe=>({oe, capa:localCapa[oe.oe_code]}))
        .filter(({capa})=>capa&&capa.finding);

      if(capaEntries.length>0){
        newPage(); y=50;
        doc.setFontSize(16); doc.setTextColor('#eef4f9');
        doc.text('Corrective Actions (CAPA)',60,y); y+=10;
        doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=18;
        doc.setFontSize(8); doc.setTextColor('#3a5870');
        doc.text(`${capaEntries.length} CAPA(s) recorded for weak OEs`,60,y); y+=20;

        capaEntries.forEach(({oe,capa})=>{
          const sc  = localScores[oe.oe_code]||0;
          const scC = scoreCol(sc);
          doc.setFontSize(8);
          const findLines  = doc.splitTextToSize(capa.finding||'',W-180);
          const actionLines= doc.splitTextToSize(capa.action_planned||'',W-180);
          const estH = 14+findLines.length*10+actionLines.length*10+28+16;
          if(y+estH>H-40){ newPage(); y=50; }
          doc.setFillColor('#0a1a2a');
          doc.roundedRect(60,y-4,W-120,estH,3,3,'F');
          doc.setDrawColor('#1a3550');
          doc.roundedRect(60,y-4,W-120,estH,3,3,'S');
          doc.setFontSize(9); doc.setTextColor('#4fc3f7');
          doc.text(oe.oe_code,68,y+8);
          doc.setFontSize(8); doc.setTextColor('#8aadcc');
          doc.text(oe.category||'',130,y+8);
          doc.setFontSize(8); doc.setTextColor(scC);
          doc.text(`Score: ${sc}/5`,W-64,y+8,{align:'right'});
          y+=18;
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('FINDING',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          findLines.forEach((line,i)=>doc.text(line,68,y+9+i*10));
          y+=9+findLines.length*10+4;
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('ACTION PLANNED',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          actionLines.forEach((line,i)=>doc.text(line,68,y+9+i*10));
          y+=9+actionLines.length*10+4;
          const person = capa.responsible_person||'—';
          const dateStr2= capa.target_date ? new Date(capa.target_date).toLocaleDateString('en-IN',{day:'2-digit',month:'short',year:'numeric'}) : '—';
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('RESPONSIBLE: ',68,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text(person,68+doc.getTextWidth('RESPONSIBLE: '),y);
          doc.setFontSize(7); doc.setTextColor('#3a5870');
          doc.text('TARGET DATE: ',W/2,y);
          doc.setFontSize(8); doc.setTextColor('#c8dcea');
          doc.text(dateStr2,W/2+doc.getTextWidth('TARGET DATE: '),y);
          y+=18;
        });
      }

      // SUMMARY PAGE
      newPage(); y=60;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Report Summary',60,y); y+=36;

      const summaryRows=[
        ['Assessment Type',    assessTypeLabel,                              '#06b6d4'],
        ['Total OEs in Scope', String(relevantOEs.length),                   '#eef4f9'],
        ['OEs Scored',         `${scoredCount} of ${relevantOEs.length}`,    '#4caf7d'],
        ['OEs Unscored',       String(relevantOEs.length-scoredCount),       scoredCount===relevantOEs.length?'#4caf7d':'#f4a441'],
        ['Weak OEs (<=3)',       String(weakOEs.length),                       weakOEs.length===0?'#4caf7d':'#f4a441'],
        ['Critical (Core <4)', String(criticalOEs.length),                   criticalOEs.length===0?'#4caf7d':'#e05a5a'],
        ['Core+Commit Compliance', `${ccPct}%`,                              ccPct>=80?'#4caf7d':'#e05a5a'],
        ['Overall Verdict',    verdictText,                                  allRulesPass?'#4caf7d':'#e05a5a'],
      ];

      summaryRows.forEach(([lbl,val,col])=>{
        if(y>H-60){ newPage(); y=60; }
        doc.setFillColor('#081525'); doc.roundedRect(60,y-15,W-120,28,3,3,'F');
        doc.setFontSize(10); doc.setTextColor('#c8dcea');
        doc.text(lbl,80,y-1);
        doc.setFontSize(11); doc.setTextColor(col);
        doc.text(val,W-80,y-1,{align:'right'});
        y+=36;
      });

      y+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=22;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`Report generated on ${dateStr} via accredready.in`,W/2,y,{align:'center'}); y+=16;
      doc.text('This report is based on self-assessment scores entered by the organisation team.',W/2,y,{align:'center'}); y+=13;
      doc.text('It is not an official NABH assessment and must not replace a formal NABH evaluation.',W/2,y,{align:'center'});

      const nPages = doc.internal.getNumberOfPages();
      for(let i=1;i<=nPages;i++){
        doc.setPage(i);
        doc.setFontSize(7); doc.setTextColor('#3a5870');
        doc.text(`Page ${i} of ${nPages}`,W-60,H-18,{align:'right'});
      }

      const cleanName = cleanHospital.replace(/[^a-zA-Z0-9]/g,'_');
      doc.save(`${cleanName}_ECO_Gap_Report_${fileDateStr}.pdf`);
    } catch(e){ console.error('ECO Full PDF generation failed:',e); }
    finally{ setEcoFullPdfLoading(false); }
  };

  const generateElcPDF = async () => {
    setElcPdfLoading(true);
    try {
      const SEV_ORDER  = {CRITICAL:0, HIGH:1, MEDIUM:2, LOW:3};
      const SEV_COLORS = {CRITICAL:'#e05a5a', HIGH:'#f4a441', MEDIUM:'#c9a84c', LOW:'#3a5870'};
      const getSevC  = sev => SEV_COLORS[sev]||'#3a5870';
      const lvlColor = lvl => lvl==='CORE'?'#e05a5a':lvl==='Commitment'?'#f4a441':'#c9a84c';
      const dotCode  = code => code.replace(/^([A-Z]+)(\d+)([a-z]+)$/, '$1.$2.$3');
      const sanitize = str => (str||'').replace(/ﬀ/g,'ff').replace(/ﬁ/g,'fi').replace(/ﬂ/g,'fl').replace(/ﬃ/g,'ffi').replace(/ﬄ/g,'ffl').replace(/‘/g,"'").replace(/’/g,"'").replace(/“/g,'"').replace(/”/g,'"').replace(/–/g,'-').replace(/—/g,'--').replace(/[^\x20-\x7E\xA0-\xFF]/g,'');

      const getElcSev = code => {
        const s   = elcScores[code];
        const lvl = hcoOeLevels[code];
        if (!s) return null;
        if (lvl==='CORE')       return s==='not_met'?'CRITICAL':s==='partial'?'HIGH':null;
        if (lvl==='Commitment') return s==='not_met'?'HIGH':s==='partial'?'MEDIUM':null;
        if (lvl==='Excellence') return s==='not_met'?'MEDIUM':s==='partial'?'LOW':null;
        return null;
      };

      const gaps = HCO_ELC_OE_LIST
        .map(oe => { const sev=getElcSev(oe.code); return sev?{oe_code:oe.code,oe_text:oe.text,level:hcoOeLevels[oe.code]||'',severity:sev}:null; })
        .filter(Boolean)
        .sort((a,b)=>(SEV_ORDER[a.severity]??9)-(SEV_ORDER[b.severity]??9));

      const capaEntries = gaps.filter(g=>elcCapaDb[g.oe_code]?.finding);
      const counts = {CRITICAL:0, HIGH:0, MEDIUM:0, LOW:0};
      gaps.forEach(g=>{ if(counts[g.severity]!==undefined) counts[g.severity]++; });

      const doc = new jsPDF({unit:'pt', format:'a4'});
      const W = doc.internal.pageSize.getWidth();
      const H = doc.internal.pageSize.getHeight();
      const today = new Date();
      const dateStr = today.toLocaleDateString('en-IN',{day:'2-digit',month:'long',year:'numeric'});
      const fileDateStr = String(today.getDate()).padStart(2,'0')+String(today.getMonth()+1).padStart(2,'0')+today.getFullYear();
      const cleanHospital = (context?.hospitalName||'Hospital').replace(/\s+(New|Trial|Active|Expired)$/i,'').trim();
      const GOLD = '#c9a84c';

      const newPage = () => {
        doc.addPage();
        doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
        doc.setFillColor(GOLD); doc.rect(0,0,W,4,'F');
      };

      // ── PAGE 1: COVER ──────────────────────────────────────────────────────
      doc.setFillColor('#050e1a'); doc.rect(0,0,W,H,'F');
      doc.setFillColor(GOLD); doc.rect(0,0,W,6,'F');

      doc.setFontSize(9);  doc.setTextColor(GOLD);
      doc.text('ACCREDREADY · NABH HCO ELC',W/2,58,{align:'center'});
      doc.setFontSize(27); doc.setTextColor('#eef4f9');
      doc.text('NABH HCO ELC Gap Report',W/2,106,{align:'center'});
      doc.setDrawColor(GOLD); doc.setLineWidth(0.5);
      doc.line(60,124,W-60,124);

      doc.setFontSize(22); doc.setTextColor(GOLD);
      const hospLines = doc.splitTextToSize(cleanHospital, W-160);
      doc.text(hospLines, W/2, 160, {align:'center'});
      const afterHosp = 160+(hospLines.length-1)*28;
      doc.setFontSize(9); doc.setTextColor('#3a5870');
      doc.text(`Generated on ${dateStr}`, W/2, afterHosp+30, {align:'center'});

      const tileY = afterHosp+80;
      const tileW = (W-120)/4;
      ['CRITICAL','HIGH','MEDIUM','LOW'].forEach((sev,i)=>{
        const col = getSevC(sev);
        const cx  = 60+tileW*i+tileW/2;
        doc.setFillColor('#081525'); doc.roundedRect(60+tileW*i+4, tileY-20, tileW-8, 50, 4,4,'F');
        doc.setFontSize(24); doc.setTextColor(col);
        doc.text(String(counts[sev]), cx, tileY+6,  {align:'center'});
        doc.setFontSize(8);  doc.setTextColor(col);
        doc.text(sev,          cx, tileY+22, {align:'center'});
      });

      doc.setFontSize(12); doc.setTextColor('#eef4f9');
      doc.text(`${gaps.length} total gap${gaps.length!==1?'s':''}`, W/2, tileY+56, {align:'center'});
      doc.setFontSize(10); doc.setTextColor('#3a5870');
      doc.text(`${capaEntries.length} CAPA${capaEntries.length!==1?'s':''} recorded`, W/2, tileY+74, {align:'center'});
      doc.setFontSize(7);  doc.setTextColor('#3a5870');
      doc.text('Generated by accredready.in — Independent educational tool — Not affiliated with NABH/QCI',W/2,H-28,{align:'center'});

      if(gaps.length===0){
        newPage();
        doc.setFontSize(18); doc.setTextColor('#4caf7d');
        doc.text('No gaps found', W/2, 230, {align:'center'});
        doc.setFontSize(10); doc.setTextColor('#3a5870');
        doc.text('All scored OEs are Met. Score more OEs in the OE Browser to see gaps here.',W/2,262,{align:'center',maxWidth:W-120});
      } else {
        // ── GAP LIST ──────────────────────────────────────────────────────────
        newPage(); let y=50;
        doc.setFontSize(16); doc.setTextColor('#eef4f9');
        doc.text('Gap Analysis',60,y); y+=10;
        doc.setDrawColor('#0f2640'); doc.setLineWidth(0.5);
        doc.line(60,y,W-60,y); y+=18;
        doc.setFontSize(8); doc.setTextColor('#3a5870');
        doc.text(`${gaps.length} OE(s) not yet Met — sorted by severity`,60,y); y+=20;

        const cX1=44, cX2=106, cX3=168, cX4=240;
        const textColW=240; const rowPad=5; const lineH=9;

        const drawGapHeader = () => {
          doc.setFillColor('#081525'); doc.rect(40,y-11,W-80,16,'F');
          doc.setFontSize(7); doc.setTextColor(GOLD);
          doc.text('OE CODE',cX1,y-2);
          doc.text('LEVEL',cX2,y-2);
          doc.text('SEVERITY',cX3,y-2);
          doc.text('OE TEXT',cX4,y-2);
          y+=14;
        };
        drawGapHeader();

        gaps.forEach(g=>{
          const sevC  = getSevC(g.severity);
          const lvlC  = lvlColor(g.level);
          const rowBg = g.severity==='CRITICAL'?'#180606':g.severity==='HIGH'?'#140e00':g.severity==='MEDIUM'?'#121208':'#0a1520';
          const wrapped = doc.splitTextToSize(sanitize(g.oe_text), textColW);
          const rowH    = Math.max(20, wrapped.length*lineH+rowPad*2);
          if(y+rowH>H-40){ newPage(); y=50; drawGapHeader(); }
          doc.setFillColor(rowBg); doc.rect(40,y-rowPad,W-80,rowH,'F');
          doc.setFontSize(8);   doc.setTextColor('#4fc3f7'); doc.text(dotCode(g.oe_code),cX1,y+2);
          doc.setFontSize(7);   doc.setTextColor(lvlC);      doc.text((g.level||'').slice(0,12),cX2,y+2);
          doc.setFontSize(7);   doc.setTextColor(sevC);      doc.text(g.severity,cX3,y+2);
          doc.setFontSize(7.5); doc.setTextColor('#c8dcea'); wrapped.forEach((ln,i)=>doc.text(ln,cX4,y+2+i*lineH));
          y+=rowH+6;
        });

        // ── CAPA PAGE ─────────────────────────────────────────────────────────
        if(capaEntries.length>0){
          newPage(); y=50;
          doc.setFontSize(16); doc.setTextColor('#eef4f9');
          doc.text('Corrective Actions (CAPA)',60,y); y+=10;
          doc.setDrawColor('#0f2640'); doc.line(60,y,W-60,y); y+=18;
          doc.setFontSize(8); doc.setTextColor('#3a5870');
          doc.text(`${capaEntries.length} CAPA${capaEntries.length!==1?'s':''} recorded for gap OEs`,60,y); y+=20;

          capaEntries.forEach(g=>{
            const capa      = elcCapaDb[g.oe_code];
            const sevC      = getSevC(g.severity);
            const findLines = doc.splitTextToSize(sanitize(capa.finding||''), W-180);
            const actLines  = doc.splitTextToSize(sanitize(capa.action_planned||''), W-180);
            const estH      = 14+findLines.length*10+actLines.length*10+28+16;
            if(y+estH>H-40){ newPage(); y=50; }
            doc.setFillColor('#0a1a2a');
            doc.roundedRect(60,y-4,W-120,estH,3,3,'F');
            doc.setDrawColor('#1a3550');
            doc.roundedRect(60,y-4,W-120,estH,3,3,'S');
            doc.setFontSize(9); doc.setTextColor('#4fc3f7');       doc.text(dotCode(g.oe_code),68,y+8);
            doc.setFontSize(8); doc.setTextColor(lvlColor(g.level)); doc.text(g.level||'',130,y+8);
            doc.setFontSize(8); doc.setTextColor(sevC);            doc.text(g.severity,W-64,y+8,{align:'right'});
            y+=18;
            doc.setFontSize(7); doc.setTextColor('#3a5870'); doc.text('FINDING',68,y);
            doc.setFontSize(8); doc.setTextColor('#c8dcea'); findLines.forEach((ln,i)=>doc.text(ln,68,y+9+i*10));
            y+=9+findLines.length*10+4;
            doc.setFontSize(7); doc.setTextColor('#3a5870'); doc.text('ACTION PLANNED',68,y);
            doc.setFontSize(8); doc.setTextColor('#c8dcea'); actLines.forEach((ln,i)=>doc.text(ln,68,y+9+i*10));
            y+=9+actLines.length*10+4;
            const person = capa.responsible_person||'—';
            const dStr2  = capa.target_date?new Date(capa.target_date).toLocaleDateString('en-IN',{day:'2-digit',month:'short',year:'numeric'}):'—';
            doc.setFontSize(7); doc.setTextColor('#3a5870'); doc.text('RESPONSIBLE: ',68,y);
            doc.setFontSize(8); doc.setTextColor('#c8dcea'); doc.text(person,68+doc.getTextWidth('RESPONSIBLE: '),y);
            doc.setFontSize(7); doc.setTextColor('#3a5870'); doc.text('TARGET DATE: ',W/2,y);
            doc.setFontSize(8); doc.setTextColor('#c8dcea'); doc.text(dStr2,W/2+doc.getTextWidth('TARGET DATE: '),y);
            y+=18;
          });
        }
      }

      // ── SUMMARY ───────────────────────────────────────────────────────────
      newPage(); let y2=60;
      doc.setFontSize(16); doc.setTextColor('#eef4f9');
      doc.text('Report Summary',60,y2); y2+=36;
      const scoredCt  = Object.keys(elcScores).length;
      const metCt     = Object.values(elcScores).filter(v=>v==='met').length;
      const partialCt = Object.values(elcScores).filter(v=>v==='partial').length;
      const notMetCt  = Object.values(elcScores).filter(v=>v==='not_met').length;
      [
        ['Programme',      'NABH HCO ELC 2nd Edition',    GOLD],
        ['Total OEs',      String(HCO_ELC_OE_LIST.length), '#eef4f9'],
        ['OEs Scored',     String(scoredCt),               scoredCt>0?'#4caf7d':'#f4a441'],
        ['Met',            String(metCt),                  metCt>0?'#4caf7d':'#3a5870'],
        ['Partial',        String(partialCt),              partialCt>0?'#f4a441':'#3a5870'],
        ['Not Met',        String(notMetCt),               notMetCt>0?'#e05a5a':'#3a5870'],
        ['Total Gaps',     String(gaps.length),            gaps.length===0?'#4caf7d':'#f4a441'],
        ['Critical Gaps',  String(counts.CRITICAL),        counts.CRITICAL===0?'#4caf7d':'#e05a5a'],
        ['High Gaps',      String(counts.HIGH),            counts.HIGH===0?'#4caf7d':'#f4a441'],
        ['CAPAs Recorded', String(capaEntries.length),     capaEntries.length>0?'#4caf7d':'#3a5870'],
      ].forEach(([lbl,val,col])=>{
        if(y2>H-60){ newPage(); y2=60; }
        doc.setFillColor('#081525'); doc.roundedRect(60,y2-15,W-120,28,3,3,'F');
        doc.setFontSize(10); doc.setTextColor('#c8dcea'); doc.text(lbl,80,y2-1);
        doc.setFontSize(11); doc.setTextColor(col);       doc.text(val,W-80,y2-1,{align:'right'});
        y2+=36;
      });
      y2+=10;
      doc.setDrawColor('#0f2640'); doc.line(60,y2,W-60,y2); y2+=22;
      doc.setFontSize(8); doc.setTextColor('#3a5870');
      doc.text(`Report generated on ${dateStr} via accredready.in`,W/2,y2,{align:'center'}); y2+=16;
      doc.text('This report is based on self-assessment scores entered by the hospital team.',W/2,y2,{align:'center'}); y2+=13;
      doc.text('It is not an official NABH assessment and must not replace a formal NABH evaluation.',W/2,y2,{align:'center'});

      const nPages = doc.internal.getNumberOfPages();
      for(let i=1;i<=nPages;i++){
        doc.setPage(i);
        doc.setFontSize(7); doc.setTextColor('#3a5870');
        doc.text(`Page ${i} of ${nPages}`,W-60,H-18,{align:'right'});
      }
      const cleanName = cleanHospital.replace(/[^a-zA-Z0-9]/g,'_');
      doc.save(`${cleanName}_HCO_ELC_Gap_Report_${fileDateStr}.pdf`);
    } catch(e){ console.error('ELC PDF generation failed:',e); }
    finally{ setElcPdfLoading(false); }
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
      else setAuthState("homepage");
    });
    const{data:{subscription}}=supabase.auth.onAuthStateChange((event,session)=>{
      if(event==="PASSWORD_RECOVERY"){
        if(session?.user)setUser(session.user);
        setAuthState("recovery");
        return;
      }
      if(session?.user){setUser(session.user);setAuthState(s=>s==="recovery"?s:s==="loading"?"setup":s);}
      else if(event==="INITIAL_SESSION"){setUser(null);setAuthState("homepage");setContext(null);}
      else{setUser(null);setAuthState("login");setContext(null);}
    });
    return()=>subscription.unsubscribe();
  },[]);

  // Show #resources-section only on the homepage
  useEffect(()=>{
    const rs=document.getElementById('resources-section');
    if(rs) rs.style.display=authState==="homepage"?"block":"none";
  },[authState]);

  // Back button: login screen (unauthenticated) → homepage
  useEffect(()=>{
    const onPop=()=>{ if(authState==="login"&&!user) setAuthState("homepage"); };
    window.addEventListener("popstate",onPop);
    return()=>window.removeEventListener("popstate",onPop);
  },[authState,user]);

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

  // Preload ELC oe_level badges — shared by both HCO and SHCO ELC (same unified 2nd Edition levels)
  useEffect(()=>{
    if(selectedProgramme!=="hco-elc"&&selectedProgramme!=="shco-elc")return;
    supabase.from("achieve_tips")
      .select("oe_code,oe_level")
      .eq("programme","ELC")
      .then(({data})=>{
        if(!data)return;
        const map={};
        data.forEach(r=>{ map[r.oe_code]=r.oe_level; });
        setHcoOeLevels(map);
      });
  },[selectedProgramme]);

  // Load existing HCO ELC scores for this hospital
  useEffect(()=>{
    if(selectedProgramme!=="hco-elc"||!context?.hospitalId)return;
    supabase.from("elc_scores")
      .select("oe_code,status")
      .eq("hospital_id",context.hospitalId)
      .eq("programme","HCO_ELC")
      .then(({data})=>{
        if(!data)return;
        const map={};
        data.forEach(r=>{ map[r.oe_code]=r.status; });
        setElcScores(map);
      });
  },[selectedProgramme,context?.hospitalId]);

  // Load HCO ELC CAPAs for this hospital
  useEffect(() => {
    if (selectedProgramme !== "hco-elc" || !context?.hospitalId) return;
    supabase.from("hco_elc_capa")
      .select("*")
      .eq("hospital_id", context.hospitalId)
      .then(({data}) => {
        if (!data) return;
        const m = {};
        data.forEach(r => { m[r.oe_code] = r; });
        setElcCapaDb(m);
      })
      .catch(() => {});
  }, [selectedProgramme, context?.hospitalId]); // eslint-disable-line

  const submitElcCapa = async (oeCode) => {
    const fc = elcCapaForm[oeCode];
    if (!fc?.finding || !fc?.action || !context?.hospitalId) return;
    setElcCapaSaving(p => ({...p, [oeCode]: true}));
    const {error} = await supabase.from("hco_elc_capa").upsert(
      {hospital_id: context.hospitalId, oe_code: oeCode,
       finding: fc.finding, root_cause: fc.root_cause || '',
       action_planned: fc.action, action_type: fc.action_type || 'Process',
       responsible_person: fc.person || '', target_date: fc.date || null,
       status: 'open'},
      {onConflict: "hospital_id,oe_code"}
    );
    setElcCapaSaving(p => ({...p, [oeCode]: false}));
    if (error) { alert("CAPA save failed: " + error.message); return; }
    const {data: fresh} = await supabase.from("hco_elc_capa")
      .select("*").eq("hospital_id", context.hospitalId);
    if (fresh) { const m = {}; fresh.forEach(r => { m[r.oe_code] = r; }); setElcCapaDb(m); }
    setElcCapaForm(p => ({...p, [oeCode]: {...p[oeCode], expanded: false}}));
  };

  const deleteElcCapa = async (oeCode) => {
    if (!window.confirm('Delete this CAPA entry?')) return;
    setElcCapaDeleting(p => ({...p, [oeCode]: true}));
    await supabase.from("hco_elc_capa").delete()
      .eq("hospital_id", context.hospitalId).eq("oe_code", oeCode);
    setElcCapaDb(p => { const n = {...p}; delete n[oeCode]; return n; });
    setElcCapaForm(p => { const n = {...p}; delete n[oeCode]; return n; });
    setElcCapaDeleting(p => ({...p, [oeCode]: false}));
  };

  // Load SHCO Full OEs + scores + CAPAs
  useEffect(()=>{
    if(selectedProgramme!=="shco-full"||!context?.hospitalId)return;
    setShcoFullLoading(true);
    Promise.all([
      supabase.from("shco_full_oes").select("*").order("oe_code"),
      supabase.from("shco_full_scores").select("oe_code,score").eq("hospital_id",context.hospitalId),
    ]).then(([{data:oeData},{data:scoreData}])=>{
      if(oeData)setShcoFullOes(oeData);
      if(scoreData){const m={};scoreData.forEach(s=>{m[s.oe_code]=s.score;});setShcoFullScores(m);}
      setShcoFullLoading(false);
    }).catch(()=>setShcoFullLoading(false));
    supabase.from("shco_full_capa").select("*").eq("hospital_id",context.hospitalId)
      .then(({data:capaData})=>{
        if(capaData){const m={};capaData.forEach(c=>{m[c.oe_code]=c;});setShcoFullCapaDb(m);}
      }).catch(()=>{});
  },[selectedProgramme,context?.hospitalId]);

  const saveShcoFullCapa = async (oeCode) => {
    const f = shcoFullCapaForm[oeCode];
    if(!f?.finding||!f?.action||!context?.hospitalId) return;
    setShcoFullCapaSaving(p=>({...p,[oeCode]:true}));
    await supabase.from("shco_full_capa").upsert({
      hospital_id:context.hospitalId, oe_code:oeCode,
      finding:f.finding, action_planned:f.action,
      responsible_person:f.person||'', target_date:f.date||null, status:'open',
    },{onConflict:"hospital_id,oe_code"});
    const {data:fresh}=await supabase.from("shco_full_capa").select("*").eq("hospital_id",context.hospitalId);
    if(fresh){const m={};fresh.forEach(c=>{m[c.oe_code]=c;});setShcoFullCapaDb(m);}
    setShcoFullCapaSaving(p=>({...p,[oeCode]:false}));
    setShcoFullCapaForm(p=>({...p,[oeCode]:{...p[oeCode],saved:true,expanded:false}}));
  };

  const deleteShcoFullCapa = async (oeCode) => {
    if(!window.confirm('Delete this CAPA? This cannot be undone.')) return;
    await supabase.from("shco_full_capa").delete()
      .eq("hospital_id",context.hospitalId).eq("oe_code",oeCode);
    setShcoFullCapaDb(p=>{const n={...p};delete n[oeCode];return n;});
    setShcoFullCapaForm(p=>{const n={...p};delete n[oeCode];return n;});
  };

  // Load ECO Full OEs + scores + CAPAs
  useEffect(()=>{
    if(selectedProgramme!=="eco-full"||!context?.hospitalId)return;
    setEcoFullLoading(true);
    // Load OEs and scores first — these tables always exist
    Promise.all([
      supabase.from("eco_full_oes").select("*").order("oe_code"),
      supabase.from("eco_full_scores").select("oe_code,score").eq("hospital_id",context.hospitalId),
    ]).then(([{data:oeData},{data:scoreData}])=>{
      if(oeData)setEcoFullOes(oeData);
      if(scoreData){const m={};scoreData.forEach(s=>{m[s.oe_code]=s.score;});setEcoFullScores(m);}
      setEcoFullLoading(false);
    }).catch(()=>setEcoFullLoading(false));
    // Load CAPAs independently — table may not exist yet
    supabase.from("eco_full_capa").select("*").eq("hospital_id",context.hospitalId)
      .then(({data:capaData})=>{
        if(capaData){const m={};capaData.forEach(c=>{m[c.oe_code]=c;});setEcoFullCapaDb(m);}
      }).catch(()=>{});
  },[selectedProgramme,context?.hospitalId,user?.id]);

  const saveEcoFullCapa = async (oeCode) => {
    const f = ecoFullCapaForm[oeCode];
    if(!f?.finding||!f?.action||!context?.hospitalId) return;
    setEcoFullCapaSaving(p=>({...p,[oeCode]:true}));
    const {error}=await supabase.from("eco_full_capa").upsert({
      hospital_id:context.hospitalId, oe_code:oeCode,
      finding:f.finding, action_planned:f.action,
      responsible_person:f.person||'', target_date:f.date||null, status:'open',
    },{onConflict:"hospital_id,oe_code"});
    setEcoFullCapaSaving(p=>({...p,[oeCode]:false}));
    if(error){alert("CAPA save failed: "+error.message);return;}
    const {data:fresh}=await supabase.from("eco_full_capa").select("*").eq("hospital_id",context.hospitalId);
    if(fresh){const m={};fresh.forEach(c=>{m[c.oe_code]=c;});setEcoFullCapaDb(m);}
    setEcoFullCapaForm(p=>({...p,[oeCode]:{...p[oeCode],saved:true,expanded:false}}));
  };

  const deleteEcoFullCapa = async (oeCode) => {
    if(!window.confirm('Delete this CAPA? This cannot be undone.')) return;
    await supabase.from("eco_full_capa").delete()
      .eq("hospital_id",context.hospitalId).eq("oe_code",oeCode);
    setEcoFullCapaDb(p=>{const n={...p};delete n[oeCode];return n;});
    setEcoFullCapaForm(p=>{const n={...p};delete n[oeCode];return n;});
  };

  // Load existing SHCO ELC scores for this hospital
  useEffect(()=>{
    if(selectedProgramme!=="shco-elc"||!context?.hospitalId)return;
    supabase.from("elc_scores")
      .select("oe_code,status")
      .eq("hospital_id",context.hospitalId)
      .eq("programme","SHCO_ELC")
      .then(({data})=>{
        if(!data)return;
        const map={};
        data.forEach(r=>{ map[r.oe_code]=r.status; });
        setShcoElcScores(map);
      });
  },[selectedProgramme,context?.hospitalId]);


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

  // Close user menu on outside click
  useEffect(()=>{
    if(!showUserMenu)return;
    const handler=()=>setShowUserMenu(false);
    document.addEventListener("click",handler);
    return()=>document.removeEventListener("click",handler);
  },[showUserMenu]);

  // NavStack refs — kept in sync via effects so goBack/navigate closures always read current values
  const currentNavStateRef = useRef(null);
  const navStackRef = useRef([]);

  useEffect(() => {
    currentNavStateRef.current = { screen, committeesView, auditMainTab, drillsView, selectedDrill, tracerView, tracerType, showLicenseAdd };
  }, [screen, committeesView, auditMainTab, drillsView, selectedDrill, tracerView, tracerType, showLicenseAdd]);

  useEffect(() => { navStackRef.current = navStack; }, [navStack]);

  const navigate = useCallback((newState) => {
    const snap = currentNavStateRef.current || {};
    setNavStack(prev => [...prev, snap]);
    if (newState.screen !== undefined) setScreen(newState.screen);
    if (newState.committeesView !== undefined) setCommitteesView(newState.committeesView);
    if (newState.auditMainTab !== undefined) setAuditMainTab(newState.auditMainTab);
    if (newState.drillsView !== undefined) setDrillsView(newState.drillsView);
    if (newState.selectedDrill !== undefined) setSelectedDrill(newState.selectedDrill);
    if (newState.tracerView !== undefined) setTracerView(newState.tracerView);
    if (newState.tracerType !== undefined) setTracerType(newState.tracerType);
    if (newState.showLicenseAdd !== undefined) setShowLicenseAdd(newState.showLicenseAdd);
  }, []);

  const goBack = useCallback(() => {
    const stack = navStackRef.current;
    if (stack.length === 0) return;
    const prev = stack[stack.length - 1];
    setNavStack(stack.slice(0, -1));
    setScreen(prev.screen);
    setCommitteesView(prev.committeesView);
    setAuditMainTab(prev.auditMainTab);
    setDrillsView(prev.drillsView);
    setSelectedDrill(prev.selectedDrill);
    setTracerView(prev.tracerView);
    setTracerType(prev.tracerType);
    if (prev.showLicenseAdd !== undefined) setShowLicenseAdd(prev.showLicenseAdd);
  }, []);

  // Browser back button → navigate within app
  useEffect(() => {
    window.history.pushState({ idx: 0 }, '', window.location.pathname);
    const handlePopState = () => {
      window.history.pushState({ idx: 0 }, '', window.location.pathname);
      goBack();
    };
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, [goBack]);

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
    if(ctx?.hospitalId){
      const{data:hospWt}=await supabase.from("hospitals").select("walkthrough_dismissed").eq("id",ctx.hospitalId).maybeSingle();
      if(hospWt&&!hospWt.walkthrough_dismissed)setTourStep(0);
    }
  },[]);

  const handleReady=(ctx)=>{setContext(ctx);setAuthState("programme");};
  const handleSignOut=async()=>{await supabase.auth.signOut();};
  const handleProgrammeSelect=(key,ctx)=>{
    const resolvedCtx=ctx||context;
    if(key==="hco_full"){setSelectedProgramme("hco");setScreen("dashboard");setAuthState("app");loadData(resolvedCtx);}
    else if(key==="shco_full"){setSelectedProgramme("shco-full");setScreen("shco-full");setAuthState("app");}
    else if(key==="shco_elc"){setSelectedProgramme("shco-elc");setScreen("shco");setAuthState("app");}
    else if(key==="hco_elc"){setSelectedProgramme("hco-elc");setScreen("hco-elc");setAuthState("app");}
    else if(key==="eco_full"){setSelectedProgramme("eco-full");setScreen("eco-full");setAuthState("app");}
  };

  if(authState==="loading") return <div style={{minHeight:"100vh",background:T.bg,display:"flex",alignItems:"center",justifyContent:"center",color:T.gold,fontFamily:"Segoe UI,sans-serif",fontSize:16}}>Loading…</div>;
  if(authState==="homepage") return <HomepageScreen onSignIn={()=>{window.history.pushState({screen:"login"},"",window.location.pathname);setAuthState("login");}} />;
  if(authState==="recovery") return <RecoveryScreen user={user} onDone={()=>{setUser(null);setAuthState("login");setContext(null);}}/>;
  if(authState==="login") return <LoginScreen onLogin={u=>{setUser(u);setAuthState("setup");}} initialError={authErrorMsg}/>;
  if(authState==="setup") return <SetupScreen user={user} onReady={handleReady}/>;
  if(authState==="programme") return <ProgrammeSelector user={user} ctx={context} onSelect={handleProgrammeSelect}/>;

  const isFree = context?.plan === 'free';
  const isPaid = context?.plan === 'paid';
  const accessUntil = context?.access_until ? new Date(context.access_until) : null;
  const hasAccess = isFree || (accessUntil !== null && accessUntil > new Date());
  const daysLeft = accessUntil ? Math.max(0, Math.ceil((accessUntil.getTime() - Date.now()) / (1000*60*60*24))) : 0;
  const trialExpired = !hasAccess;
  const isTrialActive = hasAccess && !isFree && !isPaid;

  if(trialExpired) return <UpgradeWall onSignOut={handleSignOut}/>;

  const readinessColor=decision.readiness==="NOT READY"?T.red:decision.readiness==="RISKY"?T.orange:T.green;
  const verdictColor=decision.verdict==="FAIL"?T.red:decision.verdict==="PASS"?T.green:decision.verdict==="PARTIAL"?T.orange:T.blue;

  const renderSHCOTab = () => {

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
          {ch:'ROM',name:'Responsibility of Management',stds:4,oes:19},
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
    return (
      <div style={{padding:16,display:'flex',flexDirection:'column',gap:16}}>

        {/* 2nd Edition notice */}
        <div style={{background:'#1a0a00',border:`1px solid ${T.orange}`,borderRadius:10,padding:14}}>
          <div style={{color:T.orange,fontWeight:700,fontSize:15,marginBottom:4}}>📋 2nd Edition Active — March 2026</div>
          <div style={{color:'#c8dcea',fontSize:14,lineHeight:1.6}}>
            ELC now uses the unified 2nd Edition standards (Jan 2026). New applicants from March 2026 must apply via <strong style={{color:T.gold}}>hope.qcin.org</strong>.
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

        {/* OE Compliance Summary */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:14}}>📋 OE Compliance Summary</div>
          {(()=>{
            const shcoCoreTotal = SHCO_ELC_OE_SUMMARY.reduce((a,c)=>a+c.core,0);
            const shcoCommTotal = SHCO_ELC_OE_SUMMARY.reduce((a,c)=>a+c.commitment,0);
            const shcoExclTotal = SHCO_ELC_OE_SUMMARY.reduce((a,c)=>a+c.excellence,0);
            const shcoOeTotal   = shcoCoreTotal + shcoCommTotal + shcoExclTotal;
            const shcoScoreVals = Object.values(shcoElcScores);
            const shcoMet       = shcoScoreVals.filter(s=>s==='met').length;
            const shcoPartial   = shcoScoreVals.filter(s=>s==='partial').length;
            const shcoNotMet    = shcoScoreVals.filter(s=>s==='not_met').length;
            const shcoUnscored  = shcoOeTotal - shcoMet - shcoPartial - shcoNotMet;
            const shcoMetPct    = shcoOeTotal > 0 ? Math.round((shcoMet/shcoOeTotal)*100) : 0;
            // Per-level met counts — uses shared hcoOeLevels (same unified 2nd Edition levels)
            const shcoCoreMet = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code]==='CORE' && shcoElcScores[oe.code]==='met').length;
            const shcoCommMet = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code]==='Commitment' && shcoElcScores[oe.code]==='met').length;
            const shcoExclMet = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code]==='Excellence' && shcoElcScores[oe.code]==='met').length;
            const shcoCoreNotMet= shcoCoreTotal - shcoCoreMet;
            let shcoVerdict, shcoVerdictColor;
            if(shcoMet===shcoOeTotal&&shcoMet>0){shcoVerdict='✓ Ready for Excellence';shcoVerdictColor=T.gold;}
            else if(shcoCoreMet===shcoCoreTotal&&shcoCommMet===shcoCommTotal&&shcoCoreTotal>0){shcoVerdict='✓ Ready for 2nd Cycle';shcoVerdictColor=T.green;}
            else if(shcoCoreMet===shcoCoreTotal&&shcoCoreTotal>0){shcoVerdict='✓ Ready for 1st Cycle Certification';shcoVerdictColor=T.green;}
            else{shcoVerdict=`${shcoCoreNotMet} CORE OE${shcoCoreNotMet!==1?'s':''} not yet met`;shcoVerdictColor=T.muted;}
            return(
              <>
                <div style={{display:'flex',gap:10,flexWrap:'wrap',marginBottom:10}}>
                  {[
                    {label:'✓ Met',val:shcoMet,color:'#4caf7d'},
                    {label:'~ Partial',val:shcoPartial,color:'#f4a441'},
                    {label:'✗ Not Met',val:shcoNotMet,color:'#e05a5a'},
                    {label:'— Unscored',val:shcoUnscored,color:T.muted},
                  ].map(({label,val,color})=>(
                    <div key={label} style={{background:T.panel2,borderRadius:8,padding:'8px 14px',border:`1px solid ${T.border}`,textAlign:'center',flex:1,minWidth:70}}>
                      <div style={{fontSize:18,fontWeight:800,color}}>{val}</div>
                      <div style={{fontSize:11,color,fontWeight:600}}>{label}</div>
                      <div style={{fontSize:10,color:T.muted}}>of {shcoOeTotal}</div>
                    </div>
                  ))}
                </div>
                <div style={{height:7,borderRadius:4,background:T.border,overflow:'hidden',marginBottom:12}}>
                  <div style={{height:'100%',width:`${shcoMetPct}%`,background:'#4caf7d',borderRadius:4,transition:'width 0.3s'}}/>
                </div>
                <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:8,marginBottom:12}}>
                  {[
                    {label:'CORE',total:shcoCoreTotal,met:shcoCoreMet,color:'#e05a5a'},
                    {label:'Commitment',total:shcoCommTotal,met:shcoCommMet,color:'#f4a441'},
                    {label:'Excellence',total:shcoExclTotal,met:shcoExclMet,color:'#c9a84c'},
                  ].map(({label,total:t,met,color})=>(
                    <div key={label} style={{background:T.panel2,borderRadius:8,padding:'8px 10px',border:`1px solid ${T.border}`,textAlign:'center'}}>
                      <div style={{fontSize:10,fontWeight:700,color,letterSpacing:0.5,marginBottom:4}}>{label}</div>
                      <div style={{fontSize:16,fontWeight:800,color:'#4caf7d'}}>{met}</div>
                      <div style={{fontSize:11,color:T.muted}}>Met / {t}</div>
                    </div>
                  ))}
                </div>
                <div style={{padding:'10px 14px',borderRadius:8,background:`${shcoVerdictColor}18`,border:`1px solid ${shcoVerdictColor}44`,textAlign:'center'}}>
                  <span style={{fontSize:13,fontWeight:700,color:shcoVerdictColor}}>{shcoVerdict}</span>
                </div>
              </>
            );
          })()}
        </div>

        {/* Fee Reference */}
        <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
          <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>💰 Certification Fee</div>
          <div style={{background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
            <div style={{color:T.muted,fontSize:14,marginBottom:10}}>Fees vary by bed strength and are updated periodically by NABH.</div>
            <a
              href="https://nabh.co/accreditations-certifications-and-empanelments/"
              target="_blank"
              rel="noopener noreferrer"
              style={{color:T.blue,fontWeight:600,fontSize:14,textDecoration:'underline'}}
            >
              View current fee structure on the official NABH website →
            </a>
            <div style={{fontSize:12,color:T.muted,marginTop:10}}>
              18% GST applicable. Fee is non-refundable and non-transferable. Focus assessment and re-issue charges apply separately.
            </div>
          </div>
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
        <div style={{color:'#c8dcea',fontSize:14}}>Desktop Assessment now has a <strong style={{color:'#eef4f9'}}>single NC closure cycle only</strong>. There is no second chance to respond. Submit complete NC responses the first time.</div>
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
              ['Fee','See nabh.co','See nabh.co'],
              ['Portal','hope.qcin.org','portal.nabh.co'],
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
        {phase:'Month 4',action:'Submit ELC application on hope.qcin.org',color:T.blue},
        {phase:'Month 5–6',action:'Desktop Assessment + NC closure (two rounds available)',color:T.orange},
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
    </div>
  );

  // ── ELC sub-tab router ──
  // ── SHCO ELC OE Scoring ─────────────────────────────────────────────────
  const shcoElcLevelColor = lvl => lvl==='CORE'?'#e05a5a':lvl==='Commitment'?'#f4a441':'#c9a84c';

  const setShcoElcScore = async (code, status) => {
    const prev = shcoElcScores[code];
    setShcoElcScores(p=>({...p,[code]:status}));
    setShcoElcScoreSaving(p=>({...p,[code]:true}));
    const {error} = await supabase.from("elc_scores").upsert(
      {hospital_id:context.hospitalId,oe_code:code,status,programme:"SHCO_ELC",updated_at:new Date().toISOString(),updated_by:user.id},
      {onConflict:"hospital_id,oe_code,programme"}
    );
    if(error) setShcoElcScores(p=>({...p,[code]:prev}));
    setShcoElcScoreSaving(p=>({...p,[code]:false}));
  };

  const clearShcoElcScore = async (code) => {
    const prev = shcoElcScores[code];
    setShcoElcScores(p=>{const n={...p};delete n[code];return n;});
    setShcoElcScoreSaving(p=>({...p,[code]:true}));
    const {error} = await supabase.from("elc_scores")
      .delete()
      .eq("hospital_id",context.hospitalId)
      .eq("oe_code",code)
      .eq("programme","SHCO_ELC");
    if(error) setShcoElcScores(p=>({...p,[code]:prev}));
    setShcoElcScoreSaving(p=>({...p,[code]:false}));
  };

  const toggleShcoElcOe = (code) => {
    const isOpen = shcoOeExpanded[code];
    setShcoOeExpanded(p=>({...p,[code]:!isOpen}));
    if(!isOpen && shcoOeTips[code]===undefined){
      const local = ELC_OE_TIPS[code];
      setShcoOeTips(p=>({...p,[code]:local?{...local,oe_level:hcoOeLevels[code]||null}:null}));
    }
  };

  const renderSHCOOEBrowser = () => {
    const q = shcoOeSearch.toLowerCase().trim();
    const filtered = HCO_ELC_OE_LIST.filter(oe => {
      const chMatch = shcoOeChapter==='all' || oe.chapter===shcoOeChapter;
      const txMatch = !q || oe.code.toLowerCase().includes(q) || oe.text.toLowerCase().includes(q);
      return chMatch && txMatch;
    });
    const grouped = SHCO_ELC_OE_SUMMARY.map(c=>({
      ch:c.ch,
      name:HCO_ELC_CHAPTER_SUMMARY.find(h=>h.ch===c.ch)?.name||c.name,
      oes:filtered.filter(oe=>oe.chapter===c.ch),
    })).filter(g=>g.oes.length>0);

    const total        = HCO_ELC_OE_LIST.length;
    const totalMet     = HCO_ELC_OE_LIST.filter(oe=>shcoElcScores[oe.code]==='met').length;
    const totalPartial = HCO_ELC_OE_LIST.filter(oe=>shcoElcScores[oe.code]==='partial').length;
    const totalNotMet  = HCO_ELC_OE_LIST.filter(oe=>shcoElcScores[oe.code]==='not_met').length;
    const totalUnscored= total - totalMet - totalPartial - totalNotMet;
    const coreCodes    = HCO_ELC_OE_LIST.filter(oe=>hcoOeLevels[oe.code]==='CORE');
    const commCodes    = HCO_ELC_OE_LIST.filter(oe=>hcoOeLevels[oe.code]==='Commitment');
    const exclCodes    = HCO_ELC_OE_LIST.filter(oe=>hcoOeLevels[oe.code]==='Excellence');
    const coreMet      = coreCodes.filter(oe=>shcoElcScores[oe.code]==='met').length;
    const corePartial  = coreCodes.filter(oe=>shcoElcScores[oe.code]==='partial').length;
    const coreNM       = coreCodes.filter(oe=>shcoElcScores[oe.code]==='not_met').length;
    const commMet      = commCodes.filter(oe=>shcoElcScores[oe.code]==='met').length;
    const commPartial  = commCodes.filter(oe=>shcoElcScores[oe.code]==='partial').length;
    const commNM       = commCodes.filter(oe=>shcoElcScores[oe.code]==='not_met').length;
    const exclMet      = exclCodes.filter(oe=>shcoElcScores[oe.code]==='met').length;
    const exclPartial  = exclCodes.filter(oe=>shcoElcScores[oe.code]==='partial').length;
    const exclNM       = exclCodes.filter(oe=>shcoElcScores[oe.code]==='not_met').length;
    const coreTotal    = coreCodes.length||122;
    const commTotal    = commCodes.length||35;
    const exclTotal    = exclCodes.length||32;
    const metPct       = Math.round((totalMet/total)*100);
    const coreNotMet   = coreTotal - coreMet;

    let verdict=null, verdictColor=T.muted;
    if(totalMet===total){verdict='✓ Ready for Excellence';verdictColor=T.gold;}
    else if(coreMet===coreTotal&&commMet===commTotal){verdict='✓ Ready for 2nd Cycle';verdictColor=T.green;}
    else if(coreMet===coreTotal){verdict='✓ Ready for 1st Cycle Certification';verdictColor=T.green;}
    else{verdict=`${coreNotMet} CORE OE${coreNotMet!==1?'s':''} not yet met`;verdictColor=T.muted;}

    const SCORE_BTNS=[
      {s:'met',    label:'✓ Met',    color:'#4caf7d'},
      {s:'partial',label:'~ Partial',color:'#f4a441'},
      {s:'not_met',label:'✗ Not Met',color:'#e05a5a'},
    ];

    return (
      <div style={{padding:16}}>
        {/* Progress summary */}
        <div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:10,padding:'12px 14px',marginBottom:14}}>
          <div style={{display:'flex',gap:10,flexWrap:'wrap',alignItems:'center',marginBottom:8}}>
            <span style={{fontSize:12,fontWeight:700,color:'#4caf7d'}}>✓ {totalMet} Met</span>
            <span style={{fontSize:12,fontWeight:700,color:'#f4a441'}}>~ {totalPartial} Partial</span>
            <span style={{fontSize:12,fontWeight:700,color:'#e05a5a'}}>✗ {totalNotMet} Not Met</span>
            <span style={{fontSize:12,fontWeight:700,color:T.muted}}>— {totalUnscored} Unscored</span>
            <span style={{marginLeft:'auto',fontSize:11,fontWeight:700,color:verdictColor}}>{verdict}</span>
          </div>
          <div style={{height:7,borderRadius:4,background:T.border,overflow:'hidden',marginBottom:10}}>
            <div style={{height:'100%',width:`${metPct}%`,background:'#4caf7d',borderRadius:4,transition:'width 0.3s'}}/>
          </div>
          <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:8}}>
            {[
              {label:'CORE',total:coreTotal,met:coreMet,partial:corePartial,nm:coreNM,color:'#e05a5a'},
              {label:'Commitment',total:commTotal,met:commMet,partial:commPartial,nm:commNM,color:'#f4a441'},
              {label:'Excellence',total:exclTotal,met:exclMet,partial:exclPartial,nm:exclNM,color:'#c9a84c'},
            ].map(({label,total:t,met,partial,nm,color})=>(
              <div key={label} style={{background:T.panel,borderRadius:7,padding:'7px 9px',border:`1px solid ${T.border}`}}>
                <div style={{fontSize:10,fontWeight:700,color,marginBottom:4,letterSpacing:0.5}}>{label} (/{t})</div>
                <div style={{fontSize:11,color:'#4caf7d'}}>✓ {met} Met</div>
                <div style={{fontSize:11,color:'#f4a441'}}>~ {partial} Partial</div>
                <div style={{fontSize:11,color:'#e05a5a'}}>✗ {nm} Not Met</div>
              </div>
            ))}
          </div>
        </div>

        {/* Search + chapter filter */}
        <div style={{marginBottom:12,display:'flex',gap:8,flexDirection:'column'}}>
          <input
            value={shcoOeSearch} onChange={e=>setShcoOeSearch(e.target.value)}
            placeholder="Search by OE code or text…"
            style={{width:'100%',padding:'9px 12px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:'border-box'}}
          />
          <div style={{display:'flex',gap:6,flexWrap:'wrap'}}>
            <button onClick={()=>setShcoOeChapter('all')}
              style={{padding:'4px 10px',borderRadius:20,border:`1px solid ${shcoOeChapter==='all'?T.gold:T.border}`,background:shcoOeChapter==='all'?T.gold+'22':'transparent',color:shcoOeChapter==='all'?T.gold:T.muted,fontSize:12,cursor:'pointer'}}>
              All ({HCO_ELC_OE_LIST.length})
            </button>
            {SHCO_ELC_OE_SUMMARY.map(c=>(
              <button key={c.ch} onClick={()=>setShcoOeChapter(c.ch)}
                style={{padding:'4px 10px',borderRadius:20,border:`1px solid ${shcoOeChapter===c.ch?T.gold:T.border}`,background:shcoOeChapter===c.ch?T.gold+'22':'transparent',color:shcoOeChapter===c.ch?T.gold:T.muted,fontSize:12,cursor:'pointer'}}>
                {c.ch} ({c.oes})
              </button>
            ))}
          </div>
        </div>

        {filtered.length===0 ? (
          <div style={{color:T.muted,fontSize:14,textAlign:'center',padding:24}}>No OEs match your search.</div>
        ) : (
          <div style={{display:'flex',flexDirection:'column',gap:16}}>
            {grouped.map(g=>(
              <div key={g.ch}>
                <div style={{color:T.gold,fontWeight:700,fontSize:14,marginBottom:6,display:'flex',alignItems:'center',gap:8}}>
                  <span>{g.ch}</span>
                  <span style={{color:T.muted,fontWeight:400,fontSize:13}}>{g.name}</span>
                  <span style={{marginLeft:'auto',color:T.blue,fontSize:12}}>{g.oes.length} OEs</span>
                </div>
                <div style={{display:'flex',flexDirection:'column',gap:4}}>
                  {g.oes.map(oe=>{
                    const isOpen   = !!shcoOeExpanded[oe.code];
                    const tips     = shcoOeTips[oe.code];
                    const loading  = !!shcoOeTipsLoading[oe.code];
                    const lvl      = hcoOeLevels[oe.code]||tips?.oe_level||null;
                    const lvlColor = lvl ? shcoElcLevelColor(lvl) : T.muted;
                    const scoreVal = shcoElcScores[oe.code]||null;
                    const saving   = !!shcoElcScoreSaving[oe.code];
                    const rowBorder= scoreVal==='met'?'#4caf7d':scoreVal==='partial'?'#f4a441':scoreVal==='not_met'?'#e05a5a':isOpen?T.blue:T.border;
                    return (
                      <div key={oe.code} style={{background:T.panel2,borderRadius:8,border:`1px solid ${rowBorder}`,overflow:'hidden',transition:'border-color 0.15s'}}>
                        <div style={{padding:'10px 12px'}}>
                          {/* Row 1: OE code + level badge + current score */}
                          <div style={{display:'flex',gap:8,alignItems:'center',marginBottom:6}}>
                            <span style={{color:T.gold,fontWeight:700,fontSize:13,fontFamily:'monospace'}}>{oe.code}</span>
                            {lvl&&(
                              <span style={{fontSize:9,fontWeight:700,letterSpacing:0.5,padding:'1px 6px',borderRadius:4,background:`${lvlColor}20`,color:lvlColor,border:`1px solid ${lvlColor}40`}}>{lvl}</span>
                            )}
                            <div style={{marginLeft:'auto',display:'flex',gap:8,alignItems:'center'}}>
                              {scoreVal&&<span style={{fontSize:11,fontWeight:700,color:scoreVal==='met'?'#4caf7d':scoreVal==='partial'?'#f4a441':'#e05a5a'}}>{scoreVal==='met'?'✓ Met':scoreVal==='partial'?'~ Partial':'✗ Not Met'}</span>}
                              <span onClick={()=>toggleShcoElcOe(oe.code)} style={{cursor:'pointer',color:T.muted,fontSize:12,userSelect:'none'}}>{isOpen?'▲':'▼'}</span>
                            </div>
                          </div>
                          {/* Row 2: OE text */}
                          <div onClick={()=>toggleShcoElcOe(oe.code)} style={{color:T.text,fontSize:13,lineHeight:1.5,marginBottom:10,cursor:'pointer'}}>{oe.text}</div>
                          {/* Row 3: scoring buttons */}
                          <div style={{display:'flex',gap:4,flexWrap:'wrap',alignItems:'center'}}>
                            {SCORE_BTNS.map(({s,label,color})=>{
                              const active=scoreVal===s;
                              return(
                                <button key={s}
                                  onClick={e=>{e.stopPropagation();if(!saving)setShcoElcScore(oe.code,s);}}
                                  style={{padding:'4px 10px',borderRadius:5,fontSize:11,fontWeight:700,cursor:saving?'wait':'pointer',
                                    background:active?color:'transparent',
                                    border:`1px solid ${active?color:T.border}`,
                                    color:active?'#fff':T.muted,
                                    opacity:saving?0.5:1,whiteSpace:'nowrap'}}>
                                  {label}
                                </button>
                              );
                            })}
                            {scoreVal&&(
                              <button
                                onClick={e=>{e.stopPropagation();if(!saving)clearShcoElcScore(oe.code);}}
                                style={{padding:'4px 10px',borderRadius:5,fontSize:11,fontWeight:700,cursor:saving?'wait':'pointer',
                                  background:'transparent',border:`1px solid ${T.border}`,color:T.muted,
                                  opacity:saving?0.5:1,whiteSpace:'nowrap'}}>
                                ✕ Clear
                              </button>
                            )}
                          </div>
                        </div>
                        {isOpen&&(
                          <div style={{padding:'0 12px 12px'}}>
                            {loading?(
                              <div style={{fontSize:12,color:T.muted,padding:'8px 0'}}>Loading…</div>
                            ):tips?(
                              <div style={{marginTop:4,background:T.blueD,border:`1px solid ${T.blue}20`,borderRadius:8,padding:'12px 14px'}}>
                                <div style={{fontSize:11,letterSpacing:2,color:T.blue,marginBottom:8}}>HOW TO ACHIEVE THIS OE</div>
                                {[tips.tip_1,tips.tip_2,tips.tip_3,tips.tip_4].map((tip,i)=>(
                                  <div key={i} style={{display:'flex',gap:8,marginBottom:6,alignItems:'flex-start'}}>
                                    <div style={{width:18,height:18,borderRadius:'50%',background:`${T.blue}20`,border:`1px solid ${T.blue}40`,display:'flex',alignItems:'center',justifyContent:'center',flexShrink:0,fontSize:11,color:T.blue,fontWeight:700}}>{i+1}</div>
                                    <div style={{fontSize:13,color:T.text,lineHeight:1.6,paddingTop:1}}>{tip}</div>
                                  </div>
                                ))}
                              </div>
                            ):null}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        )}
        <div style={{marginTop:12,color:T.muted,fontSize:12,textAlign:'center'}}>
          {filtered.length} of {HCO_ELC_OE_LIST.length} OEs — NABH SHCO ELC 2nd Edition (Jan 2026)
        </div>
      </div>
    );
  };

  const ELC_TABS = [
    {key:'overview', label:'📊 Overview'},
    {key:'oes', label:'📑 OE Browser'},
    {key:'docs', label:'📂 Documents'},
    {key:'licenses', label:'📋 Licenses'},
    {key:'process', label:'🗺️ Process'},
    {key:'upgrade', label:'⬆️ Upgrade Path'},
  ];

  const renderELCTab = () => {
    switch(shcoElcTab) {
      case 'overview': return renderOverview();
      case 'oes': return renderSHCOOEBrowser();
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

  // ── SHCO FULL ACCREDITATION DASHBOARD ────────────────────────────────────
  const renderSHCOFullTab = () => {
    // Chapter metadata — names from book TOC, counts verified from book p.24
    const CHAPTERS = [
      {key:'AAC',name:'Access, Assessment and Continuity of Care',stds:8},
      {key:'COP',name:'Care of Patients',stds:13},
      {key:'MOM',name:'Management of Medication',stds:9},
      {key:'PRE',name:'Patient Rights and Education',stds:6},
      {key:'HIC',name:'Hospital Infection Control',stds:6},
      {key:'PSQ',name:'Patient Safety and Quality Improvement',stds:5},
      {key:'ROM',name:'Responsibilities of Management',stds:4},
      {key:'FMS',name:'Facility Management and Safety',stds:5},
      {key:'HRM',name:'Human Resource Management',stds:9},
      {key:'IMS',name:'Information Management System',stds:6},
    ];
    const LEVELS = ['Core','Commitment','Achievement','Excellence'];
    const levelColor = l => l==='Core'?T.red:l==='Commitment'?T.orange:l==='Achievement'?T.gold:T.blue;
    // Score labels — exactly from book p.19
    const SCORE_LABELS = ['','No compliance','Poor compliance','Partial compliance','Good compliance','Full compliance'];
    const SCORE_COLORS = ['',T.red,T.red,T.orange,T.green,T.blue];

    // Chapter OE counts from live DB data (not hardcoded)
    const chapterOeCount = ch => shcoFullOes.filter(oe=>oe.chapter===ch).length;

    const handleScore = async (oeCode, score) => {
      if(shcoFullScores[oeCode]===score){
        setShcoFullScores(prev=>{const n={...prev};delete n[oeCode];return n;});
        setShcoFullScoreSaving(prev=>({...prev,[oeCode]:true}));
        await supabase.from("shco_full_scores").delete().match({hospital_id:context.hospitalId,oe_code:oeCode});
        setShcoFullScoreSaving(prev=>({...prev,[oeCode]:false}));
        return;
      }
      setShcoFullScores(prev=>({...prev,[oeCode]:score}));
      setShcoFullScoreSaving(prev=>({...prev,[oeCode]:true}));
      await supabase.from("shco_full_scores").upsert(
        {hospital_id:context.hospitalId,oe_code:oeCode,score},
        {onConflict:"hospital_id,oe_code"}
      );
      setShcoFullScoreSaving(prev=>({...prev,[oeCode]:false}));
    };

    // ── OE subsets by level ──────────────────────────────────────────────
    const coreCommOEs = shcoFullOes.filter(oe=>oe.level==='Core'||oe.level==='Commitment'); // 357
    const achieveOEs  = shcoFullOes.filter(oe=>oe.level==='Achievement');                   // 35
    const excelOEs    = shcoFullOes.filter(oe=>oe.level==='Excellence');                    // 16
    const coreOEs     = shcoFullOes.filter(oe=>oe.level==='Core');                          // 100

    // Relevant OEs for selected assessment type (book pp.21-23)
    const relevantOEs = shcoFullAssessType==='final'        ? coreCommOEs
                      : shcoFullAssessType==='surveillance' ? shcoFullOes.filter(oe=>oe.level!=='Excellence')
                      : shcoFullOes;

    // Compliance % = sum(scores) / (count × 5) × 100; unscored = 0 (book formula)
    const compliance = arr => arr.length>0
      ? Math.round(arr.reduce((a,oe)=>a+(shcoFullScores[oe.oe_code]||0),0)/(arr.length*5)*100) : 0;

    const commitmentOEs = shcoFullOes.filter(oe=>oe.level==='Commitment');
    const ccPct         = compliance(coreCommOEs);
    const commitPct     = compliance(commitmentOEs);
    const achPct        = compliance(achieveOEs);
    const excelPct      = compliance(excelOEs);

    // Core rule: every Core OE ≥4
    const coreScoredBelow4 = coreOEs.filter(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]<4);
    const coreUnscoredOEs  = coreOEs.filter(oe=>!shcoFullScores[oe.oe_code]);
    const corePass = coreScoredBelow4.length===0&&coreUnscoredOEs.length===0;

    // Per-standard checks (on relevantOEs)
    const stdMap={};
    relevantOEs.forEach(oe=>{
      if(!stdMap[oe.standard_code])stdMap[oe.standard_code]={text:oe.standard_text,ch:oe.chapter,oes:[]};
      stdMap[oe.standard_code].oes.push(oe);
    });
    const stdChecks=Object.entries(stdMap).map(([code,{oes}])=>{
      const scored=oes.filter(oe=>shcoFullScores[oe.oe_code]);
      const avg=scored.length>0?scored.reduce((a,oe)=>a+shcoFullScores[oe.oe_code],0)/scored.length:null;
      const atOrBelow2=oes.filter(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]<=2).length;
      return {code,avg,atOrBelow2,total:oes.length,scoredCount:scored.length};
    });

    // Renewal: no standard with ANY OE ≤2; others: no standard with >1 OE ≤2
    const maxLowPerStd = shcoFullAssessType==='renewal' ? 0 : 1;
    const stdLowFails  = stdChecks.filter(s=>s.atOrBelow2>maxLowPerStd);
    const stdAvgFails  = stdChecks.filter(s=>s.avg!==null&&s.avg<4);

    // Per-chapter checks
    const chapterStats=CHAPTERS.map(c=>{
      const chOes=relevantOEs.filter(oe=>oe.chapter===c.key);
      const chScored=chOes.filter(oe=>shcoFullScores[oe.oe_code]);
      const chAvg=chScored.length>0?chScored.reduce((a,oe)=>a+shcoFullScores[oe.oe_code],0)/chScored.length:null;
      const totalCount=shcoFullOes.filter(oe=>oe.chapter===c.key).length; // all 408
      return {...c,relevantCount:chOes.length,totalCount,scoredCount:chScored.length,
        avg:chAvg,pct:chAvg!==null?Math.round(chAvg/5*100):null,pass:chAvg!==null&&chAvg>=4};
    });
    const chapAvgFails=chapterStats.filter(c=>c.avg!==null&&c.avg<4);

    // Rules checklist — no page references
    const rules=[];
    rules.push({
      label:`Core + Commitment overall compliance ≥80% (${coreCommOEs.length} OEs)`,
      pct:ccPct,pass:ccPct>=80,
      detail:`Current: ${ccPct}% — need ≥80%`,
    });
    rules.push({
      label:`Commitment compliance ≥80% (${commitmentOEs.length} OEs)`,
      pct:commitPct,pass:commitPct>=80,
      detail:`Current: ${commitPct}% — need ≥80%`,
    });
    if(shcoFullAssessType==='surveillance'||shcoFullAssessType==='renewal'){
      rules.push({
        label:`Achievement overall compliance ≥80% (${achieveOEs.length} OEs)`,
        pct:achPct,pass:achPct>=80,
        detail:`Current: ${achPct}% — need ≥80%`,
      });
    }
    if(shcoFullAssessType==='renewal'){
      rules.push({
        label:`Excellence overall compliance ≥80% (${excelOEs.length} OEs)`,
        pct:excelPct,pass:excelPct>=80,
        detail:`Current: ${excelPct}% — need ≥80%`,
      });
    }
    rules.push({
      label:`All ${coreOEs.length} Core OEs must score ≥4 (Good compliance)`,
      pass:corePass,
      detail:coreScoredBelow4.length>0
        ?`${coreScoredBelow4.length} Core OE(s) scored <4: ${coreScoredBelow4.slice(0,4).map(o=>o.oe_code).join(', ')}${coreScoredBelow4.length>4?'…':''}`
        :coreUnscoredOEs.length>0?`${coreUnscoredOEs.length} Core OE(s) not yet scored`
        :'✓ All Core OEs ≥4',
    });
    rules.push({
      label:shcoFullAssessType==='renewal'
        ?`No standard should have any OE scored ≤2 (Poor compliance)`
        :`No standard should have more than 1 OE scored ≤2`,
      pass:stdLowFails.length===0,
      detail:stdLowFails.length>0
        ?`${stdLowFails.length} standard(s) failing: ${stdLowFails.slice(0,4).map(s=>s.code).join(', ')}${stdLowFails.length>4?'…':''}`
        :'✓ All standards OK',
    });
    rules.push({
      label:`Average score per standard must be ≥4`,
      pass:stdAvgFails.length===0,
      detail:stdAvgFails.length>0
        ?`${stdAvgFails.length} standard(s) below average 4: ${stdAvgFails.slice(0,4).map(s=>s.code).join(', ')}${stdAvgFails.length>4?'…':''}`
        :'✓ All standards ≥4',
    });
    rules.push({
      label:`Average score per chapter must be ≥4`,
      pass:chapAvgFails.length===0,
      detail:chapAvgFails.length>0
        ?`${chapAvgFails.length} chapter(s) below average 4: ${chapAvgFails.map(c=>c.key).join(', ')}`
        :'✓ All chapters ≥4',
    });

    const rulesPass=rules.filter(r=>r.pass).length;
    const allPass=rules.every(r=>r.pass);
    const totalScored=shcoFullOes.filter(oe=>shcoFullScores[oe.oe_code]).length;
    const relevantScored=relevantOEs.filter(oe=>shcoFullScores[oe.oe_code]).length;

    // ── Score OEs tab: filter + group ────────────────────────────────────
    const q=shcoFullSearch.toLowerCase().trim();
    const filteredOes=shcoFullOes.filter(oe=>{
      const chMatch=shcoFullChapter==='all'||oe.chapter===shcoFullChapter;
      const lvlMatch=shcoFullLevel==='all'||oe.level===shcoFullLevel;
      const txMatch=!q||oe.oe_code.toLowerCase().includes(q)||oe.text.toLowerCase().includes(q);
      return chMatch&&lvlMatch&&txMatch;
    });
    const byStandard=filteredOes.reduce((acc,oe)=>{
      if(!acc[oe.standard_code])acc[oe.standard_code]={std:oe.standard_text,oes:[]};
      acc[oe.standard_code].oes.push(oe);
      return acc;
    },{});

    // ── Dashboard sub-render ──────────────────────────────────────────────
    const renderDashboard=()=>(
      <div style={{padding:'12px 16px 40px'}}>
        {/* Assessment mode cards */}
        <div id="shco-tour-assess-mode" style={{marginBottom:12}}>
          <div style={{fontSize:11,color:T.muted,fontWeight:700,letterSpacing:1,marginBottom:8}}>ASSESSMENT MODE</div>
          <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
            {[
              {key:'final',       label:'Final Assessment',       sub:'Core + Commitment · 357 OEs', note:'Initial 4-year award'},
              {key:'surveillance',label:'Surveillance Assessment', sub:'+ Achievement · 392 OEs',    note:'At 14–18 months'},
              {key:'renewal',     label:'Re-accreditation',       sub:'All 408 OEs',                 note:'4-year renewal'},
            ].map(at=>(
              <button key={at.key} onClick={()=>setShcoFullAssessType(at.key)}
                style={{flex:1,minWidth:130,padding:'10px 12px',borderRadius:10,cursor:'pointer',textAlign:'left',border:'none',
                  background:shcoFullAssessType===at.key?T.orange+'22':T.panel,
                  outline:shcoFullAssessType===at.key?`2px solid ${T.orange}`:`1px solid ${T.border}`}}>
                <div style={{color:shcoFullAssessType===at.key?T.orange:T.white,fontWeight:700,fontSize:13,marginBottom:2}}>{at.label}</div>
                <div style={{color:T.muted,fontSize:11}}>{at.sub}</div>
                <div style={{color:shcoFullAssessType===at.key?T.orange:T.muted,fontSize:10,marginTop:2}}>{at.note}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Overall stats row */}
        <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:8,marginBottom:12}}>
          {[
            {label:'Total OEs',val:408,color:T.text},
            {label:'Scored',val:`${totalScored}/408`,color:totalScored===408?T.green:T.orange},
            {label:'Overall %',val:`${ccPct}%`,color:ccPct>=80?T.green:T.red},
            {label:'Core Fails',val:coreScoredBelow4.length+coreUnscoredOEs.length,
              color:(coreScoredBelow4.length+coreUnscoredOEs.length)>0?T.red:T.green},
          ].map(s=>(
            <div key={s.label} style={{background:T.panel,borderRadius:8,padding:'10px 8px',textAlign:'center',border:`1px solid ${T.border}`}}>
              <div style={{fontSize:20,fontWeight:800,color:s.color}}>{s.val}</div>
              <div style={{fontSize:11,color:T.muted,marginTop:2}}>{s.label}</div>
            </div>
          ))}
        </div>

        {/* Rules checklist */}
        <div id="shco-tour-rules" style={{marginBottom:12}}>
          <div style={{fontSize:11,color:T.muted,fontWeight:700,letterSpacing:1,marginBottom:8}}>ACCREDITATION RULES</div>
          <div style={{display:'grid',gap:5}}>
            {rules.map((r,i)=>(
              <div key={i} style={{display:'flex',alignItems:'flex-start',gap:8,padding:'8px 10px',borderRadius:8,
                background:r.pass?T.green+'10':T.red+'10',border:`1px solid ${r.pass?T.green:T.red}28`}}>
                <span style={{fontSize:14,flexShrink:0}}>{r.pass?'✅':'❌'}</span>
                <div style={{flex:1,minWidth:0}}>
                  <div style={{fontSize:12,fontWeight:600,color:r.pass?T.green:T.red,lineHeight:1.4}}>{r.label}</div>
                  <div style={{fontSize:11,color:T.muted,marginTop:2}}>{r.detail}</div>
                  {'pct' in r&&(
                    <div style={{display:'flex',alignItems:'center',gap:6,marginTop:4}}>
                      <div style={{flex:1,height:4,borderRadius:2,background:T.border,overflow:'hidden'}}>
                        <div style={{height:'100%',width:`${r.pct}%`,background:r.pass?T.green:T.red,borderRadius:2,transition:'width 0.3s'}}/>
                      </div>
                      <span style={{color:r.pass?T.green:T.red,fontWeight:700,fontSize:11,minWidth:34}}>{r.pct}%</span>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
          <div style={{marginTop:8,padding:'9px 14px',borderRadius:8,textAlign:'center',
            background:allPass?T.green+'18':rulesPass>0?T.orange+'18':T.red+'18',
            border:`1px solid ${allPass?T.green:rulesPass>0?T.orange:T.red}44`}}>
            <span style={{fontSize:13,fontWeight:800,color:allPass?T.green:rulesPass>0?T.orange:T.red}}>
              {allPass?'✓ ALL RULES PASS — READY FOR ACCREDITATION':`${rulesPass} of ${rules.length} rules passing`}
            </span>
          </div>
        </div>

        {/* Chapter health */}
        <div>
          <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:8}}>
            <div style={{fontSize:11,color:T.muted,fontWeight:700,letterSpacing:1}}>CHAPTER HEALTH</div>
            <div style={{fontSize:11,color:T.muted}}>{relevantScored}/{relevantOEs.length} relevant OEs scored</div>
          </div>
          <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(140px,1fr))',gap:6}}>
            {chapterStats.map(c=>{
              const col=c.avg===null?T.muted:c.pass?T.green:T.orange;
              return(
                <div key={c.key} style={{background:T.panel,border:`1px solid ${col}44`,borderRadius:8,padding:'10px 12px'}}>
                  <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:3}}>
                    <span style={{color:T.orange,fontWeight:800,fontSize:14}}>{c.key}</span>
                    <span style={{fontSize:13,fontWeight:700,color:col}}>{c.avg!==null?c.avg.toFixed(1)+' / 5':'—'}</span>
                  </div>
                  <div style={{fontSize:10,color:T.muted,marginBottom:2}}>{c.scoredCount} of {c.relevantCount} relevant scored</div>
                  <div style={{fontSize:10,color:T.muted,marginBottom:4}}>{c.totalCount} total OEs in chapter</div>
                  <div style={{height:4,borderRadius:2,background:T.border,overflow:'hidden',marginBottom:4}}>
                    <div style={{height:'100%',width:`${c.relevantCount>0?Math.round(c.scoredCount/c.relevantCount*100):0}%`,background:col,borderRadius:2,transition:'width 0.3s'}}/>
                  </div>
                  <div style={{fontSize:10,color:T.muted,lineHeight:1.4}}>{c.name}</div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );

    // ── Score OEs sub-render ──────────────────────────────────────────────
    const renderScoreOEs=()=>(
      <div style={{padding:'12px 16px 80px'}}>
        {/* Search bar */}
        <input
          value={shcoFullSearch} onChange={e=>setShcoFullSearch(e.target.value)}
          placeholder="Search by OE code (e.g. AAC.1.a) or keyword…"
          style={{width:'100%',padding:'9px 12px',borderRadius:8,border:`1px solid ${T.border}`,
            background:T.panel2,color:T.text,fontSize:14,boxSizing:'border-box',marginBottom:10}}
        />

        {/* Chapter tabs */}
        <div style={{display:'flex',overflowX:'auto',gap:0,borderBottom:`1px solid ${T.border}`,marginBottom:8}}>
          {[{key:'all',count:shcoFullOes.length},...CHAPTERS.map(c=>({key:c.key,count:chapterOeCount(c.key)}))].map(tab=>(
            <button key={tab.key} onClick={()=>setShcoFullChapter(tab.key)}
              style={{padding:'6px 10px',border:'none',cursor:'pointer',whiteSpace:'nowrap',background:'transparent',
                fontSize:12,fontWeight:600,
                color:shcoFullChapter===tab.key?T.orange:T.muted,
                borderBottom:shcoFullChapter===tab.key?`2px solid ${T.orange}`:'2px solid transparent'}}>
              {tab.key==='all'?'All':tab.key} ({tab.count})
            </button>
          ))}
        </div>

        {/* Level pills */}
        <div style={{display:'flex',gap:6,flexWrap:'wrap',marginBottom:12,alignItems:'center'}}>
          {['all',...LEVELS].map(lv=>(
            <button key={lv} onClick={()=>setShcoFullLevel(lv)}
              style={{padding:'3px 11px',borderRadius:20,cursor:'pointer',
                border:`1px solid ${shcoFullLevel===lv?(lv==='all'?T.gold:levelColor(lv)):T.border}`,
                background:shcoFullLevel===lv?(lv==='all'?T.gold+'22':levelColor(lv)+'22'):'transparent',
                color:shcoFullLevel===lv?(lv==='all'?T.gold:levelColor(lv)):T.muted,
                fontSize:12,fontWeight:600}}>
              {lv==='all'?'All Levels':lv}
            </button>
          ))}
          <span style={{marginLeft:'auto',fontSize:11,color:T.muted}}>{filteredOes.length} OEs</span>
        </div>

        {/* OE list */}
        {shcoFullLoading ? (
          <div style={{textAlign:'center',padding:40,color:T.muted}}>Loading OEs…</div>
        ) : Object.keys(byStandard).length===0 ? (
          <div style={{textAlign:'center',padding:40,color:T.muted}}>No OEs match the current filter.</div>
        ) : (
          Object.entries(byStandard).map(([stdCode,{std,oes:stdOes}])=>{
            const stdScoredOes=stdOes.filter(oe=>shcoFullScores[oe.oe_code]);
            const stdAvg=stdScoredOes.length>0?stdScoredOes.reduce((a,oe)=>a+shcoFullScores[oe.oe_code],0)/stdScoredOes.length:null;
            const stdLowCount=stdOes.filter(oe=>shcoFullScores[oe.oe_code]&&shcoFullScores[oe.oe_code]<=2).length;
            const stdFails=(stdAvg!==null&&stdAvg<4)||(stdLowCount>maxLowPerStd);
            const stdBorder=stdAvg===null?T.border:stdFails?T.red:T.green;
            return (
              <div key={stdCode} style={{marginBottom:14}}>
                <div style={{background:T.panel,border:`1px solid ${stdBorder}`,borderRadius:10,
                  padding:'9px 13px',marginBottom:5,display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:10}}>
                  <div style={{flex:1}}>
                    <span style={{color:T.orange,fontWeight:800,fontSize:13,marginRight:8}}>{stdCode}</span>
                    <span style={{color:T.text,fontSize:13,lineHeight:1.5}}>{std}</span>
                  </div>
                  <div style={{flexShrink:0,textAlign:'right'}}>
                    {stdAvg!==null&&<div style={{fontSize:12,fontWeight:700,color:stdAvg>=4?T.green:T.red}}>avg {stdAvg.toFixed(1)}</div>}
                    {stdLowCount>maxLowPerStd&&<div style={{fontSize:10,color:T.red}}>{stdLowCount} OE(s) ≤2</div>}
                    <div style={{fontSize:10,color:T.muted}}>{stdScoredOes.length}/{stdOes.length} scored</div>
                  </div>
                </div>
                {stdOes.map(oe=>{
                  const sc=shcoFullScores[oe.oe_code]||0;
                  const saving=shcoFullScoreSaving[oe.oe_code];
                  const lc=levelColor(oe.level);
                  const rowBorder=sc>=4?T.green:sc===3?T.orange:sc>=1?T.red:T.border;
                  return (
                    <div key={oe.oe_code} style={{background:T.panel2,border:`1px solid ${rowBorder}`,
                      borderRadius:8,padding:'10px 12px',marginBottom:5,marginLeft:8}}>
                      <div style={{display:'flex',alignItems:'center',gap:7,marginBottom:5,flexWrap:'wrap'}}>
                        <span style={{fontSize:12,fontWeight:700,color:T.muted,fontFamily:'monospace'}}>{oe.oe_code}</span>
                        <span style={{fontSize:11,padding:'1px 7px',borderRadius:10,
                          background:lc+'22',color:lc,border:`1px solid ${lc}44`,fontWeight:700}}>{oe.level}</span>
                        {sc>0
                          ?<span style={{fontSize:11,fontWeight:700,color:SCORE_COLORS[sc],
                              padding:'1px 8px',borderRadius:8,background:SCORE_COLORS[sc]+'18',border:`1px solid ${SCORE_COLORS[sc]}44`}}>
                              {sc} – {SCORE_LABELS[sc]}
                            </span>
                          :<span style={{fontSize:11,color:T.muted}}>Not scored</span>
                        }
                        {saving&&<span style={{fontSize:11,color:T.muted,fontStyle:'italic'}}>saving…</span>}
                        <button onClick={()=>setShcoFullShowTip(p=>({...p,[oe.oe_code]:!p[oe.oe_code]}))}
                          style={{marginLeft:'auto',padding:'3px 10px',borderRadius:7,fontSize:11,cursor:'pointer',
                            background:shcoFullShowTip[oe.oe_code]?T.blue+'22':'transparent',
                            border:`1px solid ${shcoFullShowTip[oe.oe_code]?T.blue:T.muted}`,
                            color:shcoFullShowTip[oe.oe_code]?T.blue:T.muted}}>
                          {shcoFullShowTip[oe.oe_code]?'▲ Hide':'? How to achieve'}
                        </button>
                        <button onClick={()=>{setAiWidgetOpen(true);setAiWidgetTrigger({code:oe.oe_code,id:Date.now()});}}
                          style={{padding:'3px 10px',borderRadius:7,fontSize:11,cursor:'pointer',
                            background:T.gold+'18',border:`1px solid ${T.gold}55`,color:T.gold,fontWeight:600}}>
                          ✦ Ask AI
                        </button>
                      </div>
                      <div style={{fontSize:13,color:T.text,lineHeight:1.6,marginBottom:8}}>{oe.text}</div>
                      {shcoFullShowTip[oe.oe_code]&&(()=>{
                        const tips = oe.achieve_tips;
                        const lvlTips = oe.level==='Core'
                          ? ['This is a Core OE — assessors will examine records, observe practice directly, and interview staff on every visit.','Ensure 100% of patient files show evidence of compliance, with no exceptions — even one missing record is a finding.','Conduct a monthly internal audit specifically for this OE and display the trend chart in the department.','Prepare staff with a 2-minute verbal response explaining the process — assessors routinely ask nurses and doctors directly.']
                          : oe.level==='Achievement'
                          ? ['Collect before/after data to demonstrate measurable improvement — a chart or table showing trend over 3 months is ideal.','Ensure the quality committee has reviewed and minuted this indicator at least once in the last quarter.','Show actual outcome numbers (e.g., percentage compliance, incident rates) not just that a system is in place.','Achievement OEs are assessed at Surveillance — begin collecting data from Day 1 of accreditation.']
                          : oe.level==='Excellence'
                          ? ['Excellence OEs are assessed at Re-accreditation — document innovation and leadership beyond basic compliance.','Benchmark against national or international standards and record the comparison formally.','Seek external validation (external audit, peer review, or published best practice adoption) and document it.','Excellence means demonstrated sustained improvement over multiple assessment cycles with supporting data.']
                          : ['Create a dated, signed SOP for this process and place it in the relevant department folder — version-controlled.','Train all concerned staff and maintain a signed attendance register as evidence of training.','Maintain a monthly audit record showing consistent compliance; the audit tool and results must be available for assessors.','Ensure any relevant forms/registers are filled completely — incomplete records are scored as non-compliance.'];
                        const displayTips = tips || lvlTips;
                        const tipLabel = tips ? 'HOW TO ACHIEVE THIS OE' : `GENERAL GUIDANCE — ${oe.level.toUpperCase()}`;
                        return (
                          <div style={{marginTop:6,marginBottom:8,background:T.blue+'14',border:`1px solid ${T.blue}22`,borderRadius:8,padding:'12px 14px'}}>
                            <div style={{fontSize:10,letterSpacing:2,color:T.blue,marginBottom:8,fontWeight:700}}>{tipLabel}</div>
                            {displayTips.map((tip,i)=>(
                              <div key={i} style={{display:'flex',gap:8,marginBottom:6,alignItems:'flex-start'}}>
                                <div style={{width:18,height:18,borderRadius:'50%',background:T.blue+'22',border:`1px solid ${T.blue}44`,
                                  display:'flex',alignItems:'center',justifyContent:'center',flexShrink:0,fontSize:11,color:T.blue,fontWeight:700}}>{i+1}</div>
                                <div style={{fontSize:12,color:T.text,lineHeight:1.6,paddingTop:1}}>{tip}</div>
                              </div>
                            ))}
                            {!tips&&<div style={{fontSize:11,color:T.muted,marginTop:4,fontStyle:'italic'}}>OE-specific tips will appear here once loaded — showing {oe.level} guidance for now.</div>}
                          </div>
                        );
                      })()}
                      <div style={{display:'flex',gap:4,flexWrap:'wrap'}}>
                        {[1,2,3,4,5].map(n=>(
                          <button key={n} onClick={()=>handleScore(oe.oe_code,n)}
                            style={{padding:'4px 9px',borderRadius:7,fontSize:11,fontWeight:700,cursor:'pointer',
                              background:sc===n?`${SCORE_COLORS[n]}28`:T.panel,
                              border:`1px solid ${sc===n?SCORE_COLORS[n]:SCORE_COLORS[n]+'40'}`,
                              color:sc===n?SCORE_COLORS[n]:T.muted,transition:'all 0.12s'}}>
                            {n} – {SCORE_LABELS[n]}
                          </button>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            );
          })
        )}
      </div>
    );

    // ── Fix Gaps sub-render ────────────────────────────────────────────────
    const gapSeverity = oe => {
      const sc = shcoFullScores[oe.oe_code]||0;
      if(sc===0) return null; // unscored — not a gap
      if(oe.level==='Core') return sc<=3 ? 'CRITICAL' : null;
      if(oe.level==='Commitment') return sc<=2 ? 'HIGH' : sc===3 ? 'MEDIUM' : null;
      return sc<=3 ? 'LOW' : null; // Achievement / Excellence
    };

    const allGaps = shcoFullOes
      .map(oe=>({oe, sev:gapSeverity(oe)}))
      .filter(({sev})=>sev!==null)
      .map(({oe,sev})=>({
        oe_code: oe.oe_code, oe_text: oe.text, level: oe.level,
        standard_code: oe.standard_code, severity: sev,
        score: shcoFullScores[oe.oe_code]||0,
      }));

    const renderFixGaps = () => {
      const q = shcoFullGapSearch.toLowerCase().trim();
      const filtered = allGaps.filter(g=>{
        const matchSev = shcoFullGapFilter==='ALL' || g.severity===shcoFullGapFilter;
        const matchQ   = !q || g.oe_code.toLowerCase().includes(q) || g.oe_text.toLowerCase().includes(q);
        return matchSev && matchQ;
      });

      return (
        <div style={{padding:'12px 16px 80px'}}>
          {/* Search */}
          <input value={shcoFullGapSearch} onChange={e=>setShcoFullGapSearch(e.target.value)}
            placeholder="Search gaps by OE code (e.g. AAC.1.a) or keyword…"
            style={{width:'100%',padding:'10px 14px',borderRadius:8,border:`1px solid ${T.border}`,
              background:T.panel2,color:T.text,fontSize:14,marginBottom:10,boxSizing:'border-box'}}/>

          {/* Severity filter + count */}
          <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap',alignItems:'center'}}>
            {['ALL','CRITICAL','HIGH','MEDIUM','LOW'].map(s=>(
              <button key={s} onClick={()=>setShcoFullGapFilter(s)}
                style={{padding:'5px 14px',borderRadius:8,fontSize:12,cursor:'pointer',
                  background:shcoFullGapFilter===s?`${sevColor(s)}20`:'transparent',
                  border:`1px solid ${shcoFullGapFilter===s?sevColor(s):T.border}`,
                  color:shcoFullGapFilter===s?sevColor(s):T.muted}}>{s}</button>
            ))}
            <div style={{marginLeft:'auto',fontSize:13,color:T.muted}}>{allGaps.length} gaps</div>
          </div>

          {filtered.length===0 && (
            <div style={{textAlign:'center',color:T.muted,padding:'40px',fontSize:14}}>
              {allGaps.length===0 ? 'No gaps found. Score OEs first.' : 'No gaps at this severity level.'}
            </div>
          )}

          <div style={{display:'grid',gap:10}}>
            {filtered.map(g=>{
              const fc   = shcoFullCapaForm[g.oe_code]||{};
              const dbC  = shcoFullCapaDb[g.oe_code];
              const expanded = fc.expanded;
              const hasSaved = dbC || fc.saved;
              return (
                <div key={g.oe_code} style={{background:T.panel,border:`1px solid ${sevColor(g.severity)}25`,borderRadius:12,overflow:'hidden'}}>
                  <div style={{height:3,background:sevColor(g.severity)}}/>
                  <div style={{padding:'14px 16px'}}>
                    {/* Header row */}
                    <div style={{display:'flex',gap:10,alignItems:'flex-start',marginBottom:8}}>
                      <div style={{flex:1}}>
                        <div style={{display:'flex',gap:8,alignItems:'center',marginBottom:4,flexWrap:'wrap'}}>
                          <span style={{fontFamily:'monospace',fontSize:13,fontWeight:700,color:lvColor(g.level)}}>{g.oe_code}</span>
                          <span style={{fontSize:11,padding:'2px 7px',borderRadius:5,background:`${sevColor(g.severity)}15`,color:sevColor(g.severity),fontWeight:700}}>{g.severity}</span>
                          <span style={{fontSize:11,padding:'2px 6px',borderRadius:5,background:`${lvColor(g.level)}18`,color:lvColor(g.level)}}>{g.level}</span>
                          {hasSaved&&<span style={{fontSize:11,padding:'2px 6px',borderRadius:5,background:T.green+'22',color:T.green}}>✓ CAPA saved</span>}
                        </div>
                        <div style={{fontSize:12,color:T.text,lineHeight:1.5}}>{g.oe_text}</div>
                      </div>
                      <div style={{textAlign:'center',flexShrink:0}}>
                        <div style={{fontSize:22,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
                        <div style={{fontSize:7,color:T.muted}}>/ 5</div>
                      </div>
                    </div>

                    {/* CAPA action buttons */}
                    <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                      {!expanded && hasSaved ? (
                        <>
                          <button
                            onClick={()=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{
                              ...fc, expanded:true,
                              finding: fc.finding!==undefined ? fc.finding : (dbC?.finding||''),
                              action:  fc.action!==undefined  ? fc.action  : (dbC?.action_planned||''),
                              person:  fc.person!==undefined  ? fc.person  : (dbC?.responsible_person||''),
                              date:    fc.date!==undefined    ? fc.date    : (dbC?.target_date||''),
                            }}))}
                            style={{fontSize:12,color:T.gold,background:'transparent',border:`1px solid ${T.gold}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                            ✏️ Edit CAPA
                          </button>
                          <button
                            onClick={()=>deleteShcoFullCapa(g.oe_code)}
                            style={{fontSize:12,color:T.red,background:'transparent',border:`1px solid ${T.red}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                            🗑 Delete CAPA
                          </button>
                        </>
                      ) : expanded ? (
                        <button
                          onClick={()=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,expanded:false}}))}
                          style={{fontSize:12,color:T.muted,background:'transparent',border:`1px solid ${T.border}`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                          ▲ Hide CAPA
                        </button>
                      ) : (
                        <button
                          onClick={()=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,expanded:true}}))}
                          style={{fontSize:12,color:T.gold,background:'transparent',border:`1px solid ${T.gold}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                          ▼ Add CAPA
                        </button>
                      )}
                    </div>

                    {/* CAPA form */}
                    {expanded&&(
                      <div style={{marginTop:12,display:'grid',gap:8}}>
                        {fc.saved&&<div style={{fontSize:12,color:T.green,padding:'6px 10px',background:T.green+'14',borderRadius:6}}>✓ CAPA saved successfully</div>}
                        <div>
                          <div style={{fontSize:11,color:T.muted,marginBottom:4}}>FINDING *</div>
                          <textarea value={fc.finding!==undefined ? fc.finding : (dbC?.finding||'')}
                            onChange={e=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,finding:e.target.value,saved:false}}))}
                            rows={2} placeholder="Describe the non-compliance finding…"
                            style={{width:'100%',padding:'8px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:'vertical',boxSizing:'border-box'}}/>
                        </div>
                        <div>
                          <div style={{fontSize:11,color:T.muted,marginBottom:4}}>ACTION PLANNED *</div>
                          <textarea value={fc.action!==undefined ? fc.action : (dbC?.action_planned||'')}
                            onChange={e=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,action:e.target.value,saved:false}}))}
                            rows={2} placeholder="Corrective action to be taken…"
                            style={{width:'100%',padding:'8px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:'vertical',boxSizing:'border-box'}}/>
                        </div>
                        <div style={{display:'flex',gap:8,flexWrap:'wrap',alignItems:'flex-end'}}>
                          <div style={{flex:1,minWidth:140}}>
                            <div style={{fontSize:11,color:T.muted,marginBottom:4}}>RESPONSIBLE PERSON</div>
                            <input value={fc.person!==undefined ? fc.person : (dbC?.responsible_person||'')}
                              onChange={e=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,person:e.target.value,saved:false}}))}
                              placeholder="Name / Designation"
                              style={{width:'100%',padding:'7px 10px',borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:'border-box'}}/>
                          </div>
                          <div>
                            <div style={{fontSize:11,color:T.muted,marginBottom:4}}>TARGET DATE</div>
                            <input type="date" value={fc.date!==undefined ? fc.date : (dbC?.target_date||'')}
                              onChange={e=>setShcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,date:e.target.value,saved:false}}))}
                              style={{padding:'7px 10px',borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
                          </div>
                          <button onClick={()=>saveShcoFullCapa(g.oe_code)}
                            disabled={shcoFullCapaSaving[g.oe_code]||!(fc.finding!==undefined?fc.finding:dbC?.finding)||!(fc.action!==undefined?fc.action:dbC?.action_planned)}
                            style={{padding:'7px 20px',borderRadius:10,background:`linear-gradient(135deg,${T.green},#3d9e6e)`,
                              border:'none',color:T.bg,fontSize:14,fontWeight:700,
                              cursor:'pointer',opacity:1}}>
                            {shcoFullCapaSaving[g.oe_code]?'Saving…':'Save CAPA →'}
                          </button>
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
    };

    return (
      <div style={{background:T.bg,minHeight:'100vh',color:T.text,fontFamily:'Segoe UI,system-ui,sans-serif'}}>
        {/* Tab header */}
        <div style={{display:'flex',alignItems:'center',borderBottom:`1px solid ${T.border}`,padding:'0 16px',background:T.panel}}>
          {[
            {key:'dashboard',label:'📊 Dashboard'},
            {key:'scoring',  label:'✏️ Score OEs', tourId:'shco-tour-score'},
            {key:'fixgaps',  label:`🔧 Fix Gaps${allGaps.length>0?' ('+allGaps.length+')':''}`, tourId:'shco-tour-fixgaps'},
            {key:'kpis',     label:'📈 KPIs'},
          ].map(tab=>(
            <button key={tab.key} id={tab.tourId||undefined} onClick={()=>setShcoFullTab(tab.key)}
              style={{padding:'12px 16px',border:'none',cursor:'pointer',background:'transparent',fontSize:13,fontWeight:600,
                color:shcoFullTab===tab.key?T.orange:T.muted,
                borderBottom:shcoFullTab===tab.key?`2px solid ${T.orange}`:'2px solid transparent'}}>
              {tab.label}
            </button>
          ))}
          <button id="shco-tour-pdf" onClick={generateShcoFullPDF} disabled={shcoFullPdfLoading}
            style={{marginLeft:'auto',padding:'6px 14px',borderRadius:7,border:`1px solid ${T.gold}`,
              background:'transparent',color:T.gold,fontSize:12,fontWeight:700,cursor:shcoFullPdfLoading?'default':'pointer',
              opacity:shcoFullPdfLoading?0.6:1,whiteSpace:'nowrap'}}>
            {shcoFullPdfLoading ? '⏳ Generating…' : '⬇ Download Gap Report'}
          </button>
        </div>
        {shcoFullTab==='dashboard' ? renderDashboard() : shcoFullTab==='scoring' ? renderScoreOEs() : shcoFullTab==='kpis' ? <ShcoFullKpiTab hospitalId={context?.hospitalId}/> : renderFixGaps()}
      </div>
    );
  };

  // ── ECO FULL TAB ──────────────────────────────────────────────────────────
  const renderECOFullTab = () => {
    const ECO_COLOR = '#06b6d4';
    // Derive chapters dynamically from loaded OE data
    const chapterKeys = [...new Set(ecoFullOes.map(oe=>oe.chapter))].filter(Boolean).sort();
    const CHAPTERS = chapterKeys.map(key=>{
      const chOe = ecoFullOes.find(oe=>oe.chapter===key);
      return {key, name: chOe?.chapter_name || key};
    });
    const LEVELS = ['Core','Commitment','Achievement','Excellence'];
    const levelColor = l => l==='Core'?T.red:l==='Commitment'?T.orange:l==='Achievement'?T.gold:T.blue;
    const SCORE_LABELS = ['','No compliance','Poor compliance','Partial compliance','Good compliance','Full compliance'];
    const SCORE_COLORS = ['',T.red,T.red,T.orange,T.green,T.blue];

    const chapterOeCount = ch => ecoFullOes.filter(oe=>oe.chapter===ch).length;

    const handleScore = async (oeCode, score) => {
      if(ecoFullScores[oeCode]===score){
        setEcoFullScores(prev=>{const n={...prev};delete n[oeCode];return n;});
        setEcoFullScoreSaving(prev=>({...prev,[oeCode]:true}));
        await supabase.from("eco_full_scores").delete().match({hospital_id:context.hospitalId,oe_code:oeCode});
        setEcoFullScoreSaving(prev=>({...prev,[oeCode]:false}));
        return;
      }
      setEcoFullScores(prev=>({...prev,[oeCode]:score}));
      setEcoFullScoreSaving(prev=>({...prev,[oeCode]:true}));
      await supabase.from("eco_full_scores").delete().eq("hospital_id",context.hospitalId).eq("oe_code",oeCode);
      await supabase.from("eco_full_scores").insert({hospital_id:context.hospitalId,oe_code:oeCode,score});
      setEcoFullScoreSaving(prev=>({...prev,[oeCode]:false}));
    };

    // OE subsets by level
    const coreCommOEs = ecoFullOes.filter(oe=>oe.category==='core'||oe.category==='commitment'); // 282
    const achieveOEs  = ecoFullOes.filter(oe=>oe.category==='achievement');                     // 12
    const excelOEs    = ecoFullOes.filter(oe=>oe.category==='excellence');                      // 8
    const coreOEs     = ecoFullOes.filter(oe=>oe.category==='core');

    const relevantOEs = ecoFullAssessType==='final'        ? coreCommOEs
                      : ecoFullAssessType==='surveillance' ? ecoFullOes.filter(oe=>oe.category!=='excellence')
                      : ecoFullOes;

    const compliance = arr => arr.length>0
      ? Math.round(arr.reduce((a,oe)=>a+(ecoFullScores[oe.oe_code]||0),0)/(arr.length*5)*100) : 0;

    const commitmentOEs = ecoFullOes.filter(oe=>oe.category==='commitment');
    const ccPct         = compliance(coreCommOEs);
    const commitPct     = compliance(commitmentOEs);
    const achPct        = compliance(achieveOEs);
    const excelPct      = compliance(excelOEs);

    const coreScoredBelow4 = coreOEs.filter(oe=>ecoFullScores[oe.oe_code]&&ecoFullScores[oe.oe_code]<4);
    const coreUnscoredOEs  = coreOEs.filter(oe=>!ecoFullScores[oe.oe_code]);
    const corePass = coreScoredBelow4.length===0&&coreUnscoredOEs.length===0;

    const stdMap={};
    relevantOEs.forEach(oe=>{
      if(!stdMap[oe.standard_code])stdMap[oe.standard_code]={text:oe.standard_text,ch:oe.chapter,oes:[]};
      stdMap[oe.standard_code].oes.push(oe);
    });
    const stdChecks=Object.entries(stdMap).map(([code,{oes}])=>{
      const scored=oes.filter(oe=>ecoFullScores[oe.oe_code]);
      const avg=scored.length>0?scored.reduce((a,oe)=>a+ecoFullScores[oe.oe_code],0)/scored.length:null;
      const atOrBelow2=oes.filter(oe=>ecoFullScores[oe.oe_code]&&ecoFullScores[oe.oe_code]<=2).length;
      return {code,avg,atOrBelow2,total:oes.length,scoredCount:scored.length};
    });

    const maxLowPerStd = ecoFullAssessType==='renewal' ? 0 : 1;
    const stdLowFails  = stdChecks.filter(s=>s.atOrBelow2>maxLowPerStd);
    const stdAvgFails  = stdChecks.filter(s=>s.avg!==null&&s.avg<4);

    const chapterStats=CHAPTERS.map(c=>{
      const chOes=relevantOEs.filter(oe=>oe.chapter===c.key);
      const chScored=chOes.filter(oe=>ecoFullScores[oe.oe_code]);
      const chAvg=chScored.length>0?chScored.reduce((a,oe)=>a+ecoFullScores[oe.oe_code],0)/chScored.length:null;
      const totalCount=ecoFullOes.filter(oe=>oe.chapter===c.key).length;
      return {...c,relevantCount:chOes.length,totalCount,scoredCount:chScored.length,
        avg:chAvg,pct:chAvg!==null?Math.round(chAvg/5*100):null,pass:chAvg!==null&&chAvg>=4};
    });
    const chapAvgFails=chapterStats.filter(c=>c.avg!==null&&c.avg<4);

    const rules=[];
    rules.push({
      label:`Core + Commitment overall compliance ≥80% (${coreCommOEs.length} OEs)`,
      pct:ccPct,pass:ccPct>=80,
      detail:`Current: ${ccPct}% — need ≥80%`,
    });
    rules.push({
      label:`Commitment compliance ≥80% (${commitmentOEs.length} OEs)`,
      pct:commitPct,pass:commitPct>=80,
      detail:`Current: ${commitPct}% — need ≥80%`,
    });
    if(ecoFullAssessType==='surveillance'||ecoFullAssessType==='renewal'){
      rules.push({
        label:`Achievement overall compliance ≥80% (${achieveOEs.length} OEs)`,
        pct:achPct,pass:achPct>=80,
        detail:`Current: ${achPct}% — need ≥80%`,
      });
    }
    if(ecoFullAssessType==='renewal'){
      rules.push({
        label:`Excellence overall compliance ≥80% (${excelOEs.length} OEs)`,
        pct:excelPct,pass:excelPct>=80,
        detail:`Current: ${excelPct}% — need ≥80%`,
      });
    }
    rules.push({
      label:`All ${coreOEs.length} Core OEs must score ≥4 (Good compliance)`,
      pass:corePass,
      detail:coreScoredBelow4.length>0
        ?`${coreScoredBelow4.length} Core OE(s) scored <4: ${coreScoredBelow4.slice(0,4).map(o=>o.oe_code).join(', ')}${coreScoredBelow4.length>4?'…':''}`
        :coreUnscoredOEs.length>0?`${coreUnscoredOEs.length} Core OE(s) not yet scored`
        :'✓ All Core OEs ≥4',
    });
    rules.push({
      label:ecoFullAssessType==='renewal'
        ?`No standard should have any OE scored ≤2 (Poor compliance)`
        :`No standard should have more than 1 OE scored ≤2`,
      pass:stdLowFails.length===0,
      detail:stdLowFails.length>0
        ?`${stdLowFails.length} standard(s) failing: ${stdLowFails.slice(0,4).map(s=>s.code).join(', ')}${stdLowFails.length>4?'…':''}`
        :'✓ All standards OK',
    });
    rules.push({
      label:`Average score per standard must be ≥4`,
      pass:stdAvgFails.length===0,
      detail:stdAvgFails.length>0
        ?`${stdAvgFails.length} standard(s) below average 4: ${stdAvgFails.slice(0,4).map(s=>s.code).join(', ')}${stdAvgFails.length>4?'…':''}`
        :'✓ All standards ≥4',
    });
    rules.push({
      label:`Average score per chapter must be ≥4`,
      pass:chapAvgFails.length===0,
      detail:chapAvgFails.length>0
        ?`${chapAvgFails.length} chapter(s) below average 4: ${chapAvgFails.map(c=>c.key).join(', ')}`
        :'✓ All chapters ≥4',
    });

    const rulesPass=rules.filter(r=>r.pass).length;
    const allPass=rules.every(r=>r.pass);
    const totalScored=ecoFullOes.filter(oe=>ecoFullScores[oe.oe_code]).length;
    const relevantScored=relevantOEs.filter(oe=>ecoFullScores[oe.oe_code]).length;

    const q=ecoFullSearch.toLowerCase().trim();
    const filteredOes=ecoFullOes.filter(oe=>{
      const chMatch=ecoFullChapter==='all'||oe.chapter===ecoFullChapter;
      const lvlMatch=ecoFullLevel==='all'||oe.category?.toLowerCase()===ecoFullLevel.toLowerCase();
      const txMatch=!q||oe.oe_code.toLowerCase().includes(q)||(oe.oe_text||'').toLowerCase().includes(q);
      return chMatch&&lvlMatch&&txMatch;
    });
    const byStandard=filteredOes.reduce((acc,oe)=>{
      const stdKey=oe.standard_code||(oe.oe_code?oe.oe_code.replace(/\.[^.]+$/,''):oe.chapter||'Other');
      const stdText=oe.standard_text||stdKey;
      if(!acc[stdKey])acc[stdKey]={std:stdText,oes:[]};
      acc[stdKey].oes.push(oe);
      return acc;
    },{});

    const renderDashboard=()=>(
      <div style={{padding:'12px 16px 40px'}}>
        <div style={{marginBottom:12}}>
          <div style={{fontSize:11,color:T.muted,fontWeight:700,letterSpacing:1,marginBottom:8}}>ASSESSMENT MODE</div>
          <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
            {[
              {key:'final',       label:'Final Assessment',       sub:`Core + Commitment · ${coreCommOEs.length} OEs`, note:'Initial 4-year award'},
              {key:'surveillance',label:'Surveillance Assessment', sub:`+ Achievement · ${coreCommOEs.length+achieveOEs.length} OEs`,    note:'At 21–24 months'},
              {key:'renewal',     label:'Re-accreditation',       sub:`All ${ecoFullOes.length} OEs`,                 note:'4-year renewal'},
            ].map(at=>(
              <button key={at.key} onClick={()=>setEcoFullAssessType(at.key)}
                style={{flex:1,minWidth:130,padding:'10px 12px',borderRadius:10,cursor:'pointer',textAlign:'left',border:'none',
                  background:ecoFullAssessType===at.key?ECO_COLOR+'22':T.panel,
                  outline:ecoFullAssessType===at.key?`2px solid ${ECO_COLOR}`:`1px solid ${T.border}`}}>
                <div style={{color:ecoFullAssessType===at.key?ECO_COLOR:T.white,fontWeight:700,fontSize:13,marginBottom:2}}>{at.label}</div>
                <div style={{color:T.muted,fontSize:11}}>{at.sub}</div>
                <div style={{color:ecoFullAssessType===at.key?ECO_COLOR:T.muted,fontSize:10,marginTop:2}}>{at.note}</div>
              </button>
            ))}
          </div>
        </div>

        <div style={{display:'grid',gridTemplateColumns:'repeat(4,1fr)',gap:8,marginBottom:12}}>
          {[
            {label:'Total OEs',val:ecoFullOes.length,color:T.text},
            {label:'Scored',val:`${totalScored}/${ecoFullOes.length}`,color:totalScored===ecoFullOes.length?T.green:T.orange},
            {label:'Overall %',val:`${ccPct}%`,color:ccPct>=80?T.green:T.red},
            {label:'Core Fails',val:coreScoredBelow4.length+coreUnscoredOEs.length,
              color:(coreScoredBelow4.length+coreUnscoredOEs.length)>0?T.red:T.green},
          ].map(s=>(
            <div key={s.label} style={{background:T.panel,borderRadius:8,padding:'10px 8px',textAlign:'center',border:`1px solid ${T.border}`}}>
              <div style={{fontSize:20,fontWeight:800,color:s.color}}>{s.val}</div>
              <div style={{fontSize:11,color:T.muted,marginTop:2}}>{s.label}</div>
            </div>
          ))}
        </div>

        <div style={{marginBottom:12}}>
          <div style={{fontSize:11,color:T.muted,fontWeight:700,letterSpacing:1,marginBottom:8}}>ACCREDITATION RULES</div>
          <div style={{display:'grid',gap:5}}>
            {rules.map((r,i)=>(
              <div key={i} style={{display:'flex',alignItems:'flex-start',gap:8,padding:'8px 10px',borderRadius:8,
                background:r.pass?T.green+'10':T.red+'10',border:`1px solid ${r.pass?T.green:T.red}28`}}>
                <span style={{fontSize:14,flexShrink:0}}>{r.pass?'✅':'❌'}</span>
                <div style={{flex:1,minWidth:0}}>
                  <div style={{fontSize:12,fontWeight:600,color:r.pass?T.green:T.red,lineHeight:1.4}}>{r.label}</div>
                  <div style={{fontSize:11,color:T.muted,marginTop:2}}>{r.detail}</div>
                  {'pct' in r&&(
                    <div style={{display:'flex',alignItems:'center',gap:6,marginTop:4}}>
                      <div style={{flex:1,height:4,borderRadius:2,background:T.border,overflow:'hidden'}}>
                        <div style={{height:'100%',width:`${r.pct}%`,background:r.pass?T.green:T.red,borderRadius:2,transition:'width 0.3s'}}/>
                      </div>
                      <span style={{color:r.pass?T.green:T.red,fontWeight:700,fontSize:11,minWidth:34}}>{r.pct}%</span>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
          <div style={{marginTop:8,padding:'9px 14px',borderRadius:8,textAlign:'center',
            background:allPass?T.green+'18':rulesPass>0?T.orange+'18':T.red+'18',
            border:`1px solid ${allPass?T.green:rulesPass>0?T.orange:T.red}44`}}>
            <span style={{fontSize:13,fontWeight:800,color:allPass?T.green:rulesPass>0?T.orange:T.red}}>
              {allPass?'✓ ALL RULES PASS — READY FOR ACCREDITATION':`${rulesPass} of ${rules.length} rules passing`}
            </span>
          </div>
        </div>

        <div>
          <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:8}}>
            <div style={{fontSize:11,color:T.muted,fontWeight:700,letterSpacing:1}}>CHAPTER HEALTH</div>
            <div style={{fontSize:11,color:T.muted}}>{relevantScored}/{relevantOEs.length} relevant OEs scored</div>
          </div>
          <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fill,minmax(140px,1fr))',gap:6}}>
            {chapterStats.map(c=>{
              const col=c.avg===null?T.muted:c.pass?T.green:T.orange;
              return(
                <div key={c.key} style={{background:T.panel,border:`1px solid ${col}44`,borderRadius:8,padding:'10px 12px'}}>
                  <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:3}}>
                    <span style={{color:ECO_COLOR,fontWeight:800,fontSize:14}}>{c.key}</span>
                    <span style={{fontSize:13,fontWeight:700,color:col}}>{c.avg!==null?c.avg.toFixed(1)+' / 5':'—'}</span>
                  </div>
                  <div style={{fontSize:10,color:T.muted,marginBottom:2}}>{c.scoredCount} of {c.relevantCount} relevant scored</div>
                  <div style={{fontSize:10,color:T.muted,marginBottom:4}}>{c.totalCount} total OEs in chapter</div>
                  <div style={{height:4,borderRadius:2,background:T.border,overflow:'hidden',marginBottom:4}}>
                    <div style={{height:'100%',width:`${c.relevantCount>0?Math.round(c.scoredCount/c.relevantCount*100):0}%`,background:col,borderRadius:2,transition:'width 0.3s'}}/>
                  </div>
                  <div style={{fontSize:10,color:T.muted,lineHeight:1.4}}>{c.name}</div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );

    const renderScoreOEs=()=>(
      <div style={{padding:'12px 16px 80px'}}>
        <input
          value={ecoFullSearch} onChange={e=>setEcoFullSearch(e.target.value)}
          placeholder="Search by OE code or keyword…"
          style={{width:'100%',padding:'9px 12px',borderRadius:8,border:`1px solid ${T.border}`,
            background:T.panel2,color:T.text,fontSize:14,boxSizing:'border-box',marginBottom:10}}
        />
        <div style={{display:'flex',overflowX:'auto',gap:0,borderBottom:`1px solid ${T.border}`,marginBottom:8}}>
          {[{key:'all',count:ecoFullOes.length},...CHAPTERS.map(c=>({key:c.key,count:chapterOeCount(c.key)}))].map(tab=>(
            <button key={tab.key} onClick={()=>setEcoFullChapter(tab.key)}
              style={{padding:'6px 10px',border:'none',cursor:'pointer',whiteSpace:'nowrap',background:'transparent',
                fontSize:12,fontWeight:600,
                color:ecoFullChapter===tab.key?ECO_COLOR:T.muted,
                borderBottom:ecoFullChapter===tab.key?`2px solid ${ECO_COLOR}`:'2px solid transparent'}}>
              {tab.key==='all'?'All':tab.key} ({tab.count})
            </button>
          ))}
        </div>
        <div style={{display:'flex',gap:6,flexWrap:'wrap',marginBottom:12,alignItems:'center'}}>
          {['all',...LEVELS].map(lv=>(
            <button key={lv} onClick={()=>setEcoFullLevel(lv)}
              style={{padding:'3px 11px',borderRadius:20,cursor:'pointer',
                border:`1px solid ${ecoFullLevel===lv?(lv==='all'?ECO_COLOR:levelColor(lv)):T.border}`,
                background:ecoFullLevel===lv?(lv==='all'?ECO_COLOR+'22':levelColor(lv)+'22'):'transparent',
                color:ecoFullLevel===lv?(lv==='all'?ECO_COLOR:levelColor(lv)):T.muted,
                fontSize:12,fontWeight:600}}>
              {lv==='all'?'All Levels':lv}
            </button>
          ))}
          <span style={{marginLeft:'auto',fontSize:11,color:T.muted}}>{filteredOes.length} OEs</span>
        </div>

        {ecoFullLoading ? (
          <div style={{textAlign:'center',padding:40,color:T.muted}}>Loading OEs…</div>
        ) : Object.keys(byStandard).length===0 ? (
          <div style={{textAlign:'center',padding:40,color:T.muted}}>No OEs match the current filter.</div>
        ) : (
          Object.entries(byStandard).map(([stdCode,{std,oes:stdOes}])=>{
            const stdScoredOes=stdOes.filter(oe=>ecoFullScores[oe.oe_code]);
            const stdAvg=stdScoredOes.length>0?stdScoredOes.reduce((a,oe)=>a+ecoFullScores[oe.oe_code],0)/stdScoredOes.length:null;
            const stdLowCount=stdOes.filter(oe=>ecoFullScores[oe.oe_code]&&ecoFullScores[oe.oe_code]<=2).length;
            const stdFails=(stdAvg!==null&&stdAvg<4)||(stdLowCount>maxLowPerStd);
            const stdBorder=stdAvg===null?T.border:stdFails?T.red:T.green;
            return (
              <div key={stdCode} style={{marginBottom:14}}>
                <div style={{background:T.panel,border:`1px solid ${stdBorder}`,borderRadius:10,
                  padding:'9px 13px',marginBottom:5,display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:10}}>
                  <div style={{flex:1}}>
                    <span style={{color:ECO_COLOR,fontWeight:800,fontSize:13,marginRight:8}}>{stdCode}</span>
                    <span style={{color:T.text,fontSize:13,lineHeight:1.5}}>{std}</span>
                  </div>
                  <div style={{flexShrink:0,textAlign:'right'}}>
                    {stdAvg!==null&&<div style={{fontSize:12,fontWeight:700,color:stdAvg>=4?T.green:T.red}}>avg {stdAvg.toFixed(1)}</div>}
                    {stdLowCount>maxLowPerStd&&<div style={{fontSize:10,color:T.red}}>{stdLowCount} OE(s) ≤2</div>}
                    <div style={{fontSize:10,color:T.muted}}>{stdScoredOes.length}/{stdOes.length} scored</div>
                  </div>
                </div>
                {stdOes.map(oe=>{
                  const sc=ecoFullScores[oe.oe_code]||0;
                  const saving=ecoFullScoreSaving[oe.oe_code];
                  const catCap=oe.category?oe.category[0].toUpperCase()+oe.category.slice(1):'';
                  const lc=levelColor(catCap);
                  const rowBorder=sc>=4?T.green:sc===3?T.orange:sc>=1?T.red:T.border;
                  return (
                    <div key={oe.oe_code} style={{background:T.panel2,border:`1px solid ${rowBorder}`,
                      borderRadius:8,padding:'10px 12px',marginBottom:5,marginLeft:8}}>
                      <div style={{display:'flex',alignItems:'center',gap:7,marginBottom:5,flexWrap:'wrap'}}>
                        <span style={{fontSize:12,fontWeight:700,color:T.muted,fontFamily:'monospace'}}>{oe.oe_code}</span>
                        <span style={{fontSize:11,padding:'1px 7px',borderRadius:10,
                          background:lc+'22',color:lc,border:`1px solid ${lc}44`,fontWeight:700}}>{catCap}</span>
                        {sc>0
                          ?<span style={{fontSize:11,fontWeight:700,color:SCORE_COLORS[sc],
                              padding:'1px 8px',borderRadius:8,background:SCORE_COLORS[sc]+'18',border:`1px solid ${SCORE_COLORS[sc]}44`}}>
                              {sc} – {SCORE_LABELS[sc]}
                            </span>
                          :<span style={{fontSize:11,color:T.muted}}>Not scored</span>
                        }
                        {saving&&<span style={{fontSize:11,color:T.muted,fontStyle:'italic'}}>saving…</span>}
                        <button type="button" onClick={e=>{e.stopPropagation();setEcoFullShowTip(p=>({...p,[oe.oe_code]:!p[oe.oe_code]}));}}
                          style={{marginLeft:'auto',padding:'3px 10px',borderRadius:7,fontSize:11,cursor:'pointer',
                            background:ecoFullShowTip[oe.oe_code]?T.blue+'22':'transparent',
                            border:`1px solid ${ecoFullShowTip[oe.oe_code]?T.blue:T.muted}`,
                            color:ecoFullShowTip[oe.oe_code]?T.blue:T.muted}}>
                          {ecoFullShowTip[oe.oe_code]?'▲ Hide':'▶ How to achieve'}
                        </button>
                      </div>
                      <div style={{fontSize:13,color:T.text,lineHeight:1.6,marginBottom:8}}>{oe.oe_text}</div>
                      {ecoFullShowTip[oe.oe_code] && EcoTipBox(oe)}
                      <div style={{display:'flex',gap:4,flexWrap:'wrap'}}>
                        {[1,2,3,4,5].map(n=>(
                          <button key={n} onClick={()=>handleScore(oe.oe_code,n)}
                            style={{padding:'4px 9px',borderRadius:7,fontSize:11,fontWeight:700,cursor:'pointer',
                              background:sc===n?`${SCORE_COLORS[n]}28`:T.panel,
                              border:`1px solid ${sc===n?SCORE_COLORS[n]:SCORE_COLORS[n]+'40'}`,
                              color:sc===n?SCORE_COLORS[n]:T.muted,transition:'all 0.12s'}}>
                            {n} – {SCORE_LABELS[n]}
                          </button>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            );
          })
        )}
      </div>
    );

    const gapSeverity = oe => {
      const sc = ecoFullScores[oe.oe_code]||0;
      if(sc===0) return null;
      if(oe.category==='core') return sc<=3 ? 'CRITICAL' : null;
      if(oe.category==='commitment') return sc<=2 ? 'HIGH' : sc===3 ? 'MEDIUM' : null;
      return sc<=3 ? 'LOW' : null;
    };

    const allGaps = ecoFullOes
      .map(oe=>({oe, sev:gapSeverity(oe)}))
      .filter(({sev})=>sev!==null)
      .map(({oe,sev})=>({
        oe_code: oe.oe_code, oe_text: oe.oe_text, level: oe.category,
        standard_code: oe.standard_code, severity: sev,
        score: ecoFullScores[oe.oe_code]||0,
      }));

    const renderFixGaps = () => {
      const qg = ecoFullGapSearch.toLowerCase().trim();
      const filtered = allGaps.filter(g=>{
        const matchSev = ecoFullGapFilter==='ALL' || g.severity===ecoFullGapFilter;
        const matchQ   = !qg || g.oe_code.toLowerCase().includes(qg) || g.oe_text.toLowerCase().includes(qg);
        return matchSev && matchQ;
      });

      return (
        <div style={{padding:'12px 16px 80px'}}>
          <input value={ecoFullGapSearch} onChange={e=>setEcoFullGapSearch(e.target.value)}
            placeholder="Search gaps by OE code or keyword…"
            style={{width:'100%',padding:'10px 14px',borderRadius:8,border:`1px solid ${T.border}`,
              background:T.panel2,color:T.text,fontSize:14,marginBottom:10,boxSizing:'border-box'}}/>

          <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap',alignItems:'center'}}>
            {['ALL','CRITICAL','HIGH','MEDIUM','LOW'].map(s=>(
              <button key={s} onClick={()=>setEcoFullGapFilter(s)}
                style={{padding:'5px 14px',borderRadius:8,fontSize:12,cursor:'pointer',
                  background:ecoFullGapFilter===s?`${sevColor(s)}20`:'transparent',
                  border:`1px solid ${ecoFullGapFilter===s?sevColor(s):T.border}`,
                  color:ecoFullGapFilter===s?sevColor(s):T.muted}}>{s}</button>
            ))}
            <div style={{marginLeft:'auto',fontSize:13,color:T.muted}}>{allGaps.length} gaps</div>
          </div>

          {filtered.length===0 && (
            <div style={{textAlign:'center',color:T.muted,padding:'40px',fontSize:14}}>
              {allGaps.length===0 ? 'No gaps found. Score OEs first.' : 'No gaps at this severity level.'}
            </div>
          )}

          <div style={{display:'grid',gap:10}}>
            {filtered.map(g=>{
              const fc   = ecoFullCapaForm[g.oe_code]||{};
              const dbC  = ecoFullCapaDb[g.oe_code];
              const expanded = fc.expanded;
              const hasSaved = dbC || fc.saved;
              return (
                <div key={g.oe_code} style={{background:T.panel,border:`1px solid ${sevColor(g.severity)}25`,borderRadius:12,overflow:'hidden'}}>
                  <div style={{height:3,background:sevColor(g.severity)}}/>
                  <div style={{padding:'14px 16px'}}>
                    <div style={{display:'flex',gap:10,alignItems:'flex-start',marginBottom:8}}>
                      <div style={{flex:1}}>
                        <div style={{display:'flex',gap:8,alignItems:'center',marginBottom:4,flexWrap:'wrap'}}>
                          <span style={{fontFamily:'monospace',fontSize:13,fontWeight:700,color:lvColor(g.level)}}>{g.oe_code}</span>
                          <span style={{fontSize:11,padding:'2px 7px',borderRadius:5,background:`${sevColor(g.severity)}15`,color:sevColor(g.severity),fontWeight:700}}>{g.severity}</span>
                          <span style={{fontSize:11,padding:'2px 6px',borderRadius:5,background:`${lvColor(g.level)}18`,color:lvColor(g.level)}}>{g.level}</span>
                          {hasSaved&&<span style={{fontSize:11,padding:'2px 6px',borderRadius:5,background:T.green+'22',color:T.green}}>✓ CAPA saved</span>}
                        </div>
                        <div style={{fontSize:12,color:T.text,lineHeight:1.5}}>{g.oe_text}</div>
                      </div>
                      <div style={{textAlign:'center',flexShrink:0}}>
                        <div style={{fontSize:22,fontWeight:800,color:g.score<=2?T.red:g.score===3?T.orange:T.green}}>{g.score}</div>
                        <div style={{fontSize:7,color:T.muted}}>/ 5</div>
                      </div>
                    </div>

                    <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                      {!expanded && hasSaved ? (
                        <>
                          <button
                            onClick={()=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{
                              ...fc, expanded:true,
                              finding: fc.finding!==undefined ? fc.finding : (dbC?.finding||''),
                              action:  fc.action!==undefined  ? fc.action  : (dbC?.action_planned||''),
                              person:  fc.person!==undefined  ? fc.person  : (dbC?.responsible_person||''),
                              date:    fc.date!==undefined    ? fc.date    : (dbC?.target_date||''),
                            }}))}
                            style={{fontSize:12,color:T.gold,background:'transparent',border:`1px solid ${T.gold}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                            ✏️ Edit CAPA
                          </button>
                          <button
                            onClick={()=>deleteEcoFullCapa(g.oe_code)}
                            style={{fontSize:12,color:T.red,background:'transparent',border:`1px solid ${T.red}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                            🗑 Delete CAPA
                          </button>
                        </>
                      ) : expanded ? (
                        <button
                          onClick={()=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,expanded:false}}))}
                          style={{fontSize:12,color:T.muted,background:'transparent',border:`1px solid ${T.border}`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                          ▲ Hide CAPA
                        </button>
                      ) : (
                        <button
                          onClick={()=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,expanded:true}}))}
                          style={{fontSize:12,color:T.gold,background:'transparent',border:`1px solid ${T.gold}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                          ▼ Add CAPA
                        </button>
                      )}
                    </div>

                    {expanded&&(
                      <div style={{marginTop:12,display:'grid',gap:8}}>
                        {fc.saved&&<div style={{fontSize:12,color:T.green,padding:'6px 10px',background:T.green+'14',borderRadius:6}}>✓ CAPA saved successfully</div>}
                        <div>
                          <div style={{fontSize:11,color:T.muted,marginBottom:4}}>FINDING *</div>
                          <textarea value={fc.finding!==undefined ? fc.finding : (dbC?.finding||'')}
                            onChange={e=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,finding:e.target.value,saved:false}}))}
                            rows={2} placeholder="Describe the non-compliance finding…"
                            style={{width:'100%',padding:'8px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:'vertical',boxSizing:'border-box'}}/>
                        </div>
                        <div>
                          <div style={{fontSize:11,color:T.muted,marginBottom:4}}>ACTION PLANNED *</div>
                          <textarea value={fc.action!==undefined ? fc.action : (dbC?.action_planned||'')}
                            onChange={e=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,action:e.target.value,saved:false}}))}
                            rows={2} placeholder="Corrective action to be taken…"
                            style={{width:'100%',padding:'8px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:'vertical',boxSizing:'border-box'}}/>
                        </div>
                        <div style={{display:'flex',gap:8,flexWrap:'wrap',alignItems:'flex-end'}}>
                          <div style={{flex:1,minWidth:140}}>
                            <div style={{fontSize:11,color:T.muted,marginBottom:4}}>RESPONSIBLE PERSON</div>
                            <input value={fc.person!==undefined ? fc.person : (dbC?.responsible_person||'')}
                              onChange={e=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,person:e.target.value,saved:false}}))}
                              placeholder="Name / Designation"
                              style={{width:'100%',padding:'7px 10px',borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:'border-box'}}/>
                          </div>
                          <div>
                            <div style={{fontSize:11,color:T.muted,marginBottom:4}}>TARGET DATE</div>
                            <input type="date" value={fc.date!==undefined ? fc.date : (dbC?.target_date||'')}
                              onChange={e=>setEcoFullCapaForm(p=>({...p,[g.oe_code]:{...fc,date:e.target.value,saved:false}}))}
                              style={{padding:'7px 10px',borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
                          </div>
                          <button onClick={()=>saveEcoFullCapa(g.oe_code)}
                            disabled={ecoFullCapaSaving[g.oe_code]||!(fc.finding!==undefined?fc.finding:dbC?.finding)||!(fc.action!==undefined?fc.action:dbC?.action_planned)}
                            style={{padding:'7px 20px',borderRadius:10,background:`linear-gradient(135deg,${T.green},#3d9e6e)`,
                              border:'none',color:T.bg,fontSize:14,fontWeight:700,cursor:'pointer',opacity:1}}>
                            {ecoFullCapaSaving[g.oe_code]?'Saving…':'Save CAPA →'}
                          </button>
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
    };

    return (
      <div style={{background:T.bg,minHeight:'100vh',color:T.text,fontFamily:'Segoe UI,system-ui,sans-serif'}}>
        <div style={{display:'flex',alignItems:'center',borderBottom:`1px solid ${T.border}`,padding:'0 16px',background:T.panel}}>
          {[
            {key:'dashboard',label:'📊 Dashboard'},
            {key:'scoring',  label:'✏️ Score OEs'},
            {key:'fixgaps',  label:`🔧 Fix Gaps${allGaps.length>0?' ('+allGaps.length+')':''}`},
            {key:'kpis',     label:'📈 KPIs'},
          ].map(tab=>(
            <button key={tab.key} onClick={()=>setEcoFullTab(tab.key)}
              style={{padding:'12px 16px',border:'none',cursor:'pointer',background:'transparent',fontSize:13,fontWeight:600,
                color:ecoFullTab===tab.key?ECO_COLOR:T.muted,
                borderBottom:ecoFullTab===tab.key?`2px solid ${ECO_COLOR}`:'2px solid transparent'}}>
              {tab.label}
            </button>
          ))}
          <button onClick={generateEcoFullPDF} disabled={ecoFullPdfLoading}
            style={{marginLeft:'auto',padding:'6px 14px',borderRadius:7,border:`1px solid ${ECO_COLOR}`,
              background:'transparent',color:ECO_COLOR,fontSize:12,fontWeight:700,cursor:ecoFullPdfLoading?'default':'pointer',
              opacity:ecoFullPdfLoading?0.6:1,whiteSpace:'nowrap'}}>
            {ecoFullPdfLoading ? '⏳ Generating…' : '⬇ Download Gap Report'}
          </button>
        </div>
        {ecoFullTab==='dashboard' ? renderDashboard() : ecoFullTab==='scoring' ? renderScoreOEs() : ecoFullTab==='kpis' ? <EcoFullKpiTab hospitalId={context?.hospitalId}/> : renderFixGaps()}
      </div>
    );
  };

  // ── HCO ELC TAB ──────────────────────────────────────────────────────────
  const renderHCOTab = () => {

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
          {ch:'AAC',name:'Access, Assessment & Continuity of Care',oes:87},
          {ch:'COP',name:'Care of Patients',oes:135},
          {ch:'MOM',name:'Management of Medication',oes:68},
          {ch:'PRE',name:'Patient Rights & Education',oes:52},
          {ch:'IPC',name:'Infection Prevention & Control',oes:49},
          {ch:'PSQ',name:'Patient Safety & Quality Improvement',oes:46},
          {ch:'ROM',name:'Responsibilities of Management',oes:37},
          {ch:'FMS',name:'Facility Management & Safety',oes:43},
          {ch:'HRM',name:'Human Resource Management',oes:76},
          {ch:'IMS',name:'Information Management System',oes:45},
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
      <div style={{background:T.blueD,border:`1px solid ${T.blue}`,borderRadius:10,padding:14}}>
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
          <div style={{marginTop:8,padding:'8px 12px',background:T.gold+'18',borderRadius:8,border:`1px solid ${T.gold}44`}}>
            <span style={{color:T.gold,fontWeight:600,fontSize:13}}>Note: </span>
            <span style={{color:T.text,fontSize:13}}>In the first certification cycle, HCOs ({'>'} 50 beds) must meet both <strong style={{color:T.text}}>Core AND Commitment</strong> criteria. SHCOs (≤ 50 beds) need only Core criteria in their first cycle.</span>
          </div>
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
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:14}}>📋 OE Compliance Summary</div>
        {(()=>{
          const oeTotal    = HCO_ELC_OE_LIST.length;
          const oeMet      = HCO_ELC_OE_LIST.filter(oe => elcScores[oe.code] === 'met').length;
          const oePartial  = HCO_ELC_OE_LIST.filter(oe => elcScores[oe.code] === 'partial').length;
          const oeNotMet   = HCO_ELC_OE_LIST.filter(oe => elcScores[oe.code] === 'not_met').length;
          const oeUnscored = oeTotal - oeMet - oePartial - oeNotMet;
          const oeCoreCodes = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code] === 'CORE');
          const oeCommCodes = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code] === 'Commitment');
          const oeExclCodes = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code] === 'Excellence');
          const oeCoreMet  = oeCoreCodes.filter(oe => elcScores[oe.code] === 'met').length;
          const oeCommMet  = oeCommCodes.filter(oe => elcScores[oe.code] === 'met').length;
          const oeExclMet  = oeExclCodes.filter(oe => elcScores[oe.code] === 'met').length;
          const oeCoreTotal= oeCoreCodes.length || 124;
          const oeCommTotal= oeCommCodes.length || 36;
          const oeExclTotal= oeExclCodes.length || 29;
          const oeMetPct   = Math.round((oeMet / oeTotal) * 100);
          const oeCoreNotMet = oeCoreTotal - oeCoreMet;
          let oeVerdict, oeVerdictColor;
          if (oeMet === oeTotal) { oeVerdict = '✓ Ready for Excellence'; oeVerdictColor = T.gold; }
          else if (oeCoreMet === oeCoreTotal && oeCommMet === oeCommTotal) { oeVerdict = '✓ Ready for 1st Cycle Certification'; oeVerdictColor = T.green; }
          else { const oeCoreLeft=oeCoreTotal-oeCoreMet,oeCommLeft=oeCommTotal-oeCommMet,oeParts=[];if(oeCoreLeft>0)oeParts.push(`${oeCoreLeft} Core OE${oeCoreLeft!==1?'s':''}`);if(oeCommLeft>0)oeParts.push(`${oeCommLeft} Commitment OE${oeCommLeft!==1?'s':''}`);oeVerdict=`${oeParts.join(' + ')} not yet met for 1st Cycle`;oeVerdictColor=T.muted; }
          return (
            <>
              {/* Row 1 — overall counts */}
              <div style={{display:'flex',gap:10,flexWrap:'wrap',marginBottom:10}}>
                {[
                  {label:`✓ Met`,val:oeMet,color:'#4caf7d'},
                  {label:`~ Partial`,val:oePartial,color:'#f4a441'},
                  {label:`✗ Not Met`,val:oeNotMet,color:'#e05a5a'},
                  {label:`— Unscored`,val:oeUnscored,color:T.muted},
                ].map(({label,val,color})=>(
                  <div key={label} style={{background:T.panel2,borderRadius:8,padding:'8px 14px',border:`1px solid ${T.border}`,textAlign:'center',flex:1,minWidth:70}}>
                    <div style={{fontSize:18,fontWeight:800,color}}>{val}</div>
                    <div style={{fontSize:11,color,fontWeight:600}}>{label}</div>
                    <div style={{fontSize:10,color:T.muted}}>of {oeTotal}</div>
                  </div>
                ))}
              </div>
              {/* Progress bar */}
              <div style={{height:7,borderRadius:4,background:T.border,overflow:'hidden',marginBottom:12}}>
                <div style={{height:'100%',width:`${oeMetPct}%`,background:'#4caf7d',borderRadius:4,transition:'width 0.3s'}}/>
              </div>
              {/* Row 2 — level breakdown */}
              <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:8,marginBottom:12}}>
                {[
                  {label:'CORE',total:oeCoreTotal,met:oeCoreMet,color:'#e05a5a'},
                  {label:'Commitment',total:oeCommTotal,met:oeCommMet,color:'#f4a441'},
                  {label:'Excellence',total:oeExclTotal,met:oeExclMet,color:'#c9a84c'},
                ].map(({label,total:t,met,color})=>(
                  <div key={label} style={{background:T.panel2,borderRadius:8,padding:'8px 10px',border:`1px solid ${T.border}`,textAlign:'center'}}>
                    <div style={{fontSize:10,fontWeight:700,color,letterSpacing:0.5,marginBottom:4}}>{label}</div>
                    <div style={{fontSize:16,fontWeight:800,color:'#4caf7d'}}>{met}</div>
                    <div style={{fontSize:11,color:T.muted}}>Met / {t}</div>
                  </div>
                ))}
              </div>
              {/* Row 3 — cycle readiness badge */}
              <div style={{padding:'10px 14px',borderRadius:8,background:`${oeVerdictColor}18`,border:`1px solid ${oeVerdictColor}44`,textAlign:'center'}}>
                <span style={{fontSize:13,fontWeight:700,color:oeVerdictColor}}>{oeVerdict}</span>
              </div>
            </>
          );
        })()}
      </div>

      <div style={{background:T.panel,borderRadius:12,padding:16,border:`1px solid ${T.border}`}}>
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>💰 HCO ELC Certification Fee</div>
        <div style={{background:T.panel2,borderRadius:10,padding:14,border:`1px solid ${T.gold}44`}}>
          <div style={{color:T.muted,fontSize:13,marginBottom:10}}>{HCO_FEE.label}</div>
          <div style={{color:T.muted,fontSize:13,marginBottom:10}}>Fees vary by bed strength and are updated periodically by NABH.</div>
          <a
            href="https://nabh.co/accreditations-certifications-and-empanelments/"
            target="_blank"
            rel="noopener noreferrer"
            style={{color:T.blue,fontWeight:600,fontSize:13,textDecoration:'underline'}}
          >
            View current fee structure on the official NABH website →
          </a>
          <div style={{fontSize:12,color:T.muted,marginTop:10}}>
            18% GST applicable. Fee is non-refundable and non-transferable. Focus assessment and re-issue charges apply separately.
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
                ['ELC Fee','See nabh.co','See nabh.co'],
                ['Certification Validity','2 Years','2 Years'],
                ['Portal','hope.qcin.org','hope.qcin.org'],
                ['Upgrade Path','NABH 6th Ed. (639 OEs)','NABH Hospital (408 OEs)'],
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
        <div style={{color:T.white,fontWeight:700,fontSize:16,marginBottom:12}}>📖 HCO ELC — 10 Chapters · 189 OEs (2nd Edition, Jan 2026)</div>
        <div style={{display:'grid',gap:6}}>
          {HCO_ELC_CHAPTER_SUMMARY.map(c => (
            <div key={c.ch} style={{background:T.panel2,borderRadius:8,padding:'10px 12px',border:`1px solid ${T.border}`}}>
              <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:3}}>
                <span style={{color:T.gold,fontWeight:700,fontSize:14,minWidth:36}}>{c.ch}</span>
                <span style={{color:T.text,fontSize:14,fontWeight:600,flex:1}}>{c.name}</span>
                <span style={{color:T.blue,fontWeight:600,fontSize:13,whiteSpace:'nowrap'}}>{c.oes} OEs</span>
              </div>
              <div style={{color:T.muted,fontSize:13,lineHeight:1.4,paddingLeft:44}}>{c.desc}</div>
            </div>
          ))}
        </div>
        <div style={{marginTop:10,color:T.muted,fontSize:13,textAlign:'center'}}>Source: NABH ELC Standards for HCOs — 2nd Edition (Effective January 2026)</div>
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
          <div style={{color:'#c8dcea',fontSize:13}}>Unlike SHCOs, HCOs ({'>'} 50 beds) must have the Pollution Control Board License for water and Air Pollution. Mark as N/A only if NABH formally exempts your facility.</div>
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
        <div style={{color:'#c8dcea',fontSize:14,lineHeight:1.6}}>
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
        {phase:'Month 4–5',action:'Register on hope.qcin.org. Fill all 7 parts. Upload portal + mobile app documents. Pay the applicable certification fee (see nabh.co for current rates) + 18% GST.',color:T.orange},
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

  const toElcDotCode = code => code.replace(/^([A-Z]+)(\d+)([a-z]+)$/, '$1.$2.$3');
  const elcLevelColor = lvl => lvl === 'CORE' ? '#e05a5a' : lvl === 'Commitment' ? '#f4a441' : '#c9a84c';

  const setElcScore = async (code, status) => {
    const prev = elcScores[code];
    setElcScores(p => ({...p, [code]: status}));
    setElcScoreSaving(p => ({...p, [code]: true}));
    const { error } = await supabase.from("elc_scores").upsert(
      { hospital_id: context.hospitalId, oe_code: code, status, programme: "HCO_ELC", updated_at: new Date().toISOString(), updated_by: user.id },
      { onConflict: "hospital_id,oe_code,programme" }
    );
    if (error) setElcScores(p => ({...p, [code]: prev}));
    setElcScoreSaving(p => ({...p, [code]: false}));
  };

  const clearElcScore = async (code) => {
    const prev = elcScores[code];
    setElcScores(p => { const n = {...p}; delete n[code]; return n; });
    setElcScoreSaving(p => ({...p, [code]: true}));
    const { error } = await supabase.from("elc_scores")
      .delete()
      .eq("hospital_id", context.hospitalId)
      .eq("oe_code", code)
      .eq("programme", "HCO_ELC");
    if (error) setElcScores(p => ({...p, [code]: prev}));
    setElcScoreSaving(p => ({...p, [code]: false}));
  };

  const toggleElcOe = async (code) => {
    const isOpen = hcoOeExpanded[code];
    setHcoOeExpanded(p => ({...p, [code]: !isOpen}));
    if (!isOpen && hcoOeTips[code] === undefined && !hcoOeTipsLoading[code]) {
      const local = ELC_OE_TIPS[code];
      if (local) {
        setHcoOeTips(p => ({...p, [code]: {...local, oe_level: hcoOeLevels[code] || null}}));
      } else {
        setHcoOeTipsLoading(p => ({...p, [code]: true}));
        const { data } = await supabase
          .from('achieve_tips')
          .select('tip_1, tip_2, tip_3, tip_4, oe_level')
          .eq('oe_code', code)
          .eq('programme', 'ELC')
          .limit(1)
          .maybeSingle();
        const merged = data ? {...data, oe_level: data.oe_level || hcoOeLevels[code] || null} : null;
        setHcoOeTips(p => ({...p, [code]: merged}));
        setHcoOeTipsLoading(p => ({...p, [code]: false}));
      }
    }
  };

  const renderOEBrowser = () => {
    const q = hcoOeSearch.toLowerCase().trim();
    const filtered = HCO_ELC_OE_LIST.filter(oe => {
      const chapterMatch = hcoOeChapter === 'all' || oe.chapter === hcoOeChapter;
      const textMatch = !q || oe.code.toLowerCase().includes(q) || oe.text.toLowerCase().includes(q);
      return chapterMatch && textMatch;
    });
    const chapters = HCO_ELC_CHAPTER_SUMMARY.map(c => c.ch);
    const grouped = chapters.map(ch => ({
      ch,
      name: HCO_ELC_CHAPTER_SUMMARY.find(c => c.ch === ch)?.name || ch,
      oes: filtered.filter(oe => oe.chapter === ch),
    })).filter(g => g.oes.length > 0);

    // Progress calculations
    const total       = HCO_ELC_OE_LIST.length;
    const totalMet    = HCO_ELC_OE_LIST.filter(oe => elcScores[oe.code] === 'met').length;
    const totalPartial= HCO_ELC_OE_LIST.filter(oe => elcScores[oe.code] === 'partial').length;
    const totalNotMet = HCO_ELC_OE_LIST.filter(oe => elcScores[oe.code] === 'not_met').length;
    const totalUnscored = total - totalMet - totalPartial - totalNotMet;
    const coreCodes   = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code] === 'CORE');
    const commCodes   = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code] === 'Commitment');
    const exclCodes   = HCO_ELC_OE_LIST.filter(oe => hcoOeLevels[oe.code] === 'Excellence');
    const coreMet     = coreCodes.filter(oe => elcScores[oe.code] === 'met').length;
    const corePartial = coreCodes.filter(oe => elcScores[oe.code] === 'partial').length;
    const coreNM      = coreCodes.filter(oe => elcScores[oe.code] === 'not_met').length;
    const commMet     = commCodes.filter(oe => elcScores[oe.code] === 'met').length;
    const commPartial = commCodes.filter(oe => elcScores[oe.code] === 'partial').length;
    const commNM      = commCodes.filter(oe => elcScores[oe.code] === 'not_met').length;
    const exclMet     = exclCodes.filter(oe => elcScores[oe.code] === 'met').length;
    const exclPartial = exclCodes.filter(oe => elcScores[oe.code] === 'partial').length;
    const exclNM      = exclCodes.filter(oe => elcScores[oe.code] === 'not_met').length;
    const coreTotal   = coreCodes.length || 124;
    const commTotal   = commCodes.length || 36;
    const exclTotal   = exclCodes.length || 29;
    const metPct      = Math.round((totalMet / total) * 100);
    const coreNotMet  = coreTotal - coreMet; // includes partial + not_met + unscored

    let verdict = null, verdictColor = T.muted;
    if (totalMet === total) {
      verdict = '✓ Ready for Excellence'; verdictColor = T.gold;
    } else if (coreMet === coreTotal && commMet === commTotal) {
      verdict = '✓ Ready for 1st Cycle Certification'; verdictColor = T.green;
    } else {
      const coreLeft = coreTotal - coreMet;
      const commLeft = commTotal - commMet;
      const parts = [];
      if (coreLeft > 0) parts.push(`${coreLeft} Core OE${coreLeft !== 1 ? 's' : ''}`);
      if (commLeft > 0) parts.push(`${commLeft} Commitment OE${commLeft !== 1 ? 's' : ''}`);
      verdict = `${parts.join(' + ')} not yet met for 1st Cycle`; verdictColor = T.muted;
    }

    const SCORE_BTNS = [
      {s:'met',    label:'✓ Met',     color:'#4caf7d'},
      {s:'partial',label:'~ Partial', color:'#f4a441'},
      {s:'not_met',label:'✗ Not Met', color:'#e05a5a'},
    ];

    return (
      <div style={{padding:16}}>

        {/* Progress summary */}
        <div style={{background:T.panel2,border:`1px solid ${T.border}`,borderRadius:10,padding:'12px 14px',marginBottom:14}}>
          {/* Row 1 — counts */}
          <div style={{display:'flex',gap:10,flexWrap:'wrap',alignItems:'center',marginBottom:8}}>
            <span style={{fontSize:12,fontWeight:700,color:'#4caf7d'}}>✓ {totalMet} Met</span>
            <span style={{fontSize:12,fontWeight:700,color:'#f4a441'}}>~ {totalPartial} Partial</span>
            <span style={{fontSize:12,fontWeight:700,color:'#e05a5a'}}>✗ {totalNotMet} Not Met</span>
            <span style={{fontSize:12,fontWeight:700,color:T.muted}}>— {totalUnscored} Unscored</span>
            <span style={{marginLeft:'auto',fontSize:11,fontWeight:700,color:verdictColor}}>{verdict}</span>
          </div>
          {/* Progress bar — fill = met / 189 */}
          <div style={{height:7,borderRadius:4,background:T.border,overflow:'hidden',marginBottom:10}}>
            <div style={{height:'100%',width:`${metPct}%`,background:'#4caf7d',borderRadius:4,transition:'width 0.3s'}}/>
          </div>
          {/* Row 2 — level breakdown */}
          <div style={{display:'grid',gridTemplateColumns:'1fr 1fr 1fr',gap:8}}>
            {[
              {label:'CORE',total:coreTotal,met:coreMet,partial:corePartial,nm:coreNM,color:'#e05a5a'},
              {label:'Commitment',total:commTotal,met:commMet,partial:commPartial,nm:commNM,color:'#f4a441'},
              {label:'Excellence',total:exclTotal,met:exclMet,partial:exclPartial,nm:exclNM,color:'#c9a84c'},
            ].map(({label,total:t,met,partial,nm,color}) => (
              <div key={label} style={{background:T.panel,borderRadius:7,padding:'7px 9px',border:`1px solid ${T.border}`}}>
                <div style={{fontSize:10,fontWeight:700,color,marginBottom:4,letterSpacing:0.5}}>{label} (/{t})</div>
                <div style={{fontSize:11,color:'#4caf7d'}}>✓ {met} Met</div>
                <div style={{fontSize:11,color:'#f4a441'}}>~ {partial} Partial</div>
                <div style={{fontSize:11,color:'#e05a5a'}}>✗ {nm} Not Met</div>
              </div>
            ))}
          </div>
        </div>

        <div style={{marginBottom:12,display:'flex',gap:8,flexDirection:'column'}}>
          <input
            value={hcoOeSearch} onChange={e => setHcoOeSearch(e.target.value)}
            placeholder="Search by OE code or text…"
            style={{width:'100%',padding:'9px 12px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:'border-box'}}
          />
          <div style={{display:'flex',gap:6,flexWrap:'wrap'}}>
            <button onClick={() => setHcoOeChapter('all')}
              style={{padding:'4px 10px',borderRadius:20,border:`1px solid ${hcoOeChapter==='all'?T.gold:T.border}`,background:hcoOeChapter==='all'?T.gold+'22':'transparent',color:hcoOeChapter==='all'?T.gold:T.muted,fontSize:12,cursor:'pointer'}}>
              All ({HCO_ELC_OE_LIST.length})
            </button>
            {HCO_ELC_CHAPTER_SUMMARY.map(c => (
              <button key={c.ch} onClick={() => setHcoOeChapter(c.ch)}
                style={{padding:'4px 10px',borderRadius:20,border:`1px solid ${hcoOeChapter===c.ch?T.gold:T.border}`,background:hcoOeChapter===c.ch?T.gold+'22':'transparent',color:hcoOeChapter===c.ch?T.gold:T.muted,fontSize:12,cursor:'pointer'}}>
                {c.ch} ({c.oes})
              </button>
            ))}
          </div>
        </div>

        {filtered.length === 0 ? (
          <div style={{color:T.muted,fontSize:14,textAlign:'center',padding:24}}>No OEs match your search.</div>
        ) : (
          <div style={{display:'flex',flexDirection:'column',gap:16}}>
            {grouped.map(g => (
              <div key={g.ch}>
                <div style={{color:T.gold,fontWeight:700,fontSize:14,marginBottom:6,display:'flex',alignItems:'center',gap:8}}>
                  <span>{g.ch}</span>
                  <span style={{color:T.muted,fontWeight:400,fontSize:13}}>{g.name}</span>
                  <span style={{marginLeft:'auto',color:T.blue,fontSize:12}}>{g.oes.length} OEs</span>
                </div>
                <div style={{display:'flex',flexDirection:'column',gap:4}}>
                  {g.oes.map(oe => {
                    const isOpen   = !!hcoOeExpanded[oe.code];
                    const tips     = hcoOeTips[oe.code];
                    const loading  = !!hcoOeTipsLoading[oe.code];
                    const lvl      = hcoOeLevels[oe.code] || tips?.oe_level || null;
                    const lvlColor = lvl ? elcLevelColor(lvl) : T.muted;
                    const scoreVal = elcScores[oe.code] || null;
                    const saving   = !!elcScoreSaving[oe.code];
                    const rowBorder = scoreVal === 'met' ? '#4caf7d' : scoreVal === 'partial' ? '#f4a441' : scoreVal === 'not_met' ? '#e05a5a' : isOpen ? T.blue : T.border;
                    return (
                      <div key={oe.code} style={{background:T.panel2,borderRadius:8,border:`1px solid ${rowBorder}`,overflow:'hidden',transition:'border-color 0.15s'}}>
                        <div style={{padding:'10px 12px'}}>
                          {/* Row 1: OE code + level badge + current score */}
                          <div style={{display:'flex',gap:8,alignItems:'center',marginBottom:6}}>
                            <span style={{color:T.gold,fontWeight:700,fontSize:13,fontFamily:'monospace'}}>{oe.code}</span>
                            {lvl && (
                              <span style={{fontSize:9,fontWeight:700,letterSpacing:0.5,padding:'1px 6px',borderRadius:4,background:`${lvlColor}20`,color:lvlColor,border:`1px solid ${lvlColor}40`}}>{lvl}</span>
                            )}
                            <div style={{marginLeft:'auto',display:'flex',gap:8,alignItems:'center'}}>
                              {scoreVal && <span style={{fontSize:11,fontWeight:700,color:scoreVal==='met'?'#4caf7d':scoreVal==='partial'?'#f4a441':'#e05a5a'}}>{scoreVal==='met'?'✓ Met':scoreVal==='partial'?'~ Partial':'✗ Not Met'}</span>}
                              <span onClick={()=>toggleElcOe(oe.code)} style={{cursor:'pointer',color:T.muted,fontSize:12,userSelect:'none'}}>{isOpen?'▲':'▼'}</span>
                            </div>
                          </div>
                          {/* Row 2: OE text */}
                          <div onClick={()=>toggleElcOe(oe.code)} style={{color:T.text,fontSize:13,lineHeight:1.5,marginBottom:10,cursor:'pointer'}}>{oe.text}</div>
                          {/* Row 3: scoring buttons */}
                          <div style={{display:'flex',gap:4,flexWrap:'wrap',alignItems:'center'}}>
                            {SCORE_BTNS.map(({s,label,color}) => {
                              const active = scoreVal === s;
                              return (
                                <button key={s}
                                  onClick={e => { e.stopPropagation(); if(!saving) setElcScore(oe.code, s); }}
                                  style={{padding:'4px 10px',borderRadius:5,fontSize:11,fontWeight:700,cursor:saving?'wait':'pointer',
                                    background: active ? color : 'transparent',
                                    border: `1px solid ${active ? color : T.border}`,
                                    color: active ? '#fff' : T.muted,
                                    opacity: saving ? 0.5 : 1,
                                    whiteSpace:'nowrap'}}>
                                  {label}
                                </button>
                              );
                            })}
                            {scoreVal && (
                              <button
                                onClick={e => { e.stopPropagation(); if(!saving) clearElcScore(oe.code); }}
                                style={{padding:'4px 10px',borderRadius:5,fontSize:11,fontWeight:700,cursor:saving?'wait':'pointer',
                                  background:'transparent',border:`1px solid ${T.border}`,color:T.muted,
                                  opacity:saving?0.5:1,whiteSpace:'nowrap'}}>
                                ✕ Clear
                              </button>
                            )}
                          </div>
                        </div>
                        {/* Row 4: Tips panel */}
                        {isOpen && (
                          <div style={{padding:'0 12px 12px'}}>
                            {loading ? (
                              <div style={{fontSize:12,color:T.muted,padding:'8px 0'}}>Loading…</div>
                            ) : tips ? (
                              <div style={{marginTop:4,background:T.blueD,border:`1px solid ${T.blue}20`,borderRadius:8,padding:'12px 14px'}}>
                                <div style={{fontSize:11,letterSpacing:2,color:T.blue,marginBottom:8}}>HOW TO ACHIEVE THIS OE</div>
                                {[tips.tip_1, tips.tip_2, tips.tip_3, tips.tip_4].map((tip, i) => (
                                  <div key={i} style={{display:'flex',gap:8,marginBottom:6,alignItems:'flex-start'}}>
                                    <div style={{width:18,height:18,borderRadius:'50%',background:`${T.blue}20`,border:`1px solid ${T.blue}40`,display:'flex',alignItems:'center',justifyContent:'center',flexShrink:0,fontSize:11,color:T.blue,fontWeight:700}}>{i+1}</div>
                                    <div style={{fontSize:13,color:T.text,lineHeight:1.6,paddingTop:1}}>{tip}</div>
                                  </div>
                                ))}
                              </div>
                            ) : null}
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        )}
        <div style={{marginTop:12,color:T.muted,fontSize:12,textAlign:'center'}}>
          {filtered.length} of {HCO_ELC_OE_LIST.length} OEs — NABH HCO ELC 2nd Edition (Jan 2026)
        </div>
      </div>
    );
  };

  // ── HCO ELC Fix Gaps ────────────────────────────────────────────────────
  const elcGapSeverity = (oe) => {
    const s   = elcScores[oe.code];
    const lvl = hcoOeLevels[oe.code];
    if (!s) return null;
    if (lvl === 'CORE')       return s === 'not_met' ? 'CRITICAL' : s === 'partial' ? 'HIGH'   : null;
    if (lvl === 'Commitment') return s === 'not_met' ? 'HIGH'     : s === 'partial' ? 'MEDIUM' : null;
    if (lvl === 'Excellence') return s === 'not_met' ? 'MEDIUM'   : s === 'partial' ? 'LOW'    : null;
    return null;
  };

  const allElcGaps = HCO_ELC_OE_LIST
    .map(oe => ({ oe, sev: elcGapSeverity(oe) }))
    .filter(({ sev }) => sev !== null)
    .map(({ oe, sev }) => ({
      oe_code:  oe.code,
      oe_text:  oe.text,
      level:    hcoOeLevels[oe.code] || '',
      severity: sev,
    }));

  const renderELCFixGaps = () => {
    const q = hcoElcGapSearch.toLowerCase().trim();
    const filtered = allElcGaps.filter(g => {
      const matchSev = hcoElcGapFilter === 'ALL' || g.severity === hcoElcGapFilter;
      const matchQ   = !q || g.oe_code.toLowerCase().includes(q) || g.oe_text.toLowerCase().includes(q);
      return matchSev && matchQ;
    });

    return (
      <div style={{padding:'12px 16px 80px'}}>
        <input
          value={hcoElcGapSearch}
          onChange={e => setHcoElcGapSearch(e.target.value)}
          placeholder="Search gaps by OE code (e.g. AAC.1.a) or keyword…"
          style={{width:'100%',padding:'10px 14px',borderRadius:8,border:`1px solid ${T.border}`,
            background:T.panel2,color:T.text,fontSize:14,marginBottom:10,boxSizing:'border-box'}}
        />

        <div style={{display:'flex',gap:8,marginBottom:14,flexWrap:'wrap',alignItems:'center'}}>
          {['ALL','CRITICAL','HIGH','MEDIUM','LOW'].map(s => (
            <button key={s} onClick={() => setHcoElcGapFilter(s)}
              style={{padding:'5px 14px',borderRadius:8,fontSize:12,cursor:'pointer',
                background: hcoElcGapFilter === s ? `${sevColor(s)}20` : 'transparent',
                border: `1px solid ${hcoElcGapFilter === s ? sevColor(s) : T.border}`,
                color:  hcoElcGapFilter === s ? sevColor(s) : T.muted}}>
              {s}
            </button>
          ))}
          <div style={{marginLeft:'auto',display:'flex',gap:8,alignItems:'center'}}>
            <span style={{fontSize:13,color:T.muted}}>{allElcGaps.length} gap{allElcGaps.length !== 1 ? 's' : ''}</span>
            <button onClick={generateElcPDF} disabled={elcPdfLoading}
              style={{padding:'6px 14px',borderRadius:7,border:`1px solid ${T.gold}`,
                background:'transparent',color:T.gold,fontSize:12,fontWeight:700,
                cursor:elcPdfLoading?'default':'pointer',opacity:elcPdfLoading?0.6:1,whiteSpace:'nowrap'}}>
              {elcPdfLoading?'⏳ Generating…':'⬇ Download Gap Report'}
            </button>
          </div>
        </div>

        {filtered.length === 0 && (
          <div style={{textAlign:'center',color:T.muted,padding:'40px 0',fontSize:14}}>
            {allElcGaps.length === 0 ? 'No gaps found. Score OEs in the OE Browser first.' : 'No gaps at this severity level.'}
          </div>
        )}

        <div style={{display:'grid',gap:10}}>
          {filtered.map(g => {
            const fc       = elcCapaForm[g.oe_code] || {};
            const dbC      = elcCapaDb[g.oe_code];
            const hasSaved = !!dbC;
            const expanded = fc.expanded;
            return (
              <div key={g.oe_code} style={{background:T.panel,border:`1px solid ${sevColor(g.severity)}25`,borderRadius:12,overflow:'hidden'}}>
                <div style={{height:3,background:sevColor(g.severity)}}/>
                <div style={{padding:'14px 16px'}}>
                  <div style={{display:'flex',gap:8,alignItems:'center',marginBottom:6,flexWrap:'wrap'}}>
                    <span style={{fontFamily:'monospace',fontSize:13,fontWeight:700,color:elcLevelColor(g.level)}}>
                      {toElcDotCode(g.oe_code)}
                    </span>
                    <span style={{fontSize:11,padding:'2px 7px',borderRadius:5,fontWeight:700,
                      background:`${sevColor(g.severity)}15`,color:sevColor(g.severity)}}>
                      {g.severity}
                    </span>
                    <span style={{fontSize:11,padding:'2px 6px',borderRadius:5,
                      background:`${elcLevelColor(g.level)}18`,color:elcLevelColor(g.level)}}>
                      {g.level}
                    </span>
                    {hasSaved && <span style={{fontSize:11,padding:'2px 6px',borderRadius:5,background:T.green+'22',color:T.green}}>✓ CAPA saved</span>}
                  </div>
                  <div style={{fontSize:13,color:T.text,lineHeight:1.6,marginBottom:10}}>{g.oe_text}</div>
                  <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                    {!expanded && hasSaved ? (
                      <>
                        <button
                          onClick={() => setElcCapaForm(p => ({...p, [g.oe_code]: {
                            ...fc, expanded: true,
                            finding: fc.finding !== undefined ? fc.finding : (dbC?.finding || ''),
                            action:  fc.action  !== undefined ? fc.action  : (dbC?.action_planned || ''),
                            person:  fc.person  !== undefined ? fc.person  : (dbC?.responsible_person || ''),
                            date:    fc.date    !== undefined ? fc.date    : (dbC?.target_date || ''),
                          }}))}
                          style={{fontSize:12,color:T.gold,background:'transparent',border:`1px solid ${T.gold}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                          ✏️ Edit CAPA
                        </button>
                        <button
                          onClick={() => deleteElcCapa(g.oe_code)}
                          disabled={elcCapaDeleting[g.oe_code] || elcCapaSaving[g.oe_code]}
                          style={{fontSize:12,color:T.red,background:'transparent',border:`1px solid ${T.red}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                          {elcCapaDeleting[g.oe_code] ? 'Deleting…' : '🗑 Delete CAPA'}
                        </button>
                      </>
                    ) : expanded ? (
                      <button
                        onClick={() => setElcCapaForm(p => ({...p, [g.oe_code]: {...fc, expanded: false}}))}
                        style={{fontSize:12,color:T.muted,background:'transparent',border:`1px solid ${T.border}`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                        ▲ Hide CAPA
                      </button>
                    ) : (
                      <button
                        onClick={() => setElcCapaForm(p => ({...p, [g.oe_code]: {...fc, expanded: true}}))}
                        style={{fontSize:12,color:T.gold,background:'transparent',border:`1px solid ${T.gold}44`,borderRadius:8,padding:'4px 14px',cursor:'pointer'}}>
                        ▼ Add CAPA
                      </button>
                    )}
                  </div>
                  {expanded && (
                    <div style={{marginTop:12,display:'grid',gap:8}}>
                      <div>
                        <div style={{fontSize:11,color:T.muted,marginBottom:4}}>FINDING *</div>
                        <textarea value={fc.finding || ''} onChange={e => setElcCapaForm(p => ({...p, [g.oe_code]: {...fc, finding: e.target.value}}))}
                          rows={2} placeholder="Describe the non-compliance finding…"
                          style={{width:'100%',padding:'8px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:'vertical',boxSizing:'border-box'}}/>
                      </div>
                      <div>
                        <div style={{fontSize:11,color:T.muted,marginBottom:4}}>ACTION PLANNED *</div>
                        <textarea value={fc.action || ''} onChange={e => setElcCapaForm(p => ({...p, [g.oe_code]: {...fc, action: e.target.value}}))}
                          rows={2} placeholder="Corrective action to be taken…"
                          style={{width:'100%',padding:'8px 10px',borderRadius:8,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,resize:'vertical',boxSizing:'border-box'}}/>
                      </div>
                      <div style={{display:'flex',gap:8,flexWrap:'wrap',alignItems:'flex-end'}}>
                        <div style={{flex:1,minWidth:140}}>
                          <div style={{fontSize:11,color:T.muted,marginBottom:4}}>RESPONSIBLE PERSON</div>
                          <input value={fc.person || ''} onChange={e => setElcCapaForm(p => ({...p, [g.oe_code]: {...fc, person: e.target.value}}))}
                            placeholder="Name / Designation"
                            style={{width:'100%',padding:'7px 10px',borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13,boxSizing:'border-box'}}/>
                        </div>
                        <div>
                          <div style={{fontSize:11,color:T.muted,marginBottom:4}}>TARGET DATE</div>
                          <input type="date" value={fc.date || ''} onChange={e => setElcCapaForm(p => ({...p, [g.oe_code]: {...fc, date: e.target.value}}))}
                            style={{padding:'7px 10px',borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:13}}/>
                        </div>
                        <button onClick={() => submitElcCapa(g.oe_code)}
                          disabled={elcCapaSaving[g.oe_code] || elcCapaDeleting[g.oe_code] || !fc.finding || !fc.action}
                          style={{padding:'7px 20px',borderRadius:10,background:`linear-gradient(135deg,${T.green},#3d9e6e)`,
                            border:'none',color:T.bg,fontSize:14,fontWeight:700,
                            cursor: fc.finding && fc.action ? 'pointer' : 'default',
                            opacity: fc.finding && fc.action ? 1 : 0.5}}>
                          {elcCapaSaving[g.oe_code] ? 'Saving…' : 'Save CAPA →'}
                        </button>
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
  };

  const HCO_ELC_TABS = [
    {key:'overview', label:'📊 Overview'},
    {key:'oes', label:'📑 OE Browser'},
    {key:'fixgaps', label:`🔧 Fix Gaps${allElcGaps.length > 0 ? ' (' + allElcGaps.length + ')' : ''}`},
    {key:'docs', label:'📂 Documents'},
    {key:'licenses', label:'📋 Licenses'},
    {key:'process', label:'🗺️ Process'},
    {key:'upgrade', label:'⬆️ Upgrade Path'},
  ];

  const renderHCOELCTab = () => {
    switch(hcoElcTab) {
      case 'overview': return renderOverview();
      case 'oes': return renderOEBrowser();
      case 'fixgaps': return renderELCFixGaps();
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
          {key:'elc', label:'📋 ELC Prep', sub:'NABH ELC 2nd Edition — Effective January 2026'},
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
    {id:"pricing",label:"Pricing",icon:"💎",programmes:["hco","shco-elc","hco-elc","shco-full"],primary:false},
    {id:"profile",label:"Profile",icon:"👤",programmes:["hco","shco-elc","hco-elc","shco-full"],primary:false},
    {id:"shco",label:"SHCO",icon:"🏥",programmes:["shco-elc"]},
    {id:"hco-elc",label:"HCO ELC",icon:"🎯",programmes:["hco-elc"]},
    {id:"shco-full",label:"Score OEs",icon:"✏️",programmes:["shco-full"],primary:true},
    {id:"eco-full", label:"Score OEs",icon:"✏️",programmes:["eco-full"], primary:true},
    {id:"pricing",  label:"Pricing",  icon:"💎",programmes:["eco-full"], primary:false},
    {id:"profile",  label:"Profile",  icon:"👤",programmes:["eco-full"], primary:false},
  ];
  const NAV=ALL_NAV.filter(n=>n.programmes.includes(selectedProgramme));
  const PRIMARY_NAV=NAV.filter(n=>n.primary);
  const SECONDARY_NAV=NAV.filter(n=>!n.primary&&n.id!=="pricing"&&n.id!=="profile");
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
            <div style={{fontSize:7,letterSpacing:3,color:theme==='light'?"rgba(255,255,255,0.7)":T.gold}}>{selectedProgramme==="shco-full"?"NABH SHCO 3RD EDITION":selectedProgramme==="shco-elc"?"NABH SHCO ELC":selectedProgramme==="hco-elc"?"NABH HCO ELC":selectedProgramme==="eco-full"?"NABH ECO FULL ACCREDITATION":"NABH 6TH EDITION"}</div>
            <div style={{fontSize:14,fontWeight:700,color:"#ffffff"}}>{context?.hospitalName||"AccredReady"}{context?.assessmentName&&<span style={{fontSize:11,color:theme==='light'?"rgba(255,255,255,0.7)":T.muted,marginLeft:6}}>{context.assessmentName}</span>}</div>
          </div>
          {loading&&<div style={{fontSize:11,color:theme==='light'?"rgba(255,255,255,0.7)":T.muted}}>Refreshing…</div>}
          {selectedProgramme==="hco"&&<div style={{padding:"3px 10px",borderRadius:20,background:`${readinessColor}25`,border:`1px solid ${readinessColor}60`,fontSize:11,fontWeight:700,color:theme==='light'?"#ffffff":readinessColor}}>{decision.readiness==="NOT READY"?"❌":decision.readiness==="RISKY"?"⚠️":"✅"} {decision.readiness||"—"}</div>}
          {selectedProgramme==="hco"&&<div style={{padding:"3px 10px",borderRadius:20,background:`${verdictColor}25`,border:`1px solid ${verdictColor}60`,fontSize:12,fontWeight:800,color:theme==='light'?"#ffffff":verdictColor}}>{decision.verdict==="PARTIAL"?"⚠️":""}{decision.verdict||"—"}</div>}
          <div style={{display:"flex",gap:3,flexWrap:"wrap",position:"relative"}}>
            {PRIMARY_NAV.map(n=>{const _tourIds={dashboard:"tour-target-dashboard",scoring:"tour-target-score",gaps:"tour-target-fixgaps",audits:"tour-target-audits"};return(
              <button key={n.id} id={_tourIds[n.id]||undefined} onClick={()=>navigate({ screen: n.id })} style={{
                padding:"4px 9px",borderRadius:7,fontSize:11,cursor:"pointer",
                background:screen===n.id?(theme==='light'?"rgba(255,255,255,0.25)":T.goldD):"transparent",
                border:`1px solid ${screen===n.id?(theme==='light'?"rgba(255,255,255,0.6)":T.gold):(theme==='light'?"rgba(255,255,255,0.3)":T.border)}`,
                color:"#ffffff",
                fontWeight:screen===n.id?700:400,
              }}>{n.icon} {n.label}</button>
            );})}

            {SECONDARY_NAV.length>0&&(
              <div style={{position:"relative"}}>
                <button
                  onClick={e=>{e.stopPropagation();setShowMoreMenu(v=>!v);}}
                  style={{padding:"4px 9px",borderRadius:7,fontSize:11,cursor:"pointer",letterSpacing:2,
                    background:(secondaryActive||showMoreMenu)?(theme==='light'?"rgba(255,255,255,0.25)":T.goldD):"transparent",
                    border:`1px solid ${(secondaryActive||showMoreMenu)?(theme==='light'?"rgba(255,255,255,0.6)":T.gold):(theme==='light'?"rgba(255,255,255,0.3)":T.border)}`,
                    color:"#ffffff",
                  }}
                id="tour-target-more">•••</button>
                {showMoreMenu&&(
                  <div
                    onClick={e=>e.stopPropagation()}
                    style={{position:"absolute",top:"calc(100% + 6px)",left:0,background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"6px 0",display:"flex",flexDirection:"column",zIndex:300,minWidth:220,boxShadow:"0 8px 30px rgba(0,0,0,0.15)"}}>
                    {SECONDARY_NAV.map(n=>(
                      <button key={n.id} onClick={()=>{navigate({ screen: n.id });setShowMoreMenu(false);}}
                        style={{padding:"9px 16px",border:"none",borderLeft:`3px solid ${screen===n.id?T.gold:"transparent"}`,background:screen===n.id?T.goldD:"transparent",color:screen===n.id?T.gold:T.text,fontSize:13,cursor:"pointer",display:"flex",flexDirection:"row",alignItems:"center",gap:10,fontWeight:screen===n.id?700:400,width:"100%",textAlign:"left"}}>
                        <span style={{width:20,fontSize:15}}>{n.icon}</span>
                        <span>{n.label}</span>
                      </button>
                    ))}
                    <a href="https://drive.google.com/drive/folders/1DOfGmHg_dO5blXw_3Mz07dtre6IKYYlI" target="_blank" rel="noopener noreferrer" onClick={()=>setShowMoreMenu(false)}
                      style={{padding:"9px 16px",borderLeft:"3px solid transparent",background:"transparent",color:T.gold,fontSize:13,display:"flex",alignItems:"center",gap:10,textDecoration:"none",fontWeight:700,width:"100%"}}>
                      <span style={{fontSize:15,width:20,textAlign:"center"}}>📁</span>
                      <span>Docs</span>
                    </a>
                    <a href="https://wa.me/918511180957?text=Hi%2C%20I%20have%20a%20suggestion%20for%20AccredReady%3A%20" target="_blank" rel="noopener noreferrer" onClick={()=>setShowMoreMenu(false)}
                      style={{padding:"9px 16px",borderLeft:"3px solid transparent",background:"transparent",color:T.text,fontSize:13,display:"flex",alignItems:"center",gap:10,textDecoration:"none",fontWeight:400,width:"100%"}}>
                      <span style={{fontSize:15,width:20,textAlign:"center"}}>💬</span>
                      <span>Suggest a feature</span>
                    </a>
                  </div>
                )}
              </div>
            )}
          </div>
          <button onClick={()=>setAuthState("programme")} style={{padding:"4px 9px",borderRadius:7,background:"transparent",border:`1px solid ${theme==='light'?"rgba(255,255,255,0.3)":T.border}`,color:"#ffffff",fontSize:11,cursor:"pointer"}}>Switch</button>

          <button onClick={toggleTheme} title={theme==='dark'?'Switch to light mode':'Switch to dark mode'} style={{padding:"4px 9px",borderRadius:7,background:theme==='light'?"rgba(255,255,255,0.2)":"transparent",border:`1px solid ${theme==='light'?"rgba(255,255,255,0.4)":T.border}`,color:"#ffffff",fontSize:15,cursor:"pointer",lineHeight:1}}>{theme==='dark'?'☀️':'🌙'}</button>
          <div style={{position:"relative"}}>
            <button onClick={e=>{e.stopPropagation();setShowUserMenu(v=>!v);}} style={{width:30,height:30,borderRadius:"50%",background:theme==='light'?"rgba(255,255,255,0.2)":T.goldD,border:`1px solid ${theme==='light'?"rgba(255,255,255,0.4)":T.gold}`,color:"#ffffff",fontSize:16,cursor:"pointer",display:"flex",alignItems:"center",justifyContent:"center",padding:0}}>👤</button>
            {showUserMenu&&(
              <div onClick={e=>e.stopPropagation()} style={{position:"absolute",top:"calc(100% + 6px)",right:0,background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"6px 0",display:"flex",flexDirection:"column",zIndex:300,minWidth:160,boxShadow:"0 8px 30px rgba(0,0,0,0.15)"}}>
                <button onClick={()=>{navigate({ screen: "profile" });setShowUserMenu(false);}} style={{padding:"9px 16px",border:"none",borderLeft:`3px solid ${screen==="profile"?T.gold:"transparent"}`,background:screen==="profile"?T.goldD:"transparent",color:screen==="profile"?T.gold:T.text,fontSize:13,cursor:"pointer",display:"flex",alignItems:"center",gap:10,width:"100%",textAlign:"left"}}>
                  <span style={{width:20,fontSize:15}}>👤</span><span>Profile</span>
                </button>
                <button onClick={()=>{navigate({ screen: "pricing" });setShowUserMenu(false);}} style={{padding:"9px 16px",border:"none",borderLeft:`3px solid ${screen==="pricing"?T.gold:"transparent"}`,background:screen==="pricing"?T.goldD:"transparent",color:screen==="pricing"?T.gold:T.text,fontSize:13,cursor:"pointer",display:"flex",alignItems:"center",gap:10,width:"100%",textAlign:"left"}}>
                  <span style={{width:20,fontSize:15}}>💎</span><span>Pricing</span>
                </button>
                <div style={{height:1,background:T.border,margin:"4px 0"}}/>
                <button onClick={handleSignOut} style={{padding:"9px 16px",border:"none",borderLeft:"3px solid transparent",background:"transparent",color:T.red,fontSize:13,cursor:"pointer",display:"flex",alignItems:"center",gap:10,width:"100%",textAlign:"left"}}>
                  <span style={{width:20,fontSize:15}}>🚪</span><span>Sign out</span>
                </button>
              </div>
            )}
          </div>
        </div>
      </div>

      {isTrialActive && daysLeft <= 5 && (
        <div style={{background:"#1a0a00",borderBottom:"1px solid #f4a44140",padding:"8px 20px",display:"flex",justifyContent:"space-between",alignItems:"center",flexWrap:"wrap",gap:8}}>
          <span style={{fontSize:13,color:"#f4a441",fontWeight:700}}>⏳ Trial expires in {daysLeft} day{daysLeft!==1?"s":""} — upgrade to keep your data.</span>
          <a href="https://wa.me/918511180957?text=Hi%20Dr.%20Mehul%2C%20I%20want%20to%20upgrade%20AccredReady" target="_blank" rel="noopener noreferrer" style={{padding:"5px 14px",borderRadius:8,background:"#f4a441",color:"#050e1a",fontSize:12,fontWeight:800,textDecoration:"none"}}>Upgrade Now</a>
        </div>
      )}

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
      {selectedProgramme==="shco-full"&&shcoFullOes.filter(oe=>oe.level==='Core'&&(shcoFullScores[oe.oe_code]||0)<4).length>0&&(
        <div style={{background:T.redD,padding:"8px 20px",display:"flex",gap:10,alignItems:"center"}}>
          <span style={{fontSize:16}}>🚨</span>
          <span style={{fontSize:13,fontWeight:700,color:T.red}}>
            CORE FAILURE: {shcoFullOes.filter(oe=>oe.level==='Core'&&(shcoFullScores[oe.oe_code]||0)<4).length} Core OE{shcoFullOes.filter(oe=>oe.level==='Core'&&(shcoFullScores[oe.oe_code]||0)<4).length>1?"s":""} below 4 — accreditation will be at risk.
          </span>
        </div>
      )}

      <div style={{maxWidth:1200,margin:"0 auto",padding:"16px"}}>
        {screen==="dashboard"&&<Dashboard decision={decision} gaps={gaps} onNav={id=>navigate({screen:id})}/>}
        {screen==="dashboard"&&<button onClick={generatePDF} disabled={pdfLoading}
          style={{position:'fixed',bottom:20,right:20,zIndex:9999,padding:'8px 16px',borderRadius:9,border:`1px solid ${T.gold}`,background:T.bg,color:T.gold,fontSize:12,fontWeight:700,cursor:pdfLoading?'default':'pointer',opacity:pdfLoading?0.6:1,boxShadow:'0 2px 12px rgba(0,0,0,0.5)'}}>
          {pdfLoading?'⏳ Generating…':'⬇ Export PDF'}
        </button>}
        {screen==="scoring"&&<ScoringScreen assessmentId={context?.assessmentId} oes={oes} standards={standards} onRefresh={()=>loadData(context)}/>}
        {screen==="gaps"&&<GapFixScreen assessmentId={context?.assessmentId} gaps={gaps} onRefresh={()=>loadData(context)} onDownloadReport={generatePDF} pdfLoading={pdfLoading}/>}
        {screen==="committees"&&<CommitteesScreen hospitalId={context?.hospitalId} committeesView={committeesView} navigate={navigate}/>}
        {screen==="committee-calendar"&&<CommitteeCalendarScreen hospitalId={context?.hospitalId}/>}
        {screen==="kpis"&&<KPIsScreen hospitalId={context?.hospitalId} user={user}/>}
        {screen==="checklists"&&<ChecklistsScreen hospitalId={context?.hospitalId}/>}
        {screen==="audits"&&<AuditsScreen hospitalId={context?.hospitalId} auditMainTab={auditMainTab} navigate={navigate}/>}
        {screen==="drills"&&<MockDrillsScreen hospitalId={context?.hospitalId} drillsView={drillsView} selectedDrill={selectedDrill} navigate={navigate} goBack={goBack} setDrillsView={setDrillsView} setSelectedDrill={setSelectedDrill}/>}
        {screen==="licenses"&&<StatutoryLicensesScreen hospitalId={context?.hospitalId} showAdd={showLicenseAdd} navigate={navigate} setShowAdd={setShowLicenseAdd}/>}
        {screen==="tracer"&&<PatientTracerScreen hospitalId={context?.hospitalId} tracerView={tracerView} tracerType={tracerType} navigate={navigate} goBack={goBack} setTracerView={setTracerView} setTracerType={setTracerType}/>}
        {screen==="pricing"&&<PricingScreen/>}
        {screen==="profile"&&<ProfileScreen user={user} context={context} onContextUpdate={setContext}/>}
        {screen==="shco"&&renderSHCOTab()}
        {screen==="shco-full"&&renderSHCOFullTab()}
        {screen==="eco-full"&&renderECOFullTab()}
        {screen==="hco-elc"&&renderHCOTab()}
      </div>

      <button onClick={()=>setTourStep(0)} title="Replay app tour"
        style={{position:"fixed",bottom:148,right:20,zIndex:9997,width:48,height:48,borderRadius:24,background:T.gold,border:"none",color:T.bg,fontSize:22,fontWeight:900,cursor:"pointer",boxShadow:`0 4px 16px rgba(201,168,76,0.5)`,display:"flex",alignItems:"center",justifyContent:"center",lineHeight:1}}>?</button>
      {selectedProgramme==="shco-full"&&(
        <AIAssistantWidget
          T={T}
          open={aiWidgetOpen}
          onOpen={()=>setAiWidgetOpen(true)}
          onClose={()=>setAiWidgetOpen(false)}
          trigger={aiWidgetTrigger}
        />
      )}
      {tourStep!==null&&<WalktourOverlay step={tourStep} totalSteps={activeSteps.length} onNext={nextTourStep} onSkip={dismissTour} steps={activeSteps}/>}
      <div style={{textAlign:"center",padding:"14px",color:T.muted,fontSize:11,borderTop:`1px solid ${T.border}`,marginTop:20}}>
        NABH Accreditation Platform — Independent educational tool — Not affiliated with NABH/QCI
      </div>
    </div>
  );
}

// ── MOCK DRILLS ───────────────────────────────────────────────
function MockDrillsScreen({ hospitalId, drillsView, selectedDrill, navigate, goBack, setDrillsView, setSelectedDrill }) {
  const [drills,setDrills]=useState([]);
  const [records,setRecords]=useState([]);
  const [form,setForm]=useState({drill_date:"",drill_time:"",location:"",conducted_by:"",supervised_by:"",participants_category:"",total_participants:"",pre_briefing:"Done",scenario_desc:"",drill_description:"",observations:["","",""],debriefing:"Done",corrective_actions:"",preventive_actions:"",additional_points:"",status:"completed",evidence_url:""});
  const [saving,setSaving]=useState(false);
  const [expanded,setExpanded]=useState(null);
  const [expandedRec,setExpandedRec]=useState(null);
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
    const {error}=await supabase.from("mock_drill_records").insert({
      hospital_id:hospitalId,drill_id:selectedDrill.id,
      drill_date:form.drill_date,drill_time:form.drill_time||null,
      location:form.location||null,conducted_by:form.conducted_by||null,
      supervised_by:form.supervised_by||null,
      participants_category:form.participants_category||null,
      total_participants:form.total_participants?parseInt(form.total_participants):null,
      pre_briefing:form.pre_briefing,scenario_desc:form.scenario_desc||null,
      drill_description:form.drill_description||null,
      observations:obs,debriefing:form.debriefing,
      corrective_actions:form.corrective_actions||null,
      preventive_actions:form.preventive_actions||null,
      additional_points:form.additional_points||null,status:form.status,
      evidence_url:form.evidence_url||null
    });
    if(error){alert("Error saving drill record: "+error.message);setSaving(false);return;}
    const {data:r}=await supabase.from("mock_drill_records").select("*").eq("hospital_id",hospitalId).order("drill_date",{ascending:false});
    setRecords(r||[]);setSaving(false);setDrillsView("tracker");setSelectedDrill(null);
  };

  if(loading)return <div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  // RECORD FORM
  if(drillsView==="record"&&selectedDrill)return(
    <div>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:14}}>
        <button onClick={goBack} style={{padding:"5px 12px",borderRadius:7,background:"transparent",border:`1px solid ${T.border}`,color:T.muted,fontSize:13,cursor:"pointer"}}>← Back</button>
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
                <button onClick={e=>{e.stopPropagation();setForm({drill_date:"",drill_time:"",location:"",conducted_by:"",supervised_by:"",participants_category:"",total_participants:"",pre_briefing:"Done",scenario_desc:"",drill_description:"",observations:["","",""],debriefing:"Done",corrective_actions:"",preventive_actions:"",additional_points:"",status:"completed",evidence_url:""});navigate({ drillsView: 'record', selectedDrill: drill });}}
                  style={{padding:"5px 12px",borderRadius:7,background:T.goldD,border:`1px solid ${T.gold}`,color:T.goldL,fontSize:12,fontWeight:700,cursor:"pointer",whiteSpace:"nowrap"}}>+ Record</button>
                <div style={{color:T.muted,fontSize:13}}>{isOpen?"▲":"▼"}</div>
              </div>
              {isOpen&&(
                <div style={{borderTop:`1px solid ${T.border}`,padding:"12px 14px"}}>
                  <div style={{fontSize:12,color:T.muted,marginBottom:8,lineHeight:1.6}}>{drill.description}</div>
                  {recs.length>0&&(
                    <div>
                      <div style={{fontSize:11,fontWeight:700,color:T.gold,marginBottom:6}}>DRILL HISTORY</div>
                      {recs.slice(0,5).map(r=>{
                        const recOpen=expandedRec===r.id;
                        const obsList=Array.isArray(r.observations)?r.observations.filter(o=>o&&String(o).trim()):[];
                        const shortFields=[["TIME",r.drill_time],["LOCATION",r.location],["CONDUCTED BY",r.conducted_by],["SUPERVISED BY",r.supervised_by],["PARTICIPANTS CATEGORY",r.participants_category],["TOTAL PARTICIPANTS",r.total_participants],["PRE-BRIEFING",r.pre_briefing],["DEBRIEFING",r.debriefing],["STATUS",r.status]].filter(([,v])=>v!==null&&v!==undefined&&String(v).trim()!=="");
                        const longFields=[["SCENARIO DESCRIPTION",r.scenario_desc],["DRILL DESCRIPTION & RESPONSE",r.drill_description],["CORRECTIVE ACTIONS",r.corrective_actions],["PREVENTIVE ACTIONS",r.preventive_actions],["ADDITIONAL POINTS",r.additional_points]].filter(([,v])=>v&&String(v).trim());
                        return(
                        <div key={r.id} style={{background:T.panel2,borderRadius:7,marginBottom:5,overflow:"hidden",border:`1px solid ${recOpen?`${T.gold}40`:"transparent"}`}}>
                          <div style={{padding:"8px 12px",fontSize:11,color:T.muted,display:"flex",gap:10,alignItems:"center",cursor:"pointer"}} onClick={()=>setExpandedRec(recOpen?null:r.id)}>
                            <div style={{fontWeight:700,color:T.text,minWidth:80}}>{r.drill_date}</div>
                            <div style={{flex:1}}>{r.location&&`📍 ${r.location} · `}{r.total_participants&&`👥 ${r.total_participants} participants · `}{r.conducted_by&&`👤 ${r.conducted_by}`}</div>
                            {r.corrective_actions&&<div style={{color:T.orange}}>⚡ CAPA raised</div>}
                            <button onClick={e=>{e.stopPropagation();deleteRecord(r.id);}} style={{padding:"2px 8px",borderRadius:5,background:"transparent",border:`1px solid ${T.red}40`,color:T.red,fontSize:11,cursor:"pointer",flexShrink:0}}>Delete</button>
                            <div style={{fontSize:11}}>{recOpen?"▲":"▼"}</div>
                          </div>
                          {recOpen&&(
                            <div style={{borderTop:`1px solid ${T.border}`,padding:"12px 14px",display:"grid",gap:12}}>
                              {shortFields.length>0&&(
                                <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(150px,1fr))",gap:10}}>
                                  {shortFields.map(([l,v])=>(
                                    <div key={l}><div style={{fontSize:10,color:T.muted,letterSpacing:1,marginBottom:3}}>{l}</div><div style={{fontSize:13,color:T.text}}>{String(v)}</div></div>
                                  ))}
                                </div>
                              )}
                              {longFields.map(([l,v])=>(
                                <div key={l}><div style={{fontSize:10,color:T.muted,letterSpacing:1,marginBottom:3}}>{l}</div><div style={{fontSize:13,color:T.text,lineHeight:1.6,whiteSpace:"pre-wrap"}}>{v}</div></div>
                              ))}
                              {obsList.length>0&&(
                                <div>
                                  <div style={{fontSize:10,color:T.muted,letterSpacing:1,marginBottom:3}}>DEVIATIONS / OBSERVATIONS</div>
                                  <ul style={{margin:0,paddingLeft:18}}>{obsList.map((o,i)=><li key={i} style={{fontSize:13,color:T.text,lineHeight:1.6}}>{o}</li>)}</ul>
                                </div>
                              )}
                              {r.evidence_url&&(
                                <div>
                                  <div style={{fontSize:10,color:T.muted,letterSpacing:1,marginBottom:3}}>EVIDENCE</div>
                                  <a href={r.evidence_url} target="_blank" rel="noopener noreferrer" style={{fontSize:13,color:T.blue,wordBreak:"break-all"}}>{r.evidence_url}</a>
                                </div>
                              )}
                            </div>
                          )}
                        </div>
                        );
                      })}
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
      <div style={{display:"flex",flexWrap:"wrap",alignItems:"center",marginBottom:10,gap:8}}>
        <div style={{flex:"1 1 160px"}}>
          <div style={{fontSize:15,fontWeight:700,color:T.gold}}>{viewMode==="committee"?"Committee Calendar":"Mock Drill Calendar"}</div>
          <div style={{fontSize:12,color:T.muted}}>FY {year}–{year+1}{viewMode==="committee"?` · ${totalDone}/${totalExpected} done · ${pct}%`:""}</div>
        </div>
        <div style={{display:"flex",borderRadius:8,border:`1px solid ${T.border}`,overflow:"hidden",flex:"1 1 220px",width:"100%"}}>
          <button onClick={()=>setViewMode("committee")} style={{flex:1,padding:"7px 10px",fontSize:13,fontWeight:700,cursor:"pointer",background:viewMode==="committee"?T.goldD:"transparent",border:"none",color:viewMode==="committee"?T.goldL:T.muted,whiteSpace:"nowrap"}}>🏛️ Committees</button>
          <div style={{width:1,background:T.border,flexShrink:0}}/>
          <button onClick={()=>setViewMode("drill")} style={{flex:1,padding:"7px 10px",fontSize:13,fontWeight:700,cursor:"pointer",background:viewMode==="drill"?T.goldD:"transparent",border:"none",color:viewMode==="drill"?T.goldL:T.muted,whiteSpace:"nowrap"}}>🚨 Drills</button>
        </div>
        <div style={{display:"flex",gap:6,alignItems:"center",justifyContent:"flex-end",flex:"0 0 auto"}}>
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

function StatutoryLicensesScreen({ hospitalId, showAdd, navigate, setShowAdd }) {
  const [licenses,setLicenses]=useState([]);
  const [loading,setLoading]=useState(true);
  const [saving,setSaving]=useState(false);
  const [editId,setEditId]=useState(null);
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
    navigate({ showLicenseAdd: true });
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
        <button onClick={()=>{navigate({ showLicenseAdd: true });setEditId(null);setForm({license_name:"",issuing_authority:"",license_type:"",license_number:"",issue_date:"",expiry_date:"",evidence_url:"",notes:""});}} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>+ Add License</button>
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

function PatientTracerScreen({ hospitalId, tracerView, tracerType, navigate, goBack, setTracerView, setTracerType }) {
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

  const startNew=(typeOverride)=>{
    setResponses({});
    setMeta({patient_ref:"",conducted_by:"",conducted_date:new Date().toISOString().split("T")[0],notes:""});
    setActiveTracer(null);
    navigate(typeof typeOverride==="string"&&TRACER_TYPES[typeOverride] ? { tracerType: typeOverride, tracerView: 'new' } : { tracerView: 'new' });
  };

  const startConduct=()=>{
    navigate({ tracerView: 'conduct' });
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
    setTracerView("list");
  };

  const scoreColor=(pct)=>pct>=80?T.green:pct>=60?T.orange:T.red;

  const inp={width:"100%",padding:"8px 10px",borderRadius:7,border:`1px solid ${T.border}`,background:T.panel2,color:T.text,fontSize:14,boxSizing:"border-box"};

  if(loading)return<div style={{textAlign:"center",padding:40,color:T.muted}}>Loading…</div>;

  // LIST VIEW
  if(tracerView==="list")return(
    <div>
      <div style={{display:"flex",justifyContent:"space-between",alignItems:"center",marginBottom:14,flexWrap:"wrap",gap:8}}>
        <div>
          <div style={{fontSize:16,fontWeight:700,color:T.gold}}>🩺 Patient Tracer</div>
          <div style={{fontSize:12,color:T.muted}}>Simulate assessor patient file review — identify gaps before they do</div>
        </div>
        <button onClick={()=>startNew()} style={{padding:"7px 16px",borderRadius:8,background:`linear-gradient(135deg,${T.gold},#f0d070)`,border:"none",color:T.bg,fontSize:13,fontWeight:700,cursor:"pointer"}}>+ New Tracer</button>
      </div>

      {/* Tracer type cards */}
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(160px,1fr))",gap:10,marginBottom:20}}>
        {Object.entries(TRACER_TYPES).map(([type,data])=>{
          const done=tracers.filter(t=>t.tracer_type===type);
          const avg=done.length>0?Math.round(done.reduce((s,t)=>s+t.score_pct,0)/done.length):null;
          return(
            <div key={type} style={{background:T.panel,border:`1px solid ${T.border}`,borderRadius:10,padding:"12px",cursor:"pointer"}} onClick={()=>startNew(type)}>
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
  if(tracerView==="new")return(
    <div>
      <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:16}}>
        <button onClick={goBack} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:12,cursor:"pointer"}}>← Back</button>
        <div style={{fontSize:15,fontWeight:700,color:T.gold}}>New Patient Tracer</div>
      </div>

      {/* Select tracer type */}
      <div style={{fontSize:11,color:T.muted,marginBottom:8,letterSpacing:1}}>SELECT TRACER TYPE</div>
      <div style={{display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(140px,1fr))",gap:8,marginBottom:18}}>
        {Object.entries(TRACER_TYPES).map(([type,data])=>(
          <div key={type} onClick={()=>setTracerType(type)} style={{background:tracerType===type?`${data.color}15`:T.panel,border:`1px solid ${tracerType===type?data.color:T.border}`,borderRadius:9,padding:"10px",cursor:"pointer",textAlign:"center"}} >
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
        Start {tracerType.replace(/ Tracer$/,"")} Tracer ({TRACER_TYPES[tracerType].questions.length} questions) →
      </button>
    </div>
  );

  // CONDUCT TRACER — answer questions
  if(tracerView==="conduct"){
    const tdata=TRACER_TYPES[tracerType];
    const answered=tdata.questions.filter(q=>responses[q.id]).length;
    const pct=calcScore();

    return(
      <div>
        <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:12,flexWrap:"wrap"}}>
          <button onClick={goBack} style={{padding:"4px 10px",borderRadius:6,border:`1px solid ${T.border}`,background:"transparent",color:T.muted,fontSize:12,cursor:"pointer"}}>← Back</button>
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
