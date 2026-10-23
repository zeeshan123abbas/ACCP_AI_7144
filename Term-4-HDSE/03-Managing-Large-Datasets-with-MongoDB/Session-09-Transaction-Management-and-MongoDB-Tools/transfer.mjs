// npm install mongodb   then: node transfer.mjs
import { MongoClient } from "mongodb";

const client = new MongoClient(process.env.MONGODB_URI || "mongodb://localhost:27018,localhost:27019,localhost:27020/?replicaSet=rs0");
await client.connect();
const accounts = client.db("bank").collection("accounts");

async function transfer(from, to, amount) {
  const session = client.startSession();
  try {
    for (let attempt = 1; attempt <= 3; attempt++) {
      session.startTransaction({ writeConcern: { w: "majority" } });
      try {
        const res = await accounts.updateOne({ _id: from, balance: { $gte: amount } }, { $inc: { balance: -amount } }, { session });
        if (res.modifiedCount === 0) throw new Error("Insufficient balance");
        await accounts.updateOne({ _id: to }, { $inc: { balance: amount } }, { session });
        await session.commitTransaction();
        return "committed";
      } catch (err) {
        await session.abortTransaction().catch(() => {});
        if (err.hasErrorLabel?.("TransientTransactionError") && attempt < 3) continue; // retry whole transaction
        throw err;
      }
    }
  } finally {
    await session.endSession();
  }
}

console.log(await transfer("A", "B", 500));
await client.close();
