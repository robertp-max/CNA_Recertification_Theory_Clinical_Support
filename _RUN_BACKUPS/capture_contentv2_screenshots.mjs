import { spawn } from "node:child_process";
import { createRequire } from "node:module";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const appRoot = path.join(repoRoot, "standalone-course-mvp");
const require = createRequire(path.join(appRoot, "package.json"));
const { chromium } = require("@playwright/test");
const outputDir = path.join(appRoot, "screenshots", "content-v2-wired");
const port = 5182;
const baseURL = `http://127.0.0.1:${port}`;

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function waitForServer() {
  for (let i = 0; i < 80; i += 1) {
    try {
      const response = await fetch(baseURL);
      if (response.ok) return;
    } catch {
      // keep waiting
    }
    await delay(500);
  }
  throw new Error("Timed out waiting for Vite screenshot server.");
}

async function capture(page, name) {
  await page.addStyleTag({
    content: "*,*::before,*::after{animation-duration:0s!important;transition-duration:0s!important;scroll-behavior:auto!important}",
  });
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(100);
  await page.screenshot({ path: path.join(outputDir, `${name}.png`), fullPage: true, animations: "disabled", caret: "hide" });
}

async function setReadyLearner(page) {
  await page.evaluate(() => {
    const lessonProgress = {};
    const lessonActiveSeconds = {};
    for (const moduleId of ["m1", "m2", "m4", "m5", "m6"]) {
      for (let lesson = 1; lesson <= 6; lesson += 1) {
        const key = `${moduleId}:l${lesson}`;
        lessonProgress[key] = { viewed: true, checkPassed: true, completedAt: new Date().toISOString() };
        lessonActiveSeconds[key] = 999;
      }
    }
    localStorage.setItem("ci-cna-learner-v1", JSON.stringify({
      legalFirstName: "James",
      legalLastName: "Bond",
      cnaNumber: "CNA-DEMO-007",
      onlineCapAck: true,
      phiAck: true,
      orientationFinalAck: true,
      lessonProgress,
      lessonActiveSeconds,
      moduleQuizPassed: { m1: true },
      activeTimeMet: true,
      finalExamAttempted: true,
      finalExamPassed: true,
      finalExamBestScorePct: 88,
      affidavitComplete: true,
      certificateFieldsPopulated: true,
      adminHoldClear: true,
      approvalMetadataPresent: false,
      optionalClinical: { hub: true, skills: true, confidence: true, documentation: true, help: false },
    }));
  });
}

await fs.rm(outputDir, { recursive: true, force: true });
await fs.mkdir(outputDir, { recursive: true });

const server = spawn("npx", ["vite", "--host", "127.0.0.1", "--port", String(port)], {
  cwd: appRoot,
  shell: process.platform === "win32",
  stdio: "pipe",
});

let browser;
try {
  await waitForServer();
  browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1440, height: 1100 }, colorScheme: "dark" });

  await page.goto(baseURL);
  await capture(page, "00-login");
  await page.getByLabel("Username").fill("admin");
  await page.getByRole("textbox", { name: "Password" }).fill("1234");
  await page.getByRole("button", { name: "Sign in" }).click();
  await page.waitForURL("**/dashboard");
  await capture(page, "01-dashboard");

  await page.goto(`${baseURL}/modules`);
  await capture(page, "02-modules");
  await page.goto(`${baseURL}/modules/m0`);
  await capture(page, "03-module-0");
  await page.goto(`${baseURL}/modules/m1`);
  await capture(page, "04-module-1-overview");
  await page.goto(`${baseURL}/modules/m1/lesson`);
  await capture(page, "05-lesson-card-1");
  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "06-lesson-card-2");
  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "07-lesson-card-3");
  const firstChoice = page.locator("button").filter({ hasText: /^A/ }).first();
  if (await firstChoice.count()) await firstChoice.click();
  const submitDecision = page.getByRole("button", { name: "Submit Decision Pattern" });
  if (await submitDecision.count()) await submitDecision.click();
  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "08-lesson-card-4");

  await page.goto(`${baseURL}/modules/m1/assessment`);
  await capture(page, "09-module-assessment-splash");
  await page.goto(`${baseURL}/modules/m1/assessment/quiz`);
  await capture(page, "10-module-assessment-quiz");
  await page.goto(`${baseURL}/final`);
  await capture(page, "11-final-splash");
  await page.goto(`${baseURL}/final/quiz`);
  await capture(page, "12-final-quiz");

  await setReadyLearner(page);
  await page.goto(`${baseURL}/final/result`);
  await capture(page, "13-final-result-passed");
  await page.goto(`${baseURL}/certificate`);
  await capture(page, "14-certificate-ready");
  await page.getByRole("button", { name: "View Mock Certificate Preview" }).click();
  await capture(page, "15-mock-certificate");
  await page.goto(`${baseURL}/clinical-hub`);
  await capture(page, "16-clinical-hub");

  console.log(JSON.stringify({ outputDir, files: (await fs.readdir(outputDir)).sort() }, null, 2));
} finally {
  if (browser) await browser.close();
  server.kill();
}
