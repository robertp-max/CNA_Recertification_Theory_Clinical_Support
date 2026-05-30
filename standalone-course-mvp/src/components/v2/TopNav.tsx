import { Link, useLocation } from "react-router-dom";
import { primaryNav, paths } from "../../app/routes";

function isActive(pathname: string, to: string, prefixes?: string[]) {
  if (prefixes?.some((p) => pathname.startsWith(p))) return true;
  return pathname === to || pathname.startsWith(to + "/");
}

export function TopNav() {
  const { pathname } = useLocation();
  return (
    <header className="px-4 sm:px-6 py-4 border-b border-stone-800/60 bg-[#0c0606]/85 backdrop-blur-md relative z-40 flex items-center justify-between shrink-0 no-print">
      <Link to={paths.dashboard} className="flex items-center gap-3" aria-label="CI Institute of Nursing — course home">
        <div>
          <img
            src="/brand/logos/ci-ion-logo-original.svg"
            alt="CI Institute of Nursing logo"
            className="h-9 w-auto object-contain brightness-0 invert"
          />
          <span className="text-[9px] text-stone-500 block -mt-1 font-mono uppercase tracking-widest">CNA CE Program Preview</span>
        </div>
      </Link>

      <nav className="flex items-center gap-1 sm:gap-3 text-xs sm:text-sm font-medium text-stone-400" aria-label="Primary">
        {primaryNav.map((item) => {
          const active = isActive(pathname, item.to, item.matchPrefixes);
          return (
            <Link
              key={item.to}
              to={item.to}
              aria-current={active ? "page" : undefined}
              className={`transition-all px-2.5 sm:px-3 py-1.5 rounded-lg border uppercase tracking-wider text-[10px] sm:text-[11px] font-semibold ${
                active
                  ? "text-amber-500 bg-[#1f0d0d] border-[#5c1111]"
                  : "border-transparent text-stone-400 hover:text-stone-200 hover:bg-stone-900/40"
              }`}
            >
              {item.label}
            </Link>
          );
        })}
        <div className="w-8 h-8 rounded bg-[#1b1212] text-amber-500 flex items-center justify-center border border-stone-800/80 ml-1 sm:ml-3">
          <span className="text-xs font-bold font-mono">JB</span>
        </div>
      </nav>
    </header>
  );
}
