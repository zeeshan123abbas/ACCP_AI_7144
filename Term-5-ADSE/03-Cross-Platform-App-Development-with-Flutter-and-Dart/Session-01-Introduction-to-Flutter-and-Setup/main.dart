// main.dart
// The smallest possible Flutter app: one line of text in the centre.

// Import the Material library. It gives us all the basic widgets.
import 'package:flutter/material.dart';

// main() is where every Dart program starts.
void main() {
  // runApp() takes a widget and makes it the root of the screen.
  runApp(
    // Center puts its child in the middle of the screen.
    const Center(
      child: Text(
        'Hello, Flutter!',
        // textDirection is needed only because we have no MaterialApp yet.
        textDirection: TextDirection.ltr,
      ),
    ),
  );
}
