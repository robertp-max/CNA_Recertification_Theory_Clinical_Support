import { moduleContents } from "./moduleContent";

export const modules = [
  ...moduleContents.map((module) => ({
    id: module.id,
    title: module.title,
    time: module.time,
    summary: module.summary,
    required: module.required,
    status: module.status,
    placeholder: module.placeholder,
  })),
  {
    id: "final",
    title: "Final Review / Exam / Affidavit / Certificate Status",
    time: "0.5 hr",
    summary:
      "Required certificate-gate section with locked final exam/test preview, remediation behavior, draft final signed statement, and certificate gate status.",
    required: true,
    status: "Required certificate gates",
    placeholder: false,
  },
];
