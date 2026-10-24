// gridview_demo.dart
// A 2-column grid of menu tiles, like a dashboard.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: DashboardPage()));
}

class DashboardPage extends StatelessWidget {
  const DashboardPage({super.key});

  @override
  Widget build(BuildContext context) {
    // Each menu item: an icon and a label.
    final List<IconData> icons = [Icons.class_, Icons.assignment, Icons.payments, Icons.event, Icons.chat, Icons.settings];
    final List<String> labels = ['Classes', 'Assignments', 'Fees', 'Events', 'Chat', 'Settings'];

    return Scaffold(
      appBar: AppBar(title: const Text('Student Dashboard')),
      body: GridView.count(
        crossAxisCount: 2,      // 2 columns
        padding: const EdgeInsets.all(12),
        mainAxisSpacing: 12,    // vertical gap
        crossAxisSpacing: 12,   // horizontal gap
        // List.generate makes one Card per item.
        children: List.generate(icons.length, (index) {
          return Card(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(icons[index], size: 48, color: Colors.teal),
                const SizedBox(height: 8),
                Text(labels[index], style: const TextStyle(fontSize: 16)),
              ],
            ),
          );
        }),
      ),
    );
  }
}
