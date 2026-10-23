// Run: node data-handling.js   (Node 21+ for Object.groupBy; Node 20 users can use the reduce version)
const orders = [
  { id: 1, customer: { name: "Ali", city: "Karachi" }, items: [{ p: "Mouse", qty: 2, price: 1500 }], paid: true },
  { id: 2, customer: { name: "Sara", city: "Lahore" }, items: [{ p: "Monitor", qty: 1, price: 52000 }], paid: false },
  { id: 3, customer: { name: "Omar" }, items: [{ p: "Keyboard", qty: 1, price: 8500 }, { p: "Pad", qty: 3, price: 600 }], paid: true },
  { id: 4, customer: null, items: [], paid: true }
];

// Destructuring with defaults inside a callback
const orderTotal = ({ items = [] }) => items.reduce((sum, { qty, price }) => sum + qty * price, 0);

// Pipeline: filter -> map -> reduce
const paid = orders.filter(o => o.paid && o.items.length);
const withTotals = paid.map(o => ({ ...o, total: orderTotal(o) }));
const revenue = withTotals.reduce((sum, o) => sum + o.total, 0);
console.log("Revenue:", revenue);

// Optional chaining + nullish coalescing for messy data
orders.forEach(o => {
  const city = o.customer?.city ?? "Unknown city";
  const name = o.customer?.name ?? "Walk-in";
  console.log(`#${o.id} ${name} - ${city}`);
});

// Grouping by city with reduce (works everywhere)
const byCity = orders.reduce((acc, o) => {
  const city = o.customer?.city ?? "Unknown";
  (acc[city] ??= []).push(o.id);
  return acc;
}, {});
console.log("Grouped:", byCity);

// Set for unique products, Map for counts
const products = orders.flatMap(o => o.items.map(i => i.p));
console.log("Unique products:", [...new Set(products)]);
const qtyMap = new Map();
orders.flatMap(o => o.items).forEach(({ p, qty }) => qtyMap.set(p, (qtyMap.get(p) ?? 0) + qty));
console.log("Quantities:", Object.fromEntries(qtyMap));

// Shallow vs deep copy
const shallow = { ...orders[0] };
const deep = structuredClone(orders[0]);
shallow.customer.city = "Hyderabad";
console.log("Original city after shallow edit:", orders[0].customer.city); // changed!
console.log("Deep copy city:", deep.customer.city);                        // still Karachi

// Non-mutating sort (ES2023)
console.log(withTotals.toSorted((a, b) => b.total - a.total).map(o => o.id));
