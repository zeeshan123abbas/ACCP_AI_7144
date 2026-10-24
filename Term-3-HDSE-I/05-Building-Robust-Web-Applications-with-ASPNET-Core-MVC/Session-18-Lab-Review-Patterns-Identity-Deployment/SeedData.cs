using Microsoft.AspNetCore.Identity;

namespace IdentitySession.Data;

// Creates the Admin role and a first admin user when the app starts.
// Call it from Program.cs:  await SeedData.CreateAdminAsync(app.Services);
public static class SeedData
{
    public static async Task CreateAdminAsync(IServiceProvider services)
    {
        using var scope = services.CreateScope();
        var roleManager = scope.ServiceProvider.GetRequiredService<RoleManager<IdentityRole>>();
        var userManager = scope.ServiceProvider.GetRequiredService<UserManager<IdentityUser>>();

        // Step 1: make sure the role exists
        if (!await roleManager.RoleExistsAsync("Admin"))
        {
            await roleManager.CreateAsync(new IdentityRole("Admin"));
        }

        // Step 2: make sure the admin user exists
        const string adminEmail = "admin@campus.local";
        var admin = await userManager.FindByEmailAsync(adminEmail);
        if (admin == null)
        {
            admin = new IdentityUser { UserName = adminEmail, Email = adminEmail, EmailConfirmed = true };
            // Read the password from configuration in real apps; this is a lab default
            await userManager.CreateAsync(admin, "Admin2026Pass");
        }

        // Step 3: put the user in the role
        if (!await userManager.IsInRoleAsync(admin, "Admin"))
        {
            await userManager.AddToRoleAsync(admin, "Admin");
        }
    }
}
