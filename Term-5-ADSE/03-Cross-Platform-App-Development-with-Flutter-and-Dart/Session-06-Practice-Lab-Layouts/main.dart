// main.dart
// Lab Task 1: a login screen layout (no real login yet, only the UI).

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: LoginPage()));
}

class LoginPage extends StatelessWidget {
  const LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // SingleChildScrollView stops overflow when the keyboard opens.
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch, // full-width children
          children: [
            const SizedBox(height: 60),
            const Icon(Icons.school, size: 80, color: Colors.indigo),
            const Text(
              'Student Portal',
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 32),
            const TextField(
              decoration: InputDecoration(
                labelText: 'Email',
                prefixIcon: Icon(Icons.email),
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 16),
            const TextField(
              obscureText: true, // hide the password with dots
              decoration: InputDecoration(
                labelText: 'Password',
                prefixIcon: Icon(Icons.lock),
                border: OutlineInputBorder(),
              ),
            ),
            // "Forgot password?" aligned to the right.
            Align(
              alignment: Alignment.centerRight,
              child: TextButton(onPressed: () {}, child: const Text('Forgot password?')),
            ),
            SizedBox(
              height: 50,
              child: FilledButton(onPressed: () {}, child: const Text('Login')),
            ),
            const SizedBox(height: 16),
            // Row centred: text + link button.
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text("Don't have an account?"),
                TextButton(onPressed: () {}, child: const Text('Sign up')),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
