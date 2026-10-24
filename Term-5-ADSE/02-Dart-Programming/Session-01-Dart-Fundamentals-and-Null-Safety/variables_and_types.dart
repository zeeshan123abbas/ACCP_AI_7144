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
