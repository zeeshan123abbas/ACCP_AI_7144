// lib/planner.dart
// Business logic: works with a list of tasks. No input/output here,
// which makes this class easy to test.

import 'task.dart';

class Planner {
  final List<Task> tasks;

  Planner(this.tasks);

  void addTask(String title, String subject) {
    tasks.add(Task(title: title, subject: subject));
  }

  // Completes the task at a 1-based position. Returns false if invalid.
  bool completeTask(int number) {
    int index = number - 1;
    if (index < 0 || index >= tasks.length) {
      return false;
    }
    tasks[index].complete();
    return true;
  }

  List<Task> get pendingTasks => tasks.where((task) => !task.isDone).toList();

  // Percentage of tasks finished, from 0 to 100.
  int get progressPercent {
    if (tasks.isEmpty) return 0;
    int done = tasks.length - pendingTasks.length;
    return (done * 100 / tasks.length).round();
  }
}
