using Microsoft.AspNetCore.Mvc;
using Modern.Models;

namespace Modern.Controllers;

[ApiController]
[Route("binding")]
public class BindingController : ControllerBase
{
    // /binding/route/5
    [HttpGet("route/{id}")]
    public string FromRouteDemo([FromRoute] int id) => $"id from route = {id}";

    // /binding/query?city=Karachi
    [HttpGet("query")]
    public string FromQueryDemo([FromQuery] string city) => $"city from query = {city}";

    // header "X-Batch: 2401"
    [HttpGet("header")]
    public string FromHeaderDemo([FromHeader(Name = "X-Batch")] string batch) => $"batch from header = {batch}";

    // POST JSON body: {"id":1,"fullName":"Ali","joinDate":"2026-01-10"}
    [HttpPost("body")]
    public Student FromBodyDemo([FromBody] Student student) => student;
}
