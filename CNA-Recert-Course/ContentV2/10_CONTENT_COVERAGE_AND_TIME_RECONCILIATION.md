# 10_CONTENT_COVERAGE_AND_TIME_RECONCILIATION — Coverage & Time

> Generated from `CNA-Recert-Course/ContentV2/data/courseContentV2.json` by `tools/rebuild_contentv2_from_json.py` on 2026-06-02T01:57:05+00:00. Do not hand-edit.


Instructional minutes are inherited from the ContentV1 syllabus (`02_THEORY_SYLLABUS_TABLE.md`). The 720-minute total is **not** recomputed from narration length or card count. Narration, reading/review, interaction, and assessment minutes are tracked **separately** and never replace the authoritative allocation. Optional Clinical Support and all assessment time are excluded.

## Required theory instructional allocation (counts toward 720)

| Module | Counts→720 | Instructional min | Lesson-allocated min | Depth gap | Narration min | Reading min | Interaction min | Assessment min (excl.) | Status |
|---|:--:|---:|---:|---:|---:|---:|---:|---:|---|
| M00 | yes | 30 | 30 | 0 | 8.8 | 9.9 | 17.5 | 5 | authored |
| M01 | yes | 90 | 90 | 0 | 19.5 | 21.7 | 21.0 | 15 | under-depth |
| M02 | yes | 120 | 105 | 15 | 22.0 | 23.8 | 17.5 | 15 | under-depth |
| M03 | yes | 120 | 105 | 15 | 16.9 | 18.3 | 17.5 | 15 | source-repair |
| M04 | yes | 120 | 105 | 15 | 23.1 | 25.0 | 17.5 | 15 | under-depth |
| M05 | yes | 120 | 105 | 15 | 22.7 | 24.6 | 17.5 | 15 | under-depth |
| M06 | yes | 90 | 80 | 10 | 18.8 | 20.6 | 17.5 | 15 | under-depth |
| M07 | yes | 30 | 17 | 13 | 25.0 | 25.7 | 17.5 | 0 | authored-partial |

**Required theory instructional minutes counted toward 720:** 720  (target 720)

**Module assessment minutes (tracked separately, excluded):** 95

**Course final assessment minutes (tracked separately, excluded):** 25

**Optional Clinical Support counts toward 720:** False

**Total authored narrated lesson minutes (descriptive only):** 156.82

**Open content-depth gap (allocation minus authored lesson minutes):** 83 min

> Narration minutes are descriptive and are far below the instructional allocation by design; they are NOT the full lesson time and must not be used to reduce the 720 model. Content-depth gaps above are reported, not padded; expand only from ContentV1 source. SME/source-repair flags are preserved.

## Time-model rules (enforced by the rebuild pipeline)

- Instructional minutes inherit from the ContentV1 syllabus allocation; the 720 total is not recomputed from narration or card count.
- Narration, reading/review, interaction/challenge/remediation, and assessment minutes are tracked separately.
- Module assessments and the final exam are excluded from the 720 instructional total.
- Optional Clinical Support never counts toward the 720 required theory minutes.
- Content-depth gaps are reported, not padded; SME/source-repair flags are preserved.
- No clinical-hour credit is claimed; production certificate remains disabled; no PHI.

## Pipeline counts

- **modules_count**: 8
- **lessons_count**: 41
- **cards_count**: 260
- **narration_clip_count**: 260
- **required_theory_instructional_minutes_total**: 720
- **module_assessment_minutes_excluded**: 95
- **course_final_assessment_minutes_excluded**: 25
- **content_depth_gap_minutes**: 83
- **total_narration_minutes**: 156.82
- **clips_over_75_seconds**: 0
- **unique_app_location_count**: 367
- **source_repair_flag_count**: 11
- **sme_review_flag_count**: 108
- **compliance_flag_count**: 260
