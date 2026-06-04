import React from "react";
import { createRoot } from "react-dom/client";
import { App } from "./app/App";
import "./styles/tokens.css";
import "./styles/base.css";
import "./styles/tailwind.css";

const params = new URLSearchParams(window.location.search);
const mode = params.get("mode") === "normal" ? "normal" : "dark";

window.localStorage.setItem("ciIonBrandingMode", JSON.stringify(mode));
window.localStorage.setItem("ci-cna-auth-v1", JSON.stringify(true));

if (window.location.pathname.endsWith("/v2-screenshot.html")) {
  window.history.replaceState(null, "", `/dashboard?mode=${mode}`);
}

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);
