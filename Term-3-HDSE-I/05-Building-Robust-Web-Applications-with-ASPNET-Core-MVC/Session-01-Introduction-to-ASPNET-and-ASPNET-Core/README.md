# Session 01: Introduction to ASP.NET and ASP.NET Core

> Module: Building Robust Web Applications with ASP.NET Core MVC · Term 3 (HDSE I) · ⏱ ~2 hours

## 🎯 Learning Objectives

- Describe the ASP.NET family and how it grew from Web Forms to ASP.NET Core
- Explain the classic Web Forms page lifecycle and its main events
- List the main advantages of ASP.NET Core over the older .NET Framework version
- Serve static files and handle exceptions in an ASP.NET Core app
- Decide when to use ASP.NET (Framework) and when to use ASP.NET Core
- Create, run and explore your first .NET 8 web project

## 📖 Concepts Explained

### 1. What is ASP.NET?

**ASP.NET** is Microsoft's framework for building websites, web apps and web APIs with C#. The browser sends an HTTP request, your C# code on the server builds a response (HTML, JSON, a file) and sends it back.

Think of a restaurant: the **browser is the customer**, the **web server is the waiter**, and **your C# code is the kitchen** that prepares each order.

### 2. A Short History

| Year | Version | What changed |
|---|---|---|
| 2002 | ASP.NET 1.0 (Web Forms) | Drag-and-drop pages, events like desktop apps |
| 2009 | ASP.NET MVC 1.0 | Clean separation: Model, View, Controller |
| 2012 | ASP.NET Web API | Build JSON services for mobile and JavaScript apps |
| 2016 | ASP.NET Core 1.0 | Rewritten: open source, cross-platform, fast |
| 2020 | .NET 5 | One unified .NET (the word "Core" dropped from the runtime name) |
| 2023 | **.NET 8 (LTS)** | Long-term support version we use in this module |

> "ASP.NET" alone usually means the old Windows-only version on **.NET Framework 4.x**. "ASP.NET Core" is the modern one.

### 3. The Web Forms Page Lifecycle (legacy, for understanding)

In Web Forms, every `.aspx` page goes through fixed stages on each request:

```mermaid
flowchart LR
    A[PreInit] --> B[Init] --> C[Load] --> D[Control events<br/>e.g. Button_Click] --> E[PreRender] --> F[Render] --> G[Unload]
```

| Event | What you typically do there |
|---|---|
| `Page_PreInit` | Set master page or theme |
| `Page_Init` | Create controls dynamically |
| `Page_Load` | Read data, check `IsPostBack` |
| Control events | Respond to a button click or dropdown change |
| `Page_PreRender` | Last changes before HTML is produced |
| `Page_Unload` | Clean up (close files, connections) |

A legacy code-behind looked like this (read only, it does not run on .NET 8):

```csharp
protected void Page_Load(object sender, EventArgs e)
{
    if (!IsPostBack)              // first visit, not a button click
        lblMessage.Text = "Welcome!";
}
```

ASP.NET Core does **not** use this lifecycle. Instead every request flows through a **middleware pipeline** (you will see it below).

### 4. Why ASP.NET Core?

| Feature | ASP.NET (Framework 4.x) | ASP.NET Core (.NET 8) |
|---|---|---|
| Operating system | Windows only | Windows, Linux, macOS |
| Hosting | IIS | Kestrel, IIS, Nginx, Docker, cloud |
| Open source | Partly | Fully, on GitHub |
| Performance | Good | Among the fastest web frameworks |
| Dependency injection | Add-on libraries | Built in |
| New features | Maintenance only | Released every year |

**Choose ASP.NET Core** for every new project. Keep **ASP.NET Framework** only to maintain an old Web Forms or MVC 5 app that cannot be moved yet.

### 5. The Request Pipeline

```mermaid
flowchart LR
    R[HTTP request] --> E[Exception handler] --> S[Static files] --> RT[Routing] --> EP[Your endpoint / controller]
    EP --> RES[HTTP response]
```

Each box is **middleware**: a small piece of code that can look at the request, do something, and pass it on. **Order matters**: the exception handler comes first so it can catch errors from everything after it.

### 6. Static Files and Exceptions

- **Static files** (HTML, CSS, JS, images) live in the `wwwroot` folder. `app.UseStaticFiles()` serves them directly, with no C# code needed.
- **Developer exception page**: in Development, a detailed error page with the stack trace (on by default in .NET 8).
- **Exception handler**: in Production, `app.UseExceptionHandler("/error")` shows a friendly message and hides details from users.

### 7. What .NET 8 Brings

- Long-Term Support (3 years of patches)
- Faster startup and lower memory use
- Minimal APIs with better tooling, Native AOT for small APIs
- Blazor improvements, built-in Identity API endpoints, better metrics

## 💻 Code Examples

Files in this folder: `HelloCore.csproj`, `Program.cs`, `wwwroot/index.html`. Run with `dotnet run` and open the URL shown in the terminal.

### Example 1: The smallest web app (`Program.cs`)

```csharp
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Step 1: friendly error page outside Development
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/error");
}

// Step 2: serve files from wwwroot (index.html is the default page)
app.UseDefaultFiles();
app.UseStaticFiles();

// Step 3: simple endpoints
app.MapGet("/hello", () => "Hello from ASP.NET Core 8!");
app.MapGet("/time", () => $"Server time: {DateTime.Now:t}");
app.MapGet("/boom", () => { throw new Exception("Test error"); });
app.MapGet("/error", () => "Sorry, something went wrong. Please try again later.");

app.Run();
```

**How it works**

1. `CreateBuilder` sets up configuration, logging and the Kestrel web server.
2. `UseDefaultFiles` + `UseStaticFiles` make `/` return `wwwroot/index.html`.
3. `MapGet` connects a URL to a small function.
4. Visit `/boom` to see the detailed developer error page. Run with `dotnet run --environment Production` and visit it again to see the friendly `/error` message.

### Example 2: A static page (`wwwroot/index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Hello Core</title></head>
<body>
  <h1>My first ASP.NET Core site</h1>
  <p>This page is a static file served from wwwroot.</p>
  <a href="/hello">Say hello</a> | <a href="/time">Server time</a> | <a href="/boom">Cause an error</a>
</body>
</html>
```

**How it works**: The server sends this file exactly as it is. No C# runs for static files, which makes them very fast.

### Example 3: Create an MVC project with the CLI

```bash
dotnet --version                 # should print 8.0.x
dotnet new mvc -n FirstMvc       # create an MVC project
cd FirstMvc
dotnet run                       # open the https://localhost:xxxx URL shown
```

**How it works**: The `mvc` template gives you `Controllers/`, `Views/`, `Models/` and `wwwroot/` folders. You will study each of them in the next sessions.

## 🧪 Lab Practice

1. Install the .NET 8 SDK and Visual Studio 2022 (or VS Code with C# Dev Kit). Run `dotnet --info`.
2. Run the code in this folder. Add a new endpoint `/about` that returns your name and batch code.
3. Add `wwwroot/css/site.css` with a background colour and link it from `index.html`.
4. Create the `FirstMvc` project, run it, and list every folder with one line about what it holds.
5. Run once in Development and once in Production and compare what `/boom` shows.

## 📝 Assignment

Write a one-page comparison (in a `README.md`) of ASP.NET Web Forms vs ASP.NET Core for a small Karachi school website. Recommend one and give three reasons.

## ❓ Quick Quiz

1. Which folder holds static files in ASP.NET Core?
2. Name the Web Forms event where you usually check `IsPostBack`.
3. Why must the exception handler be added early in the pipeline?
4. Which web server is built into ASP.NET Core?
5. True or false: ASP.NET Core runs only on Windows.

<details>
<summary>Show answers</summary>

1. `wwwroot`
2. `Page_Load`
3. Middleware can only catch errors from the middleware that runs after it.
4. Kestrel
5. False, it is cross-platform.

</details>

## 💼 Interview Questions

1. **What is middleware in ASP.NET Core?** A component in the request pipeline that can handle a request, change it, or pass it to the next component.
2. **Difference between ASP.NET and ASP.NET Core?** Core is a cross-platform, open-source rewrite with built-in DI, Kestrel and much better performance.
3. **How do you show friendly errors in production?** Use `UseExceptionHandler` with an error page and keep the developer exception page for Development only.

## ✅ Summary

- ASP.NET grew from Web Forms (events and lifecycle) to MVC, Web API and then ASP.NET Core.
- ASP.NET Core is cross-platform, open source, fast and has DI built in.
- Requests pass through a middleware pipeline where order matters.
- `wwwroot` + `UseStaticFiles` serve static content; `UseExceptionHandler` hides errors from users.
- Use .NET 8 (LTS) for all new work in this module.

---

[⬅ Previous Module](../../04-Material-UI/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-02-Web-Models-ADONET-and-EF-Core/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
