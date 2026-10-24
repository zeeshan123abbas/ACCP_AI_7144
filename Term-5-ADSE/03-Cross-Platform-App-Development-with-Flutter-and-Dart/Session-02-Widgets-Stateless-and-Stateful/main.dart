// main.dart
// A StatelessWidget: shows fixed information that never changes.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(
    debugShowCheckedModeBanner: false,
    home: ProfilePage(),
  ));
}

// StatelessWidget = no changing data inside.
class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Student Profile')),
      body: Center(
        // Column places its children one below another.
        child: Column(
          mainAxisSize: MainAxisSize.min, // take only the space needed
          children: const [
            // Icon shows a Material icon.
            Icon(Icons.account_circle, size: 100, color: Colors.teal),
            SizedBox(height: 12), // empty gap of 12 pixels
            Text(
              'Ayesha Khan',
              style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
            ),
            Text('ACCP AI · Batch 2501'),
          ],
        ),
      ),
    );
  }
}
