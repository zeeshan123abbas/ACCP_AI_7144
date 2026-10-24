using System.Text.Json;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace IdentitySession.Controllers;

[Authorize]   // only logged-in users have a cart
public class CartController : Controller
{
    private const string CartKey = "Cart";

    public IActionResult Index()
    {
        List<string> items = ReadCart();
        return Content($"Hello {User.Identity!.Name}! Cart ({items.Count}): {string.Join(", ", items)}\n" +
                       "Add items with /Cart/Add?item=Notebook");
    }

    // Demo uses GET for simplicity; real apps should use POST for changes
    public IActionResult Add(string item)
    {
        List<string> items = ReadCart();
        items.Add(item);
        HttpContext.Session.SetString(CartKey, JsonSerializer.Serialize(items));   // save to session
        return RedirectToAction(nameof(Index));
    }

    private List<string> ReadCart()
    {
        string? json = HttpContext.Session.GetString(CartKey);                     // read from session
        return json == null ? new List<string>() : JsonSerializer.Deserialize<List<string>>(json)!;
    }
}
