// lib/task_store.dart
// Saves and loads tasks from a JSON file using async file operations.

import 'dart:convert';
import 'dart:io';

import 'task.dart';

class TaskStore {
  final File file;

  TaskStore(String path) : file = File(path);

  // Read tasks from the file. Returns an empty list if there is no file yet.
  Future<List<Task>> load() async {
    if (!await file.exists()) {
      return [];
    }
    try {
      String text = await file.readAsString();
      List<dynamic> data = jsonDecode(text);
      return data.map((item) => Task.fromJson(item)).toList();
    } on FormatException {
      // The file is broken (not valid JSON). Start fresh instead of crashing.
      print('Warning: could not read ${file.path}. Starting with no tasks.');
      return [];
    }
  }

  // Write all tasks to the file as pretty JSON.
  Future<void> save(List<Task> tasks) async {
    List<Map<String, dynamic>> data = tasks.map((task) => task.toJson()).toList();
    String text = JsonEncoder.withIndent('  ').convert(data);
    await file.writeAsString(text);
  }
}
