using IdentitySession.Models;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;

namespace IdentitySession.Controllers;

public class AccountController : Controller
{
    private readonly UserManager<IdentityUser> _userManager;      // create/find users
    private readonly SignInManager<IdentityUser> _signInManager;  // log in/out

    public AccountController(UserManager<IdentityUser> userManager, SignInManager<IdentityUser> signInManager)
    {
        _userManager = userManager;
        _signInManager = signInManager;
    }

    public IActionResult Register() => View();

    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Register(AccountModel model)
    {
        if (!ModelState.IsValid) return View(model);

        var user = new IdentityUser { UserName = model.Email, Email = model.Email };
        var result = await _userManager.CreateAsync(user, model.Password);   // password is HASHED

        if (result.Succeeded)
        {
            await _signInManager.SignInAsync(user, isPersistent: false);
            return RedirectToAction("Index", "Cart");
        }

        foreach (var error in result.Errors)
        {
            ModelState.AddModelError("", error.Description);   // e.g. "Passwords must have at least one digit"
        }
        return View(model);
    }

    public IActionResult Login() => View();

    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Login(AccountModel model)
    {
        if (!ModelState.IsValid) return View(model);

        var result = await _signInManager.PasswordSignInAsync(
            model.Email, model.Password, isPersistent: false, lockoutOnFailure: true);

        if (result.Succeeded) return RedirectToAction("Index", "Cart");
        if (result.IsLockedOut) return Content("Account locked. Try again in 10 minutes.");

        ModelState.AddModelError("", "Invalid email or password");
        return View(model);
    }

    [HttpPost, ValidateAntiForgeryToken]
    public async Task<IActionResult> Logout()
    {
        await _signInManager.SignOutAsync();
        return RedirectToAction(nameof(Login));
    }
}
