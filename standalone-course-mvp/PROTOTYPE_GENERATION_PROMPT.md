# High-Fidelity Prototype Generation Prompt

Generate high-fidelity desktop and mobile UI prototypes for the CareIndeed / CI Institute of Nursing standalone CNA Recertification Theory + Clinical Support MVP.

## Brand Source

Use the repo brand kit as the controlling visual source: `CNA-Recert-Course/Branding_Kit`.

Use available assets from that kit:

- Primary logo: `logos/ci-ion-logo-original.svg`
- White logomark: `logos/ci-ion-logomark-white.svg`
- Favicons from `favicons/`
- Brand imagery from `images/landingpic1.webp` where useful

## Brand Tokens

- Primary maroon: `#8B1515`
- Primary dark maroon: `#681010`
- Accent gold: `#FFC107`
- Accent gold hover: `#E0A800`
- Background: `#F8F9FA`
- Surface: `#FFFFFF`
- Text: `#212529`
- Border: `#DEE2E6`
- Headings: Poppins 500/600/700 with Montserrat fallback
- Body: Open Sans 400/600 with Inter fallback
- Mono: Roboto Mono

## Visual Style

Create a clean, expensive, modern, professional healthcare training interface. Use high contrast, white and light-gray surfaces, strong CI maroon/gold accents, rounded cards/buttons at 8px, 12px, or 16px, large tap targets, and mobile-first spacing. Do not use pastel visuals, childish gamification, decorative blobs, or dense PDF-like walls of text.

## Compliance Guardrails

Every prototype must visibly preserve these rules:

- Prototype only.
- Not a live CE course.
- Not a live certificate system.
- Do not claim CDPH approval.
- Do not imply full CNA renewal completion.
- Do not collect PHI.
- Do not use real learner records.
- Certificate preview must be watermarked: `STAGING / PROTOTYPE ONLY - NOT A LIVE CE CERTIFICATE`.
- Optional clinical support is not a certificate gate.
- Optional clinical support is not California renewal clinical-hour credit.
- Active-time is simulated/prototype only.
- Moodle migration and plugin validation remain pending.

## Component Inventory

Design these components for both desktop and mobile:

- Splash/login shell with CareIndeed/CI Institute of Nursing lockup from the Branding_Kit.
- Stakeholder review ribbon.
- Unlock Mode ribbon.
- Top navigation with horizontally scrollable mobile behavior.
- Status pills for pass/locked/warning.
- Dashboard progress cards.
- Required vs optional pathway cards.
- Module cards with review flags and accordions.
- Gate status rows.
- PHI warning banner.
- TTS/transcript placeholder panel.
- Final exam preview question card.
- Affidavit acknowledgement panel.
- Watermarked mock certificate preview.
- Clinical support content cards.
- Audit packet evidence cards and table.
- Moodle migration map table.
- QA negative-test panel.
- Editable demo user profile form.
- Buttons, disabled buttons, error states, loading states, and sign-out action.

## Page Views

Create high-fidelity desktop and mobile variants for every view:

1. Splash/Login Page.
2. Stakeholder Review Landing Page.
3. Learner Dashboard.
4. Course Landing / Start Here.
5. Module Navigation.
6. Module 0 Orientation.
7. Module 1 Infection Control and PPE.
8. Module 2 Resident Rights, Abuse Prevention, and Boundaries.
9. Module 3 Dementia, Communication, and Respectful Care.
10. Module 4 Mobility, Falls, and Workplace Safety.
11. Module 5 Nutrition, Skin Integrity, Vital Signs, and Observation.
12. Module 6 Documentation, Reporting, PHI Avoidance, and Scope.
13. Final Review.
14. Final Exam/Test Preview.
15. Final Statement/Affidavit.
16. Certificate Gate Status.
17. Watermarked Mock Certificate Preview.
18. Optional Clinical Support Hub Landing.
19. Skills Refresh Library.
20. Practice Planner.
21. Scheduling Guidance.
22. Optional Confidence Checks.
23. Documentation Support with PHI warning.
24. RN/Preceptor Signoff Instructions.
25. Help / Office Hours / Contact.
26. Audit Packet Preview.
27. Moodle Migration Map.
28. QA / Negative Test Panel.
29. Admin/Stakeholder Review Notes.

## Required Interactions

- Stakeholder splash/login with email, password, loading, invalid-login error, and demo-only warning.
- Session-style stakeholder sign-in and sign-out.
- Editable fictional demo user profile seeded as James Bond:
  - Display name: James Bond
  - Role: Stakeholder Admin / Demo Learner
  - Email: admin@careindeed.com
  - CNA certificate number: CNA-DEMO-007
  - Renewal cycle: 2026-2028
  - Course cohort: CNA Recertification Standalone MVP Review
  - Phone: (650) 268-4983
  - Organization: Care Indeed / CI Institute of Nursing
  - Location: Menlo Park, CA
  - Review status: Stakeholder demo user
  - Notes: Fictional seeded profile for prototype review only; not a real learner record.
- Reset to James Bond Demo User button.
- Stakeholder Unlock Mode toggle with persistent ribbon.
- Unlock Mode bypasses navigation locks for review only and does not mark completion gates.
- Module 0 acknowledgement controls.
- Module 1 scenario check with correct/incorrect feedback.
- Final exam pass/fail simulation.
- Affidavit acknowledgement.
- Certificate gate list that remains truthful.
- Optional clinical support pages that never affect certificate readiness.
- PHI warning before uploads, documentation support, signoff support, and free-text areas.
- QA controls for negative tests and passing-state simulation.

## Output Expectations

Return polished, implementation-ready UI prototypes with desktop and mobile frames. Use realistic healthcare training content, concise learner copy, WCAG-aware contrast, accessible labels, keyboard-friendly forms, and clear required vs optional separation. Do not generate fake CDPH approval claims, official certificate language, production-readiness claims, or clinical-credit claims. Keep the certificate mock visibly watermarked as prototype only.
