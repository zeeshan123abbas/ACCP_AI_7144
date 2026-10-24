using LibraryOnion.Domain;

namespace LibraryOnion.Service;

public class LoanService
{
    public const int MaxBooksPerMember = 3;
    private readonly IBookRepository _books;

    public LoanService(IBookRepository books)
    {
        _books = books;
    }

    // Returns a message instead of throwing, to keep the lab simple
    public string Borrow(int bookId, string member)
    {
        var book = _books.GetById(bookId);
        if (book == null) return "Book not found";
        if (book.IsBorrowed) return "Book is already borrowed";
        if (_books.CountBorrowedBy(member) >= MaxBooksPerMember) return "Limit reached";

        book.IsBorrowed = true;
        book.BorrowedBy = member;
        _books.Update(book);
        return "OK";
    }
}
