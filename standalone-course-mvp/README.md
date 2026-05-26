# CareIndeed Standalone Course MVP

Browser-usable prototype for the CNA Recertification 12-hour online theory course, certificate-gate logic, optional clinical support hub, audit preview, and future Moodle migration mapping.

## Scope

- Standalone MVP only; not the final Moodle production course.
- Uses mock learner state only.
- Does not issue real certificates.
- Does not collect real learner data or PHI.
- Keeps optional clinical support separate from required online CE certificate progress.
- Includes a stakeholder splash/login experience for review only. This is not production authentication.

## Run

```powershell
npm install
npm run dev
```

For local visual demo login, either run with Vercel Functions configured through `vercel dev`, or set explicit local-only Vite fallback values in `.env.local`. Do not commit `.env.local`.

```powershell
Copy-Item .env.example .env.local
```

The local fallback credential is embedded only for stakeholder prototype review so Vite can run without Vercel Functions. The `VITE_*` fallback variables are exposed to the browser and are only a visual demo gate. Use Vercel Deployment Protection or Vercel Authentication for actual access control.

## Build

```powershell
npm run build
```

## Vercel Deployment

Use these Vercel settings:

- Root Directory: `standalone-course-mvp`
- Framework Preset: `Vite`
- Install Command: `npm install`
- Build Command: `npm run build`
- Output Directory: `dist`

`vercel.json` is included with the Vite build command and output directory.

Enable Vercel Deployment Protection or Vercel Authentication for stakeholder review links. The in-app splash/login is a stakeholder experience layer only and must never be treated as secure access control.

If using the Vercel Function demo login, add these environment variables in Vercel:

- `DEMO_LOGIN_ENABLED=true`
- `DEMO_LOGIN_EMAIL`
- `DEMO_LOGIN_PASSWORD`
- `DEMO_LOGIN_HINTS=false`

If env vars are omitted, the Vercel Function falls back to the stakeholder demo credential for review. If `DEMO_LOGIN_ENABLED=false`, demo login is disabled. Do not use the stakeholder demo credential as production authentication.

## Source Anchors

This MVP follows the repo blueprint and Phase 5 build packet, especially:

- `CNA-Recert-Course/FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md`
- `CNA-Recert-Course/PHASE_0_COMPLIANCE_FOUNDATION.md`
- `CNA-Recert-Course/PHASE_5_BUILD_SPEC_PACKET/`
- `CNA-Recert-Course/Content/theory/modules/04_THEORY_MODULE_00_ORIENTATION_FULL.md`
- `CNA-Recert-Course/Content/theory/modules/05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md`

## Brand Source

The visual identity is sourced from `CNA-Recert-Course/Branding_Kit`, including the CI Institute of Nursing logo, favicons, brand image, maroon/gold palette, and Poppins/Open Sans typography guidance.

## Production Warnings

Certificate issuance, certificate wording, NAC#/provider metadata, e-signature method, active-time validation, and CDPH course approval remain unresolved and must be handled in Moodle staging/production before any live use.

## Stakeholder Review Mode

The default fictional demo profile is James Bond, Stakeholder Admin / Demo Learner. The profile editor updates only prototype display state and certificate profile gates. Unlock Mode is for stakeholder navigation review only; it does not mark gates complete unless QA controls are explicitly used.
