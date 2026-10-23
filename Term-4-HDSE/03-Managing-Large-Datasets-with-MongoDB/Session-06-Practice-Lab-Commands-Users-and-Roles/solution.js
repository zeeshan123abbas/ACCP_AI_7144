db = db.getSiblingDB("campus");
for (const name of db.getCollectionNames()) {
  const s = db.getCollection(name).aggregate([{ $collStats: { storageStats: { scale: 1024 } } }]).next();
  print(`${name}: ${s.storageStats.size} KB data, ${s.storageStats.count} docs`);
}

db.attendance.drop();
db.createCollection("attendance", { validator: { $jsonSchema: {
  bsonType: "object", required: ["student", "date", "present"],
  properties: { student: { bsonType: "string" }, date: { bsonType: "date" }, present: { bsonType: "bool" } } } } });
db.attendance.insertOne({ student: "Ali Raza", date: new Date(), present: true });

if (!db.getRole("attendanceClerk")) {
  db.createRole({ role: "attendanceClerk", roles: [],
    privileges: [{ resource: { db: "campus", collection: "attendance" }, actions: ["insert", "find"] }] });
}
db.createUser({ user: "clerk1", pwd: "Temp#Pass2026", roles: ["attendanceClerk"] });
db.changeUserPassword("clerk1", "New#Pass2026");
db.dropUser("clerk1");

printjson(db.runCommand({ distinct: "students", key: "batch" }).values);
printjson(db.students.aggregate([{ $match: { active: true } }, { $group: { _id: "$batch", active: { $sum: 1 } } }]).toArray());
