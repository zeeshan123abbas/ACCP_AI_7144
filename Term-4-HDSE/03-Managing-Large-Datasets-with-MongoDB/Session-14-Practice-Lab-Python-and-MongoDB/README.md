# Session 14: Practice Lab: Python and MongoDB

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Session 13. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Write PyMongo CRUD code without help
- Use aggregation from Python
- Combine MongoDB with pandas for analysis
- Structure code into functions

## 📖 Concepts Explained

### Tasks

| # | Task |
|---|---|
| 1 | Create `sales` with 30 random documents (product, city, qty, price, date) using `random` |
| 2 | Print total revenue per city sorted descending |
| 3 | Find the best-selling product per month |
| 4 | Load all sales into a pandas DataFrame and compute the same as task 2 |
| 5 | Delete sales older than 90 days |

## 💻 Code Examples

### Example 1: Solution

📄 File: [`solution.py`](solution.py)

```python
"""pip install pymongo pandas   then  python solution.py"""
import random
from datetime import datetime, timedelta, timezone

import pandas as pd
from pymongo import MongoClient

products = ["Mouse", "Keyboard", "Monitor", "Cable"]
cities = ["Karachi", "Lahore", "Islamabad"]
now = datetime.now(timezone.utc)

with MongoClient("mongodb://localhost:27017") as client:
    sales = client.pylab.sales
    sales.drop()
    sales.insert_many([
        {"product": random.choice(products), "city": random.choice(cities), "qty": random.randint(1, 5),
         "price": random.choice([1200, 5500, 38000, 650]), "date": now - timedelta(days=random.randint(0, 150))}
        for _ in range(30)
    ])

    revenue = {"$sum": {"$multiply": ["$qty", "$price"]}}
    print("Revenue per city:")
    for r in sales.aggregate([{"$group": {"_id": "$city", "revenue": revenue}}, {"$sort": {"revenue": -1}}]):
        print(f"  {r['_id']}: Rs. {r['revenue']:,}")

    print("Best seller per month:")
    pipeline = [
        {"$group": {"_id": {"m": {"$dateToString": {"format": "%Y-%m", "date": "$date"}}, "p": "$product"}, "qty": {"$sum": "$qty"}}},
        {"$sort": {"qty": -1}},
        {"$group": {"_id": "$_id.m", "product": {"$first": "$_id.p"}, "qty": {"$first": "$qty"}}},
        {"$sort": {"_id": 1}},
    ]
    for r in sales.aggregate(pipeline):
        print(f"  {r['_id']}: {r['product']} ({r['qty']})")

    df = pd.DataFrame(list(sales.find({}, {"_id": 0})))
    df["revenue"] = df["qty"] * df["price"]
    print(df.groupby("city")["revenue"].sum().sort_values(ascending=False))

    print("Deleted old:", sales.delete_many({"date": {"$lt": now - timedelta(days=90)}}).deleted_count)
```

**How it works**

- A list comprehension generates random test data.
- `$sort` followed by `$group` with `$first` picks the top product per month.
- pandas reproduces the city totals, a useful cross-check.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Complete tasks 1-5.
2. Plot revenue per city with matplotlib.
3. Wrap each task in a function and add a `main()`.

## 📝 Assignment

Write a Python script that reads attendance records from MongoDB and produces a CSV report of each student's attendance percentage, flagging students below 75%.

## ❓ Quick Quiz

**Q1.** Which accumulator picks the first value in a group?

**Q2.** How do you convert a cursor to a DataFrame?

**Q3.** How do you create a date 90 days ago?

**Q4.** Why exclude `_id` before pandas?

**Q5.** Which method removes many documents?

<details>
<summary>Show answers</summary>

1. `$first`
2. `pd.DataFrame(list(cursor))`
3. `datetime.now(timezone.utc) - timedelta(days=90)`
4. ObjectId values are not needed for analysis and complicate output.
5. `delete_many`

</details>

## 💼 Interview Questions

**1. When would you use aggregation instead of pandas?**

> For large datasets, to process on the server and transfer only results.

**2. How do you store timezone-aware dates?**

> Use UTC `datetime` objects; MongoDB stores dates in UTC.

**3. How do you speed up bulk inserts?**

> Use `insert_many` with `ordered=False` or `bulk_write` batches.

## ✅ Summary

- Python + MongoDB is ideal for data analysis.
- Server-side aggregation saves bandwidth.
- Cross-check results with a second method.

---

[⬅ Previous](../Session-13-MongoDB-Connectivity-with-Python/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-15-AI-Powered-MongoDB/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
