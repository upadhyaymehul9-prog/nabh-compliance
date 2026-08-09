#!/usr/bin/env python3
"""Generate 10 NABH landing pages from verified nabh.co / official NABH facts only."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def faq_json(pairs: list[tuple[str, str]]) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in pairs
        ],
    }
    return json.dumps(payload, indent=2)


def related_html(items: list[tuple[str, str]]) -> str:
    lis = []
    for url, text in items:
        lis.append(
            f'          <li>→ <a href="https://accredready.in/{url}" class="rounded text-verify '
            f'underline-offset-2 hover:underline focus-visible:ring-2 focus-visible:ring-verify">{text}</a></li>'
        )
    return "\n".join(lis)


def render(page: dict) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['title']}</title>
  <meta name="description" content="{page['meta']}" />
  <meta name="keywords" content="{page['keywords']}" />
  <link rel="canonical" href="https://accredready.in/{page['canonical']}" />
  <meta property="og:title" content="{page['og_title']}" />
  <meta property="og:description" content="{page['meta']}" />
  <meta property="og:url" content="https://accredready.in/{page['canonical']}" />
  <meta property="og:image" content="https://accredready.in/logo512.png" />
  <meta property="og:type" content="article" />
  <script type="application/ld+json">
{page['faq_json']}
  </script>
  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{page['h1_plain']}",
  "description": "{page['meta']}",
  "author": {{"@type": "Person", "name": "Dr. Mehul Upadhyay", "jobTitle": "Healthcare Operations Leader"}},
  "publisher": {{"@type": "Organization", "name": "AccredReady", "url": "https://accredready.in"}},
  "datePublished": "2026-08-09",
  "dateModified": "2026-08-09",
  "mainEntityOfPage": "https://accredready.in/{page['canonical']}"
}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{ extend: {{
        colors: {{ ink:'#0B1B2B', paper:'#FBFDFD', verify:'#0E8A5F', verifydark:'#0A6B4A', signal:'#D97706', alert:'#DC2626', slate:'#4B5D6E', hairline:'#DCE6E4', mint:'#EBF4F0' }},
        fontFamily: {{ display:['"Bricolage Grotesque"','sans-serif'], body:['"IBM Plex Sans"','sans-serif'], mono:['"IBM Plex Mono"','monospace'] }}
      }}}}
    }};
  </script>
  <style type="text/tailwindcss">
    @layer components {{
      .tbl {{ @apply w-full border-collapse text-[0.9rem]; }}
      .tbl th {{ @apply bg-mint px-4 py-3 text-left font-mono text-[0.78rem] font-medium uppercase tracking-wide text-ink; }}
      .tbl td {{ @apply border-b border-hairline px-4 py-2.5 align-top text-slate; }}
      .tbl strong {{ @apply text-ink; }}
    }}
  </style>
  <style>
    body {{ background:#FBFDFD; }}
    html {{ scroll-behavior: smooth; }}
    @media (prefers-reduced-motion: reduce) {{
      html {{ scroll-behavior: auto; }}
      *, *::before, *::after {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }}
    }}
  </style>
</head>
<body class="font-body text-ink leading-[1.7] antialiased">
  <a href="#main" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-[200] focus:rounded-lg focus:bg-verify focus:px-4 focus:py-2 focus:text-white focus:outline-none">Skip to content</a>
  <nav class="sticky top-0 z-[100] border-b border-hairline bg-paper/90 backdrop-blur">
    <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:px-8">
      <a href="https://accredready.in" class="rounded font-display text-[22px] font-bold tracking-[-0.01em] text-ink focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2">AccredReady</a>
      <a href="https://accredready.in" class="rounded-xl bg-verify px-5 py-2.5 text-[15px] font-semibold text-white transition-all duration-150 hover:-translate-y-px hover:bg-verifydark hover:shadow-[0_6px_16px_rgba(14,138,95,0.25)] focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 motion-reduce:transform-none motion-reduce:transition-none">Start free trial</a>
    </div>
  </nav>
  <main id="main">
    <header class="mx-auto max-w-3xl px-5 pb-10 pt-16 text-center sm:px-8">
      <span class="mb-6 inline-flex items-center gap-2 rounded-lg border border-verify/20 bg-mint px-3 py-1.5 font-mono text-[13px] uppercase tracking-wide text-verify"><span class="h-1.5 w-1.5 rounded-full bg-verify"></span>{page['eyebrow']}</span>
      <h1 class="mb-5 font-display text-[clamp(1.8rem,4vw,3rem)] font-bold leading-[1.1] tracking-[-0.02em]">{page['h1']}</h1>
      <p class="mx-auto max-w-2xl text-lg text-slate">{page['sub']}</p>
    </header>
    <article class="mx-auto max-w-3xl px-5 pb-16 sm:px-8 [&_h2]:mb-4 [&_h2]:mt-10 [&_h2]:font-display [&_h2]:text-2xl [&_h2]:font-bold [&_h3]:mb-2 [&_h3]:mt-7 [&_h3]:font-display [&_h3]:text-lg [&_h3]:font-bold [&_h3]:text-ink [&_p]:mb-4 [&_p]:text-[0.97rem] [&_p]:text-slate [&_strong]:text-ink">
      <div class="mb-8 flex flex-wrap items-center gap-x-4 gap-y-1 border-b border-hairline pb-5 text-[0.83rem] text-slate">
        <span class="flex items-center gap-1.5">
          <span class="h-6 w-6 rounded-full bg-mint flex items-center justify-center font-display text-[11px] font-bold text-verify" aria-hidden="true">MU</span>
          <strong class="text-ink">Dr. Mehul Upadhyay</strong>
        </span>
        <span class="text-slate/50">·</span>
        <span>Healthcare Operations Leader</span>
        <span class="text-slate/50">·</span>
        <time datetime="2026-08-09">Published: August 2026</time>
        <span class="text-slate/50">·</span>
        <time datetime="2026-08-09">Updated: August 2026</time>
      </div>
{page['body']}
      <div class="my-8 rounded-xl border border-hairline bg-white px-5 py-4 text-[0.83rem] text-slate">
        <p class="!mb-0"><strong class="text-ink">Sources:</strong> {page['sources']} Always verify live rules and fees at <a href="https://nabh.co" target="_blank" rel="noopener noreferrer" class="rounded text-verify underline-offset-2 hover:underline focus-visible:ring-2 focus-visible:ring-verify">nabh.co</a>.</p>
      </div>
      <div class="my-6 rounded-xl border border-hairline bg-white px-5 py-4 text-[0.9rem]">
        <p class="!mb-2 font-mono text-[12px] uppercase tracking-wide text-slate">Related pages</p>
        <ul class="space-y-1.5 !mb-0">
{page['related']}
        </ul>
      </div>
      <div class="my-10 rounded-2xl bg-ink px-6 py-12 text-center">
        <p class="font-mono text-[12px] uppercase tracking-widest text-white/50 mb-3">AccredReady</p>
        <h2 class="!mt-0 font-display text-2xl font-bold !text-white">{page['cta_h']}</h2>
        <p class="mx-auto mt-3 max-w-lg !text-white/70">{page['cta_p']}</p>
        <a href="https://accredready.in" class="mt-5 inline-block rounded-xl bg-verify px-8 py-3.5 font-semibold text-white transition-all duration-150 hover:-translate-y-px hover:bg-verifydark hover:shadow-[0_6px_16px_rgba(14,138,95,0.25)] focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink motion-reduce:transform-none motion-reduce:transition-none">Start free on AccredReady →</a>
      </div>
    </article>
  </main>
  <footer class="bg-ink text-white/70">
    <div class="mx-auto max-w-7xl px-6 py-12 lg:px-8">
      <nav aria-label="Footer" class="flex flex-wrap justify-center gap-x-7 gap-y-3 text-[14px]">
        <a href="https://accredready.in" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">Home</a>
        <a href="https://accredready.in/learn" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">Learn</a>
        <a href="https://accredready.in/nabh-accreditation-software" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">NABH Software</a>
        <a href="https://accredready.in/privacy" class="rounded hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-verify focus-visible:ring-offset-2 focus-visible:ring-offset-ink">Privacy Policy</a>
      </nav>
      <p class="mt-8 text-center font-mono text-[12px] text-white/45">© 2026 AccredReady by MK Tech.</p>
    </div>
  </footer>
</body>
</html>
"""


def page(
    *,
    path: str,
    title: str,
    meta: str,
    keywords: str,
    canonical: str,
    og_title: str,
    h1_plain: str,
    eyebrow: str,
    h1: str,
    sub: str,
    faqs: list[tuple[str, str]],
    body: str,
    sources: str,
    related: list[tuple[str, str]],
    cta_h: str,
    cta_p: str,
) -> dict:
    return {
        "path": path,
        "title": title,
        "meta": meta,
        "keywords": keywords,
        "canonical": canonical,
        "og_title": og_title,
        "h1_plain": h1_plain,
        "eyebrow": eyebrow,
        "h1": h1,
        "sub": sub,
        "faq_json": faq_json(faqs),
        "body": body,
        "sources": sources,
        "related": related_html(related),
        "cta_h": cta_h,
        "cta_p": cta_p,
    }


PAGES = [
    page(
        path="public/learn/nabh-surveillance-assessment.html",
        title="NABH surveillance assessment — mid-cycle check explained | AccredReady",
        meta="NABH HCO Full Accreditation includes surveillance at 21–24 months in the 4-year cycle. What it is, how it differs from renewal, and how to stay ready.",
        keywords="NABH surveillance assessment, NABH mid cycle surveillance, NABH 21-24 months, NABH surveillance vs renewal",
        canonical="learn/nabh-surveillance-assessment",
        og_title="NABH surveillance assessment — mid-cycle check explained",
        h1_plain="NABH surveillance assessment — what happens mid-cycle",
        eyebrow="NABH Guide · Surveillance",
        h1="NABH surveillance assessment — what happens mid-cycle",
        sub="For already-accredited hospitals: the mid-cycle verification that quality did not freeze after certificate day.",
        faqs=[
            (
                "When does NABH surveillance happen for HCO Full Accreditation?",
                "Under NABH Hospital Accreditation Standards 6th Edition (effective 1 January 2025), the cycle includes a Surveillance Assessment at 21–24 months within 4-year validity. Source: NABH HCO 6th Edition.",
            ),
            (
                "Is surveillance the same as renewal assessment?",
                "No. Surveillance is mid-cycle. For HCO Full, NABH states the accredited hospital has to apply for Renewal Assessment 6 months prior to expiry. Source: NABH HCO 6th Edition.",
            ),
            (
                "Do Entry Level certificates use the same 21–24 month surveillance?",
                "Entry Level Certification is a 2-year cycle with its own assessment matrix on nabh.co. Do not assume the HCO Full 21–24 month calendar applies to ELC without checking the Entry-Level Certification Programme (2nd Edition) page and your certificate.",
            ),
            (
                "Can NABH also do focus or surprise assessments?",
                "Yes. NABH publishes separate Focus Assessment and Surprise Assessment policies, listed under programme document sections on nabh.co. These are distinct from scheduled surveillance.",
            ),
            (
                "What should hospitals keep ready between award and surveillance?",
                "Continuous evidence: committee activity, KPI trends with action, closed CAPAs, current statutory/FMS documents, and staff who can demonstrate current practice.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>For NABH HCO Full Accreditation under the 6th Edition (effective 1 January 2025), the certificate is valid for 4 years and the published cycle includes a Surveillance Assessment at 21–24 months.</strong> Renewal is separate: NABH states the accredited hospital has to apply for Renewal Assessment 6 months prior to expiry. Source: NABH Accreditation Standards for Hospitals, 6th Edition.</p>
      <div class="my-5 rounded-xl border border-signal/30 bg-signal/5 px-6 py-4"><p class="!mb-0 !text-ink"><strong>Three different events:</strong> final/renewal assessment that awards the certificate, mid-cycle surveillance inside validity, and focus/surprise assessments under separate NABH policies.</p></div>
      <h2>HCO Full cycle milestones (published)</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Stage</th><th>NABH HCO 6th Edition</th></tr></thead><tbody>
      <tr><td><strong>Certificate validity</strong></td><td><strong>4 years</strong></td></tr>
      <tr><td><strong>Surveillance Assessment</strong></td><td><strong>21–24 months</strong></td></tr>
      <tr><td><strong>Renewal application</strong></td><td><strong>6 months prior</strong> to expiry</td></tr>
      </tbody></table></div>
      <h2>What surveillance is checking</h2>
      <p>Surveillance confirms continued compliance after award — not a paperwork re-launch. Expect scrutiny of whether processes are still practised, whether quality data is still analysed, and whether statutory/facility requirements remain current. Exact scope follows NABH assessment and surveillance policy documents linked from programme pages on <a href="https://nabh.co" target="_blank" rel="noopener noreferrer" class="rounded text-verify underline-offset-2 hover:underline focus-visible:ring-2 focus-visible:ring-verify">nabh.co</a>.</p>
      <h2>SHCO and Entry Level — do not copy the HCO calendar blindly</h2>
      <p>SHCO Full Accreditation and Entry Level Certification publish their own programme rules on nabh.co. NABH hospital FAQs state most accreditations are valid for three to four years with mid-cycle surveillance. Entry Level Certification is a <strong>2-year</strong> certification cycle (Entry-Level Certification Programme, 2nd Edition). Always match your pathway’s page and the dates on your certificate.</p>
      <h2>Frequently asked questions</h2>
      <h3>When does NABH surveillance happen for HCO Full Accreditation?</h3>
      <p>At <strong>21–24 months</strong> in the 4-year HCO Full cycle under the 6th Edition process description.</p>
      <h3>Is surveillance the same as renewal assessment?</h3>
      <p>No. Surveillance is mid-cycle. HCO Full renewal applications are due <strong>6 months prior</strong> to expiry.</p>
      <h3>Do Entry Level certificates use the same 21–24 month surveillance?</h3>
      <p>ELC is a 2-year cycle with its own matrix. Confirm on the ELC programme page and your certificate.</p>
      <h3>Can NABH also do focus or surprise assessments?</h3>
      <p>Yes — under separate published NABH policies listed on nabh.co programme pages.</p>
      <h3>What should hospitals keep ready between award and surveillance?</h3>
      <p>Live committees, KPI action, closed CAPAs, current statutory documents, and staff demonstration of practice.</p>
""",
        sources='NABH Accreditation Standards for Hospitals, 6th Edition (effective 1 Jan 2025): 4-year validity, surveillance at 21–24 months, renewal application 6 months prior. ELC 2-year cycle: <a href="https://nabh.co/programmes/entry-level-hospitals-certification-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">Entry-Level Certification Programme</a>. Validity FAQ: nabh.co FAQs – Hospitals.',
        related=[
            ("learn/nabh-renewal-guide", "NABH renewal and reaccreditation"),
            ("learn/nabh-certificate-validity", "NABH certificate validity by programme"),
            ("learn/nabh-assessment-preparation", "NABH assessment preparation"),
            ("nabh-accreditation-software", "NABH accreditation software"),
        ],
        cta_h="Stay ready between assessments",
        cta_p="Track compliance, CAPAs, KPIs, and dates on AccredReady so surveillance is continuity — not a scramble.",
    ),
    page(
        path="public/learn/nabh-certificate-validity.html",
        title="NABH certificate validity — HCO, SHCO, Entry Level | AccredReady",
        meta="NABH HCO Full Accreditation is valid 4 years; Entry Level Certification is a 2-year cycle. What nabh.co and the HCO 6th Edition publish about validity and renewal timing.",
        keywords="NABH certificate validity, NABH accreditation validity years, NABH ELC 2 years, NABH HCO 4 years",
        canonical="learn/nabh-certificate-validity",
        og_title="NABH certificate validity — HCO, SHCO, Entry Level",
        h1_plain="NABH certificate validity — how long accreditation lasts",
        eyebrow="NABH Guide · Validity",
        h1="NABH certificate validity — how long accreditation lasts",
        sub="Validity periods and renewal timing from official NABH programme documents — not guesswork from old PDFs.",
        faqs=[
            (
                "How long is NABH HCO Full Accreditation valid?",
                "Four years from the date the Accreditation Committee formally approves the result, per NABH Hospital Accreditation Standards 6th Edition (effective 1 January 2025).",
            ),
            (
                "How long is NABH Entry Level Certification valid?",
                "The Entry-Level Certification Programme (2nd Edition) fee table is published as certification fees for 2 years on nabh.co. Treat ELC as a 2-year certification cycle and confirm dates on your certificate.",
            ),
            (
                "How long is SHCO Full Accreditation valid?",
                "NABH hospital FAQs state most accreditations are valid for three to four years with mid-cycle surveillance. Confirm the validity printed on your SHCO certificate and the current SHCO programme documents on nabh.co before planning renewal.",
            ),
            (
                "When must an HCO apply for renewal?",
                "For HCO Full under the 6th Edition process description, the accredited hospital has to apply for Renewal Assessment 6 months prior to expiry of validity.",
            ),
            (
                "What happens if the certificate expires?",
                "You no longer hold current accredited/certified status until a new certificate is issued. For scheme incentives that depend on valid NABH status, the State Health Agency tier may revert until a valid certificate is re-submitted. Confirm with your SHA and nabh.co.",
            ),
        ],
        body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH HCO Full Accreditation is valid for 4 years under the Hospital Accreditation Standards 6th Edition (effective 1 January 2025). NABH Entry Level Certification is published as a 2-year certification fee/cycle on the Entry-Level Certification Programme (2nd Edition) page.</strong> For SHCO Full Accreditation, confirm the validity on your certificate and current nabh.co SHCO documents — NABH FAQs describe most accreditations as three to four years with mid-cycle surveillance.</p>
      <h2>Validity snapshot (official sources)</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Programme</th><th>Validity (as published)</th><th>Source</th></tr></thead><tbody>
      <tr><td><strong>HCO Full Accreditation</strong></td><td><strong>4 years</strong></td><td>HCO 6th Edition (effective 1 Jan 2025)</td></tr>
      <tr><td><strong>Entry Level Certification</strong></td><td><strong>2-year</strong> certification cycle/fees</td><td>ELC 2nd Edition page, nabh.co</td></tr>
      <tr><td><strong>SHCO Full Accreditation</strong></td><td>Confirm on certificate / current SHCO docs (FAQ: 3–4 years typical)</td><td>nabh.co SHCO programme + FAQs</td></tr>
      </tbody></table></div>
      <h2>Renewal timing that is explicitly published</h2>
      <p>For HCO Full, NABH’s 6th Edition process note states the accredited hospital has to apply for Renewal Assessment <strong>6 months prior</strong> to expiry. The same edition places Surveillance Assessment at <strong>21–24 months</strong>. Entry Level renewals follow the ELC assessment matrix (Core / Commitment / Excellence by bed strength and cycle) on the ELC programme page — do not invent ELC surveillance months that NABH has not published there.</p>
      <h2>Always trust the certificate face</h2>
      <p>Programme pages and editions change. The unique certificate number and validity dates on your issued certificate, plus the live programme page on nabh.co, override any secondary guide — including this one — if they disagree.</p>
      <h2>Frequently asked questions</h2>
      <h3>How long is NABH HCO Full Accreditation valid?</h3>
      <p><strong>4 years</strong> under HCO 6th Edition (effective 1 January 2025).</p>
      <h3>How long is NABH Entry Level Certification valid?</h3>
      <p>Published as a <strong>2-year</strong> certification cycle/fee structure on the ELC 2nd Edition page.</p>
      <h3>How long is SHCO Full Accreditation valid?</h3>
      <p>Confirm on your certificate and current SHCO documents. NABH FAQs describe most accreditations as three to four years with mid-cycle surveillance.</p>
      <h3>When must an HCO apply for renewal?</h3>
      <p><strong>6 months prior</strong> to expiry for HCO Full under the 6th Edition process description.</p>
      <h3>What happens if the certificate expires?</h3>
      <p>Current accredited/certified status lapses until re-issued. Scheme incentive tiers that depend on valid NABH status may drop until the SHA receives a valid certificate.</p>
""",
        sources='HCO 6th Edition (effective 1 Jan 2025); <a href="https://nabh.co/programmes/entry-level-hospitals-certification-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">Entry-Level Certification Programme (2nd Edition)</a>; <a href="https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">SHCO Accreditation Programme</a>; nabh.co FAQs – Hospitals.',
        related=[
            ("learn/nabh-renewal-guide", "NABH renewal guide"),
            ("learn/nabh-surveillance-assessment", "NABH surveillance assessment"),
            ("nabh-accreditation-cost", "NABH accreditation cost"),
            ("nabh-entry-level-certification", "NABH Entry Level Certification guide"),
        ],
        cta_h="Track validity dates with your compliance work",
        cta_p="AccredReady helps quality teams keep programme tracking and renewal dates in one place across HCO, SHCO, ELC, and ECO.",
    ),
]

# Remaining pages appended below in main


def more_pages() -> list[dict]:
    out = []
    out.append(
        page(
            path="public/learn/nabh-entry-level-vs-full.html",
            title="NABH Entry Level vs Full Accreditation — which to choose | AccredReady",
            meta="Compare NABH Entry Level Certification (2nd Edition, 2-year cycle) with HCO/SHCO Full Accreditation using official nabh.co eligibility, process, and fee facts.",
            keywords="NABH Entry Level vs Full Accreditation, ELC vs NABH full, HOPE ELC vs hospital accreditation",
            canonical="learn/nabh-entry-level-vs-full",
            og_title="NABH Entry Level vs Full Accreditation — which to choose",
            h1_plain="NABH Entry Level vs Full Accreditation — which pathway fits",
            eyebrow="NABH Guide · Programme choice",
            h1="NABH Entry Level vs Full Accreditation — which pathway fits",
            sub="A decision page built from nabh.co programme pages — not marketing slogans.",
            faqs=[
                (
                    "What is NABH Entry Level Certification?",
                    "The Entry-Level Certification Programme (2nd Edition) is a unified quality framework for SHCOs (up to 50 beds) and hospitals (51 beds and above), with Core/Commitment/Excellence applicability varying by bed strength and assessment cycle. Source: nabh.co ELC programme page.",
                ),
                (
                    "How long does each pathway’s certificate last?",
                    "HCO Full Accreditation: 4 years (HCO 6th Edition). Entry Level Certification: 2-year certification cycle/fees (ELC 2nd Edition page). Confirm SHCO Full validity on your certificate and current SHCO documents.",
                ),
                (
                    "Can a hospital start with ELC and later go for Full Accreditation?",
                    "Yes in principle — nabh.co describes Entry Level as a structured start and foundation for growth toward fuller accreditation. Your facility must still meet the eligibility and standards of the Full programme you later choose.",
                ),
                (
                    "What occupancy does ELC require?",
                    "ELC publishes minimum occupancy: final assessment — minimum 20% occupancy during the last 3 months; 1st renewal — minimum 25% over the preceding 1 year; 2nd renewal — minimum 30% over the preceding 1 year. Source: nabh.co ELC page.",
                ),
                (
                    "Which fees apply?",
                    "Use the live fee tables on nabh.co for ELC, HCO Full, and SHCO Full. ELC lists 2-year certification fees by bed slab (with discounted fees till 30 September 2026 on selected slabs) plus 18% GST. Do not rely on secondary sites for fee decisions.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>Choose NABH Entry Level Certification when you need a published 2-year certification pathway with a staged Core/Commitment/Excellence matrix; choose HCO or SHCO Full Accreditation when your facility type and readiness match the full accreditation programme for hospitals (&gt;50 beds typically) or small healthcare organisations (≤50 beds).</strong> Exact fit depends on bed strength, services, and eligibility on nabh.co — not on which brochure looks simpler.</p>
      <h2>Side-by-side facts from nabh.co</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Question</th><th>Entry Level Certification (2nd Edition)</th><th>Full Accreditation</th></tr></thead><tbody>
      <tr><td><strong>Who it covers</strong></td><td>Unified framework for ≤50 beds (SHCO) and 51+ beds (HCO)</td><td>HCO Full for hospitals; SHCO Full for ≤50 sanctioned beds (separate programmes)</td></tr>
      <tr><td><strong>Validity / cycle</strong></td><td>2-year certification fees/cycle</td><td>HCO Full: 4 years (6th Edition)</td></tr>
      <tr><td><strong>Standards model</strong></td><td>Core / Commitment / Excellence by bed strength &amp; cycle</td><td>Full programme standards for HCO or SHCO edition in force</td></tr>
      <tr><td><strong>Functional minimum before apply</strong></td><td>Functional ≥6 months; standards implemented ≥3 months</td><td>SHCO page: operational data ≥6 months; standards ≥3 months (plus occupancy rule)</td></tr>
      </tbody></table></div>
      <h2>ELC assessment matrix (published)</h2>
      <p>On first assessment, 1–50 bed new applicants are assessed on <strong>Only Core</strong>; 51+ bed new applicants on <strong>Core + Commitment</strong>. Later renewal cycles add Commitment and Excellence per the matrix on the ELC programme page. Source: nabh.co Entry-Level Certification Programme (2nd Edition).</p>
      <h2>When Full Accreditation is the better first target</h2>
      <p>If leadership already wants the full hospital or SHCO accreditation scope, empanelment partners specifically require Full Accreditation, or your quality system is already near full-programme depth, starting Full can avoid a double transition. If you are building basics — SOPs, infection control, patient rights, governance — ELC is the published stepping-stone pathway.</p>
      <h2>Frequently asked questions</h2>
      <h3>What is NABH Entry Level Certification?</h3>
      <p>A unified 2nd Edition certification framework for SHCOs (≤50 beds) and hospitals (51+), with Core/Commitment/Excellence applicability by bed strength and cycle.</p>
      <h3>How long does each pathway’s certificate last?</h3>
      <p>HCO Full: <strong>4 years</strong>. ELC: <strong>2-year</strong> cycle/fees. SHCO Full: confirm on certificate and current nabh.co documents.</p>
      <h3>Can a hospital start with ELC and later go for Full?</h3>
      <p>Yes in principle — ELC is described as a foundation for growth. You must still meet Full programme eligibility later.</p>
      <h3>What occupancy does ELC require?</h3>
      <p>Final assessment 20% (last 3 months); 1st renewal 25% (preceding 1 year); 2nd renewal 30% (preceding 1 year).</p>
      <h3>Which fees apply?</h3>
      <p>Only the live nabh.co fee tables for your programme and bed slab, plus 18% GST.</p>
""",
            sources='<a href="https://nabh.co/programmes/entry-level-hospitals-certification-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">ELC 2nd Edition</a>; HCO 6th Edition validity; <a href="https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">SHCO programme</a>; nabh.co FAQs – Hospitals.',
            related=[
                ("nabh-entry-level-certification", "Complete ELC guide"),
                ("learn/nabh-hco-vs-shco", "HCO vs SHCO — which programme"),
                ("nabh-accreditation-cost", "NABH fee structure"),
                ("nabh-elc-software", "NABH ELC software"),
            ],
            cta_h="Pick a programme, then track it properly",
            cta_p="AccredReady supports HCO Full, SHCO Full, HCO/SHCO Entry Level pathways, and ECO — so your tracker matches the programme you actually applied for.",
        )
    )
    out.append(
        page(
            path="public/learn/nabh-hco-vs-shco.html",
            title="NABH HCO vs SHCO — which programme for your beds | AccredReady",
            meta="NABH FAQs: hospitals with more than 50 beds typically use Hospital (HCO) Accreditation; 50 beds or fewer may use SHCO Accreditation or Entry Level. Official eligibility facts.",
            keywords="NABH HCO vs SHCO, NABH 50 beds, small healthcare organisation accreditation, hospital accreditation programme choice",
            canonical="learn/nabh-hco-vs-shco",
            og_title="NABH HCO vs SHCO — which programme for your beds",
            h1_plain="NABH HCO vs SHCO — which programme fits your facility",
            eyebrow="NABH Guide · HCO vs SHCO",
            h1="NABH HCO vs SHCO — which programme fits your facility",
            sub="Bed strength and facility type decide the pathway. Here is what nabh.co actually publishes.",
            faqs=[
                (
                    "What is the bed threshold between SHCO and HCO?",
                    "NABH hospital FAQs state large hospitals (more than 50 beds) typically opt for Hospital Accreditation, while smaller institutions (50 beds or fewer) may pursue SHCO Accreditation or Entry-Level Certification. The SHCO programme page states eligibility for hospitals/day care/super-specialty centres with ≤50 sanctioned beds.",
                ),
                (
                    "What are SHCO eligibility minimums?",
                    "Per the SHCO Accreditation Programme page: ≤50 sanctioned beds; minimum 6 months of operational data; minimum 30% average bed occupancy over the last 6 months; implementation of NABH SHCO standards for at least 3 months; commitment to legal/statutory compliance. Exclusions include polyclinics, diagnostic centres, and standalone eye/dental hospitals or centres.",
                ),
                (
                    "Is Entry Level only for small hospitals?",
                    "No. Entry-Level Certification Programme (2nd Edition) is a unified framework for SHCOs (up to 50 beds) and hospitals (51 beds and above), with different Core/Commitment/Excellence matrices by bed strength and cycle.",
                ),
                (
                    "Which SHCO standards edition is current on nabh.co?",
                    "The SHCO programme page references SHCO Accreditation Programme (3rd Edition August 2022) with revised fees w.e.f. 01.04.2024. Confirm the live guidebook/edition on nabh.co before implementation.",
                ),
                (
                    "What are current SHCO Full fees on nabh.co?",
                    "For up to 50 beds (revised w.e.f. 01.04.2024): application fee ₹25,000; annual fee ₹1,50,000; virtual assessment fee ₹3,000; focus assessment ₹15,000; re-issue ₹6,000; plus 18% GST. Verify live figures before payment.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>If you have more than 50 beds, NABH’s hospital FAQ points you toward Hospital (HCO) Accreditation; if you have 50 beds or fewer, SHCO Accreditation or Entry-Level Certification are the typical pathways.</strong> Sanctioned bed strength, service type, and exclusions matter more than what a neighbouring hospital chose.</p>
      <h2>Official routing rule</h2>
      <p>From nabh.co FAQs – Hospitals: large hospitals (with more than 50 beds) typically opt for Hospital Accreditation, while smaller institutions (50 beds or fewer) may pursue the SHCO Accreditation or Entry-Level Certification. Clinics, dental centres, AYUSH, imaging, and laboratories have separate programmes.</p>
      <h2>SHCO Full — published eligibility</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>≤50 sanctioned beds (hospitals, day care, super/specialty centres)</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Minimum 6 months operational data</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Minimum 30% average bed occupancy over the last 6 months</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>SHCO standards implemented at least 3 months</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Exclusions: polyclinics, diagnostic centres, standalone eye/dental hospitals or centres</span></li>
      </ul>
      <h2>HCO Full — where it sits</h2>
      <p>HCO Full Accreditation uses the Hospital Accreditation Standards (6th Edition effective 1 January 2025 for the current hospital standards cycle described by NABH). Certificate validity is <strong>4 years</strong>, with surveillance at 21–24 months and renewal application 6 months prior to expiry. Confirm your hospital’s applicable edition and portal instructions before applying.</p>
      <h2>Frequently asked questions</h2>
      <h3>What is the bed threshold between SHCO and HCO?</h3>
      <p>FAQ guidance: &gt;50 beds typically HCO; ≤50 beds typically SHCO or Entry Level. SHCO page: ≤50 sanctioned beds.</p>
      <h3>What are SHCO eligibility minimums?</h3>
      <p>6 months operations, 30% occupancy over last 6 months, standards implemented 3 months, plus statutory commitment — see SHCO page for full list and exclusions.</p>
      <h3>Is Entry Level only for small hospitals?</h3>
      <p>No. ELC 2nd Edition covers ≤50 and 51+ with different assessment matrices.</p>
      <h3>Which SHCO edition is current?</h3>
      <p>Programme page cites 3rd Edition August 2022 with fees revised w.e.f. 01.04.2024 — confirm live on nabh.co.</p>
      <h3>What are current SHCO Full fees?</h3>
      <p>Application ₹25,000; annual ₹1,50,000; virtual ₹3,000; focus ₹15,000; re-issue ₹6,000; +18% GST (up to 50 beds table).</p>
""",
            sources='nabh.co FAQs – Hospitals; <a href="https://nabh.co/programmes/small-healthcare-organisation-shco-accreditation-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">SHCO Accreditation Programme</a>; HCO 6th Edition validity/surveillance notes; ELC 2nd Edition unified framework.',
            related=[
                ("learn/nabh-entry-level-vs-full", "Entry Level vs Full Accreditation"),
                ("learn/nabh-shco-standards", "SHCO standards guide"),
                ("shco-accreditation-software", "SHCO accreditation software"),
                ("nabh-accreditation-software", "HCO accreditation software"),
            ],
            cta_h="Track the programme you actually chose",
            cta_p="AccredReady includes dedicated HCO and SHCO modes so OE tracking matches your nabh.co pathway.",
        )
    )
    return out


def even_more() -> list[dict]:
    out = []
    out.append(
        page(
            path="public/learn/nabh-how-to-apply.html",
            title="How to apply for NABH accreditation online | AccredReady",
            meta="How to apply for NABH: select programme, implement standards, self-assess, submit documents and fees, undergo onsite assessment. Steps from nabh.co FAQs and programme pages.",
            keywords="how to apply for NABH accreditation, NABH online application, NABH portal apply, NABH assessment process steps",
            canonical="learn/nabh-how-to-apply",
            og_title="How to apply for NABH accreditation online",
            h1_plain="How to apply for NABH accreditation — official process steps",
            eyebrow="NABH Guide · Application",
            h1="How to apply for NABH accreditation — official process steps",
            sub="The application sequence NABH publishes — before you pay fees or book consultants.",
            faqs=[
                (
                    "What is the NABH accreditation process?",
                    "Per nabh.co FAQs – Hospitals: select the appropriate programme; study and implement the relevant standards; conduct a self-assessment; submit documents and fees; undergo an onsite assessment by NABH-empanelled assessors; then close non-conformities before accreditation is granted.",
                ),
                (
                    "Where do I apply online?",
                    "Programme pages on nabh.co provide Apply Online / Renew actions. Applications are submitted through NABH’s online registration/application flow described on the relevant programme page (for example SHCO and Entry Level pages).",
                ),
                (
                    "How long must standards be implemented before applying?",
                    "Entry Level: hospital must have NABH Standards for a minimum of 3 months and be functional at least six months prior to application. SHCO Full: implement SHCO standards for at least 3 months; minimum 6 months operational data. Always re-read the live programme page.",
                ),
                (
                    "What if we do not fully meet standards at assessment?",
                    "NABH FAQs state that if a facility falls short, it receives a non-conformity report with a reasonable timeframe to address them. Accreditation follows successful closure as per NABH process.",
                ),
                (
                    "Are public hospitals eligible to apply?",
                    "Yes. NABH FAQs state programmes are open to public sector hospitals, teaching institutions, armed forces facilities, and railway hospitals if they meet eligibility criteria.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH’s published process is: select the programme → implement the standards → self-assess → submit documents and fees → undergo onsite assessment → close non-conformities → receive accreditation/certification.</strong> Skipping implementation and jumping to the portal is the most expensive way to fail.</p>
      <h2>Process steps (nabh.co FAQs – Hospitals)</h2>
      <ol class="my-6 space-y-4 text-[0.95rem] text-slate list-decimal pl-5">
        <li><strong class="text-ink">Select the appropriate programme</strong> — HCO, SHCO, Entry Level, ECO, dental, AYUSH, etc.</li>
        <li><strong class="text-ink">Study and implement the relevant standards</strong> — not download-only.</li>
        <li><strong class="text-ink">Conduct a self-assessment</strong> against the applicable objective elements.</li>
        <li><strong class="text-ink">Submit documents and fees</strong> through the online application flow.</li>
        <li><strong class="text-ink">Onsite assessment</strong> by NABH-empanelled assessors.</li>
        <li><strong class="text-ink">Close non-conformities</strong> within the timeframe NABH provides, then grant decision.</li>
      </ol>
      <h2>Programme-page extras you must not miss</h2>
      <p><strong>Entry Level (2nd Edition):</strong> functional ≥6 months; standards ≥3 months; occupancy thresholds by assessment/renewal cycle; allopathic services only; exclusions for AYUSH mix, standalone dental/physio/diagnostics, multi-location separate licences, etc. Source: ELC programme page.</p>
      <p><strong>SHCO Full:</strong> download 3rd Edition standards, purchase guidebook as directed, implement 3 months, submit online application with documents and application fee, then assessment scheduling. Source: SHCO programme page.</p>
      <h2>Frequently asked questions</h2>
      <h3>What is the NABH accreditation process?</h3>
      <p>Select programme → implement standards → self-assess → submit documents/fees → onsite assessment → close NCs → grant. Source: nabh.co FAQs.</p>
      <h3>Where do I apply online?</h3>
      <p>Use Apply Online / Renew on the relevant programme page at nabh.co.</p>
      <h3>How long must standards be implemented before applying?</h3>
      <p>ELC and SHCO pages both require standards implementation for at least 3 months (plus functional/operational minimums). Confirm live text before you apply.</p>
      <h3>What if we do not fully meet standards at assessment?</h3>
      <p>NABH provides a non-conformity report and timeframe to address gaps.</p>
      <h3>Are public hospitals eligible?</h3>
      <p>Yes, if they meet the programme eligibility criteria (nabh.co FAQs).</p>
""",
            sources='nabh.co FAQs – Hospitals; ELC and SHCO programme pages under nabh.co/programmes/.',
            related=[
                ("learn/nabh-elc-eligibility", "NABH ELC eligibility & occupancy"),
                ("learn/nabh-gap-analysis", "NABH gap analysis guide"),
                ("nabh-accreditation-cost", "NABH fees"),
                ("nabh-accreditation-software", "NABH accreditation software"),
            ],
            cta_h="Self-assess before you submit",
            cta_p="Run gap analysis and evidence tracking on AccredReady while you prepare the nabh.co application.",
        )
    )
    out.append(
        page(
            path="public/learn/nabh-elc-eligibility.html",
            title="NABH Entry Level eligibility and occupancy rules | AccredReady",
            meta="Official NABH Entry Level Certification (2nd Edition) eligibility: 6 months functional, 3 months standards, occupancy 20%/25%/30% by cycle, inclusions and exclusions from nabh.co.",
            keywords="NABH Entry Level eligibility, NABH ELC occupancy requirements, NABH ELC exclusion criteria, Entry Level Certification 2nd Edition",
            canonical="learn/nabh-elc-eligibility",
            og_title="NABH Entry Level eligibility and occupancy rules",
            h1_plain="NABH Entry Level eligibility — occupancy and exclusions",
            eyebrow="NABH Guide · ELC eligibility",
            h1="NABH Entry Level eligibility — occupancy and exclusions",
            sub="The inclusion, exclusion, and occupancy rules published on nabh.co for Entry-Level Certification Programme (2nd Edition).",
            faqs=[
                (
                    "How long must a hospital be functional before ELC application?",
                    "Hospitals must be functional since at least six months prior to the application, and must have NABH Standards for a minimum of 3 months. Source: nabh.co Entry-Level Certification Programme (2nd Edition).",
                ),
                (
                    "What occupancy is required for ELC final assessment?",
                    "Minimum 20% occupancy during the last 3 months for final assessment. 1st renewal: minimum 25% during the preceding 1 year. 2nd renewal: minimum 30% during the preceding 1 year.",
                ),
                (
                    "Which facilities are excluded from ELC?",
                    "Published exclusions include: below-required occupancy; AYUSH services with or without allopathy; standalone dental, physiotherapy, diagnostics & pathology, psychology, diabetology and de-addiction centres; hospitals established within six months of application; multi-location hospitals with separate statutory licences not in the same premises; multi-building setups with separate statutory licences and distinct legal identities.",
                ),
                (
                    "Does ELC cover both small and large hospitals?",
                    "Yes. It is a unified framework for SHCOs (up to 50 beds) and hospitals (51 beds and above), with assessment matrices that differ by bed strength and cycle.",
                ),
                (
                    "Are day-care beds counted for occupancy?",
                    "For standalone day-care centres (e.g., ophthalmology, chemotherapy, IVF, dialysis), day-care beds are considered census beds for occupancy. Specialty scope rules also reference minimum case volumes over six months — see the live ELC page.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>To apply for NABH Entry-Level Certification Programme (2nd Edition), the organisation must be functional for at least six months, must have implemented NABH Standards for a minimum of three months, and must meet the published occupancy thresholds for the assessment cycle — 20% (final), 25% (1st renewal), or 30% (2nd renewal).</strong> Allopathic services only; several facility types are explicitly excluded. Source: nabh.co ELC programme page.</p>
      <h2>Inclusion criteria (published)</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Hospitals providing Allopathic services only</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Functional ≥6 months prior to application</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>NABH Standards in place ≥3 months</span></li>
      </ul>
      <h2>Occupancy thresholds</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Assessment point</th><th>Minimum occupancy</th></tr></thead><tbody>
      <tr><td><strong>Final Assessment</strong></td><td>20% during the last 3 months</td></tr>
      <tr><td><strong>1st Renewal</strong></td><td>25% during the preceding 1 year</td></tr>
      <tr><td><strong>2nd Renewal</strong></td><td>30% during the preceding 1 year</td></tr>
      </tbody></table></div>
      <h2>Exclusions (published)</h2>
      <p>Hospitals below required occupancy; AYUSH (with or without allopathy); standalone dental/physio/diagnostics &amp; pathology/psychology/diabetology/de-addiction; hospitals younger than six months at application; multi-location separate licences outside same premises; multiple buildings with separate statutory licences and distinct legal identities. Certification uses an all-or-none principle for services offered — every service being offered should be applied for certification.</p>
      <h2>Frequently asked questions</h2>
      <h3>How long must a hospital be functional before ELC application?</h3>
      <p>At least <strong>six months</strong>, with standards for at least <strong>three months</strong>.</p>
      <h3>What occupancy is required for ELC final assessment?</h3>
      <p><strong>20%</strong> during the last 3 months (then 25% / 30% at later renewals).</p>
      <h3>Which facilities are excluded from ELC?</h3>
      <p>See the exclusion list above — including AYUSH mix and several standalone centre types.</p>
      <h3>Does ELC cover both small and large hospitals?</h3>
      <p>Yes — unified for ≤50 and 51+ beds with different matrices.</p>
      <h3>Are day-care beds counted for occupancy?</h3>
      <p>For listed standalone day-care centre types, day-care beds are census beds for occupancy; confirm specialty case rules on the live page.</p>
""",
            sources='<a href="https://nabh.co/programmes/entry-level-hospitals-certification-programme/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">Entry-Level Certification Programme (2nd Edition)</a> eligibility, occupancy, and exclusion sections.',
            related=[
                ("learn/nabh-entry-level-vs-full", "Entry Level vs Full"),
                ("nabh-entry-level-certification", "ELC complete guide"),
                ("nabh-entry-level-incentive", "PMJAY ELC incentive"),
                ("nabh-elc-software", "ELC software"),
            ],
            cta_h="Check eligibility before you spend on preparation",
            cta_p="If you qualify, track ELC standards and evidence on AccredReady while you build the 3-month implementation window.",
        )
    )
    out.append(
        page(
            path="public/learn/nabh-e-mitra.html",
            title="NABH E-Mitra — free templates and checklists explained | AccredReady",
            meta="NABH E-Mitra is a free official platform with sample policies, SOPs, formats and checklists. What it is, who can use it, and why templates alone do not guarantee accreditation.",
            keywords="NABH E-Mitra, NABH free templates, NABH sample SOP, nabh.co e-mitra, NABH documentation support",
            canonical="learn/nabh-e-mitra",
            og_title="NABH E-Mitra — free templates and checklists explained",
            h1_plain="NABH E-Mitra — what the free official toolkit actually is",
            eyebrow="NABH Guide · E-Mitra",
            h1="NABH E-Mitra — what the free official toolkit actually is",
            sub="Official free resources from NABH — and the limits NABH itself publishes.",
            faqs=[
                (
                    "What is NABH E-Mitra?",
                    "NABH E-Mitra is an online platform launched by NABH to help HCOs and SHCOs understand and implement NABH standards using structured guidance and downloadable resources. Access: https://nabh.co/e-mitra/",
                ),
                (
                    "Is E-Mitra free?",
                    "Yes. NABH FAQs state there is no cost associated with accessing E-Mitra documents and resources, and login credentials are not required.",
                ),
                (
                    "Does downloading E-Mitra policies guarantee accreditation?",
                    "No. NABH explicitly states that downloading and implementing E-Mitra documents does not guarantee accreditation or certification. Assessment is based on actual implementation and compliance.",
                ),
                (
                    "Are E-Mitra documents universal for every hospital?",
                    "No. NABH states resources must be reviewed and customised to the organisation’s scope, size, location, and complexity.",
                ),
                (
                    "Which programmes can use E-Mitra?",
                    "NABH FAQs state E-Mitra resources are broadly applicable across programmes including HCO, SHCO, eye care, dental clinics, CHCs, blood banks, and others, as foundational support to refine per programme.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH E-Mitra is NABH’s free official resource platform — sample policies, SOPs, formats, registers, and checklists — available at nabh.co/e-mitra without login.</strong> NABH also states clearly: templates alone do not grant accreditation; every document must be customised and actually implemented.</p>
      <h2>What you can get</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Sample policies and procedures for clinical and administrative processes</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Department-specific guidelines, checklists, and formats</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Forms, formats, and registers for compliance</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Guidance supporting assessment preparation</span></li>
      </ul>
      <h2>Hard limits (from NABH FAQs)</h2>
      <div class="my-5 rounded-xl border border-signal/30 bg-signal/5 px-6 py-4"><p class="!mb-0 !text-ink">E-Mitra is a framework to adapt — not a paste-and-pass kit. Assessment judges practice and compliance, not how many templates you downloaded.</p></div>
      <h2>How quality teams should use it</h2>
      <p>Use E-Mitra to draft faster, then rewrite in your hospital’s language, assign owners, train staff, and prove implementation through audits and indicators. Pair templates with a living gap tracker — otherwise documents outrun practice.</p>
      <h2>Frequently asked questions</h2>
      <h3>What is NABH E-Mitra?</h3>
      <p>NABH’s free online implementation-support platform at <a href="https://nabh.co/e-mitra/" target="_blank" rel="noopener noreferrer" class="rounded text-verify underline-offset-2 hover:underline">nabh.co/e-mitra</a>.</p>
      <h3>Is E-Mitra free?</h3>
      <p>Yes — no access cost; no login required per NABH FAQs.</p>
      <h3>Does downloading policies guarantee accreditation?</h3>
      <p>No. NABH says implementation and assessment compliance decide the outcome.</p>
      <h3>Are documents universal?</h3>
      <p>No — customise to your scope and operations.</p>
      <h3>Which programmes can use it?</h3>
      <p>Broadly across NABH programmes as foundational support; refine per programme.</p>
""",
            sources='nabh.co FAQs – Hospitals (E-Mitra questions); ELC/SHCO programme pages referencing E-Mitra; <a href="https://nabh.co/e-mitra/" class="rounded text-verify underline-offset-2 hover:underline" target="_blank" rel="noopener noreferrer">nabh.co/e-mitra</a>.',
            related=[
                ("learn/nabh-how-to-apply", "How to apply for NABH"),
                ("learn/nabh-gap-analysis", "Gap analysis guide"),
                ("nabh-software-vs-excel", "Software vs Excel"),
                ("nabh-accreditation-software", "NABH accreditation software"),
            ],
            cta_h="Templates start the file — tracking finishes the job",
            cta_p="Use E-Mitra for drafts; use AccredReady to track OE status, CAPAs, and evidence so implementation stays visible.",
        )
    )
    out.append(
        page(
            path="public/learn/nabh-focus-assessment.html",
            title="NABH focus assessment — what it is and fees | AccredReady",
            meta="NABH Focus Assessment is a targeted assessment under a published NABH policy. Fee commonly listed at ₹15,000 (+18% GST) on current HCO/SHCO/ELC fee tables — verify on nabh.co.",
            keywords="NABH focus assessment, NABH focus visit, NABH focus assessment fee, NABH targeted assessment",
            canonical="learn/nabh-focus-assessment",
            og_title="NABH focus assessment — what it is and fees",
            h1_plain="NABH focus assessment — targeted verification explained",
            eyebrow="NABH Guide · Focus assessment",
            h1="NABH focus assessment — targeted verification explained",
            sub="Not the same as surveillance or renewal. Here is what programme fee tables and policy lists on nabh.co tell you.",
            faqs=[
                (
                    "What is a NABH Focus Assessment?",
                    "NABH publishes a Policy & Procedure for Focus Assessment (listed on HCO/SHCO/ELC programme document sections). It is a targeted assessment mechanism distinct from routine surveillance and full renewal assessment. Read the current policy PDF from nabh.co for triggers and process.",
                ),
                (
                    "How much is the Focus Assessment fee?",
                    "Current nabh.co fee tables for SHCO Full, Entry Level Certification, and related programme tables list Focus assessment at ₹15,000, with 18% GST applicable extra. Confirm the live table for your programme before payment.",
                ),
                (
                    "Is focus assessment the same as surveillance?",
                    "No. Surveillance is the scheduled mid-cycle check in the accreditation cycle (for HCO Full: 21–24 months). Focus assessment is governed by a separate focus-assessment policy.",
                ),
                (
                    "Is focus assessment the same as surprise assessment?",
                    "No. NABH also publishes a Policy for Surprise Assessment. Keep focus and surprise policies separate when you brief leadership.",
                ),
                (
                    "Where do I find the official focus assessment policy?",
                    "On nabh.co programme pages under Documents — look for “NABH Policy & Procedure for Focus Assessment”. Always use the latest issue number published there.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>A NABH Focus Assessment is a targeted assessment under NABH’s published Focus Assessment policy — not a nickname for surveillance and not a full renewal assessment.</strong> Current SHCO and Entry Level fee tables on nabh.co list Focus assessment at <strong>₹15,000</strong> with <strong>18% GST</strong> extra. Always open the latest policy PDF and fee table for your programme before budgeting.</p>
      <h2>Where this sits among assessment types</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th>Type</th><th>Role</th></tr></thead><tbody>
      <tr><td><strong>Final / renewal assessment</strong></td><td>Awards or renews accreditation/certification</td></tr>
      <tr><td><strong>Surveillance</strong></td><td>Mid-cycle continued compliance (HCO Full: 21–24 months)</td></tr>
      <tr><td><strong>Focus assessment</strong></td><td>Targeted assessment per Focus Assessment policy</td></tr>
      <tr><td><strong>Surprise assessment</strong></td><td>Separate surprise-assessment policy</td></tr>
      </tbody></table></div>
      <h2>Fees currently listed on nabh.co tables</h2>
      <p>SHCO Accreditation Programme fee table (revised w.e.f. 01.04.2024) and Entry Level Certification fee table both list Focus assessment at ₹15,000 (GST extra). HCO fee communications on AccredReady’s cost page also reflect ₹15,000 focus assessment for hospital programmes — re-verify on the live HCO fee notification you are paying against.</p>
      <h2>Frequently asked questions</h2>
      <h3>What is a NABH Focus Assessment?</h3>
      <p>A targeted assessment under the Focus Assessment policy published on nabh.co programme document lists.</p>
      <h3>How much is the fee?</h3>
      <p>₹15,000 + 18% GST on current SHCO/ELC tables — confirm live.</p>
      <h3>Is it the same as surveillance?</h3>
      <p>No.</p>
      <h3>Is it the same as surprise assessment?</h3>
      <p>No — different policy.</p>
      <h3>Where is the official policy?</h3>
      <p>Programme Documents → “NABH Policy &amp; Procedure for Focus Assessment” on nabh.co.</p>
""",
            sources='nabh.co SHCO and ELC fee tables (Focus assessment ₹15,000 + GST); programme Documents lists for Focus Assessment and Surprise Assessment policies; HCO 6th Edition surveillance timing for contrast.',
            related=[
                ("learn/nabh-surveillance-assessment", "Surveillance assessment"),
                ("nabh-accreditation-cost", "Full fee structure"),
                ("learn/nabh-assessment-preparation", "Assessment preparation"),
                ("nabh-accreditation-software", "NABH software"),
            ],
            cta_h="Keep corrective actions closed before any targeted visit",
            cta_p="AccredReady tracks CAPAs and evidence so focus-assessment preparation is based on live compliance status.",
        )
    )
    out.append(
        page(
            path="public/learn/nabh-poi-quality-connect.html",
            title="NABH POI training and Quality Connect masterclasses | AccredReady",
            meta="NABH Programme on Implementation (POI) workshops and free monthly Quality Connect masterclasses — what nabh.co says they cover and where to find schedules.",
            keywords="NABH POI, Programme on Implementation, NABH Quality Connect, NABH training masterclass, NABH assessor training hospital",
            canonical="learn/nabh-poi-quality-connect",
            og_title="NABH POI training and Quality Connect masterclasses",
            h1_plain="NABH POI and Quality Connect — official training pathways",
            eyebrow="NABH Guide · Training",
            h1="NABH POI and Quality Connect — official training pathways",
            sub="What NABH itself offers for implementation training — separate from paid consultancy.",
            faqs=[
                (
                    "What is NABH Programme on Implementation (POI)?",
                    "POI is NABH’s targeted training for implementing standards, delivered by senior assessors. SHCO and Entry Level programme pages both reference POI as implementation support. Check nabh.co Education/Training listings for schedules.",
                ),
                (
                    "What is NABH Quality Connect?",
                    "NABH Quality Connect refers to free monthly masterclasses on topics such as KPI, medication management, document control, and infection prevention (as described on the ELC programme support section). Confirm current topics on nabh.co.",
                ),
                (
                    "Does attending POI guarantee accreditation?",
                    "No. Training supports implementation. Accreditation/certification still depends on assessment against applicable standards and closure of non-conformities.",
                ),
                (
                    "Where are upcoming trainings listed?",
                    "SHCO programme support text points to https://nabh.co/EducationTraining.aspx for upcoming training programmes. Verify the live URL/navigation on nabh.co if links move.",
                ),
                (
                    "Can NABH train our hospital staff?",
                    "Yes. NABH FAQs state NABH conducts regular training sessions directly and through certified trainers/assessors covering implementation strategies and programme-specific standards.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH offers Programme on Implementation (POI) workshops by senior assessors and free monthly “NABH Quality Connect” masterclasses on practical quality topics.</strong> These are official education supports described on nabh.co programme pages and FAQs — they help teams implement standards; they do not replace assessment.</p>
      <h2>POI — Programme on Implementation</h2>
      <p>SHCO and Entry Level pages describe POI as targeted training to simplify standard implementation. Use it when your team needs a shared reading of the standards before documentation sprawl begins.</p>
      <h2>Quality Connect — monthly masterclasses</h2>
      <p>ELC support text lists free monthly masterclasses under NABH Quality Connect on topics like KPI, medication management, document control, and infection prevention. SHCO support text similarly references monthly masterclasses on KPI monitoring, documentation, infection control, and clinical audits.</p>
      <h2>How to use training without confusing it for readiness</h2>
      <ul class="my-5 space-y-2.5 text-[0.95rem] text-slate">
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Send process owners, not only the quality manager.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Convert each session into assigned CAPAs or SOP edits within one week.</span></li>
        <li class="flex gap-3"><span class="text-verify mt-0.5" aria-hidden="true">→</span><span>Keep attendance records — useful for HRM/training evidence later.</span></li>
      </ul>
      <h2>Frequently asked questions</h2>
      <h3>What is NABH POI?</h3>
      <p>Programme on Implementation — NABH training by senior assessors to support standards implementation.</p>
      <h3>What is Quality Connect?</h3>
      <p>Free monthly masterclasses on practical quality topics, as described on nabh.co programme support sections.</p>
      <h3>Does POI guarantee accreditation?</h3>
      <p>No.</p>
      <h3>Where are schedules listed?</h3>
      <p>Check nabh.co Education/Training listings (SHCO page references EducationTraining.aspx).</p>
      <h3>Can NABH train our staff?</h3>
      <p>Yes — per nabh.co FAQs on training support.</p>
""",
            sources='ELC and SHCO programme Support sections on nabh.co; nabh.co FAQs – Hospitals (training / POI / masterclasses).',
            related=[
                ("learn/nabh-e-mitra", "NABH E-Mitra guide"),
                ("learn/nabh-quality-manager-first-90-days", "New quality manager — first 90 days"),
                ("learn/nabh-kpi-tracking", "NABH KPI tracking"),
                ("nabh-accreditation-software", "NABH software"),
            ],
            cta_h="Turn training into tracked actions",
            cta_p="After POI or Quality Connect, log gaps and CAPAs in AccredReady so learning becomes compliance evidence.",
        )
    )
    out.append(
        page(
            path="public/learn/nabh-empanelment-vs-accreditation.html",
            title="NABH accreditation vs PMJAY empanelment — difference | AccredReady",
            meta="NABH accreditation/certification is a quality programme from NABH; PMJAY empanelment is a scheme network status via State Health Agencies. How they differ and how they connect.",
            keywords="NABH vs PMJAY empanelment, NABH accreditation empanelment, Ayushman Bharat NABH requirement, SHA empanelment vs NABH",
            canonical="learn/nabh-empanelment-vs-accreditation",
            og_title="NABH accreditation vs PMJAY empanelment — difference",
            h1_plain="NABH accreditation vs PMJAY empanelment — do not mix them up",
            eyebrow="NABH Guide · Empanelment",
            h1="NABH accreditation vs PMJAY empanelment — do not mix them up",
            sub="One is a quality accreditation/certification. The other is scheme network status. Hospitals need clarity on both.",
            faqs=[
                (
                    "Is NABH accreditation the same as PMJAY empanelment?",
                    "No. NABH accreditation/certification is granted by NABH against NABH standards. PMJAY/state-scheme empanelment is managed through State Health Agencies under AB-PMJAY operational arrangements. You can be empanelled without NABH, or hold NABH without being empanelled.",
                ),
                (
                    "Does NABH help with empanelment and insurance?",
                    "NABH FAQs state NABH accreditation is increasingly accepted as a quality requirement for empanelment under government schemes, insurance providers, and corporate programmes. Entry Level pages also note certified hospitals are often preferred for empanelment. Prefer ≠ automatic empanelment.",
                ),
                (
                    "How does the PMJAY NABH incentive relate?",
                    "AB-PMJAY quality incentives commonly differentiate Entry Level NABH (about 10%) and Full NABH (about 15%) over base package rates in SHA schedules — but only after empanelment and SHA tier update. See AccredReady’s ELC incentive guides and confirm with your SHA.",
                ),
                (
                    "Which body do I apply to for each?",
                    "NABH programmes: apply via nabh.co programme flows. PMJAY/state scheme empanelment: apply via your State Health Agency / scheme portal processes.",
                ),
                (
                    "If my NABH certificate lapses, what happens to scheme rates?",
                    "If your SHA incentive tier depends on valid NABH status, a lapsed certificate can drop you to base rates until a valid certificate is re-submitted. Confirm with your SHA claims cell.",
                ),
            ],
            body="""
      <p class="!text-[1.05rem] !text-ink"><strong>NABH accreditation or Entry Level Certification is a quality determination by NABH. PMJAY (Ayushman Bharat) empanelment is network participation under the scheme via your State Health Agency.</strong> They interact — especially for quality-linked package incentives — but they are not the same application and not the same certificate.</p>
      <h2>Quick contrast</h2>
      <div class="my-6 overflow-x-auto rounded-xl border border-hairline shadow-sm"><table class="tbl"><thead><tr><th></th><th>NABH accreditation / ELC</th><th>PMJAY empanelment</th></tr></thead><tbody>
      <tr><td><strong>Authority</strong></td><td>NABH (QCI)</td><td>NHA / State Health Agency scheme operations</td></tr>
      <tr><td><strong>Question answered</strong></td><td>Do you meet NABH standards?</td><td>Are you in the scheme provider network?</td></tr>
      <tr><td><strong>Where to apply</strong></td><td>nabh.co programme application</td><td>SHA / scheme empanelment process</td></tr>
      <tr><td><strong>Incentive link</strong></td><td>Quality status used by many SHA schedules</td><td>Pays claims; may uplift rates if NABH tier active</td></tr>
      </tbody></table></div>
      <h2>What NABH itself says about empanelment value</h2>
      <p>NABH FAQs: accreditation is increasingly accepted as a quality requirement for empanelment under government healthcare schemes and insurers. ELC benefits text: certified hospitals are often preferred for empanelment. Neither statement says NABH automatically empanels you under PMJAY.</p>
      <h2>Frequently asked questions</h2>
      <h3>Is NABH the same as PMJAY empanelment?</h3>
      <p>No.</p>
      <h3>Does NABH help with empanelment?</h3>
      <p>It is often preferred / increasingly required as a quality signal — confirm your scheme rules.</p>
      <h3>How does the PMJAY NABH incentive relate?</h3>
      <p>SHA schedules commonly uplift package rates for Entry Level / Full NABH after tier update — only if you are empanelled.</p>
      <h3>Which body do I apply to?</h3>
      <p>NABH → nabh.co. Empanelment → SHA/scheme portal.</p>
      <h3>If NABH lapses, what happens to scheme rates?</h3>
      <p>Incentive tiers tied to valid NABH status can drop until re-validated with the SHA.</p>
""",
            sources='nabh.co FAQs – Hospitals (empanelment/insurance recognition); ELC programme benefits text on nabh.co; AB-PMJAY/SHA incentive practice as documented in state schedules (see AccredReady ELC incentive pages).',
            related=[
                ("nabh-entry-level-incentive", "National ELC PMJAY incentive"),
                ("nabh-elc-incentive-states", "State SHA incentive activation"),
                ("learn/nabh-entry-level-vs-full", "ELC vs Full"),
                ("nabh-elc-software", "ELC software"),
            ],
            cta_h="Keep NABH status valid if your claims depend on it",
            cta_p="Track ELC/Full compliance and renewal dates on AccredReady so SHA incentive tiers are not lost to an expired certificate.",
        )
    )
    return out


def main() -> None:
    all_pages = PAGES + more_pages() + even_more()
    if len(all_pages) != 10:
        raise SystemExit(f"expected 10 pages, got {len(all_pages)}")
    for p in all_pages:
        out = ROOT / p["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p), encoding="utf-8")
        print("wrote", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
