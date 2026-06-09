# -*- coding: utf-8 -*-
"""
Generate all markdown deliverables for the RCFE Administrator Renewal CE package
from the single-source data module (rcfe_ce_data.py):

  1) Primary course package : ../RCFE_Admin_Renewal_CE_Course_Package.md  (Sections A-X)
  2) PDF-ready full packet   : ../pdf-ready/RCFE_Admin_CE_40HR_Course_Documentation_Packet.md
  3) PDF-ready 12 modules    : ../pdf-ready/RCFE_M01_...md ... RCFE_M12_...md
  4) Conversion instructions : ../pdf-ready/CONVERSION_INSTRUCTIONS.md

Run: python build_docs.py
"""
import os
import rcfe_ce_data as D

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(BASE, "pdf-ready")
os.makedirs(PDF, exist_ok=True)

PF = D.PACKET_FACTS
C = D.COURSE

PDF_FILENAMES = {
    "M01": "RCFE_M01_Laws_Regulations_Policies_Procedural_Standards",
    "M02": "RCFE_M02_Business_Operations_Records_Accountability",
    "M03": "RCFE_M03_Staff_Management_Supervision_Training",
    "M04": "RCFE_M04_Psychosocial_Needs_Community_Supports",
    "M05": "RCFE_M05_Physical_Needs_Restricted_Conditions_Hospice",
    "M06": "RCFE_M06_Medication_Management_Psychotropics",
    "M07": "RCFE_M07_Admission_Retention_Reappraisal_Needs_Services",
    "M08": "RCFE_M08_Dementia_Care_Direct_Care",
    "M09": "RCFE_M09_Dementia_Environment_Assessment_Admissions",
    "M10": "RCFE_M10_Residents_Rights_Abuse_LGBT_Cultural_Competency",
    "M11": "RCFE_M11_Physical_Environment_Emergency_Preparedness",
    "M12": "RCFE_M12_Capstone_Audit_Readiness_Final_Assessment",
}


# --------------------------------------------------------------------------
# Reusable narrative blocks (shared by primary package and full packet)
# --------------------------------------------------------------------------
def block_pending():
    return f"> **{D.PENDING_LANGUAGE}**\n"


def block_compliance_guardrails():
    return f"""\
- **Approval status:** {C['status']}. {D.PENDING_LANGUAGE}
- **No initial certification:** This course is renewal continuing education only. It does **not** grant initial RCFE administrator certification and does **not** replace the administrator certification training program or exam.
- **No CEU/approval claims:** Do not claim CDSS/ACS approval, vendor approval, or CEU eligibility until the applicable approval is issued. "40 CE hours" is **draft design math only**.
- **No PHI / no real residents:** All cases are fictional and de-identified. No protected health information or real resident, staff, or facility data is used anywhere in the course.
- **Scope discipline:** RCFE Administrator renewal CE only. Not BRN/RN Care Manager CE; not CNA recertification. No CNA ContentV2 source material was used.
- **Verify before final:** All regulatory specifics are marked "Needs confirmation" until verified against current CDSS/ACS / Title 22 / Health & Safety Code source materials.
- **Source of truth:** Vendor identity and instructor facts are taken from the Git master application packet at `{PF['source_path']}`. Nothing was invented.
"""


def block_packet_facts_table():
    rows = [
        ("Provider / Vendor (placeholder)", PF["provider_vendor_name"]),
        ("Address", PF["address"]),
        ("Authorized Representative", PF["authorized_representative"]),
        ("Business phone", PF["business_phone"]),
        ("Email", PF["email"]),
        ("Company type", PF["company_type"]),
        ("Business authority", PF["bppe"]),
        ("Program / Vendor type", f"{PF['program_type']} / {PF['vendor_type']}"),
        ("Vendor number", PF["vendor_number"]),
        ("Course number", PF["course_number"]),
        ("Instructor of record", PF["instructor_of_record"]),
        ("Default delivery format", PF["default_format"]),
    ]
    out = "| Field | Value (from master packet) |\n| --- | --- |\n"
    for k, v in rows:
        out += f"| {k} | {v} |\n"
    return out


def block_course_map_table():
    out = ("| ID | Module | CE hrs | Min | Delivery | Dementia | Self-paced | Core knowledge area |\n"
           "| --- | --- | --- | --- | --- | --- | --- | --- |\n")
    for m in D.MODULES:
        out += (f"| {m['id']} | {m['title']} | {m['ce_hours']} | {m['minutes']} | "
                f"{'Self-paced' if m['delivery']=='Self-paced online' else 'Live'} | "
                f"{(str(m['dementia_hours'])+'h') if m['dementia_hours'] else '-'} | "
                f"{'Yes' if m['delivery']=='Self-paced online' else 'No'} | "
                f"{'; '.join(m['core_knowledge'])} |\n")
    out += (f"| **TOTAL** | **12 modules** | **{C['total_hours']}** | **{C['total_minutes']}** | "
            f"**{C['self_paced_planned_hours']}h SP / {C['instructor_interactive_hours']}h live** | "
            f"**{C['dementia_planned_hours']}h** | **{C['self_paced_planned_hours']}h** | All 12 areas |\n")
    return out


def block_hour_calc():
    return f"""\
**40-hour calculation (conservative; 1 CE hour = {C['minutes_per_ce_hour']} minutes of instruction):**

- Total instructional minutes: **{C['total_minutes']} minutes** = {C['total_minutes']}/{C['minutes_per_ce_hour']} = **{C['total_hours']} CE hours**.
- No module is under {C['min_module_minutes']} minutes (smallest modules = 180 minutes / 3 hours).
- Each module documents minutes behind every hour in its lesson table.
"""


def block_self_paced_reconciliation():
    sp = [m for m in D.MODULES if m["delivery"] == "Self-paced online"]
    live = [m for m in D.MODULES if m["delivery"] != "Self-paced online"]
    sp_rows = "\n".join(f"  - {m['id']} {m['title']} - {m['ce_hours']}h" for m in sp)
    live_rows = "\n".join(f"  - {m['id']} {m['title']} - {m['ce_hours']}h" for m in live)
    return f"""\
**Self-paced hour cap reconciliation (no more than one-half / 20 of 40 may be self-paced):**

- Statutory cap: **{C['self_paced_cap_hours']} self-paced hours maximum**.
- Planned self-paced: **{C['self_paced_planned_hours']} hours** (a conservative **{C['self_paced_buffer_hours']}-hour buffer** below the cap).
- Planned live / instructor-interactive: **{C['instructor_interactive_hours']} hours**.
- {C['self_paced_planned_hours']} + {C['instructor_interactive_hours']} = **{C['total_hours']} hours**. Self-paced {C['self_paced_planned_hours']}h <= cap {C['self_paced_cap_hours']}h. **Compliant.**

Self-paced online modules ({C['self_paced_planned_hours']}h):
{sp_rows}

Live / instructor-interactive modules ({C['instructor_interactive_hours']}h) - delivered in an instructional setting where participants interact simultaneously with each other and the instructor (or equivalent approved instructional interaction):
{live_rows}
"""


def block_dementia_calc():
    dm = [m for m in D.MODULES if m["dementia_hours"]]
    rows = "\n".join(f"  - {m['id']} {m['title']} - {m['dementia_hours']}h" for m in dm)
    return f"""\
**Dementia-hour calculation (at least 8 of 40 hours must include dementia instruction covering direct care, physical environment, admissions procedures, and assessment):**

- Required: **>= {C['dementia_required_hours']} dementia hours**. Planned: **{C['dementia_planned_hours']} hours**. **Compliant.**
{rows}
- Required dementia topic coverage:
  - **Direct care:** M08 (Dementia Care I) - communication, ADL support, behavior-as-communication.
  - **Physical environment:** M09-L1 dementia-supportive environment audit.
  - **Admissions procedures:** M09-L3 dementia admissions and disclosures.
  - **Assessment:** M09-L2 dementia-specific assessment.
- Both dementia modules are delivered **live/instructor-interactive** to support skills practice; this does not consume any self-paced hours.
"""


def block_lms_build_plan():
    return f"""\
**Moodle course shell structure** (one course; Topics format; 12 numbered topic sections + intro/orientation + capstone/certificate section):

- **Section 0 - Orientation:** syllabus, no-PHI policy, identity-confirmation setup, how-CE-hours-work, accessibility statement, technical check.
- **Sections 1-12 - Modules M01-M12:** each section contains the module's lessons, knowledge check, assignment(s), and (for live modules) the web-conference activity + attendance.
- **Final section - Certificate & Records:** signed completion statement, gated certificate, course evaluation.

**Sections/topics layout:** one Moodle topic per module; activities ordered exactly as the LMS activity sequence in each blueprint.

**Completion tracking configuration:** enable course + activity completion. Each activity uses explicit completion conditions (view + activity, or passing grade). Module section completion requires all in-section activities complete.

**Restrict access rules:** sequential gating - a module unlocks when the prior module is complete; the **knowledge check** unlocks only after that module's lessons are complete; the **final assessment** unlocks only after all 12 modules + identity confirmation; the **certificate** unlocks only after all gates + signed statement.

**Quiz settings:** knowledge checks = unlimited attempts, immediate per-item feedback, highest grade; final = up to 3 attempts, **{C['pass_threshold_pct']}% pass**, shuffled questions/answers, **no review of correct answers / no answer key shown to learners**, deferred feedback (score + remediation pointer only), secure window, identity confirmation immediately before.

**Attempt settings:** knowledge checks unlimited (mastery); final 3 attempts then mandatory remediation + faculty release.

**Passing threshold:** **{C['pass_threshold_pct']}%** on knowledge checks and on the final.

**Gradebook structure:** category per module (knowledge check + graded assignments) plus a **Final** category and a **Capstone** category; certificate gate reads category completion + final grade.

**Certificate gate conditions:** see Section L. Certificate is **manually/restricted released** and only after approval is issued.

**Activity completion conditions:** view-all + complete-activity for content; passing grade for quizzes; submission (+ manual accept) for assignments and the signed statement; attendance-marked for live sessions.

**Self-paced identity confirmation checkpoints:** PIN/identity attestation at the start of each self-paced module and again immediately before each self-paced knowledge check; logged.

**Signed completion statement workflow:** see Section M.

**Time/participation evidence strategy:** self-paced = activity logs + interactive-activity completion + minimum-time pacing where supported; live = attendance module + web-conference join/leave logs + in-session participation artifacts (polls, breakout, submissions).

**Learner progress dashboard recommendations:** enable the course completion progress block and a learner-facing completion checklist; staff use the Completion report and Gradebook for cohort oversight.

**Live/instructor-interactive session attendance evidence:** Attendance activity + web-conference logs + at least one participation artifact per live session (poll, breakout output, or submitted exercise).

**Mobile-first design notes:** responsive Boost-based theme; all content readable on phone; avoid drag-only interactions without mobile-friendly alternatives; downloadable transcripts; test on small screens.

**Accessibility requirements:** WCAG 2.1 AA; captions + transcripts for all media; keyboard-accessible alternatives for H5P/drag activities; sufficient contrast; screen-reader-friendly structure; extended-time accommodation path on the final.

**No-PHI / no-real-resident-information guardrails:** orientation policy + per-assignment reminder; submission instructions prohibit real identifiers; fictional-only templates; faculty reject any submission containing real PHI.

**Audit evidence export plan:** see Section R / the Audit_Evidence_Log workbook sheet - completion report (CSV/PDF), gradebook export, attendance export, identity-confirmation log, assignment bulk download, signed-statement PDFs, issued-certificate log; retained **{C['completion_record_retention_years']} years**.
"""


def block_assessment_plan():
    return f"""\
1. **Low-stakes module knowledge checks** - one per module; auto-graded; unlimited attempts; immediate per-item feedback; **{C['pass_threshold_pct']}%** to complete the module.
2. **Scenario-based activities** - each module includes a fictional scenario + a documentation/decision exercise graded for applied administrator judgment.
3. **Final cumulative assessment** - 30 items across all modules in M12; **{C['pass_threshold_pct']}% pass**; up to 3 attempts.
4. **Capstone audit-readiness activity** - assemble an audit-ready evidence binder + plan of correction; rubric-scored (see Section K).
5. **Pass threshold** - minimum **{C['pass_threshold_pct']}%** recommended on knowledge checks and final.
6. **Remediation** - after a failed attempt, the learner is routed to the targeted lesson(s) for re-review before re-attempt; after 3 failed final attempts, mandatory faculty-guided remediation before release.
7. **No learner answer key** - learners see their score and remediation pointers only; correct-answer review is disabled on the final.
8. **Internal answer key** - maintained separately for administrator/faculty use (Assessment_Blueprint workbook sheet + module internal answer-key appendices).
9. **Interactive feedback (self-paced)** - branching Lesson/H5P provide input-based feedback in every self-paced module.
10. **Identity confirmation (self-paced)** - PIN/identity checkpoints in every self-paced module and before each self-paced knowledge check.
"""


def block_final_blueprint():
    out = f"""\
- **Format:** 30 multiple-choice/scenario items sampling all 12 modules (weighted toward higher-hour modules and the 8 dementia hours).
- **Pass standard:** **{C['pass_threshold_pct']}%**; up to 3 attempts; shuffled; secure; identity-confirmed; deferred feedback (score + remediation, **no answer key**).
- **Blueprint coverage (target item counts - Needs confirmation / SME finalization):**

| Module | Target items | Emphasis |
| --- | --- | --- |
"""
    weights = {"M01": 3, "M02": 2, "M03": 2, "M04": 2, "M05": 2, "M06": 3,
               "M07": 3, "M08": 4, "M09": 4, "M10": 3, "M11": 2, "M12": 0}
    for m in D.MODULES:
        emph = "Dementia (required topic)" if m["dementia_hours"] else m["core_knowledge"][0]
        out += f"| {m['id']} | {weights.get(m['id'],0)} | {emph} |\n"
    out += "| **Total** | **30** | Dementia-weighted; full bank pending SME authoring |\n\n"
    out += "Sample final items (full internal key kept separate):\n\n"
    for it in D.FINAL_ASSESSMENT_ITEMS:
        out += f"- **{it['id']} ({it['module']}):** {it['stem']}\n  - {it['choices']}\n  - *Internal key:* {it['answer']} - {it['rationale']}\n"
    return out


def block_capstone():
    out = "Capstone = live audit-readiness simulation + cumulative final (M12). Rubric-scored tasks:\n\n"
    out += "| Task | Scenario | Deliverable | Rubric criterion | Passing standard |\n| --- | --- | --- | --- | --- |\n"
    for c in D.CAPSTONE_TASKS:
        out += f"| {c['id']} | {c['scenario']} | {c['deliverable']} | {c['rubric']} | {c['passing']} |\n"
    out += ("\n- **Resident privacy:** all capstone work uses fictional, de-identified facilities/residents; "
            "real identifiers are prohibited and rejected.\n"
            "- **Evidence:** submitted binder index, plan of correction, dementia evidence map, and personal action plan, "
            "each rubric-graded in the gradebook.\n")
    return out


def block_certificate_gate():
    out = "A learner certificate is released only when **every** gate below is satisfied (and only after CDSS/ACS approval is issued):\n\n"
    out += "| Gate | Required condition | LMS evidence source | Manual review | Risk if omitted |\n| --- | --- | --- | --- | --- |\n"
    for g in D.CERTIFICATE_GATE:
        out += f"| {g['gate']} | {g['condition']} | {g['source']} | {g['manual']} | {g['risk']} |\n"
    return out


def block_signed_statement_workflow():
    return f"""\
**Signed completion statement workflow** (required for self-paced online CE; applied course-wide for consistency):

1. Learner completes all modules, the final assessment (**>= {C['pass_threshold_pct']}%**), and identity confirmation.
2. The LMS unlocks a **final printable completion statement** pre-filled with learner name, course title, completion date, delivery mode, and draft CE hours (placeholder until approval).
3. The learner **signs** the statement (wet-signature upload or compliant e-signature), **certifying completion**.
4. Compliance/faculty **reviews and accepts** the signed statement.
5. Only then is the **certificate released**.
6. The signed statement is **retained by the vendor for {C['completion_record_retention_years']} years** and is exportable for audit.

**Draft completion-statement text:**

> I, ________________________ (participant), certify that I personally completed all required components of "{C['title']}" ({C['total_hours']} CE hours, draft - pending CDSS/ACS approval), including the interactive activities and the final assessment, and that the identity information/PIN I provided is my own.
> Participant signature: ____________________  Date: __________
> Identity confirmation reference: __________
> {D.PENDING_LANGUAGE}
"""


def block_recordkeeping():
    out = f"""\
**Recordkeeping & retention model:** all completion evidence retained **{C['completion_record_retention_years']} years** (signed completion statements must be obtained **before** certificate issuance and retained {C['completion_record_retention_years']} years).

**Audit evidence log:**

| Evidence item | Generated by | Stored where | Retention | Review | Export |
| --- | --- | --- | --- | --- | --- |
"""
    for e in D.AUDIT_EVIDENCE_LOG:
        out += f"| {e['item']} | {e['by']} | {e['where']} | {e['retention']} | {e['review']} | {e['export']} |\n"
    return out


def block_flyer():
    sp = C["self_paced_planned_hours"]; live = C["instructor_interactive_hours"]
    return f"""\
**DRAFT - Pending CDSS/ACS Approval**

**{C['title']}**

- **Audience:** {C['audience']}.
- **Course description:** A comprehensive {C['total_hours']}-hour continuing education program for California RCFE Administrators renewing their certificate. Covers RCFE laws and regulations, business operations, staff supervision, resident psychosocial and physical needs, medication oversight, admission/retention, **dementia care (8 hours)**, residents' rights and abuse prevention, the physical environment and emergency preparedness, and an integrated audit-readiness capstone.
- **Learning objectives (summary):** apply current RCFE regulatory requirements; strengthen operations, records, and staff oversight; deliver person-centered and dementia-capable care; manage medications and resident rights safely; and demonstrate audit readiness.
- **Draft CE hours:** {C['total_hours']} CE hours *(draft design math; not yet approved)*.
- **Delivery method:** blended - **{sp} hours self-paced online** + **{live} hours live/instructor-interactive**.
- **Self-paced / instructor-interactive split:** {sp}h self-paced (within the {C['self_paced_cap_hours']}h cap) / {live}h live.
- **Dementia-hour statement:** includes **8 hours of dementia instruction** covering direct care, physical environment, admissions procedures, and assessment.
- **Completion requirements:** complete all modules and interactive activities; pass each knowledge check and the final at **>= {C['pass_threshold_pct']}%**; confirm identity (self-paced); sign the completion statement.
- **Refund/cancellation policy:** *[Placeholder - business decision pending; fees TBD.]*
- **This course does NOT** grant initial RCFE administrator certification and does **not** replace the certification training program or exam. It does not expand administrator scope of practice.
- **Privacy:** all examples are fictional and de-identified; **no PHI or real resident information**.

> {D.PENDING_LANGUAGE}
"""


def block_certificate():
    return f"""\
**DRAFT CERTIFICATE TEXT - Pending CDSS/ACS Approval (placeholders only)**

> **Certificate of Completion**
>
> This certifies that
> **____________________________** (Learner Name)
> has completed
> **{C['title']}**
> Completion date: **__________**
> Provider/Vendor: **{PF['provider_vendor_name']}** *(vendor approval pending)*
> Vendor number: **{PF['vendor_number']}**
> Course/Approval number: **{PF['course_number']}**
> CE hours: **{{CE_HOURS_PLACEHOLDER}}** *(draft {C['total_hours']} hours; not valid until approved)*
> Delivery mode: **Blended - {C['self_paced_planned_hours']}h self-paced online / {C['instructor_interactive_hours']}h live-interactive**
> Authorized signature: ____________________  Title: ________________
>
> *{D.PENDING_LANGUAGE}*

(No real provider/vendor/course number is used; the values above are placeholders from the master packet and are not valid CE identifiers until approval is issued.)
"""


def block_evaluation_form():
    return """\
**Course Evaluation Form (Participant) - Draft**

Rate 1 (strongly disagree) to 5 (strongly agree):

1. The stated learning objectives were met.
2. The content was relevant to my role as an RCFE administrator.
3. The dementia-care content (direct care, environment, admissions, assessment) was useful.
4. The self-paced modules were clear and the interactive feedback was helpful.
5. The live/instructor-interactive sessions allowed real interaction with the instructor and peers.
6. The assessments fairly measured the objectives.
7. The LMS was easy to use (including on mobile) and accessible.
8. The instructor/facilitator was knowledgeable and effective.

Open response:
- What was most valuable?
- What should be improved?
- What additional RCFE topics would you want in future CE?
- Did you encounter any accessibility barriers? (If yes, describe.)

Administrative:
- Delivery mode taken (self-paced / live / both): ______
- Estimated time to complete: ______
"""


def block_advertising_checklist():
    return """\
**Advertising compliance checklist (pre-approval):**

- [ ] All materials marked "Draft - Pending CDSS/ACS Approval".
- [ ] No claim of CDSS/ACS approval, vendor approval, or CEU eligibility.
- [ ] CE hours presented as draft design math only (no "approved for X hours").
- [ ] No statement implying initial certification or scope expansion.
- [ ] No real vendor/course/approval numbers used.
- [ ] No PHI or real resident/staff/facility data in any promotional example.
- [ ] Refund/cancellation policy present (placeholder acceptable pre-launch).
- [ ] Self-paced cap and dementia-hour statements accurate.
"""


def block_open_items():
    return f"""\
Items requiring confirmation/sign-off **before** submission or launch:

- **CDSS/ACS requirement verification:** confirm current RCFE renewal CE rules (40h; <=20 self-paced; >=8 dementia; self-paced interactivity/identity/signed-statement; recordkeeping) against current official source. *(Needs confirmation.)*
- **Core-of-knowledge wording:** confirm exact uniform-core-of-knowledge area names/categories. *(Needs confirmation.)*
- **Regulatory specifics:** Title 22 citation numbers, civil penalty amounts, restricted-condition list, hospice waiver, mandated-reporting timelines, eviction notice periods, emergency-plan elements, LGBT cultural-competency requirements - verify each. *(Needs confirmation.)*
- **Assessment bank:** author and SME-review the full knowledge-check and 30-item final bank (only samples provided). *(Open.)*
- **Proctoring/identity standard:** confirm acceptable identity/proctoring approach for the self-paced and final assessment. *(Needs confirmation.)*
- **Fees & refund policy:** business decision on participant fees and refund/cancellation terms. *(Open - placeholder.)*
- **Vendor/course numbers:** assigned only after approval; keep placeholders until issued. *(Pending approval.)*
- **Instructor evidence:** confirm/attach instructor qualification evidence ({PF['instructor_of_record']}) per master packet instructor evidence index. *(Final verification.)*
- **Reviewer LMS access:** prepare reviewer log-on credentials for course review. *(Final verification.)*
- **SME + compliance sign-off:** dementia/medication clinical content (RN SME) and full compliance review. *(Open.)*
- **Owner approval:** final owner/authorized-representative sign-off. *(Open.)*
"""


def block_compliance_checklist():
    return f"""\
- [ ] 40 CE hours reconciled ({C['total_minutes']} min / {C['minutes_per_ce_hour']}).
- [ ] Self-paced <= {C['self_paced_cap_hours']}h (planned {C['self_paced_planned_hours']}h).
- [ ] Dementia >= {C['dementia_required_hours']}h (planned {C['dementia_planned_hours']}h) covering direct care, environment, admissions, assessment.
- [ ] No module under {C['min_module_minutes']} minutes.
- [ ] Self-paced modules: interactive feedback present.
- [ ] Self-paced modules: identity confirmation present.
- [ ] Signed completion statement workflow before certificate; {C['completion_record_retention_years']}-year retention.
- [ ] Final pass threshold {C['pass_threshold_pct']}%; no learner answer key; internal key separated.
- [ ] No PHI / fictional cases only.
- [ ] No initial-certification or scope-expansion claims.
- [ ] No approval/CEU claims; "Draft - Pending CDSS/ACS Approval" on all artifacts.
- [ ] Live modules: simultaneous-interaction attendance evidence captured.
"""


def block_sme_checklist():
    return """\
- [ ] Regulatory accuracy verified vs current CDSS/Title 22/HSC source (all modules).
- [ ] Dementia content (M08-M09) reviewed by dementia/RN SME for accuracy and currency.
- [ ] Medication content (M06) reviewed by RN SME; kept at administrator-oversight level.
- [ ] Restricted-conditions/hospice content (M05) reviewed for scope accuracy.
- [ ] Mandated-reporting and LGBT cultural-competency content (M10) reviewed for current requirements.
- [ ] Assessment items reviewed for validity, fairness, and key accuracy.
- [ ] Scenarios confirmed fictional/de-identified (no PHI).
- [ ] Accessibility reviewed (WCAG 2.1 AA).
- [ ] Hour math and delivery-mode classifications confirmed.
"""


def block_owner_checklist():
    return """\
- [ ] Owner/authorized representative reviewed full package.
- [ ] SME sign-off received.
- [ ] Compliance sign-off received.
- [ ] Vendor identity confirmed against master packet.
- [ ] Instructor evidence attached/verified.
- [ ] Reviewer LMS access prepared.
- [ ] Fees/refund policy decided.
- [ ] All "Needs confirmation" items resolved or documented.
- [ ] Confirmed: do NOT advertise/issue certificates/claim approval until approval issued.
- [ ] Approved to assemble for CDSS/ACS submission.
"""


def block_xlsx_plan():
    sheets = ["Course_Map", "Module_Blueprints", "Core_Knowledge_Map", "Dementia_Hour_Map",
              "Delivery_Mode_Map", "LMS_Activity_Map", "Assessment_Blueprint", "Capstone_Map",
              "Application_Packet_Checklist", "Certificate_Gate", "SME_Compliance_Flags", "Audit_Evidence_Log"]
    out = ("Supporting workbook **`RCFE_Admin_CE_LMS_BUILD_WORKBOOK.xlsx`** (build-support/defensibility artifact only; "
           "the markdown package remains the primary deliverable). Generated from the same single source "
           "(`_build/rcfe_ce_data.py`). Sheets:\n\n")
    for i, s in enumerate(sheets, 1):
        out += f"{i}. `{s}`\n"
    out += "\nRegenerate with: `python _build/build_workbook.py`\n"
    return out


def block_pdf_packet_plan():
    out = ("PDF-ready Markdown is in **`/pdf-ready/`** (no PDF engine was available in the build environment, "
           "so per the task fallback, clean PDF-ready Markdown was generated with the exact target file names "
           "and conversion instructions). Files:\n\n")
    out += "- `RCFE_Admin_CE_40HR_Course_Documentation_Packet.md` -> `...pdf`\n"
    for m in D.MODULES:
        out += f"- `{PDF_FILENAMES[m['id']]}.md` -> `{PDF_FILENAMES[m['id']]}.pdf`\n"
    out += "\nSee `/pdf-ready/CONVERSION_INSTRUCTIONS.md` for the exact pandoc commands.\n"
    return out


# --------------------------------------------------------------------------
# Module rendering (used by primary Section G and by per-module PDF docs)
# --------------------------------------------------------------------------
def render_lesson_table(m):
    out = "| Lesson | Title | Min | Objective | Activity type | Moodle | Completion |\n| --- | --- | --- | --- | --- | --- | --- |\n"
    for l in m["lessons"]:
        out += f"| {l['id']} | {l['title']} | {l['minutes']} | {l['objective']} | {l['activity_type']} | {l['moodle']} | {l['completion']} |\n"
    return out


def render_knowledge_items(m, internal=True):
    kc = m["knowledge_check"]
    out = f"_{kc['blueprint']}_\n\n"
    for i, it in enumerate(kc["items"], 1):
        out += f"**Sample item {i} ({it['type']}):** {it['stem']}\n\n"
        for ch in it["choices"]:
            out += f"- {ch}\n"
        if internal:
            out += f"\n*Internal key:* **{it['answer']}** - {it['rationale']}\n*Remediation:* {it['remediation']}\n\n"
        else:
            out += "\n*(Answer key withheld from learners; see internal key appendix.)*\n\n"
    return out


def render_module_blueprint(m, heading="###"):
    """Compact blueprint for the primary package Section G."""
    dem = f"{m['dementia_hours']}h" if m["dementia_hours"] else "None"
    out = f"""{heading} {m['id']} - {m['title']}

- **CE hours / minutes:** {m['ce_hours']}h / {m['minutes']} min
- **Delivery mode:** {m['delivery']}
- **RCFE core knowledge:** {'; '.join(m['core_knowledge'])}
- **Dementia-hour mapping:** {dem}
- **Compliance rationale:** {m['compliance_rationale']}

**Description:** {m['description']}

**Measurable learning objectives:**
"""
    for o in m["objectives"]:
        out += f"- {o}\n"
    out += "\n**Lesson breakdown / LMS activity sequence:**\n\n" + render_lesson_table(m)
    out += f"\n**Knowledge checks:**\n\n{render_knowledge_items(m, internal=True)}"
    out += f"**Case scenario (fictional/de-identified):** {m['scenario']}\n\n"
    out += f"**Documentation/decision exercise:** {m['doc_exercise']}\n\n"
    out += f"**Completion requirement:** {m['completion_requirement']}\n\n"
    out += f"**Evidence artifact:** {m['evidence_artifact']}\n\n"
    out += f"**Suggested Moodle activity types:** {', '.join(m['moodle_activities'])}\n\n"
    if m["delivery"] == "Self-paced online":
        out += f"**Interactive feedback (self-paced):** {m['interactive_feedback']}\n\n"
        out += f"**Identity confirmation (self-paced):** {m['identity_confirmation']}\n\n"
    out += f"**SME review flags:** {'; '.join(m['sme_flags'])}\n\n"
    out += f"**Compliance review flags:** {'; '.join(m['compliance_flags'])}\n\n"
    out += f"**PHI/resident-privacy notes:** {m['privacy_notes']}\n\n"
    out += "**Accessibility notes:** " + "; ".join(m["accessibility"]) + "\n\n"
    out += f"**Application-packet defensibility:** {m['defensibility_notes']}\n"
    return out


def render_module_pdf(m):
    """Full-depth per-module PDF-ready document (CCCCO-style organization)."""
    dem = f"{m['dementia_hours']}h" if m["dementia_hours"] else "Not applicable"
    out = f"""# {D.DRAFT_BANNER}

# {m['id']} - {m['title']}

{block_pending()}
## Module identification

| Field | Value |
| --- | --- |
| Module ID | {m['id']} |
| Module title | {m['title']} |
| CE hours | {m['ce_hours']} |
| Estimated learner minutes | {m['minutes']} |
| Delivery mode | {m['delivery']} |
| RCFE core knowledge mapping | {'; '.join(m['core_knowledge'])} |
| Dementia-hour mapping | {dem} |
| Provider/Vendor (placeholder) | {PF['provider_vendor_name']} |
| Instructor of record | {PF['instructor_of_record']} |
| Approval status | {C['status']} |

## Module description

{m['description']}

## Measurable learning objectives

"""
    for o in m["objectives"]:
        out += f"- {o}\n"
    out += "\n## Required readings / learning content sections\n\n"
    for l in m["lessons"]:
        out += f"- **{l['id']} - {l['title']}** ({l['minutes']} min): {l['summary']}\n"
    out += "\n## Detailed lesson outline\n\n" + render_lesson_table(m)
    out += "\n## Key terms\n\n" + ", ".join(m["key_terms"]) + "\n"
    out += f"\n## Fictional / de-identified scenario\n\n{m['scenario']}\n"
    out += "\n## Learner activities\n\n"
    for a in m["activities"]:
        out += f"- {a}\n"
    out += f"\n## Documentation / decision-making exercise\n\n{m['doc_exercise']}\n"
    out += "\n## Knowledge check blueprint & assessment items\n\n" + render_knowledge_items(m, internal=False)
    out += "## Internal answer key appendix (faculty/admin only - do NOT show learners)\n\n"
    for i, it in enumerate(m["knowledge_check"]["items"], 1):
        out += f"- Item {i}: **{it['answer']}** - {it['rationale']} (Remediation: {it['remediation']})\n"
    out += "\n## Debrief / remediation guidance\n\n"
    out += (f"- Provide per-item feedback on submission; route failed attempts to the targeted lesson before re-attempt.\n"
            f"- Knowledge check requires **>= {C['pass_threshold_pct']}%** to complete the module.\n"
            f"- For live modules, debrief activities/role-play immediately with instructor feedback.\n")
    out += f"\n## LMS completion criteria\n\n{m['completion_requirement']}\n"
    out += f"\n## Evidence generated by learner completion\n\n{m['evidence_artifact']}\n"
    out += "\n## Moodle activity recommendations\n\n" + ", ".join(m["moodle_activities"]) + "\n"
    if m["delivery"] == "Self-paced online":
        out += f"\n**Self-paced interactive feedback:** {m['interactive_feedback']}\n"
        out += f"\n**Self-paced identity confirmation:** {m['identity_confirmation']}\n"
    else:
        out += f"\n**Live interaction / identity:** {m['interactive_feedback']} Identity: {m['identity_confirmation']}\n"
    out += "\n## Accessibility considerations\n\n"
    for a in m["accessibility"]:
        out += f"- {a}\n"
    out += f"\n## Resident privacy guardrails\n\n{m['privacy_notes']}\n"
    out += "\n## SME review flags\n\n"
    for f in m["sme_flags"]:
        out += f"- {f}\n"
    out += "\n## Compliance review flags\n\n"
    for f in m["compliance_flags"]:
        out += f"- {f}\n"
    out += f"\n## Application-packet defensibility notes\n\n{m['defensibility_notes']}\n"
    out += f"\n---\n\n_{D.CLOSING_LANGUAGE}_\n"
    return out


# --------------------------------------------------------------------------
# Primary package (Sections A-X)
# --------------------------------------------------------------------------
def build_primary():
    p = []
    p.append(f"# {D.DRAFT_BANNER}\n")
    p.append(block_pending())
    p.append("**Primary deliverable: complete LMS-ready RCFE Administrator renewal CE course package.** "
             "Supporting artifacts: `RCFE_Admin_CE_LMS_BUILD_WORKBOOK.xlsx` and `/pdf-ready/` documentation.\n")
    # TOC
    secs = ["A. Executive Summary", "B. Compliance Guardrails", "C. RCFE Core Knowledge Fit Rationale",
            "D. 40-Hour Course Map", "E. Self-Paced Hour Cap Reconciliation", "F. Dementia-Hour Mapping",
            "G. Detailed Module Blueprints", "H. LMS/Moodle Build Plan", "I. Assessment Plan",
            "J. Final Assessment Blueprint", "K. Capstone Activity Blueprint",
            "L. Certificate Gate and Completion Logic", "M. Signed Completion Statement Workflow",
            "N. Draft Course/Application Support Content", "O. Draft Flyer/Brochure Copy",
            "P. Draft Certificate Text", "Q. Course Evaluation Form",
            "R. Recordkeeping and Audit Evidence Plan", "S. Supporting XLSX Workbook Plan",
            "T. PDF-Ready Module Documentation Packet", "U. Compliance Review Checklist",
            "V. SME Review Checklist", "W. Open Questions / Missing Packet Items",
            "X. Final Build Handoff Checklist"]
    p.append("## Contents\n\n" + "\n".join(f"- {s}" for s in secs) + "\n")

    # A
    p.append(f"""## A. Executive Summary

**{C['title']}** is a draft, application-stage **{C['total_hours']}-hour** continuing education package for **{C['audience']}**. It is organized into **12 LMS modules** designed for Moodle, blending **{C['self_paced_planned_hours']} hours of self-paced online** instruction with **{C['instructor_interactive_hours']} hours of live/instructor-interactive** instruction, and includes **{C['dementia_planned_hours']} hours of dementia content**.

This package reconciles the three controlling RCFE renewal CE constraints: **40 total hours**, **no more than 20 self-paced hours** (planned at {C['self_paced_planned_hours']}h, a {C['self_paced_buffer_hours']}h conservative buffer), and **at least 8 dementia hours** (planned at {C['dementia_planned_hours']}h, covering direct care, physical environment, admissions, and assessment). Vendor identity and instructor facts are drawn from the Git master application packet (`{PF['source_path']}`); nothing was invented.

Status: **{C['status']}**. This is renewal CE only - it does not grant initial administrator certification and does not replace the certification training program or exam. All scenarios are fictional and de-identified.
""")
    # B
    p.append("## B. Compliance Guardrails\n\n" + block_compliance_guardrails())
    p.append("**Packet facts used (source of truth):**\n\n" + block_packet_facts_table())
    # C
    p.append("## C. RCFE Core Knowledge Fit Rationale\n\n"
             "Every module maps to one or more RCFE administrator uniform core-of-knowledge areas "
             "(area wording: *Needs confirmation* against current CDSS/ACS source). Coverage:\n\n")
    ck = "| Core knowledge area | Covered by |\n| --- | --- |\n"
    for area in D.CORE_KNOWLEDGE_AREAS:
        cov = ", ".join(m["id"] for m in D.MODULES if area in m["core_knowledge"]) or "Needs confirmation"
        ck += f"| {area} | {cov} |\n"
    p.append(ck + "\nThe sequence moves from regulatory/operational foundations (M01-M03), to resident-centered "
             "and clinical-oversight content (M04-M07), to the required dementia block (M08-M09), to rights/safety "
             "(M10-M11), and finally to an integrative capstone and assessment (M12).\n")
    # D
    p.append("## D. 40-Hour Course Map\n\n" + block_course_map_table() + "\n" + block_hour_calc())
    # E
    p.append("## E. Self-Paced Hour Cap Reconciliation\n\n" + block_self_paced_reconciliation())
    # F
    p.append("## F. Dementia-Hour Mapping\n\n" + block_dementia_calc())
    # G
    p.append("## G. Detailed Module Blueprints\n\n"
             "_Full-depth, PDF-ready versions of each module are in `/pdf-ready/`. Compact blueprints below._\n")
    for m in D.MODULES:
        p.append(render_module_blueprint(m, heading="###"))
    # H
    p.append("## H. LMS/Moodle Build Plan\n\n" + block_lms_build_plan())
    # I
    p.append("## I. Assessment Plan\n\n" + block_assessment_plan())
    # J
    p.append("## J. Final Assessment Blueprint\n\n" + block_final_blueprint())
    # K
    p.append("## K. Capstone Activity Blueprint\n\n" + block_capstone())
    # L
    p.append("## L. Certificate Gate and Completion Logic\n\n" + block_certificate_gate())
    # M
    p.append("## M. Signed Completion Statement Workflow\n\n" + block_signed_statement_workflow())
    # N
    p.append("## N. Draft Course/Application Support Content\n\n"
             "Draft application-packet support content (full versions in `/pdf-ready/` and the workbook):\n\n"
             "**Course outline:** the 12-module map in Section D, each module expanded in Section G.\n\n"
             "**Course objectives:** the measurable objectives listed per module in Section G.\n\n"
             "**Hour allocation table:** Section D / `Course_Map` sheet.\n\n"
             "**Dementia-hour mapping table:** Section F / `Dementia_Hour_Map` sheet.\n\n"
             "**Self-paced vs instructor-interactive table:** Section E / `Delivery_Mode_Map` sheet.\n\n"
             "**Attendance/completion/proof-of-participation policy:** Section R + certificate gate (Section L).\n\n"
             "**Refund/cancellation policy placeholder:** *[Placeholder - fees and refund terms are a pending business decision.]*\n\n"
             + block_advertising_checklist())
    # O
    p.append("## O. Draft Flyer/Brochure Copy\n\n" + block_flyer())
    # P
    p.append("## P. Draft Certificate Text\n\n" + block_certificate())
    # Q
    p.append("## Q. Course Evaluation Form\n\n" + block_evaluation_form())
    # R
    p.append("## R. Recordkeeping and Audit Evidence Plan\n\n" + block_recordkeeping())
    # S
    p.append("## S. Supporting XLSX Workbook Plan\n\n" + block_xlsx_plan())
    # T
    p.append("## T. PDF-Ready Module Documentation Packet\n\n" + block_pdf_packet_plan())
    # U
    p.append("## U. Compliance Review Checklist\n\n" + block_compliance_checklist())
    # V
    p.append("## V. SME Review Checklist\n\n" + block_sme_checklist())
    # W
    p.append("## W. Open Questions / Missing Packet Items\n\n" + block_open_items())
    # X
    p.append("## X. Final Build Handoff Checklist\n\n" + block_owner_checklist())

    p.append(f"\n---\n\n**{D.CLOSING_LANGUAGE}**\n")
    return "\n".join(p)


# --------------------------------------------------------------------------
# Full course documentation packet (PDF-ready)
# --------------------------------------------------------------------------
def build_full_packet():
    p = []
    p.append(f"# {D.DRAFT_BANNER}\n")
    p.append("# Full Course Documentation Packet\n")
    p.append(f"## {C['title']}\n")
    p.append(block_pending())
    p.append("## Course overview\n\n"
             f"A {C['total_hours']}-hour RCFE Administrator renewal continuing education course for "
             f"{C['audience']}, organized into 12 Moodle modules ({C['self_paced_planned_hours']}h self-paced + "
             f"{C['instructor_interactive_hours']}h live), including {C['dementia_planned_hours']} dementia hours. "
             f"Provider/vendor (placeholder): {PF['provider_vendor_name']}; instructor of record: {PF['instructor_of_record']}. "
             f"Status: {C['status']}.\n")
    p.append("## 40-hour calculation\n\n" + block_hour_calc())
    p.append("## Self-paced hour cap reconciliation\n\n" + block_self_paced_reconciliation())
    p.append("## Dementia-hour calculation\n\n" + block_dementia_calc())
    p.append("## Module sequence\n\n" + block_course_map_table())
    p.append("## RCFE core knowledge fit rationale\n\n")
    ck = "| Core knowledge area | Covered by |\n| --- | --- |\n"
    for area in D.CORE_KNOWLEDGE_AREAS:
        cov = ", ".join(m["id"] for m in D.MODULES if area in m["core_knowledge"]) or "Needs confirmation"
        ck += f"| {area} | {cov} |\n"
    p.append(ck)
    p.append("## LMS delivery model\n\n" + block_lms_build_plan())
    p.append("## Assessment strategy\n\n" + block_assessment_plan() + "\n### Final assessment blueprint\n\n" + block_final_blueprint())
    p.append("## Certificate gate logic\n\n" + block_certificate_gate())
    p.append("## Signed completion statement workflow\n\n" + block_signed_statement_workflow())
    p.append("## Completion / evidence model\n\n" + block_recordkeeping())
    p.append("## Recordkeeping model\n\n"
             f"All completion evidence is retained for **{C['completion_record_retention_years']} years**. "
             "Signed completion statements are obtained **before** certificate issuance and retained for "
             f"{C['completion_record_retention_years']} years. Records are stored in the LMS and exported per the audit-evidence log above.\n")
    p.append("## No-PHI / no-real-resident-information policy\n\n"
             "All cases, residents, staff, and facilities in this course are **fictional and de-identified**. "
             "No protected health information or real resident/staff/facility data may be entered by learners or staff. "
             "Submission instructions prohibit real identifiers; faculty reject any submission containing real PHI. "
             "Sample license numbers are obviously fake (e.g., 00-FAKE-001).\n")
    p.append("## Draft flyer/brochure copy\n\n" + block_flyer())
    p.append("## Draft certificate text\n\n" + block_certificate())
    p.append("## Course evaluation form\n\n" + block_evaluation_form())
    p.append("## SME/compliance checklist\n\n### Compliance review checklist\n\n" + block_compliance_checklist()
             + "\n### SME review checklist\n\n" + block_sme_checklist())
    p.append("## Capstone activity blueprint\n\n" + block_capstone())
    p.append("## Module documentation index\n\n"
             "Full per-module PDF-ready documentation:\n\n" +
             "".join(f"- `{PDF_FILENAMES[m['id']]}.md` - {m['id']} {m['title']}\n" for m in D.MODULES))
    p.append("## Open items requiring confirmation before submission\n\n" + block_open_items())
    p.append(f"\n---\n\n**{D.CLOSING_LANGUAGE}**\n")
    return "\n".join(p)


def build_conversion_instructions():
    lines = [m["id"] for m in D.MODULES]
    files = ["RCFE_Admin_CE_40HR_Course_Documentation_Packet"] + [PDF_FILENAMES[m["id"]] for m in D.MODULES]
    cmds = "\n".join(f"pandoc \"{f}.md\" -o \"{f}.pdf\"" for f in files)
    return f"""# PDF Conversion Instructions

{D.DRAFT_BANNER}

No PDF engine (xelatex/pdflatex/wkhtmltopdf/weasyprint/typst) was available in the build
environment, so per the task's fallback these PDF-ready Markdown files were generated with the
**exact target file names**. Convert them to PDF with any of the methods below.

## Files to convert

- `RCFE_Admin_CE_40HR_Course_Documentation_Packet.md` -> `RCFE_Admin_CE_40HR_Course_Documentation_Packet.pdf`
""" + "".join(f"- `{PDF_FILENAMES[m['id']]}.md` -> `{PDF_FILENAMES[m['id']]}.pdf`\n" for m in D.MODULES) + f"""

## Option A - Pandoc + a LaTeX engine (best fidelity)

1. Install a LaTeX engine (e.g., MiKTeX on Windows, or TeX Live), which provides `xelatex`.
2. From this `/pdf-ready/` folder run:

```
{cmds}
```

(Add `--toc -V geometry:margin=1in` for a table of contents and margins.)

## Option B - Pandoc + wkhtmltopdf (HTML engine, no LaTeX)

1. Install `wkhtmltopdf` and ensure it is on PATH.
2. Run, for each file: `pandoc "FILE.md" -t html5 -o "FILE.pdf" --pdf-engine=wkhtmltopdf`

## Option C - VS Code / editor extension

Use a "Markdown PDF" extension (e.g., yzane.markdown-pdf) and export each `.md` to `.pdf`.

## Option D - Word intermediate

`pandoc "FILE.md" -o "FILE.docx"` then "Save as PDF" from Word.

_{D.CLOSING_LANGUAGE}_
"""


def main():
    # Primary package
    primary_path = os.path.join(BASE, "RCFE_Admin_Renewal_CE_Course_Package.md")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(build_primary())
    print("Wrote", primary_path)

    # Full PDF-ready packet
    full_path = os.path.join(PDF, "RCFE_Admin_CE_40HR_Course_Documentation_Packet.md")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(build_full_packet())
    print("Wrote", full_path)

    # Per-module PDF-ready docs
    for m in D.MODULES:
        path = os.path.join(PDF, PDF_FILENAMES[m["id"]] + ".md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(render_module_pdf(m))
        print("Wrote", path)

    # Conversion instructions
    conv_path = os.path.join(PDF, "CONVERSION_INSTRUCTIONS.md")
    with open(conv_path, "w", encoding="utf-8") as f:
        f.write(build_conversion_instructions())
    print("Wrote", conv_path)


if __name__ == "__main__":
    main()
