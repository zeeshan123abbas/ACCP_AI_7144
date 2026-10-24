// light_switch.dart
// Lab Task 3: a Switch turns a light bulb on and off.

import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(home: LightSwitchPage()));
}

class LightSwitchPage extends StatefulWidget {
  const LightSwitchPage({super.key});

  @override
  State<LightSwitchPage> createState() => _LightSwitchPageState();
}

class _LightSwitchPageState extends State<LightSwitchPage> {
  bool isOn = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Page colour depends on the state.
      backgroundColor: isOn ? Colors.yellow.shade100 : Colors.grey.shade800,
      body: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              isOn ? Icons.lightbulb : Icons.lightbulb_outline,
              size: 120,
              color: isOn ? Colors.amber : Colors.white,
            ),
            // Switch gives us the new value in onChanged.
            Switch(
              value: isOn,
              onChanged: (newValue) {
                setState(() {
                  isOn = newValue;
                });
              },
            ),
          ],
        ),
      ),
    );
  }
}
