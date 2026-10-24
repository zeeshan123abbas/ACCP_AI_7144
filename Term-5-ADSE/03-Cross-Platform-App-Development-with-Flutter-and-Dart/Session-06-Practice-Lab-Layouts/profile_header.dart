// profile_header.dart
// Lab Task 4: cover photo + overlapping avatar + a row of stats.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: ProfileHeaderPage()));
}

class ProfileHeaderPage extends StatelessWidget {
  const ProfileHeaderPage({super.key});

  // Helper method: one number with a label under it.
  Widget statBox(String number, String label) {
    return Column(
      children: [
        Text(number, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
        Text(label, style: const TextStyle(color: Colors.grey)),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          // Stack with clipBehavior none so the avatar can hang below the cover.
          Stack(
            clipBehavior: Clip.none,
            alignment: Alignment.center,
            children: [
              Container(height: 160, color: Colors.teal),
              const Positioned(
                bottom: -40, // half of the avatar sits below the cover
                child: CircleAvatar(
                  radius: 45,
                  backgroundColor: Colors.white,
                  child: Icon(Icons.person, size: 50),
                ),
              ),
            ],
          ),
          const SizedBox(height: 50), // room for the hanging avatar
          const Text('Zara Ahmed', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
          const SizedBox(height: 16),
          // The stats row.
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: [
              statBox('24', 'Projects'),
              statBox('1.2k', 'Followers'),
              statBox('180', 'Following'),
            ],
          ),
        ],
      ),
    );
  }
}
