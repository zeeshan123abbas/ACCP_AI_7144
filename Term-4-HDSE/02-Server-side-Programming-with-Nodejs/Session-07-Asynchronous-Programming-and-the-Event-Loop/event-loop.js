// Run: node event-loop.js  - try to predict the order first!
import fs from "node:fs";

console.log("1 sync start");

setTimeout(() => console.log("6 timeout"), 0);
setImmediate(() => console.log("7 immediate"));

fs.readFile(import.meta.filename, () => {
  console.log("8 I/O callback");
  setTimeout(() => console.log("10 timeout inside I/O"), 0);
  setImmediate(() => console.log("9 immediate inside I/O (always before the timeout here)"));
});

Promise.resolve().then(() => console.log("4 promise microtask"));
process.nextTick(() => console.log("3 nextTick"));
queueMicrotask(() => console.log("5 queueMicrotask"));

console.log("2 sync end");
