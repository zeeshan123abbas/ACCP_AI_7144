# Session 07: Subqueries and Common Table Expressions

> Module: Working with MySQL · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Write single-row and multi-row subqueries in WHERE, FROM and SELECT
- Use IN, ANY, ALL and EXISTS correctly
- Explain correlated vs non-correlated subqueries
- Write readable queries with WITH (CTEs) and recursive CTEs
- Use window functions such as RANK() and running totals

## 📖 Concepts Explained

### 1. What is a subquery?

A **subquery** is a `SELECT` written inside another statement. MySQL runs the inner query and uses its result in the outer one. Think of it as asking a helper question first: *"What is the average fee?"* and then *"Which courses cost more than that?"*

| Where it appears | Returns | Example use |
|---|---|---|
| `WHERE col = (subquery)` | one value (scalar) | courses above average fee |
| `WHERE col IN (subquery)` | a list | students who paid by card |
| `FROM (subquery) AS t` | a table (derived table) | average of per-student totals |
| `SELECT (subquery) AS x` | one value per row | course count per student |

### 2. Operators for multi-row subqueries

| Operator | Meaning |
|---|---|
| `IN` | equals any value in the list |
| `> ANY` | greater than at least one value |
| `> ALL` | greater than every value |
| `EXISTS` | true if the subquery returns at least one row |

`NOT IN` has a trap: if the list contains a `NULL`, nothing matches. Prefer `NOT EXISTS` for anti-joins.

### 3. Correlated subqueries

A **correlated** subquery refers to a column of the outer query, so it is re-evaluated for each outer row (e.g. "students whose marks are above the average **of their own course**"). Correct but potentially slow on big tables; a join or window function is often faster.

### 4. CTEs (WITH clause) — MySQL 8.0+

A **Common Table Expression** gives a subquery a name so the main query reads top-to-bottom like a story. A **recursive CTE** calls itself and is perfect for number series, calendars and hierarchies (category trees, manager chains).

```mermaid
flowchart LR
  A[WITH totals AS ...] --> B[WITH ranked AS ... uses totals]
  B --> C[Final SELECT uses ranked]
```

### 5. Window functions

Window functions compute across related rows **without collapsing them** like `GROUP BY` does: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `SUM() OVER (...)`, `LAG()`, `LEAD()`.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Subqueries on institute_db (`subqueries.sql`)

```sql
-- subqueries.sql  (run after institute-schema.sql and seed-data.sql)
USE institute_db;

-- Scalar subquery: courses that cost more than the average fee
SELECT code, title, fee
FROM courses
WHERE fee > (SELECT AVG(fee) FROM courses);

-- IN: students who have paid at least once by card
SELECT full_name FROM students
WHERE student_id IN (
  SELECT e.student_id
  FROM enrollments e JOIN payments p ON p.enrollment_id = e.enrollment_id
  WHERE p.method = 'card');

-- NOT EXISTS: students with no enrollment at all
SELECT s.full_name FROM students s
WHERE NOT EXISTS (SELECT 1 FROM enrollments e WHERE e.student_id = s.student_id);

-- Correlated: enrollments scoring above their own course average
SELECT e.student_id, e.course_id, e.marks
FROM enrollments e
WHERE e.marks > (SELECT AVG(e2.marks) FROM enrollments e2 WHERE e2.course_id = e.course_id);

-- Derived table: average amount paid per student
SELECT ROUND(AVG(total_paid)) AS avg_paid_per_student
FROM (
  SELECT e.student_id, SUM(p.amount) AS total_paid
  FROM enrollments e JOIN payments p ON p.enrollment_id = e.enrollment_id
  GROUP BY e.student_id
) AS t;

-- Scalar subquery in SELECT: number of courses per student
SELECT s.full_name,
       (SELECT COUNT(*) FROM enrollments e WHERE e.student_id = s.student_id) AS courses_taken
FROM students s;
```

**How it works:**

- The first query computes `AVG(fee)` once and compares each row to it.
- `NOT EXISTS` stops at the first matching row, so it is efficient and NULL-safe.
- The correlated query re-runs the inner `AVG` for each outer row, using `e.course_id` from outside.
- A derived table must always have an alias (`AS t`).

### Example 2: CTEs, recursion and window functions (`ctes-and-windows.sql`)

```sql
-- ctes-and-windows.sql  (MySQL 8.0+)
USE institute_db;

-- Named steps with WITH
WITH course_avg AS (
  SELECT course_id, AVG(marks) AS avg_marks
  FROM enrollments WHERE marks IS NOT NULL
  GROUP BY course_id
)
SELECT c.title, ROUND(ca.avg_marks, 1) AS avg_marks
FROM course_avg ca JOIN courses c ON c.course_id = ca.course_id
ORDER BY avg_marks DESC;

-- Recursive CTE: the 12 months of 2025 (useful for reports with empty months)
WITH RECURSIVE months AS (
  SELECT DATE('2025-01-01') AS m
  UNION ALL
  SELECT m + INTERVAL 1 MONTH FROM months WHERE m < '2025-12-01'
)
SELECT DATE_FORMAT(m, '%b %Y') AS month,
       COALESCE((SELECT SUM(amount) FROM payments
                 WHERE DATE_FORMAT(paid_on, '%Y-%m') = DATE_FORMAT(m, '%Y-%m')), 0) AS collected
FROM months;

-- Window functions: rank students inside each course
SELECT c.title, s.full_name, e.marks,
       RANK() OVER (PARTITION BY e.course_id ORDER BY e.marks DESC) AS position
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id
WHERE e.marks IS NOT NULL;

-- Running total of collections by date
SELECT DATE(paid_on) AS day, SUM(amount) AS collected,
       SUM(SUM(amount)) OVER (ORDER BY DATE(paid_on)) AS running_total
FROM payments
GROUP BY DATE(paid_on);
```

**How it works:**

- `course_avg` is computed once and joined like a normal table.
- The recursive CTE starts with January (anchor) and keeps adding a month until December.
- `PARTITION BY` restarts the ranking for every course; rows are not collapsed.
- `SUM(SUM(amount)) OVER (...)` adds a window sum on top of the grouped daily sum.

## 🧪 Lab Practice

1. List courses whose fee is lower than the fee of **every** 6-week course (use `ALL`).
2. Find students who are enrolled in the same course as Ayesha Khan (subquery with `IN`).
3. Rewrite the `NOT EXISTS` query using `LEFT JOIN ... IS NULL` and compare results.
4. Use a CTE to find the top-scoring student in each course (`ROW_NUMBER()` = 1).
5. Generate numbers 1 to 20 with a recursive CTE.

## 📝 Assignment

Write `toppers.sql` that prints, for each city, the student with the highest average marks. Use one CTE for per-student averages and a window function to pick the best per city. Add comments explaining each step.

## ❓ Quick Quiz

1. A subquery that returns one value is called?
   - a) Derived table
   - b) Scalar subquery
   - c) CTE
   - d) View
2. Why can `NOT IN` return no rows unexpectedly?
3. What keyword starts a CTE?
4. What makes a subquery correlated?
5. Difference between RANK() and DENSE_RANK()?

<details>
<summary>Show answers</summary>

1. b) Scalar subquery
2. If the subquery list contains a NULL, every comparison becomes UNKNOWN.
3. `WITH` (and `WITH RECURSIVE` for recursive ones)
4. It references a column from the outer query, so it runs per outer row.
5. RANK leaves gaps after ties (1,1,3); DENSE_RANK does not (1,1,2).

</details>

## 💼 Interview Questions

1. **When would you use EXISTS instead of IN?**

   <details><summary>Model answer</summary>

   EXISTS is ideal for checking whether related rows exist, especially for large or correlated sets; it stops at the first match and NOT EXISTS is safe with NULLs, unlike NOT IN.

   </details>

2. **What is the advantage of a CTE over a derived table?**

   <details><summary>Model answer</summary>

   Readability and reuse: a CTE is named once and can be referenced several times in the same query, and CTEs can be recursive.

   </details>

3. **How are window functions different from GROUP BY?**

   <details><summary>Model answer</summary>

   GROUP BY collapses rows into one per group; window functions compute values over a set of rows but keep every row in the output.

   </details>

## ✅ Summary

- Subqueries let one query use the answer of another.
- Use IN/ANY/ALL/EXISTS for multi-row results; prefer NOT EXISTS over NOT IN.
- Correlated subqueries run per row; consider joins or windows for speed.
- CTEs make long queries readable; recursive CTEs generate series and walk trees.
- Window functions rank and accumulate without losing detail rows.

---

[⬅ Previous](../Session-06-Joins-and-Set-Operators/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Functions-Procedures-Triggers/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
