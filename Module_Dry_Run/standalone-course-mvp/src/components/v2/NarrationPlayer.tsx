import { useEffect, useRef, useState } from "react";
import { FileText, Pause, Play, Volume2, VolumeX } from "lucide-react";
import { hasNarrationAudio, narrationAssetPath } from "../../data/narrationManifest";
import { useUiState } from "../../lib/uiState";

// Production-ready narration control.
// - If an authorized audio file exists for this app.location, it plays it.
// - If not, the play button is a clearly-labeled placeholder (no broken audio,
//   no console errors) and an optional browser-preview (SpeechSynthesis) button
//   is offered, labeled as a non-production preview.
// - The transcript is always available as the accessible fallback.

export function NarrationPlayer({
  appLocation,
  transcript,
  label = "Lesson Narration",
  estSeconds,
}: {
  appLocation: string;
  transcript: string;
  label?: string;
  estSeconds?: number;
}) {
  const { brandingMode } = useUiState();
  const isDark = brandingMode === "dark";
  const audioReady = hasNarrationAudio(appLocation);
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [playing, setPlaying] = useState(false);
  const [showTranscript, setShowTranscript] = useState(false);
  const [speaking, setSpeaking] = useState(false);

  const speechSupported = typeof window !== "undefined" && "speechSynthesis" in window;

  useEffect(() => {
    // Stop any in-flight browser preview when the clip changes or unmounts.
    return () => {
      if (speechSupported) window.speechSynthesis.cancel();
    };
  }, [appLocation, speechSupported]);

  const toggleAudio = () => {
    const el = audioRef.current;
    if (!el) return;
    if (el.paused) {
      void el.play().then(() => setPlaying(true)).catch(() => setPlaying(false));
    } else {
      el.pause();
      setPlaying(false);
    }
  };

  const toggleSpeech = () => {
    if (!speechSupported) return;
    if (speaking) {
      window.speechSynthesis.cancel();
      setSpeaking(false);
      return;
    }
    window.speechSynthesis.cancel();
    const utter = new SpeechSynthesisUtterance(transcript);
    utter.rate = 0.95;
    utter.onend = () => setSpeaking(false);
    utter.onerror = () => setSpeaking(false);
    setSpeaking(true);
    window.speechSynthesis.speak(utter);
  };

  return (
    <div className={`px-6 py-4 border-t ${isDark ? "bg-[#0a0505] border-stone-850" : "bg-stone-50 border-stone-200"}`}>
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          {audioReady ? (
            <button
              onClick={toggleAudio}
              className={`w-10 h-10 rounded-full border flex items-center justify-center transition-colors shrink-0 ${
                isDark
                  ? "bg-[#1c0d0d] border-[#5c1111]/40 text-amber-500 hover:bg-[#2c1212]"
                  : "bg-white border-[#8B1515]/25 text-[#8B1515] hover:bg-[#8B1515]/5"
              }`}
              aria-label={playing ? "Pause narration" : "Play narration"}
            >
              {playing ? <Pause size={16} className="fill-current" /> : <Play size={16} className="fill-current ml-0.5" />}
            </button>
          ) : (
            <div
              className={`w-10 h-10 rounded-full border flex items-center justify-center shrink-0 ${
                isDark ? "bg-stone-950 border-stone-800 text-stone-600" : "bg-white border-stone-200 text-stone-400"
              }`}
              title="Narration audio asset pending approval"
              aria-disabled
            >
              <Play size={16} className="ml-0.5" />
            </div>
          )}
          <div>
            <span className={`text-xs font-semibold block ${isDark ? "text-stone-200" : "text-stone-800"}`}>{label}</span>
            <span className={`text-[10px] font-mono block ${isDark ? "text-stone-500" : "text-stone-500"}`}>
              {audioReady
                ? playing
                  ? "Playing approved audio"
                  : "Approved audio ready"
                : `Audio asset pending${estSeconds ? ` · ${estSeconds}s clip` : ""}`}
            </span>
          </div>
        </div>

        <div className="flex items-center gap-2">
          {!audioReady && speechSupported && (
            <button
              onClick={toggleSpeech}
              className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded border text-xs font-mono transition-all ${
                speaking
                  ? isDark
                    ? "bg-amber-950/40 text-amber-400 border-amber-500/30"
                    : "bg-[#8B1515]/10 text-[#8B1515] border-[#8B1515]/25"
                  : isDark
                    ? "bg-transparent border-stone-900 text-stone-500 hover:text-stone-300"
                    : "bg-white border-stone-300 text-stone-600 hover:text-[#8B1515]"
              }`}
              title="Browser preview only — not approved production audio"
            >
              {speaking ? <VolumeX size={12} /> : <Volume2 size={12} />} {speaking ? "Stop Preview" : "Browser Preview"}
            </button>
          )}
          <button
            onClick={() => setShowTranscript((t) => !t)}
            className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded border text-xs font-mono transition-all ${
              showTranscript
                ? isDark
                  ? "bg-amber-950/40 text-amber-400 border-amber-500/30"
                  : "bg-[#8B1515]/10 text-[#8B1515] border-[#8B1515]/25"
                : isDark
                  ? "bg-transparent border-stone-900 text-stone-500 hover:text-stone-300"
                  : "bg-white border-stone-300 text-stone-600 hover:text-[#8B1515]"
            }`}
          >
            <FileText size={12} /> Transcript
          </button>
        </div>
      </div>

      {audioReady && <audio ref={audioRef} src={narrationAssetPath(appLocation)} onEnded={() => setPlaying(false)} preload="none" />}

      {!audioReady && (
        <p className={`text-[10px] font-mono mt-2 ${isDark ? "text-stone-600" : "text-stone-500"}`}>
          Narration audio is not yet authorized for production. The transcript below is the accessible source of record.
        </p>
      )}

      {showTranscript && (
        <div className={`mt-3 px-4 py-3 text-xs italic leading-relaxed border rounded whitespace-pre-line ${
          isDark ? "bg-stone-950 text-stone-400 border-stone-900" : "bg-white text-stone-700 border-stone-200"
        }`}>
          {transcript}
        </div>
      )}
    </div>
  );
}
