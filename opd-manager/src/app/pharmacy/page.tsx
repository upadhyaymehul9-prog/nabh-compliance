"use client";

import { useState } from "react";
import { ConsoleLayout } from "@/components/ConsoleLayout";
import { VisitCard } from "@/components/VisitCard";
import { ActionButton, FirebaseSetupBanner } from "@/components/ui";
import { useVisits } from "@/hooks/useVisits";
import { transitionVisit } from "@/lib/firestore/visits";
import type { Visit } from "@/lib/types";

const PHARMACY_STAGES = ["at_pharmacy", "pharmacy_processing", "completed"] as const;

export default function PharmacyPage() {
  const { visits, loading, error } = useVisits({ stages: [...PHARMACY_STAGES] });
  const [busyId, setBusyId] = useState<string | null>(null);

  async function act(visit: Visit, stage: Parameters<typeof transitionVisit>[1], note: string) {
    setBusyId(visit.id);
    try {
      const extras = stage === "exited" ? { exitedAt: new Date() } : undefined;
      await transitionVisit(visit.id, stage, note, extras);
    } finally {
      setBusyId(null);
    }
  }

  return (
    <ConsoleLayout title="Pharmacy" subtitle="Dispense and send patient out of clinic">
      <FirebaseSetupBanner />
      {loading ? <p className="text-slate-600">Loading pharmacy queue…</p> : null}
      {error ? <p className="text-rose-600">{error}</p> : null}

      <div className="space-y-4">
        {visits.map((visit) => (
          <VisitCard
            key={visit.id}
            visit={visit}
            actions={
              <>
                {visit.currentStage === "at_pharmacy" ? (
                  <ActionButton
                    label="Start dispensing"
                    disabled={busyId === visit.id}
                    onClick={() => act(visit, "pharmacy_processing", "Dispensing")}
                  />
                ) : null}
                {visit.currentStage === "pharmacy_processing" ? (
                  <ActionButton
                    label="Medicines given"
                    disabled={busyId === visit.id}
                    onClick={() => act(visit, "completed", "Pharmacy complete")}
                  />
                ) : null}
                {visit.currentStage === "completed" ? (
                  <ActionButton
                    label="Patient exited"
                    variant="danger"
                    disabled={busyId === visit.id}
                    onClick={() => act(visit, "exited", "Left clinic")}
                  />
                ) : null}
              </>
            }
          />
        ))}
        {!loading && visits.length === 0 ? (
          <p className="rounded-xl border border-dashed border-slate-300 p-8 text-center text-slate-500">
            Pharmacy queue is empty.
          </p>
        ) : null}
      </div>
    </ConsoleLayout>
  );
}
