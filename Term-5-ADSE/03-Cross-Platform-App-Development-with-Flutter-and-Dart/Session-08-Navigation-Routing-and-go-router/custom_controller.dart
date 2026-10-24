// custom_controller.dart
// A custom controller: our own class that holds a value and notifies listeners.

import 'package:flutter/material.dart';

// ValueNotifier<int> already knows how to store a value and notify listeners.
// We just add our own easy-to-read methods.
class StepController extends ValueNotifier<int> {
  StepController() : super(1); // start at step 1

  final int maxStep = 3;

  void next() {
    if (value < maxStep) value++; // changing value notifies listeners
  }

  void back() {
    if (value > 1) value--;
  }
}

void main() {
  runApp(const MaterialApp(home: StepperPage()));
}

class StepperPage extends StatefulWidget {
  const StepperPage({super.key});

  @override
  State<StepperPage> createState() => _StepperPageState();
}

class _StepperPageState extends State<StepperPage> {
  final StepController controller = StepController();

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Admission Form Steps')),
      body: Center(
        // ValueListenableBuilder rebuilds only this part when the value changes.
        child: ValueListenableBuilder<int>(
          valueListenable: controller,
          builder: (context, step, child) {
            return Text('Step $step of ${controller.maxStep}', style: const TextStyle(fontSize: 28));
          },
        ),
      ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            OutlinedButton(onPressed: controller.back, child: const Text('Back')),
            FilledButton(onPressed: controller.next, child: const Text('Next')),
          ],
        ),
      ),
    );
  }
}
