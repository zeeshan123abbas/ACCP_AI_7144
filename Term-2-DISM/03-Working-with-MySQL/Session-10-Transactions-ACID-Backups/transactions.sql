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
