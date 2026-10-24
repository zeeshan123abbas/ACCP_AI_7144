// main.dart
// Container: size, colour, padding, margin and alignment.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: ContainerDemo()));
}

class ContainerDemo extends StatelessWidget {
  const ContainerDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Container Basics')),
      body: Container(
        color: Colors.grey.shade300,              // outer grey area (whole body)
        child: Container(
          width: 250,                              // fixed width
          height: 150,                             // fixed height
          margin: const EdgeInsets.all(30),        // space OUTSIDE the blue box
          padding: const EdgeInsets.all(16),       // space INSIDE the blue box
          color: Colors.blue,                      // box colour
          alignment: Alignment.bottomRight,        // child goes bottom-right
          child: const Text(
            'Inside the box',
            style: TextStyle(color: Colors.white),
          ),
        ),
      ),
    );
  }
}
