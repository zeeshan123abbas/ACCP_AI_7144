# Session 10: Practice Lab: Transactions and Tools

> Module: Managing Large Datasets with MongoDB · Term 4 (HDSE) · ⏱ ~2 hours

Hands-on practice session for Session 9. Try every task yourself first, then compare with the solution script in this folder.

## 🎯 Learning Objectives

- Write safe multi-document transactions
- Handle aborts and retries
- Use Compass for daily tasks
- Explain BI connectivity

## 📖 Concepts Explained

### Tasks

| # | Task |
|---|---|
| 1 | Create `inventory` (product, stock) and `sales` collections |
| 2 | Write a `sell(product, qty)` transaction that reduces stock and records a sale |
| 3 | Make it abort when stock is insufficient |
| 4 | Run 5 sales in a loop and verify totals in Compass |
| 5 | Use Compass Schema tab to describe the `sales` collection |

## 💻 Code Examples

### Example 1: Solution script

📄 File: [`solution.js`](solution.js)

```js
// Run on a replica set
const shop = db.getSiblingDB("shoplab");
shop.inventory.drop(); shop.sales.drop();
shop.inventory.insertMany([{ _id: "pen", stock: 50 }, { _id: "notebook", stock: 5 }]);
shop.createCollection("sales"); // create before the transaction

const session = db.getMongo().startSession();
const s = session.getDatabase("shoplab");

function sell(product, qty) {
  try {
    session.withTransaction(() => {
      const r = s.inventory.updateOne({ _id: product, stock: { $gte: qty } }, { $inc: { stock: -qty } });
      if (r.modifiedCount !== 1) throw new Error(`Not enough ${product}`);
      s.sales.insertOne({ product, qty, at: new Date() });
    });
    print(`Sold ${qty} ${product}`);
  } catch (e) { print("Aborted:", e.message); }
}

[["pen", 10], ["notebook", 3], ["notebook", 4], ["pen", 5], ["notebook", 2]].forEach(([p, q]) => sell(p, q));
printjson(shop.inventory.find().toArray());
printjson(shop.sales.aggregate([{ $group: { _id: "$product", sold: { $sum: "$qty" } } }]).toArray());
session.endSession();
```

**How it works**

- The conditional update both checks and reduces stock atomically.
- The third sale (4 notebooks when only 2 remain) aborts; nothing is recorded for it.

### ▶️ How to run

1. Install MongoDB Community Server 8 and `mongosh` (or use a free Atlas cluster).
2. Open a terminal in this folder and run a script with `mongosh --file <script>.js` (add your connection string before `--file` for Atlas).
3. Python files need Python 3.12 and `pip install pymongo`; run with `python <file>.py`.

## 🧪 Lab Practice

1. Complete tasks 1-5.
2. Open two mongosh windows and create a write conflict on the same document inside transactions; observe the error label.
3. Export a Compass query as Python code.

## 📝 Assignment

Build a **seat reservation** transaction for a cinema (seats collection + bookings collection) that books multiple seats at once or none. Test with overlapping requests and document the results.

## ❓ Quick Quiz

**Q1.** Why create collections before a transaction in older versions?

**Q2.** What error label appears on a write conflict?

**Q3.** Which Compass tab analyses field types?

**Q4.** Can you export Compass queries to code?

**Q5.** What happens to inserts if the transaction aborts?

<details>
<summary>Show answers</summary>

1. Creating collections inside transactions was not allowed before MongoDB 4.4 and is still best avoided.
2. `TransientTransactionError`
3. Schema.
4. Yes, to languages such as Node.js, Python, Java and C#.
5. They are discarded.

</details>

## 💼 Interview Questions

**1. How do drivers implement retryable writes?**

> They automatically retry certain single write operations once after network errors or elections, using a transaction number to avoid duplicates.

**2. What isolation level do MongoDB transactions use?**

> Snapshot isolation with readConcern `snapshot`.

**3. How would you monitor transaction performance?**

> serverStatus transaction metrics, profiler/slow query logs and Atlas monitoring.

## ✅ Summary

- Conditional updates make checks atomic.
- Aborts leave data untouched.
- Compass speeds up inspection and code generation.

---

[⬅ Previous](../Session-09-Transaction-Management-and-MongoDB-Tools/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-11-MongoDB-Cloud-with-Atlas/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
