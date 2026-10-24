using LibraryOnion.Domain;
using LibraryOnion.Service;
using Xunit;

namespace LibraryOnion.Tests;

public class LoanServiceTests
{
    [Fact]
    public void Borrow_FreeBook_ReturnsOk()
    {
        // Arrange
        var repo = new FakeBookRepository();
        repo.Books.Add(new Book { Id = 1, Title = "C# Basics" });
        var service = new LoanService(repo);

        // Act
        string result = service.Borrow(1, "Ali");

        // Assert
        Assert.Equal("OK", result);
        Assert.True(repo.Books[0].IsBorrowed);
    }

    [Fact]
    public void Borrow_AlreadyBorrowed_IsRejected()
    {
        var repo = new FakeBookRepository();
        repo.Books.Add(new Book { Id = 1, IsBorrowed = true, BorrowedBy = "Sara" });
        var service = new LoanService(repo);

        Assert.Equal("Book is already borrowed", service.Borrow(1, "Ali"));
    }
}
