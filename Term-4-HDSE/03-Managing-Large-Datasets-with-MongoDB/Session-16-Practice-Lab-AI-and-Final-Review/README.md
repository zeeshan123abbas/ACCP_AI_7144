# Session 16: Practice Lab: AI-Powered MongoDB and Final Review

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Sessions 9 to 15 and the whole module. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Revise every major MongoDB topic
- Combine aggregation, indexes and Python in one task
- Use AI responsibly to speed up work
- Prepare for the modular and practical exams

## 📖 Concepts Explained

### 1. Module checklist

| Topic | Key skills |
|---|---|
| Basics | data types, CRUD, mongoimport/export |
| Operators | comparison, logical, array, update operators |
| Aggregation | `$match $group $project $unwind $lookup $sort` |
| Admin | commands, validators, users and roles |
| Performance | indexes, ESR, `explain()` |
| Scale | replica sets, sharding, shard keys |
| Transactions | sessions, `withTransaction`, error labels |
| Tools | Compass, BI Connector, Atlas |
| Python | PyMongo CRUD and aggregation |
| AI | safe NL queries, anomalies, Colab |

### 2. Capstone task

Build a **Student Performance Insights** script that:
1. seeds 200 student result documents,
2. creates a suitable compound index and shows `explain()` proof,
3. reports average and pass rate per module,
4. flags anomalous marks,
5. (optional) asks an AI to summarise the report numbers.

## 💻 Code Examples

### Example 1: Capstone solution

📄 File: [`solution.py`](solution.py)

```python
"""pip install pymongo   (optional: openai)   then python solution.py"""
import os
import random
from statistics import mean, pstdev

from pymongo import MongoClient

modules = ["React", "Node", "MongoDB", "Azure"]

with MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017")) as client:
    col = client.capstone.results
    col.drop()
    docs = [{"student": f"S{i:03d}", "module": random.choice(modules),
             "marks": max(0, min(100, int(random.gauss(65, 15))))} for i in range(200)]
    docs[7]["marks"] = 0  # injected anomaly
    col.insert_many(docs)

    col.create_index([("module", 1), ("marks", -1)])
    plan = col.find({"module": "React"}).sort("marks", -1).explain()
    print("Plan uses index:", "IXSCAN" in str(plan["queryPlanner"]["winningPlan"]))

    report = list(col.aggregate([
        {"$group": {"_id": "$module", "avg": {"$avg": "$marks"},
                    "passed": {"$sum": {"$cond": [{"$gte": ["$marks", 40]}, 1, 0]}}, "total": {"$sum": 1}}},
        {"$project": {"avg": {"$round": ["$avg", 1]}, "passRate": {"$round": [{"$multiply": [{"$divide": ["$passed", "$total"]}, 100]}, 1]}}},
        {"$sort": {"_id": 1}},
    ]))
    for r in report:
        print(f"{r['_id']:8} avg={r['avg']}  pass={r['passRate']}%")

    marks = [d["marks"] for d in col.find({}, {"marks": 1})]
    m, sd = mean(marks), pstdev(marks)
    outliers = list(col.find({"$or": [{"marks": {"$lt": m - 2.5 * sd}}, {"marks": {"$gt": m + 2.5 * sd}}]}, {"_id": 0}))
    print("Anomalies:", outliers)

    if os.getenv("OPENAI_API_KEY"):
        from openai import OpenAI
        reply = OpenAI().chat.completions.create(
            model=os.getenv("AI_MODEL", "gpt-4o-mini"),
            messages=[{"role": "user", "content": f"Summarise this module report for teachers in 3 bullets: {report}"}],
        )
        print(reply.choices[0].message.content)
```

**How it works**

- `$cond` inside `$sum` counts passes; pass rate is computed in `$project`.
- `explain()` confirms the compound index is used.
- Only aggregated numbers (no student identities) go to the AI.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Complete the capstone without looking at the solution.
2. Rewrite the report in mongosh as a single aggregation.
3. Make a one-page revision sheet from the checklist table.

## 📝 Assignment

Choose a dataset you care about (cricket scores, weather, sales), load it into Atlas, and produce: three aggregations, two justified indexes, one transaction scenario, a Python report and an AI-generated summary of aggregated results. Present it as a README with screenshots.

## ❓ Quick Quiz

**Q1.** Which operator counts conditionally inside `$sum`?

**Q2.** How do you confirm an index is used?

**Q3.** What does a replica set provide?

**Q4.** Which API retries transactions automatically?

**Q5.** Name one safe practice when using AI with databases.

<details>
<summary>Show answers</summary>

1. `$cond`
2. Check for IXSCAN in `explain()` output.
3. High availability and redundancy.
4. The callback API (`withTransaction`).
5. Send schema/aggregated data only / validate generated queries / use read-only users.

</details>

## 💼 Interview Questions

**1. How would you design a MongoDB backend for 10 million users?**

> Model by access patterns, index carefully, use replica sets, shard on a high-cardinality key, cache hot data and monitor with Atlas.

**2. Explain one real use of change streams.**

> Watching a collection for inserts to push live notifications or sync data to a search index.

**3. What is the aggregation equivalent of SQL HAVING?**

> A `$match` stage placed after `$group`.

## ✅ Summary

- You can now store, query, analyse, secure and scale MongoDB data.
- Combine aggregation, indexes and code for real reports.
- Use AI as an assistant, never as an unchecked operator.

---

[⬅ Previous](../Session-15-AI-Powered-MongoDB/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../../04-Developing-Microsoft-Azure-Applications/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
