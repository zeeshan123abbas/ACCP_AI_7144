// Session 09 - HelloHttp.cs: a serverless API endpoint (HTTP trigger)
using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

public class HelloHttp
{
    private readonly ILogger<HelloHttp> _logger;

    public HelloHttp(ILogger<HelloHttp> logger)
    {
        _logger = logger;
    }

    // GET /api/Hello?name=Ali
    [Function("Hello")]
    public async Task<HttpResponseData> Run(
        [HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequestData request)
    {
        // Step 1: read the name from the query string (default: "student")
        string name = request.Query["name"] ?? "student";
        _logger.LogInformation("Hello function called for {Name}", name);

        // Step 2: build a 200 OK response with plain text
        HttpResponseData response = request.CreateResponse(HttpStatusCode.OK);
        await response.WriteStringAsync($"Hello, {name}! This answer came from Azure Functions.");
        return response;
    }
}
