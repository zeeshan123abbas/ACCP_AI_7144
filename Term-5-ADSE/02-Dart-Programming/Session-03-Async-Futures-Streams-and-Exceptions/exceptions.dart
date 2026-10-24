// exceptions.dart
// Handling errors so the program does not crash.

// Our own exception type with a clear message.
class InsufficientBalanceException implements Exception {
  final String message;
  InsufficientBalanceException(this.message);

  @override
  String toString() => 'InsufficientBalanceException: $message';
}

double withdraw(double balance, double amount) {
  if (amount > balance) {
    // throw: raise an error and stop this function.
    throw InsufficientBalanceException('You only have Rs. $balance');
  }
  return balance - amount;
}

Future<String> loadProfile(bool serverIsUp) async {
  await Future.delayed(Duration(milliseconds: 300));
  if (!serverIsUp) {
    throw Exception('Server not responding');
  }
  return 'Profile loaded';
}

Future<void> main() async {
  // 1. try / catch / finally
  try {
    int marks = int.parse('eighty'); // this is not a number!
    print('Marks: $marks');
  } catch (e) {
    print('Could not read marks: $e');
  } finally {
    print('finally always runs (good for cleanup).');
  }

  // 2. on: catch one specific type of error.
  try {
    withdraw(1000, 5000);
  } on InsufficientBalanceException catch (e) {
    print('Withdraw failed -> $e');
  }

  // 3. Errors inside async code are caught with try/catch around await.
  try {
    String profile = await loadProfile(false);
    print(profile);
  } catch (e) {
    print('Async error caught: $e');
  }

  print('The program is still running. No crash!');
}
