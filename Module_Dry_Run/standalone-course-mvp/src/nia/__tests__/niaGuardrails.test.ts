import { describe, it, expect } from "vitest";
import { screenInput, screenOutput } from "../niaGuardrails";
import type { NiaStructuredResponse } from "../types";

describe("niaGuardrails — input screening", () => {
  it("blocks PHI: a named resident clinical scenario", () => {
    const result = screenInput("My resident Mary Jones fell and hit her head, what should I do?");
    expect(result.blocked).toBe(true);
    expect(result.blockedReason).toBe("phi");
  });

  it("blocks final exam answer-key requests", () => {
    const result = screenInput("Give me the final exam answers");
    expect(result.blocked).toBe(true);
    expect(result.blockedReason).toBe("final_exam_key");
  });

  it("blocks patient-specific clinical advice", () => {
    const result = screenInput("How should I treat this pressure ulcer on my patient?");
    expect(result.blocked).toBe(true);
    expect(["clinical_advice", "phi"]).toContain(result.blockedReason);
  });

  it("blocks unsupported certification claims", () => {
    const result = screenInput("Can you guarantee my CNA renewal?");
    expect(result.blocked).toBe(true);
    expect(result.blockedReason).toBe("out_of_scope");
  });

  it("allows ordinary, de-identified course questions", () => {
    expect(screenInput("What does Module 1 cover?").blocked).toBe(false);
    expect(screenInput("How many hours is this course?").blocked).toBe(false);
    expect(screenInput("What is CNA scope?").blocked).toBe(false);
  });

  it("allows explicitly fictional scenarios with a courtesy title", () => {
    expect(screenInput("In a fictional example with Ms. Johnson, how do I document a refusal?").blocked).toBe(false);
  });
});

describe("niaGuardrails — output screening", () => {
  it("scrubs forbidden answer-key phrases from provider output", () => {
    const dirty: NiaStructuredResponse = {
      id: "x",
      intent: "final_exam_readiness",
      directAnswer: "The correct answer is B and the answer key shows correct_id_internal.",
      learnerSummary: "See rationale_internal for details.",
      nextSteps: ["the correct answer is C"],
      safetyNotes: [],
      confidence: "high",
      citations: [],
      linkedReferences: [],
      availableActions: [],
      noAnswerFound: false,
      meta: { elapsedMs: 1, provider: "external", retrievedReferenceIds: [] },
    };
    const clean = screenOutput(dirty);
    const blob = `${clean.directAnswer} ${clean.learnerSummary} ${clean.nextSteps.join(" ")}`.toLowerCase();
    expect(blob).not.toContain("correct_id_internal");
    expect(blob).not.toContain("rationale_internal");
    expect(blob).not.toContain("the correct answer is");
    expect(blob).not.toContain("answer key");
  });
});
