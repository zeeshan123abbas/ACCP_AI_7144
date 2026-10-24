using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace TaskBoard.Filters;

// Exception filter: catches errors thrown inside controller actions
public class FriendlyErrorFilter : IExceptionFilter
{
    public void OnException(ExceptionContext context)
    {
        Console.WriteLine($"Error: {context.Exception.Message}");   // log it
        context.Result = new ContentResult
        {
            Content = "Oops! That task could not be processed.",
            StatusCode = 500
        };
        context.ExceptionHandled = true;   // stop the error from going further
    }
}
