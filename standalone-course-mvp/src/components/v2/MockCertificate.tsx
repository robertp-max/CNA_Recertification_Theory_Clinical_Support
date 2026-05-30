import { ArrowLeft, ShieldCheck } from "lucide-react";

// Mock certificate preview surface. PRODUCTION ISSUANCE/DOWNLOAD IS ALWAYS
// DISABLED. Clearly watermarked; carries the legal disclaimer; NAC key is
// pending metadata; nothing here constitutes official certification.
export function MockCertificate({
  firstName,
  lastName,
  cnaNumber,
  onClose,
}: {
  firstName: string;
  lastName: string;
  cnaNumber: string;
  onClose: () => void;
}) {
  return (
    <div className="space-y-6">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 max-w-[1050px] mx-auto w-full no-print">
        <button onClick={onClose} className="text-stone-400 hover:text-stone-100 inline-flex items-center gap-1.5 text-xs font-semibold uppercase tracking-wider self-start">
          <ArrowLeft size={14} /> Back to Gates
        </button>
        <div className="flex items-center gap-3">
          <span className="text-xs text-stone-500 italic">Production download disabled</span>
          <button disabled className="px-5 py-2 rounded bg-stone-900 text-stone-500 border border-stone-800 text-xs font-bold uppercase tracking-wider cursor-not-allowed">
            Print Certificate
          </button>
        </div>
      </div>

      <div className="w-full overflow-x-auto pb-12 flex justify-center">
        <div className="min-w-[760px] max-w-[1050px] w-full shrink-0 relative bg-white shadow-2xl">
          <div className="relative w-full aspect-[11/8.5] bg-[#faf8f5] overflow-hidden flex flex-col text-stone-900 border-8 border-stone-900">
            <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-[#4a0d0d]/5 via-transparent to-transparent pointer-events-none" />

            <div className="absolute inset-0 flex items-center justify-center rotate-[-15deg] select-none pointer-events-none opacity-5">
              <span className="text-5xl md:text-7xl font-black font-mono tracking-widest text-stone-900">MOCK PREVIEW ONLY</span>
            </div>

            <div className="absolute select-none pointer-events-none z-30 opacity-30 border border-red-500 bg-red-50/75 px-3 py-1.5 text-center leading-none rounded" style={{ left: "38%", top: "65%", transform: "translate(-50%, -50%) rotate(-12deg)" }}>
              <span className="text-[10px] font-bold text-red-700 tracking-wider font-mono block">MOCK PREVIEW ONLY</span>
              <span className="text-[7px] font-mono text-stone-600 block mt-0.5 uppercase">Production issuance disabled</span>
            </div>

            <div className="absolute inset-4 border-[3px] border-[#4a0f0f] pointer-events-none z-10" />
            <div className="absolute inset-6 border border-amber-600/40 pointer-events-none z-10" />

            <div className="relative z-20 flex-1 flex flex-col items-center justify-center p-8 md:p-16 text-center">
              <div className="mb-6 flex flex-col items-center gap-2">
                <div className="w-20 h-12 rounded bg-[#4a0f0f] flex items-center justify-center border border-amber-500/20 px-2">
                  <img
                    src="/brand/logos/ci-ion-logo-original.svg"
                    alt="CI Institute of Nursing logo"
                    className="max-h-8 w-auto object-contain brightness-0 invert"
                  />
                </div>
                <div className="tracking-[0.25em] text-[10px] uppercase text-[#4a0f0f] font-bold">CI Institute of Nursing</div>
              </div>

              <h1 className="font-serif text-3xl md:text-5xl text-[#2a0808] mb-2 tracking-wide font-medium">Certificate of Completion</h1>
              <div className="w-24 h-0.5 bg-[#4a0f0f]/20 mb-6" />
              <p className="text-xs uppercase tracking-widest text-stone-500 mb-3 font-semibold">This is to certify that</p>
              <h2 className="font-serif text-3xl md:text-4xl text-[#1a0505] mb-5 tracking-wide">{firstName} {lastName}</h2>
              <div className="text-xs font-semibold text-stone-600 mb-6 font-mono">
                CNA Certificate #: <span className="bg-stone-200/50 px-2 py-0.5 rounded border border-stone-300">{cnaNumber || "—"}</span>
              </div>
              <p className="text-xs text-stone-700 max-w-2xl leading-relaxed mb-8">
                has completed the 12-hour online continuing education theory pathway, demonstrating theoretical knowledge in
                Infection Control, Resident Rights, and Safety standards.
              </p>

              <div className="bg-stone-100/80 border border-stone-200 rounded p-3 text-[9px] text-stone-500 max-w-2xl leading-relaxed text-justify mb-8">
                <strong>Disclaimer:</strong> This preview does not constitute official certification or full California CNA
                renewal. Learners remain responsible for satisfying overall renewal minimums, annual and online-hour limits,
                in-person/practice components, and license timelines.
              </div>

              <div className="w-full px-2 md:px-6 grid grid-cols-3 items-end pt-2 text-[9px] md:text-[10px] font-mono text-stone-500">
                <div className="text-left space-y-1.5 border-l border-stone-300 pl-3">
                  <div><strong className="text-stone-700">Date:</strong> [COMPLETION DATE PLACEHOLDER]</div>
                  <div><strong className="text-stone-700">Active CE:</strong> 12.0 Hours (demo)</div>
                  <div><strong className="text-stone-700">Audit Status:</strong> MOCK PREVIEW</div>
                  <div><strong className="text-stone-700">NAC Key:</strong> [PENDING METADATA]</div>
                </div>
                <div className="flex flex-col items-center justify-center">
                  <div className="relative flex items-center justify-center w-20 h-20 md:w-24 md:h-24">
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-500 to-amber-700 rotate-12 rounded opacity-25" />
                    <div className="absolute inset-0 bg-gradient-to-br from-amber-500 to-amber-700 rotate-45 rounded opacity-25" />
                    <div className="absolute inset-2 border border-dashed border-amber-600 rounded-full" />
                    <div className="absolute inset-3 border border-[#4a0f0f] rounded-full bg-white flex flex-col items-center justify-center shadow-sm">
                      <ShieldCheck size={20} className="text-[#4a0f0f] mb-0.5" />
                      <span className="text-[5px] uppercase tracking-[0.1em] text-[#4a0f0f] font-bold text-center leading-none">MOCK<br />SEAL</span>
                    </div>
                  </div>
                </div>
                <div className="text-right space-y-1">
                  <div className="border-b border-stone-400 pb-1 italic font-serif text-stone-700 text-sm">Program Director</div>
                  <span className="block uppercase tracking-widest text-[8px] text-stone-500 font-bold">Pending Signatory</span>
                  <span className="block text-[8px] text-stone-400 leading-none">CI Institute of Nursing</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
