# Session 13: Programming Transact-SQL

> Module: Effective Data Solutions with SQL Server · Term 3 (HDSE I) · ⏱ ~2 hours

## 🎯 Learning Objectives

- Write T-SQL programs with variables, batches and control-of-flow statements
- Use `IF...ELSE`, `WHILE`, `BREAK`, `CONTINUE`, `BEGIN...END`, `WAITFOR` and `RETURN`
- Apply built-in string, date, maths, conversion and logical functions
- Create and alter scalar and table-valued user-defined functions (UDFs)
- Define windows with `OVER (PARTITION BY ... ORDER BY ...)`
- Use ranking, offset and aggregate window functions

## 📖 Concepts Explained

### 1. T-SQL as a Programming Language

T-SQL lets you write small programs that run on the server: declare variables, branch, loop, and call functions. Keep in mind that **set-based** queries (one statement for many rows) are almost always faster than row-by-row loops. Use loops for admin tasks, not for processing table data.

### 2. Program Flow Statements

| Statement | Purpose |
|---|---|
| `BEGIN ... END` | Group statements into a block |
| `IF ... ELSE` | Branch on a condition |
| `WHILE` | Repeat while a condition is true |
| `BREAK` / `CONTINUE` | Leave / skip to next loop iteration |
| `RETURN` | Exit a batch or procedure (optionally with an int status) |
| `WAITFOR DELAY '00:00:05'` | Pause |
| `GOTO label` | Jump (avoid; hard to read) |
| `TRY...CATCH` | Error handling (next session) |

### 3. Built-in Function Families

| Family | Examples |
|---|---|
| String | `LEN`, `LEFT`, `RIGHT`, `SUBSTRING`, `CHARINDEX`, `REPLACE`, `TRIM`, `UPPER`, `STRING_AGG`, `STRING_SPLIT`, `FORMAT` |
| Date | `GETDATE`, `SYSDATETIME`, `DATEADD`, `DATEDIFF`, `DATEPART`, `EOMONTH`, `DATETRUNC` (2022), `DATE_BUCKET` (2022) |
| Math | `ROUND`, `CEILING`, `FLOOR`, `ABS`, `POWER`, `SQRT`, `RAND` |
| Conversion | `CAST`, `CONVERT`, `TRY_CAST`, `TRY_CONVERT`, `PARSE` |
| Logical | `IIF`, `CHOOSE`, `COALESCE`, `NULLIF`, `ISNULL`, `GREATEST`, `LEAST` (2022) |
| System | `@@ROWCOUNT`, `@@SPID`, `NEWID`, `DB_NAME`, `SUSER_SNAME` |

### 4. User-Defined Functions

| Type | Returns | Called as |
|---|---|---|
| Scalar | One value | `SELECT dbo.fn_Grade(Marks)` |
| Inline table-valued (iTVF) | A table from one `SELECT` | `SELECT * FROM dbo.fn_TopStudents(5)` |
| Multi-statement TVF | A table variable filled by several statements | Same as iTVF |

Rules: functions cannot change data (`INSERT/UPDATE` on real tables), cannot use `TRY...CATCH` or `NEWID()` directly, and must be deterministic where used in indexes. **Inline TVFs perform best** because the optimizer expands them like a view. SQL Server 2019+ can also *inline* simple scalar UDFs automatically.

### 5. Window Functions

A **window function** computes a value for each row using a set (window) of related rows — **without collapsing rows** like `GROUP BY` does.

```text
function(...) OVER (
    [PARTITION BY col]          -- split into groups
    [ORDER BY col]              -- order inside each group
    [ROWS BETWEEN ... AND ...]  -- frame for running totals
)
```

| Category | Functions |
|---|---|
| Ranking | `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE(n)` |
| Offset | `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE` |
| Aggregate | `SUM`, `AVG`, `COUNT`, `MIN`, `MAX` with `OVER` |

`RANK` leaves gaps after ties (1,1,3); `DENSE_RANK` does not (1,1,2). SQL Server 2022 adds the `WINDOW` clause to name and reuse a window definition.

## 💻 Code Examples

File: `flow_and_functions.sql`

```sql
DECLARE @i INT = 1, @Report NVARCHAR(200) = N'';
WHILE @i <= 10
BEGIN
    IF @i % 2 = 0 BEGIN SET @i += 1; CONTINUE; END;   -- skip even numbers
    IF @i > 7 BREAK;
    SET @Report += CONCAT(@i, N' ');
    SET @i += 1;
END;
PRINT N'Odd numbers up to 7: ' + @Report;

SELECT UPPER(LEFT(N'zeeshan', 1)) + SUBSTRING(N'zeeshan', 2, 50) AS Capitalised,
       CHARINDEX('@', 'student@aptech.pk') AS AtPosition,
       FORMAT(1234567.891, 'N2')           AS Formatted,
       EOMONTH('2026-02-10')               AS MonthEnd,
       DATETRUNC(MONTH, SYSDATETIME())     AS MonthStart,
       TRY_CAST('12a' AS INT)              AS SafeCast,
       GREATEST(4, 19, 7)                  AS Biggest,
       COALESCE(NULL, NULL, N'fallback')   AS FirstNonNull;
```

**How it works**

- `CONTINUE` jumps back to the `WHILE` test, `BREAK` leaves the loop completely.
- `TRY_CAST` returns NULL instead of failing on bad input.
- `DATETRUNC` and `GREATEST` are new in SQL Server 2022.

File: `udfs.sql` (CampusDB)

```sql
USE CampusDB;
GO
CREATE OR ALTER FUNCTION dbo.fn_Grade (@Marks DECIMAL(5,2))
RETURNS CHAR(2)
AS
BEGIN
    RETURN CASE WHEN @Marks IS NULL THEN 'NA'
                WHEN @Marks >= 85 THEN 'A'
                WHEN @Marks >= 70 THEN 'B'
                WHEN @Marks >= 55 THEN 'C'
                WHEN @Marks >= 50 THEN 'D'
                ELSE 'F' END;
END;
GO
CREATE OR ALTER FUNCTION dbo.fn_CourseRoster (@CourseCode CHAR(6))
RETURNS TABLE
AS
RETURN (
    SELECT s.FullName, e.Marks, dbo.fn_Grade(e.Marks) AS Grade
    FROM dbo.Enrollment e JOIN dbo.Student s ON s.StudentId = e.StudentId
    WHERE e.CourseCode = @CourseCode
);
GO
SELECT * FROM dbo.fn_CourseRoster('SQL101') ORDER BY Marks DESC;
```

**How it works**

- `fn_Grade` is a scalar UDF used inside another query.
- `fn_CourseRoster` is an inline TVF: one `RETURN (SELECT ...)`, used in `FROM` like a parameterised view.

File: `window_functions.sql` (AdventureWorks2022)

```sql
USE AdventureWorks2022;
GO
SELECT h.SalesPersonID, h.SalesOrderID, h.OrderDate, h.TotalDue,
       ROW_NUMBER() OVER w                                        AS RowNum,
       RANK()       OVER (PARTITION BY h.SalesPersonID ORDER BY h.TotalDue DESC) AS SizeRank,
       SUM(h.TotalDue) OVER (w ROWS UNBOUNDED PRECEDING)         AS RunningTotal,
       LAG(h.TotalDue) OVER w                                     AS PrevOrder,
       h.TotalDue - AVG(h.TotalDue) OVER (PARTITION BY h.SalesPersonID) AS DiffFromAvg
FROM Sales.SalesOrderHeader h
WHERE h.SalesPersonID IS NOT NULL
WINDOW w AS (PARTITION BY h.SalesPersonID ORDER BY h.OrderDate, h.SalesOrderID);
```

**How it works**

- `WINDOW w AS (...)` (SQL Server 2022, compatibility level 160) defines the window once.
- `ROWS UNBOUNDED PRECEDING` makes `SUM` a running total per salesperson.
- `LAG` reads the previous order's value; `AVG ... OVER (PARTITION BY ...)` compares each order with that person's average — all without `GROUP BY`.

## 🧪 Lab Practice

1. Write a `WHILE` loop that prints the multiplication table of 7.
2. Using string functions, split `'Ali Raza Khan'` into first and last name (`LEFT`, `CHARINDEX`, `RIGHT`).
3. Create `dbo.fn_AgeInYears(@Dob DATE)` and test it with several dates.
4. Return the top 3 products by price **per subcategory** using `DENSE_RANK` in a CTE.
5. Show monthly sales and the month-over-month change using `LAG`.

## 📝 Assignment

For CampusDB: create an inline TVF `fn_DepartmentToppers(@DepartmentId INT, @Top INT)` that uses `ROW_NUMBER` to return the top N students by average marks in that department, plus a scalar function that converts marks to GPA points. Include test calls.

## ❓ Quick Quiz

1. What is the difference between `RANK` and `DENSE_RANK`?
2. Which UDF type usually performs best?
3. What does `TRY_CONVERT` return on failure?
4. Does a window function reduce the number of rows returned?
5. Which keyword skips to the next loop iteration?

<details>
<summary>Show answers</summary>

1. `RANK` leaves gaps after ties, `DENSE_RANK` does not.
2. Inline table-valued function.
3. NULL.
4. No; every row stays, with an extra computed column.
5. `CONTINUE`.

</details>

## 💼 Interview Questions

1. **How do you get the second-highest salary per department?** `DENSE_RANK() OVER (PARTITION BY Dept ORDER BY Salary DESC)` in a CTE, then filter `= 2`.
2. **Why avoid scalar UDFs on large tables (pre-2019)?** They ran once per row and blocked parallelism; inline TVFs or expressions are faster.
3. **`ISNULL` vs `COALESCE`?** `ISNULL` takes two arguments and uses the first one's type; `COALESCE` is ANSI, takes many arguments and uses type precedence.

## ✅ Summary

- T-SQL supports blocks, branching and loops, but prefer set-based logic.
- A rich library of string, date, math, conversion and logical functions is built in.
- UDFs package reusable logic; inline TVFs are the fastest kind.
- Window functions (`OVER`) rank, compare and total rows without grouping them away.

---

[⬅ Previous](../Session-12-Lab-Review-Queries-Indexes-Triggers/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-14-Transactions-and-Error-Handling/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
