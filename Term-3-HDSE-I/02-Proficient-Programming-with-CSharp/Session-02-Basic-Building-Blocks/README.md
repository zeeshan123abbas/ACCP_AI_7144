# Session 02: Basic Building Blocks in C#

> Module: Proficient Programming with C# · Term 3 (HDSE I) · ⏱ ~2 hours

## 🎯 Learning Objectives

- Declare variables and constants using the correct data types
- Tell the difference between value types and reference types
- Use arithmetic, comparison, logical and conditional operators
- Convert between types safely with `TryParse` and casting
- Format console output and write XML documentation comments

## 📖 Concepts Explained

### 1. Variables and constants

A **variable** is a named box in memory that holds a value which can change. A **constant** (`const`) is a box whose value is fixed at compile time.

```csharp
int age = 20;              // can change later
const double Pi = 3.14159; // can never change
var city = "Karachi";      // var: compiler works out the type (string)
```

Naming rules: start with a letter or `_`, no spaces, case-sensitive (`Age` ≠ `age`). Use **camelCase** for variables and **PascalCase** for constants, methods and classes.

### 2. Common data types

| Type | Example | Size / notes |
|---|---|---|
| `int` | `25` | 32-bit whole number |
| `long` | `9_000_000_000L` | 64-bit whole number |
| `double` | `3.75` | decimal point, fast, small rounding errors |
| `decimal` | `8500.50m` | exact — use for **money** |
| `bool` | `true` / `false` | yes/no |
| `char` | `'A'` | one character |
| `string` | `"Hello"` | text (reference type) |

### 3. Value types vs reference types

| Value type (`int`, `double`, `bool`, `struct`) | Reference type (`string`, arrays, classes) |
|---|---|
| Stores the actual value | Stores an address pointing to the object |
| Copying makes an independent copy | Copying shares the same object |
| Lives on the stack (usually) | Object lives on the managed heap |

### 4. Operators

| Kind | Operators | Example |
|---|---|---|
| Arithmetic | `+ - * / %` | `7 % 2` → `1` |
| Assignment | `= += -= *=` | `total += 500;` |
| Comparison | `== != > < >= <=` | `marks >= 50` |
| Logical | `&& \|\| !` | `age > 18 && hasCnic` |
| Conditional | `? :` | `marks >= 50 ? "Pass" : "Fail"` |
| Null-coalescing | `??` | `input ?? "Unknown"` |

> **Watch out:** `7 / 2` is `3` (integer division). Use `7 / 2.0` to get `3.5`.

### 5. Type conversion

- **Implicit** (safe, automatic): `int` → `long` → `double`.
- **Explicit cast** (may lose data): `int n = (int)9.8;` gives `9`.
- **Parsing text**: `int.Parse("12")` throws an error on bad input; `int.TryParse(text, out int n)` returns `false` instead — always prefer `TryParse` for user input.

### 6. Special strings and comments

- Verbatim string `@"C:\Folder\file.txt"` — backslashes are not escapes.
- Raw string `"""{ "a": 1 }"""` — quotes inside without escaping (C# 11).
- `//` single-line, `/* */` multi-line, `///` XML documentation shown by IntelliSense.

## 💻 Code Examples

File: `Program.cs`

```csharp
// Session 02: Variables, constants, operators and console I/O
const string Institute = "Aptech North Nazimabad";
const string Welcome = $"Fee calculator - {Institute}";

Console.WriteLine(Welcome);
Console.WriteLine(new string('-', Welcome.Length));

Console.Write("Student name: ");
string name = Console.ReadLine() ?? "Unknown";

Console.Write("Monthly fee (Rs): ");
if (!decimal.TryParse(Console.ReadLine(), out decimal monthlyFee))
{
    Console.WriteLine("Invalid amount, using Rs 8,500.");
    monthlyFee = 8500m;
}

const int Months = 6;
const decimal DiscountRate = 0.10m;
decimal total = monthlyFee * Months;
bool getsDiscount = total >= 50_000m && name.Length > 0;
decimal discount = getsDiscount ? total * DiscountRate : 0;

Console.WriteLine($"\nStudent\t: {name}");
Console.WriteLine($"Total\t: {total,12:N2}");
Console.WriteLine($"Discount\t: {discount,12:N2}");
Console.WriteLine($"Payable\t: {total - discount,12:N2}");
Console.WriteLine($"7 / 2 = {7 / 2}, 7 / 2.0 = {7 / 2.0}, 7 % 2 = {7 % 2}");

string path = @"C:\Students\Report.txt";
string json = """{ "course": "C#", "level": 3 }""";
Console.WriteLine($"Saved to {path}\nJSON: {json}");
Console.WriteLine($"GPA for 86 marks: {MathHelper.ToGpa(86)}");
```

**How it works**

1. `const` values are fixed; even an interpolated string can be `const` if it uses only constants.
2. `decimal.TryParse` checks the typed amount; on failure we fall back to Rs 8,500.
3. The `m` suffix (`8500m`) marks a `decimal` literal; `_` in `50_000m` is just for readability.
4. `getsDiscount ? total * DiscountRate : 0` chooses a value with the conditional operator.
5. `{total,12:N2}` right-aligns in 12 characters with thousand separators and 2 decimals.
6. The last lines show integer vs decimal division, a verbatim path and a raw JSON string.

File: `MathHelper.cs` — a static helper with XML documentation:

```csharp
/// <summary>Utility methods for marks.</summary>
public static class MathHelper
{
    /// <summary>Converts marks out of 100 to a 4.0 GPA scale.</summary>
    /// <param name="marks">Marks between 0 and 100.</param>
    /// <returns>GPA rounded to two decimals.</returns>
    public static double ToGpa(double marks) => Math.Round(marks / 100 * 4, 2);
}
```

**How it works:** `static` means you call it on the class (`MathHelper.ToGpa(86)`) without creating an object. The `///` comments appear as tooltips in Visual Studio.

## 🧪 Lab Practice

1. Run the program and enter a valid fee, then an invalid fee like `abc`. Compare the output.
2. Change `Months` to 12 and see when the discount applies.
3. Print the `MaxValue` of `int`, `long` and `decimal`.
4. Write `int x = 10; int y = x; y = 20;` and print both — then try the same with two arrays.
5. Add a `bool isHosteller` question and add Rs 5,000 per month if true.

## 📝 Assignment

Create **TemperatureConverter**: read a temperature in Celsius with `double.TryParse`, print Fahrenheit (`C * 9 / 5 + 32`) and Kelvin, formatted to 1 decimal place, and print "Hot" if above 35 using the conditional operator.

## ❓ Quick Quiz

1. Which type should you use for money?
2. What is the result of `17 % 5`?
3. What is the difference between `Parse` and `TryParse`?
4. Is `string` a value type or a reference type?
5. What does `??` do?

<details>
<summary>Show answers</summary>

1. `decimal`
2. `2`
3. `Parse` throws an exception on bad input; `TryParse` returns `false`.
4. Reference type.
5. Returns the right-hand value when the left side is `null`.

</details>

## 💼 Interview Questions

1. Explain value types vs reference types with an example.
2. When would you choose `double` over `decimal`?
3. What is the difference between `const` and `readonly`?

## ✅ Summary

- Pick the right type: `int` for counts, `decimal` for money, `bool` for flags.
- Value types copy data; reference types copy the address.
- Use `TryParse` for any text typed by a user.
- Interpolated strings with format specifiers make output clean.

---

[⬅ Previous](../Session-01-Getting-Started-with-CSharp-and-DotNet/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-03-Programming-Constructs-and-Arrays/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
