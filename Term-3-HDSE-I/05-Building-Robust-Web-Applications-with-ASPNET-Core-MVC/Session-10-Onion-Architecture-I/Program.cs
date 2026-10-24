using OnionBasics.Application;
using OnionBasics.Domain.Interfaces;
using OnionBasics.Infrastructure;

var builder = WebApplication.CreateBuilder(args);

// PRESENTATION layer wires everything together (the "composition root")
builder.Services.AddSingleton<IStudentRepository, InMemoryStudentRepository>();
builder.Services.AddScoped<StudentService>();

var app = builder.Build();

app.MapGet("/students/passed", (StudentService service) => service.GetPassedStudents());

app.MapPost("/students", (StudentService service, string name, int marks) =>
{
    var student = service.Register(name, marks);
    return Results.Created($"/students/{student.Id}", student);
});

app.Run();
