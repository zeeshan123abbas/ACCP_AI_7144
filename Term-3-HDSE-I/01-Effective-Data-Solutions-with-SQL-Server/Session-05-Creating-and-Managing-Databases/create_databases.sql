-- Session 05: Create databases (adjust C:\SQLData to an existing folder)
USE master;
GO
CREATE DATABASE QuickDB;
GO
CREATE DATABASE SalesDB
ON PRIMARY
(   NAME = SalesDB_Data,
    FILENAME = 'C:\SQLData\SalesDB.mdf',
    SIZE = 64MB, MAXSIZE = 1GB, FILEGROWTH = 64MB )
LOG ON
(   NAME = SalesDB_Log,
    FILENAME = 'C:\SQLData\SalesDB_log.ldf',
    SIZE = 32MB, FILEGROWTH = 32MB );
GO
SELECT name, recovery_model_desc, compatibility_level FROM sys.databases WHERE name IN ('QuickDB','SalesDB');
GO
