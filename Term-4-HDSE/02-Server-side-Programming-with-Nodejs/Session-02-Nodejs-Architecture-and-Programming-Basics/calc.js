// Run: node calc.js 12 + 5
const [, , a, op, b] = process.argv;
const x = Number(a);
const y = Number(b);

if (Number.isNaN(x) || Number.isNaN(y)) {
  console.error("Usage: node calc.js <number> <+|-|x|/> <number>");
  process.exit(1);
}

let result;
switch (op) {
  case "+": result = x + y; break;
  case "-": result = x - y; break;
  case "x": result = x * y; break;
  case "/": result = y === 0 ? "cannot divide by zero" : x / y; break;
  default:
    console.error(`Unknown operator: ${op}`);
    process.exit(1);
}
console.log(`${x} ${op} ${y} = ${result}`);
