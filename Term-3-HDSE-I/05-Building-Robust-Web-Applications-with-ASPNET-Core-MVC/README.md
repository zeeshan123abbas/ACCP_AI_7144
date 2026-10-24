# Module 05: Building Robust Web Applications with ASP.NET Core MVC

![.NET](https://img.shields.io/badge/.NET-8.0%20LTS-512BD4?logo=dotnet&logoColor=white)
![C#](https://img.shields.io/badge/Language-C%23%2012-239120)
![ASP.NET Core](https://img.shields.io/badge/ASP.NET%20Core-MVC%20%7C%20Web%20API-5C2D91)
![EF Core](https://img.shields.io/badge/EF%20Core-8-6DB33F)
![SQLite](https://img.shields.io/badge/DB-SQLite%20%7C%20SQL%20Server%20LocalDB-003B57?logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-Identity%20%7C%20JWT-black?logo=jsonwebtokens)
![Sessions](https://img.shields.io/badge/Sessions-18-success)

> Term 3 (HDSE I) · 18 sessions × 2 hours · Skill: building secure, layered, data-driven web apps and REST APIs with ASP.NET Core 8

## What You Will Learn

- How ASP.NET Core works: Kestrel, the middleware pipeline, routing and dependency injection
- Build MVC apps with controllers, Razor views, layouts, partial views and tag helpers
- Read and write data with ADO.NET and Entity Framework Core (code-first, Fluent API)
- Validate input on the client and the server with data annotations
- Secure apps with cookie auth, roles, ASP.NET Core Identity and JWT tokens
- Build REST Web APIs with correct verbs, status codes, DTOs and AutoMapper
- Structure real projects with Onion Architecture, Repository and Unit of Work
- Add logging, health checks and safe error handling, then publish to IIS or Docker

## Prerequisites

- Module 02 (C#): classes, interfaces, generics, LINQ, async/await
- Module 01 (SQL Server): tables, keys, joins
- Basic HTML/CSS and Bootstrap from earlier terms

## Tools to Install

| Tool | Why | Link |
|---|---|---|
| .NET 8 SDK | Build and run every example | https://dotnet.microsoft.com/download/dotnet/8.0 |
| Visual Studio 2022 (Community) with "ASP.NET and web development" | Main IDE, publishing to IIS/Azure | https://visualstudio.microsoft.com/vs/ |
| VS Code + C# Dev Kit (optional) | Lightweight editor on any OS | https://code.visualstudio.com/docs/csharp/get-started |
| SQL Server Express LocalDB (optional) | Use SQL Server instead of SQLite | https://learn.microsoft.com/sql/database-engine/configure-windows/sql-server-express-localdb |
| DB Browser for SQLite (optional) | Look inside `.db` files | https://sqlitebrowser.org/ |
| EF Core CLI tools | Migrations: `dotnet tool install --global dotnet-ef` | https://learn.microsoft.com/ef/core/cli/dotnet |

> Every session folder is a small project. Open a terminal in the folder and run `dotnet run`. Examples use **SQLite** so they work on Windows, macOS and Linux; Session 02 shows the one-line switch to SQL Server LocalDB.

## Session Index

| Session | Topic | Link |
|:---:|---|---|
| 01 | Introduction to ASP.NET and ASP.NET Core | [Open notes](./Session-01-Introduction-to-ASPNET-and-ASPNET-Core/README.md) |
| 02 | Web Development Models, ADO.NET and Entity Framework Core | [Open notes](./Session-02-Web-Models-ADONET-and-EF-Core/README.md) |
| 03 | Client-Side Development with ASP.NET Core MVC | [Open notes](./Session-03-Client-Side-Development-with-MVC/README.md) |
| 04 | Lab and Review: MVC Foundations | [Open notes](./Session-04-Lab-Review-MVC-Foundations/README.md) |
| 05 | Authorization, Tag Helpers, Filters and Partial Views | [Open notes](./Session-05-Authorization-Helpers-Filters-Partials/README.md) |
| 06 | Action Methods, Web API, Areas and Bundling | [Open notes](./Session-06-Action-Methods-Web-API-Areas-Bundling/README.md) |
| 07 | Modern ASP.NET Core Enhancements | [Open notes](./Session-07-Modern-ASPNET-Core-Enhancements/README.md) |
| 08 | Lab and Review: Advanced MVC | [Open notes](./Session-08-Lab-Review-Advanced-MVC/README.md) |
| 09 | .NET Architecture, Kestrel and REST APIs | [Open notes](./Session-09-DotNet-Architecture-Kestrel-and-REST/README.md) |
| 10 | Onion Architecture I: Principles and Layers | [Open notes](./Session-10-Onion-Architecture-I/README.md) |
| 11 | Onion Architecture II: Project Structure, Security and Monitoring | [Open notes](./Session-11-Onion-Architecture-II/README.md) |
| 12 | Lab and Review: Architecture | [Open notes](./Session-12-Lab-Review-Architecture/README.md) |
| 13 | Fluent API and AutoMapper | [Open notes](./Session-13-Fluent-API-and-AutoMapper/README.md) |
| 14 | Token Authentication with JWT | [Open notes](./Session-14-Token-Authentication-with-JWT/README.md) |
| 15 | Lab and Review: Fluent API, AutoMapper and JWT | [Open notes](./Session-15-Lab-Review-Fluent-AutoMapper-JWT/README.md) |
| 16 | Repository and Unit of Work Patterns | [Open notes](./Session-16-Repository-and-Unit-of-Work/README.md) |
| 17 | Identity, Session State and Deployment | [Open notes](./Session-17-Identity-Session-and-Deployment/README.md) |
| 18 | Lab and Review: Patterns, Identity and Deployment | [Open notes](./Session-18-Lab-Review-Patterns-Identity-Deployment/README.md) |

## Module Mini-Project: Campus Course Portal

Build one app step by step as you finish the sessions:

1. **MVC + EF Core (S01–04)** – `Course`, `Student`, `Enrollment` models; list and create pages with validation and a Bootstrap layout.
2. **Security and UI (S05–08)** – cookie login with Admin/Student roles, a `[LogTime]` filter, partial course cards, an Admin area.
3. **API (S06, S09)** – `api/courses` REST endpoints with correct status codes, tested with a `.http` file.
4. **Architecture (S10–12)** – split into Domain, Service, Infrastructure and Web projects; unit-test the enrollment rules.
5. **Data and tokens (S13–15)** – Fluent API configuration, DTOs with AutoMapper, JWT-protected write endpoints.
6. **Patterns and users (S16–18)** – Unit of Work for enrolment + fee records, ASP.NET Core Identity, session-based "selected courses" basket.
7. **Ship** – publish to IIS or Docker and complete the release checklist from Session 18.

## Resources (Official Documentation)

- ASP.NET Core documentation: https://learn.microsoft.com/aspnet/core/
- MVC overview: https://learn.microsoft.com/aspnet/core/mvc/overview
- Web APIs: https://learn.microsoft.com/aspnet/core/web-api/
- Entity Framework Core: https://learn.microsoft.com/ef/core/
- Security and Identity: https://learn.microsoft.com/aspnet/core/security/
- JWT bearer authentication: https://learn.microsoft.com/aspnet/core/security/authentication/configure-jwt-bearer-authentication
- Host and deploy (IIS, Docker, Azure): https://learn.microsoft.com/aspnet/core/host-and-deploy/
- AutoMapper: https://docs.automapper.org/
- .NET architecture guides: https://learn.microsoft.com/dotnet/architecture/

---

[⬅ Previous Module](../04-Material-UI/README.md) · [🏠 Term Home](../README.md) · [Next: eProject ➡](../eProject/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
