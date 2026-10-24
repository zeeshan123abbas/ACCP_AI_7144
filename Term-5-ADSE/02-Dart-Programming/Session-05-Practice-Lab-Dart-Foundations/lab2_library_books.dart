// lab2_library_books.dart
// Practice: classes, inheritance, abstract classes and collections.

abstract class LibraryItem {
  final String title;
  bool isIssued = false;

  LibraryItem(this.title);

  // Each type of item has its own late-return fine per day.
  int finePerDay();

  void issue() {
    if (isIssued) {
      print('Sorry, "$title" is already issued.');
      return;
    }
    isIssued = true;
    print('"$title" issued.');
  }
}

class Book extends LibraryItem {
  final String author;
  Book(super.title, this.author);

  @override
  int finePerDay() => 20;
}

class Magazine extends LibraryItem {
  Magazine(super.title);

  @override
  int finePerDay() => 10;
}

void main() {
  List<LibraryItem> shelf = [
    Book('Clean Code', 'Robert C. Martin'),
    Book('Dart Apprentice', 'Jonathan Sande'),
    Magazine('Tech Monthly'),
  ];

  shelf[0].issue();
  shelf[0].issue(); // second try should be refused
  shelf[2].issue();

  // Show which items are still available using where().
  List<LibraryItem> available = shelf.where((item) => !item.isIssued).toList();
  print('Available now:');
  for (LibraryItem item in available) {
    print('  - ${item.title}');
  }

  // Fine for returning each item 3 days late.
  int daysLate = 3;
  for (LibraryItem item in shelf) {
    print('${item.title}: fine for $daysLate days = Rs. ${item.finePerDay() * daysLate}');
  }
}
