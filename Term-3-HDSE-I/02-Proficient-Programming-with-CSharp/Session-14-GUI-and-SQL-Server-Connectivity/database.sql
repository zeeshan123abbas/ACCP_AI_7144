-- Session 14: Database used by both examples (run in SSMS or Azure Data Studio)

-- Step 1: create the database
CREATE DATABASE AptechCollege;
GO

USE AptechCollege;
GO

-- Step 2: create a simple Students table
CREATE TABLE Students
(
    StudentId INT IDENTITY(1,1) PRIMARY KEY,   -- auto number
    FullName  NVARCHAR(100) NOT NULL,
    City      NVARCHAR(50)  NOT NULL,
    Marks     INT           NOT NULL CHECK (Marks BETWEEN 0 AND 100)
);
GO

-- Step 3: add a few sample rows
INSERT INTO Students (FullName, City, Marks) VALUES
(N'Ali Raza',   N'Karachi', 78),
(N'Sana Khan',  N'Lahore',  91),
(N'Bilal Ahmed',N'Karachi', 64);
GO

-- Step 4: a stored procedure with a parameter
CREATE PROCEDURE GetStudentsByCity
    @City NVARCHAR(50)
AS
BEGIN
    SELECT StudentId, FullName, City, Marks
    FROM Students
    WHERE City = @City
    ORDER BY FullName;
END
GO
