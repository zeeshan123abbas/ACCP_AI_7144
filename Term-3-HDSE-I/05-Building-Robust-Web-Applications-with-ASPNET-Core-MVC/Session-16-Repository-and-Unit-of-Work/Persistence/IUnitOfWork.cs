using UowDemo.Models;
using UowDemo.Repositories;

namespace UowDemo.Persistence;

// Groups repositories and saves all their changes together
public interface IUnitOfWork
{
    IRepository<Customer> Customers { get; }
    IRepository<Order> Orders { get; }

    Task<int> CompleteAsync();   // one SaveChanges = one transaction
}
