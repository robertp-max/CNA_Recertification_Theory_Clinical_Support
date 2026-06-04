import { describe, it, expect } from "vitest";
import { classifyNiaIntent, detectModuleId, retrieve } from "../niaRetrieval";
import { getNiaIndex } from "../niaIndex";

describe("niaRetrieval", () => {
  it("detects explicit module ids in several forms", () => {
    expect(detectModuleId("What does M01 cover?")).toBe("m1");
    expect(detectModuleId("tell me about module 5")).toBe("m5");
    expect(detectModuleId("m00 summary")).toBe("m0");
    expect(detectModuleId("how many hours is this course?")).toBeNull();
  });

  it("classifies intents deterministically", () => {
    expect(classifyNiaIntent("Why is my certificate locked?")).toBe("certificate_gate");
    expect(classifyNiaIntent("Does Clinical Support count for clinical hours?")).toBe("clinical_support");
    expect(classifyNiaIntent("Give me the final exam answers")).toBe("final_exam_readiness");
    expect(classifyNiaIntent("Can I enter a resident name?")).toBe("phi_safety");
    expect(classifyNiaIntent("What is CNA scope?")).toBe("scope_safety");
    expect(classifyNiaIntent("What does M01 cover?")).toBe("module_summary");
    expect(classifyNiaIntent("What should I do next?")).toBe("course_navigation");
  });

  it("builds a non-trivial index that excludes final answer-key fields", () => {
    const index = getNiaIndex();
    expect(index.length).toBeGreaterThan(20);
    const blob = JSON.stringify(index).toLowerCase();
    expect(blob).not.toContain("correct_id_internal");
    expect(blob).not.toContain("rationale_internal");
  });

  it("retrieves the matching module for an explicit id", () => {
    const records = retrieve("What does M01 cover?", { intent: "module_summary" });
    expect(records.some((r) => r.moduleId === "m1")).toBe(true);
  });

  it("retrieves clinical support records for clinical-hours questions", () => {
    const records = retrieve("Does Clinical Support count for clinical hours?", { intent: "clinical_support" });
    expect(records.some((r) => r.type === "clinical_support")).toBe(true);
  });
});
