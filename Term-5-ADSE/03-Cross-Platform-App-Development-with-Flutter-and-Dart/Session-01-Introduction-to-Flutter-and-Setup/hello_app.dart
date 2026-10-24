// hello_app.dart
// A real app structure: MaterialApp -> Scaffold -> AppBar + body.

import 'package:flutter/material.dart';

void main() {
  runApp(const HelloApp());
}

// Our app is itself a widget.
class HelloApp extends StatelessWidget {
  const HelloApp({super.key});

  @override
  Widget build(BuildContext context) {
    // MaterialApp sets up theme, text direction and navigation.
    return MaterialApp(
      title: 'Hello App',
      debugShowCheckedModeBanner: false, // hide the red "DEBUG" ribbon
      home: Scaffold(
        // AppBar is the bar at the top of the screen.
        appBar: AppBar(
          title: const Text('My First Flutter App'),
          backgroundColor: Colors.teal,
          foregroundColor: Colors.white,
        ),
        // body is the main area of the page.
        body: const Center(
          child: Text(
            'Assalam-o-Alaikum, Students!',
            style: TextStyle(fontSize: 24),
          ),
        ),
      ),
    );
  }
}
