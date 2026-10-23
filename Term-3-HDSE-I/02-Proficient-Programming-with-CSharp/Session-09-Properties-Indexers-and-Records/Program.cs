// Session 09: Properties, indexers and records
var p = new Product { Name = "Keyboard", Sku = "KB-01", Price = 3500 };
p.Receive(12);
Console.WriteLine($"{p.Name} stock {p.Stock}, value Rs {p.StockValue:N0}");

var g = new Gradebook();
g["SQL"] = 88; g["C#"] = 140;
Console.WriteLine($"SQL {g["SQL"]}, C# {g["C#"]}, Math {g["Math"]}");

var s1 = new Student("R-1", "Ali", 3.4);
var s2 = s1 with { Cgpa = 3.6 };
Console.WriteLine(s1);
Console.WriteLine($"Equal? {s1 == new Student("R-1", "Ali", 3.4)}");
var (roll, name, _) = s2;
Console.WriteLine($"{roll} {name} improved to {s2.Cgpa}");
