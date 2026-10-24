// main.dart
// Lifting state up: the parent owns the score; two child widgets share it.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: ScorePage()));
}

// Parent: holds the state.
class ScorePage extends StatefulWidget {
  const ScorePage({super.key});

  @override
  State<ScorePage> createState() => _ScorePageState();
}

class _ScorePageState extends State<ScorePage> {
  int score = 0;

  void addPoint() {
    setState(() {
      score++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Lifting State Up')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ScoreDisplay(score: score),     // pass the value DOWN
            AddPointButton(onAdd: addPoint), // pass a callback DOWN
          ],
        ),
      ),
    );
  }
}

// Child 1: only shows the score (stateless).
class ScoreDisplay extends StatelessWidget {
  final int score;
  const ScoreDisplay({super.key, required this.score});

  @override
  Widget build(BuildContext context) {
    return Text('Score: $score', style: const TextStyle(fontSize: 40));
  }
}

// Child 2: only has a button; it calls the parent's function.
class AddPointButton extends StatelessWidget {
  final VoidCallback onAdd; // VoidCallback = a function with no inputs/outputs
  const AddPointButton({super.key, required this.onAdd});

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(onPressed: onAdd, child: const Text('+1 Point'));
  }
}
