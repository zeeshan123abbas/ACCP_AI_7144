// align_and_spacing.dart
// Padding, Align, Center and SizedBox in one screen.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: AlignDemo()));
}

class AlignDemo extends StatelessWidget {
  const AlignDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Align & Spacing')),
      // Padding: keep everything 16 px away from the screen edges.
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // Align: put the badge on the right side.
            const Align(
              alignment: Alignment.centerRight,
              child: Chip(label: Text('New')),
            ),

            // SizedBox as an empty gap of 40 px.
            const SizedBox(height: 40),

            // SizedBox to force a full-width button.
            SizedBox(
              width: double.infinity, // as wide as allowed
              height: 50,
              child: ElevatedButton(
                onPressed: () {},
                child: const Text('Full-width button'),
              ),
            ),

            const SizedBox(height: 40),

            // Center inside a fixed-size coloured box.
            Container(
              width: 200,
              height: 120,
              color: Colors.orange.shade200,
              child: const Center(child: Text('Centred text')),
            ),
          ],
        ),
      ),
    );
  }
}
