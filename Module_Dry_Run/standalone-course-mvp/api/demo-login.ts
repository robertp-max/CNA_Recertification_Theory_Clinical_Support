export default async function handler(request: any, response: any) {
  if (request.method !== "POST") {
    response.setHeader("Allow", "POST");
    response.status(405).json({ ok: false, message: "Method not allowed" });
    return;
  }

  if (process.env.DEMO_LOGIN_ENABLED === "false") {
    response.status(403).json({ ok: false, message: "Demo login is disabled." });
    return;
  }

  let body: Record<string, unknown> = {};
  try {
    body = typeof request.body === "string" ? JSON.parse(request.body || "{}") : request.body || {};
  } catch {
    body = {};
  }
  const email = String(body.email || "").trim().toLowerCase();
  const password = String(body.password || "");
  const expectedEmail = String(process.env.DEMO_LOGIN_EMAIL || "admin@careindeed.com").trim().toLowerCase();
  const expectedPassword = String(process.env.DEMO_LOGIN_PASSWORD || "Caregiver2012!");

  if (email && password && email === expectedEmail && password === expectedPassword) {
    response.status(200).json({ ok: true, displayName: "Stakeholder Reviewer", email: expectedEmail });
    return;
  }

  response.status(401).json({ ok: false, message: "Invalid demo credentials." });
}
