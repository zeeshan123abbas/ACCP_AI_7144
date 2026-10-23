db = db.getSiblingDB("campus");
const q = { city: "Quetta", score: { $gt: 80 } };
let s = db.bigdata.find(q).sort({ age: 1 }).explain("executionStats").executionStats;
print("Before:", s.totalDocsExamined, "docs");
db.bigdata.createIndex({ city: 1, age: 1, score: 1 }, { name: "city_age_score" }); // E, S, R
s = db.bigdata.find(q).sort({ age: 1 }).explain("executionStats").executionStats;
print("After:", s.totalDocsExamined, "docs,", s.executionTimeMillis, "ms");

db.bigdata.aggregate([{ $indexStats: {} }]).forEach((i) => print(i.name, "used", i.accesses.ops, "times"));

db.otp.drop();
db.otp.createIndex({ createdAt: 1 }, { expireAfterSeconds: 60 });
db.otp.insertOne({ phone: "03001234567", code: "482913", createdAt: new Date() });
print("OTP docs now:", db.otp.countDocuments(), "- check again after ~2 minutes");

// Task 5 (when connected to the replica set):
// db.orders.insertOne({ item: "laptop" }, { writeConcern: { w: "majority", wtimeout: 5000 } });
