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
