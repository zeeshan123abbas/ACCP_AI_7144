using TaskBoard.Data;
using TaskBoard.Filters;

var builder = WebApplication.CreateBuilder(args);

// Register our exception filter for ALL controllers
builder.Services.AddControllersWithViews(options =>
{
    options.Filters.Add<FriendlyErrorFilter>();
});

var app = builder.Build();

app.MapControllerRoute("default", "{controller=Tasks}/{action=Index}/{id?}");

// Minimal API: the same tasks as JSON
app.MapGet("/api/tasks", () => TaskStore.Tasks);
app.MapGet("/api/tasks/pending", () => TaskStore.Tasks.Where(t => !t.IsDone));

app.Run();
