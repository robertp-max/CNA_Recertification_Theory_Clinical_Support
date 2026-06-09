# PDF Conversion Instructions — CNA Recertification Modules 10–17

These Markdown files are **PDF-ready**. Convert them to the exact target PDF file names below. All content is **Draft / Pending Approval**.

## Target file names

| Markdown source | Target PDF |
| --- | --- |
| `CNA_Recert_Modules_10_17_24HR_Course_Documentation_Packet.md` | `CNA_Recert_Modules_10_17_24HR_Course_Documentation_Packet.pdf` |
| `CNA_M10_Vital_Signs.md` | `CNA_M10_Vital_Signs.pdf` |
| `CNA_M11_Nutrition.md` | `CNA_M11_Nutrition.pdf` |
| `CNA_M12_Emergency_Procedures.md` | `CNA_M12_Emergency_Procedures.pdf` |
| `CNA_M13_Long_Term_Care_Resident.md` | `CNA_M13_Long_Term_Care_Resident.pdf` |
| `CNA_M14_Rehabilitative_Restorative_Nursing.md` | `CNA_M14_Rehabilitative_Restorative_Nursing.pdf` |
| `CNA_M15_Observation_and_Charting.md` | `CNA_M15_Observation_and_Charting.pdf` |
| `CNA_M16_Death_and_Dying.md` | `CNA_M16_Death_and_Dying.pdf` |
| `CNA_M17_Patient_Resident_Abuse.md` | `CNA_M17_Patient_Resident_Abuse.pdf` |

## Option A — Pandoc (recommended)

```bash
# from this pdf-ready/ folder
for f in CNA_Recert_Modules_10_17_24HR_Course_Documentation_Packet CNA_M10_Vital_Signs CNA_M11_Nutrition CNA_M12_Emergency_Procedures CNA_M13_Long_Term_Care_Resident CNA_M14_Rehabilitative_Restorative_Nursing CNA_M15_Observation_and_Charting CNA_M16_Death_and_Dying CNA_M17_Patient_Resident_Abuse; do
  pandoc "$f.md" -o "$f.pdf" --pdf-engine=xelatex -V geometry:margin=1in -V mainfont="Calibri" --toc
done
```

PowerShell equivalent:

```powershell
$files = @(
  "CNA_Recert_Modules_10_17_24HR_Course_Documentation_Packet",
  "CNA_M10_Vital_Signs","CNA_M11_Nutrition","CNA_M12_Emergency_Procedures",
  "CNA_M13_Long_Term_Care_Resident","CNA_M14_Rehabilitative_Restorative_Nursing",
  "CNA_M15_Observation_and_Charting","CNA_M16_Death_and_Dying","CNA_M17_Patient_Resident_Abuse")
foreach ($f in $files) { pandoc "$f.md" -o "$f.pdf" -V geometry:margin=1in --toc }
```

## Option B — VS Code / Markdown editor
Open each `.md` and use a Markdown-to-PDF extension (e.g., "Markdown PDF"), saving with the exact target name above.

## Option C — Browser
Open the rendered Markdown, Print → Save as PDF, name the file exactly as in the table.

> Do not advertise, issue certificates, or represent this course as approved until the official approval status, provider/course identifiers, and certificate wording are confirmed.
