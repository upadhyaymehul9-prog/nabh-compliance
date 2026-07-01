"use client";

import { useEffect, useState } from "react";
import type { Doctor } from "@/lib/types";
import { CLINIC_ID } from "@/lib/firebase/config";
import { subscribeDoctors } from "@/lib/firestore/visits";

export function useDoctors(clinicId = CLINIC_ID) {
  const [doctors, setDoctors] = useState<Doctor[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    const unsub = subscribeDoctors(
      clinicId,
      (data) => {
        setDoctors(data);
        setLoading(false);
        setError(null);
      },
      (err) => {
        setError(err.message);
        setLoading(false);
      },
    );
    return () => unsub();
  }, [clinicId]);

  return { doctors, loading, error };
}
