namespace UowDemo.Models;

public class Order
{
    public int Id { get; set; }
    public int CustomerId { get; set; }
    public decimal Amount { get; set; }
    public DateTime PlacedAt { get; set; } = DateTime.UtcNow;
}
