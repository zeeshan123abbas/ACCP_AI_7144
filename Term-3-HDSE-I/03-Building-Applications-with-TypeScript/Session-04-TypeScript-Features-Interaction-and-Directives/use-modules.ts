// use-modules.ts - import what another module exported
import { PASS_MARK, percentage } from "./math-utils";

const result = percentage(410, 500);
console.log("Percentage:", result);
console.log(result >= PASS_MARK ? "Passed" : "Failed");
