// Session 15: Advanced concepts in C# - one small example per idea

// ===== 1. Anonymous method (delegate with no name) =====
Func<int, int> doubleIt = delegate (int x) { return x * 2; };
Console.WriteLine($"1) Anonymous method: double of 7 = {doubleIt(7)}");

// ===== 2. Lambda expression (shorter way to write the same thing) =====
Func<int, int> square = x => x * x;               // input => output
Console.WriteLine($"2) Lambda: square of 6 = {square(6)}");

// ===== 3. Built-in generic delegates: Func, Action, Predicate =====
Func<int, int, int> add = (a, b) => a + b;        // takes 2 ints, RETURNS an int
Action<string> greet = name => Console.WriteLine($"3) Action says: Salam, {name}!"); // returns nothing
Predicate<int> isEven = n => n % 2 == 0;          // takes 1 value, returns bool
greet("Sana");
Console.WriteLine($"   Func add(4,5) = {add(4, 5)}, Predicate isEven(10) = {isEven(10)}");

// ===== 4. Extension methods (see StringExtensions.cs) =====
Console.WriteLine($"4) Extension: {"ali raza khan".ToTitle()}, 45 passed? {45.IsPass()}");

// ===== 5. Anonymous type (a quick object without writing a class) =====
var laptop = new { Brand = "Dell", Ram = 16, Price = 185000 };
Console.WriteLine($"5) Anonymous type: {laptop.Brand} with {laptop.Ram} GB costs Rs {laptop.Price:N0}");

// ===== 6. Partial class (see Student.Info.cs + Student.Methods.cs) =====
var student = new Student { Name = "Hira", Marks = 88 };
Console.WriteLine($"6) Partial class: {student.Name} got grade {student.Grade()}");

// ===== 7. Nullable types and null safety =====
int? bonusMarks = null;                           // a value type that can also be null
Console.WriteLine($"7) Has bonus? {bonusMarks.HasValue}, bonus or 0 = {bonusMarks ?? 0}");
string? email = student.Email;                    // may be null
Console.WriteLine($"   Email length: {email?.Length ?? 0}");  // ?. stops if null, ?? gives a default

// ===== 8. LINQ query expression vs method syntax =====
List<Student> batch =
[
    new Student { Name = "Ali", Marks = 72 },
    new Student { Name = "Sana", Marks = 91 },
    new Student { Name = "Bilal", Marks = 45 },
    new Student { Name = "Zoya", Marks = 66 }
];

// Query syntax (looks like SQL)
var passedQuery = from s in batch
                  where s.Marks >= 50
                  orderby s.Marks descending
                  select s.Name;
Console.WriteLine($"8) Passed (query syntax): {string.Join(", ", passedQuery)}");

// Method syntax (uses lambdas) - same result
var passedMethod = batch.Where(s => s.Marks >= 50).OrderByDescending(s => s.Marks).Select(s => s.Name);
Console.WriteLine($"   Passed (method syntax): {string.Join(", ", passedMethod)}");
Console.WriteLine($"   Average marks: {batch.Average(s => s.Marks):F1}");

// ===== 9. Parallel programming: use all CPU cores =====
long[] results = new long[5];
Parallel.For(0, 5, i =>
{
    results[i] = (long)i * i;                     // each i may run on a different core
});
Console.WriteLine($"9) Parallel.For squares: {string.Join(", ", results)}");

// ===== 10. dynamic: type is checked at RUN time, not compile time =====
dynamic value = 10;
Console.WriteLine($"10) dynamic as int: {value + 5}");
value = "Karachi";
Console.WriteLine($"    dynamic as string: {value.ToUpper()}");

// ===== 11. async / await (intro) =====
Console.WriteLine("11) Downloading report...");
string report = await DownloadReportAsync();      // waits WITHOUT freezing the program
Console.WriteLine($"    {report}");

// A method that pretends to do slow work (like calling a web API)
static async Task<string> DownloadReportAsync()
{
    await Task.Delay(1000);                       // simulate a 1 second wait
    return "Report ready!";
}
