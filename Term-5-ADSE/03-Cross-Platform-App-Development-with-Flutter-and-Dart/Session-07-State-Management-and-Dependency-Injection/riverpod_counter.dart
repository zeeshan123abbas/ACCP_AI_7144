// riverpod_counter.dart
// Riverpod intro: state lives in a Notifier; widgets read it with ref.

import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

// STEP 1: a Notifier holds the state (here an int) and the methods.
class CounterNotifier extends Notifier<int> {
  @override
  int build() => 0; // starting value

  void increment() => state++; // changing "state" updates listeners
}

// STEP 2: declare the provider as a global variable.
final counterProvider = NotifierProvider<CounterNotifier, int>(CounterNotifier.new);

void main() {
  // STEP 3: ProviderScope stores all providers. It must wrap the app.
  runApp(const ProviderScope(child: MaterialApp(home: CounterPage())));
}

// STEP 4: ConsumerWidget gives us "ref" to read providers.
class CounterPage extends ConsumerWidget {
  const CounterPage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final int count = ref.watch(counterProvider); // rebuilds on change

    return Scaffold(
      appBar: AppBar(title: const Text('Riverpod Counter')),
      body: Center(child: Text('$count', style: const TextStyle(fontSize: 60))),
      floatingActionButton: FloatingActionButton(
        // .notifier gives us the CounterNotifier object to call methods.
        onPressed: () => ref.read(counterProvider.notifier).increment(),
        child: const Icon(Icons.add),
      ),
    );
  }
}
