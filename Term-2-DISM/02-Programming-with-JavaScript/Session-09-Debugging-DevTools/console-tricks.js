const students = [
  { name: "Ali", marks: 78 },
  { name: "Sara", marks: 91 },
  { name: "Omar", marks: 45 }
];

console.table(students);

console.group("Results");
students.forEach(s => {
  console.count("checked");
  console.assert(s.marks >= 50, `${s.name} failed with ${s.marks}`);
});
console.groupEnd();

console.time("sort");
const sorted = [...students].sort((a, b) => b.marks - a.marks);
console.timeEnd("sort");

function level3() { console.trace("Who called me?"); }
function level2() { level3(); }
level2();

console.warn("This is a warning");
console.error("This is an error (not a crash)");
console.log("Top student:", sorted[0].name);
