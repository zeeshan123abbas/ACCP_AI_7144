-- Session 13: Scalar and inline table-valued functions (CampusDB)
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
SELECT dbo.fn_Grade(72.5) AS SampleGrade;
SELECT * FROM dbo.fn_CourseRoster('SQL101') ORDER BY Marks DESC;
GO
