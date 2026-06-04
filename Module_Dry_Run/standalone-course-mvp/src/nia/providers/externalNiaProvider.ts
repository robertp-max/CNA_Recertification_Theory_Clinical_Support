// External Nia provider — SCAFFOLD.
//
// Phase 1 keeps this disabled by default. The deterministic provider is the
// permanent safe fallback; this provider only activates when the public toggle
// VITE_NIA_ENABLED === "true" AND a server route (/api/nia/query) is present.
//
// SECURITY MODEL (do not violate):
//   - The browser NEVER sees the model API key. Secrets live only on the server
//     route, read from NON-VITE env: NIA_LLM_PROVIDER / NIA_LLM_BASE_URL /
//     NIA_LLM_API_KEY / NIA_LLM_MODEL / NIA_LLM_TIMEOUT_MS.
//   - The browser sends only: input, intent, top retrieved records, context.
//   - The server must NOT receive final answer keys, correct_id_internal,
//     rationale_internal, raw PHI, or the entire course JSON.
//   - Any failure (disabled, network, timeout, invalid JSON) falls back to the
//     deterministic provider so Nia never crashes.
//
// LATER CLAUDE SWAP: implement /api/nia/query server-side, set NIA_LLM_PROVIDER
// (e.g. "anthropic"), and add an AnthropicNiaProvider behind this same
// NiaProvider interface. The UI and response contract do not change.

import type { NiaProvider, NiaProviderRequest, NiaStructuredResponse } from "../types";
import { deterministicNiaProvider } from "./deterministicNiaProvider";

const EXTERNAL_ENDPOINT = "/api/nia/query";

export function isExternalNiaEnabled(): boolean {
  // Public, non-secret feature toggle only. NEVER read a secret key here.
  return import.meta.env?.VITE_NIA_ENABLED === "true";
}

function timeoutMs(): number {
  const raw = import.meta.env?.VITE_NIA_TIMEOUT_MS;
  const parsed = raw ? Number(raw) : NaN;
  return Number.isFinite(parsed) && parsed > 0 ? parsed : 12000;
}

// Minimal runtime validation (no extra dependency). If zod is later added to the
// repo, replace this with a zod schema parse.
function isValidNiaResponse(value: unknown): value is NiaStructuredResponse {
  if (!value || typeof value !== "object") return false;
  const r = value as Record<string, unknown>;
  return (
    typeof r.id === "string" &&
    typeof r.intent === "string" &&
    typeof r.directAnswer === "string" &&
    typeof r.learnerSummary === "string" &&
    Array.isArray(r.nextSteps) &&
    Array.isArray(r.safetyNotes) &&
    Array.isArray(r.citations) &&
    Array.isArray(r.linkedReferences) &&
    Array.isArray(r.availableActions) &&
    typeof r.noAnswerFound === "boolean" &&
    typeof r.meta === "object" &&
    r.meta !== null
  );
}

// Only the safe subset of records is sent over the wire.
function safeRecordPayload(req: NiaProviderRequest) {
  return req.records.map((rec) => ({
    id: rec.id,
    type: rec.type,
    title: rec.title,
    body: rec.body,
    appLocation: rec.appLocation,
    moduleId: rec.moduleId,
    lessonId: rec.lessonId,
    cardId: rec.cardId,
    status: rec.status,
    safetyFlags: rec.safetyFlags,
  }));
}

export class ExternalNiaProvider implements NiaProvider {
  readonly providerId = "external" as const;

  async generate(req: NiaProviderRequest): Promise<NiaStructuredResponse> {
    if (!isExternalNiaEnabled()) {
      return deterministicNiaProvider.generate(req);
    }

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs());

    try {
      const res = await fetch(EXTERNAL_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        signal: controller.signal,
        body: JSON.stringify({
          input: req.request.input,
          intent: req.intent,
          context: req.context,
          records: safeRecordPayload(req),
        }),
      });

      if (!res.ok) throw new Error(`Nia external route returned ${res.status}`);
      const data: unknown = await res.json();
      if (!isValidNiaResponse(data)) throw new Error("Nia external response failed validation");

      return { ...data, meta: { ...data.meta, provider: "external" } };
    } catch (err) {
      if (import.meta.env?.DEV) {
        // eslint-disable-next-line no-console
        console.warn("[Nia] external provider failed; using deterministic fallback.", err);
      }
      return deterministicNiaProvider.generate(req);
    } finally {
      clearTimeout(timer);
    }
  }
}

export const externalNiaProvider = new ExternalNiaProvider();
