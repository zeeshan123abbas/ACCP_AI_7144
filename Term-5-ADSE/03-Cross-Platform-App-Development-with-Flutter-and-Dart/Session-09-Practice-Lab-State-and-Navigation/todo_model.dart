// todo_model.dart
// The shared state of the app. Every screen reads tasks from here.

import 'package:flutter/foundation.dart';

// A single task: a title and whether it is done.
class Task {
  String title;
  bool isDone;

  Task({required this.title, this.isDone = false});
}

// The list of tasks plus the actions we can do on it.
class TodoModel extends ChangeNotifier {
  final List<Task> tasks = [
    Task(title: 'Revise Flutter layouts'),
    Task(title: 'Finish Provider assignment'),
  ];

  // How many tasks are finished (shown on the list screen).
  int get doneCount => tasks.where((task) => task.isDone).length;

  void add(String title) {
    tasks.add(Task(title: title));
    notifyListeners(); // tell screens to rebuild
  }

  void toggle(int index) {
    tasks[index].isDone = !tasks[index].isDone;
    notifyListeners();
  }

  void remove(int index) {
    tasks.removeAt(index);
    notifyListeners();
  }
}
