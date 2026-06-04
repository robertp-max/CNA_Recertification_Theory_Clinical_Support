/**
 * Tailwind for the authenticated V2 app surface only.
 * Preflight is DISABLED so global element resets never reach the approved,
 * frozen login screen (which uses its own scoped CSS). A scoped reset that
 * replicates the parts of preflight the V2 markup relies on (border defaults,
 * button/heading normalization) lives under `.v2-root` in styles/tailwind.css.
 */
module.exports = {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  corePlugins: {
    preflight: false,
  },
  theme: {
    extend: {
      colors: {
        stone: {
          850: "#1f1a1a",
          955: "#070404",
        },
      },
    },
  },
  plugins: [],
};
