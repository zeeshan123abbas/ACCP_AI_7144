using Microsoft.AspNetCore.Mvc;
using Microsoft.Data.Sqlite;
using SchoolData.Data;

namespace SchoolData.Controllers;

public class StudentsController : Controller
{
    private readonly SchoolContext _db;
    private readonly IConfiguration _config;

    public StudentsController(SchoolContext db, IConfiguration config)
    {
        _db = db;          // EF Core context, given to us by DI
        _config = config;  // used to read the connection string
    }

    // GET /Students  -> list students using EF Core (LINQ)
    public IActionResult Index()
    {
        var students = _db.Students.OrderBy(s => s.Name).ToList();
        return View(students);
    }

    // GET /Students/Ado  -> same data using plain ADO.NET
    public IActionResult Ado()
    {
        var names = new List<string>();

        using var connection = new SqliteConnection(_config.GetConnectionString("School"));
        connection.Open();

        using var command = connection.CreateCommand();
        command.CommandText = "SELECT Name FROM Students WHERE Age >= $minAge";
        command.Parameters.AddWithValue("$minAge", 18);   // parameter = safe from SQL injection

        using var reader = command.ExecuteReader();
        while (reader.Read())
        {
            names.Add(reader.GetString(0));
        }
        return Content("Adults (ADO.NET): " + string.Join(", ", names));
    }
}
