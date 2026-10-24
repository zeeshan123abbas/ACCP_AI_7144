// bin/study_planner.dart
// The console user interface. Run from the study_planner folder:
//   dart pub get
//   dart run

import 'dart:io';

import 'package:study_planner/planner.dart';
import 'package:study_planner/task_store.dart';

Future<void> main() async {
  // Step 1: load saved tasks (async) and create the planner.
  TaskStore store = TaskStore('tasks.json');
  Planner planner = Planner(await store.load());

  print('=== Study Planner ===');

  // Step 2: show the menu again and again until the user quits.
  while (true) {
    print('\n1) Show tasks  2) Add task  3) Complete task  4) Save & quit');
    stdout.write('Choose an option: ');
    String? choice = stdin.readLineSync(); // null if input ends

    switch (choice) {
      case '1':
        showTasks(planner);
      case '2':
        String title = ask('Task title: ');
        String subject = ask('Subject: ');
        if (title.isEmpty) {
          print('Title cannot be empty.');
        } else {
          planner.addTask(title, subject.isEmpty ? 'General' : subject);
          print('Task added.');
        }
      case '3':
        showTasks(planner);
        int? number = int.tryParse(ask('Task number to complete: '));
        if (number != null && planner.completeTask(number)) {
          print('Well done!');
        } else {
          print('Invalid task number.');
        }
      case '4' || null:
        await store.save(planner.tasks); // Step 3: save before leaving
        print('Saved ${planner.tasks.length} tasks. Allah Hafiz!');
        return;
      default:
        print('Please type 1, 2, 3 or 4.');
    }
  }
}

// Prints every task with its number and the overall progress.
void showTasks(Planner planner) {
  if (planner.tasks.isEmpty) {
    print('No tasks yet. Add one!');
    return;
  }
  for (int i = 0; i < planner.tasks.length; i++) {
    print('${i + 1}. ${planner.tasks[i]}');
  }
  print('Progress: ${planner.progressPercent}% done');
}

// Shows a prompt and returns what the user typed (never null).
String ask(String prompt) {
  stdout.write(prompt);
  return (stdin.readLineSync() ?? '').trim();
}
