using Microsoft.EntityFrameworkCore;
using UowDemo.Models;

namespace UowDemo.Data;

public class AppDbContext : DbContext
{
    public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

    public DbSet<Customer> Customers => Set<Customer>();
    public DbSet<Order> Orders => Set<Order>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Customer>().Property(c => c.TotalSpent).HasPrecision(12, 2);
        modelBuilder.Entity<Order>().Property(o => o.Amount).HasPrecision(12, 2);
        modelBuilder.Entity<Customer>().HasData(new Customer { Id = 1, Name = "Danish Traders" });
    }
}
