using System.Security.Claims;
using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Mvc;

namespace AuthFilters.Controllers;

public class AccountController : Controller
{
    [HttpGet]
    public IActionResult Login() => View();

    // DEMO ONLY: no password check. Type "admin" to become an Admin.
    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Login(string userName)
    {
        string role = userName == "admin" ? "Admin" : "Student";

        // Step 1: facts about the user (claims)
        var claims = new List<Claim>
        {
            new Claim(ClaimTypes.Name, userName),
            new Claim(ClaimTypes.Role, role)
        };

        // Step 2: wrap them in an identity and sign in (creates the cookie)
        var identity = new ClaimsIdentity(claims, CookieAuthenticationDefaults.AuthenticationScheme);
        await HttpContext.SignInAsync(new ClaimsPrincipal(identity));

        return RedirectToAction("Index", "Home");
    }

    public async Task<IActionResult> Logout()
    {
        await HttpContext.SignOutAsync();
        return RedirectToAction("Index", "Home");
    }

    public IActionResult Denied() => Content("Sorry, you do not have permission for that page.");
}
