-- Session 10: Inspect and maintain indexes
USE CampusDB;
GO
SELECT i.name AS IndexName, i.type_desc, ps.avg_fragmentation_in_percent, ps.page_count
FROM sys.dm_db_index_physical_stats(DB_ID(), OBJECT_ID('dbo.Customer'), NULL, NULL, 'LIMITED') ps
JOIN sys.indexes i ON i.object_id = ps.object_id AND i.index_id = ps.index_id;

ALTER INDEX IX_Customer_City_Joined ON dbo.Customer REORGANIZE;
ALTER INDEX ALL ON dbo.Customer REBUILD WITH (FILLFACTOR = 90);
EXEC sp_helpindex 'dbo.Customer';
GO
