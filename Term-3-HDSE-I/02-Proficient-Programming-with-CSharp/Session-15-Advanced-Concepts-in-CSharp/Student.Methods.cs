// Session 15: Partial class - part 2 (behaviour)
public partial class Student
{
    public string Grade() => Marks >= 85 ? "A" : Marks >= 70 ? "B" : Marks >= 50 ? "C" : "F";
}
