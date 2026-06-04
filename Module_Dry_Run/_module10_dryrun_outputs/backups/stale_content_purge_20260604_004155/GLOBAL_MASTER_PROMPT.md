# Global Master Prompt: CNA Recertification Theory + Clinical Support Project

Use this prompt for all future work in this repository.

Repository:

`C:\AI\Git\CNA_Recertification_Theory_Clinical_Support`

Primary app:

`standalone-course-mvp`

## Product Mission

Build and maintain a standalone CNA recertification theory and optional clinical support preview for CI Institute of Nursing. The application must support required online theory workflows, certificate gate previews, audit-safe learner progress surfaces, no-PHI safeguards, and optional non-gating clinical support.

## Non-Negotiable Compliance Rules

1. No PHI.
   - Do not request, display, store, or encourage real patient/resident identifiers, facility identifiers, medical record numbers, dates of birth, or actual case details.
   - All clinical documentation examples must be fictional or de-identified.

2. Do not imply full California CNA renewal completion.
   - The app may describe required online theory completion, but must preserve the distinction between online CE theory and full renewal requirements.

3. Optional clinical support is always non-gating and non-credit.
   - It must never count toward certificate readiness.
   - It must never be represented as clinical-hour credit.

4. Certificate surfaces are mock previews unless production approval metadata, provider identification, approved wording, affidavit method, and all compliance gates are configured.

5. Exams must not reveal answer keys or learner-facing rationales that compromise assessment integrity.

## Viewing Modes Requirement

The project has two viewing modes:

- `dark`
- `normal`

Every new component, page, element, state, modal, panel, drawer, card, control, and visual primitive must implement both designs in code.

This means:

- Do not only implement a dark design.
- Do not only implement a normal design.
- Do not provide design notes instead of implementation.
- Do not rely on screenshots, comments, or future TODOs as the second mode.
- Do not rely on a brittle global remap to rescue hardcoded dark classes.

The deliverable for any UI work includes real code paths for both modes.

## Theme Implementation Standard

When adding or changing UI, use one of these approaches:

1. Preferred: shared primitives or theme-aware class maps.
2. Acceptable: local `brandingMode` branching via `useUiState()` when a component has special visual needs.
3. Acceptable: CSS variables or scoped selectors when they are stable and easy to inspect.
4. Avoid: hardcoded dark-only classes such as `bg-stone-950`, `bg-[#080404]`, `text-white`, or dark gradients unless they are behind an explicit dark-mode branch.
5. Avoid: expanding a centralized selector-remap list for every new escaped Tailwind class.

Normal mode should use:

- white or near-white surfaces
- subtle gray borders
- readable dark text
- restrained CI maroon accents
- warning surfaces that are light and legible, not black boxes

Dark mode should use:

- charcoal/burgundy surfaces
- readable light text
- amber/maroon accents used intentionally
- strong contrast without washing out hierarchy

## UI Quality Rules

1. Build actual usable experiences, not landing-page placeholders.
2. Do not add decorative cards inside cards.
3. Do not add decorative gradient orbs or bokeh backgrounds.
4. Keep cards at 8px radius or less unless the existing component requires otherwise.
5. Use icons for common controls when available, preferably from `lucide-react`.
6. Text must not overflow, overlap, or become unreadable on mobile or desktop.
7. Fixed-format controls need stable dimensions so hover, labels, dynamic text, and loading states do not shift layout.
8. Do not scale font size with viewport width.
9. Letter spacing should be `0` unless matching an established local pattern.
10. Avoid one-note palettes. Normal mode must not look like a pale dark mode, and dark mode must not become muddy or low-contrast.

## Engineering Rules

1. Read the existing code before editing.
2. Follow local patterns and existing app architecture.
3. Keep changes scoped to the request.
4. Do not revert unrelated worktree changes.
5. Use shared primitives when they reduce duplicated theme logic.
6. Preserve learner state, certificate gate, exam, and audit behavior unless the task explicitly requests a behavior change.
7. Keep comments minimal and useful.
8. Use TypeScript types already present in the project.

## Verification Standard For UI Changes

For any UI change, verify both modes.

At minimum:

```powershell
cd standalone-course-mvp
npm run typecheck
```

When the change affects visible UI, run the app and capture or inspect both modes:

```powershell
npm run dev -- --port 5173
```

Normal mode seed:

```js
localStorage.setItem("ciIonBrandingMode", JSON.stringify("normal"));
localStorage.setItem("ci-cna-auth-v1", JSON.stringify(true));
```

Dark mode seed:

```js
localStorage.setItem("ciIonBrandingMode", JSON.stringify("dark"));
localStorage.setItem("ci-cna-auth-v1", JSON.stringify(true));
```

For page-level or shared-component work, use Playwright screenshots for both modes.

## Definition Of Done For New UI

A new UI deliverable is complete only when:

- The feature works.
- The normal-mode design is implemented.
- The dark-mode design is implemented.
- Both modes are visually reviewed.
- No text or controls overlap.
- No hidden dark-mode styling leaks into normal mode.
- No compliance copy or safety behavior is weakened.
- Typecheck passes or any failure is documented with exact cause.

