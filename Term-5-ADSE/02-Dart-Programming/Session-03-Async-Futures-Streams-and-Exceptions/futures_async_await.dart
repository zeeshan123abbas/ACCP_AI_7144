// futures_async_await.dart
// A Future is a value that will be ready LATER (like an order token at a cafe).

// This function pretends to download a result from a server.
// It returns Future<String>: "a String will arrive in the future".
Future<String> fetchResult(String rollNumber) {
  return Future.delayed(Duration(seconds: 2), () {
    return 'Result for $rollNumber: Passed with 82%';
  });
}

// async + await: write asynchronous code that reads like normal code.
Future<void> showResult() async {
  print('Fetching result... please wait');

  // await pauses THIS function until the Future finishes.
  String result = await fetchResult('STU-1024');

  print(result);
}

Future<int> countDownloads() async {
  await Future.delayed(Duration(seconds: 1));
  return 350;
}

Future<void> main() async {
  print('1. Program started');

  // The old style: then() runs when the Future completes.
  fetchResult('STU-0001').then((value) {
    print('(then) $value');
  });

  // The modern style: async / await.
  await showResult();

  // Run two Futures at the same time and wait for both.
  List<Object> both = await Future.wait([
    fetchResult('STU-2000'),
    countDownloads(),
  ]);
  print('Both finished: ${both[0]} | downloads: ${both[1]}');

  print('2. Program finished');
}
