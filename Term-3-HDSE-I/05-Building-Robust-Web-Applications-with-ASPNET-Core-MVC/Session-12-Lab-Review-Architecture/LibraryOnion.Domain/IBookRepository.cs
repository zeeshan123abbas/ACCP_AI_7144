namespace LibraryOnion.Domain;

public interface IBookRepository
{
    Book? GetById(int id);
    int CountBorrowedBy(string member);
    void Update(Book book);
}
