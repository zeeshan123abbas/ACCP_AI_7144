using Microsoft.AspNetCore.Mvc;
using OnionDemo.Domain;
using OnionDemo.Service;

namespace OnionDemo.WebApi.Controllers;

[ApiController]
[Route("api/products")]
public class ProductsController : ControllerBase
{
    private readonly ProductService _service;
    private readonly ILogger<ProductsController> _logger;

    public ProductsController(ProductService service, ILogger<ProductsController> logger)
    {
        _service = service;
        _logger = logger;
    }

    [HttpGet]
    public async Task<List<Product>> GetAll() => await _service.GetAllAsync();

    [HttpGet("{id:int}")]
    public async Task<ActionResult<Product>> GetById(int id)
    {
        var product = await _service.GetByIdAsync(id);
        if (product == null)
        {
            _logger.LogWarning("Product {ProductId} not found", id);   // structured log
            return NotFound();
        }
        return product;
    }

    public record CreateProductRequest(string Name, decimal Price, int Stock);

    [HttpPost]
    public async Task<ActionResult<Product>> Create(CreateProductRequest request)
    {
        var product = await _service.CreateAsync(request.Name, request.Price, request.Stock);
        _logger.LogInformation("Created product {ProductId}", product.Id);
        return CreatedAtAction(nameof(GetById), new { id = product.Id }, product);
    }
}
