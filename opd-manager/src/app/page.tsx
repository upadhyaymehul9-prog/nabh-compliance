import Link from "next/link";

const consoles = [
  {
    href: "/reception",
    title: "Reception",
    description: "Register patients, assign consultant and room, auto timestamp.",
    color: "border-teal-200 bg-teal-50",
  },
  {
    href: "/doctor",
    title: "Doctor console",
    description: "Call patients, consult, send to lab / radiology / pharmacy.",
    color: "border-blue-200 bg-blue-50",
  },
  {
    href: "/lab",
    title: "Laboratory",
    description: "Accept patients, set report ETA, mark ready, send back to doctor.",
    color: "border-violet-200 bg-violet-50",
  },
  {
    href: "/radiology",
    title: "Radiology",
    description: "Queue, processing, ETA, report ready, return to doctor.",
    color: "border-indigo-200 bg-indigo-50",
  },
  {
    href: "/pharmacy",
    title: "Pharmacy",
    description: "Dispense medicines and mark patient exit.",
    color: "border-orange-200 bg-orange-50",
  },
  {
    href: "/manager",
    title: "OPD Manager",
    description: "Live floor view — every patient from entry to exit.",
    color: "border-slate-300 bg-slate-100",
  },
];

const displays = [
  { href: "/display/opd", title: "OPD waiting TV" },
  { href: "/display/lab", title: "Lab status TV" },
  { href: "/display/radiology", title: "Radiology status TV" },
];

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-900 to-slate-800 text-white">
      <div className="mx-auto max-w-6xl px-4 py-12 sm:px-6">
        <p className="text-sm font-semibold uppercase tracking-widest text-teal-300">
          Clinic patient flow
        </p>
        <h1 className="mt-2 text-4xl font-bold tracking-tight sm:text-5xl">OPD Manager</h1>
        <p className="mt-4 max-w-2xl text-lg text-slate-300">
          Guide every outpatient from reception to exit — real-time consoles for staff and TV
          boards for waiting areas. Built on Firebase free tier.
        </p>

        <section className="mt-10">
          <h2 className="text-lg font-semibold text-white">Staff consoles</h2>
          <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {consoles.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={`rounded-2xl border p-5 transition hover:-translate-y-0.5 hover:shadow-lg ${item.color} text-slate-900`}
              >
                <h3 className="text-lg font-bold">{item.title}</h3>
                <p className="mt-2 text-sm text-slate-700">{item.description}</p>
              </Link>
            ))}
          </div>
        </section>

        <section className="mt-10">
          <h2 className="text-lg font-semibold text-white">TV displays</h2>
          <p className="mt-1 text-sm text-slate-400">
            Open full-screen on a smart TV browser — updates in real time.
          </p>
          <div className="mt-4 flex flex-wrap gap-3">
            {displays.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="rounded-xl border border-white/20 bg-white/10 px-4 py-3 text-sm font-medium hover:bg-white/20"
              >
                {item.title}
              </Link>
            ))}
          </div>
        </section>
      </div>
    </div>
  );
}
