using FluentMapper.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddDbContext<SchoolContext>(o => o.UseSqlite("Data Source=fluent.db"));
builder.Services.AddAutoMapper(typeof(Program));   // finds SchoolProfile in this project

var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    scope.ServiceProvider.GetRequiredService<SchoolContext>().Database.EnsureCreated();
}

app.MapControllers();
app.Run();
