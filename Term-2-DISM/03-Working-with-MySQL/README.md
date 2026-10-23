# Working with MySQL

![MySQL](https://img.shields.io/badge/MySQL-8.4%20LTS-4479a1?logo=mysql&logoColor=white) ![MySQL Workbench](https://img.shields.io/badge/MySQL%20Workbench-8.0-00758f?logo=mysql&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-ANSI-336791)

> Term 2 (DISM) · 12 sessions · ⏱ ~2 hours each

Every dynamic website you will build in this term stores its data in a database. This module takes you from "what is a database?" to designing normalized schemas, writing professional SQL, programming the server with procedures and triggers, and keeping a production database safe, fast and highly available. All examples use one realistic database, `institute_db`, so each session builds on the last.

## What You Will Learn

- Design relational databases with ER diagrams and normalization (1NF–3NF)
- Create databases and tables with correct data types and constraints
- Insert, query, update and delete data safely
- Combine tables with joins, set operators, subqueries and CTEs
- Write views, stored procedures, functions and triggers
- Summarise data with GROUP BY and ROLLUP and speed queries with indexes
- Use transactions, back up and restore, and manage users
- Understand replication, partitioning, storage engines and tuning

## Prerequisites

- Basic computer skills and file handling
- Logical thinking (conditions, loops) from Term 1 programming

## Tools to Install

| Tool | Purpose | Download |
|---|---|---|
| MySQL Community Server 8.4 LTS | Database server | [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/) |
| MySQL Workbench | GUI for queries, modelling and admin | [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/) |
| XAMPP (optional) | Apache + MariaDB + PHP bundle for later PHP modules | [https://www.apachefriends.org/](https://www.apachefriends.org/) |
| Visual Studio Code | Editing .sql scripts | [https://code.visualstudio.com/](https://code.visualstudio.com/) |

## Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to Databases and MySQL | [Open notes](./Session-01-Introduction-to-MySQL/README.md) |
| 02 | Database Design and Normalization | [Open notes](./Session-02-Database-Design-Normalization/README.md) |
| 03 | Data Types, Databases and Tables (DDL) | [Open notes](./Session-03-Data-Types-and-DDL/README.md) |
| 04 | Inserting and Retrieving Data | [Open notes](./Session-04-Insert-and-Select/README.md) |
| 05 | Updating, Deleting and Filtering Data | [Open notes](./Session-05-Update-Delete-Filter/README.md) |
| 06 | Joins and Combining Data | [Open notes](./Session-06-Joins-and-Set-Operators/README.md) |
| 07 | Subqueries and Common Table Expressions | [Open notes](./Session-07-Subqueries-and-CTEs/README.md) |
| 08 | Built-in Functions, Stored Procedures and Triggers | [Open notes](./Session-08-Functions-Procedures-Triggers/README.md) |
| 09 | Grouping, ROLLUP and Indexes | [Open notes](./Session-09-Grouping-Rollup-Indexes/README.md) |
| 10 | Transactions, ACID, Locking and Backups | [Open notes](./Session-10-Transactions-ACID-Backups/README.md) |
| 11 | Replication and Partitioning | [Open notes](./Session-11-Replication-and-Partitioning/README.md) |
| 12 | Performance Tuning and Storage Engines | [Open notes](./Session-12-Performance-and-Storage/README.md) |

## Module Mini-Project

**Institute Management Database.** Extend `institute_db` into a complete back-end for a training institute:

1. ER diagram and 3NF schema for students, faculty, courses, batches, enrollments, attendance and payments.
2. Seed data for at least 30 students and 8 courses.
3. 15 report queries (joins, subqueries, CTEs, GROUP BY/ROLLUP, window functions).
4. Views for result cards and fee status; procedures for admission and payment (with transactions); an audit trigger.
5. Indexes justified with EXPLAIN output.
6. A backup script and a least-privilege application user.

## Resources (Official Documentation)

- [MySQL 8.4 Reference Manual](https://dev.mysql.com/doc/refman/8.4/en/)
- [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/)
- [MySQL Tutorial (official)](https://dev.mysql.com/doc/refman/8.4/en/tutorial.html)
- [mysqldump documentation](https://dev.mysql.com/doc/refman/8.4/en/mysqldump.html)
- [Replication documentation](https://dev.mysql.com/doc/refman/8.4/en/replication.html)
- [Partitioning documentation](https://dev.mysql.com/doc/refman/8.4/en/partitioning.html)

---

[🏠 Term Home](../README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
