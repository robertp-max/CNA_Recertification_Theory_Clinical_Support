import { useMemo, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
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

type StepCard = { card_type?: string; internal_challenge?: unknown };

// Learner-facing step labels. Internal card IDs (e.g. C02A_DELIVERY) are NEVER
// shown to learners; they map to friendly progress labels. Technical IDs are
// only surfaced in reviewer mode.
function buildStepLabels(cards: readonly StepCard[]): string[] {
  const totalDelivery = cards.filter((c) => c.card_type === "delivery").length;
  let deliveryIdx = 0;
  return cards.map((card) => {
    if (card.card_type === "overview") return "Overview";
    if (card.card_type === "delivery") {
      deliveryIdx += 1;
      return totalDelivery > 1 ? `Learn Part ${deliveryIdx}` : "Learn";
    }
    if (card.internal_challenge || card.card_type === "challenge") return "Practice";
    if (card.card_type === "debrief") return "Review";
    return "Complete";
  });
}

export function LessonPlayerPage() {
  const navigate = useNavigate();
  const { moduleId = "m10", lessonId = "l1" } = useParams();
  const { setState } = useLearner();
  const { demoSeconds, brandingMode, reviewerOpen } = useUiState();
  const isDark = brandingMode === "dark";
  const lesson = getGeneratedLesson(moduleId, lessonId);
  const cards = useMemo(() => lesson?.cards ?? [], [lesson]);
  const stepLabels = useMemo(() => buildStepLabels(cards), [cards]);

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
        ContentV2 lesson data is unavailable for {moduleId.toUpperCase()} {lessonId.toUpperCase()}.
      </div>
    );
  }

  const currentCard = cards[currentIdx];
  const isChallengeCard = Boolean(currentCard.internal_challenge);
  const isDebriefCard = currentCard.card_type === "debrief";
  const isLast = currentIdx === cards.length - 1;

  // Read-before-continue: module-level challenges require the learner to open
  // every debrief explanation, because each plausible option teaches a common trap.
  const requiredReads = remediation
    ? remediation.options.map((opt) => opt.id)
    : [];
  const debriefReadDone = requiredReads.every((id) => openedOptions.includes(id));

  const canContinue = isChallengeCard ? submitted : isDebriefCard ? debriefReadDone : true;

  const handleNext = () => {
    if (currentIdx < cards.length - 1) {
      setCurrentIdx((idx) => idx + 1);
      return;
    }
    setState((s) => withLessonCompleted(s, moduleId, lessonId));
    navigate(paths.module(moduleId));
  };

  const challengeChoices = (challenge?.choices ?? []) as { id: string; label: string }[];
  const styles = {
    title: isDark ? "text-stone-100" : "text-stone-900",
    heading: isDark ? "text-stone-400" : "text-stone-600",
    body: isDark ? "text-stone-400" : "text-stone-700",
    muted: isDark ? "text-stone-500" : "text-stone-500",
    accent: isDark ? "text-amber-500" : "text-[#8B1515]",
    divider: isDark ? "border-stone-800/60" : "border-stone-200",
    card: isDark ? "bg-[#120909] border-stone-800/80 shadow-2xl" : "bg-white border-stone-200 shadow-sm",
    stepper: isDark ? "bg-stone-950/60 border-stone-900" : "bg-white border-stone-200 shadow-sm",
    stepDone: isDark ? "bg-amber-950/40 text-amber-400 border-amber-500/30" : "bg-[#8B1515]/10 text-[#8B1515] border-[#8B1515]/25",
    stepFuture: isDark ? "bg-transparent border-stone-800 text-stone-600" : "bg-white border-stone-300 text-stone-500",
    hairline: isDark ? "bg-stone-900" : "bg-stone-200",
    footer: isDark ? "bg-stone-950 border-stone-850" : "bg-stone-50 border-stone-200",
    secondaryText: isDark ? "text-stone-500 hover:text-stone-300" : "text-stone-500 hover:text-stone-700",
    primaryButton: isDark ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]" : "bg-[#8B1515] hover:bg-[#741111] text-white border-[#8B1515]",
  };

  return (
    <div className="space-y-6">
      <div className={`flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b ${styles.divider}`}>
        <button onClick={() => navigate(paths.module(moduleId))} className={`inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider self-start transition-colors ${isDark ? "text-stone-400 hover:text-stone-100" : "text-stone-600 hover:text-[#8B1515]"}`}>
          <ArrowLeft size={14} /> Close Lesson Player
        </button>
        <div className={`flex items-center gap-4 text-xs font-mono ${styles.body}`}>
          <span className="flex items-center gap-1"><Clock size={12} className={styles.accent} /> Lesson Session: {lesson.estimated_minutes}m</span>
          <span>•</span>
          <span className={`flex items-center gap-1 ${styles.accent}`}>
            <span className={`w-1.5 h-1.5 rounded-full ${isDark ? "bg-amber-500" : "bg-[#8B1515]"}`} /> Active time (demo): {formatHoursAndMins(demoSeconds)}
          </span>
        </div>
      </div>

      <div className={`flex items-center justify-between p-3 rounded-lg border overflow-x-auto ${styles.stepper}`}>
        {cards.map((card, idx) => (
          <div key={card.app.location} className="flex items-center gap-3 shrink-0 mx-2">
            <div className={`w-5 h-5 rounded-full border flex items-center justify-center text-[10px] font-mono font-bold ${
              currentIdx === idx
                ? isDark
                  ? "bg-amber-500 border-amber-500 text-black"
                  : "bg-[#8B1515] border-[#8B1515] text-white"
                : currentIdx > idx
                  ? styles.stepDone
                  : styles.stepFuture
            }`}>
              {currentIdx > idx ? <Check size={10} /> : idx + 1}
            </div>
            <span className={`text-[11px] font-semibold uppercase tracking-wider ${currentIdx === idx ? styles.accent : styles.muted}`}>
              {stepLabels[idx]}
            </span>
            {idx < cards.length - 1 && <div className={`w-6 h-px ${styles.hairline}`} />}
          </div>
        ))}
      </div>

      <div className={`border rounded-xl overflow-hidden flex flex-col min-h-[500px] ${styles.card}`}>
        <div className="p-6 md:p-8 flex-1 space-y-6">
          <div>
            <span className={`text-[10px] font-bold uppercase tracking-widest font-mono ${styles.muted}`}>
              {stepLabels[currentIdx]} · Step {currentIdx + 1} of {cards.length}
            </span>
            <h2 className={`text-2xl font-normal tracking-tight mt-1 ${styles.title}`}>{currentCard.display_title}</h2>
            {reviewerOpen && (
              <p className={`text-[11px] font-mono mt-1 ${styles.muted}`}>
                {currentCard.module_id} · {currentCard.lesson_id} · {currentCard.card_id} · {currentCard.app.location}
              </p>
            )}
          </div>

          <MediaSlot appLocation={currentCard.app.location} sceneTitle={currentCard.media_prompt_placeholder.scene_title} />

          {currentCard.card_type === "overview" && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <h4 className={`text-xs uppercase font-bold font-mono tracking-wider ${styles.heading}`}>Learning Goal</h4>
                <p className={`text-xs leading-relaxed ${styles.body}`}>{currentCard.learning_goal}</p>
              </div>
              <div className="space-y-2">
                <h4 className={`text-xs uppercase font-bold font-mono tracking-wider ${styles.heading}`}>Why It Matters</h4>
                <ul className={`space-y-1.5 text-xs leading-relaxed ${styles.body}`}>
                  {currentCard.why_it_matters.map((item) => <li key={item}>{item}</li>)}
                </ul>
              </div>
            </div>
          )}

          {currentCard.card_type === "delivery" && (
            <div className="space-y-4">
              <div className="space-y-2">
                <h4 className={`text-xs uppercase font-bold font-mono tracking-wider ${styles.heading}`}>Lesson Content</h4>
                <p className={`text-xs leading-relaxed whitespace-pre-line ${styles.body}`}>{currentCard.learner_facing_content}</p>
              </div>
              <div className={`p-3 border rounded ${isDark ? "bg-[#1c0d0d] border-[#5c1111]/30" : "bg-[#8B1515]/5 border-[#8B1515]/20"}`}>
                <p className={`text-[11px] leading-relaxed ${isDark ? "text-stone-300" : "text-stone-700"}`}>
                  <strong>CNA practice example:</strong> {currentCard.cna_practice_example}
                </p>
              </div>
            </div>
          )}

          {isChallengeCard && challenge && (
            <div className="space-y-4">
              <p className={`text-xs leading-relaxed font-semibold ${isDark ? "text-stone-300" : "text-stone-800"}`}>{challenge.prompt}</p>
              <div className="grid grid-cols-1 gap-2.5">
                {challengeChoices.map((ans) => (
                  <button
                    key={ans.id}
                    onClick={() => !submitted && setSelectedAnswer(ans.id)}
                    disabled={submitted}
                    className={`w-full text-left p-4 rounded border text-xs flex items-start gap-3 transition-colors ${
                      selectedAnswer === ans.id
                        ? isDark
                          ? "bg-[#1c0d0d] border-amber-500/50 text-stone-100"
                          : "bg-[#8B1515]/5 border-[#8B1515]/30 text-stone-900"
                        : isDark
                          ? "bg-[#080404] border-stone-900 hover:border-stone-800 text-stone-400"
                          : "bg-white border-stone-200 hover:border-[#8B1515]/25 text-stone-700"
                    }`}
                  >
                    <div className={`mt-0.5 w-4 h-4 rounded border flex items-center justify-center text-[10px] font-bold shrink-0 ${
                      selectedAnswer === ans.id
                        ? isDark
                          ? "bg-amber-500 text-black border-amber-500"
                          : "bg-[#8B1515] text-white border-[#8B1515]"
                        : isDark
                          ? "border-stone-600 text-stone-500"
                          : "border-stone-300 text-stone-500"
                    }`}>{ans.id}</div>
                    <span>{ans.label}</span>
                  </button>
                ))}
              </div>
              {!submitted && (
                <button
                  onClick={() => setSubmitted(true)}
                  disabled={!selectedAnswer}
                  className={`border font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed ${styles.primaryButton}`}
                >
                  Submit Response
                </button>
              )}
              {submitted && (
                <p className={`text-[11px] font-mono ${isDark ? "text-amber-500/80" : "text-[#8B1515]/80"}`}>Your response has been submitted. Continue to the Challenge Debrief.</p>
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
                <p className={`text-[11px] font-mono ${styles.muted}`}>
                  Open every option explanation in the debrief to unlock lesson completion. Each option teaches a common trap or the safest reasoning path.
                </p>
              )}
            </>
          )}

          {!isDebriefCard && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-3 pt-2">
              {currentCard.key_terms.slice(0, 3).map((term) => (
                <div key={term.term} className={`border rounded p-3 ${isDark ? "bg-[#080404] border-stone-900" : "bg-stone-50 border-stone-200"}`}>
                  <h4 className={`text-[10px] uppercase font-bold font-mono ${styles.accent}`}>{term.term}</h4>
                  <p className={`text-[11px] leading-relaxed mt-1 ${styles.muted}`}>{term.definition}</p>
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

        <div className={`px-6 py-4 border-t flex items-center justify-between ${styles.footer}`}>
          <button onClick={() => setCurrentIdx((idx) => Math.max(0, idx - 1))} disabled={currentIdx === 0} className={`px-4 py-2 text-xs font-semibold disabled:opacity-35 disabled:cursor-not-allowed uppercase tracking-wider transition-colors ${styles.secondaryText}`}>
            &larr; Previous Card
          </button>
          <button onClick={handleNext} disabled={!canContinue} className={`border font-bold px-6 py-2.5 rounded text-xs uppercase tracking-wider transition-colors disabled:opacity-40 disabled:cursor-not-allowed ${styles.primaryButton}`}>
            {isLast ? "Complete Theory Lesson" : isDebriefCard ? remediation?.continueLabel ?? "Continue" : "Continue"} &rarr;
          </button>
        </div>
      </div>
    </div>
  );
}
