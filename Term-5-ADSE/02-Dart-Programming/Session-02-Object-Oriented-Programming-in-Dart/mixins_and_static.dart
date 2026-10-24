// mixins_and_static.dart
// Mixins share abilities between classes. Static members belong to the class.

// A mixin is a bundle of methods you can "mix in" to many classes.
mixin CanSwim {
  void swim() => print('$runtimeType is swimming.');
}

mixin CanFly {
  void fly() => print('$runtimeType is flying.');
}

class Animal {
  void breathe() => print('$runtimeType is breathing.');
}

// "with" adds the mixins to the class.
class Duck extends Animal with CanSwim, CanFly {}

class Fish extends Animal with CanSwim {}

// Static members: shared by the class, not by each object.
class Student {
  // One counter for the whole class.
  static int totalStudents = 0;

  // A constant that belongs to the class.
  static const String instituteName = 'Aptech North Nazimabad';

  String name;

  Student(this.name) {
    totalStudents++; // every new student increases the shared counter
  }

  // A static method is called on the class name, not on an object.
  static void showTotal() {
    print('Total students at $instituteName: $totalStudents');
  }
}

void main() {
  Duck duck = Duck();
  duck.breathe();
  duck.swim();
  duck.fly();

  Fish fish = Fish();
  fish.swim();
  // fish.fly();   // ERROR: Fish does not have the CanFly mixin.

  Student('Hira');
  Student('Owais');
  Student('Maham');
  Student.showTotal(); // called on the class itself
}
