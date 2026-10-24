using ActionsApi.Data;
using Microsoft.AspNetCore.Mvc;

namespace ActionsApi.Controllers;

public class ProductsController : Controller
{
    // 1. ContentResult: plain text
    public IActionResult Index()
    {
        return Content($"We have {ProductStore.Products.Count} products. Try /Products/Details/1");
    }

    // 2. ViewResult + sharing data with ViewData, ViewBag and the model
    public IActionResult Details(int id)
    {
        var product = ProductStore.Products.FirstOrDefault(p => p.Id == id);
        if (product == null)
        {
            return NotFound();                 // 3. 404 result
        }
        ViewData["Title"] = "Product details"; // dictionary style
        ViewBag.Shop = "Aptech Tech Store";    // dynamic style (same storage as ViewData)
        return View(product);                  // strongly typed model (best)
    }

    // 4. JsonResult
    public IActionResult AsJson()
    {
        return Json(ProductStore.Products);
    }

    // 5. TempData survives ONE redirect
    public IActionResult Buy(int id)
    {
        TempData["Message"] = $"Product {id} added to cart";
        return RedirectToAction(nameof(Thanks));   // 6. redirect result
    }

    public IActionResult Thanks()
    {
        return Content(TempData["Message"]?.ToString() ?? "Nothing in TempData");
    }
}
