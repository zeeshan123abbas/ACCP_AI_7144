// lab4_word_counter.dart
// Practice: Strings, Map counting and sorting.

void main() {
  String paragraph =
      'Dart is fun. Dart is fast. Flutter uses Dart and Flutter is popular.';

  // Step 1: make lowercase and remove full stops.
  String cleanText = paragraph.toLowerCase().replaceAll('.', '');

  // Step 2: split the text into words wherever there is a space.
  List<String> words = cleanText.split(' ');

  // Step 3: count each word in a Map<String, int>.
  Map<String, int> counts = {};
  for (String word in words) {
    // If the word is new, start at 0, then add 1.
    counts[word] = (counts[word] ?? 0) + 1;
  }

  // Step 4: sort the words by count, biggest first.
  List<MapEntry<String, int>> sorted = counts.entries.toList();
  sorted.sort((a, b) => b.value.compareTo(a.value));

  print('Total words: ${words.length}');
  print('Top 3 words:');
  for (MapEntry<String, int> entry in sorted.take(3)) {
    print('  ${entry.key}: ${entry.value}');
  }
}
