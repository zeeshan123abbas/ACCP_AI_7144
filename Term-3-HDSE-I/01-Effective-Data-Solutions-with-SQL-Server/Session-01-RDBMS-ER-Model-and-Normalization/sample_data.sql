-- Session 01: Sample rows for CampusDB (run after campus_schema.sql)
USE CampusDB;
GO
INSERT INTO Department (Name) VALUES (N'Computer Science'), (N'Information Technology'), (N'Data Science');

INSERT INTO Student (FullName, Email, DepartmentId) VALUES
 (N'Ayesha Khan',  N'ayesha@campus.pk', 1),
 (N'Bilal Ahmed',  N'bilal@campus.pk',  2),
 (N'Sana Raza',    N'sana@campus.pk',   1),
 (N'Hamza Siddiqui', N'hamza@campus.pk', 3);

INSERT INTO Course (CourseCode, Title, CreditHours) VALUES
 ('SQL101', N'Database Fundamentals', 3),
 ('CS201',  N'Object-Oriented Programming', 4),
 ('DS110',  N'Intro to Data Science', 3);

INSERT INTO Enrollment (StudentId, CourseCode, Marks) VALUES
 (1, 'SQL101', 88), (1, 'CS201', 75), (2, 'SQL101', 91),
 (3, 'CS201', 67), (4, 'DS110', NULL);
GO

-- Restrict (rows) + Project (columns)
SELECT FullName, Email FROM Student WHERE DepartmentId = 1;
