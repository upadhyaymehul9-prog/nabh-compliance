import type { Timestamp } from "firebase/firestore";

export type UserRole =
  | "reception"
  | "doctor"
  | "lab"
  | "radiology"
  | "pharmacy"
  | "manager";

export type VisitStage =
  | "registered"
  | "waiting_doctor"
  | "doctor_calling"
  | "in_consultation"
  | "at_lab"
  | "lab_processing"
  | "report_ready_lab"
  | "at_radiology"
  | "radio_processing"
  | "report_ready_radio"
  | "back_to_doctor"
  | "at_pharmacy"
  | "pharmacy_processing"
  | "completed"
  | "exited";

export interface StageEvent {
  stage: VisitStage;
  at: Timestamp;
  note?: string;
}

export interface Doctor {
  id: string;
  clinicId: string;
  name: string;
  roomNumber: string;
  specialty?: string;
  active: boolean;
}

export interface Visit {
  id: string;
  clinicId: string;
  tokenNumber: string;
  patientName: string;
  patientPhone?: string;
  consultantId: string;
  consultantName: string;
  roomNumber: string;
  currentStage: VisitStage;
  currentLocation: string;
  registeredAt: Timestamp;
  stageHistory: StageEvent[];
  calledAt?: Timestamp;
  labEta?: Timestamp;
  radioEta?: Timestamp;
  labReadyAt?: Timestamp;
  radioReadyAt?: Timestamp;
  exitedAt?: Timestamp;
  updatedAt: Timestamp;
}

export interface Clinic {
  id: string;
  name: string;
  tokenPrefix?: string;
}
