// listview_builder.dart
// A scrolling list built from a Dart list. Only visible rows are created.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: CourseListPage()));
}

class CourseListPage extends StatelessWidget {
  const CourseListPage({super.key});

  // Our data: a simple list of course names.
  final List<String> courses = const [
    'Agile and DevOps', 'Dart Programming', 'Flutter', 'Python Apps',
    'Machine Learning', 'Deep Learning', 'NLP', 'Computer Vision',
    'Generative AI', 'Cloud Basics', 'Data Science', 'eProject',
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Courses')),
      body: ListView.builder(
        itemCount: courses.length, // how many rows
        // itemBuilder is called for each visible row with its index.
        itemBuilder: (context, index) {
          return ListTile(
            leading: CircleAvatar(child: Text('${index + 1}')),
            title: Text(courses[index]),
            trailing: const Icon(Icons.chevron_right),
          );
        },
      ),
    );
  }
}
