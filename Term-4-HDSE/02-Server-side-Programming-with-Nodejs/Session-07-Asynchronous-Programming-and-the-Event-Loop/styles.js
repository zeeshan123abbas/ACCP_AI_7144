// Run: node styles.js
import fs from "node:fs";
import { readFile } from "node:fs/promises";

const file = new URL("./sample.txt", import.meta.url);

// 1) Synchronous - blocks until done
const syncText = fs.readFileSync(file, "utf8");
console.log("SYNC:", syncText.trim());

// 2) Callback - error-first
fs.readFile(file, "utf8", (err, data) => {
  if (err) return console.error("Callback error:", err.message);
  console.log("CALLBACK:", data.trim());
});

// 3) Promise with then/catch
readFile(file, "utf8")
  .then((data) => console.log("PROMISE:", data.trim()))
  .catch((err) => console.error(err));

// 4) async/await
async function main() {
  try {
    const data = await readFile(file, "utf8");
    console.log("ASYNC/AWAIT:", data.trim());
  } catch (err) {
    console.error("Await error:", err.message);
  }
}
main();
console.log("This line prints right after SYNC - before the async results!");
