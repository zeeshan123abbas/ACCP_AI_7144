// Run: node promises.js
const wait = (ms, value, fail = false) =>
  new Promise((resolve, reject) =>
    setTimeout(() => (fail ? reject(new Error(`${value} failed`)) : resolve(value)), ms)
  );

// 1. Callback style (for comparison)
function getUserCb(id, cb) {
  setTimeout(() => cb(null, { id, name: "Ali" }), 300);
}
getUserCb(1, (err, user) => {
  if (err) return console.error(err);
  console.log("callback:", user.name);
});

// 2. Promise chain
wait(300, "promise chain")
  .then(v => v.toUpperCase())
  .then(v => console.log(v))
  .catch(err => console.error(err.message));

// 3. async/await with sequential vs parallel timing
async function demo() {
  console.time("sequential");
  await wait(500, "A");
  await wait(500, "B");
  console.timeEnd("sequential"); // ~1000ms

  console.time("parallel");
  const [a, b] = await Promise.all([wait(500, "A"), wait(500, "B")]);
  console.timeEnd("parallel"); // ~500ms
  console.log("results:", a, b);

  const settled = await Promise.allSettled([wait(100, "ok"), wait(100, "bad", true)]);
  console.log(settled.map(s => s.status));

  const fastest = await Promise.any([wait(300, "slow"), wait(100, "fast")]);
  console.log("any:", fastest);

  try {
    await Promise.all([wait(100, "x"), wait(50, "y", true)]);
  } catch (err) {
    console.log("all() rejected:", err.message);
  }
}
demo();
