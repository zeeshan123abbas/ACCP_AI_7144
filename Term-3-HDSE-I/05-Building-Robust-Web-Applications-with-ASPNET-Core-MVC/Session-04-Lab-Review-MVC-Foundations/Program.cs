using LibraryLab.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();
builder.Services.AddDbContext<LibraryContext>(o => o.UseSqlite("Data Source=library.db"));

var app = builder.Build();

// Create library.db on first run
using (var scope = app.Services.CreateScope())
{
    scope.ServiceProvider.GetRequiredService<LibraryContext>().Database.EnsureCreated();
}

app.MapControllerRoute("default", "{controller=Books}/{action=Index}/{id?}");
app.Run();
