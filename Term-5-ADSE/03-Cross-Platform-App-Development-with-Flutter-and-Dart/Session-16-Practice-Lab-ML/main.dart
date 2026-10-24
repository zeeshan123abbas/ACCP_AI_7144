// Session 16 - Step 2: "Fruit Checker" app using your own trained model
// lib/ needs: main.dart + custom_classifier.dart
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'custom_classifier.dart';

void main() {
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    theme: ThemeData(colorSchemeSeed: Colors.green),
    home: const FruitCheckerPage(),
  ));
}

class FruitCheckerPage extends StatefulWidget {
  const FruitCheckerPage({super.key});

  @override
  State<FruitCheckerPage> createState() => _FruitCheckerPageState();
}

class _FruitCheckerPageState extends State<FruitCheckerPage> {
  final classifier = CustomClassifier();
  final picker = ImagePicker();

  bool isReady = false;
  bool isBusy = false;
  File? photo;
  Prediction? latest;
  final List<Prediction> history = []; // last results, newest first

  // Results below this confidence are shown as "Not sure".
  static const double minConfidence = 0.70;

  @override
  void initState() {
    super.initState();
    classifier.load().then((_) {
      if (mounted) setState(() => isReady = true);
    });
  }

  @override
  void dispose() {
    classifier.close();
    super.dispose();
  }

  Future<void> check(ImageSource source) async {
    final picked = await picker.pickImage(source: source, maxWidth: 800);
    if (picked == null) return;

    setState(() => isBusy = true);
    final file = File(picked.path);
    final result = await classifier.classify(file);
    if (!mounted) return;

    setState(() {
      photo = file;
      latest = result;
      history.insert(0, result);
      if (history.length > 5) history.removeLast(); // keep only 5
      isBusy = false;
    });
  }

  // Friendly text for a prediction.
  String describe(Prediction p) {
    final percent = (p.confidence * 100).toStringAsFixed(0);
    if (p.confidence < minConfidence) return 'Not sure ($percent%)';
    return '${p.label} ($percent%)';
  }

  @override
  Widget build(BuildContext context) {
    if (!isReady) {
      return const Scaffold(body: Center(child: CircularProgressIndicator()));
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Fruit Checker')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          AspectRatio(
            aspectRatio: 1,
            child: photo == null
                ? const Card(child: Center(child: Text('Take a photo of a fruit')))
                : Image.file(photo!, fit: BoxFit.cover),
          ),
          const SizedBox(height: 16),
          if (isBusy) const LinearProgressIndicator(),
          if (latest != null)
            Text(describe(latest!),
                textAlign: TextAlign.center,
                style: Theme.of(context).textTheme.headlineSmall),
          const Divider(height: 32),
          const Text('History (last 5)'),
          for (final item in history)
            ListTile(leading: const Icon(Icons.history), title: Text(describe(item))),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: isBusy ? null : () => check(ImageSource.camera),
        icon: const Icon(Icons.camera_alt),
        label: const Text('Check fruit'),
      ),
    );
  }
}
