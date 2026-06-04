# Active-Time POC Test Plan

## Purpose

Prototype Build 1 must prove that the selected active-time control can support certificate gating or that a documented manual admin review/custom compliance hold can safely replace automatic gating.

Moodle logs alone are not enough.

## Fallback Rule

If the selected plugin cannot reliably gate certificate release, Prototype 1 must use manual admin review or a custom compliance hold before certificate release. The fallback must create an admin review record and appear in the audit dry run.

## Test Matrix

| Test ID | Test Case | Expected Result | Evidence to Capture | Pass/Fail |
|---|---|---|---|---|
| AT-P1-001 | Idle tab | Idle time is excluded or controlled according to documented settings | Plugin settings screenshot; before/after time report | TBD |
| AT-P1-002 | Minimized browser | Time does not continue accruing as active participation while inactive | Time report; test steps log | TBD |
| AT-P1-003 | Tab switch | Time pauses or does not accrue after inactivity threshold when learner switches tabs | Time report; browser steps log | TBD |
| AT-P1-004 | Multiple tabs | Time is not double-counted across multiple tabs in the same course | Time report; session evidence | TBD |
| AT-P1-005 | Logout/login | Time accumulates only across valid active sessions and persists after login | Session log; time report | TBD |
| AT-P1-006 | Mobile browser | Mobile browser path does not distort active-time evidence | Mobile screenshots; time report | TBD |
| AT-P1-007 | Direct final exam access | Final exam remains locked until active-time threshold or manual review is satisfied | Learner screenshot; Restrict Access settings | TBD |
| AT-P1-008 | Direct certificate access | Certificate remains locked until active-time threshold or manual review is satisfied | Learner screenshot; certificate settings | TBD |
| AT-P1-009 | Report export | Admin can export learner-level active-time evidence | CSV/PDF export; export settings screenshot | TBD |
| AT-P1-010 | Manual admin review fallback | Admin can review time evidence, clear or keep compliance hold, and create review record | Admin review record; hold status screenshot | TBD |

## Pass Standard

Active-time passes Prototype 1 only if either:

- The selected plugin reliably controls final exam and certificate availability, handles idle/minimized/tab/multiple-tab/mobile scenarios acceptably, and exports learner-level evidence.
- A manual admin review/custom compliance hold is configured, documented, role-restricted, and included in the audit dry run.

## Fail Conditions

- Time double-counts across tabs.
- Idle/minimized time is counted as active participation without defensible settings.
- Learners can bypass active-time controls through direct URLs.
- Admin cannot export or document learner-level active-time evidence.
- Manual fallback can be cleared by unauthorized roles.
