import { expect, type Page, test } from "@playwright/test";
import fs from "node:fs/promises";
import path from "node:path";

let outputDir = path.resolve(process.cwd(), "screenshots", "v2-design");

async function stabilize(page: Page) {
  await page.addStyleTag({
    content: `
      *, *::before, *::after {
        animation-duration: 0s !important;
        animation-delay: 0s !important;
        transition-duration: 0s !important;
        transition-delay: 0s !important;
        scroll-behavior: auto !important;
      }
    `,
  });
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(100);
}

async function capture(page: Page, name: string) {
  await stabilize(page);
  await page.screenshot({
    path: path.join(outputDir, `${name}.png`),
    fullPage: true,
    animations: "disabled",
    caret: "hide",
  });
}

async function openReviewerPanel(page: Page) {
  const openButton = page.getByRole("button", { name: "Open Reviewer Panel" });
  if (await openButton.isVisible()) {
    await openButton.click();
    await expect(page.getByText("Prototype State Override Panel")).toBeVisible();
  }
}

async function closeReviewerPanel(page: Page) {
  const closeButton = page.getByRole("button", { name: "Close Reviewer Panel" });
  if (await closeButton.isVisible()) {
    await closeButton.click();
  }
}

async function unlockAllButFinal(page: Page) {
  await openReviewerPanel(page);
  await page.getByRole("button", { name: "Unlock All" }).click();
  await page.getByRole("button", { name: "Fail" }).nth(1).click();
  await closeReviewerPanel(page);
  await stabilize(page);
}

async function captureLessonCards(page: Page) {
  await capture(page, "08-lesson-card-1-overview");

  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "09-lesson-card-2a-delivery");

  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "10-lesson-card-2b-delivery");

  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "11-lesson-card-2c-delivery");

  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "12-lesson-card-3-challenge");

  await page.getByRole("button", { name: /Hand hygiene performed correctly/ }).click();
  await page.getByRole("button", { name: "Submit Response" }).click();
  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "13-lesson-card-4a-debrief");
}

async function markFinalPassed(page: Page) {
  await page.evaluate(() => {
    const key = "ci-cna-learner-v1";
    const state = JSON.parse(window.localStorage.getItem(key) || "{}");
    window.localStorage.setItem(
      key,
      JSON.stringify({
        ...state,
        finalExamAttempted: true,
        finalExamAttempts: Math.max(state.finalExamAttempts || 0, 1),
        finalExamBestScorePct: Math.max(state.finalExamBestScorePct || 0, 100),
        finalExamPassed: true,
        affidavitComplete: true,
      }),
    );
  });
}

for (const mode of ["normal", "dark"] as const) {
  test(`capture every v2 design screen in ${mode} mode`, async ({ page }) => {
    outputDir = path.resolve(process.cwd(), "screenshots", "v2-design", mode);
    await fs.rm(outputDir, { recursive: true, force: true });
    await fs.mkdir(outputDir, { recursive: true });

    await page.goto(`/v2-screenshot.html?mode=${mode}`);
    await expect(page.getByText("Gate Review Status")).toBeVisible();
    await stabilize(page);

    await capture(page, "01-dashboard-default");

    await page.getByRole("button", { name: "Open Nia" }).click();
    await expect(page.getByRole("complementary", { name: "Nia (Nurse Instructor Assistant)" })).toBeVisible();
    await capture(page, "02-nia-drawer");
    await page.getByRole("button", { name: "Close Nia" }).click();

    await openReviewerPanel(page);
    await capture(page, "03-reviewer-tools-panel");
    await closeReviewerPanel(page);

    await page.getByRole("link", { name: "Certificate Gate", exact: true }).click();
    await expect(page.getByText("Certificate Status Locked")).toBeVisible();
    await capture(page, "04-certificate-gate-locked");

    await page.getByRole("link", { name: "CE Modules", exact: true }).click();
    await expect(page.getByText("Theory Recertification Modules")).toBeVisible();
    await capture(page, "05-modules-default");

    await page.getByRole("button", { name: "Open Module" }).first().click();
    await expect(page.getByText("Identity and Compliance Orientation")).toBeVisible();
    await capture(page, "06-module-0-orientation");

    await page.getByRole("link", { name: "CE Modules", exact: true }).click();
    await unlockAllButFinal(page);
    await expect(page.getByText("Theory Recertification Modules")).toBeVisible();
    await capture(page, "07-modules-unlocked-final-ready");

    await page.goto("/modules/m1");
    await expect(page.getByText("Infection Control & PPE")).toBeVisible();
    await capture(page, "08-module-1-overview");

    await page.getByRole("button", { name: "Review Theory" }).click();
    await expect(page.getByText("Why Infection Control Matters in Long-Term Care")).toBeVisible();
    await captureLessonCards(page);

    await page.getByRole("link", { name: "CE Modules", exact: true }).click();
    await page.goto("/modules/m1/assessment");
    await expect(page.getByText("Module 1 Knowledge Check")).toBeVisible();
    await capture(page, "14-module-1-assessment-splash");

    await page.getByRole("button", { name: "Begin Assessment Exam" }).click();
    await expect(page.getByText("MODULE 1 ASSESSMENT")).toBeVisible();
    await capture(page, "15-module-1-assessment-quiz");

    await page.goto("/final");
    await expect(page.getByText("Course Final Assessment")).toBeVisible();
    await capture(page, "16-final-assessment-splash");

    await page.getByRole("button", { name: "Begin Course Final Exam" }).click();
    await expect(page.getByText("COURSE THEORY FINAL EXAM")).toBeVisible();
    await capture(page, "17-final-assessment-quiz");

    await markFinalPassed(page);
    await page.goto("/final/result");
    await expect(page.getByText("Final Assessment Passed")).toBeVisible();
    await capture(page, "18-final-result-passed");

    await page.getByRole("link", { name: "Certificate Gate", exact: true }).click();
    await expect(page.getByText("Compliance Gates Cleared")).toBeVisible();
    await capture(page, "19-certificate-gate-ready");

    await page.getByRole("button", { name: "View Mock Certificate Preview" }).click();
    await expect(page.getByText("Certificate of Completion")).toBeVisible();
    await capture(page, "20-mock-certificate-preview");

    await page.getByRole("link", { name: "Clinical Hub", exact: true }).click();
    await expect(page.getByText("Clinical Scenario Support Hub")).toBeVisible();
    await capture(page, "21-clinical-hub");

    await page.goto(`/not-a-real-route?mode=${mode}`);
    await expect(page.getByText("Page not found")).toBeVisible();
    await capture(page, "22-not-found");
  });
}
