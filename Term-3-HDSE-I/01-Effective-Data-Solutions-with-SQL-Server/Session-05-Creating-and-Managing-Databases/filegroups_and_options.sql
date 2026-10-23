-- Session 05: Filegroups, extra files and options
ALTER DATABASE SalesDB ADD FILEGROUP ARCHIVE;
GO
ALTER DATABASE SalesDB ADD FILE
(   NAME = SalesDB_Archive1,
    FILENAME = 'C:\SQLData\SalesDB_Archive1.ndf',
    SIZE = 32MB, FILEGROWTH = 32MB )
TO FILEGROUP ARCHIVE;
GO
ALTER DATABASE SalesDB ADD LOG FILE
(   NAME = SalesDB_Log2, FILENAME = 'C:\SQLData\SalesDB_log2.ldf', SIZE = 16MB );
GO
ALTER DATABASE SalesDB SET RECOVERY SIMPLE;
GO
USE SalesDB;
GO
CREATE TABLE dbo.OldInvoice (InvoiceId INT PRIMARY KEY, Amount DECIMAL(10,2)) ON ARCHIVE;
INSERT INTO dbo.OldInvoice VALUES (1, 1500), (2, 2750.50), (3, 990);
SELECT name, type_desc, physical_name, size * 8 / 1024 AS SizeMB FROM sys.database_files;
SELECT name, type_desc FROM sys.filegroups;
GO
-- A second log file rarely helps; remove it again (it must be empty)
ALTER DATABASE SalesDB REMOVE FILE SalesDB_Log2;
GO
