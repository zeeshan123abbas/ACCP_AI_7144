-- Session 13: Window functions (AdventureWorks2022, compatibility level 160 for WINDOW clause)
USE AdventureWorks2022;
GO
SELECT h.SalesPersonID, h.SalesOrderID, h.OrderDate, h.TotalDue,
       ROW_NUMBER() OVER w AS RowNum,
       RANK()       OVER (PARTITION BY h.SalesPersonID ORDER BY h.TotalDue DESC) AS SizeRank,
       SUM(h.TotalDue) OVER (w ROWS UNBOUNDED PRECEDING) AS RunningTotal,
       LAG(h.TotalDue) OVER w AS PrevOrder,
       h.TotalDue - AVG(h.TotalDue) OVER (PARTITION BY h.SalesPersonID) AS DiffFromAvg
FROM Sales.SalesOrderHeader h
WHERE h.SalesPersonID IS NOT NULL
WINDOW w AS (PARTITION BY h.SalesPersonID ORDER BY h.OrderDate, h.SalesOrderID);

-- Top 3 most expensive products per subcategory
WITH Ranked AS (
    SELECT Name, ProductSubcategoryID, ListPrice,
           DENSE_RANK() OVER (PARTITION BY ProductSubcategoryID ORDER BY ListPrice DESC) AS r
    FROM Production.Product
    WHERE ProductSubcategoryID IS NOT NULL
)
SELECT * FROM Ranked WHERE r <= 3 ORDER BY ProductSubcategoryID, r;
GO
