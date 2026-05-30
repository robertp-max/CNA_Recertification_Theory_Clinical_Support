import { useEffect, useRef, useState } from "react";
import { FileText, Pause, Play, Volume2, VolumeX } from "lucide-react";
import { hasNarrationAudio, narrationAssetPath } from "../../data/narrationManifest";

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
    <div className="px-6 py-4 bg-[#0a0505] border-t border-stone-850">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          {audioReady ? (
            <button
              onClick={toggleAudio}
              className="w-10 h-10 rounded-full bg-[#1c0d0d] border border-[#5c1111]/40 flex items-center justify-center text-amber-500 hover:bg-[#2c1212] transition-colors shrink-0"
              aria-label={playing ? "Pause narration" : "Play narration"}
            >
              {playing ? <Pause size={16} className="fill-current" /> : <Play size={16} className="fill-current ml-0.5" />}
            </button>
          ) : (
            <div
              className="w-10 h-10 rounded-full bg-stone-950 border border-stone-800 flex items-center justify-center text-stone-600 shrink-0"
              title="Narration audio asset pending approval"
              aria-disabled
            >
              <Play size={16} className="ml-0.5" />
            </div>
          )}
          <div>
            <span className="text-xs font-semibold text-stone-200 block">{label}</span>
            <span className="text-[10px] text-stone-500 font-mono block">
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
                speaking ? "bg-amber-950/40 text-amber-400 border-amber-500/30" : "bg-transparent border-stone-900 text-stone-500 hover:text-stone-300"
              }`}
              title="Browser preview only — not approved production audio"
            >
              {speaking ? <VolumeX size={12} /> : <Volume2 size={12} />} {speaking ? "Stop Preview" : "Browser Preview"}
            </button>
          )}
          <button
            onClick={() => setShowTranscript((t) => !t)}
            className={`inline-flex items-center gap-1.5 px-3 py-1.5 rounded border text-xs font-mono transition-all ${
              showTranscript ? "bg-amber-950/40 text-amber-400 border-amber-500/30" : "bg-transparent border-stone-900 text-stone-500 hover:text-stone-300"
            }`}
          >
            <FileText size={12} /> Transcript
          </button>
        </div>
      </div>

      {audioReady && <audio ref={audioRef} src={narrationAssetPath(appLocation)} onEnded={() => setPlaying(false)} preload="none" />}

      {!audioReady && (
        <p className="text-[10px] text-stone-600 font-mono mt-2">
          Narration audio is not yet authorized for production. The transcript below is the accessible source of record.
        </p>
      )}

      {showTranscript && (
        <div className="mt-3 px-4 py-3 bg-stone-950 text-stone-400 text-xs italic leading-relaxed border border-stone-900 rounded whitespace-pre-line">
          {transcript}
        </div>
      )}
    </div>
  );
}
