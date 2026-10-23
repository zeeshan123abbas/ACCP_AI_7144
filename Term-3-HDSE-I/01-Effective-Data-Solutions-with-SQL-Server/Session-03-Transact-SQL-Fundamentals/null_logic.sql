-- Session 03: NULL and logical processing order
USE CampusDB;
GO
SELECT * FROM Enrollment WHERE Marks = NULL;   -- 0 rows (UNKNOWN)
SELECT * FROM Enrollment WHERE Marks IS NULL;  -- correct

SELECT StudentId, Marks * 1.1 AS Curved
FROM Enrollment
WHERE Marks * 1.1 > 80
ORDER BY Curved DESC;
GO
