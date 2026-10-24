// decorated_box.dart
// BoxDecoration: rounded corners, border, shadow and gradient.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: DecoratedBoxDemo()));
}

class DecoratedBoxDemo extends StatelessWidget {
  const DecoratedBoxDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('BoxDecoration')),
      body: Center(
        child: Container(
          width: 280,
          padding: const EdgeInsets.all(20),
          // NOTE: colour goes INSIDE decoration, not as color: on Container.
          decoration: BoxDecoration(
            // Gradient: smooth change from one colour to another.
            gradient: const LinearGradient(
              colors: [Colors.purple, Colors.blue],
            ),
            borderRadius: BorderRadius.circular(20),          // rounded corners
            border: Border.all(color: Colors.white, width: 3), // white border
            boxShadow: const [
              BoxShadow(color: Colors.black26, blurRadius: 12, offset: Offset(0, 6)),
            ],
          ),
          child: const Text(
            'Fee Voucher\nRs. 12,500\nDue: 10th of month',
            style: TextStyle(color: Colors.white, fontSize: 18),
          ),
        ),
      ),
    );
  }
}
