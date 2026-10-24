var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllersWithViews();

// Bundling + minification: many CSS/JS files become one small file each
builder.Services.AddWebOptimizer(pipeline =>
{
    pipeline.AddCssBundle("/css/bundle.css", "css/*.css");
    pipeline.AddJavaScriptBundle("/js/bundle.js", "js/*.js");
});

var app = builder.Build();

app.UseWebOptimizer();   // must come before UseStaticFiles
app.UseStaticFiles();

// Route for areas first (more specific), then the default route
app.MapControllerRoute(
    name: "areas",
    pattern: "{area:exists}/{controller=Dashboard}/{action=Index}/{id?}");
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Products}/{action=Index}/{id?}");

app.Run();
