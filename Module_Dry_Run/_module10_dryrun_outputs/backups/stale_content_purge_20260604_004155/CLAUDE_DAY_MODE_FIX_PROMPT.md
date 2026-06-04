# Claude Prompt: Resolve Normal-Mode Dark Styling Issues

You are working in:

`C:\AI\Git\CNA_Recertification_Theory_Clinical_Support`

Primary app:

`standalone-course-mvp`

## Objective

Fix all currently visible normal/day-mode UI issues where components still look like dark mode. The project supports two viewing modes:

- `dark`
- `normal`

Do not merely provide design notes. Implement both visual designs in code. Every affected component must render intentionally in both modes.

## Critical Context

The current normal mode is partly implemented as a centralized CSS remap in:

`standalone-course-mvp/src/components/v2/AppShell.tsx`

That remap is incomplete. Many components still use hardcoded dark Tailwind classes or dark gradients such as:

- `bg-[#0a0505]`
- `bg-[#120a0a]/80`
- `bg-[#180a0a]`
- `bg-[#120606]`
- `bg-stone-950/60`
- `bg-black/40`
- `bg-gradient-to-br from-[#1a0d0d] via-[#120909] to-[#080404]`
- `text-white`
- `text-stone-100`
- `border-stone-900`

Do not rely only on broad global remapping. Prefer explicit theme-aware implementation in components or shared primitives so each component has a real dark design and a real normal design.

Use the current live source in `standalone-course-mvp`. Ignore stale branch references or older app structures.

## Existing Evidence

Playwright normal-mode screenshots and DOM audit were generated here:

- `standalone-course-mvp/screenshots/day-view-audit`
- `standalone-course-mvp/screenshots/day-view-audit/dark-candidates.json`

Use those screenshots as the before state.

## Known Issues To Fix

1. Reviewer tools remain fully dark in normal mode.
   - `standalone-course-mvp/src/components/v2/ReviewerToolsPanel.tsx`
   - `standalone-course-mvp/src/components/v2/AppShell.tsx`
   - The top reviewer strip and expanded reviewer panel need explicit `normal` and `dark` styling.

2. Modules page locked/default states still read as dark disabled cards.
   - `standalone-course-mvp/src/pages/ModulesPage.tsx`
   - Default locked module cards should be light subdued cards in normal mode, not gray/dark overlays.
   - The unlocked final assessment gate should not become a near-black panel in normal mode.

3. Lesson player contains the largest dark-mode carryover.
   - `standalone-course-mvp/src/pages/LessonPlayerPage.tsx`
   - `standalone-course-mvp/src/components/v2/primitives.tsx`
   - `standalone-course-mvp/src/components/v2/NarrationPlayer.tsx`
   - Fix the stepper bar, media placeholders, narration controls, transcript area, card footer, challenge options, key-term cards, and dark dividers.

4. Challenge debrief option rows are still dark.
   - `standalone-course-mvp/src/components/v2/ChallengeDebrief.tsx`
   - Option rows should have a light normal-mode treatment while preserving status emphasis.

5. Final assessment splash still has dark icon and dark metrics panels.
   - `standalone-course-mvp/src/pages/FinalAssessmentSplashPage.tsx`

6. Certificate gate still has dark restriction/preview/affidavit panels.
   - `standalone-course-mvp/src/pages/CertificateGatePage.tsx`
   - Keep the legal restriction visually prominent, but make it a normal-mode warning/notice surface instead of a black box.

7. Clinical Hub documentation support section is visibly dark in normal mode.
   - `standalone-course-mvp/src/pages/ClinicalHubPage.tsx`
   - Fix the documentation panel, PHI warning block container, textarea, disabled upload button, and any `text-white` headings.

8. Nia floating button overlaps the footer at the 1440 x 1100 viewport in normal mode.
   - `standalone-course-mvp/src/nia/components/NiaCoachButton.tsx`
   - Adjust positioning or page/footer spacing so Playwright can click it without forcing the click.

9. Nia expanded chat console needs a locked bottom-right layout.
   - Visual reference:
     `C:\Users\razer\Pictures\Screenshots\Screenshot 2026-06-01 155124.png`
   - The expanded Nia chat console should open and remain anchored in the bottom-right corner.
   - It does not need to push or move page content when there is enough room for the console.
   - Make sure the console does not cover primary controls at common desktop sizes.
   - On smaller screens, use a responsive fallback that keeps the chat usable without clipping.

10. Replace the current Nia chat icon.
   - Remove the generic chat icon treatment.
   - The collapsed launcher should read as just `Nia`.
   - Add a visibly radiating golden light treatment around `Nia` so the assistant entry point is obvious.
   - Keep the effect polished and restrained, not noisy or cartoonish.
   - Implement both `normal` and `dark` styling for the launcher.

11. Footer container is blocking the Nia launcher.
   - The visible footer content may remain, but any oversized/invisible footer container or hitbox that blocks the Nia launcher must be fixed.
   - Make the blocking footer container invisible/non-interactive where it has no visible content.
   - Do not let footer layout or pointer events prevent clicking the Nia launcher.
   - Verify this specifically at the screenshot/reference viewport and at `1440 x 1100`.

## Implementation Requirements

Follow these requirements exactly:

1. Implement both modes, not only normal mode.
   - Every changed component must intentionally define its `dark` and `normal` visual treatment.
   - Use `useUiState().brandingMode`, shared primitives, CSS variables, or a small local theme map.
   - Avoid adding one-off hardcoded light styles that break dark mode.

2. Prefer component-level theme maps or improved primitives over expanding `AppShell` into an ever-growing list of escaped Tailwind selectors.

3. Preserve all compliance copy and course behavior.
   - Do not change certificate gate logic.
   - Do not reveal exam answer keys.
   - Do not weaken PHI warnings or compliance notices.

4. Do not revert existing user edits.
   - The worktree may already contain unrelated changes.
   - Only touch files needed for this theme cleanup and related screenshot verification.

5. Keep colors professional and restrained.
   - Normal mode should read as light UI: white or near-white surfaces, subtle gray borders, restrained CI maroon accents, readable dark text.
   - Dark mode should preserve the premium burgundy/charcoal look.
   - Avoid a one-note palette and avoid making the normal mode look like a washed-out dark mode.

## Verification

Run the app:

```powershell
cd standalone-course-mvp
npm run dev -- --port 5173
```

For normal mode, seed:

```js
localStorage.setItem("ciIonBrandingMode", JSON.stringify("normal"));
localStorage.setItem("ci-cna-auth-v1", JSON.stringify(true));
```

For dark mode, seed:

```js
localStorage.setItem("ciIonBrandingMode", JSON.stringify("dark"));
localStorage.setItem("ci-cna-auth-v1", JSON.stringify(true));
```

Use Playwright screenshots to verify at minimum:

- login
- dashboard
- Nia drawer
- reviewer panel open
- modules default
- modules unlocked/final-ready
- module 0 orientation
- module 1 overview
- lesson cards 1 through 4
- module assessment splash
- module assessment quiz
- final splash
- final quiz
- final result
- certificate locked
- certificate ready
- mock certificate preview
- clinical hub
- not-found route

Capture both `normal` and `dark` mode. Compare them visually. The deliverable is not complete unless both viewing modes still look intentional.

## Definition Of Done

- All visible normal-mode dark holdouts listed above are fixed.
- Dark mode still looks intentional and is not degraded.
- Playwright screenshots exist for both modes.
- No footer overlap blocks the Nia button click.
- `npm run typecheck` passes.
- Any existing relevant tests still pass, or failures are documented with exact reasons.
