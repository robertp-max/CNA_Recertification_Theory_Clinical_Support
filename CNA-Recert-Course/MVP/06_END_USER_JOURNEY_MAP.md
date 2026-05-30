# 06 — End-User Journey Map

From first login through completion of required theory and certificate readiness. Optional clinical support is reachable at every step and is always non-gating.

**Columns:** Goal · Page/View · User action · System response · Evidence generated · UI status · Possible blocker · Recovery path.

---

| # | Step | Goal | Page/View | User action | System response | Evidence generated | UI status | Possible blocker | Recovery path |
|---|------|------|-----------|-------------|-----------------|--------------------|-----------|------------------|---------------|
| 1 | First login | Enter the course | **Sign-in (approved)** | Enter credentials | Auth succeeds; routes to Landing | Login event/timestamp | Welcome toast | Wrong credentials | Helper text + forgot-password (out of redesign scope) |
| 2 | Landing / Course view | Understand value + pathways | Landing | Read hero; see 2 pathway cards + No-PHI block | Shows Required CE vs Optional Support, cert preview, module strip | View log | "Start Module 0" CTA above fold | Confusion about what counts | Pathway cards state required vs optional explicitly |
| 3 | Dashboard | "What now + how close?" | Dashboard | Read "Next Up" + progress | "Next Up" = Module 0; cert banner locked; Required ring 0%, Optional separate | Dashboard view | Locked certificate banner | Overwhelm | Single Next Up card; secondary stats hidden in carousel (mobile) |
| 4 | Module 0 orientation | Begin required path | Module 0 (Lesson) | Open Module 0 | Renders orientation micro-lessons | Lesson view timestamps | "In Progress" | — | — |
| 5 | Identity / profile | Provide cert identity | Module 0 | Enter legal name + CNA # | Fields validated/stored | Identity fields captured | Field validation | Missing/blank name or CNA# | Inline validation; can't advance until valid |
| 6 | Online-cap acknowledgement | Understand 24-hr cap | Module 0 | Check "I understand 24-hr online cap / partial credit" | Ack recorded; gate ticks | Acknowledgement record | Ack badge "Complete" | Skipped ack | Cannot complete M0 until acknowledged |
| 7 | Required theory begins | Unlock theory | Module 0 → Dashboard | Complete all M0 acks (incl. No-PHI + optional-separation) | M0 marked complete; **Module 1 unlocks** | M0 completion | M0 ✓; M1 unlocked | — | — |
| 8 | Module selection | Pick next module | Modules | Tap Module 1 card | Opens Module Detail | Catalog view | M1 "In Progress / Start" | Future modules locked | Locked rows show unlock condition |
| 9 | Module detail | Review goals + start | Module Detail | Read goals; tap Start/Continue | Loads first/next lesson | Module-detail view | Lesson rows w/ status icons | — | — |
| 10 | Lesson start | Enter lesson | Lesson/Player | Open lesson | Active-time timer starts; Next dimmed | Lesson-start timestamp | Hourglass 0:00; Next disabled | — | — |
| 11 | Lesson content | Consume micro-lesson | Lesson/Player | Read Scenario→Key Concept→Why→Example→Mistake | Active time accrues via heartbeat | Active-time accrual | Hourglass filling | Idle/walk-away | 60s idle modal; timer pauses |
| 12 | Required interaction | Prove engagement | Lesson/Player | Answer knowledge check | Immediate explanatory feedback | Interaction state + timestamp | Correct/incorrect card | Wrong answer | Non-punitive feedback + unlimited retry (formative) |
| 13 | Lesson completion | Finish lesson | Lesson/Player | Meet view+interaction+min-time | Lesson ✓; Next enables (gold) | Lesson completion timestamp | TOC check; Next active | Min time not met | Next stays disabled until time met |
| 14 | Module quiz | Demonstrate mastery | Lesson/Player (Quiz) | Take module quiz after all lessons | Scores; 80% required | Quiz score/attempts | Pass/Fail | Score <80% | Remediation → review chapters → retry (3 fails → forced review) |
| 15 | Module completion | Complete module | Module Detail/Dashboard | Pass quiz | Module ✓; **next module unlocks** | Module completion record | Module "Complete" | — | — |
| 16 | Progress update | See advancement | Dashboard | Return to dashboard | Required ring increases; "Next Up" updates | Progress snapshot | Ring % up | — | — |
| 17 | Next module unlock | Continue | Modules | Tap next module | Restrict-access unlocks sequentially | Unlock event | Next module available | Prereq incomplete | Locked w/ plain-English reason |
| 18 | Continue all modules | Finish theory | Modules 2–6 | Repeat steps 9–17 | Each module gated by prior completion | Per-module evidence | Cascading completes | M3 source flagged | M3 sections visibly flagged/locked until repaired |
| 19 | Case-based review | Synthesize | Module 7 (review) | Complete case-based review | Cross-topic scenarios | Review completion | "Review done" | — | — |
| 20 | Final review | Prep for exam | Module 7 | Take ungraded practice quiz | Feedback, no grade | Practice attempt | Ready indicator | — | — |
| 21 | Active-time threshold | Meet time gate | Dashboard/Gate Center | (system) accrued time evaluated | Active-time gate evaluated | Active-time report | Time gate badge | Below threshold | Continue lessons to accrue time; idle pauses honored |
| 22 | Final exam unlock | Unlock exam | Gate Center/Module 7 | (system) theory + active-time met | Final exam unlocks | Unlock event | Exam "Unlocked" | Theory/time incomplete | Helper text lists exact remaining gates |
| 23 | Final exam attempt | Pass exam | Final Exam | Take 25-of-50 randomized | Scores; 80% pass; answers hidden | Exam score/attempt/timestamp | Pass/Fail | — | — |
| 24 | Failed exam path | Recover | Final Exam | (if <80%) | Locked retake period; directs to weak modules; randomized re-attempt | Failed-attempt + remediation record | "Review then retry" | Repeated fails | Required module review before next attempt; no answer reveal |
| 25 | Passed exam path | Advance to attestation | Final Exam → Affidavit | (if ≥80%) | Affidavit unlocks | Pass record | "Exam passed" | — | — |
| 26 | Affidavit | Attest completion | Affidavit | Sign final statement | Affidavit recorded (e-sign method flagged unresolved) | Signed-statement record | "Affidavit complete" | E-sign method undecided | Wet-sign fallback noted; gate flagged in Gate Center |
| 27 | Certificate status check | See readiness | Certificate Status | View readiness ring + checklist | All required gates evaluated | Gate snapshot | Ready / N blockers | A gate failing | Checklist shows exact blocker + link to fix |
| 28 | Gate Center review | Understand each gate | Gate Center | Inspect requirement rows | Plain-English status per gate | Gate evidence detail | Per-gate badges | — | — |
| 29 | Certificate preview / unlock readiness | Confirm eligibility | Certificate Status | View mock preview | Mock watermark; **no issuance** | Cert-preview status | "Preview Open (mock)" | Provider NAC#/wording unresolved | Certificate stays mock until approval metadata confirmed |
| 30 | Audit packet readiness | Confirm evidence exists | Audit | Review required vs optional evidence + trail | Timestamped trail; export affordances | Audit packet preview | Evidence buckets filled | Missing evidence | Trace to source gate; complete it |
| 31 | Optional clinical support (anytime) | Practice w/o pressure | Clinical Hub | Open any CS tool at any step | Logs optional records **separately**; never affects readiness | Separate optional records | "Optional · Non-Credit" badge | (None — by design) | Skipping it never blocks the certificate |

---

## Journey Invariants (must always hold)

- **Optional ≠ gating:** Step 31 can be done, skipped, or repeated with zero effect on steps 27–29.
- **Sequential unlocks:** each module/gate unlocks only when its prerequisite evidence exists.
- **No PHI:** every free-text/upload (M6 practice, Clinical Hub) shows the pinned warning.
- **Resumability:** at any point, refresh/return restores progress and the "Next Up" action.
- **No certificate issuance:** the certificate remains a mock preview until provider metadata + wording + e-signature method are approved.
