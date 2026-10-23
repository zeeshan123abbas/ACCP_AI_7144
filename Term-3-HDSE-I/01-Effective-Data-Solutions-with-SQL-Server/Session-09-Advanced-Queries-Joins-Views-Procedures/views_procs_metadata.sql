-- Session 09: Views, stored procedures and metadata (AdventureWorks2022)
USE AdventureWorks2022;
GO
CREATE OR ALTER VIEW Sales.vTopCustomers
AS
SELECT c.CustomerID, SUM(h.TotalDue) AS Spent
FROM Sales.Customer c
JOIN Sales.SalesOrderHeader h ON h.CustomerID = c.CustomerID
GROUP BY c.CustomerID;
GO
CREATE OR ALTER PROCEDURE Sales.usp_OrdersByCustomer
    @CustomerID INT,
    @FromDate   DATE = '2000-01-01',
    @OrderCount INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT SalesOrderID, OrderDate, TotalDue
    FROM Sales.SalesOrderHeader
    WHERE CustomerID = @CustomerID AND OrderDate >= @FromDate
    ORDER BY OrderDate DESC;
    SET @OrderCount = @@ROWCOUNT;
END;
GO
DECLARE @n INT;
EXEC Sales.usp_OrdersByCustomer @CustomerID = 29825, @OrderCount = @n OUTPUT;
SELECT @n AS OrdersReturned;

SELECT TOP (5) * FROM Sales.vTopCustomers ORDER BY Spent DESC;

SELECT name, type_desc, create_date FROM sys.objects
WHERE schema_id = SCHEMA_ID('Sales') AND type IN ('V', 'P');
EXEC sp_helptext 'Sales.usp_OrdersByCustomer';
GO
