# grade_calculator

A tiny Dart package that converts marks (0-100) into letter grades and calculates averages.
Built as a learning example for Session 04 of the Dart Programming module.

## Usage

```dart
import 'package:grade_calculator/grade_calculator.dart';

void main() {
  print(gradeFor(85));            // A
  print(averageOf([60, 70, 80])); // 70.0
}
```

## Running the tests

```bash
dart pub get
dart test
```
