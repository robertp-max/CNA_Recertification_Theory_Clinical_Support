const path = require("node:path");

const designFile = path
  .resolve(__dirname, "../CNA-Recert-Course/MVP/UIUX/v2.tsx")
  .replace(/\\/g, "/");

module.exports = {
  content: ["./v2-screenshot.html", "./src/v2-screenshot-runner.tsx", designFile],
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
};
