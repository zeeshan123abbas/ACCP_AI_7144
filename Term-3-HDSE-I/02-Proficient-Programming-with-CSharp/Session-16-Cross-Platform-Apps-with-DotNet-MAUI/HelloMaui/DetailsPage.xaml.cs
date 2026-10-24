// Session 16: Receives the "name" value sent from MainPage
namespace HelloMaui;

[QueryProperty(nameof(StudentName), "name")]   // copies ?name=... into StudentName
public partial class DetailsPage : ContentPage
{
    public DetailsPage()
    {
        InitializeComponent();
    }

    private string studentName = "";

    public string StudentName
    {
        get => studentName;
        set
        {
            studentName = value;
            MessageLabel.Text = $"This page was opened by {value}.";
        }
    }

    private async void OnBackClicked(object? sender, EventArgs e)
    {
        await Shell.Current.GoToAsync("..");    // ".." means go back one page
    }
}
