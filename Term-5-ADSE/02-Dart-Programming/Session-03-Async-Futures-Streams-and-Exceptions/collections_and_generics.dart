// collections_and_generics.dart
// List, Set and Map, plus generics (the <Type> part).

void main() {
  // LIST: ordered, allows duplicates, accessed by index (starting at 0).
  List<String> cities = ['Karachi', 'Lahore', 'Quetta'];
  cities.add('Peshawar');
  print('First city: ${cities[0]}');
  print('All cities: $cities (count: ${cities.length})');

  // SET: no duplicates allowed. Good for unique values.
  Set<String> skills = {'Dart', 'Python'};
  skills.add('Dart'); // ignored, already there
  skills.add('SQL');
  print('Unique skills: $skills');

  // MAP: key -> value pairs, like a dictionary.
  Map<String, int> marks = {'Ayesha': 88, 'Bilal': 74};
  marks['Hina'] = 91; // add a new pair
  print('Bilal got ${marks['Bilal']}');
  marks.forEach((name, score) => print('$name -> $score'));

  // Useful list methods: where (filter), map (transform), reduce (combine).
  List<int> scores = [45, 78, 92, 60, 33];
  List<int> passed = scores.where((s) => s >= 50).toList();
  List<String> labels = scores.map((s) => 'Score $s').toList();
  int total = scores.reduce((a, b) => a + b);
  print('Passed scores: $passed');
  print('Labels: $labels');
  print('Average: ${total / scores.length}');

  // GENERICS: write one class that works with ANY type T.
  Box<int> numberBox = Box<int>(42);
  Box<String> textBox = Box<String>('Hello');
  print('Number box holds ${numberBox.item}');
  print('Text box holds ${textBox.item}');

  // A generic function.
  print('First of list: ${firstItem<String>(cities)}');
}

// T is a placeholder for a real type chosen later.
class Box<T> {
  T item;
  Box(this.item);
}

T firstItem<T>(List<T> items) {
  return items[0];
}
