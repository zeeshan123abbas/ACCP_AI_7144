// Session 07 - Example 6 (snippet): protect a Web API with Microsoft Entra ID
// 1) dotnet add package Microsoft.Identity.Web
// 2) Register an app in Entra ID (Portal > App registrations) and expose an API scope.
// 3) appsettings.json:
//    "AzureAd": { "Instance": "https://login.microsoftonline.com/",
//                 "TenantId": "<tenant-id>", "ClientId": "<api-client-id>" }
// 4) In Program.cs, replace your own JWT setup with:

using Microsoft.Identity.Web;

builder.Services.AddMicrosoftIdentityWebApiAuthentication(builder.Configuration, "AzureAd");
builder.Services.AddAuthorization();

// ...later in the pipeline:
app.UseAuthentication();
app.UseAuthorization();

// Controllers keep using [Authorize] and [Authorize(Roles = "Admin")];
// the roles now come from "App roles" you assign to users in Entra ID.
