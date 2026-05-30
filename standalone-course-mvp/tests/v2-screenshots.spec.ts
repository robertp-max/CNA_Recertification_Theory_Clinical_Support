import { expect, type Page, test } from "@playwright/test";
import fs from "node:fs/promises";
import path from "node:path";

const outputDir = path.resolve(process.cwd(), "screenshots", "v2-design");

const correctFinalAnswers = [
  "Mode of Transmission",
  "Standard Surgical Mask",
  "20 Seconds",
  "Always maintaining the drainage bag below bladder level",
  "Client medical record numbers",
];

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
  await capture(page, "09-lesson-card-2-delivery");

  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "10-lesson-card-3-challenge");

  await page.getByRole("button", { name: /Sanitize hands, don clean gown/ }).click();
  await page.getByRole("button", { name: "Submit Decision Pattern" }).click();
  await page.getByRole("button", { name: /Continue/ }).click();
  await capture(page, "11-lesson-card-4-debrief");
}

async function answerFinalExam(page: Page) {
  for (let i = 0; i < correctFinalAnswers.length; i += 1) {
    await page.getByRole("button", { name: new RegExp(correctFinalAnswers[i]) }).click();
    if (i < correctFinalAnswers.length - 1) {
      await page.getByRole("button", { name: "Next" }).click();
    }
  }
  await page.getByRole("button", { name: "Submit Exam" }).click();
  await expect(page.getByText("Competency Accomplished")).toBeVisible();
}

test("capture every v2 design screen", async ({ page }) => {
  await fs.rm(outputDir, { recursive: true, force: true });
  await fs.mkdir(outputDir, { recursive: true });

  await page.goto("/v2-screenshot.html");
  await expect(page.getByText("CNA CE Theory Portal")).toBeVisible();
  await stabilize(page);

  await capture(page, "01-dashboard-default");

  await openReviewerPanel(page);
  await capture(page, "02-reviewer-tools-panel");
  await closeReviewerPanel(page);

  await page.getByRole("button", { name: "Certificate Gate", exact: true }).click();
  await expect(page.getByText("Certificate Status Locked")).toBeVisible();
  await capture(page, "03-certificate-gate-locked");

  await page.getByRole("button", { name: "CE Modules", exact: true }).click();
  await expect(page.getByText("Theory Recertification Modules")).toBeVisible();
  await capture(page, "04-modules-default");

  await page.getByRole("button", { name: "Begin" }).click();
  await expect(page.getByText("Identity & Compliance Orientation")).toBeVisible();
  await capture(page, "05-module-0-orientation");

  await page.getByRole("button", { name: "CE Modules", exact: true }).click();
  await unlockAllButFinal(page);
  await expect(page.getByText("Theory Recertification Modules")).toBeVisible();
  await capture(page, "06-modules-unlocked-final-ready");

  await page.getByRole("button", { name: "Open Module" }).click();
  await expect(page.getByText("Infection Control & PPE")).toBeVisible();
  await capture(page, "07-module-1-overview");

  await page.getByRole("button", { name: "Review Theory" }).click();
  await expect(page.getByText("Scope of Infection Control in LTC")).toBeVisible();
  await captureLessonCards(page);

  await page.getByRole("button", { name: "CE Modules", exact: true }).click();
  await page.getByRole("button", { name: "Open Module" }).click();
  await page.getByRole("button", { name: "Start Module 1 Assessment" }).click();
  await expect(page.getByText("Module 1 Knowledge Exam")).toBeVisible();
  await capture(page, "12-module-1-assessment-splash");

  await page.getByRole("button", { name: "Begin Assessment Exam" }).click();
  await expect(page.getByText("MODULE 1 ASSESSMENT")).toBeVisible();
  await capture(page, "13-module-1-assessment-quiz");

  await page.getByRole("button", { name: "CE Modules", exact: true }).click();
  await page.getByRole("button", { name: "Enter Final Assessment" }).click();
  await expect(page.getByText("Theory Competency Exam")).toBeVisible();
  await capture(page, "14-final-assessment-splash");

  await page.getByRole("button", { name: "Begin Course Final Exam" }).click();
  await expect(page.getByText("COURSE THEORY FINAL EXAM")).toBeVisible();
  await capture(page, "15-final-assessment-quiz");

  await answerFinalExam(page);
  await capture(page, "16-final-result-passed");

  await page.getByRole("button", { name: "Certificate Gate", exact: true }).click();
  await expect(page.getByText("Compliance Gates Cleared")).toBeVisible();
  await capture(page, "17-certificate-gate-ready");

  await page.getByRole("button", { name: "View Mock Certificate Preview" }).click();
  await expect(page.getByText("Certificate of Completion")).toBeVisible();
  await capture(page, "18-mock-certificate-preview");

  await page.getByRole("button", { name: "Clinical Hub", exact: true }).click();
  await expect(page.getByText("Clinical Scenario Support Hub")).toBeVisible();
  await capture(page, "19-clinical-hub");
});
