// Session 18: Lab - the data types used by the enrollment desk

// A record is perfect for simple data
public record Course(int Id, string Title, decimal Fee, int Seats);

public record Enrollment(string StudentName, Course Course, DateTime Date);

// A custom exception for our business rule
public class CourseFullException(string courseTitle)
    : Exception($"Sorry, {courseTitle} has no seats left.");

// A small generic store that works for ANY type (generics, Session 13)
public class Store<T>
{
    private readonly List<T> items = [];

    public void Add(T item) => items.Add(item);

    public IReadOnlyList<T> All => items;

    // Accepts a rule as a Func (delegates, Session 11/15)
    public IEnumerable<T> Find(Func<T, bool> rule) => items.Where(rule);
}

// Extension method (Session 15)
public static class MoneyExtensions
{
    public static string ToRupees(this decimal amount) => $"Rs {amount:N0}";
}
