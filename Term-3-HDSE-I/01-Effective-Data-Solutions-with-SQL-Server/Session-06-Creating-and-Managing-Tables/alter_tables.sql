-- Session 06: Insert, test constraints and alter tables (run after shop_tables.sql)
USE CampusDB;
GO
INSERT INTO dbo.Category (Name) VALUES (N'Stationery'), (N'Electronics');
INSERT INTO dbo.Product (Sku, Name, Price, CategoryId)
VALUES ('ST-00001', N'Gel Pen', 60, 1), ('EL-00001', N'USB Cable', 450, 2);
SELECT SCOPE_IDENTITY() AS LastProductId;

-- Uncomment to see the CHECK constraint fail:
-- INSERT INTO dbo.Product (Sku, Name, Price, CategoryId) VALUES ('ST-00002', N'Free Pen', 0, 1);

INSERT INTO dbo.OrderLine (ProductId, Qty, UnitPrice) VALUES (1, 10, 60), (2, 2, 450);
SELECT * FROM dbo.OrderLine;

ALTER TABLE dbo.Product ADD Discount DECIMAL(4,2) NULL
    CONSTRAINT CK_Product_Discount CHECK (Discount BETWEEN 0 AND 0.5);
ALTER TABLE dbo.Product ALTER COLUMN Name NVARCHAR(150) NOT NULL;
EXEC sp_rename 'dbo.Product.InStock', 'IsAvailable', 'COLUMN';

ALTER TABLE dbo.Product DROP CONSTRAINT CK_Product_Discount;
ALTER TABLE dbo.Product DROP COLUMN Discount;
EXEC sp_help 'dbo.Product';
GO
