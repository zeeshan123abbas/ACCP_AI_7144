using System.Diagnostics;
using Microsoft.AspNetCore.Mvc.Filters;

namespace AuthFilters.Filters;

// A custom action filter: measures how long an action takes
public class LogTimeAttribute : ActionFilterAttribute
{
    // Runs BEFORE the action
    public override void OnActionExecuting(ActionExecutingContext context)
    {
        context.HttpContext.Items["watch"] = Stopwatch.StartNew();
    }

    // Runs AFTER the action
    public override void OnActionExecuted(ActionExecutedContext context)
    {
        var watch = (Stopwatch)context.HttpContext.Items["watch"]!;
        string action = context.ActionDescriptor.DisplayName ?? "action";
        Console.WriteLine($"{action} took {watch.ElapsedMilliseconds} ms");
    }
}
