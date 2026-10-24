# Session 13: Fluent API and AutoMapper

> Module: Building Robust Web Applications with ASP.NET Core MVC · Term 3 (HDSE I) · ⏱ ~2 hours

## 🎯 Learning Objectives

- Explain the **Fluent API** and how it differs from data annotations
- Configure keys, lengths, indexes, relationships and seed data in `OnModelCreating`
- Perform full CRUD with EF Core in an ASP.NET Core controller
- Explain what **AutoMapper** is and why DTOs are used
- Install, configure and use AutoMapper profiles

## 📖 Concepts Explained

### 1. Two Ways to Configure EF Core

| | Data annotations | Fluent API |
|---|---|---|
| Where | Attributes on the class (`[Required]`) | Code in `OnModelCreating` |
| Power | Common rules only | **Everything**: composite keys, indexes, precision, relationships, seed data |
| Keeps entity clean? | No, mixed with database details | Yes, entity stays a plain class (great for Onion's Domain) |
| Priority | Lower | **Wins** if both are used |

"Fluent" means calls are **chained** like a sentence: `entity.Property(s => s.FullName).IsRequired().HasMaxLength(80);`

### 2. Common Fluent API Calls

| Goal | Code |
|---|---|
| Table name | `entity.ToTable("tblStudents")` |
| Primary key / composite key | `HasKey(s => s.Id)` / `HasKey(e => new { e.StudentId, e.CourseId })` |
| Required + max length | `Property(s => s.Email).IsRequired().HasMaxLength(120)` |
| Unique index | `HasIndex(s => s.Email).IsUnique()` |
| Money precision | `Property(c => c.Fee).HasPrecision(10, 2)` |
| One-to-many | `HasOne(s => s.Course).WithMany(c => c.Students).HasForeignKey(s => s.CourseId)` |
| Ignore a property | `Ignore(s => s.TempValue)` |
| Seed rows | `HasData(new Course { Id = 1, ... })` |

For big models, move each entity's rules into its own class implementing `IEntityTypeConfiguration<T>` and call `modelBuilder.ApplyConfigurationsFromAssembly(...)`.

### 3. Why DTOs?

A **DTO (Data Transfer Object)** is a class shaped for the API, not for the database.

- Hides private fields (`InternalNotes`) and avoids sending huge object graphs
- Prevents **over-posting** (a client setting fields it should not)
- Lets the API shape change without changing the database

### 4. AutoMapper

Copying properties by hand (`dto.Name = student.FullName; dto.Email = ...`) is boring and error-prone. **AutoMapper** copies matching properties automatically.

```mermaid
flowchart LR
    E[Student entity<br/>FullName, Email, InternalNotes, Course.Title] -- IMapper.Map --> D[StudentDto<br/>Name, Email, CourseTitle]
    S[SaveStudentDto] -- IMapper.Map --> E
```

| Feature | Meaning |
|---|---|
| Same names | Copied automatically |
| Flattening | `Course.Title` → `CourseTitle` automatically |
| `ForMember(...MapFrom...)` | Custom rule for different names |
| `Profile` | A class that groups mapping rules |
| `Map(source, destination)` | Copies onto an existing object (great for updates) |

Setup: `dotnet add package AutoMapper --version 13.0.1`, then `builder.Services.AddAutoMapper(typeof(Program));`. We pin 13.0.1 for this course; newer major versions changed their licence terms, so check the official site before using them in commercial work.

## 💻 Code Examples

Folder files: `FluentMapper.csproj`, `Program.cs`, `Models/Student.cs`, `Models/Course.cs`, `Data/SchoolContext.cs`, `Dtos/StudentDtos.cs`, `Mapping/SchoolProfile.cs`, `Controllers/StudentsController.cs`, `requests.http`.

### Example 1: Fluent configuration (`Data/SchoolContext.cs`, excerpt)

```csharp
modelBuilder.Entity<Student>(entity =>
{
    entity.ToTable("tblStudents");
    entity.Property(s => s.FullName).IsRequired().HasMaxLength(80);
    entity.HasIndex(s => s.Email).IsUnique();
    entity.HasOne(s => s.Course).WithMany(c => c.Students).HasForeignKey(s => s.CourseId);
});
```

**How it works**: The `Student` class has no attributes; all database rules live here. Open `fluent.db` in a SQLite viewer and you will see the `tblStudents` table, the unique index and two seeded courses.

### Example 2: DTOs and a profile (`Mapping/SchoolProfile.cs`)

```csharp
using AutoMapper;
using FluentMapper.Dtos;
using FluentMapper.Models;

namespace FluentMapper.Mapping;

// A Profile groups related mapping rules
public class SchoolProfile : Profile
{
    public SchoolProfile()
    {
        // Entity -> DTO
        CreateMap<Student, StudentDto>()
            .ForMember(dest => dest.Name, opt => opt.MapFrom(src => src.FullName));
        // CourseTitle is filled automatically from Course.Title ("flattening")

        // DTO -> Entity
        CreateMap<SaveStudentDto, Student>();
    }
}
```

**How it works**: `Name` needs a custom rule because the names differ. `CourseTitle` is flattened automatically. `InternalNotes` has no matching DTO property, so it is never sent.

### Example 3: CRUD with AutoMapper (`Controllers/StudentsController.cs`, excerpt)

```csharp
var students = await _db.Students.Include(s => s.Course).ToListAsync();
return _mapper.Map<List<StudentDto>>(students);           // READ

var student = _mapper.Map<Student>(dto);                   // CREATE
_db.Students.Add(student);

_mapper.Map(dto, student);                                 // UPDATE existing entity
await _db.SaveChangesAsync();
```

**How it works**: `Include` loads the course so `CourseTitle` can be filled. For updates, mapping onto the tracked entity lets EF Core detect exactly which columns changed. The full file also has GET by id and DELETE.

## 🧪 Lab Practice

1. Run the app and execute the requests in `requests.http` in order.
2. POST the same email twice and observe the unique index error. Then catch `DbUpdateException` and return `Conflict()`.
3. Move the `Student` rules into `StudentConfiguration : IEntityTypeConfiguration<Student>`.
4. Add `CourseDto` (Id, Title, Fee, StudentCount) and map `StudentCount` from `Students.Count`.
5. Add `[Required]` and `[EmailAddress]` to `SaveStudentDto` and test invalid input.

## 📝 Assignment

Add a many-to-many `Subject` entity (a student takes many subjects) configured fully with the Fluent API, plus DTOs and an endpoint `GET /api/students/{id}/subjects` using AutoMapper.

## ❓ Quick Quiz

1. Which method do you override to use the Fluent API?
2. If an annotation and the Fluent API disagree, which wins?
3. What is flattening in AutoMapper?
4. Give two reasons to return DTOs instead of entities.
5. Which call copies a DTO onto an existing entity?

<details>
<summary>Show answers</summary>

1. `OnModelCreating(ModelBuilder modelBuilder)`
2. The Fluent API
3. Mapping nested properties like `Course.Title` to a flat property `CourseTitle` by naming convention.
4. Hide sensitive fields; prevent over-posting; decouple API shape from the database.
5. `_mapper.Map(dto, entity)`

</details>

## 💼 Interview Questions

1. **When would you choose the Fluent API?** When you need advanced configuration or want entity classes free of database attributes.
2. **What is over-posting and how do DTOs stop it?** A client sends extra fields (e.g. `IsAdmin`); binding to a DTO that lacks them ignores them.
3. **Any downside to AutoMapper?** Hidden mapping logic can surprise you; validate configuration with `AssertConfigurationIsValid()` in tests.

## ✅ Summary

- The Fluent API configures EF Core fully in code and keeps entities clean.
- Keys, indexes, precision, relationships and seed data all live in `OnModelCreating`.
- DTOs protect and shape API data.
- AutoMapper profiles remove repetitive mapping code for reads, creates and updates.

---

[⬅ Previous](../Session-12-Lab-Review-Architecture/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-14-Token-Authentication-with-JWT/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
