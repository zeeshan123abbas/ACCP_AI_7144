-- Session 14: Save points, marks, @@ERROR, RAISERROR and isolation
USE CampusDB;
GO
BEGIN TRAN OrderBatch WITH MARK 'Daily order import';
    INSERT INTO dbo.Account VALUES ('A003', N'Kiran', 1000);
    SAVE TRAN BeforeBonus;
    UPDATE dbo.Account SET Balance += 500;
    ROLLBACK TRAN BeforeBonus;
    SELECT @@TRANCOUNT AS OpenTrans;
COMMIT;
GO
UPDATE dbo.Account SET Balance = -1 WHERE AccountNo = 'A003';
IF @@ERROR <> 0
    RAISERROR(N'Update failed for account %s', 16, 1, 'A003');
GO
ALTER DATABASE CampusDB SET ALLOW_SNAPSHOT_ISOLATION ON;
GO
SET TRANSACTION ISOLATION LEVEL SNAPSHOT;
BEGIN TRAN;
    SELECT * FROM dbo.Account;   -- consistent view for the whole transaction
COMMIT;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
GO
