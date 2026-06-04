import { describe, it, expect } from "vitest";
import { initialLearnerState, passAllRequiredState } from "../learnerState";
import { completeAllRequiredLessons, requiredTheoryComplete, isModuleComplete } from "../moduleProgress";
import { requiredProgressPct, optionalProgressPct } from "../progress";

describe("required vs optional progress separation", () => {
  it("required progress ignores optional clinical support", () => {
    const base = completeAllRequiredLessons(passAllRequiredState(initialLearnerState));
    const withOpt = { ...base, optionalClinical: { hub: true, skills: true, confidence: true, documentation: true, help: true } };
    expect(requiredProgressPct(base)).toBe(requiredProgressPct(withOpt));
  });

  it("optional progress is tracked separately", () => {
    const s = { ...initialLearnerState, optionalClinical: { hub: true, skills: true, confidence: false, documentation: false, help: false } };
    expect(optionalProgressPct(s)).toBeGreaterThan(0);
    expect(requiredProgressPct(s)).toBe(0);
  });

  it("completing build-ready lessons + acks completes required theory", () => {
    const s = completeAllRequiredLessons({ ...initialLearnerState, onlineCapAck: true, phiAck: true, orientationFinalAck: true });
    expect(requiredTheoryComplete(s)).toBe(true);
  });

  it("Module 3 is never counted as complete (source repair)", () => {
    const s = completeAllRequiredLessons(passAllRequiredState(initialLearnerState));
    expect(isModuleComplete(s, "m3")).toBe(false);
  });
});
