using ActionsApi.Models;

namespace ActionsApi.Data;

// A simple in-memory "database" so we can focus on actions
public static class ProductStore
{
    public static List<Product> Products { get; } = new()
    {
        new Product { Id = 1, Name = "Keyboard", Price = 2500 },
        new Product { Id = 2, Name = "Mouse", Price = 1200 },
        new Product { Id = 3, Name = "USB Cable", Price = 400 }
    };
}
