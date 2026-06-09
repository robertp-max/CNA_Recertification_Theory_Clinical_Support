# PDF-Ready Module Documentation Packet - Conversion Notes

Status: Draft / Pending BRN CEP Approval. No CEP number issued.

## What is here
For each document below there is a clean PDF-ready Markdown (`.md`) source and a
generated `.pdf` (rendered via reportlab, no external engine required):

- `BRN_CM_CE_30HR_Course_Documentation_Packet.(md|pdf)` - full course documentation packet
- `BRN_CM_M01_Foundations_of_RN_Case_Management.(md|pdf)`
- `BRN_CM_M02_Assessment_Intake_Care_Planning.(md|pdf)`
- `BRN_CM_M03_Care_Coordination.(md|pdf)`
- `BRN_CM_M04_Documentation_Legal_Charting.(md|pdf)`
- `BRN_CM_M05_Patient_Rights_Advocacy_Ethics.(md|pdf)`
- `BRN_CM_M06_Transitions_of_Care_Discharge_Planning.(md|pdf)`
- `BRN_CM_M07_Utilization_Review_Payer_Communication.(md|pdf)`
- `BRN_CM_M08_Quality_Risk_Incident_Escalation.(md|pdf)`
- `BRN_CM_M09_Chronic_Disease_Geriatric_High_Risk_Care.(md|pdf)`
- `BRN_CM_M10_Capstone_Final_Assessment.(md|pdf)`

## How to regenerate the PDFs
From this `LMS_COURSE_PACKAGE` folder:

```
python build_pdf_packet.py
```

Requires `reportlab` (already present). The script re-emits both the `.md` and `.pdf`.

## Alternative converters (if you prefer your own styling)
The `.md` files are standard Markdown and convert cleanly with any of:

```
# Pandoc + a PDF engine (wkhtmltopdf / LaTeX / weasyprint)
pandoc INPUT.md -o OUTPUT.pdf --pdf-engine=wkhtmltopdf

# Or to DOCX for Word-based review
pandoc INPUT.md -o OUTPUT.docx
```

## Editing rule
The Markdown files are the editable source. If you change content, edit the data in
`build_pdf_packet.py` (single source) and re-run, or edit the `.md` and convert with
your own tool. The primary deliverable remains the main course package markdown in the
parent folder; this packet is module-level documentation support.

## Compliance reminder
Do not advertise, issue certificates, or represent this course as BRN-approved until the
official BRN CEP approval and provider number are issued. All cases are fictional and
de-identified; no PHI.
