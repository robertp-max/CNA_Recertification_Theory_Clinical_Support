# -*- coding: utf-8 -*-
"""
Single-source structured data for the RCFE Administrator Renewal CE package.

SCOPE: California RCFE Administrator renewal continuing education ONLY.
STATUS: Draft / Application Packet / Pending CDSS/ACS Approval.

This module is the build-support source of truth for:
  - RCFE_Admin_CE_LMS_BUILD_WORKBOOK.xlsx
  - the /pdf-ready/ module documentation packet
  - Section G (Detailed Module Blueprints) of the primary markdown package

Packet facts (vendor identity, instructor, format) are sourced from the Git repo
master application packet:
  __Master-Application-Packet/02_RCFE_CDSS_CETP_PACKET/
Do NOT invent packet facts. Anything not in the master packet is marked
"Needs confirmation".
"""

DRAFT_BANNER = "RCFE Administrator Renewal CE Package - Draft / Pending CDSS/ACS Approval"

PENDING_LANGUAGE = (
    "Pending CDSS/ACS approval. Do not advertise, issue certificates, or represent this "
    "course as approved until the applicable vendor/course approval has been issued."
)

CLOSING_LANGUAGE = (
    "Do not advertise, issue certificates, or represent this course as CDSS/ACS-approved "
    "until the official vendor/course approval is issued."
)

# ---------------------------------------------------------------------------
# Packet facts sourced from master application packet (source of truth)
# ---------------------------------------------------------------------------
PACKET_FACTS = {
    "provider_vendor_name": "CI Institute of Nursing, Inc.",
    "address": "419 E. Hamilton Ave., Campbell, CA 95008",
    "authorized_representative": "Maria Divina Bustos",
    "business_phone": "650-449-6706",
    "email": "humanresources@ci-ion.com",
    "company_type": "Corporation",
    "bppe": "BPPE 94886",
    "program_type": "RCFE",
    "vendor_type": "CETP (Continuing Education Training Program)",
    "vendor_number": "To be assigned after vendor approval (placeholder)",
    "course_number": "N/A - initial course approval request (placeholder)",
    "instructor_of_record": "Vanessa Valerio, RN 788389",
    "default_format": "Live-Stream (live/instructor-interactive) per existing RCFE packet posture",
    "source_path": "__Master-Application-Packet/02_RCFE_CDSS_CETP_PACKET/",
}

COURSE = {
    "title": ("RCFE Administrator Renewal CE: Resident Safety, Dementia Care, "
              "Operations, Compliance, and Quality Leadership"),
    "audience": "California RCFE Administrators renewing their administrator certificate",
    "status": "Draft / Pending CDSS/ACS Approval",
    "total_hours": 40,
    "total_minutes": 2400,
    "self_paced_cap_hours": 20,
    "self_paced_planned_hours": 17,
    "self_paced_buffer_hours": 3,
    "instructor_interactive_hours": 23,
    "dementia_required_hours": 8,
    "dementia_planned_hours": 8,
    "pass_threshold_pct": 80,
    "minutes_per_ce_hour": 60,
    "min_module_minutes": 60,
    "completion_record_retention_years": 3,
    "certificate_renewal_cycle": "Every two years (RCFE Administrator certificate)",
}

# RCFE Administrator uniform core of knowledge areas used for mapping.
# Aligned to the RCFE CETP catalog categories found in the master packet and the
# RCFE administrator core-of-knowledge framework. Verify final wording against
# current CDSS/ACS source materials before submission ("Needs confirmation").
CORE_KNOWLEDGE_AREAS = [
    "Laws, Regulations, Policies, and Procedural Standards Impacting RCFE",
    "Business Operations",
    "Management/Supervision of Staff",
    "Psychosocial Needs of Residents",
    "Physical Needs of Residents",
    "Community Resources / Support Services",
    "Medication Management",
    "Resident Admission, Retention, and Assessment Procedures",
    "Managing Alzheimer's Disease and Related Dementias",
    "Residents' Rights",
    "Managing the Physical Environment (Including Emergency Procedures)",
    "Cultural Competency (Including LGBT) and Abuse Prevention",
]

# ---------------------------------------------------------------------------
# Module blueprints (single source of truth for all deliverables)
# ---------------------------------------------------------------------------
# Delivery values: "Self-paced online" | "Live / instructor-interactive"
MODULES = [
    {
        "id": "M01",
        "title": "RCFE Laws, Regulations, Policies, and Procedural Standards",
        "ce_hours": 4,
        "minutes": 240,
        "delivery": "Self-paced online",
        "core_knowledge": ["Laws, Regulations, Policies, and Procedural Standards Impacting RCFE"],
        "dementia_hours": 0,
        "description": (
            "Self-paced review of the statutory and regulatory framework governing California "
            "Residential Care Facilities for the Elderly (Health & Safety Code Division 2, "
            "Chapter 3.2 and Title 22, Division 6, Chapter 8), licensing authority, citation and "
            "appeal processes, mandated postings, and the administrator's duty to maintain "
            "current policies and procedures. Renewal-level refresher; does not grant initial "
            "certification."),
        "compliance_rationale": (
            "Maps directly to the 'Laws, Regulations, Policies, and Procedural Standards "
            "Impacting RCFE' uniform core-of-knowledge area required for RCFE administrator "
            "renewal CE. Self-paced is defensible because content is didactic, regulation-based, "
            "and includes an interactive feedback portion plus identity confirmation."),
        "objectives": [
            "Identify the licensing authority and the primary statutes and regulations that govern RCFE operation.",
            "Differentiate between Type A, Type B, and Type C deficiencies and the associated civil penalty and appeal timelines.",
            "Locate at least five mandated facility postings and the legal basis for each.",
            "Given a regulatory scenario, determine the administrator's required reporting or corrective action and timeline.",
            "Update a facility policy statement so that it is consistent with current RCFE regulatory requirements.",
        ],
        "lessons": [
            {"id": "M01-L1", "title": "Regulatory Framework and Licensing Authority", "minutes": 55,
             "objective": "Identify the licensing authority and primary statutes/regulations governing RCFEs.",
             "activity_type": "Narrated reading + glossary", "moodle": "Page + Book + Glossary",
             "completion": "View all pages; add 1 glossary entry",
             "summary": "HSC Division 2 Ch 3.2, Title 22 Div 6 Ch 8, CDSS/Community Care Licensing role, scope vs. ARF/ADHC."},
            {"id": "M01-L2", "title": "Inspections, Citations, Civil Penalties, and Appeals", "minutes": 55,
             "objective": "Differentiate deficiency types and associated penalty/appeal timelines.",
             "activity_type": "Interactive lesson with branching feedback", "moodle": "Lesson (branching)",
             "completion": "Complete lesson; achieve feedback checkpoints",
             "summary": "Type A/B deficiencies, immediate vs. non-immediate jeopardy, plan of correction, appeal rights and timelines."},
            {"id": "M01-L3", "title": "Mandated Postings, Disclosures, and Recordkeeping Duties", "minutes": 55,
             "objective": "Locate mandated postings and the legal basis for each.",
             "activity_type": "Interactive checklist + drag-and-drop match", "moodle": "H5P (drag the words)",
             "completion": "Score recorded on H5P activity",
             "summary": "License posting, complaint poster/ombudsman number, emergency disclosure plan, resident records retention duties."},
            {"id": "M01-L4", "title": "Applied Compliance: Policy Updates and Administrator Action", "minutes": 75,
             "objective": "Given a scenario, determine required action/timeline and update a policy statement.",
             "activity_type": "Scenario + documentation exercise", "moodle": "Assignment (file/online text) + Quiz",
             "completion": "Submit policy-update exercise; pass knowledge check >=80%",
             "summary": "Fictional facility receives a deficiency notice; learner drafts a corrected policy and plan-of-correction outline."},
        ],
        "key_terms": ["Community Care Licensing Division (CCLD)", "Title 22", "Health & Safety Code 1569 et seq.",
                      "Type A / Type B deficiency", "Plan of Correction (POC)", "Civil penalty", "Ombudsman",
                      "Notice of Deficiency", "Unusual incident report"],
        "scenario": (
            "Fictional, de-identified: Maplewood Garden RCFE (license #00-FAKE-001) receives a Notice of "
            "Deficiency after an unannounced visit found an expired emergency disclosure plan and a missing "
            "ombudsman poster. No real facility, resident, or staff data is used."),
        "activities": [
            "Branching lesson where each wrong path returns regulation-based feedback before allowing retry.",
            "Drag-and-drop matching of mandated postings to their legal basis.",
            "Policy-update assignment with rubric.",
        ],
        "doc_exercise": (
            "Learner drafts a one-page Plan of Correction outline for the fictional deficiency, "
            "specifying corrective action, responsible party, completion date, and how recurrence "
            "will be prevented. No real facility data permitted."),
        "knowledge_check": {
            "blueprint": "8-item low-stakes auto-graded check; unlimited attempts; feedback on each item; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "Which entity is the primary licensing authority for California RCFEs?",
                 "choices": ["A. CDPH Licensing & Certification", "B. CDSS Community Care Licensing Division",
                             "C. Board of Registered Nursing", "D. The county ombudsman"],
                 "answer": "B",
                 "rationale": "RCFEs are licensed by CDSS Community Care Licensing Division; CDPH licenses health facilities; BRN licenses RNs.",
                 "remediation": "Re-review M01-L1 (Regulatory Framework and Licensing Authority)."},
                {"type": "MCQ", "stem": "A deficiency that presents an immediate or substantial threat to resident health/safety is generally classified as:",
                 "choices": ["A. Type B", "B. Minor", "C. Type A", "D. Advisory"],
                 "answer": "C",
                 "rationale": "Type A deficiencies present immediate/substantial hazard; Type B are less serious. Verify current penalty amounts against CDSS source ('Needs confirmation').",
                 "remediation": "Re-review M01-L2 (Inspections, Citations, Civil Penalties, and Appeals)."},
            ],
        },
        "completion_requirement": "View all lessons, pass the 8-item knowledge check at >=80%, and submit the Plan-of-Correction exercise.",
        "evidence_artifact": "Lesson completion log, knowledge-check score, submitted POC exercise, identity-confirmation record.",
        "moodle_activities": ["Page", "Book", "Lesson (branching)", "H5P", "Quiz", "Assignment", "Glossary"],
        "accessibility": [
            "All narrated content captioned and provided as accessible HTML/PDF transcript.",
            "Drag-and-drop H5P paired with a keyboard-accessible alternative (e.g., select-from-list).",
            "Color not sole means of conveying meaning; WCAG 2.1 AA contrast.",
        ],
        "privacy_notes": "All examples fictional/de-identified. No PHI or real resident, staff, or facility data. License numbers are obviously fake (00-FAKE-xxx).",
        "sme_flags": ["Confirm current Title 22 citation numbering and civil penalty amounts with CDSS source materials."],
        "compliance_flags": ["Self-paced: must include interactive feedback (branching lesson) and identity confirmation checkpoint."],
        "defensibility_notes": "Directly mirrors RCFE-CETP-001 catalog course; renewal-level refresher; clearly not initial certification.",
        "identity_confirmation": "PIN/identity attestation at module start and a second checkpoint before the knowledge check.",
        "interactive_feedback": "Branching lesson and H5P provide immediate input-based feedback; quiz shows per-item rationale after submission.",
    },
    {
        "id": "M02",
        "title": "Business Operations, Records, and Administrator Accountability",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Self-paced online",
        "core_knowledge": ["Business Operations"],
        "dementia_hours": 0,
        "description": (
            "Self-paced module on RCFE business operations: required business and resident records, "
            "fiscal accountability, admission agreements, fee disclosures, insurance/bonding, "
            "claim-safe communications, and the administrator's personal accountability for "
            "accurate recordkeeping and truthful representations."),
        "compliance_rationale": (
            "Maps to the 'Business Operations' core-of-knowledge area. Self-paced is defensible: "
            "didactic, document-centered content with interactive feedback and identity confirmation."),
        "objectives": [
            "List the categories of business and resident records an RCFE must maintain and the minimum retention periods.",
            "Explain the administrator's fiscal accountability and bonding/insurance obligations.",
            "Identify required elements of an RCFE admission agreement and fee disclosure.",
            "Given a communication scenario, rewrite a statement to be accurate and claim-safe.",
            "Construct a records-retention schedule for a fictional facility.",
        ],
        "lessons": [
            {"id": "M02-L1", "title": "Required Records and Retention", "minutes": 55,
             "objective": "List required business/resident records and retention periods.",
             "activity_type": "Book + interactive table", "moodle": "Book + H5P (interactive table)",
             "completion": "View all; complete table activity",
             "summary": "Resident records, personnel records, fiscal records, incident logs; retention minimums; storage and confidentiality."},
            {"id": "M02-L2", "title": "Admission Agreements, Fees, and Disclosures", "minutes": 55,
             "objective": "Identify required elements of admission agreements and fee disclosures.",
             "activity_type": "Annotated exemplar + branching lesson", "moodle": "Lesson (branching)",
             "completion": "Complete lesson checkpoints",
             "summary": "Required agreement terms, rate-change notice, refund handling, third-party services, prohibited terms."},
            {"id": "M02-L3", "title": "Accountability and Claim-Safe Communication", "minutes": 70,
             "objective": "Rewrite statements to be accurate/claim-safe; build a retention schedule.",
             "activity_type": "Scenario + documentation exercise", "moodle": "Assignment + Quiz",
             "completion": "Submit retention schedule; pass knowledge check >=80%",
             "summary": "Truthful marketing, avoiding overclaiming services, accurate occupancy/financial reporting, falsification consequences."},
        ],
        "key_terms": ["Admission agreement", "Rate change notice", "Surety bond (resident trust)", "Records retention schedule",
                      "Fiscal accountability", "Claim-safe communication", "Material misrepresentation"],
        "scenario": (
            "Fictional: A family asks Riverbend RCFE whether the facility 'guarantees' a resident will never "
            "be hospitalized. Learner identifies the overclaim risk and rewrites a truthful, claim-safe response. "
            "All data fictional/de-identified."),
        "activities": ["Interactive records-retention table", "Branching admission-agreement review",
                       "Claim-safe communication rewrite assignment"],
        "doc_exercise": "Build a records-retention schedule (record type, retention period, storage location, responsible role) for a fictional facility.",
        "knowledge_check": {
            "blueprint": "7-item low-stakes auto-graded check; unlimited attempts; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "Which statement is the most claim-safe response to a prospective family?",
                 "choices": ["A. 'We guarantee your parent will never fall.'", "B. 'We provide care and a service plan designed to reduce fall risk.'",
                             "C. 'We are the safest facility in California.'", "D. 'Hospitalization never happens here.'"],
                 "answer": "B",
                 "rationale": "B is accurate and avoids guarantees/superlatives that create liability and misrepresentation risk.",
                 "remediation": "Re-review M02-L3 (Accountability and Claim-Safe Communication)."},
            ],
        },
        "completion_requirement": "View all lessons, pass the 7-item check at >=80%, and submit the retention-schedule exercise.",
        "evidence_artifact": "Completion log, knowledge-check score, submitted retention schedule, identity-confirmation record.",
        "moodle_activities": ["Book", "H5P", "Lesson", "Assignment", "Quiz"],
        "accessibility": ["Captioned media + transcripts", "Keyboard-accessible interactive table", "WCAG 2.1 AA contrast"],
        "privacy_notes": "Fictional facilities/families only; no real financial or resident data.",
        "sme_flags": ["Confirm current surety bond thresholds and admission-agreement mandatory terms with CDSS source."],
        "compliance_flags": ["Self-paced: interactive feedback + identity confirmation required."],
        "defensibility_notes": "Mirrors RCFE-CETP-009 (Business Operations, Records, and Claim-Safe Communications).",
        "identity_confirmation": "PIN/attestation at start; second checkpoint before knowledge check.",
        "interactive_feedback": "Branching lesson and per-item quiz feedback based on learner input.",
    },
    {
        "id": "M03",
        "title": "Management, Supervision of Staff, Training Records, and Workplace Oversight",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": ["Management/Supervision of Staff"],
        "dementia_hours": 0,
        "description": (
            "Live/instructor-interactive module on staff management: hiring and qualification "
            "verification, required staff training and orientation, supervision and scheduling for "
            "adequate staffing, performance management, mandated-reporter training oversight, and "
            "maintenance of complete training records. Delivered live to allow facilitated "
            "discussion and peer interaction."),
        "compliance_rationale": (
            "Maps to 'Management/Supervision of Staff'. Live delivery is required so participants "
            "can interact simultaneously with the instructor and each other (supervision role-play, "
            "case discussion), supporting the non-self-paced hour requirement."),
        "objectives": [
            "Verify that staff qualification and training records meet RCFE requirements before assignment.",
            "Design a staffing/supervision plan that maintains adequate coverage across shifts.",
            "Apply a progressive performance-management approach to a fictional staff issue.",
            "Audit a training-records file and identify gaps requiring correction.",
            "Demonstrate, in a live exercise, supervisory feedback that is specific, documented, and respectful.",
        ],
        "lessons": [
            {"id": "M03-L1", "title": "Hiring, Qualifications, and Records (Facilitated)", "minutes": 55,
             "objective": "Verify staff qualification/training records meet requirements.",
             "activity_type": "Live presentation + polling", "moodle": "BigBlueButton/Zoom (LTI) + Choice poll",
             "completion": "Attendance + live poll responses logged",
             "summary": "Criminal record clearances, required orientation/in-service hours, TB clearance, training-record contents."},
            {"id": "M03-L2", "title": "Staffing, Supervision, and Performance Management", "minutes": 55,
             "objective": "Design staffing/supervision plan; apply progressive performance management.",
             "activity_type": "Facilitated breakout discussion", "moodle": "Live breakout + Forum (debrief)",
             "completion": "Breakout participation + forum post",
             "summary": "Adequate staffing, scheduling for acuity, documentation of supervision, progressive discipline."},
            {"id": "M03-L3", "title": "Supervisory Skills Role-Play and Training-File Audit", "minutes": 70,
             "objective": "Audit a training file; demonstrate documented supervisory feedback.",
             "activity_type": "Live role-play + audit exercise", "moodle": "Live session + Assignment upload",
             "completion": "Role-play participation + submitted audit findings",
             "summary": "Learners audit a fictional training file and conduct a recorded-by-notes supervisory feedback role-play."},
        ],
        "key_terms": ["Criminal record clearance/exemption", "Orientation and in-service hours", "Adequate staffing",
                      "Progressive discipline", "Training record", "Supervision documentation", "Mandated reporter"],
        "scenario": (
            "Fictional: A new caregiver at Oakhaven RCFE missed two required in-service trainings and a shift "
            "handoff was incomplete. In live breakout, teams design a corrective supervision plan. All fictional."),
        "activities": ["Live polling on qualification scenarios", "Breakout staffing-plan design",
                       "Supervisory feedback role-play", "Training-file audit exercise"],
        "doc_exercise": "Complete a training-file audit worksheet for a fictional employee and list each gap with the corrective action and deadline.",
        "knowledge_check": {
            "blueprint": "6-item check delivered post-session (auto-graded); per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "Before a new caregiver may work independently, the administrator must first confirm:",
                 "choices": ["A. The caregiver's social media history", "B. Criminal record clearance/exemption and required orientation are documented",
                             "C. That the caregiver owns a car", "D. Nothing; documentation can follow later"],
                 "answer": "B",
                 "rationale": "Clearance and required orientation must be documented before independent assignment; documentation cannot be deferred.",
                 "remediation": "Re-review M03-L1 (Hiring, Qualifications, and Records)."},
            ],
        },
        "completion_requirement": "Attend the live session (attendance evidence captured), participate in breakout/role-play, and pass the 6-item check at >=80%.",
        "evidence_artifact": "Live attendance log + engagement timestamps, breakout/forum participation, submitted audit worksheet, knowledge-check score.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Choice", "Forum", "Assignment", "Quiz", "Attendance"],
        "accessibility": ["Live captioning (CART) offered", "Materials posted in advance in accessible formats",
                          "Alternative participation path for learners who cannot use breakout audio"],
        "privacy_notes": "Role-play uses fictional employees; no real personnel data discussed.",
        "sme_flags": ["Confirm current required orientation/in-service hour counts for RCFE staff with CDSS source."],
        "compliance_flags": ["Live/instructor-interactive: must capture simultaneous-interaction attendance evidence."],
        "defensibility_notes": "Mirrors RCFE-CETP-008; live delivery satisfies the instructional-setting interaction requirement.",
        "identity_confirmation": "Live identity verification at join (name/credential check against roster).",
        "interactive_feedback": "Real-time instructor feedback during role-play and breakout debrief.",
    },
    {
        "id": "M04",
        "title": "Psychosocial Needs, Resident-Centered Care, and Community Support Services",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": ["Psychosocial Needs of Residents", "Community Resources / Support Services"],
        "dementia_hours": 0,
        "description": (
            "Live/instructor-interactive module on the psychosocial needs of older adults: dignity, "
            "autonomy, meaningful activity, depression and isolation recognition, family dynamics, "
            "and connecting residents to community support services (ombudsman, APS, hospice, "
            "behavioral health, faith and cultural communities). Delivered live to enable "
            "facilitated case discussion and peer learning."),
        "compliance_rationale": (
            "Maps to 'Psychosocial Needs of Residents' and 'Community Resources / Support Services'. "
            "Live delivery enables simultaneous interaction required for non-self-paced hours."),
        "objectives": [
            "Recognize signs of depression, anxiety, and social isolation in older residents.",
            "Design a person-centered activity plan that reflects resident preferences and culture.",
            "Match resident needs to appropriate community support services and referral pathways.",
            "Facilitate a family communication approach that preserves resident autonomy.",
            "Apply a resident-centered framework to a live case discussion.",
        ],
        "lessons": [
            {"id": "M04-L1", "title": "Psychosocial Needs and Recognizing Distress (Facilitated)", "minutes": 55,
             "objective": "Recognize depression, anxiety, and isolation signs.",
             "activity_type": "Live presentation + polling", "moodle": "BigBlueButton/Zoom (LTI) + Choice",
             "completion": "Attendance + poll responses",
             "summary": "Normal aging vs. depression, isolation risk factors, screening awareness (not diagnosis), referral triggers."},
            {"id": "M04-L2", "title": "Person-Centered Activities and Family Dynamics", "minutes": 55,
             "objective": "Design a person-centered activity plan; manage family communication.",
             "activity_type": "Facilitated breakout", "moodle": "Live breakout + Forum",
             "completion": "Breakout participation + forum post",
             "summary": "Preference-based activities, cultural/spiritual needs, autonomy vs. family wishes, dignity of risk."},
            {"id": "M04-L3", "title": "Community Resources Mapping and Live Case", "minutes": 70,
             "objective": "Match needs to community services; apply framework to a live case.",
             "activity_type": "Live case + resource-mapping exercise", "moodle": "Live session + Assignment",
             "completion": "Case participation + submitted resource map",
             "summary": "Ombudsman, APS, hospice, behavioral health, transportation, benefits programs and referral pathways."},
        ],
        "key_terms": ["Person-centered care", "Dignity of risk", "Social isolation", "Ombudsman", "Adult Protective Services (APS)",
                      "Community-based services", "Autonomy"],
        "scenario": (
            "Fictional: A resident at Birchwood RCFE has stopped attending meals and activities after a "
            "roommate move. Teams design a person-centered re-engagement plan and identify community "
            "supports. All details fictional/de-identified."),
        "activities": ["Live polling on distress recognition", "Activity-plan breakout", "Community-resource mapping exercise"],
        "doc_exercise": "Create a person-centered re-engagement plan with goals, preferred activities, responsible staff, and at least two community referrals.",
        "knowledge_check": {
            "blueprint": "6-item check post-session; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "A resident withdraws from meals/activities after a change. The MOST resident-centered first step is to:",
                 "choices": ["A. Require attendance at all activities", "B. Explore the resident's preferences and recent changes, then tailor re-engagement",
                             "C. Notify the family the resident is non-compliant", "D. Document and take no action"],
                 "answer": "B",
                 "rationale": "Person-centered care begins with understanding the individual's preferences/changes before tailoring an approach.",
                 "remediation": "Re-review M04-L2 (Person-Centered Activities)."},
            ],
        },
        "completion_requirement": "Attend live session, participate in breakout/case, submit re-engagement plan, pass 6-item check at >=80%.",
        "evidence_artifact": "Attendance/engagement log, breakout/forum participation, submitted re-engagement plan, knowledge-check score.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Choice", "Forum", "Assignment", "Quiz", "Attendance"],
        "accessibility": ["Live captioning offered", "Pre-posted accessible materials", "Non-audio participation alternative"],
        "privacy_notes": "Fictional residents/families only; no PHI.",
        "sme_flags": ["Confirm current ombudsman/APS referral expectations and any required disclosures with CDSS source."],
        "compliance_flags": ["Live/instructor-interactive: simultaneous interaction evidence required."],
        "defensibility_notes": "Renewal-level psychosocial/community content within RCFE core of knowledge.",
        "identity_confirmation": "Live roster/credential verification at join.",
        "interactive_feedback": "Instructor real-time feedback in case discussion.",
    },
    {
        "id": "M05",
        "title": "Physical Needs, Aging Changes, Restricted Health Conditions, and Hospice Awareness",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Self-paced online",
        "core_knowledge": ["Physical Needs of Residents"],
        "dementia_hours": 0,
        "description": (
            "Self-paced module on the physical needs of aging residents: normal vs. abnormal aging "
            "changes, mobility and fall-risk awareness, nutrition and hydration, skin integrity, "
            "incontinence care dignity, restricted health conditions that require physician/ "
            "waiver oversight, and hospice/end-of-life care awareness within RCFE scope. "
            "Awareness-level for administrators, not clinical training."),
        "compliance_rationale": (
            "Maps to 'Physical Needs of Residents'. Self-paced is defensible: knowledge-based "
            "awareness content with interactive feedback and identity confirmation."),
        "objectives": [
            "Distinguish normal aging changes from warning signs requiring escalation.",
            "Identify restricted health conditions and the documentation/waiver oversight an RCFE must have.",
            "Describe the administrator's role in supporting hospice care within RCFE scope.",
            "Apply fall-risk and skin-integrity awareness to a fictional service-plan decision.",
            "Determine when a condition exceeds RCFE care capability and requires escalation.",
        ],
        "lessons": [
            {"id": "M05-L1", "title": "Aging Changes and Warning Signs", "minutes": 55,
             "objective": "Distinguish normal aging from warning signs.",
             "activity_type": "Book + interactive scenarios", "moodle": "Book + H5P (branching scenario)",
             "completion": "View all; complete H5P",
             "summary": "Sensory, mobility, cognition, cardiovascular changes; red-flag symptoms; when to escalate."},
            {"id": "M05-L2", "title": "Restricted Health Conditions and Oversight", "minutes": 55,
             "objective": "Identify restricted conditions and required oversight/documentation.",
             "activity_type": "Interactive lesson with feedback", "moodle": "Lesson (branching)",
             "completion": "Complete lesson checkpoints",
             "summary": "Restricted conditions, physician orders, hospice waiver, incidental medical care boundaries, documentation."},
            {"id": "M05-L3", "title": "Hospice Awareness and Care-Capability Decisions", "minutes": 70,
             "objective": "Describe hospice support role; decide when condition exceeds capability.",
             "activity_type": "Scenario + decision exercise", "moodle": "Assignment + Quiz",
             "completion": "Submit decision exercise; pass check >=80%",
             "summary": "Hospice agency coordination, comfort care, care-capability determination, escalation/transfer decisions."},
        ],
        "key_terms": ["Restricted health condition", "Hospice waiver", "Incidental medical care", "Fall risk",
                      "Skin integrity", "Care capability determination", "Activities of daily living (ADLs)"],
        "scenario": (
            "Fictional: A resident at Cedar Point RCFE develops a stage-2 pressure area and increased "
            "confusion. Learner decides whether the facility can continue to meet needs with hospice "
            "support or must escalate. All fictional/de-identified."),
        "activities": ["Branching aging-change scenarios", "Restricted-condition oversight lesson", "Care-capability decision exercise"],
        "doc_exercise": "Complete a care-capability decision worksheet documenting the condition, current capability, required supports, and escalation decision.",
        "knowledge_check": {
            "blueprint": "7-item check; unlimited attempts; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "An RCFE may retain a resident with a restricted health condition only when:",
                 "choices": ["A. The family insists", "B. Required physician orders/approvals and a hospice waiver or appropriate oversight are in place and the facility can meet the need",
                             "C. The condition is hidden from the licensing agency", "D. Never, under any circumstance"],
                 "answer": "B",
                 "rationale": "Retention with restricted conditions requires the proper orders/waivers/oversight AND demonstrated care capability. Verify specifics with CDSS source.",
                 "remediation": "Re-review M05-L2 (Restricted Health Conditions and Oversight)."},
            ],
        },
        "completion_requirement": "View all lessons, pass the 7-item check at >=80%, submit care-capability worksheet.",
        "evidence_artifact": "Completion log, knowledge-check score, submitted worksheet, identity-confirmation record.",
        "moodle_activities": ["Book", "H5P", "Lesson", "Assignment", "Quiz"],
        "accessibility": ["Captioned media + transcripts", "Keyboard-accessible H5P alternative", "Plain-language summaries"],
        "privacy_notes": "Fictional residents; no PHI; clinical detail kept at administrator-awareness level.",
        "sme_flags": ["Confirm current restricted-health-condition list and hospice waiver requirements with CDSS/Title 22 source."],
        "compliance_flags": ["Self-paced: interactive feedback + identity confirmation required."],
        "defensibility_notes": "Administrator-awareness scope; does not represent clinical/nursing training.",
        "identity_confirmation": "PIN/attestation at start; checkpoint before knowledge check.",
        "interactive_feedback": "Branching H5P/lesson and per-item quiz feedback.",
    },
    {
        "id": "M06",
        "title": "Medication Management, Psychotropic Medications, and Safety Oversight",
        "ce_hours": 4,
        "minutes": 240,
        "delivery": "Self-paced online",
        "core_knowledge": ["Medication Management"],
        "dementia_hours": 0,
        "description": (
            "Self-paced module on RCFE medication management oversight: centrally stored vs. "
            "self-administered medications, the limits of unlicensed staff assistance, medication "
            "records (MAR) accuracy, error/discrepancy response, controlled-substance security, and "
            "psychotropic/antipsychotic medication safety including informed consent and "
            "non-pharmacological alternatives. Administrator oversight scope, not clinical "
            "administration training."),
        "compliance_rationale": (
            "Maps to 'Medication Management'. Self-paced is defensible: policy/record-oversight "
            "content with interactive feedback and identity confirmation. Psychotropic-safety content "
            "reinforces (but is counted separately from) dementia hours."),
        "objectives": [
            "Differentiate self-administration, assistance with self-administration, and prohibited tasks for unlicensed staff.",
            "Audit a fictional MAR for completeness and identify discrepancies.",
            "Describe the required response to a medication error or discrepancy.",
            "Explain informed-consent and monitoring expectations for psychotropic/antipsychotic medications.",
            "Identify non-pharmacological alternatives that should be tried/documented before reliance on psychotropics.",
        ],
        "lessons": [
            {"id": "M06-L1", "title": "Medication Assistance Scope and Limits", "minutes": 55,
             "objective": "Differentiate self-admin, assistance, and prohibited tasks.",
             "activity_type": "Book + branching scenarios", "moodle": "Book + Lesson (branching)",
             "completion": "View all; complete lesson",
             "summary": "Assistance with self-administration boundaries, training requirements, what unlicensed staff may not do."},
            {"id": "M06-L2", "title": "Medication Records, Storage, and Error Response", "minutes": 55,
             "objective": "Audit a MAR; describe error/discrepancy response.",
             "activity_type": "Interactive MAR audit (H5P)", "moodle": "H5P + Page",
             "completion": "Complete MAR audit activity",
             "summary": "MAR accuracy, central storage, controlled-substance security/count, disposal, error reporting workflow."},
            {"id": "M06-L3", "title": "Psychotropic and Antipsychotic Medication Safety", "minutes": 70,
             "objective": "Explain consent/monitoring; identify non-pharmacological alternatives.",
             "activity_type": "Interactive lesson + scenario", "moodle": "Lesson + Assignment",
             "completion": "Complete lesson; submit alternatives plan",
             "summary": "Informed consent, chemical-restraint prohibition, monitoring for side effects, behavioral alternatives first."},
            {"id": "M06-L4", "title": "Applied Oversight: Discrepancy Investigation", "minutes": 60,
             "objective": "Apply oversight to investigate a discrepancy and document corrective action.",
             "activity_type": "Scenario + documentation exercise", "moodle": "Assignment + Quiz",
             "completion": "Submit investigation note; pass check >=80%",
             "summary": "Learner investigates a fictional missing-dose discrepancy and documents corrective and preventive action."},
        ],
        "key_terms": ["Assistance with self-administration", "Centrally stored medication", "MAR", "Chemical restraint",
                      "Psychotropic/antipsychotic medication", "Informed consent", "Controlled substance count", "PRN"],
        "scenario": (
            "Fictional: At Willow Creek RCFE the evening MAR shows an unexplained missing dose of a "
            "controlled medication. Learner conducts the oversight investigation and documents action. "
            "All fictional; no real medication/resident data."),
        "activities": ["Branching medication-scope scenarios", "Interactive MAR audit", "Psychotropic-alternatives plan", "Discrepancy investigation exercise"],
        "doc_exercise": "Document a medication-discrepancy investigation: facts, immediate action, root cause, corrective/preventive action, and notifications.",
        "knowledge_check": {
            "blueprint": "8-item check; unlimited attempts; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "Using a psychotropic medication primarily to control behavior for staff convenience, without a legitimate medical indication, is best described as:",
                 "choices": ["A. Acceptable PRN use", "B. A chemical restraint and prohibited", "C. Assistance with self-administration", "D. Standard fall prevention"],
                 "answer": "B",
                 "rationale": "Medicating for convenience/discipline without medical indication is a chemical restraint and is prohibited; non-pharmacological approaches and consent are required.",
                 "remediation": "Re-review M06-L3 (Psychotropic and Antipsychotic Medication Safety)."},
            ],
        },
        "completion_requirement": "View all lessons, pass the 8-item check at >=80%, submit the discrepancy-investigation note and alternatives plan.",
        "evidence_artifact": "Completion log, knowledge-check score, submitted investigation note + alternatives plan, identity-confirmation record.",
        "moodle_activities": ["Book", "Lesson", "H5P", "Page", "Assignment", "Quiz"],
        "accessibility": ["Captioned media + transcripts", "Accessible alternative to H5P MAR activity", "Plain-language definitions"],
        "privacy_notes": "Fictional MARs/residents; no real medication or resident data; PHI excluded.",
        "sme_flags": ["Confirm current assistance-with-self-administration rules and psychotropic consent/monitoring requirements with CDSS/Title 22 source."],
        "compliance_flags": ["Self-paced: interactive feedback + identity confirmation required.", "Pharmacology kept at administrator-oversight level - SME (RN) review advised."],
        "defensibility_notes": "Mirrors RCFE-CETP-005; oversight scope only, not medication-administration certification.",
        "identity_confirmation": "PIN/attestation at start; checkpoint before knowledge check.",
        "interactive_feedback": "Branching lessons, H5P MAR audit, and per-item quiz feedback.",
    },
    {
        "id": "M07",
        "title": "Admission, Retention, Reappraisal, and Needs and Services Planning",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Self-paced online",
        "core_knowledge": ["Resident Admission, Retention, and Assessment Procedures"],
        "dementia_hours": 0,
        "description": (
            "Self-paced module on the admission-to-retention lifecycle: pre-admission appraisal, "
            "physician report, the needs and services plan, ongoing reappraisal triggers, "
            "documentation of changing needs, and lawful, dignified relocation/eviction procedures "
            "when needs exceed facility capability."),
        "compliance_rationale": (
            "Maps to 'Resident Admission, Retention, and Assessment Procedures'. Self-paced is "
            "defensible: process/documentation content with interactive feedback and identity "
            "confirmation."),
        "objectives": [
            "Sequence the required steps and documents from pre-admission appraisal to admission.",
            "Construct a needs and services plan from a fictional appraisal.",
            "Identify reappraisal triggers and required documentation of changing needs.",
            "Apply lawful relocation/eviction procedures and notice requirements.",
            "Determine when a resident's needs exceed facility capability.",
        ],
        "lessons": [
            {"id": "M07-L1", "title": "Pre-Admission Appraisal and Required Documents", "minutes": 55,
             "objective": "Sequence admission steps/documents.",
             "activity_type": "Interactive sequence (H5P) + Book", "moodle": "H5P (sort) + Book",
             "completion": "Complete sequence activity",
             "summary": "Pre-admission appraisal, physician report (LIC 602A type), TB clearance, admission agreement linkage."},
            {"id": "M07-L2", "title": "Needs and Services Plan and Reappraisal", "minutes": 55,
             "objective": "Construct a needs/services plan; identify reappraisal triggers.",
             "activity_type": "Guided builder + branching lesson", "moodle": "Lesson + Assignment",
             "completion": "Submit drafted needs/services plan",
             "summary": "Plan elements, measurable supports, reappraisal triggers (condition change, incident, periodic)."},
            {"id": "M07-L3", "title": "Retention Limits and Lawful Relocation", "minutes": 70,
             "objective": "Apply relocation/eviction procedures; judge capability limits.",
             "activity_type": "Scenario + documentation exercise", "moodle": "Assignment + Quiz",
             "completion": "Submit relocation-decision exercise; pass check >=80%",
             "summary": "Eviction notice rules, relocation safeguards, appeal/ombudsman role, capability determination."},
        ],
        "key_terms": ["Pre-admission appraisal", "Physician report", "Needs and services plan", "Reappraisal",
                      "Retention", "Relocation/eviction notice", "Care capability"],
        "scenario": (
            "Fictional: A resident at Sunrise Meadow RCFE has had three falls and new wandering. Learner "
            "performs a reappraisal, updates the needs and services plan, and decides retention vs. lawful "
            "relocation. All fictional/de-identified."),
        "activities": ["Admission-document sequencing", "Needs/services plan builder", "Relocation-decision exercise"],
        "doc_exercise": "Draft an updated needs and services plan and a retention-vs-relocation decision memo (with notice/appeal steps if relocation).",
        "knowledge_check": {
            "blueprint": "7-item check; unlimited attempts; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "A reappraisal and update to the needs and services plan is required when:",
                 "choices": ["A. Only at annual review", "B. A resident's condition changes significantly (e.g., new falls/wandering) or after a significant incident",
                             "C. Only if the family requests it", "D. Never after admission"],
                 "answer": "B",
                 "rationale": "Significant condition changes/incidents trigger reappraisal and plan updates, in addition to periodic review.",
                 "remediation": "Re-review M07-L2 (Needs and Services Plan and Reappraisal)."},
            ],
        },
        "completion_requirement": "View all lessons, pass the 7-item check at >=80%, submit the needs/services plan and decision memo.",
        "evidence_artifact": "Completion log, knowledge-check score, submitted plan + decision memo, identity-confirmation record.",
        "moodle_activities": ["H5P", "Book", "Lesson", "Assignment", "Quiz"],
        "accessibility": ["Captioned media + transcripts", "Accessible sequencing alternative", "Template provided in accessible format"],
        "privacy_notes": "Fictional residents; no PHI; uses generic form type references only.",
        "sme_flags": ["Confirm current physician-report form references, eviction notice periods, and appeal rights with CDSS/Title 22 source."],
        "compliance_flags": ["Self-paced: interactive feedback + identity confirmation required."],
        "defensibility_notes": "Mirrors RCFE-CETP-006; renewal-level process refresher.",
        "identity_confirmation": "PIN/attestation at start; checkpoint before knowledge check.",
        "interactive_feedback": "Branching lesson, sequencing feedback, and per-item quiz feedback.",
    },
    {
        "id": "M08",
        "title": "Dementia Care I: Alzheimer's Disease, Person-Centered Support, and Direct Care",
        "ce_hours": 4,
        "minutes": 240,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": ["Managing Alzheimer's Disease and Related Dementias"],
        "dementia_hours": 4,
        "description": (
            "Live/instructor-interactive dementia module focused on DIRECT CARE: Alzheimer's disease "
            "and related dementias, stages and progression, person-centered communication, supporting "
            "activities of daily living, responding to unmet needs, and reducing distress through "
            "relationship-based direct care. Delivered live so administrators practice and discuss "
            "techniques with peers and the instructor. Counts toward the required 8 dementia hours."),
        "compliance_rationale": (
            "Directly satisfies part of the mandatory >=8 hours of dementia instruction "
            "(direct care emphasis) and maps to 'Managing Alzheimer's Disease and Related Dementias'. "
            "Live delivery supports skill practice and the simultaneous-interaction requirement."),
        "objectives": [
            "Describe the common types and stages of dementia and their care implications.",
            "Apply person-centered communication techniques to a resident with dementia in a live practice.",
            "Adapt ADL support to preserve dignity and remaining abilities.",
            "Interpret behavior as communication of unmet needs and select a direct-care response.",
            "Coach direct-care staff on a relationship-based dementia care approach.",
        ],
        "lessons": [
            {"id": "M08-L1", "title": "Dementia Types, Stages, and Progression (Facilitated)", "minutes": 60,
             "objective": "Describe dementia types/stages and care implications.",
             "activity_type": "Live presentation + polling", "moodle": "BigBlueButton/Zoom (LTI) + Choice",
             "completion": "Attendance + poll responses",
             "summary": "Alzheimer's vs. vascular/Lewy/frontotemporal, trajectory, cognition/function changes, care planning impact."},
            {"id": "M08-L2", "title": "Person-Centered Communication Practice", "minutes": 60,
             "objective": "Apply person-centered communication in live practice.",
             "activity_type": "Live role-play (triads)", "moodle": "Live breakout + Forum debrief",
             "completion": "Role-play participation + debrief post",
             "summary": "Approach, validation, redirection, sensory and environmental cues, avoiding argument/correction."},
            {"id": "M08-L3", "title": "ADL Support and Dignity", "minutes": 60,
             "objective": "Adapt ADL support to preserve dignity/abilities.",
             "activity_type": "Facilitated case + demonstration", "moodle": "Live session + Assignment",
             "completion": "Case participation + submitted ADL approach",
             "summary": "Dressing/bathing/eating support, choice and cueing, reducing resistance through approach."},
            {"id": "M08-L4", "title": "Behavior as Communication: Direct-Care Response", "minutes": 60,
             "objective": "Interpret behavior as unmet need; coach staff response.",
             "activity_type": "Live case + coaching practice", "moodle": "Live session + Quiz",
             "completion": "Coaching practice + pass check >=80%",
             "summary": "Identifying triggers/unmet needs, non-pharmacological responses, staff coaching script."},
        ],
        "key_terms": ["Alzheimer's disease", "Vascular/Lewy body/frontotemporal dementia", "Person-centered care",
                      "Validation", "Redirection", "Behavior as communication", "Unmet need", "Cueing"],
        "scenario": (
            "Fictional: A resident at Glenwood Memory Neighborhood becomes distressed and resistant during "
            "afternoon care. In live triads, learners practice a person-centered approach to identify the "
            "unmet need and de-escalate. All fictional/de-identified."),
        "activities": ["Live polling on stage-based care", "Communication role-play triads", "ADL dignity case", "Behavior-as-communication coaching practice"],
        "doc_exercise": "Write a direct-care approach plan for the fictional resident: suspected unmet need, communication approach, environmental adjustments, and staff coaching points.",
        "knowledge_check": {
            "blueprint": "8-item check post-session; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "A resident with dementia resists bathing and becomes agitated. The BEST first direct-care response is to:",
                 "choices": ["A. Insist and complete the task quickly", "B. Identify the likely unmet need/trigger and adjust the approach (timing, privacy, communication)",
                             "C. Request a PRN sedative", "D. Document refusal and skip all hygiene"],
                 "answer": "B",
                 "rationale": "Behavior signals an unmet need; adjusting approach/environment is the person-centered, non-pharmacological first response.",
                 "remediation": "Re-review M08-L4 (Behavior as Communication)."},
            ],
        },
        "completion_requirement": "Attend the full live session (engagement evidence), participate in role-play/coaching, submit the direct-care approach plan, and pass the 8-item check at >=80%.",
        "evidence_artifact": "Attendance/engagement log, role-play participation, submitted direct-care plan, knowledge-check score.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Choice", "Forum", "Assignment", "Quiz", "Attendance"],
        "accessibility": ["Live captioning (CART) offered", "Pre-posted accessible materials", "Alternative role-play participation path"],
        "privacy_notes": "Fictional residents only; no PHI; role-plays use scripted fictional personas.",
        "sme_flags": ["Dementia clinical content: SME (RN/dementia specialist) review required for accuracy and currency."],
        "compliance_flags": ["Counts toward mandatory dementia hours (4 of 8).", "Live/instructor-interactive: simultaneous-interaction evidence required."],
        "defensibility_notes": "Mirrors RCFE-CETP-002 (person-centered dementia foundations); direct-care emphasis documented for the 8-hour dementia requirement.",
        "identity_confirmation": "Live roster/credential verification at join.",
        "interactive_feedback": "Instructor real-time feedback during role-play/coaching.",
    },
    {
        "id": "M09",
        "title": "Dementia Care II: Physical Environment, Assessment, Admissions, Behaviors, and Risk Reduction",
        "ce_hours": 4,
        "minutes": 240,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": ["Managing Alzheimer's Disease and Related Dementias"],
        "dementia_hours": 4,
        "description": (
            "Live/instructor-interactive dementia module focused on the SYSTEMS around dementia care: "
            "dementia-supportive physical environment, dementia-specific assessment, dementia admissions "
            "procedures and disclosures, behavior support planning, elopement/wandering risk reduction, "
            "and safety. Delivered live for facilitated environmental audit and case planning. Counts "
            "toward the required 8 dementia hours (covering physical environment, admissions, and "
            "assessment as required)."),
        "compliance_rationale": (
            "Completes the mandatory >=8 dementia hours and explicitly addresses the required dementia "
            "topics of physical environment, admissions procedures, and assessment, plus direct-care "
            "linkage from M08. Live delivery supports the environmental-audit activity and "
            "simultaneous-interaction requirement."),
        "objectives": [
            "Audit a physical environment for dementia-supportive design and safety/elopement risk.",
            "Apply dementia-specific assessment elements to inform a care plan.",
            "Apply dementia admissions procedures and required disclosures.",
            "Develop a behavior support plan that emphasizes non-pharmacological strategies.",
            "Design an elopement/wandering risk-reduction strategy.",
        ],
        "lessons": [
            {"id": "M09-L1", "title": "Dementia-Supportive Physical Environment (Facilitated Audit)", "minutes": 60,
             "objective": "Audit environment for dementia-supportive design and safety.",
             "activity_type": "Live environmental-audit exercise", "moodle": "BigBlueButton/Zoom (LTI) + Assignment (audit)",
             "completion": "Attendance + submitted audit",
             "summary": "Wayfinding, lighting/contrast, noise, secured egress, safe wandering paths, hazard reduction."},
            {"id": "M09-L2", "title": "Dementia-Specific Assessment", "minutes": 60,
             "objective": "Apply dementia-specific assessment to inform planning.",
             "activity_type": "Facilitated case + tool walkthrough", "moodle": "Live session + Choice",
             "completion": "Case participation + poll responses",
             "summary": "Cognition, function, behavior triggers, history, preferences; informing the needs/services plan."},
            {"id": "M09-L3", "title": "Dementia Admissions Procedures and Disclosures", "minutes": 60,
             "objective": "Apply dementia admissions procedures and disclosures.",
             "activity_type": "Facilitated walkthrough + breakout", "moodle": "Live breakout + Forum",
             "completion": "Breakout participation + forum post",
             "summary": "Dementia care plan of operation considerations, required disclosures, secured-setting admission appropriateness."},
            {"id": "M09-L4", "title": "Behavior Support and Elopement Risk Reduction", "minutes": 60,
             "objective": "Build behavior support plan; design elopement risk reduction.",
             "activity_type": "Live case planning + Quiz", "moodle": "Live session + Assignment + Quiz",
             "completion": "Submit behavior support plan; pass check >=80%",
             "summary": "Antecedent-behavior-consequence approach, environmental supports, elopement prevention/response drill."},
        ],
        "key_terms": ["Dementia-supportive design", "Wayfinding", "Secured perimeter / egress control", "Elopement/wandering",
                      "Dementia-specific assessment", "Behavior support plan", "ABC approach", "Disclosure of dementia care"],
        "scenario": (
            "Fictional: Glenwood Memory Neighborhood is admitting a resident with moderate dementia and a "
            "history of exit-seeking. Teams audit the environment, complete a dementia-specific assessment, "
            "and build an elopement risk-reduction and behavior support plan. All fictional/de-identified."),
        "activities": ["Live environmental audit", "Dementia assessment case", "Admissions/disclosure breakout", "Behavior support + elopement plan"],
        "doc_exercise": "Produce a dementia admissions packet outline: required disclosures, environmental fit findings, dementia-specific assessment summary, and behavior support/elopement plan.",
        "knowledge_check": {
            "blueprint": "8-item check post-session; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "Which environmental feature BEST supports a resident with dementia and exit-seeking behavior?",
                 "choices": ["A. Bright exit signs over every door", "B. Visual cueing/wayfinding plus secured egress and safe walking paths",
                             "C. Locking residents in their rooms", "D. Removing all outdoor access"],
                 "answer": "B",
                 "rationale": "Dementia-supportive design uses wayfinding, secured (not punitive) egress, and safe wandering paths; locking residents in rooms is a prohibited restraint.",
                 "remediation": "Re-review M09-L1 (Dementia-Supportive Physical Environment)."},
            ],
        },
        "completion_requirement": "Attend the full live session, complete the environmental audit, participate in breakout/case planning, submit the dementia admissions/behavior plan, and pass the 8-item check at >=80%.",
        "evidence_artifact": "Attendance/engagement log, submitted environmental audit, behavior/elopement plan, knowledge-check score.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Assignment", "Choice", "Forum", "Quiz", "Attendance"],
        "accessibility": ["Live captioning offered", "Accessible audit checklist", "Alternative participation path"],
        "privacy_notes": "Fictional residents/facility; no PHI; disclosures illustrated with fictional content.",
        "sme_flags": ["Dementia clinical/environmental content: SME review required.", "Confirm dementia disclosure and secured-setting admission requirements with CDSS/Title 22 source."],
        "compliance_flags": ["Counts toward mandatory dementia hours (4 of 8); explicitly covers physical environment, admissions, and assessment.", "Live/instructor-interactive: interaction evidence required."],
        "defensibility_notes": "Mirrors RCFE-CETP-003 (dementia safety/environment/documentation); satisfies dementia topic breadth requirement.",
        "identity_confirmation": "Live roster/credential verification at join.",
        "interactive_feedback": "Instructor real-time feedback during audit and planning.",
    },
    {
        "id": "M10",
        "title": "Residents' Rights, Abuse Prevention, LGBT Cultural Competency, and Complaint-Safe Communication",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": ["Residents' Rights", "Cultural Competency (Including LGBT) and Abuse Prevention"],
        "dementia_hours": 0,
        "description": (
            "Live/instructor-interactive module on residents' rights, abuse and neglect prevention and "
            "mandated reporting, LGBT cultural competency (per California RCFE requirements), and "
            "complaint-safe, non-retaliatory communication. Delivered live for sensitive role-play and "
            "facilitated discussion."),
        "compliance_rationale": (
            "Maps to 'Residents' Rights' and 'Cultural Competency (Including LGBT) and Abuse Prevention'. "
            "Live delivery is appropriate for sensitive role-play and discussion and supports the "
            "simultaneous-interaction requirement."),
        "objectives": [
            "Enumerate core residents' rights and the administrator's duty to uphold them.",
            "Identify signs of abuse/neglect and execute mandated-reporting obligations and timelines.",
            "Apply LGBT-inclusive, culturally competent practices required for California RCFEs.",
            "Respond to a complaint in a complaint-safe, non-retaliatory manner.",
            "Demonstrate, in live role-play, a rights-respecting response to a sensitive situation.",
        ],
        "lessons": [
            {"id": "M10-L1", "title": "Residents' Rights and Administrator Duties (Facilitated)", "minutes": 55,
             "objective": "Enumerate residents' rights and uphold duties.",
             "activity_type": "Live presentation + polling", "moodle": "BigBlueButton/Zoom (LTI) + Choice",
             "completion": "Attendance + poll responses",
             "summary": "Dignity, privacy, self-determination, freedom from restraint/retaliation, councils, grievance rights."},
            {"id": "M10-L2", "title": "Abuse/Neglect Recognition and Mandated Reporting", "minutes": 55,
             "objective": "Identify abuse/neglect; execute mandated reporting.",
             "activity_type": "Facilitated case + decision practice", "moodle": "Live session + Assignment",
             "completion": "Case participation + submitted reporting decision",
             "summary": "Abuse types, mandated-reporter duties, reporting timelines/recipients, non-retaliation, documentation."},
            {"id": "M10-L3", "title": "LGBT Cultural Competency and Complaint-Safe Communication", "minutes": 70,
             "objective": "Apply LGBT-inclusive practice; respond complaint-safely; role-play.",
             "activity_type": "Live role-play + breakout", "moodle": "Live breakout + Forum + Quiz",
             "completion": "Role-play + pass check >=80%",
             "summary": "LGBT inclusive policies/forms/training, anti-discrimination, complaint handling without retaliation."},
        ],
        "key_terms": ["Residents' rights", "Mandated reporter", "Abuse/neglect", "Retaliation prohibition",
                      "LGBT cultural competency", "Grievance/complaint process", "Resident council"],
        "scenario": (
            "Fictional: A resident at Harborview RCFE confides a concern that may indicate neglect and also "
            "reports feeling disrespected about their identity. In live role-play, learners practice a "
            "rights-respecting, mandated-reporting-compliant, inclusive response. All fictional."),
        "activities": ["Live polling on rights", "Mandated-reporting decision case", "LGBT-inclusive practice role-play", "Complaint-safe response practice"],
        "doc_exercise": "Document a mandated-reporting decision and a complaint-handling response, including required notifications, timelines, and anti-retaliation safeguards.",
        "knowledge_check": {
            "blueprint": "6-item check post-session; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "An administrator suspects resident neglect based on a resident's report. The administrator must:",
                 "choices": ["A. Investigate fully before reporting and only report if proven", "B. Make the required mandated report within the legal timeframe and document it",
                             "C. Ask the family to handle it", "D. Wait for the next licensing visit"],
                 "answer": "B",
                 "rationale": "Mandated reporters must report suspected abuse/neglect within required timeframes; proof is not a prerequisite. Verify current timelines/recipients with source.",
                 "remediation": "Re-review M10-L2 (Abuse/Neglect Recognition and Mandated Reporting)."},
            ],
        },
        "completion_requirement": "Attend the live session, participate in role-play, submit the reporting/complaint documentation exercise, and pass the 6-item check at >=80%.",
        "evidence_artifact": "Attendance/engagement log, role-play participation, submitted documentation exercise, knowledge-check score.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Choice", "Forum", "Assignment", "Quiz", "Attendance"],
        "accessibility": ["Live captioning offered", "Trauma-informed facilitation note", "Alternative participation path"],
        "privacy_notes": "Fictional residents; no PHI; sensitive scenarios are scripted and de-identified.",
        "sme_flags": ["Confirm current mandated-reporting timelines/recipients and California LGBT cultural-competency RCFE requirements with CDSS source."],
        "compliance_flags": ["Live/instructor-interactive: interaction evidence required.", "Sensitive content - trauma-informed facilitation advised."],
        "defensibility_notes": "Mirrors RCFE-CETP-004 plus LGBT cultural-competency requirement; renewal-level.",
        "identity_confirmation": "Live roster/credential verification at join.",
        "interactive_feedback": "Instructor real-time feedback during role-play.",
    },
    {
        "id": "M11",
        "title": "Physical Environment, Emergency Preparedness, Maintenance, Housekeeping, and Safety Systems",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": ["Managing the Physical Environment (Including Emergency Procedures)"],
        "dementia_hours": 0,
        "description": (
            "Live/instructor-interactive module on the physical environment and safety systems: fire "
            "safety, emergency and disaster preparedness planning, evacuation, infection-control "
            "housekeeping, maintenance and hazard management, and food/equipment safety. Delivered live "
            "to run a tabletop emergency drill and facilitated environmental review."),
        "compliance_rationale": (
            "Maps to 'Managing the Physical Environment (Including Emergency Procedures)'. Live delivery "
            "is used for the tabletop drill and supports the simultaneous-interaction requirement."),
        "objectives": [
            "Evaluate a facility emergency/disaster plan for required elements.",
            "Lead a tabletop evacuation drill and document outcomes.",
            "Identify fire-safety, maintenance, and housekeeping hazards and corrective actions.",
            "Apply infection-control and food-safety standards in operational decisions.",
            "Build a corrective-action plan from a fictional environmental inspection.",
        ],
        "lessons": [
            {"id": "M11-L1", "title": "Emergency and Disaster Preparedness (Facilitated)", "minutes": 55,
             "objective": "Evaluate emergency/disaster plan elements.",
             "activity_type": "Live presentation + plan review", "moodle": "BigBlueButton/Zoom (LTI) + Choice",
             "completion": "Attendance + poll responses",
             "summary": "Required emergency plan elements, communication, supplies, shelter/evacuate decisions, special needs (dementia/mobility)."},
            {"id": "M11-L2", "title": "Tabletop Evacuation Drill", "minutes": 55,
             "objective": "Lead a tabletop evacuation drill; document outcomes.",
             "activity_type": "Live tabletop simulation (breakouts)", "moodle": "Live breakout + Assignment (after-action)",
             "completion": "Drill participation + submitted after-action notes",
             "summary": "Roles, headcount/accountability, residents with cognitive/mobility needs, documentation of drill."},
            {"id": "M11-L3", "title": "Fire Safety, Maintenance, Housekeeping, Infection & Food Safety", "minutes": 70,
             "objective": "Identify hazards; apply infection/food safety; build corrective plan.",
             "activity_type": "Facilitated inspection case + Quiz", "moodle": "Live session + Assignment + Quiz",
             "completion": "Submit corrective-action plan; pass check >=80%",
             "summary": "Fire systems/extinguishers/exits, preventive maintenance, infection control, safe food handling, hazard logs."},
        ],
        "key_terms": ["Emergency/disaster plan", "Evacuation drill", "Shelter-in-place", "Fire safety system",
                      "Preventive maintenance", "Infection control", "Food safety", "Hazard log"],
        "scenario": (
            "Fictional: During a tabletop drill at Pinecrest RCFE, the team must evacuate residents "
            "including several with dementia and limited mobility, then complete an after-action review. "
            "All fictional/de-identified."),
        "activities": ["Live emergency-plan review", "Tabletop evacuation drill", "Hazard inspection case", "Corrective-action planning"],
        "doc_exercise": "Complete an after-action report for the tabletop drill plus a corrective-action plan for two identified environmental hazards.",
        "knowledge_check": {
            "blueprint": "6-item check post-session; per-item feedback; 80% to complete.",
            "items": [
                {"type": "MCQ", "stem": "An RCFE emergency plan must specifically address residents who:",
                 "choices": ["A. Are easiest to move only", "B. Have cognitive (e.g., dementia) and mobility needs requiring assisted evacuation",
                             "C. Have visitors that day", "D. Request it in writing"],
                 "answer": "B",
                 "rationale": "Plans must account for residents needing assistance, including those with dementia/mobility limitations, to ensure safe evacuation.",
                 "remediation": "Re-review M11-L1 (Emergency and Disaster Preparedness)."},
            ],
        },
        "completion_requirement": "Attend the live session, participate in the tabletop drill, submit the after-action + corrective-action plan, and pass the 6-item check at >=80%.",
        "evidence_artifact": "Attendance/engagement log, drill participation, submitted after-action/corrective-action plan, knowledge-check score.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Choice", "Forum", "Assignment", "Quiz", "Attendance"],
        "accessibility": ["Live captioning offered", "Accessible drill materials", "Alternative participation path"],
        "privacy_notes": "Fictional facility; no real inspection or resident data.",
        "sme_flags": ["Confirm current emergency-plan required elements and drill documentation expectations with CDSS/Title 22 and local fire authority."],
        "compliance_flags": ["Live/instructor-interactive: interaction evidence required."],
        "defensibility_notes": "Mirrors RCFE-CETP-007; live drill strengthens defensibility of instructional-setting hours.",
        "identity_confirmation": "Live roster/credential verification at join.",
        "interactive_feedback": "Instructor real-time feedback during drill and inspection case.",
    },
    {
        "id": "M12",
        "title": "Integrated RCFE Administrator Capstone, Audit Readiness, and Final Assessment",
        "ce_hours": 3,
        "minutes": 180,
        "delivery": "Live / instructor-interactive",
        "core_knowledge": [
            "Laws, Regulations, Policies, and Procedural Standards Impacting RCFE",
            "Business Operations", "Management/Supervision of Staff", "Residents' Rights",
            "Managing Alzheimer's Disease and Related Dementias",
            "Managing the Physical Environment (Including Emergency Procedures)",
        ],
        "dementia_hours": 0,
        "description": (
            "Live/instructor-interactive capstone integrating all prior modules through an audit-readiness "
            "simulation and the final cumulative assessment. Learners assemble an audit-ready evidence "
            "binder for a fictional facility, defend decisions, and complete the proctored final exam. "
            "Delivered live for presentation/defense and identity-verified final assessment."),
        "compliance_rationale": (
            "Integrates and assesses all core-of-knowledge areas, including dementia. Live delivery "
            "supports the capstone defense and identity-verified final assessment, and contributes to "
            "the instructional-setting hour requirement."),
        "objectives": [
            "Integrate knowledge from all modules to evaluate a fictional facility's compliance posture.",
            "Assemble an audit-ready evidence binder mapped to RCFE requirements.",
            "Defend administrator decisions using regulation- and person-centered-care rationale.",
            "Achieve >=80% on the cumulative final assessment.",
            "Produce a personal post-course compliance action plan.",
        ],
        "lessons": [
            {"id": "M12-L1", "title": "Audit-Readiness Simulation (Facilitated)", "minutes": 60,
             "objective": "Evaluate compliance posture; assemble evidence binder.",
             "activity_type": "Live simulation + breakout", "moodle": "BigBlueButton/Zoom (LTI) + Assignment (binder)",
             "completion": "Attendance + submitted binder",
             "summary": "Mock licensing visit; teams assemble/triage required records and identify gaps."},
            {"id": "M12-L2", "title": "Capstone Defense and Action Plan", "minutes": 60,
             "objective": "Defend decisions; produce action plan.",
             "activity_type": "Live presentation/defense", "moodle": "Live session + Assignment (action plan)",
             "completion": "Defense participation + submitted action plan",
             "summary": "Teams present findings and corrective actions; individual post-course action plan."},
            {"id": "M12-L3", "title": "Cumulative Final Assessment (Proctored/Identity-Verified)", "minutes": 60,
             "objective": "Achieve >=80% on the cumulative final.",
             "activity_type": "Final exam", "moodle": "Quiz (secure settings) + identity confirmation",
             "completion": "Pass final at >=80%; signed completion statement",
             "summary": "30-item cumulative exam across all modules; remediation pathway for failed attempts."},
        ],
        "key_terms": ["Audit readiness", "Evidence binder", "Plan of correction", "Compliance posture", "Capstone defense", "Final assessment"],
        "scenario": (
            "Fictional: Lakeside Manor RCFE is notified of a renewal-cycle review. The capstone team "
            "assembles the audit-ready binder, identifies gaps, and presents a corrective plan. All "
            "fictional/de-identified."),
        "activities": ["Audit-readiness simulation", "Evidence-binder assembly", "Capstone defense", "Cumulative final exam"],
        "doc_exercise": "Produce an audit-ready evidence binder index and a personal post-course compliance action plan with prioritized corrective actions and timelines.",
        "knowledge_check": {
            "blueprint": "Final cumulative assessment = 30 items across all modules; >=80% to pass; up to 3 attempts; remediation required after a failed attempt; answer key NOT shown to learners.",
            "items": [
                {"type": "MCQ", "stem": "(Sample final item) Which combination correctly reflects RCFE renewal CE rules?",
                 "choices": ["A. 40 hours total, up to 20 self-paced, at least 8 dementia hours",
                             "B. 20 hours total, all self-paced", "C. 40 hours total, all self-paced, no dementia requirement",
                             "D. 8 hours total, half dementia"],
                 "answer": "A",
                 "rationale": "RCFE administrator renewal requires 40 CE hours, with no more than half (20) self-paced and at least 8 dementia-related hours. Verify against current CDSS source.",
                 "remediation": "Re-review the Course Overview and all module summaries before re-attempt."},
            ],
        },
        "completion_requirement": "Attend the live capstone, submit the evidence binder and action plan, and pass the 30-item cumulative final at >=80%; identity confirmed and signed completion statement obtained.",
        "evidence_artifact": "Attendance/engagement log, submitted binder + action plan, final-exam score and attempt log, identity-confirmation record, signed completion statement.",
        "moodle_activities": ["BigBlueButton/Zoom (LTI)", "Assignment", "Quiz (secure)", "Attendance", "Certificate (gated)"],
        "accessibility": ["Live captioning offered", "Extended-time accommodation path for final exam", "Accessible binder templates"],
        "privacy_notes": "Fictional facility; no PHI; binder uses fictional sample records only.",
        "sme_flags": ["Final exam blueprint and pass standard require SME + compliance sign-off.", "Confirm proctoring/identity standard acceptable to CDSS/ACS ('Needs confirmation')."],
        "compliance_flags": ["Final assessment must be identity-verified; signed completion statement obtained before certificate issuance.", "Live/instructor-interactive: interaction evidence required."],
        "defensibility_notes": "Capstone integrates and assesses all core-of-knowledge areas including the 8 dementia hours covered in M08-M09.",
        "identity_confirmation": "Live roster/credential verification at join AND identity confirmation immediately before the final exam.",
        "interactive_feedback": "Instructor real-time feedback during defense; final exam shows score/remediation guidance (not answer key).",
    },
]

# ---------------------------------------------------------------------------
# Capstone tasks (Capstone_Map)
# ---------------------------------------------------------------------------
CAPSTONE_TASKS = [
    {"id": "CAP-1", "scenario": "Mock renewal-cycle licensing review at fictional Lakeside Manor RCFE.",
     "deliverable": "Audit-ready evidence binder index mapped to RCFE requirements.",
     "rubric": "Completeness of required records; correct mapping to requirements; gap identification.",
     "passing": "Meets/Exceeds on all required rubric rows; >=80% rubric score.",
     "doc_expectation": "Binder index lists each required record, location, owner, and status.",
     "privacy": "Fictional sample records only; no PHI or real facility data.",
     "evidence": "Submitted binder index (Assignment) + rubric grade in gradebook."},
    {"id": "CAP-2", "scenario": "Identified compliance gaps from the simulation.",
     "deliverable": "Plan of correction for top 3 gaps.",
     "rubric": "Root-cause accuracy; corrective + preventive action; responsible party; timeline.",
     "passing": "All three gaps addressed with defensible POC; >=80% rubric score.",
     "doc_expectation": "POC includes action, owner, due date, recurrence prevention.",
     "privacy": "Fictional only.",
     "evidence": "Submitted POC (Assignment) + rubric grade."},
    {"id": "CAP-3", "scenario": "Dementia-care defensibility review (integrates M08-M09).",
     "deliverable": "Evidence summary showing how 8 dementia hours/topics are met.",
     "rubric": "Direct care, physical environment, admissions, assessment all addressed.",
     "passing": "All four dementia topic areas evidenced; >=80% rubric score.",
     "doc_expectation": "Map dementia topics to module evidence artifacts.",
     "privacy": "Fictional only.",
     "evidence": "Submitted dementia evidence map + rubric grade."},
    {"id": "CAP-4", "scenario": "Personal post-course application.",
     "deliverable": "Individual compliance action plan for learner's own (described, non-identifying) setting.",
     "rubric": "Prioritization; feasibility; measurable actions; timeline.",
     "passing": "At least 5 prioritized actions with timelines; >=80% rubric score.",
     "doc_expectation": "Action, priority, target date, success measure.",
     "privacy": "No real resident/staff identifiers permitted in submissions.",
     "evidence": "Submitted action plan + rubric grade."},
]

# ---------------------------------------------------------------------------
# Additional final-assessment item bank (supplements per-module sample items)
# Full bank to be completed and SME-reviewed before submission ("Needs confirmation").
# ---------------------------------------------------------------------------
FINAL_ASSESSMENT_ITEMS = [
    {"id": "FX-01", "module": "M01", "type": "MCQ",
     "stem": "Which agency licenses California RCFEs?", "choices": "A. CDPH; B. CDSS CCLD; C. BRN; D. CMS",
     "answer": "B", "rationale": "CDSS Community Care Licensing Division licenses RCFEs.",
     "remediation": "Review M01.", "learner_vis": "Score only; no answer key", "admin_vis": "Full key + rationale"},
    {"id": "FX-02", "module": "M06", "type": "MCQ",
     "stem": "Medicating a resident for staff convenience without medical indication is:",
     "choices": "A. Allowed PRN; B. A chemical restraint (prohibited); C. Self-administration; D. Required",
     "answer": "B", "rationale": "Chemical restraint is prohibited.",
     "remediation": "Review M06-L3.", "learner_vis": "Score only", "admin_vis": "Full key + rationale"},
    {"id": "FX-03", "module": "M08", "type": "MCQ",
     "stem": "Behavior in dementia is best understood as:",
     "choices": "A. Intentional defiance; B. Communication of an unmet need; C. Always medical; D. Irrelevant",
     "answer": "B", "rationale": "Behavior signals unmet needs; person-centered response first.",
     "remediation": "Review M08-L4.", "learner_vis": "Score only", "admin_vis": "Full key + rationale"},
    {"id": "FX-04", "module": "M10", "type": "MCQ",
     "stem": "Upon suspecting abuse, a mandated reporter must:",
     "choices": "A. Prove it first; B. Report within required timeframe and document; C. Tell only family; D. Wait",
     "answer": "B", "rationale": "Report suspected abuse within required timeframe; proof not required.",
     "remediation": "Review M10-L2.", "learner_vis": "Score only", "admin_vis": "Full key + rationale"},
    {"id": "FX-05", "module": "M07", "type": "MCQ",
     "stem": "A significant change in a resident's condition requires:",
     "choices": "A. No action; B. Reappraisal and needs/services plan update; C. Immediate eviction; D. Family vote",
     "answer": "B", "rationale": "Significant changes trigger reappraisal and plan update.",
     "remediation": "Review M07-L2.", "learner_vis": "Score only", "admin_vis": "Full key + rationale"},
]

# ---------------------------------------------------------------------------
# Application packet checklist (Application_Packet_Checklist)
# ---------------------------------------------------------------------------
APPLICATION_PACKET_CHECKLIST = [
    {"item": "RCFE CE vendor/course application support content", "status": "Draft",
     "owner": "Authorized Representative (Maria Divina Bustos)", "source": "Master packet 02_RCFE_CDSS_CETP_PACKET",
     "missing": "Final CDSS/ACS form transfer + signature", "approval": "Pending", "notes": "Use existing CETP vendor identity."},
    {"item": "Course outline", "status": "Draft", "owner": "Instructional Designer", "source": "This package - Section N/D",
     "missing": "SME sign-off", "approval": "Pending", "notes": "40-hour, 12-module."},
    {"item": "Course objectives", "status": "Draft", "owner": "Instructional Designer", "source": "Module blueprints",
     "missing": "SME sign-off", "approval": "Pending", "notes": "Measurable objectives per module."},
    {"item": "Hour allocation table", "status": "Draft", "owner": "Instructional Designer", "source": "Course_Map sheet",
     "missing": "None", "approval": "Pending", "notes": "40h total; reconciled."},
    {"item": "Dementia-hour mapping table", "status": "Draft", "owner": "SME (dementia)", "source": "Dementia_Hour_Map sheet",
     "missing": "SME confirmation of topic coverage", "approval": "Pending", "notes": "8h: direct care + environment/admissions/assessment."},
    {"item": "Self-paced vs instructor-interactive delivery table", "status": "Draft", "owner": "Instructional Designer",
     "source": "Delivery_Mode_Map sheet", "missing": "None", "approval": "Pending", "notes": "17 self-paced / 23 live."},
    {"item": "Flyer/brochure text", "status": "Draft", "owner": "Authorized Representative", "source": "Section O",
     "missing": "Approval before advertising", "approval": "Pending", "notes": "Marked Draft - Pending Approval."},
    {"item": "Sample certificate text", "status": "Draft", "owner": "Authorized Representative", "source": "Section P",
     "missing": "Real vendor/course numbers (assigned after approval)", "approval": "Pending", "notes": "Placeholders only."},
    {"item": "Course evaluation form", "status": "Draft", "owner": "Instructional Designer", "source": "Section Q",
     "missing": "None", "approval": "Pending", "notes": "Participant evaluation."},
    {"item": "Attendance/completion/proof-of-participation policy", "status": "Draft", "owner": "Compliance",
     "source": "Section R", "missing": "Confirm CDSS active-participation expectations", "approval": "Pending", "notes": ""},
    {"item": "Signed completion statement template", "status": "Draft", "owner": "Compliance", "source": "Section M",
     "missing": "None", "approval": "Pending", "notes": "Retained 3 years; obtained before certificate."},
    {"item": "Recordkeeping policy", "status": "Draft", "owner": "Compliance", "source": "Section R",
     "missing": "Confirm retention specifics", "approval": "Pending", "notes": "3-year completion-record retention."},
    {"item": "Refund/cancellation policy placeholder", "status": "Draft (placeholder)", "owner": "Authorized Representative",
     "source": "Section N", "missing": "Business decision on fees/refunds", "approval": "Pending", "notes": "Fees TBD."},
    {"item": "Advertising compliance checklist", "status": "Draft", "owner": "Compliance", "source": "Section N/U",
     "missing": "None", "approval": "Pending", "notes": "No approval claims pre-approval."},
    {"item": "LMS evidence checklist", "status": "Draft", "owner": "LMS Admin", "source": "Section R / Audit_Evidence_Log",
     "missing": "None", "approval": "Pending", "notes": "Export plan defined."},
    {"item": "SME/compliance review checklist", "status": "Draft", "owner": "SME + Compliance", "source": "Sections U/V",
     "missing": "Reviewer assignment", "approval": "Pending", "notes": ""},
    {"item": "Owner approval checklist before submission", "status": "Draft", "owner": "Owner/Authorized Representative",
     "source": "Section X", "missing": "Owner sign-off", "approval": "Pending", "notes": "Final gate."},
]

# ---------------------------------------------------------------------------
# Certificate gate (Certificate_Gate)
# ---------------------------------------------------------------------------
CERTIFICATE_GATE = [
    {"gate": "All module activity completions", "condition": "Every module marked complete per activity-completion rules",
     "source": "Moodle activity completion / completion report", "manual": "No",
     "approval": "CE hours = placeholder until approval", "risk": "Hours not substantiated; non-compliant certificate."},
    {"gate": "Self-paced interactive feedback completed", "condition": "All self-paced modules' interactive activities completed",
     "source": "H5P/Lesson completion logs", "manual": "No", "approval": "Pending",
     "risk": "Fails self-paced interactivity requirement."},
    {"gate": "Identity confirmation (self-paced)", "condition": "PIN/identity confirmation recorded for each self-paced module",
     "source": "Identity-confirmation log", "manual": "No", "approval": "Pending",
     "risk": "Fails self-paced identity requirement; certificate invalid."},
    {"gate": "Live attendance evidence", "condition": "Attendance + engagement captured for each live module",
     "source": "Attendance module + session engagement logs", "manual": "Partial",
     "approval": "Pending", "risk": "Instructional-setting hours not substantiated."},
    {"gate": "Final assessment passed", "condition": "Cumulative final >=80%", "source": "Quiz grade",
     "manual": "No", "approval": "Pending", "risk": "Competency not demonstrated."},
    {"gate": "Signed completion statement", "condition": "Participant-signed completion statement obtained",
     "source": "Signed-statement upload/e-sign record", "manual": "Yes",
     "approval": "Pending", "risk": "Cannot issue certificate; recordkeeping non-compliance."},
    {"gate": "Hours/threshold reconciliation", "condition": "Total CE hours and self-paced cap reconciled for the learner",
     "source": "Completion report + gradebook", "manual": "Yes", "approval": "Hours are placeholder pre-approval",
     "risk": "Over-credit or self-paced cap breach."},
    {"gate": "Approval status check", "condition": "Vendor/course approval issued before any real certificate issuance",
     "source": "CDSS/ACS approval letter", "manual": "Yes", "approval": "MUST be issued first",
     "risk": "Issuing certificates pre-approval is prohibited and a serious compliance violation."},
]

# ---------------------------------------------------------------------------
# Audit evidence log (Audit_Evidence_Log)
# ---------------------------------------------------------------------------
AUDIT_EVIDENCE_LOG = [
    {"item": "Activity completion records", "by": "Moodle completion tracking", "where": "Moodle DB / completion report",
     "retention": "3 years (min)", "review": "LMS Admin", "export": "CSV export + PDF report", "notes": "Per-learner, per-activity."},
    {"item": "Knowledge-check & final scores", "by": "Moodle Quiz", "where": "Gradebook", "retention": "3 years",
     "review": "Faculty/Compliance", "export": "Gradebook export (CSV/XLSX)", "notes": "Attempt logs retained."},
    {"item": "Self-paced identity-confirmation records", "by": "PIN/attestation activity", "where": "Identity-confirmation log",
     "retention": "3 years", "review": "Compliance", "export": "CSV export", "notes": "Per self-paced module."},
    {"item": "Interactive-feedback completion (self-paced)", "by": "H5P/Lesson", "where": "Activity logs",
     "retention": "3 years", "review": "LMS Admin", "export": "Report export", "notes": "Demonstrates interactivity."},
    {"item": "Live attendance & engagement", "by": "Attendance module + web-conf logs", "where": "Attendance report + session logs",
     "retention": "3 years", "review": "Faculty/Compliance", "export": "CSV + session report", "notes": "Substantiates instructional-setting hours."},
    {"item": "Submitted assignments (exercises/binders)", "by": "Moodle Assignment", "where": "Assignment submissions",
     "retention": "3 years", "review": "Faculty", "export": "Bulk download", "notes": "Applied-judgment evidence."},
    {"item": "Signed completion statements", "by": "Upload/e-sign workflow", "where": "Secure signed-statement store",
     "retention": "3 years (required before certificate)", "review": "Compliance", "export": "PDF export", "notes": "Obtained before certificate issuance."},
    {"item": "Certificates issued", "by": "Certificate activity (gated)", "where": "Certificate records",
     "retention": "3 years", "review": "Compliance", "export": "PDF + issuance log", "notes": "Only after approval + all gates."},
    {"item": "Course evaluations", "by": "Feedback activity", "where": "Feedback responses", "retention": "3 years",
     "review": "Instructional Designer", "export": "CSV export", "notes": "Continuous improvement evidence."},
]
