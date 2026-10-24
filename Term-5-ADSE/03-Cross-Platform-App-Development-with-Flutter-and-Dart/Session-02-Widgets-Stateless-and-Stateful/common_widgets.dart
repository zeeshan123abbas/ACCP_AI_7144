// common_widgets.dart
// A tour of everyday widgets: Text, Icon, Image, buttons, Card and ListTile.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: CommonWidgetsPage()));
}

class CommonWidgetsPage extends StatelessWidget {
  const CommonWidgetsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Common Widgets')),
      // ListView lets the page scroll if it is taller than the screen.
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          // 1. Text with a style
          const Text('Text widget', style: TextStyle(fontSize: 22, color: Colors.blue)),
          const SizedBox(height: 16),

          // 2. Icons
          const Row(
            children: [
              Icon(Icons.favorite, color: Colors.red),
              Icon(Icons.star, color: Colors.amber),
              Icon(Icons.school, color: Colors.green),
            ],
          ),
          const SizedBox(height: 16),

          // 3. Image from the internet (needs internet permission on Android release builds)
          Image.network('https://picsum.photos/400/200', height: 150, fit: BoxFit.cover),
          const SizedBox(height: 16),

          // 4. Three kinds of buttons
          ElevatedButton(onPressed: () {}, child: const Text('ElevatedButton')),
          OutlinedButton(onPressed: () {}, child: const Text('OutlinedButton')),
          TextButton(onPressed: () {}, child: const Text('TextButton')),
          const SizedBox(height: 16),

          // 5. Card + ListTile: a ready-made row with icon, title and subtitle
          const Card(
            child: ListTile(
              leading: Icon(Icons.book),
              title: Text('Flutter Module'),
              subtitle: Text('18 sessions'),
              trailing: Icon(Icons.arrow_forward_ios),
            ),
          ),
        ],
      ),
    );
  }
}
