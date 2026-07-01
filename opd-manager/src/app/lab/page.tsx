"use client";

import { useState } from "react";
import { ConsoleLayout } from "@/components/ConsoleLayout";
import { VisitCard } from "@/components/VisitCard";
import { ActionButton, FirebaseSetupBanner } from "@/components/ui";
import { useVisits } from "@/hooks/useVisits";
import { addMinutes, transitionVisit } from "@/lib/firestore/visits";
import type { Visit } from "@/lib/types";

const LAB_STAGES = ["at_lab", "lab_processing", "report_ready_lab"] as const;

export default function LabPage() {
  const { visits, loading, error } = useVisits({ stages: [...LAB_STAGES] });
  const [busyId, setBusyId] = useState<string | null>(null);
  const [etaMinutes, setEtaMinutes] = useState<Record<string, number>>({});

  async function act(
    visit: Visit,
    stage: Parameters<typeof transitionVisit>[1],
    note: string,
    extras?: Parameters<typeof transitionVisit>[3],
  ) {
    setBusyId(visit.id);
    try {
      await transitionVisit(visit.id, stage, note, extras);
    } finally {
      setBusyId(null);
    }
  }

  return (
    <ConsoleLayout title="Laboratory" subtitle="Collect patients, set ETA, mark report ready">
      <FirebaseSetupBanner />
      {loading ? <p className="text-slate-600">Loading lab queue…</p> : null}
      {error ? <p className="text-rose-600">{error}</p> : null}

      <div className="space-y-4">
        {visits.map((visit) => (
          <VisitCard
            key={visit.id}
            visit={visit}
            actions={
              <>
                {visit.currentStage === "at_lab" ? (
                  <>
                    <div className="flex items-center gap-2">
                      <label className="text-xs text-slate-600">ETA (min)</label>
                      <input
                        type="number"
                        min={5}
                        max={240}
                        value={etaMinutes[visit.id] ?? 30}
                        onChange={(e) =>
                          setEtaMinutes((prev) => ({
                            ...prev,
                            [visit.id]: Number(e.target.value),
                          }))
                        }
                        className="w-20 rounded border border-slate-300 px-2 py-1 text-sm"
                      />
                    </div>
                    <ActionButton
                      label="Start test"
                      disabled={busyId === visit.id}
                      onClick={() =>
                        act(visit, "lab_processing", "Lab processing", {
                          labEta: addMinutes(new Date(), etaMinutes[visit.id] ?? 30),
                        })
                      }
                    />
                  </>
                ) : null}
                {visit.currentStage === "lab_processing" ? (
                  <ActionButton
                    label="Report ready"
                    disabled={busyId === visit.id}
                    onClick={() =>
                      act(visit, "report_ready_lab", "Lab report ready", {
                        labReadyAt: new Date(),
                      })
                    }
                  />
                ) : null}
                {visit.currentStage === "report_ready_lab" ? (
                  <ActionButton
                    label="Send to doctor"
                    disabled={busyId === visit.id}
                    onClick={() => act(visit, "back_to_doctor", "Return to consultant")}
                  />
                ) : null}
              </>
            }
          />
        ))}
        {!loading && visits.length === 0 ? (
          <p className="rounded-xl border border-dashed border-slate-300 p-8 text-center text-slate-500">
            Lab queue is empty.
          </p>
        ) : null}
      </div>
    </ConsoleLayout>
  );
}
