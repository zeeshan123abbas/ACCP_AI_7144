using LibraryLab.Data;
using LibraryLab.Models;
using Microsoft.AspNetCore.Mvc;

namespace LibraryLab.Controllers;

public class BooksController : Controller
{
    private readonly LibraryContext _db;

    public BooksController(LibraryContext db)
    {
        _db = db;
    }

    // GET /Books
    public IActionResult Index()
    {
        var books = _db.Books.OrderBy(b => b.Title).ToList();
        return View(books);
    }

    // GET /Books/Create
    public IActionResult Create()
    {
        return View(new Book());
    }

    // POST /Books/Create
    [HttpPost, ValidateAntiForgeryToken]
    public IActionResult Create(Book book)
    {
        if (!ModelState.IsValid) return View(book);

        _db.Books.Add(book);     // Step 1: tell EF about the new row
        _db.SaveChanges();       // Step 2: run the INSERT
        return RedirectToAction(nameof(Index));
    }
}
