// Session 07 - Example 5: a C# client that consumes the hosted Web API
using System.Net.Http.Json;

// Step 1: the API address (pass your Azure URL as an argument)
string baseUrl = args.Length > 0 ? args[0] : "http://localhost:5000/";
var http = new HttpClient { BaseAddress = new Uri(baseUrl) };

// Step 2: GET - JSON is turned into C# objects automatically
List<Student>? students = await http.GetFromJsonAsync<List<Student>>("api/students");
Console.WriteLine($"The API returned {students?.Count ?? 0} students:");
foreach (Student s in students ?? new List<Student>())
    Console.WriteLine($"  {s.Name} ({s.Course}) - {s.Marks}");

// Step 3: POST - send a new student as JSON
var newStudent = new Student(0, "Zara", "Azure", 85);
HttpResponseMessage response = await http.PostAsJsonAsync("api/students", newStudent);
Console.WriteLine($"POST status: {(int)response.StatusCode} {response.StatusCode}");

// The shape of the data we expect from the API
public record Student(int Id, string Name, string Course, int Marks);
