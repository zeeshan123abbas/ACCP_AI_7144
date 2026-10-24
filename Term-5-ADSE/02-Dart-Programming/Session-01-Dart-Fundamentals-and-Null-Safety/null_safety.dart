// null_safety.dart
// Sound null safety: a variable cannot hold null unless you allow it.

void main() {
  // 1. Non-nullable: must always have a value.
  String name = 'Hamza';
  // name = null;   // ERROR: null can't be assigned to a String.

  // 2. Nullable: add ? after the type to allow null.
  String? middleName = findMiddleName('Hamza'); // may be null
  print('Middle name: $middleName');

  // 3. ?? (if-null operator): use a backup value when it is null.
  String displayName = middleName ?? 'No middle name';
  print(displayName);

  // 4. ?. (null-aware access): only call when not null.
  print('Length of middle name: ${middleName?.length}'); // prints null

  // 5. ??= : give a value only if the variable is null right now.
  middleName ??= 'Ali';
  print('Middle name now: $middleName');

  // 6. Checking for null first. After the check Dart "promotes" the type.
  String? phone = findPhone('Hamza');
  if (phone != null) {
    // Here Dart knows phone is a String, not String?.
    print('$name\'s phone has ${phone.length} digits.');
  } else {
    print('No phone found for $name.');
  }

  // 7. ! (null assertion): "I promise this is not null".
  // Use it rarely. If you are wrong, the program crashes.
  String confirmedPhone = findPhone('Hamza')!; // we know Hamza exists
  print('Confirmed phone: $confirmedPhone');

  // 8. late: the value will be set later, before it is used.
  late String welcomeMessage;
  welcomeMessage = 'Welcome to the Dart module!';
  print(welcomeMessage);
}

// A function that may return null (notice the String? return type).
String? findPhone(String person) {
  if (person == 'Hamza') {
    return '03001234567';
  }
  return null;
}

// Hamza has no middle name on record, so this returns null.
String? findMiddleName(String person) {
  return null;
}
