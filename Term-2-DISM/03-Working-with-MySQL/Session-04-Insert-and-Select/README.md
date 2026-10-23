# Session 04: Inserting and Retrieving Data

> Module: Working with MySQL · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Insert single and multiple rows, including default and NULL values
- Retrieve all or selected columns with `SELECT` and column aliases
- Filter rows with `WHERE` using comparison and logical operators
- Sort results with `ORDER BY` and page them with `LIMIT ... OFFSET`
- Use calculated columns and `INSERT ... SELECT`

## 📖 Concepts Explained

### 1. INSERT forms

| Form | Example |
|---|---|
| Single row with column list (recommended) | `INSERT INTO students (full_name, email, gender) VALUES ('Ali', 'ali@x.com', 'male');` |
| Multiple rows in one statement | `VALUES (...), (...), (...);` (faster than many single inserts) |
| Use defaults | omit the column or write `DEFAULT` |
| Explicit NULL | `VALUES ('Ali', NULL)` when the column allows it |
| Copy from a query | `INSERT INTO archive (...) SELECT ... FROM students WHERE ...;` |

Always list columns: if someone adds a column later, inserts without a column list break.

`LAST_INSERT_ID()` returns the AUTO_INCREMENT value just generated in your connection. It is useful when inserting a parent and then its children.

### 2. Anatomy of SELECT

```sql
SELECT column_list          -- 5. choose columns
FROM table                  -- 1. pick the table
WHERE condition             -- 2. filter rows
GROUP BY ...                -- 3. (later session)
HAVING ...                  -- 4. (later session)
ORDER BY column [ASC|DESC]  -- 6. sort
LIMIT n OFFSET m;           -- 7. take a slice
```

The numbers show the **logical order MySQL processes** the clauses. This is why you cannot use a column alias from `SELECT` inside `WHERE`.

### 3. Selecting columns

- `SELECT *` returns every column. Fine for exploring, but in applications list the columns you need (less data, clearer code).
- **Aliases:** `SELECT full_name AS name` or with spaces `AS "Student Name"`.
- **Expressions:** `SELECT title, fee * 0.9 AS discounted_fee`.
- `CONCAT(first, ' ', last)` joins text.

### 4. WHERE operators

| Operator | Meaning | Example |
|---|---|---|
| `=`, `<>` / `!=` | equal / not equal | `city = 'Lahore'` |
| `>`, `<`, `>=`, `<=` | comparison | `fee >= 20000` |
| `AND`, `OR`, `NOT` | combine conditions | `city='Karachi' AND gender='female'` |
| `IS NULL`, `IS NOT NULL` | test for missing values | `marks IS NULL` |

> **NULL is not a value, it is "unknown".** `marks = NULL` is never true. Always use `IS NULL`.

Operator precedence: `NOT` → `AND` → `OR`. Use parentheses to be clear: `WHERE city = 'Karachi' AND (fee > 30000 OR weeks > 12)`.

### 5. ORDER BY and LIMIT

- `ORDER BY fee DESC, title ASC` sorts by fee, then by title for ties.
- You can sort by an alias or a column position (`ORDER BY 2`), but names are clearer.
- `LIMIT 5` returns the first 5 rows; `LIMIT 10 OFFSET 20` skips 20 and returns 10. This is how **pagination** works: page *p* with size *s* → `LIMIT s OFFSET (p-1)*s`.
- Without `ORDER BY`, row order is **not guaranteed**.

### 6. Seed data for the module

The file `seed-data.sql` fills the `institute_db` schema from Session 3 with realistic sample rows. Every query in Sessions 4-12 uses this data, so run it once now.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Sample data for institute_db (`seed-data.sql`)

```sql
-- seed-data.sql : run after Session 03's institute-schema.sql
USE institute_db;

INSERT INTO faculty (full_name, email, salary, hired_on) VALUES
  ('Imran Javed',   'imran@inst.pk', 185000, '2019-06-01'),
  ('Hina Rauf',     'hina@inst.pk',  165000, '2021-02-15'),
  ('Kashif Mehmood','kashif@inst.pk',210000, '2016-09-10'),
  ('Sadia Noor',    'sadia@inst.pk', 120000, '2024-01-08');

INSERT INTO students (full_name, email, gender, dob, city) VALUES
  ('Ayesha Khan',   'ayesha@mail.com', 'female', '2004-05-12', 'Karachi'),
  ('Bilal Ahmed',   'bilal@mail.com',  'male',   '2003-11-02', 'Hyderabad'),
  ('Sana Javed',    'sana@mail.com',   'female', '2005-01-25', 'Karachi'),
  ('Usman Ali',     'usman@mail.com',  'male',   '2002-07-30', 'Lahore'),
  ('Fatima Zahra',  'fatima@mail.com', 'female', '2004-09-18', 'Karachi'),
  ('Hamza Siddiqui','hamza@mail.com',  'male',   '2005-03-03', 'Sukkur'),
  ('Mariam Iqbal',  'mariam@mail.com', 'female', '2003-12-21', 'Islamabad'),
  ('Danish Raza',   'danish@mail.com', 'male',   '2004-02-14', 'Karachi'),
  ('Zoya Baig',     'zoya@mail.com',   'female', NULL,         'Lahore'),
  ('Ahmed Shah',    'ahmed@mail.com',  'male',   '2001-08-08', 'Karachi');

INSERT INTO courses (code, title, weeks, fee, faculty_id) VALUES
  ('XMLJ01', 'Data Processing with XML and JSON', 3, 15000, 2),
  ('JSPR01', 'Programming with JavaScript',       6, 28000, 1),
  ('MYSQ01', 'Working with MySQL',                6, 26000, 3),
  ('PHPW01', 'Dynamic Web Development with PHP',  9, 42000, 1),
  ('LRVL01', 'Laravel Framework',                 4, 30000, 3),
  ('CMSW01', 'Websites with CMS',                 4, 22000, NULL);

INSERT INTO enrollments (student_id, course_id, enrolled_on, marks) VALUES
  (1,1,'2025-01-20',88),(1,2,'2025-02-15',91),(1,3,'2025-03-20',79),
  (2,1,'2025-01-20',64),(2,3,'2025-03-20',72),
  (3,2,'2025-02-15',55),(3,4,'2025-05-01',NULL),
  (4,3,'2025-03-20',95),(4,4,'2025-05-01',87),(4,5,'2025-08-01',90),
  (5,1,'2025-01-20',47),(5,2,'2025-02-15',68),
  (6,4,'2025-05-01',NULL),
  (7,2,'2025-02-15',82),(7,3,'2025-03-20',77),(7,5,'2025-08-01',NULL),
  (8,1,'2025-01-20',73),
  (10,3,'2025-03-20',38);

INSERT INTO payments (enrollment_id, amount, paid_on, method) VALUES
  (1,15000,'2025-01-20 10:00','cash'),(2,28000,'2025-02-15 11:30','card'),
  (3,13000,'2025-03-20 09:15','bank'),(3,13000,'2025-04-20 09:20','bank'),
  (4,15000,'2025-01-21 12:00','cash'),(5,26000,'2025-03-22 16:45','card'),
  (6,14000,'2025-02-16 10:10','cash'),(8,26000,'2025-03-20 13:00','bank'),
  (9,21000,'2025-05-02 15:00','card'),(9,21000,'2025-06-02 15:05','card'),
  (10,30000,'2025-08-01 10:30','bank'),(11,15000,'2025-01-20 14:00','cash'),
  (14,28000,'2025-02-17 11:00','card'),(15,26000,'2025-03-21 12:00','bank'),
  (17,15000,'2025-01-22 09:00','cash'),(18,10000,'2025-03-25 17:30','cash');
```

**How it works:**

Multi-row `INSERT` statements load the data quickly. Some values are deliberately missing (`NULL` marks, a `NULL` date of birth, a course with no faculty, a student with no enrollments) so later sessions can practise handling them.

### Example 2: Retrieving data (`select-practice.sql`)

```sql
-- select-practice.sql
USE institute_db;

-- 1. All columns, then chosen columns with aliases
SELECT * FROM courses;
SELECT code AS "Course Code", title, fee AS "Fee (PKR)" FROM courses;

-- 2. Calculated column
SELECT title, fee, ROUND(fee * 0.90) AS fee_after_10pct_discount FROM courses;

-- 3. WHERE with comparison and logical operators
SELECT full_name, city FROM students WHERE city = 'Karachi';
SELECT full_name, city, gender FROM students WHERE city = 'Karachi' AND gender = 'female';
SELECT title, fee, weeks FROM courses WHERE fee > 25000 AND (weeks >= 6 OR code = 'LRVL01');
SELECT full_name FROM students WHERE NOT city = 'Karachi';

-- 4. NULL handling
SELECT student_id, course_id FROM enrollments WHERE marks IS NULL;  -- results pending
SELECT title FROM courses WHERE faculty_id IS NULL;                 -- no teacher assigned

-- 5. Sorting
SELECT full_name, dob FROM students ORDER BY dob;                   -- oldest first
SELECT title, fee FROM courses ORDER BY fee DESC, title;

-- 6. Top-N and pagination
SELECT student_id, course_id, marks FROM enrollments
WHERE marks IS NOT NULL ORDER BY marks DESC LIMIT 3;                -- top 3 marks

SELECT student_id, full_name FROM students ORDER BY student_id LIMIT 4 OFFSET 4;  -- page 2 (size 4)

-- 7. Insert a student, then use the generated id
INSERT INTO students (full_name, email, gender, city) VALUES ('Rida Fatima', 'rida@mail.com', 'female', 'Multan');
SELECT LAST_INSERT_ID() AS new_student_id;

-- 8. INSERT ... SELECT : copy Karachi students into a new table
CREATE TABLE IF NOT EXISTS karachi_students LIKE students;
INSERT INTO karachi_students SELECT * FROM students WHERE city = 'Karachi';
SELECT COUNT(*) AS copied FROM karachi_students;
```

**How it works:**

Run each query separately (Ctrl+Enter in Workbench) and read the result. Notice that query 4 needs `IS NULL`, query 6 combines `WHERE`, `ORDER BY` and `LIMIT`, and query 8 copies rows from one table to another in a single statement.

## 🧪 Lab Practice

1. **Seed:** run `institute-schema.sql` (Session 3) then `seed-data.sql`. Confirm with `SELECT COUNT(*) FROM enrollments;` (18 rows).
2. **Columns:** list each course's title and its fee per week (`fee / weeks`) rounded to 0 decimals, with a clear alias.
3. **Filters:** find female students from Karachi or Lahore born after 2004-01-01 (use parentheses).
4. **Pagination:** write the query for page 3 of students with 3 students per page, ordered by name.
5. **Insert:** add yourself as a student and enroll yourself in two courses using `LAST_INSERT_ID()`.

## 📝 Assignment

Using `institute_db`, write `my-queries.sql` with 10 queries: three with different WHERE combinations, two involving NULL, two calculated columns with aliases, two sorted top-N queries, and one INSERT ... SELECT. Add a comment above each query explaining in plain English what question it answers.

## ❓ Quick Quiz

1. Which clause filters rows?
   - a) ORDER BY
   - b) WHERE
   - c) LIMIT
   - d) FROM
2. How do you find rows where `marks` is missing?
3. What does `LIMIT 10 OFFSET 20` return?
4. Is the result order guaranteed without ORDER BY?
   - a) Yes
   - b) No
5. Which function returns the last AUTO_INCREMENT id from your connection?

<details>
<summary>Show answers</summary>

1. b) WHERE
2. `WHERE marks IS NULL`
3. 10 rows starting after the first 20 (rows 21-30).
4. b) No
5. `LAST_INSERT_ID()`

</details>

## 💼 Interview Questions

1. **Why should you avoid `SELECT *` in application code?**

   <details><summary>Model answer</summary>

   It fetches unnecessary data, wastes network and memory, can break code when columns change, and prevents index-only (covering) optimisations. Listing columns is clearer and safer.

   </details>

2. **Why can't you use a SELECT alias in the WHERE clause?**

   <details><summary>Model answer</summary>

   Logically, WHERE is evaluated before SELECT, so the alias does not exist yet. Repeat the expression, use a subquery or derived table, or use HAVING where appropriate.

   </details>

3. **How do you implement pagination in MySQL?**

   <details><summary>Model answer</summary>

   With `ORDER BY` plus `LIMIT size OFFSET (page-1)*size`. For very large tables, keyset pagination (`WHERE id > last_seen_id ORDER BY id LIMIT size`) is faster than large offsets.

   </details>

## ✅ Summary

- `INSERT` supports single rows, multiple rows, defaults, NULLs and `INSERT ... SELECT`.
- `SELECT` chooses columns, aliases and calculated expressions.
- `WHERE` filters with comparison and logical operators; use `IS NULL` for missing values.
- `ORDER BY` sorts; `LIMIT ... OFFSET` returns slices for top-N and pagination.
- MySQL processes FROM → WHERE → SELECT → ORDER BY → LIMIT.

---

[⬅ Previous](../Session-03-Data-Types-and-DDL/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Update-Delete-Filter/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
