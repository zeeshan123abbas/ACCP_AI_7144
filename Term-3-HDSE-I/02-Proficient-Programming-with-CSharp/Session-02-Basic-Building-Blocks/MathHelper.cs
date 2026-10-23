/// <summary>Utility methods for marks.</summary>
public static class MathHelper
{
    /// <summary>Converts marks out of 100 to a 4.0 GPA scale.</summary>
    /// <param name="marks">Marks between 0 and 100.</param>
    /// <returns>GPA rounded to two decimals.</returns>
    public static double ToGpa(double marks) => Math.Round(marks / 100 * 4, 2);
}
