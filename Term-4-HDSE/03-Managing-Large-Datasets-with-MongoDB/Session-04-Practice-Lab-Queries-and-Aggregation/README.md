# Session 04: Practice Lab: Queries and Aggregation

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Session 3. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Choose the correct operator for a requirement
- Update arrays and nested fields
- Build multi-stage aggregation reports
- Read pipeline output critically

## 📖 Concepts Explained

### Scenario: online orders

Collection `orders`: `{ customer, city, items: [{ product, qty, price }], status, createdAt }`

| # | Requirement |
|---|---|
| 1 | Orders from Karachi or Lahore with status `"delivered"` |
| 2 | Orders that contain at least one item with qty ≥ 3 (`$elemMatch`) |
| 3 | Mark all `"pending"` orders older than 7 days as `"cancelled"` |
| 4 | Revenue per city (sum of qty × price) sorted high to low |
| 5 | Top 3 products by quantity sold |
| 6 | Monthly order count using `$dateToString` |

## 💻 Code Examples

### Example 1: Solution script

📄 File: [`solution.js`](solution.js)

```js
db = db.getSiblingDB("campus");
db.orders.drop();
const day = 24 * 60 * 60 * 1000, now = Date.now();
db.orders.insertMany([
  { customer: "Ali", city: "Karachi", status: "delivered", createdAt: new Date(now - 40 * day), items: [{ product: "Mouse", qty: 2, price: 1200 }, { product: "Cable", qty: 3, price: 650 }] },
  { customer: "Hira", city: "Lahore", status: "pending", createdAt: new Date(now - 10 * day), items: [{ product: "Keyboard", qty: 1, price: 5500 }] },
  { customer: "Sana", city: "Islamabad", status: "delivered", createdAt: new Date(now - 5 * day), items: [{ product: "Mouse", qty: 4, price: 1200 }] },
  { customer: "Bilal", city: "Karachi", status: "pending", createdAt: new Date(now - 2 * day), items: [{ product: "Monitor", qty: 1, price: 38000 }, { product: "Cable", qty: 1, price: 650 }] },
  { customer: "Zara", city: "Lahore", status: "delivered", createdAt: new Date(now - 1 * day), items: [{ product: "Cable", qty: 5, price: 650 }] }
]);
print("1"); printjson(db.orders.find({ city: { $in: ["Karachi", "Lahore"] }, status: "delivered" }, { _id: 0, customer: 1 }).toArray());
print("2"); printjson(db.orders.find({ items: { $elemMatch: { qty: { $gte: 3 } } } }, { _id: 0, customer: 1 }).toArray());
print("3"); printjson(db.orders.updateMany({ status: "pending", createdAt: { $lt: new Date(now - 7 * day) } }, { $set: { status: "cancelled" } }));
print("4"); printjson(db.orders.aggregate([
  { $match: { status: { $ne: "cancelled" } } }, { $unwind: "$items" },
  { $group: { _id: "$city", revenue: { $sum: { $multiply: ["$items.qty", "$items.price"] } } } },
  { $sort: { revenue: -1 } }]).toArray());
print("5"); printjson(db.orders.aggregate([
  { $unwind: "$items" }, { $group: { _id: "$items.product", sold: { $sum: "$items.qty" } } },
  { $sort: { sold: -1 } }, { $limit: 3 }]).toArray());
print("6"); printjson(db.orders.aggregate([
  { $group: { _id: { $dateToString: { format: "%Y-%m", date: "$createdAt" } }, orders: { $sum: 1 } } },
  { $sort: { _id: 1 } }]).toArray());
```

**How it works**

- `$elemMatch` requires one array element to meet all conditions.
- Revenue uses `$unwind` then `$multiply` inside `$sum`.
- `$dateToString` turns dates into `YYYY-MM` keys for monthly grouping.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Solve requirements 1-6 yourself.
2. Add `$lookup` to a `customers` collection to show each customer's phone in report 4.
3. Rewrite report 5 to also return total revenue per product.

## 📝 Assignment

Create a `results` collection (student, module, marks, semester). Build reports: pass percentage per module, top student per module (`$sort` + `$group` with `$first`), and students who failed more than one module.

## ❓ Quick Quiz

**Q1.** Which operator ensures one array element meets several conditions?

**Q2.** How do you compute qty × price in a pipeline?

**Q3.** Which stage limits output to N documents?

**Q4.** How do you group by month?

**Q5.** What does `$ne` mean?

<details>
<summary>Show answers</summary>

1. `$elemMatch`
2. `{ $multiply: ["$items.qty", "$items.price"] }`
3. `$limit`
4. Group on `$dateToString` with format `%Y-%m` (or `$year`/`$month`).
5. Not equal.

</details>

## 💼 Interview Questions

**1. How would you paginate aggregation results?**

> Add `$sort`, `$skip` and `$limit`, or use `$facet` to return a page plus total count.

**2. What is the 100 MB aggregation memory limit?**

> Stages like `$sort`/`$group` are limited in RAM; `allowDiskUse` lets them spill to disk (default true in recent versions for many operations).

**3. Why can `$unwind` be expensive?**

> It multiplies documents by array length, increasing data flowing through the pipeline.

## ✅ Summary

- Pick operators based on the exact requirement.
- `$unwind` + `$group` power most array reports.
- Always validate report numbers with a small sample.

---

[⬅ Previous](../Session-03-MongoDB-Operators-and-Aggregation-Pipeline/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Database-Commands-and-MongoDB-Shell-Methods/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
