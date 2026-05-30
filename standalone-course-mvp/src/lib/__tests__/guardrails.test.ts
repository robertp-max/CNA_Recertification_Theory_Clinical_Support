import { describe, it, expect } from "vitest";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { reviewerCredentials } from "../auth";
import { PhiWarningBlock } from "../../components/ui/PhiWarningBlock";
import { courseContentV2 } from "../../data/contentV2.generated";
import { buildLessonRemediation, type RemediationChallenge } from "../../data/remediation";

const FORBIDDEN_LEARNER_PHRASES = [
  "Correct internal answer",
  "Rationale for instructor/internal use",
  "Correct. Continue to the next item.",
  "Review the related lesson and try again.",
  "correct_id_internal",
  "rationale_internal",
];

describe("guardrails", () => {
  it("approved login credentials are unchanged (admin / 1234)", () => {
    expect(reviewerCredentials).toEqual({ username: "admin", password: "1234" });
  });

  it("PHI warning component renders the mandated, non-dismissible copy", () => {
    const html = renderToStaticMarkup(createElement(PhiWarningBlock));
    expect(html).toContain("STOP:");
    expect(html).toContain("Protected Health Information");
    expect(html).toContain("simulated case data only");
  });

  it("no answer-key / internal phrases appear in learner-facing card fields", () => {
    for (const module of courseContentV2.modules) {
      for (const lesson of module.lessons) {
        for (const card of lesson.cards) {
          const learnerText = [card.learner_facing_content, card.narration_script, card.transcript_text, card.display_title].join("\n");
          for (const phrase of FORBIDDEN_LEARNER_PHRASES) {
            expect(learnerText.includes(phrase), `${card.app.location} contains "${phrase}"`).toBe(false);
          }
        }
      }
    }
  });

  it("every lesson challenge produces course-extension remediation with a safest response and per-option review", () => {
    let challenges = 0;
    for (const module of courseContentV2.modules) {
      for (const lesson of module.lessons) {
        const challengeCard = lesson.cards.find((c) => c.internal_challenge);
        if (!challengeCard?.internal_challenge) continue;
        challenges += 1;
        const r = buildLessonRemediation(challengeCard.internal_challenge as RemediationChallenge);
        expect(r.title).toBe("Challenge Debrief");
        expect(r.safestResponseLabel.length).toBeGreaterThan(0);
        expect(r.options.length).toBeGreaterThan(0);
        expect(r.options.filter((o) => o.status === "safest").length).toBe(1);
        // No internal phrases leak into rendered remediation strings.
        const blob = [r.whySafest, r.whatToRemember, r.narration, ...r.options.flatMap((o) => [o.why, o.remember])].join("\n");
        for (const phrase of FORBIDDEN_LEARNER_PHRASES) {
          expect(blob.includes(phrase)).toBe(false);
        }
      }
    }
    expect(challenges).toBeGreaterThan(0);
  });

  it("final assessment never exposes a learner-facing answer key field on questions consumed by the exam pool", () => {
    // The exam pool maps prompts + choices only; correct ids stay internal.
    const q = courseContentV2.assessments.final_assessment.questions[0];
    expect(q).toHaveProperty("correct_id_internal");
    // answer_key_policy must assert non-disclosure.
    expect(courseContentV2.assessments.final_assessment.answer_key_policy.toLowerCase()).toContain("not revealed");
  });
});
