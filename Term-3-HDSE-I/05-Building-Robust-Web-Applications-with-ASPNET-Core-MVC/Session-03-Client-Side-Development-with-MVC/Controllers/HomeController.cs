using ClientSide.Services;
using Microsoft.AspNetCore.Mvc;

namespace ClientSide.Controllers;

public class HomeController : Controller
{
    private readonly IQuoteService _quotes;

    // DI gives us the service; we never write "new QuoteService()"
    public HomeController(IQuoteService quotes)
    {
        _quotes = quotes;
    }

    // Conventional route: /  or  /Home/Index
    public IActionResult Index()
    {
        ViewData["Quote"] = _quotes.GetQuote();
        return View();
    }

    // Attribute route: /about-us
    [Route("about-us")]
    public IActionResult About()
    {
        return Content("Aptech North Nazimabad - ASP.NET Core batch");
    }
}
