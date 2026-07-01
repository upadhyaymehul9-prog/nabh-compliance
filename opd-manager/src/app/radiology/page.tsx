"use client";

import { useState } from "react";
import { ConsoleLayout } from "@/components/ConsoleLayout";
import { VisitCard } from "@/components/VisitCard";
import { ActionButton, FirebaseSetupBanner } from "@/components/ui";
import { useVisits } from "@/hooks/useVisits";
import { addMinutes, transitionVisit } from "@/lib/firestore/visits";
import type { Visit } from "@/lib/types";

const RADIO_STAGES = ["at_radiology", "radio_processing", "report_ready_radio"] as const;

export default function RadiologyPage() {
  const { visits, loading, error } = useVisits({ stages: [...RADIO_STAGES] });
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
    <ConsoleLayout title="Radiology" subtitle="Queue, processing, ETA, report ready">
      <FirebaseSetupBanner />
      {loading ? <p className="text-slate-600">Loading radiology queue…</p> : null}
      {error ? <p className="text-rose-600">{error}</p> : null}

      <div className="space-y-4">
        {visits.map((visit) => (
          <VisitCard
            key={visit.id}
            visit={visit}
            actions={
              <>
                {visit.currentStage === "at_radiology" ? (
                  <>
                    <div className="flex items-center gap-2">
                      <label className="text-xs text-slate-600">ETA (min)</label>
                      <input
                        type="number"
                        min={5}
                        max={240}
                        value={etaMinutes[visit.id] ?? 20}
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
                      label="Start scan"
                      disabled={busyId === visit.id}
                      onClick={() =>
                        act(visit, "radio_processing", "Radiology processing", {
                          radioEta: addMinutes(new Date(), etaMinutes[visit.id] ?? 20),
                        })
                      }
                    />
                  </>
                ) : null}
                {visit.currentStage === "radio_processing" ? (
                  <ActionButton
                    label="Report ready"
                    disabled={busyId === visit.id}
                    onClick={() =>
                      act(visit, "report_ready_radio", "Radiology report ready", {
                        radioReadyAt: new Date(),
                      })
                    }
                  />
                ) : null}
                {visit.currentStage === "report_ready_radio" ? (
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
            Radiology queue is empty.
          </p>
        ) : null}
      </div>
    </ConsoleLayout>
  );
}
