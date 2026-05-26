# Test Learner Matrix

Prototype Build 1 uses synthetic staging users only. Do not use real learner records or PHI.

| Test Learner | Purpose | Required Setup | Expected Certificate Result |
|---|---|---|---|
| Passing learner | Confirm certificate releases when every required gate is satisfied. | Legal name present, CNA number present, online cap acknowledgement complete, required theory activity complete, interaction complete, active-time evidence accepted or manual hold cleared, exam passed, affidavit complete, admin hold clear, audit evidence present. | Certificate available in staging-only mode. |
| Missing legal name learner | Confirm identity field gate blocks certificate. | Leave Required Legal Name blank; complete all other required items. | Certificate blocked. |
| Missing CNA number learner | Confirm CNA certificate number gate blocks certificate. | Leave Required CNA Certificate Number blank; complete all other required items. | Certificate blocked. |
| Skipped online cap acknowledgement learner | Confirm online cap acknowledgement is required. | Complete all items except Online Cap Acknowledgement. | Certificate blocked. |
| Skipped theory activity learner | Confirm required theory completion is required. | Complete all items except Sample Theory Activity. | Certificate blocked. |
| Skipped interaction learner | Confirm required interaction/check is required. | Complete all items except Required Interaction/Check. | Certificate blocked. |
| Insufficient active-time learner | Confirm active-time evidence or manual review hold blocks certificate. | Complete visible required activities but leave active-time candidate below threshold or manual review hold uncleared. | Certificate blocked. |
| Failed exam learner | Confirm final exam/test pass is required. | Complete required activities and affidavit but fail Final Exam/Test Placeholder. | Certificate blocked. |
| Missing affidavit learner | Confirm final signed statement/affidavit is required. | Complete all items except Final Signed Statement/Affidavit. | Certificate blocked. |
| Admin hold learner | Confirm admin hold blocks release. | Complete all required learner-facing items but keep Admin Hold active. | Certificate blocked. |
| Optional clinical skipped learner | Confirm optional clinical support does not gate the online CE certificate. | Complete all required theory gates and skip optional clinical support activities. | Certificate available in staging-only mode if all required gates pass. |
| Mobile-path learner | Confirm mobile path preserves required gates and evidence capture. | Complete required theory path on mobile viewport/device; capture mobile screenshots and test direct URL denial. | Certificate result follows same required-gate logic as desktop. |
