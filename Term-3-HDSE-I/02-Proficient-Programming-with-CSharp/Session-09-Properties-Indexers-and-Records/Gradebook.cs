public class Gradebook
{
    private readonly Dictionary<string, int> _marks = new();
    public int this[string subject]
    {
        get => _marks.TryGetValue(subject, out int m) ? m : 0;
        set => _marks[subject] = Math.Clamp(value, 0, 100);
    }
    public int Count => _marks.Count;
}
