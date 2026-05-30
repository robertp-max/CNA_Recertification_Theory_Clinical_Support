import { Settings, Shield } from "lucide-react";
import { useLearner } from "../../lib/learnerState";
import { useUiState, formatHoursAndMins } from "../../lib/uiState";
import {
  module0Complete,
  lessonCompleted,
  moduleAssessmentPassed,
  withLessonCompleted,
  withLessonReset,
  withModuleAssessment,
  withEverythingUnlocked,
} from "../../lib/v2state";
import { DEFAULT_PROFILE } from "../../lib/learnerState";

// Reviewer-only prototype controls. These never appear in the normal learner
// flow — they live in a collapsible panel above the app chrome and write into
// the canonical LearnerState. They do NOT issue any certificate.
export function ReviewerToolsPanel() {
  const { state, setState, update, resetDemo } = useLearner();
  const { reviewerOpen, setReviewerOpen, demoSeconds } = useUiState();

  const m0 = module0Complete(state);
  const lesson = lessonCompleted(state);
  const m1Exam = moduleAssessmentPassed(state);

  const toggleBtn = (active: boolean, label: string, onClick: () => void) => (
    <button
      onClick={onClick}
      className={`px-3 py-1.5 rounded text-xs font-semibold w-full border transition-colors ${
        active ? "bg-[#310c0c] text-amber-400 border-amber-500/30" : "bg-stone-900 text-stone-400 border-stone-800 hover:text-stone-200"
      }`}
    >
      {label}
    </button>
  );

  return (
    <div className="relative z-50">
      <div className="bg-[#180a0a] border-b border-amber-500/20 text-xs py-1.5 px-4 flex items-center justify-between text-stone-400 no-print">
        <div className="flex items-center gap-2">
          <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
          <span className="font-mono tracking-wide">Reviewer Tools — Prototype Controls Only</span>
        </div>
        <button
          onClick={() => setReviewerOpen((o) => !o)}
          aria-expanded={reviewerOpen}
          className="flex items-center gap-1.5 text-amber-500 hover:text-amber-400 font-semibold uppercase tracking-wider px-2 py-0.5 rounded bg-amber-950/40 border border-amber-500/20 transition-all"
        >
          <Settings size={12} />
          {reviewerOpen ? "Close Reviewer Panel" : "Open Reviewer Panel"}
        </button>
      </div>

      {reviewerOpen && (
        <div className="bg-[#120606] border-b border-[#5c1111] p-4 text-sm">
          <div className="max-w-6xl mx-auto">
            <div className="flex items-center justify-between mb-3 border-b border-stone-800 pb-2">
              <span className="font-semibold text-stone-200 uppercase tracking-widest text-[11px] flex items-center gap-2">
                <Shield size={14} className="text-amber-500" /> Prototype State Override Panel
              </span>
              <span className="text-xs text-stone-500 italic">Simulates user progress &amp; compliance actions</span>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              <div>
                <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Module 0 Status</label>
                <div className="flex gap-2">
                  {toggleBtn(m0, m0 ? "Complete" : "Complete", () =>
                    setState((s) => ({
                      ...s,
                      legalFirstName: s.legalFirstName || DEFAULT_PROFILE.legalFirstName,
                      legalLastName: s.legalLastName || DEFAULT_PROFILE.legalLastName,
                      cnaNumber: s.cnaNumber || DEFAULT_PROFILE.cnaNumber,
                      orientationFinalAck: true,
                      phiAck: true,
                      onlineCapAck: true,
                    })),
                  )}
                  <button
                    onClick={() => setState((s) => ({ ...s, orientationFinalAck: false, phiAck: false, onlineCapAck: false }))}
                    className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-stone-500 hover:text-stone-300"
                  >
                    Reset
                  </button>
                </div>
              </div>

              <div>
                <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Lesson Completed</label>
                {toggleBtn(lesson, lesson ? "Completed" : "Not Started", () =>
                  setState((s) => (lessonCompleted(s) ? withLessonReset(s) : withLessonCompleted(s))),
                )}
              </div>

              <div>
                <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Module 1 Exam</label>
                <div className="flex gap-1">
                  <button
                    onClick={() => setState((s) => withModuleAssessment(s, true))}
                    className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${
                      m1Exam ? "bg-[#310c0c] text-amber-400 border-amber-500/30" : "bg-stone-900 text-stone-400 border-stone-800"
                    }`}
                  >
                    Pass
                  </button>
                  <button
                    onClick={() => setState((s) => withModuleAssessment(s, false))}
                    className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-red-400 font-semibold hover:bg-stone-850"
                  >
                    Fail
                  </button>
                </div>
              </div>

              <div>
                <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Final Exam</label>
                <div className="flex gap-1">
                  <button
                    onClick={() => setState((s) => ({ ...s, finalExamPassed: true, finalExamAttempted: true }))}
                    className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${
                      state.finalExamPassed ? "bg-[#310c0c] text-amber-400 border-amber-500/30" : "bg-stone-900 text-stone-400 border-stone-800"
                    }`}
                  >
                    Pass
                  </button>
                  <button
                    onClick={() => setState((s) => ({ ...s, finalExamPassed: false, finalExamAttempted: true }))}
                    className="px-2 py-1.5 rounded text-xs bg-stone-900 border border-stone-800 text-red-400 font-semibold hover:bg-stone-850"
                  >
                    Fail
                  </button>
                </div>
              </div>

              <div className="flex flex-col justify-end">
                <label className="block text-stone-500 text-[10px] uppercase font-bold mb-1">Affidavit</label>
                {toggleBtn(state.affidavitComplete, state.affidavitComplete ? "Signed" : "Unsigned", () =>
                  update("affidavitComplete", !state.affidavitComplete),
                )}
              </div>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mt-4">
              <div className="md:col-span-2 flex items-end gap-2">
                <button
                  onClick={() => setState((s) => withEverythingUnlocked(s))}
                  className="flex-1 bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] text-xs font-bold py-2 px-2 rounded transition-colors uppercase tracking-wider"
                >
                  Unlock All
                </button>
                <button
                  onClick={() => resetDemo()}
                  className="flex-1 bg-stone-900 border border-stone-800 hover:bg-stone-850 text-stone-400 text-xs font-bold py-2 px-2 rounded transition-colors uppercase tracking-wider"
                >
                  Reset All
                </button>
              </div>
              <div className="md:col-span-3 flex items-end">
                <div className="text-[11px] text-stone-500 flex flex-wrap gap-x-4 gap-y-1">
                  <span>
                    <strong>Active study time:</strong> {formatHoursAndMins(demoSeconds)}{" "}
                    <span className="text-amber-500/80">(demo / MVP — not CDPH-validated)</span>
                  </span>
                  <span>
                    <strong>Affidavit:</strong> {state.affidavitComplete ? "Signed" : "No"}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
