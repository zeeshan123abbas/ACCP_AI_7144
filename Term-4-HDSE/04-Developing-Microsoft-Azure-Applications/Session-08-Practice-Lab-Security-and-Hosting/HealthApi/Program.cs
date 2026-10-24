// Lab 08 - Task 1: a tiny API that proves a Key Vault secret reached the app
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Step 1: a home endpoint
app.MapGet("/", () => "Lab 08 API is running");

// Step 2: /health tells us IF the secret exists, but never shows its value
app.MapGet("/health", (IConfiguration config) =>
{
    string? apiKey = config["DemoApiKey"];      // filled from Key Vault on Azure
    return new
    {
        status = "healthy",
        secretLoaded = !string.IsNullOrEmpty(apiKey),
        serverTimeUtc = DateTime.UtcNow
    };
});

app.Run();
