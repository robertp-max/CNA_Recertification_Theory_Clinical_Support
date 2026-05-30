import { describe, it, expect } from "vitest";
import { initialLearnerState, passAllRequiredState } from "../learnerState";
import { completeAllRequiredLessons } from "../moduleProgress";
import { summarizeGates, computeGates } from "../gates";

function fullyPassing() {
  return completeAllRequiredLessons(passAllRequiredState(initialLearnerState));
}

describe("unified gate model", () => {
  it("optional clinical support never changes certificate readiness", () => {
    const base = fullyPassing();
    const allOptional = { ...base, optionalClinical: { hub: true, skills: true, confidence: true, documentation: true, help: true } };
    const noOptional = { ...base, optionalClinical: { hub: false, skills: false, confidence: false, documentation: false, help: false } };
    const a = summarizeGates(allOptional);
    const b = summarizeGates(noOptional);
    expect(a.certificatePreviewReady).toBe(b.certificatePreviewReady);
    expect(a.productionIssuable).toBe(b.productionIssuable);
    expect(a.passingCount).toBe(b.passingCount);
  });

  it("certificate preview is ready when all required gates pass", () => {
    expect(summarizeGates(fullyPassing()).certificatePreviewReady).toBe(true);
  });

  it("production issuance remains false without approval metadata", () => {
    const s = fullyPassing();
    expect(s.approvalMetadataPresent).toBe(false);
    expect(summarizeGates(s).productionIssuable).toBe(false);
    const withApproval = { ...s, approvalMetadataPresent: true };
    expect(summarizeGates(withApproval).productionIssuable).toBe(true);
  });

  it("active-time gate is truth-labeled as simulated/MVP (not CDPH-validated)", () => {
    const at = computeGates(fullyPassing()).find((g) => g.key === "activeTime");
    expect(at?.simulated).toBe(true);
    expect(at?.label.toLowerCase()).toContain("not cdph-validated");
  });

  it("a fresh learner is blocked from the certificate", () => {
    expect(summarizeGates(initialLearnerState).certificatePreviewReady).toBe(false);
  });
});
