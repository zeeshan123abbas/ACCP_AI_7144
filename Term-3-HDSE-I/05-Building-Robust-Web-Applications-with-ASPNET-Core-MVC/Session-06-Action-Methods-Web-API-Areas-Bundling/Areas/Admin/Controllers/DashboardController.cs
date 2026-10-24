using Microsoft.AspNetCore.Mvc;

namespace ActionsApi.Areas.Admin.Controllers;

// This controller belongs to the "Admin" area: URL /Admin/Dashboard
[Area("Admin")]
public class DashboardController : Controller
{
    public IActionResult Index()
    {
        return Content("Admin area dashboard");
    }
}
