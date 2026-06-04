# 09 — Optional Clinical Support Separation Reconciliation

## Purpose

Verify that Optional Clinical Support is separate, optional, non-credit, and non-gating — and that
the export's skipped skill videos do not change that posture.

## Inputs Reviewed

- `CNA-Recert-Course\Content\03_CLINICAL_SUPPORT_SYLLABUS_TABLE.md`.
- `CNA-Recert-Course\Content\clinical-support\32_CLINICAL_SUPPORT_FULL_CONTENT.md`.
- `CNA-Recert-Course\Content\clinical-support\confidence-checks\33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE.md`.
- App: `standalone-course-mvp\src\pages\ClinicalHubPage.tsx`.
- `manifest.json` skipped videos (35 CNA skill / Moodle tutorial videos).

## Preserved Facts

- Optional Clinical Support is **NOT** California clinical-hour credit.
- Optional Clinical Support is **NOT** a certificate gate (unless written approval is present and
  cited — none is).
- It may be documented as support / confidence / skills-refresh only.

## Evidence Table

| Separation control | Control doc | Evidence | Status |
|---|---|---|---|
| Separate course section | OPTIONAL_CLINICAL_HUB_STUB_SPEC (referenced) | `ClinicalHubPage.tsx` | Needs Compliance Review |
| Labeled non-credit | `03_CLINICAL_SUPPORT_SYLLABUS_TABLE.md` | app labeling | Needs Compliance Review |
| Confidence checks non-graded | `33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE.md` | app | In Progress |
| Skill videos = support only | `32_CLINICAL_SUPPORT_FULL_CONTENT.md` | 35 videos skipped in export | Skipped by Copy Config |
| Not a certificate prerequisite | REQUIRED_OPTIONAL_SEPARATION_CHECK (referenced) | gate logic | Needs Compliance Review |

## Export Note

The 35 skipped videos in `manifest.json` are CNA clinical-skill demonstrations and Moodle
tutorials. Their absence locally does **not** affect required-theory credit. They support the
Optional Clinical pathway only. Transferring them is an owner decision, not a theory blocker.

## Gaps Found

- App labeling/gating must be verified to confirm non-credit, non-gating presentation.
- Confidence-check non-graded status must be confirmed in the running app.

## Owner / Action Needed

- Compliance: confirm separation language and that clinical content is never credit-bearing.
- App Engineer/QA: verify the hub cannot gate the certificate (QA-02).

## Blocker Status

Not a production blocker for theory, but a **compliance verification** item to prevent learner
misperception of clinical credit.

## Next Verification Step

Run QA-02 (skip clinical, attempt certificate) and confirm the certificate path is unaffected.
