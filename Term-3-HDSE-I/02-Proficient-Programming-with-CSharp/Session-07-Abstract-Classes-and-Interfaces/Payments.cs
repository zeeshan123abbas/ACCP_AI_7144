// Session 07: Abstract classes and interfaces
public interface IRefundable
{
    bool Refund(decimal amount);
}

public interface ILogger
{
    void Log(string message) => Console.WriteLine($"[LOG {DateTime.Now:HH:mm:ss}] {message}");
}

public abstract class Payment
{
    private static int _counter;
    public int Id { get; } = ++_counter;
    public decimal Amount { get; }

    protected Payment(decimal amount)
    {
        if (amount <= 0) throw new ArgumentOutOfRangeException(nameof(amount));
        Amount = amount;
    }

    public abstract bool Process();
    public virtual string Receipt() => $"#{Id} {GetType().Name} Rs {Amount:N0}";
}

public class CardPayment : Payment, IRefundable, ILogger
{
    public string CardLast4 { get; }
    public CardPayment(decimal amount, string last4) : base(amount) => CardLast4 = last4;

    public override bool Process()
    {
        ((ILogger)this).Log($"Charging card ****{CardLast4}");
        return true;
    }

    public bool Refund(decimal amount) => amount <= Amount;
    public override string Receipt() => base.Receipt() + $" (card ****{CardLast4})";
}

public class CashPayment : Payment
{
    public decimal Tendered { get; }
    public CashPayment(decimal amount, decimal tendered) : base(amount) => Tendered = tendered;

    public override bool Process() => Tendered >= Amount;
    public override string Receipt() => base.Receipt() + $" change Rs {Tendered - Amount:N0}";
}

public class WalletPayment(decimal amount, string mobile) : Payment(amount), IRefundable
{
    public override bool Process() => mobile.StartsWith("03") && mobile.Length == 11;
    bool IRefundable.Refund(decimal amt) => amt <= Amount;
}
