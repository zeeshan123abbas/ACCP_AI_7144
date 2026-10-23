// Session 11: Delegates, events and collections
Func<decimal, decimal> gst = a => a * 0.18m;
Action<string> log = m => Console.WriteLine($"[log] {m}");
log += m => File.AppendAllText("log.txt", m + Environment.NewLine);
log($"GST on 2,000 = {gst(2000)}");

var counter = new TokenCounter();
counter.TokenIssued += (s, e) => Console.WriteLine($"Token {e.Token} issued, {e.Waiting} waiting");
counter.TokenServed += t => Console.WriteLine($"Now serving {t}");
counter.Issue(); counter.Issue(); counter.Issue();
counter.Serve();

var marks = new List<int> { 72, 91, 55, 38, 84 };
marks.Sort();
Predicate<int> failed = m => m < 50;
Console.WriteLine($"Sorted: {string.Join(",", marks)} | failed: {marks.FindAll(failed).Count}");

var phoneBook = new Dictionary<string, string> { ["Ali"] = "0300-1112223", ["Sana"] = "0321-4445556" };
phoneBook.TryAdd("Ali", "dup");
if (phoneBook.TryGetValue("Sana", out var num)) Console.WriteLine($"Sana: {num}");

var undo = new Stack<string>();
undo.Push("type A"); undo.Push("type B");
Console.WriteLine($"Undo: {undo.Pop()}");

var sqlBatch = new HashSet<string> { "Ali", "Sana", "Hira" };
var csBatch  = new HashSet<string> { "Sana", "Omar" };
sqlBatch.IntersectWith(csBatch);
Console.WriteLine($"In both batches: {string.Join(",", sqlBatch)}");
