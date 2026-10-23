// Run: mongosh --file crud-basics.js  (after seed.js)
db = db.getSiblingDB("campus");

// CREATE
const res = db.students.insertOne({ name: "Ayesha Noor", city: "Karachi", age: 19, batch: "T4-B",
  marks: { react: 70, node: 66, mongo: 81 }, skills: ["react"], fee: 40000, active: true, joined: new Date() });
print("New id:", res.insertedId);

// READ
printjson(db.students.find({ city: "Karachi" }, { name: 1, age: 1, _id: 0 }).toArray());
printjson(db.students.findOne({ name: "Hira Khan" }));
print("Active students:", db.students.countDocuments({ active: true }));

// UPDATE
db.students.updateOne({ name: "Usman Ali" }, { $set: { active: true, city: "Hyderabad" } });
db.students.updateMany({ batch: "T4-B" }, { $set: { room: "Lab 3" } });

// DELETE
db.students.deleteOne({ name: "Ayesha Noor" });
print("Remaining:", db.students.countDocuments());
