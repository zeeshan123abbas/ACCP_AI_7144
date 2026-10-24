// loops-and-conditions.ts - the same constructs you know, now with types
export {}; // makes this file a module, so its variables stay private to it

const marks: number[] = [45, 72, 88, 39, 95];

// for...of loop: visit every value
for (const mark of marks) {
  // if / else if / else
  if (mark >= 80) {
    console.log(mark, "Excellent");
  } else if (mark >= 50) {
    console.log(mark, "Pass");
  } else {
    console.log(mark, "Fail");
  }
}

// switch statement
const day: string = "Sat";
switch (day) {
  case "Sat":
  case "Sun":
    console.log("Weekend class");
    break;
  default:
    console.log("Weekday class");
}
