using OnionBasics.Domain.Entities;
using OnionBasics.Domain.Interfaces;

namespace OnionBasics.Application;

// APPLICATION layer: use cases. Depends only on the Domain interface.
public class StudentService
{
    private readonly IStudentRepository _repository;

    public StudentService(IStudentRepository repository)
    {
        _repository = repository;    // we do not know (or care) which database it is
    }

    public List<Student> GetPassedStudents()
    {
        return _repository.GetAll().Where(s => s.HasPassed()).ToList();
    }

    public Student Register(string name, int marks)
    {
        if (string.IsNullOrWhiteSpace(name))
            throw new ArgumentException("Name is required");

        var student = new Student { Name = name, Marks = marks };
        _repository.Add(student);
        return student;
    }
}
