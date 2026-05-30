import { describe, it, expect } from "vitest";
import { createElement } from "react";
import { renderToStaticMarkup } from "react-dom/server";
import { reviewerCredentials } from "../auth";
import { PhiWarningBlock } from "../../components/ui/PhiWarningBlock";

describe("guardrails", () => {
  it("approved login credentials are unchanged (admin / 1234)", () => {
    expect(reviewerCredentials).toEqual({ username: "admin", password: "1234" });
  });

  it("PHI warning component renders the mandated, non-dismissible copy", () => {
    const html = renderToStaticMarkup(createElement(PhiWarningBlock));
    expect(html).toContain("STOP:");
    expect(html).toContain("Protected Health Information");
    expect(html).toContain("simulated case data only");
  });
});
