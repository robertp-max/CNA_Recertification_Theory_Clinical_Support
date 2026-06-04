// Module10_Dry_Run clean shell.
// Stale authored remediation overrides were purged during cleanup.
// Future overrides must be generated only after source extraction from the approved Module 10 PDF.

export type OptionOverride = { why?: string; remember?: string };

export type RemediationOverride = {
  safetyPrinciple?: string;
  whySafest?: string;
  cnaScopeNote?: string;
  residentSafetyNote?: string;
  whatToRemember?: string;
  options?: Record<string, OptionOverride>;
  narration?: string;
  transcript?: string;
};

export const remediationOverrides: Record<string, RemediationOverride> = {};
