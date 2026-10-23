# Session 10: Transactions, ACID, Locking and Backups

> Module: Working with MySQL · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain the ACID properties with real examples
- Use START TRANSACTION, COMMIT, ROLLBACK and SAVEPOINT
- Describe isolation levels and the problems they prevent
- Explain row locks, deadlocks and SELECT ... FOR UPDATE
- Back up and restore databases with mysqldump and Workbench
- Manage users and privileges with GRANT and REVOKE

## 📖 Concepts Explained

### 1. What is a transaction?

A **transaction** is a group of statements that must succeed or fail **together**. Classic example: moving a fee from a student's wallet to the institute account — debiting without crediting would be a disaster.

### 2. ACID

| Property | Meaning | Example |
|---|---|---|
| **Atomicity** | all or nothing | debit and credit both happen or neither |
| **Consistency** | rules (constraints) always hold | balance never negative |
| **Isolation** | concurrent transactions do not see each other's half-done work | two cashiers paying at once |
| **Durability** | committed data survives a crash | redo log flushed to disk |

InnoDB is ACID compliant; the old MyISAM engine is not.

### 3. Autocommit

By default MySQL commits each statement immediately (`autocommit = 1`). `START TRANSACTION` suspends that until `COMMIT` or `ROLLBACK`. DDL statements (`CREATE`, `ALTER`, `DROP`) cause an **implicit commit**.

### 4. Isolation levels

| Level | Dirty read | Non-repeatable read | Phantom |
|---|---|---|---|
| READ UNCOMMITTED | possible | possible | possible |
| READ COMMITTED | no | possible | possible |
| **REPEATABLE READ** (InnoDB default) | no | no | mostly prevented (gap locks) |
| SERIALIZABLE | no | no | no |

### 5. Locks and deadlocks

InnoDB locks **rows**, not whole tables. `SELECT ... FOR UPDATE` locks rows you plan to change; `FOR SHARE` allows others to read but not modify. A **deadlock** happens when two transactions each wait for a lock the other holds; InnoDB detects it and rolls one back (error 1213) — your app should retry.

### 6. Backups

| Method | Type | Notes |
|---|---|---|
| `mysqldump` | logical (SQL text) | portable, simple, slower for huge DBs |
| Workbench → Data Export | logical | GUI wrapper around mysqldump |
| MySQL Enterprise Backup / Percona XtraBackup | physical | hot copies of data files, fast restore |
| Binary log | incremental | point-in-time recovery |

Rule of thumb: automate daily backups, keep copies off the server, and **test restores**.

### 7. Users and privileges

`CREATE USER`, `GRANT`, `REVOKE`, `SHOW GRANTS`. Apply **least privilege**: a PHP app needs `SELECT, INSERT, UPDATE, DELETE` on its own schema, not `ALL` on everything.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Fee transfer with transactions (`transactions.sql`)

```sql
-- transactions.sql
USE institute_db;

CREATE TABLE IF NOT EXISTS wallets (
  owner   VARCHAR(50) PRIMARY KEY,
  balance DECIMAL(10,2) NOT NULL CHECK (balance >= 0)
);
INSERT INTO wallets VALUES ('ayesha', 20000), ('institute', 0)
  ON DUPLICATE KEY UPDATE balance = VALUES(balance);

-- Successful transfer
START TRANSACTION;
  UPDATE wallets SET balance = balance - 15000 WHERE owner = 'ayesha';
  UPDATE wallets SET balance = balance + 15000 WHERE owner = 'institute';
COMMIT;

-- Failed transfer: CHECK constraint fails, so we roll back
START TRANSACTION;
  UPDATE wallets SET balance = balance + 9000 WHERE owner = 'institute';
  UPDATE wallets SET balance = balance - 9000 WHERE owner = 'ayesha'; -- error: balance < 0
ROLLBACK;
SELECT * FROM wallets;   -- institute still 15000, ayesha 5000

-- Savepoints
START TRANSACTION;
  INSERT INTO marks_audit (enrollment_id, old_marks, new_marks, changed_by) VALUES (1, 88, 89, 'demo');
  SAVEPOINT after_first;
  INSERT INTO marks_audit (enrollment_id, old_marks, new_marks, changed_by) VALUES (2, 91, 10, 'typo');
  ROLLBACK TO SAVEPOINT after_first;   -- undo only the typo
COMMIT;

-- Locking a row before changing it
START TRANSACTION;
  SELECT balance FROM wallets WHERE owner = 'ayesha' FOR UPDATE;
  UPDATE wallets SET balance = balance - 1000 WHERE owner = 'ayesha';
COMMIT;

SELECT @@transaction_isolation;
```

**How it works:**

- Both UPDATEs in the first block become permanent together at `COMMIT`.
- In the second block the CHECK constraint stops the debit; `ROLLBACK` also undoes the credit that already ran.
- `ROLLBACK TO SAVEPOINT` undoes part of a transaction while keeping earlier work.
- `FOR UPDATE` holds a row lock so no other session can change Ayesha's balance until we commit.
- Note: `marks_audit` comes from Session 08's script.

### Example 2: Backup, restore and user management (`backup-and-users.sh`)

```bash
#!/usr/bin/env bash
# backup-and-users.sh  - run from a terminal where `mysql` and `mysqldump` are on PATH

# 1) Consistent backup of one database (InnoDB) including routines and triggers
mysqldump -u root -p --single-transaction --routines --triggers \
  --databases institute_db > institute_db_$(date +%F).sql

# 2) Restore into the server (creates the database because of --databases)
mysql -u root -p < institute_db_$(date +%F).sql

# 3) Backup only the structure (no data)
mysqldump -u root -p --no-data institute_db > institute_schema_only.sql

# 4) Least-privilege application user
mysql -u root -p <<'SQL'
CREATE USER IF NOT EXISTS 'institute_app'@'localhost' IDENTIFIED BY 'Change_Me_123!';
GRANT SELECT, INSERT, UPDATE, DELETE ON institute_db.* TO 'institute_app'@'localhost';
CREATE USER IF NOT EXISTS 'report_viewer'@'%' IDENTIFIED BY 'Viewer_456!';
GRANT SELECT ON institute_db.v_result_card TO 'report_viewer'@'%';
SHOW GRANTS FOR 'institute_app'@'localhost';
REVOKE DELETE ON institute_db.* FROM 'institute_app'@'localhost';
SQL
```

**How it works:**

- `--single-transaction` takes a consistent snapshot without locking InnoDB tables.
- `--routines --triggers` include stored procedures, functions and triggers in the dump.
- The app user can only work inside `institute_db`; the viewer can only read one view.
- On Windows run the same commands in Command Prompt (replace `$(date +%F)` with a fixed file name).

## 🧪 Lab Practice

1. Open two Workbench tabs. In tab 1 start a transaction and update a wallet without committing; in tab 2 read the row. What do you see? Commit and read again.
2. Create a deadlock on purpose (two sessions updating two rows in opposite order) and read the 1213 error.
3. Change the isolation level for your session to READ COMMITTED and repeat lab 1.
4. Back up `institute_db` with mysqldump, drop it, and restore it.
5. Create a user that can only `SELECT` from `courses` and test what it cannot do.

## 📝 Assignment

Write `admission.sql`: a stored procedure `sp_admit(student_name, email, course_id, first_payment)` that inserts a student, an enrollment and a payment inside one transaction, and rolls back everything if any step fails (use `DECLARE EXIT HANDLER FOR SQLEXCEPTION`). Document how you tested the failure path.

## ❓ Quick Quiz

1. Which ACID property guarantees all-or-nothing?
   - a) Atomicity
   - b) Consistency
   - c) Isolation
   - d) Durability
2. What is InnoDB's default isolation level?
3. What does ROLLBACK TO SAVEPOINT do?
4. Which mysqldump option gives a consistent InnoDB backup without locking?
5. What should an application do after a deadlock error?

<details>
<summary>Show answers</summary>

1. a) Atomicity
2. REPEATABLE READ
3. Undoes changes made after the savepoint while keeping the transaction open.
4. `--single-transaction`
5. Retry the transaction.

</details>

## 💼 Interview Questions

1. **Explain a dirty read.**

   <details><summary>Model answer</summary>

   Reading data another transaction has changed but not committed; if that transaction rolls back you have read data that never existed. Prevented from READ COMMITTED upwards.

   </details>

2. **Logical vs physical backup?**

   <details><summary>Model answer</summary>

   Logical (mysqldump) exports SQL statements: portable but slow for large data. Physical copies the data files: fast backup and restore, but tied to the MySQL version and platform.

   </details>

3. **What is the principle of least privilege?**

   <details><summary>Model answer</summary>

   Give each user or application only the permissions it needs, nothing more, to limit damage if credentials leak.

   </details>

## ✅ Summary

- Transactions group statements into one all-or-nothing unit.
- ACID = Atomicity, Consistency, Isolation, Durability.
- Isolation levels balance correctness and concurrency; InnoDB uses REPEATABLE READ.
- Row locks and FOR UPDATE prevent lost updates; retry on deadlock.
- Back up regularly with mysqldump and test restores; grant least privilege.

---

[⬅ Previous](../Session-09-Grouping-Rollup-Indexes/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-11-Replication-and-Partitioning/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
