// go_router_app.dart
// go_router: URL-style routes, a path parameter, go() vs push().

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

// Our data: a simple list of courses. The index is used as the id.
const List<String> courses = ['Dart', 'Flutter', 'Firebase', 'Machine Learning'];

// STEP 1: describe all routes in one place.
final GoRouter router = GoRouter(
  initialLocation: '/',
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const HomeScreen(),
    ),
    GoRoute(
      path: '/courses',
      builder: (context, state) => const CoursesScreen(),
    ),
    GoRoute(
      // ":id" is a path parameter, e.g. /courses/1
      path: '/courses/:id',
      builder: (context, state) {
        // Read the parameter as text and turn it into a number.
        final int id = int.parse(state.pathParameters['id']!);
        return CourseDetailScreen(id: id);
      },
    ),
  ],
);

void main() {
  // STEP 2: use MaterialApp.router and give it our router.
  runApp(MaterialApp.router(routerConfig: router));
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Center(
        child: FilledButton(
          // go() jumps to /courses (good for main sections / menus).
          onPressed: () => context.go('/courses'),
          child: const Text('View courses'),
        ),
      ),
    );
  }
}

class CoursesScreen extends StatelessWidget {
  const CoursesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Courses')),
      body: ListView.builder(
        itemCount: courses.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(courses[index]),
            // push() adds the detail screen on top, so Back returns here.
            onTap: () => context.push('/courses/$index'),
          );
        },
      ),
    );
  }
}

class CourseDetailScreen extends StatelessWidget {
  final int id;
  const CourseDetailScreen({super.key, required this.id});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(courses[id])),
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text('Course id: $id', style: const TextStyle(fontSize: 22)),
            TextButton(onPressed: () => context.go('/'), child: const Text('Back to Home')),
          ],
        ),
      ),
    );
  }
}
