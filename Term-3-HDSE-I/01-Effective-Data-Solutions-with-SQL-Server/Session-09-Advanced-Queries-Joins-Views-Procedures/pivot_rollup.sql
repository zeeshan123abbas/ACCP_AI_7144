-- Session 09: ROLLUP, CUBE and PIVOT (AdventureWorks2022)
USE AdventureWorks2022;
GO
SELECT t.Name AS Territory, YEAR(h.OrderDate) AS OrderYear,
       SUM(h.TotalDue) AS Total, GROUPING(t.Name) AS IsGrandTotal
FROM Sales.SalesOrderHeader h
JOIN Sales.SalesTerritory t ON t.TerritoryID = h.TerritoryID
GROUP BY ROLLUP (t.Name, YEAR(h.OrderDate));

SELECT t.[Group] AS Region, sm.Name AS ShipMethod, COUNT(*) AS Orders
FROM Sales.SalesOrderHeader h
JOIN Sales.SalesTerritory t ON t.TerritoryID = h.TerritoryID
JOIN Purchasing.ShipMethod sm ON sm.ShipMethodID = h.ShipMethodID
GROUP BY CUBE (t.[Group], sm.Name);

-- Check which years exist first: SELECT DISTINCT YEAR(OrderDate) FROM Sales.SalesOrderHeader;
SELECT Territory, [2012], [2013], [2014]
FROM (SELECT t.Name AS Territory, YEAR(h.OrderDate) AS Yr, h.TotalDue
      FROM Sales.SalesOrderHeader h
      JOIN Sales.SalesTerritory t ON t.TerritoryID = h.TerritoryID) AS src
PIVOT (SUM(TotalDue) FOR Yr IN ([2012], [2013], [2014])) AS pvt;
GO
