-- Session 11: INSTEAD OF DELETE = soft delete
USE CampusDB;
GO
IF COL_LENGTH('dbo.Product', 'IsDeleted') IS NULL
    ALTER TABLE dbo.Product ADD IsDeleted BIT NOT NULL CONSTRAINT DF_Product_IsDeleted DEFAULT 0;
GO
CREATE OR ALTER TRIGGER dbo.trg_Product_SoftDelete
ON dbo.Product
INSTEAD OF DELETE
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE p SET IsDeleted = 1
    FROM dbo.Product p
    JOIN deleted d ON d.ProductId = p.ProductId;
END;
GO
DELETE FROM dbo.Product WHERE ProductId = 1;
SELECT ProductId, Name, IsDeleted FROM dbo.Product;
GO
