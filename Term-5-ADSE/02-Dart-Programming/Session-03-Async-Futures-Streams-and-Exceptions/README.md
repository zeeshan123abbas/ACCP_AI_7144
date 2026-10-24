# Session 03: Collections, Async Programming, Streams and Exceptions

> Module: Dart Programming · Term 5 (ADSE) · ⏱ ~2 hours

Real apps load data from the internet, read files and react to user events — all things that take time. In this session you learn Dart's collections and generics, then how Dart waits for slow work **without freezing** using Futures and Streams, and how to handle errors gracefully.

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Use `List`, `Set` and `Map` and their common methods (`where`, `map`, `reduce`)
- Write generic classes and functions with `<T>`
- Explain synchronous vs asynchronous code and the event loop
- Use `Future`, `async` and `await` to handle one delayed result
- Create and listen to `Stream`s for many values over time
- Handle errors with `try`, `catch`, `on`, `finally` and custom exceptions

## 📖 Concepts Explained

### 1. Collections

| Collection | Ordered? | Duplicates? | Access by | Example use |
|------------|----------|-------------|-----------|-------------|
| `List<T>` | Yes | Yes | Index `[0]` | Students in a class |
| `Set<T>` | No guaranteed index | No | Value | Unique skills |
| `Map<K, V>` | Insertion order | Keys unique | Key `['Ali']` | Name → marks |

Handy methods: `add`, `remove`, `contains`, `length`, `where` (filter), `map` (transform), `reduce` (combine), `forEach`.

### 2. Generics

`<T>` is a **type placeholder**. `List<int>` only accepts ints, so mistakes are caught early. You can write your own generic code — e.g. `Box<T>` — that works for any type while staying type safe.

### 3. Synchronous vs asynchronous

- **Synchronous:** each line waits for the previous one. A slow task blocks everything.
- **Asynchronous:** start a slow task, keep the app responsive, and handle the result when it arrives.

> **Analogy:** at a busy cafe you order, receive a token (a **Future**), and sit down. When your token is called, you collect your food. A **Stream** is like a live cricket score ticker — updates keep arriving until the match ends.

Dart runs your code on a single thread with an **event loop** that picks up finished tasks one by one:

```mermaid
sequenceDiagram
  participant Main as main()
  participant Loop as Event loop
  participant Server as Slow task
  Main->>Server: start fetchResult()
  Main->>Main: keeps running other code
  Server-->>Loop: result ready
  Loop-->>Main: resume after await
```

### 4. Futures, async and await

| Keyword | Meaning |
|---------|---------|
| `Future<T>` | A value of type T that will be ready later (or an error) |
| `async` | Marks a function that uses `await`; it always returns a Future |
| `await` | Pause this function until the Future completes |
| `.then()` | Older callback style to handle a Future |
| `Future.wait([...])` | Wait for several Futures running together |

### 5. Streams

- A `Stream<T>` delivers **zero or more** values, then an optional "done".
- Create one with an `async*` function and `yield`.
- Consume it with `await for` (inside async code) or `listen()` (event callbacks — this is exactly how button clicks work in Session 06).

### 6. Exceptions

An exception is an error that happens while the program runs. Without handling, the program stops.

- `try` — code that might fail; `catch (e)` — handle any error; `on Type catch (e)` — handle one specific type; `finally` — always runs.
- `throw` raises an error. Create your own by implementing `Exception`.

## 💻 Code Examples

### Example 1: Collections and generics

📄 File: [`collections_and_generics.dart`](./collections_and_generics.dart)

```dart
// collections_and_generics.dart
// List, Set and Map, plus generics (the <Type> part).

void main() {
  // LIST: ordered, allows duplicates, accessed by index (starting at 0).
  List<String> cities = ['Karachi', 'Lahore', 'Quetta'];
  cities.add('Peshawar');
  print('First city: ${cities[0]}');
  print('All cities: $cities (count: ${cities.length})');

  // SET: no duplicates allowed. Good for unique values.
  Set<String> skills = {'Dart', 'Python'};
  skills.add('Dart'); // ignored, already there
  skills.add('SQL');
  print('Unique skills: $skills');

  // MAP: key -> value pairs, like a dictionary.
  Map<String, int> marks = {'Ayesha': 88, 'Bilal': 74};
  marks['Hina'] = 91; // add a new pair
  print('Bilal got ${marks['Bilal']}');
  marks.forEach((name, score) => print('$name -> $score'));

  // Useful list methods: where (filter), map (transform), reduce (combine).
  List<int> scores = [45, 78, 92, 60, 33];
  List<int> passed = scores.where((s) => s >= 50).toList();
  List<String> labels = scores.map((s) => 'Score $s').toList();
  int total = scores.reduce((a, b) => a + b);
  print('Passed scores: $passed');
  print('Labels: $labels');
  print('Average: ${total / scores.length}');

  // GENERICS: write one class that works with ANY type T.
  Box<int> numberBox = Box<int>(42);
  Box<String> textBox = Box<String>('Hello');
  print('Number box holds ${numberBox.item}');
  print('Text box holds ${textBox.item}');

  // A generic function.
  print('First of list: ${firstItem<String>(cities)}');
}

// T is a placeholder for a real type chosen later.
class Box<T> {
  T item;
  Box(this.item);
}

T firstItem<T>(List<T> items) {
  return items[0];
}
```

**How it works**

- The `Set` silently ignores the duplicate `'Dart'`.
- `where`, `map` and `reduce` replace manual loops for filtering, transforming and totalling.
- `Box<T>` is one class that safely stores an `int` or a `String`.

### Example 2: Futures with async / await

📄 File: [`futures_async_await.dart`](./futures_async_await.dart)

```dart
// futures_async_await.dart
// A Future is a value that will be ready LATER (like an order token at a cafe).

// This function pretends to download a result from a server.
// It returns Future<String>: "a String will arrive in the future".
Future<String> fetchResult(String rollNumber) {
  return Future.delayed(Duration(seconds: 2), () {
    return 'Result for $rollNumber: Passed with 82%';
  });
}

// async + await: write asynchronous code that reads like normal code.
Future<void> showResult() async {
  print('Fetching result... please wait');

  // await pauses THIS function until the Future finishes.
  String result = await fetchResult('STU-1024');

  print(result);
}

Future<int> countDownloads() async {
  await Future.delayed(Duration(seconds: 1));
  return 350;
}

Future<void> main() async {
  print('1. Program started');

  // The old style: then() runs when the Future completes.
  fetchResult('STU-0001').then((value) {
    print('(then) $value');
  });

  // The modern style: async / await.
  await showResult();

  // Run two Futures at the same time and wait for both.
  List<Object> both = await Future.wait([
    fetchResult('STU-2000'),
    countDownloads(),
  ]);
  print('Both finished: ${both[0]} | downloads: ${both[1]}');

  print('2. Program finished');
}
```

**How it works**

- `Future.delayed` simulates a 2-second network call.
- Notice in the output that `(then)` and the awaited result arrive later than "Fetching result...", because the program did not freeze while waiting.
- `Future.wait` runs both tasks together, so the total wait is the longest one, not the sum.

### Example 3: Streams

📄 File: [`streams.dart`](./streams.dart)

```dart
// streams.dart
// A Stream delivers MANY values over time (like a live cricket score feed).

// async* + yield: a function that produces a stream of values.
Stream<int> countdown(int from) async* {
  for (int i = from; i >= 1; i--) {
    await Future.delayed(Duration(milliseconds: 500));
    yield i; // send one value into the stream
  }
}

// A stream of score updates.
Stream<String> cricketScore() async* {
  List<String> updates = ['10/0', '45/1', '88/2', '120/2'];
  for (String score in updates) {
    await Future.delayed(Duration(milliseconds: 300));
    yield 'Pakistan: $score';
  }
}

Future<void> main() async {
  // 1. await for: read each value as it arrives.
  print('Countdown:');
  await for (int number in countdown(3)) {
    print('  $number');
  }
  print('  Go!');

  // 2. listen(): event-driven style with callbacks.
  print('Live score:');
  cricketScore().listen(
    (update) => print('  $update'),   // runs for every new value
    onDone: () => print('  Innings over.'), // runs at the end
  );

  // Wait so the listener above can finish before main ends.
  await Future.delayed(Duration(seconds: 2));

  // 3. Streams have list-like helpers such as where and map.
  Stream<int> numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
  await for (int even in numbers.where((n) => n.isEven)) {
    print('Even number from stream: $even');
  }
}
```

**How it works**

- `async*` + `yield` produce values one at a time.
- `await for` reads values in order; `listen` reacts to each event and to `onDone`.

### Example 4: Exception handling

📄 File: [`exceptions.dart`](./exceptions.dart)

```dart
// exceptions.dart
// Handling errors so the program does not crash.

// Our own exception type with a clear message.
class InsufficientBalanceException implements Exception {
  final String message;
  InsufficientBalanceException(this.message);

  @override
  String toString() => 'InsufficientBalanceException: $message';
}

double withdraw(double balance, double amount) {
  if (amount > balance) {
    // throw: raise an error and stop this function.
    throw InsufficientBalanceException('You only have Rs. $balance');
  }
  return balance - amount;
}

Future<String> loadProfile(bool serverIsUp) async {
  await Future.delayed(Duration(milliseconds: 300));
  if (!serverIsUp) {
    throw Exception('Server not responding');
  }
  return 'Profile loaded';
}

Future<void> main() async {
  // 1. try / catch / finally
  try {
    int marks = int.parse('eighty'); // this is not a number!
    print('Marks: $marks');
  } catch (e) {
    print('Could not read marks: $e');
  } finally {
    print('finally always runs (good for cleanup).');
  }

  // 2. on: catch one specific type of error.
  try {
    withdraw(1000, 5000);
  } on InsufficientBalanceException catch (e) {
    print('Withdraw failed -> $e');
  }

  // 3. Errors inside async code are caught with try/catch around await.
  try {
    String profile = await loadProfile(false);
    print(profile);
  } catch (e) {
    print('Async error caught: $e');
  }

  print('The program is still running. No crash!');
}
```

**How it works**

- `int.parse('eighty')` throws a `FormatException`, which is caught instead of crashing.
- `on InsufficientBalanceException` catches only our custom error type.
- Wrapping `await` in `try/catch` handles errors from async code.

## 🧪 Lab Practice

1. Create a `Map<String, double>` of 5 product prices. Print products costing more than Rs. 500 using `where` on `entries`.
2. Write `Future<String> downloadFile(String name)` that waits 3 seconds and returns "name downloaded". Call it with `await` and print a message before and after.
3. Download three files at the same time using `Future.wait` and measure the time with `Stopwatch`.
4. Create `Stream<int> tableOf(int n)` that yields `n × 1` to `n × 10` every 300 ms. Print it with `await for`.
5. Write `double divide(int a, int b)` that throws a custom `DivideByZeroException` when `b == 0`, and handle it with `on ... catch`.

## 📝 Assignment

Build `order_tracker.dart`: a `Stream<String>` that yields order states ("Placed", "Preparing", "Out for delivery", "Delivered") one second apart. Before tracking, `await` a `Future<bool> checkPayment(double amount)` that throws an exception if amount is 0. Handle the error with a friendly message and print every order state as it arrives.

## ❓ Quick Quiz

1. Which collection automatically removes duplicates?
2. What does a function marked `async` always return?
3. What is the difference between a Future and a Stream?
4. Which keyword sends a value out of an `async*` function?
5. When does a `finally` block run?

<details>
<summary>Show answers</summary>

1. `Set`.
2. A `Future`.
3. A Future gives one value (or error) later; a Stream gives many values over time.
4. `yield`.
5. Always — whether an exception happened or not.

</details>

## 💼 Interview Questions

1. **Is Dart single-threaded? How does it handle async work?** — Your code runs on one thread (per isolate) with an event loop; slow I/O happens outside and its result is queued back as an event, so the UI never blocks. For heavy CPU work Dart uses separate isolates.
2. **What happens if you forget `await`?** — You get a `Future` object instead of the value, and the next lines run before the work finishes, causing bugs.
3. **`catch` vs `on`?** — `on Type` filters by exception type; `catch (e)` gives access to the error object. They can be combined: `on FormatException catch (e)`.

## ✅ Summary

- `List`, `Set` and `Map` store groups of values; generics keep them type safe.
- Async code keeps apps responsive; the event loop resumes your code when work finishes.
- `Future` + `async/await` = one delayed value; `Stream` + `await for`/`listen` = many values.
- `try/catch/on/finally` and custom exceptions make programs robust instead of crash-prone.

---

[⬅ Previous](../Session-02-Object-Oriented-Programming-in-Dart/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Packages-and-Pub/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
