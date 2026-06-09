"""
Build the supporting XLSX workbook for the CNA Recertification online CE build.

Aligned structure: 12 units x 2 online CE hours = 24 online CE hours total
(Year 1 = U01-U06; Year 2 = U07-U12). Source backbone: CCCCO Nurse Assistant
Model Curriculum (Revised Dec 2018), Modules 10-17, mapped under each unit.

Support/defensibility artifact only. The markdown course package is the primary
deliverable. All content is Draft / Pending Approval. No real approval/provider/
course numbers. Fictional, de-identified scenarios only; no PHI. Online CE only;
no clinical hours.

Run:  python build_workbook.py
"""

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

OUT = "CNA_Recert_Modules_10_17_24HR_LMS_BUILD_WORKBOOK.xlsx"

HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
HEADER_FONT = Font(color="FFFFFF", bold=True, size=11)
TITLE_FONT = Font(bold=True, size=13, color="1F4E78")
NOTE_FONT = Font(italic=True, size=9, color="7F7F7F")
WRAP = Alignment(vertical="top", wrap_text=True)
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

BANNER = ("DRAFT / PENDING APPROVAL - Do not advertise, issue certificates, or "
          "represent this course as approved until approval status, "
          "provider/course identifiers, and certificate wording are confirmed. "
          "Online CE only; no clinical hours. 12 units x 2 online CE hours = 24. "
          "Source backbone: Modules 10-17. Fictional data only; no PHI.")

# (unit_id, year, unit_title, source_module_num, source_module_title)
UNITS = [
    ("U01", 1, "Vital Signs I: Purpose, Terminology, Temperature, and Pain Observation", 10, "Vital Signs"),
    ("U02", 1, "Vital Signs II: Pulse, Respirations, Blood Pressure, Recording, and Reporting", 10, "Vital Signs"),
    ("U03", 1, "Nutrition, Hydration, Diets, Feeding Assistance, and Aspiration Awareness", 11, "Nutrition"),
    ("U04", 1, "Emergency Procedures, Distress Recognition, Choking Response, and Facility Codes", 12, "Emergency Procedures"),
    ("U05", 1, "Long Term Care Patient/Resident I: Aging, Body Systems, and Common Conditions", 13, "Long Term Care Patient/Resident"),
    ("U06", 1, "Long Term Care Patient/Resident II: Dementia-Sensitive Care, Psychosocial Needs, and Community Resources", 13, "Long Term Care Patient/Resident"),
    ("U07", 2, "Rehabilitative Nursing and Restorative Care", 14, "Rehabilitative Nursing"),
    ("U08", 2, "Observation and Charting I: Objective/Subjective Observation, Terminology, and Reporting Cues", 15, "Observation and Charting"),
    ("U09", 2, "Observation and Charting II: Charting Documents, Legal Documentation, and Change Reporting", 15, "Observation and Charting"),
    ("U10", 2, "Death and Dying: Grief, Comfort, Hospice Awareness, and Postmortem Care Boundaries", 16, "Death and Dying"),
    ("U11", 2, "Patient/Resident Abuse I: Rights, Abuse Types, Prevention, and Risk Recognition", 17, "Patient/Resident Abuse"),
    ("U12", 2, "Patient/Resident Abuse II: Mandated Reporting, Confidentiality, Documentation, and Final Applied Scenario", 17, "Patient/Resident Abuse"),
]

UNIT_FLAG = {
    "U01": "Confirm normal-range values; observe/report level only (no hands-on competency)",
    "U02": "Confirm BP/pulse/resp ranges; recording within CNA scope; report abnormal findings",
    "U03": "Confirm therapeutic-diet list vs facility manual; feeding at assistance level; aspiration precautions",
    "U04": "HIGH: state no hands-on CPR/Heimlich competency; confirm facility codes/AHA-ARC language",
    "U05": "Confirm aging/A&P content; complications of immobility at observe/report level",
    "U06": "Confirm person-centered dementia language; CNA scope (no behavioral diagnosis)",
    "U07": "ROM/restorative at assist/observe level only; confirm device list",
    "U08": "Objective vs subjective accuracy; reporting cues within scope",
    "U09": "HIGH PHI emphasis (charting); document observations not diagnoses",
    "U10": "Add sensitivity note; postmortem-care boundaries; no pronouncement of death",
    "U11": "Confirm abuse types and resident-rights framing",
    "U12": "HIGH: confirm CA mandated-reporter channels/timelines/ombudsman framing",
}

UNIT_OBJ = {
    "U01": "Define vital-signs terminology; temperature routes/ranges and influencing factors; objective pain observation and scope-safe reporting.",
    "U02": "Pulse, respirations, and blood-pressure concepts and adult normal ranges; record T-P-R and BP within scope; report abnormal findings.",
    "U03": "Therapeutic diets and the CNA role; safe feeding-assistance and aspiration prevention; hydration/I&O; cultural/religious respect; observe-report alternative routes.",
    "U04": "Recognize distress; immediate scope-safe actions (stay, call nurse, EMS chain); conscious-choking response within scope; facility codes. No hands-on CPR certification.",
    "U05": "Aging changes by body system; common conditions; complications of immobility observed and reported; basic A&P for scope-safe observation.",
    "U06": "Dementia-sensitive person-centered care and de-escalation within scope; psychosocial/spiritual needs; community resources.",
    "U07": "Restorative philosophy; CNA role on the rehab team; ADLs and self-care; adaptive devices; ROM and immobility prevention at assist/observe level.",
    "U08": "Objective vs subjective observation and senses used; medical word elements/abbreviations; reporting cues and scope-safe escalation.",
    "U09": "Charting document types; accurate/timely/factual scope-safe recording and corrections; objective incident report; change-in-condition reporting.",
    "U10": "Five stages of grief; scope-safe emotional/spiritual support; dying-resident rights; approaching vs biological death; comfort, hospice support, postmortem boundaries.",
    "U11": "Abuse terminology and types; resident rights; CNA prevention role and risk recognition.",
    "U12": "Mandated-reporter duty, pathways, and timelines; confidentiality; objective documentation; final applied scenario.",
}


def style_sheet(ws, headers, widths, title):
    ws["A1"] = title
    ws["A1"].font = TITLE_FONT
    ws["A2"] = BANNER
    ws["A2"].font = NOTE_FONT
    ws["A2"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=len(headers))
    ws.row_dimensions[2].height = 42
    header_row = 4
    for c, h in enumerate(headers, start=1):
        cell = ws.cell(row=header_row, column=c, value=h)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border = BORDER
    for c, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.freeze_panes = ws.cell(row=header_row + 1, column=1)
    return header_row


def write_rows(ws, header_row, rows):
    for r, row in enumerate(rows, start=header_row + 1):
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.alignment = WRAP
            cell.border = BORDER


wb = Workbook()

# ---------------------------------------------------------------- Course_Map
ws = wb.active
ws.title = "Course_Map"
headers = ["Unit ID", "Year", "Unit Title", "Online CE Hours", "Source Module #",
           "Source Module Title", "Source Reference", "Completion Requirement",
           "Evidence Artifact", "SME/Compliance Flag"]
hr = style_sheet(ws, headers, [9, 6, 40, 12, 12, 26, 30, 36, 36, 34],
                 "Course_Map - 24-Hour CNA Recertification Online CE (12 units x 2 hours)")
src = "ContentV2/survey-evidence/_source_text/module-{n}.txt"
comp = ("All lessons viewed + knowledge check attempted + scenario completed + "
        "documentation/reflection submitted")
evid = ("Activity-completion timestamps, KC attempt record, scenario branch log, "
        "submitted simulated artifact, time-in-unit log")
rows = []
for uid, yr, title, mnum, mtitle in UNITS:
    rows.append([uid, yr, title, 2, mnum, mtitle, src.format(n=mnum), comp, evid, UNIT_FLAG[uid]])
rows.append(["TOTAL", "", "12 units x 2 online CE hours", 24, "10-17",
             "Modules 10-17 (source backbone)",
             "Year 1 = U01-U06 (12h); Year 2 = U07-U12 (12h)",
             "Both Year assessments passed at 80% + attestation + seat-time",
             "Course completion report + certificate record (post-approval)",
             "Aligned 12-unit x 2-hour structure; no unit-vs-module conflict"])
write_rows(ws, hr, rows)

# --------------------------------------------------------- Module_Source_Map
ws = wb.create_sheet("Module_Source_Map")
headers = ["Unit ID", "Unit Title", "Source Module #", "Source Module Title",
           "Required Source Content to Preserve", "LMS Destination",
           "Assessment Linkage", "Notes / Risks"]
hr = style_sheet(ws, headers, [9, 38, 12, 24, 50, 16, 24, 34],
                 "Module_Source_Map - each unit mapped to source Modules 10-17")
preserve = {
    10: "TPR + BP concepts, adult normal ranges, factors raising/lowering vitals, pain as observation, scope-safe reporting/charting",
    11: "Nutrients/diets, dysphagia/aspiration awareness, hydration/I&O, feeding assistance, cultural respect, alternative routes (observe/report)",
    12: "Distress recognition, EMS/help chain, conscious-choking response within scope, facility codes, scope boundaries",
    13: "Aging changes/body systems, common conditions, immobility complications, dementia-sensitive care, psychosocial needs, community resources",
    14: "Restorative philosophy, rehab-team role, ADLs, ROM types, adaptive/comfort devices, immobility prevention, documentation role",
    15: "Objective vs subjective, word elements/abbreviations, charting document types, accurate/timely/factual recording, incident reporting",
    16: "Five stages of grief, comfort/dignity, dying rights, approaching vs biological death, hospice role, postmortem boundaries",
    17: "Abuse types/definitions, mandated-reporter duty, prevention, recognition, reporting pathways, confidentiality/HIPAA basics",
}
msm = []
for uid, yr, title, mnum, mtitle in UNITS:
    msm.append([uid, title, mnum, mtitle, preserve[mnum], f"Year {yr} > {uid}",
                f"KC-{uid} + S-{uid} + Year {yr} Assessment",
                "Source title preserved as backbone; objectives at observe/report level"])
write_rows(ws, hr, msm)

# ----------------------------------------------------------- LMS_Activity_Map
ws = wb.create_sheet("LMS_Activity_Map")
headers = ["Activity ID", "Year", "Unit ID", "Source Module #", "Activity Name",
           "Moodle Activity Type", "Learner Action Required",
           "Completion Tracking Setting", "Restrict Access Rule",
           "Gradebook Category", "Evidence Generated"]
hr = style_sheet(ws, headers, [12, 6, 9, 12, 28, 18, 28, 24, 30, 20, 26],
                 "LMS_Activity_Map - Moodle build, unit IDs U01-U12 (Draft)")
act_rows = []
for uid, yr, title, mnum, mtitle in UNITS:
    cat = f"Year {yr} - Formative"
    act_rows += [
        [f"{uid}-PAGE", yr, uid, mnum, f"{uid} Objectives & Banner", "Page",
         "View objectives + compliance banner", "Mark as viewed",
         "After Section 0 complete", cat, "View timestamp"],
        [f"{uid}-LSN", yr, uid, mnum, f"{uid} Lesson", "Lesson",
         "Work through branching lesson content", "Require view (+min pages/time)",
         f"After {uid}-PAGE viewed", cat, "Lesson completion + time"],
        [f"{uid}-H5P", yr, uid, mnum, f"{uid} Interactive Practice", "H5P",
         "Complete interactive practice", "Require attempt",
         f"After {uid}-LSN viewed", cat, "Interaction/xAPI record"],
        [f"S-{uid}", yr, uid, mnum, f"{uid} Scenario (fictional)", "Lesson (branching)",
         "Make scope-safe decisions", "Require completion",
         f"After {uid}-LSN viewed", cat, "Scenario branch log"],
        [f"KC-{uid}", yr, uid, mnum, f"{uid} Knowledge Check", "Quiz",
         "Attempt low-stakes quiz (unlimited)", "Require attempt",
         f"After S-{uid} complete", cat, "Attempt record + score"],
        [f"DOC-{uid}", yr, uid, mnum, f"{uid} Documentation/Reflection", "Assignment",
         "Submit simulated documentation (fictional)", "Require submission",
         f"Available with {uid}-LSN", cat, "Submitted artifact"],
    ]
act_rows += [
    ["SEC0-ID", 0, "-", "-", "Identity Confirmation", "Feedback/Choice",
     "Confirm legal name (+CNA # if required)", "Require submission",
     "Available at enrollment", "Orientation", "Identity record"],
    ["SEC0-NOPHI", 0, "-", "-", "No-PHI Agreement", "Feedback",
     "Accept no-PHI agreement", "Require submission",
     "Available at enrollment", "Orientation", "Agreement record"],
    ["Y1-ASSESS", 1, "-", "10-13", "Year 1 Assessment", "Quiz",
     "Pass summative at 80%", "Require pass grade (>=80%)",
     "After U01-U06 complete", "Year 1 - Summative", "Attempts, score, duration"],
    ["Y2-ASSESS", 2, "-", "14-17", "Year 2 Assessment", "Quiz",
     "Pass summative at 80%", "Require pass grade (>=80%)",
     "After U07-U12 complete", "Year 2 - Summative", "Attempts, score, duration"],
    ["FINAL-AFF", 2, "-", "-", "Final Affidavit", "Assignment",
     "Submit completion affidavit", "Require submission",
     "After both Year assessments passed", "Course", "Affidavit submission"],
    ["CERT", 2, "-", "-", "Certificate (gated, post-approval)", "Custom certificate",
     "Download once gate met + approval confirmed", "Restricted by course completion",
     "After all gate items incl. APPROVAL CONFIRMED (currently OFF)", "Course",
     "Certificate record + unique ID"],
]
write_rows(ws, hr, act_rows)

# -------------------------------------------------------- Assessment_Blueprint
ws = wb.create_sheet("Assessment_Blueprint")
headers = ["Assessment ID", "Unit ID", "Source Module #", "Question Type",
           "Question Stem", "Correct Answer", "Rationale",
           "Remediation Guidance", "Learner Visibility", "Admin/Faculty Visibility"]
hr = style_sheet(ws, headers, [14, 9, 12, 14, 46, 12, 40, 32, 20, 20],
                 "Assessment_Blueprint - seed items mapped to U01-U12 (Internal key - DO NOT publish)")
ab_seed = {
    "U01": ("Which adult finding should the CNA report to the nurse as abnormal?", "Oral temp 103F (febrile)", "Febrile temperature is abnormal and reported within scope."),
    "U02": ("A CNA may adjust a resident's blood pressure medication if the reading is high.", "False", "Out of CNA scope; CNAs observe and report, never medicate/adjust orders."),
    "U03": ("A resident on a thickened-liquid diet is served thin juice. The CNA should:", "Withhold and verify the diet order with the nurse", "Aspiration risk; verify order and report before serving."),
    "U04": ("Completing this online unit certifies the CNA in hands-on CPR.", "False", "Online CE only; hands-on CPR certification is separate."),
    "U05": ("Which is a complication of immobility the CNA observes and reports?", "Pressure injury / skin breakdown", "Immobility raises pressure-injury risk; observe and report."),
    "U06": ("A resident with dementia is agitated during evening care. Best scope-safe approach?", "Calm, simple, reassuring approach; reduce stimulation", "Person-centered de-escalation within scope."),
    "U07": ("Restorative care for a resident who can do part of their ADLs means the CNA should:", "Assist only as needed and encourage independence", "Restorative philosophy promotes maximum independence."),
    "U08": ("Which is an OBJECTIVE observation?", "Resident ate 50% of lunch", "Objective = measurable/observed fact; others are subjective/diagnostic."),
    "U09": ("A CNA may chart 'resident has pneumonia' based on a cough.", "False", "CNAs document observations, not diagnoses."),
    "U10": ("A dying resident's family member is angry at staff. Best CNA response?", "Respond with compassion, listen, and report concerns to the nurse", "Compassionate, scope-safe support; escalate appropriately."),
    "U11": ("Which is an example of involuntary seclusion / a resident-rights violation?", "Confining a resident to a room against their will as punishment", "Involuntary seclusion is a form of abuse/rights violation."),
    "U12": ("A CNA witnesses a coworker handling a resident roughly and threatening them. The CNA must:", "Ensure resident safety and report immediately per mandated-reporter duty", "CNAs are mandated reporters; ensure safety and report promptly."),
}
ab = []
for uid, yr, title, mnum, mtitle in UNITS:
    stem, ans, rat = ab_seed[uid]
    ab.append([f"KC-{uid}-01", uid, mnum, "MCQ/TF", stem, ans, rat,
               f"Route to {uid} lesson review (source Module {mnum}).",
               "Score + remediation only", "Full internal key"])
write_rows(ws, hr, ab)

# ------------------------------------------------------------- Certificate_Gate
ws = wb.create_sheet("Certificate_Gate")
headers = ["Gate Item", "Required Condition", "LMS Evidence Source",
           "Manual Review Needed", "Approval Placeholder", "Risk if Omitted"]
hr = style_sheet(ws, headers, [26, 36, 30, 18, 26, 36],
                 "Certificate_Gate - blocked until ALL 12 units + both Years complete (Draft)")
cg = [
    ["Identity confirmed", "Section 0 identity checkpoint complete",
     "Section 0 activity completion + attestation", "Optional", "N/A",
     "Cannot tie completion to a verified learner"],
    ["No-PHI agreement", "Accepted in Section 0", "Activity completion record",
     "No", "N/A", "Privacy/PHI exposure risk"],
    ["Year 1 units complete", "U01-U06 all activities complete",
     "Activity completion roll-up", "No", "N/A", "Incomplete content coverage"],
    ["Year 1 assessment passed", ">= 80%", "Gradebook (grade-to-pass)", "No",
     "N/A", "Unverified competency at the knowledge level"],
    ["Year 2 units complete", "U07-U12 all activities complete",
     "Activity completion roll-up", "No", "N/A", "Incomplete content coverage"],
    ["Year 2 assessment passed", ">= 80%", "Gradebook (grade-to-pass)", "No",
     "N/A", "Unverified competency at the knowledge level"],
    ["Seat-time evidence", "Minimum documented engaged time met (24 online CE hours)",
     "Logs / time reports / min-time conditions", "Recommended spot-check",
     "N/A", "Hour claims not defensible"],
    ["Learner attestation/affidavit", "Final affidavit submitted",
     "Assignment/Feedback submission", "Recommended", "N/A",
     "Integrity of completion not attested"],
    ["Approval status confirmed",
     "Provider/course approval + certificate wording confirmed",
     "Master packet / CDPH confirmation", "REQUIRED",
     "APPROVAL PLACEHOLDER - PENDING (currently NOT met)",
     "Issuing an unapproved certificate = compliance violation"],
]
write_rows(ws, hr, cg)

# ------------------------------------------------------ Application_Packet_Checklist
ws = wb.create_sheet("Application_Packet_Checklist")
headers = ["Packet Item", "Draft Status", "Owner", "Source Reference",
           "Missing Information", "Approval Status", "Notes"]
hr = style_sheet(ws, headers, [34, 14, 16, 36, 34, 16, 34],
                 "Application_Packet_Checklist (Draft) - 12 units x 2 hours")
mp = "__Master-Application-Packet/01_CNA_CDPH_CE_PACKET/"
apc = [
    ["Course outline (12 units x 2 hours)", "Draft", "Owner/SME",
     "24_HOUR_CNA_COURSE_MATRIX_FINAL.md; CDPH_192B_COURSE_LIST_ATTACHMENT.md",
     "None (structure aligned)", "Pending", "12 units U01-U12; Modules 10-17 source backbone"],
    ["24-hour allocation table", "Draft", "Owner/SME", "Section D / matrix",
     "None", "Pending", "12 units x 2 hours = 24"],
    ["Year 1 / Year 2 split", "Draft", "Owner", "Section E", "None", "Pending",
     "U01-U06 / U07-U12 (12 / 12)"],
    ["Unit-to-source mapping", "Draft", "SME", "Sections C & F", "None", "Pending",
     "Each unit maps to source Module 10-17"],
    ["Flyer / brochure copy", "Draft", "Owner/Marketing", "Course package",
     "Final approval + provider/course IDs; refund policy", "Pending",
     "Marked Draft - Pending Approval"],
    ["Certificate text", "Draft", "Owner", "Course package",
     "Approval/provider/course #, signer, CNA # requirement", "Pending",
     "Placeholders only"],
    ["Course evaluation form", "Draft", "SME", "Course package", "None", "Pending", ""],
    ["Recordkeeping policy", "Draft", "Owner/LMS admin", "Section L",
     "Retention period (CDPH vs BPPE)", "Pending", "12-unit completion evidence"],
    ["Refund / cancellation policy", "Placeholder", "Owner/Finance",
     "BPPE refund/pro-rata source files", "Pull institution's approved policy",
     "Pending", "Placeholder only"],
    ["SME/instructor of record", "Draft", "SME/Compliance",
     mp, "Vanessa Valerio evidence attachment (resume/CV, license, expiration)",
     "Pending", "Vanessa Valerio assigned; evidence is final verification"],
    ["Provider/course approval evidence", "Pending", "Owner",
     mp, "No approved provider/course # issued", "Pending",
     "Course stays Draft until obtained"],
]
write_rows(ws, hr, apc)

# ------------------------------------------------------------ SME_Compliance_Flags
ws = wb.create_sheet("SME_Compliance_Flags")
headers = ["Item ID", "Unit / Source Module", "Flag Type", "Issue", "Risk Level",
           "Reviewer Needed", "Required Action", "Status"]
hr = style_sheet(ws, headers, [12, 18, 18, 44, 12, 18, 40, 12],
                 "SME_Compliance_Flags (Draft) - source-hour normalization flagged only if clinically necessary")
sf = [
    ["F-APPROVAL", "ALL", "Compliance",
     "No approved provider/course number; certificate/advertising are Draft",
     "HIGH", "Owner", "Obtain approval before issuing/advertising", "Open"],
    ["F-NORM", "ALL", "Clinical normalization",
     "Source CCCCO theory hours are uneven; the CE build normalizes to 2 hours/unit. Flag only if a specific unit needs more time for clinical accuracy.",
     "LOW", "Clinical SME",
     "Confirm 2-hour unit time is clinically sufficient per unit; adjust content depth, not structure", "Open"],
    ["F-U01U02", "U01-U02 / M10", "Clinical accuracy",
     "Vital-signs ranges/factors must match current standards", "MEDIUM",
     "Clinical SME", "Verify ranges; observe/report framing", "Open"],
    ["F-U03", "U03 / M11", "Clinical accuracy",
     "Therapeutic-diet list and aspiration precautions", "MEDIUM",
     "Clinical SME", "Confirm vs facility diet manual; assistance level only", "Open"],
    ["F-U04", "U04 / M12", "Scope/Clinical",
     "Must not imply hands-on CPR/Heimlich certification", "HIGH",
     "Clinical SME", "Explicit disclaimer; verify codes + AHA/ARC language", "Open"],
    ["F-U05U06", "U05-U06 / M13", "Scope/Content",
     "Dementia-sensitive person-centered language; aging/A&P accuracy", "MEDIUM",
     "Clinical SME", "Confirm person-centered language; CNA scope (no diagnosis)", "Open"],
    ["F-U07", "U07 / M14", "Scope",
     "ROM/restorative must stay assist/observe level", "MEDIUM",
     "Clinical SME", "No independent-therapy claim; confirm devices", "Open"],
    ["F-U08U09", "U08-U09 / M15", "PHI/Scope",
     "Charting units; observations not diagnoses; PHI risk", "HIGH",
     "SME/Compliance", "Reinforce no-PHI + objective documentation rules", "Open"],
    ["F-U10", "U10 / M16", "Sensitivity/Scope",
     "End-of-life content; postmortem boundaries; no pronouncement of death", "MEDIUM",
     "Clinical SME", "Add sensitivity note; confirm postmortem steps", "Open"],
    ["F-U11U12", "U11-U12 / M17", "Legal/Compliance",
     "CA mandated-reporter channels, timelines, ombudsman framing", "HIGH",
     "Compliance/Legal", "Verify current CA reporting requirements", "Open"],
    ["F-PHI", "ALL", "Privacy",
     "No real resident/facility data anywhere; fictional only", "HIGH",
     "Compliance", "Verify banners/agreements; periodic free-text review", "Open"],
]
write_rows(ws, hr, sf)

# -------------------------------------------------------------- Audit_Evidence_Log
ws = wb.create_sheet("Audit_Evidence_Log")
headers = ["Evidence Item", "Generated By", "Stored Where", "Retention Period",
           "Review Responsibility", "Export Method", "Notes"]
hr = style_sheet(ws, headers, [30, 26, 28, 18, 22, 28, 30],
                 "Audit_Evidence_Log (Draft) - 12-unit completion evidence")
ael = [
    ["Enrollment & identity record", "Section 0 / LMS enrollment",
     "Moodle user + activity records", "[confirm]", "LMS admin",
     "CSV/PDF export", "CNA # only if required"],
    ["Unit completion data (U01-U12)", "Unit activities", "Moodle completion report",
     "[confirm]", "LMS admin/faculty", "Completion report (CSV)", "12 units x 2 hours"],
    ["Time / participation logs", "Moodle logs", "Moodle logs/reports",
     "[confirm]", "LMS admin", "Logs export (CSV)", "Supplemental to attestation"],
    ["Knowledge-check attempts (KC-U01..U12)", "Formative quizzes", "Gradebook/quiz reports",
     "[confirm]", "Faculty", "Quiz report export", "Unlimited attempts"],
    ["Year assessment attempts/scores", "Summative quizzes", "Gradebook",
     "[confirm]", "Faculty", "Grade export", "80% pass"],
    ["Scenario decision logs (S-U01..U12)", "Lesson/H5P", "Activity reports", "[confirm]",
     "Faculty", "Report export", "Branch choices"],
    ["Learner attestation / affidavit", "Assignment/Feedback", "Submission records",
     "[confirm]", "LMS admin", "PDF/CSV export", ""],
    ["Course evaluation responses", "Feedback module", "Feedback module",
     "[confirm]", "Admin", "CSV export", "No PHI"],
    ["Certificate record (post-approval)", "Certificate activity",
     "Certificate logs", "[confirm]", "LMS admin", "PDF + verification ID",
     "Only after approval confirmed"],
]
write_rows(ws, hr, ael)

wb.save(OUT)
print("Wrote", OUT, "with sheets:", [s.title for s in wb.worksheets])
