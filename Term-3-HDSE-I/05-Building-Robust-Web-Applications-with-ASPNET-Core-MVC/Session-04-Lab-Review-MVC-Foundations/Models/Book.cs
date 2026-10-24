using System.ComponentModel.DataAnnotations;

namespace LibraryLab.Models;

public class Book
{
    public int Id { get; set; }

    [Required, StringLength(100)]
    public string Title { get; set; } = "";

    [Required]
    public string Author { get; set; } = "";

    [Range(1900, 2100)]
    public int Year { get; set; } = DateTime.Now.Year;
}
