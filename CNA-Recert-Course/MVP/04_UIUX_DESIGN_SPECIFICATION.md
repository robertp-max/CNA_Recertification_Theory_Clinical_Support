# 04 — UI/UX Design Specification

**Direction:** Dark Premium Cinematic. Replace the task interface with a guided page-view system. Mobile-first for shift workers. WCAG 2.2 AA. **The sign-in/login page is approved — do not redesign it.**

---

## 1. Design Principles

1. **One next action.** Every screen answers "what do I do now?" via progressive disclosure ("Next Up"), never a backlog.
2. **Impenetrable wall** between Required Online CE and Optional Clinical Support — visual, structural, and computational.
3. **Calm under fatigue.** Charcoal base, generous spacing, no decorative gamification, ≤3–4 sentence text blocks.
4. **Premium institutional tone.** Serif display + clean sans body; antique gold used sparingly as the "where to look" signal.
5. **Accessibility is non-negotiable.** AA contrast, status never by color alone, 44×44px targets, visible focus, keyboard-complete.
6. **Evidence over decoration.** Compliance data shown as polished human-readable rows, never raw booleans or spreadsheets.

---

## 2. Color Palette (tokens)

| Token | Hex | Use |
|-------|-----|-----|
| `--bg` | `#121212` | App base (never pure black) |
| `--surface` | `#1E1E1E` | Cards/panels |
| `--surface-raised` | `#262626` | Elevation (lighter, not drop-shadow) |
| `--burgundy` | `#7A1026` | Structural headers, required accents, warning blocks |
| `--oxblood` | `#5A0F1D` | PHI warning blocks, deep accents |
| `--gold` | `#D2A84C` | Primary CTAs, active states, progress rings, focus ring |
| `--gold-deep` | `#B7892B` | Gold hover/pressed |
| `--text` | `#F7EEDC` | Primary reading text (warm white) |
| `--text-2` | `#E0E0E0` | Secondary text |
| `--muted` | `#B0B0B0` | Metadata/labels |
| `--line` | `#444444` | Hairline borders |
| `--success` | accessible green | Complete (always paired w/ check + label) |
| `--warn` | desaturated amber | Locked/Needs Review (paired w/ icon + label) |

**Rule:** charcoal/black ~80% of surface; burgundy for structure; gold strictly for interactive/CTA. All text pairings must pass 4.5:1 (3:1 large).

---

## 3. Typography

- **Display (h1–h3):** Serif (Playfair Display / Lora / Merriweather) — page titles, module headers only.
- **Body/UI:** Sans (Inter / Public Sans / Roboto) — body ≥16px, labels, tables.
- Line-height ≥1.5; lesson reading column 60–75 characters wide.
- Semantic mapping: Page title `<h1>` → Module `<h2>` → Section `<h3>`; never skip levels for sizing.

---

## 4. Layout Grid & Navigation

- **Desktop:** sticky top header; content max-width 1200px, centered, generous margins. Lesson view = 3 columns.
- **Mobile:** persistent bottom nav (Home/Modules/Certificate/Hub), single-column stacks, sticky prev/next on lesson.
- **Progress bar** anchored directly under the header on lesson views (endowed-progress effect).
- **Navigation behavior:** primary nav reflects current route; locked destinations show a lock affordance, not a dead click.

---

## 5. Desktop Shell vs Mobile Shell

| Element | Desktop | Mobile |
|---------|---------|--------|
| Wayfinding | Sticky top nav (wordmark left, links center w/ gold hover, bell+avatar right), breadcrumbs in lesson | 4–5 icon bottom bar, oxblood active w/ gold icon |
| Lesson nav | Persistent left column TOC | Hamburger / bottom sheet |
| Status/transcript | Right column | Off-canvas drawer / bottom of stack |
| Lesson controls | Inline | Sticky bottom prev/bookmark/next |
| Content width | ≤1200px | Full-width cards, dynamic type |

---

## 6. Card System

- 8px rounded corners; elevation via surface-lightness shift or soft colored glow (drop shadows vanish on charcoal).
- Card types: **Info/Key Concept** (neutral surface), **Scenario** (distinct tint + scenario icon), **Knowledge Check** (distinct tint + check icon), **Why It Matters** (bulleted), **Common Mistake** (amber callout), **PHI Warning** (oxblood, non-dismissible).
- Safe glassmorphism only on progress/help/reviewer-note panels: blur ≤15px, 5–10% white tint, 1px `rgba(255,255,255,.15)` border, `@supports` flat fallback.

---

## 7. Status Badge System (never color-only)

| State | Icon (shape) | Label | Color |
|-------|--------------|-------|-------|
| Not Started | empty circle | "Not Started" | muted |
| In Progress | half-filled circle | "In Progress" | gold |
| Needs Review | triangle | "Needs Review" | amber |
| Blocked / Locked | padlock | "Locked" | muted/amber |
| Complete | check | "Complete" | green |
| Optional / Non-Credit | tag/diamond | "Optional · Non-Credit" | neutral (clinical hub) |

---

## 8. Progress Indicators

- **Circular** (pathway/dashboard): heavy gold SVG stroke on muted track, **always** paired with text "%".
- **Linear** (module/lesson): thin burgundy fill; ARIA label announces percentage.
- **Active-time**: subtle filling hourglass; non-anxiety-inducing; proves engagement.

---

## 9. Certificate Path Timeline

Vertical stepper with connecting lines: Complete = green check; Active = gold highlight; Locked = grey padlock. Steps: Identity → Online-Cap Ack → Required Theory → Required Interaction → Active-Time → Final Exam → Affidavit → Certificate Fields → Admin Hold Clear → **Certificate**.

## 10. Gate Requirement Rows

Icon + requirement title + plain-English description + status badge. Example helper text: *"Final Exam — Unlocks upon verified completion of Modules 0–6 and active-time validation."* Never show `is_active_time_met = false`.

## 11. Audit Evidence Rows

Dense but padded (16px) rows: timestamp · action · actor/IP. e.g., *"Affidavit electronically signed — 10:45 AM PDT — IP logged."* Required evidence and optional records in separate tabs/sections.

## 12. Optional Support Tool Cards

Lighter charcoal, no burgundy border, "Optional · Non-Credit" overline on every card. Visually subordinate to required CE.

## 13. PHI Warning Blocks

Oxblood background, warning triangle, high-contrast white text, **non-dismissible**, pinned directly above each free-text/upload field: *"STOP: Do not enter Protected Health Information (PHI), real patient names, or facility data. Use simulated case data only."*

## 14. Active-Time Display

Filling hourglass + "Time on lesson: 2:40 / ~4:00". Next button visibly dimmed + disabled until time + interaction satisfied. Idle → 60s countdown modal: *"Still there? Your time pauses in 0:60."*

## 15. Lesson Check Interaction States

`default` (unanswered, gold submit) → `selected` (gold ring on choice) → `submitted-correct` → `submitted-incorrect`. One question per screen on mobile.

## 16. Correct / Incorrect Feedback States

- **Correct:** muted green border + check icon; reinforcement rationale (20–40 words).
- **Incorrect:** **muted amber** border + caution icon (never jarring red); "Not quite. Remember that…" + rationale; offer retry.

## 17. Empty / Locked / Unlocked States

- **Empty:** soft professional illustration + single CTA to next logical area.
- **Locked:** padlock + plain-English unlock condition; subdued opacity; still keyboard-focusable with explanation.
- **Unlocked:** gold accent + clear CTA.

---

## 18. Page-by-Page UI/UX Plan

### 1) Sign-in — APPROVED, DO NOT CHANGE
Frozen. No visual or structural edits. (Current `ReviewerLogin` + demo-login function.)

### 2) Course / Landing
- **Purpose:** value prop + pathway distinction + frictionless start.
- **Layout:** cinematic hero (charcoal + burgundy gradient, serif title) → primary CTA "Start Module 0" → two heavy pathway cards (12-hr Required CE vs Optional Support) → module progress strip → certificate status preview.
- **Required:** No-PHI block; pathway separation; CTA above fold (mobile).
- **Avoid:** task lists; blending CE and optional.

### 3) Dashboard (command center)
- **Purpose:** answer "what now + how close" in <5s.
- **Layout:** greeting → **"Next Up" gold card** (top-left/top-mobile) → locked Certificate banner → Required Theory CE ring → **separate** Optional Support progress → quick access tiles.
- **States:** certificate preview locked (padlock + desaturated) until gates pass.
- **Mobile:** Next Up at very top; secondary stats in swipeable carousel.

### 4) Modules (catalog)
- **Purpose:** see full 12-hr curriculum + macro progress.
- **Layout:** left mission/brand panel + module-card grid (title, duration, linear progress, status badge). Streaming-premium look, not file directory.

### 5) Module Detail
- **Purpose:** review goals + start correct lesson.
- **Layout:** overview card (time commitment) → learning goals → sequential lesson rows (locked rows dimmed) → Start/Continue FAB. Mobile: module selector → sticky dropdown.

### 6) Lesson / Player
- **Purpose:** consume content, pass checks, accrue active time.
- **Layout (desktop 3-col):** left TOC w/ status icons · center cards (Scenario/Key Concept/Why It Matters/Example/Common Mistake/Knowledge Check) · right status+transcript+key terms. Bottom: sticky prev/bookmark/next; Next disabled until time+interaction met.
- **Mobile:** single column; sidebars → bottom sheet/hamburger; sticky bottom controls.

### 7) Certificate Status
- **Purpose:** explain lock + remaining actions in plain English.
- **Layout:** large readiness ring → gate checklist (Theory / Active-Time / Exam / Affidavit…) → notice "Optional clinical support does not affect this score." Mock watermark; no issuance.

### 8) Gate Center
- **Purpose:** deep compliance control + scenario simulator (retain existing strength).
- **Layout:** integrity controls → requirement-row table (icon+title+plain desc+badge) → optional-boundary panel → audit-evidence tie-in → certificate decision card. No raw booleans.

### 9) Clinical Support Hub
- **Purpose:** optional, non-credit practice sandbox.
- **Layout:** unmissable "Optional & Non-Credit" banner → tool categories (CS-1…CS-7) → practice cards (each badged) → featured case → No-PHI block above every input. Lighter charcoal, no burgundy borders.

### 10) Audit
- **Purpose:** verify defensible records.
- **Layout:** tabs — Required Certificate Evidence | Optional Support Records → audit-trail timeline (timestamps) → Export PDF / Export CSV. Premium padded tables.

### 11) Moodle Map
- **Purpose:** executive migration roadmap.
- **Layout:** 3-column mapping (MVP section / Moodle component `mod_*` / implementation notes) in app-shell styling. Reads as roadmap, not Jira.

---

## 19. Anti-Patterns to Avoid (design)

Long PDFs/passive audio; required video; decorative gamification (leaderboards/avatars/badges); dense quiz banks without feedback; drag/drop & matching on mobile; complex (>3-node) branching; free-text reflections that invite PHI; **merged required/optional progress**; optional activities acting as certificate gates; pure-black backgrounds; medium-grey-on-dark-grey text; color-only status; hidden/below-the-fold PHI warnings; shrinking the desktop header instead of a real mobile bottom nav.
