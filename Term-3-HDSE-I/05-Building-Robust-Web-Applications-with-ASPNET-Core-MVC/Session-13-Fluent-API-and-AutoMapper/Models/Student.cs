namespace FluentMapper.Models;

// Notice: NO data annotations here. All rules are in the Fluent API.
public class Student
{
    public int Id { get; set; }
    public string FullName { get; set; } = "";
    public string Email { get; set; } = "";
    public string? InternalNotes { get; set; }   // must never go to the client

    public int CourseId { get; set; }             // foreign key
    public Course? Course { get; set; }           // navigation property
}
