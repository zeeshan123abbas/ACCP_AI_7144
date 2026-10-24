namespace OnionBasics.Domain.Entities;

// CORE: a business entity. No EF, no ASP.NET, no database code here.
public class Student
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public int Marks { get; set; }

    // Business rule lives with the entity
    public bool HasPassed() => Marks >= 50;
}
