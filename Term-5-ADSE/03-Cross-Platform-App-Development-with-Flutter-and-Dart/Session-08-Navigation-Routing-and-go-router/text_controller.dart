// text_controller.dart
// TextEditingController: read, set and clear the text of a TextField.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: NotePage()));
}

class NotePage extends StatefulWidget {
  const NotePage({super.key});

  @override
  State<NotePage> createState() => _NotePageState();
}

class _NotePageState extends State<NotePage> {
  // STEP 1: create the controller once.
  final TextEditingController nameController = TextEditingController();
  String savedName = '';

  @override
  void dispose() {
    // STEP 4: always dispose controllers to free memory.
    nameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('TextEditingController')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // STEP 2: connect the controller to the TextField.
            TextField(
              controller: nameController,
              decoration: const InputDecoration(labelText: 'Student name', border: OutlineInputBorder()),
            ),
            const SizedBox(height: 12),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                // STEP 3: read the text with controller.text
                ElevatedButton(
                  onPressed: () => setState(() => savedName = nameController.text),
                  child: const Text('Save'),
                ),
                // Set the text from code.
                ElevatedButton(
                  onPressed: () => nameController.text = 'Ali Khan',
                  child: const Text('Fill sample'),
                ),
                // Clear the field.
                ElevatedButton(
                  onPressed: () => nameController.clear(),
                  child: const Text('Clear'),
                ),
              ],
            ),
            const SizedBox(height: 24),
            Text('Saved: $savedName', style: const TextStyle(fontSize: 20)),
          ],
        ),
      ),
    );
  }
}
