// Session 12 - Step 1: The Task model (one row of the "tasks" table)
class Task {
  final int? id;      // null until the database gives it an id
  final String title;
  final bool isDone;

  Task({this.id, required this.title, this.isDone = false});

  // Object -> Map, so sqflite can save it. SQLite has no bool, so we use 1/0.
  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'title': title,
      'isDone': isDone ? 1 : 0,
    };
  }

  // Map -> Object, when we read a row back.
  factory Task.fromMap(Map<String, dynamic> map) {
    return Task(
      id: map['id'] as int,
      title: map['title'] as String,
      isDone: map['isDone'] == 1,
    );
  }
}
