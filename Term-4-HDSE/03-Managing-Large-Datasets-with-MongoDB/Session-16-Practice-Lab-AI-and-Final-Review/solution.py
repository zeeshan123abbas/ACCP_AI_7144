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
