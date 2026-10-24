using ClientSide.Services;

var builder = WebApplication.CreateBuilder(args);

// Step 1: MVC + our own service in the DI container
builder.Services.AddControllersWithViews();
builder.Services.AddSingleton<IQuoteService, QuoteService>();

var app = builder.Build();

// Step 2: static files (css) and routing
app.UseStaticFiles();
app.MapControllerRoute(name: "default", pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
