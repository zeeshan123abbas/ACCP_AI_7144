// Run seed.js from Session 1 first
db = db.getSiblingDB("campus");

// Comparison + logical
printjson(db.students.find({ $or: [{ city: "Lahore" }, { age: { $gte: 23 } }] }, { _id: 0, name: 1, city: 1, age: 1 }).toArray());
// $in and nested field
printjson(db.students.find({ city: { $in: ["Karachi", "Islamabad"] }, "marks.mongo": { $gt: 80 } }, { _id: 0, name: 1 }).toArray());
// Array operators
printjson(db.students.find({ skills: { $all: ["react", "node"] } }, { _id: 0, name: 1 }).toArray());
printjson(db.students.find({ skills: { $size: 3 } }, { _id: 0, name: 1 }).toArray());
// Regex + $expr (compare two fields)
printjson(db.students.find({ name: { $regex: /^S/ } }, { _id: 0, name: 1 }).toArray());
printjson(db.students.find({ $expr: { $gt: ["$marks.node", "$marks.react"] } }, { _id: 0, name: 1 }).toArray());

// Update operators
db.students.updateOne({ name: "Ali Raza" }, { $inc: { "marks.react": 5 }, $push: { skills: "azure" } });
db.students.updateMany({}, { $addToSet: { skills: "git" } });          // no duplicates
db.students.updateOne({ name: "Hira Khan" }, { $pull: { skills: "azure" } });
db.students.updateMany({ active: false }, { $unset: { fee: "" }, $currentDate: { updatedAt: true } });
db.students.updateMany({ batch: "T4-B" }, { $mul: { fee: 0.9 } });      // 10% discount
printjson(db.students.find({}, { _id: 0, name: 1, skills: 1, fee: 1 }).toArray());
