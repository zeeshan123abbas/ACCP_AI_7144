// Needs a replica set or Atlas (transactions do not run on a standalone server)
const session = db.getMongo().startSession();
const bank = session.getDatabase("bank");
db.getSiblingDB("bank").accounts.drop();
db.getSiblingDB("bank").accounts.insertMany([{ _id: "A", owner: "Ali", balance: 10000 }, { _id: "B", owner: "Sana", balance: 2000 }]);

function transfer(from, to, amount) {
  session.withTransaction(() => {
    const src = bank.accounts.findOne({ _id: from });
    if (src.balance < amount) throw new Error("Insufficient balance");
    bank.accounts.updateOne({ _id: from }, { $inc: { balance: -amount } });
    bank.accounts.updateOne({ _id: to }, { $inc: { balance: amount } });
    bank.transfers.insertOne({ from, to, amount, at: new Date() });
  }, { readConcern: { level: "snapshot" }, writeConcern: { w: "majority" } });
}

transfer("A", "B", 3000);
try { transfer("B", "A", 999999); } catch (e) { print("Rolled back:", e.message); }
printjson(db.getSiblingDB("bank").accounts.find().toArray());
session.endSession();
