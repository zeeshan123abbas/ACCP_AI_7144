// Session 12 - Step 3: Study Tasks app (sqflite + saved dark mode)
// lib/ needs: main.dart, task.dart, task_database.dart
import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'task.dart';
import 'task_database.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // Read the saved theme choice before showing the app.
  final prefs = await SharedPreferences.getInstance();
  final savedDark = prefs.getBool('darkMode') ?? false;
  runApp(StudyTasksApp(startDark: savedDark));
}

class StudyTasksApp extends StatefulWidget {
  final bool startDark;
  const StudyTasksApp({super.key, required this.startDark});

  @override
  State<StudyTasksApp> createState() => _StudyTasksAppState();
}

class _StudyTasksAppState extends State<StudyTasksApp> {
  late bool isDark = widget.startDark;

  Future<void> toggleTheme() async {
    setState(() => isDark = !isDark);
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('darkMode', isDark); // remember for next launch
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(colorSchemeSeed: Colors.indigo),
      darkTheme: ThemeData(colorSchemeSeed: Colors.indigo, brightness: Brightness.dark),
      themeMode: isDark ? ThemeMode.dark : ThemeMode.light,
      home: TasksPage(isDark: isDark, onToggleTheme: toggleTheme),
    );
  }
}

class TasksPage extends StatefulWidget {
  final bool isDark;
  final VoidCallback onToggleTheme;
  const TasksPage({super.key, required this.isDark, required this.onToggleTheme});

  @override
  State<TasksPage> createState() => _TasksPageState();
}

class _TasksPageState extends State<TasksPage> {
  final inputController = TextEditingController();
  List<Task> tasks = [];

  @override
  void initState() {
    super.initState();
    refresh();
  }

  Future<void> refresh() async {
    final all = await TaskDatabase.getAll();
    setState(() => tasks = all);
  }

  Future<void> addTask() async {
    final title = inputController.text.trim();
    if (title.isEmpty) return;
    await TaskDatabase.insert(Task(title: title));
    inputController.clear();
    await refresh();
  }

  Future<void> toggleDone(Task task) async {
    // Make a copy with the opposite isDone value and save it.
    await TaskDatabase.update(Task(id: task.id, title: task.title, isDone: !task.isDone));
    await refresh();
  }

  Future<void> deleteTask(Task task) async {
    await TaskDatabase.delete(task.id!);
    await refresh();
  }

  @override
  Widget build(BuildContext context) {
    final doneCount = tasks.where((t) => t.isDone).length;

    return Scaffold(
      appBar: AppBar(
        title: Text('Study Tasks ($doneCount/${tasks.length} done)'),
        actions: [
          IconButton(
            icon: Icon(widget.isDark ? Icons.light_mode : Icons.dark_mode),
            onPressed: widget.onToggleTheme,
          ),
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(12),
            child: TextField(
              controller: inputController,
              decoration: const InputDecoration(
                labelText: 'What will you study?',
                border: OutlineInputBorder(),
              ),
              onSubmitted: (_) => addTask(), // press Enter to add
            ),
          ),
          Expanded(
            child: tasks.isEmpty
                ? const Center(child: Text('No tasks yet. Add one above!'))
                : ListView.builder(
                    itemCount: tasks.length,
                    itemBuilder: (context, index) {
                      final task = tasks[index];
                      return CheckboxListTile(
                        value: task.isDone,
                        onChanged: (_) => toggleDone(task),
                        title: Text(
                          task.title,
                          style: TextStyle(
                            decoration: task.isDone ? TextDecoration.lineThrough : null,
                          ),
                        ),
                        secondary: IconButton(
                          icon: const Icon(Icons.delete_outline),
                          onPressed: () => deleteTask(task),
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
