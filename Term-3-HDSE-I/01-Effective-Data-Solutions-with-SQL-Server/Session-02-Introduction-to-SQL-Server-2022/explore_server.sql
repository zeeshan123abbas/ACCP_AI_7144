-- Session 02: Explore your SQL Server instance
SELECT @@SERVERNAME AS ServerName,
       @@VERSION    AS VersionInfo,
       SERVERPROPERTY('Edition')        AS Edition,
       SERVERPROPERTY('ProductVersion') AS ProductVersion;
GO

SELECT name, database_id, create_date, compatibility_level
FROM sys.databases
ORDER BY name;
GO
