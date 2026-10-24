// main.dart
// Lab Task 1: a digital business card. Nothing changes, so it is Stateless.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: BusinessCardPage(),
  ));
}

class BusinessCardPage extends StatelessWidget {
  const BusinessCardPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.teal, // colour of the whole page
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: const [
            // CircleAvatar: a round picture or icon.
            CircleAvatar(
              radius: 50,
              backgroundColor: Colors.white,
              child: Icon(Icons.person, size: 60, color: Colors.teal),
            ),
            SizedBox(height: 12),
            Text(
              'Bilal Ahmed',
              style: TextStyle(fontSize: 30, color: Colors.white, fontWeight: FontWeight.bold),
            ),
            Text(
              'FLUTTER DEVELOPER',
              style: TextStyle(fontSize: 16, color: Colors.white70, letterSpacing: 2),
            ),
            SizedBox(height: 20),
            // Card + ListTile for each contact line.
            Card(
              margin: EdgeInsets.symmetric(horizontal: 32, vertical: 6),
              child: ListTile(
                leading: Icon(Icons.phone, color: Colors.teal),
                title: Text('+92 300 0000000'),
              ),
            ),
            Card(
              margin: EdgeInsets.symmetric(horizontal: 32, vertical: 6),
              child: ListTile(
                leading: Icon(Icons.email, color: Colors.teal),
                title: Text('bilal@example.com'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
