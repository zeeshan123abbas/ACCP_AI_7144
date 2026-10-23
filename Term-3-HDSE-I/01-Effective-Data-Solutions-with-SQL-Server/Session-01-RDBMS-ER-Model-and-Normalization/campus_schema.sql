-- Session 01: Campus database designed from the E-R model (3NF)
-- Run in SSMS or Azure Data Studio connected to SQL Server 2022.
IF DB_ID('CampusDB') IS NULL
    CREATE DATABASE CampusDB;
GO
USE CampusDB;
GO

CREATE TABLE Department (
    DepartmentId INT IDENTITY(1,1) PRIMARY KEY,
    Name         NVARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Student (
    StudentId    INT IDENTITY(1,1) PRIMARY KEY,
    FullName     NVARCHAR(100) NOT NULL,
    Email        NVARCHAR(120) NOT NULL UNIQUE,
    DepartmentId INT NOT NULL REFERENCES Department(DepartmentId)
);

CREATE TABLE Course (
    CourseCode  CHAR(6) PRIMARY KEY,
    Title       NVARCHAR(100) NOT NULL,
    CreditHours TINYINT NOT NULL CHECK (CreditHours BETWEEN 1 AND 6)
);

CREATE TABLE Enrollment (
    StudentId  INT     NOT NULL REFERENCES Student(StudentId),
    CourseCode CHAR(6) NOT NULL REFERENCES Course(CourseCode),
    Marks      DECIMAL(5,2) NULL CHECK (Marks BETWEEN 0 AND 100),
    PRIMARY KEY (StudentId, CourseCode)
);
GO
