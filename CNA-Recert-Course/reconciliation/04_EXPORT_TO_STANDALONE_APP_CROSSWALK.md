# 04 — Export → Standalone App Crosswalk

## Purpose

Reconcile ContentV2/source content against the `standalone-course-mvp` prototype app and identify
app-wiring verification gaps.

## Inputs Reviewed

- `standalone-course-mvp\src\data\` (`contentV2.generated.ts` 2.1 MB, `examPool.ts`,
  `courseModules.ts`, `lessonModel.ts`, `mediaManifest.ts`, `narrationManifest.ts`,
  `contentV2Adapter.ts`, `remediation*.ts`, `v2ModuleQuiz.ts`).
- App pages: `ModulesPage.tsx`, `LessonPlayerPage.tsx`, `CertificateGatePage.tsx`,
  `ClinicalHubPage.tsx`, `FinalAssessmentSplashPage.tsx`, `ReviewerLogin.tsx`.
- Components: `PhiWarningBlock.tsx`, `NarrationPlayer.tsx`, v2 shell components.

## Important Caveat

The working tree is **dirty** — many app files are modified/uncommitted (captured in
`_backups\pre_reconciliation_dirty_state_*.patch`). Claims below are **file-presence** evidence,
not runtime verification. App wiring must be verified in a running build.

## Evidence Table

| App capability | File evidence | Maps To | Status |
|---|---|---|---|
| Generated content bundle | `src\data\contentV2.generated.ts` | ContentV2 JSON | Needs App Verification |
| ContentV2 adapter | `src\data\contentV2Adapter.ts` | schema bind | Needs App Verification |
| Module listing/player | `ModulesPage.tsx`, `LessonPlayerPage.tsx` | M00–M07 | Needs App Verification |
| Exam pool | `src\data\examPool.ts` | 50-question pool | Needs App Verification |
| Final assessment splash | `FinalAssessmentSplashPage.tsx` | M07 | Needs App Verification |
| Certificate gate | `CertificateGatePage.tsx` | gate logic | Needs App Verification (prototype, not live issuance) |
| Optional clinical hub | `ClinicalHubPage.tsx` | Optional Clinical Support | Needs App Verification (non-gating) |
| PHI warning | `PhiWarningBlock.tsx` | PHI avoidance | Needs App Verification (must precede uploads/free-text) |
| Narration | `NarrationPlayer.tsx`, `narrationManifest.ts` | TTS (planning) | Needs App Verification |

## Gaps Found

- No runtime confirmation that the app reads `contentV2.generated.ts` for all 8 modules.
- Certificate gate is a prototype; it must not imply live certificate issuance.
- PHI warning presence on every upload/free-text surface is not verified.

## Owner / Action Needed

- App Engineer: build the app and confirm module/exam/gate/hub wiring.
- QA: run negative tests from `12_QA_NEGATIVE_TEST_AND_ACCEPTANCE_PLAN.md`.

## Blocker Status

App wiring is **Needs App Verification**. Certificate issuance remains BLOCKED regardless of app
state until compliance/legal blockers clear.

## Next Verification Step

Run the app build and confirm `contentV2.generated.ts` drives all module pages; capture screenshots
for the audit packet.
