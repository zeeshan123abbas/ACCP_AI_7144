using AutoMapper;
using FluentMapper.Data;
using FluentMapper.Dtos;
using FluentMapper.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace FluentMapper.Controllers;

[ApiController]
[Route("api/students")]
public class StudentsController : ControllerBase
{
    private readonly SchoolContext _db;
    private readonly IMapper _mapper;

    public StudentsController(SchoolContext db, IMapper mapper)
    {
        _db = db;
        _mapper = mapper;
    }

    // READ all
    [HttpGet]
    public async Task<List<StudentDto>> GetAll()
    {
        var students = await _db.Students.Include(s => s.Course).ToListAsync();
        return _mapper.Map<List<StudentDto>>(students);
    }

    // READ one
    [HttpGet("{id:int}")]
    public async Task<ActionResult<StudentDto>> GetById(int id)
    {
        var student = await _db.Students.Include(s => s.Course).FirstOrDefaultAsync(s => s.Id == id);
        if (student == null) return NotFound();
        return _mapper.Map<StudentDto>(student);
    }

    // CREATE
    [HttpPost]
    public async Task<ActionResult<StudentDto>> Create(SaveStudentDto dto)
    {
        var student = _mapper.Map<Student>(dto);   // DTO -> entity
        _db.Students.Add(student);
        await _db.SaveChangesAsync();
        return CreatedAtAction(nameof(GetById), new { id = student.Id }, null);
    }

    // UPDATE
    [HttpPut("{id:int}")]
    public async Task<IActionResult> Update(int id, SaveStudentDto dto)
    {
        var student = await _db.Students.FindAsync(id);
        if (student == null) return NotFound();

        _mapper.Map(dto, student);                 // copy DTO values onto the existing entity
        await _db.SaveChangesAsync();
        return NoContent();
    }

    // DELETE
    [HttpDelete("{id:int}")]
    public async Task<IActionResult> Delete(int id)
    {
        var student = await _db.Students.FindAsync(id);
        if (student == null) return NotFound();

        _db.Students.Remove(student);
        await _db.SaveChangesAsync();
        return NoContent();
    }
}
