// table_and_wrap.dart
// Table for a timetable, Wrap for tags that flow onto the next line.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: TableWrapDemo()));
}

class TableWrapDemo extends StatelessWidget {
  const TableWrapDemo({super.key});

  // Small helper that makes one padded table cell.
  Widget cell(String text) {
    return Padding(padding: const EdgeInsets.all(8), child: Text(text));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Table & Wrap')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            Table(
              border: TableBorder.all(color: Colors.grey),
              children: [
                TableRow(children: [cell('Day'), cell('Module'), cell('Time')]),
                TableRow(children: [cell('Mon'), cell('Flutter'), cell('6–8 pm')]),
                TableRow(children: [cell('Wed'), cell('Python'), cell('6–8 pm')]),
              ],
            ),
            const SizedBox(height: 24),
            // Wrap: chips move to a new line when the row is full.
            Wrap(
              spacing: 8,     // horizontal gap
              runSpacing: 8,  // gap between lines
              children: ['Dart', 'Flutter', 'Firebase', 'REST', 'SQLite', 'TFLite', 'ML Kit']
                  .map((tag) => Chip(label: Text(tag)))
                  .toList(),
            ),
          ],
        ),
      ),
    );
  }
}
