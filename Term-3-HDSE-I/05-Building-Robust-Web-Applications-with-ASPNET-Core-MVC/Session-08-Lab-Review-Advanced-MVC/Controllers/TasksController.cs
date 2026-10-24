using Microsoft.AspNetCore.Mvc;
using TaskBoard.Data;

namespace TaskBoard.Controllers;

public class TasksController : Controller
{
    // GET /Tasks
    public IActionResult Index()
    {
        ViewData["Title"] = "Task Board";
        return View(TaskStore.Tasks);
    }

    // POST /Tasks/Complete/2
    [HttpPost, ValidateAntiForgeryToken]
    public IActionResult Complete(int id)
    {
        var task = TaskStore.Tasks.FirstOrDefault(t => t.Id == id);
        if (task == null)
        {
            throw new InvalidOperationException($"Task {id} not found");  // handled by our filter
        }
        task.IsDone = true;
        TempData["Message"] = $"'{task.Title}' marked as done.";
        return RedirectToAction(nameof(Index));
    }
}
