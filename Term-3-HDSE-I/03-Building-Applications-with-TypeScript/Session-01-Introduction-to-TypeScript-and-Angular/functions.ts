// functions.ts - typed functions
export {}; // makes this file a module, so its variables stay private to it

// Parameters and the return value have types
function add(a: number, b: number): number {
  return a + b;
}

// Optional parameter (?) and default parameter (= value)
function greet(name: string, city?: string, greeting: string = "Hello"): string {
  if (city) {
    return `${greeting} ${name} from ${city}`;
  }
  return `${greeting} ${name}`;
}

// Arrow function: a short way to write a function
const square = (n: number): number => n * n;

// A function that returns nothing uses the type void
function logLine(message: string): void {
  console.log("-> " + message);
}

logLine(String(add(10, 5)));          // -> 15
logLine(greet("Sara"));                // -> Hello Sara
logLine(greet("Ali", "Karachi"));      // -> Hello Ali from Karachi
logLine(greet("Omar", undefined, "Hi")); // -> Hi Omar
logLine(String(square(7)));            // -> 49
