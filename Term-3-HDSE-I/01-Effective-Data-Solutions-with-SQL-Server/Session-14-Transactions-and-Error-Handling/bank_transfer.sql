-- Session 14: Transactions with TRY...CATCH and THROW
USE CampusDB;
GO
DROP TABLE IF EXISTS dbo.Account;
CREATE TABLE dbo.Account (
    AccountNo CHAR(4) PRIMARY KEY,
    Holder    NVARCHAR(50),
    Balance   DECIMAL(12,2) NOT NULL CHECK (Balance >= 0)
);
INSERT INTO dbo.Account VALUES ('A001', N'Hina', 20000), ('A002', N'Omar', 5000);
GO
CREATE OR ALTER PROCEDURE dbo.usp_Transfer
    @From CHAR(4), @To CHAR(4), @Amount DECIMAL(12,2)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;
    BEGIN TRY
        IF @Amount <= 0
            THROW 50010, 'Amount must be positive.', 1;

        BEGIN TRAN;
            UPDATE dbo.Account SET Balance -= @Amount WHERE AccountNo = @From;
            IF @@ROWCOUNT = 0 THROW 50011, 'Source account not found.', 1;

            UPDATE dbo.Account SET Balance += @Amount WHERE AccountNo = @To;
            IF @@ROWCOUNT = 0 THROW 50012, 'Target account not found.', 1;
        COMMIT;
        PRINT 'Transfer complete.';
    END TRY
    BEGIN CATCH
        IF XACT_STATE() <> 0 ROLLBACK;
        SELECT ERROR_NUMBER() AS Num, ERROR_SEVERITY() AS Sev, ERROR_STATE() AS State,
               ERROR_LINE() AS Line, ERROR_PROCEDURE() AS ProcName, ERROR_MESSAGE() AS Msg;
        THROW;
    END CATCH;
END;
GO
EXEC dbo.usp_Transfer 'A001', 'A002', 3000;
GO
EXEC dbo.usp_Transfer 'A002', 'A001', 999999;   -- fails with error 547 and is rolled back
GO
SELECT * FROM dbo.Account;
GO
