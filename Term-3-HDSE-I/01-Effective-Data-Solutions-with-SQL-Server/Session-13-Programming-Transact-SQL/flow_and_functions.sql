-- Session 13: Control-of-flow and built-in functions (SQL Server 2022)
DECLARE @i INT = 1, @Report NVARCHAR(200) = N'';
WHILE @i <= 10
BEGIN
    IF @i % 2 = 0 BEGIN SET @i += 1; CONTINUE; END;
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
GO
