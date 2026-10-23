db = db.getSiblingDB("campus");
db.orders.drop();
const day = 24 * 60 * 60 * 1000, now = Date.now();
db.orders.insertMany([
  { customer: "Ali", city: "Karachi", status: "delivered", createdAt: new Date(now - 40 * day), items: [{ product: "Mouse", qty: 2, price: 1200 }, { product: "Cable", qty: 3, price: 650 }] },
  { customer: "Hira", city: "Lahore", status: "pending", createdAt: new Date(now - 10 * day), items: [{ product: "Keyboard", qty: 1, price: 5500 }] },
  { customer: "Sana", city: "Islamabad", status: "delivered", createdAt: new Date(now - 5 * day), items: [{ product: "Mouse", qty: 4, price: 1200 }] },
  { customer: "Bilal", city: "Karachi", status: "pending", createdAt: new Date(now - 2 * day), items: [{ product: "Monitor", qty: 1, price: 38000 }, { product: "Cable", qty: 1, price: 650 }] },
  { customer: "Zara", city: "Lahore", status: "delivered", createdAt: new Date(now - 1 * day), items: [{ product: "Cable", qty: 5, price: 650 }] }
]);
print("1"); printjson(db.orders.find({ city: { $in: ["Karachi", "Lahore"] }, status: "delivered" }, { _id: 0, customer: 1 }).toArray());
print("2"); printjson(db.orders.find({ items: { $elemMatch: { qty: { $gte: 3 } } } }, { _id: 0, customer: 1 }).toArray());
print("3"); printjson(db.orders.updateMany({ status: "pending", createdAt: { $lt: new Date(now - 7 * day) } }, { $set: { status: "cancelled" } }));
print("4"); printjson(db.orders.aggregate([
  { $match: { status: { $ne: "cancelled" } } }, { $unwind: "$items" },
  { $group: { _id: "$city", revenue: { $sum: { $multiply: ["$items.qty", "$items.price"] } } } },
  { $sort: { revenue: -1 } }]).toArray());
print("5"); printjson(db.orders.aggregate([
  { $unwind: "$items" }, { $group: { _id: "$items.product", sold: { $sum: "$items.qty" } } },
  { $sort: { sold: -1 } }, { $limit: 3 }]).toArray());
print("6"); printjson(db.orders.aggregate([
  { $group: { _id: { $dateToString: { format: "%Y-%m", date: "$createdAt" } }, orders: { $sum: 1 } } },
  { $sort: { _id: 1 } }]).toArray());
