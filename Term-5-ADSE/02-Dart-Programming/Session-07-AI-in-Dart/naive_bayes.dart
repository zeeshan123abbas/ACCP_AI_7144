// naive_bayes.dart
// A tiny "spam or not spam" classifier written in plain Dart (no packages).
// Run with:  dart run naive_bayes.dart
//
// Idea: count how often each word appears in spam and in normal (ham)
// messages, then use those counts to guess the label of a new message.

import 'dart:math';

class NaiveBayesClassifier {
  // How many training messages each label has, e.g. {'spam': 4, 'ham': 4}
  final Map<String, int> messagesPerLabel = {};

  // Word counts per label, e.g. {'spam': {'free': 3, 'win': 2}, ...}
  final Map<String, Map<String, int>> wordCounts = {};

  // Every different word we have seen (the vocabulary).
  final Set<String> vocabulary = {};

  // Turn a sentence into a list of clean lowercase words.
  List<String> tokenize(String text) {
    String clean = text.toLowerCase().replaceAll(RegExp(r'[^a-z0-9 ]'), '');
    return clean.split(' ').where((word) => word.isNotEmpty).toList();
  }

  // TRAINING: learn from one example message and its correct label.
  void train(String text, String label) {
    messagesPerLabel[label] = (messagesPerLabel[label] ?? 0) + 1;
    wordCounts.putIfAbsent(label, () => {});

    for (String word in tokenize(text)) {
      Map<String, int> counts = wordCounts[label]!;
      counts[word] = (counts[word] ?? 0) + 1;
      vocabulary.add(word);
    }
  }

  // PREDICTION: return the most likely label for a new message.
  String predict(String text) {
    int totalMessages = messagesPerLabel.values.reduce((a, b) => a + b);
    String bestLabel = '';
    double bestScore = double.negativeInfinity;

    for (String label in messagesPerLabel.keys) {
      // Step 1: prior = how common this label is overall.
      // We add logarithms instead of multiplying tiny numbers (safer).
      double score = log(messagesPerLabel[label]! / totalMessages);

      // Step 2: total words seen in this label.
      Map<String, int> counts = wordCounts[label]!;
      int wordsInLabel = counts.values.reduce((a, b) => a + b);

      // Step 3: add the likelihood of every word in the message.
      for (String word in tokenize(text)) {
        int wordCount = counts[word] ?? 0;
        // "+1" is Laplace smoothing: unseen words do not give zero.
        double probability = (wordCount + 1) / (wordsInLabel + vocabulary.length);
        score += log(probability);
      }

      // Step 4: keep the label with the highest score.
      if (score > bestScore) {
        bestScore = score;
        bestLabel = label;
      }
    }
    return bestLabel;
  }
}

void main() {
  NaiveBayesClassifier model = NaiveBayesClassifier();

  // Small training data set (made-up examples).
  model.train('Win a FREE phone now', 'spam');
  model.train('Claim your free prize money today', 'spam');
  model.train('Congratulations you won a lucky draw', 'spam');
  model.train('Free recharge offer click now', 'spam');
  model.train('Class is shifted to room 4 today', 'ham');
  model.train('Please submit your Dart assignment', 'ham');
  model.train('Can we meet after the lab session', 'ham');
  model.train('The exam schedule is on the notice board', 'ham');

  // Test with messages the model has never seen.
  List<String> newMessages = [
    'You won a free prize, click now',
    'Is the Dart lab session today',
    'Lucky draw offer for you',
    'Submit the assignment before the exam',
  ];

  for (String message in newMessages) {
    print('${model.predict(message).toUpperCase().padRight(5)} <- "$message"');
  }
}
