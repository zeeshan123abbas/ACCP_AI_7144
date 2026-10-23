# Session 08: Practice Lab: Indexes and Replica Sets

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Session 7. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Diagnose slow queries with explain()
- Design compound indexes
- Verify uniqueness and TTL behaviour
- Operate a replica set

## 📖 Concepts Explained

### Tasks

| # | Task |
|---|---|
| 1 | Use `bigdata` from Session 7. Find users from Quetta with score > 80 sorted by age; record examined docs |
| 2 | Create the best compound index for task 1 and re-check |
| 3 | Find an index that is never used with `$indexStats` and drop it |
| 4 | Create a TTL index of 60 seconds on a `otp` collection and watch documents disappear (TTL monitor runs every ~60 s) |
| 5 | In the replica set, insert with `writeConcern: { w: "majority" }` |

## 💻 Code Examples

### Example 1: Solution script

📄 File: [`solution.js`](solution.js)

```js
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
```

**How it works**

- Equality (`city`), then sort (`age`), then range (`score`) removes the in-memory sort.
- `$indexStats` reveals unused indexes that only slow down writes.
- TTL deletion is done by a background task, so it is not instant.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Complete tasks 1-5.
2. Compare an index `{ city: 1, score: 1, age: 1 }` with the ESR version and explain the difference.
3. Hide an index with `hideIndex` to test impact before dropping it.

## 📝 Assignment

Profile three slow queries on any dataset you create (100k+ documents): show `explain()` before/after, the index you added, and a short conclusion on write-performance trade-offs.

## ❓ Quick Quiz

**Q1.** Which stage shows how often each index is used?

**Q2.** How often does the TTL monitor run?

**Q3.** What does `w: "majority"` guarantee?

**Q4.** Why drop unused indexes?

**Q5.** What does `hideIndex` do?

<details>
<summary>Show answers</summary>

1. `$indexStats`
2. About every 60 seconds.
3. Acknowledgement after a majority of voting members have the write.
4. They cost storage and slow writes without helping reads.
5. Makes the planner ignore an index without deleting it.

</details>

## 💼 Interview Questions

**1. How can an index cover a query?**

> If all filtered and returned fields are in the index (and `_id` is excluded), MongoDB answers from the index alone.

**2. What happens to writes during an election?**

> Writes fail briefly until a new primary is elected; drivers with retryable writes retry automatically.

**3. How many indexes are too many?**

> There is no fixed number; each must serve real queries. Monitor with `$indexStats` and write latency.

## ✅ Summary

- Measure, index, re-measure.
- Order compound index fields by ESR.
- Use majority write concern for important data.

---

[⬅ Previous](../Session-07-MongoDB-Indexing-Replication-and-Sharding/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-09-Transaction-Management-and-MongoDB-Tools/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
