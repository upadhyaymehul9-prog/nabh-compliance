"use client";

import Link from "next/link";
import { ConsoleLayout } from "@/components/ConsoleLayout";
import { FirebaseSetupBanner } from "@/components/ui";
import { useDoctors } from "@/hooks/useDoctors";

export default function DoctorPickerPage() {
  const { doctors, loading, error } = useDoctors();

  return (
    <ConsoleLayout title="Doctor console" subtitle="Select your profile to open your queue">
      <FirebaseSetupBanner />
      {loading ? <p className="text-slate-600">Loading doctors…</p> : null}
      {error ? <p className="text-rose-600">{error}</p> : null}
      <div className="grid gap-4 sm:grid-cols-2">
        {doctors.map((doctor) => (
          <Link
            key={doctor.id}
            href={`/doctor/${doctor.id}`}
            className="rounded-xl border border-slate-200 bg-white p-5 shadow-sm hover:border-teal-300"
          >
            <h2 className="text-lg font-bold text-slate-900">Dr. {doctor.name}</h2>
            <p className="text-sm text-slate-600">Room {doctor.roomNumber}</p>
            {doctor.specialty ? (
              <p className="mt-1 text-xs text-slate-500">{doctor.specialty}</p>
            ) : null}
          </Link>
        ))}
      </div>
    </ConsoleLayout>
  );
}
