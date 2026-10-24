// Session 11 - SlotDemo: shows which version and slot is answering
var builder = WebApplication.CreateBuilder(args);

// Step 1: send requests, errors and timings to Application Insights
// (reads the APPLICATIONINSIGHTS_CONNECTION_STRING setting; does nothing if it is empty)
builder.Services.AddApplicationInsightsTelemetry();

var app = builder.Build();

// Step 2: values come from App Service settings (different per slot)
string version = app.Configuration["APP_VERSION"] ?? "1.0";
string environmentName = app.Configuration["ENVIRONMENT_NAME"] ?? "Local";

// Step 3: endpoints
app.MapGet("/", () => $"Version {version} running in {environmentName}");
app.MapGet("/health", () => Results.Ok(new { status = "healthy", version }));
app.MapGet("/error", () =>
{
    // used in the lab to create an exception you can find in Application Insights
    throw new InvalidOperationException("Test exception for monitoring practice");
});

app.Run();
