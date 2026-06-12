# CI-ION Redesign QA Report

- Source folder verified: True
- Output folder verified: True
- Design HTML verified: True
- PDFs processed/adopted: 27
- PDFs pending: 0
- PDFs blocked: 0
- Standalone official form hash mismatches: 0
- Mixed appendix verifications passed: 6
- Mixed appendix verifications failed: 0
- Removed pending-context terms found: 0

Official government forms are preserved by direct PDF copy/append validation. No CI styling is applied by this checkpoint runner.

## Wording Cleanup QA - 2026-06-12
- Non-official banned wording findings: 0 (TJ, compiler, role-disclaimer wording, human review, human verification).
- Standalone official form SHA mismatches: 0.
- Mixed official appendix visual comparison failures: 0.
- RCFE LMS raw course-content PDF remains skipped and absent.

## Course Materials / Handoff QA - 2026-06-12
- Compiled course-material PDFs rebuilt from source Markdown using Studio HTML/CSS styling.
- Raw LMS course-content PDFs removed/skipped: 3.
- Raw Markdown syntax findings in compiled course packets: 0.
- Handoff/Moodle build-start agency-approval wording findings: 0.
- Official standalone form SHA mismatches: 0.
- Superseded item: RCFE source official forms contain DRAFT text. Final pass removed the separable DRAFT watermark from output copies only at user request; source PDFs remain unchanged.

## Final Fix Pass QA - 2026-06-12
- Active PDFs validated/opened: 24.
- Trim-edge overflow findings: 0.
- Official-form DRAFT text findings in output PDFs: 0.
- RCFE output-only exception: separable DRAFT watermark XObject removed from RCFE official-form output PDFs at user request. Source folder was not modified, pages were not rasterized, and form fields/text were not rewritten.
- CNA and BRN standalone official-form PDFs remain byte-identical to source.
- Remaining raw-Markdown scan flags are false positives: literal word "markdown" in Start Here text and official BRN "***IMPORTANT***" source text.
- RCFE course-material long tables were chunked so rows no longer split/truncate at page breaks.
- Moodle requirements PDF cleaned of visible `M##`, `U##`, `### feedback`, and excluded asset-folder path artifacts.
