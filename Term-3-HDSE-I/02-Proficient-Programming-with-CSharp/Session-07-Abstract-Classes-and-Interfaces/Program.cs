// Session 07: Working through abstract types and interfaces
List<Payment> payments =
[
    new CardPayment(12_500, "4421"),
    new CashPayment(3_200, 5_000),
    new WalletPayment(1_800, "03001234567")
];

foreach (Payment p in payments)
    Console.WriteLine(p.Process() ? p.Receipt() : $"#{p.Id} FAILED");

foreach (var p in payments)
{
    if (p is IRefundable r)
        Console.WriteLine($"#{p.Id} refund 1,000 allowed? {r.Refund(1_000)}");
}
