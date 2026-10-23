-- Session 08: Lab and Review - Event ticketing database
IF DB_ID('EventDB') IS NULL CREATE DATABASE EventDB;
GO
USE EventDB;
GO
DROP TABLE IF EXISTS Ticket, Event, Venue;
CREATE TABLE Venue (
    VenueId  INT IDENTITY CONSTRAINT PK_Venue PRIMARY KEY,
    Name     NVARCHAR(80) NOT NULL CONSTRAINT UQ_Venue_Name UNIQUE,
    City     NVARCHAR(40) NOT NULL CONSTRAINT DF_Venue_City DEFAULT N'Karachi',
    Capacity INT NOT NULL CONSTRAINT CK_Venue_Capacity CHECK (Capacity BETWEEN 10 AND 50000)
);
CREATE TABLE Event (
    EventId   INT IDENTITY CONSTRAINT PK_Event PRIMARY KEY,
    Title     NVARCHAR(120) NOT NULL,
    StartsAt  DATETIME2(0)  NOT NULL,
    BasePrice DECIMAL(8,2)  NOT NULL CONSTRAINT CK_Event_Price CHECK (BasePrice >= 0),
    VenueId   INT NOT NULL CONSTRAINT FK_Event_Venue REFERENCES Venue(VenueId),
    Extras    XML NULL
);
CREATE TABLE Ticket (
    TicketId  UNIQUEIDENTIFIER CONSTRAINT PK_Ticket PRIMARY KEY DEFAULT NEWID(),
    EventId   INT NOT NULL CONSTRAINT FK_Ticket_Event REFERENCES Event(EventId) ON DELETE CASCADE,
    Buyer     NVARCHAR(80) NOT NULL,
    Seats     TINYINT NOT NULL CONSTRAINT CK_Ticket_Seats CHECK (Seats BETWEEN 1 AND 10),
    PricePaid DECIMAL(8,2) NOT NULL
);
GO
INSERT INTO Venue (Name, Capacity) VALUES (N'Expo Centre Hall 1', 3000), (N'Arts Council Auditorium', 800);
INSERT INTO Venue (Name, City, Capacity) VALUES (N'Alhamra Hall', N'Lahore', 1200);

INSERT INTO Event (Title, StartsAt, BasePrice, VenueId, Extras) VALUES
 (N'Tech Career Fair', DATEADD(DAY, 7, SYSDATETIME()), 0, 1, N'<extras><parking>Free</parking><wifi>yes</wifi></extras>'),
 (N'Qawwali Night', DATEADD(DAY, 12, SYSDATETIME()), 2500, 2, N'<extras><parking>Paid</parking></extras>'),
 (N'Startup Seminar', DATEADD(DAY, 45, SYSDATETIME()), 1000, 3, NULL);

INSERT INTO Ticket (EventId, Buyer, Seats, PricePaid) VALUES
 (1, N'Ahmed', 2, 0), (2, N'Maryam', 4, 10000), (2, N'Kashif', 1, 2500);
GO
SELECT e.Title, v.Name AS Venue, e.StartsAt, e.BasePrice
FROM Event e JOIN Venue v ON v.VenueId = e.VenueId
WHERE e.StartsAt BETWEEN SYSDATETIME() AND DATEADD(DAY, 30, SYSDATETIME())
ORDER BY e.BasePrice;

SELECT Title, Extras.value('(/extras/parking)[1]', 'nvarchar(10)') AS Parking
FROM Event
WHERE Extras.exist('/extras/parking') = 1;

SELECT Buyer, Seats, PricePaid FROM Ticket ORDER BY PricePaid DESC
OFFSET 0 ROWS FETCH NEXT 2 ROWS ONLY;
GO
