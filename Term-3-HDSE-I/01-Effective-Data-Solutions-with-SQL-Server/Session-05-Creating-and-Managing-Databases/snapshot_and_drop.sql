-- Session 05: Snapshot, revert and drop
USE master;
GO
-- One sparse file per data file of the source database
CREATE DATABASE SalesDB_Snap ON
( NAME = SalesDB_Data,     FILENAME = 'C:\SQLData\SalesDB_Data.ss' ),
( NAME = SalesDB_Archive1, FILENAME = 'C:\SQLData\SalesDB_Archive1.ss' )
AS SNAPSHOT OF SalesDB;
GO
DELETE FROM SalesDB.dbo.OldInvoice;            -- simulate a mistake
SELECT COUNT(*) AS RowsInSource FROM SalesDB.dbo.OldInvoice;
SELECT COUNT(*) AS RowsInSnapshot FROM SalesDB_Snap.dbo.OldInvoice;
GO
RESTORE DATABASE SalesDB FROM DATABASE_SNAPSHOT = 'SalesDB_Snap';
GO
SELECT COUNT(*) AS RowsAfterRevert FROM SalesDB.dbo.OldInvoice;
DROP DATABASE SalesDB_Snap;
GO
ALTER DATABASE QuickDB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
DROP DATABASE QuickDB;
GO
