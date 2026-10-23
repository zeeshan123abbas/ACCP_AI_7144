// Session 06: Inheritance, overriding, sealed
public class Employee
{
    public string Name { get; }
    public decimal BaseSalary { get; }

    public Employee(string name, decimal baseSalary)
    {
        Name = name;
        BaseSalary = baseSalary;
    }

    public virtual decimal MonthlyPay() => BaseSalary;

    public override string ToString() => $"{GetType().Name,-12} {Name,-10} Rs {MonthlyPay(),10:N0}";
}

public class Manager : Employee
{
    public decimal Allowance { get; }
    public Manager(string name, decimal baseSalary, decimal allowance)
        : base(name, baseSalary) => Allowance = allowance;

    public override decimal MonthlyPay() => base.MonthlyPay() + Allowance;
}

public class SalesPerson : Employee
{
    public decimal Sales { get; set; }
    public SalesPerson(string name, decimal baseSalary) : base(name, baseSalary) { }

    public sealed override decimal MonthlyPay() => BaseSalary + Sales * 0.05m;
}

public sealed class Intern : Employee
{
    public Intern(string name) : base(name, 25_000) { }
    public new string ToString() => $"Intern {Name}";
}
