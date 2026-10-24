# Module 02: Proficient Programming with C#

![C#](https://img.shields.io/badge/C%23-12-512BD4?logo=csharp&logoColor=white)
![.NET](https://img.shields.io/badge/.NET-8_LTS-512BD4?logo=dotnet&logoColor=white)
![Visual Studio](https://img.shields.io/badge/Visual_Studio-2022-5C2D91?logo=visualstudio&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-ADO.NET-CC2927?logo=microsoftsqlserver&logoColor=white)
![.NET MAUI](https://img.shields.io/badge/.NET_MAUI-8-512BD4?logo=dotnet&logoColor=white)
![Sessions](https://img.shields.io/badge/Sessions-18-success)

> Term 3 (HDSE I) · 18 sessions × 2 hours · [⬅ Term Home](../README.md)

This module takes you from your very first C# line to object-oriented design, collections, generics, LINQ, database connectivity and cross-platform apps. Every session folder contains a small **.NET 8 project** (`.csproj` + `Program.cs`) that you can run with one command. The code is deliberately short, well commented and focused on one idea at a time.

## 🎯 What You Will Learn

- Write, build and run C# programs with the .NET 8 SDK and Visual Studio / VS Code
- Use variables, data types, operators, selection, loops and arrays confidently
- Design programs with classes, constructors, inheritance, polymorphism, abstract classes and interfaces
- Use properties, indexers, records, namespaces and structured exception handling
- Work with delegates, events, collections, generics and iterators
- Query data with LINQ and use lambdas, extension methods, nullable types and `async/await`
- Build a Windows Forms screen and perform CRUD on SQL Server with ADO.NET
- Understand .NET MAUI for cross-platform apps and what is new in modern .NET

## 📋 Prerequisites

- Logic building and basic programming ideas (variables, if/else, loops) from earlier terms
- Module 01 of this term (SQL Server) — needed for Session 14
- Comfort with the command line and installing software

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| .NET 8 SDK | compiler + runtime (`dotnet` command) | [https://dotnet.microsoft.com/download/dotnet/8.0](https://dotnet.microsoft.com/download/dotnet/8.0) |
| Visual Studio 2022 Community (Windows) | full IDE; needed for WinForms and MAUI | [https://visualstudio.microsoft.com/vs/community/](https://visualstudio.microsoft.com/vs/community/) |
| Visual Studio Code + C# Dev Kit | light editor on any OS | [https://code.visualstudio.com/docs/csharp/get-started](https://code.visualstudio.com/docs/csharp/get-started) |
| SQL Server 2022 Express / Developer | database for Session 14 | [https://www.microsoft.com/sql-server/sql-server-downloads](https://www.microsoft.com/sql-server/sql-server-downloads) |
| SQL Server Management Studio (SSMS) | run `database.sql` | [https://learn.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms](https://learn.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms) |

### How to run any session's code

```bash
cd Session-05-Classes-and-Methods
dotnet run
```

> ⚠️ **Windows only:** Session 14's WinForms project and Session 16's .NET MAUI app need Windows with Visual Studio 2022 (MAUI can also target Android/iOS/macOS). All other examples run on Windows, Linux and macOS.

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Getting Started with C# and .NET | [Open notes](./Session-01-Getting-Started-with-CSharp-and-DotNet/README.md) |
| 02 | Basic Building Blocks in C# | [Open notes](./Session-02-Basic-Building-Blocks/README.md) |
| 03 | Programming Constructs and Arrays | [Open notes](./Session-03-Programming-Constructs-and-Arrays/README.md) |
| 04 | Lab and Review: C# Fundamentals | [Open notes](./Session-04-Lab-Review-CSharp-Fundamentals/README.md) |
| 05 | Classes and Methods | [Open notes](./Session-05-Classes-and-Methods/README.md) |
| 06 | Inheritance and Polymorphism | [Open notes](./Session-06-Inheritance-and-Polymorphism/README.md) |
| 07 | Abstract Classes and Interfaces | [Open notes](./Session-07-Abstract-Classes-and-Interfaces/README.md) |
| 08 | Lab and Review: Object-Oriented Programming | [Open notes](./Session-08-Lab-Review-Object-Oriented-Programming/README.md) |
| 09 | Properties, Indexers and Record Types | [Open notes](./Session-09-Properties-Indexers-and-Records/README.md) |
| 10 | Namespaces and Exception Handling | [Open notes](./Session-10-Namespaces-and-Exception-Handling/README.md) |
| 11 | Delegates, Events and Collections | [Open notes](./Session-11-Delegates-Events-and-Collections/README.md) |
| 12 | Lab and Review: Properties, Exceptions and Collections | [Open notes](./Session-12-Lab-Review-Properties-Exceptions-Collections/README.md) |
| 13 | Generics and Iterators | [Open notes](./Session-13-Generics-and-Iterators/README.md) |
| 14 | GUI and SQL Server Connectivity | [Open notes](./Session-14-GUI-and-SQL-Server-Connectivity/README.md) |
| 15 | Advanced Concepts in C# | [Open notes](./Session-15-Advanced-Concepts-in-CSharp/README.md) |
| 16 | Cross-Platform Apps with .NET MAUI | [Open notes](./Session-16-Cross-Platform-Apps-with-DotNet-MAUI/README.md) |
| 17 | .NET Development and the Future | [Open notes](./Session-17-DotNet-Development-and-the-Future/README.md) |
| 18 | Lab and Review: Advanced C# and .NET | [Open notes](./Session-18-Lab-Review-Advanced-CSharp-and-DotNet/README.md) |

## 🚀 Module Mini-Project

**Student Fee Manager** — a console (or WinForms) app for a training centre:

1. Classes: `Student`, `Course`, `Payment` (abstract) with `CashPayment` and `CardPayment`.
2. Properties with validation, a `record` for receipts, and a custom `FeeException`.
3. Store data in `List<T>` / `Dictionary<TKey,TValue>` through a generic `Repository<T>`.
4. Raise an event `PaymentReceived` and print an SMS-style message from a handler.
5. Reports with LINQ: unpaid students, income per course, top 3 payers.
6. Bonus: save and load students from SQL Server with ADO.NET (Session 14).
7. Push the project to GitHub with a README showing sample output.

## 🔗 Resources (official documentation)

- [C# documentation](https://learn.microsoft.com/dotnet/csharp/)
- [.NET fundamentals](https://learn.microsoft.com/dotnet/fundamentals/)
- [What's new in .NET 8](https://learn.microsoft.com/dotnet/core/whats-new/dotnet-8/overview)
- [LINQ overview](https://learn.microsoft.com/dotnet/csharp/linq/)
- [Windows Forms docs](https://learn.microsoft.com/dotnet/desktop/winforms/)
- [Microsoft.Data.SqlClient / ADO.NET](https://learn.microsoft.com/sql/connect/ado-net/introduction-microsoft-data-sqlclient-namespace)
- [.NET MAUI documentation](https://learn.microsoft.com/dotnet/maui/)

---

[⬅ Previous Module](../01-Effective-Data-Solutions-with-SQL-Server/README.md) · [⬅ Term Home](../README.md) · [Next Module ➡](../03-Building-Applications-with-TypeScript/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
