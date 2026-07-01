"use client";

import { ConsoleLayout } from "@/components/ConsoleLayout";
import { FirebaseSetupBanner } from "@/components/ui";
import { STAGE_COLORS, STAGE_LABELS } from "@/lib/constants";
import { useVisits } from "@/hooks/useVisits";
import { ACTIVE_STAGES } from "@/lib/constants";

export default function ManagerPage() {
  const { visits, loading, error } = useVisits();
  const active = visits.filter((v) => ACTIVE_STAGES.includes(v.currentStage));

  const byStage = ACTIVE_STAGES.map((stage) => ({
    stage,
    count: active.filter((v) => v.currentStage === stage).length,
  })).filter((row) => row.count > 0);

  return (
    <ConsoleLayout
      title="OPD Manager"
      subtitle="Live view — every patient from reception to exit"
    >
      <FirebaseSetupBanner />
      {loading ? <p className="text-slate-600">Loading…</p> : null}
      {error ? <p className="text-rose-600">{error}</p> : null}

      <div className="mb-6 grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <Stat label="Active today" value={active.length} />
        <Stat
          label="In consultation"
          value={active.filter((v) => v.currentStage === "in_consultation").length}
        />
        <Stat
          label="At lab / radiology"
          value={
            active.filter((v) =>
              ["at_lab", "lab_processing", "at_radiology", "radio_processing"].includes(
                v.currentStage,
              ),
            ).length
          }
        />
        <Stat
          label="At pharmacy"
          value={
            active.filter((v) =>
              ["at_pharmacy", "pharmacy_processing"].includes(v.currentStage),
            ).length
          }
        />
      </div>

      {byStage.length > 0 ? (
        <div className="mb-6 flex flex-wrap gap-2">
          {byStage.map(({ stage, count }) => (
            <span
              key={stage}
              className={`rounded-full px-3 py-1 text-xs font-semibold ${STAGE_COLORS[stage]}`}
            >
              {STAGE_LABELS[stage]}: {count}
            </span>
          ))}
        </div>
      ) : null}

      <div className="overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm">
        <table className="min-w-full text-left text-sm">
          <thead className="border-b border-slate-200 bg-slate-50 text-xs uppercase text-slate-500">
            <tr>
              <th className="px-4 py-3">Token</th>
              <th className="px-4 py-3">Patient</th>
              <th className="px-4 py-3">Consultant</th>
              <th className="px-4 py-3">Stage</th>
              <th className="px-4 py-3">Location</th>
            </tr>
          </thead>
          <tbody>
            {active.map((visit) => (
              <tr key={visit.id} className="border-b border-slate-100">
                <td className="px-4 py-3 font-mono font-bold">#{visit.tokenNumber}</td>
                <td className="px-4 py-3">{visit.patientName}</td>
                <td className="px-4 py-3">Dr. {visit.consultantName}</td>
                <td className="px-4 py-3">
                  <span
                    className={`rounded-full px-2 py-1 text-xs font-medium ${STAGE_COLORS[visit.currentStage]}`}
                  >
                    {STAGE_LABELS[visit.currentStage]}
                  </span>
                </td>
                <td className="px-4 py-3">{visit.currentLocation}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {!loading && active.length === 0 ? (
          <p className="p-8 text-center text-slate-500">No active patients.</p>
        ) : null}
      </div>
    </ConsoleLayout>
  );
}

function Stat({ label, value }: { label: string; value: number }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-4 shadow-sm">
      <p className="text-xs font-medium uppercase tracking-wide text-slate-500">{label}</p>
      <p className="mt-1 text-3xl font-bold text-slate-900">{value}</p>
    </div>
  );
}
