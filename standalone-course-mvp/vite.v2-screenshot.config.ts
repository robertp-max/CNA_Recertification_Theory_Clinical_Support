import path from "node:path";
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

const projectRoot = path.resolve(".");
const fromNodeModules = (...parts: string[]) =>
  path.resolve(projectRoot, "node_modules", ...parts);

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      react: fromNodeModules("react"),
      "react-dom": fromNodeModules("react-dom"),
      "lucide-react": fromNodeModules(
        "lucide-react",
        "dist",
        "esm",
        "lucide-react.js",
      ),
    },
    dedupe: ["react", "react-dom"],
  },
  server: {
    host: "127.0.0.1",
    fs: {
      allow: [path.resolve("."), path.resolve("..")],
    },
  },
});
