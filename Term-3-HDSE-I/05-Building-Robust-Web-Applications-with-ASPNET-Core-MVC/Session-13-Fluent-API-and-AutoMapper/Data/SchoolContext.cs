using FluentMapper.Models;
using Microsoft.EntityFrameworkCore;

namespace FluentMapper.Data;

public class SchoolContext : DbContext
{
    public SchoolContext(DbContextOptions<SchoolContext> options) : base(options) { }

    public DbSet<Student> Students => Set<Student>();
    public DbSet<Course> Courses => Set<Course>();

    // Fluent API: configure the database model in code
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Student>(entity =>
        {
            entity.ToTable("tblStudents");                          // custom table name
            entity.HasKey(s => s.Id);                               // primary key
            entity.Property(s => s.FullName).IsRequired().HasMaxLength(80);
            entity.Property(s => s.Email).IsRequired().HasMaxLength(120);
            entity.HasIndex(s => s.Email).IsUnique();               // no duplicate emails

            entity.HasOne(s => s.Course)                            // relationship
                  .WithMany(c => c.Students)
                  .HasForeignKey(s => s.CourseId);
        });

        modelBuilder.Entity<Course>(entity =>
        {
            entity.Property(c => c.Title).IsRequired().HasMaxLength(60);
            entity.Property(c => c.Fee).HasPrecision(10, 2);

            // Seed data
            entity.HasData(
                new Course { Id = 1, Title = "ASP.NET Core MVC", Fee = 15000 },
                new Course { Id = 2, Title = "Angular", Fee = 12000 });
        });
    }
}
