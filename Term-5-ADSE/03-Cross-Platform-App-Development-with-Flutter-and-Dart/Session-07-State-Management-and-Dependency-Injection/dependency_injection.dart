// dependency_injection.dart
// Dependency injection: the page RECEIVES a quote service instead of creating it.

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

// An abstract "contract": any quote service must have getQuote().
abstract class QuoteService {
  String getQuote();
}

// Real version (imagine it calls an API later in Session 13).
class OnlineQuoteService implements QuoteService {
  @override
  String getQuote() => 'Learning never exhausts the mind.';
}

// Fake version for testing or offline demos.
class FakeQuoteService implements QuoteService {
  @override
  String getQuote() => 'This is a test quote.';
}

void main() {
  runApp(
    // Inject ONE service for the whole app. Swap to FakeQuoteService() to test.
    Provider<QuoteService>(
      create: (context) => OnlineQuoteService(),
      child: const MaterialApp(home: QuotePage()),
    ),
  );
}

class QuotePage extends StatelessWidget {
  const QuotePage({super.key});

  @override
  Widget build(BuildContext context) {
    // The page asks for "a QuoteService" — it does not care which one.
    final QuoteService service = context.read<QuoteService>();

    return Scaffold(
      appBar: AppBar(title: const Text('Dependency Injection')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          child: Text(service.getQuote(), style: const TextStyle(fontSize: 22)),
        ),
      ),
    );
  }
}
