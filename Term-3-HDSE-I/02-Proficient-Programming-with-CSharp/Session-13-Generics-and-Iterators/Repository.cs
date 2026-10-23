public interface IEntity { int Id { get; } }

public class Repository<T> : IEnumerable<T> where T : class, IEntity
{
    private readonly Dictionary<int, T> _items = new();
    public void Add(T item)
    {
        if (!_items.TryAdd(item.Id, item))
            throw new InvalidOperationException($"{typeof(T).Name} {item.Id} already exists.");
    }
    public T? Find(int id) => _items.GetValueOrDefault(id);
    public IEnumerable<T> Where(Func<T, bool> predicate)
    {
        foreach (var item in _items.Values)
            if (predicate(item)) yield return item;
    }
    public IEnumerator<T> GetEnumerator() => _items.Values.GetEnumerator();
    System.Collections.IEnumerator System.Collections.IEnumerable.GetEnumerator() => GetEnumerator();
}

public record Course(int Id, string Title, int Hours) : IEntity;
public record Trainer(int Id, string Name) : IEntity;

public static class Util
{
    public static T Max<T>(T a, T b) where T : IComparable<T> => a.CompareTo(b) >= 0 ? a : b;

    public static IEnumerable<int> Evens(int limit)
    {
        for (int i = 0; ; i += 2)
        {
            if (i > limit) yield break;
            yield return i;
        }
    }
}
