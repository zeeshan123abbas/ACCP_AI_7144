// Session 03: Selection, loops, jump statements and arrays
int[] marks = { 78, 92, 45, 66, 85, 59, 100, 38 };

foreach (int m in marks)
{
    string grade = m switch { >= 85 => "A", >= 70 => "B", >= 50 => "C", _ => "F" };
    Console.Write($"{m}:{grade}  ");
}
Console.WriteLine();

int sumPassed = 0;
for (int i = 0; i < marks.Length; i++)
{
    if (marks[i] < 50) continue;
    if (marks[i] == 100) { Console.WriteLine("Perfect score found, stop."); break; }
    sumPassed += marks[i];
}
Console.WriteLine($"Sum of passed (until perfect score): {sumPassed}");

int[] sorted = (int[])marks.Clone();
Array.Sort(sorted);
Console.WriteLine($"Sorted: {string.Join(", ", sorted)}");
Console.WriteLine($"Highest: {sorted[^1]}, Lowest: {sorted[0]}, Top 3: {string.Join(",", sorted[^3..])}");
Console.WriteLine($"Index of 66 in sorted: {Array.BinarySearch(sorted, 66)}");
Console.WriteLine($"Any below 40? {Array.Exists(marks, m => m < 40)}");

int[,] table = { { 80, 70 }, { 90, 60 }, { 55, 75 } };
for (int r = 0; r < table.GetLength(0); r++)
    Console.WriteLine($"Student {r + 1}: SQL={table[r, 0]}, C#={table[r, 1]}");

string[][] batches =
{
    new[] { "Ali", "Sana" },
    new[] { "Bilal", "Hira", "Usman" },
    new[] { "Zoya" }
};
for (int b = 0; b < batches.Length; b++)
    Console.WriteLine($"Batch {b + 1} ({batches[b].Length}): {string.Join(", ", batches[b])}");

int choice;
do
{
    Console.Write("1) Average  2) Count passed  0) Exit : ");
    int.TryParse(Console.ReadLine(), out choice);
    switch (choice)
    {
        case 1: Console.WriteLine($"Average = {marks.Average():F1}"); break;
        case 2: Console.WriteLine($"Passed = {Array.FindAll(marks, m => m >= 50).Length}"); break;
        case 0: Console.WriteLine("Allah Hafiz!"); break;
        default: Console.WriteLine("Invalid choice"); break;
    }
} while (choice != 0);
