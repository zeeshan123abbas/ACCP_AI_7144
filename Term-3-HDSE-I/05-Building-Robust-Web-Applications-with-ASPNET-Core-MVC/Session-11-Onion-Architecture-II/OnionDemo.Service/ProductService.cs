using OnionDemo.Domain;

namespace OnionDemo.Service;

public class ProductService
{
    private readonly IProductRepository _repository;

    public ProductService(IProductRepository repository)
    {
        _repository = repository;
    }

    public Task<List<Product>> GetAllAsync() => _repository.GetAllAsync();

    public Task<Product?> GetByIdAsync(int id) => _repository.GetByIdAsync(id);

    public async Task<Product> CreateAsync(string name, decimal price, int stock)
    {
        // Business validation belongs in the service, not in the controller
        if (price <= 0) throw new ArgumentException("Price must be positive");

        var product = new Product { Name = name, Price = price, Stock = stock };
        await _repository.AddAsync(product);
        return product;
    }
}
