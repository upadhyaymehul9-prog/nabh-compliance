"use client";

import { useEffect, useMemo, useState } from "react";
import { useParams } from "next/navigation";
import { useVisits } from "@/hooks/useVisits";
import { STAGE_LABELS } from "@/lib/constants";
import type { Visit } from "@/lib/types";

type ScreenKind = "opd" | "lab" | "radiology";

export default function DisplayPage() {
  const params = useParams<{ screen: string }>();
  const screen = (params.screen as ScreenKind) || "opd";
  const { visits } = useVisits();
  const [clock, setClock] = useState(new Date());

  useEffect(() => {
    const id = setInterval(() => setClock(new Date()), 1000);
    return () => clearInterval(id);
  }, []);

  const rows = useMemo(() => filterForScreen(visits, screen), [visits, screen]);

  const title =
    screen === "lab"
      ? "Laboratory status"
      : screen === "radiology"
        ? "Radiology status"
        : "OPD — Now serving";

  return (
    <div className="min-h-screen bg-slate-950 px-6 py-8 text-white">
      <header className="mb-8 flex items-end justify-between border-b border-white/10 pb-6">
        <div>
          <p className="text-sm uppercase tracking-[0.2em] text-teal-300">OPD Manager</p>
          <h1 className="mt-2 text-4xl font-bold md:text-5xl">{title}</h1>
        </div>
        <p className="font-mono text-2xl text-slate-300">
          {clock.toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" })}
        </p>
      </header>

      <div className="space-y-4">
        {rows.map((visit) => (
          <div
            key={visit.id}
            className="flex flex-wrap items-center justify-between gap-4 rounded-2xl border border-white/10 bg-white/5 px-6 py-5"
          >
            <div className="flex items-center gap-4">
              <span className="rounded-xl bg-teal-500 px-4 py-2 text-2xl font-black text-slate-950">
                #{visit.tokenNumber}
              </span>
              <div>
                <p className="text-2xl font-semibold">{visit.patientName}</p>
                <p className="text-slate-300">
                  Dr. {visit.consultantName} · {visit.currentLocation}
                </p>
              </div>
            </div>
            <div className="text-right">
              <p className="text-xl font-bold text-teal-200">
                {STAGE_LABELS[visit.currentStage]}
              </p>
              {visit.labEta && screen === "lab" ? (
                <p className="mt-1 text-lg text-violet-200">
                  Ready ~{" "}
                  {visit.labEta.toDate().toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                </p>
              ) : null}
              {visit.radioEta && screen === "radiology" ? (
                <p className="mt-1 text-lg text-indigo-200">
                  Ready ~{" "}
                  {visit.radioEta.toDate().toLocaleTimeString([], {
                    hour: "2-digit",
                    minute: "2-digit",
                  })}
                </p>
              ) : null}
            </div>
          </div>
        ))}
        {rows.length === 0 ? (
          <p className="rounded-2xl border border-dashed border-white/20 p-12 text-center text-2xl text-slate-400">
            No updates to display
          </p>
        ) : null}
      </div>
    </div>
  );
}

function filterForScreen(visits: Visit[], screen: ScreenKind): Visit[] {
  if (screen === "lab") {
    return visits.filter((v) =>
      ["at_lab", "lab_processing", "report_ready_lab"].includes(v.currentStage),
    );
  }
  if (screen === "radiology") {
    return visits.filter((v) =>
      ["at_radiology", "radio_processing", "report_ready_radio"].includes(v.currentStage),
    );
  }
  return visits.filter((v) =>
    ["doctor_calling", "waiting_doctor", "back_to_doctor", "report_ready_lab", "report_ready_radio"].includes(
      v.currentStage,
    ),
  );
}
