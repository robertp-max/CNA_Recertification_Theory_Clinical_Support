# Content Output - Coordinator Summary

This worker did not create canonical `ContentV2` course files. Output is limited to audit guidance for source inventory, precedence, coverage, and merge planning.

## Recommended Source Precedence

1. Treat `source-verification/SOURCE_TITLE_VERIFICATION_PASS.md` as authoritative for NATP Module 10-17 titles and for the active skin integrity source gap.
2. Treat `source-verification/TIME_ALLOCATION_CORRECTION_NOTICE.md` as authoritative for Module 7 timing and the 720-minute theory total.
3. Treat updated complete files as canonical over older duplicates:
   - File 30 over File 10 for final exam pool
   - File 31 over File 11 for quiz CSV
   - File 34 over File 16 for TTS planning only
   - File 35 over File 23 for package index
4. Treat QA files as controls and blockers, not learner-facing content.
5. Treat raw transcript files as secondary reconstruction inputs only.

## Required Flag Preservation

Preserve the following flags through any ContentV2 merge:
- Module 1 infection-control SME/source-review
- Module 5 skin integrity / pressure injury SME/source-review
- Final exam Q01, Q02, Q03, Q41
- Final exam and CSV Q21/Q38
- Confidence Checks 06 and 07 for skin integrity
- TTS Module 1 and Module 5 skin integrity segments as planning-only and review-required

## Coverage Risks To Resolve

- Content count mismatch: `GIT_TRACKING_VERIFICATION.md` reports 45 tracked Content files; `CONTENT_EXTRACTION_REPORT.md` reports 43 created files; current connector inventory surfaced 47 Content paths.
- QA filename mismatch: QA report references `GROK_NEXT_BUILD_ACTIONS.md`, but the current `qa` listing shows `NEXT_MOODLE_BUILD_PROMPT.md`.
- Raw source mismatch: extraction report references `Content/Raw/Claude/Batch2.md`, but only `Content/Raw/Claude/Batch1.md` surfaced in the assigned listing.
- No confirmed standalone NATP source exists in the reviewed controls for Module 1 infection control or Module 5 skin integrity.

## Coordinator Action

Before canonical merge, create or verify a `source_copy` manifest that records exact source paths, status class, source precedence, and active flags. Do not copy QA/control content into learner routes except where it is intentionally transformed into internal admin metadata.
