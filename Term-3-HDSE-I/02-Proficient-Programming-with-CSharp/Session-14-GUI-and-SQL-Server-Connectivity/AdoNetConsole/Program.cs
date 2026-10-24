// Session 14: CRUD with ADO.NET in a console app (runs on Windows, Linux and macOS)
using System.Data;
using Microsoft.Data.SqlClient;

// Step 1: the connection string tells .NET WHERE the database is.
// Change "Server=" to your own SQL Server name, e.g. "localhost\\SQLEXPRESS".
string connectionString =
    "Server=localhost;Database=AptechCollege;Trusted_Connection=True;TrustServerCertificate=True;";

// ---------- CREATE (INSERT) ----------
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();                                   // open the door to the database

    string sql = "INSERT INTO Students (FullName, City, Marks) VALUES (@name, @city, @marks)";
    using SqlCommand command = new SqlCommand(sql, connection);

    // Parameters keep us safe from SQL injection. Never join user text into SQL!
    command.Parameters.AddWithValue("@name", "Hira Noor");
    command.Parameters.AddWithValue("@city", "Karachi");
    command.Parameters.AddWithValue("@marks", 88);

    int rowsAdded = command.ExecuteNonQuery();           // used for INSERT/UPDATE/DELETE
    Console.WriteLine($"Inserted rows: {rowsAdded}");
}

// ---------- READ (SELECT with SqlDataReader) ----------
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();
    using SqlCommand command = new SqlCommand("SELECT StudentId, FullName, City, Marks FROM Students", connection);
    using SqlDataReader reader = command.ExecuteReader(); // reads row by row, forward only

    Console.WriteLine("\nAll students:");
    while (reader.Read())                                  // Read() moves to the next row
    {
        int id = reader.GetInt32(0);
        string name = reader.GetString(1);
        string city = reader.GetString(2);
        int marks = reader.GetInt32(3);
        Console.WriteLine($"{id,3}  {name,-12} {city,-8} {marks}");
    }
}

// ---------- UPDATE ----------
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();
    using SqlCommand command = new SqlCommand(
        "UPDATE Students SET Marks = @marks WHERE FullName = @name", connection);
    command.Parameters.AddWithValue("@marks", 95);
    command.Parameters.AddWithValue("@name", "Hira Noor");
    Console.WriteLine($"\nUpdated rows: {command.ExecuteNonQuery()}");
}

// ---------- READ with a STORED PROCEDURE and SqlDataAdapter ----------
using (SqlConnection connection = new SqlConnection(connectionString))
{
    using SqlCommand command = new SqlCommand("GetStudentsByCity", connection);
    command.CommandType = CommandType.StoredProcedure;    // tell ADO.NET it is a procedure
    command.Parameters.AddWithValue("@City", "Karachi");

    // The adapter opens/closes the connection by itself and fills a DataTable
    SqlDataAdapter adapter = new SqlDataAdapter(command);
    DataTable table = new DataTable();
    adapter.Fill(table);

    Console.WriteLine($"\nStudents in Karachi: {table.Rows.Count}");
    foreach (DataRow row in table.Rows)
        Console.WriteLine($" - {row["FullName"]} ({row["Marks"]})");
}

// ---------- DELETE ----------
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();
    using SqlCommand command = new SqlCommand("DELETE FROM Students WHERE FullName = @name", connection);
    command.Parameters.AddWithValue("@name", "Hira Noor");
    Console.WriteLine($"\nDeleted rows: {command.ExecuteNonQuery()}");
}

// ---------- COUNT (ExecuteScalar returns ONE value) ----------
using (SqlConnection connection = new SqlConnection(connectionString))
{
    connection.Open();
    using SqlCommand command = new SqlCommand("SELECT COUNT(*) FROM Students", connection);
    int total = (int)command.ExecuteScalar();
    Console.WriteLine($"Total students now: {total}");
}
