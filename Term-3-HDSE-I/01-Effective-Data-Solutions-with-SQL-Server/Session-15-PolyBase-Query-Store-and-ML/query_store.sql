-- Session 15: Query Store basics
ALTER DATABASE AdventureWorks2022 SET QUERY_STORE = ON (OPERATION_MODE = READ_WRITE);
GO
USE AdventureWorks2022;
GO
SELECT TOP (10) qt.query_sql_text, rs.avg_duration / 1000.0 AS AvgMs, rs.count_executions
FROM sys.query_store_query_text qt
JOIN sys.query_store_query q          ON q.query_text_id = qt.query_text_id
JOIN sys.query_store_plan p           ON p.query_id = q.query_id
JOIN sys.query_store_runtime_stats rs ON rs.plan_id = p.plan_id
ORDER BY rs.avg_duration DESC;
-- EXEC sp_query_store_force_plan @query_id = 42, @plan_id = 7;
-- EXEC sys.sp_query_store_set_hints @query_id = 42, @query_hints = N'OPTION (MAXDOP 1)';
GO
