// main.dart
// Connects the shared state (Provider) and the screens (go_router).

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';

import 'todo_model.dart';
import 'todo_list_screen.dart';
import 'add_todo_screen.dart';
import 'todo_detail_screen.dart';

// All routes of the app in one place.
final GoRouter router = GoRouter(
  routes: [
    GoRoute(path: '/', builder: (context, state) => const TodoListScreen()),
    GoRoute(path: '/add', builder: (context, state) => const AddTodoScreen()),
    GoRoute(
      path: '/task/:index',
      builder: (context, state) {
        final int index = int.parse(state.pathParameters['index']!);
        return TodoDetailScreen(index: index);
      },
    ),
  ],
);

void main() {
  runApp(
    // The model is placed ABOVE the app, so every screen can use it.
    ChangeNotifierProvider(
      create: (context) => TodoModel(),
      child: MaterialApp.router(
        title: 'Study To-Do',
        debugShowCheckedModeBanner: false,
        theme: ThemeData(colorSchemeSeed: Colors.indigo), // Material 3 colours
        routerConfig: router,
      ),
    ),
  );
}
