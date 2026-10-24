using LibraryLab.Models;
using Microsoft.EntityFrameworkCore;

namespace LibraryLab.Data;

public class LibraryContext : DbContext
{
    public LibraryContext(DbContextOptions<LibraryContext> options) : base(options) { }

    public DbSet<Book> Books => Set<Book>();
}
