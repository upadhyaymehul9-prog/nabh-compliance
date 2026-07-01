import type { Visit } from "@/lib/types";
import { STAGE_COLORS, STAGE_LABELS } from "@/lib/constants";
import { formatDistanceToNow } from "date-fns";

interface VisitCardProps {
  visit: Visit;
  actions?: React.ReactNode;
  highlight?: boolean;
}

export function VisitCard({ visit, actions, highlight }: VisitCardProps) {
  const registeredAt = visit.registeredAt?.toDate?.();
  const waitLabel = registeredAt
    ? formatDistanceToNow(registeredAt, { addSuffix: true })
    : "—";

  return (
    <article
      className={`rounded-xl border bg-white p-4 shadow-sm ${
        highlight ? "border-teal-400 ring-2 ring-teal-100" : "border-slate-200"
      }`}
    >
      <div className="flex flex-wrap items-start justify-between gap-3">
        <div>
          <div className="flex items-center gap-2">
            <span className="rounded-md bg-slate-900 px-2 py-1 text-sm font-bold text-white">
              #{visit.tokenNumber}
            </span>
            <h3 className="text-lg font-semibold text-slate-900">{visit.patientName}</h3>
          </div>
          <p className="mt-1 text-sm text-slate-600">
            Dr. {visit.consultantName} · {visit.currentLocation}
          </p>
          <p className="mt-1 text-xs text-slate-500">Registered {waitLabel}</p>
        </div>
        <span
          className={`rounded-full px-3 py-1 text-xs font-semibold ${STAGE_COLORS[visit.currentStage]}`}
        >
          {STAGE_LABELS[visit.currentStage]}
        </span>
      </div>
      {visit.labEta ? (
        <p className="mt-2 text-sm text-violet-800">
          Lab ETA: {visit.labEta.toDate().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
        </p>
      ) : null}
      {visit.radioEta ? (
        <p className="mt-1 text-sm text-indigo-800">
          Radiology ETA:{" "}
          {visit.radioEta.toDate().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })}
        </p>
      ) : null}
      {actions ? <div className="mt-4 flex flex-wrap gap-2">{actions}</div> : null}
    </article>
  );
}
