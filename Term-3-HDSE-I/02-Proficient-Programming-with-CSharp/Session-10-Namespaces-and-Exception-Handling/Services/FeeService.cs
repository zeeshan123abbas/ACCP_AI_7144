namespace Aptech.Fees.Services;
using Aptech.Fees.Models;

public class FeeService
{
    private decimal _wallet = 20_000;
    public decimal Pay(string amountText)
    {
        decimal amount = decimal.Parse(amountText);
        ArgumentOutOfRangeException.ThrowIfNegativeOrZero(amount);
        if (amount > _wallet) throw new InsufficientBalanceException(amount - _wallet);
        _wallet -= amount;
        return _wallet;
    }
}
