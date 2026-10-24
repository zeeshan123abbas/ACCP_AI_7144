// counter_app.dart
// A StatefulWidget: the number changes every time the button is pressed.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: CounterPage()));
}

// Part 1: the widget itself (it only creates the State object).
class CounterPage extends StatefulWidget {
  const CounterPage({super.key});

  @override
  State<CounterPage> createState() => _CounterPageState();
}

// Part 2: the State class holds the changing data and the build method.
class _CounterPageState extends State<CounterPage> {
  // This is our state: a number that will change.
  int count = 0;

  // Called when the button is pressed.
  void increaseCount() {
    // setState tells Flutter: "data changed, please rebuild".
    setState(() {
      count = count + 1;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Tasbeeh Counter')),
      body: Center(
        child: Text(
          '$count', // shows the current value
          style: const TextStyle(fontSize: 72),
        ),
      ),
      // The round button at the bottom-right.
      floatingActionButton: FloatingActionButton(
        onPressed: increaseCount, // run our function on tap
        child: const Icon(Icons.add),
      ),
    );
  }
}
