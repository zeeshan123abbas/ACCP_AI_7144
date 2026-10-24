// Session 14: A simple form that adds students to SQL Server and shows them in a grid.
// Controls are created in code (no designer file) so you can read everything in one place.
using System.Data;
using Microsoft.Data.SqlClient;

namespace WinFormsStudents;

public class StudentForm : Form
{
    // Change the server name to match your PC (e.g. localhost\SQLEXPRESS)
    private const string ConnectionString =
        "Server=localhost;Database=AptechCollege;Trusted_Connection=True;TrustServerCertificate=True;";

    // Step 1: declare the controls we need
    private readonly Label lblName = new() { Text = "Name", Left = 20, Top = 20, Width = 60 };
    private readonly TextBox txtName = new() { Left = 90, Top = 18, Width = 180 };
    private readonly Label lblCity = new() { Text = "City", Left = 20, Top = 55, Width = 60 };
    private readonly TextBox txtCity = new() { Left = 90, Top = 53, Width = 180 };
    private readonly Label lblMarks = new() { Text = "Marks", Left = 20, Top = 90, Width = 60 };
    private readonly TextBox txtMarks = new() { Left = 90, Top = 88, Width = 80 };
    private readonly Button btnSave = new() { Text = "Save", Left = 90, Top = 125, Width = 80 };
    private readonly Button btnRefresh = new() { Text = "Refresh", Left = 190, Top = 125, Width = 80 };
    private readonly DataGridView grid = new() { Left = 20, Top = 170, Width = 440, Height = 200, ReadOnly = true };

    public StudentForm()
    {
        // Step 2: set up the window
        Text = "Students - Aptech College";
        Width = 500;
        Height = 430;

        // Step 3: put the controls on the form
        Controls.AddRange(new Control[] { lblName, txtName, lblCity, txtCity, lblMarks, txtMarks, btnSave, btnRefresh, grid });

        // Step 4: connect events to methods (event handlers)
        Load += (sender, e) => LoadStudents();          // when the form first opens
        btnRefresh.Click += (sender, e) => LoadStudents();
        btnSave.Click += BtnSave_Click;
    }

    private void BtnSave_Click(object? sender, EventArgs e)
    {
        // Step 5: validate input before touching the database
        if (string.IsNullOrWhiteSpace(txtName.Text) || string.IsNullOrWhiteSpace(txtCity.Text))
        {
            MessageBox.Show("Name and City are required.", "Validation");
            return;
        }
        if (!int.TryParse(txtMarks.Text, out int marks) || marks < 0 || marks > 100)
        {
            MessageBox.Show("Marks must be a number from 0 to 100.", "Validation");
            return;
        }

        try
        {
            // Step 6: INSERT with parameters
            using var connection = new SqlConnection(ConnectionString);
            connection.Open();
            using var command = new SqlCommand(
                "INSERT INTO Students (FullName, City, Marks) VALUES (@name, @city, @marks)", connection);
            command.Parameters.AddWithValue("@name", txtName.Text.Trim());
            command.Parameters.AddWithValue("@city", txtCity.Text.Trim());
            command.Parameters.AddWithValue("@marks", marks);
            command.ExecuteNonQuery();

            MessageBox.Show("Student saved!", "Success");
            txtName.Clear(); txtCity.Clear(); txtMarks.Clear();
            LoadStudents();
        }
        catch (SqlException ex)
        {
            MessageBox.Show("Database error: " + ex.Message, "Error");
        }
    }

    private void LoadStudents()
    {
        try
        {
            // Step 7: SELECT into a DataTable and bind it to the grid
            using var adapter = new SqlDataAdapter("SELECT * FROM Students ORDER BY StudentId", ConnectionString);
            var table = new DataTable();
            adapter.Fill(table);
            grid.DataSource = table;   // the grid draws one row per DataRow
        }
        catch (SqlException ex)
        {
            MessageBox.Show("Could not load students: " + ex.Message, "Error");
        }
    }
}
