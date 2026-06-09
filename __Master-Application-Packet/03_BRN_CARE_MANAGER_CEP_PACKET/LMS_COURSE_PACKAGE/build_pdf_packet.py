"""
Build the PDF-ready BRN Case Management CE module documentation packet.

Single-sources all content, writes clean PDF-ready Markdown into ./pdf-ready/
(exact requested base names), and renders matching PDFs via reportlab (md2pdf).

CCCCO-style ORGANIZATION only (structured overview, objectives, content outline,
activities, facilitator notes, assessment mapping, compliance support). No CCCCO
content is copied.

Status: Draft / Pending BRN CEP Approval. No CEP number issued.

Usage: python build_pdf_packet.py
"""

import os
from md2pdf import markdown_to_pdf

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "pdf-ready")
os.makedirs(OUT, exist_ok=True)

PROVIDER = ("**Provider (from master packet):** CI Institute of Nursing, Inc. — "
            "419 E. Hamilton Ave., Campbell, CA 95008 — 650-449-6706 — "
            "humanresources@ci-ion.com — https://www.ci-ion.com")
COURSE = ("RN Case Management in Home Health: Care Coordination, Documentation, "
          "Patient Advocacy, and Safe Transitions of Care")
PLACEHOLDER = ('"Pending California Board of Registered Nursing Continuing Education '
               'Provider approval. Do not advertise, issue certificates, or represent '
               'this course as approved until a BRN CEP number has been issued."')
BANNER = "# BRN Case Management CE Package - Draft / Pending BRN CEP Approval"
FOOTER = ("*Do not advertise, issue certificates, or represent this course as "
          "BRN-approved until the official BRN CEP approval and provider number are issued.*")

DOC_MODEL_NOTE = ("This document follows a CCCCO-style documentation *organization* only "
                  "(structured overview, objectives, content outline, activities, facilitator "
                  "notes, assessment mapping, compliance support). No CCCCO content is copied; "
                  "all content is original and customized for California BRN Case Management CE.")


def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join(["---"] * len(headers)) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


# --------------------------------------------------------------------------- DATA
MODULES = [
    {
        "id": "CM-M01", "num": "01",
        "file": "BRN_CM_M01_Foundations_of_RN_Case_Management",
        "title": "Foundations of RN Case Management and Nursing Scope",
        "hours": 3, "minutes": 165, "linkage": "Indirect patient/client care",
        "rationale": ("Establishes the RN scope-of-practice and role boundaries that make "
                      "nurse-led case management safe and lawful, framing case management as a "
                      "function within registered-nursing practice rather than a separate license."),
        "description": ("Orients the RN to the definition, purpose, and process of nurse-led case "
                        "management; differentiates it from social work and unlicensed coordination; "
                        "and fixes the scope boundaries and escalation duties that govern every later "
                        "module."),
        "objectives": [
            "Define RN case management and distinguish it from social work and unlicensed care coordination using BRN scope language.",
            "Identify three RN scope-of-practice boundaries that constrain case-management decisions.",
            "Describe how care coordination qualifies as direct/indirect patient care under nursing practice.",
            "Recognize when a case-management task must be escalated to a licensed prescriber or RN supervisor.",
        ],
        "content_sections": [
            "Reading 1.1 - Definition and purpose of RN case management.",
            "Reading 1.2 - California RN scope of practice and legal boundaries (overview; not legal advice).",
            "Reading 1.3 - Care-team roles: RN vs. social worker vs. unlicensed staff.",
            "Reading 1.4 - The case-management process model and escalation duties.",
        ],
        "lessons": [
            ("CM-M01-L1", "What RN case management is (and is not)", 35),
            ("CM-M01-L2", "Nursing scope of practice and legal boundaries", 40),
            ("CM-M01-L3", "Roles on the care team; RN vs. SW vs. unlicensed staff", 35),
            ("CM-M01-L4", "The case-management process model (screen-assess-plan-coordinate-monitor-evaluate)", 35),
            ("CM-M01-KC", "Knowledge check + scope/escalation note", 20),
        ],
        "key_terms": [
            ("Case management", "A collaborative process of assessment, planning, coordination, and monitoring of services to meet a patient's health needs."),
            ("Scope of practice", "The activities a licensed RN is authorized to perform under state law and competency."),
            ("Escalation", "Routing a decision or task to a prescriber/RN supervisor when it exceeds the case manager's role."),
            ("Indirect patient care", "Nursing activities that support patient outcomes without hands-on care (e.g., coordination, documentation)."),
            ("Care coordination", "Organizing patient care activities and sharing information among participants to achieve safer, more effective care."),
        ],
        "scenario": ("Nurse R receives a home-health referral for a fictional 72-year-old client "
                     "recovering from a hip procedure. The referral asks Nurse R to 'adjust the pain "
                     "medication.' No prescriber order accompanies the request."),
        "activities": [
            "Read Sections 1.1-1.4.",
            "Complete the team-role matching exercise (RN vs. SW vs. unlicensed).",
            "Work the fictional referral scenario and choose the correct first action.",
            "Complete Knowledge Check 1.",
        ],
        "exercise": ("Write a 5-line scope-and-escalation note documenting why the requested "
                     "medication change is outside RN case-management scope, what you did instead, "
                     "and to whom the request was routed."),
        "kc_blueprint": ("8 items (MCQ + true/false), unlimited attempts, immediate per-item feedback, "
                         "no full answer key shown, >=80% to complete."),
        "items": [
            {"id": "KC1-Q1", "type": "MCQ",
             "stem": "A home-health referral asks the RN case manager to 'adjust the pain medication.' What is the correct first action?",
             "choices": ["A) Adjust the dose yourself", "B) Decline and route to the prescriber/RN supervisor",
                         "C) Ask the family to decide", "D) Ignore the referral"],
             "answer": "B",
             "rationale": "Medication changes require a prescriber order and are outside RN case-management scope; route appropriately.",
             "remediation": "Review Reading 1.2 (scope boundaries) and CM-M01-L2."},
            {"id": "KC1-Q2", "type": "True/False",
             "stem": "Care coordination performed by an RN can qualify as indirect patient care under nursing practice.",
             "choices": ["True", "False"], "answer": "True",
             "rationale": "Coordination that supports patient outcomes is recognized indirect patient care when tied to nursing practice.",
             "remediation": "Review Reading 1.1 and the BRN fit rationale."},
            {"id": "KC1-Q3", "type": "MCQ",
             "stem": "Which task is clearly within the RN case manager's role?",
             "choices": ["A) Diagnosing a new condition", "B) Prescribing medication",
                         "C) Coordinating services and monitoring the care plan", "D) Performing surgery"],
             "answer": "C",
             "rationale": "Coordination and monitoring are core case-management functions; the others require different authority.",
             "remediation": "Review CM-M01-L4 (process model)."},
        ],
        "debrief": ("Debrief the scenario by contrasting scope-compliant routing with common pitfalls "
                    "(acting without an order, deferring clinical decisions to family). After a failed "
                    "knowledge check, route the learner to Reading 1.2 and require one retry."),
        "sme_flags": ["Confirm BRN/California RN scope phrasing with RN SME (Vanessa Valerio)."],
        "compliance_flags": ["Ensure no statement reads as legal advice; mark scope content as educational overview."],
        "defensibility": ("Anchors the entire course in registered-nursing scope, supporting the BRN "
                          "requirement that content be relevant to the practice of registered nursing."),
        "moodle": ["Page (overview)", "Book (lessons)", "Quiz (KC1)", "Assignment (scope note)", "Label (checkpoint)"],
    },
    {
        "id": "CM-M02", "num": "02",
        "file": "BRN_CM_M02_Assessment_Intake_Care_Planning",
        "title": "Assessment, Intake, and Patient-Centered Care Planning",
        "hours": 3, "minutes": 170, "linkage": "Direct patient/client care",
        "rationale": ("Nursing assessment, problem identification, and patient-centered goal setting "
                      "are core RN clinical practice and the foundation of safe care plans."),
        "description": ("Builds skill in structured intake, distinguishing subjective/objective data, "
                        "screening social determinants of health, and writing measurable, patient-centered "
                        "goals while checking for implicit bias."),
        "objectives": [
            "Conduct a structured intake using a standardized nursing assessment framework.",
            "Differentiate subjective and objective data and document each appropriately.",
            "Write at least two measurable, patient-centered goals from assessment findings.",
            "Identify social determinants of health and screen for implicit bias in intake judgments.",
        ],
        "content_sections": [
            "Reading 2.1 - Intake workflow and consent-to-assess.",
            "Reading 2.2 - Nursing assessment frameworks and SDOH screening.",
            "Reading 2.3 - From assessment data to nursing problems.",
            "Reading 2.4 - Writing measurable, patient-centered goals.",
        ],
        "lessons": [
            ("CM-M02-L1", "Intake workflow & consent-to-assess", 35),
            ("CM-M02-L2", "Nursing assessment frameworks / SDOH", 40),
            ("CM-M02-L3", "From data to nursing problems", 35),
            ("CM-M02-L4", "Writing measurable, patient-centered goals", 40),
            ("CM-M02-KC", "Knowledge check + care-plan worksheet", 20),
        ],
        "key_terms": [
            ("Subjective data", "Information reported by the patient (e.g., 'I feel tired')."),
            ("Objective data", "Measurable/observable findings (e.g., blood pressure, observed gait)."),
            ("SDOH", "Social determinants of health - conditions affecting health (housing, transport, income)."),
            ("Patient-centered goal", "A measurable outcome defined with the patient's values and priorities."),
            ("Implicit bias", "Unconscious attitudes that can affect clinical judgment and equity."),
        ],
        "scenario": ("A fictional new home-health client with type 2 diabetes reports difficulty "
                     "attending appointments because of limited transportation and lives alone."),
        "activities": [
            "Read Sections 2.1-2.4.",
            "Sort sample data points into subjective vs. objective.",
            "Identify the SDOH barrier in the scenario and a nursing intervention.",
            "Complete the Care-Plan Worksheet and Knowledge Check 2.",
        ],
        "exercise": ("Complete the Care-Plan Worksheet (template provided): list 3 nursing problems, "
                     "2 measurable patient-centered goals, 1 SDOH intervention, and a one-line "
                     "implicit-bias check note."),
        "kc_blueprint": ("10 items (MCQ + multi-select, scenario-tagged), unlimited attempts, "
                         "immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC2-Q1", "type": "Multi-select",
             "stem": "Which are examples of objective assessment data? (select all that apply)",
             "choices": ["A) Reported pain 7/10", "B) Blood pressure reading", "C) Observed unsteady gait", "D) 'I feel tired'"],
             "answer": "B, C",
             "rationale": "Objective data are measurable/observed; A and D are patient-reported (subjective).",
             "remediation": "Review Reading 2.2 (subjective vs. objective)."},
            {"id": "KC2-Q2", "type": "MCQ",
             "stem": "Which is the best-written measurable, patient-centered goal?",
             "choices": ["A) Patient will be healthier", "B) Patient will check blood glucose twice daily and log results for 2 weeks",
                         "C) Patient will try harder", "D) Nurse will fix the diabetes"],
             "answer": "B",
             "rationale": "B is measurable, time-bound, and patient-performed; the others are vague or not patient-centered.",
             "remediation": "Review Reading 2.4 (writing goals)."},
            {"id": "KC2-Q3", "type": "MCQ",
             "stem": "The transportation barrier in the scenario is best classified as:",
             "choices": ["A) A medication error", "B) A social determinant of health", "C) Objective vital sign", "D) A billing issue"],
             "answer": "B",
             "rationale": "Transportation access is a social determinant of health affecting care.",
             "remediation": "Review Reading 2.2 (SDOH)."},
        ],
        "debrief": ("Discuss how an SDOH barrier reshapes goals and interventions, and how a quick "
                    "bias check prevents assumptions about 'noncompliance.' Failed attempts route to "
                    "Reading 2.2/2.4 before retry."),
        "sme_flags": ["Validate the care-plan template against current nursing-process standards."],
        "compliance_flags": ["Pre-load template with fictional data; field-level 'no PHI' reminder."],
        "defensibility": ("Direct nursing assessment and care planning are unambiguous registered-nursing "
                          "practice, strongly supporting BRN content relevance."),
        "moodle": ["Page", "Book", "Glossary", "Quiz (KC2)", "Assignment (worksheet)", "Database"],
    },
    {
        "id": "CM-M03", "num": "03",
        "file": "BRN_CM_M03_Care_Coordination",
        "title": "Care Coordination Across Disciplines and Settings",
        "hours": 3, "minutes": 165, "linkage": "Direct + indirect patient/client care",
        "rationale": ("Nurse-led interdisciplinary coordination protects continuity and prevents gaps "
                      "that cause patient harm."),
        "description": ("Develops the RN's coordinating role across the interdisciplinary team and care "
                        "settings using structured handoff communication and loop-closure tracking."),
        "objectives": [
            "Map an interdisciplinary team and each member's contribution to a care plan.",
            "Apply structured handoff communication (e.g., SBAR) to a coordination event.",
            "Identify two failure points in cross-setting transitions and a nursing mitigation for each.",
            "Distinguish information that may be shared under minimum-necessary principles.",
        ],
        "content_sections": [
            "Reading 3.1 - The interdisciplinary team and the RN's coordinating role.",
            "Reading 3.2 - Structured communication and SBAR.",
            "Reading 3.3 - Cross-setting coordination (home health, primary care, specialty, payer).",
            "Reading 3.4 - Closing the loop and follow-up tracking.",
        ],
        "lessons": [
            ("CM-M03-L1", "The interdisciplinary team & RN's coordinating role", 35),
            ("CM-M03-L2", "Structured communication / SBAR", 40),
            ("CM-M03-L3", "Cross-setting coordination", 35),
            ("CM-M03-L4", "Closing the loop & follow-up tracking", 35),
            ("CM-M03-KC", "Knowledge check + coordination map", 20),
        ],
        "key_terms": [
            ("SBAR", "Situation-Background-Assessment-Recommendation: a structured handoff format."),
            ("Interdisciplinary team", "Clinicians and staff from multiple disciplines collaborating on care."),
            ("Loop closure", "Confirming that a referral/order/result was completed and acted upon."),
            ("Minimum necessary", "Sharing only the information needed for the purpose."),
            ("Transition point", "A handoff between settings/providers where care can break down."),
        ],
        "scenario": ("A fictional client is discharged from a hospital to home health, but the "
                     "medication reconciliation is missing and the primary care follow-up is unscheduled."),
        "activities": [
            "Read Sections 3.1-3.4.",
            "Build an interdisciplinary team map for the scenario.",
            "Draft a 3-line SBAR to the primary care office.",
            "Complete the branching coordination scenario and Knowledge Check 3.",
        ],
        "exercise": ("Build an Interdisciplinary Coordination Map (who / what / when / loop-closure) "
                     "for the scenario and write a 3-line SBAR handoff."),
        "kc_blueprint": ("8 items + 1 branching-lesson decision path, unlimited attempts, "
                         "immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC3-Q1", "type": "MCQ",
             "stem": "Which tool best structures a nurse-to-provider handoff?",
             "choices": ["A) SOAP", "B) SBAR", "C) PDSA", "D) SWOT"], "answer": "B",
             "rationale": "SBAR is a structured handoff communication tool.",
             "remediation": "Review Reading 3.2 (SBAR)."},
            {"id": "KC3-Q2", "type": "MCQ",
             "stem": "The missing medication reconciliation in the scenario is best described as a:",
             "choices": ["A) Loop-closure failure at a transition point", "B) Billing dispute",
                         "C) Normal finding", "D) Scope violation"], "answer": "A",
             "rationale": "A required step did not close the loop at the hospital-to-home transition.",
             "remediation": "Review Reading 3.3/3.4."},
            {"id": "KC3-Q3", "type": "True/False",
             "stem": "Under minimum-necessary principles, the RN should share only the information needed for the coordination purpose.",
             "choices": ["True", "False"], "answer": "True",
             "rationale": "Minimum-necessary limits disclosure to what the purpose requires.",
             "remediation": "Review Reading 3.4."},
        ],
        "debrief": ("Highlight how a single unclosed loop (med rec) cascades into harm, and how SBAR "
                    "plus tracking prevents it. Failed attempts route to Reading 3.2-3.4."),
        "sme_flags": ["Confirm SBAR/handoff examples reflect current practice."],
        "compliance_flags": ["All team/member/facility names must be fictional."],
        "defensibility": ("Coordination and handoff communication directly protect continuity of patient "
                          "care - clearly nursing-relevant indirect/direct care."),
        "moodle": ["Lesson (branching)", "Wiki", "Database", "Quiz (KC3)", "Assignment (map)"],
    },
    {
        "id": "CM-M04", "num": "04",
        "file": "BRN_CM_M04_Documentation_Legal_Charting",
        "title": "Documentation, Legal Charting, and Audit-Ready Records",
        "hours": 3, "minutes": 170, "linkage": "Indirect patient/client care (legal aspects of nursing)",
        "rationale": ("Accurate, timely, defensible documentation is a patient-safety and legal function "
                      "of nursing practice."),
        "description": ("Teaches documentation standards, error-correction conventions, audit-readiness, "
                        "and retention - the legal-aspects-of-nursing content that protects patients and "
                        "the provider."),
        "objectives": [
            "Apply documentation standards (accurate, objective, timely, complete, legible/attributable).",
            "Correct a non-compliant chart entry using accepted late-entry/error-correction conventions.",
            "Identify documentation that would and would not withstand an audit.",
            "Explain retention requirements and the four-year certificate/record posture.",
        ],
        "content_sections": [
            "Reading 4.1 - Purpose and legal weight of the record.",
            "Reading 4.2 - Documentation standards and charting do/don't.",
            "Reading 4.3 - Error correction, late entries, addenda.",
            "Reading 4.4 - Audit-readiness and retention (>=4-year posture).",
        ],
        "lessons": [
            ("CM-M04-L1", "Purpose & legal weight of the record", 35),
            ("CM-M04-L2", "Standards & charting do/don't", 40),
            ("CM-M04-L3", "Error correction, late entries, addenda", 35),
            ("CM-M04-L4", "Audit-readiness & retention", 35),
            ("CM-M04-KC", "Knowledge check + chart-note rewrite", 25),
        ],
        "key_terms": [
            ("Audit-ready", "Documentation complete and defensible enough to withstand external review."),
            ("Addendum", "A dated, attributed addition to a record made after the original entry."),
            ("Late entry", "A properly labeled entry made after the time of the event."),
            ("Attributable", "Clearly tied to the author and time (signature, credential, timestamp)."),
            ("Retention", "The required period records must be kept (>=4 years for CE records)."),
        ],
        "scenario": ("A fictional vague chart note reads: 'pt seems fine, will follow up.' It lacks "
                     "objective findings, a plan, a time, and a clear author."),
        "activities": [
            "Read Sections 4.1-4.4.",
            "Identify the deficiencies in the weak note.",
            "Rewrite the note to an audit-ready standard.",
            "Add a properly formatted correction/addendum and complete Knowledge Check 4.",
        ],
        "exercise": ("Rewrite the weak note into a compliant, audit-ready, de-identified entry, then add "
                     "a correctly formatted error-correction or addendum."),
        "kc_blueprint": ("10 items including 'spot the documentation error' items, unlimited attempts, "
                         "immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC4-Q1", "type": "MCQ",
             "stem": "Which note best meets audit-ready documentation standards?",
             "choices": ["A) 'Pt seems fine, will follow up'",
                         "B) Objective findings + action + plan + time + signature/credential",
                         "C) 'No issues'", "D) 'See chart'"], "answer": "B",
             "rationale": "Audit-ready notes are objective, complete, timed, and attributable.",
             "remediation": "Review Reading 4.2 (standards)."},
            {"id": "KC4-Q2", "type": "MCQ",
             "stem": "The correct way to fix a charting error is to:",
             "choices": ["A) Erase or delete it", "B) Use correction fluid",
                         "C) Draw a single line, label as error, date/sign, add correct entry",
                         "D) Rewrite the whole note silently"], "answer": "C",
             "rationale": "Errors are corrected transparently, never obliterated.",
             "remediation": "Review Reading 4.3 (corrections)."},
            {"id": "KC4-Q3", "type": "True/False",
             "stem": "Continuing-education provider records must be retained for at least four years.",
             "choices": ["True", "False"], "answer": "True",
             "rationale": "BRN/provider posture requires >=4-year retention (institution keeps 5).",
             "remediation": "Review Reading 4.4 (retention)."},
        ],
        "debrief": ("Compare the before/after note line by line; emphasize that the record is the legal "
                    "account of nursing judgment. Failed attempts route to Reading 4.2/4.3."),
        "sme_flags": ["RN SME + legal review of charting/correction standards."],
        "compliance_flags": ["Legal-aspects content; provided notes use fictional placeholders only; learners never paste real records."],
        "defensibility": ("Legal aspects of nursing and documentation are expressly recognized BRN-relevant "
                          "content when tied to patient care."),
        "moodle": ["Page", "Book", "Quiz (KC4)", "Assignment (rewrite)"],
    },
    {
        "id": "CM-M05", "num": "05",
        "file": "BRN_CM_M05_Patient_Rights_Advocacy_Ethics",
        "title": "Patient Rights, Consent, Advocacy, and Ethical Boundaries",
        "hours": 3, "minutes": 165, "linkage": "Direct patient/client care",
        "rationale": ("Advocacy, informed consent, confidentiality, and ethical boundaries are direct "
                      "nursing duties protecting patients."),
        "description": ("Equips the RN to protect patient rights, support informed consent and refusal, "
                        "advocate ethically, and navigate boundary conflicts and conflicts of interest."),
        "objectives": [
            "Describe core patient rights relevant to care management.",
            "Distinguish informed consent, assent, and refusal and the RN's role in each.",
            "Apply an ethical decision-making framework to a boundary conflict.",
            "Identify implicit-bias risks in advocacy decisions and a mitigation.",
        ],
        "content_sections": [
            "Reading 5.1 - Patient rights and confidentiality.",
            "Reading 5.2 - Informed consent, assent, and refusal.",
            "Reading 5.3 - Advocacy in practice.",
            "Reading 5.4 - Ethical boundaries and conflicts of interest.",
        ],
        "lessons": [
            ("CM-M05-L1", "Patient rights & confidentiality", 35),
            ("CM-M05-L2", "Informed consent / refusal", 35),
            ("CM-M05-L3", "Advocacy in practice", 35),
            ("CM-M05-L4", "Ethical boundaries & conflicts of interest", 40),
            ("CM-M05-KC", "Knowledge check + ethics reflection", 20),
        ],
        "key_terms": [
            ("Informed consent", "Voluntary agreement to care after disclosure of risks, benefits, alternatives."),
            ("Refusal", "A competent patient's right to decline recommended care."),
            ("Advocacy", "Acting to protect and promote the patient's rights, interests, and values."),
            ("Autonomy", "The patient's right to self-determination."),
            ("Conflict of interest", "A competing interest that could compromise patient-centered judgment."),
        ],
        "scenario": ("A fictional, decisionally-capable client declines a recommended home service that "
                     "the family strongly wants the client to accept."),
        "activities": [
            "Read Sections 5.1-5.4.",
            "Participate in the ethics poll (Choice).",
            "Apply a named ethical framework to the scenario.",
            "Write the ethics reflection and complete Knowledge Check 5.",
        ],
        "exercise": ("Write a 250-350 word ethics reflection applying a named decision framework, and "
                     "document the consent/refusal conversation in note form (fictional, de-identified)."),
        "kc_blueprint": ("8 items + 1 ethics scenario item, unlimited attempts, immediate feedback, "
                         "no full key, >=80% to complete."),
        "items": [
            {"id": "KC5-Q1", "type": "MCQ",
             "stem": "A capable client refuses a service the family wants. The RN's role is to:",
             "choices": ["A) Override the client", "B) Support informed autonomy and document the refusal",
                         "C) Withdraw all care", "D) Defer entirely to the family"], "answer": "B",
             "rationale": "The RN advocates for informed autonomy and documents the refusal.",
             "remediation": "Review Reading 5.2/5.3."},
            {"id": "KC5-Q2", "type": "True/False",
             "stem": "Confidentiality may be limited by minimum-necessary sharing for legitimate coordination.",
             "choices": ["True", "False"], "answer": "True",
             "rationale": "Coordination may require limited, minimum-necessary disclosure.",
             "remediation": "Review Reading 5.1."},
            {"id": "KC5-Q3", "type": "MCQ",
             "stem": "Accepting a personal gift that could influence service decisions is an example of:",
             "choices": ["A) Good rapport", "B) A conflict of interest", "C) Advocacy", "D) Informed consent"],
             "answer": "B",
             "rationale": "Such gifts create a conflict of interest that can compromise judgment.",
             "remediation": "Review Reading 5.4."},
        ],
        "debrief": ("Reinforce that advocacy means supporting the informed, capable patient's choice even "
                    "against family pressure, with careful documentation. Failed attempts route to Reading 5.2-5.4."),
        "sme_flags": ["Confirm consent/advocacy content; ensure no scope or legal-advice overreach."],
        "compliance_flags": ["Legal/ethics review; reflection rubric forbids real cases."],
        "defensibility": ("Patient advocacy and consent are direct nursing duties, squarely within BRN "
                          "patient-care relevance."),
        "moodle": ["Page", "Book", "Choice (poll)", "Quiz (KC5)", "Assignment (reflection)"],
    },
    {
        "id": "CM-M06", "num": "06",
        "file": "BRN_CM_M06_Transitions_of_Care_Discharge_Planning",
        "title": "Transitions of Care, Discharge Planning, and Community Resources",
        "hours": 3, "minutes": 170, "linkage": "Direct patient/client care",
        "rationale": ("Effective discharge planning and warm handoffs reduce avoidable readmissions and "
                      "patient harm."),
        "description": ("Builds competency in transition risk assessment, discharge-plan construction, "
                        "teach-back verification, and matching community resources to identified needs."),
        "objectives": [
            "Build a discharge/transition plan addressing meds, follow-up, equipment, and caregiver needs.",
            "Apply teach-back to confirm patient/caregiver understanding.",
            "Match at least three community resources to identified needs.",
            "Identify red-flag gaps that should delay or modify a transition.",
        ],
        "content_sections": [
            "Reading 6.1 - Transition risk and readmission drivers.",
            "Reading 6.2 - Discharge-plan components.",
            "Reading 6.3 - Teach-back and caregiver readiness.",
            "Reading 6.4 - Community resources and referrals.",
        ],
        "lessons": [
            ("CM-M06-L1", "Transition risk & readmission drivers", 35),
            ("CM-M06-L2", "Discharge-plan components", 40),
            ("CM-M06-L3", "Teach-back & caregiver readiness", 35),
            ("CM-M06-L4", "Community resources & referrals", 35),
            ("CM-M06-KC", "Knowledge check + discharge plan", 25),
        ],
        "key_terms": [
            ("Teach-back", "Having the patient/caregiver restate or demonstrate instructions to confirm understanding."),
            ("Readmission driver", "A factor that increases the chance of returning to acute care."),
            ("Warm handoff", "A transfer of care conducted in real time with the patient present."),
            ("Caregiver readiness", "The caregiver's ability and resources to safely support the patient."),
            ("Red-flag gap", "A safety gap serious enough to delay or modify a transition."),
        ],
        "scenario": ("A fictional client is going home with new oxygen equipment; the only caregiver "
                     "works full time and has not been trained on the equipment."),
        "activities": [
            "Read Sections 6.1-6.4.",
            "Identify the red-flag gap(s) in the scenario.",
            "Match at least three community resources to needs.",
            "Complete the Discharge/Transition Plan and Knowledge Check 6.",
        ],
        "exercise": ("Complete a Discharge/Transition Plan template (meds, follow-up, equipment, "
                     "caregiver support, community resources) including a teach-back confirmation line."),
        "kc_blueprint": ("10 items, unlimited attempts, immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC6-Q1", "type": "MCQ",
             "stem": "Which best confirms a caregiver understands new equipment instructions?",
             "choices": ["A) Ask 'Do you understand?'", "B) Teach-back demonstration",
                         "C) Hand them a pamphlet", "D) Assume understanding"], "answer": "B",
             "rationale": "Teach-back verifies understanding; yes/no questions do not.",
             "remediation": "Review Reading 6.3 (teach-back)."},
            {"id": "KC6-Q2", "type": "MCQ",
             "stem": "In the scenario, the untrained full-time caregiver is best treated as a:",
             "choices": ["A) Reason to cancel care", "B) Red-flag gap to address before/at transition",
                         "C) Billing problem", "D) Non-issue"], "answer": "B",
             "rationale": "It is a safety gap that must be addressed to ensure a safe transition.",
             "remediation": "Review Reading 6.1/6.3."},
            {"id": "KC6-Q3", "type": "Multi-select",
             "stem": "Core components of a discharge plan include: (select all)",
             "choices": ["A) Medication reconciliation", "B) Follow-up appointments",
                         "C) Equipment/supplies", "D) Caregiver support"], "answer": "A, B, C, D",
             "rationale": "All four are core discharge-plan components.",
             "remediation": "Review Reading 6.2."},
        ],
        "debrief": ("Emphasize that an unaddressed caregiver-training gap is a classic readmission driver; "
                    "teach-back and resource matching close it. Failed attempts route to Reading 6.2/6.3."),
        "sme_flags": ["Validate teach-back technique and resource categories."],
        "compliance_flags": ["Resource directory uses fictional/generic resource types; no real client data."],
        "defensibility": ("Discharge planning to prevent readmission harm is direct patient care and a "
                          "recognized BRN-relevant topic."),
        "moodle": ["Page", "Book", "Database (resources)", "Quiz (KC6)", "Assignment (plan)"],
    },
    {
        "id": "CM-M07", "num": "07",
        "file": "BRN_CM_M07_Utilization_Review_Payer_Communication",
        "title": "Utilization Review, Medical Necessity, and Payer-Safe Communication",
        "hours": 3, "minutes": 165, "linkage": "Indirect patient/client care (current healthcare trends)",
        "rationale": ("Utilization review tied to nursing judgment ensures patients receive appropriate, "
                      "safe, non-excessive care; payer-safe communication protects the patient and the record."),
        "description": ("Clarifies the RN's lane in utilization review and medical necessity, how to "
                        "document a defensible nursing rationale, and how to communicate with payers without "
                        "misrepresentation or scope overreach. Highest-scrutiny module - kept anchored to "
                        "nursing judgment and patient safety."),
        "objectives": [
            "Define medical necessity and the RN's role in supporting (not determining coverage of) it.",
            "Apply criteria-based review to a fictional service request.",
            "Write a defensible medical-necessity rationale in nursing terms.",
            "Communicate with payers without misrepresentation or scope overreach.",
        ],
        "content_sections": [
            "Reading 7.1 - What utilization review is and the RN's lane.",
            "Reading 7.2 - Medical-necessity criteria and evidence.",
            "Reading 7.3 - Documentation that supports necessity.",
            "Reading 7.4 - Payer-safe, accurate communication.",
        ],
        "lessons": [
            ("CM-M07-L1", "What UR is and the RN's lane", 40),
            ("CM-M07-L2", "Medical-necessity criteria & evidence", 40),
            ("CM-M07-L3", "Documentation that supports necessity", 35),
            ("CM-M07-L4", "Payer-safe, accurate communication", 30),
            ("CM-M07-KC", "Knowledge check + necessity rationale", 20),
        ],
        "key_terms": [
            ("Utilization review", "Evaluation of the appropriateness/necessity of services against criteria."),
            ("Medical necessity", "Services appropriate and required for a patient's condition per accepted criteria."),
            ("Payer-safe communication", "Accurate, non-misleading communication that avoids scope overreach."),
            ("Criteria-based review", "Comparing a request to defined clinical criteria."),
            ("Defensible rationale", "A documented clinical reasoning that withstands review."),
        ],
        "scenario": ("A fictional request seeks extended home-health visits beyond the typical period; "
                     "the documentation must be reviewed against criteria and a rationale drafted."),
        "activities": [
            "Read Sections 7.1-7.4.",
            "Review the fictional request against sample criteria.",
            "Draft a medical-necessity rationale (facts -> criteria -> conclusion).",
            "Write a payer-safe communication snippet and complete Knowledge Check 7.",
        ],
        "exercise": ("Write a Medical-Necessity Rationale note (clinical facts -> criteria -> conclusion) "
                     "plus a short payer-safe communication snippet for the fictional request."),
        "kc_blueprint": ("8 items, unlimited attempts, immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC7-Q1", "type": "MCQ",
             "stem": "When supporting medical necessity, the RN case manager should:",
             "choices": ["A) Decide coverage", "B) Document clinical facts against accepted criteria",
                         "C) Tell the payer whatever secures approval", "D) Omit unfavorable facts"], "answer": "B",
             "rationale": "The RN supports necessity with accurate documentation and does not determine coverage.",
             "remediation": "Review Reading 7.2/7.3."},
            {"id": "KC7-Q2", "type": "True/False",
             "stem": "Overstating a patient's condition to secure authorization is acceptable if it helps the patient.",
             "choices": ["True", "False"], "answer": "False",
             "rationale": "Misrepresentation is never acceptable; it harms the patient, record, and provider.",
             "remediation": "Review Reading 7.4 (payer-safe communication)."},
            {"id": "KC7-Q3", "type": "MCQ",
             "stem": "A defensible medical-necessity rationale is structured as:",
             "choices": ["A) Conclusion only", "B) Opinion without evidence",
                         "C) Clinical facts -> criteria -> conclusion", "D) Billing codes only"], "answer": "C",
             "rationale": "Linking facts to criteria to a conclusion makes the rationale defensible.",
             "remediation": "Review Reading 7.3."},
        ],
        "debrief": ("Stress the nursing-judgment and patient-safety thread: UR exists to ensure "
                    "appropriate, safe care - never to misrepresent. Failed attempts route to Reading 7.2-7.4."),
        "sme_flags": ["HIGH SCRUTINY: keep nursing-judgment/patient-safety thread explicit so content reads as indirect patient care, not business administration."],
        "compliance_flags": ["Compliance review required; fictional request data only."],
        "defensibility": ("Framed as nursing judgment protecting appropriate, safe patient care - "
                          "qualifying as indirect patient care rather than pure administration. SME must confirm."),
        "moodle": ["Page", "Book", "Quiz (KC7)", "Assignment (rationale)"],
    },
    {
        "id": "CM-M08", "num": "08",
        "file": "BRN_CM_M08_Quality_Risk_Incident_Escalation",
        "title": "Quality Assurance, Risk Management, Incident Reporting, and Escalation",
        "hours": 3, "minutes": 165, "linkage": "Indirect patient/client care (quality assurance; legal aspects)",
        "rationale": ("QA, risk identification, incident reporting, and escalation are nursing "
                      "patient-safety functions."),
        "description": ("Develops the RN's ability to recognize quality indicators and risks, complete a "
                        "compliant incident report, and escalate within a just-culture framework. "
                        "Highest-scrutiny module - anchored to patient safety, not administration."),
        "objectives": [
            "Identify quality indicators relevant to case management.",
            "Recognize a reportable event and complete a compliant incident report.",
            "Apply an escalation pathway (who, when, how) to a safety concern.",
            "Distinguish quality improvement from blame and describe a just-culture response.",
        ],
        "content_sections": [
            "Reading 8.1 - QA fundamentals and indicators.",
            "Reading 8.2 - Risk identification.",
            "Reading 8.3 - Incident reporting standards.",
            "Reading 8.4 - Escalation and just culture.",
        ],
        "lessons": [
            ("CM-M08-L1", "QA fundamentals & indicators", 35),
            ("CM-M08-L2", "Risk identification", 35),
            ("CM-M08-L3", "Incident reporting standards", 40),
            ("CM-M08-L4", "Escalation & just culture", 35),
            ("CM-M08-KC", "Knowledge check + incident report", 20),
        ],
        "key_terms": [
            ("Quality indicator", "A measurable element of care used to monitor quality."),
            ("Near-miss", "An event that could have caused harm but did not."),
            ("Incident report", "A factual, objective record of an adverse event or near-miss."),
            ("Just culture", "A framework balancing accountability with learning, not blame."),
            ("Escalation pathway", "The defined who/when/how for raising a safety concern."),
        ],
        "scenario": ("During a fictional home visit, the RN discovers a medication discrepancy that did "
                     "not reach the patient (a near-miss) caused by an outdated medication list."),
        "activities": [
            "Read Sections 8.1-8.4.",
            "Classify the event (near-miss vs. adverse event).",
            "Complete a de-identified incident report.",
            "Write an escalation note and complete Knowledge Check 8.",
        ],
        "exercise": ("Complete a de-identified Incident Report for the near-miss and write an escalation "
                     "note identifying who is notified, when, and how."),
        "kc_blueprint": ("10 items, unlimited attempts, immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC8-Q1", "type": "MCQ",
             "stem": "On finding a near-miss medication discrepancy, the RN should first:",
             "choices": ["A) Ignore it because no harm occurred", "B) Address safety, then file an incident report and escalate",
                         "C) Blame the prior nurse", "D) Delete the medication note"], "answer": "B",
             "rationale": "Patient safety first, then objective reporting and escalation.",
             "remediation": "Review Reading 8.3/8.4."},
            {"id": "KC8-Q2", "type": "MCQ",
             "stem": "An incident report should be:",
             "choices": ["A) An opinion about who is at fault", "B) Objective, factual, and timely",
                         "C) Stored only verbally", "D) Written days later from memory"], "answer": "B",
             "rationale": "Reports must be factual, objective, and timely.",
             "remediation": "Review Reading 8.3."},
            {"id": "KC8-Q3", "type": "True/False",
             "stem": "A just-culture response focuses on system learning rather than individual blame for honest errors.",
             "choices": ["True", "False"], "answer": "True",
             "rationale": "Just culture balances accountability with system learning.",
             "remediation": "Review Reading 8.4."},
        ],
        "debrief": ("Connect the near-miss to a system fix (medication-list reconciliation) and a "
                    "blame-free report. Failed attempts route to Reading 8.3/8.4."),
        "sme_flags": ["HIGH SCRUTINY: anchor QA/risk content to patient safety and nursing practice, not pure administration."],
        "compliance_flags": ["Compliance review required; incident template uses fictional data with explicit no-PHI banner."],
        "defensibility": ("Quality assurance and legal aspects of nursing are expressly BRN-relevant when "
                          "tied to patient safety. SME must confirm framing."),
        "moodle": ["Page", "Book", "Quiz (KC8)", "Assignment (incident report)"],
    },
    {
        "id": "CM-M09", "num": "09",
        "file": "BRN_CM_M09_Chronic_Disease_Geriatric_High_Risk_Care",
        "title": "Chronic Disease, Geriatric, and High-Risk Patient Management",
        "hours": 3, "minutes": 170, "linkage": "Direct patient/client care (scientific knowledge)",
        "rationale": ("Applies clinical/scientific knowledge to manage high-risk populations and reduce "
                      "decompensation."),
        "description": ("Strengthens risk-stratification, chronic-disease management priorities, "
                        "geriatric-syndrome awareness, and monitoring plans with escalation triggers. "
                        "Educational content only; not medical advice."),
        "objectives": [
            "Apply risk-stratification to identify high-risk patients in a panel.",
            "Describe nursing management priorities for common chronic conditions in care management.",
            "Identify geriatric-specific risks (falls, polypharmacy, cognition) and nursing mitigations.",
            "Build a monitoring plan with escalation triggers.",
        ],
        "content_sections": [
            "Reading 9.1 - Risk stratification.",
            "Reading 9.2 - Chronic-disease management priorities.",
            "Reading 9.3 - Geriatric syndromes and polypharmacy.",
            "Reading 9.4 - Monitoring plans and escalation triggers.",
        ],
        "lessons": [
            ("CM-M09-L1", "Risk stratification", 40),
            ("CM-M09-L2", "Chronic-disease management priorities", 40),
            ("CM-M09-L3", "Geriatric syndromes & polypharmacy", 35),
            ("CM-M09-L4", "Monitoring plans & triggers", 35),
            ("CM-M09-KC", "Knowledge check + risk-stratification worksheet", 20),
        ],
        "key_terms": [
            ("Risk stratification", "Classifying patients by risk to target resources."),
            ("Polypharmacy", "Use of multiple medications, raising interaction/adverse-event risk."),
            ("Geriatric syndrome", "Multifactorial conditions common in older adults (falls, delirium)."),
            ("Escalation trigger", "A predefined change that prompts a higher level of action."),
            ("Decompensation", "Functional/clinical decline as a condition worsens."),
        ],
        "scenario": ("A fictional 80-year-old with heart failure, diabetes, and mild cognitive impairment "
                     "takes nine medications and had one recent fall."),
        "activities": [
            "Read Sections 9.1-9.4.",
            "Stratify the client's risk level with justification.",
            "Identify polypharmacy and fall risks with nursing mitigations.",
            "Build a monitoring plan with >=3 triggers and complete Knowledge Check 9.",
        ],
        "exercise": ("Complete a Risk-Stratification + Monitoring Worksheet for the scenario, including at "
                     "least three escalation triggers tied to specific findings."),
        "kc_blueprint": ("10 items, unlimited attempts, immediate feedback, no full key, >=80% to complete."),
        "items": [
            {"id": "KC9-Q1", "type": "Multi-select",
             "stem": "Which factors raise this geriatric client's risk profile? (select all)",
             "choices": ["A) Polypharmacy (9 meds)", "B) Recent fall", "C) Cognitive impairment", "D) A single stable condition"],
             "answer": "A, B, C",
             "rationale": "A-C are high-risk geriatric markers; D is comparatively lower risk.",
             "remediation": "Review Reading 9.1/9.3."},
            {"id": "KC9-Q2", "type": "MCQ",
             "stem": "An appropriate escalation trigger in a heart-failure monitoring plan is:",
             "choices": ["A) Weight gain of >=3 lb in a day / 5 lb in a week", "B) Any change in TV channel",
                         "C) Normal daily walk", "D) Stable weight"], "answer": "A",
             "rationale": "Rapid weight gain can signal fluid overload requiring escalation.",
             "remediation": "Review Reading 9.4."},
            {"id": "KC9-Q3", "type": "True/False",
             "stem": "Polypharmacy increases the risk of adverse drug events and warrants medication review.",
             "choices": ["True", "False"], "answer": "True",
             "rationale": "Multiple medications raise interaction/adverse-event risk.",
             "remediation": "Review Reading 9.3."},
        ],
        "debrief": ("Show how stratification drives monitoring intensity and triggers, and how "
                    "polypharmacy review prevents harm. Failed attempts route to Reading 9.1/9.3/9.4. "
                    "Reinforce content is educational, not medical advice."),
        "sme_flags": ["Confirm clinical content currency; mark as education, not medical advice or standing orders."],
        "compliance_flags": ["Fictional clinical profile only; avoid color-only risk tiers (use labels)."],
        "defensibility": ("Application of scientific/clinical knowledge to high-risk patients is core "
                          "direct patient care and strongly BRN-relevant."),
        "moodle": ["Page", "Book", "Quiz (KC9)", "Assignment (worksheet)"],
    },
    {
        "id": "CM-M10", "num": "10",
        "file": "BRN_CM_M10_Capstone_Final_Assessment",
        "title": "Integrated Case Management Capstone and Final Assessment",
        "hours": 3, "minutes": 175, "linkage": "Direct + indirect patient/client care",
        "rationale": ("Synthesizes nurse-led care management across the full patient journey and verifies "
                      "competency."),
        "description": ("Integrates assessment, coordination, documentation, advocacy, transitions, UR, "
                        "and QA into one fictional end-to-end case, then verifies mastery via a cumulative "
                        "final examination."),
        "objectives": [
            "Integrate assessment, coordination, documentation, advocacy, transitions, and QA into one case.",
            "Produce an audit-ready, de-identified case-management documentation package.",
            "Demonstrate >=80% mastery on a cumulative final assessment.",
            "Reflect on implicit-bias and ethical considerations in the integrated case.",
        ],
        "content_sections": [
            "Briefing 10.1 - Capstone scenario and rubric walkthrough.",
            "Work session 10.2 - Building the integrated case package.",
            "Self-review 10.3 - Rubric self-check.",
            "Final exam 10.4 - Cumulative assessment (bank draw).",
        ],
        "lessons": [
            ("CM-M10-L1", "Capstone briefing & rubric walkthrough", 30),
            ("CM-M10-L2", "Building the integrated case package", 60),
            ("CM-M10-L3", "Self-review against rubric", 25),
            ("CM-M10-FE", "Final cumulative assessment", 60),
        ],
        "key_terms": [
            ("Capstone", "A culminating, integrative performance task demonstrating competence."),
            ("Rubric", "A scoring guide defining criteria and performance levels."),
            ("Cumulative assessment", "A summative exam covering the entire course."),
            ("Integration", "Combining skills from all modules into coherent practice."),
            ("Internal answer key", "An admin/faculty-only key, never shown to learners."),
        ],
        "scenario": ("A fictional, de-identified high-risk home-health client is followed from intake "
                     "through a safe transition; the learner produces the full documentation package."),
        "activities": [
            "Review the capstone briefing and rubric.",
            "Assemble the integrated case package (nine artifacts).",
            "Complete the rubric self-check.",
            "Sit the cumulative final exam (>=80% to pass).",
        ],
        "exercise": ("Submit the Capstone Documentation Package: intake/assessment, care plan, "
                     "coordination map + SBAR, audit-ready chart note, consent/advocacy + ethics "
                     "reflection, discharge/transition plan with teach-back, medical-necessity rationale, "
                     "incident/escalation note, and risk-stratification + monitoring plan - all fictional "
                     "and de-identified, with a no-PHI attestation."),
        "kc_blueprint": ("Capstone rubric self-check; the cumulative final exam (40-50 items, ~4-5 per "
                         "module, bank draw, shuffled, time-limited, max 3 attempts, no full key) is the "
                         "summative assessment. >=80% to pass."),
        "items": [
            {"id": "FINAL-SCN1", "type": "Scenario",
             "stem": "Given the fictional end-to-end case, select the action sequence that best protects a safe transition.",
             "choices": ["A) Reconcile meds -> confirm follow-up -> teach-back -> document",
                         "B) Discharge first -> reconcile later", "C) Skip teach-back if rushed",
                         "D) Defer all follow-up to the family"], "answer": "A",
             "rationale": "Reconcile, confirm follow-up, verify understanding, then document - integrates M03/M04/M06/M08.",
             "remediation": "Route to the weakest objective area; require re-do before retry."},
            {"id": "FINAL-Q2", "type": "MCQ",
             "stem": "Across the case, which is always required before issuing a certificate of completion?",
             "choices": ["A) A blank certificate on file", "B) Meeting all completion criteria + final >=80%",
                         "C) A real CEP number regardless of approval", "D) Family sign-off"], "answer": "B",
             "rationale": "Certificates issue only after completion criteria + passing the final; no blank certificates.",
             "remediation": "Review the certificate-gate logic."},
            {"id": "FINAL-BANK", "type": "Bank (40-50 items)",
             "stem": "Cumulative bank: ~4-5 items per module, randomized draw across all 10 modules.",
             "choices": ["Mixed MCQ / multi-select / true-false / scenario"], "answer": "Per SME-validated key (admin-only)",
             "rationale": "SME-authored rationales per item; not shown to learners.",
             "remediation": "Remediation routing between attempts; lock after 3 attempts -> faculty review."},
        ],
        "debrief": ("Faculty debrief uses the rubric to give criterion-level feedback (no answer key). "
                    "After a failed final, route to remediation and require a short reflection/re-do before "
                    "the next attempt; lock after three attempts for faculty/SME review."),
        "sme_flags": ["Capstone rubric and final-exam items require SME authoring and sign-off for validity/fairness."],
        "compliance_flags": ["Capstone instructions forbid real cases; automated no-PHI reminder + manual PHI review before scoring."],
        "defensibility": ("Demonstrates integrated nurse-led care management and verifies competency, "
                          "supporting the course's overall BRN relevance and rigor."),
        "moodle": ["Page (briefing)", "Assignment (capstone, rubric-graded)", "Quiz (final, gated >=80%)", "Certificate (gated)"],
    },
]


# ----------------------------------------------------------------- ASSEMBLERS
def module_md(m):
    L = []
    L.append(BANNER)
    L.append("")
    L.append(f"## {m['title']}")
    L.append("")
    L.append(PROVIDER)
    L.append("")
    L.append(f"> {PLACEHOLDER}")
    L.append("")
    L.append(f"*{DOC_MODEL_NOTE}*")
    L.append("")
    # quick facts table
    L.append("### Module At a Glance")
    L.append("")
    L.append(md_table(
        ["Field", "Value"],
        [["Module ID", m["id"]],
         ["Module title", m["title"]],
         ["Parent course", COURSE],
         ["Contact hours", f"{m['hours']} (draft design math)"],
         ["Estimated learner minutes", f"{m['minutes']} (>=150 floor)"],
         ["Direct/indirect linkage", m["linkage"]],
         ["Approval status", "Draft / Pending BRN CEP Approval"]]))
    L.append("")
    L.append("### BRN Relevance Rationale")
    L.append("")
    L.append(m["rationale"])
    L.append("")
    L.append("### Module Description")
    L.append("")
    L.append(m["description"])
    L.append("")
    L.append("### Measurable Learning Objectives")
    L.append("")
    L.append("By the end of this module the learner will be able to:")
    L.append("")
    for i, o in enumerate(m["objectives"], 1):
        L.append(f"{i}. {o}")
    L.append("")
    L.append("### Required Readings / Learning Content Sections")
    L.append("")
    for c in m["content_sections"]:
        L.append(f"- {c}")
    L.append("")
    L.append("### Detailed Lesson Outline")
    L.append("")
    L.append(md_table(["Lesson ID", "Lesson", "Est. minutes"],
                      [[l[0], l[1], l[2]] for l in m["lessons"]]))
    L.append("")
    total = sum(l[2] for l in m["lessons"])
    L.append(f"Total estimated instructional minutes: **{total}** (meets the >=150-minute / 3-contact-hour floor).")
    L.append("")
    L.append("### Key Terms")
    L.append("")
    L.append(md_table(["Term", "Definition"], [[t[0], t[1]] for t in m["key_terms"]]))
    L.append("")
    L.append("### Fictional / De-identified Case Scenario")
    L.append("")
    L.append(f"*All clinical content is fictional and de-identified. No PHI.* {m['scenario']}")
    L.append("")
    L.append("### Learner Activities")
    L.append("")
    for a in m["activities"]:
        L.append(f"- {a}")
    L.append("")
    L.append("### Documentation / Decision-Making Exercise")
    L.append("")
    L.append(m["exercise"])
    L.append("")
    L.append("### Knowledge Check Blueprint")
    L.append("")
    L.append(m["kc_blueprint"])
    L.append("")
    L.append("### Assessment Items (Learner-Facing Stems)")
    L.append("")
    for it in m["items"]:
        L.append(f"**{it['id']} ({it['type']}).** {it['stem']}")
        for ch in it["choices"]:
            L.append(f"- {ch}")
        L.append("")
    L.append("### LMS Completion Criteria")
    L.append("")
    if m["id"] == "CM-M10":
        L.append("- Capstone package submitted and meets the rubric minimum on every criterion.")
        L.append("- Cumulative final exam passed at >=80%.")
        L.append("- Course evaluation submitted (course-level gate).")
    else:
        L.append("- All lesson pages viewed (activity completion: require view).")
        L.append(f"- {m['id']} knowledge check passed at >=80% (require passing grade).")
        L.append("- Documentation/decision exercise submitted (require submission).")
    L.append("")
    L.append("### Evidence Generated by Learner Completion")
    L.append("")
    L.append("- Activity-completion timestamps (time-on-task evidence).")
    L.append("- Knowledge-check score and attempt log.")
    L.append("- Submitted exercise artifact (retained >=4 years; no PHI).")
    if m["id"] == "CM-M10":
        L.append("- Capstone submission + rubric scoring + no-PHI attestation.")
        L.append("- Final-exam attempt record + item analytics.")
    L.append("")
    L.append("### Moodle Activity Recommendations")
    L.append("")
    for mo in m["moodle"]:
        L.append(f"- {mo}")
    L.append("")
    L.append("### Accessibility Considerations")
    L.append("")
    L.append("- Captions + transcripts for any media; semantic headings; alt text on diagrams.")
    L.append("- Sufficient color contrast; no color-only meaning; keyboard-navigable activities.")
    L.append("- Accessible downloadable templates (tagged PDF + DOCX); extended-time accommodation supported.")
    L.append("- Target WCAG 2.1 AA on the built course.")
    L.append("")
    L.append("### PHI / Privacy Guardrails")
    L.append("")
    L.append("- All cases fictional and de-identified; no real patient/resident/family/facility data.")
    L.append(f"- {m['compliance_flags'][0]}")
    L.append("- Submission reminders and (for capstone) attestation + manual PHI review.")
    L.append("")
    L.append("### SME Review Flags")
    L.append("")
    for f in m["sme_flags"]:
        L.append(f"- [[SME REVIEW REQUIRED]] {f}")
    L.append("")
    L.append("### Compliance Review Flags")
    L.append("")
    for f in m["compliance_flags"]:
        L.append(f"- [[COMPLIANCE REVIEW]] {f}")
    L.append("")
    L.append("### Internal Answer Key Appendix (ADMIN / FACULTY ONLY - DO NOT SHOW LEARNERS)")
    L.append("")
    L.append(md_table(
        ["Item ID", "Type", "Correct answer", "Rationale", "Remediation"],
        [[it["id"], it["type"], it["answer"], it["rationale"], it["remediation"]] for it in m["items"]]))
    L.append("")
    L.append("### Debrief / Remediation Guidance")
    L.append("")
    L.append(m["debrief"])
    L.append("")
    L.append("### Application-Packet Defensibility Notes")
    L.append("")
    L.append(m["defensibility"])
    L.append("")
    L.append("> **Program-structure note:** This module is part of the 30-contact-hour, 10-module RN "
             "case management program (10 modules x 3 contact hours; 50 instructional minutes = 1 contact "
             "hour; minimum 1,500 instructional minutes, 1,680 design minutes). The official BRN contact-hour "
             "map and transfer worksheet are aligned to this 30-contact-hour structure. Any earlier "
             "4-contact-hour representative course is superseded and is not part of the current BRN CEP "
             "signer-review package. [[SME REVIEW REQUIRED BEFORE SUBMISSION]]")
    L.append("")
    L.append("---")
    L.append("")
    L.append(FOOTER)
    return "\n".join(L)


def course_md():
    L = []
    L.append(BANNER)
    L.append("")
    L.append("## Full Course Documentation Packet (30 Contact Hours)")
    L.append("")
    L.append(PROVIDER)
    L.append("")
    L.append(f"**Course:** {COURSE}")
    L.append("")
    L.append(f"> {PLACEHOLDER}")
    L.append("")
    L.append(f"*{DOC_MODEL_NOTE}*")
    L.append("")
    L.append("> **Program-structure note (read first):** The BRN / CEP lane is a **30-contact-hour, "
             "10-module** RN case management program (10 modules x 3 contact hours each; 50 instructional "
             "minutes = 1 contact hour; minimum **1,500 instructional minutes**, 1,680 design minutes). The "
             "official BRN contact-hour map and transfer worksheet are aligned to this 30-contact-hour "
             "structure. Any earlier 4-contact-hour representative course is **superseded** and is **not part "
             "of the current BRN CEP signer-review package**. Approval posture: pending BRN CEP approval "
             "(provider approval, not course-by-course approval). [[SME REVIEW REQUIRED BEFORE SUBMISSION]]")
    L.append("")

    L.append("### 1. Course Overview")
    L.append("")
    L.append("A fully online, self-paced continuing education course for California registered nurses in "
             "care/case management. Ten modules build nurse-led care coordination, patient-centered "
             "assessment and care planning, audit-ready documentation, patient advocacy and ethics, safe "
             "transitions and discharge planning, utilization review, quality/risk management, and "
             "high-risk patient management - applied through fictional, de-identified scenarios and "
             "documentation practice, with a capstone and cumulative final exam.")
    L.append("")
    L.append("**Audience:** California RNs working or preparing to work in care management, case "
             "management, home-health coordination, intake coordination, discharge planning, quality "
             "review, or patient advocacy.")
    L.append("")
    L.append("**This course is NOT** a case management certification, CCM certification, social-work "
             "license credit, or any scope expansion. It is RN continuing education only.")
    L.append("")

    L.append("### 2. 30-Contact-Hour Calculation")
    L.append("")
    L.append("- Contact-hour rule: 50 instructional minutes = 1 contact hour.")
    L.append("- 30 contact hours x 50 minutes = **1,500 instructional minutes minimum**.")
    L.append("- 10 modules x 3 contact hours = 30 contact hours; each module >=150 minutes; none < 60 minutes.")
    L.append("- Design total estimated learner minutes = **1,680** (buffer above the 1,500 floor).")
    L.append("- This is draft course-design math only - **not** an 'approved for' claim.")
    L.append("")

    L.append("### 3. Module Sequence")
    L.append("")
    L.append(md_table(
        ["Module ID", "Title", "Contact hrs", "Est. min", "Linkage"],
        [[m["id"], m["title"], m["hours"], m["minutes"], m["linkage"]] for m in MODULES] +
        [["TOTAL", "10 modules", 30, 1680, "Direct + Indirect"]]))
    L.append("")

    L.append("### 4. BRN Fit Rationale")
    L.append("")
    L.append("BRN CE content must be relevant to the practice of registered nursing and related to "
             "scientific knowledge, technical skills, or direct/indirect patient/client care. Each module "
             "is anchored to that standard:")
    L.append("")
    L.append(md_table(["Module", "Linkage", "Nursing-practice anchor"],
                      [[m["id"], m["linkage"], m["rationale"]] for m in MODULES]))
    L.append("")
    L.append("**Highest-scrutiny modules:** CM-M07 (Utilization Review) and CM-M08 (QA/Risk) border "
             "administrative content; both keep the nursing-judgment and patient-safety thread explicit so "
             "they read as indirect patient care. [[SME REVIEW REQUIRED BEFORE SUBMISSION]]")
    L.append("")

    L.append("### 5. LMS Delivery Model")
    L.append("")
    L.append("- **Platform:** Moodle. **Format:** Topics format - Section 0 'Start Here' + 10 module "
             "sections + 'Certificate & Records' section.")
    L.append("- **Sequential gating:** each module is restricted until the prior module is complete; the "
             "final exam is restricted until Modules 1-9 are complete and the capstone is submitted.")
    L.append("- **Completion tracking:** lessons require view; knowledge checks require a passing grade "
             "(>=80%); assignments require submission (and grade where faculty-scored).")
    L.append("- **Mobile-first:** single-column responsive layout, large tap targets, chunked lessons, "
             "accessible downloadable templates; tested in the Moodle mobile app.")
    L.append("- **Progress visibility:** completion-progress and course-completion-status blocks.")
    L.append("")

    L.append("### 6. Assessment Strategy")
    L.append("")
    L.append(md_table(
        ["Layer", "Instrument", "Threshold", "Learner sees", "Admin/faculty sees"],
        [["1", "Module knowledge checks (KC1-KC9 + capstone self-check)", ">=80% to complete", "Per-item feedback only", "Item analysis + internal key"],
         ["2", "Scenario-based assignments (per module)", "Submission + rubric", "Rubric feedback", "Submissions + scores"],
         ["3", "Capstone documentation package", "Meets rubric minimum", "Rubric feedback", "Full rubric scoring"],
         ["4", "Cumulative final exam", ">=80% to pass", "Pass/fail + remediation", "Item analysis + internal key"]]))
    L.append("")
    L.append("**Pass threshold:** 80% on all graded knowledge checks and the final exam. **No final "
             "answer key is shown to learners**; a separate internal key (admin/faculty) holds correct "
             "answers + rationales. **Remediation:** targeted feedback -> route to relevant lesson(s) -> "
             "require reflection/re-do before retry -> lock after maximum attempts for faculty/SME review.")
    L.append("")

    L.append("### 7. Certificate Gate Logic")
    L.append("")
    L.append("A certificate issues **only** when all conditions are met (no blank certificates):")
    L.append("")
    L.append(md_table(
        ["Gate item", "Required condition", "Evidence source", "Manual review"],
        [["All modules complete", "CM-M01..CM-M10 activity completion done", "Completion report", "No"],
         ["Knowledge checks passed", "Each KC >=80%", "Gradebook", "No"],
         ["Capstone meets rubric", "Minimum met on all criteria", "Assignment grade", "Yes (faculty)"],
         ["Final exam passed", ">=80%", "Quiz grade", "No"],
         ["Evaluation submitted", "Course evaluation complete", "Feedback activity", "No"],
         ["No-PHI attestation", "Attestation + faculty PHI review", "Assignment attestation", "Yes"],
         ["Approval placeholder", "CEP number shows placeholder until issued", "Certificate template", "Yes"],
         ["Retention statement", "4-year retention notice present", "Certificate template", "Yes"]]))
    L.append("")

    L.append("### 8. Completion / Evidence Model")
    L.append("")
    L.append("Course completion = all 10 module checkpoints + final exam passed + evaluation submitted, "
             "which unlocks the gated certificate. Evidence captured per learner: completion report, "
             "knowledge-check scores, assignment submissions, capstone + rubric, final-exam records, "
             "time-on-task logs, evaluation responses, issued-certificate record, and no-PHI attestations.")
    L.append("")

    L.append("### 9. Recordkeeping Model")
    L.append("")
    L.append("Provider/CE records retained **>=4 years** (institutional posture 5 years; transcripts "
             "indefinitely) at 419 E. Hamilton Ave., Campbell, CA 95008. Records custodian: **Yadvir "
             "Saandal** (per master packet). No blank certificates; certificates issued only after "
             "completion criteria are met; learners instructed to retain the certificate for four years. "
             "Audit evidence exported per learner at certificate issuance and as a full-course export "
             "quarterly. **No PHI** is stored in any evidence artifact.")
    L.append("")

    L.append("### 10. No-PHI Policy")
    L.append("")
    L.append("All instructional cases are fictional and de-identified. Learners must never enter real "
             "patient/resident/family/employer/facility information. Site/course banners and assignment "
             "reminders restate the rule; faculty perform a PHI spot-check before grading and a manual "
             "PHI review of the capstone; a learner no-PHI attestation is required.")
    L.append("")

    L.append("### 11. Draft Flyer / Brochure Copy")
    L.append("")
    L.append("> **Draft - Pending BRN CEP Approval.** " + PLACEHOLDER)
    L.append("")
    L.append("**CI Institute of Nursing** - 419 E. Hamilton Ave., Campbell, CA 95008 - 650-449-6706 - "
             "humanresources@ci-ion.com - https://www.ci-ion.com")
    L.append("")
    L.append(f"**Course title:** {COURSE}")
    L.append("")
    L.append("**Who it's for:** California RNs in (or preparing for) care management, case management, "
             "home-health coordination, intake, discharge planning, quality review, or patient advocacy.")
    L.append("")
    L.append("**Description:** A practical, fully online CE course. Across ten modules you will strengthen "
             "nurse-led care coordination, patient-centered assessment and care planning, audit-ready "
             "documentation, advocacy and ethics, safe transitions, utilization review, and quality/risk "
             "management - applied through fictional, de-identified cases.")
    L.append("")
    L.append("**Learning objectives (summary):** Coordinate care across disciplines and settings; "
             "document to an audit-ready standard; protect patient rights and advocate ethically; plan safe "
             "transitions; support medical necessity in nursing terms; and manage high-risk, chronic, and "
             "geriatric patients.")
    L.append("")
    L.append("**Draft contact hours:** 30 contact hours *(draft design math; not 'approved for' any hours "
             "until a BRN CEP number is issued)*. **Delivery:** Online, self-paced via Moodle; 80% pass "
             "requirement. **Completion:** all 10 modules, all knowledge checks and the final exam at "
             ">=80%, the capstone, and the course evaluation.")
    L.append("")
    L.append("**Refund/cancellation (placeholder):** Written cancellation honored through the first "
             "session or the 7th calendar day after enrollment, whichever is later; pro-rata refund when "
             "<=60% completed; refunds within 45 days.")
    L.append("")
    L.append("**Notices:** Does **not** grant a case management certification, CCM certification, "
             "social-work license credit, or any scope expansion - RN continuing education only. "
             "**No PHI:** all examples are fictional and de-identified.")
    L.append("")

    L.append("### 12. Draft Certificate Text")
    L.append("")
    L.append("> Draft certificate - Pending BRN CEP Approval. Not for issuance until a CEP number is "
             "issued. No blank certificates.")
    L.append("")
    L.append("```")
    L.append("CI INSTITUTE OF NURSING")
    L.append("Certificate of Completion - Continuing Education for Registered Nurses")
    L.append("")
    L.append("This certifies that  ______________________________  [Learner Full Name]")
    L.append("")
    L.append("has successfully completed:")
    L.append(f"  {COURSE}")
    L.append("")
    L.append("Completion date: ____________________")
    L.append("Contact hours:   [____ contact hours - placeholder until BRN CEP approval]")
    L.append("")
    L.append("Provider: CI Institute of Nursing")
    L.append("BRN CEP Provider Number: [CEP # PENDING - placeholder until issued by the")
    L.append("California Board of Registered Nursing. Do not represent as approved until issued.]")
    L.append("")
    L.append("Authorized signature: ____________________   Title: ____________________")
    L.append("")
    L.append("RETENTION NOTICE: Please retain this certificate of completion for FOUR (4) YEARS.")
    L.append("")
    L.append("This course is continuing education only. It does not grant a case management")
    L.append("certification, CCM certification, social work license credit, or any scope")
    L.append("expansion. All instructional cases are fictional and de-identified.")
    L.append("```")
    L.append("")
    L.append("Required elements present: learner name, course title, completion date, provider-name "
             "placeholder, BRN CEP number placeholder, contact-hours placeholder, signature/title "
             "placeholder, 4-year retention statement, approval-placeholder language, and "
             "no-certification/no-scope statement. No real provider number is used (none exists in the "
             "master packet).")
    L.append("")

    L.append("### 13. Course Evaluation Form")
    L.append("")
    L.append("Delivered as a Moodle Feedback activity; required for completion.")
    L.append("")
    L.append("**Part 1 - Objective achievement (1=strongly disagree ... 5=strongly agree):**")
    L.append("1. The stated learning objectives were met.")
    L.append("2. Content was relevant to my registered-nursing practice in care/case management.")
    L.append("3. The contact-hour/time commitment matched the workload.")
    L.append("4. Scenarios and exercises improved my applied judgment.")
    L.append("5. Documentation practice was useful and realistic.")
    L.append("6. The course was free of commercial bias.")
    L.append("7. Materials were accessible and easy to navigate (mobile included).")
    L.append("")
    L.append("**Part 2 - Instruction & design:** 8. Instructor/SME content was clear and credible. "
             "9. Assessments fairly measured the objectives. 10. Feedback/remediation was helpful.")
    L.append("")
    L.append("**Part 3 - Open response:** 11. Most valuable? 12. What to improve? 13. Any concerns about "
             "accuracy, accessibility, or content?")
    L.append("")
    L.append("**Part 4 - Attestation (required checkbox):** 'I confirm I completed the activities myself "
             "and did not submit any real patient information (no PHI).'")
    L.append("")

    L.append("### 14. SME / Compliance Checklist")
    L.append("")
    L.append(md_table(
        ["#", "Item", "Module(s)", "Reviewer", "Status"],
        [["S1", "RN scope statements accurate/current", "M01", "SME", "Pending"],
         ["S2", "Assessment frameworks & care-plan template current", "M02", "SME", "Pending"],
         ["S3", "Handoff/SBAR examples reflect practice", "M03", "SME", "Pending"],
         ["S4", "Documentation/legal-charting standards correct", "M04", "SME + Legal", "Pending"],
         ["S5", "Consent/advocacy/ethics correct", "M05", "SME + Legal", "Pending"],
         ["S6", "Discharge/teach-back content correct", "M06", "SME", "Pending"],
         ["S7", "Medical-necessity stays in nursing lane", "M07", "SME + Compliance", "Pending"],
         ["S8", "QA/risk patient-safety framed", "M08", "SME + Compliance", "Pending"],
         ["S9", "Chronic/geriatric content current & education-only", "M09", "SME", "Pending"],
         ["S10", "Capstone rubric & final items valid/fair", "M10", "SME", "Pending"],
         ["C1", "Placeholder approval language everywhere", "All", "Compliance", "Drafted"],
         ["C2", "'Contact hours' not 'CEUs'; no 'approved for' claims", "All", "Compliance", "Drafted"],
         ["C3", "Each module >=150 min; none <60; 30-hr math correct", "All", "Compliance", "Verified"],
         ["C4", "Certificate 4-yr retention; no blank certificates", "All", "Compliance/Legal", "Drafted"],
         ["C5", "No PHI; all cases fictional/de-identified", "All", "Compliance/Privacy", "Designed-in"],
         ["C6", "No certification/scope-expansion claims", "All", "Compliance/Legal", "Drafted"],
         ["C7", "80% threshold; no learner key; internal key separated", "All", "Faculty/Admin", "Designed-in"],
         ["C8", "Offering-type & contact-hour discrepancy vs. packet reconciled", "All", "SME/Compliance", "OPEN"],
         ["C9", "Accessibility (WCAG 2.1 AA) verified on build", "All", "Accessibility", "Pending"]]))
    L.append("")

    L.append("### 15. Open Items Requiring Confirmation Before Submission")
    L.append("")
    L.append("1. **Offering-type reconciliation:** contact hours are reconciled at 30 contact hours across "
             "the official BRN contact-hour map, transfer worksheet, and this design. Delivery mode still "
             "differs (worksheet: live webinar / live-stream; this design: online self-paced); confirm the "
             "intended delivery mode before submission. [[SME REVIEW REQUIRED]]")
    L.append("2. **Offering type / independent-study:** confirm BRN independent-study methodology "
             "requirements if delivered online self-paced.")
    L.append("3. **Instructor evidence (Vanessa Valerio, RN 788389):** license expiration, education, "
             "experience, teaching experience, adult-education info - all **Needs confirmation**.")
    L.append("4. **SME of record for the expanded 30-hour scope** (especially CM-M07/CM-M08) - "
             "**Needs confirmation**.")
    L.append("5. **Prior California nursing CE provider history** answer - final verification.")
    L.append("6. **CE coordinator designation** - final verification.")
    L.append("7. **Course offer dates / schedule** - **Needs confirmation**.")
    L.append("8. **Legal/privacy sign-off** on policy + certificate wording - pending.")
    L.append("9. **$750 payment/check attachment** confirmation - pending.")
    L.append("10. **BRN CEP number** - **not issued**; all approval language stays placeholder until issued.")
    L.append("11. **Final-exam & knowledge-check item bank** - blueprinted here; full item text + "
             "validated internal key require SME authoring/sign-off.")
    L.append("")
    L.append("**Confirmed from packet (source of truth):** provider identity, address/phone/email/website, "
             "FEIN, corporation status, records custodian (Yadvir Saandal), instructor of record "
             "(Vanessa Valerio, RN 788389), refund/cancellation/recordkeeping policy, certificate required "
             "elements + 4-year retention, $750 fee.")
    L.append("")
    L.append("### 16. Individual Module Documentation Index")
    L.append("")
    L.append(md_table(["Module ID", "Title", "PDF file"],
                      [[m["id"], m["title"], m["file"] + ".pdf"] for m in MODULES]))
    L.append("")
    L.append("---")
    L.append("")
    L.append(FOOTER)
    return "\n".join(L)


# --------------------------------------------------------------------- DRIVER
def write_pair(basename, md_text):
    md_path = os.path.join(OUT, basename + ".md")
    pdf_path = os.path.join(OUT, basename + ".pdf")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    markdown_to_pdf(md_text, pdf_path)
    return basename


def main():
    written = []
    written.append(write_pair("BRN_CM_CE_30HR_Course_Documentation_Packet", course_md()))
    for m in MODULES:
        written.append(write_pair(m["file"], module_md(m)))
    # conversion README
    readme = README_TEXT
    with open(os.path.join(OUT, "README_PDF_CONVERSION.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    print("Generated PDF-ready .md + .pdf for:")
    for w in written:
        print("  -", w)
    print(f"Output folder: {OUT}")


README_TEXT = """# PDF-Ready Module Documentation Packet - Conversion Notes

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
"""


if __name__ == "__main__":
    main()
