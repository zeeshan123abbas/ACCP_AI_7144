// todo_detail_screen.dart
// Screen 3: details of one task, opened with /task/:index.

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

import 'todo_model.dart';

class TodoDetailScreen extends StatelessWidget {
  final int index; // comes from the URL
  const TodoDetailScreen({super.key, required this.index});

  @override
  Widget build(BuildContext context) {
    final TodoModel model = context.watch<TodoModel>();

    // Guard: the index may be wrong if someone types a bad URL.
    if (index < 0 || index >= model.tasks.length) {
      return Scaffold(
        appBar: AppBar(title: const Text('Not found')),
        body: const Center(child: Text('This task does not exist.')),
      );
    }

    final Task task = model.tasks[index];

    return Scaffold(
      appBar: AppBar(title: const Text('Task Details')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(task.title, style: const TextStyle(fontSize: 26, fontWeight: FontWeight.bold)),
            const SizedBox(height: 8),
            Chip(label: Text(task.isDone ? 'Done' : 'Pending')),
            const SizedBox(height: 24),
            SwitchListTile(
              title: const Text('Mark as done'),
              value: task.isDone,
              onChanged: (_) => context.read<TodoModel>().toggle(index),
            ),
            const Spacer(), // pushes the delete button to the bottom
            OutlinedButton.icon(
              icon: const Icon(Icons.delete),
              label: const Text('Delete task'),
              onPressed: () {
                context.read<TodoModel>().remove(index);
                context.pop();
              },
            ),
          ],
        ),
      ),
    );
  }
}
