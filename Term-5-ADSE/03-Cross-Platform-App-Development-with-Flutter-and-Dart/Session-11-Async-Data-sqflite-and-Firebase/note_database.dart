// Session 11 - Example 1: A tiny helper class for a local SQLite database
import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class NoteDatabase {
  // We keep one open database and reuse it.
  static Database? _database;

  // Step 1: open the database (create it the first time).
  static Future<Database> getDatabase() async {
    if (_database != null) return _database!;

    final folder = await getDatabasesPath();       // where the phone keeps databases
    final filePath = join(folder, 'notes.db');     // e.g. .../databases/notes.db

    _database = await openDatabase(
      filePath,
      version: 1,
      // onCreate runs only once, when the file does not exist yet.
      onCreate: (db, version) {
        return db.execute(
          'CREATE TABLE notes(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT)',
        );
      },
    );
    return _database!;
  }

  // Step 2: INSERT a new note.
  static Future<void> addNote(String title) async {
    final db = await getDatabase();
    await db.insert('notes', {'title': title});
  }

  // Step 3: SELECT all notes (newest first).
  static Future<List<Map<String, dynamic>>> getNotes() async {
    final db = await getDatabase();
    return db.query('notes', orderBy: 'id DESC');
  }

  // Step 4: DELETE one note by its id.
  static Future<void> deleteNote(int id) async {
    final db = await getDatabase();
    await db.delete('notes', where: 'id = ?', whereArgs: [id]);
  }
}
