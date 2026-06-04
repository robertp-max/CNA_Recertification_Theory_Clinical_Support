import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  timeout: 90_000,
  expect: {
    timeout: 10_000,
  },
  use: {
    baseURL: "http://127.0.0.1:5177",
    viewport: { width: 1440, height: 1100 },
    deviceScaleFactor: 1,
    colorScheme: "dark",
  },
  webServer: {
    command:
      "npx vite --config vite.v2-screenshot.config.ts --host 127.0.0.1 --port 5177",
    url: "http://127.0.0.1:5177/v2-screenshot.html",
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },
  ],
});
