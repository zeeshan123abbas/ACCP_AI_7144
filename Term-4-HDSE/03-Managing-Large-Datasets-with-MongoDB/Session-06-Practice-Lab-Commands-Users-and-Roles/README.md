# Session 06: Practice Lab: Commands, Users and Roles

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Session 5. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Use diagnostic commands to inspect a database
- Apply schema validation
- Design least-privilege roles
- Manage user lifecycle

## 📖 Concepts Explained

### Tasks

| # | Task |
|---|---|
| 1 | Show the size of each collection in `campus` in KB |
| 2 | Create a validated `attendance` collection (`student` string, `date` date, `present` bool) |
| 3 | Create role `attendanceClerk`: insert + find on `attendance` only |
| 4 | Create user `clerk1` with that role; change its password; then drop it |
| 5 | List all distinct batches and the number of active students per batch using commands |

## 💻 Code Examples

### Example 1: Solution script

📄 File: [`solution.js`](solution.js)

```js
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
```

**How it works**

- `$collStats` gives storage details per collection.
- The role is created only if it does not exist, so the script can be re-run.
- Passwords appear in plain text here only for a disposable lab user; use `passwordPrompt()` in real work.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Complete tasks 1-5.
2. Enable authorization locally, connect as a limited user and test what is denied.
3. Write down which built-in role you would give a backup operator and why.

## 📝 Assignment

Design the security model for a small e-commerce database: list collections, define three custom roles in a table, write the script that creates them and two users, and explain each privilege choice.

## ❓ Quick Quiz

**Q1.** Which stage returns collection storage statistics?

**Q2.** Which method changes a user's password?

**Q3.** Where must authorization be enabled for users to matter?

**Q4.** What does a validator do with invalid inserts by default?

**Q5.** Which command lists unique values of a field?

<details>
<summary>Show answers</summary>

1. `$collStats`
2. `db.changeUserPassword()`
3. In the mongod configuration (`security.authorization: enabled`).
4. Rejects them with an error.
5. `distinct`

</details>

## 💼 Interview Questions

**1. How would you rotate a database password used by an app?**

> Create the new password, update the app's secret store/env, redeploy, verify, then remove the old one.

**2. What is `validationLevel: moderate`?**

> Validation applies to inserts and to updates of documents that already satisfy the schema.

**3. Why not give an application the root role?**

> A bug or leak would expose full control of the cluster.

## ✅ Summary

- Diagnostic commands reveal sizes and server health.
- Validators enforce structure.
- Custom roles implement least privilege.

---

[⬅ Previous](../Session-05-Database-Commands-and-MongoDB-Shell-Methods/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-07-MongoDB-Indexing-Replication-and-Sharding/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
