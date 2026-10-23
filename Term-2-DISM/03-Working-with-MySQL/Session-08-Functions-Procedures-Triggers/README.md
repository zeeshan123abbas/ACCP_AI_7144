# Session 08: Built-in Functions, Stored Procedures and Triggers

> Module: Working with MySQL · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Use common string, numeric, date and control-flow functions
- Create and call stored procedures with IN, OUT and INOUT parameters
- Write stored functions that return a single value
- Create views to simplify and secure queries
- Create BEFORE/AFTER triggers for validation and auditing

## 📖 Concepts Explained

### 1. Built-in functions

| Group | Useful functions |
|---|---|
| String | `CONCAT`, `UPPER`, `LOWER`, `LENGTH`, `CHAR_LENGTH`, `SUBSTRING`, `TRIM`, `REPLACE`, `LPAD` |
| Numeric | `ROUND`, `CEIL`, `FLOOR`, `ABS`, `MOD`, `RAND` |
| Date/time | `NOW`, `CURDATE`, `DATE_FORMAT`, `DATEDIFF`, `TIMESTAMPDIFF`, `DATE_ADD` |
| Control flow | `IF`, `IFNULL`, `COALESCE`, `NULLIF`, `CASE` |
| Aggregate | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP_CONCAT` |

### 2. Stored programs

| Object | What it is | Called by |
|---|---|---|
| **View** | a saved SELECT that behaves like a table | `SELECT * FROM v` |
| **Stored procedure** | a named block of SQL with parameters | `CALL proc(...)` |
| **Stored function** | returns one value, usable inside SQL | `SELECT fn(...)` |
| **Trigger** | runs automatically on INSERT/UPDATE/DELETE | the server |

Why use them? Business rules live in one place, fewer round trips from PHP, and you can grant `EXECUTE` without giving table access.

### 3. DELIMITER

Inside a procedure body, statements end with `;`. To tell the client where the whole `CREATE PROCEDURE` ends, temporarily change the delimiter to `$$` (Workbench and the mysql client both need this).

### 4. Parameters

- `IN` – value passed in (default)
- `OUT` – value sent back to the caller via a session variable (`@x`)
- `INOUT` – both

### 5. Triggers

`BEFORE` triggers can change or reject the incoming row (`NEW.col`); `AFTER` triggers are good for audit logs. `OLD` holds the previous values for UPDATE/DELETE. Use `SIGNAL SQLSTATE '45000'` to raise a custom error.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Built-in functions in action (`functions.sql`)

```sql
-- functions.sql
USE institute_db;

SELECT UPPER(full_name)                         AS name_caps,
       CONCAT(LEFT(full_name, 1), '.', city)    AS short_tag,
       CHAR_LENGTH(full_name)                   AS name_length,
       TIMESTAMPDIFF(YEAR, dob, CURDATE())      AS age,
       DATE_FORMAT(created_at, '%d-%b-%Y')      AS joined,
       IFNULL(dob, 'not given')                 AS dob_or_text
FROM students;

SELECT title, fee, ROUND(fee / weeks) AS fee_per_week,
       CASE WHEN fee >= 30000 THEN 'Premium'
            WHEN fee >= 20000 THEN 'Standard'
            ELSE 'Short course' END AS band
FROM courses;

SELECT c.title, GROUP_CONCAT(s.full_name ORDER BY s.full_name SEPARATOR ', ') AS students
FROM courses c
JOIN enrollments e ON e.course_id = c.course_id
JOIN students s ON s.student_id = e.student_id
GROUP BY c.title;
```

**How it works:**

- `TIMESTAMPDIFF(YEAR, dob, CURDATE())` gives the exact age in whole years.
- `CASE` turns numbers into readable categories.
- `GROUP_CONCAT` joins many rows into one comma-separated string per group.

### Example 2: View, procedure, function and triggers (`procedures-triggers.sql`)

```sql
-- procedures-triggers.sql
USE institute_db;

-- 1) View: a safe, simple result card
CREATE OR REPLACE VIEW v_result_card AS
SELECT s.full_name, c.title, e.marks,
       CASE WHEN e.marks IS NULL THEN 'PENDING'
            WHEN e.marks >= 50 THEN 'PASS' ELSE 'FAIL' END AS result
FROM enrollments e
JOIN students s ON s.student_id = e.student_id
JOIN courses  c ON c.course_id  = e.course_id;

DELIMITER $$

-- 2) Procedure with IN and OUT parameters
DROP PROCEDURE IF EXISTS sp_student_balance $$
CREATE PROCEDURE sp_student_balance(IN p_student INT, OUT p_due DECIMAL(10,2))
BEGIN
  SELECT COALESCE(SUM(c.fee), 0) - COALESCE((
           SELECT SUM(p.amount) FROM payments p
           JOIN enrollments e2 ON e2.enrollment_id = p.enrollment_id
           WHERE e2.student_id = p_student), 0)
  INTO p_due
  FROM enrollments e JOIN courses c ON c.course_id = e.course_id
  WHERE e.student_id = p_student;
END $$

-- 3) Stored function: grade letter
DROP FUNCTION IF EXISTS fn_grade $$
CREATE FUNCTION fn_grade(p_marks INT) RETURNS CHAR(2)
DETERMINISTIC
BEGIN
  RETURN CASE
    WHEN p_marks IS NULL THEN '-'
    WHEN p_marks >= 85 THEN 'A+'
    WHEN p_marks >= 75 THEN 'A'
    WHEN p_marks >= 65 THEN 'B'
    WHEN p_marks >= 50 THEN 'C'
    ELSE 'F' END;
END $$

-- 4) Audit table + triggers
CREATE TABLE IF NOT EXISTS marks_audit (
  id INT AUTO_INCREMENT PRIMARY KEY,
  enrollment_id INT UNSIGNED,
  old_marks TINYINT UNSIGNED,
  new_marks TINYINT UNSIGNED,
  changed_by VARCHAR(100),
  changed_at DATETIME DEFAULT CURRENT_TIMESTAMP
) $$

DROP TRIGGER IF EXISTS trg_marks_before_update $$
CREATE TRIGGER trg_marks_before_update
BEFORE UPDATE ON enrollments FOR EACH ROW
BEGIN
  IF NEW.marks > 100 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Marks cannot exceed 100';
  END IF;
END $$

DROP TRIGGER IF EXISTS trg_marks_after_update $$
CREATE TRIGGER trg_marks_after_update
AFTER UPDATE ON enrollments FOR EACH ROW
BEGIN
  IF NOT (OLD.marks <=> NEW.marks) THEN
    INSERT INTO marks_audit (enrollment_id, old_marks, new_marks, changed_by)
    VALUES (NEW.enrollment_id, OLD.marks, NEW.marks, CURRENT_USER());
  END IF;
END $$

DELIMITER ;

-- Try it
SELECT * FROM v_result_card;
CALL sp_student_balance(4, @due);
SELECT @due AS amount_due_for_student_4;
SELECT full_name, title, marks, fn_grade(marks) AS grade FROM v_result_card;
UPDATE enrollments SET marks = 52 WHERE enrollment_id = 11;
SELECT * FROM marks_audit;
```

**How it works:**

- The view hides the joins; users simply `SELECT` from it.
- `sp_student_balance` subtracts total payments from total fees and returns the result through the `OUT` parameter `@due`.
- `fn_grade` is `DETERMINISTIC` (same input → same output), which MySQL requires when binary logging is on.
- The BEFORE trigger rejects invalid marks; the AFTER trigger writes an audit row only when marks actually change (`<=>` is the NULL-safe equals).

## 🧪 Lab Practice

1. Write a query that shows each student's first name only (hint: `SUBSTRING_INDEX(full_name, ' ', 1)`).
2. Create `sp_enroll(IN p_student INT, IN p_course INT)` that inserts an enrollment with today's date.
3. Create `fn_fee_after_discount(fee, percent)` and use it in a SELECT on `courses`.
4. Create a trigger that stops payments with `amount` greater than the course fee.
5. Run `SHOW PROCEDURE STATUS WHERE Db = 'institute_db';` and `SHOW TRIGGERS;`.

## 📝 Assignment

Build `fee-module.sql` containing: a view `v_fee_status` (student, course, fee, paid, due), a procedure `sp_pay(IN enrollment, IN amount, IN method)` that records a payment, and a trigger that logs every payment into a `payment_log` table. Include test calls.

## ❓ Quick Quiz

1. Which statement runs a stored procedure?
   - a) EXEC
   - b) RUN
   - c) CALL
   - d) DO
2. Why do we change DELIMITER before CREATE PROCEDURE?
3. In a trigger, what do OLD and NEW refer to?
4. Can a stored function be used inside SELECT?
5. Which function returns the first non-NULL argument?

<details>
<summary>Show answers</summary>

1. c) CALL
2. So the semicolons inside the body do not end the CREATE statement early.
3. OLD = row values before the change; NEW = values after (or being inserted).
4. Yes, it returns a single value and can be used like a built-in function.
5. `COALESCE()`

</details>

## 💼 Interview Questions

1. **Procedure vs function in MySQL?**

   <details><summary>Model answer</summary>

   A procedure is invoked with CALL, can return result sets and OUT parameters, and can perform transactions. A function returns exactly one value and is used inside SQL expressions.

   </details>

2. **Give two good uses of triggers and one risk.**

   <details><summary>Model answer</summary>

   Uses: audit logging and enforcing complex validation. Risk: hidden logic that surprises developers and slows bulk writes.

   </details>

3. **What is a view and is it stored data?**

   <details><summary>Model answer</summary>

   A view is a saved query. It normally stores no data; the underlying query runs whenever you select from it.

   </details>

## ✅ Summary

- Built-in functions transform strings, numbers and dates inside queries.
- Views simplify and secure complex SELECTs.
- Procedures (CALL) and functions (inside SELECT) package reusable logic.
- Triggers fire automatically BEFORE/AFTER data changes.
- Use DELIMITER $$ when creating stored programs in a client.

---

[⬅ Previous](../Session-07-Subqueries-and-CTEs/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-09-Grouping-Rollup-Indexes/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
