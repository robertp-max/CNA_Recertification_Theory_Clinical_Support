# ContentV2 Time-Depth Audit

> Deterministic estimate of actual learner-facing active-learning time vs the displayed/declared
> instructional minutes. Displayed labels are NOT lowered and content is NOT fabricated; the gap is
> reported so it can be closed with approved ContentV1 source or kept visible as under-depth.

## Estimation model
- **reading_wpm**: 130.0
- **delivery_active**: max(narration_min, reading_min) + 0.5 reflection (no double-count of identical text)
- **overview_active**: clamp(max(narration,reading),0.5,1.0)
- **challenge_active**: clamp(1.5 + words/180,1.5,3.0)
- **debrief_active**: clamp(2.0 + (words+remediation)/180,2.0,4.0)
- **assessment**: module + final assessment minutes excluded from lesson depth
- **clinical_support**: 0 toward required theory

## Course totals
- Required theory model (declared): **720 min** (12.0 h)
- Displayed lesson minutes (sum): **637.0 min**
- Estimated active-learning: **462.51 min (~7.71 h)**
- Module-assessment minutes excluded: 95
- Final-assessment minutes excluded: 25
- Optional clinical support counts toward 720: False
- Certificate production enabled: False
- Failing lessons: **27**

## Per-module summary

| Module | Declared min | Est. active min | Gap min | % of declared | Failing | Status |
|---|---:|---:|---:|---:|:--:|---|
| M00 | 30 | 35.34 | 0.0 | 118% | no | draft |
| M01 | 90 | 55.52 | 34.48 | 62% | YES | sme-review |
| M02 | 120 | 57.19 | 62.81 | 48% | YES | draft |
| M03 | 120 | 46.07 | 73.93 | 38% | YES | source-repair |
| M04 | 120 | 73.67 | 46.33 | 61% | YES | draft |
| M05 | 120 | 78.49 | 41.51 | 65% | YES | sme-review |
| M06 | 90 | 51.82 | 38.18 | 58% | YES | draft |
| M07 | 30 | 64.41 | 0.0 | 215% | no | draft |

### M00 - Orientation and Compliance Boundaries

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L00 | 5.0 | 5.0 | 4 | 1 | 1 | 1 | 266 | 1.68 | 2.05 | 0.5 | 1.75 | 4.0 | 7.03 | 0.0 |  | N |
| L01 | 8.0 | 8.0 | 4 | 1 | 1 | 1 | 281 | 1.78 | 2.16 | 0.5 | 1.77 | 4.0 | 7.08 | 0.92 |  | N |
| L02 | 5.0 | 5.0 | 4 | 1 | 1 | 1 | 277 | 1.75 | 2.13 | 0.5 | 1.79 | 4.0 | 7.06 | 0.0 |  | N |
| L03 | 5.0 | 5.0 | 4 | 1 | 1 | 1 | 296 | 1.88 | 2.28 | 0.5 | 1.83 | 4.0 | 7.13 | 0.0 |  | N |
| L04 | 7.0 | 7.0 | 4 | 1 | 1 | 1 | 266 | 1.68 | 2.05 | 0.5 | 1.75 | 4.0 | 7.03 | 0.0 |  | N |


### M01 - Infection Control and PPE
- **Module flags:** active 55.52min < 75% of declared 90min
- SME flag: Module 1 infection-control content requires SME/source review (no dedicated NATP 10-17 source module).
- Source status: Source-supported expansion from ContentV1 Module 01 screens. Infection control has no dedicated NATP 10-17 source module; 90-minute allocation is supported by teaching screens but requires SME/source review before production.

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 15.0 | 15.0 | 6 | 3 | 1 | 1 | 589 | 3.73 | 4.53 | 1.5 | 1.91 | 4.0 | 9.83 | 5.17 | Y | N |
| L02 | 15.0 | 15.0 | 5 | 2 | 1 | 1 | 519 | 3.4 | 3.99 | 1.0 | 1.94 | 4.0 | 9.25 | 5.75 | Y | N |
| L03 | 15.0 | 15.0 | 5 | 2 | 1 | 1 | 457 | 2.95 | 3.52 | 1.0 | 1.93 | 4.0 | 8.77 | 6.23 | Y | N |
| L04 | 15.0 | 15.0 | 6 | 3 | 1 | 1 | 482 | 3.15 | 3.71 | 1.5 | 1.83 | 4.0 | 9.57 | 5.43 | Y | N |
| L05 | 15.0 | 15.0 | 5 | 2 | 1 | 1 | 477 | 3.07 | 3.67 | 1.0 | 1.91 | 4.0 | 8.86 | 6.14 | Y | N |
| L06 | 15.0 | 15.0 | 6 | 3 | 1 | 1 | 511 | 3.22 | 3.93 | 1.5 | 1.9 | 4.0 | 9.25 | 5.75 | Y | N |

  - L01 flags: displayed>=15min but active<10min; active 9.83min < 70% of displayed 15.0min; only 3 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L02 flags: displayed>=15min but active<10min; active 9.25min < 70% of displayed 15.0min; only 2 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L03 flags: displayed>=15min but active<10min; active 8.77min < 70% of displayed 15.0min; only 2 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L04 flags: displayed>=15min but active<10min; active 9.57min < 70% of displayed 15.0min; only 3 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L05 flags: displayed>=15min but active<10min; active 8.86min < 70% of displayed 15.0min; only 2 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L06 flags: displayed>=15min but active<10min; active 9.25min < 70% of displayed 15.0min; only 3 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.

### M02 - Resident Rights, Abuse Prevention, and Boundaries
- **Module flags:** active 57.19min < 75% of declared 120min

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 20.0 | 20.0 | 8 | 5 | 1 | 1 | 691 | 4.58 | 5.32 | 2.5 | 1.81 | 4.0 | 12.24 | 7.76 | Y | N |
| L02 | 25.0 | 25.0 | 8 | 5 | 1 | 1 | 817 | 5.45 | 6.28 | 2.5 | 1.92 | 4.0 | 13.11 | 11.89 | Y | N |
| L03 | 20.0 | 20.0 | 6 | 3 | 1 | 1 | 497 | 3.22 | 3.82 | 1.5 | 1.76 | 4.0 | 9.67 | 10.33 | Y | N |
| L04 | 20.0 | 20.0 | 6 | 3 | 1 | 1 | 645 | 4.25 | 4.96 | 1.5 | 1.98 | 4.0 | 10.65 | 9.35 | Y | N |
| L05 | 20.0 | 20.0 | 7 | 4 | 1 | 1 | 684 | 4.53 | 5.26 | 2.0 | 1.94 | 4.0 | 11.52 | 8.48 | Y | N |

  - L01 flags: active 12.24min < 70% of displayed 20.0min; only 5 delivery cards for 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L02 flags: active 13.11min < 70% of displayed 25.0min; only 5 delivery cards for 25.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L03 flags: displayed>=15min but active<10min; active 9.67min < 70% of displayed 20.0min; only 3 delivery cards for 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L04 flags: active 10.65min < 70% of displayed 20.0min; only 3 delivery cards for 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L05 flags: active 11.52min < 70% of displayed 20.0min; only 4 delivery cards for 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.

### M03 - Dementia, Communication, and Respectful Care
- **Module flags:** active 46.07min < 75% of declared 120min
- SME flag: Module 3 placement and sensitive end-of-life/trauma-informed content should receive SME review.
- Source status: Draft / Source Repair Required for missing canonical sections after Screen 3.2.3.

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 25.0 | 25.0 | 8 | 5 | 1 | 1 | 907 | 6.05 | 6.98 | 2.5 | 1.99 | 4.0 | 13.69 | 11.31 | Y | N |
| L02 | 25.0 | 25.0 | 6 | 3 | 1 | 1 | 620 | 4.07 | 4.77 | 1.5 | 1.99 | 4.0 | 10.5 | 14.5 | Y | N |
| L03 | 20.0 | 20.0 | 4 | 1 | 1 | 1 | 339 | 2.22 | 2.61 | 0.5 | 1.91 | 4.0 | 7.31 | 12.69 | Y | N |
| L04 | 25.0 | 25.0 | 4 | 1 | 1 | 1 | 353 | 2.3 | 2.72 | 0.5 | 1.91 | 4.0 | 7.31 | 17.69 | Y | N |
| L05 | 10.0 | 10.0 | 4 | 1 | 1 | 1 | 339 | 2.22 | 2.61 | 0.5 | 1.86 | 4.0 | 7.26 | 2.74 |  | N |

  - L01 flags: active 13.69min < 70% of displayed 25.0min; only 5 delivery cards for 25.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L02 flags: active 10.5min < 70% of displayed 25.0min; only 3 delivery cards for 25.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L03 flags: displayed>=15min but active<10min; active 7.31min < 70% of displayed 20.0min; only 1 delivery cards for 20.0min
    - source gap: No canonical ContentV1 source (truncated/contaminated after Screen 3.2.3); Source Repair Required.
  - L04 flags: displayed>=15min but active<10min; active 7.31min < 70% of displayed 25.0min; only 1 delivery cards for 25.0min
    - source gap: No canonical ContentV1 source (truncated/contaminated after Screen 3.2.3); Source Repair Required.

### M04 - Mobility, Falls, and Workplace Safety
- **Module flags:** active 73.67min < 75% of declared 120min

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 20.0 | 20.0 | 9 | 6 | 1 | 1 | 850 | 5.62 | 6.54 | 3.0 | 1.89 | 4.0 | 13.71 | 6.29 | Y | N |
| L02 | 25.0 | 25.0 | 10 | 7 | 1 | 1 | 936 | 6.25 | 7.2 | 3.5 | 1.93 | 4.0 | 14.91 | 10.09 | Y | N |
| L03 | 20.0 | 20.0 | 11 | 8 | 1 | 1 | 997 | 6.7 | 7.67 | 4.0 | 1.82 | 4.0 | 15.98 | 4.02 |  | N |
| L04 | 20.0 | 20.0 | 9 | 6 | 1 | 1 | 876 | 5.83 | 6.74 | 3.0 | 1.99 | 4.0 | 13.95 | 6.05 | Y | N |
| L05 | 20.0 | 20.0 | 10 | 7 | 1 | 1 | 962 | 6.37 | 7.4 | 3.5 | 1.87 | 4.0 | 15.11 | 4.89 |  | N |

  - L01 flags: active 13.71min < 70% of displayed 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L02 flags: active 14.91min < 70% of displayed 25.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L04 flags: active 13.95min < 70% of displayed 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.

### M05 - Nutrition, Skin Integrity, Vital Signs, and Observation
- **Module flags:** active 78.49min < 75% of declared 120min
- SME flag: Skin integrity / pressure injury content requires SME/source review.
- Source status: Skin integrity source review active; CCCCO Module 13 skin source mapped but SME review retained.

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 25.0 | 25.0 | 12 | 9 | 1 | 1 | 1241 | 8.35 | 9.55 | 4.5 | 1.91 | 4.0 | 18.26 | 6.74 |  | N |
| L02 | 20.0 | 20.0 | 9 | 6 | 1 | 1 | 868 | 5.78 | 6.68 | 3.0 | 1.82 | 4.0 | 14.0 | 6.0 |  | N |
| L03 | 25.0 | 25.0 | 12 | 9 | 1 | 1 | 1187 | 8.0 | 9.13 | 4.5 | 1.77 | 4.0 | 18.0 | 7.0 |  | N |
| L04 | 25.0 | 25.0 | 12 | 9 | 1 | 1 | 1176 | 7.95 | 9.05 | 4.5 | 1.74 | 4.0 | 17.97 | 7.03 |  | N |
| L05 | 10.0 | 10.0 | 6 | 3 | 1 | 1 | 594 | 3.87 | 4.57 | 1.5 | 1.92 | 4.0 | 10.25 | 0.0 |  | N |


### M06 - Documentation, Reporting, PHI Avoidance, and Scope
- **Module flags:** active 51.82min < 75% of declared 90min

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 15.0 | 15.0 | 5 | 2 | 1 | 1 | 505 | 3.27 | 3.88 | 1.0 | 1.91 | 4.0 | 9.06 | 5.94 | Y | N |
| L02 | 20.0 | 20.0 | 6 | 3 | 1 | 1 | 628 | 4.12 | 4.83 | 1.5 | 1.92 | 4.0 | 10.52 | 9.48 | Y | N |
| L03 | 20.0 | 20.0 | 7 | 4 | 1 | 1 | 665 | 4.28 | 5.12 | 2.0 | 1.97 | 4.0 | 11.59 | 8.41 | Y | N |
| L04 | 15.0 | 15.0 | 7 | 4 | 1 | 1 | 572 | 3.75 | 4.4 | 2.0 | 1.82 | 4.0 | 10.74 | 4.26 | Y | N |
| L05 | 10.0 | 10.0 | 6 | 3 | 1 | 1 | 517 | 3.43 | 3.98 | 1.5 | 1.86 | 4.0 | 9.91 | 0.09 |  | N |

  - L01 flags: displayed>=15min but active<10min; active 9.06min < 70% of displayed 15.0min; only 2 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L02 flags: active 10.52min < 70% of displayed 20.0min; only 3 delivery cards for 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L03 flags: active 11.59min < 70% of displayed 20.0min; only 4 delivery cards for 20.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L04 flags: only 4 delivery cards for 15.0min
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.

### M07 - Final Review, Exam/Test, Affidavit, and Certificate Status
- Source status: Module 7 timing corrected to 30 minutes.

| Lesson | Disp | Instr | Cards | Dlv | Chl | Dbf | Words | Narr | Read | Intr | Chl-m | Rem-m | Active | Gap | Fail | Expand? |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|:--:|:--:|
| L01 | 5.0 | 5.0 | 10 | 7 | 1 | 1 | 725 | 4.98 | 5.58 | 3.5 | 1.85 | 4.0 | 13.33 | 0.0 | Y | N |
| L02 | 5.0 | 5.0 | 9 | 6 | 1 | 1 | 721 | 5.0 | 5.55 | 3.0 | 1.85 | 4.0 | 12.78 | 0.0 | Y | N |
| L03 | 3.0 | 3.0 | 7 | 4 | 1 | 1 | 466 | 3.18 | 3.58 | 2.0 | 1.85 | 4.0 | 9.85 | 0.0 | Y | N |
| L04 | 2.0 | 2.0 | 8 | 5 | 1 | 1 | 662 | 4.48 | 5.09 | 2.5 | 1.83 | 4.0 | 11.84 | 0.0 | Y | N |
| L05 | 2.0 | 2.0 | 12 | 9 | 1 | 1 | 1021 | 7.33 | 7.85 | 4.5 | 1.87 | 4.0 | 16.62 | 0.0 | Y | N |

  - L01 flags: scaffolding/answer-key phrase: On-Screen Text:
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L02 flags: scaffolding/answer-key phrase: On-Screen Text:
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L03 flags: scaffolding/answer-key phrase: On-Screen Text:
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L04 flags: scaffolding/answer-key phrase: On-Screen Text:
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.
  - L05 flags: scaffolding/answer-key phrase: On-Screen Text:
    - source gap: ContentV1 teaching screens for this lesson are already fully transformed; remaining gap requires NEW SME-authored source (not available) - not padded.

