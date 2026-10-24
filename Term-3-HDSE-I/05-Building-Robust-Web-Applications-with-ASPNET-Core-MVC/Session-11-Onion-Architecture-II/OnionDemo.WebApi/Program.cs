using Microsoft.EntityFrameworkCore;
using OnionDemo.Domain;
using OnionDemo.Infrastructure;
using OnionDemo.Service;

var builder = WebApplication.CreateBuilder(args);

// Step 1: wire the layers together (composition root)
builder.Services.AddDbContext<AppDbContext>(o =>
    o.UseSqlite(builder.Configuration.GetConnectionString("Default")));
builder.Services.AddScoped<IProductRepository, ProductRepository>();
builder.Services.AddScoped<ProductService>();
builder.Services.AddControllers();

// Step 2: monitoring helpers
builder.Services.AddProblemDetails();          // standard JSON error format
builder.Services.AddHealthChecks();            // /health endpoint
builder.Services.AddHttpLogging(o => { });     // log each request and response line

var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    scope.ServiceProvider.GetRequiredService<AppDbContext>().Database.EnsureCreated();
}

// Step 3: security + error handling middleware
app.UseExceptionHandler();                     // turns exceptions into ProblemDetails JSON
if (!app.Environment.IsDevelopment())
{
    app.UseHsts();                             // tell browsers: always use HTTPS
}
app.UseHttpsRedirection();
app.UseHttpLogging();
app.Use(async (context, next) =>               // simple security headers
{
    context.Response.Headers["X-Content-Type-Options"] = "nosniff";
    context.Response.Headers["X-Frame-Options"] = "DENY";
    await next(context);
});

app.MapControllers();
app.MapHealthChecks("/health");
app.Run();
