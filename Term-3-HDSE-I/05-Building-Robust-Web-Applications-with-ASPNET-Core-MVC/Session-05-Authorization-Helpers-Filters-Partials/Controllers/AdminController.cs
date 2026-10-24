using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace AuthFilters.Controllers;

// Role-based authorization: only users in the Admin role
[Authorize(Roles = "Admin")]
public class AdminController : Controller
{
    public IActionResult Index()
    {
        return Content($"Welcome to the admin area, {User.Identity!.Name}.");
    }
}
