-- Session 12: Lab and Review - Pharmacy chain
IF DB_ID('PharmacyDB') IS NULL CREATE DATABASE PharmacyDB;
GO
USE PharmacyDB;
GO
DROP TABLE IF EXISTS dbo.PriceLog, dbo.Sale, dbo.Medicine, dbo.Branch;
CREATE TABLE dbo.Branch (BranchId INT IDENTITY PRIMARY KEY, Name NVARCHAR(60) NOT NULL);
CREATE TABLE dbo.Medicine (
    MedicineId INT IDENTITY PRIMARY KEY,
    Name  NVARCHAR(80) NOT NULL,
    Price DECIMAL(8,2) NOT NULL CHECK (Price > 0),
    Stock INT NOT NULL DEFAULT 100
);
CREATE TABLE dbo.Sale (
    SaleId     INT IDENTITY PRIMARY KEY,
    BranchId   INT NOT NULL REFERENCES dbo.Branch(BranchId),
    MedicineId INT NOT NULL REFERENCES dbo.Medicine(MedicineId),
    Qty        INT NOT NULL CHECK (Qty > 0),
    UnitPrice  DECIMAL(8,2) NOT NULL,
    SoldAt     DATETIME2(0) NOT NULL DEFAULT SYSDATETIME()
);
CREATE TABLE dbo.PriceLog (
    LogId INT IDENTITY PRIMARY KEY, MedicineId INT, OldPrice DECIMAL(8,2),
    NewPrice DECIMAL(8,2), ChangedAt DATETIME2 DEFAULT SYSDATETIME()
);
GO
INSERT INTO dbo.Branch (Name) VALUES (N'Gulshan'), (N'North Nazimabad'), (N'Clifton');
INSERT INTO dbo.Medicine (Name, Price) VALUES
 (N'Panadol 500mg', 35), (N'Brufen 400mg', 60), (N'ORS Sachet', 25),
 (N'Vitamin C 1000', 450), (N'Cough Syrup 120ml', 210), (N'Insulin Pen', 2900);
INSERT INTO dbo.Sale (BranchId, MedicineId, Qty, UnitPrice, SoldAt)
SELECT (value % 3) + 1, (value % 5) + 1, (value % 4) + 1,
       CHOOSE((value % 5) + 1, 35, 60, 25, 450, 210),
       DATEADD(HOUR, -value * 5, SYSDATETIME())
FROM GENERATE_SERIES(1, 300);
GO
CREATE OR ALTER VIEW dbo.vDailyBranchSales AS
SELECT b.Name AS Branch, CAST(s.SoldAt AS DATE) AS SaleDate,
       COUNT(*) AS Bills, SUM(s.Qty * s.UnitPrice) AS Revenue
FROM dbo.Sale s JOIN dbo.Branch b ON b.BranchId = s.BranchId
GROUP BY b.Name, CAST(s.SoldAt AS DATE);
GO
CREATE OR ALTER PROCEDURE dbo.usp_BranchReport
    @BranchId INT, @Days INT = 7, @Revenue DECIMAL(12,2) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;
    SELECT m.Name, SUM(s.Qty) AS UnitsSold
    FROM dbo.Sale s JOIN dbo.Medicine m ON m.MedicineId = s.MedicineId
    WHERE s.BranchId = @BranchId AND s.SoldAt >= DATEADD(DAY, -@Days, SYSDATETIME())
    GROUP BY m.Name ORDER BY UnitsSold DESC;

    SELECT @Revenue = ISNULL(SUM(Qty * UnitPrice), 0)
    FROM dbo.Sale
    WHERE BranchId = @BranchId AND SoldAt >= DATEADD(DAY, -@Days, SYSDATETIME());
END;
GO
CREATE NONCLUSTERED INDEX IX_Medicine_Name ON dbo.Medicine(Name) INCLUDE (Price);
GO
-- TODO (lab task 4): complete the WHERE clause so only real changes are logged
CREATE OR ALTER TRIGGER dbo.trg_Medicine_PriceLog ON dbo.Medicine AFTER UPDATE AS
BEGIN
    SET NOCOUNT ON;
    INSERT INTO dbo.PriceLog (MedicineId, OldPrice, NewPrice)
    SELECT i.MedicineId, d.Price, i.Price
    FROM inserted i JOIN deleted d ON d.MedicineId = i.MedicineId
    WHERE 1 = 1;   -- replace with the correct condition
END;
GO
DECLARE @rev DECIMAL(12,2);
EXEC dbo.usp_BranchReport @BranchId = 2, @Revenue = @rev OUTPUT;
SELECT @rev AS LastWeekRevenue;

SELECT Branch, SUM(Revenue) AS Revenue FROM dbo.vDailyBranchSales GROUP BY ROLLUP (Branch);

SELECT m.Name FROM dbo.Medicine m
WHERE NOT EXISTS (SELECT 1 FROM dbo.Sale s
                  WHERE s.MedicineId = m.MedicineId
                    AND s.SoldAt >= DATEADD(DAY, -30, SYSDATETIME()));
GO
