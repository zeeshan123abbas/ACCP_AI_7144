db = db.getSiblingDB("shop");
db.products.drop();
db.products.insertMany([
  { name: "Galaxy A15", category: "mobile", price: 42000, qty: 12, inStock: true },
  { name: "Redmi 13C", category: "mobile", price: 31000, qty: 0, inStock: false },
  { name: "USB Cable", category: "accessory", price: 650, qty: 200, inStock: true },
  { name: "Power Bank", category: "accessory", price: 4200, qty: 35, inStock: true },
  { name: "ThinkPad E14", category: "laptop", price: 215000, qty: 4, inStock: true },
  { name: "Earbuds", category: "accessory", price: 3500, qty: 0, inStock: false },
  { name: "iPhone 15", category: "mobile", price: 289000, qty: 3, inStock: true },
  { name: "Mouse", category: "accessory", price: 1200, qty: 60, inStock: true }
]);
print("Task 2:"); printjson(db.products.find({ price: { $lt: 5000 } }, { _id: 0, name: 1, price: 1 }).toArray());
print("Task 3:"); printjson(db.products.find({ category: "mobile", inStock: true }, { _id: 0, name: 1 }).toArray());
db.products.updateMany({}, { $rename: { qty: "stock" } });
const r = db.products.deleteMany({ stock: 0 });
print("Task 5 deleted:", r.deletedCount, "remaining:", db.products.countDocuments());
// Task 6 (run in a normal terminal, not mongosh):
// mongoexport --db shop --collection products --out products-export.json --jsonArray
