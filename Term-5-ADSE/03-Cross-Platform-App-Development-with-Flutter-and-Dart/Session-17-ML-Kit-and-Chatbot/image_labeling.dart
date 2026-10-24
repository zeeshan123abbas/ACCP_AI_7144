// Session 17 - Example 2: Describe a photo with ML Kit Image Labeling
// Uses ML Kit's built-in model (400+ everyday labels), no model file needed.
import 'package:flutter/material.dart';
import 'package:google_mlkit_image_labeling/google_mlkit_image_labeling.dart';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: LabelPage()));
}

class LabelPage extends StatefulWidget {
  const LabelPage({super.key});

  @override
  State<LabelPage> createState() => _LabelPageState();
}

class _LabelPageState extends State<LabelPage> {
  // Only return labels with at least 60% confidence.
  final labeler = ImageLabeler(options: ImageLabelerOptions(confidenceThreshold: 0.6));
  List<ImageLabel> labels = [];

  @override
  void dispose() {
    labeler.close();
    super.dispose();
  }

  Future<void> pickAndLabel() async {
    final photo = await ImagePicker().pickImage(source: ImageSource.gallery);
    if (photo == null) return;

    final found = await labeler.processImage(InputImage.fromFilePath(photo.path));
    if (!mounted) return;
    setState(() => labels = found);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Image Labels (ML Kit)')),
      body: labels.isEmpty
          ? const Center(child: Text('Pick a photo to see what is in it.'))
          : ListView(
              children: [
                for (final label in labels)
                  ListTile(
                    leading: const Icon(Icons.label),
                    title: Text(label.label),
                    trailing: Text('${(label.confidence * 100).toStringAsFixed(0)}%'),
                  ),
              ],
            ),
      floatingActionButton: FloatingActionButton(
        onPressed: pickAndLabel,
        child: const Icon(Icons.photo_library),
      ),
    );
  }
}
