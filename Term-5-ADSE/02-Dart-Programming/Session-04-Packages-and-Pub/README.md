# Session 04: Packages, pub and Writing Your Own Package

> Module: Dart Programming · Term 5 (ADSE) · ⏱ ~2 hours

No developer writes everything from scratch. Dart's package manager **pub** and the website [pub.dev](https://pub.dev/) give you thousands of ready-made packages for HTTP, dates, databases and more. In this session you use packages, then build, document and test your own small package — exactly the way professionals share code.

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain what a package is and the role of `pubspec.yaml`
- Add hosted (pub.dev) and path (local) dependencies and run `dart pub get`
- Understand semantic versioning and the caret `^` constraint
- Create a package with the standard folder layout and doc comments
- Write unit tests with `package:test` and prepare a package for publishing

## 📖 Concepts Explained

### 1. What is a package?

A **package** is a folder of Dart code with a `pubspec.yaml` file that describes it. Every Dart project is a package, even if you never publish it.

| File / folder | Purpose |
|---------------|---------|
| `pubspec.yaml` | Name, version, description, SDK range and dependencies |
| `lib/` | Public code other packages can import |
| `lib/src/` | Private implementation, exposed only through `export` |
| `bin/` | Command-line entry points (`dart run`) |
| `test/` | Unit tests (`dart test`) |
| `example/` | Short usage example (shown on pub.dev) |
| `README.md`, `CHANGELOG.md`, `LICENSE` | Documentation needed to publish |
| `pubspec.lock` | Exact versions pub chose (commit it for apps, not for packages) |

### 2. Dependencies

- `dependencies:` — needed to run your code (e.g. `http`, `intl`).
- `dev_dependencies:` — needed only while developing (e.g. `test`, `lints`).
- **Hosted** dependency: `intl: ^0.20.0` (downloaded from pub.dev).
- **Path** dependency: `grade_calculator: { path: ../grade_calculator }` (local folder — great while developing).
- Commands: `dart pub add http`, `dart pub get`, `dart pub upgrade`, `dart pub outdated`.

### 3. Semantic versioning (SemVer)

Versions look like `MAJOR.MINOR.PATCH`, e.g. `1.4.2`.

| Change | Bump | Example |
|--------|------|---------|
| Bug fix, nothing breaks | PATCH | 1.4.2 → 1.4.3 |
| New feature, old code still works | MINOR | 1.4.3 → 1.5.0 |
| Breaking change | MAJOR | 1.5.0 → 2.0.0 |

`^1.4.2` means "1.4.2 or newer, but **below 2.0.0**". For versions below 1.0, `^0.20.0` means `>=0.20.0 <0.21.0`.

### 4. Documentation comments

Comments starting with `///` become official docs. `dart doc` turns them into a website, and pub.dev shows them automatically. Put names of parameters in square brackets: `/// Returns the grade for [marks].`

### 5. Publishing flow

```mermaid
flowchart LR
  A[Write code in lib/] --> B[Add tests and docs]
  B --> C[dart test]
  C --> D[dart pub publish --dry-run]
  D --> E[Fix warnings]
  E --> F[dart pub publish]
  F --> G[Package live on pub.dev]
```

Before publishing: a unique name, a good description, a `repository` URL, README, CHANGELOG and an open-source LICENSE. **Publishing is permanent** — you cannot delete a version, so practise with `--dry-run`.

## 💻 Code Examples

The session folder contains two projects: [`grade_calculator/`](./grade_calculator/) (our package) and [`report_app/`](./report_app/) (an app that uses it).

### Example 1: The package's pubspec

📄 File: [`grade_calculator/pubspec.yaml`](./grade_calculator/pubspec.yaml)

```yaml
# pubspec.yaml - the "ID card" of a Dart package.
name: grade_calculator
description: A tiny beginner package that turns marks into grades and calculates averages.
version: 1.0.0
# repository: https://github.com/your-username/grade_calculator  # add before publishing

environment:
  sdk: ^3.5.0

# Packages needed only while developing (tests, linting).
dev_dependencies:
  lints: ^5.0.0
  test: ^1.25.0
```

**How it works**

- The package has no runtime dependencies; `test` and `lints` are only for development.
- `sdk: ^3.5.0` means "any Dart 3 version from 3.5 onward".

### Example 2: Library file and implementation

📄 File: [`grade_calculator/lib/grade_calculator.dart`](./grade_calculator/lib/grade_calculator.dart)

```dart
/// A tiny library for converting marks into grades.
///
/// Import it with:
/// ```dart
/// import 'package:grade_calculator/grade_calculator.dart';
/// ```
library;

// Export the public parts so users need only ONE import.
export 'src/grades.dart';
```

📄 File: [`grade_calculator/lib/src/grades.dart`](./grade_calculator/lib/src/grades.dart)

```dart
// Code inside lib/src/ is private to the package.
// It becomes public only because lib/grade_calculator.dart exports it.

/// Returns the letter grade for [marks] out of 100.
///
/// Throws an [ArgumentError] if [marks] is below 0 or above 100.
String gradeFor(int marks) {
  // Step 1: reject impossible values.
  if (marks < 0 || marks > 100) {
    throw ArgumentError('Marks must be between 0 and 100, got $marks');
  }

  // Step 2: pick the grade from the highest band down.
  if (marks >= 80) return 'A';
  if (marks >= 70) return 'B';
  if (marks >= 60) return 'C';
  if (marks >= 50) return 'D';
  return 'F';
}

/// Returns the average of [allMarks], or 0 when the list is empty.
double averageOf(List<int> allMarks) {
  if (allMarks.isEmpty) return 0;

  int total = 0;
  for (int marks in allMarks) {
    total += marks;
  }
  return total / allMarks.length;
}

/// Returns true when [marks] is a passing score (50 or more).
bool isPass(int marks) => marks >= 50;
```

**How it works**

- Users import one file; it re-exports the code from `lib/src/`.
- `///` comments document every public function.

### Example 3: Unit tests

📄 File: [`grade_calculator/test/grade_calculator_test.dart`](./grade_calculator/test/grade_calculator_test.dart)

```dart
// Unit tests for the package. Run with:  dart test
import 'package:grade_calculator/grade_calculator.dart';
import 'package:test/test.dart';

void main() {
  // group() keeps related tests together.
  group('gradeFor', () {
    test('gives A for 80 and above', () {
      expect(gradeFor(80), equals('A'));
      expect(gradeFor(100), equals('A'));
    });

    test('gives F below 50', () {
      expect(gradeFor(49), equals('F'));
    });

    test('throws for marks outside 0-100', () {
      expect(() => gradeFor(120), throwsArgumentError);
    });
  });

  group('averageOf', () {
    test('calculates the average', () {
      expect(averageOf([60, 70, 80]), equals(70));
    });

    test('returns 0 for an empty list', () {
      expect(averageOf([]), equals(0));
    });
  });

  test('isPass checks the 50 mark boundary', () {
    expect(isPass(50), isTrue);
    expect(isPass(49), isFalse);
  });
}
```

**Run it:**

```bash
cd grade_calculator
dart pub get
dart test
dart run example/main.dart
```

**How it works**

- `expect(actual, matcher)` checks a result; `throwsArgumentError` checks that bad input fails correctly.
- Test the boundaries (49, 50, 80) — that is where bugs usually hide.

### Example 4: Using packages in an app

📄 File: [`report_app/pubspec.yaml`](./report_app/pubspec.yaml)

```yaml
# A small app that USES two packages:
#  1. intl            -> downloaded from pub.dev (a "hosted" dependency)
#  2. grade_calculator -> our own package, taken from a local folder (a "path" dependency)
name: report_app
description: Prints a result card using the grade_calculator package.
version: 1.0.0
publish_to: none # this app is not meant for pub.dev

environment:
  sdk: ^3.5.0

dependencies:
  intl: ^0.20.0            # caret (^) = any 0.20.x version, but not 0.21.0
  grade_calculator:
    path: ../grade_calculator
```

📄 File: [`report_app/bin/report_app.dart`](./report_app/bin/report_app.dart)

```dart
// bin/report_app.dart
// Run from the report_app folder:
//   dart pub get
//   dart run

// Imports from packages always start with "package:".
import 'package:grade_calculator/grade_calculator.dart';
import 'package:intl/intl.dart';

void main() {
  // Data for one student.
  String studentName = 'Ayesha Khan';
  Map<String, int> subjectMarks = {
    'Dart': 88,
    'Flutter': 76,
    'Python': 64,
  };

  // intl formats today's date in a friendly way, e.g. 24 Oct 2026.
  String today = DateFormat('d MMM yyyy').format(DateTime.now());

  print('===== RESULT CARD =====');
  print('Student: $studentName');
  print('Date:    $today');
  print('-----------------------');

  // grade_calculator turns each mark into a grade.
  subjectMarks.forEach((subject, marks) {
    print('${subject.padRight(10)} $marks  (${gradeFor(marks)})');
  });

  double average = averageOf(subjectMarks.values.toList());
  print('-----------------------');
  print('Average:   ${average.toStringAsFixed(1)}  (${gradeFor(average.round())})');
}
```

**Run it:** `cd report_app`, then `dart pub get` and `dart run`.

**How it works**

- `intl` comes from pub.dev; `grade_calculator` comes from the neighbouring folder.
- `publish_to: none` stops the app from being published by mistake.

## 🧪 Lab Practice

1. Run `dart create -t package string_tools` and look at the generated folders.
2. Add a function `String capitalizeWords(String text)` in `lib/src/`, export it, and document it with `///`.
3. Write three tests for it (normal sentence, empty string, extra spaces) and run `dart test`.
4. Create a console app with `dart create text_app` and add `string_tools` as a path dependency. Use your function.
5. Add `http` with `dart pub add http`, open `pubspec.yaml` and note the version constraint it added. Run `dart pub outdated`.

## 📝 Assignment

Create a package `pk_utils` with two functions: `bool isValidCnic(String cnic)` (format `12345-1234567-1`) and `String formatRupees(num amount)` (e.g. `Rs. 1,250`). Include doc comments, an `example/main.dart`, a README, a CHANGELOG for version `0.1.0`, at least five tests, and run `dart pub publish --dry-run` (do **not** actually publish). Submit a screenshot of passing tests.

## ❓ Quick Quiz

1. Which file lists a package's dependencies?
2. Where should private implementation code go?
3. What range does `^2.3.1` allow?
4. What is the difference between `dependencies` and `dev_dependencies`?
5. Which command checks a package for publishing problems without uploading it?

<details>
<summary>Show answers</summary>

1. `pubspec.yaml`.
2. `lib/src/`.
3. `>=2.3.1 <3.0.0`.
4. `dependencies` are needed to run the code; `dev_dependencies` only for development tasks like testing.
5. `dart pub publish --dry-run`.

</details>

## 💼 Interview Questions

1. **What is `pubspec.lock` and should it be committed?** — It records the exact versions resolved by pub. Commit it for applications (repeatable builds); packages usually do not, so users resolve their own versions.
2. **What is a breaking change and how is it versioned?** — A change that makes existing user code fail (renamed function, changed parameters); it needs a MAJOR version bump.
3. **Why keep code in `lib/src/` and export selectively?** — It hides internal details, keeps the public API small and lets you refactor internals without breaking users.

## ✅ Summary

- A package = code + `pubspec.yaml`; pub downloads dependencies from pub.dev.
- Use hosted dependencies for published packages and path dependencies while developing locally.
- SemVer and `^` constraints keep upgrades safe.
- A good package has `lib/`, `lib/src/`, tests, example, docs, CHANGELOG and LICENSE.
- Always `dart test` and `dart pub publish --dry-run` before publishing.

---

[⬅ Previous](../Session-03-Async-Futures-Streams-and-Exceptions/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Practice-Lab-Dart-Foundations/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
