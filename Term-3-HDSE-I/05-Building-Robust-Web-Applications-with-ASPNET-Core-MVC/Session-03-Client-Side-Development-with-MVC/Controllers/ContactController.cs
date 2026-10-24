using ClientSide.Models;
using Microsoft.AspNetCore.Mvc;

namespace ClientSide.Controllers;

public class ContactController : Controller
{
    // GET /Contact/Create  -> show the empty form
    [HttpGet]
    public IActionResult Create()
    {
        return View();
    }

    // POST /Contact/Create  -> check the data on the SERVER
    [HttpPost]
    [ValidateAntiForgeryToken]
    public IActionResult Create(Contact contact)
    {
        if (!ModelState.IsValid)
        {
            return View(contact);   // show the form again with errors
        }
        TempData["Name"] = contact.Name;
        return RedirectToAction("Thanks");
    }

    public IActionResult Thanks()
    {
        return Content($"Thank you, {TempData["Name"]}! We will reply soon.");
    }
}
