# Module 04: Developing Microsoft Azure Applications

![Azure](https://img.shields.io/badge/Microsoft_Azure-Cloud-0078D4?logo=microsoftazure&logoColor=white) ![.NET 8](https://img.shields.io/badge/.NET-8.0-512BD4?logo=dotnet&logoColor=white) ![C#](https://img.shields.io/badge/C%23-12-239120?logo=csharp&logoColor=white) ![Azure CLI](https://img.shields.io/badge/Azure_CLI-2.x-0078D4?logo=microsoftazure&logoColor=white) ![Bicep](https://img.shields.io/badge/IaC-Bicep-0078D4) ![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?logo=githubactions&logoColor=white)

> Term 4 (HDSE) · 12 sessions × 2 hours · [⬅ Term Home](../README.md)

This module teaches you to build, secure, deploy and run applications on Microsoft Azure. You start with cloud basics and virtual machines, learn to automate Azure with the CLI, PowerShell and Bicep, store data with EF Core 8 and Azure data services, and build an ASP.NET Core Web API with JWT and role-based access. Then you protect it with Key Vault and network security, host it on App Service and containers, go serverless with Azure Functions, put API Management in front, automate releases with GitHub Actions and finish with traffic management, monitoring and zero-downtime deployment slots. Every concept session is followed by a practice lab with full solutions. Scripts are short `az` commands and code is small, commented C#.

## 🎯 What You Will Learn

- Explain cloud models, Azure regions, availability zones and SLAs
- Create and manage VMs and resources with the Portal, Azure CLI, PowerShell and Bicep
- Monitor apps with Azure Monitor, Log Analytics, KQL and Application Insights
- Access data with EF Core 8 and choose between Azure SQL, Cosmos DB, Redis and analytics services
- Build REST Web APIs with async actions, JWT authentication, RBAC, versioning and HATEOAS
- Secure apps with NSGs, Azure Firewall, DDoS Protection, Key Vault, managed identities and Entra ID
- Host APIs on App Service and Container Apps, and consume them from C#
- Build serverless, event-driven code with Azure Functions and publish APIs through API Management
- Automate CI/CD with GitHub Actions and release with deployment slots, Traffic Manager and Front Door

## 📋 Prerequisites

- C# and object-oriented programming (Term 3)
- SQL basics and relational databases (Term 3)
- ASP.NET Core basics are helpful (controllers, `Program.cs`)
- Git and GitHub basics
- An Azure subscription: [Azure for Students](https://azure.microsoft.com/free/students/) gives free credit without a credit card

> 💡 **Cost rule for every lab:** create one resource group per lab and delete it the same day with `az group delete --name <group> --yes`.

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|---|---|---|
| .NET 8 SDK | build and run C# projects | [https://dotnet.microsoft.com/download/dotnet/8.0](https://dotnet.microsoft.com/download/dotnet/8.0) |
| Visual Studio Code (+ C# Dev Kit, Azure extensions) | editor | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| Azure CLI | `az` commands on your PC | [https://learn.microsoft.com/cli/azure/install-azure-cli](https://learn.microsoft.com/cli/azure/install-azure-cli) |
| Azure PowerShell (optional) | `Az` cmdlets | [https://learn.microsoft.com/powershell/azure/install-azure-powershell](https://learn.microsoft.com/powershell/azure/install-azure-powershell) |
| Azure Cloud Shell | browser terminal, nothing to install | [https://shell.azure.com](https://shell.azure.com) |
| Bicep | infrastructure as code (`az bicep install`) | [https://learn.microsoft.com/azure/azure-resource-manager/bicep/install](https://learn.microsoft.com/azure/azure-resource-manager/bicep/install) |
| Azure Functions Core Tools | run and publish Functions | [https://learn.microsoft.com/azure/azure-functions/functions-run-local](https://learn.microsoft.com/azure/azure-functions/functions-run-local) |
| Azurite | local storage emulator for Functions | [https://learn.microsoft.com/azure/storage/common/storage-use-azurite](https://learn.microsoft.com/azure/storage/common/storage-use-azurite) |
| Docker Desktop (optional) | build container images locally | [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) |

## 📚 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to Azure Cloud and Virtual Machines | [Open notes](./Session-01-Introduction-to-Azure-Cloud-and-Virtual-Machines/README.md) |
| 02 | Azure CLI, PowerShell, ARM/Bicep and Azure Monitor | [Open notes](./Session-02-Azure-CLI-PowerShell-ARM-Bicep-and-Monitor/README.md) |
| 03 | Practice Lab: Azure Basics and Management Tools | [Open notes](./Session-03-Practice-Lab-Azure-Basics-and-Management-Tools/README.md) |
| 04 | Entity Framework Core 8 and Azure Data Services | [Open notes](./Session-04-Entity-Framework-Core-8-and-Azure-Data-Services/README.md) |
| 05 | ASP.NET Core Web API, Authentication, RBAC and Versioning | [Open notes](./Session-05-ASPNET-Core-Web-API-RBAC-and-Versioning/README.md) |
| 06 | Practice Lab: EF Core and Web API | [Open notes](./Session-06-Practice-Lab-EF-Core-and-Web-API/README.md) |
| 07 | Azure Security and Hosting a Web API on App Service | [Open notes](./Session-07-Azure-Security-and-Hosting-Web-API-on-App-Service/README.md) |
| 08 | Practice Lab: Security and Hosting | [Open notes](./Session-08-Practice-Lab-Security-and-Hosting/README.md) |
| 09 | Serverless Azure Functions, API Management and CI/CD with GitHub Actions | [Open notes](./Session-09-Azure-Functions-API-Management-and-CI-CD/README.md) |
| 10 | Practice Lab: Serverless, API Management and CI/CD | [Open notes](./Session-10-Practice-Lab-Serverless-APIM-and-CI-CD/README.md) |
| 11 | Traffic Management, Monitoring and Deployment Slots | [Open notes](./Session-11-Traffic-Management-Monitoring-and-Deployment-Slots/README.md) |
| 12 | Practice Lab: Traffic, Slots and Final Review | [Open notes](./Session-12-Practice-Lab-Traffic-Slots-and-Final-Review/README.md) |

## 🚀 Module Mini-Project

**Campus Events Cloud Platform**

1. Bicep template: Log Analytics, Application Insights, S1 App Service plan, web app with staging slot, Key Vault and an HTTP 5xx alert.
2. ASP.NET Core Web API (`/api/v1/events`) with EF Core 8 on Azure SQL: CRUD, async actions, paging in `/api/v2/events` with HATEOAS links.
3. JWT or Entra ID login: students can read, organisers (Admin role) can create and edit.
4. Connection string in Key Vault, read through the web app's managed identity.
5. An Azure Function triggered by a queue sends a "new event" notification log whenever an event is created.
6. API Management in front of the API with a subscription key and a rate limit.
7. GitHub Actions pipeline: build → deploy to staging → smoke test `/health` → swap.
8. A README with an architecture diagram, KQL queries for errors and response times, and a cost-saving note.

## 🔗 Resources (official documentation)

- [Azure documentation](https://learn.microsoft.com/azure/)
- [Azure CLI reference](https://learn.microsoft.com/cli/azure/)
- [Bicep documentation](https://learn.microsoft.com/azure/azure-resource-manager/bicep/)
- [Azure Monitor and Application Insights](https://learn.microsoft.com/azure/azure-monitor/)
- [Entity Framework Core](https://learn.microsoft.com/ef/core/)
- [ASP.NET Core Web API](https://learn.microsoft.com/aspnet/core/web-api/)
- [Azure Key Vault](https://learn.microsoft.com/azure/key-vault/)
- [Azure App Service](https://learn.microsoft.com/azure/app-service/)
- [Azure Functions](https://learn.microsoft.com/azure/azure-functions/)
- [Azure API Management](https://learn.microsoft.com/azure/api-management/)
- [GitHub Actions for Azure](https://learn.microsoft.com/azure/developer/github/github-actions)
- [Microsoft Learn: free Azure training paths](https://learn.microsoft.com/training/azure/)

---

[⬅ Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
