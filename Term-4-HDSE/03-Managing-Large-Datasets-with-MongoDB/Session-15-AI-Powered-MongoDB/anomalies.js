// mongosh --file anomalies.js
db = db.getSiblingDB("campus");
db.payments.drop();
const amounts = [4500, 4700, 4400, 4600, 4550, 4800, 4650, 45000, 4500, 4720, 300, 4610];
db.payments.insertMany(amounts.map((a, i) => ({ student: `S${i + 1}`, amount: a, at: new Date() })));

const [stats] = db.payments.aggregate([{ $group: { _id: null, mean: { $avg: "$amount" }, sd: { $stdDevPop: "$amount" } } }]).toArray();
print(`mean=${stats.mean.toFixed(0)} sd=${stats.sd.toFixed(0)}`);

printjson(db.payments.aggregate([
  { $addFields: { z: { $divide: [{ $subtract: ["$amount", stats.mean] }, stats.sd] } } },
  { $match: { $expr: { $gt: [{ $abs: "$z" }, 2] } } },
  { $project: { _id: 0, student: 1, amount: 1, z: { $round: ["$z", 2] } } }
]).toArray());
