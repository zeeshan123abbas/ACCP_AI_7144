// Session 17 - Example 1: Read text from a photo with ML Kit (OCR)
// Runs on Android and iOS only (ML Kit is a mobile SDK).
import 'package:flutter/material.dart';
import 'package:google_mlkit_text_recognition/google_mlkit_text_recognition.dart';
import 'package:image_picker/image_picker.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: TextScannerPage()));
}

class TextScannerPage extends StatefulWidget {
  const TextScannerPage({super.key});

  @override
  State<TextScannerPage> createState() => _TextScannerPageState();
}

class _TextScannerPageState extends State<TextScannerPage> {
  // Step 1: create the recognizer once (Latin script = English, Urdu-roman, etc.).
  final textRecognizer = TextRecognizer(script: TextRecognitionScript.latin);
  String scannedText = 'Take a photo of a page, a sign or a business card.';

  @override
  void dispose() {
    textRecognizer.close(); // release native resources
    super.dispose();
  }

  Future<void> scan() async {
    // Step 2: get a photo from the camera.
    final photo = await ImagePicker().pickImage(source: ImageSource.camera);
    if (photo == null) return;

    // Step 3: wrap the file as an InputImage and process it.
    final inputImage = InputImage.fromFilePath(photo.path);
    final result = await textRecognizer.processImage(inputImage);

    // Step 4: result.text is all the text; result.blocks gives paragraphs.
    if (!mounted) return;
    setState(() {
      scannedText = result.text.isEmpty ? 'No text found.' : result.text;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Text Scanner (ML Kit)')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        // SelectableText lets the user copy the result.
        child: SelectableText(scannedText, style: const TextStyle(fontSize: 18)),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: scan,
        child: const Icon(Icons.document_scanner),
      ),
    );
  }
}
