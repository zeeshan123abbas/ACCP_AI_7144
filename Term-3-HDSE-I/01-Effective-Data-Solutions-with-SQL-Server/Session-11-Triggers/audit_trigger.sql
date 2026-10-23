-- Session 11: AFTER UPDATE audit trigger (uses dbo.Product from Session 06)
USE CampusDB;
GO
DROP TABLE IF EXISTS dbo.PriceAudit;
CREATE TABLE dbo.PriceAudit (
    AuditId   INT IDENTITY PRIMARY KEY,
    ProductId INT,
    OldPrice  DECIMAL(10,2),
    NewPrice  DECIMAL(10,2),
    ChangedBy SYSNAME   DEFAULT SUSER_SNAME(),
    ChangedAt DATETIME2 DEFAULT SYSDATETIME()
);
GO
CREATE OR ALTER TRIGGER dbo.trg_Product_PriceAudit
ON dbo.Product
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    IF NOT UPDATE(Price) RETURN;

    INSERT INTO dbo.PriceAudit (ProductId, OldPrice, NewPrice)
    SELECT i.ProductId, d.Price, i.Price
    FROM inserted i
    JOIN deleted  d ON d.ProductId = i.ProductId
    WHERE i.Price <> d.Price;
END;
GO
UPDATE dbo.Product SET Price = Price * 1.10;
UPDATE dbo.Product SET Name = Name;   -- no audit rows (price not in SET)
SELECT * FROM dbo.PriceAudit;
GO
