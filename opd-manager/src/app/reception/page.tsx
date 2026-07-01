"use client";

import { FormEvent, useState } from "react";
import { ConsoleLayout } from "@/components/ConsoleLayout";
import { FirebaseSetupBanner } from "@/components/ui";
import { useDoctors } from "@/hooks/useDoctors";
import { registerPatient } from "@/lib/firestore/visits";
import { isFirebaseConfigured } from "@/lib/firebase/config";

export default function ReceptionPage() {
  const { doctors, loading, error } = useDoctors();
  const [patientName, setPatientName] = useState("");
  const [patientPhone, setPatientPhone] = useState("");
  const [consultantId, setConsultantId] = useState("");
  const [submitting, setSubmitting] = useState(false);
  const [message, setMessage] = useState<string | null>(null);

  const selectedDoctor = doctors.find((d) => d.id === consultantId);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!isFirebaseConfigured() || !selectedDoctor) return;

    setSubmitting(true);
    setMessage(null);
    try {
      const visitId = await registerPatient({
        patientName,
        patientPhone: patientPhone || undefined,
        consultantId: selectedDoctor.id,
        consultantName: selectedDoctor.name,
        roomNumber: selectedDoctor.roomNumber,
      });
      setMessage(`Patient registered. Token queued for Dr. ${selectedDoctor.name}.`);
      setPatientName("");
      setPatientPhone("");
      setConsultantId("");
      console.info("visit created", visitId);
    } catch (err) {
      setMessage(err instanceof Error ? err.message : "Registration failed");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <ConsoleLayout
      title="Reception"
      subtitle="Register patient — name, consultant, room, auto timestamp"
    >
      <FirebaseSetupBanner />
      <form
        onSubmit={handleSubmit}
        className="max-w-xl space-y-4 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm"
      >
        <div>
          <label className="block text-sm font-medium text-slate-700">Patient name</label>
          <input
            required
            value={patientName}
            onChange={(e) => setPatientName(e.target.value)}
            className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
            placeholder="Full name"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700">Mobile (optional)</label>
          <input
            value={patientPhone}
            onChange={(e) => setPatientPhone(e.target.value)}
            className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
            placeholder="10-digit mobile"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-700">Consultant</label>
          <select
            required
            value={consultantId}
            onChange={(e) => setConsultantId(e.target.value)}
            className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
          >
            <option value="">Select doctor</option>
            {doctors.map((d) => (
              <option key={d.id} value={d.id}>
                Dr. {d.name} — Room {d.roomNumber}
              </option>
            ))}
          </select>
          {loading ? <p className="mt-1 text-xs text-slate-500">Loading doctors…</p> : null}
          {error ? <p className="mt-1 text-xs text-rose-600">{error}</p> : null}
        </div>
        {selectedDoctor ? (
          <p className="rounded-lg bg-teal-50 px-3 py-2 text-sm text-teal-900">
            Room <strong>{selectedDoctor.roomNumber}</strong> will be assigned automatically.
          </p>
        ) : null}
        <button
          type="submit"
          disabled={submitting || !isFirebaseConfigured()}
          className="w-full rounded-lg bg-teal-700 px-4 py-3 font-semibold text-white hover:bg-teal-800 disabled:opacity-50"
        >
          {submitting ? "Registering…" : "Register & queue for doctor"}
        </button>
        {message ? (
          <p className="rounded-lg bg-slate-100 px-3 py-2 text-sm text-slate-800">{message}</p>
        ) : null}
      </form>
    </ConsoleLayout>
  );
}
