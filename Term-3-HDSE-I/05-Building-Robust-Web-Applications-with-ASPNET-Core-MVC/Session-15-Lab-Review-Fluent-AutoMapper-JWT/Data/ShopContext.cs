using Microsoft.EntityFrameworkCore;
using ShopApi.Models;

namespace ShopApi.Data;

public class ShopContext : DbContext
{
    public ShopContext(DbContextOptions<ShopContext> options) : base(options) { }

    public DbSet<Product> Products => Set<Product>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Picks up ProductConfiguration (and any other IEntityTypeConfiguration classes)
        modelBuilder.ApplyConfigurationsFromAssembly(typeof(ShopContext).Assembly);
    }
}
