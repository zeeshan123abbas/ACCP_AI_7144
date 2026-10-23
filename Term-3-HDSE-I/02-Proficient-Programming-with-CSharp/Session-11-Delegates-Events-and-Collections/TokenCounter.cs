public class TokenIssuedEventArgs(int token, int waiting) : EventArgs
{
    public int Token { get; } = token;
    public int Waiting { get; } = waiting;
}

public class TokenCounter
{
    private readonly Queue<int> _queue = new();
    private int _next = 100;
    public event EventHandler<TokenIssuedEventArgs>? TokenIssued;
    public event Action<int>? TokenServed;

    public void Issue()
    {
        _queue.Enqueue(++_next);
        TokenIssued?.Invoke(this, new TokenIssuedEventArgs(_next, _queue.Count));
    }
    public void Serve()
    {
        if (_queue.TryDequeue(out int t)) TokenServed?.Invoke(t);
    }
}
