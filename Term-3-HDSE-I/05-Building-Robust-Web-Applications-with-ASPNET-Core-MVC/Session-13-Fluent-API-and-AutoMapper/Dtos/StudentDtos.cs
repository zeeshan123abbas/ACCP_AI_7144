namespace FluentMapper.Dtos;

// What we SEND to the client (no InternalNotes!)
public class StudentDto
{
    public int Id { get; set; }
    public string Name { get; set; } = "";         // comes from FullName
    public string Email { get; set; } = "";
    public string CourseTitle { get; set; } = "";  // flattened from Course.Title
}

// What we RECEIVE from the client
public class SaveStudentDto
{
    public string FullName { get; set; } = "";
    public string Email { get; set; } = "";
    public int CourseId { get; set; }
}
