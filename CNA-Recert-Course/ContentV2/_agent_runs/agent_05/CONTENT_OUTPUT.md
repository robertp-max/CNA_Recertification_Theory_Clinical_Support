# Content Output

## Final Assessment

Coordinator should treat the final exam as a protected assessment object, not learner-facing content. Source pool details:

- 50 total questions, Q01-Q50.
- 25 questions drawn per attempt.
- Passing score: 80%, meaning 20 of 25 correct.
- Maximum attempts: 2.
- Timer: 45 minutes.
- Question format: multiple choice; source mentions select-all-that-apply as possible, but reviewed Q01-Q50 are multiple choice only.

Suggested final assessment build:

- `final.assessment.splash`: learner-facing rules only; no answers/rationales.
- `final.assessment.quiz`: server-side random draw, server-side scoring, one question per page if retained from source.
- `final.assessment.result`: show pass/fail and next gate status. Do not expose item answer key unless a coordinator-approved review policy exists.
- `admin.examBank.protected`: admin-only source for Q01-Q50, answers, rationales, source references, SME flags.

Preserve final exam SME flags:

- Q01, Q02, Q03, Q41: Module 1 infection-control SME/source review.
- Q21, Q38: Module 5 skin integrity/pressure injury SME/source review.

## Certificate Gate And Affidavit

Certificate production must stay disabled. Use a status/gate view only until coordinator enables production with approved provider metadata and approved certificate wording.

Required gate logic to preserve:

- Prior modules complete.
- Prior module knowledge checks passed at 80%.
- Final exam passed at 80%.
- Active-time threshold met.
- Affidavit submitted with required attestations.
- Legal name captured if required by approved policy.

Do not fabricate provider numbers, CDPH contacts, certificate IDs, approval metadata, certificate wording, or affidavit legal language. The reviewed source includes placeholders and legal-sounding affidavit language; these need legal/compliance approval before learner deployment.

## Clinical Support

Clinical Support must remain:

- Optional.
- Non-credit.
- Non-gating.
- Not California renewal clinical-hour credit.
- Not clinical practicum or competency validation.
- Not displayed on the online CE certificate.

The reviewed clinical support set includes Units 1-7 and 21 confidence checks. Confidence checks are low-stakes self-ratings and should not affect course progress, certificate status, quiz grades, or CE evidence records.

Clinical non-gating checks for coordinator:

- No clinical unit should be a prerequisite for Module 7, final exam, affidavit, or certificate status.
- Optional view records may exist for UX analytics, but should not count as CE completion evidence.
- Do not store RN/preceptor signoff forms in Moodle as CE evidence.
- Do not ask learners to upload resident documentation, real resident examples, or identifiers.
- Keep fictional/de-identified scenario language prominent wherever free-text practice is offered.

## Answer-Key Protection Guidance

The markdown exam pool and CSV include correct answers and rationales. Protect them as assessment secrets:

- Keep keyed exam data server-side/admin-only.
- Do not bundle answers/rationales in frontend JSON, static ContentV2 learner pages, or downloadable learner resources.
- Limit admin capabilities for question bank, quiz reports, exports, and CSV import files.
- Randomize question order and answer order where the platform supports it.
- Do not show correct answers before final submission or between attempts unless explicitly approved.
- Log access to answer-key files where possible.
