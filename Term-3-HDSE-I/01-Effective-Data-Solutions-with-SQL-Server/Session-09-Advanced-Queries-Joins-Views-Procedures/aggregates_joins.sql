-- Session 09: Aggregates, CTEs, joins and subqueries (AdventureWorks2022)
USE AdventureWorks2022;
GO
WITH OrderCounts AS (
    SELECT CustomerID, COUNT(*) AS Orders, SUM(TotalDue) AS Spent
    FROM Sales.SalesOrderHeader
    GROUP BY CustomerID
    HAVING COUNT(*) > 20
)
SELECT p.FirstName + ' ' + p.LastName AS Customer, oc.Orders, oc.Spent
FROM OrderCounts oc
JOIN Sales.Customer c ON c.CustomerID = oc.CustomerID
JOIN Person.Person p  ON p.BusinessEntityID = c.PersonID
ORDER BY oc.Spent DESC;

SELECT p.ProductID, p.Name
FROM Production.Product p
LEFT JOIN Sales.SalesOrderDetail d ON d.ProductID = p.ProductID
WHERE d.ProductID IS NULL;

SELECT ProductID FROM Production.Product
EXCEPT
SELECT ProductID FROM Sales.SalesOrderDetail;

SELECT p.Name, p.ListPrice, p.ProductSubcategoryID
FROM Production.Product p
WHERE p.ListPrice = (SELECT MAX(p2.ListPrice) FROM Production.Product p2
                     WHERE p2.ProductSubcategoryID = p.ProductSubcategoryID);
GO
