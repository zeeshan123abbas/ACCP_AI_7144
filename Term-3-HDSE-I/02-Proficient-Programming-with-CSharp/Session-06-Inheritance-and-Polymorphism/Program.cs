// Session 06: Run-time polymorphism in a payroll
var staff = new List<Employee>
{
    new Employee("Asad", 80_000),
    new Manager("Nadia", 150_000, 40_000),
    new SalesPerson("Faraz", 60_000) { Sales = 900_000 },
    new Intern("Mahnoor")
};

decimal payroll = 0;
foreach (Employee e in staff)
{
    Console.WriteLine(e);
    payroll += e.MonthlyPay();
}
Console.WriteLine($"Total payroll: Rs {payroll:N0}");

foreach (var e in staff)
{
    if (e is Manager m)
        Console.WriteLine($"{m.Name} gets allowance Rs {m.Allowance:N0}");
}

Intern i = new Intern("Mahnoor");
Employee asBase = i;
Console.WriteLine(i.ToString());
Console.WriteLine(asBase.ToString());
