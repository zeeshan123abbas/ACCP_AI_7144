using Microsoft.EntityFrameworkCore;
using UowDemo.Data;

namespace UowDemo.Repositories;

// Generic EF Core implementation. Notice: NO SaveChanges here!
public class Repository<T> : IRepository<T> where T : class
{
    protected readonly AppDbContext _db;
    private readonly DbSet<T> _set;

    public Repository(AppDbContext db)
    {
        _db = db;
        _set = db.Set<T>();
    }

    public Task<List<T>> GetAllAsync() => _set.ToListAsync();

    public async Task<T?> GetByIdAsync(int id) => await _set.FindAsync(id);

    public async Task AddAsync(T entity) => await _set.AddAsync(entity);

    public void Remove(T entity) => _set.Remove(entity);
}
