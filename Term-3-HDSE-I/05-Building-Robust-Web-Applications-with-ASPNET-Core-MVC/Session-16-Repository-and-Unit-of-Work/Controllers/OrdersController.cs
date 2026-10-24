using Microsoft.AspNetCore.Mvc;
using UowDemo.Models;
using UowDemo.Persistence;

namespace UowDemo.Controllers;

[ApiController]
[Route("api/orders")]
public class OrdersController : ControllerBase
{
    private readonly IUnitOfWork _uow;

    public OrdersController(IUnitOfWork uow)
    {
        _uow = uow;
    }

    public record PlaceOrderRequest(int CustomerId, decimal Amount);

    // POST api/orders  -> two changes, ONE save
    [HttpPost]
    public async Task<IActionResult> Place(PlaceOrderRequest request)
    {
        var customer = await _uow.Customers.GetByIdAsync(request.CustomerId);
        if (customer == null) return NotFound("Customer not found");

        // Change 1: add the order
        await _uow.Orders.AddAsync(new Order { CustomerId = customer.Id, Amount = request.Amount });

        // Change 2: update the customer's total
        customer.TotalSpent += request.Amount;

        // Save both together: either both succeed or neither does
        await _uow.CompleteAsync();

        return Ok(new { customer.Name, customer.TotalSpent });
    }

    [HttpGet]
    public async Task<List<Order>> GetAll() => await _uow.Orders.GetAllAsync();
}
