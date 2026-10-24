using Microsoft.EntityFrameworkCore;
using UowDemo.Data;
using UowDemo.Repositories;
using UowDemo.Persistence;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<AppDbContext>(o => o.UseSqlite("Data Source=uow.db"));
builder.Services.AddScoped(typeof(IRepository<>), typeof(Repository<>));   // open generic
builder.Services.AddScoped<IUnitOfWork, UnitOfWork>();
builder.Services.AddControllers();

var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    scope.ServiceProvider.GetRequiredService<AppDbContext>().Database.EnsureCreated();
}

app.MapControllers();
app.Run();
