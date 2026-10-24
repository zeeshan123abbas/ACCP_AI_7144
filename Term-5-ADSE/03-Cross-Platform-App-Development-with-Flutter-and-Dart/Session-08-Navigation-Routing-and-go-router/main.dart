// main.dart
// Navigator: push a details screen, send data forward, get a result back.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: HomePage()));
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String message = 'No rating yet';

  // async because we WAIT for the details screen to return a value.
  Future<void> openDetails() async {
    final String? rating = await Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => const DetailsPage(courseName: 'Flutter'), // data forward
      ),
    );

    // rating is null if the user pressed the back arrow instead.
    if (rating != null) {
      setState(() {
        message = 'You rated the course: $rating';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(message, style: const TextStyle(fontSize: 18)),
            const SizedBox(height: 16),
            ElevatedButton(onPressed: openDetails, child: const Text('Open Flutter course')),
          ],
        ),
      ),
    );
  }
}

class DetailsPage extends StatelessWidget {
  final String courseName; // received from the Home page
  const DetailsPage({super.key, required this.courseName});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(courseName)), // back arrow added automatically
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text('How was $courseName?', style: const TextStyle(fontSize: 22)),
            // pop with a value sends it back to the Home page.
            TextButton(onPressed: () => Navigator.pop(context, 'Excellent'), child: const Text('Excellent')),
            TextButton(onPressed: () => Navigator.pop(context, 'Good'), child: const Text('Good')),
          ],
        ),
      ),
    );
  }
}
