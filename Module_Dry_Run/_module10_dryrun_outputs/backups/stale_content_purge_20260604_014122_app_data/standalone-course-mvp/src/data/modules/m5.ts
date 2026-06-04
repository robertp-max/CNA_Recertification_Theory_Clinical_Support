import type { ModuleDef } from "../lessonModel";

// Module 5 — Nutrition, Skin Integrity, Vital Signs, and Observation.
// Skin integrity content carries an SME/source review flag (surfaced to reviewers).
export const m5: ModuleDef = {
  id: "m5",
  code: "M5",
  title: "Module 5: Nutrition, Skin Integrity, Vital Signs, and Observation",
  shortTitle: "Nutrition, Skin & Vitals",
  time: "2.0 hr",
  summary: "Nutrition and hydration, aspiration prevention, skin integrity, vital signs, and observation/reporting.",
  kind: "lesson",
  status: "sme-review",
  countsTowardTheory: true,
  reviewerNote:
    "Skin integrity / pressure injury content and exam items Q21 & Q38 are flagged for SME/source review before production.",
  learningObjectives: [
    "Support nutrition and hydration within diet-order boundaries.",
    "Use safe feeding assistance and aspiration-prevention practices.",
    "Recognize skin integrity concerns for reporting (SME review pending).",
    "Measure and report vital signs and changes from baseline.",
  ],
  lessons: [
    {
      id: "l1",
      index: 1,
      title: "Nutrition, Hydration, and Feeding Safety",
      estMinutes: 25,
      learningGoal: "Follow diet and liquid-consistency orders and report concerns.",
      scenario: "A resident on nectar-thick liquids dislikes them and asks you for a glass of regular water.",
      keyConcept:
        "CNAs do not change diet or liquid-consistency orders. Thickened liquids are ordered to prevent aspiration. Offer ordered alternatives, encourage intake, and report the resident's concern to the nurse.",
      whyItMatters: [
        "Thin liquids can cause aspiration and pneumonia for at-risk residents.",
        "Diet orders are clinical decisions outside CNA scope to change.",
        "Reporting the concern lets the nurse reassess if appropriate.",
      ],
      practiceExample: "You kindly explain you can only provide the ordered thickened liquids, offer flavored options, and report her dislike to the nurse.",
      commonMistake: "Giving thin liquids because the resident dislikes thickened ones.",
      knowledgeCheck: {
        prompt: "A resident on nectar-thick liquids dislikes them and wants thin water. The CNA should:",
        choices: [
          { id: "a", label: "Give a small amount of thin water." },
          { id: "b", label: "Follow the order, offer ordered alternatives, and report the concern to the nurse." },
          { id: "c", label: "Change the order to regular liquids." },
          { id: "d", label: "Withhold all fluids until the next meal." },
        ],
        correctId: "b",
        feedbackCorrect: "Correct. CNAs follow diet/consistency orders and report concerns; they do not change orders.",
        feedbackIncorrect: "Not quite. Remember that CNAs cannot change consistency orders — follow the order and report the concern. Try again.",
        remediation: "Review feeding assistance and aspiration prevention in this lesson.",
      },
      keyTerms: [
        { term: "Aspiration", definition: "Food or liquid entering the airway/lungs, risking pneumonia." },
        { term: "Thickened liquids", definition: "Liquids ordered at a set consistency to reduce aspiration risk." },
      ],
      transcript: "CNAs do not change diet or liquid-consistency orders. Offer ordered options, encourage intake, and report concerns to the nurse.",
      summary: "Follow diet/consistency orders exactly; report concerns instead of changing orders.",
    },
    {
      id: "l2",
      index: 2,
      title: "Skin Integrity and Pressure Injury Awareness",
      estMinutes: 25,
      learningGoal: "Recognize and report skin concerns and reposition to prevent pressure injuries.",
      scenario: "While giving care you notice a reddened area over a resident's tailbone that does not fade.",
      keyConcept:
        "Reposition at-risk residents on schedule, keep skin clean and dry, and report any new redness, breakdown, or non-blanching areas to the nurse. Never massage reddened bony areas. (This section is pending SME/source review.)",
      whyItMatters: [
        "Early reporting can stop a pressure injury from worsening.",
        "Repositioning relieves pressure that damages tissue.",
        "Massaging reddened bony prominences can worsen tissue damage.",
      ],
      practiceExample: "You reposition the resident off the area, keep the skin clean and dry, and report the non-fading redness to the nurse.",
      commonMistake: "Massaging a reddened bony prominence, which can worsen damage.",
      knowledgeCheck: {
        prompt: "A CNA notices non-fading redness over a resident's tailbone. The CNA should:",
        choices: [
          { id: "a", label: "Massage the area to improve circulation." },
          { id: "b", label: "Reposition off the area, keep skin clean/dry, and report to the nurse." },
          { id: "c", label: "Apply heat to the area." },
          { id: "d", label: "Wait a week to see if it resolves." },
        ],
        correctId: "b",
        feedbackCorrect: "Correct. Reposition, protect the skin, and report; never massage reddened bony prominences.",
        feedbackIncorrect: "Not quite. Remember to reposition and report — and never massage a reddened bony prominence. Try again.",
        remediation: "Review skin integrity and pressure-injury prevention in this lesson.",
      },
      keyTerms: [
        { term: "Pressure injury", definition: "Skin/tissue damage from sustained pressure, often over bony areas." },
        { term: "Non-blanching redness", definition: "Redness that does not fade with light pressure — an early warning sign." },
      ],
      transcript: "Reposition at-risk residents, keep skin clean and dry, report new redness or breakdown, and never massage reddened bony prominences.",
      summary: "Prevent and report pressure injuries; never massage reddened bony areas.",
      smeFlag: "Skin integrity / pressure injury content requires SME/source review before production use.",
    },
    {
      id: "l3",
      index: 3,
      title: "Vital Signs and Reporting Changes",
      estMinutes: 25,
      learningGoal: "Measure vital signs and report meaningful changes from baseline.",
      scenario: "A resident whose baseline blood pressure is about 130/80 reads 148/92 this morning.",
      keyConcept:
        "Measure vital signs per facility policy, compare to the resident's baseline, and report meaningful changes to the nurse, then document per procedure. CNAs report; the nurse interprets and acts.",
      whyItMatters: [
        "A change from baseline can be the first sign of a problem.",
        "Timely reporting allows early nursing assessment.",
        "Accurate measurement and documentation support safe care.",
      ],
      practiceExample: "You recheck if appropriate, report the elevated reading to the nurse now, and document per facility procedure.",
      commonMistake: "Only charting an abnormal vital sign without reporting it promptly.",
      knowledgeCheck: {
        prompt: "A resident's BP is 148/92 with a baseline near 130/80. The CNA should:",
        choices: [
          { id: "a", label: "Chart it and continue without reporting." },
          { id: "b", label: "Report the change to the nurse now, then document per procedure." },
          { id: "c", label: "Tell the resident to rest and recheck tomorrow." },
          { id: "d", label: "Adjust the resident's medication." },
        ],
        correctId: "b",
        feedbackCorrect: "Correct. A meaningful change from baseline should be reported to the nurse, then documented.",
        feedbackIncorrect: "Not quite. Remember to report meaningful changes from baseline promptly, then document. Try again.",
        remediation: "Review vital-sign reporting in this lesson.",
      },
      keyTerms: [
        { term: "Baseline", definition: "A resident's usual measurements used for comparison." },
        { term: "Vital signs", definition: "Temperature, pulse, respirations, blood pressure, and often O2 saturation/pain." },
      ],
      transcript: "Measure vital signs per policy, compare to baseline, report meaningful changes to the nurse, then document.",
      summary: "Compare vitals to baseline and report meaningful changes before documenting.",
    },
  ],
};
