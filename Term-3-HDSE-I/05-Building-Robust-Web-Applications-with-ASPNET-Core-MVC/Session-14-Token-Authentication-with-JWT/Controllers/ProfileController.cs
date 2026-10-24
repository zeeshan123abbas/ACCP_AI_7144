using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace JwtDemo.Controllers;

[ApiController]
[Route("api/profile")]
[Authorize]                       // every action needs a valid token
public class ProfileController : ControllerBase
{
    // GET api/profile
    [HttpGet]
    public IActionResult Me()
    {
        var claims = User.Claims.Select(c => new { c.Type, c.Value });
        return Ok(new { name = User.Identity!.Name, claims });
    }

    // GET api/profile/admin  -> only the Admin role
    [HttpGet("admin")]
    [Authorize(Roles = "Admin")]
    public IActionResult AdminOnly() => Ok("Secret admin report");

    // GET api/profile/public -> no token needed
    [HttpGet("public")]
    [AllowAnonymous]
    public IActionResult Public() => Ok("Anyone can see this");
}
