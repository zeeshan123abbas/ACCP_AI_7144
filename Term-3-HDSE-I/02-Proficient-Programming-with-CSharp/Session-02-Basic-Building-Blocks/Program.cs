// Session 02: Variables, constants, operators and console I/O
const string Institute = "Aptech North Nazimabad";
const string Welcome = $"Fee calculator - {Institute}";

Console.WriteLine(Welcome);
Console.WriteLine(new string('-', Welcome.Length));

Console.Write("Student name: ");
string name = Console.ReadLine() ?? "Unknown";

Console.Write("Monthly fee (Rs): ");
if (!decimal.TryParse(Console.ReadLine(), out decimal monthlyFee))
{
    Console.WriteLine("Invalid amount, using Rs 8,500.");
    monthlyFee = 8500m;
}

const int Months = 6;
const decimal DiscountRate = 0.10m;
decimal total = monthlyFee * Months;
bool getsDiscount = total >= 50_000m && name.Length > 0;
decimal discount = getsDiscount ? total * DiscountRate : 0;

Console.WriteLine($"\nStudent\t: {name}");
Console.WriteLine($"Total\t: {total,12:N2}");
Console.WriteLine($"Discount\t: {discount,12:N2}");
Console.WriteLine($"Payable\t: {total - discount,12:N2}");
Console.WriteLine($"7 / 2 = {7 / 2}, 7 / 2.0 = {7 / 2.0}, 7 % 2 = {7 % 2}");

string path = @"C:\Students\Report.txt";
string json = """{ "course": "C#", "level": 3 }""";
Console.WriteLine($"Saved to {path}\nJSON: {json}");
Console.WriteLine($"GPA for 86 marks: {MathHelper.ToGpa(86)}");
