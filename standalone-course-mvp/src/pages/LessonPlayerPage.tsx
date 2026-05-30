import { useMemo, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ArrowLeft, Check, Clock, FileText, Pause, Play } from "lucide-react";
import { useLearner } from "../lib/learnerState";
import { useUiState, formatHoursAndMins } from "../lib/uiState";
import { withLessonCompleted } from "../lib/v2state";
import { paths } from "../app/routes";
import { getGeneratedLesson } from "../data/contentV2Adapter";
import { MediaPanel } from "../components/v2/primitives";

type Challenge = {
  prompt: string;
  choices: { id: string; label: string }[];
  correct_id_internal?: string;
  rationale_internal?: string;
  learner_feedback_correct?: string;
  learner_feedback_incorrect?: string;
};

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
  const [isPlaying, setIsPlaying] = useState(false);
  const [showTranscript, setShowTranscript] = useState(false);
  const [openedRationales, setOpenedRationales] = useState<string[]>([]);

  if (!lesson || cards.length === 0) {
    return (
      <div className="bg-[#120909] border border-stone-800/80 rounded-xl p-6 text-stone-300">
        ContentV2 lesson data is unavailable for Module 1 Lesson 1.
      </div>
    );
  }

  const currentCard = cards[currentIdx];
  const challenge = (currentCard.internal_challenge ?? null) as Challenge | null;
  const deliveryCards = cards.filter((card) => card.card_type === "delivery").length;
  const isChallengeCard = Boolean(challenge);
  const canContinue = !isChallengeCard || submitted;

  const handleNext = () => {
    if (currentIdx < cards.length - 1) {
      setCurrentIdx((idx) => idx + 1);
      setShowTranscript(false);
      return;
    }
    setState((s) => withLessonCompleted(s));
    navigate(paths.module1);
  };

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

          <MediaPanel
            label={`Visual Blueprint ${currentCard.card_id}`}
            caption={currentCard.media_prompt_placeholder.scene_title}
          >
            <div className="w-28 h-28 rounded-full border border-amber-500/30 bg-[#1c0d0d] flex items-center justify-center text-amber-500/70">
              <FileText size={40} />
            </div>
          </MediaPanel>

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
                <h4 className="text-xs uppercase font-bold text-stone-400 font-mono tracking-wider">
                  Delivery Segment {deliveryCards > 1 ? currentCard.card_id.split("_")[0] : ""}
                </h4>
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
                {challenge.choices.map((ans) => (
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
              {!submitted && selectedAnswer && (
                <button onClick={() => setSubmitted(true)} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors">
                  Submit Decision Pattern
                </button>
              )}
              {submitted && <p className="text-[11px] text-amber-500/80 font-mono">Decision submitted. Continue to the debrief for rationale review.</p>}
            </div>
          )}

          {currentCard.card_type === "debrief" && (
            <div className="space-y-4">
              <p className="text-xs text-stone-400 leading-relaxed whitespace-pre-line">{currentCard.learner_facing_content}</p>
              {currentCard.debrief_rationale && (
                <div className="p-4 rounded border border-stone-900 bg-stone-950/60">
                  <h4 className="text-[10px] uppercase font-bold text-stone-300 font-mono mb-2">ContentV2 Debrief Rationale</h4>
                  <p className="text-[11px] text-stone-400 leading-relaxed whitespace-pre-line">{currentCard.debrief_rationale}</p>
                </div>
              )}
              {cards.find((card) => card.internal_challenge)?.internal_challenge && (
                <div className="space-y-3">
                  {((cards.find((card) => card.internal_challenge)?.internal_challenge ?? null) as Challenge | null)?.choices.map((item) => {
                    const open = openedRationales.includes(item.id);
                    const sourceChallenge = (cards.find((card) => card.internal_challenge)?.internal_challenge ?? null) as Challenge | null;
                    const correct = item.id === sourceChallenge?.correct_id_internal;
                    return (
                      <button
                        key={item.id}
                        type="button"
                        onClick={() => setOpenedRationales((current) => (current.includes(item.id) ? current : [...current, item.id]))}
                        className={`w-full text-left p-4 rounded border text-xs transition-all ${open ? "bg-[#080404] border-[#5c1111]/60" : "bg-stone-950/40 border-stone-900/60 opacity-75 hover:opacity-100"}`}
                      >
                        <div className="flex items-center justify-between mb-2">
                          <div className="flex items-center gap-2">
                            <span className={`px-2 py-0.5 rounded text-[9px] font-mono font-bold ${correct ? "bg-amber-950/60 text-amber-300" : "bg-red-950/60 text-red-400"}`}>
                              {item.id} - {correct ? "CORRECT OPTION" : "REVIEW OPTION"}
                            </span>
                            <h4 className="font-semibold text-stone-200">{item.label}</h4>
                          </div>
                          <span className="text-[10px] text-amber-500 font-mono font-semibold">{open ? "Read" : "Click to Review"}</span>
                        </div>
                        {open && (
                          <p className="text-stone-400 leading-relaxed pl-1">
                            {correct ? sourceChallenge?.learner_feedback_correct : sourceChallenge?.learner_feedback_incorrect}
                          </p>
                        )}
                      </button>
                    );
                  })}
                </div>
              )}
            </div>
          )}

          <div className="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
            {currentCard.key_terms.slice(0, 3).map((term) => (
              <div key={term.term} className="bg-[#080404] border border-stone-900 rounded p-3">
                <h4 className="text-[10px] uppercase font-bold text-amber-500 font-mono">{term.term}</h4>
                <p className="text-[11px] text-stone-500 leading-relaxed mt-1">{term.definition}</p>
              </div>
            ))}
          </div>
        </div>

        <div className="px-6 py-4 bg-[#0a0505] border-t border-stone-850 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <button onClick={() => setIsPlaying((p) => !p)} className="w-10 h-10 rounded-full bg-[#1c0d0d] border border-[#5c1111]/40 flex items-center justify-center text-amber-500 hover:bg-[#2c1212] transition-colors shrink-0">
              {isPlaying ? <Pause size={16} className="fill-current" /> : <Play size={16} className="fill-current ml-0.5" />}
            </button>
            <div>
              <span className="text-xs font-semibold text-stone-200 block">Required Core Narration Audio</span>
              <span className="text-[10px] text-stone-500 font-mono block">
                {isPlaying ? "Active Playback" : "Playback Standby"} ({currentCard.estimated_narration_seconds}s planning clip)
              </span>
            </div>
          </div>
          <button onClick={() => setShowTranscript((t) => !t)} className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded border text-xs font-mono transition-all ${showTranscript ? "bg-amber-950/40 text-amber-400 border-amber-500/30" : "bg-transparent border-stone-900 text-stone-500 hover:text-stone-300"}`}>
            <FileText size={12} /> Transcript Text
          </button>
        </div>

        {showTranscript && (
          <div className="px-6 py-4 bg-stone-950 text-stone-400 text-xs italic leading-relaxed border-t border-stone-900 whitespace-pre-line">
            {currentCard.transcript_text}
          </div>
        )}

        <div className="px-6 py-4 bg-stone-950 border-t border-stone-850 flex items-center justify-between">
          <button onClick={() => setCurrentIdx((idx) => Math.max(0, idx - 1))} disabled={currentIdx === 0} className="px-4 py-2 text-xs font-semibold text-stone-500 hover:text-stone-300 disabled:opacity-35 disabled:cursor-not-allowed uppercase tracking-wider">
            &larr; Previous Card
          </button>
          <button onClick={handleNext} disabled={!canContinue} className="bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed">
            {currentIdx === cards.length - 1 ? "Complete Theory Lesson" : "Continue"} &rarr;
          </button>
        </div>
      </div>
    </div>
  );
}

