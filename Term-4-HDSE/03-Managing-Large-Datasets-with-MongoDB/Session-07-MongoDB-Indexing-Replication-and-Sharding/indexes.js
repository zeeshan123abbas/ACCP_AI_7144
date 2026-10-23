db = db.getSiblingDB("campus");
db.bigdata.drop();
const cities = ["Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar"];
const docs = [];
for (let i = 0; i < 50000; i++) {
  docs.push({ email: `user${i}@example.com`, city: cities[i % 5], age: 18 + (i % 30), score: i % 100, createdAt: new Date() });
}
db.bigdata.insertMany(docs);

const query = { city: "Lahore", age: { $gte: 25 } };
const before = db.bigdata.find(query).sort({ score: -1 }).explain("executionStats");
print("Before:", before.queryPlanner.winningPlan.stage, "docs examined:", before.executionStats.totalDocsExamined);

db.bigdata.createIndex({ city: 1, score: -1, age: 1 });   // ESR: equality, sort, range
db.bigdata.createIndex({ email: 1 }, { unique: true });
db.bigdata.createIndex({ createdAt: 1 }, { expireAfterSeconds: 7 * 24 * 3600, name: "ttl_week" });

const after = db.bigdata.find(query).sort({ score: -1 }).explain("executionStats");
print("After docs examined:", after.executionStats.totalDocsExamined, "keys examined:", after.executionStats.totalKeysExamined);
printjson(db.bigdata.getIndexes().map((i) => i.name));

try { db.bigdata.insertOne({ email: "user1@example.com" }); } catch (e) { print("Unique index blocked duplicate"); }
db.bigdata.dropIndex("ttl_week");
