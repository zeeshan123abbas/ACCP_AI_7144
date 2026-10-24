// Lab 10 - Task 1: HTTP POST that saves feedback into a queue
using System.Net;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;

// A function can return TWO things: a queue message AND an HTTP response
public class FeedbackOutput
{
    [QueueOutput("feedback", Connection = "AzureWebJobsStorage")]
    public string? QueueMessage { get; set; }     // null = nothing is written

    public HttpResponseData? HttpResponse { get; set; }
}

public class SubmitFeedback
{
    // POST /api/feedback   body: any text or JSON
    [Function("SubmitFeedback")]
    public async Task<FeedbackOutput> Run(
        [HttpTrigger(AuthorizationLevel.Function, "post", Route = "feedback")] HttpRequestData request)
    {
        // Step 1: read the request body as text
        string body = await new StreamReader(request.Body).ReadToEndAsync();

        // Step 2: reject empty feedback with 400
        if (string.IsNullOrWhiteSpace(body))
        {
            var bad = request.CreateResponse(HttpStatusCode.BadRequest);
            await bad.WriteStringAsync("Feedback cannot be empty");
            return new FeedbackOutput { HttpResponse = bad };
        }

        // Step 3: accept it - send to the queue and reply 202 Accepted
        var ok = request.CreateResponse(HttpStatusCode.Accepted);
        await ok.WriteStringAsync("Thank you! Your feedback was received.");
        return new FeedbackOutput { QueueMessage = body, HttpResponse = ok };
    }
}
