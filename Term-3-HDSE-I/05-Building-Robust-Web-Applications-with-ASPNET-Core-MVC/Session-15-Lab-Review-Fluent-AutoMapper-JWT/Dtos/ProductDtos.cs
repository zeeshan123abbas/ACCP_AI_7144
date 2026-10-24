using System.ComponentModel.DataAnnotations;

namespace ShopApi.Dtos;

public record ProductDto(int Id, string Name, string Sku, decimal Price);

public class SaveProductDto
{
    [Required, StringLength(100)]
    public string Name { get; set; } = "";

    [Required, StringLength(20)]
    public string Sku { get; set; } = "";

    [Range(1, 1_000_000)]
    public decimal Price { get; set; }

    [Range(0, 1_000_000)]
    public decimal CostPrice { get; set; }
}
