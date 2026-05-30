# SME Flags

## Preserve Existing Flags

No SME/source-review flags should be removed during ContentV2 merge unless the coordinator has both:
- a confirmed approved source, and
- documented SME signoff against that source.

## Active SME/Source Review Flags

| Flag area | Affected items from reviewed controls | Required preservation |
|---|---|---|
| Module 1 infection control | Prior Module 1 content; Final Exam Q01, Q02, Q03, Q41; CSV rows Q01, Q02, Q03, Q41; TTS Module 1 segments; QA/Risk R01; Index File 30 and File 31 entries | Preserve SME/source-review flag. Do not treat Module 1 as fully source-confirmed until a confirmed CDPH-approved infection-control source is available. |
| Module 5 skin integrity / pressure injury | File 27 Lesson 5.3; Final Exam Q21 and Q38; CSV Q21 and Q38; Confidence Checks 06 and 07; TTS-5-003; QA/Risk R02; Index File 27, 30, 31, 33, 34 entries | Preserve SME/source-review flag. Do not finalize skin integrity content for production until confirmed source and SME review are complete. |
| Optional clinical support skin-integrity references | File 32 references per index/QA; File 33 Checks 06 and 07 | Preserve flag and optional/non-credit boundary. |
| TTS planning segments | Module 1 TTS segments and Module 5 skin integrity segment | Preserve SME flags and TTS authorization block. Scripts remain planning artifacts only. |

## Final Exam Flag Inventory

| Question ID | Source-review reason | Preserve flag? |
|---|---|---|
| Q01 | Module 1 infection-control source gap | Yes |
| Q02 | Module 1 infection-control source gap | Yes |
| Q03 | Module 1 infection-control source gap | Yes |
| Q21 | Skin integrity / pressure injury source gap | Yes |
| Q38 | Skin integrity / pressure injury source gap | Yes |
| Q41 | Module 1 infection-control source gap | Yes |

## Removal Conditions

Flags may be removed only after:
1. The source file is uploaded or otherwise available in the approved source set.
2. The source title and scope are recorded in the source-verification controls.
3. A qualified SME reviews the affected lesson, exam, CSV, optional clinical support, and TTS planning references.
4. The coordinator updates the merge manifest with who approved the change, when, and which source was used.

## New SME Issues Found

No new SME issue was found beyond the existing Module 1 infection-control and Module 5 skin integrity / pressure injury source gaps. The main new audit concern is coverage reconciliation, not content accuracy.
