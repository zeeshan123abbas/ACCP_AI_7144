// warmup.ts - TypeScript revision exercises (run: npx tsx warmup.ts)
export {}; // keep this file's variables private

// Exercise 1: a typed function that returns the larger of two numbers
function larger(a: number, b: number): number {
  return a > b ? a : b;
}
console.log("Larger:", larger(12, 30));

// Exercise 2: total of an array using a for...of loop
function total(values: number[]): number {
  let sum = 0;
  for (const value of values) {
    sum = sum + value;
  }
  return sum;
}
console.log("Total:", total([10, 20, 30]));

// Exercise 3: a union type parameter
function showId(id: string | number): string {
  if (typeof id === "number") {
    return "Numeric ID: " + id;
  }
  return "Text ID: " + id.toUpperCase();
}
console.log(showId(7));
console.log(showId("hdse-7"));

// Exercise 4: enum + switch
enum Level { Beginner, Intermediate, Advanced }
function describe(level: Level): string {
  switch (level) {
    case Level.Beginner: return "Start with the basics";
    case Level.Intermediate: return "Build real projects";
    default: return "Teach others!";
  }
}
console.log(describe(Level.Intermediate));
