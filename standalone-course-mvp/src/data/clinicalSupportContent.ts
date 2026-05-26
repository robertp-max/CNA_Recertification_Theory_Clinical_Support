export type ClinicalSupportSection = {
  title: string;
  sourcePath: string;
  status: string;
  description: string;
  bullets: string[];
  phiWarning?: boolean;
  reviewFlags?: string[];
};

const sourcePath = "CNA-Recert-Course/Content/clinical-support/32_CLINICAL_SUPPORT_FULL_CONTENT.md";

export const clinicalSupportSections: ClinicalSupportSection[] = [
  {
    title: "Start Here: What This Is / What This Is Not",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description:
      "Optional support for confidence, practice planning, and documentation support. It is separate from the online CE certificate gates.",
    bullets: [
      "Not required for the online CE certificate preview.",
      "Not counted as California CNA renewal clinical-hour credit.",
      "Not used to inflate required online CE progress.",
      "Not a substitute for employer policy, licensed supervision, or approval decisions.",
    ],
  },
  {
    title: "Skills Refresh Library",
    sourcePath,
    status: "Seeded from extracted optional clinical support content; skin-integrity references retain SME review flag.",
    description: "Topic library for optional skills review and confidence support.",
    bullets: [
      "PPE and infection-control refresh.",
      "Body mechanics, transfers, ambulation, and fall prevention.",
      "Nutrition, hydration, feeding assistance, and aspiration reminders.",
      "Skin integrity and pressure-injury awareness with SME/source review flag.",
      "Vital signs, observation, documentation, and dementia communication.",
    ],
    reviewFlags: ["Skin integrity references require SME/source review before production use."],
  },
  {
    title: "Practice Planner",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Learner planning area for optional practice support using fictional or non-resident examples only.",
    bullets: [
      "Choose workplace support, lab support if offered, preceptor support if available, or self-review.",
      "Identify confidence goals without entering resident details.",
      "Keep required online CE progress separate from optional support activity.",
    ],
    phiWarning: true,
  },
  {
    title: "Scheduling Guidance",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Guidance for optional support windows and contact steps.",
    bullets: [
      "Use scheduling support only if optional support is offered.",
      "Scheduling is not a certificate gate.",
      "Future Moodle/Scheduler validation remains pending.",
    ],
  },
  {
    title: "What to Bring / What to Expect",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Preparation reminders for optional support sessions.",
    bullets: [
      "Bring items requested by the site or instructor.",
      "Follow local site policy, dress, and safety requirements.",
      "Do not bring patient records, chart screenshots, medication records, or resident identifiers.",
    ],
    phiWarning: true,
  },
  {
    title: "Optional Confidence Checks",
    sourcePath: "CNA-Recert-Course/Content/clinical-support/confidence-checks/33_OPTIONAL_CLINICAL_CONFIDENCE_CHECKS_COMPLETE.md",
    status: "Seeded from extracted confidence-check package.",
    description: "Ungraded support checks for confidence only.",
    bullets: [
      "Checks are optional and non-gating.",
      "Skipping checks does not block the online CE certificate preview.",
      "Skin-integrity checks 06/07 retain SME/source review flags from the package.",
    ],
    reviewFlags: ["Optional confidence checks 06/07 require SME/source review for skin integrity."],
  },
  {
    title: "Documentation Support",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Non-PHI documentation support area with warning, attestation, mock upload, and resubmission support.",
    bullets: [
      "Use fictional or de-identified practice examples only.",
      "Do not enter resident names, faces, chart identifiers, dates of birth, addresses, medication records, or screenshots.",
      "Documentation support does not change certificate-gate status.",
    ],
    phiWarning: true,
  },
  {
    title: "RN/Preceptor Signoff Instructions",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Optional signoff support for practice documentation only.",
    bullets: [
      "Possible fields: learner name, date, setting type, RN/preceptor name, title/role, site, contact, signature, and non-PHI attestation.",
      "Signoff support is not required for online CE certificate preview.",
      "Signoff support must not be described as renewal clinical-hour credit.",
    ],
    phiWarning: true,
  },
  {
    title: "What Not to Upload: PHI Warning",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Explicit PHI warning before any mock upload, documentation support, or free-text practice area.",
    bullets: [
      "No patient/resident names or faces.",
      "No medical record numbers, chart screenshots, medication records, dates of birth, addresses, or identifying details.",
      "Use fictional practice notes only.",
    ],
    phiWarning: true,
  },
  {
    title: "Help / Office Hours / Contact",
    sourcePath,
    status: "Seeded from extracted optional clinical support content.",
    description: "Support contact and office-hours placeholder.",
    bullets: [
      "Asking for help does not lower a score.",
      "Office-hours participation is optional.",
      "Help requests do not affect certificate gates.",
    ],
  },
];
