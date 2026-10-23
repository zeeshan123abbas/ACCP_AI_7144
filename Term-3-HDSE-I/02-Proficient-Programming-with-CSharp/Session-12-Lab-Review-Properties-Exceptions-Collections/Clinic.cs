public record Patient(string Mrn, string Name, int Age);

public class InvalidPatientException(string message) : Exception(message);

public class Clinic
{
    private readonly Queue<Patient> _waiting = new();
    private readonly Dictionary<string, List<DateTime>> _history = new();
    public event Action<Patient, decimal>? AppointmentCompleted;
    public int Waiting => _waiting.Count;
    public IReadOnlyList<DateTime> this[string mrn] =>
        _history.TryGetValue(mrn, out var v) ? v : [];

    public void CheckIn(Patient p)
    {
        if (p.Age is < 0 or > 120) throw new InvalidPatientException($"Invalid age {p.Age} for {p.Name}.");
        if (_waiting.Any(w => w.Mrn == p.Mrn)) throw new InvalidPatientException($"{p.Name} already waiting.");
        _waiting.Enqueue(p);
    }

    public void ServeNext(Func<Patient, decimal> feeRule)
    {
        if (!_waiting.TryDequeue(out var p)) throw new InvalidOperationException("No patients waiting.");
        if (!_history.ContainsKey(p.Mrn)) _history[p.Mrn] = new List<DateTime>();
        _history[p.Mrn].Add(DateTime.Now);
        AppointmentCompleted?.Invoke(p, feeRule(p));
    }
}
