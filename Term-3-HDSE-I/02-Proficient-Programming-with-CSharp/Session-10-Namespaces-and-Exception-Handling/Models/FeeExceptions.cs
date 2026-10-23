namespace Aptech.Fees.Models;

public class InsufficientBalanceException : Exception
{
    public decimal Shortfall { get; }
    public InsufficientBalanceException(decimal shortfall)
        : base($"Balance is short by Rs {shortfall:N0}.") => Shortfall = shortfall;
    public InsufficientBalanceException(string message, Exception inner) : base(message, inner) { }
}
