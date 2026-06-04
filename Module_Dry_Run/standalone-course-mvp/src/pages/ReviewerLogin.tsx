// PROTECTED — APPROVED SIGN-IN PAGE (FROZEN).
// JSX, copy, classes, credentials, and behavior preserved verbatim from the original.
// Only change vs. original: it manages its own form state and calls onAuthenticated().
import React, { useEffect, useRef, useState } from "react";
import { ChevronRight, Lock, Map, ShieldCheck, UserRound } from "lucide-react";
import { reviewerCredentials, type LoginFormState } from "../lib/auth";
import { useUiState } from "../lib/uiState";
import { BrandingModeToggle } from "../components/v2/BrandingModeToggle";
import "../styles/login.css";

export function ReviewerLogin({ onAuthenticated }: { onAuthenticated: () => void }) {
  const { brandingMode } = useUiState();
  const [loginForm, setLoginForm] = useState<LoginFormState>({ username: "", password: "" });
  const [showPassword, setShowPassword] = useState(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);
  const toastTimeout = useRef<number | null>(null);

  const updateLoginForm = <K extends keyof LoginFormState>(key: K, value: LoginFormState[K]) =>
    setLoginForm((current) => ({ ...current, [key]: value }));

  const showLoginMessage = (message: string) => {
    setToastMessage(message);
    if (toastTimeout.current) window.clearTimeout(toastTimeout.current);
    toastTimeout.current = window.setTimeout(() => setToastMessage(null), 2400);
  };

  const onSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const usernameMatches = loginForm.username.trim().toLowerCase() === reviewerCredentials.username;
    const passwordMatches = loginForm.password === reviewerCredentials.password;
    if (usernameMatches && passwordMatches) {
      if (toastTimeout.current) window.clearTimeout(toastTimeout.current);
      setToastMessage(null);
      onAuthenticated();
      return;
    }
    showLoginMessage("Use reviewer access: admin / 1234.");
  };

  useEffect(() => {
    return () => {
      if (toastTimeout.current) window.clearTimeout(toastTimeout.current);
    };
  }, []);

  return (
    <div className="reviewer-login-page" data-theme={brandingMode}>
      <main className="reviewer-login-shell" aria-label="CI Institute of Nursing login page">
        <section className="reviewer-login-card relative" aria-label="Sign in">
          <div className="absolute top-4 right-4 z-10">
            <BrandingModeToggle />
          </div>
          <div className="reviewer-login-brand-row">
            <div className="reviewer-login-brand-lockup">
              <img
                className="reviewer-login-brand-logo"
                src="/brand/logos/ci-ion-logo-original.svg"
                alt="CI Institute of Nursing logo"
              />
              <span className="reviewer-login-brand-tagline">Nursing Excellence. Elevating Care.</span>
            </div>
          </div>

          <div className="reviewer-login-headline">
            <h1>Welcome back.<br />Let&apos;s continue your journey.</h1>
            <p className="reviewer-login-course-title">CNA Recertification Theory + Clinical Support</p>
            <p className="reviewer-login-course-copy">
              Complete your required online theory and strengthen your skills through optional clinical support.
            </p>
          </div>

          <form onSubmit={onSubmit} className="reviewer-login-form">
            <div className="reviewer-login-field-group">
              <label htmlFor="reviewer-username">Username</label>
              <div className="reviewer-login-input-shell">
                <UserRound />
                <input
                  id="reviewer-username"
                  type="text"
                  autoComplete="username"
                  placeholder="Enter your username"
                  value={loginForm.username}
                  onChange={(event) => updateLoginForm("username", event.target.value)}
                />
              </div>
            </div>

            <div className="reviewer-login-field-group">
              <label htmlFor="reviewer-password">Password</label>
              <div className="reviewer-login-input-shell">
                <Lock />
                <input
                  id="reviewer-password"
                  type={showPassword ? "text" : "password"}
                  autoComplete="current-password"
                  placeholder="Enter your password"
                  value={loginForm.password}
                  onChange={(event) => updateLoginForm("password", event.target.value)}
                />
                <button
                  className="reviewer-login-icon-button"
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  aria-label={showPassword ? "Hide password" : "Show password"}
                >
                  {showPassword ? "Hide" : "Show"}
                </button>
              </div>
              <div className="reviewer-login-password-row">
                <button className="reviewer-login-forgot" type="button">
                  Forgot password?
                </button>
              </div>
            </div>

            <div className="reviewer-login-portal-select" role="button" tabIndex={0} aria-label="Access organization local portal">
              <Map />
              <span>
                <strong className="reviewer-login-portal-title">Are you signing in at a facility or school?</strong>
                <span className="reviewer-login-portal-sub">Access your organization&apos;s local portal</span>
              </span>
              <ChevronRight />
            </div>

            <button className="reviewer-login-sign-in" type="submit">
              Sign in
              <ChevronRight />
            </button>
          </form>

          <div className="reviewer-login-notice">
            <div className="reviewer-login-shield"><ShieldCheck /></div>
            <div>
              This is a reviewer and stakeholder access environment
              <br />
              for CI Institute of Nursing. Use is monitored and logged.
            </div>
          </div>
        </section>
      </main>

      <div className={toastMessage ? "reviewer-login-toast show" : "reviewer-login-toast"} role="status" aria-live="polite">
        {toastMessage || "Login preview only."}
      </div>
    </div>
  );
}
