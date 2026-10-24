using TaskBoard.Models;

namespace TaskBoard.Data;

public static class TaskStore
{
    public static List<TaskItem> Tasks { get; } = new()
    {
        new TaskItem { Id = 1, Title = "Revise action results" },
        new TaskItem { Id = 2, Title = "Practice partial views" },
        new TaskItem { Id = 3, Title = "Write a custom filter", IsDone = true }
    };
}
