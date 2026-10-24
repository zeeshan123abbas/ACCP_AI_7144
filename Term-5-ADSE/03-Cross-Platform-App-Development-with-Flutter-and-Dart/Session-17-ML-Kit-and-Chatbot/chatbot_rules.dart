// Session 17 - Example 3: A simple rule-based chatbot (no AI, no internet)
// Good for learning the chat UI. Runs on every platform, including web.
import 'package:flutter/material.dart';

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: ChatPage()));
}

// One chat message.
class Message {
  final String text;
  final bool isUser; // true = user, false = bot
  Message(this.text, this.isUser);
}

// The "brain": look for keywords and return an answer.
String getBotReply(String userText) {
  final text = userText.toLowerCase();
  if (text.contains('hello') || text.contains('salam')) {
    return 'Wa alaikum assalam! Ask me about timings, fees or courses.';
  }
  if (text.contains('timing') || text.contains('time')) {
    return 'Classes run Monday to Saturday, 9 am to 9 pm.';
  }
  if (text.contains('course')) {
    return 'We teach Flutter, Python, AI and web development.';
  }
  if (text.contains('fee')) {
    return 'Please visit the front desk for the latest fee details.';
  }
  return "Sorry, I don't understand yet. Try 'timing' or 'course'.";
}

class ChatPage extends StatefulWidget {
  const ChatPage({super.key});

  @override
  State<ChatPage> createState() => _ChatPageState();
}

class _ChatPageState extends State<ChatPage> {
  final inputController = TextEditingController();
  final List<Message> messages = [Message('Hi! I am CampusBot. How can I help?', false)];

  void send() {
    final text = inputController.text.trim();
    if (text.isEmpty) return;
    setState(() {
      messages.add(Message(text, true));             // user's message
      messages.add(Message(getBotReply(text), false)); // bot's answer
    });
    inputController.clear();
  }

  @override
  Widget build(BuildContext context) {
    final colors = Theme.of(context).colorScheme;

    return Scaffold(
      appBar: AppBar(title: const Text('CampusBot')),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(12),
              itemCount: messages.length,
              itemBuilder: (context, index) {
                final message = messages[index];
                // User bubbles on the right, bot bubbles on the left.
                return Align(
                  alignment: message.isUser ? Alignment.centerRight : Alignment.centerLeft,
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 4),
                    padding: const EdgeInsets.all(12),
                    constraints: const BoxConstraints(maxWidth: 300),
                    decoration: BoxDecoration(
                      color: message.isUser ? colors.primaryContainer : colors.surfaceContainerHighest,
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Text(message.text),
                  ),
                );
              },
            ),
          ),
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.all(8),
              child: Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: inputController,
                      onSubmitted: (_) => send(),
                      decoration: const InputDecoration(hintText: 'Type a message...'),
                    ),
                  ),
                  IconButton(icon: const Icon(Icons.send), onPressed: send),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
