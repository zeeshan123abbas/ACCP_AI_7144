// Run: node grade-cli.js
import readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

function grade(marks) {
  if (marks >= 75) return "Distinction";
  if (marks >= 60) return "Credit";
  if (marks >= 40) return "Pass";
  return "Referred";
}

const results = [];
try {
  const count = Number(await rl.question("How many students? "));
  for (let i = 1; i <= count; i++) {
    const name = await rl.question(`Name of student ${i}: `);
    const marks = Number(await rl.question(`Marks of ${name}: `));
    results.push({ name, marks, grade: grade(marks) });
  }
  console.table(results);
} catch (err) {
  console.error("Something went wrong:", err.message);
} finally {
  rl.close();
}
