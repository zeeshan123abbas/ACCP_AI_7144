using OnionBasics.Domain.Entities;

namespace OnionBasics.Domain.Interfaces;

// CORE defines WHAT it needs. Outer layers decide HOW.
public interface IStudentRepository
{
    List<Student> GetAll();
    Student? GetById(int id);
    void Add(Student student);
}
