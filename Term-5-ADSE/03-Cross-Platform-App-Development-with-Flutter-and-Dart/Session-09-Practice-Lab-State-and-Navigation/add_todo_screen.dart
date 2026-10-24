// add_todo_screen.dart
// Screen 2: a form with a TextEditingController to add a new task.

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

import 'todo_model.dart';

class AddTodoScreen extends StatefulWidget {
  const AddTodoScreen({super.key});

  @override
  State<AddTodoScreen> createState() => _AddTodoScreenState();
}

class _AddTodoScreenState extends State<AddTodoScreen> {
  final TextEditingController titleController = TextEditingController();
  String? errorText; // shown under the field when input is invalid

  @override
  void dispose() {
    titleController.dispose();
    super.dispose();
  }

  void save() {
    final String title = titleController.text.trim(); // remove extra spaces

    // Simple validation: the title must not be empty.
    if (title.isEmpty) {
      setState(() => errorText = 'Please type a task');
      return;
    }

    context.read<TodoModel>().add(title); // update shared state
    context.pop();                        // go back to the list
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Add Task')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            TextField(
              controller: titleController,
              autofocus: true, // open the keyboard straight away
              decoration: InputDecoration(
                labelText: 'Task title',
                border: const OutlineInputBorder(),
                errorText: errorText,
              ),
              onSubmitted: (_) => save(), // pressing Enter also saves
            ),
            const SizedBox(height: 16),
            FilledButton(onPressed: save, child: const Text('Save')),
          ],
        ),
      ),
    );
  }
}
