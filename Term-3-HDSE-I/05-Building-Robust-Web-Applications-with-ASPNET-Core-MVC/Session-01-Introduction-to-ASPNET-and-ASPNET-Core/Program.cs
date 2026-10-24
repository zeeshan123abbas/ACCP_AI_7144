// Session 01: smallest ASP.NET Core app with static files and error handling
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
