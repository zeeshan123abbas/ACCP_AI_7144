using System.ComponentModel.DataAnnotations;

namespace IdentitySession.Models;

// Used by both the Register and Login forms
public class AccountModel
{
    [Required, EmailAddress]
    public string Email { get; set; } = "";

    [Required, DataType(DataType.Password)]
    public string Password { get; set; } = "";
}
