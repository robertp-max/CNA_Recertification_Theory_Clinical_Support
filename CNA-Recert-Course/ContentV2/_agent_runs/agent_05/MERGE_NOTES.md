# Merge Notes

## Coordinator Cautions

- Do not merge the keyed final exam markdown or CSV into learner-facing ContentV2 pages or frontend static data. Split learner prompts from admin-only answer/rationale data.
- Preserve all required SME/source-review flags: Module 1 infection control, Module 5 skin integrity/pressure injury, Q01, Q02, Q03, Q41, Q21, and Q38.
- Keep certificate generation disabled. Merge only a certificate gate/status pattern until approved certificate wording, provider metadata, contact information, and certificate ID rules are available.
- Treat affidavit text as draft legal/compliance material. Do not deploy "under penalty of perjury" wording without legal approval.
- Keep Optional Clinical Support fully separate from required course progress, final exam access, affidavit access, and certificate status.
- Do not collect or store optional clinical confidence check responses as CE evidence.

## Source Inconsistencies To Resolve

- Module 7 timing conflicts: metadata says 30 minutes total, but lesson-level estimates total much more when 7.1, 7.2, 7.3, exam, 7.4, and 7.5 are counted.
- Certificate/Next Steps page is described as both a certificate gate and a page shown after all gates pass. Avoid circular gating; make it a status/next-steps page, not a prerequisite for releasing itself.
- Clinical Support Unit 4 says "20-item" confidence check list, but reviewed sources contain 21 checks. Either update the label to 21 or intentionally remove/merge one check.
- Source text appears to contain UTF-8 BOM and mojibake sequences in some punctuation. Normalize encoding when creating canonical ContentV2 copy.

## Assessment Build Notes

- Use server-side randomization and scoring for the final exam.
- Consider category-balanced random draws so a 25-question attempt does not under-sample smaller modules, especially Module 1's flagged infection-control items.
- Keep final exam review settings conservative between attempts; avoid exposing correct answers/rationales before the second attempt.
- Ensure "closed-book during the attempt" language is presented as a learner instruction, not as a technical guarantee unless proctoring/lockdown exists.

## Clinical Support Merge Notes

- Label all clinical support routes with "Optional" and "Not required for certificate."
- Avoid terms prohibited by source guardrails: required clinical hours, clinical credit, clinical practicum, clinical competency validation.
- Emergency response, CPR/DNR, choking response, and abuse-reporting content should receive clinical/facility policy review before learner release.
- No file upload workflow should be created for documentation practice or preceptor signoff.
