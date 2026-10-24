// Session 15 - Example 1: A simple image classifier with TensorFlow Lite
// Model: MobileNet v1 (quantized). Input [1, 224, 224, 3] uint8, output [1, 1001] uint8.
import 'dart:io';
import 'package:flutter/services.dart';        // rootBundle (read asset files)
import 'package:image/image.dart' as img;      // decode + resize
import 'package:tflite_flutter/tflite_flutter.dart';

class Classifier {
  late Interpreter interpreter;
  late List<String> labels;

  // Step 1: load the model and the labels from assets (call once).
  Future<void> load() async {
    interpreter = await Interpreter.fromAsset('assets/models/mobilenet_quant.tflite');
    final labelText = await rootBundle.loadString('assets/models/labels.txt');
    labels = labelText
        .split('\n')
        .map((line) => line.trim())
        .where((line) => line.isNotEmpty) // skip a blank last line
        .toList();
  }

  // Step 2: classify one photo and return the top 3 (label, confidence).
  Future<List<MapEntry<String, double>>> classify(File photo) async {
    // 2a. Read the file and decode it into pixels.
    final bytes = await photo.readAsBytes();
    final original = img.decodeImage(bytes)!;

    // 2b. Resize to the size the model expects: 224 x 224.
    final resized = img.copyResize(original, width: 224, height: 224);

    // 2c. Build the input tensor: [1][224][224][3] numbers 0-255 (R, G, B).
    final input = [
      List.generate(224, (y) {
        return List.generate(224, (x) {
          final pixel = resized.getPixel(x, y);
          return [pixel.r.toInt(), pixel.g.toInt(), pixel.b.toInt()];
        });
      }),
    ];

    // 2d. Prepare an empty output: one score (0-255) for each of 1001 labels.
    //     We ask the model how many scores it returns (1001 for MobileNet).
    final scoreCount = interpreter.getOutputTensor(0).shape[1];
    final output = [List<int>.filled(scoreCount, 0)];

    // 2e. Run the model.
    interpreter.run(input, output);

    // 2f. Turn scores into (label, confidence 0.0-1.0) pairs and sort them.
    final results = <MapEntry<String, double>>[];
    for (var i = 0; i < scoreCount && i < labels.length; i++) {
      results.add(MapEntry(labels[i], output[0][i] / 255.0));
    }
    results.sort((a, b) => b.value.compareTo(a.value)); // highest first
    return results.take(3).toList();
  }

  void close() => interpreter.close();
}
