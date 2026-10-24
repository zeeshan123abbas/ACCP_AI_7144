// alignment_grid.dart
// Move a ball around a box using Alignment(x, y). Tap the button to change position.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: AlignmentGrid()));
}

class AlignmentGrid extends StatefulWidget {
  const AlignmentGrid({super.key});

  @override
  State<AlignmentGrid> createState() => _AlignmentGridState();
}

class _AlignmentGridState extends State<AlignmentGrid> {
  // A list of positions to visit, one after another.
  final List<Alignment> positions = const [
    Alignment.topLeft,      // (-1, -1)
    Alignment.topRight,     // ( 1, -1)
    Alignment.center,       // ( 0,  0)
    Alignment.bottomLeft,   // (-1,  1)
    Alignment(0.5, 0.8),    // a custom position
  ];
  int index = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Alignment: ${positions[index]}')),
      body: Container(
        margin: const EdgeInsets.all(20),
        height: 300,
        color: Colors.green.shade100,
        child: Align(
          alignment: positions[index],
          child: const Icon(Icons.sports_cricket, size: 48),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            // Go to the next position; % wraps back to 0 at the end.
            index = (index + 1) % positions.length;
          });
        },
        child: const Icon(Icons.navigate_next),
      ),
    );
  }
}
