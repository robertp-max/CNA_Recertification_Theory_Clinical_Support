# PDF Conversion Instructions

RCFE Administrator Renewal CE Package - Draft / Pending CDSS/ACS Approval

No PDF engine (xelatex/pdflatex/wkhtmltopdf/weasyprint/typst) was available in the build
environment, so per the task's fallback these PDF-ready Markdown files were generated with the
**exact target file names**. Convert them to PDF with any of the methods below.

## Files to convert

- `RCFE_Admin_CE_40HR_Course_Documentation_Packet.md` -> `RCFE_Admin_CE_40HR_Course_Documentation_Packet.pdf`
- `RCFE_M01_Laws_Regulations_Policies_Procedural_Standards.md` -> `RCFE_M01_Laws_Regulations_Policies_Procedural_Standards.pdf`
- `RCFE_M02_Business_Operations_Records_Accountability.md` -> `RCFE_M02_Business_Operations_Records_Accountability.pdf`
- `RCFE_M03_Staff_Management_Supervision_Training.md` -> `RCFE_M03_Staff_Management_Supervision_Training.pdf`
- `RCFE_M04_Psychosocial_Needs_Community_Supports.md` -> `RCFE_M04_Psychosocial_Needs_Community_Supports.pdf`
- `RCFE_M05_Physical_Needs_Restricted_Conditions_Hospice.md` -> `RCFE_M05_Physical_Needs_Restricted_Conditions_Hospice.pdf`
- `RCFE_M06_Medication_Management_Psychotropics.md` -> `RCFE_M06_Medication_Management_Psychotropics.pdf`
- `RCFE_M07_Admission_Retention_Reappraisal_Needs_Services.md` -> `RCFE_M07_Admission_Retention_Reappraisal_Needs_Services.pdf`
- `RCFE_M08_Dementia_Care_Direct_Care.md` -> `RCFE_M08_Dementia_Care_Direct_Care.pdf`
- `RCFE_M09_Dementia_Environment_Assessment_Admissions.md` -> `RCFE_M09_Dementia_Environment_Assessment_Admissions.pdf`
- `RCFE_M10_Residents_Rights_Abuse_LGBT_Cultural_Competency.md` -> `RCFE_M10_Residents_Rights_Abuse_LGBT_Cultural_Competency.pdf`
- `RCFE_M11_Physical_Environment_Emergency_Preparedness.md` -> `RCFE_M11_Physical_Environment_Emergency_Preparedness.pdf`
- `RCFE_M12_Capstone_Audit_Readiness_Final_Assessment.md` -> `RCFE_M12_Capstone_Audit_Readiness_Final_Assessment.pdf`


## Option A - Pandoc + a LaTeX engine (best fidelity)

1. Install a LaTeX engine (e.g., MiKTeX on Windows, or TeX Live), which provides `xelatex`.
2. From this `/pdf-ready/` folder run:

```
pandoc "RCFE_Admin_CE_40HR_Course_Documentation_Packet.md" -o "RCFE_Admin_CE_40HR_Course_Documentation_Packet.pdf"
pandoc "RCFE_M01_Laws_Regulations_Policies_Procedural_Standards.md" -o "RCFE_M01_Laws_Regulations_Policies_Procedural_Standards.pdf"
pandoc "RCFE_M02_Business_Operations_Records_Accountability.md" -o "RCFE_M02_Business_Operations_Records_Accountability.pdf"
pandoc "RCFE_M03_Staff_Management_Supervision_Training.md" -o "RCFE_M03_Staff_Management_Supervision_Training.pdf"
pandoc "RCFE_M04_Psychosocial_Needs_Community_Supports.md" -o "RCFE_M04_Psychosocial_Needs_Community_Supports.pdf"
pandoc "RCFE_M05_Physical_Needs_Restricted_Conditions_Hospice.md" -o "RCFE_M05_Physical_Needs_Restricted_Conditions_Hospice.pdf"
pandoc "RCFE_M06_Medication_Management_Psychotropics.md" -o "RCFE_M06_Medication_Management_Psychotropics.pdf"
pandoc "RCFE_M07_Admission_Retention_Reappraisal_Needs_Services.md" -o "RCFE_M07_Admission_Retention_Reappraisal_Needs_Services.pdf"
pandoc "RCFE_M08_Dementia_Care_Direct_Care.md" -o "RCFE_M08_Dementia_Care_Direct_Care.pdf"
pandoc "RCFE_M09_Dementia_Environment_Assessment_Admissions.md" -o "RCFE_M09_Dementia_Environment_Assessment_Admissions.pdf"
pandoc "RCFE_M10_Residents_Rights_Abuse_LGBT_Cultural_Competency.md" -o "RCFE_M10_Residents_Rights_Abuse_LGBT_Cultural_Competency.pdf"
pandoc "RCFE_M11_Physical_Environment_Emergency_Preparedness.md" -o "RCFE_M11_Physical_Environment_Emergency_Preparedness.pdf"
pandoc "RCFE_M12_Capstone_Audit_Readiness_Final_Assessment.md" -o "RCFE_M12_Capstone_Audit_Readiness_Final_Assessment.pdf"
```

(Add `--toc -V geometry:margin=1in` for a table of contents and margins.)

## Option B - Pandoc + wkhtmltopdf (HTML engine, no LaTeX)

1. Install `wkhtmltopdf` and ensure it is on PATH.
2. Run, for each file: `pandoc "FILE.md" -t html5 -o "FILE.pdf" --pdf-engine=wkhtmltopdf`

## Option C - VS Code / editor extension

Use a "Markdown PDF" extension (e.g., yzane.markdown-pdf) and export each `.md` to `.pdf`.

## Option D - Word intermediate

`pandoc "FILE.md" -o "FILE.docx"` then "Save as PDF" from Word.

_Do not advertise, issue certificates, or represent this course as CDSS/ACS-approved until the official vendor/course approval is issued._
