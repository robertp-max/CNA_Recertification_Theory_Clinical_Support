import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useLearner } from "../lib/learnerState";
import { drawAttempt, scoreAttempt } from "../data/examPool";
import { paths } from "../app/routes";
import { QuizRunner } from "../components/v2/QuizRunner";

export function FinalAssessmentQuizPage() {
  const navigate = useNavigate();
  const { recordExamAttempt } = useLearner();
  // Draw once per mount from the real preview pool (no fixed order, no key reveal).
  const [attempt] = useState(() => drawAttempt());

  const questions = attempt.map((it) => ({
    id: it.id,
    prompt: it.prompt,
    choices: it.choices,
  }));

  return (
    <QuizRunner
      label="COURSE THEORY FINAL EXAM"
      questions={questions}
      onSubmit={(answers) => {
        const scored = scoreAttempt(attempt, answers);
        recordExamAttempt(scored.pct, scored.passed);
        navigate(paths.finalResult, { state: { pct: scored.pct, passed: scored.passed } });
      }}
    />
  );
}
