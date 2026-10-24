// Lab 10 - Task 2: runs for every message that SubmitFeedback put in the queue
using Microsoft.Azure.Functions.Worker;
using Microsoft.Extensions.Logging;

public class ProcessFeedback
{
    private readonly ILogger<ProcessFeedback> _logger;

    public ProcessFeedback(ILogger<ProcessFeedback> logger)
    {
        _logger = logger;
    }

    [Function("ProcessFeedback")]
    public void Run([QueueTrigger("feedback", Connection = "AzureWebJobsStorage")] string feedback)
    {
        // Step 1: a very simple "analysis" - count words
        int wordCount = feedback.Split(' ', StringSplitOptions.RemoveEmptyEntries).Length;

        // Step 2: log the result (visible in Application Insights on Azure)
        _logger.LogInformation("Feedback with {Words} words: {Text}", wordCount, feedback);
    }
}
