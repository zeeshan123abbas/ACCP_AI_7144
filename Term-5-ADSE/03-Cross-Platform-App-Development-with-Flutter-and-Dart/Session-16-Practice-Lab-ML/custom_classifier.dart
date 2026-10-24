// Session 16 - Step 1: Classifier for YOUR Teachable Machine model
// Floating-point model: input [1, 224, 224, 3] float32 in range -1..1, output [1, N] float32.
import 'dart:io';
import 'package:flutter/services.dart';
import 'package:image/image.dart' as img;
import 'package:tflite_flutter/tflite_flutter.dart';

// A small class to hold one prediction.
class Prediction {
  final String label;
  final double confidence; // 0.0 - 1.0
  Prediction(this.label, this.confidence);
}

class CustomClassifier {
  late Interpreter interpreter;
  late List<String> labels;

  Future<void> load() async {
    interpreter = await Interpreter.fromAsset('assets/model_unquant.tflite');

    // Teachable Machine labels look like "0 Apple". Keep only the name part.
    final text = await rootBundle.loadString('assets/labels.txt');
    labels = text
        .split('\n')
        .map((line) => line.trim())
        .where((line) => line.isNotEmpty)
        .map((line) => line.substring(line.indexOf(' ') + 1)) // "0 Apple" -> "Apple"
        .toList();
  }

  // Convert one colour value 0..255 into the range -1..1 the model was trained on.
  double normalize(num value) => (value - 127.5) / 127.5;

  Future<Prediction> classify(File photo) async {
    // 1. Decode and resize.
    final image = img.decodeImage(await photo.readAsBytes())!;
    final resized = img.copyResize(image, width: 224, height: 224);

    // 2. Build a float input tensor [1][224][224][3].
    final input = [
      List.generate(224, (y) => List.generate(224, (x) {
            final p = resized.getPixel(x, y);
            return [normalize(p.r), normalize(p.g), normalize(p.b)];
          })),
    ];

    // 3. One output score per label (scores already add up to 1.0).
    final output = [List<double>.filled(labels.length, 0)];
    interpreter.run(input, output);

    // 4. Find the index of the biggest score.
    final scores = output[0];
    var bestIndex = 0;
    for (var i = 1; i < scores.length; i++) {
      if (scores[i] > scores[bestIndex]) bestIndex = i;
    }
    return Prediction(labels[bestIndex], scores[bestIndex]);
  }

  void close() => interpreter.close();
}
