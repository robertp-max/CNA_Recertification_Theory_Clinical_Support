# Merge Notes For Coordinator

## Do Not Merge As Production-Ready Content

This scratch output is guidance only. Do not copy Module 1 into canonical V2 production content without preserving the Module 1 all-content SME/source-review flag.

## Specific Cautions

1. Preserve Module 1 critical gap status.
   - The source states there is no dedicated infection-control NATP Module 10-17 source.
   - Keep a visible SME/source-review banner on `modules.m1.overview` and retain per-card review metadata until cleared.

2. Keep Module 0 certificate language conservative.
   - Use "gate status," "completion evidence," or "eligibility status" language.
   - Do not enable certificate production.
   - Do not invent certificate wording, affidavit wording, NAC numbers, provider numbers, CDPH contacts, or approval metadata.

3. Keep Optional Clinical Support optional.
   - It may be linked from dashboard/navigation, but it must remain optional, non-credit, non-gating, not clinical-hour credit, and never a certificate gate.

4. Normalize encoding artifacts.
   - The reviewed source text contains mojibake in headings, arrows, check/cross symbols, and warning icons.
   - Convert to clean ASCII or valid Unicode according to canonical V2 style before publishing.

5. Keep app locations stable.
   - Recommended locations use `modules.m0.*`, `modules.m1.*`, `certificate.gate.status`, `dashboard.*`, `final.assessment.splash`, and `clinical.unit01.overview`.
   - If canonical naming differs, preserve the intent and avoid changing routing/build files as part of content merge.

6. Preserve unrelated global flags.
   - Module 5 skin integrity/pressure injury SME/source-review flag remains outside this assignment but must carry forward.
   - Final exam Q01, Q02, Q03, Q41 and Q21/Q38 flags where present must carry forward.

7. Accessibility merge requirements.
   - Chain-of-infection matching must have a text alternative.
   - PPE tables must be readable as text on mobile.
   - Correct/incorrect feedback cannot rely on color only.

8. Source coverage limitation.
   - Local shell reads were blocked, so source review used the GitHub fallback mirror.
   - Secondary sources named by the assigned files were not opened.
   - TTS package was referenced but not reviewed; do not treat this run as narration-ready.
