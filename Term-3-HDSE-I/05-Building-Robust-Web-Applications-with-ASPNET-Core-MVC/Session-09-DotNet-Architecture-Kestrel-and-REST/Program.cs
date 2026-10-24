using RestKestrel.Models;

namespace RestKestrel;

// We write Main by hand (instead of top-level statements) to SEE the start-up steps
public class Program
{
    private static readonly List<Book> Books = new()
    {
        new Book { Id = 1, Title = "Clean Code", Author = "Robert C. Martin" },
        new Book { Id = 2, Title = "The Pragmatic Programmer", Author = "Hunt and Thomas" }
    };

    public static void Main(string[] args)
    {
        Console.WriteLine("1. Main started");

        // Step 1: the builder reads config, sets up logging and DI
        var builder = WebApplication.CreateBuilder(args);

        // Step 2: configure Kestrel (the built-in web server)
        builder.WebHost.ConfigureKestrel(options =>
        {
            options.ListenLocalhost(5050);                          // http://localhost:5050
            options.Limits.MaxRequestBodySize = 1 * 1024 * 1024;    // 1 MB max upload
        });

        var app = builder.Build();
        Console.WriteLine("2. App built, adding middleware");

        // Step 3: a tiny custom middleware (OWIN-style "request in, response out")
        app.Use(async (context, next) =>
        {
            Console.WriteLine($"--> {context.Request.Method} {context.Request.Path}");
            await next(context);                                    // call the next middleware
            Console.WriteLine($"<-- {context.Response.StatusCode}");
        });

        // Step 4: REST endpoints for the "books" resource
        var books = app.MapGroup("/api/books");

        books.MapGet("/", () => Results.Ok(Books));                 // 200

        books.MapGet("/{id:int}", (int id) =>
        {
            var book = Books.FirstOrDefault(b => b.Id == id);
            return book is null ? Results.NotFound() : Results.Ok(book);   // 404 or 200
        });

        books.MapPost("/", (Book book) =>
        {
            book.Id = Books.Count == 0 ? 1 : Books.Max(b => b.Id) + 1;
            Books.Add(book);
            return Results.Created($"/api/books/{book.Id}", book);        // 201
        });

        books.MapPut("/{id:int}", (int id, Book input) =>
        {
            var book = Books.FirstOrDefault(b => b.Id == id);
            if (book is null) return Results.NotFound();
            book.Title = input.Title;
            book.Author = input.Author;
            return Results.NoContent();                                   // 204
        });

        books.MapDelete("/{id:int}", (int id) =>
        {
            int removed = Books.RemoveAll(b => b.Id == id);
            return removed == 0 ? Results.NotFound() : Results.NoContent();
        });

        Console.WriteLine("3. Starting Kestrel...");
        app.Run();   // blocks here and listens for requests
    }
}
