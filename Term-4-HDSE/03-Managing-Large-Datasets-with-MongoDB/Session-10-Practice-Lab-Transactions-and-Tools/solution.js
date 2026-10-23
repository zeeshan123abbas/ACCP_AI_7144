// Run on a replica set
const shop = db.getSiblingDB("shoplab");
shop.inventory.drop(); shop.sales.drop();
shop.inventory.insertMany([{ _id: "pen", stock: 50 }, { _id: "notebook", stock: 5 }]);
shop.createCollection("sales"); // create before the transaction

const session = db.getMongo().startSession();
const s = session.getDatabase("shoplab");

function sell(product, qty) {
  try {
    session.withTransaction(() => {
      const r = s.inventory.updateOne({ _id: product, stock: { $gte: qty } }, { $inc: { stock: -qty } });
      if (r.modifiedCount !== 1) throw new Error(`Not enough ${product}`);
      s.sales.insertOne({ product, qty, at: new Date() });
    });
    print(`Sold ${qty} ${product}`);
  } catch (e) { print("Aborted:", e.message); }
}

[["pen", 10], ["notebook", 3], ["notebook", 4], ["pen", 5], ["notebook", 2]].forEach(([p, q]) => sell(p, q));
printjson(shop.inventory.find().toArray());
printjson(shop.sales.aggregate([{ $group: { _id: "$product", sold: { $sum: "$qty" } } }]).toArray());
session.endSession();
