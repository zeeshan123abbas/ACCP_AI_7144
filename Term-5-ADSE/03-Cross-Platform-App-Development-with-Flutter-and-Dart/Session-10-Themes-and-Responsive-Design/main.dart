// Session 10 - Example 1: Light / dark theme with a toggle switch
// Run: copy into lib/main.dart of a new Flutter project, then `flutter run`.
import 'package:flutter/material.dart';

void main() {
  runApp(const ThemeDemoApp());
}

// StatefulWidget because the chosen theme mode can change.
class ThemeDemoApp extends StatefulWidget {
  const ThemeDemoApp({super.key});

  @override
  State<ThemeDemoApp> createState() => _ThemeDemoAppState();
}

class _ThemeDemoAppState extends State<ThemeDemoApp> {
  // Step 1: remember whether dark mode is on.
  bool isDarkMode = false;

  // Step 2: a function that flips the value and rebuilds the app.
  void toggleTheme(bool value) {
    setState(() {
      isDarkMode = value;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Theme Demo',
      debugShowCheckedModeBanner: false,

      // Step 3: light theme built from ONE seed colour.
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
        useMaterial3: true,
      ),

      // Step 4: dark theme from the same seed colour.
      darkTheme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.teal,
          brightness: Brightness.dark,
        ),
        useMaterial3: true,
      ),

      // Step 5: choose which theme is active right now.
      themeMode: isDarkMode ? ThemeMode.dark : ThemeMode.light,

      home: HomePage(isDarkMode: isDarkMode, onToggle: toggleTheme),
    );
  }
}

class HomePage extends StatelessWidget {
  final bool isDarkMode;
  final ValueChanged<bool> onToggle;

  const HomePage({super.key, required this.isDarkMode, required this.onToggle});

  @override
  Widget build(BuildContext context) {
    // Read colours and text styles from the current theme.
    final colors = Theme.of(context).colorScheme;
    final textStyles = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Themes in Flutter'),
        backgroundColor: colors.primaryContainer,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Hello, students!', style: textStyles.headlineMedium),
            const SizedBox(height: 8),
            Text('All colours on this screen come from the theme.',
                style: textStyles.bodyLarge),
            const SizedBox(height: 16),
            // The switch calls onToggle, which changes the whole app theme.
            SwitchListTile(
              title: const Text('Dark mode'),
              value: isDarkMode,
              onChanged: onToggle,
            ),
            const SizedBox(height: 16),
            ElevatedButton(onPressed: () {}, child: const Text('Themed button')),
          ],
        ),
      ),
    );
  }
}
