# Build Readiness Status

## Ready Now

| Item | Status | Notes |
|---|---|---|
| Repository source planning packet | Ready | Phase 0, Phase 2, Phase 3, Phase 4, unified blueprint, and Phase 5 build specs are present. |
| Certificate gate requirements | Ready for staging POC | Gate list is defined; staging must prove behavior before pilot. |
| Required vs optional separation rules | Ready for staging POC | Optional clinical support must not gate the online CE certificate. |
| QA negative-test baseline | Ready for Prototype 1 | Source negative tests exist and are scoped in the prototype tracker. |
| Audit packet source list | Ready for dry run | Prototype 1 will prove exportability, not production retention. |
| Learner disclaimer draft copy | Ready for review use | Use as draft staging labels only; not final legal/CDPH-approved copy. |

## Blocked by CDPH/Legal

| Item | Blocker |
|---|---|
| Production certificate issuance | CDPH provider/course approval, NAC#/provider metadata, approved certificate wording, and approved retention language are not documented in this repo. |
| Final affidavit/e-signature method | Legal/CDPH approval is required before production use. |
| Clinical support counting for renewal clinical hours | Written CDPH approval is required; default is not allowed. |
| Simulation or LTI simulation counting for clinical hours | Written CDPH approval is required; default is not allowed. |
| Final learner-facing compliance wording | Legal/CDPH review is required before release. |

## Blocked by Plugin Validation

| Item | Blocker |
|---|---|
| Active-time automatic gate | Candidate plugin must pass idle, minimized, tab switch, multi-tab, mobile, export, and direct-access tests. |
| Certificate plugin production use | Certificate plugin must prove field population, lock behavior, issue logs, PDF output, and role restrictions. |
| Dashboard/progress plugin use | Required CE progress must remain separate from optional clinical support progress. |
| Scheduler or upload tools for optional support | Must pass privacy, mobile, and export validation before use. |

## Blocked by Staging QA

| Item | Blocker |
|---|---|
| Certificate gate pilot readiness | All required gate negative tests must block certificate release when incomplete. |
| Optional clinical separation | Optional clinical support skipped must not block the online CE certificate. |
| Direct URL bypass prevention | Final exam and certificate direct-access attempts must be denied before prerequisites are met. |
| Audit dry run | Required evidence must be exportable or captured through a documented admin-review fallback. |
| Role permissions | Unauthorized users must not override certificate gates or active-time/admin holds. |

## Excluded from MVP

| Exclusion | Reason |
|---|---|
| Full course build | Prototype 1 only proves the gate path with one sample theory module. |
| Final lesson content | Out of scope for Prototype 1. |
| Production Moodle configuration | Requires validation and approvals first. |
| Custom Moodle plugins | Out of scope unless later approved and specified. |
| New video production | Excluded from MVP. |
| PHI collection | Not allowed. |
| Clinical hours on online CE certificate | Not allowed by default and not part of the online CE certificate. |
| Optional clinical support as certificate gate | Prohibited unless written CDPH-approved instructions exist. |

## First Prototype Success Criteria

Prototype Build 1 succeeds only if Moodle staging proves that:

- Required identity, online cap acknowledgement, theory activity, interaction, active-time control or fallback, final exam/test, final affidavit, certificate fields, and admin hold controls block certificate release when incomplete.
- Optional clinical support, optional confidence checks, and optional documentation support do not block certificate release.
- Active-time control either gates reliably or a documented manual admin review/custom compliance hold exists.
- Audit dry-run exports can produce required evidence.
- Role permissions prevent unauthorized override.
- Learner-facing labels clearly separate required online CE certificate requirements from optional clinical support.
- No PHI collection is present.
- Certificate remains disabled or clearly staging-only until approval metadata exists.
