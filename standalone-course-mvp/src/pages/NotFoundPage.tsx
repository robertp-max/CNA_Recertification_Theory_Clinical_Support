import { Link } from "react-router-dom";
import { paths } from "../app/routes";

export function NotFoundPage() {
  return (
    <div className="max-w-xl mx-auto text-center space-y-4 py-16">
      <h1 className="text-2xl font-normal text-stone-100">Page not found</h1>
      <p className="text-sm text-stone-400">That route does not exist in this preview.</p>
      <Link to={paths.dashboard} className="inline-flex items-center justify-center bg-[#5c1111] hover:bg-[#781616] text-stone-100 border border-[#8a1d1d] font-bold px-5 py-2.5 rounded text-xs uppercase tracking-wider transition-colors">
        Back to Dashboard
      </Link>
    </div>
  );
}
