// lib/task.dart
// The data model: one study task.

class Task {
  final String title;
  final String subject;
  bool isDone;

  Task({required this.title, required this.subject, this.isDone = false});

  // Mark the task as finished.
  void complete() {
    isDone = true;
  }

  // Convert a Task into a Map so it can be saved as JSON.
  Map<String, dynamic> toJson() {
    return {'title': title, 'subject': subject, 'isDone': isDone};
  }

  // Named constructor: build a Task back from a JSON Map.
  Task.fromJson(Map<String, dynamic> json)
      : title = json['title'] as String,
        subject = json['subject'] as String,
        isDone = json['isDone'] as bool;

  // How a task looks when printed, e.g. "[x] Revise OOP (Dart)".
  @override
  String toString() {
    String box = isDone ? '[x]' : '[ ]';
    return '$box $title ($subject)';
  }
}
