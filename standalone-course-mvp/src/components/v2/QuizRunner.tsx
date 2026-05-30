import { useState } from "react";

export type QuizChoice = { id: string; label: string };
export type QuizQuestion = { id: string; prompt: string; choices: QuizChoice[] };

// One-question-at-a-time runner. No right/wrong feedback while answering and no
// answer key is ever revealed (compliance: final exams must not expose keys).
// "Next" is locked until the current question is answered; "Submit" is locked
// until every question has a selection.
export function QuizRunner({
  questions,
  label,
  onSubmit,
}: {
  questions: QuizQuestion[];
  label: string;
  onSubmit: (answers: Record<string, string>) => void;
}) {
  const [currentIdx, setCurrentIdx] = useState(0);
  const [answers, setAnswers] = useState<Record<string, string>>({});

  const q = questions[currentIdx];
  const allAnswered = questions.every((item) => answers[item.id]);
  const isLast = currentIdx === questions.length - 1;

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex justify-between items-center pb-3 border-b border-stone-800/60 font-mono text-xs text-stone-400">
        <span>Question {currentIdx + 1} of {questions.length}</span>
        <span>{label}</span>
      </div>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 md:p-8 shadow-xl space-y-6">
        <div>
          <span className="text-[10px] font-bold text-amber-500 uppercase tracking-widest font-mono">Select One Response</span>
          <h2 className="text-base font-semibold text-stone-200 mt-1 leading-relaxed">{q.prompt}</h2>
        </div>

        <div className="grid grid-cols-1 gap-2.5">
          {q.choices.map((opt) => {
            const selected = answers[q.id] === opt.id;
            return (
              <button
                key={opt.id}
                onClick={() => setAnswers((a) => ({ ...a, [q.id]: opt.id }))}
                className={`w-full text-left p-4 rounded border text-xs flex items-start gap-3 transition-colors ${
                  selected ? "bg-[#1c0d0d] border-amber-500/50 text-stone-100" : "bg-[#080404] border-stone-900 hover:border-stone-800 text-stone-400"
                }`}
              >
                <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${selected ? "bg-amber-500 text-black border-amber-500" : "border-stone-600 text-stone-500"}`}>{opt.id}</div>
                <span>{opt.label}</span>
              </button>
            );
          })}
        </div>

        <div className="bg-stone-950 p-3 rounded border border-stone-900/60 text-[10px] text-stone-500 font-mono">
          Compliance guardrail: responses are recorded silently. No correct-answer key is shown during or after the exam.
        </div>

        <div className="pt-4 border-t border-stone-850 flex justify-between">
          <button
            onClick={() => setCurrentIdx((i) => Math.max(0, i - 1))}
            disabled={currentIdx === 0}
            className="px-4 py-2 text-xs font-semibold text-stone-500 hover:text-stone-300 disabled:opacity-35 uppercase tracking-wider"
          >
            Back
          </button>

          {!isLast ? (
            <button
              onClick={() => setCurrentIdx((i) => Math.min(questions.length - 1, i + 1))}
              disabled={!answers[q.id]}
              className="bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-200 font-bold px-5 py-2 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40"
            >
              Next
            </button>
          ) : (
            <button
              onClick={() => onSubmit(answers)}
              disabled={!allAnswered}
              className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40"
            >
              Submit Exam
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
