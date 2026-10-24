// constructors_getters_setters.dart
// Different constructors, plus getters and setters for safe data access.

class BankAccount {
  // final: the owner never changes after the account is created.
  final String owner;

  // The underscore (_) makes the field private to this file.
  double _balance;

  // 1. Normal constructor with a named, optional parameter.
  BankAccount(this.owner, {double openingBalance = 0}) : _balance = openingBalance;

  // 2. Named constructor: another way to create an object.
  BankAccount.student(this.owner) : _balance = 500; // bonus for students

  // Getter: read-only access to the private balance.
  double get balance => _balance;

  // A computed getter: calculated every time it is read.
  bool get isEmpty => _balance == 0;

  // Setter with a check, so nobody can set a negative limit.
  double _dailyLimit = 20000;
  double get dailyLimit => _dailyLimit;
  set dailyLimit(double value) {
    if (value < 0) {
      print('Limit cannot be negative. Keeping $_dailyLimit');
      return;
    }
    _dailyLimit = value;
  }

  void deposit(double amount) {
    _balance = _balance + amount;
    print('$owner deposited Rs. $amount');
  }
}

void main() {
  BankAccount account = BankAccount('Zainab', openingBalance: 1000);
  BankAccount studentAccount = BankAccount.student('Ali');

  account.deposit(250);
  print('${account.owner} balance: Rs. ${account.balance}');
  print('${studentAccount.owner} balance: Rs. ${studentAccount.balance}');

  // account.balance = 99999;  // ERROR: there is no setter for balance.

  account.dailyLimit = -5;      // rejected by the setter
  account.dailyLimit = 50000;   // accepted
  print('Daily limit: Rs. ${account.dailyLimit}');
  print('Is empty? ${account.isEmpty}');
}
