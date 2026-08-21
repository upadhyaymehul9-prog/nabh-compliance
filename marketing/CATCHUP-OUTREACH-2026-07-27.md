# Catch-up outreach — send today (2026-07-27)

All Batch 1 and Batch 2 touches are **14+ days overdue**. Nothing has been sent yet —
every contact is still on **T1 (prospects)** or **P1 (consultants)**. Send today, then
update `stage` and `last_touch_date` in the CSVs after each send.

**Rule:** Personalise before sending. Never paste verbatim. Verify LinkedIn profiles first.

---

## Consultants — send P1 today (6 contacts)

| ID | Who | Channel | Contact |
|----|-----|---------|---------|
| C001 | Poonam Changani | LinkedIn | [linkedin.com/in/poonam-changani-107a63bb](https://linkedin.com/in/poonam-changani-107a63bb) |
| C002 | Prajakta Tirthakar | **Email or LinkedIn** | **prajakta.tirthakar@gmail.com** · [LinkedIn](https://linkedin.com/in/prajakta-pethe-tirthakar-883338145) |
| C003 | Vinay G Kutty | LinkedIn | [linkedin.com/in/vinay-g-kutty-5455bb1b](https://linkedin.com/in/vinay-g-kutty-5455bb1b) |
| C004 | Rohit / Ichelon | **WhatsApp or email** | **+91 81302 26224** · **rohit@ichelonconsulting.com** |
| C005 | Neeraj Joshi | LinkedIn | [linkedin.com/in/neeraj-joshi-30810297](https://in.linkedin.com/in/neeraj-joshi-30810297) |
| C006 | Surbhi Mandloi Verma | LinkedIn | [linkedin.com/in/surbhi-mandloi-verma-95a692154](https://linkedin.com/in/surbhi-mandloi-verma-95a692154) |

**Fastest win:** Email C002 (Prajakta) — public email, no LinkedIn connect wait.

Drafts: `marketing/WEEK1-OUTREACH.md` (Batch 1 = C001–C003, Batch 2 = C004–C006).

After sending, update `consultants.csv`:
- `stage` → `contacted`
- `last_touch` → `P1`
- `last_touch_date` → `2026-07-27`
- `next_action` → `P2 follow-up`
- `next_action_date` → `2026-07-30`

---

## Prospects — send T1 today (10 contacts)

| ID | Who | City | LinkedIn |
|----|-----|------|----------|
| P001 | Shivani Kulkarni | Pune | [profile](https://www.linkedin.com/in/shivani-kulkarni-720401179) |
| P002 | Ram Prasad Golli | Hyderabad | [profile](https://in.linkedin.com/in/ram-prasad-golli-mha-723934122) |
| P003 | Ranjitha B N | Bengaluru | [profile](https://in.linkedin.com/in/ranjitha-b-n-2a134378) |
| P004 | Dr Vidushi | Jammu / multi-site | [profile](https://www.linkedin.com/in/dr-vidushi-a1a830212) |
| P005 | Bhushan Chavan | Maharashtra | [profile](https://linkedin.com/in/bhushan-chavan-653844194) — verify role first |
| P006 | Pranaam Hospital | Hyderabad | [hiring post](https://www.linkedin.com/posts/pranaam-hospital_hiring-qualityhead-hospitalquality-activity-7476959423962222592-SWg5) |
| P007 | Deepika Massey | Delhi NCR | [profile](https://linkedin.com/in/deepika-massey-664952324) — lowest priority |
| P008 | Pradeepa M | Thoothukudi | [profile](https://in.linkedin.com/in/pradeepa-m-89435943) |
| P009 | Subham Hospital | Cooch Behar | [hiring post](https://www.linkedin.com/posts/ashish-bhattacharya-36572026a_hiring-qualitymanager-nabh-activity-7466807857863098368-KbYh) |
| P010 | Bodyline Hospital | Ahmedabad | Email: **contact@bodylinehospitals.com** · Phone: **8153020945** |

Drafts: `marketing/WEEK1-OUTREACH.md` (P001–P007) plus new hooks below for P008–P010.

After sending, update `prospects.csv`:
- `stage` → `connected` (if LinkedIn request sent) or keep `identified` until accepted
- `last_touch` → `T1`
- `last_touch_date` → `2026-07-27`
- `next_action` → `T2 useful pointer`
- `next_action_date` → `2026-07-30`

---

## New prospect drafts (P008–P010)

**P008 · Pradeepa M — Head Quality & Performance Improvement, A.V.M. Hospital, Thoothukudi**
> Hi Pradeepa, your work leading NABH readiness at AVM Hospital — and the team
> recognition on Hospital Day — shows the kind of quality leadership that makes
> accreditation stick. I head medical services at HMP Foundation and build NABH
> readiness systems. Good to connect with someone doing this hands-on.

**P009 · Subham Hospital, Cooch Behar — hiring Quality Manager (facility-level)**
> Hi [Name from post / hospital page], saw Subham Hospital is hiring a Quality
> Manager with full NABH accreditation experience. Between now and that hire,
> readiness tracking still has to move — stalled scoring shows up at assessment.
> AccredReady keeps gap and KPI data current so your new QM starts from a
> baseline, not a cold spreadsheet. Happy to show you in 10 minutes.

**P010 · Bodyline Hospital, Ahmedabad — hiring NABH Quality Coordinator**
> Hi, saw Bodyline Hospital is recruiting a NABH Quality Coordinator in Ahmedabad.
> If the accreditation push is active before the seat is filled, a shared
> readiness tracker keeps documentation and gap closure moving across departments.
> I built AccredReady for exactly that — happy to connect.

---

## T2 follow-ups (send Wed 30 Jul if no reply)

One useful fact only — no product pitch:

- **HCO prospects:** "CORE gaps closed first — assessors weight them heavily even when documentation looks complete elsewhere."
- **ELC prospects:** "HOPE Entry Level fee rebates run until 30 September 2026 on several bed slabs — worth checking your application timing on nabh.co."
- **Consultants:** Share `/nabh-consultant-vs-software` — "clients lose track between visits; this is how we frame software vs advice."

---

## After you send — log it

Open these files and update one row per contact:

```
.claude/skills/accredready-marketing-agent/data/prospects.csv
.claude/skills/accredready-marketing-agent/data/consultants.csv
```

No outreach logged = pipeline stays at zero. That is the bottleneck for customer 1.
