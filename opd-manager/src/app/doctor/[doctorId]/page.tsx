"use client";

import { useParams } from "next/navigation";
import { useMemo, useState } from "react";
import { ConsoleLayout } from "@/components/ConsoleLayout";
import { VisitCard } from "@/components/VisitCard";
import { ActionButton, FirebaseSetupBanner } from "@/components/ui";
import { useDoctors } from "@/hooks/useDoctors";
import { useVisits } from "@/hooks/useVisits";
import { transitionVisit } from "@/lib/firestore/visits";
import type { Visit } from "@/lib/types";

const DOCTOR_STAGES = [
  "waiting_doctor",
  "doctor_calling",
  "in_consultation",
  "report_ready_lab",
  "report_ready_radio",
  "back_to_doctor",
  "at_pharmacy",
  "pharmacy_processing",
  "completed",
] as const;

export default function DoctorConsolePage() {
  const params = useParams<{ doctorId: string }>();
  const doctorId = params.doctorId;
  const { doctors } = useDoctors();
  const doctor = doctors.find((d) => d.id === doctorId);
  const { visits, loading, error } = useVisits({ consultantId: doctorId });
  const [busyId, setBusyId] = useState<string | null>(null);

  const queue = useMemo(
    () => visits.filter((v) => DOCTOR_STAGES.includes(v.currentStage as (typeof DOCTOR_STAGES)[number])),
    [visits],
  );

  async function act(visit: Visit, stage: Parameters<typeof transitionVisit>[1], note: string) {
    setBusyId(visit.id);
    try {
      const extras =
        stage === "doctor_calling" ? { calledAt: new Date() } : undefined;
      await transitionVisit(visit.id, stage, note, extras);
    } finally {
      setBusyId(null);
    }
  }

  return (
    <ConsoleLayout
      title={doctor ? `Dr. ${doctor.name}` : "Doctor console"}
      subtitle={doctor ? `Room ${doctor.roomNumber} — tap to guide patient` : "Loading…"}
    >
      <FirebaseSetupBanner />
      {loading ? <p className="text-slate-600">Loading queue…</p> : null}
      {error ? <p className="text-rose-600">{error}</p> : null}

      <div className="space-y-4">
        {queue.map((visit) => (
          <VisitCard
            key={visit.id}
            visit={visit}
            highlight={visit.currentStage === "doctor_calling"}
            actions={
              <>
                {["waiting_doctor", "back_to_doctor", "report_ready_lab", "report_ready_radio"].includes(
                  visit.currentStage,
                ) ? (
                  <ActionButton
                    label="Call patient"
                    disabled={busyId === visit.id}
                    onClick={() => act(visit, "doctor_calling", "Doctor calling")}
                  />
                ) : null}
                {visit.currentStage === "doctor_calling" ? (
                  <ActionButton
                    label="In consultation"
                    disabled={busyId === visit.id}
                    onClick={() => act(visit, "in_consultation", "Consultation started")}
                  />
                ) : null}
                {visit.currentStage === "in_consultation" ? (
                  <>
                    <ActionButton
                      label="Send to lab"
                      disabled={busyId === visit.id}
                      onClick={() => act(visit, "at_lab", "Sent to laboratory")}
                    />
                    <ActionButton
                      label="Send to radiology"
                      variant="secondary"
                      disabled={busyId === visit.id}
                      onClick={() => act(visit, "at_radiology", "Sent to radiology")}
                    />
                    <ActionButton
                      label="Send to pharmacy"
                      variant="secondary"
                      disabled={busyId === visit.id}
                      onClick={() => act(visit, "at_pharmacy", "Sent to pharmacy")}
                    />
                    <ActionButton
                      label="Complete (exit)"
                      variant="danger"
                      disabled={busyId === visit.id}
                      onClick={() =>
                        transitionVisit(visit.id, "exited", "Discharged", { exitedAt: new Date() })
                      }
                    />
                  </>
                ) : null}
              </>
            }
          />
        ))}
        {!loading && queue.length === 0 ? (
          <p className="rounded-xl border border-dashed border-slate-300 p-8 text-center text-slate-500">
            No patients in your queue right now.
          </p>
        ) : null}
      </div>
    </ConsoleLayout>
  );
}
