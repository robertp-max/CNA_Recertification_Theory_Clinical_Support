import { defineConfig } from "vitest/config";

// Vitest runs the unit suite under src/. Playwright specs (the screenshot
// capture in tests/) use @playwright/test and are run separately via the
// screenshots:v2 script — they must not be collected here.
export default defineConfig({
  test: {
    include: ["src/**/*.{test,spec}.{ts,tsx}"],
  },
});
