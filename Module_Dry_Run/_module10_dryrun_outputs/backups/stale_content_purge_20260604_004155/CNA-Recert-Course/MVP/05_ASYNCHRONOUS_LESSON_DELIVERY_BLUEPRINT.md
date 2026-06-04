# 05 — Asynchronous Lesson Delivery Blueprint

A word-level illustration of how one micro-lesson is delivered asynchronously, plus a fully worked sample for **Module 1: Infection Control and PPE**.

---

## 1. The Lesson Player Layout (what the learner sees)

**Desktop (3-column):**

```
┌───────────────────────────────────────────────────────────────────────┐
│  CI INSTITUTE wordmark        Breadcrumb: Modules › M1 › Lesson 1.3      │  ← sticky header
├───────────────────────────────────────────────────────────────────────┤
│  ▓▓▓▓▓▓▓▓░░░░░  Module progress 52%                                     │  ← progress bar
├──────────────┬────────────────────────────────────────┬───────────────┤
│ LESSON TOC   │  CENTER CONTENT (cards stack)           │ STATUS PANEL  │
│ ◉ 1.1 ✓      │  ┌─ Scenario card ───────────────────┐  │ ⏳ 2:40 / 4:00│
│ ◉ 1.2 ✓      │  │ "A resident with C. diff needs…"  │  │ ▶ Play audio  │
│ ◑ 1.3 ▸ now  │  └───────────────────────────────────┘  │ ▾ Transcript  │
│ ○ 1.4        │  ┌─ Key Concept ─────────────────────┐  │ Key terms:    │
│ ○ 1.5        │  │ Soap & water vs sanitizer…        │  │ • C. diff     │
│ ○ 1.6        │  └───────────────────────────────────┘  │ • Spores      │
│ ○ Quiz       │  ┌─ Knowledge Check ─────────────────┐  │               │
│              │  │ 1 question, 4 choices             │  │               │
├──────────────┴────────────────────────────────────────┴───────────────┤
│  ‹ Previous          🔖 Bookmark                 Next ›  (dimmed)        │  ← sticky bottom
└───────────────────────────────────────────────────────────────────────┘
```

**Mobile:** single column; TOC → hamburger/bottom sheet; status panel → bottom of stack; prev/next sticky at bottom; one question per screen.

---

## 2. Anatomy of a Micro-Lesson (3–5 minutes, in order)

| # | Element | What it shows | Length | Evidence |
|---|---------|---------------|--------|----------|
| 1 | **Lesson title & estimated time** | "Lesson 1.3 — Hand Hygiene · 4 min" | 1 line | — |
| 2 | **Learning goal** | "By the end you can choose soap vs sanitizer correctly." | 1 sentence | — |
| 3 | **Opening CNA scenario** | A recognizable shift moment (scenario card, distinct tint) | 30–50 words | active-time tracked |
| 4 | **Key concept** | The core rule in plain language (key-concept card) | 50–75 words / ≤150 words/screen | active-time tracked |
| 5 | **Why it matters** | 2–3 bullets tying to safety/legal/infection control | bullets | active-time tracked |
| 6 | **CNA practice example** | How it looks during a real task | 30–50 words | active-time tracked |
| 7 | **Common mistake** | One frequent error (amber callout) | 1 sentence | active-time tracked |
| 8 | **Knowledge check** | 1 WCAG-safe question (MC/Single Choice/True-False) | 1 question | interaction state + timestamp logged |
| 9 | **Feedback** | Immediate, explanatory, non-punitive | 20–40 words | feedback-viewed timestamp |
| 10 | **Remediation (conditional)** | If wrong: rationale + retry; module-quiz fail → back to chapter | — | remediation attempts logged |
| 11 | **Key terms / transcript / audio** | Right panel: definitions, "Read full transcript" accordion, optional ≤90s audio toggle (no autoplay; pauses on check) | reference | — |
| 12 | **Active-time indicator** | Filling hourglass "2:40 / ~4:00" | persistent | accrued time logged |
| 13 | **Completion status** | Lesson marked complete only when viewed + interaction done + min time met | — | completion timestamp |
| 14 | **Next-lesson unlock** | Sticky **Next** stays dimmed/disabled until requirements met, then enables and routes to next micro-lesson | — | progression timestamp |

### Interaction & feedback rules
- Allowed check types: Multiple Choice, Single Choice Set, True/False (with ARIA labels), Dialog Cards, short (2–3 node) Branching, Confidence Check. **Excluded:** Drag/Drop, Matching, free-text reflections (PHI risk).
- Feedback wording: "Not quite. Remember that…" — never bare "Incorrect."
- Embedded (formative) checks → unlimited retakes. Module-ending quiz → 80% to pass; 3 fails → forced chapter review before re-attempt. Final exam → no answer-key reveal after submit.

### Active-time rules
- Heartbeat (~30s) confirms scrolling/clicking/interacting.
- Idle > threshold → 60s countdown modal; no confirm → pause/stop accrual.
- Next button gated on **min active time AND interaction complete** — neutralizes click-and-walk-away.

---

## 3. Worked Sample — Module 1: Infection Control and PPE

**Module framing the learner reads first (Module Detail):**
> *Module 1: Infection Control and Standard Precautions — Infection control is one of the most important things you do every day… You already practice many of these skills. This module helps you stay sharp.* **Estimated time: 90 minutes · 6 lessons · 1 module quiz.**

Lessons: 1.1 Why It Matters · 1.2 Chain of Infection · 1.3 Hand Hygiene · 1.4 PPE · 1.5 Recognizing & Reporting · 1.6 Environmental Cleaning · Module Quiz.

### Worked micro-lesson: **Lesson 1.3 — Hand Hygiene** (≈4 min)

**Start.** Learner taps Lesson 1.3 in the TOC (1.1, 1.2 show green checks; 1.3 is half-filled "now"). Progress bar reads 52%. Hourglass starts at 0:00 / ~4:00. **Next** is dimmed.

**Scenario (card, tinted, scenario icon):**
> *You just helped a resident with a bowel movement and removed your gloves. Your hands look clean. You're already thinking about your next task down the hall.*

**Key concept (card):**
> Alcohol-based sanitizer is fine **between routine contacts** when hands aren't visibly soiled. But after body-fluid contact — even with gloves on — you must wash with **soap and water for 20 seconds**. Sanitizer does **not** kill all germs (e.g., C. diff spores, norovirus).

**Why it matters (bullets):**
> - Protects the next resident you touch.
> - Gloves leak and hands get contaminated during removal.
> - Soap and water physically removes spores sanitizer can't kill.

**CNA practice example:**
> Before leaving the room you step to the sink, wash for a full 20 seconds (hum "Happy Birthday" twice), dry, then go.

**Common mistake (amber callout):**
> ⚠ Using hand sanitizer instead of soap and water after fecal contact — spores survive alcohol.

**Knowledge check (one question):**
> *A CNA has just assisted a resident with a bowel movement and removed their gloves. Their hands appear clean. What should the CNA do?*
> A) Use alcohol-based hand sanitizer
> B) **Wash hands with soap and water**
> C) Put on new gloves immediately
> D) Wipe hands on their scrubs

Learner selects **B**, taps Submit (audio, if on, auto-pauses).

**Feedback (correct, muted-green + check):**
> ✅ "Correct. After exposure to body fluids — even if gloves were worn — soap and water handwashing is required."

**(If wrong, remediation, muted-amber + caution):**
> "Not quite. After body-fluid exposure, always wash with soap and water — sanitizer alone isn't sufficient after contact with fecal matter." → **Try again** (unlimited on formative check).

**Transcript / audio panel (right):** "Read full transcript" accordion holds the screen text verbatim; optional ≤90s neural-voice toggle (no autoplay). Key terms: *C. difficile, spores, WHO 5 Moments*.

**Completion + unlock.** Once the learner has (a) viewed the cards, (b) submitted the check, and (c) met the minimum active time, the hourglass fills, the lesson flips to a green check in the TOC, module progress ticks to ~63%, and **Next** brightens to gold: **"Next: Lesson 1.4 — Personal Protective Equipment ›"**. Tapping it logs a progression timestamp and loads 1.4.

### How Module 1 chains to completion
1. Learner completes 1.1→1.6 (each as above; 6 inline knowledge checks with ✅/❌ feedback).
2. **Module Quiz** unlocks after all 6 lessons; 80% to pass (items drawn from the question bank).
3. Pass → Module 1 marked complete → **Module 2 unlocks** (Restrict Access).
4. Completion evidence generated: lesson timestamps, 6 KC attempts, interaction completion (chain-of-infection, PPE selection, reporting priority), quiz score/attempts, accrued active time.

> **Compliance note for M1:** infection control has no dedicated NATP 10–17 source module; this content is drafted from legacy + scattered references and is flagged **NEEDS SME/source review** before production. The lesson delivery mechanics above are production-ready; the clinical text must be SME-signed first.
