using UowDemo.Data;
using UowDemo.Models;
using UowDemo.Repositories;

namespace UowDemo.Persistence;

public class UnitOfWork : IUnitOfWork
{
    private readonly AppDbContext _db;

    public UnitOfWork(AppDbContext db)
    {
        _db = db;
        // Both repositories share the SAME DbContext
        Customers = new Repository<Customer>(db);
        Orders = new Repository<Order>(db);
    }

    public IRepository<Customer> Customers { get; }
    public IRepository<Order> Orders { get; }

    public Task<int> CompleteAsync() => _db.SaveChangesAsync();
}
