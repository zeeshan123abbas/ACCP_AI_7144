// Run: node parallel.js
const wait = (ms, value, fail = false) =>
  new Promise((resolve, reject) => setTimeout(() => (fail ? reject(new Error(value)) : resolve(value)), ms));

async function sequential() {
  console.time("sequential");
  const a = await wait(500, "users");
  const b = await wait(500, "courses");
  console.timeEnd("sequential"); // ~1000 ms
  return [a, b];
}

async function parallel() {
  console.time("parallel");
  const result = await Promise.all([wait(500, "users"), wait(500, "courses")]);
  console.timeEnd("parallel");   // ~500 ms
  return result;
}

async function withTimeout(promise, ms) {
  const timeout = wait(ms, "Timed out", true);
  return Promise.race([promise, timeout]);
}

await sequential();
await parallel();

const settled = await Promise.allSettled([wait(100, "ok"), wait(100, "db down", true)]);
console.log(settled.map((r) => r.status)); // [ 'fulfilled', 'rejected' ]

try {
  await withTimeout(wait(2000, "slow API"), 300);
} catch (err) {
  console.log("Caught:", err.message);
}
