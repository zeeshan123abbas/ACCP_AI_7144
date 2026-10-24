// example/main.dart - shows people how to use the package.
// Run from the package folder with:  dart run example/main.dart
import 'package:grade_calculator/grade_calculator.dart';

void main() {
  List<int> classMarks = [91, 67, 48, 75];

  for (int marks in classMarks) {
    print('$marks marks -> grade ${gradeFor(marks)}');
  }

  print('Class average: ${averageOf(classMarks).toStringAsFixed(1)}');
}
