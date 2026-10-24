// Session 18: Lab - the enrollment desk (events + exceptions + LINQ)
public class EnrollmentDesk
{
    private readonly Store<Enrollment> enrollments = new();

    // Event raised after every successful enrollment (Session 11)
    public event Action<Enrollment>? StudentEnrolled;

    public void Enroll(string studentName, Course course)
    {
        // Rule 1: name is required
        if (string.IsNullOrWhiteSpace(studentName))
            throw new ArgumentException("Student name is required.");

        // Rule 2: the course must have a free seat
        int taken = enrollments.Find(e => e.Course.Id == course.Id).Count();
        if (taken >= course.Seats)
            throw new CourseFullException(course.Title);

        var enrollment = new Enrollment(studentName, course, DateTime.Now);
        enrollments.Add(enrollment);
        StudentEnrolled?.Invoke(enrollment);   // tell everyone who is listening
    }

    public IReadOnlyList<Enrollment> All => enrollments.All;

    // Simulates saving to a server / database without freezing (async, Session 15)
    public async Task<int> SaveAsync()
    {
        await Task.Delay(500);
        return enrollments.All.Count;
    }
}
