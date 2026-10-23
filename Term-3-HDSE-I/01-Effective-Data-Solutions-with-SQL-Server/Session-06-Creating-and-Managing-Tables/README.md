# Session 06: Creating and Managing Tables

> Module: Effective Data Solutions with SQL Server · Term 3 (HDSE I) · ⏱ ~2 hours

## 🎯 Learning Objectives

- List SQL Server 2022 data types and pick the right one for each column
- Create tables with constraints: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `CHECK`, `DEFAULT`, `NOT NULL`
- Use `IDENTITY` and computed columns
- Modify tables with `ALTER TABLE`: add, change and drop columns and constraints
- Drop tables safely and in the right order
- Insert, update and delete rows to test your constraints

## 📖 Concepts Explained

### 1. Choosing Data Types

| Data | Good type | Why |
|---|---|---|
| Auto ID | `INT IDENTITY(1,1)` | Fast, 4 bytes, up to ~2.1 billion |
| Very large IDs | `BIGINT` | Up to 9.2 quintillion |
| Yes/No flag | `BIT` | 0 or 1 |
| Name, address | `NVARCHAR(100)` | Unicode, variable length |
| Fixed code (country, CNIC) | `CHAR(2)`, `CHAR(13)` | Always same length |
| Money | `DECIMAL(12,2)` | Exact |
| Birth date | `DATE` | No time needed |
| Created timestamp | `DATETIME2(0)` | Precise and smaller than `DATETIME` |
| Global ID | `UNIQUEIDENTIFIER` with `NEWID()` | Unique across servers |
| Images / files | `VARBINARY(MAX)` | Binary data (often better stored as a file path) |
| Long text | `NVARCHAR(MAX)` | Up to 2 GB |

Avoid deprecated types `TEXT`, `NTEXT`, `IMAGE`.

### 2. Constraints — Rules the Database Enforces

| Constraint | Guarantees |
|---|---|
| `NOT NULL` | Value must be supplied |
| `PRIMARY KEY` | Unique + not NULL; creates a clustered index by default |
| `UNIQUE` | No duplicates (one NULL allowed) |
| `FOREIGN KEY` | Value must exist in the referenced table |
| `CHECK` | Value satisfies a condition |
| `DEFAULT` | Value used when none supplied |

**Name your constraints** (`CONSTRAINT PK_Product PRIMARY KEY`) so error messages and `ALTER` statements are readable.

### 3. Foreign Key Actions

`ON DELETE` / `ON UPDATE` can be `NO ACTION` (default, block the change), `CASCADE` (apply to children too), `SET NULL` or `SET DEFAULT`. Use `CASCADE` carefully: deleting one category could silently delete hundreds of products.

### 4. IDENTITY and Computed Columns

- `IDENTITY(seed, increment)` auto-numbers rows. Read the last value with `SCOPE_IDENTITY()`.
- A **computed column** derives its value: `LineTotal AS (Qty * UnitPrice)`. Add `PERSISTED` to store it physically.

### 5. Changing Tables

| Task | Statement |
|---|---|
| Add a column | `ALTER TABLE t ADD col type NULL;` |
| Change type/size | `ALTER TABLE t ALTER COLUMN col NVARCHAR(200) NOT NULL;` |
| Rename a column | `EXEC sp_rename 't.old', 'new', 'COLUMN';` |
| Drop a column | `ALTER TABLE t DROP COLUMN col;` (drop its constraints first) |
| Add constraint | `ALTER TABLE t ADD CONSTRAINT CK_x CHECK (...);` |
| Drop table | `DROP TABLE IF EXISTS t;` (children before parents) |

## 💻 Code Examples

File: `shop_tables.sql`

```sql
USE CampusDB;   -- any practice database works
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
```

**How it works**

- Every constraint has a readable name such as `CK_Product_Price`.
- `DEFAULT SYSDATETIME()` stamps the creation time automatically.
- `LineTotal` is a persisted computed column, so it can never disagree with `Qty` and `UnitPrice`.
- Tables are dropped child-first (`OrderLine` before `Product` before `Category`).

File: `alter_tables.sql`

```sql
INSERT INTO dbo.Category (Name) VALUES (N'Stationery'), (N'Electronics');
INSERT INTO dbo.Product (Sku, Name, Price, CategoryId)
VALUES ('ST-00001', N'Gel Pen', 60, 1), ('EL-00001', N'USB Cable', 450, 2);
SELECT SCOPE_IDENTITY() AS LastProductId;

-- Test a constraint (fails with CK_Product_Price)
-- INSERT INTO dbo.Product (Sku, Name, Price, CategoryId) VALUES ('ST-00002', N'Free Pen', 0, 1);

ALTER TABLE dbo.Product ADD Discount DECIMAL(4,2) NULL
    CONSTRAINT CK_Product_Discount CHECK (Discount BETWEEN 0 AND 0.5);
ALTER TABLE dbo.Product ALTER COLUMN Name NVARCHAR(150) NOT NULL;
EXEC sp_rename 'dbo.Product.InStock', 'IsAvailable', 'COLUMN';

ALTER TABLE dbo.Product DROP CONSTRAINT CK_Product_Discount;
ALTER TABLE dbo.Product DROP COLUMN Discount;
```

**How it works**

- `SCOPE_IDENTITY()` returns the last identity value created in this scope.
- A column with a constraint cannot be dropped until the constraint is dropped.
- `sp_rename` renames objects without recreating them (update any code that uses the old name).

## 🧪 Lab Practice

1. Run `shop_tables.sql`, then expand *Keys* and *Constraints* in Object Explorer to see the names you gave.
2. Try inserting a product with `Price = 0`, a duplicate `Sku`, and a non-existent `CategoryId`. Record each error message.
3. Add a `Supplier` table and a nullable `SupplierId` foreign key on `Product` with `ON DELETE SET NULL`.
4. Insert two order lines and check that `LineTotal` is calculated.
5. Use `sp_help 'dbo.Product'` to list all columns and constraints.

## 📝 Assignment

Create tables for an **online course platform**: `Instructor`, `Course`, `Lesson`, `Learner`, `Purchase`. Use at least one of each constraint type, one computed column, one `UNIQUEIDENTIFIER` and one foreign key with `ON DELETE CASCADE` (justify it in a comment). Then write three `ALTER TABLE` changes.

## ❓ Quick Quiz

1. Which type would you use for a CNIC stored as `4210112345671`?
2. What does `PERSISTED` do on a computed column?
3. Why name constraints explicitly?
4. In which order must you drop `Category` and `Product`?
5. Which function returns the last identity value in the current scope?

<details>
<summary>Show answers</summary>

1. `CHAR(13)` (it is an identifier, not a number for maths).
2. Stores the computed value physically so it can be indexed and read faster.
3. Clear error messages and easy `ALTER`/`DROP` scripts.
4. `Product` first (child), then `Category` (parent).
5. `SCOPE_IDENTITY()`.

</details>

## 💼 Interview Questions

1. **`CHAR` vs `VARCHAR`?** `CHAR(n)` always uses n characters (padded), good for fixed codes; `VARCHAR(n)` uses only the length stored plus 2 bytes.
2. **What is the difference between `SCOPE_IDENTITY()`, `@@IDENTITY` and `IDENT_CURRENT()`?** Scope-limited, session-wide (affected by triggers), and last value for a table in any session respectively.
3. **Can a foreign key reference a UNIQUE column instead of a primary key?** Yes, any column with a primary key or unique constraint.

## ✅ Summary

- Choose the smallest exact type that fits; `NVARCHAR` for text, `DECIMAL` for money.
- Constraints make the database guard its own data.
- `IDENTITY` auto-numbers; computed columns derive values.
- `ALTER TABLE` changes structure; drop constraints before columns and children before parents.

---

[⬅ Previous](../Session-05-Creating-and-Managing-Databases/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-07-Azure-SQL-and-Accessing-Data/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
