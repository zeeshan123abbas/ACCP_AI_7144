// Session 16: Code-behind for MainPage.xaml (event handlers live here)
namespace HelloMaui;

public partial class MainPage : ContentPage
{
    private int clickCount = 0;

    public MainPage()
    {
        InitializeComponent();   // builds the controls written in the XAML file

        // Device feature (basic): read information about the phone/PC we are running on
        DeviceLabel.Text = $"Running on {DeviceInfo.Current.Platform} " +
                           $"({DeviceInfo.Current.Idiom}), version {DeviceInfo.Current.VersionString}";
    }

    private void OnGreetClicked(object? sender, EventArgs e)
    {
        clickCount++;

        // Read the text the user typed in the Entry control
        string name = string.IsNullOrWhiteSpace(NameEntry.Text) ? "Student" : NameEntry.Text.Trim();

        ResultLabel.Text = $"Assalam-o-Alaikum, {name}! (clicked {clickCount} times)";
    }

    private async void OnDetailsClicked(object? sender, EventArgs e)
    {
        // Navigate to the page we registered as "details" and pass the name along
        string name = NameEntry.Text ?? "Student";
        await Shell.Current.GoToAsync($"details?name={Uri.EscapeDataString(name)}");
    }
}
