// Session 13: Generics and iterators
var courses = new Repository<Course>();
courses.Add(new Course(1, "C# Programming", 36));
courses.Add(new Course(2, "SQL Server", 32));
courses.Add(new Course(3, "Angular", 24));

foreach (var c in courses) Console.WriteLine(c);
Console.WriteLine($"Long courses: {string.Join(", ", courses.Where(c => c.Hours > 30).Select(c => c.Title))}");
Console.WriteLine($"Find 2: {courses.Find(2)?.Title}");

var trainers = new Repository<Trainer> { new Trainer(7, "Sir Zeeshan") };
Console.WriteLine($"Trainers: {trainers.Count()}");

Console.WriteLine(Util.Max(14, 9));
Console.WriteLine(Util.Max("Karachi", "Lahore"));
Console.WriteLine(string.Join(" ", Util.Evens(10)));
