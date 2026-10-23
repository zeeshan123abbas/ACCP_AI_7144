-- Session 03: T-SQL language elements (requires CampusDB from Session 01)
USE CampusDB;
GO
DECLARE @PassMark DECIMAL(5,2) = 50,
        @Today    DATE = CAST(GETDATE() AS DATE),
        @City     NVARCHAR(30) = N'کراچی';

SELECT @Today AS Today, @City AS City, LEN(@City) AS Letters;
PRINT CONCAT('Pass mark is ', @PassMark);

SELECT s.FullName,
       e.CourseCode,
       e.Marks,
       e.Marks / 100 * 4 AS GradePoints,
       CONCAT(s.FullName, ' - ', e.CourseCode) AS Label,
       CASE WHEN e.Marks >= @PassMark THEN 'Pass'
            WHEN e.Marks IS NULL      THEN 'Pending'
            ELSE 'Fail' END AS Result
FROM Student AS s
JOIN Enrollment AS e ON e.StudentId = s.StudentId;
GO
