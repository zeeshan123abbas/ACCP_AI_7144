// Session 05: Classes, methods, overloading and constructors
public class BankAccount
{
    private static int _nextNumber = 1001;
    public static int TotalAccounts { get; private set; }

    private readonly string _accountNo;
    private decimal _balance;
    public string Holder { get; }

    static BankAccount() => Console.WriteLine("[Bank system loaded]");

    public BankAccount(string holder, decimal opening)
    {
        Holder = holder;
        _accountNo = $"PK-{_nextNumber++}";
        _balance = opening;
        TotalAccounts++;
    }

    public BankAccount(string holder) : this(holder, 0m) { }

    public void Deposit(decimal amount)
    {
        if (amount <= 0) throw new ArgumentException("Amount must be positive.");
        _balance += amount;
    }

    public bool Withdraw(decimal amount, out decimal remaining)
    {
        if (amount > _balance) { remaining = _balance; return false; }
        _balance -= amount;
        remaining = _balance;
        return true;
    }

    public void Deposit(params decimal[] amounts)
    {
        foreach (var a in amounts) Deposit(a);
    }

    public string Statement(bool showNumber = true) =>
        showNumber ? $"{_accountNo} | {Holder,-10} | Rs {_balance:N0}" : $"{Holder}: Rs {_balance:N0}";

    ~BankAccount() { /* finalizer: rarely needed; runs during garbage collection */ }
}
