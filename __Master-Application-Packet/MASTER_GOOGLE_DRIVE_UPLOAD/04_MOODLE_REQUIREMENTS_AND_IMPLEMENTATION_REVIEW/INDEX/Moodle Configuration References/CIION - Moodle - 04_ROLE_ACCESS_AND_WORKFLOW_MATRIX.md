# 04 - Role, Access, and Workflow Matrix

Status: Draft / Pending Approval. See machine-readable companion `import_assets/ROLE_MATRIX_IMPORT_REFERENCE.csv`.

## Roles and access

### Site Administrator
- Allowed: full site configuration, plugin management, role definition, backups, all reports/grades/exports, certificate enablement (post-approval only).
- Prohibited: shared logins; enabling certificates before approval; undocumented grade overrides.
- Reports: all. Grades: all. Certificates: control (post-approval). User data: all. Export: all. Risk controls: dedicated account, MFA where supported, actions logged.

### Moodle Manager
- Allowed: manage categories/courses, enroll users, run/export reports, document grade overrides, provision reviewer accounts.
- Prohibited: enabling certificates before approval; undocumented overrides.
- Reports: all assigned. Grades: view/edit with documentation. Certificates: control (post-approval). User data: yes. Export: yes.

### Course Creator
- Allowed: create and build course shells and content within assigned category.
- Prohibited: editing learner grades; releasing certificates; site config.
- Reports: limited. Grades: no (default). Certificates: no. User data: no. Export: no.

### Editing Teacher
- Allowed: build/edit course content, manage activities, grade, view course reports.
- Prohibited: site config; enabling certificates before approval.
- Reports: course-level. Grades: yes. Certificates: no. User data: limited. Export: limited.

### Non-editing Teacher
- Allowed: view content, grade assigned activities, view course reports.
- Prohibited: editing content; site config.
- Reports: course-level. Grades: view (grade if assigned). Certificates: no. User data: limited. Export: limited.

### External Survey Reviewer (custom read-only role)
- Allowed: read-only view of assigned categories/courses, content, completion and grade reports, exported evidence bundle.
- Prohibited: any edit, grade change, enrollment change, content change, certificate action, access to unrelated courses or full PII.
- Reports: read-only. Grades: read-only. Certificates: none. User data: de-identified/limited for review. Export: provided as a prepared bundle. Risk controls: temporary credential, forced password reset, time-limited, deactivated after survey window.

### Read-only Compliance Reviewer (internal)
- Allowed: internal read-only review of assigned courses, reports, and evidence.
- Prohibited: edits, grade changes, certificate actions.
- Reports/Grades: read-only. Certificates: none. Export: read-only. Risk controls: documented access, scoped.

### Onboarding Policy and Workflow Viewer (custom limited role)
- Allowed: read-only access to approved onboarding policy pages, workflow pages, and related acknowledgments in the dedicated policy/workflow resource category.
- Prohibited: course enrollment, course content access outside onboarding policy/workflow resources, learner records, grades, reports, certificates, exports, reviewer access, editing, enrollment changes, role assignment, and site configuration.
- Reports/Grades: none. Certificates: none. User data: none. Export: none. Risk controls: scoped category/resource access only, documented assignment, removed when onboarding is complete.

### Learner (Student)
- Allowed: access enrolled course content, attempt quizzes, submit activities, view own grades/progress, download own certificate (post-approval only).
- Prohibited: viewing answer keys, others' data, or any admin function.
- Reports/Grades: own only. Certificates: own (post-approval). User data: own. Export: own certificate (post-approval).

### Support/Admin Staff (custom scoped role)
- Allowed: account support, password resets, enrollment assistance, basic troubleshooting (scoped).
- Prohibited: content edits, grade edits, certificate control.
- Reports: limited. Grades: limited. Certificates: none. User data: limited to support tasks. Export: limited. Risk controls: actions logged.

## Reviewer workflow (generated)

1. Account creation: Manager creates a reviewer account (manual auth) with a non-personal username pattern (e.g., `surveyreviewer1`).
2. Temporary password: set a strong temporary password communicated through a secure channel (no real reviewer password stored in this package - final human verification required).
3. Forced password reset: enable "force password change on next login."
4. Read-only role: assign the custom External Survey Reviewer role at the assigned category/course context only.
5. Enrollment/category access: scope to the specific lane/courses under review; no access to unrelated content.
6. Expiration/deactivation: set an enrollment/account end date aligned to the survey window; suspend or delete after.
7. Export logs: capture access logs for the reviewer account as part of evidence.
8. No edit rights: verify the role has no editing, grading, enrollment, or certificate capabilities (test RV-01 in `08_SURVEY_READINESS_QA_TEST_PLAN.md`).

See `15_REVIEWER_ACCESS_AND_SURVEY_WORKFLOW.md` for the full survey-day workflow and `generated_missing_elements/GENERATED_SURVEY_REVIEWER_SCRIPT.md` for the reviewer-facing script.
