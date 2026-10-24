// hot_reload_demo.dart
// Run this app, then change the values marked "CHANGE ME" and press r (hot reload).

import 'package:flutter/material.dart';

void main() {
  runApp(const HotReloadDemo());
}

class HotReloadDemo extends StatelessWidget {
  const HotReloadDemo({super.key});

  @override
  Widget build(BuildContext context) {
    // CHANGE ME: try 'Karachi', 'Lahore' or your own city.
    const String city = 'Karachi';

    // CHANGE ME: try Colors.orange or Colors.purple.
    const Color boxColor = Colors.indigo;

    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Hot Reload Demo')),
        body: Center(
          // Container draws a coloured box around its child.
          child: Container(
            padding: const EdgeInsets.all(24),
            color: boxColor,
            child: const Text(
              'I am learning Flutter in $city',
              style: TextStyle(color: Colors.white, fontSize: 20),
            ),
          ),
        ),
      ),
    );
  }
}
