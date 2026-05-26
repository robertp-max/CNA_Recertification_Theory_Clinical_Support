export type GateKey =
  | "providerOverride"
  | "legalName"
  | "cnaNumber"
  | "onlineCapAcknowledgement"
  | "theoryActivity"
  | "interaction"
  | "activeTimeOrManualReview"
  | "finalExamPassed"
  | "affidavitComplete"
  | "certificateFieldsPopulated"
  | "adminHoldClear";

export type GateDefinition = {
  key: GateKey;
  label: string;
  source: string;
};

export type GateScenario = {
  id: string;
  name: string;
  summary: string;
  gates: Record<GateKey, boolean>;
  optionalClinical: Record<string, boolean>;
};

export const executiveCards = [
  {
    title: "Prevents Premature Certificates",
    text: "Certificate preview remains locked until required online CE gates are complete.",
  },
  {
    title: "Separates Required CE From Optional Support",
    text: "Optional clinical support helps learners but does not inflate CE progress or gate the certificate.",
  },
  {
    title: "Audit-Ready Decision Trail",
    text: "Every certificate decision can show what passed, what failed, and what evidence would be exported.",
  },
  {
    title: "Moodle Migration Ready",
    text: "The standalone gate model maps to Moodle restrictions, completion settings, quiz results, affidavit workflow, active-time review, and certificate issue logs.",
  },
];

export const gateDefinitions: GateDefinition[] = [
  {
    key: "providerOverride",
    label: "Provider/course approval metadata or reviewer override present",
    source: "Approval/NAC# metadata placeholder or reviewer-only override",
  },
  { key: "legalName", label: "Legal name present", source: "Required user profile field" },
  { key: "cnaNumber", label: "CNA certificate number present", source: "Required user profile field" },
  { key: "onlineCapAcknowledgement", label: "Online cap acknowledgement complete", source: "Module 0 acknowledgement" },
  { key: "theoryActivity", label: "Required theory activity complete", source: "Required module completion report" },
  { key: "interaction", label: "Required interaction/check complete", source: "Scenario/check attempt record" },
  {
    key: "activeTimeOrManualReview",
    label: "Simulated active-time or manual review hold cleared",
    source: "Review active-time gate; Moodle validation pending",
  },
  { key: "finalExamPassed", label: "Final exam/test passed", source: "Final quiz/test attempt record" },
  { key: "affidavitComplete", label: "Final signed statement/affidavit complete", source: "Draft affidavit workflow" },
  { key: "certificateFieldsPopulated", label: "Certificate fields populated", source: "Certificate field map" },
  { key: "adminHoldClear", label: "Admin hold clear", source: "Manual compliance hold" },
];

const passingGates: Record<GateKey, boolean> = {
  providerOverride: true,
  legalName: true,
  cnaNumber: true,
  onlineCapAcknowledgement: true,
  theoryActivity: true,
  interaction: true,
  activeTimeOrManualReview: true,
  finalExamPassed: true,
  affidavitComplete: true,
  certificateFieldsPopulated: true,
  adminHoldClear: true,
};

const optionalComplete = {
  hub: true,
  skills: true,
  confidence: true,
  documentation: true,
  help: true,
};

const optionalSkipped = {
  hub: false,
  skills: false,
  confidence: false,
  documentation: false,
  help: false,
};

function scenario(id: string, name: string, summary: string, failedGate?: GateKey, optionalClinical = optionalSkipped): GateScenario {
  return {
    id,
    name,
    summary,
    gates: failedGate ? { ...passingGates, [failedGate]: false } : { ...passingGates },
    optionalClinical,
  };
}

export const gateScenarios: GateScenario[] = [
  scenario("passing", "Passing learner", "All required online CE gates pass. Optional support may be viewed or skipped.", undefined, optionalComplete),
  scenario("missing-legal-name", "Missing legal name", "Identity is incomplete, so the certificate cannot release.", "legalName"),
  scenario("missing-cna-number", "Missing CNA number", "Required certificate identity metadata is incomplete.", "cnaNumber"),
  scenario("online-cap-missing", "Online cap acknowledgement missing", "The learner has not acknowledged the online CE cap and partial-credit boundary.", "onlineCapAcknowledgement"),
  scenario("required-theory-incomplete", "Required theory incomplete", "Required theory completion evidence is missing.", "theoryActivity", { ...optionalComplete }),
  scenario("interaction-incomplete", "Required interaction/check incomplete", "Required feedback/check evidence is missing.", "interaction"),
  scenario("active-time-not-met", "Active-time not met", "Simulated active-time/manual review requirement is not cleared.", "activeTimeOrManualReview"),
  scenario("final-exam-failed", "Final exam failed", "The final exam/test gate has not passed.", "finalExamPassed"),
  scenario("affidavit-missing", "Affidavit missing", "Final signed statement evidence is missing.", "affidavitComplete"),
  scenario("certificate-fields-missing", "Certificate fields missing", "Required certificate output fields are incomplete.", "certificateFieldsPopulated"),
  scenario("admin-hold-active", "Admin hold active", "A manual admin/compliance hold is active.", "adminHoldClear", { ...optionalComplete, confidence: false }),
  scenario("optional-clinical-skipped", "Optional clinical support skipped", "Required gates pass even when optional support is skipped.", undefined, optionalSkipped),
];

export const optionalClinicalBoundaryRows = [
  { key: "hub", label: "Optional Clinical Support Hub" },
  { key: "skills", label: "Skills Refresh" },
  { key: "confidence", label: "Confidence Checks" },
  { key: "documentation", label: "Documentation Support" },
  { key: "help", label: "Help/Contact" },
];

export const gateAuditEvidence = [
  "Learner profile",
  "Acknowledgements",
  "Theory completion",
  "Active-time report",
  "Interaction records",
  "Final exam",
  "Affidavit",
  "Certificate issue status",
  "Optional clinical support separately labeled",
];

export const stakeholderDemoScript =
  "This screen shows how the MVP protects certificate integrity. A learner can complete optional support or skip it entirely, but the certificate depends only on required online CE gates. This gives leadership and compliance reviewers a clear reason for every certificate decision.";

export function evaluateGateScenario(scenarioToEvaluate: GateScenario) {
  const blockers = gateDefinitions.filter((gate) => !scenarioToEvaluate.gates[gate.key]);
  return {
    available: blockers.length === 0,
    blockers,
  };
}
