# Session 12: Practice Lab: MongoDB Atlas

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Session 11. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Deploy and secure an Atlas cluster
- Migrate data both ways
- Query sample datasets
- Monitor a cluster

## 📖 Concepts Explained

### Tasks

| # | Task |
|---|---|
| 1 | Load the sample dataset; find the 5 highest-rated movies after 2010 in `sample_mflix` |
| 2 | Count Airbnb listings per country in `sample_airbnb.listingsAndReviews` |
| 3 | Create user `analyst` with read-only role on `sample_mflix` |
| 4 | Restore your local `campus` into Atlas and compare counts |
| 5 | Note three metrics from the cluster's Metrics tab |

## 💻 Code Examples

### Example 1: Solution queries

📄 File: [`solution.js`](solution.js)

```js
// mongosh "mongodb+srv://<cluster>/" --username <user> --file solution.js
const mflix = db.getSiblingDB("sample_mflix");
printjson(mflix.movies.find(
  { year: { $gt: 2010 }, "imdb.rating": { $type: "number" }, "imdb.votes": { $gt: 10000 } },
  { _id: 0, title: 1, year: 1, "imdb.rating": 1 }
).sort({ "imdb.rating": -1 }).limit(5).toArray());

const airbnb = db.getSiblingDB("sample_airbnb");
printjson(airbnb.listingsAndReviews.aggregate([
  { $group: { _id: "$address.country", listings: { $sum: 1 }, avgPrice: { $avg: { $toDouble: "$price" } } } },
  { $project: { listings: 1, avgPrice: { $round: ["$avgPrice", 0] } } },
  { $sort: { listings: -1 } }
]).toArray());
// Task 3 is done in the Atlas UI: Database Access -> Add New Database User -> Built-in role "read" on sample_mflix
```

**How it works**

- `$type: "number"` skips documents where the rating is missing or text.
- The Airbnb `price` is Decimal128, converted with `$toDouble` before averaging.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Complete tasks 1-5.
2. Connect Compass to Atlas and build task 2 visually.
3. Try connecting from a non-allowed IP (e.g. mobile hotspot) and note the error.

## 📝 Assignment

Create a small **movie explorer** script (Node or Python) that connects to Atlas and prints the top 10 movies for a genre given as a command-line argument, using an index you created for that query.

## ❓ Quick Quiz

**Q1.** Which database holds the movie sample data?

**Q2.** Why convert price with `$toDouble`?

**Q3.** Where do you create Atlas users?

**Q4.** What happens when your IP is not allowed?

**Q5.** Can Compass connect to Atlas?

<details>
<summary>Show answers</summary>

1. `sample_mflix`
2. It is stored as Decimal128; conversion makes averaging/rounding straightforward.
3. Database Access (Security section).
4. Connection times out / is refused.
5. Yes, with the cluster's connection string.

</details>

## 💼 Interview Questions

**1. How would you give an app and a human analyst different access?**

> Separate database users with different roles (readWrite for app, read for analyst), ideally separate projects or IP rules.

**2. What is Atlas Data Federation?**

> A feature that queries data across Atlas clusters and cloud object storage with MQL.

**3. How do you scale an Atlas cluster?**

> Change tier or storage in the UI/API, enable auto-scaling, or shard on dedicated tiers.

## ✅ Summary

- Sample datasets are great practice data.
- Separate users by role.
- Always verify migrations with counts.

---

[⬅ Previous](../Session-11-MongoDB-Cloud-with-Atlas/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-13-MongoDB-Connectivity-with-Python/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
