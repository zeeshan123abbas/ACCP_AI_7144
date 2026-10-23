public class Product
{
    private decimal _price;
    public required string Name { get; init; }
    public string Sku { get; init; } = "N/A";
    public int Stock { get; private set; }
    public decimal Price
    {
        get => _price;
        set => _price = value >= 0 ? value : throw new ArgumentOutOfRangeException(nameof(Price));
    }
    public decimal StockValue => Price * Stock;
    public void Receive(int qty) => Stock += qty;
}
