# Module 01: Effective Data Solutions with SQL Server

![SQL Server](https://img.shields.io/badge/SQL%20Server-2022-CC2927?logo=microsoftsqlserver&logoColor=white)
![T-SQL](https://img.shields.io/badge/Language-T--SQL-0078D4)
![SSMS](https://img.shields.io/badge/Tool-SSMS%2020-5C2D91)
![Azure SQL](https://img.shields.io/badge/Cloud-Azure%20SQL-0089D6?logo=microsoftazure&logoColor=white)
![Sessions](https://img.shields.io/badge/Sessions-16-success)

> Term 3 (HDSE I) · 16 sessions × 2 hours · Skill: designing, building, querying and tuning relational databases

## What You Will Learn

- Model real business data with E-R diagrams and normalize it to 3NF
- Install and work with SQL Server 2022, SSMS and Azure SQL
- Create databases, filegroups, snapshots, tables and constraints with T-SQL
- Query data with `SELECT`, joins, subqueries, CTEs, grouping, pivoting and window functions
- Package logic in views, stored procedures, functions and triggers
- Speed up queries with indexes and Query Store
- Protect data with transactions, isolation levels and structured error handling
- Explore PolyBase, Intelligent Query Processing and Python ML inside SQL Server

## Prerequisites

- Comfortable using Windows and a text editor
- Basic idea of tables (spreadsheets) and of programming logic from Terms 1–2 (MySQL experience helps a lot)

## Tools to Install

| Tool | Why | Link |
|---|---|---|
| SQL Server 2022 Developer Edition | Free full-featured engine | https://www.microsoft.com/sql-server/sql-server-downloads |
| SQL Server Management Studio (SSMS) | Main IDE for this module | https://learn.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms |
| AdventureWorks2022 sample database | Realistic practice data | https://learn.microsoft.com/sql/samples/adventureworks-install-configure |
| Azure free account (optional) | Azure SQL sessions | https://azure.microsoft.com/free/ |
| VS Code + MSSQL extension (optional) | Lightweight editor, works on macOS/Linux | https://learn.microsoft.com/sql/tools/visual-studio-code/sql-server-develop-use-vscode |

> On macOS or Linux, run SQL Server 2022 in Docker: https://learn.microsoft.com/sql/linux/quickstart-install-connect-docker

## Session Index

| Session | Topic | Link |
|:---:|---|---|
| 01 | RDBMS Concepts, E-R Model and Normalization | [Open notes](./Session-01-RDBMS-ER-Model-and-Normalization/README.md) |
| 02 | Introduction to SQL Server 2022 | [Open notes](./Session-02-Introduction-to-SQL-Server-2022/README.md) |
| 03 | Transact-SQL Fundamentals | [Open notes](./Session-03-Transact-SQL-Fundamentals/README.md) |
| 04 | Lab and Review: Database Foundations | [Open notes](./Session-04-Lab-Review-Database-Foundations/README.md) |
| 05 | Creating and Managing Databases | [Open notes](./Session-05-Creating-and-Managing-Databases/README.md) |
| 06 | Creating and Managing Tables | [Open notes](./Session-06-Creating-and-Managing-Tables/README.md) |
| 07 | Azure SQL and Accessing Data with SELECT | [Open notes](./Session-07-Azure-SQL-and-Accessing-Data/README.md) |
| 08 | Lab and Review: Databases, Tables and Queries | [Open notes](./Session-08-Lab-Review-Databases-Tables-Queries/README.md) |
| 09 | Advanced Queries, Joins, Views and Stored Procedures | [Open notes](./Session-09-Advanced-Queries-Joins-Views-Procedures/README.md) |
| 10 | Indexes | [Open notes](./Session-10-Indexes/README.md) |
| 11 | Triggers | [Open notes](./Session-11-Triggers/README.md) |
| 12 | Lab and Review: Queries, Indexes and Triggers | [Open notes](./Session-12-Lab-Review-Queries-Indexes-Triggers/README.md) |
| 13 | Programming Transact-SQL | [Open notes](./Session-13-Programming-Transact-SQL/README.md) |
| 14 | Transactions and Error Handling | [Open notes](./Session-14-Transactions-and-Error-Handling/README.md) |
| 15 | PolyBase, Query Store and Machine Learning in SQL Server | [Open notes](./Session-15-PolyBase-Query-Store-and-ML/README.md) |
| 16 | Lab and Review: Programming, Transactions and Performance | [Open notes](./Session-16-Lab-Review-Programming-Transactions-Performance/README.md) |

## Module Mini-Project: Campus Management Database

Build `CampusDB` into a complete backend for a training campus:

1. **Design** – E-R diagram for departments, students, faculty, courses, batches, enrollments, attendance and fees (3NF).
2. **Build** – database with a separate filegroup for attendance history, all tables with named constraints.
3. **Data** – at least 20 students, 6 courses and 3 months of attendance (use `GENERATE_SERIES`).
4. **Query** – views for results, attendance percentage and fee defaulters; a `ROLLUP` report by department.
5. **Logic** – procedures `usp_EnrollStudent`, `usp_MarkAttendance`, `usp_CollectFee` with transactions and `TRY...CATCH`.
6. **Protect** – an audit trigger on marks and a soft-delete trigger on students.
7. **Tune** – two indexes with before/after `STATISTICS IO` evidence.
8. **Present** – a `README.md` with the diagram, how to run the scripts, and screenshots.

## Resources (Official Documentation)

- SQL Server documentation: https://learn.microsoft.com/sql/sql-server/
- T-SQL reference: https://learn.microsoft.com/sql/t-sql/language-reference
- What's new in SQL Server 2022: https://learn.microsoft.com/sql/sql-server/what-s-new-in-sql-server-2022
- Azure SQL documentation: https://learn.microsoft.com/azure/azure-sql/
- Query Store: https://learn.microsoft.com/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store
- PolyBase: https://learn.microsoft.com/sql/relational-databases/polybase/polybase-guide
- Machine Learning Services: https://learn.microsoft.com/sql/machine-learning/sql-server-machine-learning-services

---

[🏠 Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
