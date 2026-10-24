// bloc_counter.dart
// BLoC intro using a Cubit: the simplest form of BLoC.

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

// STEP 1: a Cubit holds one state value and emits new ones.
class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0); // starting state is 0

  void increment() => emit(state + 1); // emit = publish a new state
  void reset() => emit(0);
}

void main() {
  runApp(
    // STEP 2: BlocProvider creates the Cubit and shares it below.
    BlocProvider(
      create: (context) => CounterCubit(),
      child: const MaterialApp(home: CounterPage()),
    ),
  );
}

class CounterPage extends StatelessWidget {
  const CounterPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Cubit Counter')),
      body: Center(
        // STEP 3: BlocBuilder rebuilds only this part when the state changes.
        child: BlocBuilder<CounterCubit, int>(
          builder: (context, count) {
            return Text('$count', style: const TextStyle(fontSize: 60));
          },
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => context.read<CounterCubit>().increment(),
        child: const Icon(Icons.add),
      ),
    );
  }
}
