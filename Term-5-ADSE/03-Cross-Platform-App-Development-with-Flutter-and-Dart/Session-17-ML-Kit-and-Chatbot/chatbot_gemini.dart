// Session 17 - Example 4: The same chat idea, but answers come from Gemini
// Setup: Firebase project + `flutterfire configure` + enable "AI Logic" in the console.
import 'package:firebase_ai/firebase_ai.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'firebase_options.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: GeminiChatPage()));
}

class GeminiChatPage extends StatefulWidget {
  const GeminiChatPage({super.key});

  @override
  State<GeminiChatPage> createState() => _GeminiChatPageState();
}

class _GeminiChatPageState extends State<GeminiChatPage> {
  // Step 1: choose a model. Model names change; check the Firebase AI Logic docs.
  final model = FirebaseAI.googleAI().generativeModel(
    model: 'gemini-3.5-flash-lite',
    // A system instruction gives the bot its role and rules.
    systemInstruction: Content.system(
      'You are a friendly tutor for beginner Flutter students. Answer in short, simple English.',
    ),
  );

  // Step 2: a chat session remembers earlier messages automatically.
  late final ChatSession chat = model.startChat();

  final inputController = TextEditingController();
  final List<String> lines = [];   // "You: ..." and "Bot: ..."
  bool isWaiting = false;

  Future<void> send() async {
    final question = inputController.text.trim();
    if (question.isEmpty || isWaiting) return;
    inputController.clear();
    setState(() {
      lines.add('You: $question');
      isWaiting = true;
    });

    try {
      // Step 3: send the message and wait for the reply.
      final response = await chat.sendMessage(Content.text(question));
      lines.add('Bot: ${response.text ?? '(no answer)'}');
    } catch (error) {
      lines.add('Bot: Sorry, something went wrong ($error).');
    }
    if (mounted) setState(() => isWaiting = false);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Flutter Tutor (Gemini)')),
      body: Column(
        children: [
          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(12),
              children: [
                for (final line in lines)
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 6),
                    child: Text(line),
                  ),
              ],
            ),
          ),
          if (isWaiting) const LinearProgressIndicator(),
          SafeArea(
            child: Row(
              children: [
                Expanded(
                  child: Padding(
                    padding: const EdgeInsets.all(8),
                    child: TextField(
                      controller: inputController,
                      onSubmitted: (_) => send(),
                      decoration: const InputDecoration(hintText: 'Ask about Flutter...'),
                    ),
                  ),
                ),
                IconButton(icon: const Icon(Icons.send), onPressed: send),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
