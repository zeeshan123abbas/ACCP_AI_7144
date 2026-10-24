// loops.dart
// Repeating work with for, for-in, while and do-while.

void main() {
  // 1. Classic for loop: start; condition; step.
  print('Counting 1 to 5:');
  for (int i = 1; i <= 5; i++) {
    print('  $i');
  }

  // 2. for-in loop: visit every item of a list.
  List<String> subjects = ['Dart', 'Flutter', 'Python'];
  print('Subjects this term:');
  for (String subject in subjects) {
    print('  - $subject');
  }

  // 3. while loop: repeats as long as the condition is true.
  int balance = 1000;
  int month = 0;
  while (balance > 0) {
    balance = balance - 300; // spend 300 each month
    month++;
  }
  print('Money finished after $month months.');

  // 4. do-while loop: runs the body at least once.
  int tries = 0;
  do {
    tries++;
    print('Attempt number $tries');
  } while (tries < 3);

  // 5. break and continue
  for (int n = 1; n <= 10; n++) {
    if (n % 2 == 0) {
      continue; // skip even numbers
    }
    if (n > 7) {
      break; // stop the loop completely
    }
    print('Odd number: $n');
  }

  // 6. A multiplication table using a loop.
  int table = 7;
  for (int i = 1; i <= 10; i++) {
    print('$table x $i = ${table * i}');
  }
}
