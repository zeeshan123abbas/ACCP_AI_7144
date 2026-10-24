// Tests for the Task and Planner classes. Run with:  dart test
import 'package:study_planner/planner.dart';
import 'package:study_planner/task.dart';
import 'package:test/test.dart';

void main() {
  test('a new task is not done', () {
    Task task = Task(title: 'Revise OOP', subject: 'Dart');
    expect(task.isDone, isFalse);
  });

  test('task survives a JSON round trip', () {
    Task original = Task(title: 'Read streams', subject: 'Dart', isDone: true);
    Task copy = Task.fromJson(original.toJson());
    expect(copy.title, equals('Read streams'));
    expect(copy.isDone, isTrue);
  });

  test('completeTask marks the right task and updates progress', () {
    Planner planner = Planner([]);
    planner.addTask('Task A', 'Dart');
    planner.addTask('Task B', 'Flutter');

    bool ok = planner.completeTask(1);

    expect(ok, isTrue);
    expect(planner.pendingTasks.length, equals(1));
    expect(planner.progressPercent, equals(50));
  });

  test('completeTask rejects an invalid number', () {
    Planner planner = Planner([]);
    expect(planner.completeTask(5), isFalse);
  });
}
