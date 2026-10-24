using ShopApi.Services;
using Microsoft.AspNetCore.Mvc;

namespace ShopApi.Controllers;

[ApiController]
[Route("api/auth")]
public class AuthController : ControllerBase
{
    private readonly TokenService _tokens;

    public AuthController(TokenService tokens)
    {
        _tokens = tokens;
    }

    public record LoginRequest(string UserName, string Password);

    // POST api/auth/login  -> returns a JWT
    [HttpPost("login")]
    public IActionResult Login(LoginRequest request)
    {
        // DEMO users only. Real apps check a hashed password in a database (see Session 17).
        string? role = (request.UserName, request.Password) switch
        {
            ("admin", "Admin@123") => "Admin",
            ("student", "Student@123") => "Student",
            _ => null
        };

        if (role == null) return Unauthorized();   // 401

        string token = _tokens.CreateToken(request.UserName, role);
        return Ok(new { token, expiresInMinutes = 30 });
    }
}
