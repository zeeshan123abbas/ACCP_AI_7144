-- Session 11: Business rule trigger that rolls back invalid orders
USE CampusDB;
GO
IF COL_LENGTH('dbo.Product', 'Stock') IS NULL
    ALTER TABLE dbo.Product ADD Stock INT NOT NULL CONSTRAINT DF_Product_Stock DEFAULT 50;
GO
CREATE OR ALTER TRIGGER dbo.trg_OrderLine_ReduceStock
ON dbo.OrderLine
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE p SET Stock = p.Stock - x.Qty
    FROM dbo.Product p
    JOIN (SELECT ProductId, SUM(Qty) AS Qty FROM inserted GROUP BY ProductId) x
      ON x.ProductId = p.ProductId;

    IF EXISTS (SELECT 1 FROM dbo.Product p JOIN inserted i ON i.ProductId = p.ProductId
               WHERE p.Stock < 0)
        THROW 50001, 'Not enough stock for one or more products. Order cancelled.', 1;
END;
GO
INSERT INTO dbo.OrderLine (ProductId, Qty, UnitPrice) VALUES (2, 5, 450);    -- succeeds
-- INSERT INTO dbo.OrderLine (ProductId, Qty, UnitPrice) VALUES (2, 500, 450); -- fails and rolls back
SELECT ProductId, Name, Stock FROM dbo.Product;
GO
