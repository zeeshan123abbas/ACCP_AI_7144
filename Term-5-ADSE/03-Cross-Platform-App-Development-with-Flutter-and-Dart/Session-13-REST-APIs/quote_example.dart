// Session 13 - Example 1: The smallest possible GET request
// Shows one random quote from https://dummyjson.com/quotes/random
import 'dart:convert';                     // jsonDecode
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;   // the http package

void main() {
  runApp(const MaterialApp(debugShowCheckedModeBanner: false, home: QuotePage()));
}

// Step 1: a function that calls the API and returns the quote text.
Future<String> fetchRandomQuote() async {
  final url = Uri.parse('https://dummyjson.com/quotes/random');
  final response = await http.get(url);               // send the request

  if (response.statusCode == 200) {                    // 200 = OK
    final data = jsonDecode(response.body);            // text -> Map
    return '"${data['quote']}"\n\n- ${data['author']}';
  } else {
    throw Exception('Server error: ${response.statusCode}');
  }
}

class QuotePage extends StatefulWidget {
  const QuotePage({super.key});

  @override
  State<QuotePage> createState() => _QuotePageState();
}

class _QuotePageState extends State<QuotePage> {
  // Step 2: keep the Future in a variable so it runs only when we ask.
  late Future<String> quoteFuture = fetchRandomQuote();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Random Quote')),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(24),
          // Step 3: FutureBuilder shows loading, error or data.
          child: FutureBuilder<String>(
            future: quoteFuture,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.waiting) {
                return const CircularProgressIndicator();
              }
              if (snapshot.hasError) {
                return Text('Oops: ${snapshot.error}');
              }
              return Text(snapshot.data!, textAlign: TextAlign.center,
                  style: const TextStyle(fontSize: 20));
            },
          ),
        ),
      ),
      // Step 4: get a new quote by creating a new Future.
      floatingActionButton: FloatingActionButton(
        onPressed: () => setState(() => quoteFuture = fetchRandomQuote()),
        child: const Icon(Icons.refresh),
      ),
    );
  }
}
