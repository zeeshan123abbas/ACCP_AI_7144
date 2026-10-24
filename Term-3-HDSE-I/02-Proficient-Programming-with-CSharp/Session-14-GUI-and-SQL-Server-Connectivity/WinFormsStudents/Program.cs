// Session 14: Entry point of the Windows Forms app (Windows only)
namespace WinFormsStudents;

internal static class Program
{
    [STAThread]                              // WinForms needs a single-threaded apartment
    static void Main()
    {
        ApplicationConfiguration.Initialize(); // high-DPI, default font, visual styles
        Application.Run(new StudentForm());    // show our form and wait until it closes
    }
}
