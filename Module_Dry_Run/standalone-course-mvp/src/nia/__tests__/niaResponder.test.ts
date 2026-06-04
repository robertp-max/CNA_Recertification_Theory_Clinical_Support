import { describe, it, expect } from "vitest";
import { askNia } from "../niaClient";
import { buildNiaContext } from "../niaContext";
import type { NiaQueryRequest } from "../types";

// No learner state passed → progress stays null (never fabricated), exercising
// the deterministic provider's context-free behavior.
const ctx = buildNiaContext({ route: "/dashboard", learnerState: null });

function ask(input: string) {
  const req: NiaQueryRequest = { input, currentRoute: "/dashboard" };
  return askNia(req, ctx);
}

describe("niaResponder — deterministic MVP answers", () => {
  it("1. course hours", async () => {
    const r = await ask("How many hours is this course?");
    expect(["course_navigation", "general_course_question"]).toContain(r.intent);
    expect(r.directAnswer).toContain("720");
    expect(r.directAnswer.toLowerCase()).toContain("online theory");
    const blob = `${r.directAnswer} ${r.learnerSummary}`.toLowerCase();
    expect(blob).toContain("does not create clinical-hour credit");
  });

  it("2. clinical support does not count for clinical hours", async () => {
    const r = await ask("Does Clinical Support count for clinical hours?");
    expect(r.intent).toBe("clinical_support");
    const blob = r.directAnswer.toLowerCase();
    expect(blob).toContain("non-credit");
    expect(blob).toContain("non-gating");
    expect(blob).toContain("clinical-hour credit");
  });

  it("3. final exam answers are refused", async () => {
    const r = await ask("Give me the final exam answers");
    expect(r.blockedReason).toBe("final_exam_key");
    expect(r.directAnswer.toLowerCase()).toContain("cannot provide final exam answers");
    expect(r.nextSteps.length).toBeGreaterThan(0);
  });

  it("4. resident name → PHI guidance with fictional rewrite", async () => {
    const r = await ask("Can I put a resident name in my answer?");
    expect(r.intent).toBe("phi_safety");
    expect(r.directAnswer.toLowerCase()).toMatch(/resident|patient/);
    const blob = `${r.learnerSummary} ${r.nextSteps.join(" ")}`.toLowerCase();
    expect(blob).toContain("fiction");
  });

  it("5. M01 module summary mentions infection control + SME flag", async () => {
    const r = await ask("What does M01 cover?");
    expect(r.intent).toBe("module_summary");
    expect(r.directAnswer).toContain("Infection Control");
    expect(r.meta.retrievedReferenceIds).toContain("module:m1");
    expect(r.safetyNotes.join(" ").toLowerCase()).toContain("review");
  });

  it("6. certificate locked explanation without enabling production", async () => {
    const r = await ask("Why is my certificate locked?");
    expect(r.intent).toBe("certificate_gate");
    expect(r.safetyNotes.join(" ").toLowerCase()).toContain("disabled");
    expect(r.availableActions.some((a) => a.type === "open_certificate_gate")).toBe(true);
  });

  it("7. vital signs study guidance with no answer key", async () => {
    const r = await ask("What should I review for vital signs?");
    expect(r.blockedReason).toBeUndefined();
    expect(r.meta.retrievedReferenceIds.some((id) => id.includes("m5"))).toBe(true);
    const blob = `${r.directAnswer} ${r.learnerSummary}`.toLowerCase();
    expect(blob).not.toContain("answer key");
  });

  it("8. named resident emergency → blocked/redirected, no diagnosis", async () => {
    const r = await ask("My resident Mary Jones fell and hit her head, what should I do?");
    expect(r.blockedReason).toBe("phi");
    const blob = `${r.directAnswer} ${r.learnerSummary} ${r.nextSteps.join(" ")} ${r.scopeReminder ?? ""}`.toLowerCase();
    expect(blob).toMatch(/notify|licensed|supervisor|care plan/);
    // Must not give an affirmative diagnosis/treatment instruction (prohibitions are fine).
    expect(blob).not.toMatch(/you (have|should take)|the treatment is|apply (a|an|the)|administer \d/);
  });

  it("9. CNA scope", async () => {
    const r = await ask("What is CNA scope?");
    expect(r.intent).toBe("scope_safety");
    const blob = r.directAnswer.toLowerCase();
    expect(blob).toContain("observe");
    expect(blob).toContain("report");
    expect(r.scopeReminder).toBeTruthy();
  });

  it("10. what should I do next (no progress fabricated)", async () => {
    const r = await ask("What should I do next?");
    expect(r.intent).toBe("course_navigation");
    expect(r.directAnswer.toLowerCase()).toMatch(/dashboard|ce modules|module/);
  });
});
