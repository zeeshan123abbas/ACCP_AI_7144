// classes_and_objects.dart
// A class is a blueprint. An object is a real thing made from that blueprint.

// The blueprint: every Student has a name, a roll number and marks.
class Student {
  // Fields (also called properties or instance variables).
  String name;
  String rollNumber;
  int marks;

  // A constructor that fills the fields. "this.name" is a shortcut.
  Student(this.name, this.rollNumber, this.marks);

  // A method: a function that belongs to the class.
  void introduce() {
    print('I am $name, roll number $rollNumber.');
  }

  // A method that returns a value.
  bool hasPassed() {
    return marks >= 50;
  }
}

void main() {
  // Create two objects (instances) from the same class.
  Student first = Student('Ayesha', 'STU-01', 82);
  Student second = Student('Usman', 'STU-02', 45);

  // Call methods using the dot (.) operator.
  first.introduce();
  print('Passed? ${first.hasPassed()}');

  second.introduce();
  print('Passed? ${second.hasPassed()}');

  // We can read and change fields of an object.
  second.marks = 55; // after re-sit exam
  print('${second.name} marks after re-sit: ${second.marks}');
  print('Passed now? ${second.hasPassed()}');
}
