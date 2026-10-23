-- Session 07: SELECT practice on AdventureWorks2022
USE AdventureWorks2022;
GO
SELECT DISTINCT Color FROM Production.Product WHERE Color IS NOT NULL ORDER BY Color;

SELECT TOP (10) WITH TIES Name, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;

SELECT ProductID, Name AS ProductName, ListPrice * 280 AS PricePKR
FROM Production.Product
WHERE Name LIKE N'%Bike%' AND ListPrice BETWEEN 500 AND 2000
ORDER BY PricePKR;

SELECT BusinessEntityID, FirstName, LastName
FROM Person.Person
ORDER BY LastName, FirstName
OFFSET 40 ROWS FETCH NEXT 20 ROWS ONLY;
GO
