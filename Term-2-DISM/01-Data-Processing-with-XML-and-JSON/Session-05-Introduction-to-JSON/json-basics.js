// Run: node json-basics.js
const fs = require("fs");

// 1. Deserialize: JSON text -> JS object
const text = fs.readFileSync("inventory.json", "utf8");
const data = JSON.parse(text);
console.log("Store:", data.store);
console.log("First product:", data.products[0].name);
console.log("Second supplier:", data.products[1].supplier.name);

// 2. Work with the data like any JS object
const available = data.products.filter(p => p.inStock);
const totalValue = available.reduce((sum, p) => sum + p.price, 0);
console.log(`In stock: ${available.length}, total value: Rs. ${totalValue}`);

// 3. Serialize: JS object -> JSON text (pretty printed)
const summary = { count: available.length, totalValue, generatedAt: new Date() };
const json = JSON.stringify(summary, null, 2);
console.log(json);
fs.writeFileSync("summary.json", json);

// 4. Replacer: keep only selected keys
console.log(JSON.stringify(data.products[0], ["sku", "price"]));

// 5. Reviver: turn ISO date strings back into Date objects
const revived = JSON.parse(text, (key, value) =>
  key === "updated" ? new Date(value) : value
);
console.log("Updated year:", revived.updated.getFullYear());

// 6. Always guard against bad JSON
try {
  JSON.parse("{ name: 'Ali' }"); // invalid: unquoted key, single quotes
} catch (err) {
  console.log("Invalid JSON ->", err.message);
}
