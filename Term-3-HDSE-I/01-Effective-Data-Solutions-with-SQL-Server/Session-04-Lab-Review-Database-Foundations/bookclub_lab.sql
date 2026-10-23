-- Session 04: Lab and Review - Karachi Book Club
IF DB_ID('BookClubDB') IS NULL CREATE DATABASE BookClubDB;
GO
USE BookClubDB;
GO
DROP TABLE IF EXISTS Loan, BookAuthor, Member, Book, Author;
GO
CREATE TABLE Author (
    AuthorId INT IDENTITY PRIMARY KEY,
    Name     NVARCHAR(80) NOT NULL
);
CREATE TABLE Book (
    BookId   INT IDENTITY PRIMARY KEY,
    Title    NVARCHAR(150) NOT NULL,
    Price    DECIMAL(8,2)  NOT NULL CHECK (Price >= 0)
);
CREATE TABLE BookAuthor (
    BookId   INT REFERENCES Book(BookId),
    AuthorId INT REFERENCES Author(AuthorId),
    PRIMARY KEY (BookId, AuthorId)
);
CREATE TABLE Member (
    MemberId INT IDENTITY PRIMARY KEY,
    Name     NVARCHAR(80) NOT NULL,
    Phone    VARCHAR(15)  NULL
);
CREATE TABLE Loan (
    LoanId     INT IDENTITY PRIMARY KEY,
    BookId     INT  NOT NULL REFERENCES Book(BookId),
    MemberId   INT  NOT NULL REFERENCES Member(MemberId),
    LoanDate   DATE NOT NULL DEFAULT CAST(GETDATE() AS DATE),
    ReturnDate DATE NULL
);
GO
INSERT INTO Author (Name) VALUES (N'Umera Ahmed'), (N'Ashfaq Ahmed'), (N'Mustansar Hussain Tarar');
INSERT INTO Book (Title, Price) VALUES (N'Peer-e-Kamil', 950), (N'Zavia', 700), (N'Bahao', 850);
INSERT INTO BookAuthor VALUES (1,1), (2,2), (3,3);
INSERT INTO Member (Name, Phone) VALUES (N'Fatima', '03001234567'), (N'Usman', NULL), (N'Zara', '03211234567');
INSERT INTO Loan (BookId, MemberId, LoanDate, ReturnDate) VALUES
 (1, 1, DATEADD(DAY, -20, CAST(GETDATE() AS DATE)), NULL),
 (2, 1, DATEADD(DAY, -5,  CAST(GETDATE() AS DATE)), NULL),
 (3, 2, DATEADD(DAY, -30, CAST(GETDATE() AS DATE)), DATEADD(DAY, -18, CAST(GETDATE() AS DATE)));
GO
DECLARE @Today DATE = CAST(GETDATE() AS DATE);
SELECT m.Name, b.Title, l.LoanDate,
       DATEDIFF(DAY, l.LoanDate, @Today) AS DaysOut,
       CASE WHEN l.ReturnDate IS NULL AND DATEDIFF(DAY, l.LoanDate, @Today) > 14
            THEN 'Overdue' WHEN l.ReturnDate IS NULL THEN 'On loan'
            ELSE 'Returned' END AS Status
FROM Loan l
JOIN Member m ON m.MemberId = l.MemberId
JOIN Book b   ON b.BookId   = l.BookId
ORDER BY Status, DaysOut DESC;
GO
