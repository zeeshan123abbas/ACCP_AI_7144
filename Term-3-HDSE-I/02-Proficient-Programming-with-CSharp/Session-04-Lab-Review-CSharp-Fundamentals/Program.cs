// Session 04: Lab and Review - Student Marks Manager
const int Max = 10;
string[] names = new string[Max];
int[] marks = new int[Max];
int count = 0;

while (true)
{
    Console.WriteLine("\n=== Marks Manager ===");
    Console.WriteLine("1) Add student  2) List  3) Statistics  4) Search  0) Exit");
    Console.Write("Choice: ");
    string? input = Console.ReadLine();
    if (input is null) return;   // end of input stream

    switch (input)
    {
        case "1":
            if (count == Max) { Console.WriteLine("List is full."); break; }
            Console.Write("Name: ");
            names[count] = Console.ReadLine() ?? "";
            marks[count] = ReadInt("Marks (0-100): ", 0, 100);
            count++;
            break;
        case "2":
            for (int i = 0; i < count; i++)
                Console.WriteLine($"{i + 1,2}. {names[i],-15} {marks[i],3}  {Grade(marks[i])}");
            break;
        case "3":
            if (count == 0) { Console.WriteLine("No data."); break; }
            int[] copy = marks[..count];
            Array.Sort(copy);
            Console.WriteLine($"Avg {copy.Average():F1} | Min {copy[0]} | Max {copy[^1]}");
            break;
        case "4":
            Console.Write("Name to find: ");
            string target = Console.ReadLine() ?? "";
            int pos = Array.FindIndex(names, 0, count,
                      n => n.Equals(target, StringComparison.OrdinalIgnoreCase));
            Console.WriteLine(pos >= 0 ? $"{names[pos]} has {marks[pos]}" : "Not found");
            break;
        case "0":
            return;
        default:
            Console.WriteLine("Invalid option.");
            break;
    }
}

static int ReadInt(string prompt, int min, int max)
{
    int value;
    do { Console.Write(prompt); }
    while (!int.TryParse(Console.ReadLine(), out value) || value < min || value > max);
    return value;
}

static string Grade(int m) => m switch { >= 85 => "A", >= 70 => "B", >= 50 => "C", _ => "F" };
