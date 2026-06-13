# 17 - Accessibility and Mobile Requirements

Status: Draft / Pending Approval. Target: WCAG-oriented accessibility and mobile usability. Final accessibility audit: recommended before production.

## WCAG-oriented checks
- Aim for WCAG 2.1 AA-oriented practices across content and activities. Run an accessibility checker (e.g., Moodle's built-in/brickfield-style tools if available) and remediate findings.

## Keyboard navigation
- All interactive elements (menus, quizzes, activities) operable via keyboard; visible focus indicators.

## Screen reader headings
- Use proper heading structure (H1/H2/H3) in pages and labels; avoid skipping levels; meaningful link text.

## Alt text
- All meaningful images include descriptive alt text; decorative images marked as decorative.

## Captions / transcripts
- All audio/video include captions and/or transcripts.

## Color contrast
- Text/background contrast meets AA ratios; do not rely on color alone to convey meaning.

## Table readability
- Use real data tables with header cells/scope; avoid layout tables; keep tables simple and labeled.

## Mobile responsiveness
- Use a responsive theme; verify quizzes, content, and navigation render and function on small screens (test AC-01).

## Low bandwidth design
- Optimize media sizes; avoid auto-playing heavy media; provide text alternatives so content works on slow connections.

## PDF accessibility notes
- Any PDF resources should be tagged/accessible (headings, reading order, alt text, selectable text - not scanned images). Prefer native Moodle pages over PDFs where feasible.
