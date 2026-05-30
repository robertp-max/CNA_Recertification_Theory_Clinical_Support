// Phase 1 prototype lesson data — Module 1: Infection Control and PPE.
// Adapted from CNA-Recert-Course/Content/theory/modules/05_THEORY_MODULE_01_INFECTION_CONTROL_FULL.md
// SME/source-review status is surfaced to reviewers only (see reviewerNote).

export type KnowledgeCheckChoice = { id: string; label: string };

export type KnowledgeCheck = {
  prompt: string;
  choices: KnowledgeCheckChoice[];
  correctId: string;
  feedbackCorrect: string;
  feedbackIncorrect: string;
};

export type Module1Lesson = {
  id: string;
  index: number;
  title: string;
  estMinutes: number;
  learningGoal: string;
  scenario: string;
  keyConcept: string;
  whyItMatters: string[];
  practiceExample: string;
  commonMistake: string;
  knowledgeCheck: KnowledgeCheck;
  keyTerms: { term: string; definition: string }[];
  transcript: string;
  summary: string;
};

export const module1Meta = {
  id: "m1",
  code: "M1",
  title: "Infection Control and PPE",
  estHours: 1.5,
  estMinutes: 90,
  intro:
    "Infection control is one of the most important things you do every day. In long-term care, residents are especially vulnerable — and you are often the first person to notice when something is wrong. This module helps you stay sharp.",
  learningObjectives: [
    "Describe healthcare-associated infections (HAIs) and why LTC residents are at higher risk.",
    "Identify the six links in the chain of infection.",
    "Demonstrate proper hand hygiene technique, including the WHO 5 Moments.",
    "Select the correct PPE for common CNA tasks.",
    "Recognize common signs and symptoms of infection in LTC residents.",
    "Apply environmental cleaning and safe linen handling principles.",
  ],
  reviewerNote:
    "SME/SOURCE REVIEW REQUIRED: There is no dedicated NATP 10–17 infection-control module. Content is drafted from legacy CNA-CE-001 + scattered NATP references and must be SME-verified before production. The graded module quiz is referenced in the source but not yet authored (Phase 2).",
};

export const module1Lessons: Module1Lesson[] = [
  {
    id: "l1",
    index: 1,
    title: "Why Infection Control Matters in Long-Term Care",
    estMinutes: 15,
    learningGoal: "Explain why long-term care residents are at higher risk for infection and the CNA's role in prevention.",
    scenario:
      "It is a busy morning shift. You are moving between several residents — helping with breakfast, changing linens, and answering call lights. Each contact is a chance to either spread germs or stop them.",
    keyConcept:
      "A healthcare-associated infection (HAI) is an infection a person gets while receiving care. LTC residents are especially vulnerable because of advanced age, chronic conditions, indwelling devices, shared living spaces, and frequent hands-on care. As a CNA you are positioned to both prevent infections and recognize them early.",
    whyItMatters: [
      "Residents with weakened immune systems can become seriously ill from common germs.",
      "You have more contact with residents than any other caregiver.",
      "Early recognition and prevention protect every resident on the unit.",
    ],
    practiceExample:
      "Before and after helping each resident with breakfast, you perform hand hygiene — turning routine care into active infection prevention.",
    commonMistake: "Treating infection control as 'extra' steps instead of a core part of safe, compassionate care.",
    knowledgeCheck: {
      prompt: "Why are long-term care residents at higher risk for infection?",
      choices: [
        { id: "a", label: "They are younger and more active than hospital patients." },
        { id: "b", label: "Advanced age, chronic conditions, shared spaces, and frequent hands-on care." },
        { id: "c", label: "They never share common areas or equipment." },
        { id: "d", label: "They rarely need assistance from caregivers." },
      ],
      correctId: "b",
      feedbackCorrect:
        "Correct. Age, chronic illness, devices, shared spaces, and frequent caregiver contact all raise infection risk in LTC.",
      feedbackIncorrect:
        "Not quite. LTC residents are higher-risk because of advanced age, chronic conditions, shared living spaces, and frequent hands-on care.",
    },
    keyTerms: [
      { term: "HAI", definition: "Healthcare-associated infection — an infection acquired while receiving care." },
      { term: "Indwelling device", definition: "A device such as a catheter or feeding tube that creates an entry point for germs." },
    ],
    transcript:
      "Infection control is one of the most important things you do every day. Long-term care residents are especially vulnerable because of age, chronic conditions, devices, and shared spaces. As a CNA, every hand wash and glove change is infection control in action.",
    summary: "LTC residents are high-risk; the CNA is central to both preventing and recognizing infection.",
  },
  {
    id: "l2",
    index: 2,
    title: "The Chain of Infection",
    estMinutes: 15,
    learningGoal: "Identify the six links in the chain of infection and how CNAs break it.",
    scenario:
      "A resident has a productive cough. You think about how that germ could travel — from the resident, through the air or your hands, to the next person you care for.",
    keyConcept:
      "Infections spread through six connected links: infectious agent, reservoir, portal of exit, mode of transmission, portal of entry, and susceptible host. Breaking any single link stops the spread. Hand hygiene breaks the chain at the most common transmission point.",
    whyItMatters: [
      "Understanding the chain shows you where your actions make the biggest difference.",
      "Hand hygiene is the single most effective break point.",
      "Cleaning, PPE, and reporting each break a different link.",
    ],
    practiceExample:
      "After helping the coughing resident, you perform hand hygiene before touching anything else — breaking the 'mode of transmission' link.",
    commonMistake: "Assuming gowns or hourly surface cleaning matter more than consistent hand hygiene.",
    knowledgeCheck: {
      prompt: "Which is the MOST effective way to break the chain of infection in daily CNA practice?",
      choices: [
        { id: "a", label: "Wearing a gown for every resident interaction." },
        { id: "b", label: "Hand hygiene before and after each resident contact." },
        { id: "c", label: "Disinfecting all surfaces every hour." },
        { id: "d", label: "Isolating all residents with chronic conditions." },
      ],
      correctId: "b",
      feedbackCorrect:
        "Correct. Hand hygiene is consistently identified as the single most effective infection-prevention measure.",
      feedbackIncorrect:
        "Not quite. Hand hygiene before and after every resident contact has the greatest impact on breaking the chain.",
    },
    keyTerms: [
      { term: "Reservoir", definition: "Where a germ lives and multiplies (a person, surface, or standing water)." },
      { term: "Mode of transmission", definition: "How a germ travels to a new host — broken most often by hand hygiene." },
    ],
    transcript:
      "Infections spread through six links: agent, reservoir, portal of exit, mode of transmission, portal of entry, and susceptible host. Break any link to stop the spread. Hand hygiene breaks the chain at the most common point.",
    summary: "Six links form the chain of infection; hand hygiene is the strongest break point.",
  },
  {
    id: "l3",
    index: 3,
    title: "Hand Hygiene — Your Most Important Tool",
    estMinutes: 15,
    learningGoal: "Choose correctly between soap-and-water and sanitizer, and apply the WHO 5 Moments.",
    scenario:
      "You just helped a resident with a bowel movement and removed your gloves. Your hands look clean. You're already thinking about your next task down the hall.",
    keyConcept:
      "Alcohol-based sanitizer is fine between routine contacts when hands are not visibly soiled. But after body-fluid contact — even with gloves on — you must wash with soap and water for 20 seconds. Sanitizer does not kill all germs (for example, C. difficile spores and norovirus). The WHO 5 Moments define when hand hygiene is required.",
    whyItMatters: [
      "Gloves leak and hands get contaminated during removal.",
      "Soap and water physically removes spores sanitizer cannot kill.",
      "Clean hands protect the next resident you touch.",
    ],
    practiceExample:
      "Before leaving the room you step to the sink, wash for a full 20 seconds, dry, then continue to your next task.",
    commonMistake: "Using hand sanitizer instead of soap and water after contact with fecal matter or C. diff.",
    knowledgeCheck: {
      prompt:
        "A CNA has just assisted a resident with a bowel movement and removed their gloves. Their hands appear clean. What should the CNA do?",
      choices: [
        { id: "a", label: "Use alcohol-based hand sanitizer." },
        { id: "b", label: "Wash hands with soap and water." },
        { id: "c", label: "Put on new gloves immediately." },
        { id: "d", label: "Wipe hands on their scrubs." },
      ],
      correctId: "b",
      feedbackCorrect:
        "Correct. After exposure to body fluids — even if gloves were worn — soap and water handwashing is required.",
      feedbackIncorrect:
        "Not quite. After body-fluid exposure, always wash with soap and water; sanitizer alone is not sufficient after contact with fecal matter.",
    },
    keyTerms: [
      { term: "WHO 5 Moments", definition: "Before touching a resident, before a clean/aseptic task, after fluid exposure risk, after touching a resident, after touching their surroundings." },
      { term: "C. difficile", definition: "A spore-forming bacterium that requires soap-and-water handwashing; sanitizer is not enough." },
    ],
    transcript:
      "Use sanitizer between routine contacts, but wash with soap and water for twenty seconds after body-fluid contact even if you wore gloves. Sanitizer does not kill C. diff spores or norovirus.",
    summary: "Soap and water after body fluids; sanitizer only for routine, non-soiled contacts.",
  },
  {
    id: "l4",
    index: 4,
    title: "Personal Protective Equipment (PPE)",
    estMinutes: 15,
    learningGoal: "Apply standard precautions, select PPE by task, and follow the correct donning/doffing order.",
    scenario:
      "You are about to assist a resident with perineal care, where splashing of body fluids is possible.",
    keyConcept:
      "Standard precautions assume all body fluids (except sweat) may be infectious — protect every resident, every time. Match PPE to the task. Donning order: gown → mask → eye protection → gloves. Doffing order: gloves → eye protection → gown → mask, because gloves are the most contaminated item. Perform hand hygiene after removing all PPE.",
    whyItMatters: [
      "Removing gloves first reduces the chance of touching your face with contaminated gloves.",
      "Standard precautions protect you and every resident, not just known-infected residents.",
      "The right PPE for the task prevents exposure without wasting supplies.",
    ],
    practiceExample:
      "For perineal care you wear gloves, and add a gown if there is a splashing risk; afterward you doff gloves first and wash your hands.",
    commonMistake: "Removing the gown or mask before the gloves during doffing.",
    knowledgeCheck: {
      prompt: "When removing PPE, which item should a CNA remove FIRST?",
      choices: [
        { id: "a", label: "Gown" },
        { id: "b", label: "Mask" },
        { id: "c", label: "Gloves" },
        { id: "d", label: "Eye protection" },
      ],
      correctId: "c",
      feedbackCorrect: "Correct. Gloves are removed first because they are the most contaminated item.",
      feedbackIncorrect: "Not quite. Gloves come off first. Remember: Gloves → Eye protection → Gown → Mask.",
    },
    keyTerms: [
      { term: "Standard precautions", definition: "Treating all body fluids (except sweat) as potentially infectious for every resident." },
      { term: "Doffing", definition: "Removing PPE in the correct order: gloves, eye protection, gown, mask." },
    ],
    transcript:
      "Standard precautions protect every resident every time. Don PPE gown, mask, eye protection, gloves. Doff in reverse, gloves first, because they are most contaminated. Wash your hands after.",
    summary: "Match PPE to the task; doff gloves first; hand hygiene after every removal.",
  },
  {
    id: "l5",
    index: 5,
    title: "Recognizing and Reporting Infection Signs",
    estMinutes: 15,
    learningGoal: "Recognize early signs of infection and report changes from baseline immediately.",
    scenario:
      "An 87-year-old resident (fictional, 'Mrs. J') who is normally alert and oriented suddenly seems confused and agitated during your shift.",
    keyConcept:
      "You see residents more often than anyone else, so you are often first to notice change. Report signs such as fever, new cough, cloudy or foul-smelling urine, wound redness/drainage, decreased intake, and — especially in elderly residents — new confusion. You report; the nurse assesses.",
    whyItMatters: [
      "In elderly residents, new confusion may be the FIRST sign of infection.",
      "Prompt reporting can prevent a small problem from becoming an emergency.",
      "Reporting a concern is never wrong; not reporting one can be dangerous.",
    ],
    practiceExample:
      "You notice Mrs. J's new confusion and report it to the licensed nurse right away, rather than waiting for charting time.",
    commonMistake: "Waiting to document a change instead of reporting it to the nurse immediately.",
    knowledgeCheck: {
      prompt:
        "An 87-year-old resident who is normally alert and oriented suddenly seems confused and agitated. The CNA's best first action is to:",
      choices: [
        { id: "a", label: "Assume the resident did not sleep well." },
        { id: "b", label: "Report the change to the licensed nurse immediately." },
        { id: "c", label: "Wait to see if the confusion resolves by the next day." },
        { id: "d", label: "Document the change and continue with other tasks." },
      ],
      correctId: "b",
      feedbackCorrect:
        "Correct. New confusion in an elderly resident may be the first sign of infection — report it immediately.",
      feedbackIncorrect:
        "Not quite. New confusion in an elderly resident should be reported to the nurse immediately; it may be the first sign of infection.",
    },
    keyTerms: [
      { term: "Baseline", definition: "A resident's normal status; changes from baseline should be reported." },
      { term: "Change of condition", definition: "Any new or worsening sign that the licensed nurse needs to assess." },
    ],
    transcript:
      "You are often first to notice change. Report fever, new cough, urine changes, wound changes, decreased intake, and especially new confusion in elderly residents. You report; the nurse assesses.",
    summary: "Report changes from baseline immediately — confusion in the elderly is a key early sign.",
  },
  {
    id: "l6",
    index: 6,
    title: "Environmental Cleaning and Safe Practices",
    estMinutes: 15,
    learningGoal: "Apply environmental cleaning, safe linen handling, and sharps-safety principles.",
    scenario:
      "You are stripping a soiled bed and preparing to take the linens to the hamper at the end of the hall.",
    keyConcept:
      "A clean environment breaks the chain at the reservoir link. Clean high-touch surfaces, work clean-to-dirty and top-to-bottom, and use approved disinfectants for the full contact time. Hold soiled linen away from your body, never shake it, and place it directly in the designated container. Never recap needles; use sharps containers and report injuries.",
    whyItMatters: [
      "Shaking soiled linen launches germs into the air.",
      "Correct contact time is required for disinfectants to actually work.",
      "Sharps safety prevents needlestick injuries and exposure.",
    ],
    practiceExample:
      "You roll the soiled linen inward, hold it away from your body, and place it straight into the linen bag without shaking it.",
    commonMistake: "Shaking soiled linen or placing it on the floor while preparing the hamper.",
    knowledgeCheck: {
      prompt: "When handling soiled linen, a CNA should:",
      choices: [
        { id: "a", label: "Shake the linen to remove debris before bagging it." },
        { id: "b", label: "Hold the linen close to their body for stability." },
        { id: "c", label: "Hold the linen away from their body and place it directly in the linen bag." },
        { id: "d", label: "Place the linen on the floor temporarily." },
      ],
      correctId: "c",
      feedbackCorrect: "Correct. Hold soiled linen away from your body and place it directly in the container; never shake it.",
      feedbackIncorrect: "Not quite. Never shake soiled linen. Hold it away from your body and place it directly in the linen bag.",
    },
    keyTerms: [
      { term: "Contact time", definition: "The time a disinfectant must stay wet on a surface to kill germs." },
      { term: "Clean-to-dirty", definition: "Cleaning from the least to most contaminated areas to avoid spreading germs." },
    ],
    transcript:
      "Clean high-touch surfaces, work clean to dirty and top to bottom, and respect disinfectant contact time. Hold soiled linen away from your body, never shake it, and never recap needles.",
    summary: "Clean methodically, handle linen safely, and follow sharps safety to break the chain.",
  },
];

export const module1LessonIds = module1Lessons.map((lesson) => lesson.id);
