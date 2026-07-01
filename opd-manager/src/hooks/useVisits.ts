"use client";

import { useEffect, useState } from "react";
import type { Visit } from "@/lib/types";
import { subscribeVisits, type VisitQuery } from "@/lib/firestore/visits";

export function useVisits(filters: VisitQuery = {}) {
  const [visits, setVisits] = useState<Visit[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    const unsub = subscribeVisits(
      filters,
      (data) => {
        setVisits(data);
        setLoading(false);
        setError(null);
      },
      (err) => {
        setError(err.message);
        setLoading(false);
      },
    );
    return () => unsub();
  }, [filters.clinicId, filters.consultantId, filters.stages?.join(",")]);

  return { visits, loading, error };
}
