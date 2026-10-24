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
