db = db.getSiblingDB("campus");

print("Average marks per city (active students):");
printjson(db.students.aggregate([
  { $match: { active: true } },
  { $addFields: { avg: { $avg: ["$marks.react", "$marks.node", "$marks.mongo"] } } },
  { $group: { _id: "$city", students: { $sum: 1 }, avgMark: { $avg: "$avg" }, names: { $push: "$name" } } },
  { $project: { _id: 0, city: "$_id", students: 1, avgMark: { $round: ["$avgMark", 1] }, names: 1 } },
  { $sort: { avgMark: -1 } }
]).toArray());

print("Grade per student:");
printjson(db.students.aggregate([
  { $project: {
      _id: 0,
      label: { $concat: [{ $toUpper: "$name" }, " (", "$batch", ")"] },
      mongo: "$marks.mongo",
      grade: { $switch: { branches: [
        { case: { $gte: ["$marks.mongo", 75] }, then: "Distinction" },
        { case: { $gte: ["$marks.mongo", 60] }, then: "Credit" },
        { case: { $gte: ["$marks.mongo", 40] }, then: "Pass" } ], default: "Referred" } } } }
]).toArray());

print("Most common skills:");
printjson(db.students.aggregate([
  { $unwind: "$skills" },
  { $group: { _id: "$skills", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 3 }
]).toArray());
