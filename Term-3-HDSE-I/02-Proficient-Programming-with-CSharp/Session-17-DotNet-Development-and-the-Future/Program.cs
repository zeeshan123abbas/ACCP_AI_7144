// Session 17: A tour of modern .NET 8 / C# 12 features (one small example each)
using System.Collections.Frozen;
using System.Runtime.InteropServices;
using System.Text.Json;

// ===== 1. Which .NET am I running? =====
Console.WriteLine($"1) Runtime: {RuntimeInformation.FrameworkDescription}");
Console.WriteLine($"   OS     : {RuntimeInformation.OSDescription}");
Console.WriteLine($"   CPU    : {RuntimeInformation.ProcessArchitecture}, cores = {Environment.ProcessorCount}");

// ===== 2. Top-level statements (.NET 6+) =====
// This whole file has no "class Program" or "static void Main" - the compiler adds them.
Console.WriteLine("2) Top-level statements: no Main method needed!");

// ===== 3. Collection expressions (C# 12) =====
int[] marks = [78, 92, 45, 66];
List<string> cities = ["Karachi", "Lahore", "Islamabad"];
Console.WriteLine($"3) Collection expressions: {marks.Length} marks, {cities.Count} cities");

// ===== 4. Primary constructor (C# 12) - see the Course class at the bottom =====
var course = new Course("C# Programming", 36);
Console.WriteLine($"4) Primary constructor: {course.Describe()}");

// ===== 5. Records (C# 9+) - data classes with value equality =====
var s1 = new Student("R-101", "Ayesha");
var s2 = new Student("R-101", "Ayesha");
Console.WriteLine($"5) Records equal? {s1 == s2} -> {s1}");

// ===== 6. Pattern matching with switch expressions =====
string Grade(int m) => m switch
{
    >= 85 => "A",
    >= 70 and < 85 => "B",
    >= 50 => "C",
    _ => "F"
};
Console.WriteLine($"6) Pattern matching: 92 -> {Grade(92)}, 45 -> {Grade(45)}");

// ===== 7. Raw string literals (C# 11) - no escaping needed =====
string json = """
    { "name": "Ayesha", "marks": 92 }
    """;
Console.WriteLine($"7) Raw string: {json.Trim()}");

// ===== 8. Built-in JSON (System.Text.Json) =====
Student? fromJson = JsonSerializer.Deserialize<Student>("""{"RollNo":"R-202","Name":"Omar"}""");
Console.WriteLine($"8) JSON -> object: {fromJson?.Name}; object -> JSON: {JsonSerializer.Serialize(s1)}");

// ===== 9. New in .NET 8: Random.Shared.GetItems and Shuffle =====
string[] colours = ["Red", "Green", "Blue", "Yellow"];
string[] picked = Random.Shared.GetItems(colours, 2);   // pick 2 random items (an item may repeat)
Random.Shared.Shuffle(colours);                          // shuffle in place
Console.WriteLine($"9) Random picks: {string.Join(", ", picked)} | shuffled: {string.Join(", ", colours)}");

// ===== 10. New in .NET 8: FrozenDictionary (read-only, very fast lookups) =====
var cityCodes = new Dictionary<string, string>
{
    ["Karachi"] = "KHI",
    ["Lahore"] = "LHE",
    ["Islamabad"] = "ISB"
}.ToFrozenDictionary();
Console.WriteLine($"10) FrozenDictionary: Karachi = {cityCodes["Karachi"]}");

// ===== 11. New in .NET 8: TimeProvider (makes time testable) =====
TimeProvider clock = TimeProvider.System;
Console.WriteLine($"11) TimeProvider UTC now: {clock.GetUtcNow():yyyy-MM-dd HH:mm}");

// ---------- Types used above ----------
public record Student(string RollNo, string Name);

public class Course(string title, int hours)   // primary constructor parameters
{
    public string Describe() => $"{title} runs for {hours} hours";
}
