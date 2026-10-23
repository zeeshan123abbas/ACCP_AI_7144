// Setup: npm init -y && npm install ajv
// Run:   node validate.js
const Ajv2020 = require("ajv/dist/2020");
const schema = require("./product.schema.json");

const ajv = new Ajv2020({ allErrors: true });
const validate = ajv.compile(schema);

const samples = [
  { sku: "TZ-1001", name: "Wireless Mouse", price: 1500, inStock: true, category: "accessory" },
  { sku: "1001", name: "TV", price: -5, inStock: "yes", color: "black" }
];

for (const item of samples) {
  if (validate(item)) {
    console.log(`VALID   -> ${item.name}`);
  } else {
    console.log(`INVALID -> ${item.name}`);
    validate.errors.forEach(e => console.log(`   ${e.instancePath || "(root)"} ${e.message}`));
  }
}
