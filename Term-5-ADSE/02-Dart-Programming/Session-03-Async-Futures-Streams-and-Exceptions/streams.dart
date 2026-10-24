// streams.dart
// A Stream delivers MANY values over time (like a live cricket score feed).

// async* + yield: a function that produces a stream of values.
Stream<int> countdown(int from) async* {
  for (int i = from; i >= 1; i--) {
    await Future.delayed(Duration(milliseconds: 500));
    yield i; // send one value into the stream
  }
}

// A stream of score updates.
Stream<String> cricketScore() async* {
  List<String> updates = ['10/0', '45/1', '88/2', '120/2'];
  for (String score in updates) {
    await Future.delayed(Duration(milliseconds: 300));
    yield 'Pakistan: $score';
  }
}

Future<void> main() async {
  // 1. await for: read each value as it arrives.
  print('Countdown:');
  await for (int number in countdown(3)) {
    print('  $number');
  }
  print('  Go!');

  // 2. listen(): event-driven style with callbacks.
  print('Live score:');
  cricketScore().listen(
    (update) => print('  $update'),   // runs for every new value
    onDone: () => print('  Innings over.'), // runs at the end
  );

  // Wait so the listener above can finish before main ends.
  await Future.delayed(Duration(seconds: 2));

  // 3. Streams have list-like helpers such as where and map.
  Stream<int> numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
  await for (int even in numbers.where((n) => n.isEven)) {
    print('Even number from stream: $even');
  }
}
