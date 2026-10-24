using Microsoft.EntityFrameworkCore;
using SchoolData.Models;

namespace SchoolData.Data;

// The DbContext is our "session" with the database.
public class SchoolContext : DbContext
{
    public SchoolContext(DbContextOptions<SchoolContext> options) : base(options) { }

    // Each DbSet becomes a table: Students
    public DbSet<Student> Students => Set<Student>();
}
