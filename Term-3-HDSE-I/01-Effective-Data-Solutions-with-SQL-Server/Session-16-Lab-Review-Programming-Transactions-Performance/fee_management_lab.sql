-- Session 16: Lab and Review - Fee management with procedures, transactions and windows
IF DB_ID('FeeDB') IS NULL CREATE DATABASE FeeDB;
GO
USE FeeDB;
GO
DROP TABLE IF EXISTS dbo.Payment, dbo.Learner, dbo.ErrorLog;
CREATE TABLE dbo.Learner (
    LearnerId INT IDENTITY PRIMARY KEY,
    Name      NVARCHAR(80) NOT NULL,
    FeeDue    DECIMAL(10,2) NOT NULL CHECK (FeeDue >= 0)
);
CREATE TABLE dbo.Payment (
    PaymentId INT IDENTITY(1001,1) PRIMARY KEY,
    LearnerId INT NOT NULL REFERENCES dbo.Learner(LearnerId),
    Amount    DECIMAL(10,2) NOT NULL CHECK (Amount > 0),
    PaidOn    DATE NOT NULL DEFAULT CAST(GETDATE() AS DATE)
);
CREATE TABLE dbo.ErrorLog (
    ErrorLogId INT IDENTITY PRIMARY KEY, Num INT, Msg NVARCHAR(4000),
    ProcName SYSNAME NULL, LoggedAt DATETIME2 DEFAULT SYSDATETIME()
);
GO
INSERT INTO dbo.Learner (Name, FeeDue) VALUES
 (N'Areeba', 60000), (N'Danish', 45000), (N'Mehwish', 30000), (N'Saad', 75000);
INSERT INTO dbo.Payment (LearnerId, Amount, PaidOn) VALUES
 (1, 15000, '2026-07-05'), (2, 10000, '2026-07-10'), (1, 15000, '2026-08-04'),
 (3, 30000, '2026-08-15'), (4, 20000, '2026-09-02'), (2, 10000, '2026-09-11');
UPDATE l SET FeeDue -= p.Paid
FROM dbo.Learner l JOIN (SELECT LearnerId, SUM(Amount) Paid FROM dbo.Payment GROUP BY LearnerId) p
  ON p.LearnerId = l.LearnerId;
GO
CREATE OR ALTER PROCEDURE dbo.usp_CollectFee
    @StudentId INT, @Amount DECIMAL(10,2), @ReceiptNo INT OUTPUT
AS
BEGIN
    SET NOCOUNT ON; SET XACT_ABORT ON;
    BEGIN TRY
        DECLARE @Due DECIMAL(10,2) =
            (SELECT FeeDue FROM dbo.Learner WHERE LearnerId = @StudentId);
        IF @Due IS NULL      THROW 50100, 'Learner not found.', 1;
        IF @Amount > @Due    THROW 50101, 'Payment exceeds outstanding fee.', 1;

        BEGIN TRAN;
            INSERT INTO dbo.Payment (LearnerId, Amount) VALUES (@StudentId, @Amount);
            SET @ReceiptNo = SCOPE_IDENTITY();
            UPDATE dbo.Learner SET FeeDue -= @Amount WHERE LearnerId = @StudentId;
        COMMIT;
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0 ROLLBACK;
        INSERT INTO dbo.ErrorLog (Num, Msg, ProcName)
        VALUES (ERROR_NUMBER(), ERROR_MESSAGE(), ERROR_PROCEDURE());
        THROW;
    END CATCH;
END;
GO
DECLARE @r INT;
EXEC dbo.usp_CollectFee @StudentId = 4, @Amount = 5000, @ReceiptNo = @r OUTPUT;
SELECT @r AS ReceiptNo;
GO
SELECT FORMAT(PaidOn, 'yyyy-MM') AS Month,
       SUM(Amount) AS Collected,
       SUM(SUM(Amount)) OVER (ORDER BY FORMAT(PaidOn, 'yyyy-MM')) AS RunningTotal,
       RANK() OVER (ORDER BY SUM(Amount) DESC) AS BestMonthRank
FROM dbo.Payment
GROUP BY FORMAT(PaidOn, 'yyyy-MM');

SELECT l.Name, p.PaidOn, p.Amount,
       LAG(p.PaidOn) OVER (PARTITION BY p.LearnerId ORDER BY p.PaidOn) AS PrevPayment,
       DATEDIFF(DAY, LAG(p.PaidOn) OVER (PARTITION BY p.LearnerId ORDER BY p.PaidOn), p.PaidOn) AS GapDays
FROM dbo.Payment p JOIN dbo.Learner l ON l.LearnerId = p.LearnerId;
SELECT * FROM dbo.ErrorLog;
GO
