// functions.dart
// Writing reusable functions with different kinds of parameters.

// A simple function that returns a value.
int add(int a, int b) {
  return a + b;
}

// Arrow syntax: a short way to write a one-line function.
int square(int n) => n * n;

// Optional positional parameter in [ ] with a default value.
String greet(String name, [String title = 'Student']) {
  return 'Hello $title $name';
}

// Named parameters in { }. "required" means the caller must pass it.
double calculateFee({required double monthlyFee, int months = 1}) {
  return monthlyFee * months;
}

// A function that returns nothing uses void.
void printLine() {
  print('-' * 30);
}

void main() {
  print('2 + 3 = ${add(2, 3)}');
  print('Square of 9 = ${square(9)}');
  printLine();

  print(greet('Bilal'));          // uses the default title
  print(greet('Sana', 'Miss'));   // passes a title
  printLine();

  // Named arguments can be written in any order.
  double fee = calculateFee(months: 3, monthlyFee: 4500);
  print('Fee for 3 months: Rs. $fee');
  printLine();

  // Functions are values too: we can store one in a variable.
  int Function(int) myFunction = square;
  print('Using a stored function: ${myFunction(4)}');

  // Anonymous function (no name) passed to forEach.
  List<int> numbers = [1, 2, 3];
  numbers.forEach((number) {
    print('Number x 10 = ${number * 10}');
  });
}
