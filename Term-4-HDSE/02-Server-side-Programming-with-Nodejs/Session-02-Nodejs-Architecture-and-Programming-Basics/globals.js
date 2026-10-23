// Run: APP_MODE=dev node globals.js   (Windows PowerShell: $env:APP_MODE="dev"; node globals.js)
console.log("Mode:", process.env.APP_MODE ?? "not set");
console.log("This file:", import.meta.filename);   // Node 20.11+
console.log("This folder:", import.meta.dirname);
console.log("Memory used (MB):", (process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2));

console.time("loop");
let total = 0;
for (let i = 0; i < 1e6; i++) total += i;
console.timeEnd("loop");

setTimeout(() => console.log("2. setTimeout after 0 ms"), 0);
setImmediate(() => console.log("3. setImmediate"));
console.log("1. synchronous code runs first");
