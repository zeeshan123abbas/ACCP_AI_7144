// greeting_input.dart
// Lab Task 4: type your name and see a greeting update while you type.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: GreetingPage()));
}

class GreetingPage extends StatefulWidget {
  const GreetingPage({super.key});

  @override
  State<GreetingPage> createState() => _GreetingPageState();
}

class _GreetingPageState extends State<GreetingPage> {
  String name = '';

  @override
  Widget build(BuildContext context) {
    // If nothing is typed yet, show a default word.
    String shownName = name.isEmpty ? 'Guest' : name;

    return Scaffold(
      appBar: AppBar(title: const Text('Greeting')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              decoration: const InputDecoration(
                labelText: 'Your name',
                border: OutlineInputBorder(),
              ),
              // onChanged runs on every key press.
              onChanged: (text) {
                setState(() {
                  name = text;
                });
              },
            ),
            const SizedBox(height: 24),
            Text('Welcome, $shownName!', style: const TextStyle(fontSize: 24)),
          ],
        ),
      ),
    );
  }
}
