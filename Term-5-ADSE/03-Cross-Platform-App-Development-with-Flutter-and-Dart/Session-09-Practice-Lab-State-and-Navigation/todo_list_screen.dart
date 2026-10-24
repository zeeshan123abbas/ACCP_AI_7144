// todo_list_screen.dart
// Screen 1: shows all tasks. Tap to open, tick to finish.

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

import 'todo_model.dart';

class TodoListScreen extends StatelessWidget {
  const TodoListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    // watch: rebuild this screen whenever the tasks change.
    final TodoModel model = context.watch<TodoModel>();

    return Scaffold(
      appBar: AppBar(
        title: Text('Tasks (${model.doneCount}/${model.tasks.length} done)'),
      ),
      // Show a friendly message when the list is empty.
      body: model.tasks.isEmpty
          ? const Center(child: Text('No tasks. Tap + to add one.'))
          : ListView.builder(
              itemCount: model.tasks.length,
              itemBuilder: (context, index) {
                final Task task = model.tasks[index];
                return ListTile(
                  leading: Checkbox(
                    value: task.isDone,
                    onChanged: (_) => context.read<TodoModel>().toggle(index),
                  ),
                  title: Text(
                    task.title,
                    // Strike through finished tasks.
                    style: TextStyle(
                      decoration: task.isDone ? TextDecoration.lineThrough : null,
                    ),
                  ),
                  trailing: const Icon(Icons.chevron_right),
                  onTap: () => context.push('/task/$index'),
                );
              },
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => context.push('/add'),
        child: const Icon(Icons.add),
      ),
    );
  }
}
