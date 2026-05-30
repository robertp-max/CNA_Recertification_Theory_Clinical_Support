// Route path constants + primary navigation config (V2 design — four entries).
export const paths = {
  dashboard: "/dashboard",
  modules: "/modules",
  module0: "/modules/m0",
  module1: "/modules/m1",
  lesson: "/modules/m1/lesson",
  moduleAssessment: "/modules/m1/assessment",
  moduleAssessmentQuiz: "/modules/m1/assessment/quiz",
  finalSplash: "/final",
  finalQuiz: "/final/quiz",
  finalResult: "/final/result",
  certificate: "/certificate",
  clinicalHub: "/clinical-hub",
};

export type NavItem = {
  to: string;
  label: string;
  matchPrefixes?: string[];
};

// Global top-nav — mirrors the V2 prototype header.
export const primaryNav: NavItem[] = [
  { to: paths.dashboard, label: "Dashboard" },
  { to: paths.modules, label: "CE Modules", matchPrefixes: ["/modules", "/final"] },
  { to: paths.certificate, label: "Certificate Gate" },
  { to: paths.clinicalHub, label: "Clinical Hub" },
];
