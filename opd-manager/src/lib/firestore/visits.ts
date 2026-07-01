import {
  addDoc,
  collection,
  doc,
  getDocs,
  limit,
  onSnapshot,
  orderBy,
  query,
  runTransaction,
  serverTimestamp,
  Timestamp,
  updateDoc,
  where,
  type Unsubscribe,
} from "firebase/firestore";
import { CLINIC_ID, getDb } from "@/lib/firebase/config";
import type { Doctor, StageEvent, Visit, VisitStage } from "@/lib/types";
import { STAGE_LABELS } from "@/lib/constants";

const visitsRef = () => collection(getDb(), "visits");
const doctorsRef = () => collection(getDb(), "doctors");

function locationForStage(stage: VisitStage, roomNumber: string): string {
  switch (stage) {
    case "registered":
    case "waiting_doctor":
    case "doctor_calling":
    case "in_consultation":
    case "back_to_doctor":
      return `Room ${roomNumber}`;
    case "at_lab":
    case "lab_processing":
    case "report_ready_lab":
      return "Laboratory";
    case "at_radiology":
    case "radio_processing":
    case "report_ready_radio":
      return "Radiology";
    case "at_pharmacy":
    case "pharmacy_processing":
      return "Pharmacy";
    case "completed":
    case "exited":
      return "Exit";
    default:
      return STAGE_LABELS[stage];
  }
}

export async function listDoctors(clinicId = CLINIC_ID): Promise<Doctor[]> {
  const q = query(
    doctorsRef(),
    where("clinicId", "==", clinicId),
    where("active", "==", true),
  );
  const snap = await getDocs(q);
  return snap.docs.map((d) => ({ id: d.id, ...d.data() }) as Doctor);
}

export function subscribeDoctors(
  clinicId: string,
  onData: (doctors: Doctor[]) => void,
  onError?: (error: Error) => void,
): Unsubscribe {
  const q = query(
    doctorsRef(),
    where("clinicId", "==", clinicId),
    where("active", "==", true),
  );
  return onSnapshot(
    q,
    (snap) => {
      const doctors = snap.docs.map((d) => ({ id: d.id, ...d.data() }) as Doctor);
      doctors.sort((a, b) => a.name.localeCompare(b.name));
      onData(doctors);
    },
    (err) => onError?.(err),
  );
}

async function nextToken(clinicId: string): Promise<string> {
  const startOfDay = new Date();
  startOfDay.setHours(0, 0, 0, 0);

  const q = query(
    visitsRef(),
    where("clinicId", "==", clinicId),
    where("registeredAt", ">=", Timestamp.fromDate(startOfDay)),
    orderBy("registeredAt", "desc"),
    limit(1),
  );
  const snap = await getDocs(q);
  const last = snap.docs[0]?.data()?.tokenNumber as string | undefined;
  const lastNum = last ? parseInt(last.replace(/\D/g, ""), 10) : 0;
  return String(lastNum + 1).padStart(3, "0");
}

export interface RegisterPatientInput {
  patientName: string;
  patientPhone?: string;
  consultantId: string;
  consultantName: string;
  roomNumber: string;
  clinicId?: string;
}

export async function registerPatient(input: RegisterPatientInput): Promise<string> {
  const clinicId = input.clinicId ?? CLINIC_ID;
  const tokenNumber = await nextToken(clinicId);
  const stage: VisitStage = "waiting_doctor";
  const stageHistory: StageEvent[] = [
    { stage: "registered", at: Timestamp.now(), note: "Reception" },
    { stage, at: Timestamp.now(), note: "Queued for doctor" },
  ];

  const docRef = await addDoc(visitsRef(), {
    clinicId,
    tokenNumber,
    patientName: input.patientName.trim(),
    patientPhone: input.patientPhone?.trim() || null,
    consultantId: input.consultantId,
    consultantName: input.consultantName,
    roomNumber: input.roomNumber,
    currentStage: stage,
    currentLocation: locationForStage(stage, input.roomNumber),
    registeredAt: serverTimestamp(),
    stageHistory,
    updatedAt: serverTimestamp(),
  });

  return docRef.id;
}

export interface VisitQuery {
  clinicId?: string;
  consultantId?: string;
  stages?: VisitStage[];
}

function mapVisit(id: string, data: Record<string, unknown>): Visit {
  return {
    id,
    clinicId: data.clinicId as string,
    tokenNumber: data.tokenNumber as string,
    patientName: data.patientName as string,
    patientPhone: (data.patientPhone as string | undefined) ?? undefined,
    consultantId: data.consultantId as string,
    consultantName: data.consultantName as string,
    roomNumber: data.roomNumber as string,
    currentStage: data.currentStage as VisitStage,
    currentLocation: data.currentLocation as string,
    registeredAt: data.registeredAt as Timestamp,
    stageHistory: (data.stageHistory as StageEvent[]) ?? [],
    calledAt: data.calledAt as Timestamp | undefined,
    labEta: data.labEta as Timestamp | undefined,
    radioEta: data.radioEta as Timestamp | undefined,
    labReadyAt: data.labReadyAt as Timestamp | undefined,
    radioReadyAt: data.radioReadyAt as Timestamp | undefined,
    exitedAt: data.exitedAt as Timestamp | undefined,
    updatedAt: data.updatedAt as Timestamp,
  };
}

export function subscribeVisits(
  filters: VisitQuery,
  onData: (visits: Visit[]) => void,
  onError?: (error: Error) => void,
): Unsubscribe {
  const clinicId = filters.clinicId ?? CLINIC_ID;
  const constraints = [
    where("clinicId", "==", clinicId),
    orderBy("registeredAt", "desc"),
    limit(200),
  ];

  if (filters.consultantId) {
    constraints.splice(1, 0, where("consultantId", "==", filters.consultantId));
  }

  const q = query(visitsRef(), ...constraints);

  return onSnapshot(
    q,
    (snap) => {
      let visits = snap.docs.map((d) => mapVisit(d.id, d.data()));
      if (filters.stages?.length) {
        visits = visits.filter((v) => filters.stages!.includes(v.currentStage));
      }
      onData(visits);
    },
    (err) => onError?.(err),
  );
}

export async function transitionVisit(
  visitId: string,
  nextStage: VisitStage,
  note?: string,
  extras?: Partial<{
    labEta: Date;
    radioEta: Date;
    labReadyAt: Date;
    radioReadyAt: Date;
    exitedAt: Date;
    calledAt: Date;
  }>,
): Promise<void> {
  const ref = doc(getDb(), "visits", visitId);

  await runTransaction(getDb(), async (tx) => {
    const snap = await tx.get(ref);
    if (!snap.exists()) throw new Error("Visit not found");

    const data = snap.data();
    const roomNumber = data.roomNumber as string;
    const history = (data.stageHistory as StageEvent[]) ?? [];
    const event: StageEvent = {
      stage: nextStage,
      at: Timestamp.now(),
      note,
    };

    const patch: Record<string, unknown> = {
      currentStage: nextStage,
      currentLocation: locationForStage(nextStage, roomNumber),
      stageHistory: [...history, event],
      updatedAt: serverTimestamp(),
    };

    if (extras?.labEta) patch.labEta = Timestamp.fromDate(extras.labEta);
    if (extras?.radioEta) patch.radioEta = Timestamp.fromDate(extras.radioEta);
    if (extras?.labReadyAt) patch.labReadyAt = Timestamp.fromDate(extras.labReadyAt);
    if (extras?.radioReadyAt) patch.radioReadyAt = Timestamp.fromDate(extras.radioReadyAt);
    if (extras?.exitedAt) patch.exitedAt = Timestamp.fromDate(extras.exitedAt);
    if (extras?.calledAt) patch.calledAt = Timestamp.fromDate(extras.calledAt);

    tx.update(ref, patch);
  });
}

export function addMinutes(date: Date, minutes: number): Date {
  return new Date(date.getTime() + minutes * 60_000);
}
