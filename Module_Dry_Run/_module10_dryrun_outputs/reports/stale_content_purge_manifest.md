# Stale Content Purge Manifest — Module10_Dry_Run

Created: 2026-06-04T00:41:55

Output path note: the user prompt wrote `Module10_Dry_Run_module10_dryrun_outputs`; this cleanup uses the existing approved output root `Module10_Dry_Run/_module10_dryrun_outputs`.

Future LMS workers must treat `Module10_Dry_Run/_module10_dryrun_outputs/backups/` as recovery only and must ignore it as source authority.

Planned recovery location: `Module10_Dry_Run/_module10_dryrun_outputs/backups/stale_content_purge_20260604_004155`

## Purge candidates

| Classification | Path | Exists | Reason |
|---|---|---:|---|
| purge | `_RUN_BACKUPS` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `.venv` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `CNA-Recert-Course` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `staging` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `standalone-mvp-sandbox` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `BUILD_READINESS_STATUS.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `CLAUDE_DAY_MODE_FIX_PROMPT.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `extract_package.ps1` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `GLOBAL_MASTER_PROMPT.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `NEXT_BUILD_STEP.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `REPOSITORY_STRUCTURE.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `SECURITY.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `WORKFLOW.md` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `standalone-course-mvp/dist` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `standalone-course-mvp/screenshots` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |
| purge | `standalone-course-mvp/test-results` | True | Stale copied course/repo/generated content not required for clean Module 10 app shell. |

## Preserve candidates

| Classification | Path | Exists | Reason |
|---|---|---:|---|
| preserve | `_module10_dryrun_outputs/reports/preflight_report.md` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/package.json` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/package-lock.json` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/index.html` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/src` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/public` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/api` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/node_modules` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/vite.config.ts` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/tsconfig.json` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/tailwind.config.cjs` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/postcss.config.cjs` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/vitest.config.ts` | True | Required active app shell, config, dependencies, or preflight report. |
| preserve | `standalone-course-mvp/playwright.v2-screenshot.config.ts` | True | Required active app shell, config, dependencies, or preflight report. |

## Unsure candidates preserved

| Classification | Path | Exists | Reason |
|---|---|---:|---|
| unsure | `.cursor` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `.gitignore` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `README.md` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/README.md` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/PROTOTYPE_GENERATION_PROMPT.md` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/src/data` | True | Contains stale generated course data, but is imported by the current app shell; preserved for now and flagged as a post-cleanup blocker for source-first replacement. |
| unsure | `standalone-course-mvp/src/pages/LessonPlayerPage.tsx` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/v2-screenshot.html` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/vite.v2-screenshot.config.ts` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/tailwind.v2-screenshot.config.cjs` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |
| unsure | `standalone-course-mvp/tests` | True | Preserved to avoid breaking app shell/build or deleting potentially useful setup/lesson-player structure before source-first replacement. |

---

# Stale Content Purge Manifest — App Data Second Pass

Created: 2026-06-04T01:41:22

Recovery location: `Module10_Dry_Run/_module10_dryrun_outputs/backups/stale_content_purge_20260604_014122_app_data`

Future LMS workers must treat `Module10_Dry_Run/_module10_dryrun_outputs/backups/` as recovery only and must ignore it as source authority.

## Candidate Classification

| Classification | Path | Exists | Reason |
|---|---|---:|---|
| purge | `standalone-course-mvp/src/data/contentV2.generated.ts` | True | Clearly stale generated/multi-module course data or authored overrides from old course package; moved to recovery and replaced only with source-extraction-pending shell where imports require it. |
| purge | `standalone-course-mvp/src/data/modules` | True | Clearly stale generated/multi-module course data or authored overrides from old course package; moved to recovery and replaced only with source-extraction-pending shell where imports require it. |
| purge | `standalone-course-mvp/src/data/phase1Module1.ts` | True | Clearly stale generated/multi-module course data or authored overrides from old course package; moved to recovery and replaced only with source-extraction-pending shell where imports require it. |
| purge | `standalone-course-mvp/src/data/remediationOverrides.ts` | True | Clearly stale generated/multi-module course data or authored overrides from old course package; moved to recovery and replaced only with source-extraction-pending shell where imports require it. |
| preserve | `standalone-course-mvp/src/data/contentV2Adapter.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/courseModules.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/examPool.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/lessonModel.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/mediaManifest.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/narrationManifest.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/remediation.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/v2ModuleQuiz.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| preserve | `standalone-course-mvp/src/data/__tests__/exam.test.ts` | True | Adapter/model/generic shell file needed to keep app buildable; not source authority. |
| unsure | `standalone-course-mvp/src/pages` | True | Preserved to avoid breaking app shell or deleting non-data UI infrastructure before authorized source-first implementation. |
| unsure | `standalone-course-mvp/src/components` | True | Preserved to avoid breaking app shell or deleting non-data UI infrastructure before authorized source-first implementation. |
| unsure | `standalone-course-mvp/src/lib` | True | Preserved to avoid breaking app shell or deleting non-data UI infrastructure before authorized source-first implementation. |
| unsure | `standalone-course-mvp/src/nia` | True | Preserved to avoid breaking app shell or deleting non-data UI infrastructure before authorized source-first implementation. |
| unsure | `standalone-course-mvp/public/brand` | True | Preserved to avoid breaking app shell or deleting non-data UI infrastructure before authorized source-first implementation. |
