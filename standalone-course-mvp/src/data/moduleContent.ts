export type ReviewFlag = {
  kind: "SME" | "Compliance" | "Source" | "CDPH/Legal" | "TTS";
  note: string;
};

export type LessonSection = {
  title: string;
  minutes: number;
  summary: string;
  sourceStatus?: string;
};

export type ScenarioCheck = {
  title: string;
  prompt: string;
  choices?: string[];
  correctAnswer?: string;
  feedback?: string;
  remediation?: string;
  sourceStatus?: string;
};

export type SeededModuleContent = {
  id: string;
  title: string;
  time: string;
  required: boolean;
  status: string;
  placeholder: boolean;
  sourcePath: string;
  sourceStatus: string;
  summary: string;
  objectives: string[];
  lessonSections: LessonSection[];
  scenarioChecks: ScenarioCheck[];
  remediation: string;
  tts: {
    sourcePath: string;
    status: string;
    transcriptSummary: string;
  };
  moodleNotes: string;
  reviewFlags: ReviewFlag[];
};

export const moduleContents: SeededModuleContent[] = [
  {
    id: "m0",
    title: "Module 0: Orientation and Course Requirements",
    time: "0.5 hr",
    required: true,
    status: "Seeded review package",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/04_THEORY_MODULE_00_ORIENTATION_FULL.md",
    sourceStatus: "Extracted source present; ready for packaging with compliance review for disclaimer wording.",
    summary:
      "Course scope, renewal reminders, online CE cap, no-PHI boundary, identity/profile fields, and required acknowledgements.",
    objectives: [
      "Identify the course scope and partial-credit boundary.",
      "Acknowledge the 48-hour renewal requirement, 12-hours-per-year reminder, and 24-hour online CE cap.",
      "Confirm no-PHI expectations and optional clinical support boundaries.",
    ],
    lessonSections: [
      { title: "Course scope and renewal boundaries", minutes: 10, summary: "Frames the course as online theory CE support, not full renewal completion." },
      { title: "Identity and profile fields", minutes: 5, summary: "Collects review learner name and CNA certificate number for gate evidence." },
      { title: "Required acknowledgements", minutes: 15, summary: "Online cap, no-PHI, and optional clinical support boundary acknowledgements." },
    ],
    scenarioChecks: [],
    remediation: "Learner must complete all Module 0 acknowledgements before continuing to required theory.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "Transcript planning exists; no audio generated. Audio remains pending approved cloned-voice authorization.",
      transcriptSummary: "Orientation narration would explain scope, renewal boundaries, online cap, no-PHI rules, and next steps.",
    },
    moodleNotes: "Moodle Page/Book plus required acknowledgement activity; completion gates Module 1 and later certificate conditions.",
    reviewFlags: [{ kind: "Compliance", note: "Disclaimer and approval wording require final compliance review before production use." }],
  },
  {
    id: "m1",
    title: "Module 1: Infection Control and PPE",
    time: "1.5 hr",
    required: true,
    status: "Seeded lesson package; SME/source review required",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md",
    sourceStatus: "Extracted source present; content package index flags Module 1 for SME/source review.",
    summary:
      "Infection control, chain of infection, hand hygiene, PPE selection/donning/doffing, reporting infection signs, and environmental cleaning.",
    objectives: [
      "Explain how CNAs help break the chain of infection.",
      "Apply hand hygiene and PPE principles in common long-term care situations.",
      "Recognize and report possible infection-related changes from baseline.",
    ],
    lessonSections: [
      { title: "Why infection control matters", minutes: 15, summary: "Connects infection prevention to resident and staff safety.", sourceStatus: "SME/source review required." },
      { title: "Hand hygiene and PPE", minutes: 25, summary: "Reviews hand hygiene moments and PPE workflow.", sourceStatus: "SME/source review required." },
      { title: "Recognition and reporting", minutes: 25, summary: "Focuses on sudden changes and prompt reporting to licensed staff.", sourceStatus: "SME/source review required." },
      { title: "Cleaning and safe handling", minutes: 15, summary: "Covers environmental cleaning and linen handling boundaries.", sourceStatus: "SME/source review required." },
      { title: "Module check", minutes: 10, summary: "Scenario check and quiz evidence step.", sourceStatus: "SME/source review required." },
    ],
    scenarioChecks: [
      {
        title: "Sudden confusion and poor intake",
        prompt:
          "A resident who is usually alert and talkative is suddenly confused and ate very little. The safest CNA action is to report the change to the licensed nurse immediately.",
        correctAnswer: "Report the change to the licensed nurse immediately.",
        feedback:
          "Correct feedback should reinforce prompt reporting of sudden changes from baseline and avoid diagnosis by the CNA.",
        remediation: "Review recognition/reporting section before retry.",
        sourceStatus: "Interaction aligned to extracted Module 1 theme; SME/source review required.",
      },
    ],
    remediation: "Review infection-control reporting content before retaking the module check.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "Transcript planning exists; no audio generated. Module 1 narration is flagged for SME/source review.",
      transcriptSummary: "Narration would summarize infection-control basics, PPE, and change-reporting responsibilities.",
    },
    moodleNotes: "Moodle Lesson/H5P/Quiz interaction plus activity completion; completion contributes to required theory and interaction gates.",
    reviewFlags: [
      { kind: "SME", note: "Content package index flags Module 1 because no dedicated NATP infection-control source module was identified." },
      { kind: "TTS", note: "Module 1 audio cannot be produced until script and cloned-voice authorization are approved." },
    ],
  },
  {
    id: "m2",
    title: "Module 2: Resident Rights, Abuse Prevention, and Boundaries",
    time: "2.0 hr",
    required: true,
    status: "Seeded from extracted content",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/24_THEORY_MODULE_02_RESIDENT_RIGHTS_ABUSE_PREVENTION_FULL.md",
    sourceStatus: "Extracted source complete; compliance and CDPH/legal review still required before production.",
    summary:
      "Resident rights, dignity, abuse and neglect types, objective observations, mandated reporting, prevention, and professional boundaries.",
    objectives: [
      "Define resident rights, dignity, privacy, autonomy, and grievance rights.",
      "Identify physical, verbal, psychological, sexual, financial, neglect, abandonment, involuntary seclusion, and fraud-related abuse categories.",
      "Recognize objective signs and symptoms that must be reported.",
      "Apply CNA mandated-reporter responsibilities and professional boundaries.",
    ],
    lessonSections: [
      { title: "Resident rights foundation", minutes: 20, summary: "Dignity, privacy, autonomy, choices, and grievance protections." },
      { title: "Types of abuse and neglect", minutes: 25, summary: "Abuse, neglect, exploitation, abandonment, involuntary seclusion, and related examples." },
      { title: "Signs, symptoms, and evidence", minutes: 20, summary: "Objective observations, resident statements, and avoiding investigation by the CNA." },
      { title: "Mandated reporter obligations", minutes: 20, summary: "Immediate reporting path and documentation expectations." },
      { title: "Prevention, boundaries, and safety", minutes: 20, summary: "Boundaries, respectful care, and prevention strategies." },
      { title: "Module 2 quiz", minutes: 15, summary: "Scenario and classification checks with feedback and remediation." },
    ],
    scenarioChecks: [
      {
        title: "Resident grievance and retaliation protection",
        prompt:
          "A resident is afraid to complain about food because staff might get angry. The CNA should support the resident's right to complain without retaliation and follow facility reporting/support steps.",
        correctAnswer: "Support the resident's grievance right without retaliation.",
        feedback: "Correct. Resident grievance rights include the right to voice concerns without retaliation.",
        remediation: "Review resident rights and grievance protections.",
      },
      {
        title: "Mandated reporting decision",
        prompt:
          "A resident says a night CNA slapped him. The best action is to ensure immediate safety, report to the licensed nurse/supervisor, and document objectively.",
        correctAnswer: "Report immediately and document objectively.",
        feedback: "Correct. CNAs report suspected abuse promptly; they do not investigate or wait for proof.",
        remediation: "Review mandated reporting obligations before retaking the check.",
      },
    ],
    remediation: "Review Lessons 2.2 and 2.4 before retaking missed abuse-prevention/reporting checks.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "Transcript planning exists for Module 2; no audio generated. Audio pending authorization.",
      transcriptSummary: "Narration would explain resident rights, abuse types, objective signs, and reporting responsibilities.",
    },
    moodleNotes: "Five Moodle Lessons plus Quiz; completion, quiz attempt, and feedback evidence contribute to required theory gates.",
    reviewFlags: [
      { kind: "Compliance", note: "Compliance review required before production wording is used." },
      { kind: "CDPH/Legal", note: "CDPH/legal review required for reporting and certificate-course alignment." },
    ],
  },
  {
    id: "m3",
    title: "Module 3: Dementia, Communication, and Respectful Care",
    time: "2.0 hr",
    required: true,
    status: "Partially seeded; source remediation required",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/25_THEORY_MODULE_03_DEMENTIA_COMMUNICATION_CULTURAL_RESPECT_FULL.md",
    sourceStatus:
      "Extracted file is present but contains an interrupted-generation artifact at Screen 3.2.3; only available source sections are seeded.",
    summary:
      "Available source covers dementia basics and communication strategies; source outline also lists cultural respect, end-of-life care, and trauma-informed care, but inspected body content is incomplete.",
    objectives: [
      "Define dementia, Alzheimer's disease, and delirium in CNA-appropriate terms.",
      "Use calm communication strategies for residents with cognitive impairment.",
      "Recognize dementia-related behaviors such as agitation, sundowning, catastrophic reactions, and elopement risk.",
      "Respect cultural, spiritual, and end-of-life preferences when content is finalized.",
      "Use trauma-informed communication and de-escalation when content is finalized.",
    ],
    lessonSections: [
      { title: "Understanding dementia and cognitive conditions", minutes: 25, summary: "Available source explains dementia, Alzheimer's disease, delirium, and common cognitive changes." },
      { title: "Communication strategies for cognitive impairment", minutes: 25, summary: "Available source begins communication strategies and repetition example.", sourceStatus: "Body content stops during Screen 3.2.3." },
      { title: "Cultural sensitivity and spiritual respect", minutes: 20, summary: "Listed in source time breakdown; body content not available in inspected file.", sourceStatus: "Pending source remediation." },
      { title: "End-of-life care, grief, and hospice", minutes: 25, summary: "Listed in source time breakdown; body content not available in inspected file.", sourceStatus: "Pending source remediation." },
      { title: "Trauma-informed care and de-escalation", minutes: 10, summary: "Listed in source time breakdown; body content not available in inspected file.", sourceStatus: "Pending source remediation." },
      { title: "Module 3 quiz", minutes: 15, summary: "Quiz placeholder remains pending repaired source and approved question mapping.", sourceStatus: "Pending source remediation." },
    ],
    scenarioChecks: [
      {
        title: "Repeated question from resident with Alzheimer's disease",
        prompt:
          "A resident with mid-stage Alzheimer's disease asks the same question several times. The source-supported response is to answer patiently each time because the resident does not remember asking.",
        correctAnswer: "Answer patiently each time.",
        feedback: "Correct. Repetition is related to memory loss; patience and calm tone support respectful care.",
        remediation: "Review available dementia communication content.",
      },
      {
        title: "Incomplete source scenario",
        prompt: "The source begins a scenario about Mrs. Okafor in Screen 3.2.3 but does not provide complete choices or feedback.",
        sourceStatus: "Not used as a scored check until the source file is repaired.",
      },
    ],
    remediation: "Review available dementia and communication sections; do not use incomplete cultural/end-of-life/trauma sections until source remediation is complete.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "TTS planning lists Module 3 segments, but audio remains pending authorization and repaired source confirmation.",
      transcriptSummary: "Narration planning covers dementia basics, communication, cultural respect, end-of-life care, and trauma-informed care.",
    },
    moodleNotes: "Moodle Lesson content should not be finalized until the interrupted source file is repaired and reviewed.",
    reviewFlags: [
      { kind: "Source", note: "Source file contains an interrupted-generation artifact and requires remediation before production use." },
      { kind: "Compliance", note: "Incomplete body content should remain visibly flagged." },
    ],
  },
  {
    id: "m4",
    title: "Module 4: Mobility, Falls, and Workplace Safety",
    time: "2.0 hr",
    required: true,
    status: "Seeded from extracted content",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/26_THEORY_MODULE_04_MOBILITY_FALLS_WORKPLACE_SAFETY_FULL.md",
    sourceStatus: "Extracted source complete; compliance and CDPH/legal review still required before production.",
    summary:
      "Body mechanics, safe transfers, ambulation, range of motion, restorative care, fall prevention, emergency procedures, and workplace safety.",
    objectives: [
      "Apply body mechanics to reduce injury risk.",
      "Follow care-plan directions for transfers and ambulation.",
      "Support range-of-motion and restorative-care goals within CNA scope.",
      "Recognize fall risks and follow prevention procedures.",
      "Respond appropriately to fire, choking, disaster, and workplace hazards.",
    ],
    lessonSections: [
      { title: "Body mechanics and injury prevention", minutes: 20, summary: "Bending knees, close load position, leg muscles, pivoting, and asking for help." },
      { title: "Safe transfers and ambulation", minutes: 25, summary: "Care-plan transfer directions, assistive devices, gait belt support, and two-person assist boundaries." },
      { title: "Range of motion and restorative care", minutes: 20, summary: "AROM/PROM support and encouraging independence." },
      { title: "Fall prevention", minutes: 20, summary: "Fall risks, call light access, environment, footwear, and reporting." },
      { title: "Emergency procedures", minutes: 20, summary: "Fire safety, choking response, disaster procedures, and workplace safety." },
      { title: "Module 4 quiz", minutes: 15, summary: "Scenario checks with feedback and remediation." },
    ],
    scenarioChecks: [
      {
        title: "Two-person transfer boundary",
        prompt:
          "A resident's care plan requires a two-person assist, but the coworker is unavailable. The CNA should wait and find another trained staff member before transferring.",
        correctAnswer: "Wait for another trained staff member.",
        feedback: "Correct. A two-person assist order is a safety requirement, not a suggestion.",
        remediation: "Review safe transfer and care-plan sections.",
      },
      {
        title: "Restorative feeding independence",
        prompt:
          "A resident can feed herself slowly with an adaptive spoon. The CNA should encourage independence, check regularly, and allow extra time.",
        correctAnswer: "Encourage independence with support.",
        feedback: "Correct. Restorative care supports remaining ability and dignity.",
        remediation: "Review restorative-care principles.",
      },
    ],
    remediation: "Review the missed body-mechanics, transfer, fall-prevention, or emergency section before retaking checks.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "Transcript planning exists for Module 4; no audio generated. Audio pending authorization.",
      transcriptSummary: "Narration would summarize body mechanics, transfer safety, restorative care, fall prevention, and emergency response.",
    },
    moodleNotes: "Moodle Lessons plus Quiz; required completion and scored checks feed theory and interaction evidence.",
    reviewFlags: [
      { kind: "Compliance", note: "Compliance review required before production wording is used." },
      { kind: "CDPH/Legal", note: "Emergency and safety wording should be reviewed before approval submission/use." },
    ],
  },
  {
    id: "m5",
    title: "Module 5: Nutrition, Skin Integrity, Vital Signs, and Observation",
    time: "2.0 hr",
    required: true,
    status: "Seeded from extracted content; skin-integrity SME/source review required",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/27_THEORY_MODULE_05_NUTRITION_SKIN_INTEGRITY_VITAL_SIGNS_FULL.md",
    sourceStatus: "Extracted source complete; skin integrity content and related questions are flagged for SME/source review.",
    summary:
      "Nutrition and hydration, feeding assistance, aspiration prevention, skin integrity, pressure injury prevention, vital signs, observation, and reporting.",
    objectives: [
      "Support nutrition and hydration within care-plan and diet-order boundaries.",
      "Use safe feeding assistance and aspiration-prevention practices.",
      "Recognize skin integrity concerns and pressure injury risks for reporting.",
      "Measure and report vital signs according to facility policy and CNA scope.",
      "Observe, document, and report changes without including PHI in course practice areas.",
    ],
    lessonSections: [
      { title: "Nutrition and hydration", minutes: 20, summary: "Diet orders, hydration support, intake observation, and reporting concerns." },
      { title: "Feeding assistance and aspiration prevention", minutes: 20, summary: "Positioning, swallowing concerns, thickened liquids, and nurse notification." },
      { title: "Skin integrity and pressure injury prevention", minutes: 25, summary: "Pressure injury risk, repositioning, and staged examples for reporting.", sourceStatus: "SME/source review required." },
      { title: "Vital signs - measurement and reporting", minutes: 25, summary: "Vital sign measurement, baseline comparison, abnormal findings, and reporting." },
      { title: "Monitoring, documentation, and reporting", minutes: 10, summary: "Objective monitoring and reporting changes." },
      { title: "Module 5 quiz", minutes: 15, summary: "Scenario checks include feeding orders, pressure injury staging, and vital sign reporting." },
    ],
    scenarioChecks: [
      {
        title: "Thickened liquid order",
        prompt:
          "A resident dislikes nectar-thick liquids. The CNA should not provide thin liquids; the CNA should offer ordered alternatives and report the concern to the nurse.",
        correctAnswer: "Follow the order and report the concern.",
        feedback: "Correct. CNAs do not change diet or liquid-consistency orders.",
        remediation: "Review feeding assistance and aspiration-prevention content.",
      },
      {
        title: "Blood pressure change from baseline",
        prompt:
          "A resident's blood pressure is 148/92 when baseline is about 130/80. The CNA should report the change to the nurse and document according to facility procedure.",
        correctAnswer: "Report the change to the nurse now, then document.",
        feedback: "Correct. A meaningful change from baseline should be reported.",
        remediation: "Review vital-sign reporting content.",
      },
    ],
    remediation: "Review Lessons 5.3 and 5.4 before retaking skin-integrity or vital-sign checks.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "Transcript planning exists for Module 5; skin-integrity narration is flagged. No audio generated.",
      transcriptSummary: "Narration would cover nutrition, feeding safety, skin integrity, vital signs, and observation/reporting.",
    },
    moodleNotes: "Moodle Lessons plus Quiz; skin-integrity items should remain flagged until SME/source review is complete.",
    reviewFlags: [
      { kind: "SME", note: "Skin integrity and pressure injury content is flagged for SME/source review." },
      { kind: "Source", note: "Exam items Q21 and Q38 are flagged for skin integrity review in the extracted question bank." },
      { kind: "Compliance", note: "Compliance review required before production wording is used." },
    ],
  },
  {
    id: "m6",
    title: "Module 6: Documentation, Reporting, PHI Avoidance, and Scope",
    time: "1.5 hr",
    required: true,
    status: "Seeded from extracted content",
    placeholder: false,
    sourcePath: "CNA-Recert-Course/Content/theory/modules/28_THEORY_MODULE_06_DOCUMENTATION_CHANGE_OF_CONDITION_SCOPE_FULL.md",
    sourceStatus: "Extracted source complete; compliance and CDPH/legal review still required before production.",
    summary:
      "Objective documentation, change-of-condition reporting, PHI avoidance, scope of practice, delegation, professionalism, and ethics.",
    objectives: [
      "Differentiate objective and subjective information.",
      "Document accurately and report changes in condition promptly.",
      "Identify changes that require immediate licensed-nurse notification.",
      "Stay within CNA scope of practice and delegation boundaries.",
      "Apply professionalism, confidentiality, truthfulness, and advocacy principles.",
    ],
    lessonSections: [
      { title: "Observation - objective vs subjective", minutes: 15, summary: "Distinguishes measurable findings from resident statements or interpretations." },
      { title: "Documentation standards", minutes: 20, summary: "Accurate, timely, factual documentation and correction boundaries." },
      { title: "Change of condition - what to report", minutes: 20, summary: "Immediate reporting for sudden changes, abnormal signs, and safety concerns." },
      { title: "CNA scope of practice", minutes: 15, summary: "Tasks CNAs may perform and out-of-scope tasks that must be referred." },
      { title: "Professionalism, ethics, delegation", minutes: 10, summary: "Confidentiality, honesty, advocacy, and chain-of-command behavior." },
      { title: "Module 6 quiz", minutes: 10, summary: "Objective documentation, reporting, and scope checks." },
    ],
    scenarioChecks: [
      {
        title: "Objective documentation",
        prompt:
          "A strong documentation note records time, observed intake, resident quote, fatigue, and nurse notification without adding a diagnosis.",
        correctAnswer: "Use factual, timed, objective documentation and report the change.",
        feedback: "Correct. Documentation should be accurate, objective, and tied to reporting action when needed.",
        remediation: "Review objective documentation standards.",
      },
      {
        title: "Out-of-scope sterile dressing",
        prompt:
          "If asked to perform a sterile wound dressing change, the CNA should decline the task as outside CNA scope and notify the nurse.",
        correctAnswer: "Decline and notify the nurse.",
        feedback: "Correct. CNAs must not perform tasks outside scope even when busy staff ask.",
        remediation: "Review CNA scope and delegation boundaries.",
      },
    ],
    remediation: "Review Lessons 6.3 and 6.4 before retaking reporting or scope checks.",
    tts: {
      sourcePath: "CNA-Recert-Course/Content/theory/tts/34_TTS_NARRATION_PACKAGE_COMPLETE.md",
      status: "Transcript planning exists for Module 6; no audio generated. Audio pending authorization.",
      transcriptSummary: "Narration would summarize objective observations, documentation, change reporting, scope, and professionalism.",
    },
    moodleNotes: "Moodle Lessons plus Quiz; required checks feed interaction and theory evidence without collecting PHI.",
    reviewFlags: [
      { kind: "Compliance", note: "Compliance review required before production wording is used." },
      { kind: "CDPH/Legal", note: "Scope and affidavit alignment should be reviewed before production use." },
    ],
  },
];

export const examPreviewQuestions = [
  {
    id: "Q04",
    module: "Module 2",
    sourcePath: "CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md",
    prompt: "A resident reports that money is missing from his wallet. Which abuse category is most directly involved?",
    answer: "Financial abuse or exploitation.",
    reviewStatus: "Extracted question bank; preview pending approval.",
  },
  {
    id: "Q09",
    module: "Module 3",
    sourcePath: "CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md",
    prompt: "A resident with Alzheimer's disease asks the same question repeatedly. What is the best CNA response?",
    answer: "Answer patiently each time.",
    reviewStatus: "Extracted question bank; Module 3 source file requires remediation before production use.",
  },
  {
    id: "Q17",
    module: "Module 4",
    sourcePath: "CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md",
    prompt: "A care plan requires a two-person transfer, but only one CNA is available. What should the CNA do?",
    answer: "Wait and obtain another trained staff member before transferring.",
    reviewStatus: "Extracted question bank; preview pending approval.",
  },
  {
    id: "Q21",
    module: "Module 5",
    sourcePath: "CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md",
    prompt: "A pressure injury with visible bone or tendon is identified in the source bank as a staging question.",
    answer: "Stage 4 pressure injury.",
    reviewStatus: "SME/source review required for skin-integrity question before production use.",
  },
  {
    id: "Q25",
    module: "Module 6",
    sourcePath: "CNA-Recert-Course/Content/theory/exam/30_FINAL_EXAM_POOL_50_COMPLETE.md",
    prompt: "Which note is most objective and appropriate for a CNA documentation record?",
    answer: "A factual, timed note with observable details and nurse notification when needed.",
    reviewStatus: "Extracted question bank; preview pending approval.",
  },
];
