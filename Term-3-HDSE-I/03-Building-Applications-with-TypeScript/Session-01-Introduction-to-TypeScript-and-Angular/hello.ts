// hello.ts - your first TypeScript program
export {}; // makes this file a module, so its variables stay private to it

// A variable with a type annotation: name can only hold text
let studentName: string = "Ayesha";

// TypeScript can also guess (infer) the type from the value
let sessionNumber = 1; // inferred as number

// Print a message using a template string
console.log(`Welcome ${studentName}! This is session ${sessionNumber}.`);

// Uncomment the next line and run "npx tsc hello.ts" to see a type error:
// sessionNumber = "one";
