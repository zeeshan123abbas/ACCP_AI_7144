// Session 08: Lab and Review - library model
public interface IBorrowable
{
    void Borrow(Member member);
    void Return();
}

public abstract class LibraryItem(string title)
{
    public string Title { get; } = title;
    public Member? BorrowedBy { get; protected set; }
    public bool IsBorrowed => BorrowedBy is not null;
    public abstract decimal LateFee(int daysLate);
    public override string ToString() =>
        $"{GetType().Name,-9} {Title,-28} {(IsBorrowed ? "out: " + BorrowedBy!.Name : "available")}";
}

public class Book(string title, string author) : LibraryItem(title), IBorrowable
{
    public string Author { get; } = author;
    public override decimal LateFee(int daysLate) => daysLate * 20m;
    public void Borrow(Member m)
    {
        if (IsBorrowed) throw new InvalidOperationException($"{Title} is already borrowed.");
        m.Add(this);
        BorrowedBy = m;
    }
    public void Return() { BorrowedBy?.Remove(this); BorrowedBy = null; }
}

public class Dvd(string title, int minutes) : LibraryItem(title), IBorrowable
{
    public int Minutes { get; } = minutes;
    public override decimal LateFee(int daysLate) => Math.Min(daysLate * 50m, 500m);
    public void Borrow(Member m) { m.Add(this); BorrowedBy = m; }
    public void Return() { BorrowedBy?.Remove(this); BorrowedBy = null; }
}

public class Magazine(string title) : LibraryItem(title)
{
    public override decimal LateFee(int daysLate) => 0;
}

public class Member(string name, int limit = 2)
{
    private readonly List<LibraryItem> _items = new();
    public string Name { get; } = name;
    public IReadOnlyList<LibraryItem> Items => _items;
    internal void Add(LibraryItem item)
    {
        if (_items.Count >= limit) throw new InvalidOperationException($"{Name} reached the limit of {limit}.");
        _items.Add(item);
    }
    internal void Remove(LibraryItem item) => _items.Remove(item);
}
