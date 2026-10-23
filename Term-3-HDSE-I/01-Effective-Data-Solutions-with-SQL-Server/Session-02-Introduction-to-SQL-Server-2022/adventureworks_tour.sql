-- Session 02: First look at AdventureWorks2022
USE AdventureWorks2022;
GO
SELECT TOP (5) ProductID, Name, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;

SELECT s.name AS SchemaName, COUNT(*) AS TableCount
FROM sys.tables AS t
JOIN sys.schemas AS s ON s.schema_id = t.schema_id
GROUP BY s.name
ORDER BY TableCount DESC;
GO
