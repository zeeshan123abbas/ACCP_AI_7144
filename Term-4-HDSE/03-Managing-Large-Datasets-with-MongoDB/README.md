# Module 03: Managing Large Datasets with MongoDB

![MongoDB 8](https://img.shields.io/badge/MongoDB-8.0-47A248?logo=mongodb&logoColor=white) ![Atlas](https://img.shields.io/badge/MongoDB_Atlas-Cloud-00ED64?logo=mongodb&logoColor=black) ![mongosh](https://img.shields.io/badge/mongosh-2.x-13AA52) ![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![PyMongo](https://img.shields.io/badge/PyMongo-4.x-47A248)

> Term 4 (HDSE) · 16 sessions × 2 hours · [⬅ Term Home](../README.md)

This module teaches you to store, query and manage large amounts of data with MongoDB, the "M" in MERN. You will master CRUD, operators and aggregation, administer databases with commands, users and roles, speed up queries with indexes, scale with replication and sharding, protect data with transactions, work in the cloud with Atlas, connect from Python and use AI to work smarter. Every concept session is followed by a practice lab with a full solution script.

## 🎯 What You Will Learn

- Install and configure MongoDB Server, mongosh and Database Tools
- Perform CRUD with rich data types, operators and aggregation pipelines
- Use database commands, shell methods, validators, users and roles
- Create and analyse indexes for fast queries
- Understand replica sets and sharding for availability and scale
- Write ACID transactions and use Compass and the BI Connector
- Deploy and administer clusters on MongoDB Atlas
- Connect from Python with PyMongo and apply AI to database work

## 📋 Prerequisites

- Basic database concepts (tables, keys) from MySQL / SQL Server
- JavaScript basics (mongosh uses JavaScript syntax)
- Python basics for Sessions 13-16

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| MongoDB Community Server 8 | local database server | [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community) |
| MongoDB Shell (mongosh) | command-line client | [https://www.mongodb.com/try/download/shell](https://www.mongodb.com/try/download/shell) |
| MongoDB Database Tools | mongoimport, mongodump, ... | [https://www.mongodb.com/try/download/database-tools](https://www.mongodb.com/try/download/database-tools) |
| MongoDB Compass | GUI client | [https://www.mongodb.com/products/tools/compass](https://www.mongodb.com/products/tools/compass) |
| MongoDB Atlas | free cloud cluster | [https://www.mongodb.com/atlas](https://www.mongodb.com/atlas) |
| Python 3.12 | PyMongo sessions | [https://www.python.org/downloads/](https://www.python.org/downloads/) |

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to MongoDB and Working with Databases | [Open notes](./Session-01-Introduction-to-MongoDB-and-Working-with-Databases/README.md) |
| 02 | Practice Lab: MongoDB Basics | [Open notes](./Session-02-Practice-Lab-MongoDB-Basics/README.md) |
| 03 | MongoDB Operators and the Aggregation Pipeline | [Open notes](./Session-03-MongoDB-Operators-and-Aggregation-Pipeline/README.md) |
| 04 | Practice Lab: Queries and Aggregation | [Open notes](./Session-04-Practice-Lab-Queries-and-Aggregation/README.md) |
| 05 | Database Commands and MongoDB Shell Methods | [Open notes](./Session-05-Database-Commands-and-MongoDB-Shell-Methods/README.md) |
| 06 | Practice Lab: Commands, Users and Roles | [Open notes](./Session-06-Practice-Lab-Commands-Users-and-Roles/README.md) |
| 07 | MongoDB Indexing, Replication and Sharding | [Open notes](./Session-07-MongoDB-Indexing-Replication-and-Sharding/README.md) |
| 08 | Practice Lab: Indexes and Replica Sets | [Open notes](./Session-08-Practice-Lab-Indexes-and-Replica-Sets/README.md) |
| 09 | Transaction Management and MongoDB Tools | [Open notes](./Session-09-Transaction-Management-and-MongoDB-Tools/README.md) |
| 10 | Practice Lab: Transactions and Tools | [Open notes](./Session-10-Practice-Lab-Transactions-and-Tools/README.md) |
| 11 | MongoDB in the Cloud with Atlas | [Open notes](./Session-11-MongoDB-Cloud-with-Atlas/README.md) |
| 12 | Practice Lab: MongoDB Atlas | [Open notes](./Session-12-Practice-Lab-Atlas/README.md) |
| 13 | MongoDB Database Connectivity with Python | [Open notes](./Session-13-MongoDB-Connectivity-with-Python/README.md) |
| 14 | Practice Lab: Python and MongoDB | [Open notes](./Session-14-Practice-Lab-Python-and-MongoDB/README.md) |
| 15 | AI-Powered MongoDB | [Open notes](./Session-15-AI-Powered-MongoDB/README.md) |
| 16 | Practice Lab: AI-Powered MongoDB and Final Review | [Open notes](./Session-16-Practice-Lab-AI-and-Final-Review/README.md) |

## 🚀 Module Mini-Project

**City Library Analytics Platform**

1. Design collections for books, members and loans (embedding vs referencing justified in the README).
2. Seed at least 5,000 documents with a script and add JSON Schema validators.
3. Create indexes for the five most common queries and prove them with `explain()`.
4. Build aggregation reports: most borrowed books, late returns per month, active members per area.
5. Implement the "issue book" operation as a transaction (update stock + insert loan).
6. Host the data on Atlas with separate admin and read-only users.
7. A Python script exports a monthly report to CSV, and an AI step summarises the aggregated figures.

## 🔗 Resources (official documentation)

- [MongoDB Manual](https://www.mongodb.com/docs/manual/)
- [mongosh documentation](https://www.mongodb.com/docs/mongodb-shell/)
- [Aggregation reference](https://www.mongodb.com/docs/manual/reference/aggregation/)
- [Indexes](https://www.mongodb.com/docs/manual/indexes/)
- [Replication](https://www.mongodb.com/docs/manual/replication/)
- [Sharding](https://www.mongodb.com/docs/manual/sharding/)
- [Transactions](https://www.mongodb.com/docs/manual/core/transactions/)
- [MongoDB Atlas docs](https://www.mongodb.com/docs/atlas/)
- [PyMongo documentation](https://pymongo.readthedocs.io/)
- [MongoDB University (free courses)](https://learn.mongodb.com/)

---

[⬅ Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
