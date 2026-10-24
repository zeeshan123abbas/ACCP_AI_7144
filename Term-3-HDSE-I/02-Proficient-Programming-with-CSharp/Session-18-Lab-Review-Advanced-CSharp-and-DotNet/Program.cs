// Session 18: Lab and Review - Course Enrollment Desk
// Combines: records, generics, delegates, events, exceptions, extension methods, LINQ, async.

// Step 1: the courses on offer
Course[] courses =
[
    new(1, "C# Programming", 15000m, 2),
    new(2, "Angular", 12000m, 3),
    new(3, "ASP.NET Core MVC", 18000m, 2)
];

// Step 2: create the desk and listen to its event
var desk = new EnrollmentDesk();
desk.StudentEnrolled += e => Console.WriteLine($"[OK] {e.StudentName} joined {e.Course.Title}");

// Step 3: try some enrollments (some will fail on purpose)
(string Name, int CourseId)[] requests =
[
    ("Ali", 1), ("Sana", 1), ("Bilal", 1),   // third one: C# is full
    ("Hira", 2), ("", 2),                    // empty name
    ("Omar", 3), ("Zoya", 2)
];

foreach (var request in requests)
{
    Course course = courses.First(c => c.Id == request.CourseId);
    try
    {
        desk.Enroll(request.Name, course);
    }
    catch (CourseFullException ex)
    {
        Console.WriteLine($"[FULL] {ex.Message}");
    }
    catch (ArgumentException ex)
    {
        Console.WriteLine($"[ERROR] {ex.Message}");
    }
}

// Step 4: reports with LINQ
Console.WriteLine("\n--- Students per course ---");
var perCourse = desk.All
    .GroupBy(e => e.Course.Title)
    .Select(g => new { Course = g.Key, Count = g.Count(), Income = g.Sum(e => e.Course.Fee) });

foreach (var row in perCourse)
    Console.WriteLine($"{row.Course,-18} {row.Count} student(s)  {row.Income.ToRupees()}");

decimal totalIncome = desk.All.Sum(e => e.Course.Fee);
Console.WriteLine($"Total income: {totalIncome.ToRupees()}");

var names = desk.All.Select(e => e.StudentName).OrderBy(n => n);
Console.WriteLine($"All students (A-Z): {string.Join(", ", names)}");

// Step 5: save asynchronously
Console.WriteLine("\nSaving...");
int saved = await desk.SaveAsync();
Console.WriteLine($"Saved {saved} enrollments.");
