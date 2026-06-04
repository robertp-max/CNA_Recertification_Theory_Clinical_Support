# Prototype 1 Acceptance Criteria

## Pass Criteria

Prototype Build 1 passes only if all of the following are true:

| Criterion | Pass Standard | Evidence |
|---|---|---|
| Required gates block certificate when incomplete | Each required gate negative test prevents certificate release | QA tracker results and screenshots |
| Optional clinical support does not block certificate | Learner can skip optional clinical support, optional confidence check, and optional documentation support and still access staging certificate after required gates pass | QA tracker results and settings screenshots |
| Active-time control works or fallback exists | Plugin reliably gates final exam/certificate, or manual admin review/custom compliance hold is configured and documented | Active-time test results; admin review record |
| Audit dry run produces evidence | Required profile, acknowledgement, completion, interaction, active-time/review, exam, affidavit, certificate status, admin hold, and optional status evidence can be exported or captured | Audit dry-run packet |
| Role permissions prevent unauthorized override | Unauthorized roles cannot clear holds, override gates, or issue certificates | Role test log |
| Learner-facing labels distinguish required vs optional | Required online CE certificate requirements and optional clinical support are visually separated | Course screenshots |
| No PHI collection is present | Prototype does not request PHI; optional documentation stub warns against PHI | Privacy screenshot/review note |
| Certificate remains disabled or staging-only until approval metadata exists | Certificate is unavailable without approval metadata/staging override and clearly not production | Certificate settings screenshot |
| Direct URL access is blocked | Direct final exam and certificate URLs do not bypass restrictions | Direct URL test screenshots |
| Optional clinical support is not clinical-hour credit | Labels do not present optional support as required renewal clinical hours or clinical-hour credit | Copy review and screenshots |

## Fail Conditions

Prototype Build 1 fails if any required incomplete gate allows certificate release, if optional clinical support is required for certificate release, if active-time evidence cannot be gated or reviewed through a documented fallback, if audit evidence cannot be exported or captured, or if PHI collection is introduced.

## Decision Outcomes

| Outcome | Meaning | Next Action |
|---|---|---|
| Pass | Gate proof of concept is staging-ready for next build increment | Plan Prototype Build 2 or expand staging content shell |
| Pass with fallback | Active-time or certificate tooling needs manual/admin fallback but gate logic is defensible | Document fallback owner, workflow, and audit evidence |
| Fail | One or more required controls do not work | Fix configuration or revise tooling before any pilot |
