import type { ModuleDef } from "../lessonModel";

// Module 2 — Resident Rights, Abuse Prevention, and Boundaries.
// Adapted from Content/theory/modules/24_THEORY_MODULE_02_... (seeded scenario checks reused).
export const m2: ModuleDef = {
  id: "m2",
  code: "M2",
  title: "Module 2: Resident Rights, Abuse Prevention, and Boundaries",
  shortTitle: "Resident Rights & Abuse Prevention",
  time: "2.0 hr",
  summary: "Resident rights, abuse and neglect, objective observation, mandated reporting, and professional boundaries.",
  kind: "lesson",
  status: "sme-review",
  countsTowardTheory: true,
  reviewerNote:
    "Compliance + CDPH/legal review required before production. NATP Module 17 (6 hr) is compressed to 2 hr — content prioritized.",
  learningObjectives: [
    "Define resident rights, dignity, privacy, autonomy, and grievance protections.",
    "Identify the categories of abuse, neglect, and exploitation.",
    "Recognize objective signs that must be reported, without investigating.",
    "Apply CNA mandated-reporter responsibilities and professional boundaries.",
  ],
  lessons: [
    {
      id: "l1",
      index: 1,
      title: "Resident Rights Foundation",
      estMinutes: 20,
      learningGoal: "Describe core resident rights and protect a resident's right to voice concerns.",
      scenario: "A resident tells you she is afraid to complain about the food because staff might get angry with her.",
      keyConcept:
        "Residents have rights to dignity, privacy, autonomy, and to voice grievances without retaliation. Supporting those rights is part of every CNA's role. You support the resident's right to complain and follow your facility's reporting/support steps.",
      whyItMatters: [
        "Grievance rights are protected by law; retaliation is never acceptable.",
        "Residents who feel safe to speak up get safer care.",
        "Dignity and choice are part of quality care, not extras.",
      ],
      practiceExample: "You reassure the resident she may raise concerns safely and let the nurse/supervisor know per facility process.",
      commonMistake: "Discouraging a resident from complaining to 'keep the peace.'",
      knowledgeCheck: {
        prompt: "A resident is afraid to complain about food because staff might get angry. The best CNA response is to:",
        choices: [
          { id: "a", label: "Tell her complaints usually cause problems." },
          { id: "b", label: "Support her grievance right without retaliation and follow facility reporting steps." },
          { id: "c", label: "Ask her to wait until the next care conference." },
          { id: "d", label: "Handle the kitchen staff yourself." },
        ],
        correctId: "b",
        feedbackCorrect: "Correct. Residents have the right to voice concerns without retaliation; support that right and follow facility steps.",
        feedbackIncorrect: "Not quite. Remember that grievance rights are protected — support the resident and follow facility reporting steps. Try again.",
        remediation: "Review resident rights and grievance protections in this lesson.",
      },
      keyTerms: [
        { term: "Grievance right", definition: "A resident's protected right to raise concerns without retaliation." },
        { term: "Autonomy", definition: "A resident's right to make choices about their own care and daily life." },
      ],
      transcript: "Residents have rights to dignity, privacy, autonomy, and to complain without retaliation. Support those rights and follow facility processes.",
      summary: "Protect resident dignity, choice, and the right to voice concerns without retaliation.",
    },
    {
      id: "l2",
      index: 2,
      title: "Types of Abuse and Neglect",
      estMinutes: 25,
      learningGoal: "Identify the major categories of abuse, neglect, and exploitation.",
      scenario: "During report you hear that a resident's spending money keeps going missing from his room.",
      keyConcept:
        "Abuse can be physical, verbal/psychological, sexual, or financial. Neglect, abandonment, involuntary seclusion, and exploitation are also reportable. Missing money or belongings points to possible financial abuse or exploitation.",
      whyItMatters: [
        "Recognizing categories helps you describe what you observed accurately.",
        "Financial exploitation is easy to miss but seriously harms residents.",
        "Every category must be reported, not investigated by the CNA.",
      ],
      practiceExample: "You document the objective observation (missing money as reported) and notify the nurse/supervisor rather than questioning other staff.",
      commonMistake: "Assuming only physical harm 'counts' as abuse.",
      knowledgeCheck: {
        prompt: "A resident reports that money is missing from his wallet. Which abuse category is most directly involved?",
        choices: [
          { id: "a", label: "Physical abuse" },
          { id: "b", label: "Involuntary seclusion" },
          { id: "c", label: "Financial abuse or exploitation" },
          { id: "d", label: "Neglect" },
        ],
        correctId: "c",
        feedbackCorrect: "Correct. Missing money or belongings points to financial abuse or exploitation.",
        feedbackIncorrect: "Not quite. Remember that missing money or property indicates financial abuse/exploitation. Try again.",
        remediation: "Review the abuse and neglect categories in this lesson.",
      },
      keyTerms: [
        { term: "Exploitation", definition: "Misuse of a resident's money, property, or resources." },
        { term: "Involuntary seclusion", definition: "Separating a resident from others against their will, outside care-plan orders." },
      ],
      transcript: "Abuse includes physical, verbal, psychological, sexual, and financial harm, plus neglect, abandonment, and exploitation. Missing money suggests financial abuse.",
      summary: "Abuse and neglect take many forms — financial exploitation included; all are reportable.",
    },
    {
      id: "l3",
      index: 3,
      title: "Signs, Evidence, and Mandated Reporting",
      estMinutes: 25,
      learningGoal: "Apply mandated-reporter duties: ensure safety, report promptly, document objectively.",
      scenario: "A resident tells you a night-shift CNA slapped him. You notice no visible mark.",
      keyConcept:
        "CNAs are mandated reporters. When abuse is suspected, ensure the resident's immediate safety, report to the licensed nurse/supervisor right away, and document objectively. You do not investigate, confront the accused, or wait for proof.",
      whyItMatters: [
        "Prompt reporting protects the resident and meets legal duty.",
        "Objective documentation supports a fair, accurate review.",
        "Investigating yourself can compromise safety and the process.",
      ],
      practiceExample: "You make sure the resident is safe, report immediately to the nurse, and write exactly what the resident said in his own words.",
      commonMistake: "Waiting for proof or telling the accused coworker before reporting.",
      knowledgeCheck: {
        prompt: "A resident says a night CNA slapped him. The best CNA action is to:",
        choices: [
          { id: "a", label: "Ask other staff if it really happened first." },
          { id: "b", label: "Wait to see if a bruise appears." },
          { id: "c", label: "Ensure safety, report immediately to the nurse/supervisor, and document objectively." },
          { id: "d", label: "Tell the accused coworker to be careful." },
        ],
        correctId: "c",
        feedbackCorrect: "Correct. CNAs ensure safety, report suspected abuse promptly, and document objectively — they do not investigate.",
        feedbackIncorrect: "Not quite. Remember that CNAs report suspected abuse immediately and do not investigate or wait for proof. Try again.",
        remediation: "Review mandated reporter obligations in this lesson.",
      },
      keyTerms: [
        { term: "Mandated reporter", definition: "A worker legally required to report suspected abuse promptly." },
        { term: "Objective documentation", definition: "Factual notes of what was seen/heard, including the resident's own words." },
      ],
      transcript: "CNAs are mandated reporters. Ensure safety, report suspected abuse immediately, and document objectively. Do not investigate or wait for proof.",
      summary: "Suspected abuse: safety first, report immediately, document objectively — never investigate.",
      smeFlag: "Reporting/CDPH alignment requires compliance review before production.",
    },
    {
      id: "l4",
      index: 4,
      title: "Prevention, Boundaries, and Safety",
      estMinutes: 20,
      learningGoal: "Apply professional boundaries and prevention strategies in daily care.",
      scenario: "A resident offers you a generous cash 'tip' for the extra help you gave today.",
      keyConcept:
        "Professional boundaries protect both residents and CNAs. Accepting money or gifts, sharing personal contact, or doing favors outside policy can blur boundaries and enable exploitation. Decline gracefully and follow facility policy.",
      whyItMatters: [
        "Clear boundaries prevent exploitation and protect your certification.",
        "Respectful, consistent care is the best abuse-prevention tool.",
        "Policies exist to protect residents and staff alike.",
      ],
      practiceExample: "You thank the resident warmly, explain you cannot accept tips, and let your supervisor know per policy.",
      commonMistake: "Accepting gifts or money because it feels rude to refuse.",
      knowledgeCheck: {
        prompt: "A resident offers a CNA a cash tip for good care. The CNA should:",
        choices: [
          { id: "a", label: "Accept it quietly so the resident isn't offended." },
          { id: "b", label: "Decline graciously and follow facility policy." },
          { id: "c", label: "Accept it and split it with coworkers." },
          { id: "d", label: "Accept only small amounts." },
        ],
        correctId: "b",
        feedbackCorrect: "Correct. Declining gifts/tips maintains professional boundaries and protects residents and staff.",
        feedbackIncorrect: "Not quite. Remember that professional boundaries mean declining tips and following facility policy. Try again.",
        remediation: "Review professional boundaries in this lesson.",
      },
      keyTerms: [
        { term: "Professional boundary", definition: "The limits that keep the caregiver–resident relationship safe and ethical." },
      ],
      transcript: "Professional boundaries protect residents and CNAs. Decline gifts and tips, follow policy, and provide consistent respectful care.",
      summary: "Maintain professional boundaries and prevent abuse through respectful, policy-based care.",
    },
  ],
};
