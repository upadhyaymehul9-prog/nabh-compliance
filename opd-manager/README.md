# OPD Manager

End-to-end outpatient flow for clinics: **reception → doctor → lab / radiology → doctor → pharmacy → exit**, with real-time TV boards.

Built with **Next.js** + **Firebase** (Firestore realtime, Spark free tier).

## Consoles

| URL | Role |
|-----|------|
| `/reception` | Register patient, assign consultant & room |
| `/doctor` | Pick doctor profile → call / consult / route patient |
| `/lab` | Lab queue, ETA, report ready |
| `/radiology` | Radiology queue, ETA, report ready |
| `/pharmacy` | Dispense & mark exit |
| `/manager` | Live floor dashboard |
| `/display/opd` | TV — calling & waiting |
| `/display/lab` | TV — lab ETAs |
| `/display/radiology` | TV — radiology ETAs |

## Firebase setup (free tier)

### 1. Create project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. **Add project** → name e.g. `opd-manager`
3. Stay on **Spark (free)** plan

### 2. Enable Firestore

1. **Build → Firestore Database → Create database**
2. Start in **test mode** for local dev (lock down before go-live)
3. Region: pick closest to your clinic (e.g. `asia-south1` Mumbai)

### 3. Web app config

1. **Project settings → Your apps → Web** (`</>`)
2. Copy config into `.env.local`:

```bash
cp .env.local.example .env.local
```

### 4. Seed demo data

In Firestore, add:

**Collection `clinics`**, document ID `demo-clinic`:

```json
{
  "name": "Demo Clinic",
  "tokenPrefix": "OPD"
}
```

**Collection `doctors`** (one doc per doctor), example document:

```json
{
  "clinicId": "demo-clinic",
  "name": "Sharma",
  "roomNumber": "3",
  "specialty": "General Medicine",
  "active": true
}
```

Set `NEXT_PUBLIC_CLINIC_ID=demo-clinic` in `.env.local` (default).

### 5. Deploy rules & indexes (when ready)

```bash
npm install -g firebase-tools
firebase login
firebase use --add
firebase deploy --only firestore:rules,firestore:indexes
```

> Firestore will also prompt you to create composite indexes from error links in the browser console on first run.

## Local development

```bash
cd opd-manager
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Firebase free tier notes (Spark)

| Resource | Free allowance | OPD Manager |
|----------|----------------|-------------|
| Firestore reads | 50K/day | Fine for one clinic MVP |
| Firestore writes | 20K/day | ~10–30 writes per patient visit |
| Auth | Free | Add before production |
| Hosting | Free | Static export or Vercel |

For a busy clinic in production, monitor usage in Firebase Console and upgrade to **Blaze (pay-as-you-go)** only if you exceed free quotas — many single-clinic deployments stay on free tier early on.

## Patient flow

```
Reception → waiting_doctor → doctor_calling → in_consultation
    → at_lab / at_radiology / at_pharmacy
    → lab_processing (+ ETA on TV) → report_ready → back_to_doctor
    → pharmacy_processing → completed → exited
```

## Security (before go-live)

Current rules are open for MVP dev. Before real patient data:

1. Enable **Firebase Authentication** (email/password or Google)
2. Store staff `role` in custom claims or `staff/{uid}` collection
3. Restrict `visits` writes by role (reception create, doctor/lab/pharmacy update)
4. TV displays: read-only public collection or signed tokens

## Deploy frontend

**Option A — Vercel (recommended for Next.js)**

Connect repo, set env vars, deploy.

**Option B — Firebase Hosting**

```bash
npm run build
# configure static export if using Firebase Hosting only
```

## Next steps

- [ ] Firebase Auth + role-based consoles
- [ ] Hindi labels on TV screens
- [ ] Token-only display (privacy)
- [ ] SMS when report ready (Firebase Extensions or Twilio)
- [ ] Multi-clinic / branches
