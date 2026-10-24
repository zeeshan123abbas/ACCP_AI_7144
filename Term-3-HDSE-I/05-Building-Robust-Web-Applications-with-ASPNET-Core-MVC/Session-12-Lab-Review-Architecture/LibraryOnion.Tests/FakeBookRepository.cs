using LibraryOnion.Domain;

namespace LibraryOnion.Tests;

// A fake repository: no database needed to test the business rules
public class FakeBookRepository : IBookRepository
{
    public List<Book> Books { get; } = new();

    public Book? GetById(int id) => Books.FirstOrDefault(b => b.Id == id);

    public int CountBorrowedBy(string member) => Books.Count(b => b.BorrowedBy == member);

    public void Update(Book book) { /* list already holds the same object */ }
}
