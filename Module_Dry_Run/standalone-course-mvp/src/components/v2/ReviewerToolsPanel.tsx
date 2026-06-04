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
  const { reviewerOpen, setReviewerOpen, demoSeconds, brandingMode } = useUiState();
  const isDark = brandingMode === "dark";

  const m0 = module0Complete(state);
  const lesson = lessonCompleted(state);
  const m1Exam = moduleAssessmentPassed(state);
  const styles = {
    strip: isDark
      ? "bg-[#180a0a] border-amber-500/20 text-stone-400"
      : "bg-white border-stone-200 text-stone-600 shadow-sm",
    panel: isDark ? "bg-[#120606] border-[#5c1111] text-stone-300" : "bg-[#FBF9F9] border-stone-200 text-stone-700 shadow-sm",
    divider: isDark ? "border-stone-800" : "border-stone-200",
    heading: isDark ? "text-stone-200" : "text-stone-700",
    muted: isDark ? "text-stone-500" : "text-stone-500",
    label: isDark ? "text-stone-500" : "text-stone-600",
    inactiveButton: isDark
      ? "bg-stone-900 text-stone-400 border-stone-800 hover:text-stone-200"
      : "bg-white text-stone-600 border-stone-300 hover:text-[#8B1515] hover:border-[#8B1515]/30",
    activeButton: isDark
      ? "bg-[#310c0c] text-amber-400 border-amber-500/30"
      : "bg-[#8B1515]/10 text-[#8B1515] border-[#8B1515]/25",
    dangerButton: isDark
      ? "bg-stone-900 border-stone-800 text-red-400 hover:bg-stone-850"
      : "bg-white border-red-200 text-red-700 hover:bg-red-50",
  };

  const toggleBtn = (active: boolean, label: string, onClick: () => void) => (
    <button
      onClick={onClick}
      className={`px-3 py-1.5 rounded text-xs font-semibold w-full border transition-colors ${
        active ? styles.activeButton : styles.inactiveButton
      }`}
    >
      {label}
    </button>
  );

  return (
    <div className="reviewer-tools-root relative z-50">
      <div className={`border-b text-xs py-1.5 px-4 flex items-center justify-between no-print ${styles.strip}`}>
        <div className="flex items-center gap-2">
          <span className={`w-1.5 h-1.5 rounded-full ${isDark ? "bg-amber-500" : "bg-[#8B1515]"}`} />
          <span className="font-mono tracking-wide">Reviewer Tools — Prototype Controls Only</span>
        </div>
        <button
          onClick={() => setReviewerOpen((o) => !o)}
          className={`flex items-center gap-1.5 font-semibold uppercase tracking-wider px-2 py-0.5 rounded border transition-all ${
            isDark
              ? "text-amber-500 hover:text-amber-400 bg-amber-950/40 border-amber-500/20"
              : "text-[#8B1515] hover:text-[#6F1111] bg-[#8B1515]/5 border-[#8B1515]/20"
          }`}
        >
          <Settings size={12} />
          {reviewerOpen ? "Close Reviewer Panel" : "Open Reviewer Panel"}
        </button>
      </div>

      {reviewerOpen && (
        <div className={`border-b p-4 text-sm ${styles.panel}`}>
          <div className="max-w-6xl mx-auto">
            <div className={`flex items-center justify-between mb-3 border-b pb-2 ${styles.divider}`}>
              <span className={`font-semibold uppercase tracking-widest text-[11px] flex items-center gap-2 ${styles.heading}`}>
                <Shield size={14} className={isDark ? "text-amber-500" : "text-[#8B1515]"} /> Prototype State Override Panel
              </span>
              <span className={`text-xs italic ${styles.muted}`}>Simulates user progress &amp; compliance actions</span>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
              <div>
                <label className={`block text-[10px] uppercase font-bold mb-1 ${styles.label}`}>Module 0 Status</label>
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
                    className={`px-2 py-1.5 rounded text-xs border transition-colors ${styles.inactiveButton}`}
                  >
                    Reset
                  </button>
                </div>
              </div>

              <div>
                <label className={`block text-[10px] uppercase font-bold mb-1 ${styles.label}`}>Lesson Completed</label>
                {toggleBtn(lesson, lesson ? "Completed" : "Not Started", () =>
                  setState((s) => (lessonCompleted(s) ? withLessonReset(s) : withLessonCompleted(s))),
                )}
              </div>

              <div>
                <label className={`block text-[10px] uppercase font-bold mb-1 ${styles.label}`}>Module 1 Exam</label>
                <div className="flex gap-1">
                  <button
                    onClick={() => setState((s) => withModuleAssessment(s, true))}
                    className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${
                      m1Exam ? styles.activeButton : styles.inactiveButton
                    }`}
                  >
                    Pass
                  </button>
                  <button
                    onClick={() => setState((s) => withModuleAssessment(s, false))}
                    className={`px-2 py-1.5 rounded text-xs border font-semibold transition-colors ${styles.dangerButton}`}
                  >
                    Fail
                  </button>
                </div>
              </div>

              <div>
                <label className={`block text-[10px] uppercase font-bold mb-1 ${styles.label}`}>Final Exam</label>
                <div className="flex gap-1">
                  <button
                    onClick={() => setState((s) => ({ ...s, finalExamPassed: true, finalExamAttempted: true }))}
                    className={`px-2 py-1.5 rounded text-xs font-semibold flex-1 border ${
                      state.finalExamPassed ? styles.activeButton : styles.inactiveButton
                    }`}
                  >
                    Pass
                  </button>
                  <button
                    onClick={() => setState((s) => ({ ...s, finalExamPassed: false, finalExamAttempted: true }))}
                    className={`px-2 py-1.5 rounded text-xs border font-semibold transition-colors ${styles.dangerButton}`}
                  >
                    Fail
                  </button>
                </div>
              </div>

              <div className="flex flex-col justify-end">
                <label className={`block text-[10px] uppercase font-bold mb-1 ${styles.label}`}>Affidavit</label>
                {toggleBtn(state.affidavitComplete, state.affidavitComplete ? "Signed" : "Unsigned", () =>
                  update("affidavitComplete", !state.affidavitComplete),
                )}
              </div>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mt-4">
              <div className="md:col-span-2 flex items-end gap-2">
                <button
                  onClick={() => setState((s) => withEverythingUnlocked(s))}
                  className={`flex-1 text-xs font-bold py-2 px-2 rounded transition-colors uppercase tracking-wider border ${
                    isDark
                      ? "bg-[#5c1111] hover:bg-[#781616] text-stone-100 border-[#8a1d1d]"
                      : "bg-[#8B1515] hover:bg-[#741111] text-white border-[#8B1515]"
                  }`}
                >
                  Unlock All
                </button>
                <button
                  onClick={() => resetDemo()}
                  className={`flex-1 border text-xs font-bold py-2 px-2 rounded transition-colors uppercase tracking-wider ${styles.inactiveButton}`}
                >
                  Reset All
                </button>
              </div>
              <div className="md:col-span-3 flex items-end">
                <div className={`text-[11px] flex flex-wrap gap-x-4 gap-y-1 ${styles.muted}`}>
                  <span>
                    <strong>Active study time:</strong> {formatHoursAndMins(demoSeconds)}{" "}
                    <span className={isDark ? "text-amber-500/80" : "text-[#8B1515]/80"}>(demo / MVP — not CDPH-validated)</span>
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
