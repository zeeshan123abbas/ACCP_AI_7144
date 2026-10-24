# Session 01: Dart Fundamentals and Null Safety

> Module: Dart Programming · Term 5 (ADSE) · ⏱ ~2 hours

Dart is the language behind Flutter, the toolkit used to build Android, iOS, web and desktop apps from one codebase.
In this session you install Dart, write your first program and learn the building blocks every Dart program uses: variables, types, decisions, loops, functions and **null safety**.

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain what Dart is, where it is used and why it is popular
- Install the Dart SDK and run a program from the terminal
- Declare variables with `var`, `final`, `const` and explicit types
- Control program flow with `if`, `switch` and loops
- Write functions with positional, optional and named parameters
- Use null safety operators (`?`, `??`, `?.`, `!`, `late`) correctly

## 📖 Concepts Explained

### 1. What is Dart?

Dart is an open-source, **type-safe**, object-oriented language created by Google. It is designed for building fast apps on any screen.

| Feature | What it means for you |
|---------|-----------------------|
| Type safe | Mistakes like putting text into a number variable are caught before the program runs |
| Sound null safety | A variable cannot be `null` unless you say so, which removes a very common crash |
| JIT + AOT compilation | Fast reloads while developing (JIT), fast native apps when released (AOT) |
| Compiles to JavaScript / WebAssembly | The same language runs in the browser |
| Familiar syntax | If you know Java, C# or JavaScript, Dart will feel natural |

> **Analogy:** think of Dart as the *engine* and Flutter as the *car body*. This module teaches the engine; the next module builds the car.

### 2. Installing Dart

1. Go to [dart.dev/get-dart](https://dart.dev/get-dart) and follow the steps for your OS (Windows users can use the ZIP or `choco install dart-sdk`). If you install Flutter later, Dart comes included.
2. Open a new terminal and check: `dart --version`
3. Install [VS Code](https://code.visualstudio.com/) and the official **Dart** extension.
4. Create a project with `dart create my_app`, then `cd my_app` and `dart run`. For single files in this session, simply use `dart run file_name.dart`.

```mermaid
flowchart LR
  A[Write .dart file] --> B[dart run]
  B --> C[Dart VM compiles JIT]
  C --> D[Output in terminal]
```

### 3. Variables and data types

| Type | Holds | Example |
|------|-------|---------|
| `int` | Whole numbers | `int age = 20;` |
| `double` | Decimal numbers | `double cgpa = 3.4;` |
| `String` | Text | `String city = 'Karachi';` |
| `bool` | true / false | `bool isPaid = true;` |
| `List`, `Set`, `Map` | Collections (Session 03) | `List<int> marks = [80, 75];` |

- `var` lets Dart **infer** the type from the first value. The type is then fixed.
- `final` = can be assigned **once** (value known at run time).
- `const` = fixed at **compile time** (e.g. `const pi = 3.14159;`).

### 4. Control flow and loops

- `if / else if / else` checks conditions top to bottom; the ternary `condition ? a : b` is a short version.
- `switch` compares one value to many cases. Dart 3 adds **switch expressions** that return a value.
- Loops: `for` (known count), `for-in` (each item of a list), `while` (unknown count), `do-while` (runs at least once). `break` exits a loop; `continue` skips to the next round.

### 5. Functions

A function is a named block of reusable code. Dart supports **positional** parameters, **optional positional** `[ ]`, and **named** parameters `{ }` (with `required` when they must be passed). One-line functions can use the arrow `=>`.

### 6. Null safety

`null` means "no value". In Dart, types are **non-nullable by default**.

| Syntax | Meaning |
|--------|---------|
| `String?` | This variable may be null |
| `a ?? b` | Use `a`, but if it is null use `b` |
| `a?.length` | Read `length` only if `a` is not null (otherwise gives null) |
| `a ??= b` | Assign `b` only if `a` is currently null |
| `a!` | "Trust me, it is not null" — crashes if you are wrong |
| `late` | I will assign it later, before first use |

## 💻 Code Examples

### Example 1: First program

📄 File: [`hello.dart`](./hello.dart)

```dart
// hello.dart
// Your first Dart program.
// Run it with:  dart run hello.dart

// Every Dart program starts from a function called main().
void main() {
  // print() writes a line of text to the console.
  print('Assalam-o-Alaikum! Welcome to Dart.');

  // A variable that stores the student's name.
  String studentName = 'Ayesha';

  // String interpolation: $variable puts the value inside the text.
  print('Hello, $studentName. Let us learn Dart together.');
}
```

**Run it:** `dart run hello.dart`

**How it works**

- `main()` is the entry point; Dart starts running here.
- `$studentName` inside single quotes inserts the variable's value (string interpolation).

### Example 2: Variables and types

📄 File: [`variables_and_types.dart`](./variables_and_types.dart)

```dart
// variables_and_types.dart
// Shows the basic data types and the different ways to declare variables.

void main() {
  // 1. Explicit types: we write the type ourselves.
  String city = 'Karachi';
  int age = 20;
  double cgpa = 3.45;
  bool isEnrolled = true;

  // 2. var: Dart works out (infers) the type from the value.
  var course = 'ACCP AI'; // Dart knows this is a String

  // 3. final: the value is set once and can never change.
  final String rollNumber = 'STU-1024';

  // 4. const: a value that is fixed when the program is compiled.
  const int maxSessions = 8;

  // Print everything using string interpolation.
  print('City: $city');
  print('Age: $age');
  print('CGPA: $cgpa');
  print('Enrolled: $isEnrolled');
  print('Course: $course');
  print('Roll number: $rollNumber');
  print('Sessions in module: $maxSessions');

  // Use ${ } when you need an expression inside the text.
  print('Next year you will be ${age + 1} years old.');

  // Type safety: Dart stops wrong types at compile time.
  // age = 'twenty';   // ERROR: A String can't be assigned to an int.

  // Changing a normal variable is fine.
  age = 21;
  print('Updated age: $age');

  // rollNumber = 'STU-2000';  // ERROR: final variables can't change.

  // Converting between types.
  String marksText = '85';
  int marks = int.parse(marksText); // String -> int
  String priceText = 249.5.toString(); // double -> String
  print('Marks as number + 5 = ${marks + 5}');
  print('Price as text: $priceText');
}
```

**How it works**

- Explicit types, `var`, `final` and `const` are shown side by side.
- The commented-out lines are errors Dart would catch **before** running — try uncommenting one.
- `int.parse()` and `toString()` convert between text and numbers.

### Example 3: Decisions

📄 File: [`control_flow.dart`](./control_flow.dart)

```dart
// control_flow.dart
// Making decisions with if / else if / else and switch.

void main() {
  int marks = 78;

  // if / else if / else: checks conditions from top to bottom.
  if (marks >= 80) {
    print('Grade: A');
  } else if (marks >= 70) {
    print('Grade: B');
  } else if (marks >= 60) {
    print('Grade: C');
  } else {
    print('Grade: F - please revise and try again.');
  }

  // The ternary operator is a short if/else that gives back a value.
  String result = marks >= 50 ? 'Pass' : 'Fail';
  print('Result: $result');

  // Logical operators: && (and), || (or), ! (not)
  bool hasFeePaid = true;
  bool hasAttendance = true;
  if (hasFeePaid && hasAttendance) {
    print('You can sit in the exam.');
  }

  // switch: compares one value with many cases.
  String day = 'Sat';
  switch (day) {
    case 'Sat':
    case 'Sun':
      print('$day: Weekend batch');
    case 'Mon':
      print('$day: Morning batch');
    default:
      print('$day: Regular class');
  }
  // Note: in Dart 3 you do not need "break" at the end of a case.

  // Dart 3 switch expression: returns a value directly.
  int dayNumber = 3;
  String dayName = switch (dayNumber) {
    1 => 'Monday',
    2 => 'Tuesday',
    3 => 'Wednesday',
    _ => 'Some other day', // _ means "anything else"
  };
  print('Day $dayNumber is $dayName');
}
```

**How it works**

- The grade ladder checks the highest band first.
- In Dart 3 a `case` does not fall through, so `break` is not needed. `_` in a switch expression means "anything else".

### Example 4: Loops

📄 File: [`loops.dart`](./loops.dart)

```dart
// loops.dart
// Repeating work with for, for-in, while and do-while.

void main() {
  // 1. Classic for loop: start; condition; step.
  print('Counting 1 to 5:');
  for (int i = 1; i <= 5; i++) {
    print('  $i');
  }

  // 2. for-in loop: visit every item of a list.
  List<String> subjects = ['Dart', 'Flutter', 'Python'];
  print('Subjects this term:');
  for (String subject in subjects) {
    print('  - $subject');
  }

  // 3. while loop: repeats as long as the condition is true.
  int balance = 1000;
  int month = 0;
  while (balance > 0) {
    balance = balance - 300; // spend 300 each month
    month++;
  }
  print('Money finished after $month months.');

  // 4. do-while loop: runs the body at least once.
  int tries = 0;
  do {
    tries++;
    print('Attempt number $tries');
  } while (tries < 3);

  // 5. break and continue
  for (int n = 1; n <= 10; n++) {
    if (n % 2 == 0) {
      continue; // skip even numbers
    }
    if (n > 7) {
      break; // stop the loop completely
    }
    print('Odd number: $n');
  }

  // 6. A multiplication table using a loop.
  int table = 7;
  for (int i = 1; i <= 10; i++) {
    print('$table x $i = ${table * i}');
  }
}
```

**How it works**

- Each loop type solves a different problem; the `while` loop stops when the balance runs out.
- `%` gives the remainder, so `n % 2 == 0` means "n is even".

### Example 5: Functions

📄 File: [`functions.dart`](./functions.dart)

```dart
// functions.dart
// Writing reusable functions with different kinds of parameters.

// A simple function that returns a value.
int add(int a, int b) {
  return a + b;
}

// Arrow syntax: a short way to write a one-line function.
int square(int n) => n * n;

// Optional positional parameter in [ ] with a default value.
String greet(String name, [String title = 'Student']) {
  return 'Hello $title $name';
}

// Named parameters in { }. "required" means the caller must pass it.
double calculateFee({required double monthlyFee, int months = 1}) {
  return monthlyFee * months;
}

// A function that returns nothing uses void.
void printLine() {
  print('-' * 30);
}

void main() {
  print('2 + 3 = ${add(2, 3)}');
  print('Square of 9 = ${square(9)}');
  printLine();

  print(greet('Bilal'));          // uses the default title
  print(greet('Sana', 'Miss'));   // passes a title
  printLine();

  // Named arguments can be written in any order.
  double fee = calculateFee(months: 3, monthlyFee: 4500);
  print('Fee for 3 months: Rs. $fee');
  printLine();

  // Functions are values too: we can store one in a variable.
  int Function(int) myFunction = square;
  print('Using a stored function: ${myFunction(4)}');

  // Anonymous function (no name) passed to forEach.
  List<int> numbers = [1, 2, 3];
  numbers.forEach((number) {
    print('Number x 10 = ${number * 10}');
  });
}
```

**How it works**

- `greet` has an optional title with a default; `calculateFee` uses named parameters, so calls read clearly.
- Functions can be stored in variables and passed to other functions such as `forEach`.

### Example 6: Null safety

📄 File: [`null_safety.dart`](./null_safety.dart)

```dart
// null_safety.dart
// Sound null safety: a variable cannot hold null unless you allow it.

void main() {
  // 1. Non-nullable: must always have a value.
  String name = 'Hamza';
  // name = null;   // ERROR: null can't be assigned to a String.

  // 2. Nullable: add ? after the type to allow null.
  String? middleName = findMiddleName('Hamza'); // may be null
  print('Middle name: $middleName');

  // 3. ?? (if-null operator): use a backup value when it is null.
  String displayName = middleName ?? 'No middle name';
  print(displayName);

  // 4. ?. (null-aware access): only call when not null.
  print('Length of middle name: ${middleName?.length}'); // prints null

  // 5. ??= : give a value only if the variable is null right now.
  middleName ??= 'Ali';
  print('Middle name now: $middleName');

  // 6. Checking for null first. After the check Dart "promotes" the type.
  String? phone = findPhone('Hamza');
  if (phone != null) {
    // Here Dart knows phone is a String, not String?.
    print('$name\'s phone has ${phone.length} digits.');
  } else {
    print('No phone found for $name.');
  }

  // 7. ! (null assertion): "I promise this is not null".
  // Use it rarely. If you are wrong, the program crashes.
  String confirmedPhone = findPhone('Hamza')!; // we know Hamza exists
  print('Confirmed phone: $confirmedPhone');

  // 8. late: the value will be set later, before it is used.
  late String welcomeMessage;
  welcomeMessage = 'Welcome to the Dart module!';
  print(welcomeMessage);
}

// A function that may return null (notice the String? return type).
String? findPhone(String person) {
  if (person == 'Hamza') {
    return '03001234567';
  }
  return null;
}

// Hamza has no middle name on record, so this returns null.
String? findMiddleName(String person) {
  return null;
}
```

**How it works**

- `findPhone` returns `String?`, so the caller **must** handle the null case.
- After `if (phone != null)`, Dart *promotes* `phone` to a normal `String` — no `!` needed.

## 🧪 Lab Practice

1. Install the Dart SDK and VS Code extension. Run `dart --version` and take a screenshot.
2. Run every example above, then change values (name, marks, day) and predict the output before running.
3. Write `bmi.dart`: store weight (kg) and height (m) in `double` variables, calculate BMI and print *Underweight / Normal / Overweight* using `if`.
4. Write a function `isEven(int n)` using arrow syntax and print even numbers from 1 to 20 with a loop.
5. Make a `String? nickname` variable and print it three ways: with `??`, with `?.length`, and after an `if` null check.

## 📝 Assignment

Create `fee_calculator.dart` with a function `double totalFee({required double monthlyFee, required int months, double? discountPercent})`.
If `discountPercent` is null, apply no discount. Print the fee for 3, 6 and 12 months, and give an automatic extra 5% off when months is 12 (use `if`).

## ❓ Quick Quiz

1. What is the difference between `final` and `const`?
2. Which loop always runs its body at least once?
3. What does `name ?? 'Guest'` return when `name` is null?
4. How do you mark a named parameter as compulsory?
5. Why should you avoid using `!` too often?

<details>
<summary>Show answers</summary>

1. `final` is set once at run time; `const` must be known at compile time.
2. `do-while`.
3. `'Guest'`.
4. With the `required` keyword, e.g. `{required int months}`.
5. If the value is actually null, `!` throws an error and the app crashes. Prefer `??`, `?.` or a null check.

</details>

## 💼 Interview Questions

1. **What is sound null safety in Dart?** — Types are non-nullable by default and the compiler guarantees a non-nullable variable never holds null, so null errors are caught at compile time.
2. **What is the difference between JIT and AOT compilation?** — JIT compiles while the app runs (fast development and hot reload); AOT compiles to machine code before release (fast start-up and performance).
3. **Positional vs named parameters?** — Positional arguments are matched by order; named arguments are matched by name, can be in any order and are optional unless marked `required`.

## ✅ Summary

- Dart is a type-safe, null-safe language used by Flutter for mobile, web and desktop.
- Use `var` for inference, `final` for one-time values and `const` for compile-time constants.
- `if`, `switch`, and loops control the flow of a program.
- Functions support optional and named parameters and can be passed around like values.
- `?`, `??`, `?.`, `??=`, `!` and `late` are the null-safety toolkit.

---

⬅ Previous · [🏠 Module Home](../README.md) · [Next ➡](../Session-02-Object-Oriented-Programming-in-Dart/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
