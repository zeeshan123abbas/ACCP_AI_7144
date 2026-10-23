// Session 08: Lab and Review - using the library model
var ayesha = new Member("Ayesha");
var hamza = new Member("Hamza", limit: 3);

var items = new List<LibraryItem>
{
    new Book("Clean Code", "Robert C. Martin"),
    new Book("The Pragmatic Programmer", "Hunt & Thomas"),
    new Dvd("Intro to .NET 8", 95),
    new Magazine("Spectrum Monthly")
};

((IBorrowable)items[0]).Borrow(ayesha);
((IBorrowable)items[2]).Borrow(ayesha);

try
{
    ((IBorrowable)items[1]).Borrow(ayesha);      // third item: over the limit
}
catch (InvalidOperationException ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}

try
{
    ((IBorrowable)items[0]).Borrow(hamza);       // already borrowed
}
catch (InvalidOperationException ex)
{
    Console.WriteLine($"Error: {ex.Message}");
}

Console.WriteLine();
items.ForEach(Console.WriteLine);

Console.WriteLine("\nLate fee for 6 days:");
foreach (var item in items)
    Console.WriteLine($"  {item.Title,-28} Rs {item.LateFee(6),5:N0}");

((IBorrowable)items[0]).Return();
Console.WriteLine($"\nAfter return, {ayesha.Name} holds {ayesha.Items.Count} item(s).");
Console.WriteLine($"Borrowable items: {items.Count(i => i is IBorrowable)}");
