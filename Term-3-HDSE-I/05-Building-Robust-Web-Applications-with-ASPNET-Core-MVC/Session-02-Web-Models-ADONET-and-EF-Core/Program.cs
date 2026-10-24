using Microsoft.EntityFrameworkCore;
using SchoolData.Data;
using SchoolData.Models;

var builder = WebApplication.CreateBuilder(args);

// Step 1: register MVC and our DbContext (SQLite file school.db)
builder.Services.AddControllersWithViews();
builder.Services.AddDbContext<SchoolContext>(options =>
    options.UseSqlite(builder.Configuration.GetConnectionString("School")));

var app = builder.Build();

// Step 2: create the database and add sample rows (only for learning)
using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<SchoolContext>();
    db.Database.EnsureCreated();
    if (!db.Students.Any())
    {
        db.Students.AddRange(
            new Student { Name = "Ayesha", Age = 19 },
            new Student { Name = "Bilal", Age = 17 },
            new Student { Name = "Sana", Age = 21 });
        db.SaveChanges();
    }
}

// Step 3: default route  /{controller}/{action}/{id?}
app.MapControllerRoute(name: "default", pattern: "{controller=Students}/{action=Index}/{id?}");
app.Run();
