namespace LibraryOnion.Domain;

public class Book
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public bool IsBorrowed { get; set; }
    public string? BorrowedBy { get; set; }
}
