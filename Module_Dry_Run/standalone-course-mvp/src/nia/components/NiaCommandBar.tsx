import { useState } from "react";
import { Send } from "lucide-react";

const DEFAULT_SUGGESTIONS = [
  "What should I do next?",
  "Why is my certificate locked?",
  "What does Module 1 cover?",
  "Does Clinical Support count for clinical hours?",
  "Help me study for the final exam",
  "What does no PHI mean?",
];

export function NiaCommandBar({
  onSubmit,
  busy,
  suggestions = DEFAULT_SUGGESTIONS,
}: {
  onSubmit: (input: string) => void;
  busy?: boolean;
  suggestions?: string[];
}) {
  const [value, setValue] = useState("");

  function submit(text: string) {
    const trimmed = text.trim();
    if (!trimmed || busy) return;
    onSubmit(trimmed);
    setValue("");
  }

  return (
    <div className="space-y-3">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          submit(value);
        }}
        className="flex items-center gap-2"
      >
        <input
          type="text"
          value={value}
          onChange={(e) => setValue(e.target.value)}
          disabled={busy}
          aria-label="Ask Nia a course question"
          placeholder="Ask about modules, quizzes, certificate gate, clinical support, or CNA scope…"
          className="flex-1 bg-[#0c0606] border border-stone-800 focus:border-amber-500/40 rounded-lg px-3 py-2.5 text-sm text-stone-100 placeholder:text-stone-600 outline-none transition-colors"
        />
        <button
          type="submit"
          disabled={busy || !value.trim()}
          className="inline-flex items-center justify-center bg-[#5c1111] hover:bg-[#781616] disabled:opacity-40 disabled:cursor-not-allowed text-stone-100 border border-[#8a1d1d] rounded-lg p-2.5 transition-colors"
          aria-label="Send"
        >
          <Send size={16} />
        </button>
      </form>

      <div className="flex flex-wrap gap-1.5">
        {suggestions.map((s) => (
          <button
            key={s}
            type="button"
            disabled={busy}
            onClick={() => submit(s)}
            className="text-[10px] text-stone-400 hover:text-stone-100 bg-[#0c0606] hover:bg-stone-900 border border-stone-800 rounded-full px-2.5 py-1 transition-colors disabled:opacity-40"
          >
            {s}
          </button>
        ))}
      </div>
    </div>
  );
}
