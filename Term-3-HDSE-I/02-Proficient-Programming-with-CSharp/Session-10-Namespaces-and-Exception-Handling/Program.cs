// Session 10: Namespaces and exception handling
using Aptech.Fees.Models;
using Aptech.Fees.Services;

var service = new FeeService();
string[] inputs = ["5000", "abc", "-10", "50000", "8000"];

foreach (string input in inputs)
{
    try
    {
        try
        {
            decimal left = service.Pay(input);
            Console.WriteLine($"Paid {input}. Wallet: {left:N0}");
        }
        catch (FormatException ex)
        {
            throw new InvalidOperationException($"'{input}' is not a number.", ex);
        }
    }
    catch (InsufficientBalanceException ex) when (ex.Shortfall > 10_000)
    {
        Console.WriteLine($"Big shortfall: {ex.Message}");
    }
    catch (ArgumentOutOfRangeException)
    {
        Console.WriteLine($"Amount {input} must be positive.");
    }
    catch (InvalidOperationException ex)
    {
        Console.WriteLine($"{ex.Message} (inner: {ex.InnerException?.GetType().Name})");
    }
    finally
    {
        Console.WriteLine("-- attempt logged --");
    }
}
