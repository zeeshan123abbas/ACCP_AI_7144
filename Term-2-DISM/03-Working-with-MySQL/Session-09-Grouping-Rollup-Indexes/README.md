# Session 09: Grouping, ROLLUP and Indexes

> Module: Working with MySQL · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Summarise data with GROUP BY and aggregate functions
- Filter groups with HAVING and know how it differs from WHERE
- Produce subtotals and grand totals with WITH ROLLUP and GROUPING()
- Explain how B-tree indexes speed up queries
- Create, inspect and drop single, composite, unique and full-text indexes
- Read an EXPLAIN plan to confirm index usage

## 📖 Concepts Explained

### 1. GROUP BY

`GROUP BY` puts rows with the same value(s) into buckets and lets aggregates (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`) summarise each bucket. Every column in the `SELECT` list must be grouped or aggregated (MySQL's `ONLY_FULL_GROUP_BY` mode enforces this).

### 2. WHERE vs HAVING

| WHERE | HAVING |
|---|---|
| filters **rows** before grouping | filters **groups** after grouping |
| cannot use aggregates | usually uses aggregates |
| `WHERE city = 'Karachi'` | `HAVING COUNT(*) >= 3` |

Logical order: `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`.

### 3. ROLLUP

`WITH ROLLUP` adds extra summary rows: subtotals for each higher level and a grand total. The total rows show `NULL` in the rolled-up column; `GROUPING(col)` returns 1 on those rows so you can label them.

### 4. Indexes

An index is like the index at the back of a book: instead of reading every page (a **full table scan**), MySQL jumps straight to the right rows. InnoDB uses **B+ tree** indexes; the primary key is the **clustered index** (rows are stored in PK order).

| Type | Create with | Use |
|---|---|---|
| Primary | `PRIMARY KEY` | unique row identity |
| Unique | `CREATE UNIQUE INDEX` | no duplicates (emails) |
| Regular | `CREATE INDEX` | speed up WHERE/JOIN/ORDER BY |
| Composite | `(col1, col2)` | multi-column filters; **leftmost prefix** rule |
| Full-text | `FULLTEXT` | word search with `MATCH ... AGAINST` |

Trade-off: indexes speed reads but slow `INSERT/UPDATE/DELETE` and use disk. Index columns that appear in WHERE, JOIN and ORDER BY, and that have many distinct values.

### 5. EXPLAIN

`EXPLAIN SELECT ...` shows the plan. Watch `type` (`ALL` = full scan, `ref`/`range`/`const` = good), `key` (index used) and `rows` (estimated rows read). `EXPLAIN ANALYZE` (8.0.18+) actually runs the query and shows real timings.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: GROUP BY, HAVING and ROLLUP (`grouping.sql`)

```sql
-- grouping.sql
USE institute_db;

-- Students per city
SELECT city, COUNT(*) AS students
FROM students
GROUP BY city
ORDER BY students DESC;

-- Course statistics, only courses with at least 3 graded students
SELECT c.title, COUNT(e.marks) AS graded, ROUND(AVG(e.marks),1) AS avg_marks,
       MIN(e.marks) AS lowest, MAX(e.marks) AS highest
FROM courses c JOIN enrollments e ON e.course_id = c.course_id
GROUP BY c.title
HAVING COUNT(e.marks) >= 3;

-- Collections by method and month, with subtotals and grand total
SELECT IF(GROUPING(method), 'ALL METHODS', method)              AS method,
       IF(GROUPING(ym), 'Subtotal', ym)                         AS month,
       SUM(amount)                                              AS collected
FROM (SELECT method, DATE_FORMAT(paid_on, '%Y-%m') AS ym, amount FROM payments) p
GROUP BY method, ym WITH ROLLUP;
```

**How it works:**

- `HAVING COUNT(e.marks) >= 3` removes whole groups; `COUNT(col)` ignores NULL marks.
- `WITH ROLLUP` adds a subtotal per method and a final grand total row.
- `GROUPING()` returns 1 on the generated summary rows, letting us print friendly labels instead of NULL.

### Example 2: Creating and testing indexes (`indexes.sql`)

```sql
-- indexes.sql
USE institute_db;

SHOW INDEX FROM students;

-- Before: full scan on city
EXPLAIN SELECT full_name FROM students WHERE city = 'Karachi';

CREATE INDEX idx_students_city ON students(city);

-- After: uses idx_students_city (type = ref)
EXPLAIN SELECT full_name FROM students WHERE city = 'Karachi';

-- Composite index: helps WHERE course_id = ? AND marks >= ?
CREATE INDEX idx_enr_course_marks ON enrollments(course_id, marks);
EXPLAIN SELECT student_id FROM enrollments WHERE course_id = 3 AND marks >= 70;
-- Leftmost-prefix rule: this one cannot use it efficiently
EXPLAIN SELECT student_id FROM enrollments WHERE marks >= 70;

-- Full-text search on course titles
ALTER TABLE courses ADD FULLTEXT INDEX ft_course_title (title);
SELECT title FROM courses WHERE MATCH(title) AGAINST ('web development');

-- Clean up
DROP INDEX idx_students_city ON students;
```

**How it works:**

- Compare the `type`, `key` and `rows` columns before and after creating the index.
- The composite index serves queries that filter on `course_id` first; filtering only on `marks` skips the leftmost column.
- `MATCH ... AGAINST` uses the FULLTEXT index for natural-language word search.

## 🧪 Lab Practice

1. Show total fee revenue expected per faculty member (join courses → faculty, GROUP BY).
2. List cities that have more than one student using HAVING.
3. Use ROLLUP to show payments per student per method with subtotals.
4. Create an index on `payments(paid_on)` and EXPLAIN a date-range query before and after.
5. Try `EXPLAIN ANALYZE` on a join and note the actual time.

## 📝 Assignment

Prepare `dashboard.sql` with five management summaries (students per city, average marks per course, monthly collections with ROLLUP, top 3 courses by revenue, faculty workload). For each, state which index (if any) would help, create it, and paste the EXPLAIN output as comments.

## ❓ Quick Quiz

1. Which clause filters groups?
   - a) WHERE
   - b) HAVING
   - c) ORDER BY
   - d) LIMIT
2. What does WITH ROLLUP add?
3. What is the leftmost-prefix rule?
4. In EXPLAIN, what does type = ALL mean?
5. Name one cost of adding indexes.

<details>
<summary>Show answers</summary>

1. b) HAVING
2. Subtotal rows for each grouping level plus a grand total.
3. A composite index (a,b,c) can be used for filters on a, a+b, or a+b+c, but not b or c alone.
4. A full table scan; no index was used.
5. Slower writes and extra storage space.

</details>

## 💼 Interview Questions

1. **How do you decide which columns to index?**

   <details><summary>Model answer</summary>

   Index columns used in WHERE, JOIN and ORDER BY with high selectivity; confirm with EXPLAIN and the slow query log; avoid indexing tiny tables or low-cardinality flags alone.

   </details>

2. **What is a clustered index in InnoDB?**

   <details><summary>Model answer</summary>

   The primary key index, whose leaf pages store the full rows. Secondary indexes store the PK value to locate the row.

   </details>

3. **Difference between COUNT(*) and COUNT(col)?**

   <details><summary>Model answer</summary>

   COUNT(*) counts rows; COUNT(col) counts only rows where col is not NULL.

   </details>

## ✅ Summary

- GROUP BY + aggregates turn detail rows into summaries.
- WHERE filters rows, HAVING filters groups.
- WITH ROLLUP and GROUPING() produce subtotals and grand totals.
- Indexes trade write speed and space for much faster reads.
- Always check your query plan with EXPLAIN.

---

[⬅ Previous](../Session-08-Functions-Procedures-Triggers/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-10-Transactions-ACID-Backups/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
