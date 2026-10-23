// Session 01: First C# program on .NET 8 (top-level statements)
using System.Runtime.InteropServices;

Console.Title = "Hello .NET";
Console.WriteLine("Assalam-o-Alaikum! Welcome to C# on .NET 8");

Console.Write("What is your name? ");
string? name = Console.ReadLine();
if (string.IsNullOrWhiteSpace(name)) name = "Student";

Console.WriteLine($"Nice to meet you, {name}!");
Console.WriteLine($"Runtime : {RuntimeInformation.FrameworkDescription}");
Console.WriteLine($"OS      : {RuntimeInformation.OSDescription}");
Console.WriteLine($"64-bit  : {Environment.Is64BitProcess}");
Console.WriteLine($"Today   : {DateTime.Now:dddd, dd MMMM yyyy}");
