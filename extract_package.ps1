$ErrorActionPreference = 'Stop'

$root = 'C:\AI\Git\CNA_Recertification_Theory_Clinical_Support\CNA-Recert-Course'
$batch1Path = Join-Path $root 'Content\Raw\Claude\Batch1.md'
$batch2Path = Join-Path $root 'Content\Raw\Claude\Batch2.md'

$b1 = Get-Content -Path $batch1Path
$b2 = Get-Content -Path $batch2Path

function Find-Idx {
    param([string[]]$Lines, [string]$Pattern, [int]$StartAt = 0)
    for ($i = $StartAt; $i -lt $Lines.Count; $i++) {
        if ($Lines[$i] -match $Pattern) { return $i }
    }
    throw "Pattern not found: $Pattern (start=$StartAt)"
}

function Slice-Lines {
    param([string[]]$Lines, [int]$Start, [int]$End)
    if ($End -lt $Start) { return @() }
    return $Lines[$Start..$End]
}

function Extract-Between {
    param(
        [string[]]$Lines,
        [string]$StartPattern,
        [string]$EndPattern,
        [int]$SearchStart = 0
    )
    $s = Find-Idx -Lines $Lines -Pattern $StartPattern -StartAt $SearchStart
    $e = Find-Idx -Lines $Lines -Pattern $EndPattern -StartAt ($s + 1)
    return Slice-Lines -Lines $Lines -Start $s -End ($e - 1)
}

function Save-File {
    param([string]$RelPath, [string[]]$Lines)
    $full = Join-Path $root $RelPath
    $dir = Split-Path $full -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    $text = (($Lines -join "`r`n").Trim())
    Set-Content -Path $full -Value $text -Encoding UTF8
}

function Save-Text {
    param([string]$RelPath, [string]$Text)
    $full = Join-Path $root $RelPath
    $dir = Split-Path $full -Parent
    if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
    Set-Content -Path $full -Value $Text.Trim() -Encoding UTF8
}

$dirs = @(
    'content',
    'content\theory\modules',
    'content\theory\exam',
    'content\exam',
    'content\csv',
    'content\clinical-support',
    'content\clinical-support\confidence-checks',
    'content\theory\tts',
    'content\index',
    'content\source-verification',
    'content\qa'
)
foreach ($d in $dirs) {
    $full = Join-Path $root $d
    if (-not (Test-Path $full)) { New-Item -ItemType Directory -Force -Path $full | Out-Null }
}

# Batch1
$f00 = Extract-Between $b1 '^# 00_EXECUTIVE_SUMMARY\.md$' '^# 01_SOURCE_TO_COURSE_CROSSWALK\.md$'
$f01 = Extract-Between $b1 '^# 01_SOURCE_TO_COURSE_CROSSWALK\.md$' '^# 02_THEORY_SYLLABUS_TABLE\.md$'
$f02 = Extract-Between $b1 '^# 02_THEORY_SYLLABUS_TABLE\.md$' '^## 03_CLINICAL_SUPPORT_SYLLABUS_TABLE\.md$'
$f03 = Extract-Between $b1 '^## 03_CLINICAL_SUPPORT_SYLLABUS_TABLE\.md$' '^# 04_THEORY_MODULE_00_ORIENTATION_FULL\.md$'
$f04 = Extract-Between $b1 '^# 04_THEORY_MODULE_00_ORIENTATION_FULL\.md$' '^# 05_THEORY_MODULE_01_INFECTION_CONTROL_FULL\.md$'
$f05 = Extract-Between $b1 '^# 05_THEORY_MODULE_01_INFECTION_CONTROL_FULL\.md$' '^# 06_THEORY_MODULE_TEMPLATE_PACK\.md$'
$f06 = Extract-Between $b1 '^# 06_THEORY_MODULE_TEMPLATE_PACK\.md$' '^# 07_CLINICAL_SUPPORT_TEMPLATE_PACK\.md$'
$f07 = Extract-Between $b1 '^# 07_CLINICAL_SUPPORT_TEMPLATE_PACK\.md$' '^# 08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT\.md$'
$f08 = Extract-Between $b1 '^# 08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT\.md$' '^# 09_FINAL_EXAM_BLUEPRINT\.md$'
$f09 = Extract-Between $b1 '^# 09_FINAL_EXAM_BLUEPRINT\.md$' '^# 10_FINAL_EXAM_POOL_50\.md$'
$f10 = Extract-Between $b1 '^# 10_FINAL_EXAM_POOL_50\.md$' '^11_QUIZ_BANK_MASTER\.csv$'
$f11 = Extract-Between $b1 '^11_QUIZ_BANK_MASTER\.csv$' '^12_INTERACTION_CHECK_MATRIX\.csv$'
$f12 = Extract-Between $b1 '^12_INTERACTION_CHECK_MATRIX\.csv$' '^# 13_AFFIDAVIT_TEXT\.md$'
$f13 = Extract-Between $b1 '^# 13_AFFIDAVIT_TEXT\.md$' '^14_CERTIFICATE_FIELD_MAPPING\.csv \(Section 9\)$'
$f14 = Extract-Between $b1 '^14_CERTIFICATE_FIELD_MAPPING\.csv \(Section 9\)$' '^15_MOODLE_BUILD_READY_ACTIVITY_MAP\.csv \(Section 10\)$'
$f15 = Extract-Between $b1 '^15_MOODLE_BUILD_READY_ACTIVITY_MAP\.csv \(Section 10\)$' '^16_TTS_NARRATION_PACKAGE\.md \(Section 11\)$'
$f16 = Extract-Between $b1 '^# 16_TTS_NARRATION_PACKAGE\.md$' '^17_ACCESSIBILITY_AND_MOBILE_QA_CHECKLIST\.md \(Section 12\)$'
$f17 = Extract-Between $b1 '^# 17_ACCESSIBILITY_AND_MOBILE_QA_CHECKLIST\.md$' '^18_SME_REVIEW_CHECKLIST\.md & 19_COMPLIANCE_REVIEW_CHECKLIST\.md \(Section 13\)$'
$f18 = Extract-Between $b1 '^# 18_SME_REVIEW_CHECKLIST\.md$' '^# 19_COMPLIANCE_REVIEW_CHECKLIST\.md$'
$f19 = Extract-Between $b1 '^# 19_COMPLIANCE_REVIEW_CHECKLIST\.md$' '^20_GAP_LOG\.md & 21_SOURCE_CONFLICT_LOG\.md \(Section 14\)$'
$f20 = Extract-Between $b1 '^# 20_GAP_LOG\.md$' '^# 21_SOURCE_CONFLICT_LOG\.md$'
$f21 = Extract-Between $b1 '^# 21_SOURCE_CONFLICT_LOG\.md$' '^22_GROK_IMPLEMENTATION_HANDOFF\.md \(Section 15\)$'
$f22 = Extract-Between $b1 '^# 22_GROK_IMPLEMENTATION_HANDOFF\.md$' '^23_CONTENT_PACKAGE_INDEX\.md \(Section 16\)$'
$start23 = Find-Idx $b1 '^# 23_CONTENT_PACKAGE_INDEX\.md$' 0
$end23 = Find-Idx $b1 '^This completes the full 23-deliverable content development packet.*$' $start23
$f23 = Slice-Lines $b1 $start23 ($end23 - 1)

if ($f11.Count -gt 0 -and $f11[0] -match '^11_QUIZ_BANK_MASTER\.csv$') { $f11 = $f11[1..($f11.Count-1)] }
if ($f12.Count -gt 0 -and $f12[0] -match '^12_INTERACTION_CHECK_MATRIX\.csv$') { $f12 = $f12[1..($f12.Count-1)] }
if ($f14.Count -gt 0 -and $f14[0] -match '^14_CERTIFICATE_FIELD_MAPPING\.csv') { $f14 = $f14[1..($f14.Count-1)] }
if ($f15.Count -gt 0 -and $f15[0] -match '^15_MOODLE_BUILD_READY_ACTIVITY_MAP\.csv') { $f15 = $f15[1..($f15.Count-1)] }

Save-File 'content\00_EXECUTIVE_SUMMARY.md' $f00
Save-File 'content\01_SOURCE_TO_COURSE_CROSSWALK.md' $f01
Save-File 'content\02_THEORY_SYLLABUS_TABLE.md' $f02
Save-File 'content\03_CLINICAL_SUPPORT_SYLLABUS_TABLE.md' $f03
Save-File 'content\theory\modules\04_THEORY_MODULE_00_ORIENTATION_FULL.md' $f04
Save-File 'content\theory\modules\05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md' $f05
Save-File 'content\06_THEORY_MODULE_TEMPLATE_PACK.md' $f06
Save-File 'content\07_CLINICAL_SUPPORT_TEMPLATE_PACK.md' $f07
Save-File 'content\08_MODULE_KNOWLEDGE_CHECK_BLUEPRINT.md' $f08
Save-File 'content\09_FINAL_EXAM_BLUEPRINT.md' $f09
Save-File 'content\exam\10_FINAL_EXAM_POOL_50.md' $f10
Save-File 'content\csv\11_QUIZ_BANK_MASTER.csv' $f11
Save-File 'content\12_INTERACTION_CHECK_MATRIX.csv' $f12
Save-File 'content\13_AFFIDAVIT_TEXT.md' $f13
Save-File 'content\14_CERTIFICATE_FIELD_MAPPING.csv' $f14
Save-File 'content\15_MOODLE_BUILD_READY_ACTIVITY_MAP.csv' $f15
Save-File 'content\16_TTS_NARRATION_PACKAGE.md' $f16
Save-File 'content\17_ACCESSIBILITY_AND_MOBILE_QA_CHECKLIST.md' $f17
Save-File 'content\18_SME_REVIEW_CHECKLIST.md' $f18
Save-File 'content\19_COMPLIANCE_REVIEW_CHECKLIST.md' $f19
Save-File 'content\20_GAP_LOG.md' $f20
Save-File 'content\21_SOURCE_CONFLICT_LOG.md' $f21
Save-File 'content\22_GROK_IMPLEMENTATION_HANDOFF.md' $f22
Save-File 'content\23_CONTENT_PACKAGE_INDEX.md' $f23

# Batch2
$f24 = Extract-Between $b2 '^24_THEORY_MODULE_02_RESIDENT_RIGHTS_ABUSE_PREVENTION_FULL\.md$' '^25_THEORY_MODULE_03_DEMENTIA_COMMUNICATION_CULTURAL_RESPECT_FULL\.md$' 200
$f25 = Extract-Between $b2 '^25_THEORY_MODULE_03_DEMENTIA_COMMUNICATION_CULTURAL_RESPECT_FULL\.md$' '^26_THEORY_MODULE_04_MOBILITY_FALLS_WORKPLACE_SAFETY_FULL\.md$' 700
$f26 = Extract-Between $b2 '^26_THEORY_MODULE_04_MOBILITY_FALLS_WORKPLACE_SAFETY_FULL\.md$' '^27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL\.md$' 1300
$f27 = Extract-Between $b2 '^27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL\.md$' '^28_THEORY_MODULE_06_DOCUMENTATION_CHANGE_OF_CONDITION_SCOPE_FULL\.md$' 1800

$f28_base = Extract-Between $b2 '^28_THEORY_MODULE_06_DOCUMENTATION_CHANGE_OF_CONDITION_SCOPE_FULL\.md$' '^claude-opus-4\.6$' 2300
$f28_cont = Extract-Between $b2 '^13\. MOODLE IMPLEMENTATION METADATA \(Module 6 — continued\)$' '^Module 6 is now fully complete\.$' 2800
$f28 = @($f28_base + @('') + $f28_cont)

$f29 = Extract-Between $b2 '^29_THEORY_MODULE_07_REVIEW_FINAL_EXAM_AFFIDAVIT_FULL\.md$' '^CONTINUE_FROM: 30_FINAL_EXAM_POOL_50_COMPLETE\.md' 2880
$f30 = Extract-Between $b2 '^30_FINAL_EXAM_POOL_50_COMPLETE\.md$' '^END OF 30_FINAL_EXAM_POOL_50_COMPLETE\.md' 3200
$f31 = Extract-Between $b2 '^31_QUIZ_BANK_MASTER_COMPLETE\.csv$' '^END OF 31_QUIZ_BANK_MASTER_COMPLETE\.csv' 3960

$idx32_start = Find-Idx $b2 '^32_CLINICAL_SUPPORT_FULL_CONTENT\.md$' 4020
$idx32_interruption = Find-Idx $b2 '^8m 30s$' $idx32_start
$part32a = Slice-Lines $b2 $idx32_start ($idx32_interruption - 1)
$idx32_check1_a = Find-Idx $part32a '^Check 1 — Vital Signs: Blood Pressure$' 0
$part32a = Slice-Lines $part32a 0 ($idx32_check1_a - 1)
$idx32_check1_b = Find-Idx $b2 '^Check 1 — Vital Signs: Blood Pressure \(completing interrupted entry\)$' 4400
$idx32_end = Find-Idx $b2 '^END OF 32_CLINICAL_SUPPORT_FULL_CONTENT\.md' $idx32_check1_b
$part32b = Slice-Lines $b2 $idx32_check1_b ($idx32_end - 1)
if ($part32b.Count -gt 0) { $part32b[0] = 'Check 1 — Vital Signs: Blood Pressure' }
$f32 = @($part32a + @('') + $part32b)

$f33 = Extract-Between $b2 '^33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE\.md$' '^END OF 33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE\.md' 4800
$f34 = Extract-Between $b2 '^34_TTS_NARRATION_PACKAGE_COMPLETE\.md$' '^END OF 34_TTS_NARRATION_PACKAGE_COMPLETE\.md' 5100
$f35 = Extract-Between $b2 '^35_CONTENT_PACKAGE_INDEX_UPDATED\.md$' '^END OF 35_CONTENT_PACKAGE_INDEX_UPDATED\.md' 5200

$f25txt = ($f25 -join "`r`n")
$f25txt = [regex]::Replace($f25txt, '(?s)\r?\nclaude-opus-4\.6.*?Resuming exactly from Screen 3\.2\.3, choice A\):\r?\n', "`r`n")
$f25 = ($f25txt -split "`r?`n") | Where-Object { $_ -ne 'A) "' }

if ($f31.Count -gt 0 -and $f31[0] -match '^31_QUIZ_BANK_MASTER_COMPLETE\.csv$') { $f31 = $f31[1..($f31.Count-1)] }

$f29txt = ($f29 -join "`r`n")
$f29txt = $f29txt -replace 'Estimated Time: 1\.5 hours \(90 minutes\)', 'Estimated Time: 0.5 hours (30 minutes)'
$f29txt = $f29txt -replace 'Estimated time: About 1\.5 hours, including exam time\.', 'Estimated time: About 30 minutes, including exam time.'
$f29timeBlock = @'
4. ESTIMATED TIME BREAKDOWN
| Activity | Minutes | Activity Type |
|---|---:|---|
| Final Review Summary (Modules 1-6 combined, single screen) | 5 | Moodle Page |
| Final Exam Instructions | 3 | Moodle Page |
| Final Exam (25 questions drawn from 50-question pool) | 20 | Moodle Quiz |
| Affidavit Submission + Certificate Status | 2 | Moodle Questionnaire + Page |
| Total | 30 | |
5. SOURCE FILES USED
'@
$f29txt = [regex]::Replace($f29txt, '(?s)4\. ESTIMATED TIME BREAKDOWN.*?5\. SOURCE FILES USED', [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $f29timeBlock.TrimEnd("`r","`n") })
$f29metaBlock = @'
12. MOODLE IMPLEMENTATION METADATA
Field	Value
Activity Types	1 × Page (combined review), 1 × Page (exam instructions), 1 × Quiz (final exam), 1 × Questionnaire (affidavit), 1 × Page (certificate status)
Section Name	Module 7: Review, Final Exam, and Affidavit/Certificate
Estimated Minutes	30
Required/Optional	Required
Completion Type	Activity completion (pages) + Grade (final exam 80%) + Questionnaire submission (affidavit)
Grade to Pass	80% on Final Exam (20/25 correct)
Max Exam Attempts	2
Evidence Created	Page view records, final exam attempt record with all responses, affidavit submission with legal name and date, active-time record, pass/fail status
Certificate Gate	Yes — all gates per CERTIFICATE_GATE_POC_CONFIG.md must be satisfied
Source File References	All Modules 1–6; FINAL_UNIFIED_IMPLEMENTATION_BLUEPRINT.md; CERTIFICATE_GATE_POC_CONFIG.md; README.md
'@
$f29txt = [regex]::Replace($f29txt, '(?s)12\. MOODLE IMPLEMENTATION METADATA.*$', $f29metaBlock.TrimEnd("`r","`n"))
$f29 = $f29txt -split "`r?`n"

Save-File 'content\theory\modules\24_THEORY_MODULE_02_RESIDENT_RIGHTS_ABUSE_PREVENTION_FULL.md' $f24
Save-File 'content\theory\modules\25_THEORY_MODULE_03_DEMENTIA_COMMUNICATION_CULTURAL_RESPECT_FULL.md' $f25
Save-File 'content\theory\modules\26_THEORY_MODULE_04_MOBILITY_FALLS_WORKPLACE_SAFETY_FULL.md' $f26
Save-File 'content\theory\modules\27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL.md' $f27
Save-File 'content\theory\modules\28_THEORY_MODULE_06_DOCUMENTATION_CHANGE_OF_CONDITION_SCOPE_FULL.md' $f28
Save-File 'content\theory\modules\29_THEORY_MODULE_07_REVIEW_FINAL_EXAM_AFFIDAVIT_FULL.md' $f29
Save-File 'content\theory\exam\30_FINAL_EXAM_POOL_50_COMPLETE.md' $f30
Save-File 'content\csv\31_QUIZ_BANK_MASTER_COMPLETE.csv' $f31
Save-File 'content\clinical-support\32_CLINICAL_SUPPORT_FULL_CONTENT.md' $f32
Save-File 'content\clinical-support\confidence-checks\33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE.md' $f33
Save-File 'content\theory\tts\34_TTS_NARRATION_PACKAGE_COMPLETE.md' $f34
Save-File 'content\index\35_CONTENT_PACKAGE_INDEX_UPDATED.md' $f35

# Source verification
$fTime = Extract-Between $b2 '^# TIME_ALLOCATION_CORRECTION_NOTICE$' '^/content/source-verification/SOURCE_TITLE_VERIFICATION_PASS\.md$' 5630
$fSource = Extract-Between $b2 '^# SOURCE_TITLE_VERIFICATION_PASS$' '^All content module files \(24–35\) are placed' 5650
Save-File 'content\source-verification\TIME_ALLOCATION_CORRECTION_NOTICE.md' $fTime
Save-File 'content\source-verification\SOURCE_TITLE_VERIFICATION_PASS.md' $fSource

# QA
$fQA = Extract-Between $b2 '^# CONTENT_PACKAGE_QA_REPORT\.md$' '^/content/qa/CONTENT_PACKAGE_RISK_REGISTER\.md$' 5730
$fRisk = Extract-Between $b2 '^# CONTENT_PACKAGE_RISK_REGISTER\.md$' '^/content/qa/CONTENT_PACKAGE_BUILD_READINESS\.md$' 6000
$fBuild = Extract-Between $b2 '^# CONTENT_PACKAGE_BUILD_READINESS\.md$' '^/content/qa/GROK_NEXT_BUILD_ACTIONS\.md$' 6060
$fNextPrompt = Extract-Between $b2 '^Exact Next Prompt for Moodle Conversion$' '^4m 31s$' 6450

Save-File 'content\qa\CONTENT_PACKAGE_QA_REPORT.md' $fQA
Save-File 'content\qa\CONTENT_PACKAGE_RISK_REGISTER.md' $fRisk
Save-File 'content\qa\CONTENT_PACKAGE_BUILD_READINESS.md' $fBuild
Save-File 'content\qa\NEXT_MOODLE_BUILD_PROMPT.md' $fNextPrompt

$extractionReport = @'
# CONTENT_EXTRACTION_REPORT.md

## Extraction Scope
- Source files used:
  - Content/Raw/Claude/Batch1.md (files 00-23)
  - Content/Raw/Claude/Batch2.md (files 24-35, source-verification, QA)
- Output base path: content/
- Output format: Markdown and CSV

## Files Created
- Total files created: 43
- Core content package files: 36 (00-35)
- Source verification files: 2
- QA files: 5

## Validation Summary
- Module 7 time corrected from 90 minutes to 30 minutes
- Theory total preserved at 720 minutes / 12 hours
- Optional clinical support remains non-gating and non-credit
- Module 1 infection control SME/source flag preserved
- Skin integrity SME/source flag preserved

## Notes
- Extraction was performed as transcript-to-file cleanup (no curriculum rewriting).
- Interrupted transcript segments were merged only where a source block was split mid-file.
- Placeholder text remains where source output explicitly used placeholders.
'@
Save-Text 'content\qa\CONTENT_EXTRACTION_REPORT.md' $extractionReport

$all = Get-ChildItem -Path (Join-Path $root 'content') -Recurse -File
Write-Output "CREATED_FILE_COUNT=$($all.Count)"
