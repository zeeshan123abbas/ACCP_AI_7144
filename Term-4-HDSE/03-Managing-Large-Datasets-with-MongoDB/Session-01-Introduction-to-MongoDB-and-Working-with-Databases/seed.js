// Seed data used across this module. Run: mongosh --file seed.js
db = db.getSiblingDB("campus");
db.students.drop();
db.students.insertMany([
  { name: "Ali Raza",   city: "Karachi",   age: 21, batch: "T4-A", marks: { react: 82, node: 74, mongo: 90 }, skills: ["react", "node"], fee: 45000, active: true },
  { name: "Hira Khan",  city: "Lahore",    age: 23, batch: "T4-A", marks: { react: 65, node: 88, mongo: 70 }, skills: ["node", "mongo", "azure"], fee: 45000, active: true },
  { name: "Usman Ali",  city: "Karachi",   age: 20, batch: "T4-B", marks: { react: 45, node: 52, mongo: 38 }, skills: ["react"], fee: 40000, active: false },
  { name: "Sana Malik", city: "Islamabad", age: 22, batch: "T4-B", marks: { react: 91, node: 79, mongo: 85 }, skills: ["react", "mongo"], fee: 40000, active: true },
  { name: "Bilal Ahmed",city: "Karachi",   age: 24, batch: "T4-A", marks: { react: 58, node: 61, mongo: 77 }, skills: ["azure", "node"], fee: 45000, active: true }
]);
print(`Inserted ${db.students.countDocuments()} students into campus.students`);
