import type { VisitStage } from "./types";

export const STAGE_LABELS: Record<VisitStage, string> = {
  registered: "Registered",
  waiting_doctor: "Waiting for doctor",
  doctor_calling: "Calling patient",
  in_consultation: "In consultation",
  at_lab: "At lab (queue)",
  lab_processing: "Lab in progress",
  report_ready_lab: "Lab report ready",
  at_radiology: "At radiology (queue)",
  radio_processing: "Radiology in progress",
  report_ready_radio: "Radiology report ready",
  back_to_doctor: "Return to doctor",
  at_pharmacy: "At pharmacy (queue)",
  pharmacy_processing: "Dispensing",
  completed: "Visit complete",
  exited: "Exited clinic",
};

export const STAGE_COLORS: Record<VisitStage, string> = {
  registered: "bg-slate-100 text-slate-800",
  waiting_doctor: "bg-amber-100 text-amber-900",
  doctor_calling: "bg-sky-100 text-sky-900",
  in_consultation: "bg-blue-100 text-blue-900",
  at_lab: "bg-violet-100 text-violet-900",
  lab_processing: "bg-violet-200 text-violet-950",
  report_ready_lab: "bg-emerald-100 text-emerald-900",
  at_radiology: "bg-indigo-100 text-indigo-900",
  radio_processing: "bg-indigo-200 text-indigo-950",
  report_ready_radio: "bg-emerald-100 text-emerald-900",
  back_to_doctor: "bg-cyan-100 text-cyan-900",
  at_pharmacy: "bg-orange-100 text-orange-900",
  pharmacy_processing: "bg-orange-200 text-orange-950",
  completed: "bg-green-100 text-green-900",
  exited: "bg-gray-100 text-gray-600",
};

export const ACTIVE_STAGES: VisitStage[] = [
  "registered",
  "waiting_doctor",
  "doctor_calling",
  "in_consultation",
  "at_lab",
  "lab_processing",
  "report_ready_lab",
  "at_radiology",
  "radio_processing",
  "report_ready_radio",
  "back_to_doctor",
  "at_pharmacy",
  "pharmacy_processing",
  "completed",
];
