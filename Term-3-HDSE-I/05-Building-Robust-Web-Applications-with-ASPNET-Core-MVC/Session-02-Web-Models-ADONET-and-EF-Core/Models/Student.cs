namespace SchoolData.Models;

// A model is a plain C# class. EF Core turns it into a table.
public class Student
{
    public int Id { get; set; }               // primary key (by convention)
    public string Name { get; set; } = "";
    public int Age { get; set; }
}
