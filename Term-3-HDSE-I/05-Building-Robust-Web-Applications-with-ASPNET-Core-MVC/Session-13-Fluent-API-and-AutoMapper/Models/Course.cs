namespace FluentMapper.Models;

public class Course
{
    public int Id { get; set; }
    public string Title { get; set; } = "";
    public decimal Fee { get; set; }

    public List<Student> Students { get; set; } = new();   // one course, many students
}
