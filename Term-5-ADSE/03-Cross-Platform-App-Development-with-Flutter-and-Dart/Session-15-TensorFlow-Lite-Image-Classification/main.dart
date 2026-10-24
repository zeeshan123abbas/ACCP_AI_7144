// Session 15 - Example 2: Pick a photo and show what the model sees
// lib/ needs: main.dart + classifier.dart. Assets: see pubspec_snippet.yaml
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'classifier.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: ClassifyPage()));
}

class ClassifyPage extends StatefulWidget {
  const ClassifyPage({super.key});

  @override
  State<ClassifyPage> createState() => _ClassifyPageState();
}

class _ClassifyPageState extends State<ClassifyPage> {
  final classifier = Classifier();
  final picker = ImagePicker();

  bool modelReady = false;
  File? selectedPhoto;
  List<MapEntry<String, double>> results = [];

  @override
  void initState() {
    super.initState();
    // Load the model once when the screen opens.
    classifier.load().then((_) {
      if (mounted) setState(() => modelReady = true);
    });
  }

  @override
  void dispose() {
    classifier.close(); // free native memory
    super.dispose();
  }

  Future<void> pickAndClassify(ImageSource source) async {
    final picked = await picker.pickImage(source: source);
    if (picked == null) return; // user cancelled

    final photo = File(picked.path);
    final top3 = await classifier.classify(photo);
    setState(() {
      selectedPhoto = photo;
      results = top3;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('What is this? (TFLite)')),
      body: !modelReady
          ? const Center(child: CircularProgressIndicator())
          : ListView(
              padding: const EdgeInsets.all(16),
              children: [
                if (selectedPhoto != null)
                  Image.file(selectedPhoto!, height: 250, fit: BoxFit.cover)
                else
                  const SizedBox(height: 250, child: Center(child: Text('Pick a photo'))),
                const SizedBox(height: 16),
                // One row per result: label + confidence bar.
                for (final result in results)
                  ListTile(
                    title: Text(result.key),
                    subtitle: LinearProgressIndicator(value: result.value),
                    trailing: Text('${(result.value * 100).toStringAsFixed(1)}%'),
                  ),
              ],
            ),
      bottomNavigationBar: Padding(
        padding: const EdgeInsets.all(16),
        child: Row(
          children: [
            Expanded(
              child: FilledButton.icon(
                onPressed: modelReady ? () => pickAndClassify(ImageSource.camera) : null,
                icon: const Icon(Icons.camera_alt),
                label: const Text('Camera'),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: OutlinedButton.icon(
                onPressed: modelReady ? () => pickAndClassify(ImageSource.gallery) : null,
                icon: const Icon(Icons.photo),
                label: const Text('Gallery'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
