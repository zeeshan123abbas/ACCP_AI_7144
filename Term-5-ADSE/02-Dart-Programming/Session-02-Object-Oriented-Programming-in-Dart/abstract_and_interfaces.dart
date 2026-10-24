// abstract_and_interfaces.dart
// Abstract classes describe WHAT must be done; child classes decide HOW.

// An abstract class cannot be turned into an object directly.
abstract class Shape {
  // Abstract method: no body. Every child must write one.
  double area();

  // A normal method that all shapes share.
  void describe() {
    print('${runtimeType} with area ${area().toStringAsFixed(2)}');
  }
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}

class Rectangle extends Shape {
  double width, height;
  Rectangle(this.width, this.height);

  @override
  double area() => width * height;
}

// Interfaces: in Dart every class can be used as an interface.
// "implements" means: I promise to provide ALL these members myself.
abstract interface class Printable {
  void printDetails();
}

class Invoice implements Printable {
  String customer;
  double amount;
  Invoice(this.customer, this.amount);

  @override
  void printDetails() {
    print('Invoice for $customer: Rs. $amount');
  }
}

void main() {
  // Shape s = Shape();   // ERROR: abstract classes can't be created.

  List<Shape> shapes = [Circle(2), Rectangle(3, 4)];
  for (Shape shape in shapes) {
    shape.describe();
  }

  Printable bill = Invoice('Ahmed Traders', 15000);
  bill.printDetails();
}
