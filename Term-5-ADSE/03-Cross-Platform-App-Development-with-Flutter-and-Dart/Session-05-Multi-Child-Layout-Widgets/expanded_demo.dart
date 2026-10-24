// expanded_demo.dart
// Expanded shares the remaining space. flex sets the ratio.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: ExpandedDemo()));
}

class ExpandedDemo extends StatelessWidget {
  const ExpandedDemo({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Expanded & flex')),
      body: Column(
        children: [
          // flex 2 : 1 : 1  -> red gets half the height, others a quarter each.
          Expanded(flex: 2, child: Container(color: Colors.red, child: const Center(child: Text('flex 2')))),
          Expanded(flex: 1, child: Container(color: Colors.green, child: const Center(child: Text('flex 1')))),
          Expanded(flex: 1, child: Container(color: Colors.blue, child: const Center(child: Text('flex 1')))),

          // A search bar row: TextField takes all space left after the button.
          Padding(
            padding: const EdgeInsets.all(8),
            child: Row(
              children: [
                const Expanded(
                  child: TextField(decoration: InputDecoration(hintText: 'Search courses')),
                ),
                IconButton(onPressed: () {}, icon: const Icon(Icons.search)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
