# 03 - Completion and Survey Evidence Matrix

Status: Draft / Pending Approval. Generated Moodle MVP implementation artifact (completion rules generated where not present in source). One row per CNA unit, RCFE course, and BRN module, plus finals.

Minimum-minutes basis: 50 instructional minutes = 1 CE/contact hour (BRN explicit; applied as a conservative seat-time target for CNA/RCFE - confirm exact seat-time policy with SME/CDPH/CDSS). Pass thresholds are configurable defaults pending SME confirmation.

Columns: lane | course/unit/module | hours | min minutes | Moodle section/activity | completion condition | grade/pass condition | restrict-access dependency | evidence generated | Moodle report/export | responsible role | survey risk if missing | gen/missing status

## CNA / CDPH CE

| lane | unit | hours | min min | section/activity | completion condition | pass condition | restrict-access dep | evidence | report/export | role | survey risk if missing | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CNA | U01 Vital Signs I | 2 | 100 | Overview/Objectives/Content/Checkpoint/Quiz/Scenario/Attestation | all activities complete + quiz passed | quiz >=80% | none | completion + grade + attempts + attestation | activity/course completion, grader, quiz responses | Teacher/Manager | seat-time/completion not evidenced | Generated |
| CNA | U02 Vital Signs II | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U01 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | sequence not enforced | Generated |
| CNA | U03 Nutrition/Hydration | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U02 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | U04 Emergency Procedures | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U03 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | U05 LTC Resident I | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U04 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | U06 LTC Resident II | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U05 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | Year 1 total not evidenced | Generated |
| CNA | U07 Rehabilitative Nursing | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U06 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | Year 2 start not gated | Generated |
| CNA | U08 Observation/Charting I | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U07 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | U09 Observation/Charting II | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U08 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | U10 Death and Dying | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U09 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | U11 Resident Abuse I | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U10 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | mandated-report topic not evidenced | Generated |
| CNA | U12 Resident Abuse II | 2 | 100 | same pattern | all complete + quiz passed | quiz >=80% | U11 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| CNA | FINAL Comprehensive | n/a | n/a | Final assessment | final passed | final >=80% | all U01-U12 complete | grade + attempts | grader, quiz responses, course completion | Teacher/Manager | overall mastery not gated | Generated |

CNA course completion = all 12 units complete + Final passed. Total online CE hours = 24 (Year 1 = 12, Year 2 = 12). Online CE only; no clinical hours.

## RCFE / CDSS CETP (9 LIC 9140 courses)

| lane | course | hours | min min | section/activity | completion condition | pass condition | restrict-access dep | evidence | report/export | role | survey risk if missing | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RCFE | RCFE-CETP-001 Laws/Regs | 4 | 200 | Overview/Objectives/Timed content/Checkpoint/Scenario/Final/Evaluation/Attestation | all complete + final passed + attestation | final >=70% | scenario complete | completion + grade + attempts + eval + attestation | completion, grader, quiz | Teacher/Manager | hour/seat-time not evidenced | Generated |
| RCFE | RCFE-CETP-002 Dementia Foundations | 4 | 200 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | dementia coverage not evidenced | Generated |
| RCFE | RCFE-CETP-003 Dementia Safety/Env | 4 | 200 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | dementia coverage not evidenced | Generated |
| RCFE | RCFE-CETP-004 Resident Rights | 2 | 100 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | rights coverage not evidenced | Generated |
| RCFE | RCFE-CETP-005 Medication Mgmt | 4 | 200 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | oversight scope not evidenced | Generated |
| RCFE | RCFE-CETP-006 Admission/Retention | 3 | 150 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| RCFE | RCFE-CETP-007 Emergency/Environment | 2 | 100 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| RCFE | RCFE-CETP-008 Staff Supervision | 2 | 100 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| RCFE | RCFE-CETP-009 Business Operations | 2 | 100 | same pattern | all complete + final passed | final >=70% | scenario complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |

RCFE total = 27 hours across 9 courses. The 40-hour/12-module concept is future expansion only and is not represented in this matrix.

## BRN / CEP RN Case Management (10 modules + capstone)

| lane | module | contact hrs | min min | section/activity | completion condition | pass condition | restrict-access dep | evidence | report/export | role | survey risk if missing | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BRN | M01 Foundations | 3 | 150 | Objectives/Timed content/Case scenario/Documentation activity/Quiz | all complete + quiz passed | quiz >=80% | none | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | contact-hour time not evidenced | Generated |
| BRN | M02 Assessment/Planning | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M01 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | sequence not enforced | Generated |
| BRN | M03 Care Coordination | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M02 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M04 Documentation/Legal | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M03 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M05 Rights/Ethics | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M04 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M06 Transitions/Discharge | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M05 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M07 Utilization/Payer | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M06 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M08 Quality/Risk | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M07 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M09 Chronic/Geriatric | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M08 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | M10 Integrated Capstone | 3 | 150 | same pattern | all complete + quiz passed | quiz >=80% | M09 complete | completion + grade + attempts | completion, grader, quiz | Teacher/Manager | completion not evidenced | Generated |
| BRN | CAPSTONE_FINAL | n/a | n/a | Capstone final assessment | capstone passed | capstone >=80% | all M01-M10 complete | grade + attempts | grader, quiz responses, course completion | Teacher/Manager | overall mastery not gated | Generated |

BRN course completion = all 10 modules complete + capstone passed. Total = 30 contact hours = at least 1,500 instructional minutes (10 x 150). Contact hours, not CEUs.
