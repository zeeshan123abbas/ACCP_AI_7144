using System.Text.Json;
using Modern.Models;

var builder = WebApplication.CreateBuilder(args);

// MVC controllers AND Razor Pages in the same app
builder.Services.AddControllers();
builder.Services.AddRazorPages();

// Global System.Text.Json settings for minimal APIs
builder.Services.ConfigureHttpJsonOptions(options =>
{
    options.SerializerOptions.WriteIndented = true;
});

var app = builder.Build();

app.MapControllers();
app.MapRazorPages();

// 1. Minimal API returning a record as JSON
app.MapGet("/students/{id:int}", (int id) =>
    new Student(id, "Hamza Ali", new DateOnly(2026, 1, 15)));

// 2. [AsParameters]: many query values in one object
//    /search?name=ali&page=2
app.MapGet("/search", ([AsParameters] SearchQuery query) =>
    $"Searching '{query.Name}' page {query.Page} (size {query.PageSize})");

// 3. System.Text.Json by hand: serialize and deserialize
app.MapGet("/json-demo", () =>
{
    var student = new Student(7, "Fatima Noor", new DateOnly(2026, 3, 1));
    var options = new JsonSerializerOptions { PropertyNamingPolicy = JsonNamingPolicy.CamelCase };

    string json = JsonSerializer.Serialize(student, options);
    Student? back = JsonSerializer.Deserialize<Student>(json, options);

    return $"JSON: {json}\nBack to object: {back}";
});

// 4. Garbage collector information
app.MapGet("/gc", () =>
{
    long before = GC.GetTotalMemory(forceFullCollection: false);
    var junk = new List<byte[]>();
    for (int i = 0; i < 100; i++) junk.Add(new byte[10_000]);   // allocate ~1 MB
    junk = null!;
    GC.Collect();   // only for learning; never call this in real apps
    long after = GC.GetTotalMemory(forceFullCollection: true);

    return $"Before: {before / 1024} KB, after collect: {after / 1024} KB, " +
           $"Gen0 collections: {GC.CollectionCount(0)}";
});

app.Run();
