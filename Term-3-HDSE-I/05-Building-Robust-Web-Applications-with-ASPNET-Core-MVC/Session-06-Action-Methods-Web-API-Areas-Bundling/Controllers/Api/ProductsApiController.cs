using ActionsApi.Data;
using ActionsApi.Models;
using Microsoft.AspNetCore.Mvc;

namespace ActionsApi.Controllers.Api;

// [ApiController] = automatic 400 for bad input + binding from JSON body
[ApiController]
[Route("api/products")]
public class ProductsApiController : ControllerBase
{
    // GET api/products
    [HttpGet]
    public ActionResult<List<Product>> GetAll()
    {
        return ProductStore.Products;
    }

    // GET api/products/2
    [HttpGet("{id:int}")]
    public ActionResult<Product> GetById(int id)
    {
        var product = ProductStore.Products.FirstOrDefault(p => p.Id == id);
        if (product == null) return NotFound();
        return product;
    }

    // POST api/products   body: { "name": "Monitor", "price": 30000 }
    [HttpPost]
    public ActionResult<Product> Create(Product product)
    {
        product.Id = ProductStore.Products.Max(p => p.Id) + 1;
        ProductStore.Products.Add(product);
        return CreatedAtAction(nameof(GetById), new { id = product.Id }, product);
    }
}
