# Plugin Validation Checklist

**Hard rule:** No plugin should be accepted into production without staging validation and rollback plan.

---

## Validation Requirements

For every tool/plugin:

1. Confirm selected Moodle version compatibility.
2. Confirm mobile browser behavior.
3. Confirm Moodle app behavior if the app is used.
4. Confirm Privacy API/data handling.
5. Confirm evidence export.
6. Confirm maintenance status and update cadence.
7. Confirm role/capability model.
8. Confirm backup/restore behavior.
9. Document rollback plan.

## Plugin Matrix

| Tool / Plugin | Purpose | MVP Need? | Version Compatibility | Mobile Behavior | Privacy API / Data Risk | Evidence Export | Maintenance Status | Decision | QA Test |
|---|---|---|---|---|---|---|---|---|---|
| Custom Certificate or equivalent | Generate locked certificate PDF and issue record | Required if Moodle core alternative not used | Validate against selected Moodle branch | Test PDF generation/download on phone | Stores certificate issue records and user data | Must export issue log and certificate PDF | Verify current maintainer/release | Candidate | Generate test certificate with all fields and code; verify release gates. |
| Active-time tracking plugin candidate | Track active participation minutes | Required | Validate selected candidate against Moodle branch | Test mobile browser and app if used | Stores learner time data | Must export learner-level report | Verify update history | Candidate until AT tests pass | Run all active-time validation cases. |
| H5P core activity | Interaction/feedback activities | MVP useful | Core behavior depends on Moodle version | Test chosen content types | Stores attempts/grades depending settings | Attempts/grades exportable | Core plus H5P library maintenance | Accept with content-type limits | Complete each H5P type on phone and verify tracking. |
| Scheduler if used | Optional support appointments | Optional MVP | Validate plugin version | Test booking/cancel on phone | Appointment records include personal data | Export bookings/outcomes | Verify maintainer/release | Use only if validated | Learner books/cancels slot; admin exports list. |
| Completion Progress/dashboard tool | Visual progress | Optional MVP | Validate plugin | Test separation of required vs optional | Progress may expose completion data | May not be audit source | Verify maintainer | Candidate only | Required CE progress excludes optional clinical support. |
| Reporting/custom SQL tool | Audit/export reports | Optional MVP; useful | Validate against Moodle DB/version | Admin-only; no learner UI | High data exposure risk | Must export CSV | Verify maintainer/security | Admin-only if used | Non-admin cannot access; export packet fields. |
| Checklist plugin | Optional support checklist | Not MVP required | Validate if considered | Test phone checkboxes | Learner checklist data | Export needed if used | Verify maintainer | Post-MVP candidate | Optional checklist does not gate certificate. |
| Attendance plugin | Optional live support attendance | Not MVP required | Validate if considered | Test mobile marking/view | Attendance data | Export needed if used | Verify maintainer | Post-MVP candidate | Attendance not counted as online CE certificate gate. |
| Moodle Mobile App behavior | Mobile access path | Optional; browser can be MVP | Confirm site/app services and SSL | Full path test | Offline/sync data risk | Reports may sync with limitations | Core app | Use only after limitations documented | Complete required path; validate time evidence limitations. |
| Theme plugin beyond Boost | Branding/mobile UX | Not MVP required | Validate branch compatibility | Test all learner gates | Theme may affect UX but not evidence | N/A | Verify maintainer | Avoid unless strong need | Required path usable on mobile. |
| External/LTI simulation | Practice scenarios | Not MVP | Requires separate vendor/version check | Test only if later used | Vendor data/privacy risk | Export uncertain | Vendor dependent | Exclude from MVP | Ensure not counted as clinical hours. |

## Acceptance Decision Values

Use one of:

- `Accept for MVP`.
- `Accept for staging only`.
- `Defer to post-MVP`.
- `Reject for MVP`.
- `Blocked pending legal/privacy review`.

## Rollback Plan Required Fields

| Field | Requirement |
|---|---|
| Plugin name/version | Exact installed version. |
| Reason installed | Business/compliance reason. |
| Data stored | User data, logs, files, grades, certificates. |
| Removal impact | What breaks if removed. |
| Replacement/fallback | Core Moodle or manual workflow. |
| Backup before install | Required. |
| Restore test | Required before production. |
| Owner | Named Moodle admin. |
