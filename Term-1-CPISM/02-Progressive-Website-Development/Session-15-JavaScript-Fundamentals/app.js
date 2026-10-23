// ---------- 1. Variables, types and output ----------
const institute = "Tech Academy";
let year = 2026;
console.log(`Welcome to ${institute}, ${year}!`);
console.log(typeof institute, typeof year, typeof true, typeof null); // string number boolean object
console.log("Line one\nLine two\t(tabbed) and a \"quote\"");

// ---------- 2. Decision making ----------
function getGrade(marks) {
  if (marks >= 80) return "A";
  else if (marks >= 65) return "B";
  else if (marks >= 50) return "C";
  return "F";
}

const marksInput = document.querySelector("#marks");
const result = document.querySelector("#result");

document.querySelector("#checkBtn").addEventListener("click", () => {
  const marks = Number(marksInput.value);
  if (marksInput.value === "" || isNaN(marks) || marks < 0 || marks > 100) {
    result.textContent = "Please enter a number from 0 to 100.";
    result.className = "fail";
    return;
  }
  const grade = getGrade(marks);
  const status = grade === "F" ? "Fail" : "Pass";     // ternary operator
  result.textContent = `Marks: ${marks} → Grade ${grade} (${status})`;
  result.className = status === "Pass" ? "pass" : "fail";

  switch (grade) {
    case "A": console.log("Excellent!"); break;
    case "B": console.log("Very good"); break;
    default:  console.log("Keep practising");
  }
});

// ---------- 3. Regular expression + input event ----------
const phonePattern = /^03\d{2}-\d{7}$/;
document.querySelector("#phone").addEventListener("input", (event) => {
  const ok = phonePattern.test(event.target.value);
  const msg = document.querySelector("#phoneMsg");
  msg.textContent = ok ? " ✔ valid" : " ✖ format 03XX-XXXXXXX";
  msg.className = ok ? "pass" : "fail";
});

// ---------- 4. Arrays and loops ----------
const students = ["Ayesha", "Hamza", "Fatima", "Daniyal", "Zara"];
const scores   = [86, 45, 91, 0, 77];          // 0 = absent

document.querySelector("#reportBtn").addEventListener("click", () => {
  let lines = [];
  let total = 0, counted = 0;

  for (let i = 0; i < students.length; i++) {
    if (scores[i] === 0) {               // skip absent students
      lines.push(`${students[i]}: absent`);
      continue;
    }
    total += scores[i];
    counted++;
    lines.push(`${students[i]}: ${scores[i]} (${getGrade(scores[i])})`);
  }

  const passed = scores.filter(s => s >= 50).length;
  const average = (total / counted).toFixed(1);
  lines.push(`Average: ${average} | Passed: ${passed}`);
  document.querySelector("#report").innerHTML = lines.map(l => `<div>${l}</div>`).join("");
});

// while and do...while
let countdown = 3;
while (countdown > 0) { console.log("while:", countdown); countdown--; }
let tries = 0;
do { tries++; } while (tries < 1);   // runs once even though the condition is false afterwards
console.log("do...while ran", tries, "time(s)");

// for...of and for...in
for (const name of students) { if (name === "Fatima") { console.log("Found Fatima"); break; } }
const course = { title: "PWD", sessions: 20, online: true };
for (const key in course) console.log(`${key} = ${course[key]}`);

// ---------- 5. Multi-dimensional array: times table ----------
const table = [];
for (let r = 1; r <= 5; r++) {
  const row = [];
  for (let c = 1; c <= 5; c++) row.push(r * c);
  table.push(row);
}
console.log("table[2][3] =", table[2][3]); // 3 x 4 = 12
document.querySelector("#table").innerHTML =
  "<table>" + table.map(row => "<tr>" + row.map(v => `<td>${v}</td>`).join("") + "</tr>").join("") + "</table>";
