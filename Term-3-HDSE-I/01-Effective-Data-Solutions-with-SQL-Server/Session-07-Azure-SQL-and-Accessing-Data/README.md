# Session 07: Azure SQL and Accessing Data with SELECT

> Module: Effective Data Solutions with SQL Server · Term 3 (HDSE I) · ⏱ ~2 hours

## 🎯 Learning Objectives

- Explain Azure SQL and its three deployment options
- Compare Azure SQL with on-premises SQL Server
- Connect SSMS to an Azure SQL Database
- Write `SELECT` queries with `WHERE`, `ORDER BY`, `TOP`, `DISTINCT`, `OFFSET/FETCH` and aliases
- Store and query XML using untyped and typed (schema-bound) `XML` columns
- Create and inspect an XML schema collection

## 📖 Concepts Explained

### 1. Azure SQL Family

**Azure SQL** is SQL Server's engine offered as a cloud service by Microsoft Azure.

| Option | What you manage | Best for |
|---|---|---|
| **Azure SQL Database** | Only your database (PaaS) | New cloud apps, serverless/auto-scale |
| **Azure SQL Managed Instance** | A full instance (PaaS) with SQL Agent, cross-db queries | Lifting existing SQL Server apps to the cloud |
| **SQL Server on Azure VM** | Whole VM and OS (IaaS) | Full control, legacy features |

**Benefits:** automatic backups and patching, built-in high availability (99.99% SLA), elastic scaling, geo-replication, threat detection, pay-as-you-go.

### 2. Azure SQL vs On-Premises

| Area | On-premises SQL Server | Azure SQL Database |
|---|---|---|
| Hardware | You buy and maintain | Microsoft manages |
| Patching/backups | Your job | Automatic |
| Scaling | Buy new hardware | Change service tier in minutes |
| Features | Everything (Agent, CLR, filestream) | Most T-SQL; no `USE` between DBs, no SQL Agent |
| Cost model | Licence + hardware | Per hour/vCore or DTU, serverless option |

### 3. Connecting SSMS to Azure SQL

1. In the Azure portal create a **SQL Database** (choose the free offer or Basic tier) with a new logical server.
2. Under *Networking*, add your client IP to the **firewall rules**.
3. In SSMS, server name: `yourserver.database.windows.net`, authentication: *SQL Server Authentication* or *Microsoft Entra*.
4. Under *Options → Connection Properties* pick the database name if you are not an admin of `master`.

### 4. SELECT in Depth

```text
SELECT [DISTINCT] [TOP (n)] column_list
FROM   table
WHERE  row_filter
ORDER BY columns [ASC|DESC]
OFFSET n ROWS FETCH NEXT m ROWS ONLY;
```

| Clause | Purpose |
|---|---|
| Column alias `AS` | Rename output column |
| `DISTINCT` | Remove duplicate rows |
| `TOP (n)` / `TOP (n) PERCENT` / `WITH TIES` | Limit rows |
| `WHERE` with `LIKE`, `IN`, `BETWEEN` | Filter rows |
| `ORDER BY` | Sort; can use alias or column position |
| `OFFSET ... FETCH` | Paging (needs `ORDER BY`) |
| `SELECT ... INTO NewTable` | Create a table from a result |

### 5. XML in SQL Server

The `XML` data type stores well-formed XML documents or fragments.

- **Untyped XML** – any well-formed XML is accepted.
- **Typed XML** – bound to an **XML schema collection** (XSD); values are validated.

Query XML with methods: `.value()` (single scalar), `.query()` (XML fragment), `.exist()` (1/0), `.nodes()` (shred into rows).

## 💻 Code Examples

File: `select_queries.sql` (AdventureWorks2022)

```sql
USE AdventureWorks2022;
GO
SELECT DISTINCT Color FROM Production.Product WHERE Color IS NOT NULL ORDER BY Color;

SELECT TOP (10) WITH TIES Name, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC;

SELECT ProductID, Name AS ProductName, ListPrice * 280 AS PricePKR
FROM Production.Product
WHERE Name LIKE N'%Bike%' AND ListPrice BETWEEN 500 AND 2000
ORDER BY PricePKR;

-- Page 3 with 20 rows per page
SELECT BusinessEntityID, FirstName, LastName
FROM Person.Person
ORDER BY LastName, FirstName
OFFSET 40 ROWS FETCH NEXT 20 ROWS ONLY;
```

**How it works**

- `WITH TIES` also returns rows tied with the 10th price.
- `PricePKR` is a calculated column (using an example exchange rate of 280) and is used in `ORDER BY`.
- `OFFSET 40` skips pages 1 and 2; `FETCH NEXT 20` returns page 3.

File: `xml_demo.sql`

```sql
USE CampusDB;
GO
CREATE XML SCHEMA COLLECTION dbo.ResumeSchema AS N'
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="resume">
    <xs:complexType><xs:sequence>
      <xs:element name="skill" type="xs:string" maxOccurs="unbounded"/>
      <xs:element name="experience" type="xs:int"/>
    </xs:sequence></xs:complexType>
  </xs:element>
</xs:schema>';
GO
CREATE TABLE dbo.Applicant (
    ApplicantId INT IDENTITY PRIMARY KEY,
    Name     NVARCHAR(80),
    Notes    XML,                         -- untyped
    Resume   XML(dbo.ResumeSchema)        -- typed
);
INSERT INTO dbo.Applicant (Name, Notes, Resume) VALUES
(N'Sara', N'<note>Strong SQL</note>',
 N'<resume><skill>SQL</skill><skill>C#</skill><experience>2</experience></resume>');

SELECT Name,
       Resume.value('(/resume/experience)[1]', 'int') AS Years,
       Resume.exist('/resume/skill[.="C#"]')          AS KnowsCSharp
FROM dbo.Applicant;

SELECT a.Name, s.x.value('.', 'nvarchar(50)') AS Skill
FROM dbo.Applicant a
CROSS APPLY a.Resume.nodes('/resume/skill') AS s(x);
```

**How it works**

- The schema collection defines what a valid `<resume>` looks like; inserting `<resume><age>5</age></resume>` would fail.
- `.value()` needs an XPath that returns one node, hence `[1]`, and a SQL type.
- `.nodes()` with `CROSS APPLY` turns each `<skill>` into its own row.
- View schemas with `SELECT * FROM sys.xml_schema_collections;`.

## 🧪 Lab Practice

1. (Optional, free tier) Create an Azure SQL Database with the *AdventureWorksLT* sample and connect from SSMS.
2. List the 15 most recent orders from `Sales.SalesOrderHeader` showing order number, date and total due.
3. Show distinct job titles from `HumanResources.Employee` sorted alphabetically.
4. Build paging: page 5 of products, 10 per page, ordered by name.
5. Insert an applicant whose resume breaks the schema and read the validation error.

## 📝 Assignment

Write `product_report.sql` that produces three reports on AdventureWorks: (a) top 5 heaviest products with `WITH TIES`, (b) products whose name starts with "HL" priced between 100 and 1500, (c) a `SELECT INTO` that copies black products into a new table `dbo.BlackProducts`. Add a typed XML column to that table holding specifications and query it with `.value()`.

## ❓ Quick Quiz

1. Which Azure SQL option is closest to a full SQL Server instance?
2. What must you configure in Azure before SSMS can connect?
3. Which clause is required for `OFFSET ... FETCH`?
4. Difference between typed and untyped XML?
5. Which XML method returns 1 or 0?

<details>
<summary>Show answers</summary>

1. Azure SQL Managed Instance.
2. A server firewall rule allowing your IP.
3. `ORDER BY`.
4. Typed XML is validated against an XML schema collection; untyped only needs to be well-formed.
5. `.exist()`.

</details>

## 💼 Interview Questions

1. **What is DTU vs vCore in Azure SQL?** DTU bundles CPU, memory and I/O into one measure; vCore lets you choose compute and storage separately.
2. **How do you implement paging in SQL Server?** `ORDER BY ... OFFSET @skip ROWS FETCH NEXT @take ROWS ONLY`.
3. **When would you store XML in a column?** For semi-structured data whose shape varies (settings, documents), when you still want to query parts of it in SQL.

## ✅ Summary

- Azure SQL offers SQL Database, Managed Instance and SQL on VM.
- Cloud brings automatic backups, HA and scaling; connect after setting firewall rules.
- `SELECT` supports aliases, `DISTINCT`, `TOP`, filtering, sorting and paging.
- `XML` columns can be typed with a schema collection and queried with XQuery methods.

---

[⬅ Previous](../Session-06-Creating-and-Managing-Tables/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Lab-Review-Databases-Tables-Queries/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
