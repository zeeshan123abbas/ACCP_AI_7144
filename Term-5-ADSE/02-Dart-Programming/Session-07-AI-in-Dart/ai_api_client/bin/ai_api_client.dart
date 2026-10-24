// bin/ai_api_client.dart
// Ask an AI model (Google Gemini) a question from the command line.
//
// 1. Get a free API key from https://aistudio.google.com/apikey
// 2. Save it in an environment variable (never write keys in code!):
//      Windows (PowerShell):  $env:GEMINI_API_KEY="your-key"
//      macOS / Linux:         export GEMINI_API_KEY="your-key"
// 3. Run:  dart pub get
//          dart run ai_api_client "Explain null safety in one line"

import 'dart:convert'; // jsonEncode / jsonDecode
import 'dart:io'; // Platform.environment and exit()

import 'package:http/http.dart' as http;

// The model name can change over time. Check the list of models at
// https://ai.google.dev/gemini-api/docs/models and update if needed.
const String defaultModel = 'gemini-2.5-flash';

Future<void> main(List<String> arguments) async {
  // Step 1: read the API key from the environment.
  String? apiKey = Platform.environment['GEMINI_API_KEY'];
  if (apiKey == null || apiKey.isEmpty) {
    print('Please set the GEMINI_API_KEY environment variable first.');
    exit(1);
  }

  // Step 2: use the question from the command line, or a default one.
  String question = arguments.isNotEmpty
      ? arguments.join(' ')
      : 'Give me 3 tips for learning Dart as a beginner.';

  print('You asked: $question');
  print('Thinking...\n');

  try {
    String answer = await askGemini(question, apiKey);
    print('AI says:\n$answer');
  } catch (e) {
    print('Something went wrong: $e');
  }
}

// Sends the question to Gemini and returns the text answer.
Future<String> askGemini(String question, String apiKey) async {
  String model = Platform.environment['GEMINI_MODEL'] ?? defaultModel;

  // Step 3: build the URL and the JSON body the API expects.
  Uri url = Uri.parse(
    'https://generativelanguage.googleapis.com/v1beta/models/$model:generateContent',
  );
  Map<String, dynamic> body = {
    'contents': [
      {
        'parts': [
          {'text': question},
        ],
      },
    ],
  };

  // Step 4: send a POST request. The key goes in a header, not the URL.
  http.Response response = await http.post(
    url,
    headers: {
      'Content-Type': 'application/json',
      'x-goog-api-key': apiKey,
    },
    body: jsonEncode(body),
  );

  // Step 5: check the status code. 200 means OK.
  if (response.statusCode != 200) {
    throw Exception('HTTP ${response.statusCode}: ${response.body}');
  }

  // Step 6: decode the JSON and dig out the answer text.
  Map<String, dynamic> data = jsonDecode(response.body);
  String text = data['candidates'][0]['content']['parts'][0]['text'];
  return text;
}
