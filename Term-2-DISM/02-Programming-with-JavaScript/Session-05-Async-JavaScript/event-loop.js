// Run: node event-loop.js   — predict the order BEFORE running!
console.log("1: script start");

setTimeout(() => console.log("6: setTimeout (macrotask)"), 0);

Promise.resolve()
  .then(() => console.log("3: promise then (microtask)"))
  .then(() => console.log("4: second then (microtask)"));

queueMicrotask(() => console.log("3b: queueMicrotask"));

(async () => {
  console.log("2: inside async function (sync part)");
  await null;
  console.log("5: after await (microtask)");
})();

console.log("2b: script end");
