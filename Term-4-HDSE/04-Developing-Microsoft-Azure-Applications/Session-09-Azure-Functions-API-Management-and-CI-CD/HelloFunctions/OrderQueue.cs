// Session 09 - OrderQueue.cs: event-driven code (runs when a queue message arrives)
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

public class OrderQueue
{
    private readonly ILogger<OrderQueue> _logger;

    public OrderQueue(ILogger<OrderQueue> logger)
    {
        _logger = logger;
    }

    // Triggered automatically for every new message in the "orders" queue
    [Function("ProcessOrder")]
    public void Run([QueueTrigger("orders", Connection = "AzureWebJobsStorage")] string message)
    {
        // A real app might send an email, update a database or call an AI service here
        _logger.LogInformation("New order received: {Message}", message);
    }
}
