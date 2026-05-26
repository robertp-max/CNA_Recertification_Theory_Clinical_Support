Exact Next Prompt for Moodle Conversion
Act as a Senior Moodle Content Conversion Engineer and LMS Build Artifact Specialist.

Repository: C:\AI\Git\CNA_Recertification_Theory_Clinical_Support

Source files are located at:
/content/theory/modules/ â€” Files 24â€“29 (Markdown)
/content/csv/31_QUIZ_BANK_MASTER_COMPLETE.csv â€” Quiz bank (50 questions)
/content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md â€” Exam pool reference
/content/clinical-support/ â€” Files 32â€“33 (Markdown)

Task:
Convert the theory module Markdown files (24â€“29) into Moodle Lesson-compatible
HTML page sections. Convert the quiz CSV into Moodle XML import format.
Create a Moodle course backup manifest (IMSCC or MBZ-compatible structure).
Build the optional clinical support section as non-gating Moodle Pages and
a Feedback activity.

Constraints:
- Do NOT enable certificates.
- Do NOT remove SME flags â€” preserve as HTML comments.
- Do NOT generate video.
- Do NOT authorize TTS production.
- Do NOT add clinical hours to any activity.
- Do NOT make optional clinical support a prerequisite for anything.
- Keep Module 7 final exam at 30 minutes, 25 questions, 80% pass, 2 attempts.
- Keep all compliance disclaimers exactly as written.
- Output all files to /content/moodle-build/ folder.
- Create /content/moodle-build/BUILD_MANIFEST.md listing every output file.
