using AutoMapper;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ShopApi.Data;
using ShopApi.Dtos;
using ShopApi.Models;

namespace ShopApi.Controllers;

[ApiController]
[Route("api/products")]
public class ProductsController : ControllerBase
{
    private readonly ShopContext _db;
    private readonly IMapper _mapper;

    public ProductsController(ShopContext db, IMapper mapper)
    {
        _db = db;
        _mapper = mapper;
    }

    // Anyone can browse products
    [HttpGet]
    public async Task<List<ProductDto>> GetAll()
    {
        var products = await _db.Products.AsNoTracking().ToListAsync();
        return _mapper.Map<List<ProductDto>>(products);
    }

    // Only Admins can add products
    [HttpPost]
    [Authorize(Roles = "Admin")]
    public async Task<ActionResult<ProductDto>> Create(SaveProductDto dto)
    {
        bool skuTaken = await _db.Products.AnyAsync(p => p.Sku == dto.Sku);
        if (skuTaken) return Conflict($"SKU {dto.Sku} already exists");   // 409

        var product = _mapper.Map<Product>(dto);
        _db.Products.Add(product);
        await _db.SaveChangesAsync();
        return Created($"/api/products/{product.Id}", _mapper.Map<ProductDto>(product));
    }

    // Only Admins can delete
    [HttpDelete("{id:int}")]
    [Authorize(Roles = "Admin")]
    public async Task<IActionResult> Delete(int id)
    {
        var product = await _db.Products.FindAsync(id);
        if (product == null) return NotFound();
        _db.Products.Remove(product);
        await _db.SaveChangesAsync();
        return NoContent();
    }
}
