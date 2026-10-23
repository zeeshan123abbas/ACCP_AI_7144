// src/report.js — imagine this file is large (charts, PDF generation...)
const sales = [
  { month: "Jan", amount: 120000 },
  { month: "Feb", amount: 98000 },
  { month: "Mar", amount: 143500 }
];

export function buildReport() {
  const total = sales.reduce((s, r) => s + r.amount, 0);
  const lines = sales.map(r => `${r.month}: ${"█".repeat(Math.round(r.amount / 10000))} ${r.amount}`);
  return [...lines, `Total: ${total}`].join("\n");
}

export function unusedExport() {
  return "tree shaking removes me";
}
