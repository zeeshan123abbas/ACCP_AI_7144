# Session 03: Data Types, Databases and Tables (DDL)

> Module: Working with MySQL · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Choose suitable MySQL data types for numbers, text, dates and JSON
- Create, select and drop databases
- Create tables with constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, DEFAULT, CHECK
- Alter tables to add, modify, rename and drop columns and constraints
- Drop and truncate tables and understand the difference

## 📖 Concepts Explained

### 1. SQL command families

| Family | Purpose | Commands |
|---|---|---|
| **DDL** – Data Definition | Define structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML** – Data Manipulation | Change data | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** – Data Query | Read data | `SELECT` |
| **DCL** – Data Control | Permissions | `GRANT`, `REVOKE` |
| **TCL** – Transaction Control | Transactions | `START TRANSACTION`, `COMMIT`, `ROLLBACK` |

### 2. MySQL data types

**Numeric**

| Type | Range / use |
|---|---|
| `TINYINT` | -128..127 (or 0..255 `UNSIGNED`): marks, flags |
| `SMALLINT` | ±32K |
| `INT` | ±2.1 billion: IDs, quantities |
| `BIGINT` | very large IDs, counters |
| `DECIMAL(10,2)` | exact money values (10 digits, 2 after the point) |
| `FLOAT` / `DOUBLE` | approximate scientific values (never for money) |
| `BOOLEAN` | alias of `TINYINT(1)` (0/1) |

**String**

| Type | Use |
|---|---|
| `CHAR(n)` | fixed length: country code `PK`, gender `M/F` |
| `VARCHAR(n)` | variable length up to n characters: names, emails |
| `TEXT` / `MEDIUMTEXT` | long text: descriptions, blog posts |
| `ENUM('a','b')` | one value from a fixed list |
| `SET('a','b')` | zero or more values from a list |
| `BLOB` | binary files (usually store files on disk and keep only the path) |

**Date and time**

| Type | Format | Use |
|---|---|---|
| `DATE` | `2026-03-15` | birthdays, admission date |
| `TIME` | `14:30:00` | class timing |
| `DATETIME` | `2026-03-15 14:30:00` | events, independent of time zone |
| `TIMESTAMP` | same, stored in UTC | created/updated times |
| `YEAR` | `2026` | batch year |

**Other:** `JSON` (validated JSON documents), spatial types (`POINT`).

### 3. Constraints

| Constraint | Purpose |
|---|---|
| `PRIMARY KEY` | unique + not null identifier |
| `AUTO_INCREMENT` | generate the next number automatically |
| `NOT NULL` | value required |
| `UNIQUE` | no duplicates (NULLs allowed) |
| `DEFAULT` | value used when none is given |
| `CHECK (expr)` | condition every row must satisfy (enforced since MySQL 8.0.16) |
| `FOREIGN KEY ... REFERENCES` | value must exist in the parent table |

Foreign key actions: `ON DELETE CASCADE` (delete children too), `ON DELETE SET NULL`, `ON DELETE RESTRICT` (default: block the delete), and the same for `ON UPDATE`.

### 4. Database commands

```sql
CREATE DATABASE IF NOT EXISTS shop_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
SHOW DATABASES;
USE shop_db;                 -- select it
SELECT DATABASE();           -- which one is selected?
DROP DATABASE IF EXISTS old_db;   -- deletes everything inside!
```

### 5. ALTER TABLE cheat sheet

| Task | Statement |
|---|---|
| Add column | `ALTER TABLE t ADD COLUMN phone VARCHAR(20) AFTER email;` |
| Change type | `ALTER TABLE t MODIFY COLUMN phone VARCHAR(25) NOT NULL;` |
| Rename column | `ALTER TABLE t RENAME COLUMN phone TO mobile;` |
| Drop column | `ALTER TABLE t DROP COLUMN mobile;` |
| Add constraint | `ALTER TABLE t ADD CONSTRAINT uq_email UNIQUE (email);` |
| Drop FK | `ALTER TABLE t DROP FOREIGN KEY fk_name;` |
| Rename table | `RENAME TABLE t TO t_new;` |

### 6. DROP vs TRUNCATE vs DELETE

| | `DROP TABLE` | `TRUNCATE TABLE` | `DELETE FROM` |
|---|---|---|---|
| Removes | Structure + data | All rows, keeps structure | Selected rows (WHERE) |
| Resets AUTO_INCREMENT | n/a | Yes | No |
| Can be rolled back | No | No | Yes (inside a transaction) |
| Speed | Fast | Very fast | Slower for large tables |

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Complete schema with constraints (`institute-schema.sql`)

```sql
-- institute-schema.sql : the database used in the rest of this module
DROP DATABASE IF EXISTS institute_db;
CREATE DATABASE institute_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE institute_db;

CREATE TABLE faculty (
  faculty_id  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name   VARCHAR(100) NOT NULL,
  email       VARCHAR(120) NOT NULL UNIQUE,
  salary      DECIMAL(10,2) CHECK (salary > 0),
  hired_on    DATE NOT NULL
);

CREATE TABLE students (
  student_id  INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  full_name   VARCHAR(100) NOT NULL,
  email       VARCHAR(120) NOT NULL UNIQUE,
  gender      ENUM('male','female','other') NOT NULL,
  dob         DATE,
  city        VARCHAR(50) NOT NULL DEFAULT 'Karachi',
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
  course_id   INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code        CHAR(6) NOT NULL UNIQUE,
  title       VARCHAR(100) NOT NULL,
  weeks       TINYINT UNSIGNED NOT NULL CHECK (weeks BETWEEN 1 AND 52),
  fee         DECIMAL(9,2) NOT NULL CHECK (fee >= 0),
  faculty_id  INT UNSIGNED,
  CONSTRAINT fk_course_faculty FOREIGN KEY (faculty_id)
    REFERENCES faculty(faculty_id) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE enrollments (
  enrollment_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  student_id    INT UNSIGNED NOT NULL,
  course_id     INT UNSIGNED NOT NULL,
  enrolled_on   DATE NOT NULL DEFAULT (CURRENT_DATE),
  marks         TINYINT UNSIGNED CHECK (marks <= 100),
  CONSTRAINT uq_student_course UNIQUE (student_id, course_id),
  CONSTRAINT fk_enr_student FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  CONSTRAINT fk_enr_course  FOREIGN KEY (course_id)  REFERENCES courses(course_id)  ON DELETE RESTRICT
);

CREATE TABLE payments (
  payment_id    INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  enrollment_id INT UNSIGNED NOT NULL,
  amount        DECIMAL(9,2) NOT NULL CHECK (amount > 0),
  paid_on       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  method        ENUM('cash','card','bank') NOT NULL,
  FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id) ON DELETE CASCADE
);

SHOW TABLES;
SHOW CREATE TABLE enrollments;
```

**How it works:**

- Tables are created **parents first** (faculty, students, courses) so foreign keys can point to them.
- `CHECK` constraints stop invalid values such as negative fees or marks above 100.
- `uq_student_course` prevents a student enrolling twice in one course.
- FK actions: deleting a student deletes their enrollments (`CASCADE`), deleting a course with enrollments is blocked (`RESTRICT`), deleting a faculty member leaves the course without a teacher (`SET NULL`).
- `DEFAULT (CURRENT_DATE)` uses an expression default, supported since MySQL 8.0.13.

### Example 2: Changing structure safely (`alter-practice.sql`)

```sql
-- alter-practice.sql  (run after institute-schema.sql)
USE institute_db;

-- Add columns
ALTER TABLE students
  ADD COLUMN phone VARCHAR(15) AFTER email,
  ADD COLUMN cnic CHAR(15) UNIQUE;

-- Modify a column type/size and nullability
ALTER TABLE students MODIFY COLUMN phone VARCHAR(20) NOT NULL DEFAULT '';

-- Rename a column
ALTER TABLE students RENAME COLUMN phone TO mobile;

-- Add a CHECK constraint with a name
ALTER TABLE students ADD CONSTRAINT chk_dob CHECK (dob > '1950-01-01');

-- Remove a column
ALTER TABLE students DROP COLUMN cnic;

-- Inspect the result
DESCRIBE students;

-- Temporary table for experiments: TRUNCATE vs DROP
CREATE TABLE temp_logs (id INT AUTO_INCREMENT PRIMARY KEY, msg VARCHAR(100));
INSERT INTO temp_logs (msg) VALUES ('a'), ('b'), ('c');
TRUNCATE TABLE temp_logs;              -- rows gone, AUTO_INCREMENT reset
INSERT INTO temp_logs (msg) VALUES ('new');
SELECT * FROM temp_logs;               -- id is 1 again
DROP TABLE IF EXISTS temp_logs;        -- table gone completely
```

**How it works:**

Each `ALTER` changes the structure without losing existing rows. Note that you can combine several changes in one `ALTER TABLE` statement separated by commas. The final block shows `TRUNCATE` resetting the counter and `DROP` removing the table itself.

## 🧪 Lab Practice

1. **Run** `institute-schema.sql`, then open Workbench's *Reverse Engineer* to see the diagram.
2. **Test constraints:** try inserting a course with `weeks = 60`, a student with gender `'unknown'`, and an enrollment for a non-existent student. Record each error code.
3. **Alter:** add `batch_code CHAR(5)` to `students`, then change it to `VARCHAR(10)` and add an index on it with `ALTER TABLE students ADD INDEX idx_batch (batch_code);`.
4. **Choose types:** pick and justify data types for: CNIC, mobile number, product price, blog post body, class start time, is_active flag, settings document.
5. **FK actions:** insert a faculty member and a course, delete the faculty member, then check the course's `faculty_id`.

## 📝 Assignment

Write `shop-schema.sql` for an online shop with tables `customers`, `categories`, `products`, `orders` and `order_items`. Use suitable data types, at least one of each constraint (PK, FK with an ON DELETE action, UNIQUE, NOT NULL, DEFAULT, CHECK, ENUM), then write 5 ALTER statements that evolve the design (e.g. add a discount column). Submit the script and a screenshot of the reverse-engineered diagram.

## ❓ Quick Quiz

1. Which data type should store money?
   - a) FLOAT
   - b) DOUBLE
   - c) DECIMAL
   - d) VARCHAR
2. Which command removes all rows but keeps the table and resets AUTO_INCREMENT?
3. Which category does `ALTER` belong to?
   - a) DML
   - b) DDL
   - c) DCL
   - d) TCL
4. What does `ON DELETE CASCADE` do?
5. Difference between CHAR(10) and VARCHAR(10)?

<details>
<summary>Show answers</summary>

1. c) DECIMAL
2. `TRUNCATE TABLE`
3. b) DDL
4. Deleting a parent row automatically deletes the child rows that reference it.
5. CHAR always uses fixed length (padded); VARCHAR uses only the length needed plus a small length byte.

</details>

## 💼 Interview Questions

1. **Why should money never be stored as FLOAT?**

   <details><summary>Model answer</summary>

   FLOAT and DOUBLE are binary approximations, so values like 0.1 cannot be stored exactly and rounding errors accumulate in totals. DECIMAL stores exact base-10 values.

   </details>

2. **Explain the difference between DELETE, TRUNCATE and DROP.**

   <details><summary>Model answer</summary>

   DELETE removes chosen rows, can use WHERE, is logged and can be rolled back. TRUNCATE removes all rows quickly, resets AUTO_INCREMENT and cannot be rolled back. DROP removes the whole table structure and data.

   </details>

3. **What is referential integrity?**

   <details><summary>Model answer</summary>

   The guarantee that a foreign key value always refers to an existing row in the parent table, enforced by FOREIGN KEY constraints and their ON DELETE/ON UPDATE rules.

   </details>

## ✅ Summary

- SQL commands fall into DDL, DML, DQL, DCL and TCL.
- Pick precise types: INT family, DECIMAL for money, VARCHAR/TEXT, DATE/DATETIME, ENUM, JSON.
- Constraints (PK, FK, UNIQUE, NOT NULL, DEFAULT, CHECK) protect data quality.
- `ALTER TABLE` adds, modifies, renames and drops columns and constraints.
- DROP removes structure; TRUNCATE empties fast; DELETE removes selected rows.

---

[⬅ Previous](../Session-02-Database-Design-Normalization/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Insert-and-Select/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
