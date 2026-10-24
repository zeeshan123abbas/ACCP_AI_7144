using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace Modern.Pages;

// A Razor Page: the page and its handler code live side by side
public class HelloModel : PageModel
{
    [BindProperty]                 // fill Name from the posted form
    public string Name { get; set; } = "";

    public string Message { get; set; } = "";

    public void OnGet()            // runs for GET /Hello
    {
        Message = "Type your name and press Greet.";
    }

    public void OnPost()           // runs for POST /Hello
    {
        Message = $"Assalam-o-Alaikum, {Name}!";
    }
}
