# 08 — Certificate Gate, Active-Time, and Affidavit Reconciliation

## Purpose

Reconcile the certificate gate chain, active-time validation, and affidavit/e-signature controls.
Confirm which are documented, which are prototype-only, and which are blocked.

## Inputs Reviewed

- `CNA-Recert-Course\Content\13_AFFIDAVIT_TEXT.md`.
- `CNA-Recert-Course\Content\14_CERTIFICATE_FIELD_MAPPING.csv`.
- `CNA-Recert-Course\Content\00_EXECUTIVE_SUMMARY.md` (gate logic, layered evidence).
- `CNA-Recert-Course\PHASE_0_COMPLIANCE_FOUNDATION.md`.
- App: `standalone-course-mvp\src\pages\CertificateGatePage.tsx`,
  `FinalAssessmentSplashPage.tsx`.

## Gate Chain Evidence Table

| Gate control | Control doc | App/export evidence | Status |
|---|---|---|---|
| Identity (legal name + CNA cert #) | gate prerequisite | M00 / CertificateGatePage | Needs Compliance Review |
| Module completion | completion tracking | ContentV2 / app | In Progress |
| Interaction checks | interaction matrix | app | In Progress |
| Active-time validation | active-time plugin / manual review | not validated | Needs Compliance Review |
| Final exam pass | exam pool + pass mark | `examPool.ts` | Needs SME Review |
| Affidavit / e-sign | `13_AFFIDAVIT_TEXT.md` | CertificateGatePage | Needs Legal/CDPH Review |
| Admin clearance | manual admin review | app | In Progress |
| Certificate wording | `14_CERTIFICATE_FIELD_MAPPING.csv` | DRAFT only | Needs Legal/CDPH Review |
| Provider / NAC metadata | `PHASE_0_COMPLIANCE_FOUNDATION.md` | not present | Needs Legal/CDPH Review |

## Non-Negotiable Compliance Statements

- No CDPH approval is claimed. **Certificate production is BLOCKED.**
- E-signature acceptance is **not** confirmed (wet-sign fallback may be required).
- Active-time validation is **not** confirmed. **Moodle logs alone are insufficient** as active
  participation evidence; a manual admin review hold is the fallback.
- Identity excludes DOB unless a controlling approval is uploaded and cited.

## Gaps Found

- Certificate wording is DRAFT only; no approved language exists.
- No provider/NAC IDs, approved hours, or approved course title.
- Active-time plugin not validated in staging.

## Owner / Action Needed

- Program Owner / Legal / CDPH: approve provider/course, certificate wording, affidavit, e-sign.
- QA/Technical: validate active-time or implement manual review hold.

## Blocker Status

**P0 BLOCKER.** Live certificate issuance must remain disabled.

## Next Verification Step

Confirm `CertificateGatePage.tsx` does not enable live issuance and shows draft-only certificate
language; record in the audit packet.
