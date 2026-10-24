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
