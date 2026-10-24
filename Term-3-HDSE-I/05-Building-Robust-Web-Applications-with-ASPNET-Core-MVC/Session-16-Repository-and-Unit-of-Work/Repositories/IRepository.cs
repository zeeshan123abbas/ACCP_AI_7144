namespace UowDemo.Repositories;

// One generic interface for the common operations on ANY entity
public interface IRepository<T> where T : class
{
    Task<List<T>> GetAllAsync();
    Task<T?> GetByIdAsync(int id);
    Task AddAsync(T entity);
    void Remove(T entity);
}
