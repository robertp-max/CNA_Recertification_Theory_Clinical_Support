# Evidence Capture Checklist

Store screenshots, exports, learner records, and audit evidence outside this repository. Use synthetic staging users only.

| Evidence Type | Source | Capture Method | Required for Prototype? | Folder |
|---|---|---|---|---|
| Profile field screenshot/export | Moodle user profile fields and test learner profile | Screenshot or staging-only export | Yes | `/test-evidence/profile-fields/` |
| Online cap acknowledgement record | Online Cap Acknowledgement activity | Completion report, attempt record, or activity export | Yes | `/test-evidence/acknowledgements/` |
| Activity completion report | Moodle completion report | Screenshot or CSV export | Yes | `/test-evidence/completion-reports/` |
| Interaction attempt record | Required Interaction/Check activity | Attempt, post, response, grade, or completion screenshot/export | Yes | `/test-evidence/interactions/` |
| Active-time report or manual review note | Active-time candidate tool, manual review hold, or grade item | Report screenshot/export or manual review note | Yes | `/test-evidence/active-time/` |
| Quiz attempt/score | Final Exam/Test Placeholder | Quiz attempt screenshot/export and gradebook evidence | Yes | `/test-evidence/final-exam/` |
| Affidavit completion record | Final Signed Statement/Affidavit activity | Submission, acknowledgement, or completion screenshot/export | Yes | `/test-evidence/affidavit/` |
| Certificate lock/issue status | Certificate activity and restriction page | Screenshot of locked state and passing learner issue state | Yes | `/test-evidence/certificate/` |
| Admin hold log | Admin Hold grade item, manual completion, group, or restriction status | Screenshot/export and implementation log row | Yes | `/test-evidence/admin-hold/` |
| Optional clinical support skipped proof | Optional clinical support activities and passing learner completion state | Screenshot showing optional activities incomplete while required certificate gates pass | Yes | `/test-evidence/optional-clinical/` |
| Direct URL access denied proof | Certificate direct URL as blocked learner | Screenshot of denied or restricted access message | Yes | `/test-evidence/direct-url-denial/` |
| Mobile path screenshots | Mobile browser/device or responsive viewport | Screenshots of required path, restriction behavior, and certificate result | Yes | `/test-evidence/mobile-path/` |
| No-PHI warning screenshot | Course orientation, profile field instructions, optional clinical support stub, or compliance note | Screenshot | Yes | `/test-evidence/no-phi-warning/` |

