-- Session 15: PolyBase external table over CSV files in S3-compatible storage
-- Replace the bucket URL and keys with your own values before running.
EXEC sp_configure 'polybase enabled', 1; RECONFIGURE;
GO
USE CampusDB;
GO
IF NOT EXISTS (SELECT 1 FROM sys.symmetric_keys WHERE name = '##MS_DatabaseMasterKey##')
    CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Str0ng!MasterKey#2026';
GO
CREATE DATABASE SCOPED CREDENTIAL S3Cred
WITH IDENTITY = 'S3 Access Key', SECRET = '<access_key_id>:<secret_key_id>';
GO
CREATE EXTERNAL DATA SOURCE SalesFiles
WITH (LOCATION = 's3://my-bucket.s3.example.com/sales', CREDENTIAL = S3Cred);
GO
CREATE EXTERNAL FILE FORMAT CsvFormat
WITH (FORMAT_TYPE = DELIMITEDTEXT,
      FORMAT_OPTIONS (FIELD_TERMINATOR = ',', FIRST_ROW = 2));
GO
CREATE EXTERNAL TABLE dbo.ExtSales (
    SaleDate DATE, City NVARCHAR(40), Amount DECIMAL(12,2)
) WITH (LOCATION = '/2026/', DATA_SOURCE = SalesFiles, FILE_FORMAT = CsvFormat);
GO
SELECT City, SUM(Amount) AS Total FROM dbo.ExtSales GROUP BY City;
GO
