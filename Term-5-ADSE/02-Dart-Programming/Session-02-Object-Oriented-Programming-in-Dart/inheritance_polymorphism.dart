// inheritance_polymorphism.dart
// A child class "extends" a parent class and can override its methods.

// Parent (base) class.
class Employee {
  String name;
  double basicSalary;

  Employee(this.name, this.basicSalary);

  // Child classes may change (override) this method.
  double calculateSalary() {
    return basicSalary;
  }

  void showSalary() {
    print('$name earns Rs. ${calculateSalary()}');
  }
}

// Child class: a Teacher IS an Employee.
class Teacher extends Employee {
  int lecturesPerMonth;

  // super(...) sends values to the parent constructor.
  Teacher(String name, double basicSalary, this.lecturesPerMonth)
      : super(name, basicSalary);

  @override
  double calculateSalary() {
    // Teachers get 500 extra for every lecture.
    return basicSalary + lecturesPerMonth * 500;
  }
}

// Another child class.
class Manager extends Employee {
  Manager(super.name, super.basicSalary); // short form of super(...)

  @override
  double calculateSalary() {
    // Managers get a 20% allowance on top of basic salary.
    return basicSalary * 1.2;
  }
}

void main() {
  // Polymorphism: one list of type Employee holds different kinds of objects.
  List<Employee> staff = [
    Employee('Kamran', 40000),
    Teacher('Sana', 50000, 20),
    Manager('Faisal', 90000),
  ];

  // The same call showSalary() behaves differently for each object.
  for (Employee person in staff) {
    person.showSalary();
  }

  // "is" checks the real type of an object.
  for (Employee person in staff) {
    if (person is Teacher) {
      print('${person.name} gives ${person.lecturesPerMonth} lectures.');
    }
  }
}
