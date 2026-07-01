"use client";

import { isFirebaseConfigured } from "@/lib/firebase/config";

export function FirebaseSetupBanner() {
  if (isFirebaseConfigured()) return null;

  return (
    <div className="mb-6 rounded-xl border border-amber-300 bg-amber-50 p-4 text-sm text-amber-950">
      <p className="font-semibold">Firebase not configured</p>
      <p className="mt-1">
        Copy <code className="rounded bg-amber-100 px-1">.env.local.example</code> to{" "}
        <code className="rounded bg-amber-100 px-1">.env.local</code> and add your Firebase
        project keys. See <code className="rounded bg-amber-100 px-1">README.md</code> for seed
        data and security rules.
      </p>
    </div>
  );
}

interface ActionButtonProps {
  label: string;
  onClick: () => void;
  variant?: "primary" | "secondary" | "danger";
  disabled?: boolean;
}

const variants = {
  primary: "bg-teal-700 text-white hover:bg-teal-800",
  secondary: "bg-white text-slate-800 border border-slate-300 hover:bg-slate-50",
  danger: "bg-rose-700 text-white hover:bg-rose-800",
};

export function ActionButton({
  label,
  onClick,
  variant = "primary",
  disabled,
}: ActionButtonProps) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={`rounded-lg px-3 py-2 text-sm font-medium disabled:opacity-50 ${variants[variant]}`}
    >
      {label}
    </button>
  );
}
