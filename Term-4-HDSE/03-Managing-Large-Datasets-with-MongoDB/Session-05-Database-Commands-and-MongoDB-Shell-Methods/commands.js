db = db.getSiblingDB("campus");

printjson(db.runCommand({ ping: 1 }));
printjson(db.runCommand({ dbStats: 1, scale: 1024 }));           // sizes in KB
print("Server version:", db.version());
print("Collections:", db.getCollectionNames().join(", "));
printjson(db.runCommand({ distinct: "students", key: "city" }));
printjson(db.runCommand({ count: "students", query: { active: true } }));

// capped collection for logs (max 1 MB or 1000 docs)
db.logs.drop();
db.createCollection("logs", { capped: true, size: 1024 * 1024, max: 1000 });
db.logs.insertOne({ level: "info", msg: "Server started", at: new Date() });

// collection with schema validation
db.feedback.drop();
db.createCollection("feedback", {
  validator: { $jsonSchema: {
    bsonType: "object", required: ["student", "rating"],
    properties: { student: { bsonType: "string" }, rating: { bsonType: "int", minimum: 1, maximum: 5 } } } }
});
db.feedback.insertOne({ student: "Ali", rating: NumberInt(5) });
try { db.feedback.insertOne({ student: "Sana", rating: NumberInt(9) }); }
catch (e) { print("Rejected by validator:", e.message); }

// bulkWrite: several operations in one round trip
printjson(db.students.bulkWrite([
  { updateOne: { filter: { name: "Ali Raza" }, update: { $set: { mentor: true } } } },
  { deleteMany: { filter: { active: false } } }
]));
