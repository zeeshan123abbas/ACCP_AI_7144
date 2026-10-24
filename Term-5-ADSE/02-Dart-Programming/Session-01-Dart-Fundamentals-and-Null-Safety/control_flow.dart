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
