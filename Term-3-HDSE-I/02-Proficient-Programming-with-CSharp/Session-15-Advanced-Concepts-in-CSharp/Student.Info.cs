// Session 15: Partial class - part 1 (data)
// The compiler joins all "partial" pieces into ONE Student class.
public partial class Student
{
    public string Name { get; set; } = "";
    public int Marks { get; set; }
    public string? Email { get; set; }      // "?" means Email is allowed to be null
}
