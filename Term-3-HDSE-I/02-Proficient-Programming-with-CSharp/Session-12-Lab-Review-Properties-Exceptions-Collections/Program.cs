// Session 12: Lab and Review - clinic appointment desk
var clinic = new Clinic();
decimal revenue = 0;
clinic.AppointmentCompleted += (p, fee) => { revenue += fee; Console.WriteLine($"Billing: {p.Name} pays Rs {fee:N0}"); };
clinic.AppointmentCompleted += (p, _) => Console.WriteLine($"SMS: Thank you {p.Name}, get well soon.");

Patient[] arrivals =
[
    new("MRN-1", "Kashif", 34),
    new("MRN-2", "Rubina", 67),
    new("MRN-3", "Baby Ayan", -2),
    new("MRN-1", "Kashif", 34)
];

foreach (var p in arrivals)
{
    try { clinic.CheckIn(p); Console.WriteLine($"Checked in {p.Name}"); }
    catch (InvalidPatientException ex) { Console.WriteLine($"Rejected: {ex.Message}"); }
}

Func<Patient, decimal> feeRule = p => p.Age >= 60 ? 1500 * 0.5m : 1500;
while (clinic.Waiting > 0) clinic.ServeNext(feeRule);

try { clinic.ServeNext(feeRule); }
catch (InvalidOperationException ex) { Console.WriteLine($"Desk: {ex.Message}"); }

Console.WriteLine($"Revenue today: Rs {revenue:N0}");
Console.WriteLine($"Kashif visits: {clinic["MRN-1"].Count}");
