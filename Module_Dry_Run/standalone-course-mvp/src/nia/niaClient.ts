// Nia client orchestrator. Single entry point used by the UI:
//   guardrails (pre) → intent classify → retrieve → provider → guardrails (post).
// Always returns a valid NiaStructuredResponse; never throws.

import type { NiaContextSnapshot, NiaHealthStatus, NiaProviderRequest, NiaQueryRequest, NiaStructuredResponse } from "./types";
import { screenInput, screenOutput } from "./niaGuardrails";
import { classifyNiaIntent, retrieve } from "./niaRetrieval";
import { getNiaIndex } from "./niaIndex";
import { deterministicNiaProvider } from "./providers/deterministicNiaProvider";
import { externalNiaProvider, isExternalNiaEnabled } from "./providers/externalNiaProvider";

export async function askNia(
  request: NiaQueryRequest,
  context: NiaContextSnapshot,
): Promise<NiaStructuredResponse> {
  const startedAt = performance.now();
  const guardrail = screenInput(request.input);
  const intent = classifyNiaIntent(request.input);
  const records = guardrail.blocked ? [] : retrieve(request.input, { intent, context, limit: 4 });

  const providerRequest: NiaProviderRequest = {
    request,
    intent,
    records,
    context,
    guardrail,
    startedAt,
  };

  const provider = isExternalNiaEnabled() ? externalNiaProvider : deterministicNiaProvider;

  try {
    const raw = await provider.generate(providerRequest);
    return screenOutput(raw);
  } catch {
    // Last-resort fallback: deterministic provider must still answer.
    try {
      const raw = await deterministicNiaProvider.generate(providerRequest);
      return screenOutput(raw);
    } catch {
      return {
        id: `nia-error-${Date.now()}`,
        intent: "general_course_question",
        directAnswer: "Something went wrong on my side. Please try rephrasing your question.",
        learnerSummary:
          "I can help with course navigation, module summaries, the certificate gate, study readiness, CNA scope, and the no-PHI rules.",
        nextSteps: ["Try asking again in a moment.", "Ask about a specific module or the certificate gate."],
        safetyNotes: [],
        confidence: "low",
        citations: [],
        linkedReferences: [],
        availableActions: [],
        noAnswerFound: true,
        noAnswerReason: "Provider error.",
        meta: {
          elapsedMs: Math.max(0, Math.round(performance.now() - startedAt)),
          provider: "deterministic",
          retrievedReferenceIds: [],
        },
      };
    }
  }
}

export function niaHealth(): NiaHealthStatus {
  const index = getNiaIndex();
  const externalEnabled = isExternalNiaEnabled();
  return {
    ok: index.length > 0,
    provider: externalEnabled ? "external" : "deterministic",
    externalEnabled,
    indexRecordCount: index.length,
    builtAt: new Date().toISOString(),
    notes: [
      externalEnabled
        ? "External provider toggle is ON; calls /api/nia/query with deterministic fallback."
        : "External provider disabled; deterministic course-grounded mode active.",
    ],
  };
}
