namespace ShopApi.Models;

public class Product
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public string Sku { get; set; } = "";        // stock keeping unit, must be unique
    public decimal Price { get; set; }
    public decimal CostPrice { get; set; }       // secret: never send to clients
    public DateTime CreatedAt { get; set; }
}
