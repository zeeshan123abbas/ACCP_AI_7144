// Session 05: Using the BankAccount class
var a1 = new BankAccount("Hina", 10_000);
var a2 = new BankAccount("Omar");
a2.Deposit(2000, 3500, 500);

if (a1.Withdraw(15_000, out decimal left))
    Console.WriteLine("Withdrawn");
else
    Console.WriteLine($"Insufficient funds. Balance stays {left:N0}");

Console.WriteLine(a1.Statement());
Console.WriteLine(a2.Statement(showNumber: false));
Console.WriteLine($"Accounts opened: {BankAccount.TotalAccounts}");

int bonus = 100;
AddBonus(ref bonus);
Console.WriteLine($"Bonus after ref call: {bonus}");

static void AddBonus(ref int value) => value += 50;
