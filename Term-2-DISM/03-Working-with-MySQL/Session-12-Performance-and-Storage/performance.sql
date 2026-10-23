-- performance.sql
USE institute_db;

SHOW ENGINES;
SELECT table_name, engine FROM information_schema.tables WHERE table_schema = 'institute_db';

-- Turn on the slow query log (needs admin privilege)
SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1;
SHOW VARIABLES LIKE 'slow_query_log_file';

-- Top statements by total time (sys schema, MySQL 8)
SELECT query, exec_count, total_latency
FROM sys.statement_analysis
ORDER BY total_latency DESC
LIMIT 5;

-- Non-sargable vs sargable
CREATE INDEX idx_pay_date ON payments(paid_on);
EXPLAIN SELECT SUM(amount) FROM payments WHERE YEAR(paid_on) = 2025;                     -- type ALL
EXPLAIN SELECT SUM(amount) FROM payments WHERE paid_on >= '2025-01-01' AND paid_on < '2026-01-01'; -- range

-- Keyset pagination instead of large OFFSET
SELECT student_id, full_name FROM students WHERE student_id > 5 ORDER BY student_id LIMIT 5;

-- Buffer pool size in MB
SELECT @@innodb_buffer_pool_size / 1024 / 1024 AS buffer_pool_mb;

-- Statistics and defragmentation
ANALYZE TABLE enrollments;
OPTIMIZE TABLE payments;
