-- partitioning.sql
USE institute_db;

-- RANGE by year: the PK must contain the partition column
CREATE TABLE fee_history (
  id      BIGINT UNSIGNED AUTO_INCREMENT,
  paid_on DATE NOT NULL,
  amount  DECIMAL(9,2) NOT NULL,
  PRIMARY KEY (id, paid_on)
)
PARTITION BY RANGE (YEAR(paid_on)) (
  PARTITION p2024 VALUES LESS THAN (2025),
  PARTITION p2025 VALUES LESS THAN (2026),
  PARTITION p2026 VALUES LESS THAN (2027),
  PARTITION pmax  VALUES LESS THAN MAXVALUE
);

INSERT INTO fee_history (paid_on, amount) VALUES
 ('2024-11-03', 15000), ('2025-02-10', 28000), ('2025-09-01', 26000), ('2026-01-15', 42000);

-- Partition pruning: only p2025 is read
EXPLAIN SELECT SUM(amount) FROM fee_history WHERE paid_on BETWEEN '2025-01-01' AND '2025-12-31';

-- Rows per partition
SELECT partition_name, table_rows
FROM information_schema.partitions
WHERE table_schema = 'institute_db' AND table_name = 'fee_history';

-- Archive old year instantly
ALTER TABLE fee_history DROP PARTITION p2024;

-- LIST by campus
CREATE TABLE campus_leads (
  id INT NOT NULL, campus_id INT NOT NULL, name VARCHAR(80),
  PRIMARY KEY (id, campus_id)
)
PARTITION BY LIST (campus_id) (
  PARTITION p_karachi VALUES IN (1, 2, 3),
  PARTITION p_lahore  VALUES IN (4, 5),
  PARTITION p_others  VALUES IN (6, 7, 8)
);

-- HASH: spread rows evenly over 4 partitions
CREATE TABLE login_events (
  user_id INT NOT NULL, logged_at DATETIME NOT NULL
)
PARTITION BY HASH (user_id) PARTITIONS 4;
