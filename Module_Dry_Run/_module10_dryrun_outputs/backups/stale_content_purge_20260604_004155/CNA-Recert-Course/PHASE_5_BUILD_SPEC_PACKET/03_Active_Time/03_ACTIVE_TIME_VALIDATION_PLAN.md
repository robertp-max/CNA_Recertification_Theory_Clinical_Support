# Active-Time Validation Plan

**Purpose:** Prove in staging that the selected active-time tool can support CDPH-style active participation evidence and certificate gating.  
**Candidates:** Timestat, Dedication, or any other time plugin/custom hold. All are unvalidated until these tests pass.  
**Hard rule:** Moodle logs alone are not enough.

---

## Validation Principles

1. Validate active-time behavior before certificate-enabled pilot.
2. Capture screenshots/exports for every pass/fail result.
3. Test browser, mobile browser, and Moodle app if the app is used.
4. Confirm idle handling, direct access prevention, exportability, and gate integration.
5. Do not use a plugin in production without a rollback plan.

## Fallback Rule

If active-time data cannot reliably gate certificate release automatically, MVP must require manual admin review of active-time reports before certificate release or a custom compliance hold. The manual review must create an admin review record and must be included in the audit packet.

## Test Matrix

| Test Case | Expected Result | Tool / Plugin | Evidence to Capture | Pass/Fail | Notes |
|---|---|---|---|---|---|
| AT-001 Idle tab for 10 minutes | Idle time is excluded or paused according to documented settings | Candidate time plugin | Before/after time report, settings screenshot | TBD | Define idle threshold before test. |
| AT-002 Browser minimized | Time does not continue accruing as active participation if learner is inactive | Candidate time plugin | Time report, screen recording if possible | TBD | Critical for active participation claim. |
| AT-003 Learner switches tabs | Time pauses or does not accrue after inactivity threshold | Candidate time plugin | Time report, browser steps log | TBD | If plugin cannot detect tab focus, document limitation. |
| AT-004 Multiple tabs open in same course | Time is not double-counted | Candidate time plugin | Time report and session logs | TBD | Double-counting is launch blocker. |
| AT-005 Page refresh | Time session remains accurate; no artificial inflation | Candidate time plugin | Time report before/after refresh | TBD | Test repeated refresh attempts. |
| AT-006 Logout/login | Time accumulates across valid sessions only | Candidate time plugin | Session log and time report | TBD | Verify previous time preserved. |
| AT-007 Mobile browser | Active-time behavior works on iOS/Android browser | Candidate time plugin | Mobile test notes and export | TBD | Required if learners use phones. |
| AT-008 Moodle app if used | App behavior is documented; offline/sync time is not misrepresented | Candidate plugin + Moodle app | App sync logs, time report | TBD | If unreliable, app cannot be used for certificate time evidence. |
| AT-009 Low connectivity | Time does not inflate or lose records unpredictably | Candidate plugin | Network condition notes and report | TBD | Use throttled connection if possible. |
| AT-010 Direct access attempt to exam | Exam remains locked until active-time threshold met | Restrict access + time hold | Learner screenshot and setting screenshot | TBD | Launch blocker if fail. |
| AT-011 Direct access attempt to certificate | Certificate remains locked until active-time threshold met | Certificate gate + time hold | Learner screenshot and certificate settings | TBD | Launch blocker if fail. |
| AT-012 Time report export | Admin can export learner-level active-time report | Candidate plugin/report | CSV/PDF export | TBD | Must be audit packet compatible. |
| AT-013 Admin review workflow | Admin can review and document time status manually | Report + admin review form | Review record | TBD | Required fallback if auto-gate not reliable. |
| AT-014 Certificate-gate integration | Time status directly or indirectly controls certificate release | Plugin/custom/manual hold | Certificate gate test evidence | TBD | Must be tested with passing and failing learner. |
| AT-015 Reset/regrade/recompletion scenario | Time evidence is not accidentally erased or reused incorrectly | Candidate plugin + completion settings | Before/after reports | TBD | Important after course edits. |
| AT-016 Role permission test | Learner cannot alter time record; instructor cannot manually inflate time | Roles/capabilities | Role test log | TBD | Prevents audit integrity risk. |

## Staging Acceptance Criteria

| Requirement | Pass Standard |
|---|---|
| Idle handling | Inactive time is excluded or controlled according to documented settings. |
| Exportability | Admin can export learner-level active-time evidence. |
| Gate behavior | Learner cannot access final exam/certificate before required active-time threshold. |
| Mobile behavior | Mobile browser path is usable and does not distort time evidence. |
| App behavior | If Moodle app is used, limitations are documented and certificate time evidence remains defensible. |
| Admin fallback | Manual review workflow exists if auto-gating is unreliable. |
| Audit traceability | Time report, settings, and review notes can be included in audit packet. |
