import { describe, it, expect } from "vitest";
import { drawAttempt, scoreAttempt, examPool, EXAM } from "../examPool";

describe("final exam preview engine", () => {
  it("draws an attempt no larger than the configured size, from the pool", () => {
    const attempt = drawAttempt();
    expect(attempt.length).toBeLessThanOrEqual(EXAM.ATTEMPT_SIZE);
    expect(attempt.length).toBeGreaterThan(0);
    attempt.forEach((it) => expect(examPool.some((p) => p.id === it.id)).toBe(true));
  });

  it("scores all-correct as a pass at/above the threshold", () => {
    const attempt = drawAttempt();
    const answers = Object.fromEntries(attempt.map((it) => [it.id, it.correctId]));
    const r = scoreAttempt(attempt, answers);
    expect(r.pct).toBe(100);
    expect(r.passed).toBe(true);
  });

  it("scores all-wrong as a fail below the threshold", () => {
    const attempt = drawAttempt();
    const answers = Object.fromEntries(
      attempt.map((it) => [it.id, it.choices.find((c) => c.id !== it.correctId)?.id ?? "x"]),
    );
    const r = scoreAttempt(attempt, answers);
    expect(r.passed).toBe(false);
    expect(r.pct).toBeLessThan(EXAM.PASS_PCT);
  });
});
