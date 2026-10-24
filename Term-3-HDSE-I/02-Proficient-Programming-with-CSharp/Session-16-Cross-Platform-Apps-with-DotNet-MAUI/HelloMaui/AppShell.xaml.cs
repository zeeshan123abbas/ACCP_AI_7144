// Session 16: Register extra pages so we can navigate to them by name
namespace HelloMaui;

public partial class AppShell : Shell
{
    public AppShell()
    {
        InitializeComponent();

        // "details" is the route name we will use in GoToAsync
        Routing.RegisterRoute("details", typeof(DetailsPage));
    }
}
