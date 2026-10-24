// stack_demo.dart
// Stack puts widgets on top of each other. Positioned pins them.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: StackDemo()));
}

class StackDemo extends StatelessWidget {
  const StackDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Stack')),
      body: Center(
        child: Stack(
          children: [
            // Layer 1 (bottom): a big coloured box like a banner image.
            Container(width: 300, height: 180, color: Colors.indigo),

            // Layer 2: text pinned to the bottom-left corner.
            const Positioned(
              left: 16,
              bottom: 16,
              child: Text('Flutter Bootcamp', style: TextStyle(color: Colors.white, fontSize: 22)),
            ),

            // Layer 3 (top): a "SALE" badge pinned to the top-right corner.
            Positioned(
              top: 10,
              right: 10,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                color: Colors.red,
                child: const Text('50% OFF', style: TextStyle(color: Colors.white)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
