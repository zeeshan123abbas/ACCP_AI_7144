// main.dart
// Row (horizontal) inside a Column (vertical), with alignment options.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: RowColumnDemo()));
}

class RowColumnDemo extends StatelessWidget {
  const RowColumnDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Row & Column')),
      body: Column(
        // Main axis of a Column is vertical: spread children top to bottom.
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        // Cross axis is horizontal: stretch children to full width.
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // A Row of three icons, spread out evenly.
          Container(
            color: Colors.blue.shade50,
            padding: const EdgeInsets.all(12),
            child: const Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(Icons.home, size: 40),
                Icon(Icons.search, size: 40),
                Icon(Icons.person, size: 40),
              ],
            ),
          ),
          // A Row with icon + text, centred.
          const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.location_on, color: Colors.red),
              SizedBox(width: 8),
              Text('North Nazimabad, Karachi', style: TextStyle(fontSize: 18)),
            ],
          ),
          // A full-width button (because of stretch).
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16),
            child: ElevatedButton(onPressed: () {}, child: const Text('Enrol Now')),
          ),
        ],
      ),
    );
  }
}
