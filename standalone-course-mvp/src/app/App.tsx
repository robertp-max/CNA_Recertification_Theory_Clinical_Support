import { useEffect, useState } from "react";
import { BrowserRouter } from "react-router-dom";
import { LearnerProvider } from "../lib/learnerState";
import { UiStateProvider } from "../lib/uiState";
import { loadJSON, saveJSON } from "../lib/storage";
import { ReviewerLogin } from "../pages/ReviewerLogin";
import { AppShell } from "../components/v2/AppShell";
import { AppRoutes } from "./router";

const AUTH_KEY = "ci-cna-auth-v1";

export function App() {
  // Demo auth persists so a refresh preserves both the route and signed-in state.
  const [authed, setAuthed] = useState<boolean>(() => loadJSON(AUTH_KEY, false));

  useEffect(() => {
    saveJSON(AUTH_KEY, authed);
  }, [authed]);

  if (!authed) {
    // Approved sign-in page — rendered full-screen, outside the app shell.
    return <ReviewerLogin onAuthenticated={() => setAuthed(true)} />;
  }

  return (
    <LearnerProvider>
      <UiStateProvider>
        <BrowserRouter>
          <a href="#main-content" className="skip-link">Skip to main content</a>
          <AppShell>
            <AppRoutes />
          </AppShell>
        </BrowserRouter>
      </UiStateProvider>
    </LearnerProvider>
  );
}
