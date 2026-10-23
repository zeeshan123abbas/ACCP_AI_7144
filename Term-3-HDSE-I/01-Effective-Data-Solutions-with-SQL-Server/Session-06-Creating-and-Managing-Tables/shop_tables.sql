-- Session 06: Creating tables with constraints
USE CampusDB;
GO
DROP TABLE IF EXISTS dbo.OrderLine, dbo.Product, dbo.Category;
GO
CREATE TABLE dbo.Category (
    CategoryId INT IDENTITY(1,1) CONSTRAINT PK_Category PRIMARY KEY,
    Name       NVARCHAR(50) NOT NULL CONSTRAINT UQ_Category_Name UNIQUE
);
CREATE TABLE dbo.Product (
    ProductId  INT IDENTITY(1,1) CONSTRAINT PK_Product PRIMARY KEY,
    Sku        CHAR(8)       NOT NULL CONSTRAINT UQ_Product_Sku UNIQUE,
    Name       NVARCHAR(100) NOT NULL,
    Price      DECIMAL(10,2) NOT NULL CONSTRAINT CK_Product_Price CHECK (Price > 0),
    InStock    BIT           NOT NULL CONSTRAINT DF_Product_InStock DEFAULT 1,
    CreatedAt  DATETIME2(0)  NOT NULL CONSTRAINT DF_Product_Created DEFAULT SYSDATETIME(),
    CategoryId INT NOT NULL CONSTRAINT FK_Product_Category
               REFERENCES dbo.Category(CategoryId)
);
CREATE TABLE dbo.OrderLine (
    OrderLineId INT IDENTITY PRIMARY KEY,
    ProductId   INT NOT NULL REFERENCES dbo.Product(ProductId),
    Qty         INT NOT NULL CHECK (Qty > 0),
    UnitPrice   DECIMAL(10,2) NOT NULL,
    LineTotal   AS (Qty * UnitPrice) PERSISTED
);
GO
