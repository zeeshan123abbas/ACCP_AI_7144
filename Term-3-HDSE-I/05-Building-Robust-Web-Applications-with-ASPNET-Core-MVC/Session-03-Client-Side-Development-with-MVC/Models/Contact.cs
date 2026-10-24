using System.ComponentModel.DataAnnotations;

namespace ClientSide.Models;

// Data annotations = validation rules written on the model
public class Contact
{
    [Required(ErrorMessage = "Please enter your name")]
    [StringLength(50)]
    public string Name { get; set; } = "";

    [Required, EmailAddress]
    public string Email { get; set; } = "";

    [Range(16, 60, ErrorMessage = "Age must be between 16 and 60")]
    public int Age { get; set; }

    [Display(Name = "Your message")]
    [Required, MinLength(10)]
    public string Message { get; set; } = "";
}
