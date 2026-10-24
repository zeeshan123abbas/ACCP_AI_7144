// Session 12 - Step 2: All database work in one place (CRUD)
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';
import 'task.dart';

class TaskDatabase {
  static Database? _db;

  static Future<Database> _open() async {
    if (_db != null) return _db!;
    _db = await openDatabase(
      join(await getDatabasesPath(), 'study_tasks.db'),
      version: 1,
      onCreate: (db, version) => db.execute(
        'CREATE TABLE tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'title TEXT NOT NULL, isDone INTEGER NOT NULL)',
      ),
    );
    return _db!;
  }

  // CREATE
  static Future<void> insert(Task task) async {
    final db = await _open();
    final data = task.toMap()..remove('id'); // let SQLite choose the id
    await db.insert('tasks', data);
  }

  // READ
  static Future<List<Task>> getAll() async {
    final db = await _open();
    final rows = await db.query('tasks', orderBy: 'id DESC');
    return rows.map((row) => Task.fromMap(row)).toList();
  }

  // UPDATE
  static Future<void> update(Task task) async {
    final db = await _open();
    await db.update('tasks', task.toMap(), where: 'id = ?', whereArgs: [task.id]);
  }

  // DELETE
  static Future<void> delete(int id) async {
    final db = await _open();
    await db.delete('tasks', where: 'id = ?', whereArgs: [id]);
  }
}
