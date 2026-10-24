// Session 11 - Example 2: Notes app that saves to SQLite (works offline)
// Files needed in lib/: main.dart + note_database.dart
import 'package:flutter/material.dart';
import 'note_database.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: NotesPage()));
}

class NotesPage extends StatefulWidget {
  const NotesPage({super.key});

  @override
  State<NotesPage> createState() => _NotesPageState();
}

class _NotesPageState extends State<NotesPage> {
  final titleController = TextEditingController();
  List<Map<String, dynamic>> notes = [];

  @override
  void initState() {
    super.initState();
    loadNotes(); // read saved notes when the screen opens
  }

  // Read from the database, then refresh the screen.
  Future<void> loadNotes() async {
    final data = await NoteDatabase.getNotes();
    setState(() {
      notes = data;
    });
  }

  Future<void> saveNote() async {
    final text = titleController.text.trim();
    if (text.isEmpty) return;          // ignore empty input
    await NoteDatabase.addNote(text);  // wait until it is saved
    titleController.clear();
    await loadNotes();                 // show the new list
  }

  Future<void> removeNote(int id) async {
    await NoteDatabase.deleteNote(id);
    await loadNotes();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('My Notes (SQLite)')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: titleController,
                    decoration: const InputDecoration(labelText: 'New note'),
                  ),
                ),
                IconButton(icon: const Icon(Icons.add), onPressed: saveNote),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: notes.length,
              itemBuilder: (context, index) {
                final note = notes[index];
                return ListTile(
                  title: Text(note['title']),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    onPressed: () => removeNote(note['id']),
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
