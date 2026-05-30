import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ArrowLeft, Check, Clock } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { withLessonCompleted } from "../lib/v2state";
import { paths } from "../app/routes";
import { getGeneratedLesson } from "../data/contentV2Adapter";
import { buildLessonRemediation, type RemediationChallenge } from "../data/remediation";
import { MediaSlot } from "../components/v2/primitives";
import { NarrationPlayer } from "../components/v2/NarrationPlayer";
import { ChallengeDebrief } from "../components/v2/ChallengeDebrief";

function cardLabel(cardId: string) {
  return cardId.replace(/_/g, " ").replace(/^C0?/, "Card ");
}

export function LessonPlayerPage() {
  const navigate = useNavigate();
  const { setState } = useLearner();
  const { demoSeconds } = useUiState();
  const lesson = getGeneratedLesson("M01", "L01");
  const cards = useMemo(() => lesson?.cards ?? [], [lesson]);

  const [currentIdx, setCurrentIdx] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [openedOptions, setOpenedOptions] = useState<string[]>([]);

  const challengeCard = useMemo(() => cards.find((card) => card.internal_challenge), [cards]);
  const challenge = (challengeCard?.internal_challenge ?? null) as RemediationChallenge | null;
  const remediation = useMemo(() => (challenge ? buildLessonRemediation(challenge) : null), [challenge]);

  if (!lesson || cards.length === 0) {
    return (
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 text-stone-300">
        ContentV2 lesson data is unavailable for Module 1 Lesson 1.
      </div>
    );
  }

  const currentCard = cards[currentIdx];
  const isChallengeCard = Boolean(currentCard.internal_challenge);
  const isDebriefCard = currentCard.card_type === "debrief";
  const isLast = currentIdx === cards.length - 1;

  // Read-before-continue: on the debrief, the learner must open the safest
  // response and their own choice (at minimum the safest response).
  const requiredReads = remediation
    ? Array.from(new Set([remediation.safestId, selectedAnswer].filter(Boolean) as string[]))
    : [];
  const debriefReadDone = requiredReads.every((id) => openedOptions.includes(id));

  const canContinue = isChallengeCard ? submitted : isDebriefCard ? debriefReadDone : true;

  const handleNext = () => {
    if (currentIdx < cards.length - 1) {
      setCurrentIdx((idx) => idx + 1);
      return;
    }
    setState((s) => withLessonCompleted(s));
    navigate(paths.module1);
  };

  const challengeChoices = (challenge?.choices ?? []) as { id: string; label: string }[];

  return (
    <div className="space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-stone-800/60">
        <button onClick={() => navigate(paths.module1)} className="text-stone-400 hover:text-stone-100 inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider self-start">
          <ArrowLeft size={14} /> Close Lesson Player
        </button>
        <div className="flex items-center gap-4 text-xs font-mono text-stone-400">
          <span className="flex items-center gap-1"><Clock size={12} className="text-amber-500" /> Lesson Session: {lesson.estimated_minutes}m</span>
          <span>•</span>
          <span className="text-amber-500 flex items-center gap-1">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-500" /> Active time (demo): {formatHoursAndMins(demoSeconds)}
          </span>
        </div>
      </div>

      <div className="flex items-center justify-between bg-stone-950/60 p-3 rounded-lg border border-stone-900 overflow-x-auto">
        {cards.map((card, idx) => (
          <div key={card.app.location} className="flex items-center gap-3 shrink-0 mx-2">
            <div className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] font-mono font-bold ${
              currentIdx === idx ? "bg-amber-500 border-amber-500 text-black" : currentIdx > idx ? "bg-amber-950/40 text-amber-400 border-amber-500/30" : "bg-transparent border-stone-800 text-stone-600"
            }`}>
              {currentIdx > idx ? <Check size={10} /> : idx + 1}
            </div>
            <span className={`text-[11px] font-semibold uppercase tracking-wider ${currentIdx === idx ? "text-amber-500" : "text-stone-500"}`}>
              {cardLabel(card.card_id)}
            </span>
            {idx < cards.length - 1 && <div className="w-6 h-px bg-stone-900" />}
          </div>
        ))}
      </div>

      <div className="bg-[#120909] border border-stone-800/80 rounded-xl overflow-hidden shadow-2xl flex flex-col min-h-[500px]">
        <div className="p-6 md:p-8 flex-1 space-y-6">
          <div>
            <span className="text-[10px] font-bold text-stone-500 uppercase tracking-widest font-mono">
              {currentCard.module_id} - {currentCard.lesson_id} - {cardLabel(currentCard.card_id)}
            </span>
            <h2 className="text-2xl font-normal text-stone-100 tracking-tight mt-1">{currentCard.display_title}</h2>
            <p className="text-[11px] text-stone-500 font-mono mt-1">{currentCard.app.location}</p>
          </div>

          <MediaSlot appLocation={currentCard.app.location} sceneTitle={currentCard.media_prompt_placeholder.scene_title} />

          {currentCard.card_type === "overview" && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider">Learning Goal</h4>
                <p className="text-xs text-stone-400 leading-relaxed">{currentCard.learning_goal}</p>
              </div>
              <div className="space-y-2">
                <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider">Why It Matters</h4>
                <ul className="space-y-1.5 text-xs text-stone-400 leading-relaxed">
                  {currentCard.why_it_matters.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </div>
            </div>
          )}

          {currentCard.card_type === "delivery" && (
            <div className="space-y-4">
              <div className="space-y-2">
                <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider">Lesson Content</h4>
                <p className="text-xs text-stone-400 leading-relaxed whitespace-pre-line">{currentCard.learner_facing_content}</p>
              </div>
              <div className="p-3 bg-[#1c0d0d] border border-[#5c1111]/30 rounded">
                <p className="text-[11px] text-stone-300 leading-relaxed">
                  <strong>CNA practice example:</strong> {currentCard.cna_practice_example}
                </p>
              </div>
            </div>
          )}

          {isChallengeCard && challenge && (
            <div className="space-y-4">
              <p className="text-xs text-stone-300 leading-relaxed font-semibold">{challenge.prompt}</p>
              <div className="grid grid-cols-1 gap-2.5">
                {challengeChoices.map((ans) => (
                  <button
                    key={ans.id}
                    onClick={() => !submitted && setSelectedAnswer(ans.id)}
                    disabled={submitted}
                    className={`w-full text-left p-4 rounded border text-xs flex items-start gap-3 transition-colors ${
                      selectedAnswer === ans.id ? "bg-[#1c0d0d] border-amber-500/50 text-stone-100" : "bg-[#080404] border-stone-900 hover:border-stone-800 text-stone-400"
                    }`}
                  >
                    <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${selectedAnswer === ans.id ? "bg-amber-500 text-black border-amber-500" : "border-stone-600 text-stone-500"}`}>{ans.id}</div>
                    <span>{ans.label}</span>
                  </button>
                ))}
              </div>
              {!submitted && (
                <button
                  onClick={() => setSubmitted(true)}
                  disabled={!selectedAnswer}
                  className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
                >
                  Submit Response
                </button>
              )}
              {submitted && (
                <p className="text-[11px] text-amber-500/80 font-mono">Your response has been submitted. Continue to the Challenge Debrief.</p>
              )}
            </div>
          )}

          {isDebriefCard && remediation && (
            <>
              <ChallengeDebrief
                remediation={remediation}
                selectedId={selectedAnswer}
                openedIds={openedOptions}
                onOpen={(id) => setOpenedOptions((cur) => (cur.includes(id) ? cur : [...cur, id]))}
              />
              {!debriefReadDone && (
                <p className="text-[11px] text-stone-500 font-mono">
                  Review the safest response{selectedAnswer && selectedAnswer !== remediation.safestId ? " and your own choice" : ""} in the option review to unlock lesson completion.
                </p>
              )}
            </>
          )}

          {!isDebriefCard && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
              {currentCard.key_terms.slice(0, 3).map((term) => (
                <div key={term.term} className="bg-[#080404] border border-stone-900 rounded p-3">
                  <h4 className="text-[10px] uppercase font-bold text-amber-500 font-mono">{term.term}</h4>
                  <p className="text-[11px] text-stone-500 leading-relaxed mt-1">{term.definition}</p>
                </div>
              ))}
            </div>
          )}
        </div>

        <NarrationPlayer
          appLocation={currentCard.app.location}
          transcript={isDebriefCard && remediation ? remediation.transcript : currentCard.transcript_text}
          label={isDebriefCard ? "Challenge Debrief Narration" : "Lesson Narration"}
          estSeconds={currentCard.estimated_narration_seconds}
        />

        <div className="px-6 py-4 bg-stone-950 border-t border-stone-850 flex items-center justify-between">
          <button onClick={() => setCurrentIdx((idx) => Math.max(0, idx - 1))} disabled={currentIdx === 0} className="px-4 py-2 text-xs font-semibold text-stone-500 hover:text-stone-300 disabled:opacity-35 disabled:cursor-not-allowed uppercase tracking-wider">
            &larr; Previous Card
          </button>
          <button onClick={handleNext} disabled={!canContinue} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed">
            {isLast ? "Complete Theory Lesson" : isDebriefCard ? remediation?.continueLabel ?? "Continue" : "Continue"} &rarr;
          </button>
        </div>
      </div>
    </div>
  );
}
