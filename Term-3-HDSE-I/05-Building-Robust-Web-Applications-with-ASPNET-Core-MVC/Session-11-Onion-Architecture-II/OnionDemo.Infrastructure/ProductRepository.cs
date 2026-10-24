using Microsoft.EntityFrameworkCore;
using OnionDemo.Domain;

namespace OnionDemo.Infrastructure;

// EF Core implementation of the Domain interface
public class ProductRepository : IProductRepository
{
    private readonly AppDbContext _db;

    public ProductRepository(AppDbContext db)
    {
        _db = db;
    }

    public Task<List<Product>> GetAllAsync() => _db.Products.AsNoTracking().ToListAsync();

    public Task<Product?> GetByIdAsync(int id) => _db.Products.FindAsync(id).AsTask();

    public async Task AddAsync(Product product)
    {
        _db.Products.Add(product);
        await _db.SaveChangesAsync();
    }
}
