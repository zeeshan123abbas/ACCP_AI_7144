using OnionBasics.Domain.Entities;
using OnionBasics.Domain.Interfaces;

namespace OnionBasics.Infrastructure;

// INFRASTRUCTURE layer: the real data access. Swap it later for EF Core.
public class InMemoryStudentRepository : IStudentRepository
{
    private readonly List<Student> _students = new()
    {
        new Student { Id = 1, Name = "Areeba", Marks = 78 },
        new Student { Id = 2, Name = "Usman", Marks = 42 },
        new Student { Id = 3, Name = "Hira", Marks = 91 }
    };

    public List<Student> GetAll() => _students;

    public Student? GetById(int id) => _students.FirstOrDefault(s => s.Id == id);

    public void Add(Student student)
    {
        student.Id = _students.Max(s => s.Id) + 1;
        _students.Add(student);
    }
}
