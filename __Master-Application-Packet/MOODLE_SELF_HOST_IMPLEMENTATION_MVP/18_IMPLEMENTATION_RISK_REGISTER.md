# 18 - Implementation Risk Register

Status: Draft / Pending Approval. Columns: risk | lane | severity | likelihood | mitigation | owner | evidence | status.

| risk | lane | severity | likelihood | mitigation | owner | evidence | status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Premature certificate release | All | Critical | Medium | Certificate disabled + approval-flag gate; only Admin/Manager can enable; test CT-01/CT-02 | Manager | gate config + test results | Open - controlled |
| Missing quiz mapping (a unit/course/module lacks items) | All | High | Low | Coverage audit verifies minimums per category; GIFT categories enforced | Manager | QUIZ_BANK_COVERAGE_AUDIT.md | Mitigated (455 items) |
| Stale BRN 4-hour reference appears | BRN | Critical | Low | Content authored to contact hours; validation scans for obsolete four-hour BRN wording | Compliance | validation scan | Mitigated |
| CNA clinical-hour overclaim | CNA | Critical | Low | "Online CE only / no clinical hours" wording; certificate excludes clinical hours; validation scan | Compliance | course text + scan | Mitigated |
| RCFE 40-hour concept confusion | RCFE | High | Medium | Build only filed 9-course/27h; 40-hour labeled future-only; validation scan | Manager | architecture docs + scan | Mitigated |
| PHI entry by learner | All | High | Medium | No-PHI warnings/prompts; quarantine/deletion process; review (test PH-02) | Compliance | warnings + review note | Open - controlled |
| Incomplete reviewer access (too much or too little) | All | High | Medium | Custom read-only role; scoped, temporary, expiring; test RV-01 | Manager | role config + test | Open - controlled |
| Missing active-time/seat-time evidence | All | High | Medium | Activity completion + time guidance; completion reports | Teacher | completion exports | Open - controlled |
| Untested restore (DR) | All | High | Medium | Scheduled backups + restore test (BR-01) | Technical Admin | restore log | Open - to test |
| Unapproved certificate wording | All | High | Low | Certificate wording gated to post-approval; must match approved terms | Manager | cert config | Open - controlled |
| Version/plugin incompatibility | All | Medium | Medium | Verify version/plugins before install (01 doc) | Technical Admin | compatibility check | Open - to verify |
| False approval claim in content | All | Critical | Low | Pending-approval posture; validation scan for "approved" implying issuance | Compliance | scan | Mitigated |
