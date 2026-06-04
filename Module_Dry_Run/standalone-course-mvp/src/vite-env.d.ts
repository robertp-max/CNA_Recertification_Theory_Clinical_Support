/// <reference types="vite/client" />

declare module "/@fs/*" {
  import type { ComponentType } from "react";

  const component: ComponentType;
  export default component;
}
