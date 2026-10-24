using AuthFilters.Filters;
using AuthFilters.Models;
using Microsoft.AspNetCore.Mvc;

namespace AuthFilters.Controllers;

[LogTime]   // our custom filter runs for every action here
public class HomeController : Controller
{
    public IActionResult Index()
    {
        var courses = new List<Course>
        {
            new("ASP.NET Core MVC", 15000),
            new("Angular", 12000),
            new("SQL Server", 10000)
        };
        return View(courses);
    }

    // Action selector: answers only GET requests, and the URL name is "contact-info"
    [HttpGet]
    [ActionName("contact-info")]
    public IActionResult ContactInfo() => Content("Call 021-0000000");

    // Not reachable from a URL
    [NonAction]
    public string Helper() => "internal";
}
