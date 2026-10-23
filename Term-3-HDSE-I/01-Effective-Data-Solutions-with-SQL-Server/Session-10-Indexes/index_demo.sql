-- Session 10: Indexes in action (SQL Server 2022 for GENERATE_SERIES)
USE CampusDB;
GO
DROP TABLE IF EXISTS dbo.Customer;
CREATE TABLE dbo.Customer (
    CustomerId INT IDENTITY PRIMARY KEY,
    FullName   NVARCHAR(100) NOT NULL,
    City       NVARCHAR(40)  NOT NULL,
    Email      NVARCHAR(120) NOT NULL,
    IsActive   BIT NOT NULL DEFAULT 1,
    JoinedOn   DATE NOT NULL
);
INSERT INTO dbo.Customer (FullName, City, Email, IsActive, JoinedOn)
SELECT CONCAT(N'Customer ', value),
       CHOOSE(value % 4 + 1, N'Karachi', N'Lahore', N'Islamabad', N'Quetta'),
       CONCAT('c', value, '@mail.pk'),
       IIF(value % 10 = 0, 0, 1),
       DATEADD(DAY, -(value % 2000), '2026-01-01')
FROM GENERATE_SERIES(1, 100000);
GO
SET STATISTICS IO ON;
SELECT CustomerId, FullName FROM dbo.Customer WHERE Email = 'c77777@mail.pk';

CREATE UNIQUE NONCLUSTERED INDEX UX_Customer_Email ON dbo.Customer(Email);
SELECT CustomerId, FullName FROM dbo.Customer WHERE Email = 'c77777@mail.pk';

CREATE NONCLUSTERED INDEX IX_Customer_City_Joined
    ON dbo.Customer(City, JoinedOn) INCLUDE (FullName)
    WHERE IsActive = 1;
SELECT FullName, JoinedOn FROM dbo.Customer
WHERE City = N'Lahore' AND JoinedOn >= '2025-06-01' AND IsActive = 1;
SET STATISTICS IO OFF;
GO
